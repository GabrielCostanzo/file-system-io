import os
from typing import Dict

from file_system_io_operator.impl.file_io_operator.impl.file_reader.file_reader_factory import File_reader_factory
from file_system_io_operator.impl.file_io_operator.impl.file_writer.file_writer_factory import File_writer_factory

from file_system_io_manager.abstract_file_system_io_manager import Abstract_file_system_io_manager
from file_system_io_source.path_detail.impl.directory_path_detail import Directory_path_detail
from file_system_io_source.path_detail.impl.file_path_detail import File_path_detail
from file_system_io_data_strategy.abstract_data_strategy import Abstract_data_strategy

class File_manager(Abstract_file_system_io_manager):
    def __init__(self, 
                 file_path: File_path_detail):
        
        self.reader = File_reader_factory.create(file_path)
        self.writer = File_writer_factory.create(file_path)

        super().__init__(file_path)

    def read(self):        
        return self.reader.read()

    def write(self, new_data: Dict, data_strategy: Abstract_data_strategy):
        write_dict = data_strategy.process_data(
            file_path=self.path,
            file_reader=self.reader, 
            new_data=new_data
        )
        return self.writer.write(write_dict)

    @classmethod
    def create(cls, file_name_with_extension: str, dir_path: Directory_path_detail | str):
        file_name, file_extension = os.path.splitext(file_name_with_extension)

        if isinstance(dir_path, str):
            dir_path_detail = Directory_path_detail.create(path=dir_path)
        else:
            dir_path_detail = dir_path

        file_path_detail = File_path_detail(
            dir_path_detail=dir_path_detail,
            file_name=file_name,
            file_extension=file_extension[1:],
            is_user_defined=False
        )

        base_file_manager = cls(
                                file_path=file_path_detail
                            )

        return base_file_manager
            
