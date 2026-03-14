
# WhiteLabeling

`tb_pe_client.models.WhiteLabeling`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **tenant_id** | [**TenantId**](TenantId.md) |  | [optional] |
| **customer_id** | [**CustomerId**](CustomerId.md) |  | [optional] |
| **type** | [**WhiteLabelingType**](WhiteLabelingType.md) |  | [optional] |
| **settings** | **object** |  | [optional] |
| **domain_id** | [**DomainId**](DomainId.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.tenant_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `WhiteLabeling.model_validate(data)` or `WhiteLabeling.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

