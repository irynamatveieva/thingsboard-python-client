
# AttributesEntityView

`tb_ce_client.models.AttributesEntityView`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **cs** | **List[str]** | List of client-side attribute keys to expose | |
| **ss** | **List[str]** | List of server-side attribute keys to expose | |
| **sh** | **List[str]** | List of shared attribute keys to expose | |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.cs`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AttributesEntityView.model_validate(data)` or `AttributesEntityView.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

