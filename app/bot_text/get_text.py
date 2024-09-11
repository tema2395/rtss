import yaml

def load_text():
    with open('text.yaml', 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)
    
    
text_cfg = load_text()
    