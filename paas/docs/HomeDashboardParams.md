
# HomeDashboardParams

`tb_paas_client.models.HomeDashboardParams`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | Home dashboard Id to assign for the new user. | [optional] |
| **hide_toolbar** | **bool** | Indicates if hide toolbar should be hidden. | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `HomeDashboardParams.model_validate(data)` or `HomeDashboardParams.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

