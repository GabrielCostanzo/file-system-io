import json
from typing import Dict
from file_system_io_operator.impl.file_io_operator.impl.file_reader.file_reader import File_reader
from file_system_io_source.path_detail.impl.file_path_detail import File_path_detail

class Json_file_reader(File_reader):
    def __init__(self, file_path: File_path_detail):
        super().__init__(file_path)

    def _read_impl(self) -> Dict:
        with open(self.path.abs_path, 'r') as file:
            try: 
                json_obj = json.load(file)
                return json_obj
            
            except json.JSONDecodeError:
                raise Exception(f" JSON Decode Error while reading file: {self.path.abs_path}")