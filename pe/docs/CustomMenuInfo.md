
# CustomMenuInfo

`tb_pe_client.models.CustomMenuInfo`

A JSON value representing the custom menu basic info fields

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**CustomMenuId**](CustomMenuId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id that owns the menu. | [optional] [readonly] |
| **customer_id** | [**CustomerId**](CustomerId.md) | JSON object with Customer Id that owns the menu. | [optional] [readonly] |
| **name** | **str** | Custom menu name | |
| **scope** | [**CMScope**](CMScope.md) | Custom menu scope. Possible values: SYSTEM, TENANT, CUSTOMER | |
| **assignee_type** | [**CMAssigneeType**](CMAssigneeType.md) | Custom menu assignee type. Possible values are: All (all users of specified scope), CUSTOMERS (specified customers), USERS (specified list of users), NO_ASSIGN (no assignees), USER_GROUPS (user groups) | |
| **user_group_names** | **List[str]** | User group names menu is applied to | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CustomMenuInfo.model_validate(data)` or `CustomMenuInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

