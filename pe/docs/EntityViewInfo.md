
# EntityViewInfo

`tb_pe_client.models.EntityViewInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**EntityViewId**](EntityViewId.md) | JSON object with the Entity View Id. Specify this field to update the Entity View. Referencing non-existing Entity View Id will cause error. Omit this field to create new Entity View. | [optional] |
| **created_time** | **int** | Timestamp of the Entity View creation, in milliseconds | [optional] [readonly] |
| **additional_info** | **object** | Additional parameters of the entity view. May include: 'description' (string). | [optional] |
| **entity_id** | [**EntityId**](EntityId.md) | JSON object with the referenced Entity Id (Device or Asset). | |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id. | [optional] [readonly] |
| **customer_id** | [**CustomerId**](CustomerId.md) | JSON object with Customer Id. Use 'assignEntityViewToCustomer' to change the Customer Id. | [optional] [readonly] |
| **name** | **str** | Entity View name | |
| **type** | **str** | Device Profile Name | |
| **keys** | [**TelemetryEntityView**](TelemetryEntityView.md) | Set of telemetry and attribute keys to expose via Entity View. | [optional] |
| **start_time_ms** | **int** | Represents the start time of the interval that is used to limit access to target device telemetry. Customer will not be able to see entity telemetry that is outside the specified interval; | [optional] |
| **end_time_ms** | **int** | Represents the end time of the interval that is used to limit access to target device telemetry. Customer will not be able to see entity telemetry that is outside the specified interval; | [optional] |
| **version** | **int** |  | [optional] |
| **owner_name** | **str** | Owner name | [optional] [readonly] |
| **groups** | [**List[EntityInfo]**](EntityInfo.md) | Groups | [optional] |
| **owner_id** | [**EntityId**](EntityId.md) | JSON object with Customer or Tenant Id | [optional] [readonly] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityViewInfo.model_validate(data)` or `EntityViewInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

