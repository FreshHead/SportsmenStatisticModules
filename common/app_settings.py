import yaml


class AppSettings:
    def __init__(self):
        with open('config.yml', 'rt') as fin:
            text = fin.read()
        data = yaml.safe_load(text)
        self.log_filename = data['logging']['filename']
        self.log_level = data['logging']['level']
        self.file_type = data['file']['type']
