
# HomeMenuItem

`tb_pe_client.models.HomeMenuItem`

**Extends:** **MenuItem**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | Unique identifier for predefined menu items | [optional] [readonly] |
| **name** | **str** | Name of the menu item | [optional] |
| **icon** | **str** | URL of the menu item icon. Overrides 'materialIcon' | [optional] |
| **pages** | [**List[DefaultMenuItem]**](DefaultMenuItem.md) | List of child menu items | [optional] |
| **home_type** | [**HomeMenuItemType**](HomeMenuItemType.md) | DEFAULT or DASHBOARD. DASHBOARD means default home page presentation changed to refer to dashboard | [optional] |
| **dashboard_id** | **str** | Id of the Dashboard to open, when user clicks the menu item | [optional] |
| **hide_dashboard_toolbar** | **bool** | Hide the dashboard toolbar | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `HomeMenuItem.model_validate(data)` or `HomeMenuItem.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

