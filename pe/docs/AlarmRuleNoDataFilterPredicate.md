
# AlarmRuleNoDataFilterPredicate

`tb_pe_client.models.AlarmRuleNoDataFilterPredicate`

**Extends:** **AlarmRuleKeyFilterPredicate**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **duration** | [**AlarmConditionValueLong**](AlarmConditionValueLong.md) |  | |
| **unit** | [**TimeUnit**](TimeUnit.md) |  | |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.duration`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRuleNoDataFilterPredicate.model_validate(data)` or `AlarmRuleNoDataFilterPredicate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

