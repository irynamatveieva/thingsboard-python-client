
# Customer

`tb_ce_client.models.Customer`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**CustomerId**](CustomerId.md) | JSON object with the customer Id. Specify this field to update the customer. Referencing non-existing customer Id will cause error. Omit this field to create new customer. | [optional] |
| **created_time** | **int** | Timestamp of the customer creation, in milliseconds | [optional] [readonly] |
| **country** | **str** | Country | [optional] |
| **state** | **str** | State | [optional] |
| **city** | **str** | City | [optional] |
| **address** | **str** | Address Line 1 | [optional] |
| **address2** | **str** | Address Line 2 | [optional] |
| **zip** | **str** | Zip code | [optional] |
| **phone** | **str** | Phone number | [optional] |
| **email** | **str** | Email | |
| **title** | **str** | Title of the customer | |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id | [optional] |
| **version** | **int** |  | [optional] |
| **name** | **str** | Name of the customer. Read-only, duplicated from title for backward compatibility | [optional] [readonly] |
| **additional_info** | **object** | Additional parameters of the customer. May include: 'description' (string), 'homeDashboardId' (string, UUID of the home dashboard), 'homeDashboardHideToolbar' (boolean, whether to hide the dashboard toolbar), 'isPublic' (boolean, whether this is a public customer). | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Customer.model_validate(data)` or `Customer.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

