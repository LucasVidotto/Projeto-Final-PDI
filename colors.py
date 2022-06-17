import cv2  # disponibiza as funções do opencv
import numpy as np


def filtroRGB(src, r, g, b):
    if r == 0:
        src[:, :, 2] = 0  # elimina o vermelho
    if g == 0:
        src[:, :, 1] = 0  # elimina o verde
    if b == 0:
        src[:, :, 0] = 0  # elimina o azul


def show_image():
    filtro = 1

    while True:
        img = cv2.imread("imagem-cores.PNG")

        if filtro == 1:
            cv2.imshow('Estudo OpenCV- Filtro', img)

        if filtro == 2:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Estudo OpenCV- Filtro', gray)

        if filtro == 3:  # vermelho e verde
            filtroRGB(img, 1, 1, 0)
            cv2.imshow('Estudo OpenCV- Filtro', img)

        if filtro == 4:  # vermelho e azul
            filtroRGB(img, 1, 0, 1)
            cv2.imshow('Estudo OpenCV- Filtro', img)

        if filtro == 5:  # verde e azul
            filtroRGB(img, 0, 1, 1)
            cv2.imshow('Estudo OpenCV- Filtro', img)

        if filtro == 6:  # vermelho
            filtroRGB(img, 1, 0, 0)
            cv2.imshow('Estudo OpenCV- Filtro', img)

        if filtro == 7:  # verde
            filtroRGB(img, 0, 1, 0)
            cv2.imshow('Estudo OpenCV- Filtro', img)

        if filtro == 8:  # azul
            filtroRGB(img, 0, 0, 1)
            cv2.imshow('Estudo OpenCV- Filtro', img)

        ret = cv2.waitKey(1)

        if ret == 27:
            break

        elif ret == -1:
            continue

        elif ret == 49:
            filtro = 1

        elif ret == 50:
            filtro = 2


        elif ret == 51:
            filtro = 3

        elif ret == 52:
            filtro = 4

        elif ret == 53:
            filtro = 5


        elif ret == 54:
            filtro = 6

        elif ret == 55:
            filtro = 7

        elif ret == 56:
            filtro = 8

    cv2.destroyAllWindows()


def main():
    show_image()
    return 0


if __name__ == '__main__':
    main()