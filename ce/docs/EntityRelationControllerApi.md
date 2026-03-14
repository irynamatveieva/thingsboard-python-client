# EntityRelationControllerApi

`ThingsboardClient` methods:

```python
EntityRelation client.delete_relation(from_id: str, from_type: str, relation_type: str, to_id: str, to_type: str, relation_type_group: Optional[str] = None)  # Delete Relation (deleteRelation)
None client.delete_relations(entity_id: str, entity_type: str)  # Delete common relations (deleteRelations)
List[EntityRelationInfo] client.find_entity_relation_infos_by_from(from_type: str, from_id: str, relation_type_group: Optional[str] = None)  # Get List of Relation Infos (findEntityRelationInfosByFrom)
List[EntityRelationInfo] client.find_entity_relation_infos_by_query(entity_relations_query: EntityRelationsQuery)  # Find related entity infos (findEntityRelationInfosByQuery)
List[EntityRelationInfo] client.find_entity_relation_infos_by_to(to_type: str, to_id: str, relation_type_group: Optional[str] = None)  # Get List of Relation Infos (findEntityRelationInfosByTo)
List[EntityRelation] client.find_entity_relations_by_from(from_type: str, from_id: str, relation_type_group: Optional[str] = None)  # Get List of Relations (findEntityRelationsByFrom)
List[EntityRelation] client.find_entity_relations_by_from_and_relation_type(from_type: str, from_id: str, relation_type: str, relation_type_group: Optional[str] = None)  # Get List of Relations (findEntityRelationsByFromAndRelationType)
List[EntityRelation] client.find_entity_relations_by_query(entity_relations_query: EntityRelationsQuery)  # Find related entities (findEntityRelationsByQuery)
List[EntityRelation] client.find_entity_relations_by_to(to_type: str, to_id: str, relation_type_group: Optional[str] = None)  # Get List of Relations (findEntityRelationsByTo)
List[EntityRelation] client.find_entity_relations_by_to_and_relation_type(to_type: str, to_id: str, relation_type: str, relation_type_group: Optional[str] = None)  # Get List of Relations (findEntityRelationsByToAndRelationType)
EntityRelation client.get_relation(from_id: str, from_type: str, relation_type: str, to_id: str, to_type: str, relation_type_group: Optional[str] = None)  # Get Relation (getRelation)
EntityRelation client.save_relation(entity_relation: EntityRelation)  # Create Relation (saveRelation)
```


## delete_relation

```python
EntityRelation client.delete_relation(from_id: str, from_type: str, relation_type: str, to_id: str, to_type: str, relation_type_group: Optional[str] = None)
```

**DELETE** `/api/v2/relation`

Delete Relation (deleteRelation)

Deletes a relation between two entities in the platform.   If the user has the authority of 'System Administrator', the server checks that 'from' and 'to' entities are owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that 'from' and 'to' entities are owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the 'from' and 'to' entities are assigned to the same customer.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **from_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **from_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **relation_type** | **str** | A string value representing relation type between entities. For example, 'Contains', 'Manages'. It can be any string value. | |
| **to_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **to_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **relation_type_group** | **str** | A string value representing relation type group. For example, 'COMMON' | [optional] |

### Return type

**EntityRelation**


## delete_relations

```python
None client.delete_relations(entity_id: str, entity_type: str)
```

**DELETE** `/api/relations`

Delete common relations (deleteRelations)

Deletes all the relations ('from' and 'to' direction) for the specified entity and relation type group: 'COMMON'.   If the user has the authority of 'System Administrator', the server checks that the entity is owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that the entity is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the entity is assigned to the same customer.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |

### Return type

None (empty response body)


## find_entity_relation_infos_by_from

```python
List[EntityRelationInfo] client.find_entity_relation_infos_by_from(from_type: str, from_id: str, relation_type_group: Optional[str] = None)
```

**GET** `/api/relations/info/from/{fromType}/{fromId}`

Get List of Relation Infos (findEntityRelationInfosByFrom)

Returns list of relation info objects for the specified entity by the 'from' direction.   If the user has the authority of 'System Administrator', the server checks that the entity is owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that the entity is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the entity is assigned to the same customer. Relation Info is an extension of the default Relation object that contains information about the 'from' and 'to' entity names. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **from_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **from_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **relation_type_group** | **str** | A string value representing relation type group. For example, 'COMMON' | [optional] |

### Return type

**List[EntityRelationInfo]**


## find_entity_relation_infos_by_query

```python
List[EntityRelationInfo] client.find_entity_relation_infos_by_query(entity_relations_query: EntityRelationsQuery)
```

**POST** `/api/relations/info`

Find related entity infos (findEntityRelationInfosByQuery)

Returns all entity infos that are related to the specific entity. The entity id, relation type, entity types, depth of the search, and other query parameters defined using complex 'EntityRelationsQuery' object. See 'Model' tab of the Parameters for more info. Relation Info is an extension of the default Relation object that contains information about the 'from' and 'to' entity names. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_relations_query** | **EntityRelationsQuery** |  | |

### Return type

**List[EntityRelationInfo]**


## find_entity_relation_infos_by_to

```python
List[EntityRelationInfo] client.find_entity_relation_infos_by_to(to_type: str, to_id: str, relation_type_group: Optional[str] = None)
```

**GET** `/api/relations/info/to/{toType}/{toId}`

