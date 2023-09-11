from tkinter import *
from tkinter import ttk
import requests

def data_get():

    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=eaf376bef4a4bcdf65a19f418bf12ee6").json()
# print(data)
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    min_temp_label1.config(text=data["main"]["temp_min"])
    max_temp_label1.config(text=data["main"]["temp_max"])
    p_label1.config(text=data["main"]["pressure"])



win = Tk()  #creating window will call Tk class
win.title("Weather App")   #title of window
win.config(bg = "light blue")   #window background color
win.geometry("700x700")   #window size

name_label = Label(win, text="Weather App",
                   font=("Times New Roman",35, "bold"))

name_label.place(x=25,y=50,height=50, width=450)  #where to place text weather app


city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar",
             "Chhattisgarh","Goa","Gujarat","Haryana",
             "Himachal Pradesh","Jammu and Kashmir","Jharkhand",
             "Karnataka","Kerala","Madhya Pradesh","Maharashtra",
             "Manipur","Meghalaya","Mizoram","Nagaland","Odisha",
             "Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana",
             "Tripura","Uttar Pradesh","Uttarakhand","West Bengal",
             "Andaman and Nicobar Islands","Chandigarh",
             "Dadra and Nagar Haveli","Daman and Diu","Lakshadweep",
             "National Capital Territory of Delhi","Puducherry"]



# creating combo box
com = ttk.Combobox(win, text="Weather App",values=list_name,
                   font=("Times New Roman",20, "bold"), textvariable=city_name)

com.place(x=25,y=120,height=50,width=450)


# creating button



w_label = Label(win, text="Weather Climate",
                   font=("Times New Roman",20))
w_label.place(x=25,y=260,height=50, width=250)
w_label1 = Label(win, text="",
                   font=("Times New Roman",20))
w_label1.place(x=250,y=260,height=50, width=250)


wb_label = Label(win, text="Weather Description",
                   font=("Times New Roman",20))
wb_label.place(x=25,y=330,height=50, width=250)
wb_label1 = Label(win, text="",
                   font=("Times New Roman",20))
wb_label1.place(x=250,y=330,height=50, width=250)


temp_label = Label(win, text="temperature",
                   font=("Times New Roman",20))
temp_label.place(x=25,y=400,height=50, width=250)
temp_label1 = Label(win, text="",
                   font=("Times New Roman",20))
temp_label1.place(x=250,y=400,height=50, width=250)


min_temp_label = Label(win, text="Min Temp",
                   font=("Times New Roman",20))
min_temp_label.place(x=25,y=470,height=50, width=250)
min_temp_label1 = Label(win, text="",
                   font=("Times New Roman",20))
min_temp_label1.place(x=250,y=470,height=50, width=250)


max_temp_label = Label(win, text="Max Temp",
                   font=("Times New Roman",20))
max_temp_label.place(x=25,y=540,height=50, width=250)
max_temp_label1 = Label(win, text="",
                   font=("Times New Roman",20))
max_temp_label1.place(x=250,y=540,height=50, width=250)


p_label = Label(win, text="Pressure",
                   font=("Times New Roman",20))
p_label.place(x=25,y=610,height=50, width=250)
p_label1 = Label(win, text="",
                   font=("Times New Roman",20))
p_label1.place(x=250,y=610,height=50, width=250)



done_button = Button(win, text="Done",
                   font=("Times New Roman",20, "bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)

win.mainloop() #window will continuously run with the help of mainloop function



















