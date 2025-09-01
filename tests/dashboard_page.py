import yaml
from pages.dashboard_page import DasboardPage

def get_config():
    with open("config/config.yaml", "r") as f:
    return yaml.safe_load(f)

def
