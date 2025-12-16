📘 README.md — Analisis Refactoring Sistem Notifikasi
1. Deskripsi Singkat Studi Kasus

Sistem notifikasi digunakan untuk mengirim pesan melalui berbagai kanal seperti Email, SMS, dan WhatsApp.<br>
Sebelum dilakukan refactoring, seluruh logika notifikasi ditangani di dalam satu kelas bernama **NotificationManager**.<br>

Kondisi ini menyebabkan banyak pelanggaran prinsip SOLID.<br>

## ❌ Analisis Pelanggaran SOLID
### 1. Pelanggaran SRP (Single Responsibility Principle)

Masalah:<br>
Class **NotificationManager** menangani terlalu banyak tanggung jawab sekaligus, yaitu:<br>
- Menentukan jenis notifikasi (email/sms/whatsapp)
- Menjalankan logika pengiriman pesan
- Menampilkan hasil notifikasi
- Melakukan validasi tipe notifikasi

Kenapa melanggar?<br>
SRP mengatakan class hanya boleh memiliki satu alasan untuk berubah.<br>
Pada kasus ini:<br>
- Jika format email berubah → class harus diubah
- Jika format SMS berubah → class harus diubah
- Jika WhatsApp ditambah fitur baru → class harus diubah<br>
Class menjadi besar, sulit dirawat, dan rawan bug.

### 2. Pelanggaran OCP (Open/Closed Principle)

Masalah:
- Untuk menambah jenis notifikasi baru (misalnya Telegram), programmer harus:
- Membuka file **NotificationManager**
- Menambah **elif** baru di dalam **send_notification()**
- Menambahkan logika baru di class yang sama

Contoh kode buruk:

if notif_type == "email": ...<br>
elif notif_type == "sms": ...<br>
elif notif_type == "whatsapp": ...<br>


**Kenapa melanggar?**<br>
OCP menyatakan bahwa:<br>
Sistem harus terbuka untuk ditambah, tetapi tertutup terhadap modifikasi.<br>

Artinya jika ingin menambah fitur, kita tidak boleh mengubah kode lama.<br>
Pada kode awal, menambahkan satu metode baru = harus mengedit bagian **if/else**.<br>

Ini membuktikan class tidak memenuhi OCP.

### 3. Pelanggaran DIP (Dependency Inversion Principle)

Masalah:<br>
**NotificationManager** bergantung secara langsung pada class konkret seperti:
- **EmailNotification**
- **SMSNotification**
- **WhatsAppNotification**
Semua implementasi hardcoded ke dalam satu fungsi.<br>

Kenapa melanggar?<br>
DIP mensyaratkan:<br>
High-level module harus bergantung pada abstraksi, bukan implementasi konkret.<br>
Namun pada kode buruk:<br>
- **NotificationManager** mengatur detail pengiriman email/sms
- Tidak ada interface/abstraksi sebagai perantara
- Perubahan implementasi notifikasi akan mempengaruhi kode utama<br>

Akibatnya sistem sulit diperluas dan diuji.

## ✔️ Kesimpulan

Kode awal melanggar 3 prinsip SOLID utama:

Prinsip	Status	Penyebab<br>
SRP	❌ Dilanggar	Satu class mengerjakan terlalu banyak hal<br>
OCP	❌ Dilanggar	Penambahan fitur baru harus mengubah kode lama<br>
DIP	❌ Dilanggar	Bergantung pada implementasi, bukan abstraksi<br>
## ✔️ Solusi (Hasil Refactoring)

Setelah direfactor:

- Dibuat interface **INotificationSender** → DIP terpenuhi
- Dibuat class terpisah: **EmailNotification**, **SMSNotification**, **WhatsAppNotification** → SRP terpenuhi
- **NotificationService** hanya menerima interface dan tidak diubah saat menambah Telegram → OCP terpenuhi

Dengan refactoring ini:

- Kode lebih bersih
- Mudah diperluas (plugin style)
- Lebih mudah diuji (mock interface)
- Lebih stabil dan scalable