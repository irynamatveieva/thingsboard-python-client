
# TwilioSmsProviderConfiguration

`tb_ce_client.models.TwilioSmsProviderConfiguration`

**Extends:** **SmsProviderConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **account_sid** | **str** | Twilio account Sid. | [optional] |
| **account_token** | **str** | Twilio account Token. | [optional] |
| **number_from** | **str** | The number/id of a sender. | [optional] |



## Referenced Types

#### SmsProviderConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AwsSnsSmsProviderConfiguration  *(extends SmsProviderConfiguration, type=`AWS_SNS`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| access_key_id | str | The AWS SNS Access Key ID. | [optional] |
| secret_access_key | str | The AWS SNS Access Key. | [optional] |
| region | str | The AWS region. | [optional] |

#### SmppSmsProviderConfiguration  *(extends SmsProviderConfiguration, type=`SMPP`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| protocol_version | Protocol_versionEnum | SMPP version |  |
| host | str | SMPP host |  |
| port | int | SMPP port |  |
| system_id | str | System ID |  |
| password | str | Password |  |
| system_type | str | System type | [optional] |
| bind_type | SmppBindType | TX - Transmitter, RX - Receiver, TRX - Transciever. By default TX is used | [optional] |
| service_type | str | Service type | [optional] |
| source_address | str | Source address | [optional] |
| source_ton | bytearray | Source TON (Type of Number). Needed is source address is set. 5 by default. 0 - Unknown 1 - International 2 - National 3 - Network Specific 4 - Subscriber Number 5 - Alphanumeric 6 - Abbreviated | [optional] |
| source_npi | bytearray | Source NPI (Numbering Plan Identification). Needed is source address is set. 0 by default. 0 - Unknown 1 - ISDN/telephone numbering plan (E163/E164) 3 - Data numbering plan (X.121) 4 - Telex numbering plan (F.69) 6 - Land Mobile (E.212) =6 8 - National numbering plan 9 - Private numbering plan 10 - ERMES numbering plan (ETSI DE/PS 3 01-3) 13 - Internet (IP) 18 - WAP Client Id (to be defined by WAP Forum) | [optional] |
| destination_ton | bytearray | Destination TON (Type of Number). 5 by default. 0 - Unknown 1 - International 2 - National 3 - Network Specific 4 - Subscriber Number 5 - Alphanumeric 6 - Abbreviated | [optional] |
| destination_npi | bytearray | Destination NPI (Numbering Plan Identification). 0 by default. 0 - Unknown 1 - ISDN/telephone numbering plan (E163/E164) 3 - Data numbering plan (X.121) 4 - Telex numbering plan (F.69) 6 - Land Mobile (E.212) =6 8 - National numbering plan 9 - Private numbering plan 10 - ERMES numbering plan (ETSI DE/PS 3 01-3) 13 - Internet (IP) 18 - WAP Client Id (to be defined by WAP Forum) | [optional] |
| address_range | str | Address range | [optional] |
| coding_scheme | bytearray | 0 - SMSC Default Alphabet (ASCII for short and long code and to GSM for toll-free, used as default) 1 - IA5 (ASCII for short and long code, Latin 9 for toll-free (ISO-8859-9)) 2 - Octet Unspecified (8-bit binary) 3 - Latin 1 (ISO-8859-1) 4 - Octet Unspecified (8-bit binary) 5 - JIS (X 0208-1990) 6 - Cyrillic (ISO-8859-5) 7 - Latin/Hebrew (ISO-8859-8) 8 - UCS2/UTF-16 (ISO/IEC-10646) 9 - Pictogram Encoding 10 - Music Codes (ISO-2022-JP) 13 - Extended Kanji JIS (X 0212-1990) 14 - Korean Graphic Character Set (KS C 5601/KS X 1001) | [optional] |

#### SmppBindType (enum)
`TX` | `RX` | `TRX`

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.account_sid`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TwilioSmsProviderConfiguration.model_validate(data)` or `TwilioSmsProviderConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

