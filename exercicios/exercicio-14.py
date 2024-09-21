# Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro

def criar_multiplicador(multiplicador):
    
    def multiplicar(numero):

        return numero * multiplicador

    return multiplicar

duplicar = criar_multiplicador(2)    
print(duplicar(2))

triplicar = criar_multiplicador(3)
print(triplicar(2))

quadruplicar = criar_multiplicador(4)
print(quadruplicar(2))
