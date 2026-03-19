
# WidgetTypeDetails

`tb_ce_client.models.WidgetTypeDetails`

A JSON value representing the Widget Type Details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**WidgetTypeId**](WidgetTypeId.md) | JSON object with the Widget Type Id. Specify this field to update the Widget Type. Referencing non-existing Widget Type Id will cause error. Omit this field to create new Widget Type. | [optional] |
| **created_time** | **int** | Timestamp of the Widget Type creation, in milliseconds | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id. | [optional] [readonly] |
| **fqn** | **str** | Unique FQN that is used in dashboards as a reference widget type | [optional] [readonly] |
| **name** | **str** | Widget name used in search and UI | [optional] [readonly] |
| **deprecated** | **bool** | Whether widget type is deprecated. | [optional] |
| **scada** | **bool** | Whether widget type is SCADA symbol. | [optional] |
| **version** | **int** |  | [optional] |
| **descriptor** | **object** | Complex JSON object that describes the widget type | [optional] [readonly] |
| **image** | **str** | Relative or external image URL. Replaced with image data URL (Base64) in case of relative URL and 'inlineImages' option enabled. | [optional] |
| **description** | **str** | Description of the widget | [optional] |
| **tags** | **List[str]** | Tags of the widget type | [optional] |
| **resources** | [**List[ResourceExportData]**](ResourceExportData.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `WidgetTypeDetails.model_validate(data)` or `WidgetTypeDetails.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

