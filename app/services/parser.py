'''
Author : Junaid Khan 
used to parse the recieved code from upload functionality and return the programming components from the file 
using abstract syntax tree (ast) , since it is helpfuli nparsing th efile and getting imports , classes and functions out of it 
also calls chunker.py to get the file split into chunks and returns chunks 

'''

import ast
from app.services.chunker import chunk_code


def parse_python_file(file_path: str):

    with open(file_path, "r", encoding="utf-8") as file:
        code = file.read()

    tree = ast.parse(code)

    functions = []
    classes = []
    imports = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)

        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)

        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)

        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module)
    chunks = chunk_code(code)
    return {
        "functions": functions,
        "classes": classes,
        "imports": imports,
        "raw_code": code,
        "chunks": chunks
    }