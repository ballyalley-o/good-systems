import os
import requests
import json
from colorama import Fore, Style
from logic.constants.constants import *
from dotenv import load_dotenv
load_dotenv()


token = os.getenv('GIT_TOKEN')
gist_id = os.getenv('GIST_ID')
filename = os.getenv('GIST_FILENAME')

content = os.getenv('PATH_GIST_MD')
content = open(content, 'r').read()


url = f'{os.getenv('GIST_API')}{gist_id}'

headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json',
}

data = {
    'files': {
        filename: {
            'content': content
        }
    }
}

response = requests.patch(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    print('\n')
    print(f'{Fore.LIGHTYELLOW_EX} + {RESPONSE_SUCCESS.format(response.json()['html_url'])} + {Style.RESET_ALL}')
    print('\n')
else:
    print('\n')
    print(f'{Fore.RED} {RESPONSE_FAILED} {Style.RESET_ALL}', response.content)
    print('\n')