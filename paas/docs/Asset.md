
# Asset

`tb_paas_client.models.Asset`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**AssetId**](AssetId.md) | JSON object with the asset Id. Specify this field to update the asset. Referencing non-existing asset Id will cause error. Omit this field to create new asset. | [optional] |
| **created_time** | **int** | Timestamp of the asset creation, in milliseconds | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id. | [optional] [readonly] |
| **customer_id** | [**CustomerId**](CustomerId.md) | JSON object with Customer Id. Use 'assignAssetToCustomer' to change the Customer Id. | [optional] [readonly] |
| **name** | **str** | Unique Asset Name in scope of Tenant | |
| **type** | **str** | Asset type | [optional] |
| **label** | **str** | Label that may be used in widgets | [optional] |
| **asset_profile_id** | [**AssetProfileId**](AssetProfileId.md) | JSON object with Asset Profile Id. | [optional] |
| **version** | **int** |  | [optional] |
| **owner_id** | [**EntityId**](EntityId.md) | JSON object with Customer or Tenant Id | [optional] [readonly] |
| **additional_info** | **object** | Additional parameters of the asset. May include: 'description' (string). | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Asset.model_validate(data)` or `Asset.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

