
# ResourceExportData

`tb_ce_client.models.ResourceExportData`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **link** | **str** |  | [optional] |
| **title** | **str** |  | [optional] |
| **type** | [**ResourceType**](ResourceType.md) |  | [optional] |
| **sub_type** | [**ResourceSubType**](ResourceSubType.md) |  | [optional] |
| **resource_key** | **str** |  | [optional] |
| **file_name** | **str** |  | [optional] |
| **public_resource_key** | **str** |  | [optional] |
| **media_type** | **str** |  | [optional] |
| **data** | **str** |  | [optional] |
| **is_public** | **bool** |  | [optional] |
| **public** | **bool** |  | [optional] |



## Referenced Types

#### ResourceType (enum)
`LWM2_M_MODEL` | `JKS` | `PKCS_12` | `JS_MODULE` | `IMAGE` | `DASHBOARD` | `GENERAL`

#### ResourceSubType (enum)
`IMAGE` | `SCADA_SYMBOL` | `EXTENSION` | `MODULE`

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.link`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ResourceExportData.model_validate(data)` or `ResourceExportData.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

