import cv2
from matplotlib import pyplot as plt
from H1.ImageDisk import ImageDisk

class UseCan:

    @staticmethod
    def use_can(img):
        edges = cv2.Canny(img, 100, 200)
        return edges

class ShowPlot:

    @staticmethod
    def mostrar_img(img, edges):
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()


if __name__ == '__PROYECTO__':
    img_disk = ImageDisk()
    img = img_disk.read_image('buho.jpg')
    im_edges = UseCan.use_can(img)
    img_disk.save_img(img, name_img="prueba2")
    ShowPlot.mostrar_img(img, im_edges)
