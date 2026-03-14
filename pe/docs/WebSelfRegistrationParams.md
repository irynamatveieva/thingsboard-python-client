
# WebSelfRegistrationParams

`tb_pe_client.models.WebSelfRegistrationParams`

**Extends:** **SelfRegistrationParams**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **domain_id** | [**DomainId**](DomainId.md) | Domain name for self registration URL. Typically this matches the domain name from the Login White Labeling page. | |
| **privacy_policy** | **str** | Privacy policy text. Supports HTML. | [optional] |
| **terms_of_use** | **str** | Terms of User text. Supports HTML. | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.domain_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `WebSelfRegistrationParams.model_validate(data)` or `WebSelfRegistrationParams.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

