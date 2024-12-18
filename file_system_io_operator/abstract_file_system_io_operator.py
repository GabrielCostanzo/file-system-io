from abc import ABC, abstractmethod
from typing import Union, NoReturn
from file_system_io_source.path_detail.abstract_path_detail import Abstract_path_detail

class Abstract_file_system_io_operator(ABC):
    def __init__(self, path: Abstract_path_detail):
        self._validate_path(path)
        self.path = path
    
    def _validate_path(self, path) -> Union[Exception | NoReturn]:
        if not path: raise Exception('missing required path')
        if not isinstance(path, Abstract_path_detail): raise('Path_detail is required')
        self._validate_path_impl(path)
    
    @abstractmethod
    def _validate_path_impl(self, path) -> Union[Exception | NoReturn]:
        raise NotImplementedError()

    def __str__(self):
        ret_str = f"\n---{self.__class__.__name__}------------------------\n\n"
        for k, v in self.__dict__.items():
            ret_str += f'{k.replace('_', '')} : {v}\n'
        ret_str += '------------------------------------------\n'
        return ret_str