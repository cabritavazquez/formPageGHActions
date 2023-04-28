import os
import glob
import json
import jsonschema
from jsonschema import validate

bodyschema = {
    "type": "object",
    "properties": {
        "function_name": {"type": "string"}, # function_name: El nombre de la función de Lambda.
        "handler": {"type": "string"}, # handler: El nombre del archivo de código y la función de controlador en la función de Lambda.
        "runtime": {"type": "string"}, # runtime: El lenguaje de programación utilizado en la función de Lambda.
        "filename": {"type": "string"}, # filename: El archivo zip que contiene el código fuente de la función de Lambda.
        "role": {"type": "string"} # role: El rol de IAM que se utilizará para ejecutar la función de Lambda.
    }
}

# resource "aws_lambda_function" "example" {
#   function_name = "example_lambda"
#   handler       = "index.handler"
#   runtime       = "nodejs14.x"
#   filename      = "example.zip"
#   role          = aws_iam_role.lambda_role.arn
# }

def check_json(json_date, bodyschema,json_file_name):
    try:
        validate(json_date,schema=bodyschema)
        return []
    except jsonschema.ValidationError as error:
        return error.schema["error_msg"]
    
json_file = os.getevn("JSON_PATH")
print(check_json(json.load(open(f"{json_file}"),bodyschema,json_file)))