"""
Imagens Biomédicas – Lab04-Python
Tutores: André Arruda / Maíra Suzuka Kudo / Eric Rocha Santos
Professor: Matheus Cardoso Moraes
MÁSCARAS PARA FILTRAGEM – (RESTAURAÇÃO E AGUÇAMENTO)
EXERCÍCIOS:
1. → No Editor, faça um vetor amostra = [15 29 5 8 255 40 1 0 10];
a. Crie uma função que ordene este vetor em ordem crescente de
valores, e chame este novo vetor de amostraOrdenada.
Obs.: pode usar → np.sort
b. Crie uma variável mediana, para receber a mediana da amostra
ordenada.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
amostra = np.array([15, 29, 5, 8, 255, 40, 1, 0, 10])
amostraOrdenada = np.sort(amostra)
mediana = np.median(amostraOrdenada)
print("Vetor amostra ordenado:", amostraOrdenada)
print("Mediana da amostra ordenada:", mediana)

"""
2. Leia, normalize e exiba a imagem IMRI = imread(‘......../TransversalMRI_salt-and-pepper.pgm’);

Adicionalmente crie uma matriz de zeros, chamada lMRIfiltrada, com o tamanho de IMRI.
a. Crie uma função que use uma máscara 3x3 para varrer a imagem e
retornar a mediana local para a posição correspondente em IMRIfiltrada.

obs.: usar as funções “np.concatenate” e “np.sort” podem ajudar)
"""

from skimage.io import imread

image_path = Path(__file__).resolve().parents[1] / 'ImagensAula' / 'TransversalMRI_salt-and-pepper.pgm'
IMRI = imread(str(image_path))
IMRI_normalizada = IMRI / 255.0
lMRIfiltrada = np.zeros(IMRI_normalizada.shape)

def mediana_local(imagem):
    linhas, colunas = imagem.shape
    resultado = np.zeros_like(imagem)
    
    for i in range(linhas):
        for j in range(colunas):
            # Definir os limites da máscara
            i_min = max(i - 1, 0)
            i_max = min(i + 2, linhas)
            j_min = max(j - 1, 0)
            j_max = min(j + 2, colunas)
            
            # Extrair a região da máscara
            regiao = imagem[i_min:i_max, j_min:j_max]
            # Calcular a mediana local
            resultado[i, j] = np.median(regiao)
    
    return resultado

lMRIfiltrada = mediana_local(IMRI_normalizada)
print("Imagem filtrada com mediana local calculada.")   


"""
b. Teste sua rotina acima usando a função “scipy.signal.medfilt2d”.
Imagens filtradas usando a função e a rotina manual devem ser iguais, ou muito próximas.
**** Mas não ficaram iguais, por que? ****
"""

from scipy.signal import medfilt2d
lMRIfiltrada_scipy = medfilt2d(IMRI_normalizada, kernel_size=3)
print("Imagem filtrada usando scipy.signal.medfilt2d calculada.")

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title('1. Imagem original')
plt.imshow(IMRI_normalizada, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('2. Mediana local 3x3')
plt.imshow(lMRIfiltrada, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('3. medfilt2d 3x3')
plt.imshow(lMRIfiltrada_scipy, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()

"""
3. → No Editor, use a função scipy.signal.gaussian (ou implemente da fórmula
original). Crie uma função gaussiana unidimensional (g(x)), que contenha 9
amostras ( x =0:8), e que possua média 4 e desvio padrão de 1

a. Plote esta função, mostre e explique para o professor.

b. Construa uma máscara 2D com valores seguindo distribuição
Gaussiana. Uma função bidimensional Gaussiana pode ser construída a
partir da convolução da máscara unidimensional com sua transposta,
ou seja:

w_Gauss2D = g1* gtranspose1;
obs: no Python deve-se fazer o seguinte procedimento
g1 = np.zeros((9,9), float)
g1[4,:] = g
gtranspose1 = np.transpose(g1)
w_Gauss2D = scipy.signal.convolve2d(g1,gtranspose1,'same')

