
# Mapping

`tb_paas_client.models.Mapping`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **columns** | [**List[ColumnMapping]**](ColumnMapping.md) |  | [optional] |
| **delimiter** | **str** |  | [optional] |
| **update** | **bool** |  | [optional] |
| **header** | **bool** |  | [optional] |



## Referenced Types

#### ColumnMapping
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | BulkImportColumnType |  | [optional] |
| key | str |  | [optional] |

#### BulkImportColumnType (enum)
`NAME` | `TYPE` | `LABEL` | `SHARED_ATTRIBUTE` | `SERVER_ATTRIBUTE` | `TIMESERIES` | `ACCESS_TOKEN` | `X509` | `MQTT_CLIENT_ID` | `MQTT_USER_NAME` | … (32 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.columns`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Mapping.model_validate(data)` or `Mapping.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

