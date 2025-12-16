class user :
    def __init__(self, username, level):
        self.__username = username
        self.__level = level # level biasa diisi apa saja
        
    def info(self):
        print(f"username: {self.__username}, level {self.__level}")

# --- bagian utama progra ---
user_1 = user("admin_ganteng", "super_admin")
user_1.info()

# coba akses langsung atribut private dari luar
try:
    print(user_1.__username)
except AttributeError as e:
    print(f"\nerror {e}")
    print("atribut __username tidak bisa di akses langsung")
    