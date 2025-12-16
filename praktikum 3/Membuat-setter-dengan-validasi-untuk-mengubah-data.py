class User:
    def __init__(self, username, level):
        # Validasi awal bisa juga ditaruh di __init__ dengan memanggil setter
        self.__username = ""
        self.__level = ""
        self.set_username(username)
        self.set_level(level)

    def info(self):
        print(f"Username: {self.__username}, Level: {self.__level}")

    # --- Getter Methods ---
    def get_username(self):
        return self.__username

    def get_level(self):
        return self.__level

    # --- Setter Methods dengan Validasi ---
    def set_username(self, username_baru):
        if len(username_baru) >= 6:
            # Validasi: username minimal 6 karakter
            self.__username = username_baru
            print("Username berhasil diubah.")
        else:
            print("Error: Username terlalu pendek! Minimal 6 karakter.")

    def set_level(self, level_baru):
        allowed_levels = ["User", "Admin", "Super Admin"]
        if level_baru in allowed_levels:
            # Validasi: level harus ada di daftar
            self.__level = level_baru
            print("Level berhasil diubah.")
        else:
            print(f"Error: Level '{level_baru}' tidak valid!")

# --- Bagian Utama Program ---
user_1 = User("pengguna_baru", "User")
user_1.info()

print("\n--- Mencoba mengubah data via Setter ---")
user_1.set_username("admin") # Ini akan gagal
user_1.set_level("Moderator") # Ini akan gagal
user_1.info() # Data tidak berubah

print("\n--- Mencoba lagi dengan data yang valid ---")
user_1.set_username("administrator_sistem") # Ini akan berhasil
user_1.set_level("Admin") # Ini akan berhasil
user_1.info() # Data berhasil diubah dengan aman