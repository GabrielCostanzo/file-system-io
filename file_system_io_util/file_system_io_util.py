from file_system_io_operator.impl.file_io_operator.enum.supported_file_extension import Supported_file_extension
import os

def get_validated_file_type(filepath):
    filename, extension = os.path.splitext(filepath)
    file_type = extension[1:]  # Remove the dot from the extension

    try:
        return Supported_file_extension[file_type.upper()]
    except KeyError:
        raise Exception(f' file type: [{file_type}] is not supported for path: {filepath}')
