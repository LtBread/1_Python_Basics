# Зададние 1

import json
import pickle

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    # (< remote_addr >, < request_type >, < requested_resource >)
    print(f.read())
