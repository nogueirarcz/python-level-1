# Operações com sets

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# União de conjuntos: pode ser feita com o operador pipe |
c = a | b
print(c)

# Intersecção entre conjuntos: é realizada com o operador &
c = a & b
print(c)

# Diferença entre conjuntos: é realizada com o operador -
c = a - b
print(c)

# Diferença simétrica: é realizada com o operador ^ (itens que não estão presentes em ambos)
c = a ^ b
print(c)
