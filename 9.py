ug=input("Yamar negen ug bicheerei: ")
ug=ug.lower()
too= ""

for useg in ug:
    if useg not in too:
        too+=useg

if useg in too:
    print(useg, ug, ug.count(useg))