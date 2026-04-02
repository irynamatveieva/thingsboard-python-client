
# BulkImportRequest

`tb_ce_client.models.BulkImportRequest`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **file** | **str** |  | [optional] |
| **mapping** | [**Mapping**](Mapping.md) |  | [optional] |



## Referenced Types

#### Mapping
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| columns | List[ColumnMapping] |  | [optional] |
| delimiter | str |  | [optional] |
| update | bool |  | [optional] |
| header | bool |  | [optional] |

#### ColumnMapping
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | BulkImportColumnType |  | [optional] |
| key | str |  | [optional] |

#### BulkImportColumnType (enum)
`NAME` | `TYPE` | `LABEL` | `SHARED_ATTRIBUTE` | `SERVER_ATTRIBUTE` | `TIMESERIES` | `ACCESS_TOKEN` | `X509` | `MQTT_CLIENT_ID` | `MQTT_USER_NAME` | … (30 values total)

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.file`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `BulkImportRequest.model_validate(data)` or `BulkImportRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

