# Зададние 1

import json
import pickle

with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    # (< remote_addr >, < request_type >, < requested_resource >)
    i = 0
    for row in range(10):
        i += 1
        print(i, file.readline(14))
