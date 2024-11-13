while True:
    try:
        temperatura = int(input("entre com a temperatura: "))
        if temperatura <= 18:
            print(f"temperatura digitada {temperatura} graus, esta baixa")
        elif temperatura <= 26:
            print(f"temperatura digitada {temperatura} graus, esta normal")
        else:
            print(f"temperatura digitada {temperatura} graus, esta alta")
        break
    except:
        print("voce nao digitou uma temperatura")