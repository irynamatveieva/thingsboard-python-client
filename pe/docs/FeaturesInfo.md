
# FeaturesInfo

`tb_pe_client.models.FeaturesInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **white_labeling_enabled** | **bool** |  | [optional] |
| **email_enabled** | **bool** |  | [optional] |
| **sms_enabled** | **bool** |  | [optional] |
| **notification_enabled** | **bool** |  | [optional] |
| **oauth_enabled** | **bool** |  | [optional] |
| **two_fa_enabled** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.white_labeling_enabled`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `FeaturesInfo.model_validate(data)` or `FeaturesInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

