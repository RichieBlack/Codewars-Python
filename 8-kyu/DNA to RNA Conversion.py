# https://www.codewars.com/kata/reviews/555628327302c4fd84000071/groups/5ec6935350fbac00017bab69

def dna_to_rna(dna):
    return dna.replace("T", "U")


# I have been studying Python for one month.

"""Best practices
-----------------

def DNAtoRNA(dna):
    return dna.replace('T', 'U')

-----------------

def DNAtoRNA(dna):
    return "".join(["U" if c == "T" else c for c in dna])

-----------------

DNAtoRNA = lambda d: d.replace("T", "U")

-----------------
"""
