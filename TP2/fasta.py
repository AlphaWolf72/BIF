def get_seq_from_fasta(path: str) -> str:
    with open(path, 'r') as f_in:
        f_in.readline()
        return f_in.readline().strip()
