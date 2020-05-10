import cv2


class ImageDisk:

    @staticmethod
    def read_image(path_img):
        if isinstance(path_img, str):
            try:
                img = cv2.imread(path_img, 0)
            except:
                print("Error con el path")
            return img
        else:
            print("formato de imagen invalido")
            return None
    @staticmethod
    def save_img(img , name_img):
        name_img = name_img + ".jpg"
        cv2.imwrite(name_img, img)