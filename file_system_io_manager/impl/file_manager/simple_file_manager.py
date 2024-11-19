import os
from typing import Dict

from file_system_io_operator.impl.file_io_operator.impl.file_reader.file_reader import File_reader
from file_system_io_operator.impl.file_io_operator.impl.file_writer.file_writer import File_writer

from file_system_io_manager.file_system_io_manager import File_system_io_manager
from file_system_io_source.path_detail.impl.directory_path_detail import Directory_path_detail
from file_system_io_source.path_detail.impl.file_path_detail import File_path_detail
from file_system_io_util.data_strategy.data_strategy import Data_strategy

class Simple_file_manager(File_system_io_manager):
    def __init__(self, 
                 file_path: File_path_detail):
        
        self.reader = File_reader.create(file_path)
        self.writer = File_writer.create(file_path)

        super().__init__(file_path)

    def read(self):        
        return self.reader.read()

    def write(self, new_data: Dict, data_strategy: Data_strategy):
        write_dict = data_strategy.process_data(
            file_path=self.path,
            file_reader=self.reader, 
            new_data=new_data
        )
        return self.writer.write(write_dict)

    @classmethod
    def create(cls, file_name_with_extension: str, dir_path_detail: Directory_path_detail):
        
        file_name, file_extension = os.path.splitext(file_name_with_extension)

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
            
