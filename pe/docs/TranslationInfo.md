
# TranslationInfo

`tb_pe_client.models.TranslationInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **locale_code** | **str** | Locale code formed by combining the ISO 639-1 language code and the ISO 3166-1 region code. For example, \"en_US\" | [optional] |
| **language** | **str** | Locale code language display name. For example, \"Polish (Polski)\" | [optional] |
| **country** | **str** | Locale code country display name. For example, \"Poland\" | [optional] |
| **progress** | **int** | Number representing translation percentage progress. For example, 40 that means 40% of all keys are translated. | [optional] |
| **customized** | **bool** | Boolean representing if current language has customization. | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.locale_code`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TranslationInfo.model_validate(data)` or `TranslationInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

