"""
Importa as Funções abaixo, caso precise instale, pip install xxx, e reinicie o
kernel
    a. import numpy as np
    b. import matplotlib.pyplot as plt
"""
import numpy as np
import matplotlib.pyplot as plt
import math

"""
Considerando a biblioteca Numpy, implemente todas as funções descritas
abaixo, descrevendo em comentários no corpo do código.py qual é o propósito
de cada uma delas. Caso seja necessário, refira-se a documentação do numpy
ou função disponível na internet:
“NumPy for MATLAB users”
https://numpy.org/doc/stable/user/numpy-for-matlab-users.html
1. # Help
    a. help()
    b. help(plt)
"""
help()
help(plt)

"""
2. # Operadores aritméticos
    a. #Assignment; defining a number
        a=3; b=1
    b. #Addition
        a + b
        np.add(a,b)
    c. #Subtraction
        a - b
        np.subtract(a,b)
    d. #Multiplication
        a * b
        np.multiply(a,b)
    e. #Division
        a / b
        np.divide(a,b)
    f. #Power, $a^b$
        a ** b
        np.power(a,b)
        pow(a,b)
    g. # Remainder
        a % b
        np.remainder(a,b)
        np.fmod(a,b)
    h. # Incremento → Muito usado em loops
        a+=1 # a = a + 1
        a+=b # a = a + b
    i. #Factorial, $n!$
        np.math.factorial(4)
"""
a=3; b=1
print(a + b)
print(np.add(a,b))
print(a - b)
print(np.subtract(a,b))
print(a * b)
print(np.multiply(a,b))
print(a / b)
print(np.divide(a,b))
print(a ** b)
print(np.power(a,b))
print(pow(a,b))
print(a % b)
print(np.remainder(a,b))
print(np.fmod(a,b))
a+=1 # a = a + 1
print(a)
a+=b # a = a + b
print(a)
print(math.factorial(4))


"""
3. # Operadores Relacionais--> Muito usados em Condicionais e Loops
    a. #Equal
        a == b
        np.equal(a,b)
    b. #Less than
        a < b
        np.less(a,b)
    c. #Greater than
        a > b
        np.greater(a,b)
    d. #Less than or equal
        a <= b
        np.less_equal(a,b)
    e. #Greater than or equal
        a >= b
        np.greater_equal(a,b)
    f. #Not Equal
        a != b
        np.not_equal(a,b)
"""


"""
4. # Operadores Lógicos --> Muito usados em Condicionais e Loops
    a. #Element-wise logical AND
        np.logical_and(a,b)
        a and b
    b. #Element-wise logical OR
        np.logical_or(a,b)
        a or b
    c. #Logical EXCLUSIVE OR
        np.logical_xor(a,b)
        not(a)
    d. #Logical NOT
        np.logical_not(a)
        not a
    e. #True if any element is nonzero
        np.any(a)
    f. #True if all elements are nonzero
        np.all(a)
"""


"""
5. # raiz e logaritmo
    a. #Square root
        np.math.sqrt(a)
        a**0.5 #raiz quadrada
    b. #Logarithm, base $e$ (natural)
        np.math.log(a)
    c. #Logarithm, base 10
        np.math.log10(a)
    d. #Logarithm, base 2 (binary)
        np.math.log(a, 2)
    e. #Exponential function
        np.math.exp(a)
"""


"""
6. # Arredondamentos
    a=1.5 # Varie de valores para entender e explorar as operações
    a. #Round
        np.around(a)
    b. #Round up
        np.ceil(a)
    c. #Round down
        np.floor(a)
    d. #Round towards zero
        np.fix(a)
"""


"""
7. # Constantes
    a. #$\pi=3.141592$
        np.math.pi
    b. #$e=2.718281$
        np.math.e
        np.math.exp(1) # Varie de valores para explorar a operação
"""


"""
8. # Valores ausentes
    np.nan # Not a Number
    np.inf #Infinity, $\infty$
"""


"""
9. # Números Complexos
    a. #A complex number, $3+4i$
        z = 1j #Imaginary unit
        z = 3+4j
        z = complex(3,4)
    b. #Absolute value (modulus)
        abs(3+4j)
    c. # Real part
        z.real
        np.real(z)
    d. #Imaginary part
        z.imag
        np.imag(z)
    e. #Complex Conjugate
        z.conjugate()
        np.conjugate(z)
"""


