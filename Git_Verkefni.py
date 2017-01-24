#Dæmi1
#Elmar Ólafsson
tala1 = int(input("Sláðu inn fyrstu töluna af tvem: "))
tala2 = int(input("Sláðu inn aðra töluna af tvem: "))#bið um tvær tölur
plus = tala1 + tala2#plusa þær
sinnum = tala1 * tala2#margfalda þær
print("\nTölurnar plúsaðar: %s" % plus)
print("Tölurnar margfaldaðar: %s" % sinnum)#prenta útkomur
#Dæmi2
fornafn = input("\nSláðu inn fornafn: ")
eftirnafn = input("Sláðu in eftirnafn: ")#bið um fullt nafn
print("\nHalló %s %s" % (fornafn,eftirnafn))#prenta
#Dæmi3
lagstafur = 0#lagstafur fær gildið 0
hastafur = 0#hástafur fær gildið 0
H_eftir_L = 0#lagstafur eftir hastaf fær gildið 0
texti = input("\nSláðu inn texta: ")#bið um texta
for c in range(len(texti)):#for lykkja er í gegnu hvern staf
    if texti[c].isupper():#ef það er hástafur
        hastafur += 1#hastafur gær +1 gildi
        if texti[c+1].islower():#ef lagstafur eftir hastaf
            H_eftir_L += 1#lagstafur eftir hasaf fær gildið +1
    if texti[c].islower():#ef lagstafur
        lagstafur += 1#lagstafur fær gildið +1
print("\nTexti: %s" % texti)
print("Lágstafir: %s" %lagstafur)
print("Hástafir: %s" %hastafur)
print("Lágstafur á eftir Hástaf: %s" %H_eftir_L)#prenta útkomur

