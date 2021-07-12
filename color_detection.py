import pandas as pd
import cv2

# opencv stores in BGR format and not RGB format

img_path = '2.jpg'
# img_path = '3.jpg'
csv_path = 'colors.csv'

index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
dataframe = pd.read_csv(csv_path, names=index, header=None)

img = cv2.imread(img_path)
img = cv2.resize(img, (800,600))

clicked = False
r = g = b = xposition = yposition = 0

def get_color_name(R,G,B):
    min = 1000
    for i in range(len(dataframe)):
        d = abs(R - int(dataframe.loc[i,'R'])) + abs(G - int(dataframe.loc[i,'G'])) + abs(B - int(dataframe.loc[i,'B']))
        if d<= min:
            min=d
            colorname = dataframe.loc[i,'color_name']

    return colorname


def draw_function(event, x, y, flags, parameters):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global clicked, r, g, b, xposition, yposition 
        clicked = True
        xposition= x
        yposition = y
        b, g, r =img[y, x]
        b = int(b)
        g = int(g)
        r= int(r)

cv2.namedWindow('COLOR DETECTOR')
cv2.setMouseCallback('COLOR DETECTOR', draw_function)

# print(clicked, r, g, b, xposition, yposition)

while True:
    cv2.imshow('COLOR DETECTOR', img)
    if clicked :
        cv2.rectangle(img, (20,20), (600,60), (b,g,r), -1)
        text = get_color_name(r,g,b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        cv2.putText(img,text, (50,50), 2, 0.8, (0,0,0), 2, cv2.LINE_AA)
        if r + g + b >=600:
            cv2.putText(img,text, (50,50), 2, 0.8, (255,255,255), 2, cv2.LINE_AA)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break


cv2.destroyAllWindows()