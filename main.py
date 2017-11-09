import os
import cv2
import scene
import obscene

def obscene_detect(img = None):
    result = obscene.detection(isRaw = True, url = None, img = img)
    print(result)
    
def controls(path, filename, shots = None):
    cap = cv2.VideoCapture()
    cap.open(path + filename)

    for i in range(shots[-1] + 1):
        (ret_val, im_cap) = cap.read()
        if i in shots:
            #obscene_detect(im_cap)
            pass
    
    # Obscene detection function
    # Blood detection function
    # Movement detecion function

def main():
    path = "./video/"
    filename = "test_video.mp4"

    # Scene detection function
    # shots = scene.detection(path, filename)
    
    shots = [84, 140, 288, 318, 342, 367, 390, 417, 443, 659, 724, 847, 881, 929, 988, 1085, 1129, 1170, 1363, 1409, 1455, 1504, 1577, 1615, 1664, 1687, 1713, 1751, 1962]

    controls(path, filename, shots)

if __name__ == '__main__':
    main()