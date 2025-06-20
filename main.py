import cv2
import numpy as np

# reading and resizing the image
img = cv2.imread("test1.jpg")
img = cv2.resize(img,(400,400))

# converting the image to grayscale and then to binary
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# Finding Contours
contours, hierarchy = cv2.findContours(binary, mode=cv2.RETR_TREE,method=cv2.CHAIN_APPROX_SIMPLE) 


image_copy=img.copy()
image_copy= cv2.drawContours(image_copy,contours,-1,(0,255,0),thickness=3,lineType=cv2.LINE_AA)

mark=0
j=0
# storing the contours center in xcoord(for X-axis) and ycoord(for Y-axis)
xcoord=[0,0,0,0]
ycoord=[0,0,0,0]

# Finding contour center
for c in contours:

    M = cv2.moments(c)

    cx=int(M["m10"]/M["m00"]) if M["m00"] !=0 else 0 
    cy=int(M["m01"]/M["m00"]) if M["m00"] !=0 else 0
    
    if mark==0:
        xcoord[j]=cx
        ycoord[j]=cy
        j=j+1
        mark=1
    elif mark==1:
        xcoord[j]=cx
        ycoord[j]=cy
        j=j+1
        mark=2
    elif mark==2:
        xcoord[j]=cx
        ycoord[j]=cy
        j=j+1
        mark=3
    elif mark==3:
        xcoord[j]=cx
        ycoord[j]=cy
        j=j+1
        mark=4
    
    # circling the center
    cv2.circle(image_copy,(cx,cy),5,(0,255,0),-1)


# converting the original image into hsv so that we can distinguish the color using the following color range
new_image=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# HSV color range for Blue
lower_blue = np.array([39,158, 0])
upper_blue = np.array([136,255,255])
# HSV color range for Red
lower_red = np.array([0,100,100])
upper_red = np.array([15,255,255])

# function for checking blue color is present or not on (c,d) coordinates using the above color ranges
def check_blue(c,d):
    value=tuple(new_image[c][d])

    if all(lower<=i<=upper for i,lower,upper in zip(value,lower_blue,upper_blue)):
          return True

# function for checking red color is present or not on (c,d) coordinates using the above color ranges
def check_red(c,d):
    value=tuple(new_image[c][d])

    if all(lower<=i<=upper for i,lower,upper in zip(value,lower_red,upper_red)):
          return True


# new arrays to store sorted coordinates
newxcoord=[0,0,0,0]
newycoord=[0,0,0,0]

#arranging  X-coordinate in accending order
i=0
for s in range(400):
    for l in range(4):
        if xcoord[l]==s:
            newxcoord[i]=s
            i=i+1

z=0
for s in range(4):
    for l in range(4):
        if newxcoord[s]==xcoord[l] and z<4:
            f=xcoord.index(newxcoord[s])
            newycoord[z]=ycoord[f]
            xcoord[l]=0
            z=z+1

# In contour's center calculation we also get our main image box's center along with the ball center since the box has size of 400X400 so its senter is at (199,199) which we get every time but if any of the ball has center at this point the it will create problem but when this happen
# we get two (199,199) so we will make one (199,199) -> (0,0) hence only one (199,199) remains and in other cases it will become (0,0) every time ,to do this following for loop is created
for g in range(4):
    if newxcoord[g]==199 and newycoord[g]==199:
        newxcoord[g]=0
        newycoord[g]=0
        break

# Now the final newxcoord and newycoord have circle's center with(0,0)

# printing our colored ball using chec_blue and check_red function 
for t in range(4):
    if newxcoord[t]!=0 and newycoord[t]!=0:
        if check_red(newycoord[t],newxcoord[t])==True:
            print("Red")
        elif check_blue(newycoord[t],newxcoord[t])==True:
            print("Blue")


cv2.imshow('contour',image_copy)
cv2.waitKey(0)
cv2.destroyAllWindows


