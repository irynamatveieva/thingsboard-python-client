
# RepositorySettings

`tb_ce_client.models.RepositorySettings`

A JSON value representing the Repository Settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **repository_uri** | **str** |  | [optional] |
| **auth_method** | [**RepositoryAuthMethod**](RepositoryAuthMethod.md) |  | [optional] |
| **username** | **str** |  | [optional] |
| **password** | **str** |  | [optional] |
| **private_key_file_name** | **str** |  | [optional] |
| **private_key** | **str** |  | [optional] |
| **private_key_password** | **str** |  | [optional] |
| **default_branch** | **str** |  | [optional] |
| **read_only** | **bool** |  | [optional] |
| **show_merge_commits** | **bool** |  | [optional] |
| **local_only** | **bool** |  | [optional] |



## Referenced Types

#### RepositoryAuthMethod (enum)
`USERNAME_PASSWORD` | `PRIVATE_KEY`

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.repository_uri`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RepositorySettings.model_validate(data)` or `RepositorySettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

