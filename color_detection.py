import pandas as pd
import cv2

# opencv stores in BGR format and not RGB format

img_path = 'pic.jpg'
csv_path = 'colors.csv'

index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
dataframe = pd.read_csv(csv_path, names=index, header=None)

img = cv2.imread(img_path)
img = cv2.resize(img, (800,600))

clicked = False
r = g = b = xposition = yposition = 0

def draw_function(event, x, y, flags, parameters):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x,y)
        b, g, r =img[y, x]
        print(b,g,r)



cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()