
# TenantSolutionTemplateInstructions

`tb_pe_client.models.TenantSolutionTemplateInstructions`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **dashboard_group_id** | [**EntityGroupId**](EntityGroupId.md) | Id of the group that contains main dashboard of the solution | [optional] |
| **dashboard_id** | [**DashboardId**](DashboardId.md) | Id of the main dashboard of the solution | [optional] |
| **public_id** | [**CustomerId**](CustomerId.md) | Id of the public customer if solution has public entities | [optional] |
| **main_dashboard_public** | **bool** | Is the main dashboard public | [optional] |
| **details** | **str** | Markdown with solution usage instructions | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.dashboard_group_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TenantSolutionTemplateInstructions.model_validate(data)` or `TenantSolutionTemplateInstructions.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

