def HelyesenVannakMegadvaASzamok (szamrendszer, elsoszam,masodikszam):
    if szamrendszer < 2 or szamrendszer > 10:
        print("Nem a megadott határok között van a számrendszer!")
        return False
    if (elsoszam[0] == '0' or elsoszam[0] == 0) and szamrendszer == 10:
    #ha tízes számrendszer van megadva de nullával kezdődik
         print("0-val kezdődik de tízes számrendszer van megadva!")
         exit()
         return False
    if (masodikszam[0] == '0' or masodikszam[0] == 0) and szamrendszer == 10:
    #ha tízes számrendszer van megadva de nullával kezdődik
         print("0-val kezdődik de tízes számrendszer van megadva!")
         exit()
         return False
    segedvalt= str(elsoszam)
    for i in range(len(segedvalt)):
        if int(segedvalt[i]) >= szamRendszer:
            print("A számban olyan elem található amely nagyobb mint maga a számrendszer engedi!")
            return False
    segedvalt = str(masodikszam)
    for i in range(len(segedvalt)):
        if int(segedvalt[i]) >= szamRendszer:
            print("A számban olyan elem található amely nagyobb mint maga a számrendszer engedi!")
            return False
    return True

def BaseNToBaseTen(b,num):#b= számrendszer num=szám
    # Átvált N számrendsz.ből decim.-be
    num = str(num)
    n = len(str(num)) #számjegyek száma
    sum = 0
    szamHanyadikja = 0
    for i in range(n-1, -1, -1):
        #print(int(num[i]),"*",b,"**",i,"=",int(num[i])*b**i)
        sum = sum + (int(num[szamHanyadikja])*b**i)
        szamHanyadikja+=1
        n -= 1
    return sum #tízesben


def BaseTenToBaseN(n,szamrendszer): #n:=decimal
    #átvált decim.ből N számrendszerbe
    m=""            #this will store the
    while n != 0:
        d = n // szamRendszer
        r = n % szamRendszer
        m = m + str(r)
        n = d
    seged = ""
    for i in range(len(m)-1,-1,-1):
        seged = seged+m[i]
    return seged
try :
    szamRendszer = int(input("Add meg a számrendszert!(egész számként, x >= 2 ^ x <= 10)"))
    elsoBeolvasas = input( "Kérem az első számot")
    masodikBeolvasas = input("Kérem a második számot")
    if not HelyesenVannakMegadvaASzamok(szamRendszer, elsoBeolvasas,masodikBeolvasas):
        quit()
except ValueError:
    print("Nem szám lett megadva!")
if szamRendszer != 10:
    elsoDecimalisban = BaseNToBaseTen(szamRendszer,elsoBeolvasas)
    masodikDecimalisban = BaseNToBaseTen(szamRendszer,masodikBeolvasas)
    print("Első decimálisban: ", elsoDecimalisban, "Második decimálisban: ", masodikDecimalisban)
    osszeadasEredmenye = elsoDecimalisban+masodikDecimalisban
    print("Összeadás eredménye 10-es számrendszerben: ", osszeadasEredmenye)
    osszeadasEredmenye = BaseTenToBaseN(osszeadasEredmenye,szamRendszer)
    print("Összeadás eredménye ",szamRendszer,"-es/as/ös/ számrendszerben: ",osszeadasEredmenye)
    print("Visszaírva 10-esbe: ",BaseNToBaseTen(szamRendszer,osszeadasEredmenye))
else:
    print("Az összeadás eredménye", int(elsoBeolvasas)+int(masodikBeolvasas))
