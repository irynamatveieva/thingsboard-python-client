
# MobileAppBundle

`tb_paas_client.models.MobileAppBundle`

A JSON value representing the Mobile Application Bundle.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**MobileAppBundleId**](MobileAppBundleId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id | [optional] |
| **title** | **str** | Application bundle title. Cannot be empty | |
| **description** | **str** | Application bundle description. | [optional] |
| **android_app_id** | [**MobileAppId**](MobileAppId.md) | Android application id | [optional] |
| **ios_app_id** | [**MobileAppId**](MobileAppId.md) | IOS application id | [optional] |
| **layout_config** | [**MobileLayoutConfig**](MobileLayoutConfig.md) | Application layout configuration | [optional] |
| **self_registration_params** | [**MobileSelfRegistrationParams**](MobileSelfRegistrationParams.md) | Application self registration configuration | [optional] |
| **oauth2_enabled** | **bool** | Whether OAuth2 settings are enabled or not | [optional] |
| **name** | **str** | Mobile app bundle title | [optional] [readonly] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `MobileAppBundle.model_validate(data)` or `MobileAppBundle.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

