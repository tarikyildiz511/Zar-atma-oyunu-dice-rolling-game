import random 
while True:
    zar = random.randint(1,6)
    print(f"zar{zar}geldi")
    tekrar = input("E/H")
    if tekrar == "E":
        print("Tekrar ediyor:")
    if tekrar =="H":
        break