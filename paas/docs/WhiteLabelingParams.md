
# WhiteLabelingParams

`tb_paas_client.models.WhiteLabelingParams`

A JSON value representing the white labeling configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **logo_image_url** | **str** | Logo image URL | [optional] |
| **logo_image_height** | **int** | The height of a logo container. Logo image will be automatically scaled. | [optional] |
| **app_title** | **str** | White-labeled name of the platform | [optional] |
| **favicon** | [**Favicon**](Favicon.md) | JSON object that contains website icon url and type | [optional] |
| **palette_settings** | [**PaletteSettings**](PaletteSettings.md) | Complex JSON that describes structure of the Angular Material Palette. See [theming](https://material.angular.io/guide/theming) for more details | [optional] |
| **help_link_base_url** | **str** | Base URL for help link | [optional] |
| **ui_help_base_url** | **str** | Base URL for the repository with the UI help components (markdown) | [optional] |
| **enable_help_links** | **bool** | Enable or Disable help links | [optional] |
| **white_labeling_enabled** | **bool** | Enable white-labeling | [optional] [readonly] |
| **show_name_version** | **bool** | Show platform name and version on UI and login screen | [optional] |
| **platform_name** | **str** | White-labeled platform name | [optional] |
| **platform_version** | **str** | White-labeled platform version | [optional] |
| **custom_css** | **str** | Custom CSS content | [optional] |
| **hide_connectivity_dialog** | **bool** | Hide device connectivity dialog | [optional] |
| **override_trendz_name** | **bool** | Override Trendz Add-on name | [optional] |
| **hide_chat_bot** | **bool** | Hide chat bot | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.logo_image_url`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `WhiteLabelingParams.model_validate(data)` or `WhiteLabelingParams.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

