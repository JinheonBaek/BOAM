import cv2
import cognitive.vision

def detection(isRaw = False, url = None, img = None):
    if isRaw == True:
        r, buf = cv2.imencode('.jpg', img)
        data = bytearray(buf)
        return cognitive.vision.processRequest(data = data, json = None)
    else:
        json = { 'url' : url }
        return cognitive.vision.processRequest(data = None, json = json)


