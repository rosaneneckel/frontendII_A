maior_altura = 0
menor_altura = 5.0  # definido um valor alto para qualquer altura ser menor que isso
soma_altura_homens = 0
qtd_homens = 0
qtd_mulheres = 0

print("Digite a sua altura e o gênero (Ex: 1.70 M):")

for i in range(1, 16):
    registros = input(f"Pessoa {i}: ").split()

    altura = float(registros[0])
    genero = registros[1].upper()

    if altura > maior_altura:
        maior_altura = altura

    if altura < menor_altura:
        menor_altura = altura


    if genero == "M":
        soma_altura_homens += altura
        qtd_homens += 1
    elif genero == "F":
        qtd_mulheres += 1


if qtd_homens > 0:
    media_homens = soma_altura_homens / qtd_homens
else:
    media_homens = 0

print("-" * 30)
print(f"Maior altura: {maior_altura}m")
print(f"Menor altura: {menor_altura}m")
print(f"Média altura homens: {media_homens:.2f}m")
print(f"Total de mulheres: {qtd_mulheres}")




