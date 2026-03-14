
# UpdateMessage

`tb_pe_client.models.UpdateMessage`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **update_available** | **bool** | 'True' if new platform update is available. | [optional] |
| **current_version** | **str** | Current ThingsBoard version. | [optional] |
| **latest_version** | **str** | Latest ThingsBoard version. | [optional] |
| **upgrade_instructions_url** | **str** | Upgrade instructions URL. | [optional] |
| **current_version_release_notes_url** | **str** | Current ThingsBoard version release notes URL. | [optional] |
| **latest_version_release_notes_url** | **str** | Latest ThingsBoard version release notes URL. | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.update_available`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `UpdateMessage.model_validate(data)` or `UpdateMessage.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

