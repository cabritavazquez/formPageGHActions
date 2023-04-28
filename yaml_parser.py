import os
import yaml

try:
    os.remove("lambda_prueba.tf")
except Exception:
    pass

def parse_yaml():
    with open("template.yaml", "r") as f:
        return yaml.safe_load(f)

def generate_terraform_code(data):
    print(data['lambdas'])

    with open("lambda_prueba.tf", "w") as f:
        f.write(
            '''
            module "lambda-bundle-netsales-process" {
                source = "tfe1.sgtech.corp/curated-catalog/module-iam-sm/aws"
                source = "1.6.1"
            }
            '''
        )


def main():
    data = parse_yaml()
    generate_terraform_code(data)
    pass

if __name__ == "__main__":
    main()