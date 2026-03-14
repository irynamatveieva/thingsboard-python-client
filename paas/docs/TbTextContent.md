
# TbTextContent

`tb_paas_client.models.TbTextContent`

Text-based content part of a user's prompt

**Extends:** **TbContent**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **text** | **str** | The text content | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.text`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TbTextContent.model_validate(data)` or `TbTextContent.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

