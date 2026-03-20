"""
5. → No Editor(review.py), importe as bibliotecas abaixo:
import numpy as np
import matplotlib.pyplot as plt
import cv2 # OpenCV
import skimage
import skimage.exposure

Caso não consigam usar o pip install se refiram ao material do link abaixo:

https://dicasdepython.com.br/resolvido-pip-nao-e-reconhecido-como-um-comando-interno/#:~:text=Uma%20situa%C3%A7%C3%A3o%20que%20pode%20acontecer,gente%20usa%20o%20pr%C3%B3prio%20python.
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2 # OpenCV
import skimage
import skimage.exposure

"""
6. Atribuição de Valores em variáveis
    a. # atribuição de variaveis
    b. i = 0 # Positivos
    c. i = -192 #negativo
    d. b = 0b0100 #binario
    e. h = 0xFF # hexadecimal
    f. f1= 2.565 # float
    g. f2 = 1e3
    h. boo = True # booleana
    i. s = "one" # string
"""
i = 0 # Positivos
i = -192 #negativo
b = 0b0100 #binario
h = 0xFF # hexadecimal
f1= 2.565 # float
f2 = 1e3
boo = True # booleana
s = "one" # string

"""
7. Promova as conversões de variáveis abaixo e verifique a alteração
no explorador de variáveis.
    a. i=1
    b. f = float(i)
    c. boo1 = bool(i)
    d. boo2 = True
    e. i = int(f)
    f. bn = int(boo2)
"""
i=1
f = float(i)
boo1 = bool(i)
boo2 = True
i = int(f)
bn = int(boo2)

"""
8. Diferença entre acessar índice e slice.
    a. Indice → Usado para acessar valores de índices, únicos
        i. → lst[index]
    b. Slice → Usado para definir intervalo de índices
        i. → lst[start slice : end slice : step]
    c. Use a função len para obter o comprimento da lista len(lst)
    d. A partir da lista declarada acima, acesse individualmente os
    índices:→ [0],[1], [2], [4].
    e. A partir da lista declarada acima, acesse os intervalos de
    Slices: → [0:4], [1:4], [2:4].
"""
lst=[10, 20, 30, 40, 50]
print('Comprimento da lista: ', len(lst)) # Comprimento da lista: 5
print(lst[0]) # Acessando índice 0 -> 10
print(lst[1]) # Acessando índice 1 -> 20
print(lst[2]) # Acessando índice 2 -> 30
print(lst[4]) # Acessando índice 4 -> 50
print(lst[0:4]) # Acessando slice do índice 0 ao 3 -> [10, 20, 30, 40]
print(lst[1:4]) # Acessando slice do índice 1 ao 3 -> [20, 30, 40]
print(lst[2:4]) # Acessando slice do índice 2 ao 3 -> [30, 40]

"""
9. Diferença entre Lista, e Vetor(Array).
    a. Conjunto de dados que pode ser de diferentes tipos
        i. lst1 = [10, "2", 1e3, 0xFF, True]
        ii. lst = [10, 20, 30, 40, 50]
    b. Array é um vetor que contém um conjunto dados do mesmo
    tipo. Ex. apenas float, apenas string, apenas int, etc.
    c. Use o NumPy para Transformar a lista lst acima em um
    vetor(array).
        i. import numpy as np
        ii. vetor = np.array(lst) # array de inteiros
