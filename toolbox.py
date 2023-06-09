def read_file(file_path):
    return [int(r.strip()) for r in open(file_path)]
