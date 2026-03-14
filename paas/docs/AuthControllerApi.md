# AuthControllerApi

`ThingsboardClient` methods:

```python
JwtPair client.activate_user(activate_user_request: ActivateUserRequest, send_activation_mail: Optional[bool] = None)  # Activate User
JwtPair client.change_password(change_password_request: ChangePasswordRequest)  # Change password for current User (changePassword)
object client.check_activate_token(activate_token: str)  # Check Activate User Token (checkActivateToken)
object client.check_reset_token(reset_token: str)  # Check password reset token (checkResetToken)
User client.get_user()  # Get current User (getUser)
UserPasswordPolicy client.get_user_password_policy()  # Get the current User password policy (getUserPasswordPolicy)
None client.logout()  # Logout (logout)
None client.request_reset_password_by_email(reset_password_email_request: ResetPasswordEmailRequest)  # Request reset password email (requestResetPasswordByEmail)
None client.reset_password(reset_password_request: ResetPasswordRequest)  # Reset password (resetPassword)
```


## activate_user

```python
JwtPair client.activate_user(activate_user_request: ActivateUserRequest, send_activation_mail: Optional[bool] = None)
```

**POST** `/api/noauth/activate`

Activate User

Checks the activation token and updates corresponding user password in the database. Now the user may start using his password to login. The response already contains the [JWT](https://jwt.io) activation and refresh tokens, to simplify the user activation flow and avoid asking user to input password again after activation. If token is valid, returns the object that contains [JWT](https://jwt.io/) access and refresh tokens. If token is not valid, returns '400 Bad Request'.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **activate_user_request** | **ActivateUserRequest** |  | |
| **send_activation_mail** | **bool** |  | [optional] [default to True] |

### Return type

**JwtPair**


## change_password

```python
JwtPair client.change_password(change_password_request: ChangePasswordRequest)
```

**POST** `/api/auth/changePassword`

Change password for current User (changePassword)

Change the password for the User which credentials are used to perform this REST API call. Be aware that previously generated [JWT](https://jwt.io/) tokens will be still valid until they expire.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **change_password_request** | **ChangePasswordRequest** |  | |

### Return type

**JwtPair**


## check_activate_token

```python
object client.check_activate_token(activate_token: str)
```

**GET** `/api/noauth/activate`

Check Activate User Token (checkActivateToken)

Checks the activation token and forwards user to 'Create Password' page. If token is valid, returns '303 See Other' (redirect) response code with the correct address of 'Create Password' page and same 'activateToken' specified in the URL parameters. If token is not valid, returns '409 Conflict'. If token is expired, redirects to error page.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **activate_token** | **str** | The activate token string. | |

### Return type

**object**


## check_reset_token

```python
object client.check_reset_token(reset_token: str)
```

**GET** `/api/noauth/resetPassword`

Check password reset token (checkResetToken)

Checks the password reset token and forwards user to 'Reset Password' page. If token is valid, returns '303 See Other' (redirect) response code with the correct address of 'Reset Password' page and same 'resetToken' specified in the URL parameters. If token is not valid, returns '409 Conflict'. If token is expired, redirects to error page.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **reset_token** | **str** | The reset token string. | |

### Return type

**object**


## get_user

```python
User client.get_user()
```

**GET** `/api/auth/user`

Get current User (getUser)

Get the information about the User which credentials are used to perform this REST API call.

### Return type

**User**


## get_user_password_policy

```python
UserPasswordPolicy client.get_user_password_policy()
```

**GET** `/api/noauth/userPasswordPolicy`

Get the current User password policy (getUserPasswordPolicy)

API call to get the password policy for the password validation form(s).

### Return type

**UserPasswordPolicy**


## logout

```python
None client.logout()
```

**POST** `/api/auth/logout`

Logout (logout)

Special API call to record the 'logout' of the user to the Audit Logs. Since platform uses [JWT](https://jwt.io/), the actual logout is the procedure of clearing the [JWT](https://jwt.io/) token on the client side. 

### Return type

None (empty response body)


## request_reset_password_by_email

```python
None client.request_reset_password_by_email(reset_password_email_request: ResetPasswordEmailRequest)
```

**POST** `/api/noauth/resetPasswordByEmail`

Request reset password email (requestResetPasswordByEmail)

Request to send the reset password email if the user with specified email address is present in the database. Always return '200 OK' status for security purposes.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **reset_password_email_request** | **ResetPasswordEmailRequest** |  | |

### Return type

None (empty response body)


## reset_password

```python
None client.reset_password(reset_password_request: ResetPasswordRequest)
```

**POST** `/api/noauth/resetPassword`

Reset password (resetPassword)

Checks the password reset token and updates the password. If token is not valid, returns '400 Bad Request'.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **reset_password_request** | **ResetPasswordRequest** |  | |

### Return type

None (empty response body)

