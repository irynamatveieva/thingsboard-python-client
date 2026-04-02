
# PageDataContactBasedObject

`tb_paas_client.models.PageDataContactBasedObject`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data** | [**List[ContactBasedObject]**](ContactBasedObject.md) | Array of the entities | [optional] |
| **has_next** | **bool** | 'false' value indicates the end of the result set | [optional] [readonly] |
| **total_elements** | **int** | Total number of elements in all available pages | [optional] [readonly] |
| **total_pages** | **int** | Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria | [optional] [readonly] |



## Referenced Types

#### ContactBasedObject
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | object |  | [optional] |
| created_time | int | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| additional_info | object |  | [optional] |
| country | str |  | [optional] |
| state | str |  | [optional] |
| city | str |  | [optional] |
| address | str |  | [optional] |
| address2 | str |  | [optional] |
| zip | str |  | [optional] |
| phone | str |  | [optional] |
| email | str |  | [optional] |
| name | str |  | [optional] |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageDataContactBasedObject.model_validate(data)` or `PageDataContactBasedObject.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

