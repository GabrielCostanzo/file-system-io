from abc import ABC, abstractmethod
from typing import NoReturn, Union
import os

class Path_detail(ABC):
    def __init__(self, 
                 path: str, 
                 is_user_defined: bool):
        
        self.abs_path = None 
        self.is_user_defined = is_user_defined
        self._validate_abs_path(path)

    def _set_abs_path(self, path):
        if not path: return
        self._set_abs_path_impl(path)

    def _validate_abs_path(self, path) -> Union[Exception | NoReturn]:
        try:
            self._set_abs_path(path)
            if not self.abs_path: raise Exception('missing required path')
            if not os.path.isabs(self.abs_path): raise Exception()

        except Exception as e:
            raise Exception('failed to validate absolute path')

    @abstractmethod
    def _set_abs_path_impl(self, path):
        raise NotImplementedError()
    
    @classmethod
    @abstractmethod
    def create(cls, path:str, is_user_defined: bool):
        raise NotImplementedError()