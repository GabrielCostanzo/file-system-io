from file_system_io_source.path_detail.impl.directory_path_detail import Directory_path_detail
from file_system_io_source.path_detail.path_detail import Path_detail
from file_system_io_util.file_system_io_util import get_validated_file_type
import os

class File_path_detail(Path_detail):
    def __init__(self, 
                 dir_path_detail: Directory_path_detail, 
                 file_name: str, 
                 file_extension:str,
                 is_user_defined:bool):
    
        self.dir_path_detail = dir_path_detail
        self.file_name = file_name
        self.file_extension = file_extension

        abs_path = os.path.join(dir_path_detail.abs_path, f'{self.file_name}.{self.file_extension}')
        super().__init__(abs_path, is_user_defined)

    def _set_abs_path_impl(self, path):
        processed_path = path
        _, ext = os.path.splitext(path)

        if not ext: 
            raise Exception('path is not a file')
            
        self.abs_path = os.path.abspath(processed_path)


    @staticmethod
    def _get_file_path_detail_components(path, is_user_defined):
        try:
            dir_path_detail = Directory_path_detail(path, is_user_defined)
            file_name_with_ext = os.path.split(path)[1]
            file_name = os.path.splitext(file_name_with_ext)[0]
            ret_ext = get_validated_file_type(path).value

            return dir_path_detail, file_name, ret_ext
        
        except Exception as e:
            raise Exception(f'failed to get file path detail components from path: {path}')
        
    @classmethod
    def create(cls, path:str, is_user_defined: bool):

        dir_path_detail, file_name, file_extension = File_path_detail._get_file_path_detail_components(path, is_user_defined)

        return cls(dir_path_detail=dir_path_detail, 
                   file_name=file_name, 
                   file_extension=file_extension,
                   is_user_defined=is_user_defined)

    @classmethod
    def create_from_components(cls, 
                               target_dir: Directory_path_detail | str, 
                               file_name: str, 
                               file_extension:str,
                               is_user_defined:bool):
        
        dir_path_detail = target_dir
        if isinstance(target_dir, str): dir_path_detail = Directory_path_detail(target_dir, is_user_defined)

        ret_ext = get_validated_file_type(f'{file_name}.{file_extension}').value

        return cls(dir_path_detail=dir_path_detail, 
                   file_name=file_name, 
                   file_extension=ret_ext,
                   is_user_defined=is_user_defined)

    def __str__(self):
        ret_str = "\n---file path detail------------------------\n\n"
        base_dir_str = '\n+/+/ base dir detail +/+/+/+/+/+/+/+/+/\n\n'
        for k, v in self.__dict__.items():
            if isinstance(v, Directory_path_detail):
                for j, k in v.__dict__.items():
                    base_dir_str += f'{j.replace('_', '')} : {k}\n'
                base_dir_str += '\n+/+/+/+/+/+/+/+/+/+/+/+/+/+/\n\n'
                continue
            ret_str += f'{k.replace('_', '')} : {v}\n'
        ret_str += base_dir_str
        ret_str += '------------------------------------------\n'
        return ret_str