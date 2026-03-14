# WhiteLabelingControllerApi

`ThingsboardClient` methods:

```python
None client.delete_current_login_white_label_params(customer_id: Optional[str] = None)  # Delete Login White Labeling configuration (deleteCurrentLoginWhiteLabelParams)
None client.delete_current_white_label_params(customer_id: Optional[str] = None)  # Delete General White Labeling configuration (deleteCurrentWhiteLabelParams)
LoginWhiteLabelingParams client.get_current_login_white_label_params(customer_id: Optional[str] = None)  # Get Login White Labeling configuration (getCurrentWhiteLabelParams)
WhiteLabelingParams client.get_current_white_label_params(customer_id: Optional[str] = None)  # Get White Labeling configuration (getCurrentWhiteLabelParams)
LoginWhiteLabelingParams client.get_login_white_label_params()  # Get Login White Labeling parameters
object client.get_mail_templates(system_by_default: Optional[bool] = None)  # Get the Mail templates settings (getMailTemplates)
WhiteLabelingParams client.get_white_label_params()  # Get White Labeling parameters
bool client.is_customer_white_labeling_allowed()  # Check Customer White Labeling Allowed
bool client.is_white_labeling_allowed()  # Check White Labeling Allowed
WhiteLabelingParams client.preview_white_label_params(white_labeling_params: WhiteLabelingParams)  # Preview Login White Labeling configuration (saveWhiteLabelParams)
LoginWhiteLabelingParams client.save_login_white_label_params(login_white_labeling_params: LoginWhiteLabelingParams, customer_id: Optional[str] = None)  # Create Or Update Login White Labeling configuration (saveWhiteLabelParams)
object client.save_mail_templates(body: object)  # Save the Mail templates settings (saveMailTemplates)
WhiteLabelingParams client.save_white_label_params(white_labeling_params: WhiteLabelingParams, customer_id: Optional[str] = None)  # Create Or Update White Labeling configuration (saveWhiteLabelParams)
```


## delete_current_login_white_label_params

```python
None client.delete_current_login_white_label_params(customer_id: Optional[str] = None)
```

**DELETE** `/api/whiteLabel/currentLoginWhiteLabelParams`

Delete Login White Labeling configuration (deleteCurrentLoginWhiteLabelParams)

Delete the Login White Labeling configuration that corresponds to the authority of the user.   Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | [optional] |

### Return type

None (empty response body)


## delete_current_white_label_params

```python
None client.delete_current_white_label_params(customer_id: Optional[str] = None)
```

**DELETE** `/api/whiteLabel/currentWhiteLabelParams`

Delete General White Labeling configuration (deleteCurrentWhiteLabelParams)

Delete the White Labeling configuration that corresponds to the authority of the user.   Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | [optional] |

### Return type

None (empty response body)


## get_current_login_white_label_params

```python
LoginWhiteLabelingParams client.get_current_login_white_label_params(customer_id: Optional[str] = None)
```

**GET** `/api/whiteLabel/currentLoginWhiteLabelParams`

Get Login White Labeling configuration (getCurrentWhiteLabelParams)

Fetch the Login  White Labeling configuration that corresponds to the authority of the user. The API call is designed to load the Login White Labeling configuration for edition. So, the result is NOT merged with the parent level White Labeling configuration. Let's assume there is a custom White Labeling  configured on a system level. And there is no custom White Labeling  items configured on a tenant level. In such a case, the API call will return default object for the tenant administrator.   Security check is performed to verify that the user has 'READ' permission for the white labeling resource.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | [optional] |

### Return type

**LoginWhiteLabelingParams**


## get_current_white_label_params

```python
WhiteLabelingParams client.get_current_white_label_params(customer_id: Optional[str] = None)
```

**GET** `/api/whiteLabel/currentWhiteLabelParams`

Get White Labeling configuration (getCurrentWhiteLabelParams)

