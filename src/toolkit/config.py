import json

def load_config():
    """Загрузка конфигурации из файла JSOn"""
    constants = open("config.json","r")
    return json.load(constants)