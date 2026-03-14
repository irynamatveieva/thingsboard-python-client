
# SelfRegistrationParams

`tb_paas_client.models.SelfRegistrationParams`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | [**SelfRegistrationType**](SelfRegistrationType.md) |  | |
| **enabled** | **bool** |  | [optional] |
| **title** | **str** |  | [optional] |
| **captcha** | [**CaptchaParams**](CaptchaParams.md) |  | [optional] |
| **permissions** | [**List[GroupPermission]**](GroupPermission.md) |  | [optional] |
| **notification_recipient** | [**NotificationTargetId**](NotificationTargetId.md) |  | [optional] |
| **sign_up_fields** | [**List[SignUpField]**](SignUpField.md) |  | [optional] |
| **customer_title_prefix** | **str** |  | [optional] |
| **show_privacy_policy** | **bool** |  | [optional] |
| **show_terms_of_use** | **bool** |  | [optional] |
| **default_dashboard** | [**DefaultDashboardParams**](DefaultDashboardParams.md) |  | [optional] |
| **home_dashboard** | [**HomeDashboardParams**](HomeDashboardParams.md) |  | [optional] |
| **customer_group_id** | [**EntityGroupId**](EntityGroupId.md) |  | [optional] |
| **custom_menu_id** | [**CustomMenuId**](CustomMenuId.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SelfRegistrationParams.model_validate(data)` or `SelfRegistrationParams.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

