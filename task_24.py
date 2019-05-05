def SzamRendszerEllenorzes (szamrendszer, szam):
    if (szam[0] == '0' or szam[0] == 0) and szamrendszer == 10:
         print("0-val kezdődik de tízes számrendszer van megadva!")
         return False
    for i in range (len(szam)):
        if int(szam[i]) > szamrendszer-1:
            print("Ez nem a megadott számrendszerben van reprezentálva!")
            return False
    return True



try :
    szamRendszer = int(input("Add meg a számrendszert!(egész számként, x >= 2 ^ x <= 10)"))
    elsoBeolvasas = input( "Kérem az első számot")
    if not SzamRendszerEllenorzes(szamRendszer, elsoBeolvasas):
        quit()
    masodikBeolvasas = input( "Kérem a második számot")
    if not SzamRendszerEllenorzes(szamRendszer, masodikBeolvasas):
        quit()
except ValueError:
    print("Nem szám lett megadva!")





"""

kettohatvamy= 0
for i in range (len(vmi),0,-1)
	for y in range(0,len(vmi),1)
		kettohatvany = kettohatvany + 2**y

"""
#for i in range(0,szamRendszer,1):
