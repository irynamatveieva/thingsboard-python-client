
# DashboardReportConfig

`tb_pe_client.models.DashboardReportConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **base_url** | **str** | Base URL of ThingsBoard UI that should be accessible by Web Report Server. | |
| **dashboard_id** | **str** | A string value representing the dashboard id. | |
| **state** | **str** | Target dashboard state for dashboard report generation. | [optional] |
| **timezone** | **str** | Timezone in which target dashboard will be presented in dashboard report. | |
| **use_dashboard_timewindow** | **bool** | If set, timewindow configured in the target dashboard will be used during dashboard report generation. | [optional] |
| **timewindow** | **object** | Specific dashboard timewindow that will be used during dashboard report generation. | [optional] |
| **name_pattern** | **str** | If set, timewindow configured in the target dashboard will be used during dashboard report generation. | |
| **type** | **str** | Dashboard report file type, can be PDF | PNG | JPEG. | [optional] |
| **use_current_user_credentials** | **bool** | If set, credentials of user created this dashboard report configuration will be used to open dashboard UI during dashboard report generation. | [optional] |
| **user_id** | **str** | A string value representing the user id. | |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.base_url`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DashboardReportConfig.model_validate(data)` or `DashboardReportConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

