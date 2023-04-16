import random
import smtplib
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.withdraw()

otp = ''.join([str(random.randint(0, 9)) for i in range(6)])

sender_email = "nayakramulu50@gmail.com"
receiver_email = input("Enter your email: ")
password = input("Enter your email password: ")

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email, password)
msg = "Hello, Your OTP is " + str(otp)
server.sendmail(sender_email, receiver_email, msg)
server.quit()

user_input_otp = input("Enter the OTP received: ")

if user_input_otp == otp:
    messagebox.showinfo("OTP verification successful!","OTP verification successful!,\U0001F60A,\U0001F60A,\U0001F60A,\U0001F60A")
else:
    messagebox.showinfo("OTP verification failed!","OTP verification failed!,\U0001F622,\U0001F622,\U0001F622,\U0001F622")
    

root.mainloop()




