#pip install Pillow

import tkinter as tk
from PIL import Image, ImageTk

emotions = {
    "netr": ("netr.png.png", ),
    "cry": ("cry.png.png", ),
    "happy": ("happy.png.png", )
}


root = tk.Tk()
root.title("AI A")
root.geometry("500x700")
root.resizable(False, False)

avatar_label = tk.Label(root)
avatar_label.pack(pady=20)

def update_avatar(emotion):
    img_path, bg_color = emotions.get(emotion, emotions["netr"])
    avatar_label.configure(bg=bg_color)
    try:
        img = Image.open(img_path)
        img = Image.resize((400,400), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
        avatar_label.configure(image=img)
        avatar_label.image = img
    except Exception as e:
        print(e)
        
        
update_avatar("happy")
root.mainloop()