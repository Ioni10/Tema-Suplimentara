import random

scor_jucator = 0
scor_calculator = 0

while True:
                alegere = input("Alege  par sau impar:")
                numar_jucator = int(input("Alege un numar intre 0 si 10:"))
                numar_caluclator = random.randint(0,10)
                suma = numar_jucator + numar_caluclator
                print("Tu ai ales:",numar_jucator)
                print("Calculatorul a ales:",numar_caluclator)
                print("Suma este:",suma)

                if suma %2 == 0:
                    rezultat="par"
                    print("Ai ales numar par")
                else:
                    rezultat="impar"
                    print("Ai ales numar impar")
                    print("Suma este",rezultat)
                if alegere == rezultat:
                    print("Ai castigat runda!")
                    scor_jucator +=1
                else:
                    print("Ai pierdut!")
                    scor_calculator +=1
                    print("Scorul tau:", scor_jucator)
                    print("Scorul calculatorului:", scor_calculator)
                continua = input("Vrei sa mai joci? (da/nu): ")
                if continua != "da": break

print("Ok, ne mai vedem!")
print("Scor final:")
print("Scorul tau:", scor_jucator)
print("Scorul calculatorului:", scor_calculator)

