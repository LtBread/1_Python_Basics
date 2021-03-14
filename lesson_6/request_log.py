import requests


def get_logs():
    response = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
    content = response.content.decode(encoding=response.encoding)
    return content


def save_logs(logs):
    with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
        f.write(logs)


if __name__ == '__main__':
    save_logs(get_logs())
