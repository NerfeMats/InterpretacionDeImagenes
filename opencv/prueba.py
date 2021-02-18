import cv2 as cv
img = cv.imread('imagenes/braile.jpg')
cv.imshow('Braile', img)
print(cv.waitKey(20))  

def changeRes(width, height):
    # vide en vivo
    capture.set(3,width)
    capture.set(4,height)

def rescaleframe(frame, scale=0.20):
    # images , videos y videos en vivo 
    width = int(frame.shape[1]*scale)   #shape regreso el numero de filas, columnas y canales.
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture('video/Video.mp4')
while True:
    isTrue, frame = capture.read()
    
    frame_resized =rescaleframe(frame)
    
    cv.imshow('Video', frame)
    cv.imshow('Video resized', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture1 = cv.VideoCapture(0)
capture.release()
cv.destroyAllWindows()
print("hola mundo")