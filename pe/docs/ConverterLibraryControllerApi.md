# ConverterLibraryControllerApi

`ThingsboardClient` methods:

```python
str client.get_downlink_converter(integration_type: IntegrationType, vendor_name: str, model: str)  # Get downlink converter (getDownlinkConverter)
str client.get_downlink_converter_metadata(integration_type: IntegrationType, vendor_name: str, model: str)  # Get downlink converter metadata (getDownlinkConverterMetadata)
str client.get_downlink_payload(integration_type: IntegrationType, vendor_name: str, model: str)  # Get downlink payload (getDownlinkPayload)
str client.get_uplink_converter(integration_type: IntegrationType, vendor_name: str, model: str)  # Get uplink converter (getUplinkConverter)
str client.get_uplink_converter_metadata(integration_type: IntegrationType, vendor_name: str, model: str)  # Get uplink converter metadata (getUplinkConverterMetadata)
str client.get_uplink_payload(integration_type: IntegrationType, vendor_name: str, model: str)  # Get uplink payload (getUplinkPayload)
List[Model] client.get_vendor_models(integration_type: IntegrationType, vendor_name: str, converter_type: Optional[str] = None, page: Optional[int] = None, page_size: Optional[int] = None, load_images: Optional[bool] = None)  # Get vendor models (getVendorModels)
List[Vendor] client.get_vendors(integration_type: IntegrationType, converter_type: Optional[str] = None, page: Optional[int] = None, page_size: Optional[int] = None, load_images: Optional[bool] = None)  # Get vendors (getVendors)
```


## get_downlink_converter

```python
str client.get_downlink_converter(integration_type: IntegrationType, vendor_name: str, model: str)
```

**GET** `/api/converter/library/{integrationType}/{vendorName}/{model}/downlink`

Get downlink converter (getDownlinkConverter)

Returns downlink converter body for the vendor, integration type and model


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **integration_type** | **IntegrationType** |  | [enum: OCEANCONNECT, SIGFOX, THINGPARK, TPE, CHIRPSTACK, PARTICLE, TMOBILE_IOT_CDP, HTTP, MQTT, PUB_SUB, AWS_IOT, AWS_SQS, AWS_KINESIS, TTN, TTI, AZURE_EVENT_HUB, OPC_UA, CUSTOM, UDP, TCP, KAFKA, AZURE_IOT_HUB, APACHE_PULSAR, RABBITMQ, LORIOT, COAP, TUYA, AZURE_SERVICE_BUS, KPN] |
| **vendor_name** | **str** |  | |
| **model** | **str** |  | |

### Return type

**str**


## get_downlink_converter_metadata

```python
str client.get_downlink_converter_metadata(integration_type: IntegrationType, vendor_name: str, model: str)
```

**GET** `/api/converter/library/{integrationType}/{vendorName}/{model}/downlink/metadata`

Get downlink converter metadata (getDownlinkConverterMetadata)

Returns downlink converter metadata for the vendor, integration type and model


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **integration_type** | **IntegrationType** |  | [enum: OCEANCONNECT, SIGFOX, THINGPARK, TPE, CHIRPSTACK, PARTICLE, TMOBILE_IOT_CDP, HTTP, MQTT, PUB_SUB, AWS_IOT, AWS_SQS, AWS_KINESIS, TTN, TTI, AZURE_EVENT_HUB, OPC_UA, CUSTOM, UDP, TCP, KAFKA, AZURE_IOT_HUB, APACHE_PULSAR, RABBITMQ, LORIOT, COAP, TUYA, AZURE_SERVICE_BUS, KPN] |
| **vendor_name** | **str** |  | |
| **model** | **str** |  | |

### Return type

**str**


## get_downlink_payload

```python
str client.get_downlink_payload(integration_type: IntegrationType, vendor_name: str, model: str)
```

**GET** `/api/converter/library/{integrationType}/{vendorName}/{model}/downlink/payload`

Get downlink payload (getDownlinkPayload)

Returns payload example for the downlink converter for the vendor, integration type and model


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **integration_type** | **IntegrationType** |  | [enum: OCEANCONNECT, SIGFOX, THINGPARK, TPE, CHIRPSTACK, PARTICLE, TMOBILE_IOT_CDP, HTTP, MQTT, PUB_SUB, AWS_IOT, AWS_SQS, AWS_KINESIS, TTN, TTI, AZURE_EVENT_HUB, OPC_UA, CUSTOM, UDP, TCP, KAFKA, AZURE_IOT_HUB, APACHE_PULSAR, RABBITMQ, LORIOT, COAP, TUYA, AZURE_SERVICE_BUS, KPN] |
| **vendor_name** | **str** |  | |
| **model** | **str** |  | |

### Return type

**str**


## get_uplink_converter

```python
str client.get_uplink_converter(integration_type: IntegrationType, vendor_name: str, model: str)
```

**GET** `/api/converter/library/{integrationType}/{vendorName}/{model}/uplink`

Get uplink converter (getUplinkConverter)

