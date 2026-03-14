
# ComponentLifecycleEvent

`tb_paas_client.models.ComponentLifecycleEvent`

## Enum Values


* `CREATED` (value: `'CREATED'`)

* `STARTED` (value: `'STARTED'`)

* `ACTIVATED` (value: `'ACTIVATED'`)

* `SUSPENDED` (value: `'SUSPENDED'`)

* `UPDATED` (value: `'UPDATED'`)

* `STOPPED` (value: `'STOPPED'`)

* `DELETED` (value: `'DELETED'`)

* `FAILED` (value: `'FAILED'`)

* `DEACTIVATED` (value: `'DEACTIVATED'`)

* `RELATION_UPDATED` (value: `'RELATION_UPDATED'`)

* `RELATION_DELETED` (value: `'RELATION_DELETED'`)



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ComponentLifecycleEvent.model_validate(data)` or `ComponentLifecycleEvent.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

