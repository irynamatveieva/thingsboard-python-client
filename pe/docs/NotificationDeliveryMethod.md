
# NotificationDeliveryMethod

`tb_pe_client.models.NotificationDeliveryMethod`

## Enum Values


* `WEB` (value: `'WEB'`)

* `EMAIL` (value: `'EMAIL'`)

* `SMS` (value: `'SMS'`)

* `SLACK` (value: `'SLACK'`)

* `MICROSOFT_TEAMS` (value: `'MICROSOFT_TEAMS'`)

* `MOBILE_APP` (value: `'MOBILE_APP'`)



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `NotificationDeliveryMethod.model_validate(data)` or `NotificationDeliveryMethod.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

