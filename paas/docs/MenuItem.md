
# MenuItem

`tb_paas_client.models.MenuItem`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | [**MenuItemType**](MenuItemType.md) | Menu item type | |
| **visible** | **bool** |  | [optional] |



## Referenced Types

#### MenuItemType (enum)
`HOME` | `DEFAULT` | `CUSTOM`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `MenuItem.model_validate(data)` or `MenuItem.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

