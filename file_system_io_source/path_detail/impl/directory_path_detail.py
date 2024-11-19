import os

from file_system_io_source.path_detail.abstract_path_detail import Abstract_path_detail

class Directory_path_detail(Abstract_path_detail):
    def __init__(self, path: str, is_user_defined: bool):
        super().__init__(path, is_user_defined)

    def _set_abs_path_impl(self, path):
        processed_path = path
        _, ext = os.path.splitext(path)
        if ext: 
            processed_path = os.path.dirname(path)
            
        self.abs_path = os.path.abspath(processed_path)

    @classmethod
    def create(cls, path, is_user_defined):
        return cls(path, is_user_defined)

    def __str__(self):
        ret_str = "\n//directory path detail////////////\n"
        for k, v in self.__dict__.items():
            ret_str += f'{k.replace('_', '')} : {v}\n'
        ret_str += '/////////////////////\n'
        return ret_str