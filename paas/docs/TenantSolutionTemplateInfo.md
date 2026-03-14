
# TenantSolutionTemplateInfo

`tb_paas_client.models.TenantSolutionTemplateInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | ID of the solution template | [optional] |
| **title** | **str** | Template Title | [optional] |
| **level** | [**SolutionTemplateLevel**](SolutionTemplateLevel.md) | Level of the subscription that is required to unlock the template | [optional] |
| **install_timeout_ms** | **int** | Timeout for the installation UI to wait while template is installing | [optional] |
| **tenant_telemetry_keys** | **List[str]** | What keys to delete during template uninstall | [optional] |
| **tenant_attribute_keys** | **List[str]** | What attributes to delete during template uninstall | [optional] |
| **preview_image_url** | **str** | URL of the preview image | [optional] |
| **video_preview_image_url** | **str** | Video preview image URL | [optional] |
| **preview_mp4_url** | **str** | Video MP4 URL | [optional] |
| **preview_webm_url** | **str** | Video WEBM URL | [optional] |
| **installed** | **bool** | Indicates that template is already installed for the current tenant | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TenantSolutionTemplateInfo.model_validate(data)` or `TenantSolutionTemplateInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

