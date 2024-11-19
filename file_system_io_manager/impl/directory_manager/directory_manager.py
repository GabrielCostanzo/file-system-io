

from file_system_io.file_system_io_manager.abstract_file_system_io_manager import Abstract_file_system_io_manager
from file_system_io_operator.impl.directory_io_operator.impl.directory_creator import Directory_creator
from file_system_io_operator.impl.directory_io_operator.impl.directory_remover import Directory_remover
from file_system_io_source.path_detail.impl.directory_path_detail import Directory_path_detail

class Directory_manager(Abstract_file_system_io_manager):
    def __init__(self, 
                 dir_path: Directory_path_detail,
                 allow_existing_creation: bool,
                 allow_missing_removal, 
                 permission_mode):

        self.allow_existing_creation = allow_existing_creation
        self.allow_missing_removal = allow_missing_removal

        self.creator: Directory_creator = Directory_creator(dir_path, self.allow_existing_creation)
        self.remover: Directory_remover = Directory_remover(dir_path, self.allow_missing_removal)

        super().__init__(dir_path)

    def create(self):
        self.creator.create()

    def remove(self):
        self.remover.remove()

    def clear_contents(self):
        self.remove()
        self.create()

    @classmethod
    def create_instance(cls, dir_path: str):
    
        dir_path_detail = Directory_path_detail(
            path=dir_path,
            is_user_defined=False
        )

        base_directory_manager = Directory_manager(
            dir_path=dir_path_detail,
            allow_existing_creation=True,
            allow_missing_removal=True,
            permission_mode=None
        )

        return base_directory_manager