"""
10.# Gerando números e sequencia de números aleatórios → Observar tamanho
    e tipo de base
    a. a = np.random.random((10,)) # 10 numbers between 0 and 1
    b. b = np.random.uniform((10,)) # 1 nymber between 0 and 10
    c. c = np.random.uniform(2,7,(10,)) #10 number Uniform distribution :
    #Numbers between 2 and 7
    d. d = np.random.uniform(0,1,(6,6)) # Uniform: 6,6 array
    e. f = np.random.standard_normal((10,))# 10 number Normal distribution
"""


"""
11.# Vetores → Observar tamanho e tipo de base
    a. a = np.array([2,3,4,5]) # Row vector, $1 \times n$-matrix
    b. b = np.array([2,3,4,5]).reshape(-1,1)
"""


"""
12. # Sequencias
    a. c = np.arange(start=1, stop=11,step=None, dtype= int) #1,2,3, ... ,10
    b. d = np.arange(0, 5, 0.5, float)
    c. e = np.arange(10.) #0.0,1.0,2.0, ... ,9.0
    d. f = np.arange(1,11,3) #1,4,7,10
    e. g = np.arange(10,0,-1) #10,9,8, ... ,1
    f. h = np.arange(10,0,-3) #10,7,4,1
    g. i = np.linspace(1,10,7) #Linearly spaced vector of n=7 samples
    h. j = a[::-1] # Reverse Espelho
    i. l = np.array([1,2,3])
    j. l[:] = 3 #Set all values to same scalar value
    k. m = range(1,11) # 1:11
    l. m = range(6) # 0:6
    m. for n in m:
        print(n) # arrumar identação
    n. for n in range(6): # Muito usado
        print(n) # arrumar identação
"""


"""
13.# Concatenar
    a. o1 = np.concatenate((a,a)) # Concatenate two vectors
    b. o2 = np.concatenate((range(1,5),a), axis=0)
    c. o3 = np.concatenate((a,range(1,5)), axis=0)
"""

"""
14.# Endereçamento de vetores
    a. p1 = a[:] # == a[0:len(a)]
    b. p2 = a[0:] # == a[0:len(a)]
    c. p3 = a[2] # Lembrar da diferença entre index e slice.
    d. p4 = a[0:2] # Lembrar da diferença entre index e slice.
    e. p5 = a[1:] #miss the first element
    f. p6 = a[-1] #last element
    g. p7 = a[-2:] #last two elements
"""


"""
15.# # Maximum and minimum
    a. q1 = np.max(a)
    b. q2 = np.maximum(a,f) #pairwise max--> Maximo pareado entre dois
    vetores
    c. q3 = np.min(a)
    d. q4 = np.minimum(a,f) #pairwise min--> Minimo pareado entre dois
    vetoresEndereçamento
"""


"""
16.# Multiplicação de Vetor
    a. r1 = a*a # Multiplicação entre elementos pareados dos vetores
    b. r2 = a*f # Multiplicação entre elementos pareados dos vetores
    c. r3 = a*o1[ : len(a)] # fazer endereçamento quando tamanho é
    diferente
"""


"""
17.#Matriz e Concatenar Matriz
    a. s1 = np.array([[2,3],[4,5]]) #Define a matrix
    b. s2 = np.array([[6,7],[8,9]]) #Define a matrix
    c. s3 = np.concatenate((s1,s2), axis=0) # Concatena em linha
    d. s4 = np.vstack((s1,s2)) # Empilha em linha
    e. s5 = np.concatenate((s1,s2), axis=1) # Concatena em coluna
    f. s6 = np.hstack((s1,s2)) # Empilha em coluna
    g. s7 = np.dstack((s1,s2))# Empilha em slice – profundidade
    h. s8 = np.concatenate((s1,s2), axis=None) #Concatenate matrices into
    one vector
"""

"""
18.#Array creation
    a. t1 = np.zeros((3,5),float) #0 filled array
    b. t2 = np.zeros((3,5), int) #0 filled array of integers
    c. t3 = np.ones((3,5),float) #1 filled array
    d. t4 = np.identity(3) #Identity matrix
    e. t5 = np.diag((4,5,6)) #Diagonal
    f. t5 = np.empty((3,3)) #Empty array
"""

"""
19.Endereçamento de Matriz → Atenção a diferença entre index e slice.
    a. #Input is a 3,4 array
    b. a1 = np.array([[ 11, 12, 13, 14 ],
                      [ 21, 22, 23, 24 ],
                      [ 31, 32, 33, 34 ]])
    c. a2 = a1[1,2]
    d. a3 = a1[0,] #First row
    e. a4 = a1[:,0] #First column
    f. a5 = a1[1:,]# All, except first row
    g. a6 = a1[-2:,] #Last two rows
    h. a7 = a1[::2,:] #Strides: Every other row
    i. a8 = a1[...,2] #Third in last dimension (axis)
    j. a9= a1.diagonal(offset=0)# Diagonal
"""


