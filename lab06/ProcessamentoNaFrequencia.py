"""
FILTRAGEM NA FREQUÊNCIA – (PROCESSAMENTO NA FREQUÊNCIA)
FUNÇÕES DE TRANSFERÊNCIAS:

1. Cria o arquivo principal ProcessamentoNaFrequencia
2. Crie uma biblioteca chamada bibFuncaoTransferencia, dentro da biblioteca,
faça as seguintes funções:
"""

"""
FILTRAGENS:

1. Dado que a filtragem no domínio da frequência é executada pela
multiplicação do espectro de frequência da imagem e uma função de
transferência, na qual o espectro da imagem e H devem ter as mesmas
dimensões.
a. Leia e exiba a imagem mamography.pgm
b. Use a função cv2.resize, para que toda imagem lida passe a ter
tamanho 400 por 400.
c. Passe a imagem lida para o domínio da frequência (ImFrequencia)
usando fft2. Obs.: Não esquecer do fftshift.
d. Faça a filtragem na frequência, usando o filtro passa baixa ideal com fc
igual 0.2:
F_filtrada = ImFrequencia x H;
e. Faça a transformada inversa de Fourier e exiba a imagem filtrada, o
resultado é coerente? explique ao professor.
f. Refaça a filtragem na frequência, usando o filtro gaussiano, com fc =
0.2 e butterworth com fc = 0.2 e 2 polos.
g. Como alterar as funções de transferências para filtros passa altas?
h. Filtre novamente a imagem com o filtro passa altas ideal com fc igual a
0.1. O resultado é coerente? Explique para o professor.
"""

"""
a. Leia e exiba a imagem mamography.pgm
b. Use a função cv2.resize, para que toda imagem lida passe a ter
tamanho 400 por 400.
c. Passe a imagem lida para o domínio da frequência (ImFrequencia)
usando fft2. Obs.: Não esquecer do fftshift.
"""

import cv2
import skimage
import matplotlib.pyplot as plt 
import numpy as np
from bibFuncaoTransferencia import fazerMascaraIdeal2D

# a. Leia e exiba a imagem mamography.pgm
i0 = cv2.imread('ImagensAula/mamography.pgm', 0) # Gray
in0 = skimage.img_as_float(i0)

# b. Use a função cv2.resize, para que toda imagem lida passe a ter
# tamanho 400 por 400.
in0_resized = cv2.resize(in0, (400, 400))

# c. Passe a imagem lida para o domínio da frequência (ImFrequencia)
ImFrequencia = np.fft.fftshift(np.fft.fft2(in0_resized))

"""
d. Faça a filtragem na frequência, usando o filtro passa baixa ideal com fc
igual 0.2:
F_filtrada = ImFrequencia x H;
e. Faça a transformada inversa de Fourier e exiba a imagem filtrada, o
resultado é coerente? explique ao professor.
"""

# d. Faça a filtragem na frequência, usando o filtro passa baixa ideal com fc
# igual 0.2:
M, N = in0_resized.shape
fc = 0.2
H = fazerMascaraIdeal2D(M, N, fc)
F_filtrada = ImFrequencia * H

# e. Faça a transformada inversa de Fourier e exiba a imagem filtrada, o
# resultado é coerente? explique ao professor.
in0_filtrada = np.fft.ifft2(np.fft.ifftshift(F_filtrada))
in0_filtrada = np.abs(in0_filtrada)

# f. Refaça a filtragem na frequência, usando o filtro gaussiano, com fc = 0.2 
# e butterworth com fc = 0.2 e 2 polos.
from bibFuncaoTransferencia import fazerMascaraGaussiana2D, fazerMascaraButter2D
H_gauss = fazerMascaraGaussiana2D(M, N, fc)
F_filtrada_gauss = ImFrequencia * H_gauss
in0_filtrada_gauss = np.fft.ifft2(np.fft.ifftshift(F_filtrada_gauss))
in0_filtrada_gauss = np.abs(in0_filtrada_gauss) 

n_polos = 2
H_butter = fazerMascaraButter2D(M, N, fc, n_polos)
F_filtrada_butter = ImFrequencia * H_butter
in0_filtrada_butter = np.fft.ifft2(np.fft.ifftshift(F_filtrada_butter))
in0_filtrada_butter = np.abs(in0_filtrada_butter)

# g. Como alterar as funções de transferências para filtros passa altas?
# h. Filtre novamente a imagem com o filtro passa altas ideal com fc igual a
# 0.1. O resultado é coerente? Explique para o professor.
H_passas_alta_ideal = 1 - fazerMascaraIdeal2D(M, N, 0.1)
F_filtrada_passas_alta_ideal = ImFrequencia * H_passas_alta_ideal
in0_filtrada_passas_alta_ideal = np.fft.ifft2(np.fft.ifftshift(F_filtrada_passas_alta_ideal))       
in0_filtrada_passas_alta_ideal = np.abs(in0_filtrada_passas_alta_ideal)

# Faca um passa alta butterworth
H_passas_alta_butter = 1 - fazerMascaraButter2D(M, N, 0.1, n_polos)
F_filtrada_passas_alta_butter = ImFrequencia * H_passas_alta_butter
in0_filtrada_passas_alta_butter = np.fft.ifft2(np.fft.ifftshift(F_filtrada_passas_alta_butter))       
in0_filtrada_passas_alta_butter = np.abs(in0_filtrada_passas_alta_butter)

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes[0, 0].imshow(in0_resized, cmap='gray')
axes[0, 0].set_title('Imagem Redimensionada')
axes[0, 0].axis('off')

axes[0, 1].imshow(in0_filtrada, cmap='gray')
axes[0, 1].set_title('Imagem Filtrada - Passa Baixa Ideal')
axes[0, 1].axis('off')

axes[0, 2].imshow(in0_filtrada_gauss, cmap='gray')
axes[0, 2].set_title('Imagem Filtrada - Passa Baixa Gaussiana')
axes[0, 2].axis('off')

axes[1, 0].imshow(in0_filtrada_butter, cmap='gray')
axes[1, 0].set_title('Imagem Filtrada - Passa Baixa Butterworth')
axes[1, 0].axis('off')

axes[1, 1].imshow(in0_filtrada_passas_alta_ideal, cmap='gray')
axes[1, 1].set_title('Imagem Filtrada - Passa Alta Ideal')
axes[1, 1].axis('off')

axes[1, 2].imshow(in0_filtrada_passas_alta_butter, cmap='gray')
axes[1, 2].set_title('Imagem Filtrada - Passa Alta Butterworth')
axes[1, 2].axis('off')

plt.tight_layout()
plt.show()