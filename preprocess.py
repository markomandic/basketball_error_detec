import numpy as np
import cv2
import os

size = {1:[225,475, 610,690],
        2:[225,475, 600,680],
        3:[200,450, 590,670],
        4:[200,450, 610,690],
        5:[205,455, 615,695],
        6:[245,495, 635,715],
        7:[215,465, 580,660],
        8:[205,455, 610,690],
        9:[205,455, 605,685],
        10:[220,470, 600,680],
        11:[205,455, 615,695],
        12:[215,465, 615,695],
        13:[230,480, 640,720],
        14:[215,465, 630,710],
        15:[215,465, 615,695],
        16:[215,465, 615,695]}
        

def get_data():
    data = np.empty((150, 60, 250, 80, 1), np.dtype('uint8'))
    labels = np.asarray([int(shot.rstrip()) for shot in open("labels.txt", "r").readlines()])

    for i in range(1,151):
            coords = size[int(i/10) + 1]
            cap = cv2.VideoCapture('/Users/marko/Desktop/basketball/videos/'+ str(i) +'.mp4')
            vid = []
            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret:
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    gray = gray[coords[0]:coords[1], coords[2]:coords[3]]
                    vid.append(gray)
                    #cv2.imshow('frame',gray)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break   
            cap.release()
            #cv2.destroyAllWindows()
            data[i-1] = np.expand_dims(np.asarray(vid), axis=3)[-60:]
    return data, labels