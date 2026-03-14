# RuleChainControllerApi

`ThingsboardClient` methods:

```python
RuleChain client.assign_rule_chain_to_edge(edge_id: str, rule_chain_id: str)  # Assign rule chain to edge (assignRuleChainToEdge)
None client.delete_rule_chain(rule_chain_id: str)  # Delete rule chain (deleteRuleChain)
RuleChainData client.export_rule_chains(limit: int)  # Export Rule Chains
List[RuleChain] client.get_auto_assign_to_edge_rule_chains()  # Get Auto Assign To Edge Rule Chains (getAutoAssignToEdgeRuleChains)
PageDataRuleChain client.get_edge_rule_chains(edge_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Edge Rule Chains (getEdgeRuleChains)
object client.get_latest_rule_node_debug_input(rule_node_id: str)  # Get latest input message (getLatestRuleNodeDebugInput)
RuleChain client.get_rule_chain_by_id(rule_chain_id: str)  # Get Rule Chain (getRuleChainById)
RuleChainMetaData client.get_rule_chain_meta_data(rule_chain_id: str)  # Get Rule Chain (getRuleChainById)
List[str] client.get_rule_chain_output_labels(rule_chain_id: str)  # Get Rule Chain output labels (getRuleChainOutputLabels)
List[RuleChainOutputLabelsUsage] client.get_rule_chain_output_labels_usage(rule_chain_id: str)  # Get output labels usage (getRuleChainOutputLabelsUsage)
PageDataRuleChain client.get_rule_chains(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Rule Chains (getRuleChains)
List[RuleChain] client.get_rule_chains_by_ids(rule_chain_ids: List[str])  # Get Rule Chains By Ids (getRuleChainsByIds)
List[RuleChainImportResult] client.import_rule_chains(rule_chain_data: RuleChainData, overwrite: Optional[bool] = None)  # Import Rule Chains
bool client.is_tbel_enabled()  # Is TBEL script executor enabled
RuleChain client.save_rule_chain(rule_chain: RuleChain)  # Create Or Update Rule Chain (saveRuleChain)
RuleChainMetaData client.save_rule_chain_meta_data(rule_chain_meta_data: RuleChainMetaData, update_related: Optional[bool] = None)  # Update Rule Chain Metadata
RuleChain client.set_auto_assign_to_edge_rule_chain(rule_chain_id: str)  # Set Auto Assign To Edge Rule Chain (setAutoAssignToEdgeRuleChain)
RuleChain client.set_device_default_rule_chain(default_rule_chain_create_request: DefaultRuleChainCreateRequest)  # Create Default Rule Chain (setDeviceDefaultRuleChain)
RuleChain client.set_edge_template_root_rule_chain(rule_chain_id: str)  # Set Edge Template Root Rule Chain (setEdgeTemplateRootRuleChain)
RuleChain client.set_root_rule_chain(rule_chain_id: str)  # Set Root Rule Chain (setRootRuleChain)
object client.test_rule_chain_script(body: object, script_lang: Optional[ScriptLanguage] = None)  # Test Script function
RuleChain client.unassign_rule_chain_from_edge(edge_id: str, rule_chain_id: str)  # Unassign rule chain from edge (unassignRuleChainFromEdge)
RuleChain client.unset_auto_assign_to_edge_rule_chain(rule_chain_id: str)  # Unset Auto Assign To Edge Rule Chain (unsetAutoAssignToEdgeRuleChain)
```


## assign_rule_chain_to_edge

```python
RuleChain client.assign_rule_chain_to_edge(edge_id: str, rule_chain_id: str)
```

**POST** `/api/edge/{edgeId}/ruleChain/{ruleChainId}`

Assign rule chain to edge (assignRuleChainToEdge)

