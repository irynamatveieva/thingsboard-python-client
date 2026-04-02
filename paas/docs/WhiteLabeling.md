
# WhiteLabeling

`tb_paas_client.models.WhiteLabeling`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **tenant_id** | [**TenantId**](TenantId.md) |  | [optional] |
| **customer_id** | [**CustomerId**](CustomerId.md) |  | [optional] |
| **type** | [**WhiteLabelingType**](WhiteLabelingType.md) |  | [optional] |
| **settings** | **object** |  | [optional] |
| **legacy_domain** | **str** |  | [optional] [readonly] |
| **domain_id** | [**DomainId**](DomainId.md) |  | [optional] |



## Referenced Types

> **EntityId types** (`CustomerId`, `DomainId`, `TenantId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### WhiteLabelingType (enum)
`LOGIN` | `GENERAL` | `MAIL_TEMPLATES` | `SELF_REGISTRATION` | `TERMS_OF_USE` | `PRIVACY_POLICY`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.tenant_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `WhiteLabeling.model_validate(data)` or `WhiteLabeling.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

