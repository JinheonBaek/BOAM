import os
import scene

def controls(shots = None):
    pass
    # Obscene detection function
    # Blood detection function
    # Movement detecion function

def main():
    path = "./video/"
    filename = "test_video.mp4"

    # Scene detection function
    shots = scene.detection(path, filename)
    
    controls(shots)

if __name__ == '__main__':
    main()