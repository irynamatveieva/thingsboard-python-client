
# CustomerUsersFilter

`tb_pe_client.models.CustomerUsersFilter`

**Extends:** **UsersFilter**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **customer_id** | **UUID** |  | |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.customer_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CustomerUsersFilter.model_validate(data)` or `CustomerUsersFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

