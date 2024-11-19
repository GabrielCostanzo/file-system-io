from typing import Dict
from file_system_io_operator.impl.file_io_operator.impl.file_writer.file_writer import File_writer
from file_system_io_source.path_detail.impl.file_path_detail import File_path_detail
import yaml

class Yaml_file_writer(File_writer):
    def __init__(self, file_path: File_path_detail):
        super().__init__(file_path)

    def _write_impl(self, data: Dict):
        with open(self.path.abs_path, 'w') as _file:
            yaml.dump(data, _file, default_flow_style=False)