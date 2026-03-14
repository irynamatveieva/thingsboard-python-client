
# SystemInfoData

`tb_paas_client.models.SystemInfoData`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **service_id** | **str** | Service Id. | [optional] |
| **service_type** | **str** | Service type. | [optional] |
| **cpu_usage** | **int** | CPU usage, in percent. | [optional] |
| **cpu_count** | **int** | Total CPU usage. | [optional] |
| **memory_usage** | **int** | Memory usage, in percent. | [optional] |
| **total_memory** | **int** | Total memory in bytes. | [optional] |
| **disc_usage** | **int** | Disk usage, in percent. | [optional] |
| **total_disc_space** | **int** | Total disc space in bytes. | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.service_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SystemInfoData.model_validate(data)` or `SystemInfoData.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

