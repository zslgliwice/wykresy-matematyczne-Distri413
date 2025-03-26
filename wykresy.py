import numpy as np
import matplotlib.pyplot as plt

#PIERWSZE

plt.title('Wyniki wyborów parlamentarnych w Polsce z roku 2023')

partie = ['pis', 'ko', 'trzecia droga', 'lewica', 'konfederacja']
mandaty = [194, 157, 65, 26, 18]
plt.bar(partie, mandaty)

plt.show()

#DRUGIE

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin(x)', color='r')
plt.plot(x, y2, label='cos(x)', color='b')

plt.title("Wykres funkcji sin(x) i cos(x)")
plt.grid(True, linestyle='--', linewidth=0.5)
plt.axhline(0, color='black', linewidth=1) 
plt.axvline(0, color='black', linewidth=1)
plt.legend()

plt.show()

#TRZECIE

wierzcholki = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])

n = 500000
p = np.zeros((n, 2))

p[0] = np.random.rand(2)

for i in range(1, n):
    w = wierzcholki[np.random.randint(0, 3)] 
    p[i] = (p[i - 1] + w) / 2 

plt.figure(figsize=(10, 10))
plt.scatter(p[:, 0], p[:, 1], s=0.2, color='k')
plt.axis("equal")
plt.axis("off")
plt.title("Trójkąt Sierpińskiego")
plt.show()
