
# ComponentDescriptor

`tb_ce_client.models.ComponentDescriptor`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**ComponentDescriptorId**](ComponentDescriptorId.md) | JSON object with the descriptor Id. Specify existing descriptor id to update the descriptor. Referencing non-existing descriptor Id will cause error. Omit this field to create new descriptor. | [optional] |
| **created_time** | **int** | Timestamp of the descriptor creation, in milliseconds | [optional] [readonly] |
| **type** | [**ComponentType**](ComponentType.md) | Type of the Rule Node | [optional] [readonly] |
| **scope** | [**ComponentScope**](ComponentScope.md) | Scope of the Rule Node. Always set to 'TENANT', since no rule chains on the 'SYSTEM' level yet. | [optional] [readonly] |
| **clustering_mode** | [**ComponentClusteringMode**](ComponentClusteringMode.md) | Clustering mode of the RuleNode. This mode represents the ability to start Rule Node in multiple microservices. | [optional] [readonly] |
| **name** | **str** | Name of the Rule Node. Taken from the @RuleNode annotation. | [optional] [readonly] |
| **clazz** | **str** | Full name of the Java class that implements the Rule Engine Node interface. | [optional] [readonly] |
| **configuration_version** | **int** | Rule node configuration version. By default, this value is 0. If the rule node is a versioned node, this value might be greater than 0. | [optional] [readonly] |
| **actions** | **str** | Rule Node Actions. Deprecated. Always null. | [optional] [readonly] |
| **has_queue_name** | **bool** | Indicates that the RuleNode supports queue name configuration. | [optional] [readonly] |
| **configuration_descriptor** | **object** |  | [optional] |



## Referenced Types

#### ComponentDescriptorId
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | UUID | string |  |

#### ComponentType (enum)
`ENRICHMENT` | `FILTER` | `TRANSFORMATION` | `ACTION` | `EXTERNAL` | `FLOW`

#### ComponentScope (enum)
`SYSTEM` | `TENANT`

#### ComponentClusteringMode (enum)
`USER_PREFERENCE` | `ENABLED` | `SINGLETON`

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ComponentDescriptor.model_validate(data)` or `ComponentDescriptor.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

