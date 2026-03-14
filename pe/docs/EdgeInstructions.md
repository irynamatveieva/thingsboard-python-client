
# EdgeInstructions

`tb_pe_client.models.EdgeInstructions`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **instructions** | **str** | Markdown with install/upgrade instructions | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.instructions`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EdgeInstructions.model_validate(data)` or `EdgeInstructions.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

