"""
1. → No Editor, fazer dois vetores, kernel w e sinal f, com os valores e
comprimentos descrito abaixo:
a. w = [1 2 3 2 8];
b. f = [0 0 0 1 0 0 0 0];
Crie um vetor fpadding, vetor f acima preenchido com zeros. Para o
preenchimento obtenha um vetor pad com comprimento de Lw - 1, e insira-o
nas posições iniciais e finais de f, para que f possua comprimento de:
– L = Lo+2*(Lw - 1)
– nos quais Lo é o comprimento inicial do sinal e Lw é o comprimento
do kernel.
– fpadding = [0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0];
Obs.: Use a função np.zeros e np.concatenate((pad,f,pad), axis=None)
"""

import numpy as np
w = np.array([1, 2, 3, 2, 8])
f = np.array([0, 0, 0, 1, 0, 0, 0, 0])
pad = np.zeros(len(w) - 1)
fpadding = np.concatenate((pad, f, pad), axis=None)
print(fpadding) 
print("Comprimento de f:", len(f))
print("Comprimento de w:", len(w))
print("Comprimento de fpadding:", len(fpadding))

"""
2. No Editor, fazer um loop de “for” que faça a varredura de todo o vetor
fpadding.
Obs.: Pode usar L = np.shape(fpadding), lembrando que o valor do
comprimento está em L[0]
"""
L = np.shape(fpadding)
#for i in range(L[0]):
#    print(fpadding[i])

"""
3. Altere o loop de “for” para fazer a operação de correlação cruzada entre w e
fpadding, ou seja a soma dos produtos entre os vetores.
for...
cor[i] = ....
Obs.: declare cor = np.zeros(.....)
para multiplicar elemento de vetores faça a[0:5]*b[0:5]
use a função np.sum para somar
"""

print("Comprimento de fpadding:", L[0])
cor = np.zeros(L[0] - len(w) + 1)
for i in range(L[0] - len(w) + 1):
    cor[i] = np.sum(w * fpadding[i:i+len(w)])
    print(fpadding[i:i+len(w)])
    print(w)
    print(cor[i])
print(cor)

"""
4. Use a função de abaixo para verificar o resultado.
corFuncao = np.correlate(f,w,"full")
"""

corFuncao = np.correlate(f, w, "full")
print("Resultado da correlação cruzada usando np.correlate:", corFuncao)

"""
5. Recorte o início e o fim do vetor do resultado Final cor, para que este tenha o
tamanho do sinal original de f ou seja, 8 posições.
ccrop[0:7] = cor[??:??]
"""

print("cor: ", cor)
print("len de cor: ", len(cor))
ccrop = cor[len(w)-1:len(w)-1+len(f)] # Conferir!
print("Resultado da correlação cruzada recortada:", ccrop)

"""
6. Usando a função “zeros”
, crie uma matriz chamada “f” e outra “c” de 5 linhas
e 5 colunas preenchidas com zeros, na matriz “f”, faça f tipo float. Substitua
o valor na posição [2,2] pelo valor 1 (Figura). Adicionalmente, crie uma
máscara w com os valores abaixo. Usando a função “np.shape”, armazene o
número de linhas M, e colunas N de f.
Obs.: criar Matrizes exemplo a = np.array([[2,3],[4,5]])
"""

f = np.zeros((5, 5), dtype=float)
c = np.zeros((5, 5))
f[2, 2] = 1
w = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
M, N = np.shape(f)

"""
7. Faça uma função de correlação 2D entre a matriz f e a máscara w, usando
apenas 2 “for”, apenas para varrer a imagem. Para não precisar fazer o
preenchimento com zeros, ajuste o início e o fim do loop de tal forma que a
abaixo.
máscara esteja posicionada dentro da matriz f, como mostrado na figura
for...Varrer linhas da imagem
for... Varrer colunas da imagem
cor2[l,c] = .......
"""

print("Matriz f:\n", f)
print("Máscara w:\n", w)

cor2 = np.zeros((M - len(w) + 1, N - len(w) + 1))
for l in range(M - len(w) + 1):
    for c in range(N - len(w) + 1):
        print(f[l:l+len(w), c:c+len(w)])
        cor2[l, c] = np.sum(w * f[l:l+len(w), c:c+len(w)])
print("Resultado da correlação 2D:\n", cor2)

