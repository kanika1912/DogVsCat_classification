import tkinter as tk
from tkinter import Toplevel, messagebox
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("model2.h5")

def load_image(file_path):
    if file_path:
        img2 = Image.open(file_path)
        img2 = img2.resize((100, 100))  # Resize the image to match model input size
        img2 = np.array(img2)
        img2 = img2 / 255.0  # Normalize pixel values (if needed)
        img2 = img2.reshape(1, 100, 100, 3)  # Reshape to match model input shape
        prediction = model.predict(img2)
        pred_label = "Model predict this as cat" if prediction > 0.5 else "Model predict this as dog"
        messagebox.showinfo("Message", pred_label)
        

def upload_file():
    frame2 = Toplevel()
    frame2.geometry("800x800")
    frame2.title("Upload")
    
    f_types = [('Jpg files', '*.jpg'), ('PNG files', '*.png'), ('JPEG files', '*.jpeg')]
    filename = askopenfilename(filetypes=f_types)
    
    if filename:
        img2 = Image.open(filename)
        img2 = img2.resize((400, 400))  # Resize the image to fit the window
        img2 = ImageTk.PhotoImage(img2)
        
        label = tk.Label(frame2, image=img2)
        label.pack()
        
        b2 = tk.Button(frame2, text="Click for prediction", font=("Helvetica", 10), command=lambda: load_image(filename))
        b2.pack()
        
    
    frame2.mainloop()

frame = tk.Tk()
frame.title("Welcome to Image Classification")
frame.geometry("1000x1000")

img = Image.open("background.jpg")
img = ImageTk.PhotoImage(img)
img_label = tk.Label(image=img)
img_label.image = img
img_label.grid(column=1, row=0)

logo_image = Image.open('logo.png')
logo_image = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(frame, image=logo_image)
logo_label.place(x=450, y=250)

title = tk.Label(frame, text="Image Classification", font=("Helvetica", 30))
title.place(x=600, y=200)

b1 = tk.Button(frame, text="Upload file", command=upload_file)
b1.place(x=750, y=650)

"""frame.attributes('-fullscreen', True)"""
frame.mainloop()
