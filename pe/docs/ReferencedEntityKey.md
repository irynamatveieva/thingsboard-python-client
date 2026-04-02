
# ReferencedEntityKey

`tb_pe_client.models.ReferencedEntityKey`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **key** | **str** |  | [optional] |
| **type** | [**ArgumentType**](ArgumentType.md) |  | [optional] |
| **scope** | [**AttributeScope**](AttributeScope.md) |  | [optional] |



## Referenced Types

#### ArgumentType (enum)
`TS_LATEST` | `ATTRIBUTE` | `TS_ROLLING`

#### AttributeScope (enum)
`CLIENT_SCOPE` | `SERVER_SCOPE` | `SHARED_SCOPE`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.key`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ReferencedEntityKey.model_validate(data)` or `ReferencedEntityKey.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

