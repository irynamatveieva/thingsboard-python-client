
# X509CertificateChainProvisionConfiguration

`tb_pe_client.models.X509CertificateChainProvisionConfiguration`

**Extends:** **DeviceProfileProvisionConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **certificate_reg_ex_pattern** | **str** |  | [optional] |
| **allow_create_new_devices_by_x509_certificate** | **bool** |  | [optional] |



## Referenced Types

#### DeviceProfileProvisionConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| provision_device_secret | str | Provision device secret | [optional] |
| type | str |  |  |

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.certificate_reg_ex_pattern`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `X509CertificateChainProvisionConfiguration.model_validate(data)` or `X509CertificateChainProvisionConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

