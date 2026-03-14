
# LoginMobileInfo

`tb_paas_client.models.LoginMobileInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **o_auth2_client_login_infos** | [**List[OAuth2ClientLoginInfo]**](OAuth2ClientLoginInfo.md) |  | [optional] |
| **self_registration_params** | [**SignUpSelfRegistrationParams**](SignUpSelfRegistrationParams.md) |  | [optional] |
| **store_info** | [**StoreInfo**](StoreInfo.md) |  | [optional] |
| **version_info** | [**MobileAppVersionInfo**](MobileAppVersionInfo.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.o_auth2_client_login_infos`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `LoginMobileInfo.model_validate(data)` or `LoginMobileInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

