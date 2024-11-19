from typing import NoReturn, Union
from file_system_io.file_system_io_operator.abstract_file_system_io_operator import Abstract_file_system_io_operator
from file_system_io_source.path_detail.impl.directory_path_detail import Directory_path_detail

class Directory_io_operator(Abstract_file_system_io_operator):
    def __init__(self, dir_path: Directory_path_detail):
        super().__init__(dir_path)

    def _validate_path_impl(self, path) -> Union[Exception | NoReturn]:
        if not isinstance(path, Directory_path_detail): raise Exception('Directory_path_detail is required')