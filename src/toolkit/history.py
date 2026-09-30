import json

def load_history():
    """Загрузка истории вычислений из файла json"""
    try:
        text = open("history.json", "r").read()
        return json.loads(text)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_history(history):
    """Сохранение истории вычислений в файл json"""
    open_history = open("history.json","w")
    json.dump(history, open_history, indent = 4)

def add_history(operation: str, expression: str, result: float):
    """Добавление правильных вычислений в историю"""
    history = load_history()
    entry = {"operation": operation,
             "expression": expression,
             "result": result}
    history.append(entry)
    save_history(history)