Returns uplink converter body for the vendor, integration type and model


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **integration_type** | **IntegrationType** |  | [enum: OCEANCONNECT, SIGFOX, THINGPARK, TPE, CHIRPSTACK, PARTICLE, TMOBILE_IOT_CDP, HTTP, MQTT, PUB_SUB, AWS_IOT, AWS_SQS, AWS_KINESIS, TTN, TTI, AZURE_EVENT_HUB, OPC_UA, CUSTOM, UDP, TCP, KAFKA, AZURE_IOT_HUB, APACHE_PULSAR, RABBITMQ, LORIOT, COAP, TUYA, AZURE_SERVICE_BUS, KPN] |
| **vendor_name** | **str** |  | |
| **model** | **str** |  | |

### Return type

**str**


## get_uplink_converter_metadata

```python
str client.get_uplink_converter_metadata(integration_type: IntegrationType, vendor_name: str, model: str)
```

**GET** `/api/converter/library/{integrationType}/{vendorName}/{model}/uplink/metadata`

Get uplink converter metadata (getUplinkConverterMetadata)

Returns uplink converter metadata for the vendor, integration type and model


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **integration_type** | **IntegrationType** |  | [enum: OCEANCONNECT, SIGFOX, THINGPARK, TPE, CHIRPSTACK, PARTICLE, TMOBILE_IOT_CDP, HTTP, MQTT, PUB_SUB, AWS_IOT, AWS_SQS, AWS_KINESIS, TTN, TTI, AZURE_EVENT_HUB, OPC_UA, CUSTOM, UDP, TCP, KAFKA, AZURE_IOT_HUB, APACHE_PULSAR, RABBITMQ, LORIOT, COAP, TUYA, AZURE_SERVICE_BUS, KPN] |
| **vendor_name** | **str** |  | |
| **model** | **str** |  | |

### Return type

**str**


## get_uplink_payload

```python
str client.get_uplink_payload(integration_type: IntegrationType, vendor_name: str, model: str)
```

**GET** `/api/converter/library/{integrationType}/{vendorName}/{model}/uplink/payload`

Get uplink payload (getUplinkPayload)

Returns payload example for the uplink converter for the vendor, integration type and model


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **integration_type** | **IntegrationType** |  | [enum: OCEANCONNECT, SIGFOX, THINGPARK, TPE, CHIRPSTACK, PARTICLE, TMOBILE_IOT_CDP, HTTP, MQTT, PUB_SUB, AWS_IOT, AWS_SQS, AWS_KINESIS, TTN, TTI, AZURE_EVENT_HUB, OPC_UA, CUSTOM, UDP, TCP, KAFKA, AZURE_IOT_HUB, APACHE_PULSAR, RABBITMQ, LORIOT, COAP, TUYA, AZURE_SERVICE_BUS, KPN] |
| **vendor_name** | **str** |  | |
| **model** | **str** |  | |

### Return type

**str**


## get_vendor_models

```python
List[Model] client.get_vendor_models(integration_type: IntegrationType, vendor_name: str, converter_type: Optional[str] = None, page: Optional[int] = None, page_size: Optional[int] = None, load_images: Optional[bool] = None)
```

**GET** `/api/converter/library/{integrationType}/{vendorName}/models`

Get vendor models (getVendorModels)

Returns a list of models for the vendor, integration type and converter type


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **integration_type** | **IntegrationType** |  | [enum: OCEANCONNECT, SIGFOX, THINGPARK, TPE, CHIRPSTACK, PARTICLE, TMOBILE_IOT_CDP, HTTP, MQTT, PUB_SUB, AWS_IOT, AWS_SQS, AWS_KINESIS, TTN, TTI, AZURE_EVENT_HUB, OPC_UA, CUSTOM, UDP, TCP, KAFKA, AZURE_IOT_HUB, APACHE_PULSAR, RABBITMQ, LORIOT, COAP, TUYA, AZURE_SERVICE_BUS, KPN] |
| **vendor_name** | **str** |  | |
| **converter_type** | **str** |  | [optional] |
| **page** | **int** |  | [optional] [default to 0] |
| **page_size** | **int** |  | [optional] [default to 2147483647] |
| **load_images** | **bool** |  | [optional] [default to True] |

### Return type

**List[Model]**


## get_vendors

```python
List[Vendor] client.get_vendors(integration_type: IntegrationType, converter_type: Optional[str] = None, page: Optional[int] = None, page_size: Optional[int] = None, load_images: Optional[bool] = None)
```

**GET** `/api/converter/library/{integrationType}/vendors`

Get vendors (getVendors)

Returns a list of vendors for the integration type


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **integration_type** | **IntegrationType** |  | [enum: OCEANCONNECT, SIGFOX, THINGPARK, TPE, CHIRPSTACK, PARTICLE, TMOBILE_IOT_CDP, HTTP, MQTT, PUB_SUB, AWS_IOT, AWS_SQS, AWS_KINESIS, TTN, TTI, AZURE_EVENT_HUB, OPC_UA, CUSTOM, UDP, TCP, KAFKA, AZURE_IOT_HUB, APACHE_PULSAR, RABBITMQ, LORIOT, COAP, TUYA, AZURE_SERVICE_BUS, KPN] |
| **converter_type** | **str** |  | [optional] |
| **page** | **int** |  | [optional] [default to 0] |
| **page_size** | **int** |  | [optional] [default to 2147483647] |
| **load_images** | **bool** |  | [optional] [default to True] |

### Return type

**List[Vendor]**