"""

lst1 = [10, "2", 1e3, 0xFF, True]
vetor = np.array(lst) # array de inteiros
print('Lista lst1: ', lst1) # Lista lst1:  [10, '2', 1000.0, 255, True]
print('Vetor: ', vetor) # Vetor:  [10 20 30 40 50]
print('Tipo da lista lst1: ', type(lst1)) # Tipo da lista lst1:  <class 'list'>
print('Tipo do vetor: ', type(vetor)) # Tipo do vetor:  <class 'numpy.ndarray'>

"""
10. Diferença entre ListaMatriz, e MatrizArray.
    a. matList = [[1,2,3], [4,5,6], [7,8,9]]
        i. matList[index] → Neste caso apenas 3 posições
    b. matArray = np.array([[1,2,3], [4,5,6], [7,8,9]])
        i. Index→ matArray [indexLinha , IndexColuna]
            1. Acesse os endereços da matArray → [0,0], [0,1],
            [0,2], e [2,0]
        ii. slices→ matArray [sliceStartLinha: sliceStopLinha,
        sliceStartColuna: sliceStopColuna]
            1. Acesse os intervalos(slices) da matArray →
            [0:3 ,0:3], [0:2,0:2], [:,0], [0,0:2]
"""
matList = [[1,2,3], [4,5,6], [7,8,9]]
matArray = np.array(matList)
print('Matriz Lista: ', matList) # Matriz Lista:  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('Matriz Array: ', matArray) # Matriz Array:  [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
print('Acessando matArray[0,0]: ', matArray[0,0]) # Acessando matArray[0,0]:  1
print('Acessando matArray[0,1]: ', matArray[0,1]) # Acessando matArray[0,1]:  2
print('Acessando matArray[0,2]: ', matArray[0,2]) # Acessando matArray[0,2]:  3
print('Acessando matArray[2,0]: ', matArray[2,0]) # Acessando matArray[2,0]:  7
print('Acessando matArray[0:3,0:3]: ', matArray[0:3,0:3]) # Acessando matArray[0:3,0:3]:  [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
print('Acessando matArray[0:2,0:2]: ', matArray[0:2,0:2]) # Acessando matArray[0:2,0:2]:  [[1 2]
#  [4 5]]
print('Acessando matArray[:,0]: ', matArray[:,0]) # Acessando matArray[:,0]:  [1 4 7]
print('Acessando matArray[0,0:2]: ', matArray[0,0:2]) # Acessando matArray[0,0:2]:  [1 2]   

print('Acessando matList[0][0]: ', matList[0][0]) # Acessando matList[0][0]:  1
print('Acessando matList[0][1]: ', matList[0][1]) # Acessando matList[0][1]:  2
print('Acessando matList[0][2]: ', matList[0][2]) # Acessando matList[0][2]:  3
print('Acessando matList[2][0]: ', matList[2][0]) # Acessando matList[2][0]:  7
print('Acessando matList[0:3][0:3]: ', matList[0:3][0:3]) # Acessando matList[0:3][0:3]:  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('Acessando matList[0:2][0:2]: ', matList[0:2][0:2]) # Acessando matList[0:2][0:2]:  [[1, 2, 3], [4, 5, 6]]
print('Acessando [linha[0] for linha in matList] ', [linha[0] for linha in matList]) # Acessando [linha[0] for linha in matList]  [1, 4, 7]
print('Acessando matList[0][0:2]: ', matList[0][0:2]) # Acessando matList[0][0:2]:  [1, 2]    

"""
11. Conversão de Base de Vetor e Matriz
    a. vetorFloat = vetor.astype(float)
    b. matArrayFloat = matArray.astype(np.float)
    c. matArrayString = matArray.astype(np.str)
"""
vetorFloat = vetor.astype(float)
matArrayFloat = matArray.astype(float) # Note: np.float is deprecated, use float instead
matArrayString = matArray.astype(str) # Note: np.str is deprecated, use str instead
print('Vetor convertido para float: ', vetorFloat) # Vetor convertido para float:  [10. 20. 30. 40. 50.]
print('Matriz Array convertida para float: ', matArrayFloat) # Matriz Array convertida para float:  [[ 1.  2.  3.]
#  [ 4.  5.  6.]
#  [ 7.  8.  9.]]
print('Matriz Array convertida para string: ', matArrayString) # Matriz Array convertida para string:  [['1' '2' '3']
#  ['4' '5' '6']
#  ['7' '8' '9']]   