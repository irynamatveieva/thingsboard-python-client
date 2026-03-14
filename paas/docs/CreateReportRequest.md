
# CreateReportRequest

`tb_paas_client.models.CreateReportRequest`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **file** | **bytearray** |  | |
| **info** | **str** |  | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.file`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CreateReportRequest.model_validate(data)` or `CreateReportRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

