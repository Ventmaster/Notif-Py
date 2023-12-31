# IMPORTING DEPENDENCIES
from tkinter import * 
from tkinter import messagebox
import plyer
# import PIL
from PIL import Image
from PIL import ImageTk
import time

#TKinter
tk = Tk()
tk.title("Notification")
tk.geometry("500x300")
image = Image.open('notification-icon.png')
tkimage = ImageTk.PhotoImage(image)

def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time1.get()

    if get_title == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert", "All fields are required!")
    else:
        int_time = int(float(get_time))
        min_to_sec = int_time * 60
        messagebox.showinfo("notifier set", "set notification ?")
        tk.destroy()
        time.sleep(min_to_sec)

        plyer.notification.notify(title=get_title,
                            message=get_msg,
                            app_name="Notifier",
                            app_icon="ico.ico",
                            toast=True,
                            timeout=10)

img_label = Label(tk, image=tkimage).grid()
# img_label = Label(tk).grid()

# Label - Title
t_label = Label(tk, text="Title to Notify",font=("poppins", 10))
t_label.place(x=12, y=70)

# ENTRY - Title
title = Entry(tk, width="25",font=("poppins", 13))
title.place(x=123, y=70)

# Label - Message
m_label = Label(tk, text="Display Message", font=("poppins", 10))
m_label.place(x=12, y=120)

# ENTRY - Message
msg = Entry(tk, width="40", font=("poppins", 13))
msg.place(x=123,height=30, y=120)

# Label - Time
time_label = Label(tk, text="Set Time", font=("poppins", 10))
time_label.place(x=12, y=175)

# ENTRY - Time
time1 = Entry(tk, width="5", font=("poppins", 13))
time1.place(x=123, y=175)

# Label - min
time_min_label = Label(tk, text="min", font=("poppins", 10))
time_min_label.place(x=175, y=180)

# Button
but = Button(tk, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
             relief="raised",
             command=get_details)
but.place(x=170, y=230)

tk.resizable(0,0)
tk.mainloop()