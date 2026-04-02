
# TimeSeriesOutput

`tb_paas_client.models.TimeSeriesOutput`

**Extends:** **Output**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **strategy** | [**TimeSeriesOutputStrategy**](TimeSeriesOutputStrategy.md) |  | [optional] |



## Referenced Types

#### Output
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| name | str |  | [optional] |
| scope | AttributeScope |  | [optional] |
| decimals_by_default | int |  | [optional] |
| strategy | object |  | [optional] |
| type | str |  |  |

#### TimeSeriesOutputStrategy
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AttributeScope (enum)
`CLIENT_SCOPE` | `SERVER_SCOPE` | `SHARED_SCOPE`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.strategy`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TimeSeriesOutput.model_validate(data)` or `TimeSeriesOutput.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

