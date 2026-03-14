# BillingEndpointControllerApi

`ThingsboardClient` methods:

```python
None client.check_tenant_can_update_plan(body: object)  # checkTenantCanUpdatePlan
None client.notify_tenant_plan_changed(body: object)  # notifyTenantPlanChanged
None client.notify_tenant_state_changed(body: object)  # notifyTenantStateChanged
None client.notify_tenant_subscription_created(body: object)  # notifyTenantSubscriptionCreated
None client.send_account_activated_email(body: object)  # sendAccountActivatedEmail
None client.send_billing_activation_email(body: object)  # sendBillingActivationEmail
None client.send_password_was_reset_email(body: object)  # sendPasswordWasResetEmail
None client.send_reset_password_email(body: object)  # sendResetPasswordEmail
bool client.tenant_has_billing_read()  # tenantHasBillingRead
bool client.tenant_has_billing_write()  # tenantHasBillingWrite
bool client.tenant_has_hidden_plans_access()  # tenantHasHiddenPlansAccess
```


## check_tenant_can_update_plan

```python
None client.check_tenant_can_update_plan(body: object)
```

**POST** `/api/billingEndpoint/tenantCanUpdatePlan`

checkTenantCanUpdatePlan


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | **object** |  | |

### Return type

None (empty response body)


## notify_tenant_plan_changed

```python
None client.notify_tenant_plan_changed(body: object)
```

**POST** `/api/billingEndpoint/tenantPlanChanged`

notifyTenantPlanChanged


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | **object** |  | |

### Return type

None (empty response body)


## notify_tenant_state_changed

```python
None client.notify_tenant_state_changed(body: object)
```

**POST** `/api/billingEndpoint/tenantStateChanged`

notifyTenantStateChanged


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | **object** |  | |

### Return type

None (empty response body)


## notify_tenant_subscription_created

```python
None client.notify_tenant_subscription_created(body: object)
```

**POST** `/api/billingEndpoint/tenantSubscriptionCreated`

notifyTenantSubscriptionCreated


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | **object** |  | |

### Return type

None (empty response body)


## send_account_activated_email

```python
None client.send_account_activated_email(body: object)
```

**POST** `/api/billingEndpoint/sendAccountActivated`

sendAccountActivatedEmail


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | **object** |  | |

### Return type

None (empty response body)


## send_billing_activation_email

```python
None client.send_billing_activation_email(body: object)
```

**POST** `/api/billingEndpoint/sendActivation`

sendBillingActivationEmail


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | **object** |  | |

### Return type

None (empty response body)


## send_password_was_reset_email

```python
None client.send_password_was_reset_email(body: object)
```

**POST** `/api/billingEndpoint/sendPasswordWasReset`

sendPasswordWasResetEmail


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | **object** |  | |

### Return type

None (empty response body)


## send_reset_password_email

```python
None client.send_reset_password_email(body: object)
```

**POST** `/api/billingEndpoint/sendResetPassword`

sendResetPasswordEmail


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | **object** |  | |

### Return type

None (empty response body)


## tenant_has_billing_read

```python
bool client.tenant_has_billing_read()
```

**GET** `/api/billingEndpoint/tenant/permission/billing/read`

tenantHasBillingRead

### Return type

**bool**


## tenant_has_billing_write

```python
bool client.tenant_has_billing_write()
```

**GET** `/api/billingEndpoint/tenant/permission/billing/write`

tenantHasBillingWrite

### Return type

**bool**


## tenant_has_hidden_plans_access

```python
bool client.tenant_has_hidden_plans_access()
```

**GET** `/api/billingEndpoint/tenant/permission/billing/hiddenPlans`

tenantHasHiddenPlansAccess

### Return type

**bool**

