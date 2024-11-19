from abc import abstractmethod
from typing import NoReturn, Union
from file_system_io_operator.abstract_file_system_io_operator import Abstract_file_system_io_operator
from file_system_io_source.path_detail.impl.file_path_detail import File_path_detail


class File_io_operator(Abstract_file_system_io_operator):
    def __init__(self, file_path: File_path_detail):
        super().__init__(file_path)

    def _validate_path_impl(self, path) -> Union[Exception | NoReturn]:
        if not isinstance(path, File_path_detail): raise Exception('File_path_detail is required')

    @classmethod
    @abstractmethod
    def create(cls, file_path: File_path_detail):
        raise NotImplementedError()