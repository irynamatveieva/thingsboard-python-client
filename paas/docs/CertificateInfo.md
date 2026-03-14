
# CertificateInfo

`tb_paas_client.models.CertificateInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **status** | [**CertificateStatus**](CertificateStatus.md) |  | [optional] |
| **domain_name** | **str** |  | [optional] |
| **serial_number** | **str** |  | [optional] |
| **not_before** | **int** |  | [optional] |
| **not_after** | **int** |  | [optional] |
| **requested_at** | **int** |  | [optional] |
| **issued_at** | **int** |  | [optional] |
| **acme_certificate_id** | [**AcmeCertificateId**](AcmeCertificateId.md) |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.status`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CertificateInfo.model_validate(data)` or `CertificateInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

