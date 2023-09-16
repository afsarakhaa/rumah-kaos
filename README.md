# Rumah Kaos

#### Nama : Afsar Rakha Farrasandi
#### NPM : 2206028636
#### Kelas : PBP C

Link Adaptable : - (Dikarenakan terdapat kendala dalam deploy dengan adaptable)


> 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- [x] Membuat sebuah proyek Django baru.

Sebagai langkah awal yang sudah diajarkan pada tutorial 0, sebagai developer, pertama - tama saya perlu membaut direktori lokal bernama `rumah_kaos` dan membuat repositori *public* di github yang terhubung dengan repositori lokal. Melalui perintah `git branch -M main`, direktori lokal dapat terhubung untuk membuat main branch dan lewat perintah `git remote add origin <URL_REPO>`, direktori lokal langsung dihubungkan dengan repositori pada GitHub. Setelah repositori dan direktori lokal terhubung, saya membuat virtual environment pada direktori lokal dengan menggunakan perintah `python -m venv env`. Setelah itu, virtual environment dapat diaktifkan dengan perintah `source env/bin/activate`. Pada direktori utama, file `requirements.txt` perlu ditambahkan untuk menjadi daftar dependensi dari proyek ini. Dependensi perlu diinstall pada direktori proyek dengan perintah `pip install -r requirements.txt`. Langkah terakhir,  proyek dapat dibuat dengan perintah `django-admin startproject rumah_kaos`.

Langkah tambahan, saya perlu mengkonfigurasikan proyek dengan menambahkan `*` pada variabel `ALLOWED_HOST` di file `settings.py` dengan tujuan untuk memberikan akses ke semua host.

- [x] Membuat aplikasi dengan nama `main` pada proyek tersebut.

Setelah menyelesaikan pembuatan proyek, saya perlu membuat direktori main di dalam direktori utama dengan menjalankan perintah `python manage.py startapp main`. Direktori ini akan berperan sebagai kerangka dasar dari proyek yang telah dibuat. Sebagai developer, saya juga mendaftarkan folder main ke dalam proyek dengan menambahkan `main` dalam variabel `INSTALLED_APPS` pada file `settings.py`.