c. Exiba a imagem e verifique se está coerente com o esperado?
plt.figure()
plt.title('w_Gauss2D ')
plt.imshow(w_Gauss2D , cmap='gray') # cmap='jet'
"""

from scipy.signal import gaussian, convolve2d
x = np.arange(9)
g = gaussian(9, std=1)
plt.figure()
plt.plot(x, g)
plt.title('Função Gaussiana Unidimensional')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.grid()
plt.show()

g1 = np.zeros((9, 9), float)
g1[4, :] = g
gtranspose1 = np.transpose(g1)
w_Gauss2D = convolve2d(g1, gtranspose1, mode='same')
plt.figure()
plt.title('Máscara Gaussiana 2D')
plt.imshow(w_Gauss2D, cmap='gray')
plt.colorbar()
plt.show()

"""
4. Faça a convolução entre a imagem mamography.pgm e a máscara Gaussiana,
e exiba a imagem filtrada. A mesma funcionou como filtro de suavização?
obs1: pode usar a a função scipy.signal.convolve2d
obs2: normalize a máscara w_Gauss2D chame de
w_Gauss2DNormalizado , no qual o somatório desta, seja igual a 1.
Assim, a convolução não acrescentara nível DC na imagem filtrada.
MamoFilt =
scipy.signal.convolve2d(Mamo,w_Gauss2DNormalizado,'same')
"""

image_path = Path(__file__).resolve().parents[1] / 'ImagensAula' / 'Mamography.pgm'
Mamo = imread(str(image_path))
Mamo_normalizada = Mamo / 255.0
w_Gauss2DNormalizado = w_Gauss2D / np.sum(w_Gauss2D)
MamoFilt = convolve2d(Mamo_normalizada, w_Gauss2DNormalizado, mode='same')
plt.figure()
plt.title('Imagem filtrada com máscara Gaussiana 2D')
plt.imshow(MamoFilt, cmap='gray')
plt.colorbar()
plt.show()

"""
5. Usando o que aprendeu acima, faça uma função na qual o usuário indique
apenas o desvio_padrão e média, e a mesma retorne uma máscara
bidimensional com distribuição gaussiana. Seguindo o princípio de computar
primeiro a função 1D para depois a 2D, o comprimento deve ser computado
automaticamente em função da media, como abaixo.
Criar Biblioteca → Abrir um arquivo dentro da pasta Aula04 e chamar
de bibMascara.py
Dentro desta biblioteca, criar a função: fazerMascaraGauss2D usando
def da seguinte forma:
def fazerMascaraGauss2D(media, desvio):
fazer lógica.......
return wGauss2D
"""


"""
6. Programa Principal: chame a função fazerMascaraGauss2D

# import lib
import bibMascara
# chame a função com as entradas e saídas
w_Gauss2DNormalizado =
bibMascara.fazerMascaraGauss2D(media=4, desvio=1)
obs1: teste outros valores de media e desvio
a. Exiba wGass2D, para verificar se a mesma esta retornando as
dimensões corretas.
b. Faça convoluções entre a imagem e diferentes máscaras. O que
acontece quando o tamanho da máscara é aumentado?
"""

# import lib
import bibMascara
# chame a função com as entradas e saídas
w_Gauss2DNormalizado = bibMascara.fazerMascaraGauss2D(media=4, desvio=1)

plt.figure()
plt.title('Máscara Gaussiana 2D Normalizada')
plt.imshow(w_Gauss2DNormalizado, cmap='gray')
plt.colorbar()
plt.show()


"""
7. Faça uma operação de afiamento de bordas na imagem
TransversalMRI2.pgm.
a. Para criar a imagem borrada (fborrado) figura abaixo: crie uma máscara
gaussiana com média 7 e desvio 3.
"""

image_path = Path(__file__).resolve().parents[1] / 'ImagensAula' / 'TransversalMRI2.pgm'
f = imread(str(image_path))
f_normalizada = f / 255.0

wGauss2D_7_3 = bibMascara.fazerMascaraGauss2D(media=7, desvio=3)
fborrado = convolve2d(f_normalizada, wGauss2D_7_3, mode='same', boundary='symm')

# Afiamento por mascara de realce: fafiada = f + (f - fborrado)
fafiada = f_normalizada + (f_normalizada - fborrado)
fafiada = np.clip(fafiada, 0.0, 1.0)

print('Mascara gaussiana 7x3 criada. Shape:', wGauss2D_7_3.shape)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title('1. MRI original')
plt.imshow(f_normalizada, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('2. fborrado (media=7, desvio=3)')
plt.imshow(fborrado, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('3. Afiamento de bordas')
plt.imshow(fafiada, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()

"""
8....
"""