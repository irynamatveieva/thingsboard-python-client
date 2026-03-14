# SolutionControllerApi

`ThingsboardClient` methods:

```python
TenantSolutionTemplateDetails client.get_solution_template_details(solution_template_id: str)  # Get Solution template details (getSolutionTemplateDetails)
List[TenantSolutionTemplateInfo] client.get_solution_template_infos()  # Get Solution templates (getSolutionTemplateInfos)
TenantSolutionTemplateInstructions client.get_solution_template_instructions(solution_template_id: str)  # Get Solution Template Instructions (getSolutionTemplateInstructions)
SolutionInstallResponse client.install_solution_template(solution_template_id: str)  # Install Solution Template (installSolutionTemplate)
None client.uninstall_solution_template(solution_template_id: str)  # Uninstall Solution Template (uninstallSolutionTemplate)
```


## get_solution_template_details

```python
TenantSolutionTemplateDetails client.get_solution_template_details(solution_template_id: str)
```

**GET** `/api/solutions/templates/details/{solutionTemplateId}`

Get Solution template details (getSolutionTemplateDetails)

Get a solution template details based on the provided id   Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **solution_template_id** | **str** | A string value representing the solution template id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**TenantSolutionTemplateDetails**


## get_solution_template_infos

```python
List[TenantSolutionTemplateInfo] client.get_solution_template_infos()
```

**GET** `/api/solutions/templates/infos`

Get Solution templates (getSolutionTemplateInfos)

Get a list of solution template descriptors   Security check is performed to verify that the user has 'READ' permission for the entity (entities).

### Return type

**List[TenantSolutionTemplateInfo]**


## get_solution_template_instructions

```python
TenantSolutionTemplateInstructions client.get_solution_template_instructions(solution_template_id: str)
```

**GET** `/api/solutions/templates/instructions/{solutionTemplateId}`

Get Solution Template Instructions (getSolutionTemplateInstructions)

Get a solution template instructions based on the provided id   Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **solution_template_id** | **str** | A string value representing the solution template id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**TenantSolutionTemplateInstructions**


## install_solution_template

```python
SolutionInstallResponse client.install_solution_template(solution_template_id: str)
```

**POST** `/api/solutions/templates/{solutionTemplateId}/install`

Install Solution Template (installSolutionTemplate)

Install solution template based on the provided id   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **solution_template_id** | **str** | A string value representing the solution template id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**SolutionInstallResponse**


## uninstall_solution_template

```python
None client.uninstall_solution_template(solution_template_id: str)
```

**DELETE** `/api/solutions/templates/{solutionTemplateId}/delete`

Uninstall Solution Template (uninstallSolutionTemplate)

Uninstall solution template based on the provided id   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **solution_template_id** | **str** | A string value representing the solution template id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)

