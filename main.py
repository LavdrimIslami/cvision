import cv2 as cv
import numpy as np

def basicOps():
    ### BASIC OPERATIONS ###
    img = cv.imread("tetrominoe.png")

    assert img is not None, "cant be read"

    #accessing pixel values

    px = img[100,100]

    print(px)


    print("modify a pixel value")
    img[100,100] = [255,255,255]
    print(img[100,100])

    print("\nImage Properties access")
    print("image shape", img.shape)
    print("image size", img.size)
    print("image datatype", img.dtype)

    




def main():
    basicOps()

if __name__ == "__main__":
    main()