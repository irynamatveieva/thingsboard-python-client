
# DeviceProfileAlarm

`tb_paas_client.models.DeviceProfileAlarm`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | String value representing the alarm rule id | [optional] |
| **alarm_type** | **str** | String value representing type of the alarm | [optional] |
| **create_rules** | [**Dict[str, AlarmRule]**](AlarmRule.md) | Complex JSON object representing create alarm rules. The unique create alarm rule can be created for each alarm severity type. There can be 5 create alarm rules configured per a single alarm type. See method implementation notes and AlarmRule model for more details | [optional] |
| **clear_rule** | [**AlarmRule**](AlarmRule.md) | JSON object representing clear alarm rule | [optional] |
| **propagate** | **bool** | Propagation flag to specify if alarm should be propagated to parent entities of alarm originator | [optional] |
| **propagate_to_owner** | **bool** | Propagation flag to specify if alarm should be propagated to the owner (tenant or customer) of alarm originator | [optional] |
| **propagate_to_owner_hierarchy** | **bool** | Propagation flag to specify if alarm should be propagated to the owner (tenant or customer) and all parent owners in the customer hierarchy | [optional] |
| **propagate_to_tenant** | **bool** | Propagation flag to specify if alarm should be propagated to the tenant entity | [optional] |
| **propagate_relation_types** | **List[str]** | JSON array of relation types that should be used for propagation. By default, 'propagateRelationTypes' array is empty which means that the alarm will be propagated based on any relation type to parent entities. This parameter should be used only in case when 'propagate' parameter is set to true, otherwise, 'propagateRelationTypes' array will be ignored. | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DeviceProfileAlarm.model_validate(data)` or `DeviceProfileAlarm.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

