import json 

def load_server_config():
    with open('settings.json', 'r') as file:
        data = json.load(file)
    return data

setting = load_server_config()
server_ip = setting['server_ip']
server_port = setting['server_port']