Get List of Relation Infos (findEntityRelationInfosByTo)

Returns list of relation info objects for the specified entity by the 'to' direction.   If the user has the authority of 'System Administrator', the server checks that the entity is owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that the entity is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the entity is assigned to the same customer. Relation Info is an extension of the default Relation object that contains information about the 'from' and 'to' entity names. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **to_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **to_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **relation_type_group** | **str** | A string value representing relation type group. For example, 'COMMON' | [optional] |

### Return type

**List[EntityRelationInfo]**


## find_entity_relations_by_from

```python
List[EntityRelation] client.find_entity_relations_by_from(from_type: str, from_id: str, relation_type_group: Optional[str] = None)
```

**GET** `/api/relations/from/{fromType}/{fromId}`

Get List of Relations (findEntityRelationsByFrom)

Returns list of relation objects for the specified entity by the 'from' direction.   If the user has the authority of 'System Administrator', the server checks that the entity is owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that the entity is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the entity is assigned to the same customer.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **from_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **from_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **relation_type_group** | **str** | A string value representing relation type group. For example, 'COMMON' | [optional] |

### Return type

**List[EntityRelation]**


## find_entity_relations_by_from_and_relation_type

```python
List[EntityRelation] client.find_entity_relations_by_from_and_relation_type(from_type: str, from_id: str, relation_type: str, relation_type_group: Optional[str] = None)
```

**GET** `/api/relations/from/{fromType}/{fromId}/{relationType}`

Get List of Relations (findEntityRelationsByFromAndRelationType)

Returns list of relation objects for the specified entity by the 'from' direction and relation type.   If the user has the authority of 'System Administrator', the server checks that the entity is owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that the entity is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the entity is assigned to the same customer.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **from_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **from_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **relation_type** | **str** | A string value representing relation type between entities. For example, 'Contains', 'Manages'. It can be any string value. | |
| **relation_type_group** | **str** | A string value representing relation type group. For example, 'COMMON' | [optional] |

### Return type

**List[EntityRelation]**


## find_entity_relations_by_query

```python
List[EntityRelation] client.find_entity_relations_by_query(entity_relations_query: EntityRelationsQuery)
```

**POST** `/api/relations`

Find related entities (findEntityRelationsByQuery)

Returns all entities that are related to the specific entity. The entity id, relation type, entity types, depth of the search, and other query parameters defined using complex 'EntityRelationsQuery' object. See 'Model' tab of the Parameters for more info.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_relations_query** | **EntityRelationsQuery** |  | |

### Return type

**List[EntityRelation]**


## find_entity_relations_by_to

```python
List[EntityRelation] client.find_entity_relations_by_to(to_type: str, to_id: str, relation_type_group: Optional[str] = None)
```

**GET** `/api/relations/to/{toType}/{toId}`

Get List of Relations (findEntityRelationsByTo)

Returns list of relation objects for the specified entity by the 'to' direction.   If the user has the authority of 'System Administrator', the server checks that the entity is owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that the entity is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the entity is assigned to the same customer.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **to_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **to_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **relation_type_group** | **str** | A string value representing relation type group. For example, 'COMMON' | [optional] |

### Return type

**List[EntityRelation]**


## find_entity_relations_by_to_and_relation_type

```python
List[EntityRelation] client.find_entity_relations_by_to_and_relation_type(to_type: str, to_id: str, relation_type: str, relation_type_group: Optional[str] = None)
```

**GET** `/api/relations/to/{toType}/{toId}/{relationType}`

Get List of Relations (findEntityRelationsByToAndRelationType)

Returns list of relation objects for the specified entity by the 'to' direction and relation type.   If the user has the authority of 'System Administrator', the server checks that the entity is owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that the entity is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the entity is assigned to the same customer.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **to_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **to_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **relation_type** | **str** | A string value representing relation type between entities. For example, 'Contains', 'Manages'. It can be any string value. | |
| **relation_type_group** | **str** | A string value representing relation type group. For example, 'COMMON' | [optional] |

### Return type

**List[EntityRelation]**


## get_relation

```python
EntityRelation client.get_relation(from_id: str, from_type: str, relation_type: str, to_id: str, to_type: str, relation_type_group: Optional[str] = None)
```

**GET** `/api/relation`

Get Relation (getRelation)

Returns relation object between two specified entities if present. Otherwise throws exception.   If the user has the authority of 'System Administrator', the server checks that 'from' and 'to' entities are owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that 'from' and 'to' entities are owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the 'from' and 'to' entities are assigned to the same customer.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **from_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **from_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **relation_type** | **str** | A string value representing relation type between entities. For example, 'Contains', 'Manages'. It can be any string value. | |
| **to_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **to_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **relation_type_group** | **str** | A string value representing relation type group. For example, 'COMMON' | [optional] |

### Return type

**EntityRelation**


## save_relation

```python
EntityRelation client.save_relation(entity_relation: EntityRelation)
```

**POST** `/api/v2/relation`

Create Relation (saveRelation)

Creates or updates a relation between two entities in the platform. Relations unique key is a combination of from/to entity id and relation type group and relation type.   If the user has the authority of 'System Administrator', the server checks that 'from' and 'to' entities are owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that 'from' and 'to' entities are owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the 'from' and 'to' entities are assigned to the same customer.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_relation** | **EntityRelation** |  | |

### Return type

**EntityRelation**

