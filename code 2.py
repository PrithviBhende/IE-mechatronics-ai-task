pnames = []
for _ in range(5):
    name = input("Enter a name: ")
    namep = name.split()
    namep[0] = namep[0].upper()
    for i in range(1, len(namep)):
        namep[i] = namep[i].lower()
    if len(namep) > 1:
        namep[-1] = namep[-1][:-2]
    pname = ''.join(namep)
    pnames.append(pname)
print("Processed names:")
for pname in pnames:
    print(pname)