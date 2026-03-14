
# MobileApp

`tb_paas_client.models.MobileApp`

A JSON value representing the Mobile Application.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**MobileAppId**](MobileAppId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id | [optional] |
| **pkg_name** | **str** | Application package name. Cannot be empty | |
| **title** | **str** | Application title | [optional] |
| **app_secret** | **str** | Application secret. The length must be at least 16 characters | |
| **platform_type** | [**PlatformType**](PlatformType.md) | Application platform type: ANDROID or IOS | |
| **status** | [**MobileAppStatus**](MobileAppStatus.md) | Application status: PUBLISHED, DEPRECATED, SUSPENDED, DRAFT | |
| **version_info** | [**MobileAppVersionInfo**](MobileAppVersionInfo.md) | Application version info | [optional] |
| **store_info** | [**StoreInfo**](StoreInfo.md) | Application store information | [optional] |
| **name** | **str** | Mobile app package name | [optional] [readonly] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `MobileApp.model_validate(data)` or `MobileApp.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

