# file-system-io

## data strategy

**ABC:** Abstract_data_strategy
**IMPL:**

- Merge
- Overwrite

## manager

**ABC:** Abstract_file_system_io_manager
**IMPL:**

- Directory_manager
- Simple_file_manager

## operator

**ABC:** Abstract_file_system_io_operator
**IMPL:**

- Directory_io_operator
  - Directory_creator
  - Directory_remover
- File_io_operator
  - File_Reader
    - Json_file_reader
    - Yaml_file_reader
  - File_Writer
    - Json_file_writer
    - Yaml_file_writer

## source

**ABC:** Abstract_path_detail
**IMPL:**

- Directory_path_detail
- File_path_detail
