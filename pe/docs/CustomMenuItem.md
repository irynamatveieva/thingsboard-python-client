
# CustomMenuItem

`tb_pe_client.models.CustomMenuItem`

**Extends:** **MenuItem**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **name** | **str** | Name of the menu item | |
| **icon** | **str** | URL of the menu item icon. Overrides 'materialIcon' | [optional] |
| **menu_item_type** | [**CMItemType**](CMItemType.md) | Type of menu item (LINK or SECTION). LINK type means item has no child items, SECTION type should have at least one child | |
| **link_type** | [**CMItemLinkType**](CMItemLinkType.md) | Type of menu item (URL or DASHBOARD) | [optional] |
| **dashboard_id** | **str** | Id of the Dashboard to open, when user clicks the menu item | [optional] |
| **hide_dashboard_toolbar** | **bool** | Hide the dashboard toolbar | [optional] |
| **url** | **str** | URL to open in the iframe, when user clicks the menu item | [optional] |
| **set_access_token** | **bool** | Set the access token of the current user to a new dashboard | [optional] |
| **visible** | **bool** | Mark if menu item is visible for user | [optional] |
| **pages** | [**List[CustomMenuItem]**](CustomMenuItem.md) | List of child menu items | [optional] |



## Referenced Types

#### MenuItem
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | MenuItemType | Menu item type |  |
| visible | bool |  | [optional] |

#### CMItemType (enum)
`LINK` | `SECTION`

#### CMItemLinkType (enum)
`URL` | `DASHBOARD`

#### MenuItemType (enum)
`HOME` | `DEFAULT` | `CUSTOM`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.name`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CustomMenuItem.model_validate(data)` or `CustomMenuItem.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

