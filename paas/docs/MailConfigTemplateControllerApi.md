# MailConfigTemplateControllerApi

`ThingsboardClient` methods:

```python
object client.get_client_registration_templates()  # Get the list of all OAuth2 client registration templates (getClientRegistrationTemplates)  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.
```


## get_client_registration_templates

```python
object client.get_client_registration_templates()
```

**GET** `/api/mail/config/template`

Get the list of all OAuth2 client registration templates (getClientRegistrationTemplates)  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.

Mail configuration template is set of default smtp settings for mail server that specific provider supports

### Return type

**object**

