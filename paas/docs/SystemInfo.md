
# SystemInfo

`tb_paas_client.models.SystemInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **monolith** | **bool** | Is monolith. | [optional] |
| **system_data** | [**List[SystemInfoData]**](SystemInfoData.md) | System data. | [optional] |



## Referenced Types

#### SystemInfoData
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| service_id | str | Service Id. | [optional] |
| service_type | str | Service type. | [optional] |
| cpu_usage | int | CPU usage, in percent. | [optional] |
| cpu_count | int | Total CPU usage. | [optional] |
| memory_usage | int | Memory usage, in percent. | [optional] |
| total_memory | int | Total memory in bytes. | [optional] |
| disc_usage | int | Disk usage, in percent. | [optional] |
| total_disc_space | int | Total disc space in bytes. | [optional] |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.monolith`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SystemInfo.model_validate(data)` or `SystemInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

