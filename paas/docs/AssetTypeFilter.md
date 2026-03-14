
# AssetTypeFilter

`tb_paas_client.models.AssetTypeFilter`

**Extends:** **EntityFilter**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **asset_types** | **List[str]** |  | [optional] |
| **asset_name_filter** | **str** |  | [optional] |
| **asset_type** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.asset_types`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AssetTypeFilter.model_validate(data)` or `AssetTypeFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

