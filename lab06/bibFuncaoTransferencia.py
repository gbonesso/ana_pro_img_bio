"""
3. Faça uma função que crie uma máscara, que será usada como função de
transferência de um filtro passa baixa ideal.
a. Para esta, o usuário fornecerá o número M de linhas, N de colunas e fc
(frequência normalizado entre 0 e 1 do valor máximo).
def fazerMascaraIdeal2D(M, N, fc):
.
.
return H_Ideal
"""

import numpy as np

def fazerMascaraIdeal2D(M, N, fc):
    H_Ideal = np.zeros((M, N), dtype=float)
    centro_linha = M // 2
    centro_coluna = N // 2
    raio = int(fc * min(centro_linha, centro_coluna))
    
    for l in range(M):
        for c in range(N):
            distancia = np.sqrt((l - centro_linha) ** 2 + (c - centro_coluna) ** 2)
            if distancia <= raio:
                H_Ideal[l, c] = 1.0
            else:
                H_Ideal[l, c] = 0.0
                
    return H_Ideal

"""
4. → Faça uma função que crie uma máscara, que será usada como função de
transferência de um filtro passa baixa gaussiano (figura abaixo).
a. Para esta, o usuário fornecerá o número M de linhas, N de colunas e fc
(frequência normalizado entre 0 e 1 do valor máximo).
def fazerMascaraGaussiana2D(M, N, fc):
.
.
return H_Gauss
"""

def fazerMascaraGaussiana2D(M, N, fc):
    H_Gauss = np.zeros((M, N), dtype=float)
    centro_linha = M // 2
    centro_coluna = N // 2
    sigma = fc * min(centro_linha, centro_coluna) / 2
    
    for l in range(M):
        for c in range(N):
            distancia = np.sqrt((l - centro_linha) ** 2 + (c - centro_coluna) ** 2)
            H_Gauss[l, c] = np.exp(- (distancia ** 2) / (2 * sigma ** 2))
                
    return H_Gauss

"""
5. → Faça uma função que crie uma máscara, que será usada como função de
transferência de um filtro passa baixa butterworth (figura abaixo).
a. Para esta, o usuário fornecerá o número M de linhas, N de colunas e fc
(frequência normalizado entre 0 e 1 do valor máximo) e n é o número
de polos do filtro.
def fazerMascaraButter2D (M, N, fc, n):
.
.
return H_Butter
"""

def fazerMascaraButter2D(M, N, fc, n):
    H_Butter = np.zeros((M, N), dtype=float)
    centro_linha = M // 2
    centro_coluna = N // 2
    D0 = fc * min(centro_linha, centro_coluna)
    
    for l in range(M):
        for c in range(N):
            distancia = np.sqrt((l - centro_linha) ** 2 + (c - centro_coluna) ** 2)
            H_Butter[l, c] = 1 / (1 + (distancia / D0) ** (2 * n))
                
    return H_Butter

