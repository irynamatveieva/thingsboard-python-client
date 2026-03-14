# TwoFactorAuthControllerApi

`ThingsboardClient` methods:

```python
JwtPair client.authenticate_by_two_fa_configuration_token()  # Get regular token pair after successfully configuring 2FA
JwtPair client.check_two_fa_verification_code(provider_type: TwoFaProviderType, verification_code: str)  # Check 2FA verification code (checkTwoFaVerificationCode)
List[TwoFaProviderInfo] client.get_available_two_fa_provider_infos()  # Get available 2FA providers (getAvailableTwoFaProviderInfos)
None client.request_two_fa_verification_code(provider_type: TwoFaProviderType)  # Request 2FA verification code (requestTwoFaVerificationCode)
```


## authenticate_by_two_fa_configuration_token

```python
JwtPair client.authenticate_by_two_fa_configuration_token()
```

**POST** `/api/auth/2fa/login`

Get regular token pair after successfully configuring 2FA

Checks 2FA is configured, returning token pair on success.

### Return type

**JwtPair**


## check_two_fa_verification_code

```python
JwtPair client.check_two_fa_verification_code(provider_type: TwoFaProviderType, verification_code: str)
```

**POST** `/api/auth/2fa/verification/check`

Check 2FA verification code (checkTwoFaVerificationCode)

Checks 2FA verification code, and if it is correct the method returns a regular access and refresh token pair.  The API method is rate limited (using rate limit config from TwoFactorAuthSettings), and also will block a user after X unsuccessful verification attempts if such behavior is configured (in TwoFactorAuthSettings).  Will return a Bad Request error if provider is not configured for usage, and Too Many Requests error if rate limits are exceeded.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **provider_type** | **TwoFaProviderType** |  | [enum: TOTP, SMS, EMAIL, BACKUP_CODE] |
| **verification_code** | **str** |  | |

### Return type

**JwtPair**


## get_available_two_fa_provider_infos

```python
List[TwoFaProviderInfo] client.get_available_two_fa_provider_infos()
```

**GET** `/api/auth/2fa/providers`

Get available 2FA providers (getAvailableTwoFaProviderInfos)

Get the list of 2FA provider infos available for user to use. Example: ``` [   {     \"type\": \"EMAIL\",     \"default\": true,     \"contact\": \"ab*****ko@gmail.com\"   },   {     \"type\": \"TOTP\",     \"default\": false,     \"contact\": null   },   {     \"type\": \"SMS\",     \"default\": false,     \"contact\": \"+38********12\"   } ] ```

### Return type

**List[TwoFaProviderInfo]**


## request_two_fa_verification_code

```python
None client.request_two_fa_verification_code(provider_type: TwoFaProviderType)
```

**POST** `/api/auth/2fa/verification/send`

Request 2FA verification code (requestTwoFaVerificationCode)

Request 2FA verification code.  To make a request to this endpoint, you need an access token with the scope of PRE_VERIFICATION_TOKEN, which is issued on username/password auth if 2FA is enabled.  The API method is rate limited (using rate limit config from TwoFactorAuthSettings). Will return a Bad Request error if provider is not configured for usage, and Too Many Requests error if rate limits are exceeded.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **provider_type** | **TwoFaProviderType** |  | [enum: TOTP, SMS, EMAIL, BACKUP_CODE] |

### Return type

None (empty response body)

