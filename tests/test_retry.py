"""
Unit tests for _RetryingRESTClient (common/_retry.py / tb_ce_client/_retry.py).

Covers RESL-01 through RESL-04:
  RESL-01: Retry on HTTP 429 up to max_retries times
  RESL-02: Exponential backoff with +/-20% jitter
  RESL-03: Retry-After header respected (integer seconds), capped at max_delay
  RESL-04: After exhausting retries, last 429 response returned (no exception)
"""
import time
import unittest
from unittest.mock import MagicMock, patch, call

from tb_ce_client._retry import _RetryingRESTClient


def _make_response(status, headers=None):
    """Create a mock RESTResponse-like object."""
    resp = MagicMock()
    resp.status = status
    resp.headers = headers or {}
    resp.read.return_value = b""
    return resp


def _make_client(max_retries=3, initial_delay_ms=1000, max_delay_ms=30000):
    """Create a _RetryingRESTClient with a mocked configuration."""
    config = MagicMock()
    config.verify_ssl = False
    config.ssl_ca_cert = None
    config.cert_file = None
    config.key_file = None
    config.ca_cert_data = None
    config.assert_hostname = None
    config.retries = None
    config.tls_server_name = None
    config.socket_options = None
    config.connection_pool_maxsize = None
    config.proxy = None
    return _RetryingRESTClient(config, max_retries, initial_delay_ms, max_delay_ms)


class TestNoRetryOnSuccess(unittest.TestCase):
    """RESL-01: Non-429 response returned immediately without retry."""

    @patch("time.sleep")
    def test_no_retry_on_success(self, mock_sleep):
        client = _make_client()
        ok_response = _make_response(200)

        with patch.object(
            type(client).__bases__[0],  # RESTClientObject
            "request",
            return_value=ok_response,
        ) as mock_req:
            result = client.request("GET", "http://example.com/api")

        self.assertEqual(result.status, 200)
        self.assertEqual(mock_req.call_count, 1)
        mock_sleep.assert_not_called()


class TestRetryOn429(unittest.TestCase):
    """RESL-01: 429 response triggers retry loop."""

    @patch("time.sleep")
    def test_retry_on_429(self, mock_sleep):
        """429, 429, 200 sequence: final response is 200, 3 requests, 2 sleeps."""
        client = _make_client(max_retries=3)
        resp_429a = _make_response(429)
        resp_429b = _make_response(429)
        resp_200 = _make_response(200)

        with patch.object(
            type(client).__bases__[0],
            "request",
            side_effect=[resp_429a, resp_429b, resp_200],
        ) as mock_req:
            result = client.request("GET", "http://example.com/api")

        self.assertEqual(result.status, 200)
        self.assertEqual(mock_req.call_count, 3)
        self.assertEqual(mock_sleep.call_count, 2)


class TestExponentialBackoffFormula(unittest.TestCase):
    """RESL-02: Exponential backoff formula: initial * 2^(attempt-1), capped at max."""

    def test_exponential_backoff_formula(self):
        """Attempts 1-4 should yield ~1000, ~2000, ~4000, ~8000 (within 20% jitter)."""
        client = _make_client(max_retries=3, initial_delay_ms=1000, max_delay_ms=30000)
        response = _make_response(429)

        expected_bases = [1000, 2000, 4000, 8000]
        for attempt, base in enumerate(expected_bases, start=1):
            delay_ms = client._compute_delay(response, attempt)
            low = base * 0.8
            high = base * 1.2
            self.assertGreaterEqual(
                delay_ms, low,
                f"attempt={attempt}: delay {delay_ms} < lower bound {low}"
            )
            self.assertLessEqual(
                delay_ms, high,
                f"attempt={attempt}: delay {delay_ms} > upper bound {high}"
            )


