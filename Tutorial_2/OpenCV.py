import cv2 
#Question 1
image = cv2.imread('Cat.jpg') 
cv2.imshow('Original', image) 
cv2.waitKey(0) 
  
# Use the cvtColor() function to grayscale the image 
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
  
cv2.imshow('Grayscale', gray_image) 
cv2.waitKey(0)   
  
# Window shown waits for any key pressing event 
cv2.destroyAllWindows()

#Question 2
cv2.imshow('Original', image) 
cv2.waitKey(0)
img_blur = cv2.GaussianBlur(gray_image, (3,3), 0) 
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
# Display Canny Edge Detection Image
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
 
cv2.destroyAllWindows()

#Question 3
image2 = cv2.imread('People.jpg') 
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY) 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


# Perform face detection
faces = face_cascade.detectMultiScale(gray_image2, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image2, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the image with detected faces
cv2.imshow('Detected Faces', image2)
cv2.waitKey(0)
cv2.destroyAllWindows()