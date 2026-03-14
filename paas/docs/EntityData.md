
# EntityData

`tb_paas_client.models.EntityData`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entity_id** | [**EntityId**](EntityId.md) |  | [optional] |
| **read_attrs** | **bool** |  | [optional] |
| **read_ts** | **bool** |  | [optional] |
| **latest** | **Dict[str, Dict[str, TsValue]]** |  | [optional] |
| **timeseries** | **Dict[str, List[TsValue]]** |  | [optional] |
| **agg_latest** | [**Dict[str, ComparisonTsValue]**](ComparisonTsValue.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.entity_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityData.model_validate(data)` or `EntityData.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

