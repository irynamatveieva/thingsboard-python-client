
# MobileAppVersionInfo

`tb_paas_client.models.MobileAppVersionInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **min_version** | **str** | Minimum supported version | [optional] |
| **min_version_release_notes** | **str** | Release notes of minimum supported version | [optional] |
| **latest_version** | **str** | Latest supported version | [optional] |
| **latest_version_release_notes** | **str** | Release notes of latest supported version | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.min_version`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `MobileAppVersionInfo.model_validate(data)` or `MobileAppVersionInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

