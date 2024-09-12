# Operação Ternária

# Construindo estruturas condicionais em uma única linha
print('Verdadeiro' if True else 'Falso')

print('É falso' if False else 'É verdadeiro')

# Atribuindo em variáveis
condicao = 10 == 10
minha_variavel = 'Valor' if condicao else 'Outro valor'
print(minha_variavel)

# Vamos usar uma operação ternária para determinar qual valor será atribuído a uma variável
digito = 10
outro_digito = digito if digito < 10 else 0
# Ou seja, a variável outro_digito receberá o valor de digito caso esta última seja menor que 10.
# Caso seja igual ou maior, o novo_digito será 0
print(outro_digito)
