
# TenantProfileData

`tb_paas_client.models.TenantProfileData`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **configuration** | [**TenantProfileConfiguration**](TenantProfileConfiguration.md) | Complex JSON object that contains profile settings: max devices, max assets, rate limits, etc. | [optional] |
| **queue_configuration** | [**List[TenantProfileQueueConfiguration]**](TenantProfileQueueConfiguration.md) | JSON array of queue configuration per tenant profile | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.configuration`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TenantProfileData.model_validate(data)` or `TenantProfileData.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

