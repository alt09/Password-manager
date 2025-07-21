import customtkinter as ctk
from passwordManager import PasswordManager

pm = PasswordManager()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Password Manager")
root.geometry("750x500")


def switch_option(switch_to):
    """Switches the visible page in the UI."""
    for widget in page_frame.winfo_children():
        widget.destroy()
    if switch_to == 'cnk':
        create_new_key_page()
    elif switch_to == 'lek':
        load_existing_key_page()
    elif switch_to == 'cnpf':
        create_new_password_file_page()
    elif switch_to == 'lepf':
        load_existing_password_file_page()
    elif switch_to == 'anp':
        add_new_password_page()
    elif switch_to == 'gp':
        get_password_page()
    elif switch_to == "menu":
        menu()
    else:
        print('Error: page not found')


page_frame = ctk.CTkFrame(
    master=root, width=500, height=550, corner_radius=100
)
page_frame.place(relx=0.5, rely=0.5, anchor="center")


def menu():
    """Displays the main menu."""
    heading_label = ctk.CTkLabel(
        master=page_frame, text="What do you want to do"
    )
    heading_label.place(relx=0.5, rely=0.2, anchor="center")

    option1 = ctk.CTkButton(
        master=page_frame,
        text='Create a new key',
        command=lambda: switch_option('cnk')
    )
    option1.place(relx=0.25, rely=0.4, anchor="center")

    option2 = ctk.CTkButton(
        master=page_frame,
        text='Load an existing key',
        command=lambda: switch_option('lek')
    )
    option2.place(relx=0.75, rely=0.4, anchor="center")

    option3 = ctk.CTkButton(
        master=page_frame,
        text='Create new password file',
        command=lambda: switch_option('cnpf')
    )
    option3.place(relx=0.25, rely=0.6, anchor="center")

    option4 = ctk.CTkButton(
        master=page_frame,
        text='Load an existing password file',
        command=lambda: switch_option('lepf')
    )
    option4.place(relx=0.75, rely=0.6, anchor="center")

    option5 = ctk.CTkButton(
        master=page_frame,
        text='Add a new password',
        command=lambda: switch_option('anp')
    )
    option5.place(relx=0.25, rely=0.8, anchor="center")

    option6 = ctk.CTkButton(
        master=page_frame,
        text='Get a password',
        command=lambda: switch_option('gp')
    )
    option6.place(relx=0.75, rely=0.8, anchor="center")


def create_new_key_page():
    """Page for creating a new key."""
    heading_label = ctk.CTkLabel(
        master=page_frame, text='Create new key'
    )
    heading_label.place(relx=0.5, rely=0.2, anchor="center")

    entry_key_path = ctk.CTkEntry(
        master=page_frame, placeholder_text="Path"
    )
    entry_key_path.place(relx=0.5, rely=0.4, anchor="center")

    button_create = ctk.CTkButton(
        master=page_frame,
        text='Create',
        command=lambda: pm.create_key(entry_key_path.get())
    )
    button_create.place(relx=0.5, rely=0.6, anchor="center")

    button_menu = ctk.CTkButton(
        master=page_frame,
        text="Menu",
        command=lambda: switch_option("menu")
    )
    button_menu.place(relx=0.5, rely=0.8, anchor="center")


def load_existing_key_page():
    """Page for loading an existing key."""
    heading_label = ctk.CTkLabel(
        master=page_frame, text='Load an existing key'
    )
    heading_label.place(relx=0.5, rely=0.2, anchor="center")

    entry_key = ctk.CTkEntry(
        master=page_frame, placeholder_text="Key"
    )
    entry_key.place(relx=0.5, rely=0.4, anchor="center")

    button_load = ctk.CTkButton(
        master=page_frame,
        text="Load key",
        command=lambda: pm.load_key(entry_key.get())
    )
    button_load.place(relx=0.5, rely=0.6, anchor="center")

    button_menu = ctk.CTkButton(
        master=page_frame,
        text="Menu",
        command=lambda: switch_option("menu")
    )
    button_menu.place(relx=0.5, rely=0.8, anchor="center")


