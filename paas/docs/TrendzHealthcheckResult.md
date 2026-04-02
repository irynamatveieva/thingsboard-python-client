
# TrendzHealthcheckResult

`tb_paas_client.models.TrendzHealthcheckResult`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **version** | **str** |  | [optional] |
| **type** | [**TrendzSynchronizationResultType**](TrendzSynchronizationResultType.md) |  | [optional] |
| **status** | [**TrendzSynchronizationStatus**](TrendzSynchronizationStatus.md) |  | [optional] |
| **message** | **str** |  | [optional] |



## Referenced Types

#### TrendzSynchronizationResultType (enum)
`SYNC_NOT_INITIALIZED` | `SYNC_COMPLETED` | `SYNC_DISABLED` | `TRENDZ_UNSUPPORTED_VERSION` | `TRENDZ_AUTH_INVALID` | `TRENDZ_URL_UNREACHABLE` | `TB_URL_MISMATCH` | `TB_URL_UNREACHABLE` | `TB_AUTH_INVALID` | `SYNC_INTERNAL_ERROR`

#### TrendzSynchronizationStatus (enum)
`NOT_AVAILABLE` | `AVAILABLE` | `SYNCED`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.version`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TrendzHealthcheckResult.model_validate(data)` or `TrendzHealthcheckResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

