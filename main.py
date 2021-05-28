import os

import requests

from pprint import pprint

TOKEN = ' '

class YaUploader:

    def __init__(self, token, file_path):
        self.token = token
        self.file_path = file_path


    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
    def _get_upload(self, disk_file_path):
        uploud_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(uploud_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def uploud_to_disk(self, disk_file_path):
        href = self._get_upload(disk_file_path=disk_file_path).get('href', )
        response = requests.put(href, data=open(self.file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Файл успешно загружен')


if __name__ == '__main__':
    uploader = YaUploader(token=TOKEN, file_path= os.path.join(os.getcwd(), 'test.txt'))
    uploader.uploud_to_disk(disk_file_path='Neto_study/test.txt.')
