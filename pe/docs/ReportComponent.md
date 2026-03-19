
# ReportComponent

`tb_pe_client.models.ReportComponent`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **sub_type** | [**ReportComponentSubType**](ReportComponentSubType.md) |  | |
| **type** | [**ReportComponentType**](ReportComponentType.md) |  | |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.sub_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ReportComponent.model_validate(data)` or `ReportComponent.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

