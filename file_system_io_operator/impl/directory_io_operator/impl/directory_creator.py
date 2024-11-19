import os

from file_system_io_operator.impl.directory_io_operator.directory_io_operator import Directory_io_operator
from file_system_io_source.path_detail.impl.directory_path_detail import Directory_path_detail

class Directory_creator(Directory_io_operator):
    def __init__(self, 
                 dir_path: Directory_path_detail,
                 allow_existing: bool, 
                 permission_mode: int | None = None):
    
        self.allow_existing = allow_existing
        self.permission_mode = permission_mode
    
        super().__init__(dir_path)

    def create(self):
        if self.permission_mode:
            os.makedirs(self.path.abs_path, 
                        mode=self.permission_mode, 
                        exist_ok=self.allow_existing)
        else:
            os.makedirs(self.path.abs_path, 
                        exist_ok=self.allow_existing)