Creates assignment of an existing rule chain to an instance of The Edge. Assignment works in async way - first, notification event pushed to edge service queue on platform. Second, remote edge service will receive a copy of assignment rule chain (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once rule chain will be delivered to edge service, it's going to start processing messages locally.   Only rule chain with type 'EDGE' can be assigned to edge.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** |  | |
| **rule_chain_id** | **str** |  | |

### Return type

**RuleChain**


## delete_rule_chain

```python
None client.delete_rule_chain(rule_chain_id: str)
```

**DELETE** `/api/ruleChain/{ruleChainId}`

Delete rule chain (deleteRuleChain)

Deletes the rule chain. Referencing non-existing rule chain Id will cause an error. Referencing rule chain that is used in the device profiles will cause an error.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rule_chain_id** | **str** | A string value representing the rule chain id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## export_rule_chains

```python
RuleChainData client.export_rule_chains(limit: int)
```

**GET** `/api/ruleChains/export`

Export Rule Chains

Exports all tenant rule chains as one JSON.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | **int** | A limit of rule chains to export. | |

### Return type

**RuleChainData**


## get_auto_assign_to_edge_rule_chains

```python
List[RuleChain] client.get_auto_assign_to_edge_rule_chains()
```

**GET** `/api/ruleChain/autoAssignToEdgeRuleChains`

Get Auto Assign To Edge Rule Chains (getAutoAssignToEdgeRuleChains)

Returns a list of Rule Chains that will be assigned to a newly created edge. The rule chain object is lightweight and contains general information about the rule chain. List of rule nodes and their connection is stored in a separate 'metadata' object.  Available for users with 'TENANT_ADMIN' authority.

### Return type

**List[RuleChain]**


## get_edge_rule_chains

```python
PageDataRuleChain client.get_edge_rule_chains(edge_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/edge/{edgeId}/ruleChains`

Get Edge Rule Chains (getEdgeRuleChains)

Returns a page of Rule Chains assigned to the specified edge. The rule chain object is lightweight and contains general information about the rule chain. List of rule nodes and their connection is stored in a separate 'metadata' object.You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the rule chain name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, root] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataRuleChain**


## get_latest_rule_node_debug_input

```python
object client.get_latest_rule_node_debug_input(rule_node_id: str)
```

**GET** `/api/ruleNode/{ruleNodeId}/debugIn`

Get latest input message (getLatestRuleNodeDebugInput)

Gets the input message from the debug events for specified Rule Chain Id. Referencing non-existing rule chain Id will cause an error.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rule_node_id** | **str** | A string value representing the rule node id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**object**


## get_rule_chain_by_id

```python
RuleChain client.get_rule_chain_by_id(rule_chain_id: str)
```

**GET** `/api/ruleChain/{ruleChainId}`

Get Rule Chain (getRuleChainById)

Fetch the Rule Chain object based on the provided Rule Chain Id. The rule chain object is lightweight and contains general information about the rule chain. List of rule nodes and their connection is stored in a separate 'metadata' object.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rule_chain_id** | **str** | A string value representing the rule chain id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**RuleChain**


## get_rule_chain_meta_data

```python
RuleChainMetaData client.get_rule_chain_meta_data(rule_chain_id: str)
```

**GET** `/api/ruleChain/{ruleChainId}/metadata`

Get Rule Chain (getRuleChainById)

Fetch the Rule Chain Metadata object based on the provided Rule Chain Id. The metadata object contains information about the rule nodes and their connections.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rule_chain_id** | **str** | A string value representing the rule chain id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**RuleChainMetaData**


## get_rule_chain_output_labels

```python
List[str] client.get_rule_chain_output_labels(rule_chain_id: str)
```

**GET** `/api/ruleChain/{ruleChainId}/output/labels`

Get Rule Chain output labels (getRuleChainOutputLabels)

Fetch the unique labels for the \"output\" Rule Nodes that belong to the Rule Chain based on the provided Rule Chain Id. The rule chain object is lightweight and contains general information about the rule chain. List of rule nodes and their connection is stored in a separate 'metadata' object.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rule_chain_id** | **str** | A string value representing the rule chain id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**List[str]**


