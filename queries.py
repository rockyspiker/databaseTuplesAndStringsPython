import parts

# part one
boltSupps = {supp[1] for supp in parts.suppliers
                       for r in parts.spj
                       for part in parts.parts 
                       if r[1]==part[0] if r[0]==supp[0] if part[1]=='Bolt'}

print('"Bolt" suppliers are listed as:')
for supp in boltSupps:
  print('\t' + supp)

# part two
redSupps = {supp[1] for supp in parts.suppliers
                       for r in parts.spj
                       for part in parts.parts 
                       if r[1]==part[0] if r[0]==supp[0] if part[2]=='Red'}

print('\n"Red" suppliers are listed as:')
for supp in redSupps:
  print('\t' + supp)

# part three
pairCity = {city[3] for city in parts.suppliers
                        for supp in parts.suppliers
                        if city[1]!=supp[1] if city[3]==supp[3]
}

print('\nCity with pairs list as:')
for city in pairCity:
  print('\t' + city + ' suppliers:')
  for supp in parts.suppliers:
    if supp[3] == city:
      print('\t\t' + supp[1])

#part four
cities = {city[3] for city in parts.suppliers}
print('\nCities with supplies list as:')
for city in cities:
  print('\t' + city + ' suppliers:')
  for supp in parts.suppliers:
    if supp[3] == city:
      print('\t\t' + supp[1])