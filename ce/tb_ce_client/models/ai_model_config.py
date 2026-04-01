#
# Copyright © 2026-2026 ThingsBoard, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from importlib import import_module
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tb_ce_client.models.amazon_bedrock_chat_model_config import AmazonBedrockChatModelConfig
    from tb_ce_client.models.anthropic_chat_model_config import AnthropicChatModelConfig
    from tb_ce_client.models.azure_open_ai_chat_model_config import AzureOpenAiChatModelConfig
    from tb_ce_client.models.git_hub_models_chat_model_config import GitHubModelsChatModelConfig
    from tb_ce_client.models.google_ai_gemini_chat_model_config import GoogleAiGeminiChatModelConfig
    from tb_ce_client.models.google_vertex_ai_gemini_chat_model_config import GoogleVertexAiGeminiChatModelConfig
    from tb_ce_client.models.mistral_ai_chat_model_config import MistralAiChatModelConfig
    from tb_ce_client.models.ollama_chat_model_config import OllamaChatModelConfig
    from tb_ce_client.models.open_ai_chat_model_config import OpenAiChatModelConfig

class AiModelConfig(BaseModel):
    """
    Root configuration for AI models
    """ # noqa: E501
    provider: StrictStr
    __properties: ClassVar[List[str]] = ["provider"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'provider'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'AMAZON_BEDROCK': 'AmazonBedrockChatModelConfig','ANTHROPIC': 'AnthropicChatModelConfig','AZURE_OPENAI': 'AzureOpenAiChatModelConfig','GITHUB_MODELS': 'GitHubModelsChatModelConfig','GOOGLE_AI_GEMINI': 'GoogleAiGeminiChatModelConfig','GOOGLE_VERTEX_AI_GEMINI': 'GoogleVertexAiGeminiChatModelConfig','MISTRAL_AI': 'MistralAiChatModelConfig','OLLAMA': 'OllamaChatModelConfig','OPENAI': 'OpenAiChatModelConfig'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.model_dump(by_alias=False, mode='json'))

    def __str__(self) -> str:
        return self.to_str()

    def __repr__(self) -> str:
        return self.to_str()

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Union[AmazonBedrockChatModelConfig, AnthropicChatModelConfig, AzureOpenAiChatModelConfig, GitHubModelsChatModelConfig, GoogleAiGeminiChatModelConfig, GoogleVertexAiGeminiChatModelConfig, MistralAiChatModelConfig, OllamaChatModelConfig, OpenAiChatModelConfig]]:
        """Create an instance of AiModelConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[AmazonBedrockChatModelConfig, AnthropicChatModelConfig, AzureOpenAiChatModelConfig, GitHubModelsChatModelConfig, GoogleAiGeminiChatModelConfig, GoogleVertexAiGeminiChatModelConfig, MistralAiChatModelConfig, OllamaChatModelConfig, OpenAiChatModelConfig]]:
        """Create an instance of AiModelConfig from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'AmazonBedrockChatModelConfig':
            return import_module("tb_ce_client.models.amazon_bedrock_chat_model_config").AmazonBedrockChatModelConfig.from_dict(obj)
        if object_type ==  'AnthropicChatModelConfig':
            return import_module("tb_ce_client.models.anthropic_chat_model_config").AnthropicChatModelConfig.from_dict(obj)
        if object_type ==  'AzureOpenAiChatModelConfig':
            return import_module("tb_ce_client.models.azure_open_ai_chat_model_config").AzureOpenAiChatModelConfig.from_dict(obj)
        if object_type ==  'GitHubModelsChatModelConfig':
            return import_module("tb_ce_client.models.git_hub_models_chat_model_config").GitHubModelsChatModelConfig.from_dict(obj)
        if object_type ==  'GoogleAiGeminiChatModelConfig':
            return import_module("tb_ce_client.models.google_ai_gemini_chat_model_config").GoogleAiGeminiChatModelConfig.from_dict(obj)
        if object_type ==  'GoogleVertexAiGeminiChatModelConfig':
            return import_module("tb_ce_client.models.google_vertex_ai_gemini_chat_model_config").GoogleVertexAiGeminiChatModelConfig.from_dict(obj)
        if object_type ==  'MistralAiChatModelConfig':
            return import_module("tb_ce_client.models.mistral_ai_chat_model_config").MistralAiChatModelConfig.from_dict(obj)
        if object_type ==  'OllamaChatModelConfig':
            return import_module("tb_ce_client.models.ollama_chat_model_config").OllamaChatModelConfig.from_dict(obj)
        if object_type ==  'OpenAiChatModelConfig':
            return import_module("tb_ce_client.models.open_ai_chat_model_config").OpenAiChatModelConfig.from_dict(obj)

        raise ValueError("AiModelConfig failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


