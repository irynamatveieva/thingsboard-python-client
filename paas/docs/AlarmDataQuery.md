
# AlarmDataQuery

`tb_paas_client.models.AlarmDataQuery`

A JSON value representing the alarm data query. See API call notes above for more details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entity_filter** | [**EntityFilter**](EntityFilter.md) |  | [optional] |
| **key_filters** | [**List[KeyFilter]**](KeyFilter.md) |  | [optional] |
| **page_link** | [**AlarmDataPageLink**](AlarmDataPageLink.md) |  | [optional] |
| **entity_fields** | [**List[EntityKey]**](EntityKey.md) |  | [optional] |
| **latest_values** | [**List[EntityKey]**](EntityKey.md) |  | [optional] |
| **alarm_fields** | [**List[EntityKey]**](EntityKey.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.entity_filter`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmDataQuery.model_validate(data)` or `AlarmDataQuery.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

