
# Button

`tb_pe_client.models.Button`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **enabled** | **bool** |  | [optional] |
| **text** | **str** |  | [optional] |
| **link_type** | [**LinkType**](LinkType.md) |  | [optional] |
| **link** | **str** |  | [optional] |
| **dashboard_id** | **UUID** |  | [optional] |
| **dashboard_state** | **str** |  | [optional] |
| **set_entity_id_in_state** | **bool** |  | [optional] |



## Referenced Types

#### LinkType (enum)
`LINK` | `DASHBOARD`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.enabled`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Button.model_validate(data)` or `Button.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

