
# WidgetBundleInfo

`tb_ce_client.models.WidgetBundleInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**EntityId**](EntityId.md) | JSON object with the entity Id.  | [optional] |
| **name** | **str** | Entity Name | [optional] |



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `WidgetBundleInfo.model_validate(data)` or `WidgetBundleInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

