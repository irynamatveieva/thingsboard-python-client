
# BlobEntityInfo

`tb_paas_client.models.BlobEntityInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**BlobEntityId**](BlobEntityId.md) | JSON object with the blob entity Id. Referencing non-existing blob entity Id will cause error | [optional] |
| **created_time** | **int** | Timestamp of the blob entity creation, in milliseconds | [optional] [readonly] |
| **additional_info** | **object** | Additional parameters of the blob entity | [optional] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id | [optional] [readonly] |
| **customer_id** | [**CustomerId**](CustomerId.md) | JSON object with Customer Id | [optional] [readonly] |
| **name** | **str** | blob entity name | [optional] [readonly] |
| **type** | **str** | blob entity type | [optional] [readonly] |
| **content_type** | **Content_typeEnum** | blob content type | [optional] [readonly] |
| **owner_id** | [**EntityId**](EntityId.md) | JSON object with Customer or Tenant Id | [optional] [readonly] |


### Enum: Content_typeEnum

| Name | Value |
|---- | -----|
| &#39;application/pdf&#39; | 'application/pdf' |
| &#39;image/jpeg&#39; | 'image/jpeg' |
| &#39;image/png&#39; | 'image/png' |



## Referenced Types

> **EntityId types** (`BlobEntityId`, `CustomerId`, `TenantId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `BlobEntityInfo.model_validate(data)` or `BlobEntityInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

