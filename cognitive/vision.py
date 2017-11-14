import os
import sys
import time
import requests
import cv2

# Config
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import config

# Variables
_url = "https://westus.api.cognitive.microsoft.com/vision/v1.0/analyze"
_key = config.getCogkey()
_maxNumRetries = 3

_headers = dict()
_headers['Content-Type'] = 'application/octet-stream'
_headers['Ocp-Apim-Subscription-Key'] = _key

_params = { 'visualFeatures' : 'Adult' }

def processRequest( json, data ):
    """
    Parameters:
    json: Used when processing images from its URL.
    data: Used when processing image read from disk.
    headres: Used to pass the key information and the data type request
    """
    
    retries = 1
    result = None

    while True:
        response = requests.request( 'POST', _url, params = _params, data = data, json = json, headers = _headers )

        if response.status_code == 200 or response.status_code == 201:
            result = response.json()

        else:
            print(retries, _maxNumRetries)
            print( "Error code: %d" % (response.status_code) )
            print( "Error Message: %s" % (response.json()))

            if retries < _maxNumRetries:
                time.sleep(3)
                retries += 1
                continue
        
        break

    return result