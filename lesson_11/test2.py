import re


def email_parse(address):
    pattern = re.compile(r'(?P<user_name>\w+)[@](?P<domain>\w+\.\w+$)')
    result = pattern.match(address)
    if not result:
        raise ValueError(f'wrong email: {address}')
    return result.groupdict()


if __name__ == '__main__':
    email_address = 'primebox21@gmail.com'
    try:
        print(email_parse(email_address))
    except ValueError as e:
        print(e)
        exit(1)
