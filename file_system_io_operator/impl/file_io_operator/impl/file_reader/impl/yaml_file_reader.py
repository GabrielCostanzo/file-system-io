from typing import Dict
from file_system_io_operator.impl.file_io_operator.impl.file_reader.file_reader import File_reader
from file_system_io_source.path_detail.impl.file_path_detail import File_path_detail
import yaml

class Yaml_file_reader(File_reader):
    def __init__(self, file_path: File_path_detail):
        super().__init__(file_path)

    def _read_impl(self) -> Dict:
        with open(self.path.abs_path, 'r') as _file:
            try:
                yaml_obj = yaml.safe_load(_file)
                return yaml_obj

            except yaml.YAMLError:
                raise Exception(f" YAML Error while reading file: {self.path.abs_path}")