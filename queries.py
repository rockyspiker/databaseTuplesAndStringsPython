import parts

# part one
boltSupps = {supp[1] for supp in parts.suppliers
                       for r in parts.spj
                       for part in parts.parts 
                       if r[1]==part[0] if r[0]==supp[0] if part[1]=='Bolt'}

print('"Bolt" suppliers are listed as:')
for supp in boltSupps:
  print(supp)

# part two
redSupps = {supp[1] for supp in parts.suppliers
                       for r in parts.spj
                       for part in parts.parts 
                       if r[1]==part[0] if r[0]==supp[0] if part[2]=='Red'}

print('\n"Red" suppliers are listed as:')
for supp in redSupps:
  print(supp)

# part three
redSupps = {supp[1] for supp in parts.suppliers
                       for r in parts.spj
                       for part in parts.parts 
                       if r[1]==part[0] if r[0]==supp[0] if part[2]=='Red'}

print('\n"Red" suppliers are listed as:')
for supp in redSupps:
  print(supp)

#part four