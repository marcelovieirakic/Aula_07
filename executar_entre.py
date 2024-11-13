
#while True:
#    try:
#        iniciar = int(input("Digite o numero incial da sequencia: "))
#        finalizar = int(input("Digite o numero final da sequencia: "))
#        while iniciar <= finalizar:
#            print( iniciar )
#            iniciar = iniciar + 1
#        break
#    except:
#        print("digite somente numeros")



continuar = True
while continuar:
    try:
        iniciar = int(input("Digite o número inicial da sequência: "))
        finalizar = int(input("Digite o número final da sequência: "))
        
        # Inicializar as listas fora do loop
        lista_par = []
        lista_impar = []
        
        while iniciar <= finalizar:
            if iniciar % 2 == 0:
                lista_par.append(iniciar)
            else:
                lista_impar.append(iniciar)
            
            iniciar += 1  # Incrementa o valor de iniciar
        
        print("Números pares:", lista_par)
        print("Números ímpares:", lista_impar)
        
        # Pergunta ao usuário se deseja continuar
        opcao = input("Deseja continuar? (s/n): ").strip().lower()
        if opcao != 's':
            continuar = False
    except ValueError:
        print("Digite somente números")


