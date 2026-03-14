
# StoreInfo

`tb_pe_client.models.StoreInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **app_id** | **str** |  | [optional] |
| **sha256_cert_fingerprints** | **str** |  | [optional] |
| **store_link** | **str** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.app_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `StoreInfo.model_validate(data)` or `StoreInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

