
# GeofencingCalculatedFieldConfiguration

`tb_paas_client.models.GeofencingCalculatedFieldConfiguration`

**Extends:** **CalculatedFieldConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entity_coordinates** | [**EntityCoordinates**](EntityCoordinates.md) |  | |
| **scheduled_update_enabled** | **bool** |  | [optional] |
| **scheduled_update_interval** | **int** |  | [optional] |
| **zone_groups** | [**Dict[str, ZoneGroupConfiguration]**](ZoneGroupConfiguration.md) |  | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.entity_coordinates`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `GeofencingCalculatedFieldConfiguration.model_validate(data)` or `GeofencingCalculatedFieldConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

