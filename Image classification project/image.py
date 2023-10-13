import tkinter as tk
from tkinter import Toplevel
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import tensorflow as tf
import numpy as np
from keras.models import load_model

model = tf.keras.models.load_model("model2.h5")

def load_image():
    file_path = tk.filedialog.askopenfilename()
    if file_path:
        img2 = Image.open(file_path)
        img2 = img.resize((100, 100))  # Resize the image to match model input size
        img2 = np.array(img)
        img2 = img / 255.0  # Normalize pixel values (if needed)
        img2 = img.reshape(1, 100, 100, 3)  # Reshape to match model input shape
        prediction = model.predict(img2)
        pred_label = "cat" if prediction > 0.5 else "dog"
        




frame=tk.Tk()
frame.title("welcome to Image Classification")
frame.geometry("1000x1000")
img=Image.open("background.jpg")
img=ImageTk.PhotoImage(img)
img_label=tk.Label(image=img)
img_label.image=img
img_label.grid(column=1,row=0)



logo_image = tk.PhotoImage(file='logo.png')
logo_label = tk.Label(frame, image=logo_image)
logo_label.place(x=450, y=250)

title=tk.Label(frame,text="Image Classification",font=("Helvetica",30))
title.place(x=600,y=200)

b1=tk.Button(frame,text="Upload file",command=lambda:upload_file())
b1.place(x=750,y=650)

def upload_file():
    frame2=Toplevel()
    frame2.geometry("200x200")
    frame2.title("Upload")
    f_types=[('Jpg files','*.jpg'),('PNG files','*.png files'),('JPEG files','*jpeg files')]
    filename=tk.filedialog.askopenfilename(filetypes=f_types)
    img2=ImageTk.PhotoImage(file=filename)
    
    e1=tk.Label(frame2)
    """e1.grid(row=0,column=1)
    e1.image=img2
    e1['image']=img2"""
    
    

    label = tk.Label(frame2, image=img2)
    label.pack(fill="both", expand=True)
    
    
    def load_image():
    
    
        img2 = Image.open(img2)
        img2 = img.resize((100, 100))  # Resize the image to match model input size
        img2 = np.array(img)
        img2 = img / 255.0  # Normalize pixel values (if needed)
        img2 = img.reshape(1, 100, 100, 3)  # Reshape to match model input shape
        prediction = model.predict(img2)
        pred_label = "cat" if prediction > 0.5 else "dog"
        messagebox.showinfo("Message",pred_label)
    
    b2=tk.Button(frame2,text="Click for prediction",font=("Helvetica",10),command=lambda:load_image())
    b2.place(x=750,y=650)
    messagebox.showinfo("Message",pred_label)
    frame2.mainloop()
    


    

frame.attributes('-fullscreen', True)
frame.mainloop()