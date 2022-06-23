import cv2
import numpy as np
from matplotlib import pyplot as plt # biblioteca para histograma
import mahotas

def particao_um(tecla):
    if tecla == 0:

        img1 = cv2.imread('./Imagens-Projeto/imagem-cores.PNG')
        cv2.imshow('Primeira ', img1)

        imagem2 = cv2.imread('./Imagens-Projeto/cubos-coloridos.png')
        cv2.imshow('Segunda Imagem', imagem2)

        imagem3 = cv2.imread('./Imagens-Projeto/shape.PNG')
        cv2.imshow('Terceira Imagem', imagem3)

        imagem4 = cv2.imread('./Imagens-Projeto/Imagem Azul e Vermelho.webp')
        cv2.imshow('Quarta Imagem', imagem4)
        cv2.waitKey(0)

    if tecla == 1:
            imagem = cv2.imread('./Imagens-Projeto/imagem-cores.PNG', 0)
            imgb = cv2.imshow('original', imagem)
            h = cv2.calcHist([imagem], [0], None, [256], [0, 256])
            plt.figure()
            plt.title("Histograma")
            plt.xlabel("Intensidade")
            plt.ylabel("Pixels da Imagem")
            plt.plot(h)
            plt.xlim([0, 256])
            plt.show()

    if tecla == 2:
        print('conversão de cores RGB para HSV')
        escolha = input('escoha uma cor 1R   3G   2B  (RGB)')
        if escolha == '1': #red
            color = np.uint8([[[0, 255, 0]]])
            color_hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
            print(color_hsv)

            img = cv2.imread("./Imagens-Projeto/shape.PNG")
            image = cv2.resize(img, (700, 600))
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            lower = np.array([-10, 100, 100])
            upper = np.array([10, 255, 255])
            mask = cv2.inRange(hsv, lower, upper)
            cv2.imshow("Image", image)
            cv2.imshow("Mask", mask)
            cv2.waitKey(0)

        if escolha == '2':#blue
            color = np.uint8([[[255, 0, 0]]])#matriz de pixel
            hsv_green = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
            print(hsv_green)

            img = cv2.imread("./Imagens-Projeto/Imagem Azul e Vermelho.webp")
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
            color_hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
            print(color_hsv)

            img = cv2.imread("./Imagens-Projeto/shape.PNG")
            image = cv2.resize(img, (700, 600))
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            lower = np.array([50, 100, 100])
            upper = np.array([70, 255, 255])
            mask = cv2.inRange(hsv, lower, upper)
            cv2.imshow("Imagem", image)
            cv2.imshow("Mascara", mask)

            cv2.waitKey(0)

    if tecla == 3:

        color = np.uint8([[[0, 255, 0]]])
        cor_hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
        print(cor_hsv)
        cv2.waitKey(0)

    if tecla == 4:
        def filtroRGB(src, r, g, b):
            if r == 0:
                src[:, :, 2] = 0  # elimina o vermelho
            if g == 0:
                src[:, :, 1] = 0  # elimina o verde
            if b == 0:
                src[:, :, 0] = 0  # elimina o azul

        def show_image():
            asci = 1

            while True:
                img = cv2.imread('./Imagens-Projeto/imagem-cores.PNG')

                if asci == 1:
                    cv2.imshow('Filtros', img)

                if asci == 2:
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    cv2.imshow('Estudo OpenCV- Filtro', gray)

                if asci == 3:  # vermelho e verde
                    filtroRGB(img, 1, 1, 0)
                    cv2.imshow('Estudo OpenCV- Filtro', img)

                if asci == 4:  # vermelho e azul
                    filtroRGB(img, 1, 0, 1)
                    cv2.imshow('Estudo OpenCV- Filtro', img)

                if asci == 5:  # verde e azul
                    filtroRGB(img, 0, 1, 1)
                    cv2.imshow('Estudo OpenCV- Filtro', img)

                if asci == 6:  # vermelho
                    filtroRGB(img, 1, 0, 0)
                    cv2.imshow('Estudo OpenCV- Filtro', img)

                if asci == 7:  # verde
                    filtroRGB(img, 0, 1, 0)
                    cv2.imshow('Estudo OpenCV- Filtro', img)

                if asci == 8:  # azul
                    filtroRGB(img, 0, 0, 1)
                    cv2.imshow('Estudo OpenCV- Filtro', img)

                ret = cv2.waitKey(1)

                if ret == 27:
                    break

                elif ret == -1:
                    continue

                elif ret == 49:
                    asci = 1

                elif ret == 50:
                    asci = 2


                elif ret == 51:
                    asci = 3

                elif ret == 52:
                    asci = 4

                elif ret == 53:
                    asci = 5


                elif ret == 54:
                    asci = 6

                elif ret == 55:
                    asci = 7

                elif ret == 56:
                    asci = 8
                cv2.destroyAllWindows()

        def main2():
            show_image()
            return 0
        main2()




def main():
    print('escolha um número de 0 a 4 sendo:')
    print('0 - amostras das imagens para teste')
    print('1 - conversão para tons de cinza, e veificação com histograma')
    print('2 - Verificação de partições que tem proximidades com a cor escolhida')
    print('3 - Conversão de tons RGB para HSV')
    print('4 - Amostragem apenas do formato com a cor escolhida')
    tecla = (int(input('informa uma tecla de 0-4')))
    particao_um(tecla)
    return 0

if __name__ == '__main__':

    main()

cv2.destroyAllWindows()