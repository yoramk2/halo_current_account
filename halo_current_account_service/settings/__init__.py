import os
import json

print("start init")

ENV_CONFIG = {"loc":"loc"}
STAGE = "loc"
STAGEX = "loc"

if 'AWS_LAMBDA_FUNCTION_NAME' in os.environ:
    if 'HALO_STAGE' in os.environ:
        STAGE = os.environ['HALO_STAGE']
    if STAGE is not None:
        ENV_SETTINGS = 'env_settings.json'
        file_dir = os.path.dirname(__file__)
        file_path = os.path.join(file_dir,'..','..','env', ENV_SETTINGS)
        with open(file_path, 'r') as fi:
            API_CONFIG = json.load(fi)
            print("env_config:" + str(API_CONFIG))
        if STAGE in API_CONFIG:
            STAGEX = API_CONFIG[STAGE]
        else:
            raise Exception(file_path+" does not contain environment "+STAGE)

        if STAGEX == 'dev':
            from .development import *
        else:
            if STAGEX == 'tst':
                from .test import *
            else:
                if STAGEX == 'prd':
                    from .production import *
    else:
        raise Exception("can not get environment ver STAGE")
else:
    from .local import *