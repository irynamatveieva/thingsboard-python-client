
# SchedulerEventFilter

`tb_pe_client.models.SchedulerEventFilter`

**Extends:** **EntityFilter**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **originator** | [**AliasEntityId**](AliasEntityId.md) |  | [optional] |
| **event_type** | **str** |  | [optional] |
| **originator_state_entity** | **bool** |  | [optional] |
| **default_state_entity** | [**AliasEntityId**](AliasEntityId.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.originator`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SchedulerEventFilter.model_validate(data)` or `SchedulerEventFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