## get_rule_chain_output_labels_usage

```python
List[RuleChainOutputLabelsUsage] client.get_rule_chain_output_labels_usage(rule_chain_id: str)
```

**GET** `/api/ruleChain/{ruleChainId}/output/labels/usage`

Get output labels usage (getRuleChainOutputLabelsUsage)

Fetch the list of rule chains and the relation types (labels) they use to process output of the current rule chain based on the provided Rule Chain Id. The rule chain object is lightweight and contains general information about the rule chain. List of rule nodes and their connection is stored in a separate 'metadata' object.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rule_chain_id** | **str** | A string value representing the rule chain id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**List[RuleChainOutputLabelsUsage]**


## get_rule_chains

```python
PageDataRuleChain client.get_rule_chains(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/ruleChains`

Get Rule Chains (getRuleChains)

Returns a page of Rule Chains owned by tenant. The rule chain object is lightweight and contains general information about the rule chain. List of rule nodes and their connection is stored in a separate 'metadata' object.You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **type** | **str** | Rule chain type (CORE or EDGE) | [optional] [enum: CORE, EDGE] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the rule chain name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, root] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataRuleChain**


## get_rule_chains_by_ids

```python
List[RuleChain] client.get_rule_chains_by_ids(rule_chain_ids: List[str])
```

**GET** `/api/ruleChains/list`

Get Rule Chains By Ids (getRuleChainsByIds)

Requested rule chains must be owned by tenant which is performing the request.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rule_chain_ids** | **List[str]** | A list of rule chain ids, separated by comma ',' | |

### Return type

**List[RuleChain]**


## import_rule_chains

```python
List[RuleChainImportResult] client.import_rule_chains(rule_chain_data: RuleChainData, overwrite: Optional[bool] = None)
```

**POST** `/api/ruleChains/import`

Import Rule Chains

Imports all tenant rule chains as one JSON.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rule_chain_data** | **RuleChainData** |  | |
| **overwrite** | **bool** | Enables overwrite for existing rule chains with the same name. | [optional] [default to False] |

### Return type

**List[RuleChainImportResult]**


## is_tbel_enabled

```python
bool client.is_tbel_enabled()
```

**GET** `/api/ruleChain/tbelEnabled`

Is TBEL script executor enabled

Returns 'True' if the TBEL script execution is enabled  Available for users with 'TENANT_ADMIN' authority.

### Return type

**bool**


## save_rule_chain

```python
RuleChain client.save_rule_chain(rule_chain: RuleChain)
```

**POST** `/api/ruleChain`

Create Or Update Rule Chain (saveRuleChain)

Create or update the Rule Chain. When creating Rule Chain, platform generates Rule Chain Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Rule Chain Id will be present in the response. Specify existing Rule Chain id to update the rule chain. Referencing non-existing rule chain Id will cause 'Not Found' error.  The rule chain object is lightweight and contains general information about the rule chain. List of rule nodes and their connection is stored in a separate 'metadata' object.Remove 'id', 'tenantId' from the request body example (below) to create new Rule Chain entity.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rule_chain** | **RuleChain** |  | |

### Return type

**RuleChain**


## save_rule_chain_meta_data

```python
RuleChainMetaData client.save_rule_chain_meta_data(rule_chain_meta_data: RuleChainMetaData, update_related: Optional[bool] = None)
```

**POST** `/api/ruleChain/metadata`

Update Rule Chain Metadata

Updates the rule chain metadata. The metadata object contains information about the rule nodes and their connections.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rule_chain_meta_data** | **RuleChainMetaData** |  | |
| **update_related** | **bool** | Update related rule nodes. | [optional] [default to True] |

### Return type

**RuleChainMetaData**


## set_auto_assign_to_edge_rule_chain

```python
RuleChain client.set_auto_assign_to_edge_rule_chain(rule_chain_id: str)
```

**POST** `/api/ruleChain/{ruleChainId}/autoAssignToEdge`

