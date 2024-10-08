from tkinter import *
import os


def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /r /t 1")



st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
#st.config(bg='Blue')

#Restart Button
rs_button = Button(st,text="Restart", font=("Time New Roman",20,"bold"),
                    relief=RAISED,cursor="plus", command=restart)
rs_button.place(x=150,y=60,height=50,width=200)

#Restart Time
rt_button = Button(st,text="Restart Time", font=("Time New Roman",20,"bold"),
                  relief=RAISED,cursor="plus", command=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)

#Log-out
lg_button = Button(st,text="Log-out", font=("Time New Roman",20,"bold"),
                               relief=RAISED,cursor="plus", command=logout)
lg_button.place(x=150,y=270,height=50,width=200)

#Shut Down
sh_button = Button(st,text="Shut down", font=("Time New Roman",20,"bold"),
                  relief=RAISED,cursor="plus", command=shutdown)
sh_button.place(x=150,y=370,height=50,width=200)

print("Hi")

st.mainloop()