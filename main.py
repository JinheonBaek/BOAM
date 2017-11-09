import os
import cv2
import scene
import obscene

def obscene_detect():
    img = cv2.imread('./cognitive/test.jpg')
    result = obscene.detection(isRaw = True, url = None, img = img)
    
def controls(shots = None):
    pass
    # Obscene detection function
    # Blood detection function
    # Movement detecion function

def main():
    path = "./video/"
    filename = "test_video.mp4"

    obscene_detect()

    # Scene detection function
    shots = scene.detection(path, filename)
    
    controls(shots)

if __name__ == '__main__':
    main()