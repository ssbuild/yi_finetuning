# -*- coding: utf-8 -*-
# @Time:  23:20
# @Author: tk
# @File：model_maps
from aigc_zoo.constants.define import (TRANSFORMERS_MODELS_TO_LORA_TARGET_MODULES_MAPPING,
                                       TRANSFORMERS_MODELS_TO_ADALORA_TARGET_MODULES_MAPPING,
                                       TRANSFORMERS_MODELS_TO_IA3_TARGET_MODULES_MAPPING,
                                       TRANSFORMERS_MODELS_TO_IA3_FEEDFORWARD_MODULES_MAPPING)

__all__ = [
    "TRANSFORMERS_MODELS_TO_LORA_TARGET_MODULES_MAPPING",
    "TRANSFORMERS_MODELS_TO_ADALORA_TARGET_MODULES_MAPPING",
    "TRANSFORMERS_MODELS_TO_IA3_TARGET_MODULES_MAPPING",
    "TRANSFORMERS_MODELS_TO_IA3_FEEDFORWARD_MODULES_MAPPING",
    "MODELS_MAP"
]

MODELS_MAP = {

    'Yi-6B': {
        'model_type': 'Yi',
        'model_name_or_path': '/data/nlp/pre_models/torch/yi/Yi-6B',
        'config_name': '/data/nlp/pre_models/torch/yi/Yi-6B/config.json',
        'tokenizer_name': '/data/nlp/pre_models/torch/yi/Yi-6B',
    },
   
    'Yi-34B': {
        'model_type': 'Yi',
        'model_name_or_path': '/data/nlp/pre_models/torch/yi/Yi-34B',
        'config_name': '/data/nlp/pre_models/torch/yi/Yi-34B/config.json',
        'tokenizer_name': '/data/nlp/pre_models/torch/yi/Yi-34B',
    },
}


# 按需修改
# TRANSFORMERS_MODELS_TO_LORA_TARGET_MODULES_MAPPING
# TRANSFORMERS_MODELS_TO_ADALORA_TARGET_MODULES_MAPPING
# TRANSFORMERS_MODELS_TO_IA3_TARGET_MODULES_MAPPING
# TRANSFORMERS_MODELS_TO_IA3_FEEDFORWARD_MODULES_MAPPING