Fetch the White Labeling configuration that corresponds to the authority of the user. The API call is designed to load the White Labeling configuration for edition. So, the result is NOT merged with the parent level White Labeling configuration. Let's assume there is a custom White Labeling  configured on a system level. And there is no custom White Labeling  items configured on a tenant level. In such a case, the API call will return default object for the tenant administrator.   Security check is performed to verify that the user has 'READ' permission for the white labeling resource.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | [optional] |

### Return type

**WhiteLabelingParams**


## get_login_white_label_params

```python
LoginWhiteLabelingParams client.get_login_white_label_params()
```

**GET** `/api/noauth/whiteLabel/loginWhiteLabelParams`

Get Login White Labeling parameters

Returns login white-labeling parameters based on the hostname from request.

### Return type

**LoginWhiteLabelingParams**


## get_mail_templates

```python
object client.get_mail_templates(system_by_default: Optional[bool] = None)
```

**GET** `/api/whiteLabel/mailTemplates`

Get the Mail templates settings (getMailTemplates)

Fetch Mail template settings.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'READ' permission for the white labeling resource.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **system_by_default** | **bool** | Use system settings if settings are not defined on tenant level. | [optional] [default to False] |

### Return type

**object**


## get_white_label_params

```python
WhiteLabelingParams client.get_white_label_params()
```

**GET** `/api/whiteLabel/whiteLabelParams`

Get White Labeling parameters

Returns white-labeling parameters for the current user.

### Return type

**WhiteLabelingParams**


## is_customer_white_labeling_allowed

```python
bool client.is_customer_white_labeling_allowed()
```

**GET** `/api/whiteLabel/isCustomerWhiteLabelingAllowed`

Check Customer White Labeling Allowed

Check if the White Labeling is enabled for the customers of the current tenant  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  Available for users with 'TENANT_ADMIN' authority.

### Return type

**bool**


## is_white_labeling_allowed

```python
bool client.is_white_labeling_allowed()
```

**GET** `/api/whiteLabel/isWhiteLabelingAllowed`

Check White Labeling Allowed

Check if the White Labeling is enabled for the current user owner (tenant or customer)  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.

### Return type

**bool**


## preview_white_label_params

```python
WhiteLabelingParams client.preview_white_label_params(white_labeling_params: WhiteLabelingParams)
```

**POST** `/api/whiteLabel/previewWhiteLabelParams`

Preview Login White Labeling configuration (saveWhiteLabelParams)

Merge the White Labeling configuration with the parent configuration and return the result.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **white_labeling_params** | **WhiteLabelingParams** |  | |

### Return type

**WhiteLabelingParams**


## save_login_white_label_params

```python
LoginWhiteLabelingParams client.save_login_white_label_params(login_white_labeling_params: LoginWhiteLabelingParams, customer_id: Optional[str] = None)
```

**POST** `/api/whiteLabel/loginWhiteLabelParams`

Create Or Update Login White Labeling configuration (saveWhiteLabelParams)

Creates or Updates the White Labeling configuration.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **login_white_labeling_params** | **LoginWhiteLabelingParams** |  | |
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | [optional] |

### Return type

**LoginWhiteLabelingParams**


## save_mail_templates

```python
object client.save_mail_templates(body: object)
```

**POST** `/api/whiteLabel/mailTemplates`

Save the Mail templates settings (saveMailTemplates)

Creates or Updates the Mail templates settings.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | **object** | A JSON value representing the Administration Settings. | |

### Return type

**object**


## save_white_label_params

```python
WhiteLabelingParams client.save_white_label_params(white_labeling_params: WhiteLabelingParams, customer_id: Optional[str] = None)
```

**POST** `/api/whiteLabel/whiteLabelParams`

Create Or Update White Labeling configuration (saveWhiteLabelParams)

Creates or Updates the White Labeling configuration.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **white_labeling_params** | **WhiteLabelingParams** |  | |
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | [optional] |

### Return type

**WhiteLabelingParams**

