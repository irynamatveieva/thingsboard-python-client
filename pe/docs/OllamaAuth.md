
# OllamaAuth

`tb_pe_client.models.OllamaAuth`

Ollama authentication schemes

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | **str** |  | |



## Subtypes

#### Basic  *(type=`BASIC`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| username | str |  |  |
| password | str |  |  |

#### ModelNone  *(type=`NONE`)*
*(no additional properties)*

#### Token  *(type=`TOKEN`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| token | str |  |  |

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `OllamaAuth.model_validate(data)` or `OllamaAuth.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

