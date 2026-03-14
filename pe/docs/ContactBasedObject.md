
# ContactBasedObject

`tb_pe_client.models.ContactBasedObject`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | **object** |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **country** | **str** |  | [optional] |
| **state** | **str** |  | [optional] |
| **city** | **str** |  | [optional] |
| **address** | **str** |  | [optional] |
| **address2** | **str** |  | [optional] |
| **zip** | **str** |  | [optional] |
| **phone** | **str** |  | [optional] |
| **email** | **str** |  | [optional] |
| **name** | **str** |  | [optional] |
| **additional_info** | **object** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ContactBasedObject.model_validate(data)` or `ContactBasedObject.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

