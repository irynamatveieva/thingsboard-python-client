
# LwM2mObject

`tb_ce_client.models.LwM2mObject`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | **int** | LwM2M Object id. | [optional] |
| **key_id** | **str** | LwM2M Object key id. | [optional] |
| **name** | **str** | LwM2M Object name. | [optional] |
| **multiple** | **bool** | LwM2M Object multiple. | [optional] |
| **mandatory** | **bool** | LwM2M Object mandatory. | [optional] |
| **instances** | [**List[LwM2mInstance]**](LwM2mInstance.md) | LwM2M Object instances. | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `LwM2mObject.model_validate(data)` or `LwM2mObject.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

