from cryptography.fernet import Fernet


class PasswordManager:
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):
        """Create and save a new encryption key."""
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)
        print("Key created.")

    def load_key(self, path):
        """Load an existing encryption key from file."""
        try:
            with open(path, 'rb') as f:
                self.key = f.read()
            print("Key loaded.")
        except FileNotFoundError:
            print("Key file not found.")

    def create_password_file(self, path, initial_values=None):
        """Create a new password file."""
        self.password_file = path
        open(self.password_file, 'a').close()
        if initial_values:
            for key, value in initial_values.items():
                self.add_password(key, value)
        print("Password file created.")

    def load_password_file(self, path):
        self.password_file = path
        try:
            with open(path, 'r') as f:
                for line in f:
                    site, encrypted = line.split(":")
                    self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()
            print("passwords file loaded")
        except:
            print("password file not found")

    def add_password(self, site, password):
        self.password_dict[site] = password
        if self.password_file is not None:
            with open(self.password_file, 'a') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")
        print("password added")

    def get_password(self, site):
        try:
            print("password getted" + self.password_dict[site])
            return self.password_dict[site]

        except:
            print(site + " is not an existing password")


def main():
    pm = PasswordManager()
    print(""" What do you want to do?
          (1) Create a new key
          (2) Load an existing key 
          (3) Create new password file
          (4) Load existing password file
          (5) Add a new password
          (6) Get a password
          (q) Quit
          """)
    done = False

    while not done:

        choice = input("Enter your choice: ")
        if choice == "1":  # create a new key (the key to decipher the passwords)
            path = input("Enter path: ")
            pm.create_key(path)

        elif choice == "2":  # load a new key (the key to decipher the passwords)
            path = input("Enter path: ")
            pm.load_key(path)

        elif choice == "3":  # Create new password file
            path = input("Enter path: ")
            pm.create_password_file(path)

        elif choice == "4":  # load existing password file
            path = input("Enter path: ")
            pm.load_password_file(path)

        elif choice == "5":  # add a new password into the password file
            site = input("Enter the site: ")
            password = input("Enter the password: ")
            pm.add_password(site, password)

        elif choice == "6":  # get a password into the password file
            site = input("Enter the site: ")
            print(f"Password for {site} is {pm.get_password(site)}")

        elif choice == "q":
            done = True
            print("see you puta")

        else:
            print("Invalid choice!!!!")


if __name__ == "__main__":
    main()

