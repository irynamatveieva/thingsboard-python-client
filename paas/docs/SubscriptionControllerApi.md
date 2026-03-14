# SubscriptionControllerApi

`ThingsboardClient` methods:

```python
DefaultTenantProfileConfiguration client.get_merged_tenant_profile_configuration()  # getMergedTenantProfileConfiguration
DefaultTenantProfileConfiguration client.get_tenant_profile_configuration_by_id(tenant_profile_id: str)  # getTenantProfileConfigurationById
SubscriptionDetails client.get_tenant_subscription()  # getTenantSubscription
SubscriptionUsage client.get_tenant_subscription_usage()  # getTenantSubscriptionUsage
bool client.trendz_used()  # trendzUsed
```


## get_merged_tenant_profile_configuration

```python
DefaultTenantProfileConfiguration client.get_merged_tenant_profile_configuration()
```

**GET** `/api/tenant/subscription/mergedProfileConfig`

getMergedTenantProfileConfiguration

### Return type

**DefaultTenantProfileConfiguration**


## get_tenant_profile_configuration_by_id

```python
DefaultTenantProfileConfiguration client.get_tenant_profile_configuration_by_id(tenant_profile_id: str)
```

**GET** `/api/tenantProfile/{tenantProfileId}/profileConfig`

getTenantProfileConfigurationById


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **tenant_profile_id** | **str** |  | |

### Return type

**DefaultTenantProfileConfiguration**


## get_tenant_subscription

```python
SubscriptionDetails client.get_tenant_subscription()
```

**GET** `/api/tenant/subscription`

getTenantSubscription

### Return type

**SubscriptionDetails**


## get_tenant_subscription_usage

```python
SubscriptionUsage client.get_tenant_subscription_usage()
```

**GET** `/api/tenant/subscription/usage`

getTenantSubscriptionUsage

### Return type

**SubscriptionUsage**


## trendz_used

```python
bool client.trendz_used()
```

**GET** `/api/tenant/subscription/trendzUsed`

trendzUsed

### Return type

**bool**

