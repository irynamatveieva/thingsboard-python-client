
# Heading

`tb_pe_client.models.Heading`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **text** | **str** |  | [optional] |
| **font** | [**Font**](Font.md) |  | [optional] |
| **color** | **str** |  | [optional] |
| **text_alignment** | [**TextAlignment**](TextAlignment.md) |  | [optional] |
| **vertical_alignment** | [**VerticalAlignment**](VerticalAlignment.md) |  | [optional] |
| **height** | **int** |  | [optional] |



## Referenced Types

#### Font
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| size | float |  | [optional] |
| weight | FontWeight |  | [optional] |
| style | FontStyle |  | [optional] |
| family | str |  | [optional] |

#### TextAlignment (enum)
`CENTER` | `RIGHT` | `LEFT` | `JUSTIFY`

#### VerticalAlignment (enum)
`BOTTOM` | `TOP` | `MIDDLE`

#### FontWeight (enum)
`NORMAL` | `BOLD` | `ENUM_500`

#### FontStyle (enum)
`NORMAL` | `ITALIC`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.text`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Heading.model_validate(data)` or `Heading.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

