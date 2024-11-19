

from file_system_io_operator.impl.file_io_operator.impl.file_writer.impl.json_file_writer import Json_file_writer
from file_system_io_operator.impl.file_io_operator.impl.file_writer.impl.yaml_file_writer import Yaml_file_writer
from file_system_io_operator.impl.file_io_operator.enum.supported_file_extension import Supported_file_extension
from file_system_io_source.path_detail.impl.file_path_detail import File_path_detail

class File_writer_factory():
    @classmethod
    def create(cls, file_path: File_path_detail):
        if not isinstance(file_path, File_path_detail):
            raise TypeError('File_path_detail is required for File_writer creation')
        
        match file_path.file_extension:
            case Supported_file_extension.YAML.value:
                return Yaml_file_writer(file_path)
            
            case Supported_file_extension.JSON.value:
                return Json_file_writer(file_path)

            case _:
                raise Exception('failed to create File_writer')