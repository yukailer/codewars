def DNA_strand(dna):
    res=""
    dna_dict = {
                "A": "T",
                "T": "A",
                "C": "G",
                "G": "C"
              }
    for i in dna:
        res=res + dna_dict[i]
    return res
