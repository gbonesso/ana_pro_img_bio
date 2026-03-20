import numpy as np
import matplotlib.pyplot as plt
import cv2 # OpenCV
import skimage
import skimage.exposure

i0 = cv2.imread('lab01/Lamina-biopsia.jpg', 1) # 1->Color
i0 = cv2.cvtColor(i0, cv2.COLOR_BGR2RGB)

"""
13.Refazer as questões usando a imagem colorida, com as 3 dimensões In1 ou
In1[:,:,:].
a. i1 = cv2.imread(' Lamina-biopsia.jpg', 1) # Color In1
b. Verifique qual o tamanho desta imagem? Quantas dimensões?
c. Trabalhar / exibir também uma banda de cada vez. In1[:,:,0], In1 [:,:,1],
In1 [:,:,2]. Indique em quais posições estão ás bandas RGB para o Open
CV?

Para mais Informações exclusivamente sobre Python
https://www.youtube.com/watch?v=lJjR906426o&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe
https://www.youtube.com/watch?v=S9uPNppGsGo&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0
"""

in0 = skimage.img_as_float(i0)

(M,N,C) = np.shape(in0)

print('Tamanho da imagem: ', M, 'x', N, 'Color', C) # M -> linhas, N -> colunas, C -> canais de cor

print('Intensidade do pixel (50,50): ', in0[50,50]) # Intensidade do pixel (50,50)

maximo = np.max(in0)
minimo = np.min(in0)
media = np.mean(in0)
dP = np.std(in0)

print('Valor máximo: ', maximo)
print('Valor mínimo: ', minimo)
print('Valor médio: ', media)
print('Desvio padrão: ', dP)

img_r = np.zeros_like(in0)
img_g = np.zeros_like(in0)
img_b = np.zeros_like(in0)

img_r[:, :, 0] = in0[:, :, 0] # Canal vermelho em vermelho
img_g[:, :, 1] = in0[:, :, 1] # Canal verde em verde
img_b[:, :, 2] = in0[:, :, 2] # Canal azul em azul

#Ibnario1 = in0>0.2 # A imagem se transformou em uma imagem binária, onde os pixels com intensidade maior que 0.2 são definidos como True (1) e os pixels com intensidade menor ou igual a 0.2 são definidos como False (0).
#Ibnario2 = in0>0.5 # A imagem se transformou em uma imagem binária, onde os pixels com intensidade maior que 0.5 são definidos como True (1) e os pixels com intensidade menor ou igual a 0.5 são definidos como False (0).
#Ibnario3 = in0>0.8 # A imagem se transformou em uma imagem binária, onde os pixels com intensidade maior que 0.8 são definidos como True (1) e os pixels com intensidade menor ou igual a 0.8 são definidos como False (0).

# Exibe as 4 imagens ao final
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.title('Imagem original')
plt.xlabel('colunas - N')
plt.ylabel('linhas - M')
plt.imshow(in0)
#plt.colorbar()

plt.subplot(2, 2, 2)
plt.xlabel('colunas - N')
plt.ylabel('linhas - M')
plt.title('Canal Vermelho')
plt.imshow(img_r)
#plt.colorbar()

plt.subplot(2, 2, 3)
plt.xlabel('colunas - N')
plt.ylabel('linhas - M')
plt.title('Canal Verde')
plt.imshow(img_g)
#plt.colorbar()

plt.subplot(2, 2, 4)
plt.xlabel('colunas - N')
plt.ylabel('linhas - M')
plt.title('Canal Azul')
plt.imshow(img_b)
#plt.colorbar()

plt.tight_layout()
plt.show(block=True)

