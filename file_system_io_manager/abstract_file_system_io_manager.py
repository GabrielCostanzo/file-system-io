import os
from abc import ABC
from file_system_io_source.path_detail.abstract_path_detail import Abstract_path_detail

class Abstract_file_system_io_manager(ABC):
    def __init__(self, path):
        self.path: Abstract_path_detail = path

    def exists(self):
        return os.path.exists(self.path.abs_path)

    def __str__(self):
        ret_str = f"\n---{self.__class__.__name__}------------------------\n\n"
        for k, v in self.__dict__.items():
            ret_str += f'{k.replace('_', '')} : {v}\n'
        ret_str += '------------------------------------------\n'
        return ret_str