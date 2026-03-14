# OAuth2ConfigTemplateControllerApi

`ThingsboardClient` methods:

```python
None client.delete_client_registration_template(client_registration_template_id: str)  # Delete OAuth2 client registration template by id (deleteClientRegistrationTemplate)  Available for users with 'SYS_ADMIN' authority.
List[OAuth2ClientRegistrationTemplate] client.get_o_auth2_client_registration_templates()  # Get the list of all OAuth2 client registration templates (getOAuth2ClientRegistrationTemplates)  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.
OAuth2ClientRegistrationTemplate client.save_client_registration_template(o_auth2_client_registration_template: OAuth2ClientRegistrationTemplate)  # Create or update OAuth2 client registration template (saveClientRegistrationTemplate)  Available for users with 'SYS_ADMIN' authority.
```


## delete_client_registration_template

```python
None client.delete_client_registration_template(client_registration_template_id: str)
```

**DELETE** `/api/oauth2/config/template/{clientRegistrationTemplateId}`

Delete OAuth2 client registration template by id (deleteClientRegistrationTemplate)  Available for users with 'SYS_ADMIN' authority.

Client registration template is OAuth2 provider configuration template with default settings for registering new OAuth2 clients


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **client_registration_template_id** | **str** | String representation of client registration template id to delete | |

### Return type

None (empty response body)


## get_o_auth2_client_registration_templates

```python
List[OAuth2ClientRegistrationTemplate] client.get_o_auth2_client_registration_templates()
```

**GET** `/api/oauth2/config/template`

Get the list of all OAuth2 client registration templates (getOAuth2ClientRegistrationTemplates)  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.

Client registration template is OAuth2 provider configuration template with default settings for registering new OAuth2 clients

### Return type

**List[OAuth2ClientRegistrationTemplate]**


## save_client_registration_template

```python
OAuth2ClientRegistrationTemplate client.save_client_registration_template(o_auth2_client_registration_template: OAuth2ClientRegistrationTemplate)
```

**POST** `/api/oauth2/config/template`

Create or update OAuth2 client registration template (saveClientRegistrationTemplate)  Available for users with 'SYS_ADMIN' authority.

Client registration template is OAuth2 provider configuration template with default settings for registering new OAuth2 clients


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **o_auth2_client_registration_template** | **OAuth2ClientRegistrationTemplate** |  | |

### Return type

**OAuth2ClientRegistrationTemplate**

