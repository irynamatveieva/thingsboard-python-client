
# ObjectAttributes

`tb_paas_client.models.ObjectAttributes`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **dim** | **int** |  | [optional] |
| **ssid** | **int** |  | [optional] |
| **uri** | **str** |  | [optional] |
| **ver** | **object** |  | [optional] |
| **lwm2m** | [**LwM2mVersion**](LwM2mVersion.md) |  | [optional] |
| **pmin** | **int** |  | [optional] |
| **pmax** | **int** |  | [optional] |
| **gt** | **float** |  | [optional] |
| **lt** | **float** |  | [optional] |
| **st** | **float** |  | [optional] |
| **epmin** | **int** |  | [optional] |
| **epmax** | **int** |  | [optional] |



## Referenced Types

#### LwM2mVersion
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| supported | bool |  | [optional] |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.dim`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ObjectAttributes.model_validate(data)` or `ObjectAttributes.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

