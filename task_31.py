import re

#V 1.0 REGEX [\w]+[\.]?[\w]+[@][\w]+([\.]?[\w])+
# TODO A KISZoLGÁLÓ ÉS A TLD KÖZÖTTI PONTOKAT NE FOGADJA EL SŐT SEHOL SE KÉNE
def EzEmailVagySem(beolv):
    kereses = None
    kereses =  re.fullmatch('[\w+\.?]+[^a-zA-Z0-9.]*[\w+\.?]+[@][\w]+([\.]?[\w])+',beolv)
    print(kereses)
    if kereses:
        print("Ez helyes e-mail cím!\n")
    else:
        print("Ez nem helyes e-mail cím!\n")

beolv = ""
while ('0' or '\0') not in beolv:
    beolv = input("Add meg az e-mail címet!\n")
    if ('0' or '\0') in beolv:
        quit()
    EzEmailVagySem(beolv)