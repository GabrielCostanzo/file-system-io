# file-system-io

This package bundle data access features and provides a class `Abstract_file_system_io_manager`

## Usage

### Directory Control

class: `Directory_manager`

consists of: (Directory_creator, Directory_remover)

public methods:

- create()
- remove()
- clear_contents()

creation (class method):

`Directory_manager.create_instance(dir_path)`

- dir_path: `str` or `Directory_path_detail`

### File Control

class: `File_manager`

consists of: (File_reader, File_writer)

public methods:

- read()
- write()

creation (class method):
`File_manager.create(file_name_with_extension, dir_path)`

- file_name_with_extension: `str`
- dir_path: `str` or `Directory_path_detail`

### Source object mapping

class: `Directory_path_detail`

consists of: (abs_path, is_user_defined)

public methods: N/A

creation (class method):
`Directory_path_detail.create(path, is_user_defined)`

- path: `str`
- is_user_defined: `boolean`
