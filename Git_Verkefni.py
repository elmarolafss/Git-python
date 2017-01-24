#Dæmi1
tala1 = int(input("Sláðu inn fyrstu töluna af tvem: "))
tala2 = int(input("Sláðu inn aðra töluna af tvem: "))
plus = tala1 + tala2
sinnum = tala1 * tala2
print("\nTölurnar plúsaðar: %s" % plus)
print("Tölurnar margfaldaðar: %s" % sinnum)
#Dæmi2
fornafn = input("\nSláðu inn fornafn: ")
eftirnafn = input("Sláðu in eftirnafn: ")
print("Halló %s %s" % (fornafn,eftirnafn))
#Dæmi3
lagstafur = 0
hastafur = 0
H_eftir_L = 0
texti = input("Sláðu inn texta: ")
for c in range(len(texti)):
    if texti[c].isupper():
        hastafur += 1
        if texti[c+1].islower():
            H_eftir_L += 1
    if texti[c].islower():
        lagstafur += 1
print("Texti: %s" % texti)
print("Lágstafir: %s" %lagstafur)
print("Hástafir: %s" %hastafur)
print("Lágstafur á eftir Hástaf: %s" %H_eftir_L)

