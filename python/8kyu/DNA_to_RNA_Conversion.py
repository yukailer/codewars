### 1
def dna_to_rna(dna):
    res=""
    dna_dict = {
                "A": "A",
                "T": "U",
                "C": "C",
                "G": "G"
              }
    for i in dna:
        res=res + dna_dict[i]
    return res

### 2
def dna_to_rna(dna):
    return dna.replace('T', 'U')


