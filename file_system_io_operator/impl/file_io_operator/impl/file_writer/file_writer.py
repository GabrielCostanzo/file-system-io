from file_system_io_operator.impl.file_io_operator.file_io_operator import File_io_operator
from file_system_io_source.path_detail.impl.file_path_detail import File_path_detail
from abc import abstractmethod
from typing import Dict

class File_writer(File_io_operator):
    def __init__(self, file_path: File_path_detail):
        super().__init__(file_path)

    def write(self, 
              data: Dict):    
        try:
            self._write_impl(data)
        except Exception as e:
            raise Exception(f' failed writing file: {self.path.abs_path}\n')

    @abstractmethod
    def _write_impl(self):
        raise NotImplementedError()