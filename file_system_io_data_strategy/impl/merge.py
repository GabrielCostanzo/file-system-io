from typing import Dict
from file_system_io_source.path_detail.impl.file_path_detail import File_path_detail
from file_system_io_data_strategy.abstract_data_strategy import Abstract_data_strategy
from file_system_io_operator.impl.file_io_operator.impl.file_reader.file_reader_factory import File_reader_factory

class Merge(Abstract_data_strategy):
    @staticmethod
    def process_data(file_path: File_path_detail, data: Dict):
        existing_data = File_reader_factory.create(file_path=file_path).read()
        return Merge._merge_data(existing_data, data)

    @staticmethod
    def _merge_data(existing_data: Dict, new_data: Dict):
        result = existing_data.copy()
        for key, value in new_data.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = Merge._merge_data(result[key], value)
            else:
                result[key] = value
        return result