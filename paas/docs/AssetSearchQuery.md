
# AssetSearchQuery

`tb_paas_client.models.AssetSearchQuery`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **parameters** | [**RelationsSearchParameters**](RelationsSearchParameters.md) | Main search parameters. | [optional] |
| **relation_type** | **str** | Type of the relation between root entity and asset (e.g. 'Contains' or 'Manages'). | [optional] |
| **asset_types** | **List[str]** | Array of asset types to filter the related entities (e.g. 'Building', 'Vehicle'). | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.parameters`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AssetSearchQuery.model_validate(data)` or `AssetSearchQuery.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

