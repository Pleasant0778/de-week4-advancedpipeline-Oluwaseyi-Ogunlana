
import pytest
from pipeline.config import ConfigManager  
import configparser

def test_config_manager_reads_values(tmp_path):
    config_path = tmp_path / "pipeline.cfg"
    config_write = configparser.ConfigParser()

    config_write['API_ENDPOINT'] = {}

    config_write['API_ENDPOINT']['limit'] = '1' 
    config_write['API_ENDPOINT']['url'] = 'https://fakestoreapi.com/' 
    with open(config_path, 'w') as config_file:
        config_write.write(config_file)

    config_manager = ConfigManager(config_path, 'API_ENDPOINT')
    config_read = config_manager.read_api_config()


    assert config_read.get("url", None) == "https://fakestoreapi.com/"
    assert config_read.get("limit", None) == "1"

    