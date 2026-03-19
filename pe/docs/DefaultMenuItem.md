
# DefaultMenuItem

`tb_pe_client.models.DefaultMenuItem`

**Extends:** **MenuItem**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | Unique identifier for predefined menu items | [optional] [readonly] |
| **name** | **str** | Name of the menu item | [optional] |
| **icon** | **str** | URL of the menu item icon. Overrides 'materialIcon' | [optional] |
| **visible** | **bool** | Mark if menu item is visible for user | [optional] |
| **pages** | [**List[DefaultMenuItem]**](DefaultMenuItem.md) | List of child menu items | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DefaultMenuItem.model_validate(data)` or `DefaultMenuItem.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

