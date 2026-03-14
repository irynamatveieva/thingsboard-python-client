# DashboardReportControllerApi

`ThingsboardClient` methods:

```python
bytearray client.download_dashboard_report(dashboard_id: str, body: object)  # Download dashboard report (downloadDashboardReport)
bytearray client.download_test_report(dashboard_report_config: DashboardReportConfig, reports_server_endpoint_url: Optional[str] = None)  # Download test report (downloadTestReport)
```


## download_dashboard_report

```python
bytearray client.download_dashboard_report(dashboard_id: str, body: object)
```

**POST** `/api/report/{dashboardId}/download`

Download dashboard report (downloadDashboardReport)

Generate and download a report from the specified dashboard. The request payload is a JSON object with params of report. For example:  ```json {     \"type\": \"pdf\",     \"timezone\": \"Europe/Kiev\",     \"timewindow\": {         \"displayValue\": \"\",         \"hideInterval\": false,         \"hideLastInterval\": false,         \"hideQuickInterval\": false,         \"hideAggregation\": false,         \"hideAggInterval\": false,         \"hideTimezone\": false,         \"selectedTab\": 0,         \"realtime\": {             \"realtimeType\": 0,             \"interval\": 1000,             \"timewindowMs\": 60000,             \"quickInterval\": \"CURRENT_DAY\"         },         \"history\": {             \"historyType\": 0,             \"interval\": 1000,             \"timewindowMs\": 60000,             \"fixedTimewindow\": {                 \"startTimeMs\": 1703687976592,                 \"endTimeMs\": 1703774376592             },             \"quickInterval\": \"CURRENT_DAY\"         },         \"aggregation\": {             \"type\": \"AVG\",             \"limit\": 25000         }     },     \"state\": null } ```   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **dashboard_id** | **str** | A string value representing the dashboard id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **body** | **object** |  | |

### Return type

**bytearray**


## download_test_report

```python
bytearray client.download_test_report(dashboard_report_config: DashboardReportConfig, reports_server_endpoint_url: Optional[str] = None)
```

**POST** `/api/report/test`

Download test report (downloadTestReport)

Generate and download test report.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **dashboard_report_config** | **DashboardReportConfig** |  | |
| **reports_server_endpoint_url** | **str** | A string value representing the report server endpoint. | [optional] |

### Return type

**bytearray**

