import matplotlib.pyplot as plt
x = list(range(10))
y = [el ** 2 for el in x]

# tracciamento di y rispetto a x con un indicatore quadrato
plt.plot(x, y, marker='s', color='blue', linestyle='-', linewidth=2)

# personalizzazione del grafico
plt.xlabel('x')
plt.ylabel('y')
plt.title('Tracciamento di y = x^2')
plt.grid(True)

# mostra il grafico
plt.show()