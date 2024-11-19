import os

from file_system_io_source.path_detail.path_detail import Path_detail

class File_system_io_manager():
    def __init__(self, path):
        self.path: Path_detail = path

    def exists(self):
        return os.path.exists(self.path.abs_path)

    def __str__(self):
        ret_str = f"\n---{self.__class__.__name__}------------------------\n\n"
        for k, v in self.__dict__.items():
            ret_str += f'{k.replace('_', '')} : {v}\n'
        ret_str += '------------------------------------------\n'
        return ret_str