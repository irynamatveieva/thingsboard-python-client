
# TbImageDeleteResult

`tb_paas_client.models.TbImageDeleteResult`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **success** | **bool** |  | [optional] |
| **white_labeling_list** | [**List[WhiteLabeling]**](WhiteLabeling.md) |  | [optional] |
| **references** | **Dict[str, List[HasIdObject]]** |  | [optional] |



## Referenced Types

> **EntityId types** (`CustomerId`, `DomainId`, `TenantId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### WhiteLabeling
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| tenant_id | TenantId |  | [optional] |
| customer_id | CustomerId |  | [optional] |
| type | WhiteLabelingType |  | [optional] |
| settings | object |  | [optional] |
| legacy_domain | str |  | [optional] [readonly] |
| domain_id | DomainId |  | [optional] |

#### WhiteLabelingType (enum)
`LOGIN` | `GENERAL` | `MAIL_TEMPLATES` | `SELF_REGISTRATION` | `TERMS_OF_USE` | `PRIVACY_POLICY`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.success`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TbImageDeleteResult.model_validate(data)` or `TbImageDeleteResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

