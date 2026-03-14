
# TbResource

`tb_ce_client.models.TbResource`

A JSON value representing the Resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**TbResourceId**](TbResourceId.md) | JSON object with the Resource Id. Specify this field to update the Resource. Referencing non-existing Resource Id will cause error. Omit this field to create new Resource. | [optional] |
| **created_time** | **int** | Timestamp of the resource creation, in milliseconds | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id. Tenant Id of the resource can't be changed. | [optional] [readonly] |
| **title** | **str** | Resource title. | [optional] |
| **resource_type** | [**ResourceType**](ResourceType.md) | Resource type. | [optional] |
| **resource_sub_type** | [**ResourceSubType**](ResourceSubType.md) | Resource sub type. | [optional] |
| **resource_key** | **str** | Resource key. | [optional] |
| **public_resource_key** | **str** | Public resource key. | [optional] |
| **etag** | **str** | Resource etag. | [optional] [readonly] |
| **file_name** | **str** | Resource file name. | [optional] |
| **descriptor** | **object** | Resource descriptor. | [optional] |
| **data** | **str** | Resource data. | [optional] |
| **preview** | **str** |  | [optional] |
| **name** | **str** |  | [optional] [readonly] |
| **public** | **bool** |  | [optional] |
| **link** | **str** |  | [optional] [readonly] |
| **public_link** | **str** |  | [optional] [readonly] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TbResource.model_validate(data)` or `TbResource.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

