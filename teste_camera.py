import cv2
import matplotlib.pyplot as plt

video = cv2.VideoCapture()
ip = 'http://200.238.238.123:8080/video'
video.open(ip)

while True:
    cv2.waitKey(1000)
    check, frame = video.read()

    # Conversão RGB para Grayscale
    R = frame[:,:,0]  # matriz correspondente à componente RED
    G = frame[:,:,1]  # matriz correspondente à componente GREEN
    B = frame[:,:,2]  # matriz correspondente à componente BLUE

    gray = 0.299 * R + 0.587 * G + 0.114 * B

    cv2.imshow('Video', gray)
    cv2.waitKey(1000)
