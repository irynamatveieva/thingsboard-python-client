
# DefaultMobilePage

`tb_paas_client.models.DefaultMobilePage`

**Extends:** **MobilePage**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **label** | **str** | Page label | [optional] |
| **icon** | **str** | URL of the page icon | [optional] |
| **id** | [**DefaultPageId**](DefaultPageId.md) | Identifier for default page | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.label`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DefaultMobilePage.model_validate(data)` or `DefaultMobilePage.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

