
# VersionLoadRequest

`tb_paas_client.models.VersionLoadRequest`

Request for loading a version

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **version_id** | **str** |  | [optional] |
| **type** | [**VersionLoadRequestType**](VersionLoadRequestType.md) | Type of the version to load | |



## Referenced Types

#### VersionLoadRequestType (enum)
`SINGLE_ENTITY` | `ENTITY_TYPE`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.version_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `VersionLoadRequest.model_validate(data)` or `VersionLoadRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

