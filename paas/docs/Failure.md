
# Failure

`tb_paas_client.models.Failure`

**Extends:** **TbChatResponse**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **error_details** | **str** | A string containing details about the failure | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.error_details`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Failure.model_validate(data)` or `Failure.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

