"""
Imagens Biomédicas – Lab07-Python
Tutores: André Arruda / Maíra Suzuka Kudo / Eric Rocha Santos
Professor: Matheus Cardoso Moraes
FILTRO DE LEE – (RESTAURAÇÃO)
EXERCÍCIOS:

1. Leia e exiba a imagem UltrassomBebe.pgm;
a. Usando a função cv2.selectROI, obtenha as localizações:
Lmin, Lmax, Cmin, Cmax da região selecionada. Obs. Estas posições
devem ser números inteiros para que elas sejam usadas como índices.
b. Obtenha a média e variância dentro da região selecionada, e chame-as de mediaLocal e varianciaLocal.
"""

from pathlib import Path
import cv2
import numpy as np

image_path = Path(__file__).resolve().parents[1] / 'ImagensAula' / 'UltrassomBebe.pgm'
ultrasom = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
#cv2.imshow('Ultrassom', ultrasom)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

roi = cv2.selectROI('Ultrassom', ultrasom)
x, y, w, h = map(int, roi)
Lmin, Lmax = y, y + h
Cmin, Cmax = x, x + w
regiao_selecionada = ultrasom[Lmin:Lmax, Cmin:Cmax]
mediaLocal = np.mean(regiao_selecionada)
varianciaLocal = np.var(regiao_selecionada)
print("Média local:", mediaLocal)
print("Variância local:", varianciaLocal)

"""
2. Sabendo que o filtro de Lee é equivalente ao filtro da média, ponderado por
um coeficiente (k), Implemente o filtro de Lee, usando a função
cv2.selectROI, para obter a varRegHomogenia e a máscara da média para
obter a varLocal.
a. Use uma máscara 7x7 para a média
Obs. Sempre confine k entre 0 e 1 →Pode usar k = np.clip(k, 0, 1)
"""

roi_homogenea = cv2.selectROI('Regiao Homogenea', ultrasom)
x, y, w, h = map(int, roi_homogenea)
regiao_homogenea = ultrasom[y:y + h, x:x + w]
varRegHomogenia = np.var(regiao_homogenea)
print("Variância da região homogênea:", varRegHomogenia)

ultrasom_float = ultrasom.astype(np.float32)
media_7x7 = cv2.blur(ultrasom_float, (7, 7))

sobel_x = np.array([[-1, 0, 1],
					[-2, 0, 2],
					[-1, 0, 1]], dtype=np.float32)
sobel_y = np.array([[-1, -2, -1],
					[0, 0, 0],
					[1, 2, 1]], dtype=np.float32)

grad_x = cv2.filter2D(ultrasom_float, cv2.CV_32F, sobel_x)
grad_y = cv2.filter2D(ultrasom_float, cv2.CV_32F, sobel_y)
gradiente_modulo = np.sqrt(grad_x ** 2 + grad_y ** 2)
k = cv2.normalize(gradiente_modulo, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
k = np.clip(k, 0, 1)

filtro_lee = media_7x7 + k * (ultrasom_float - media_7x7)
filtro_lee = np.clip(filtro_lee, 0, 255).astype(np.uint8)

cv2.imshow('Ultrassom', ultrasom)
cv2.imshow('Modulo do Gradiente', np.clip(k * 255, 0, 255).astype(np.uint8))
cv2.imshow('Filtro de Lee', filtro_lee)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
3. Desafio ;) Altere o filtro Lee, para usar o módulo do gradiente como
identificador de borda (k).
"""


def filtro_lee_com_gradiente(imagem, tamanho_janela=7):
	imagem_float = imagem.astype(np.float32)
	media_local = cv2.blur(imagem_float, (tamanho_janela, tamanho_janela))

	grad_x = cv2.Sobel(imagem_float, cv2.CV_32F, 1, 0, ksize=3)
	grad_y = cv2.Sobel(imagem_float, cv2.CV_32F, 0, 1, ksize=3)
	modulo_gradiente = cv2.magnitude(grad_x, grad_y)

	k = cv2.normalize(modulo_gradiente, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
	k = np.clip(k, 0, 1)

	saida = media_local + k * (imagem_float - media_local)
	return np.clip(saida, 0, 255).astype(np.uint8), k


filtro_lee_gradiente, mapa_k_gradiente = filtro_lee_com_gradiente(ultrasom)

cv2.imshow('Modulo do Gradiente - k', (mapa_k_gradiente * 255).astype(np.uint8))
cv2.imshow('Filtro de Lee - Gradiente', filtro_lee_gradiente)
cv2.waitKey(0)
cv2.destroyAllWindows()