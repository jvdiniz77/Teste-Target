# Questão 1
indice = 13
K = 0
soma=0

while K < indice:
    K = K + 1
    soma = soma + K

print(soma)  # Resposta: O número que retorna é 91

# Questão 2
def fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero

numero = int(input())
if fibonacci(numero):
    print(f"{numero} pertence à sequência.")
else:
    print(f"{numero} não pertence à sequência.")

# Questão 3
# a) Resposta: 9
# b) Resposta: 128
# c) Resposta: 49
# d) Resposta: 100
# e) Resposta: 13
# f) Resposta: 20

# Questão 4
# Na primeira ida eu ligaria o interruptor 1 por certo tempo e depois desligaria, logo depois ligaria o interruptor2 e voltaria para sala das lâmpadas
# voltando para a sala das lâmpadas, a lâmpada que estiver acesa é controlada pelo interruptor 2, para descobrir as lâmpadas apagadas veria qual estava apagada e quente
# pois acendi o interruptor 1 por algum tempo para que a lâmpada esquentasse, então a mesma seria controlada pelo interruptor 1
# para garantir qual interruptor acende a lâmpada 3, iria até o interruptor que eu não havia ido e acenderia, voltando a sala das lâmpdas confirmaria que a lâmpada 3 é controlada por ele. 

# Questão 5
def inverter_string(string):
    string_invertida = ""
    for char in string:
        string_invertida = char + string_invertida
    return string_invertida

string = input("Digite uma string: ")
print("A string invertida é:", inverter_string(string))
