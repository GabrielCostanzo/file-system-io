import shutil

from file_system_io_operator.impl.directory_io_operator.directory_io_operator import Directory_io_operator
from file_system_io_source.path_detail.impl.directory_path_detail import Directory_path_detail

class Directory_remover(Directory_io_operator):
    def __init__(self, 
                 dir_path: Directory_path_detail,
                 allow_missing: bool):

        self.allow_missing = allow_missing

        super().__init__(dir_path)

    def remove(self):
        try:
            shutil.rmtree(self.path.abs_path)

        except FileNotFoundError:
            if not self.allow_missing: 
                raise