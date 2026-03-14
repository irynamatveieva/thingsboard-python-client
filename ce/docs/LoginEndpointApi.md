# LoginEndpointApi

`ThingsboardClient` methods:

```python
LoginResponse client.login(login_request: Optional[LoginRequest] = None)  # Login method to get user JWT token data
LoginResponse client.refresh_token(refresh_token_request: Optional[RefreshTokenRequest] = None)  # Refresh user JWT token data
```


## login

```python
LoginResponse client.login(login_request: Optional[LoginRequest] = None)
```

**POST** `/api/auth/login`

Login method to get user JWT token data

Login method used to authenticate user and get JWT token data.  Value of the response **token** field can be used as **X-Authorization** header value:  `X-Authorization: Bearer $JWT_TOKEN_VALUE`.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **login_request** | **LoginRequest** | Login request | [optional] |

### Return type

**LoginResponse**


## refresh_token

```python
LoginResponse client.refresh_token(refresh_token_request: Optional[RefreshTokenRequest] = None)
```

**POST** `/api/auth/token`

Refresh user JWT token data

Method to refresh JWT token. Provide a valid refresh token to get a new JWT token.  The response contains a new token that can be used for authorization.  `X-Authorization: Bearer $JWT_TOKEN_VALUE`


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **refresh_token_request** | **RefreshTokenRequest** | Refresh token request | [optional] |

### Return type

**LoginResponse**