class TestJitterBounds(unittest.TestCase):
    """RESL-02: +/-20% jitter is always within [base*0.8, base*1.2]."""

    def test_jitter_bounds(self):
        """100 samples must all land in the 20% jitter band."""
        client = _make_client(initial_delay_ms=1000, max_delay_ms=30000)
        response = _make_response(429)
        base = 1000  # attempt=1

        for _ in range(100):
            delay_ms = client._compute_delay(response, 1)
            self.assertGreaterEqual(delay_ms, base * 0.8)
            self.assertLessEqual(delay_ms, base * 1.2)


class TestRetryAfterHeaderRespected(unittest.TestCase):
    """RESL-03: Retry-After header (integer seconds) used when present."""

    def test_retry_after_header_respected(self):
        """Retry-After: 5 -> delay = 5000 ms."""
        client = _make_client(initial_delay_ms=1000, max_delay_ms=30000)
        response = _make_response(429, headers={"Retry-After": "5"})
        delay_ms = client._compute_delay(response, 1)
        self.assertEqual(delay_ms, 5000)


class TestRetryAfterCappedAtMaxDelay(unittest.TestCase):
    """RESL-03: Retry-After header capped at max_delay_ms."""

    def test_retry_after_capped_at_max_delay(self):
        """Retry-After: 999 with max_delay=30000 -> 30000 ms."""
        client = _make_client(initial_delay_ms=1000, max_delay_ms=30000)
        response = _make_response(429, headers={"Retry-After": "999"})
        delay_ms = client._compute_delay(response, 1)
        self.assertEqual(delay_ms, 30000)


class TestRetryConfigParams(unittest.TestCase):
    """RESL-01: max_retries configures retry count."""

    @patch("time.sleep")
    def test_retry_config_params(self, mock_sleep):
        """max_retries=5: 6 total requests (1 initial + 5 retries), 5 sleeps."""
        client = _make_client(max_retries=5)
        always_429 = _make_response(429)

        with patch.object(
            type(client).__bases__[0],
            "request",
            return_value=always_429,
        ) as mock_req:
            result = client.request("GET", "http://example.com/api")

        self.assertEqual(mock_req.call_count, 6)
        self.assertEqual(mock_sleep.call_count, 5)
        self.assertEqual(result.status, 429)


class TestMaxRetriesZeroMeansNoRetry(unittest.TestCase):
    """RESL-01: max_retries=0 means return 429 immediately (no retry, no sleep)."""

    @patch("time.sleep")
    def test_max_retries_zero_means_no_retry(self, mock_sleep):
        client = _make_client(max_retries=0)
        resp_429 = _make_response(429)

        with patch.object(
            type(client).__bases__[0],
            "request",
            return_value=resp_429,
        ) as mock_req:
            result = client.request("GET", "http://example.com/api")

        self.assertEqual(result.status, 429)
        self.assertEqual(mock_req.call_count, 1)
        mock_sleep.assert_not_called()


class TestExhaustedRetriesReturnsLastResponse(unittest.TestCase):
    """RESL-04: After exhausting retries, last 429 response returned (no exception)."""

    @patch("time.sleep")
    def test_exhausted_retries_returns_last_response(self, mock_sleep):
        """max_retries=2: 3 total requests, returned response has status 429."""
        client = _make_client(max_retries=2)
        always_429 = _make_response(429)

        with patch.object(
            type(client).__bases__[0],
            "request",
            return_value=always_429,
        ) as mock_req:
            result = client.request("GET", "http://example.com/api")

        self.assertEqual(result.status, 429)
        self.assertEqual(mock_req.call_count, 3)  # 1 initial + 2 retries


class TestDelayCappedAtMax(unittest.TestCase):
    """RESL-02: Delay is capped at max_delay_ms."""

    def test_delay_capped_at_max(self):
        """initial=10000, max=15000, attempt=5: result must be <= 15000."""
        client = _make_client(initial_delay_ms=10000, max_delay_ms=15000)
        response = _make_response(429)
        delay_ms = client._compute_delay(response, 5)
        self.assertLessEqual(delay_ms, 15000)


if __name__ == "__main__":
    unittest.main()
