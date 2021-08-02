import numpy as np
import cv2

img = np.zeros((256,256))
cv2.imshow("Img",img)

cv2.waitKey()
cv2.destroyAllWindows()
