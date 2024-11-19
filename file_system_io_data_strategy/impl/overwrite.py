from typing import Dict
from file_system_io_source.path_detail.impl.file_path_detail import File_path_detail
from file_system_io.file_system_io_data_strategy.abstract_data_strategy import Abstract_data_strategy

class Overwrite(Abstract_data_strategy):
    @staticmethod
    def process_data(file_path: File_path_detail, data: Dict):
        return data