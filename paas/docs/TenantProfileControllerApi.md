# TenantProfileControllerApi

`ThingsboardClient` methods:

```python
None client.delete_tenant_profile(tenant_profile_id: str)  # Delete Tenant Profile (deleteTenantProfile)
EntityInfo client.get_default_tenant_profile_info()  # Get default Tenant Profile Info (getDefaultTenantProfileInfo)
TenantProfile client.get_tenant_profile_by_id(tenant_profile_id: str)  # Get Tenant Profile (getTenantProfileById)
EntityInfo client.get_tenant_profile_info_by_id(tenant_profile_id: str)  # Get Tenant Profile Info (getTenantProfileInfoById)
PageDataEntityInfo client.get_tenant_profile_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Tenant Profiles Info (getTenantProfileInfos)
List[TenantProfile] client.get_tenant_profile_list(ids: List[str])  # Get Tenant Profile list (getTenantProfileList)
PageDataTenantProfile client.get_tenant_profiles(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Tenant Profiles (getTenantProfiles)
TenantProfile client.save_tenant_profile(tenant_profile: TenantProfile)  # Create Or update Tenant Profile (saveTenantProfile)
TenantProfile client.set_default_tenant_profile(tenant_profile_id: str)  # Make tenant profile default (setDefaultTenantProfile)
```


## delete_tenant_profile

```python
None client.delete_tenant_profile(tenant_profile_id: str)
```

**DELETE** `/api/tenantProfile/{tenantProfileId}`

Delete Tenant Profile (deleteTenantProfile)

Deletes the tenant profile. Referencing non-existing tenant profile Id will cause an error. Referencing profile that is used by the tenants will cause an error.   Available for users with 'SYS_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **tenant_profile_id** | **str** | A string value representing the tenant profile id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## get_default_tenant_profile_info

```python
EntityInfo client.get_default_tenant_profile_info()
```

**GET** `/api/tenantProfileInfo/default`

Get default Tenant Profile Info (getDefaultTenantProfileInfo)

Fetch the default Tenant Profile Info object based. Tenant Profile Info is a lightweight object that contains only id and name of the profile.   Available for users with 'SYS_ADMIN' authority.

### Return type

**EntityInfo**


## get_tenant_profile_by_id

```python
TenantProfile client.get_tenant_profile_by_id(tenant_profile_id: str)
```

**GET** `/api/tenantProfile/{tenantProfileId}`

Get Tenant Profile (getTenantProfileById)

Fetch the Tenant Profile object based on the provided Tenant Profile Id.   Available for users with 'SYS_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **tenant_profile_id** | **str** | A string value representing the tenant profile id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**TenantProfile**


## get_tenant_profile_info_by_id

```python
EntityInfo client.get_tenant_profile_info_by_id(tenant_profile_id: str)
```

**GET** `/api/tenantProfileInfo/{tenantProfileId}`

Get Tenant Profile Info (getTenantProfileInfoById)

Fetch the Tenant Profile Info object based on the provided Tenant Profile Id. Tenant Profile Info is a lightweight object that contains only id and name of the profile.   Available for users with 'SYS_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **tenant_profile_id** | **str** | A string value representing the tenant profile id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**EntityInfo**


## get_tenant_profile_infos

```python
PageDataEntityInfo client.get_tenant_profile_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/tenantProfileInfos`

Get Tenant Profiles Info (getTenantProfileInfos)

Returns a page of tenant profile info objects registered in the platform. Tenant Profile Info is a lightweight object that contains only id and name of the profile. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'SYS_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the tenant profile name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: id, name] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataEntityInfo**


## get_tenant_profile_list

```python
List[TenantProfile] client.get_tenant_profile_list(ids: List[str])
```

**GET** `/api/tenantProfiles/list`

Get Tenant Profile list (getTenantProfileList)


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ids** | **List[str]** | Comma-separated list of tenant profile ids | |

### Return type

**List[TenantProfile]**


## get_tenant_profiles

```python
PageDataTenantProfile client.get_tenant_profiles(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/tenantProfiles`

Get Tenant Profiles (getTenantProfiles)

Returns a page of tenant profiles registered in the platform. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'SYS_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the tenant profile name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, description, isDefault] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataTenantProfile**


## save_tenant_profile

```python
TenantProfile client.save_tenant_profile(tenant_profile: TenantProfile)
```

**POST** `/api/tenantProfile`

Create Or update Tenant Profile (saveTenantProfile)

