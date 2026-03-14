# SelfRegistrationControllerApi

`ThingsboardClient` methods:

```python
None client.delete_web_self_registration_params()  # deleteWebSelfRegistrationParams
str client.get_privacy_policy(pkg_name: Optional[str] = None, platform: Optional[PlatformType] = None)  # Get Privacy Policy for Self Registration form (getPrivacyPolicy)
SignUpSelfRegistrationParams client.get_sign_up_self_registration_params(pkg_name: Optional[str] = None, platform_type: Optional[str] = None)  # Get Self Registration form parameters without authentication (getSignUpSelfRegistrationParams)
str client.get_terms_of_use(pkg_name: Optional[str] = None, platform: Optional[PlatformType] = None)  # Get Terms of Use for Self Registration form (getTermsOfUse)
SelfRegistrationParams client.get_web_self_registration_params()  # Get Self Registration parameters (getSelfRegistrationParams)
WebSelfRegistrationParams client.save_web_self_registration_params(web_self_registration_params: WebSelfRegistrationParams)  # Create Or Update Self Registration parameters (saveSelfRegistrationParams)
```


## delete_web_self_registration_params

```python
None client.delete_web_self_registration_params()
```

**DELETE** `/api/selfRegistration/selfRegistrationParams`

deleteWebSelfRegistrationParams

### Return type

None (empty response body)


## get_privacy_policy

```python
str client.get_privacy_policy(pkg_name: Optional[str] = None, platform: Optional[PlatformType] = None)
```

**GET** `/api/noauth/selfRegistration/privacyPolicy`

Get Privacy Policy for Self Registration form (getPrivacyPolicy)

Fetch the Privacy Policy based on the domain name from the request. Available for non-authorized users. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pkg_name** | **str** |  | [optional] |
| **platform** | **PlatformType** |  | [optional] [enum: WEB, ANDROID, IOS] |

### Return type

**str**


## get_sign_up_self_registration_params

```python
SignUpSelfRegistrationParams client.get_sign_up_self_registration_params(pkg_name: Optional[str] = None, platform_type: Optional[str] = None)
```

**GET** `/api/noauth/selfRegistration/signUpSelfRegistrationParams`

Get Self Registration form parameters without authentication (getSignUpSelfRegistrationParams)

Fetch the Self Registration parameters based on the domain name from the request. Available for non-authorized users. Contains the information to customize the sign-up form.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pkg_name** | **str** |  | [optional] |
| **platform_type** | **str** | Platform type | [optional] [enum: ANDROID, IOS] |

### Return type

**SignUpSelfRegistrationParams**


## get_terms_of_use

```python
str client.get_terms_of_use(pkg_name: Optional[str] = None, platform: Optional[PlatformType] = None)
```

**GET** `/api/noauth/selfRegistration/termsOfUse`

Get Terms of Use for Self Registration form (getTermsOfUse)

Fetch the Terms of Use based on the domain name from the request. Available for non-authorized users. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pkg_name** | **str** |  | [optional] |
| **platform** | **PlatformType** |  | [optional] [enum: WEB, ANDROID, IOS] |

### Return type

**str**


## get_web_self_registration_params

```python
SelfRegistrationParams client.get_web_self_registration_params()
```

**GET** `/api/selfRegistration/selfRegistrationParams`

Get Self Registration parameters (getSelfRegistrationParams)

Fetch the Self Registration parameters object for the tenant of the current user.   Available for users with 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'READ' permission for the white labeling resource.

### Return type

**SelfRegistrationParams**


## save_web_self_registration_params

```python
WebSelfRegistrationParams client.save_web_self_registration_params(web_self_registration_params: WebSelfRegistrationParams)
```

**POST** `/api/selfRegistration/selfRegistrationParams`

Create Or Update Self Registration parameters (saveSelfRegistrationParams)

Creates or Updates the Self Registration parameters. When creating, platform generates Admin Settings Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Admin Settings Id will be present in the response. Specify existing Admin Settings Id to update the Self Registration parameters. Referencing non-existing Admin Settings Id will cause 'Not Found' error.  Self Registration allows users to signup for using the platform and automatically create a Customer account for them. You may configure default dashboard and user roles that will be assigned for this Customer. This allows you to build out-of-the-box solutions for customers. Ability to white-label the login and main pages helps to brand the platform.  Available for users with 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **web_self_registration_params** | **WebSelfRegistrationParams** |  | |

### Return type

**WebSelfRegistrationParams**

