# OwnerControllerApi

`ThingsboardClient` methods:

```python
None client.change_owner_to_customer(owner_id: str, entity_type: str, entity_id: str, request_body: Optional[List[str]] = None)  # Change owner to customer (changeOwnerToCustomer)
None client.change_owner_to_tenant(owner_id: str, entity_type: str, entity_id: str, request_body: Optional[List[str]] = None)  # Change owner to tenant (changeOwnerToTenant)
```


## change_owner_to_customer

```python
None client.change_owner_to_customer(owner_id: str, entity_type: str, entity_id: str, request_body: Optional[List[str]] = None)
```

**POST** `/api/owner/CUSTOMER/{ownerId}/{entityType}/{entityId}`

Change owner to customer (changeOwnerToCustomer)

Tenant/Customer changes Owner to Customer or sub-Customer. Sub-Customer can`t perform this operation!   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **request_body** | **List[str]** |  | [optional] |

### Return type

None (empty response body)


## change_owner_to_tenant

```python
None client.change_owner_to_tenant(owner_id: str, entity_type: str, entity_id: str, request_body: Optional[List[str]] = None)
```

**POST** `/api/owner/TENANT/{ownerId}/{entityType}/{entityId}`

Change owner to tenant (changeOwnerToTenant)

Tenant changes Owner from Customer or sub-Customer to Tenant.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner_id** | **str** | A string value representing the tenant id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **request_body** | **List[str]** |  | [optional] |

### Return type

None (empty response body)