- [x] Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`.

Saya menambahkan path atau jalur ke dalam variabel `urlpatterns` pada `urls.py` agar rute URL aplikasi dapat didefinisikan. Path terdiri atas route, function pada `views.py`, dan parameter `name`. Setelah itu, saya mengkonfigurasikan routing URL proyek dengan menambahkan jalur yang terdiri dari rute serta fungsi include ke dalam variabel `urlpatterns`. Fungsi include digunakan untuk mengimpor rute URL dari aplikasi utama ke dalam berkas `urls.py` proyek.

- [x] Membuat model pada aplikasi `main` dengan nama `Item` dan wajib memiliki atribut wajib sebagai berikut.
    -  `name` sebagai nama dari *item* dengan tipe `CharField`.
    - `amount` sebagai jumlah dari *item* dengan tipe `IntegerField`.
    - `description` sebagai deskripsi dari *item* dengan tipe `TextField`.

- [x] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam _template_ HTML yang menampilkan nama aplikasi, nama item, jumlah item, dan deskripsi item.

Saya melakukan import function `render` agar proses rendering bisa dilakukan terhadap tampilan `main.html` yang telah saya buat. Setelah itu, dengan mendeklarasi function `show_main` dengan parameter `request`. Lalu, saya menambahkan data `name`, `amount`, dan `description` dalam fungsi `show_main`. Function `show_main` akan return `render(request, "main.html", context)` untuk menampilkan html pada web server.

- [x] Proses deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga dapat diakses oleh publik melalui internet.

Pada proses ini, saya melakukan deployment dengan menghubungkan repositori `rumah_kaos` dengan aplikasi, memilih `Python App Template` dan `PostgreSQL` sebagai database. Saya juga perlu menyesuaikan versi python yang sesuai pada komputer saya yaitu python 3.10 dan menerapkan perintah `python manage.py migrate && gunicorn rumah_kaos.wsgi`. Sebagai langkah terakhir, saya perlu mencentang opsi `HTTP Listener on PORT` dan deploy aplikasi.

*NOTES* -> Dikarenakan terdapat kendala pada Adaptable, jadi, proses deployment tidak dilakukan untuk sementara waktu. Maka, hanya sampai tahap mengumpulkan repositori.

> 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Bagan Request Client](bagan_request_client.png)

> 3.  Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Menggunakan virtual environment adalah praktik yang sangat direkomendasikan dalam pengembangan perangkat lunak, termasuk membuat aplikasi web berbasis python Django. Terdapat beberapa alasan mengapa kita perlu menggunakan virtual envoronment, yaitu:

- `Isolasi Lingkungan`: Virtual environment memungkinkan kita untuk membuat lingkungan kerja yang terisolasi dari sistem operasi utama. Hal ini tentunya dapat memasatikan bahwa dependensi dan paket-paket yang diperlukan untuk proyek tidak akan berinteraksi dan bertabrakan satu sama lain. Melalui virtual environment, konflik yang mungkin terjadi saat mengelola berbagai proyek akan terhindar.

- `Manajemen Dependensi`: Dengan virtual environment, kita dapat mengelola dependensi dan paket Python yang dibutuhkan oleh proyek secara terpisah. Kita dapat menginstall, menghapus, ataupun mengupgrade paket-paket ini tanpa memengaruhi proyek lain.

Sekarang, apabila terdapat pertanyaan "Apakah saya dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?". Jawabannya YA. Namun, sangat disarankan untuk menggunakan virtual environment karena akan membuat pengelolaan proyek lebih mudah dan mengurangi potensi masalah yang mungkin terjadi. Dengan virtual environment, kita dapat membuat lingkungan terisolasi khusus untuk proyek Django, menginstal semua dependensi yang diperlukan, dan mengelolanya dengan lebih baik.

> 4.  Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah tiga pola desain (design pattern) yang digunakan dalam pengembangan perangkat lunak untuk memisahkan logika aplikasi dan tampilan. Ini membantu dalam mengorganisasi kode dan meningkatkan pemeliharaan serta skalabilitas aplikasi. Berikut merupakan penjelasan singkat tentang ketiga pola desain tersebut:

- MVC (Mode-View-Controller):
    - Model         :  Mewakili data dan logika bisnis. Ini mengelola penyimpanan, validasi, dan manipulasi data.
    - View          :  Menampilkan informasi kepada pengguna. Ini adalah antarmuka pengguna (UI).
    - Controller    :  Bertindak sebagai penghubung antara Model dan View. Ini menerima input dari pengguna melalui View, memprosesnya menggunakan Model, dan kemudian memperbarui tampilan.

    *PERBEDAAN UTAMA*: 
    - MVC merupakan pola desain yang digunakan dalam pengembangan web tradisional (Outdated)
    - MVC lebih cocok untuk aplikasi web yang relatif sederhana

- MVT (Model-View-Template):
    - Model     : Sama halnya seperti MVC, Model mewakili data dan logika bisnis
    - View      : Merupakan antarmuka pengguna (UI), seperti pada MVC
    - Template  : Merupakan bagian yang unik dari MVT. Template adalah bagian yang mendefinisikan bagaimana data dari Model akan ditampilkan dalam View. Ini sering digunakan dalam kerangka kerja web berbasis Python, seperti Django.

    *PERBEDAAN UTAMA*: 
    - MVT merupakan varian dari MVC yang lebih spesifik untuk pengembangan web menggunakan kerangka kerja (framework) Django.
    - Template digunakan untuk memisahkan logika tampilan dari kode Python dalam Django.

- MVVM (Model-View-ViewModel):
    - Model     : Sama halnya seperti Model di MVC dan MVT, untuk mengelola data dan logika bisnis.
    - View      : Representasi tampilan, seperti dalam MVC dan MVT.
    - ViewModel : Komponen tambahan yang menghubungkan Model dan View. Ini mengonversi data dari Model menjadi format yang dapat ditampilkan oleh View. ViewModel juga dapat menangani logika tampilan tertentu.

    *PERBEDAAN UTAMA*: 
    - MVVM adalah pola desain yang sering digunakan dalam pengembangan aplikasi berbasis tampilan (UI) yang lebih kompleks dan advance, seperti aplikasi moible ataupun desktop.
    - ViewModel adalah konsep utama dalam MVVM yang tidak ada dalam MVC atau MVT. Ini membantu memisahkan logika tampilan dari Model dan memudahkan pengujian unit.

KESIMPULAN
Pemilihan pola desain tergantung pada jenis aplikasi yang akan kita kembangkan. Kompleksitas dan bahasa pemrograman yang digunakan juga menentukan pemilihan pola desain. MVC, MVT, dan MVVM semuanya bertujuan untuk memisahkan peran dalam aplikasi, meningkatkan pemeliharaan kode, dan memungkinkan skalabilitas.






