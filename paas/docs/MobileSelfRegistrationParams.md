
# MobileSelfRegistrationParams

`tb_paas_client.models.MobileSelfRegistrationParams`

**Extends:** **SelfRegistrationParams**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **privacy_policy** | **str** | Privacy policy text. Supports HTML. | [optional] |
| **redirect** | [**MobileRedirectParams**](MobileRedirectParams.md) | Mobile redirect params. | |
| **terms_of_use** | **str** | Terms of User text. Supports HTML. | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.privacy_policy`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `MobileSelfRegistrationParams.model_validate(data)` or `MobileSelfRegistrationParams.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

