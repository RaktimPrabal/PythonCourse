character = input()
new_rna = []

for item in character:
    if item == 'G':
        new_rna.append('C')
    elif item == 'C':
        new_rna.append('G')
    elif item == 'T':
        new_rna.append('A')
    elif item == 'A':
        new_rna.append('U')
    else:
        new_rna.append('Invalid Input')

rna = ''.join(new_rna)
print(rna)
