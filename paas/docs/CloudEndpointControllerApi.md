# CloudEndpointControllerApi

`ThingsboardClient` methods:

```python
None client.check_tenant_white_labeling_allowed()  # checkTenantWhiteLabelingAllowed
bool client.has_domain_read_permission()  # hasDomainReadPermission
bool client.has_domain_write_permission()  # hasDomainWritePermission
bool client.tenant_has_white_label_read()  # tenantHasWhiteLabelRead
bool client.tenant_has_white_label_write()  # tenantHasWhiteLabelWrite
```


## check_tenant_white_labeling_allowed

```python
None client.check_tenant_white_labeling_allowed()
```

**GET** `/api/cloudEndpoint/tenant/permission/whiteLabelingAllowed`

checkTenantWhiteLabelingAllowed

### Return type

None (empty response body)


## has_domain_read_permission

```python
bool client.has_domain_read_permission()
```

**GET** `/api/cloudEndpoint/permission/domain/read`

hasDomainReadPermission

### Return type

**bool**


## has_domain_write_permission

```python
bool client.has_domain_write_permission()
```

**GET** `/api/cloudEndpoint/permission/domain/write`

hasDomainWritePermission

### Return type

**bool**


## tenant_has_white_label_read

```python
bool client.tenant_has_white_label_read()
```

**GET** `/api/cloudEndpoint/tenant/permission/whiteLabel/read`

tenantHasWhiteLabelRead

### Return type

**bool**


## tenant_has_white_label_write

```python
bool client.tenant_has_white_label_write()
```

**GET** `/api/cloudEndpoint/tenant/permission/whiteLabel/write`

tenantHasWhiteLabelWrite

### Return type

**bool**