"""
8. (Deixar por último como desafio) Faça novamente função de correlação 2D
entre a matriz f e o máscara w, como anteriormente. Porém agora usando 4
“for”, 2 para varrer a imagem e 2 para varrer a máscara fazendo
multiplicação e soma.

for...Varrer linhas da imagem
    for... Varrer colunas da imagem
        soma..
        for...Varrer linhas da mascara
            for... Varrer colunas da mascara
                ......
            end
        end
        c(x,y) = .......
    end
end
"""

cor2_manual = np.zeros((M - len(w) + 1, N - len(w) + 1))
for l in range(M - len(w) + 1):
    for c in range(N - len(w) + 1):
        soma = 0
        for i in range(len(w)):
            for j in range(len(w)):
                soma += w[i, j] * f[l + i, c + j]
        cor2_manual[l, c] = soma
print("Resultado da correlação 2D manual:\n", cor2_manual)

"""
9. Novamente faça a correlação 2D entre a matriz f e o máscara w, usando a
função abaixo. O resultado foi o mesmo? Por quê o tamanho da matriz de
correlação não é o mesmo?
corFuncao2 = scipy.signal.correlate2d(f, w, boundary='symm', mode='same')
Obs.: import scipy.signal
"""

import scipy.signal
corFuncao2 = scipy.signal.correlate2d(f, w, boundary='symm', mode='same')
print("Resultado da correlação 2D usando scipy.signal.correlate2d:\n", corFuncao2)

"""
10. Leia e já normalize como float a imagem e exiba a imagem mamograph.pgm.
i0 = cv2.imread(' mamograph.pgm', 0) # Gray
in0 = skimage.img_as_float(i0)
a. Crie uma mascara w de dimensões 3x3 preenchidas por “1s”, use a
função “ones”. Multiplique por um “fator” para que cada coeficiente
de correlação computado represente a média dos pixels dentro da
área da máscara. Qual deve ser o valor desse fator para que isto
ocorra?
"""

import cv2
import skimage
from pathlib import Path

image_path = Path(__file__).resolve().parents[1] / 'ImagensAula' / 'Mamography.pgm'
i0 = cv2.imread(str(image_path), 0)  # Gray
print("Shape da imagem original:", i0.shape)
if i0 is None:
    raise FileNotFoundError(f'Nao foi possivel abrir a imagem: {image_path}')
in0 = skimage.img_as_float(i0)
print("Imagem original (normalizada):\n", in0)
w = np.ones((3, 3)) * (1/9)  # Fator para média dos pixels dentro da área da máscara
print("Máscara w:\n", w)

"""
b. Faça a correlação ente in0 e w, usando a função
“scipy.signal.correlate2d”
. Exiba os coeficientes de correlação como
uma imagem. O que houve com a imagem? Por quê?
in0Filt = scipy.signal.correlate2d (....);
in0Filt = skimage.exposure.rescale_intensity(in0Filt, in_range=(0,1))
plt.figure()
plt.title('imFilt0')
plt.imshow(in0Filt, cmap='gray')
"""

in0Filt = scipy.signal.correlate2d(in0, w, boundary='symm', mode='same')
in0Filt = skimage.exposure.rescale_intensity(in0Filt, in_range=(0, 1))

"""
c. Refaça a correlação para máscaras de 5x5 e 10x10, recalculando o fator
para cada uma das matrizes. Quais os novos valores? Exiba as duas e
explique o que houve com as imagens?
"""

w5 = np.ones((5, 5)) * (1/25)  # Fator para média dos pixels dentro da área da máscara 5x5
w10 = np.ones((10, 10)) * (1/100)  # Fator para média dos pixels dentro da área da máscara 10x10
in0Filt5 = scipy.signal.correlate2d(in0, w5, boundary='symm', mode='same')
in0Filt5 = skimage.exposure.rescale_intensity(in0Filt5, in_range=(0, 1))
in0Filt10 = scipy.signal.correlate2d(in0, w10, boundary='symm', mode='same')
in0Filt10 = skimage.exposure.rescale_intensity(in0Filt10, in_range=(0, 1))


import matplotlib.pyplot as plt
plt.figure(figsize=(12, 9))

plt.subplot(2, 2, 1)
plt.title('Original')
plt.imshow(in0, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Filtro Media 3x3')
plt.imshow(in0Filt, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('Filtro Media 5x5')
plt.imshow(in0Filt5, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('Filtro Media 10x10')
plt.imshow(in0Filt10, cmap='gray')
plt.axis('off')

plt.suptitle('Comparacao: imagem original e filtros de media', fontsize=14)
plt.tight_layout()
plt.show()