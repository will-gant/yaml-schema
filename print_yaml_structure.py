import yaml
import sys

def print_structure(data, indent=''):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                print(f"{indent}{key}:")
                print_structure(value, indent + '  ')
    elif isinstance(data, list):
        print(f"{indent}- list with {len(data)} items")
        for item in data:
            print_structure(item, indent + '  ')

def main():
    if len(sys.argv) != 2:
        print("Usage: python print_yaml_structure.py <path_to_yaml_file>")
        sys.exit(1)
    
    yaml_file_path = sys.argv[1]
    
    try:
        with open(yaml_file_path, 'r') as file:
            data = yaml.safe_load(file)
            print_structure(data)
    except Exception as e:
        print(f"Failed to read or parse the YAML file: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
