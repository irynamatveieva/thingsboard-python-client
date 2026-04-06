
# AwsSnsSmsProviderConfiguration

`tb_pe_client.models.AwsSnsSmsProviderConfiguration`

**Extends:** **SmsProviderConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **access_key_id** | **str** | The AWS SNS Access Key ID. | [optional] |
| **secret_access_key** | **str** | The AWS SNS Access Key. | [optional] |
| **region** | **str** | The AWS region. | [optional] |



## Referenced Types

#### SmsProviderConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.access_key_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AwsSnsSmsProviderConfiguration.model_validate(data)` or `AwsSnsSmsProviderConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

