
# DeliveryMethodNotificationTemplate

`tb_paas_client.models.DeliveryMethodNotificationTemplate`

Base template for different delivery methods

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **enabled** | **bool** |  | [optional] |
| **body** | **str** |  | |
| **method** | **str** |  | |



## Subtypes

#### EmailDeliveryMethodNotificationTemplate  *(method=`EMAIL`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| subject | str |  |  |

#### MicrosoftTeamsDeliveryMethodNotificationTemplate  *(method=`MICROSOFT_TEAMS`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| subject | str |  | [optional] |
| theme_color | str |  | [optional] |
| button | Button |  | [optional] |

#### MobileAppDeliveryMethodNotificationTemplate  *(method=`MOBILE_APP`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| subject | str | Subject line for the mobile notification |  |
| additional_config | object | Additional JSON configuration for web buttons/actions | [optional] |

#### SlackDeliveryMethodNotificationTemplate  *(method=`SLACK`)*
*(no additional properties)*

#### SmsDeliveryMethodNotificationTemplate  *(method=`SMS`)*
*(no additional properties)*

#### WebDeliveryMethodNotificationTemplate  *(method=`WEB`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| subject | str | Subject line for the web notification |  |
| additional_config | object | Additional JSON configuration for web buttons/actions | [optional] |

## Referenced Types

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

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.enabled`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DeliveryMethodNotificationTemplate.model_validate(data)` or `DeliveryMethodNotificationTemplate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

