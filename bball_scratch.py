import numpy as np
import cv2
import os

#data = np.empty((100, 40, 500, 600, 1), np.dtype('uint8'))
j = 0
for i in range(141,151):
        print(i)
        cap = cv2.VideoCapture('/Users/marko/Desktop/basketball/videos/'+ str(i) +'.mp4')
        i = 0
        vid = []
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray = gray[215:465, 615:695]
                vid.append(gray)
                cv2.imshow('frame',gray)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    print(filename)
                    break
            else:
                break
        #np.savez_compressed(filename, np.asarray(vid))    
        cap.release()
        cv2.destroyAllWindows()
        #data[j] = np.expand_dims(np.asarray(vid), axis=3)
        j += 1
#np.savez_compressed(filename, data)