
import cv2
import os
import numpy as np
import streamlit as st
from PIL import Image

#------------------------------load_image---------------------
@st.cache
def load_image(img):
    imge=Image.open(img)
    return imge
#----------------detection classifiers-------------------------

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyeCascade=cv2.CascadeClassifier("haarcascade_eye.xml")
smileCascade=cv2.CascadeClassifier("haarcascade_smile.xml")
#-------------------------------------------------
#detetion functions 
#-------------------------------------------------
#eyes
def detect_eyes(my_image):
    new_img=np.array(my_image.convert('RGB'))
    img=cv2.cvtColor(new_img,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    eyes = eyeCascade.detectMultiScale( gray,1.3,4)
   
# draw a rectangle #
    for (ex, ey, ew, eh) in eyes:
     cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    return img 

#@@@@@@@@@@@
#simle
def detect_smiles(my_image):
    new_img=np.array(my_image.convert('RGB'))
    img=cv2.cvtColor(new_img,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    smiles = smileCascade.detectMultiScale( gray,1.8,25)
   
# draw a rectangle #
    for (sx, sy, sw, sh) in smiles:
     cv2.rectangle(img, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)
    return img 


#@@@@@@@@@
#face
def detect_faces(my_image):
    new_img=np.array(my_image.convert('RGB'))
    img=cv2.cvtColor(new_img,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale( gray,1.1,4)
   

# draw a rectangle around the faces#
    for (x, y, w, h) in faces:
     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return img ,faces


#-----------------face detection app-----------


def main ():
    
    st.title("Face detection application :)")
    
    
    activities = ["Detection"]
    choice = st.sidebar.selectbox("Select activity",activities)
    
    if choice == 'Detection' :
     st.subheader("Face detection")
     
     
     image_file=st.file_uploader("Upload image",type=(['jpg','png','jpeg']))
     
     
     if image_file is not None :   
         my_image = Image.open(image_file)
         st.text("Original image")
         st.image(my_image)
         
    #face detection
     task=["faces","smiles","eyes"]
     feature_choice=st.sidebar.selectbox("find features",task)
     st.sidebar.markdown( "Developed by : Mohammad Badawy" )   
           
     
     if st.button ("process"):
          if feature_choice =="faces":
              result_img,result_faces=detect_faces(my_image)
              st.image(result_img)
              st.success(f"Found {len(result_faces)} faces")
              
              
          elif feature_choice=="smiles":
             result_img=detect_smiles(my_image)
             st.image(result_img)
              
          elif feature_choice=="eyes":
              result_img=detect_eyes(my_image)
              st.image(result_img)
              
            
     
   
        
    
main()