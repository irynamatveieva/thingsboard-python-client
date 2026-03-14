
# AlarmRuleNoDataFilterPredicate

`tb_ce_client.models.AlarmRuleNoDataFilterPredicate`

**Extends:** **AlarmRuleKeyFilterPredicate**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **unit** | [**TimeUnit**](TimeUnit.md) |  | |
| **duration** | [**AlarmConditionValueLong**](AlarmConditionValueLong.md) |  | |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.unit`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRuleNoDataFilterPredicate.model_validate(data)` or `AlarmRuleNoDataFilterPredicate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

