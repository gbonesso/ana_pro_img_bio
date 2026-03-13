import numpy as np
import matplotlib.pyplot as plt
import cv2 # OpenCV
import skimage
import skimage.exposure

i0 = cv2.imread('lab01/raioXTorax.pgm', 0) # Gray

"""
(Normalizar Intensidades) No Editor implemente a normalização abaixo para
a matriz de imagem ficar normalizada entre 0 e 1 com resolução de
intensidade ‘float’ .
Ex.:

# Convert to normalized floating point como se fosse im2double do
MatLab.
"""

in0 = skimage.img_as_float(i0)

(M,N) = np.shape(in0)

print('Tamanho da imagem: ', M, 'x', N) # M -> linhas, N -> colunas

print('Intensidade do pixel (50,50): ', in0[50,50]) # Intensidade do pixel (50,50)

maximo = np.max(in0)
minimo = np.min(in0)
media = np.mean(in0)
dP = np.std(in0)

print('Valor máximo: ', maximo)
print('Valor mínimo: ', minimo)
print('Valor médio: ', media)
print('Desvio padrão: ', dP)

"""
12.Transforme a imagem em binário com diferentes limiares.
Ibnario1 = in0>0.2
Ibnario1 = in0>0.5
Ibnario1 = in0>0.8
Explique em comentário no código o que aconteceu? Para qual tipo a
imagem se transformou, etc.
"""

Ibnario1 = in0>0.2 # A imagem se transformou em uma imagem binária, onde os pixels com intensidade maior que 0.2 são definidos como True (1) e os pixels com intensidade menor ou igual a 0.2 são definidos como False (0).
Ibnario2 = in0>0.5 # A imagem se transformou em uma imagem binária, onde os pixels com intensidade maior que 0.5 são definidos como True (1) e os pixels com intensidade menor ou igual a 0.5 são definidos como False (0).
Ibnario3 = in0>0.8 # A imagem se transformou em uma imagem binária, onde os pixels com intensidade maior que 0.8 são definidos como True (1) e os pixels com intensidade menor ou igual a 0.8 são definidos como False (0).

# Exibe as 4 imagens ao final
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.title('Imagem original')
plt.xlabel('colunas - N')
plt.ylabel('linhas - M')
plt.imshow(in0, cmap='gray')
plt.colorbar()

plt.subplot(2, 2, 2)
plt.title('Ibnario1 > 0.2')
plt.imshow(Ibnario1, cmap='gray')

plt.subplot(2, 2, 3)
plt.title('Ibnario2 > 0.5')
plt.imshow(Ibnario2, cmap='gray')

plt.subplot(2, 2, 4)
plt.title('Ibnario3 > 0.8')
plt.imshow(Ibnario3, cmap='gray')

plt.tight_layout()
plt.show(block=True)

