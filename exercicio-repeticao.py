   
num_tabuada = int(input("Digite o número para a tabuada: "))
num_inicio = int(input("Digite o número inicial: "))
num_fim = int(input("Digite o número final: "))

if num_fim < num_inicio: 
    print("O valor final deve ser maior que o valor inicial")

for i in range(num_inicio, num_fim + 1):
        resultado = num_tabuada * i
        print(f"{num_tabuada} x {i} = {resultado}")


