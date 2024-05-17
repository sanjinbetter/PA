import yaml
import os
import sys


class YamlConfig:
    _application_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    _config_path = f"{_application_dir}/config.yaml"

    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(YamlConfig, cls).__new__(cls)
            cls._load_all_config(cls._instance,config_path=cls._config_path)

        return cls._instance
    
    def _load_all_config(self,config_path):
        try:
            #加载主配置
            config = self.yaml_load(config_path=config_path)

            #加载环境配置
            env = config["application"]["env"]
            if env is None:
                raise Exception("未配置环境")
            
            env_config_path = f"{self._application_dir}/config-{env}.yaml"
            env_config = self.yaml_load(config_path=env_config_path)

            print(env_config)

            #合并配置，配置冲突以环境配置为准
        
            config.update(env_config)

            self._instance._config = config
        except Exception as e:
            raise Exception(f"加载应用配置异常。config_path:{config_path},exception:{e}")

    def yaml_load(self,config_path):
        try:
            with open(config_path,"r") as f:
                config = yaml.safe_load(f)

            return config
        except Exception as e:
            raise Exception(f"加载配置文件异常。config_path:{config_path},exception:{e}")

    def __getattr__(self,name):
        if self._instance._config and name in self._instance._config:
            return self._instance._config[name]
        raise AttributeError(f"配置文件中不存在该属性 {name}")