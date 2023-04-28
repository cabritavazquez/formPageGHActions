import os
import yaml

try:
    os.remove("lamda_prueba.tf")
except Exception:
    pass

def parse_yaml():
    with open("template.yaml", "r") as f:
        return yaml.safe_load(f)

def generate_terraform_code(data):
    print(data['lambdas'])


def main():
    data = parse_yaml()
    generate_terraform_code(data)
    pass

if __name__ == "__main__":
    main()