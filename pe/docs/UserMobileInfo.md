
# UserMobileInfo

`tb_pe_client.models.UserMobileInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **user** | [**User**](User.md) |  | [optional] |
| **store_info** | [**StoreInfo**](StoreInfo.md) |  | [optional] |
| **version_info** | [**MobileAppVersionInfo**](MobileAppVersionInfo.md) |  | [optional] |
| **home_dashboard_info** | [**HomeDashboardInfo**](HomeDashboardInfo.md) |  | [optional] |
| **pages** | **object** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.user`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `UserMobileInfo.model_validate(data)` or `UserMobileInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

