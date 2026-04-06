
# MicrosoftTeamsDeliveryMethodNotificationTemplate

`tb_pe_client.models.MicrosoftTeamsDeliveryMethodNotificationTemplate`

**Extends:** **DeliveryMethodNotificationTemplate**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **subject** | **str** |  | [optional] |
| **theme_color** | **str** |  | [optional] |
| **button** | [**Button**](Button.md) |  | [optional] |



## Referenced Types

#### DeliveryMethodNotificationTemplate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| enabled | bool |  | [optional] |
| body | str |  |  |
| method | str |  |  |

#### Button
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| enabled | bool |  | [optional] |
| text | str |  | [optional] |
| link_type | LinkType |  | [optional] |
| link | str |  | [optional] |
| dashboard_id | UUID |  | [optional] |
| dashboard_state | str |  | [optional] |
| set_entity_id_in_state | bool |  | [optional] |

#### LinkType (enum)
`LINK` | `DASHBOARD`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.subject`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `MicrosoftTeamsDeliveryMethodNotificationTemplate.model_validate(data)` or `MicrosoftTeamsDeliveryMethodNotificationTemplate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

