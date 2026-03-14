
# DomainInfo

`tb_pe_client.models.DomainInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**DomainId**](DomainId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id | [optional] |
| **customer_id** | [**CustomerId**](CustomerId.md) | JSON object with Customer Id | [optional] |
| **name** | **str** | Domain name. Cannot be empty | |
| **oauth2_enabled** | **bool** | Whether OAuth2 settings are enabled or not | [optional] |
| **propagate_to_edge** | **bool** | Whether OAuth2 settings are enabled on Edge or not | [optional] |
| **oauth2_client_infos** | [**List[OAuth2ClientInfo]**](OAuth2ClientInfo.md) | List of available oauth2 clients | [optional] |
| **owner_id** | [**EntityId**](EntityId.md) | JSON object with Customer or Tenant Id | [optional] [readonly] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DomainInfo.model_validate(data)` or `DomainInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

