# file-system-io public classes

## class `Directory_manager`

_extends_ `Abstract_file_system_io_manager`

manages the creation and deletion of a single directory

### Example

```python
from file_system_io_manager.impl.directory_manager.directory_manager import Directory_manager
from file_system_io_source.path_detail.impl.directory_path_detail import Directory_path_detail

directory_manager: Directory_manager = Directory_manager.create_instance(dir_path='testing_dir/nested_dir')
directory_manager.create()
# creates /Users/username/workspace/project_lib/testing_dir (in current working directory)
# creates /Users/username/workspace/project_lib/testing_dir/nested_dir (in testing_dir)
directory_manager.remove()
# removes /Users/username/workspace/project_lib/testing_dir/nested_dir
# does not change /Users/username/workspace/project_lib/testing_dir (in current working directory)
```

**creation (class method):**

```python
Directory_manager.create_instance(
	dir_path: str | Directory_path_detail
)
```

#### Parameters

| Name     | Type                             | Description |
| -------- | -------------------------------- | ----------- |
| dir_path | `str` or `Directory_path_detail` |             |

#### Properties

| Name    | Type                | Description |
| ------- | ------------------- | ----------- |
| creator | `Directory_creator` |             |
| remover | `Directory_remover` |             |

#### Methods

| Name             | Description |
| ---------------- | ----------- |
| create()         |             |
| remove()         |             |
| clear_contents() |             |

---

##### create(self)

```python
def create(self) -> NoReturn:
```

_Parameters_

- **N/A**

creates a directory

---

##### remove(self)

```python
def remove(self) -> NoReturn:
```

_Parameters_

- **N/A**

removes a directory

---

##### clear_contents(self)

```python
def clear_contents(self) -> NoReturn:
```

_Parameters_

- **N/A**

clears the contents of a directory

---

---

## class `File_manager`

_extends_ `Abstract_file_system_io_manager`

manages the reading and writing of a single file

> [! Warning] Only file types that can be read as a dictionary are supported
>
> ```python
> class Supported_file_types(Enum):
>    YAML = 'yaml'
>    JSON = 'json'
>
> ```

**creation (class method):**

```python
File_manager.create(
	file_name_with_extension: str,
	dir_path: str | Directory_path_detail
)
```

#### Parameters

| Name                     | Type                             | Description |
| ------------------------ | -------------------------------- | ----------- |
| file_name_with_extension | `str`                            |             |
| dir_path                 | `str` or `Directory_path_detail` |             |

#### Properties

| Name   | Type          | Description |
| ------ | ------------- | ----------- |
| reader | `File_reader` |             |
| writer | `File_writer` |             |

#### Methods

| Name                           | Description |
| ------------------------------ | ----------- |
| read()                         |             |
| write(new_data, data_strategy) |             |

---

##### read(self)

```python
def read(self) -> Dict:
```

_Parameters_

- **N/A**

reads data from a file

---

##### write(new_data, data_strategy)

```python
def write(self, new_data: Dict, data_strategy: Data_strategy) -> NoReturn:
```

_Parameters_

- **new_data** `Dict`
- **data_strategy** `Data_strategy` - the method to handle the transformation from the old data to new

writes data to a file

---

---

## class: `Directory_path_detail`

_extends_ `Abstract_path_detail`

A data object to represent system file paths. Relative paths are automatically converted into absolute path on init.

### Example

```python
from file_system_io_source.path_detail.impl.directory_path_detail import Directory_path_detail

cwd_path = 'test_cwd_path'
user_root_path = '/test_user_root_path'
relative_path = '../test_user_root_path'

cwd_path_detail: Directory_path_detail = Directory_path_detail.create(
    path=cwd_path,
    is_user_defined=True
)

user_root_path_detail: Directory_path_detail = Directory_path_detail.create(
    path=user_root_path,
    is_user_defined=False
)

relative_path_detail: Directory_path_detail = Directory_path_detail.create(
    path=relative_path,
    is_user_defined=False
)


'''
cwd_path_detail
--------
abspath : /Users/username/workspace/project_dir/test_cwd_path
isuserdefined : True

user_root_path_detail
--------
abspath : /test_user_root_path
isuserdefined : False

relative_path_detail
--------
abspath : /Users/username/workspace/test_user_root_path
isuserdefined : False
'''

```

**creation (class method):**

```python
Directory_path_detail.create(
	 path: str,
	 is_user_defined: boolean
)
```

#### Parameters

| Name            | Type      | Description |
| --------------- | --------- | ----------- |
| path            | `str`     |             |
| is_user_defined | `boolean` |             |

#### Properties

| Name            | Type      | Description |
| --------------- | --------- | ----------- |
| abs_path        | `str`     |             |
| is_user_defined | `boolean` |             |

#### Methods

| Name | Description |
| ---- | ----------- |
|      |             |
