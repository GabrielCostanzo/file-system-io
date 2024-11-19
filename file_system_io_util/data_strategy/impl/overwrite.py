from typing import Dict
from file_system_io_source.path_detail.impl.file_path_detail import File_path_detail
from file_system_io_util.data_strategy.data_strategy import Data_strategy

class Overwrite(Data_strategy):
    @staticmethod
    def process_data(file_path: File_path_detail, data: Dict):
        return data