
def Sorozat_N_Edik_tagja(n):
    sorozat = [1]
    while len(sorozat) < n:
        sum = 0
        for i in range(len(sorozat)):
            seged_string = str(sorozat[i])
            for y in range(len(seged_string)):
                sum+=int(seged_string[y])
        sorozat.append(sum)


    return sorozat

try:
    n = int(input("Add meg hanyadik elemre vagy kíváncsi!"))
except ValueError:
    print("Nem számot adtál meg!")
print(Sorozat_N_Edik_tagja(n))