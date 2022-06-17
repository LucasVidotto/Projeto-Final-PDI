import cv2
import numpy as np
from matplotlib import pyplot as plt # biblioteca para histograma
import mahotas

def particao_um(tecla):
    if tecla == 1:
        imgColorida = cv2.imread('dados.jpg')  # Carregamento da imagem
        # Se necessário o redimensioamento da imagem pode vir aqui.
        # Passo 1: Conversão para tons de cinza
        img = cv2.cvtColor(imgColorida, cv2.COLOR_BGR2GRAY)
        # Passo 2: Blur/Suavização da imagem
        suave = cv2.blur(img, (7, 7))
        # Passo 3: Binarização resultando em pixels brancos e pretos
        T = mahotas.thresholding.otsu(suave)
        bin = suave.copy()
        bin[bin > T] = 255
        bin[bin < 255] = 0
        bin = cv2.bitwise_not(bin)
        # Passo 4: Detecção de bordas com Canny
        bordas = cv2.Canny(bin, 70, 150)
        # Passo 5: Identificação e contagem dos contornos da imagem
        # cv2.RETR_EXTERNAL = conta apenas os contornos externos
        (lx, objetos, lx) = cv2.findContours(bordas.copy(),
                                             cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # A variável lx (lixo) recebe dados que não são utilizados
        escreve(img, "Imagem em tons de cinza", 0)
        escreve(suave, "Suavizacao com Blur", 0)
        escreve(bin, "Binarizacao com Metodo Otsu", 255)
        escreve(bordas, "Detector de bordas Canny", 255)
        temp = np.vstack([
            np.hstack([img, suave]),
            np.hstack([bin, bordas])
        ])
        cv2.imshow("Quantidade de objetos: " + str(len(objetos)), temp)
        cv2.waitKey(0)
        imgC2 = imgColorida.copy()
        cv2.imshow("Imagem Original", imgColorida)
        cv2.drawContours(imgC2, objetos, -1, (255, 0, 0), 2)
        escreve(imgC2, str(len(objetos)) + " objetos encontrados!")
        cv2.imshow("Resultado", imgC2)
        cv2.waitKey(0)

    if tecla == 2:
        print('conversão de cores RGB para HSV')
        escolha = input('escoha uma cor 1R   2G   3B  (RGB)')
        if escolha == '1': #red
            color = np.uint8([[[0, 255, 0]]])
            hsv_green = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
            print(hsv_green)

            img = cv2.imread("./Imagens-Projeto/frutas.webp")
            image = cv2.resize(img, (700, 600))
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            lower = np.array([-10, 100, 100])
            upper = np.array([10, 255, 255])
            mask = cv2.inRange(hsv, lower, upper)
            cv2.imshow("Image", image)
            cv2.imshow("Mask", mask)
            cv2.waitKey(0)

        if escolha == '2':#blue
            color = np.uint8([[[255, 0, 0]]])
            hsv_green = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
            print(hsv_green)

            img = cv2.imread("./Imagens-Projeto/frutas.webp")
            image = cv2.resize(img, (700, 600))
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            lower = np.array([100, 100, 100])
            upper = np.array([130, 255, 255])
            mask = cv2.inRange(hsv, lower, upper)
            cv2.imshow("Image", image)
            cv2.imshow("Mask", mask)
            cv2.waitKey(0)

        if escolha == '3':#green
            color = np.uint8([[[0, 0, 255]]])
            hsv_green = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
            print(hsv_green)

            img = cv2.imread("./Imagens-Projeto/frutas.webp")
            image = cv2.resize(img, (700, 600))
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            lower = np.array([50, 100, 100])
            upper = np.array([70, 255, 255])
            mask = cv2.inRange(hsv, lower, upper)
            cv2.imshow("Image", image)
            cv2.imshow("Mask", mask)

            cv2.waitKey(0)
    if tecla == 3:
        imagem = cv2.imread('imagem-cores.PNG',0)
        imgb = cv2.imshow('original',imagem)
        # Função calcHist para calcular o hisograma da imagem
        h = cv2.calcHist([imagem], [0], None, [256], [0, 256])
        plt.figure()
        plt.title("Histograma P&B")
        plt.xlabel("Intensidade")
        plt.ylabel("Qtde de Pixels")
        plt.plot(h)
        plt.xlim([0, 256])
        plt.show()

        cv2.waitKey(0)
    if tecla == 4:
        print('tecla : '+str(tecla))


def main():
    print('escolha um número de 1 a 4 sendo:')
    print('1 - Amostra da imagem e conversão para tons de cinza, e veificação com histograma')
    print('2 - Conversão de tons RGB para HSV')
    print('3 - Verificação de partições que tem proximidades com a cor escolhida')
    print('4 - Amostragem apenas do formato com a cor escolhida')
    tecla = (int(input('informa uma tecla de 0-9')))
    particao_um(tecla)
    return 0

if __name__ == '__main__':
    main()

cv2.destroyAllWindows()