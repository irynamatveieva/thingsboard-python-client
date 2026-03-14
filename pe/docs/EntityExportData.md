
# EntityExportData

`tb_pe_client.models.EntityExportData`

Base export container for ThingsBoard entities

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entity_type** | [**EntityType**](EntityType.md) |  | |
| **entity** | [**ExportableEntity**](ExportableEntity.md) |  | [optional] |
| **relations** | [**List[EntityRelation]**](EntityRelation.md) |  | [optional] |
| **attributes** | **Dict[str, List[AttributeExportData]]** | Map of attributes where key is the scope of attributes and value is the list of attributes for that scope | [optional] |
| **calculated_fields** | [**List[CalculatedField]**](CalculatedField.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.entity_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityExportData.model_validate(data)` or `EntityExportData.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