Set Auto Assign To Edge Rule Chain (setAutoAssignToEdgeRuleChain)

Makes the rule chain to be automatically assigned for any new edge that will be created. Does not assign this rule chain for already created edges.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rule_chain_id** | **str** | A string value representing the rule chain id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**RuleChain**


## set_device_default_rule_chain

```python
RuleChain client.set_device_default_rule_chain(default_rule_chain_create_request: DefaultRuleChainCreateRequest)
```

**POST** `/api/ruleChain/device/default`

Create Default Rule Chain (setDeviceDefaultRuleChain)

Create rule chain from template, based on the specified name in the request. Creates the rule chain based on the template that is used to create root rule chain.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **default_rule_chain_create_request** | **DefaultRuleChainCreateRequest** |  | |

### Return type

**RuleChain**


## set_edge_template_root_rule_chain

```python
RuleChain client.set_edge_template_root_rule_chain(rule_chain_id: str)
```

**POST** `/api/ruleChain/{ruleChainId}/edgeTemplateRoot`

Set Edge Template Root Rule Chain (setEdgeTemplateRootRuleChain)

Makes the rule chain to be root rule chain for any new edge that will be created. Does not update root rule chain for already created edges.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rule_chain_id** | **str** | A string value representing the rule chain id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**RuleChain**


## set_root_rule_chain

```python
RuleChain client.set_root_rule_chain(rule_chain_id: str)
```

**POST** `/api/ruleChain/{ruleChainId}/root`

Set Root Rule Chain (setRootRuleChain)

Makes the rule chain to be root rule chain. Updates previous root rule chain as well.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rule_chain_id** | **str** | A string value representing the rule chain id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**RuleChain**


## test_rule_chain_script

```python
object client.test_rule_chain_script(body: object, script_lang: Optional[ScriptLanguage] = None)
```

**POST** `/api/ruleChain/testScript`

Test Script function

Execute the Script function and return the result. The format of request:   ```json {   \"script\": \"Your Function as String\",   \"scriptType\": \"One of: update, generate, filter, switch, json, string\",   \"argNames\": [\"msg\", \"metadata\", \"type\"],   \"msg\": \"{\\\"temperature\\\": 42}\",    \"metadata\": {     \"deviceName\": \"Device A\",     \"deviceType\": \"Thermometer\"   },   \"msgType\": \"POST_TELEMETRY_REQUEST\" } ```   Expected result JSON contains \"output\" and \"error\".  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | **object** | Test JS request. See API call description above. | |
| **script_lang** | **ScriptLanguage** | Script language: JS or TBEL | [optional] [enum: JS, TBEL] |

### Return type

**object**


## unassign_rule_chain_from_edge

```python
RuleChain client.unassign_rule_chain_from_edge(edge_id: str, rule_chain_id: str)
```

**DELETE** `/api/edge/{edgeId}/ruleChain/{ruleChainId}`

Unassign rule chain from edge (unassignRuleChainFromEdge)

Clears assignment of the rule chain to the edge. Unassignment works in async way - first, 'unassign' notification event pushed to edge queue on platform. Second, remote edge service will receive an 'unassign' command to remove rule chain (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once 'unassign' command will be delivered to edge service, it's going to remove rule chain locally.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** |  | |
| **rule_chain_id** | **str** |  | |

### Return type

**RuleChain**


## unset_auto_assign_to_edge_rule_chain

```python
RuleChain client.unset_auto_assign_to_edge_rule_chain(rule_chain_id: str)
```

**DELETE** `/api/ruleChain/{ruleChainId}/autoAssignToEdge`

Unset Auto Assign To Edge Rule Chain (unsetAutoAssignToEdgeRuleChain)

Removes the rule chain from the list of rule chains that are going to be automatically assigned for any new edge that will be created. Does not unassign this rule chain for already assigned edges.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rule_chain_id** | **str** | A string value representing the rule chain id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**RuleChain**

