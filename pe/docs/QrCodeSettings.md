
# QrCodeSettings

`tb_pe_client.models.QrCodeSettings`

A JSON value representing the mobile apps configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**QrCodeSettingsId**](QrCodeSettingsId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id. | [optional] [readonly] |
| **use_system_settings** | **bool** | Use settings from system level | [optional] |
| **use_default_app** | **bool** | Type of application: true means use default Thingsboard app | [optional] |
| **mobile_app_bundle_id** | [**MobileAppBundleId**](MobileAppBundleId.md) | Mobile app bundle. | [optional] |
| **qr_code_config** | [**QRCodeConfig**](QRCodeConfig.md) | QR code config configuration. | |
| **android_enabled** | **bool** | Indicates if google play link is available | [optional] |
| **ios_enabled** | **bool** | Indicates if apple store link is available | [optional] |
| **google_play_link** | **str** |  | [optional] [readonly] |
| **app_store_link** | **str** |  | [optional] [readonly] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `QrCodeSettings.model_validate(data)` or `QrCodeSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

