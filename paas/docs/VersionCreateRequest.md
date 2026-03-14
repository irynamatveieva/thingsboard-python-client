
# VersionCreateRequest

`tb_paas_client.models.VersionCreateRequest`

Request for creating a version

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **version_name** | **str** |  | [optional] |
| **branch** | **str** |  | [optional] |
| **type** | [**VersionCreateRequestType**](VersionCreateRequestType.md) | Type of the version to create | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.version_name`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `VersionCreateRequest.model_validate(data)` or `VersionCreateRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

