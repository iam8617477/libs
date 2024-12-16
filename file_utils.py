import json


class FileReadWrite:

    @staticmethod
    def read(file_path, mode='r'):
        with open(file_path, mode) as file:
            return file.read()

    @staticmethod
    def write(file_path, content, mode='w'):
        with open(file_path, mode) as file:
            return file.write(content)

    @staticmethod
    def write_json(file_path, data):
        with open(file_path, 'w') as json_file:
            return json.dump(data, json_file)

    @staticmethod
    def read_json(file_path):
        with open(file_path, 'r') as json_file:
            return json.load(json_file)
