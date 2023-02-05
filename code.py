import cv2
import numpy as np
import os

source="images"


images=[]
for i in os.listdir(source):
    name,ext=os.path.splitext(i)
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        path1=source+"/"+i
        images.append(path1)

totalImg=len(images)

#shape--> height , width , channels 
read=cv2.imread(images[0])

height , width , channels = read.shape
output = cv2.VideoWriter("friends.mp4",cv2.VideoWriter_fourcc(*'mp4v'), 0.8, (width, height) )

for r in range(totalImg-1,0,-1):
    read=cv2.imread(images[r])
    output.write(read)

output.release() 
