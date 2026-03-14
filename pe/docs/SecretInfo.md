
# SecretInfo

`tb_pe_client.models.SecretInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**SecretId**](SecretId.md) | JSON object with the Secret Id. Specify this field to update the Secret. Referencing non-existing Secret Id will cause error. Omit this field to create new Secret. | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id. Tenant Id of the secret cannot be changed. | [optional] [readonly] |
| **name** | **str** | Secret name | |
| **type** | [**SecretType**](SecretType.md) | Secret type. | |
| **description** | **str** | Secret description. | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SecretInfo.model_validate(data)` or `SecretInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

