ug=input("Yamar negen ug bicheerei: ")
ug=ug.lower()
too= ""

for useg in ug:
    if useg not in too:
        too+=useg

for useg in too:
    print("{} ugend {} useg {} udaa bichigdsen baina!".format(ug, useg, ug.count(useg)))