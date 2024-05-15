# YAML Structure Printer

This Python script reads a YAML file and prints its structure/schema - i.e. all keys whose values are arrays or dictionaries.

## Setup

```shell
pip install -r requirements.txt
```

## Usage

```shell
python print_yaml_structure.py example.yml
```

## Example output

```shell
$ cat example.yml
dictionary:
  nested_dictionary:
    nested_array:
    - text: some text
    - number: 123
    - nested_dictionary:
        nested_dictionary:
          text: some text
          number: 123
          nested_dictionary:
            text: some text
            number: 123
    nested_dictionary:
      text: some text
      number: 123
      nested_dictionary:
        text: some text
    text: some text
    number: 123

$ python print_yaml_structure.py example.yml
dictionary:
  nested_dictionary:
    nested_array:
      - list with 3 items
        nested_dictionary:
          nested_dictionary:
            nested_dictionary:
    nested_dictionary:
      nested_dictionary:
````

