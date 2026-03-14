# QrCodeSettingsControllerApi

`ThingsboardClient` methods:

```python
object client.get_application_redirect(user_agent: str)  # getApplicationRedirect
str client.get_mobile_app_deep_link()  # Get the deep link to the associated mobile application (getMobileAppDeepLink)
QrCodeSettings client.get_qr_code_settings()  # Get Mobile application settings (getQrCodeSettings)
JwtPair client.get_user_token_by_mobile_secret(secret: str)  # Get User Token (getUserTokenByMobileSecret)
QrCodeSettings client.save_qr_code_settings(qr_code_settings: QrCodeSettings)  # Create Or Update the Mobile application settings (saveMobileAppSettings)
```


## get_application_redirect

```python
object client.get_application_redirect(user_agent: str)
```

**GET** `/api/noauth/qr`

getApplicationRedirect


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user_agent** | **str** |  | |

### Return type

**object**


## get_mobile_app_deep_link

```python
str client.get_mobile_app_deep_link()
```

**GET** `/api/mobile/qr/deepLink`

Get the deep link to the associated mobile application (getMobileAppDeepLink)

Fetch the url that takes user to linked mobile application   Available for any authorized user. 

### Return type

**str**


## get_qr_code_settings

```python
QrCodeSettings client.get_qr_code_settings()
```

**GET** `/api/mobile/qr/settings`

Get Mobile application settings (getQrCodeSettings)

The response payload contains configuration for android/iOS applications and platform qr code widget settings.  Available for any authorized user. 

### Return type

**QrCodeSettings**


## get_user_token_by_mobile_secret

```python
JwtPair client.get_user_token_by_mobile_secret(secret: str)
```

**GET** `/api/noauth/qr/{secret}`

Get User Token (getUserTokenByMobileSecret)

Returns the token of the User based on the provided secret key.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **secret** | **str** | A string value representing short-lived secret key | |

### Return type

**JwtPair**


## save_qr_code_settings

```python
QrCodeSettings client.save_qr_code_settings(qr_code_settings: QrCodeSettings)
```

**POST** `/api/mobile/qr/settings`

Create Or Update the Mobile application settings (saveMobileAppSettings)

The request payload contains configuration for android/iOS applications and platform qr code widget settings.  Available for users with 'SYS_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **qr_code_settings** | **QrCodeSettings** |  | |

### Return type

**QrCodeSettings**

