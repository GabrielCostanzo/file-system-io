# file-system-io

## Public Classes

### class `Directory_manager`

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

### class `File_manager`

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

### class: `Directory_path_detail`

**consists of:** (abs_path, is_user_defined)

**public methods:** N/A

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
