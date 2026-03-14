
# CustomMobilePage

`tb_paas_client.models.CustomMobilePage`

**Extends:** **MobilePage**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **label** | **str** | Page label | [optional] |
| **icon** | **str** | URL of the page icon | [optional] |
| **path** | **str** | Path to custom page | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.label`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CustomMobilePage.model_validate(data)` or `CustomMobilePage.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