Create or update the Tenant Profile. When creating tenant profile, platform generates Tenant Profile Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Tenant Profile Id will be present in the response. Specify existing Tenant Profile Id id to update the Tenant Profile. Referencing non-existing Tenant Profile Id will cause 'Not Found' error.   Update of the tenant profile configuration will cause immediate recalculation of API limits for all affected Tenants.   The **'profileData'** object is the part of Tenant Profile that defines API limits and Rate limits.   You have an ability to define maximum number of devices ('maxDevice'), assets ('maxAssets') and other entities. You may also define maximum number of messages to be processed per month ('maxTransportMessages', 'maxREExecutions', etc). The '*RateLimit' defines the rate limits using simple syntax. For example, '1000:1,20000:60' means up to 1000 events per second but no more than 20000 event per minute. Let's review the example of tenant profile data below:   ```json {   \"name\": \"Your name\",   \"description\": \"Your description\",   \"isolatedTbRuleEngine\": false,   \"profileData\": {     \"configuration\": {       \"type\": \"DEFAULT\",       \"maxDevices\": 0,       \"maxAssets\": 0,       \"maxCustomers\": 0,       \"maxUsers\": 0,       \"maxDashboards\": 0,       \"maxRuleChains\": 0,       \"maxResourcesInBytes\": 0,       \"maxOtaPackagesInBytes\": 0,       \"maxResourceSize\": 0,       \"transportTenantMsgRateLimit\": \"1000:1,20000:60\",       \"transportTenantTelemetryMsgRateLimit\": \"1000:1,20000:60\",       \"transportTenantTelemetryDataPointsRateLimit\": \"1000:1,20000:60\",       \"transportDeviceMsgRateLimit\": \"20:1,600:60\",       \"transportDeviceTelemetryMsgRateLimit\": \"20:1,600:60\",       \"transportDeviceTelemetryDataPointsRateLimit\": \"20:1,600:60\",       \"transportGatewayMsgRateLimit\": \"20:1,600:60\",       \"transportGatewayTelemetryMsgRateLimit\": \"20:1,600:60\",       \"transportGatewayTelemetryDataPointsRateLimit\": \"20:1,600:60\",       \"transportGatewayDeviceMsgRateLimit\": \"20:1,600:60\",       \"transportGatewayDeviceTelemetryMsgRateLimit\": \"20:1,600:60\",       \"transportGatewayDeviceTelemetryDataPointsRateLimit\": \"20:1,600:60\",       \"integrationMsgsPerTenantRateLimit\": \"20:1,600:60\",       \"integrationMsgsPerDeviceRateLimit\": \"20:1,600:60\",       \"integrationMsgsPerAssetRateLimit\": \"20:1,600:60\",       \"maxTransportMessages\": 10000000,       \"maxTransportDataPoints\": 10000000,       \"maxREExecutions\": 4000000,       \"maxJSExecutions\": 5000000,       \"maxDPStorageDays\": 0,       \"maxRuleNodeExecutionsPerMessage\": 50,       \"maxDebugModeDurationMinutes\": 15,       \"maxEmails\": 0,       \"maxSms\": 0,       \"maxCreatedAlarms\": 1000,       \"defaultStorageTtlDays\": 0,       \"alarmsTtlDays\": 0,       \"rpcTtlDays\": 0,       \"queueStatsTtlDays\": 0,       \"ruleEngineExceptionsTtlDays\": 0,       \"blobEntityTtlDays\": 0,       \"warnThreshold\": 0,       \"maxCalculatedFieldsPerEntity\": 100,       \"maxArgumentsPerCF\": 10,       \"minAllowedScheduledUpdateIntervalInSecForCF\": 10,       \"maxRelationLevelPerCfArgument\": 2,       \"maxRelatedEntitiesToReturnPerCfArgument\": 1000,       \"maxDataPointsPerRollingArg\": 1000,       \"maxStateSizeInKBytes\": 512,       \"maxSingleValueArgumentSizeInKBytes\": 32,      \"minAllowedDeduplicationIntervalInSecForCF\": 10,      \"minAllowedAggregationIntervalInSecForCF\": 60,      \"intermediateAggregationIntervalInSecForCF\": 300,      \"cfReevaluationCheckInterval\": 60,      \"alarmsReevaluationInterval\": 60    }   },   \"default\": false } ```Remove 'id', from the request body example (below) to create new Tenant Profile entity.  Available for users with 'SYS_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **tenant_profile** | **TenantProfile** |  | |

### Return type

**TenantProfile**


## set_default_tenant_profile

```python
TenantProfile client.set_default_tenant_profile(tenant_profile_id: str)
```

**POST** `/api/tenantProfile/{tenantProfileId}/default`

Make tenant profile default (setDefaultTenantProfile)

Makes specified tenant profile to be default. Referencing non-existing tenant profile Id will cause an error.   Available for users with 'SYS_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **tenant_profile_id** | **str** | A string value representing the tenant profile id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**TenantProfile**

