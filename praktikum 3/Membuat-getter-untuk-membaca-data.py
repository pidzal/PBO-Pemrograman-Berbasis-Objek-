class User:
    def __init__(self, username, level):
        self.__username = username
        self.__level = level

    def info(self):
        print(f"Username: {self.__username}, Level: {self.__level}")

    # Getter untuk username
    def get_username(self):
        return self.__username

    # Getter untuk level
    def get_level(self):
        return self.__level


# --- Bagian Utama Program ---
user_1 = User("admin_ganteng", "Super Admin")

# Menggunakan getter untuk membaca data secara aman
print("\n--- Mengakses data via Getter ---")
nama_user = user_1.get_username()
level_user = user_1.get_level()
print(f"Username dari getter: {nama_user}")
print(f"Level dari getter: {level_user}")
