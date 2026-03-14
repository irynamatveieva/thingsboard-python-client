
# DashboardPage

`tb_paas_client.models.DashboardPage`

**Extends:** **MobilePage**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **label** | **str** | Page label | [optional] |
| **icon** | **str** | URL of the page icon | [optional] |
| **dashboard_id** | **str** | Dashboard id | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.label`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DashboardPage.model_validate(data)` or `DashboardPage.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

