# SignUpControllerApi

`ThingsboardClient` methods:

```python
object client.accept_privacy_policy()  # Accept privacy policy (acceptPrivacyPolicy)
object client.accept_terms_of_use()  # Accept Terms of Use (acceptTermsOfUse)
str client.activate_email(email_code: str, pkg_name: Optional[str] = None, platform: Optional[str] = None)  # Activate User using code from Email (activateEmail)
JwtPair client.activate_user_by_email_code(email_code: str, pkg_name: Optional[str] = None, platform: Optional[str] = None)  # Activate and login using code from Email (activateUserByEmailCode)
str client.mobile_login(pkg_name: str, platform: str)  # Mobile Login redirect (mobileLogin)
bool client.privacy_policy_accepted()  # Check privacy policy (privacyPolicyAccepted)
None client.resend_email_activation(email: str, pkg_name: Optional[str] = None, platform: Optional[str] = None)  # Resend Activation Email (resendEmailActivation)
SignUpResult client.sign_up(sign_up_request: SignUpRequest)  # User Sign Up (signUp)
bool client.terms_of_use_accepted()  # Check Terms Of User (termsOfUseAccepted)
```


## accept_privacy_policy

```python
object client.accept_privacy_policy()
```

**POST** `/api/signup/acceptPrivacyPolicy`

Accept privacy policy (acceptPrivacyPolicy)

Accept privacy policy by the current user.

### Return type

**object**


## accept_terms_of_use

```python
object client.accept_terms_of_use()
```

**POST** `/api/signup/acceptTermsOfUse`

Accept Terms of Use (acceptTermsOfUse)

Accept Terms of Use by the current user.

### Return type

**object**


## activate_email

```python
str client.activate_email(email_code: str, pkg_name: Optional[str] = None, platform: Optional[str] = None)
```

**GET** `/api/noauth/activateEmail`

Activate User using code from Email (activateEmail)

Activate the user using code(link) from the activation email. Validates the code an redirects according to the signup flow. Checks that user was not activated yet.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **email_code** | **str** | Activation token. | |
| **pkg_name** | **str** | Optional package name of the mobile application. | [optional] |
| **platform** | **str** | Platform type | [optional] [enum: ANDROID, IOS] |

### Return type

**str**


## activate_user_by_email_code

```python
JwtPair client.activate_user_by_email_code(email_code: str, pkg_name: Optional[str] = None, platform: Optional[str] = None)
```

**POST** `/api/noauth/activateByEmailCode`

Activate and login using code from Email (activateUserByEmailCode)

Activate the user using code(link) from the activation email and return the JWT Token. Sends the notification and email about user activation. Checks that user was not activated yet.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **email_code** | **str** | Activation token. | |
| **pkg_name** | **str** | Optional package name of the mobile application. | [optional] |
| **platform** | **str** | Platform type | [optional] [enum: ANDROID, IOS] |

### Return type

**JwtPair**


## mobile_login

```python
str client.mobile_login(pkg_name: str, platform: str)
```

**GET** `/api/noauth/login`

Mobile Login redirect (mobileLogin)

This method generates redirect to the special link that is handled by mobile application. Useful for email verification flow on mobile app.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pkg_name** | **str** | Mobile app package name. Used to identify the application and build the redirect link. | |
| **platform** | **str** | Platform type | [enum: ANDROID, IOS] |

### Return type

**str**


## privacy_policy_accepted

```python
bool client.privacy_policy_accepted()
```

**GET** `/api/signup/privacyPolicyAccepted`

Check privacy policy (privacyPolicyAccepted)

Checks that current user accepted the privacy policy.

### Return type

**bool**


## resend_email_activation

```python
None client.resend_email_activation(email: str, pkg_name: Optional[str] = None, platform: Optional[str] = None)
```

**POST** `/api/noauth/resendEmailActivation`

Resend Activation Email (resendEmailActivation)

Request to resend the activation email for the user. Checks that user was not activated yet.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **email** | **str** | Email of the user. | |
| **pkg_name** | **str** | Optional package name of the mobile application. | [optional] |
| **platform** | **str** | Platform type | [optional] [enum: ANDROID, IOS] |

### Return type

None (empty response body)


## sign_up

```python
SignUpResult client.sign_up(sign_up_request: SignUpRequest)
```

**POST** `/api/noauth/signup`

User Sign Up (signUp)

Process user sign up request. Creates the Customer and corresponding User based on self Registration parameters for the domain. See [Self Registration Controller](/swagger-ui.html#/self-registration-controller) for more details.  The result is either 'SUCCESS' or 'INACTIVE_USER_EXISTS'. If Success, the user will receive an email with instruction to activate the account. The content of the email is customizable via the mail templates.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **sign_up_request** | **SignUpRequest** |  | |

### Return type

**SignUpResult**


## terms_of_use_accepted

```python
bool client.terms_of_use_accepted()
```

**GET** `/api/signup/termsOfUseAccepted`

Check Terms Of User (termsOfUseAccepted)

Checks that current user accepted the privacy policy.

### Return type

**bool**

