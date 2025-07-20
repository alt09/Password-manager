import customtkinter as ctk
from passwordManager import *
""" What do you want to do?
          (1) Create a new key
          (2) Load an existing key 
          (3) Create new password file
          (4) Load an existing password file
          (5) Add a new password
          (6) Get a password
          (q) Quit
          """
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Password manager")
root.geometry("750x500")

def switch_option(switch_to):
    if switch_to == 'CNK':
        for widgets in page_frame.winfo_children():
            widgets.destroy()
        CNK()
    elif switch_to == 'LEK':
        for widgets in page_frame.winfo_children():
            widgets.destroy()
        LEK()
    elif switch_to == 'CNPF':
        for widgets in page_frame.winfo_children():
            widgets.destroy()
        CNPF()
    elif switch_to == 'LEPF':
        for widgets in page_frame.winfo_children():
            widgets.destroy()
        LEPF()
    elif switch_to == 'ANP':
        for widgets in page_frame.winfo_children():
            widgets.destroy()
        ANP()
    elif switch_to == 'GP':
        for widgets in page_frame.winfo_children():
            widgets.destroy()
        GP()
    else:
        print('error')

page_frame = ctk.CTkFrame(master=root,width=500,height=550, corner_radius=100)
page_frame.place(relx=0.5,rely=0.5,anchor="center")

def menu():
    heading_lb =  ctk.CTkLabel(master=page_frame,text="What do you want to do")
    heading_lb.place(relx=0.5,rely=.2,  anchor= "center")

    option1 = ctk.CTkButton(master=page_frame, text='Create a new key', command=lambda:switch_option(switch_to='CNK'))
    option1.place(relx=0.25,rely=0.4,anchor="center")

    option2 = ctk.CTkButton( master=page_frame, text='Load an existing key', command=lambda:switch_option(switch_to='LEK'))
    option2.place(relx=0.75,rely=0.4,anchor="center")

    option3 = ctk.CTkButton( master=page_frame, text='Create new password file', command=lambda:switch_option(switch_to='CNPF'))
    option3.place(relx=0.25,rely=0.6,anchor="center")

    option4 = ctk.CTkButton( master=page_frame, text='Load an existing password file', command=lambda:switch_option(switch_to='LEPF'))
    option4.place(relx=0.75,rely=0.6,anchor="center")
    
    option5 = ctk.CTkButton( master=page_frame, text='Add a new password', command=lambda:switch_option(switch_to='ANP'))
    option5.place(relx=0.25,rely=0.8,anchor="center")

    option6 = ctk.CTkButton( master=page_frame, text='Get a password', command=lambda:switch_option(switch_to='GP'))
    option6.place(relx=0.75,rely=0.8,anchor="center")


def CNK(): #CNK = create new key
    heading_lb = ctk.CTkLabel(master=page_frame,text='Create new key')
    heading_lb.place(relx=0.5,rely=0.2,anchor="center")

    entry_key_path = ctk.CTkEntry(master=page_frame,placeholder_text="path")
    entry_key_path.place(relx=0.5,rely=0.4,anchor="center")

    button_CNK = ctk.CTkButton(master=page_frame,text='Create',command=lambda:PasswordManager.create_key(PasswordManager,entry_key_path.get()))
    button_CNK.place(relx=0.5, rely=0.6, anchor="center")
def LEK():#  LEK = load an existing key
    heading_lb = ctk.CTkLabel(master=page_frame,text='Load an existing key')
    heading_lb.place(relx=0.5,rely=0.2,anchor="center")

    entry_key = ctk.CTkEntry(master=page_frame,placeholder_text="key")
    entry_key.place(relx=0.5,rely=0.4,anchor="center")

    button_LEK  = ctk.CTkButton(master=page_frame,text="Load key",command=lambda:PasswordManager.load_key(PasswordManager,entry_key.get()))
    button_LEK.place(relx=0.5,rely=0.6,anchor="center")
def CNPF(): #CNPF = create new password file
    heading_lb = ctk.CTkLabel(master=page_frame,text='Create new password file')
    heading_lb.place(relx=0.5,rely=0.2,anchor="center")

    entry_passwords_path = ctk.CTkEntry(master=page_frame,placeholder_text="Path")
    entry_passwords_path.place(relx=0.5,rely=0.4, anchor="center")

    button_CNPF = ctk.CTkButton(master=page_frame,text="Create", command=lambda:PasswordManager.create_password_file(PasswordManager,entry_passwords_path.get()))
    button_CNPF.place(relx=0.5, rely=0.6,anchor="center")

def LEPF(): #LEPF = load an existing passwored file 
    heading_lb = ctk.CTkLabel(master=page_frame,text='Load an existing passwored file')
    heading_lb.place(relx=0.5,rely=0.2,anchor="center")

    entry_passwords_file = ctk.CTkEntry(master=page_frame,placeholder_text="Password file")
    entry_passwords_file.place(relx=0.5,rely=0.4, anchor="center")

    button_LEPF = ctk.CTkButton(master=page_frame,text="Load password file", command=lambda:PasswordManager.load_password_file(PasswordManager,entry_passwords_file.get()))
    button_LEPF.place(relx=0.5, rely=0.6,anchor="center")

def ANP(): #ANP = Add a new password
    heading_lb = ctk.CTkLabel(master=page_frame,text='Add a new password')
    heading_lb.place(relx=0.5,rely=0.2,anchor="center")
    
    entry_password_to_add = ctk.CTkEntry(master=page_frame,placeholder_text="Password to add")
    entry_password_to_add.place(relx=0.5,rely=0.4, anchor="center")

    button_ANP = ctk.CTkButton(master=page_frame,text="Add password", command=lambda:PasswordManager.add_password(PasswordManager,entry_password_to_add.get()))
    button_ANP.place(relx=0.5, rely=0.6,anchor="center")

def GP(): #GP = get a password
    heading_lb = ctk.CTkLabel(master=page_frame,text='Get a password')
    heading_lb.place(relx=0.5,rely=0.2,anchor="center")

    entry_password_to_get = ctk.CTkEntry(master=page_frame,placeholder_text="Password to getr")
    entry_password_to_get.place(relx=0.5,rely=0.4, anchor="center")

    button_GP = ctk.CTkButton(master=page_frame,text="Get password", command=lambda:PasswordManager.get_password(PasswordManager,entry_password_to_get.get()))
    button_GP.place(relx=0.5, rely=0.6,anchor="center")

menu()

root.mainloop()
