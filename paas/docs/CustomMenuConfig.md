
# CustomMenuConfig

`tb_paas_client.models.CustomMenuConfig`

A JSON value representing the custom menu configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **items** | [**List[MenuItem]**](MenuItem.md) |  | [optional] |



## Referenced Types

#### MenuItem
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | MenuItemType | Menu item type |  |
| visible | bool |  | [optional] |

#### MenuItemType (enum)
`HOME` | `DEFAULT` | `CUSTOM`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.items`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CustomMenuConfig.model_validate(data)` or `CustomMenuConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

