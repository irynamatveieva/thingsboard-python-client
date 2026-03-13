#
# Copyright 2026 ThingsBoard, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
client.py — ThingsboardClient: the public-facing entry point for ThingsBoard Python clients.

This file lives in common/ and is copied verbatim into each edition package directory
by generate-client.sh. Use only relative imports and stdlib; no edition-specific imports.

Stub client for Phase 4. API method delegation added in Phase 5.
ThingsboardClient wires:
  - _AuthManager for JWT/API key authentication and automatic token refresh
  - _RetryingRESTClient for transparent HTTP 429 retry with exponential backoff
"""
from .api_client import ApiClient
from .configuration import Configuration
from .models.login_request import LoginRequest
from ._auth import _AuthManager
from ._retry import _RetryingRESTClient


class ThingsboardClient:
    """User-facing ThingsBoard client.

    Wraps the generated per-controller APIs with authentication management and
    transparent 429 retry. Supports three authentication modes:

    1. Username + password (JWT):
         ThingsboardClient(url, username, password)
         Eagerly authenticates via /api/auth/login on construction.

    2. API key:
         ThingsboardClient(url, api_key="your-api-key")
         Sets X-Authorization: ApiKey <key> header; no login call made.

    3. Pre-existing token:
         ThingsboardClient(url, token="jwt", refresh_token="jwt")
         Injects an externally obtained JWT; no login call made.

    Context manager usage:
         with ThingsboardClient(url, api_key="key") as client:
             devices = client.get_tenant_devices(page_size=10, page=0)
    """

    def __init__(
        self,
        url: str,
        username: str = None,
        password: str = None,
        api_key: str = None,
        token: str = None,
        refresh_token: str = None,
        max_retries: int = 3,
        initial_retry_delay_ms: int = 1_000,
        max_retry_delay_ms: int = 30_000,
        retry_on_rate_limit: bool = True,
    ):
        """Construct ThingsboardClient and authenticate.

        Args:
            url: Base URL of the ThingsBoard server (e.g. "http://tb:9090").
            username: Username for JWT authentication.
            password: Password for JWT authentication.
            api_key: API key for X-Authorization: ApiKey authentication.
            token: Pre-existing JWT access token.
            refresh_token: Pre-existing JWT refresh token (used with token=).
            max_retries: Maximum retry attempts on HTTP 429 (default 3).
            initial_retry_delay_ms: Base backoff delay in milliseconds (default 1000).
            max_retry_delay_ms: Maximum backoff cap in milliseconds (default 30000).
            retry_on_rate_limit: If True (default), wraps rest_client with
                _RetryingRESTClient. If False, uses plain RESTClientObject.
        """
        configuration = Configuration(host=url)

        # Determine auth type
        auth_type = "api_key" if api_key is not None else "jwt"
        auth_manager = _AuthManager(url, auth_type, api_key)

        # Install the refresh hook so the hook fires before every API request
        configuration.refresh_api_key_hook = auth_manager.hook

        # API key auth: set header at construction time
        if api_key is not None:
            configuration.api_key["ApiKeyForm"] = api_key
            configuration.api_key_prefix["ApiKeyForm"] = "ApiKey"

        # Build the ApiClient
        api_client = ApiClient(configuration=configuration)

        # Optionally replace the default RESTClientObject with the retrying version
        if retry_on_rate_limit:
            api_client.rest_client = _RetryingRESTClient(
                configuration,
                max_retries,
                initial_retry_delay_ms,
                max_retry_delay_ms,
            )

        self.api_client = api_client
        self._auth_manager = auth_manager

        # JWT eager login
        if username is not None:
            from .api.login_endpoint_api import LoginEndpointApi
            login_api = LoginEndpointApi(api_client)
            response = login_api.login(LoginRequest(username=username, password=password))
            auth_manager.on_login(username, password, response.token, response.refresh_token)

        # Pre-existing token
        if token is not None:
            auth_manager.set_external_token(token, refresh_token)
            configuration.api_key["ApiKeyForm"] = token
            configuration.api_key_prefix["ApiKeyForm"] = "Bearer"

    # ------------------------------------------------------------------
    # Token accessors
    # ------------------------------------------------------------------

    def get_token(self) -> "str | None":
        """Return the current access token (JWT or API key), or None."""
        return self._auth_manager.get_token()

    def get_refresh_token(self) -> "str | None":
        """Return the current refresh token, or None if not available."""
        return self._auth_manager.get_refresh_token()

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def close(self) -> None:
        """Release connection pool resources.

        Calls pool_manager.clear() on the underlying urllib3 pool to cleanly
        close all open connections. Automatically called by __exit__.
        """
        self.api_client.rest_client.pool_manager.clear()

    def __enter__(self) -> "ThingsboardClient":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.close()
        return False
