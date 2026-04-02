
# EdqsSyncRequest

`tb_ce_client.models.EdqsSyncRequest`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **object_types** | [**List[ObjectType]**](ObjectType.md) |  | [optional] |



## Referenced Types

#### ObjectType (enum)
`TENANT` | `TENANT_PROFILE` | `CUSTOMER` | `QUEUE` | `RPC` | `RULE_CHAIN` | `OTA_PACKAGE` | `RESOURCE` | `EVENT` | `RULE_NODE` | … (37 values total)

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.object_types`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EdqsSyncRequest.model_validate(data)` or `EdqsSyncRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

