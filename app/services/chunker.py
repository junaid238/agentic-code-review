def chunk_code(code: str, chunk_size: int = 500):

    chunks = []

    for i in range(0, len(code), chunk_size):
        chunk = code[i:i + chunk_size]
        chunks.append(chunk)

    return chunks