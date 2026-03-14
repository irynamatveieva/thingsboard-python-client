
# DefaultDashboardParams

`tb_pe_client.models.DefaultDashboardParams`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | Default dashboard Id to assign for the new user. | [optional] |
| **fullscreen** | **bool** | Set default dashboard to full screen mode. | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DefaultDashboardParams.model_validate(data)` or `DefaultDashboardParams.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

