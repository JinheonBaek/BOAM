import os
import cv2
import scene
import obscene
import blooddetect.detector

def blood_detect(blood_detector = None, img = None):
    result = blood_detector.process(img)
    print("[BloodDetect] blood result:", result)

def obscene_detect(img = None):
    result = obscene.detection(isRaw = True, url = None, img = img)
    print("[ObsceneDetect] obscene result:", result)
    
def controls(path, filename, shots = None):
    jump = {'obscene' : 15, 'blood' : 10}
    
    cap = cv2.VideoCapture()
    cap.open(path + filename)

    blood_detector = blooddetect.detector.BloodColorDetector()

    for i in range(shots[-1] + 1):
        (ret_val, im_cap) = cap.read()
        
        # Obscene detection function
        if i % jump['obscene'] == 0:
            print("[ObsceneDetect] Obscene detection: {} frame".format(i))
            #obscene_detect(im_cap)
        
        # Blood detection function
        if i % jump['blood'] == 0:
            print("[BloodDetect] Blood detection: {} frame".format(i))
            #blood_detect(blood_detector, im_cap)
        
        # Movement detecion function
        if i in shots:
            pass

def main():
    path = "./video/"
    filename = "test_video.mp4"

    # Scene detection function
    shots = scene.detection(path, filename)
    
    # test video shots setting for enhance speed
    # shots = [84, 140, 288, 318, 342, 367, 390, 417, 443, 659, 724, 847, 881, 929, 988, 1085, 1129, 1170, 1363, 1409, 1455, 1504, 1577, 1615, 1664, 1687, 1713, 1751, 1962]

    controls(path, filename, shots)

if __name__ == '__main__':
    main()