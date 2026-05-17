import ast # abstract syntax tree , to split the code uploaded into imports , classes , functions etc 
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