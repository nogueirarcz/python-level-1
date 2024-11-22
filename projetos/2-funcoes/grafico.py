import matplotlib.pyplot as plt

valores_x = []
valores_y = []


def gerar_valores(a, b, c):

    for x in range(-10, 11, 1):

        valores_x.append(x)
        valores_y.append((a * (x ** 2)) + (b * x) + c)

    return valores_x, valores_y
    
def gerar_grafico(x, y):

    fig, ax = plt.subplots()
    ax.plot(valores_x, valores_y, linewidth=2)
    plt.scatter(valores_x, valores_y, color='blue', marker='o')
    plt.xticks(range(-10,11,1))
    plt.xlim(-10,10)
    plt.ylim(-5,80)
    plt.show()
    