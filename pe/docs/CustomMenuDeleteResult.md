
# CustomMenuDeleteResult

`tb_pe_client.models.CustomMenuDeleteResult`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **success** | **bool** |  | [optional] |
| **assignee_type** | [**CMAssigneeType**](CMAssigneeType.md) |  | [optional] |
| **assignee_list** | [**List[EntityInfo]**](EntityInfo.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.success`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CustomMenuDeleteResult.model_validate(data)` or `CustomMenuDeleteResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

