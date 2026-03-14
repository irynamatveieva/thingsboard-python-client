# SignUpControllerApi

`ThingsboardClient` methods:

```python
JwtPair client.accept_privacy_policy()  # Accept privacy policy (acceptPrivacyPolicy)
JwtPair client.accept_privacy_policy_and_terms_of_use()  # acceptPrivacyPolicyAndTermsOfUse
JwtPair client.accept_terms_of_use()  # Accept Terms of Use (acceptTermsOfUse)
str client.activate_cloud_email(email_code: str, pkg_name: Optional[str] = None, platform: Optional[str] = None)  # activateCloudEmail
JwtPair client.activate_cloud_user_by_email_code(email_code: str, pkg_name: Optional[str] = None, platform: Optional[str] = None)  # activateCloudUserByEmailCode
str client.activate_email(email_code: str, pkg_name: Optional[str] = None, platform: Optional[str] = None)  # Activate User using code from Email (activateEmail)
JwtPair client.activate_user_by_email_code(email_code: str, pkg_name: Optional[str] = None, platform: Optional[str] = None)  # Activate and login using code from Email (activateUserByEmailCode)
str client.cloud_mobile_login(pkg_name: str, platform: Optional[str] = None)  # Cloud mobile Login redirect (cloudMobileLogin)
None client.delete_tenant_account(delete_tenant_request: Optional[DeleteTenantRequest] = None)  # deleteTenantAccount
CaptchaClientParams client.get_recaptcha_params()  # getRecaptchaParams
bool client.is_display_welcome()  # isDisplayWelcome
str client.mobile_login(pkg_name: str, platform: str)  # Mobile Login redirect (mobileLogin)
bool client.privacy_policy_accepted()  # Check privacy policy (privacyPolicyAccepted)
None client.resend_cloud_email_activation(email: str, pkg_name: Optional[str] = None, platform: Optional[str] = None)  # resendCloudEmailActivation
None client.resend_email_activation(email: str, pkg_name: Optional[str] = None, platform: Optional[str] = None)  # Resend Activation Email (resendEmailActivation)
None client.set_not_display_welcome()  # setNotDisplayWelcome
SignUpResult client.sign_up(sign_up_request: SignUpRequest)  # User Sign Up (signUp)
bool client.terms_of_use_accepted()  # Check Terms Of User (termsOfUseAccepted)
```


## accept_privacy_policy

```python
JwtPair client.accept_privacy_policy()
```

**POST** `/api/signup/acceptPrivacyPolicy`

Accept privacy policy (acceptPrivacyPolicy)

Accept privacy policy by the current user.

### Return type

**JwtPair**


## accept_privacy_policy_and_terms_of_use

```python
JwtPair client.accept_privacy_policy_and_terms_of_use()
```

**POST** `/api/signup/acceptPrivacyPolicyAndTermsOfUse`

acceptPrivacyPolicyAndTermsOfUse

### Return type

**JwtPair**


## accept_terms_of_use

```python
JwtPair client.accept_terms_of_use()
```

**POST** `/api/signup/acceptTermsOfUse`

Accept Terms of Use (acceptTermsOfUse)

Accept Terms of Use by the current user.

### Return type

**JwtPair**


## activate_cloud_email

```python
str client.activate_cloud_email(email_code: str, pkg_name: Optional[str] = None, platform: Optional[str] = None)
```

**GET** `/api/noauth/cloud/activateEmail`

activateCloudEmail


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **email_code** | **str** |  | |
| **pkg_name** | **str** | Optional package name of the mobile application. | [optional] |
| **platform** | **str** | Platform type | [optional] [enum: ANDROID, IOS] |

### Return type

**str**


## activate_cloud_user_by_email_code

```python
JwtPair client.activate_cloud_user_by_email_code(email_code: str, pkg_name: Optional[str] = None, platform: Optional[str] = None)
```

**POST** `/api/noauth/cloud/activateByEmailCode`

activateCloudUserByEmailCode


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **email_code** | **str** |  | |
| **pkg_name** | **str** | Optional package name of the mobile application. | [optional] |
| **platform** | **str** | Platform type | [optional] [enum: ANDROID, IOS] |

### Return type

**JwtPair**


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


## cloud_mobile_login

```python
str client.cloud_mobile_login(pkg_name: str, platform: Optional[str] = None)
```

**GET** `/api/noauth/cloud/login`

Cloud mobile Login redirect (cloudMobileLogin)

This method generates redirect to the special link that is handled by mobile application. Useful for email verification flow on cloud mobile app.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pkg_name** | **str** | Mobile app package name. Used to identify the application and build the redirect link. | |
| **platform** | **str** | Platform type | [optional] [enum: ANDROID, IOS] |

### Return type

**str**


## delete_tenant_account

```python
None client.delete_tenant_account(delete_tenant_request: Optional[DeleteTenantRequest] = None)
```

**POST** `/api/signup/tenantAccount`

deleteTenantAccount


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **delete_tenant_request** | **DeleteTenantRequest** |  | [optional] |

### Return type

None (empty response body)


## get_recaptcha_params

```python
CaptchaClientParams client.get_recaptcha_params()
```

**GET** `/api/noauth/signup/recaptchaParams`

getRecaptchaParams

### Return type

**CaptchaClientParams**


## is_display_welcome

```python
bool client.is_display_welcome()
```

**GET** `/api/signup/displayWelcome`

isDisplayWelcome

### Return type

**bool**


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


## resend_cloud_email_activation

```python
None client.resend_cloud_email_activation(email: str, pkg_name: Optional[str] = None, platform: Optional[str] = None)
```

**POST** `/api/noauth/cloud/resendEmailActivation`

resendCloudEmailActivation


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **email** | **str** |  | |
| **pkg_name** | **str** |  | [optional] |
| **platform** | **str** | Platform type | [optional] [enum: ANDROID, IOS] |

### Return type

None (empty response body)


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


## set_not_display_welcome

```python
None client.set_not_display_welcome()
```

**POST** `/api/signup/notDisplayWelcome`

setNotDisplayWelcome

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

