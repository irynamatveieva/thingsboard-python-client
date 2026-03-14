
# ChecksumAlgorithm

`tb_ce_client.models.ChecksumAlgorithm`

## Enum Values


* `MD5` (value: `'MD5'`)

* `SHA256` (value: `'SHA256'`)

* `SHA384` (value: `'SHA384'`)

* `SHA512` (value: `'SHA512'`)

* `CRC32` (value: `'CRC32'`)

* `MURMUR3_32` (value: `'MURMUR3_32'`)

* `MURMUR3_128` (value: `'MURMUR3_128'`)



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ChecksumAlgorithm.model_validate(data)` or `ChecksumAlgorithm.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

