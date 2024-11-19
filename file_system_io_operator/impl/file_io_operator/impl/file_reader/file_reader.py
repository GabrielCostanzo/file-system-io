from file_system_io_operator.impl.file_io_operator.file_io_operator import File_io_operator
from file_system_io_source.path_detail.impl.file_path_detail import File_path_detail
from abc import abstractmethod
from typing import Dict

class File_reader(File_io_operator):
    def __init__(self, file_path: File_path_detail):
        super().__init__(file_path)
    
    def read(self) -> Dict:
        try:
            return self._read_impl()
        except Exception as e:
            raise Exception(f' failed reading file: {self.path.abs_path}\n')

    @abstractmethod
    def _read_impl(self) -> Dict:
        raise NotImplementedError()