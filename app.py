from tkinter import *
from PIL import Image, ImageTk
import os


def rotate_img():
    global counter
    img_label.config(image=img_array[counter%len(img_array)]) # by using %len(img_aaray) photo will load once again
    counter = counter + 1
    


counter=1
root = Tk()
# for title of the our GUI
root.title("Wallpaper Viewer")

# for set the windows size of the GUI
root.geometry('250x400')

# Now we want to change the background colour of the our GUI windows.
root.configure(background="Black")

# to read the all images which is inside the wallpaper folder.
files = os.listdir("Wallpaper")

img_array = []
for file in files:
    img = Image.open(os.path.join("Wallpaper",file))
    resized_img = img.resize((200,300))
    img_array.append(ImageTk.PhotoImage(resized_img))

# Now for printing the wallpaper we used the label function.
img_label = Label(root, image= img_array[0])
img_label.pack(pady=(15,10))

# Now we set the button for next_click
next_btn = Button(root,text="Next",bg="White",fg="Black",width=25,height=2,command=rotate_img)
next_btn.pack()


# for keeping the window consistancy in the window display.
root.mainloop()