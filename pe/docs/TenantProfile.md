
# TenantProfile

`tb_pe_client.models.TenantProfile`

A JSON value representing the tenant profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**TenantProfileId**](TenantProfileId.md) | JSON object with the tenant profile Id. Specify this field to update the tenant profile. Referencing non-existing tenant profile Id will cause error. Omit this field to create new tenant profile. | [optional] |
| **created_time** | **int** | Timestamp of the tenant profile creation, in milliseconds | [optional] [readonly] |
| **name** | **str** | Name of the tenant profile | [optional] |
| **description** | **str** | Description of the tenant profile | [optional] |
| **isolated_tb_rule_engine** | **bool** | If enabled, will push all messages related to this tenant and processed by the rule engine into separate queue. Useful for complex microservices deployments, to isolate processing of the data for specific tenants | [optional] |
| **default** | **bool** | Default Tenant profile to be used. | [optional] |
| **profile_data** | [**TenantProfileData**](TenantProfileData.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TenantProfile.model_validate(data)` or `TenantProfile.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

