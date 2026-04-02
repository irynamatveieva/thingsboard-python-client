
# DeviceProfileProvisionConfiguration

`tb_pe_client.models.DeviceProfileProvisionConfiguration`

Device profile provision configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **provision_device_secret** | **str** | Provision device secret | [optional] |
| **type** | **str** |  | |



## Subtypes

#### AllowCreateNewDevicesDeviceProfileProvisionConfiguration  *(type=`ALLOW_CREATE_NEW_DEVICES`)*
*(no additional properties)*

#### CheckPreProvisionedDevicesDeviceProfileProvisionConfiguration  *(type=`CHECK_PRE_PROVISIONED_DEVICES`)*
*(no additional properties)*

#### DisabledDeviceProfileProvisionConfiguration  *(type=`DISABLED`)*
*(no additional properties)*

#### X509CertificateChainProvisionConfiguration  *(type=`X509_CERTIFICATE_CHAIN`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| certificate_reg_ex_pattern | str |  | [optional] |
| allow_create_new_devices_by_x509_certificate | bool |  | [optional] |

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.provision_device_secret`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DeviceProfileProvisionConfiguration.model_validate(data)` or `DeviceProfileProvisionConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

