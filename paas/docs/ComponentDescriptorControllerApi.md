# ComponentDescriptorControllerApi

`ThingsboardClient` methods:

```python
ComponentDescriptor client.get_component_descriptor_by_clazz(component_descriptor_clazz: str)  # Get Component Descriptor (getComponentDescriptorByClazz)
List[ComponentDescriptor] client.get_component_descriptors_by_type(component_type: str, rule_chain_type: Optional[str] = None)  # Get Component Descriptors (getComponentDescriptorsByType)
List[ComponentDescriptor] client.get_component_descriptors_by_types(component_types: List[str], rule_chain_type: Optional[str] = None)  # Get Component Descriptors (getComponentDescriptorsByTypes)
```


## get_component_descriptor_by_clazz

```python
ComponentDescriptor client.get_component_descriptor_by_clazz(component_descriptor_clazz: str)
```

**GET** `/api/component/{componentDescriptorClazz}`

Get Component Descriptor (getComponentDescriptorByClazz)

Gets the Component Descriptor object using class name from the path parameters. Each Component Descriptor represents configuration of specific rule node (e.g. 'Save Timeseries' or 'Send Email'.). The Component Descriptors are used by the rule chain Web UI to build the configuration forms for the rule nodes. The Component Descriptors are discovered at runtime by scanning the class path and searching for @RuleNode annotation. Once discovered, the up to date list of descriptors is persisted to the database.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **component_descriptor_clazz** | **str** | Component Descriptor class name | |

### Return type

**ComponentDescriptor**


## get_component_descriptors_by_type

```python
List[ComponentDescriptor] client.get_component_descriptors_by_type(component_type: str, rule_chain_type: Optional[str] = None)
```

**GET** `/api/components/{componentType}`

Get Component Descriptors (getComponentDescriptorsByType)

Gets the Component Descriptors using rule node type and optional rule chain type request parameters. Each Component Descriptor represents configuration of specific rule node (e.g. 'Save Timeseries' or 'Send Email'.). The Component Descriptors are used by the rule chain Web UI to build the configuration forms for the rule nodes. The Component Descriptors are discovered at runtime by scanning the class path and searching for @RuleNode annotation. Once discovered, the up to date list of descriptors is persisted to the database.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **component_type** | **str** | Type of the Rule Node | [enum: ENRICHMENT, FILTER, TRANSFORMATION, ACTION, EXTERNAL] |
| **rule_chain_type** | **str** | Type of the Rule Chain | [optional] [enum: CORE, EDGE] |

### Return type

**List[ComponentDescriptor]**


## get_component_descriptors_by_types

```python
List[ComponentDescriptor] client.get_component_descriptors_by_types(component_types: List[str], rule_chain_type: Optional[str] = None)
```

**GET** `/api/components`

Get Component Descriptors (getComponentDescriptorsByTypes)

Gets the Component Descriptors using coma separated list of rule node types and optional rule chain type request parameters. Each Component Descriptor represents configuration of specific rule node (e.g. 'Save Timeseries' or 'Send Email'.). The Component Descriptors are used by the rule chain Web UI to build the configuration forms for the rule nodes. The Component Descriptors are discovered at runtime by scanning the class path and searching for @RuleNode annotation. Once discovered, the up to date list of descriptors is persisted to the database.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **component_types** | **List[str]** | List of types of the Rule Nodes, (ENRICHMENT, FILTER, TRANSFORMATION, ACTION or EXTERNAL) | |
| **rule_chain_type** | **str** | Type of the Rule Chain | [optional] [enum: CORE, EDGE] |

### Return type

**List[ComponentDescriptor]**