def create_new_password_file_page():
    """Page for creating a new password file."""
    heading_label = ctk.CTkLabel(
        master=page_frame, text='Create new password file'
    )
    heading_label.place(relx=0.5, rely=0.2, anchor="center")

    entry_passwords_path = ctk.CTkEntry(
        master=page_frame, placeholder_text="Path"
    )
    entry_passwords_path.place(relx=0.5, rely=0.4, anchor="center")

    button_create = ctk.CTkButton(
        master=page_frame,
        text="Create",
        command=lambda: pm.create_password_file(entry_passwords_path.get())
    )
    button_create.place(relx=0.5, rely=0.6, anchor="center")

    button_menu = ctk.CTkButton(
        master=page_frame,
        text="Menu",
        command=lambda: switch_option("menu")
    )
    button_menu.place(relx=0.5, rely=0.8, anchor="center")


def load_existing_password_file_page():
    """Page for loading an existing password file."""
    heading_label = ctk.CTkLabel(
        master=page_frame, text='Load an existing password file'
    )
    heading_label.place(relx=0.5, rely=0.2, anchor="center")

    entry_passwords_file = ctk.CTkEntry(
        master=page_frame, placeholder_text="Password file"
    )
    entry_passwords_file.place(relx=0.5, rely=0.4, anchor="center")

    button_load = ctk.CTkButton(
        master=page_frame,
        text="Load password file",
        command=lambda: pm.load_password_file(entry_passwords_file.get())
    )
    button_load.place(relx=0.5, rely=0.6, anchor="center")

    button_menu = ctk.CTkButton(
        master=page_frame,
        text="Menu",
        command=lambda: switch_option("menu")
    )
    button_menu.place(relx=0.5, rely=0.8, anchor="center")


def add_new_password_page():
    """Page for adding a new password."""
    heading_label = ctk.CTkLabel(
        master=page_frame, text='Add a new password'
    )
    heading_label.place(relx=0.5, rely=0.2, anchor="center")

    entry_password_to_add = ctk.CTkEntry(
        master=page_frame, placeholder_text="Password to add"
    )
    entry_password_to_add.place(relx=0.5, rely=0.4, anchor="center")

    entry_site = ctk.CTkEntry(
        master=page_frame, placeholder_text="Website of the password"
    )
    entry_site.place(relx=0.5, rely=0.6, anchor="center")

    button_add = ctk.CTkButton(
        master=page_frame,
        text="Add password",
        command=lambda: pm.add_password(entry_site.get(), entry_password_to_add.get())
    )
    button_add.place(relx=0.5, rely=0.8, anchor="center")

    button_menu = ctk.CTkButton(
        master=page_frame,
        text="Menu",
        command=lambda: switch_option("menu")
    )
    button_menu.place(relx=0.5, rely=0.9, anchor="center")


def get_password_page():
    """Page for getting a password."""
    heading_label = ctk.CTkLabel(
        master=page_frame, text='Get a password'
    )
    heading_label.place(relx=0.5, rely=0.2, anchor="center")

    entry_password_to_get = ctk.CTkEntry(
        master=page_frame, placeholder_text="Site of the password"
    )
    entry_password_to_get.place(relx=0.5, rely=0.4, anchor="center")

    button_get = ctk.CTkButton(
        master=page_frame,
        text="Get password",
        command=lambda: pm.get_password(entry_password_to_get.get())
    )
    button_get.place(relx=0.5, rely=0.6, anchor="center")

    button_menu = ctk.CTkButton(
        master=page_frame,
        text="Menu",
        command=lambda: switch_option("menu")
    )
    button_menu.place(relx=0.5, rely=0.8, anchor="center")


menu()
root.mainloop()