"""
20.Alteração de valores na Matriz Origem
    a. a1[:,0] = 99
    b. a1[:,0] = np.array([99,98,97])
    c. #Clipping: Replace elements
    d. (a1>90).choose(a1,90)
    e. a1.clip(min=None, max=90)
    f. a1.clip(min=2, max=5)
"""


"""
21.Atribuição e aquisição de Valores alterados em Novos Parâmetros
    a. a10 = a1[:,0] = 99
    b. a11 = a1[:,0] = np.array([99,98,97])
    c. #Clipping: Replace elements
    d. a12 = (a1>90).choose(a1,90)
    e. a13 = a1.clip(min=None, max=90)
    f. a14 = a1.clip(min=2, max=5)
"""


"""
22.#Somas
    a. #Input is a 3,4 array
    b. a15 = np.array([[ 1, 1, 1, 1 ],
                       [ 1, 1, 1, 1 ],
                       [ 1, 1, 1, 1 ]])
    c. a16 = a1.sum() # Sum of all elements
    d. a16 = np.sum(a1) # Sum of all elements--> Alternativo
    e. a17 = a1.sum(axis=0) #Sum of each column
    f. a17 = np.sum(a1,axis=0) #Sum of each column --> Alternativo
    g. a18 = a1.sum(axis=1) #Sum of each row
    h. a18 = np.sum(a1, axis=1) #Sum of each row --> Alternativo
    i. a19 = a1.trace(offset=0) #Sum along diagonal
    j. a20 = a1.cumsum(axis=0) #Cumulative sum (columns)
"""


"""
23.##Sorting →
    a. a21 = np.array([[4,3,2],[2,8,6],[1,4,7]]) #Example data
    b. # Flat and sort
    c. s2 = s1.ravel() # Flat
    d. s2 = np.ravel(s1)# Flat
    e. s3 = np.sort(s2) #sort
    f. s4 = np.sort(s1, axis=0) # Sort each column
    g. s5 = np.sort(s1, axis=1) #Sort each row
    h. s6 = np.argsort(s1) # return indices for sort Matrix
    i. s7 = np.argsort(s2) # return indices for sort flaten (vector)
    j. s7 =s1.ravel().argsort() # flaten (vector), return indices
    k. s8 =s1.argsort(axis=0) # return indices for Sort by column,
    l. s9 =s1.argsort(axis=1) # return indices for Sort by row,
"""

"""
24.# Maxi and Min
    a. s1 = np.array([[4,3,2],[2,8,6],[1,4,7]]) #Example data
    b. r1 = np.array([[5,2,3],[1,5,9],[2,3,6]]) #Example data
    c. r2 = np.max(r1, axis=0) # max in each colum
    d. r3 = np.max(r1, axis=1) # max in each row
    e. r4 = np.max(r1) # max in matrix
    f. r5 = np.min(r1, axis=0) # max in each colum
    g. r6 = np.min(r1, axis=1) # max in each row
    h. r7 = np.min(r1) # max in matrix
    i. r8 = np.maximum(r1,s1) # pairwise max
    j. r9 = np.ptp(r1) # max to min range
"""


"""
25.#Size or Shape
    a. s1 = np.array([[4,3,2],[2,8,6],[1,4,7]]) #Example data
    b. s2 = np.array([[ 11, 12, 13, 14 ],[ 21, 22, 23, 24 ],[ 31, 32, 33, 34 ]])
    c. r10 = np.size(s2) # number of elements
    d. r11 = np.size(s2, axis=0) # number of rows
    e. r12 = np.size(s2, axis=1) # number of coluns
    f. r11 = np.shape(s2) # size of matrix
    g. (M,N) = np.shape(s2) # obtendo valores de linhas M, e colunas N
    h. r12 = np.ndim(s2) # number of dimensions
"""


"""
26.#Find; conditional index
    a. s1 = np.array([[4,0,2],[0,8,6],[1,4,2]])
    b. (l,c) = np.where(s1==0) # Encontre zeros →
    c. (l,c) = np.nonzero(s1) # Encontre não zeros
    d. (l,c) = np.where(s1!=0) # Encontre não zeros
    e. v1 = np.extract(s1!=0,s1) # Extrai valores diferentes que zero
    f. v2 = (s1>5.5)
"""