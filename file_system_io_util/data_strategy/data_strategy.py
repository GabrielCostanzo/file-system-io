from abc import ABC, abstractmethod
from typing import Dict

from file_system_io_source.path_detail.impl.file_path_detail import File_path_detail


class Data_strategy(ABC):
    @staticmethod
    @abstractmethod
    def process_data(file_path: File_path_detail, data: Dict):
        raise NotImplementedError()