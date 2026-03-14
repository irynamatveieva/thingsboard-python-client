
# ErrorComponent

`tb_paas_client.models.ErrorComponent`

**Extends:** **ReportComponent**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **error_message** | **str** |  | [optional] |
| **exception** | [**ErrorComponentAllOfException**](ErrorComponentAllOfException.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.error_message`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ErrorComponent.model_validate(data)` or `ErrorComponent.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

