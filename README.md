### Nama : Afsar Rakha Farrasandi
### NPM : 2206028636
### Kelas : PBP C
### Link Aplikasi : http://afsar-rakha-tugas.pbp.cs.ui.ac.id. (DEPLOYMENT MASIH GAGAL)

# Rumah Kaos
![Bagan Request Client](https://github.com/afsarakhaa/rumah-kaos/assets/122893320/1ec0cfb0-becc-4aaa-ab99-c4b060aa8c2d)

### Selamat datang di **Rumah Kaos**!
### Tempat di mana gaya dan keunikan bertemu dalam ledakan warna dan desain yang mengagumkan! Kami adalah pusat fashion yang penuh semangat, tempat Anda bisa menemukan baju-baju keren yang membuat Anda berkilau sepanjang hari.

# TUGAS 2 : Implementasi Model-View-Template (MVT) pada Django
<br />

<details>
<summary> 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). 
</summary>

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
</details>

<br />

<details>
<summary> 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. </summary>

![Bagan Request Client](bagan_request_client.png)
 </details>

<br />

 <details>
<summary> 3.  Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? </summary>

Menggunakan virtual environment adalah praktik yang sangat direkomendasikan dalam pengembangan perangkat lunak, termasuk membuat aplikasi web berbasis python Django. Terdapat beberapa alasan mengapa kita perlu menggunakan virtual envoronment, yaitu:

- `Isolasi Lingkungan`: Virtual environment memungkinkan kita untuk membuat lingkungan kerja yang terisolasi dari sistem operasi utama. Hal ini tentunya dapat memasatikan bahwa dependensi dan paket-paket yang diperlukan untuk proyek tidak akan berinteraksi dan bertabrakan satu sama lain. Melalui virtual environment, konflik yang mungkin terjadi saat mengelola berbagai proyek akan terhindar.

- `Manajemen Dependensi`: Dengan virtual environment, kita dapat mengelola dependensi dan paket Python yang dibutuhkan oleh proyek secara terpisah. Kita dapat menginstall, menghapus, ataupun mengupgrade paket-paket ini tanpa memengaruhi proyek lain.

Sekarang, apabila terdapat pertanyaan "Apakah saya dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?". Jawabannya YA. Namun, sangat disarankan untuk menggunakan virtual environment karena akan membuat pengelolaan proyek lebih mudah dan mengurangi potensi masalah yang mungkin terjadi. Dengan virtual environment, kita dapat membuat lingkungan terisolasi khusus untuk proyek Django, menginstal semua dependensi yang diperlukan, dan mengelolanya dengan lebih baik.
</details>

<br />

<details>
<summary>4.  Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya. </summary>

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
</details>
<br />

# TUGAS 3 : Implementasi Form dan Data Delivery pada Django

<br />

<details>
<summary> 1. Apa perbedaan antara form POST dan form GET dalam Django? </summary>

Dalam Django, perbedaan antara form POST dan form GET terletak pada cara data dikirim dari halaman web ke server. Metode POST digunakan untuk mengirim data dengan cara yang lebih aman, dengan data tidak terlihat dalam URL, sehingga lebih cocok untuk operasi yang mengubah atau menyimpan data di server seperti mengirim formulir. Sementara itu, metode GET mengirim data melalui URL yang terlihat, yang cocok untuk operasi pencarian atau permintaan data yang tidak mengubah data di server. Penggunaan yang tepat antara keduanya sangat penting untuk menjaga keamanan, ukuran data, dan fungsionalitas aplikasi Django kita. Dalam Django, kita dapat mengetahui metode permintaan yang digunakan dengan menggunakan `request.META.get('REQUEST_METHOD')`

Referensi :
- https://docs.djangoproject.com/en/4.2/topics/forms/
- https://stackoverflow.com/questions/15017339/get-vs-post-django-forms
</details>

<br />

<details>
<summary> 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data? </summary>

- XML (eXtensible Markup Language):
    - **Struktur dan Tujuan**: 
    XML adalah bahasa markup yang digunakan untuk menyusun data dalam struktur hierarki yang dapat disesuaikan. XML tidak memiliki tujuan tertentu dan sering digunakan untuk pertukaran data antara aplikasi yang berbeda dan untuk menyimpan data konfigurasi.
    - **Notasi dan Struktur Data**:  
    XML menggunakan tag yang mendefinisikan struktur data. Ini dapat menggambarkan data yang sangat kompleks dengan baik, tetapi memiliki overhead dalam hal jumlah karakter yang digunakan.
    - **Tipe Data**: 
    Mendukung berbagai tipe data, termasuk teks, angka, tanggal, dan data yang kompleks. kita dapat mendefinisikan tipe data kustom menggunakan DTD atau XML Schema.
- JSON (JavaScript Object Notation):
    - **Struktur dan Tujuan**: 
    JSON adalah format pertukaran data yang ringan dan mudah dibaca oleh manusia. Ini terutama digunakan untuk pertukaran data antara aplikasi yang berjalan di lingkungan yang berbeda, seperti antara server dan klien web. JSON sangat populer dalam pengembangan web dan sering digunakan dalam API web.
    - **Notasi dan Struktur Data**: 
    JSON menggunakan notasi objek dan array yang lebih ringkas, membuatnya lebih efisien dalam hal ukuran data. Ini lebih mudah diproses oleh JavaScript dan bahasa pemrograman modern.
    - **Tipe Data**: Mendukung tipe data seperti string, angka, boolean, objek, dan array. Ini lebih sederhana dibandingkan dengan XML.
- HTML (Hypertext Markup Language):
    - **Struktur dan Tujuan**: 
    HTML adalah bahasa markup yang digunakan untuk membangun struktur dan tampilan halaman web. Ini fokus pada presentasi dan interaksi dengan pengguna, bukan pertukaran data mentah.
    - **Notasi dan Struktur Data**: 
    HTML adalah bahasa markup yang digunakan untuk mengatur tampilan dan struktur halaman web. Ini berfokus pada elemen-elemen seperti teks, gambar, dan tautan.
    - **Tipe Data**: 
    Digunakan untuk mengatur tampilan dan struktur halaman web, bukan untuk menggambarkan tipe data.
</details>

<br />

<details>
<summary> 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern? </summary>
- Ringan dan Efisien karena memiliki format yang ringan dan *compact*
- Mudah dipahami oleh manusia karena menggunakan notasi objek dan array yang mirip seperti `JavaScript`
- Kompatibilitas dengan JavaScript
- Dukungan pada berbagai bahasa pemrograman
- Dapat *Cross-Platform* dengan banyak platform lain, hal ini membuat JSON sangat *Versatile*
</details>

<br />

<details>
<summary> 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). </summary>

- [x] Membuat input `form` untuk menambahkan objek model pada app sebelumnya.

Sebagai Developer, pertama-tama saya mengubah fungsi `urlpatterns` pada urls.py terlebih dahulu dengan mengubah jalur `main/` menjadi `"`.

Setelah itu, saya membuat folder templates pada root folder (Folder Paling Luar) yang berisi `base.html`. File tersebut akan digunakan nantinya sebagai template bagi semua file HTML di app `rumah_kaos`. Selanjutnya, `templates` harus didaftarkan pada proyek dengan menambahkan `BASE_DIR` pada variabel `TEMPLATES` di `settings.py`. Barulah developer mengubah isi dari `main.html` agar bisa diintegrasikan dengan template pada `base.html`.

Setelah mengurus file HTML, saya baru dapat membuat form untuk input data yang nantinya akan menampilkan data item pada HTML. Saya membuat file `forms.py` pada folder `main` agar proyek bisa menerima data item baru. Pada file tersebut, saya menggunakan objek `Product` yang telah diimport pada file `models` dan membuat class `ProductForm`. Saya mengisi list list `fields` pada `ProductForm` dengan nama-nama atribut yang akan diinput ke user dalam bentuk `string` ketika membuat `Product` yaitu ("name", "price", "description"). Setelah itu, saya mengimport `ProductForm` yang berada di `forms.py` ke file `views.py` dan beberapa hal yang perlu diimport lainnya. Beberapa hal yang perlu diimport tersebut seperti gambar berikut (Termasuk Product dan ProductForm) :

**NOTES -> Pada Tugas kemarin, objek saya bernama  `Items` namun pada TUGAS-3 ini saya ganti menjadi `Product`**

```
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
```

Import di atas digunakan pada fungsi `create_product` yang akan menghasilkan form di laman form nantinya untuk menambahkan data produk ketika user melakukan submit.

Setelah itu, saya melakukan perubahan fungsi `show_main` di `views.py` dengan menambahkan variabel `products` dengan value `Product.objects.all()` yang nantinya akan mengambil semua instance dari objek `Product` pada database. Setelah itu, `products` dimasukkan ke dictionary `context`. Nilai dari `showmain` nantinya akan direturn oleh fungsi `render` dengan parameter `request`, `main.html`, dan `context`. Dapat dilihat sebagai berikut: 

```
def show_main(request):
    products = Product.objects.all()
    context = {
        'name': 'Acme De La Vie Baby Face Donut',
        'price': 'Rp850.000,00',
        'description': 'Kaos Acme De La Vie adalah kaos yang biasa dipakai oleh Koko-Koko di PIK',
        'image_url' : 'https://cdn.istyle.im/images/product/web/37/09/76/00/0/000000760937_01_800.png',
        'products' : products,

    }

    return render(request, "main.html", context)
```

Setelah itu, saya mengimport fungsi `create_product` ke `urls.py` pada folder `main` dan menambahkan path url ke `urlpatterns`. Setelah url ditambahkan, saya membuat file `create_product.html` pada folder `main/templates` untuk nantinya menampilkan laman form dalam menambahkan produk yang dilakukan oleh user. Langkah terakhir, tidak lupa saya menambahkan kode untuk menampilkan tabel yang berisi produk yang telah diinput oleh user dan button `Tambahkan Produk` di `main.html`. 
- Tampilan Tabel Form Produk serta Button `Tambahkan Produk` :

![Bagian Tabel Form Produk di main.html](bagian_tabel_produk.jpg)

- [x] Tambahkan 5 fungsi `views` untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

Pada tahap ini, saya membuat fungsi views yang nantinya akan digunakan untuk melihat data yang telah tersimpan dalam aplikasi. Suatu data dapat dilihat menggunakan format yang berbeda-beda, seperti HTML, XML, JSON. Untuk format XML dan JSON, kita dapat melihat objek spesifik menggunakan ID (Urutan Data). Pertama-tama saya perlu mengimport `HttpResponse`, agar bisa mengembalikan response ke web, dan `serializers`, agar bisa mengembalikan data dengan format yang sesuai.

Selanjutnya, saya membuat 4 fungsi, selain dari `show_main` yaitu `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id`. Keempat fungsi ini akan mengembalikan `HttpResponse` dengan parameter yang sesuai. Format data disesuaikan menggunakan method `serialize` dari `serializers`. Fungsi-fungsi berikut dapat dilihat sebagai berikut:

```
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

- [x] Membuat routing URL untuk masing-masing `views` yang telah ditambahkan pada poin 2.

Untuk semua fungsi `show` yang sudah dibuat, tidak lupa kita perlu mengimport fungsi-fungsi tersebut ke `urls.py` pada folder `main`. Setelah itu, tambahkan `path` ke`urlpatterns`. Sekarang, user bisa langsung mengakses URL dengan format HTML, XML, dan JSON baik menggunakan browser ataupun third-party aplikasi seperti POSTMAN.

- Tampilan import semua fungsi show di `urls.py` :

```
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 

```

- [x] Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

1. HTML
![Akses melalui HTML](akses_HTML.jpg)

2. XML
![Akses melalui XML](akses_XML.jpg)

3. JSON
![Akses melalui JSON](akses_JSON.jpg)

4. XML by ID
![Akses melalui XML by ID](akses_XML_by_ID.jpg)

5. JSON by ID
![Akses melalui JSON by ID](akses_JSON_by_ID.jpg)


Langkah Terakhir, Melakukan git `add`, `commit`, dan `push` ke Repository GitHub.
</details>

<br />

<details>
<summary> 5. **BONUS**  Menambahkan pesan "Kamu menyimpan X item pada aplikasi ini" (dengan X adalah jumlah data item yang tersimpan pada aplikasi) dan menampilkannya di atas tabel data. Kalimat pesan boleh dikustomisasi sesuai dengan tema aplikasi, namun harus memiliki makna yang sama. </summary>

Saya telah menambahkan pesan "Terdapat X Produk saat ini" (Dengan X adalah jumlah data item yang tersimpan pada aplikasi). Melalui method `.count()` pada variabel `product` saya dapat menghitung berapa jumlah produk yang disubmit pada form. Berikut implementasinya pada `views.py` :

```
    products = Product.objects.all()
    jumlah_produk = products.count() # Bagian untuk menghitung banyak produk
```
</details>

<br />

# TUGAS 4 : Implementasi Autentikasi, Session, dan Cookies pada Django

<br />

<details>
<summary>1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya? </summary>

`UserCreationForm` merupakan salah satu `form` bawaan yang disediakan oleh *framework* Django untuk memudahkan proses pembuatan `user` dalam aplikasi web. Formulir ini digunakan untuk membuat halaman *signup* di mana pengguna dapat mengisi informasi seperti username, password, dan lainnya untuk membuat akun baru di situs web pribadi.

- **Kelebihan** dalam menggunakan `UserCreationForm` pada Django:
    - **Kemudahan Implementasi** -> Menyediakan *plug and play* form secara bawaan, sehingga kita tidak perlu menulis form dari awal.
    - **Mudah terintegrasi dengan Model User** -> Data yang dimasukkan oleh pengguna dapat disimpan dengan mudah di dalam *database*
    - **Validasi login dan registrasi bawaan** -> Terdapat validasi login dan registrasi bawaan yang dapat memastikan bahwa kata sandi harus memenuhi syarat

- **Kekurangan** dalam menggunakan `UserCreationForm` pada Django:
    - **Kustomisasi terbatas** -> kustomisasi pada `UserCreationForm` terbatas apabila pengguna membutuhkan kebutuhan yang lebih kompleks
    - ***Default Interface* mungkin tidak sesuai** -> Tampilan default formulir pendaftaran mungkin tidak sesuai dengan desain yang pengguna inginkan
    - **Keterbatasan pembuatan akun** -> Terkadang, kebutuhan bisnis atau aplikasi yang kita buat mungkin tidak sejalan dengan alur pembuatan akun bawaan yang disediakan oleh `UserCreationForm`
</details>

<br />

<details>
<summary>2.  Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting? </summary>

| Fitur                       | Autentikasi                                      | Otorisasi                                   |
|-----------------------------|-------------------------------------------------|---------------------------------------------|
| Pengertian                   | Proses verifikasi identitas pengguna            | Proses memberikan izin akses kepada pengguna |
| Fokus Utama               | Berkaitan dengan proses login dan identifikasi pengguna                   |  Berkaitan dengan pengendalian hak akses pengguna dalam aplikasi web |
| Implementasi Django        | `authenticate(username=username, password=password)` | `@permission_required('some_permission')`   |
| Contoh                     | Kebijakan memverifikasi kata sandi sudah sesuai atau belum | Menentukan apakah pengguna memiliki hak untuk mengedit profil mereka |

**MENGAPA KEDUANYA PENTING?**

| Alasan                       | Autentikasi                                      | Otorisasi                                   |
|-----------------------------|-------------------------------------------------|---------------------------------------------|
| Keamanan                  | Memastikan bahwa hanya pengguna yang sah yang dapat mengakses akun mereka dan berinteraksi dengan aplikasi pengguna| Memastikan bahwa pengguna hanya dapat melakukan tindakan yang diizinkan |
| Regulasi               | Membantu pengguna memenuhi persyaratan dengan membatasi akses hanya kepada yang berwenang   | Membantu pengguna memenuhi persyaratan dengan membatasi akses hanya kepada yang berwenang |
| Kontrol Akses       | Membatasi akses pengguna ke berbagai fitur dari aplikasi kita setelah pengguna berhasil login | Mengendalikan dengan tepat siapa yang dapat berinteraksi dengan aplikasi   |
</details>

<br />

<details>
<summary>3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna? </summary>

Cookies merupakan potongan-potongan data kecil yang disimpan oleh server web di komputer pengguna dan dapat diakses oleh server saat pengguna melakukan permintaan ke situs web yang sama.

**Fungsi** -> Satu dari banyak cara untuk mengelola `data sesi` pengguna dalam aplikasi web

Seperti yang telah dijelaskan pada `Tutorial - 3`, kita dapat menggunakan cookies untuk mengelola data sesi pengguna dengan cara:
- Buka `views.py` yang ada pada subdirektori main dan tambahkan import `HttpResponseRedirect`, `reverse`, dan `datetime` 
- Menambahkan dan mengatur cookie dengan membuat objek `HttpResponse`tidak lupa kita perlu kita perlu memasukkannya ke dalam variable dan melakukan `return`. 

    Contoh seperti kode berikut ini: 
    ```    
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
    ```

- Ambil nilai cookies dengan menambahkan potongan kode `request.COOKIES.get('last_login')` ke dalam variable `context`
- Untuk bagian `Logout`, hapus cookie menggunakan perintah `.delete_cookie('last_login)`

Setelah melakukan langkah - langkah di atas, kita dapat mengecek sesi terakhir login dengan menambahkan potongan kode berikut pada `main.html``request.COOKIES['last_login']` atau kita dapat mengecek data sesi terakhir login menggunakan fitur *inspect element*.
</details>

<br />

<details>
<summary>4.  Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? </summary>

Penggunaan cookies dalam pengembangan web adalah alat yang umum digunakan untuk mengelola sesi pengguna, melacak preferensi, dan mengenali pengguna yang telah login

Tetapi, tentunya terdapat beberapa risiko potensial yang perlu diwaspadai oleh pengguna saat menggunakan cookies, antara lain:

- **Risiko Pencurian Data**

    Cookies dapat berisi data sensitif seperti token otentikasi atau informasi sesi yang apabila **Disalahgunakan** maka dapat berpotensi sebagai tindak kriminal.

- **Risiko Sabotase**

    Cookies dikirimkan dalam header HTTP, yang dapat disadap jika koneksi tidak dienkripsi dengan baik. 

- **Pencegahan Cross-Site Request Forgery (CSRF)**

    Cookies dapat digunakan untuk mencegah serangan CSRF dengan mengirimkan token CSRF dalam cookies.

- **Kerentanan Terhadap Serangan Cross-Site Scripting (XSS)**

    Apabila situs web kita rentan terhadap serangan XSS, penyerang dapat menyisipkan skrip berbahaya yang mengakses dan mencuri cookies pengguna.
</details>

<br />

<details>
<summary>5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). </summary>

- [x]  Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
    1. Fungsi Registrasi
        - Buka `views.py` yang ada pada subdirektori main dan buatlah fungsi dengan nama `register` yang menerima parameter `request`.
        - Tambahkan import `redirect,   UserCreationForm`, dan `messages` 
            ```
            from django.shortcuts import redirect
            from django.contrib.auth.forms import UserCreationForm
            from django.contrib import messages  
            ```
        - Menambahkan potongan kode register, untuk registrasi user,seperti di bawah ini
            ```
            def register(request):
            form = UserCreationForm()

            if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Your account has been successfully created!')
                    return redirect('main:login')
            context = {'form':form}
            return render(request, 'register.html', context)
            ```
        - Setelah itu, buat berkas HTML baru dengan nama `register.html` dengan template registrasi untuk mengatur *layout register page* 
        - Membuat routing path di `urls.py` pada subdirektori `main` dan melakukan import `from main.views import register` dan tambahkan path `path('register/', register, name='register')`

    2. Fungsi Login
        - Membuka `views.py` pada subdirektori `main` dan membuat fungsi `login_user` dengan paramater `request`

        *Notes* -> Jangan lupa untuk melakukan import `authenticate` dan `login`
        - Membuat berkas HTML baru dengan nama  `login.html` pada folder `main/template` dan menggunakan template untuk `login.html` dengan tujuan membuat *layout login page*. 
        - Membuat routing path di `urls.py` pada subdirektori `main` dan import `from main.views import login_user ` dan menambahkan path ke dalam `urlpatterns` `path('login/', login_user, name='login')`

    3. Fungsi Logout
        - Membuka `views.py` pada subdirektori `main` dan membuat fungsi `logout_user` dengan parameter `request`

        *Notes* -> Jangan lupa untuk melakukan import `logout`
        
        - Menambahkan potongan kode untuk logout di `main.html` dengan hyperlink html yang telah ditambahkan sebelumnya di `urlpatterns` pada `urls.py`

        - Membuat routing path di `urls.py` pada subdirektori `main` dan import `from main.views import logout_user` dan menambahkan path ke dalam `path('logout/', logout_user, name='logout')`

    Dengan melakukan tahapan di atas, pengguna dapat mengakses laman login, registrasi, serta interaksi untuk logout dari akun.

- [x] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

Pada bagian ini, saya membuat 2 *Account* dengan kriteria sebagai berikut:
- Akun Pertama
    - Username = afsarganteng
    - password = cobaaja123
    - Dummy data =
    ![Dummy_akun1 (1)](https://user-images.githubusercontent.com/122893320/270856459-dc667591-ec2d-4bed-8135-b3bfb150587b.png)   
    ![Dummy_akun1 (2)](https://user-images.githubusercontent.com/122893320/270856568-18f3f938-db70-4436-80e0-6859229e95ba.png)   
    ![Dummy_akun1 (3)](https://user-images.githubusercontent.com/122893320/270856587-ba7b68d5-e4b1-4ed8-a921-266eacbbd56f.png)   

- Akun Kedua
    - Username = rakhaganteng
    - password = tompel123
    - Dummy data = 
    ![Dummy_akun2 (1)](https://user-images.githubusercontent.com/122893320/270857127-7bd59e35-24b1-44da-b075-0c5096a4ddbd.png)   
    ![Dummy_akun2 (2)](https://user-images.githubusercontent.com/122893320/270857144-73117564-778c-4580-bfc1-50c04e367df8.png)   

- [x] Menghubungkan model `Item` dengan `User`.

Tujuan dilakukannya penghubungan antar `Item` dengan `User` adalah agar setiap user hanya dapat memiliki Item yang masing-masing mereka tambahkan pada akun mereka. Pada berkas `models.py`

Saya mengimplementasikan kode berikut ini:
```
user = models.ForeignKey(User, on_delete=models.CASCADE)
```

Kode di atas bertujuan untuk menghubungkan satu user dengan relationship sehingga item-item dari user tersebut bisa terasosiasikan dengan user yang mengirimkan request untuk melakukan add product. Relationship antara user dan product yang terjadi adalah **many-to-one relationship**. Kemudian, pada fungsi `create_product` di berkas `views.py` saya menambahkan kode :


 ```
form = ProductForm(request.POST or None)

if form.is_valid() and request.method == "POST":
    product = form.save(commit=False)
    product.user = request.user
    product.save()
    return HttpResponseRedirect(reverse('main:show_main'))
     
```

Kode yang ada di atas bertujuan untuk memberitahu bahwa item yang sedang ditambahkan pada page create product merupakan item yang dimiliki oleh user yang terotorisasi.

Terakhir, pada fungsi `show_main` di `views.py`, saya melakukan filter terahadap produk atau item-item yang akan ditampilkan merupakan item yang hanya dimiliki oleh user yang terotorisasi.

- [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan `cookies` seperti `last login` pada halaman utama aplikasi.

Agar nama pada main page menjadi dinamis (Tentunya tergantung pada username yang telah terotorisasi), pada fungsi `show_main` di `views.py`, saya memodifikasi pada `name` pada context menjadi `request.user.username`. Untuk menerapkan `cookies` berupa last login pada main page, saya menambahkan kode `response.set_cookie('last_login', str(datetime.datetime.now()))` yang berfungsi untuk **membuatkan cookie last_login dan menambahkannya pada response**. Kemudian, tidak lupa saat logout saya menghapus cookie tersebut dengan memodifikasi fungsi logout_user. Dan yang terakhir, saya menampilkan data last login pada main page dengan memodifikasi main.html dan menambahkan data last_login di context pada show_main.

- [x] Langkah Akhir, Saya melakukan add, commit, dan push ke repositori `rumah_kaos` yang telah saya buat dari tugas 2.

**BONUS** -> Saya mengerjakan Bonus dengan menambahkan tombol dan fungsi untuk menambahkan `amount` dari produk serta tombol dan fungsi untuk menghapus suatu objek
</details>

<br />

# TUGAS 5 : Desain Web menggunakan HTML, CSS dan Framework CSS

<br />

<details>
<summary> 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya! </summary>

- **Element Selector** (`Element atau Tag`)
    - **Manfaat**: 
    
    Selector elemen digunakan untuk memilih semua elemen HTML dengan jenis yang sama. Ini adalah cara paling sederhana dan umum untuk memberikan gaya pada elemen tertentu di halaman web kita.

    - **Kapan digunakan**: 
    
    Gunakan saat kita ingin memberikan gaya umum pada semua elemen dengan nama yang sama di seluruh halaman atau situs web kita. Misalnya, untuk mengubah tampilan teks pada semua elemen `<p>`

    *Contoh `Element Selector`:*
    ```       
    p {
        color: blue;
    }
    ```


- **Class Selector** (`.class`)
    - **Manfaat**:
    
    Selector class memungkinkan kita untuk memilih satu atau lebih elemen yang memiliki atribut class yang sama. Ini memungkinkan kita untuk memberikan gaya pada kelompok elemen dengan atribut class yang sama tanpa harus memengaruhi elemen lainnya.

    - **Kapan digunakan**: 
    
    Gunakan saat kita ingin memberikan gaya khusus pada kelompok elemen yang memiliki atribut class yang sama, tetapi elemen-elemen tersebut dapat ada di berbagai tempat di halaman kita.

    contoh `Class Selector`:
    ```    
    .highlight {
        background-color: yellow;
    }
    ```


- **ID Selector** (`#id`):
    - **Manfaat**: 
    
    Selector ID memungkinkan kita untuk memilih elemen dengan atribut id tertentu. Ini sering digunakan untuk memberikan gaya atau mengidentifikasi elemen unik di halaman web kita.

    - **Kapan digunakan**: 
    
    Gunakan saat kita ingin memberikan gaya khusus atau berinteraksi dengan elemen yang memiliki atribut id tertentu. Ingatlah bahwa ID harus unik di seluruh halaman.

    contoh `ID Selector`:
    ```
    #header {
        font-size: 24px;
    }

    ```

- **Pseudo-class Selector** (`:pseudo-class`)
    - **Manfaat:**
    
    Pseudo-class selector memungkinkan kita memilih elemen dalam keadaan atau situasi tertentu. Misalnya, :hover memilih elemen saat mouse mengarah ke atasnya.

    - **Kapan digunakan:** 
    
    Gunakan saat kita ingin memberikan gaya pada elemen dalam situasi atau keadaan tertentu, seperti elemen yang sedang dihover.

    contoh `Pseudo-class Selector`:
    ```
    a:hover {
        color: red;
    }

    ```

- **Attribute Selector** (`[attribute]`):
    - **Manfaat:** 
    
    Attribute selector memungkinkan kita memilih elemen berdasarkan atribut HTML mereka, baik dengan nilai atribut tertentu atau hanya atribut itu sendiri.

    - **Kapan digunakan:**
    
    Gunakan saat kita ingin memilih elemen berdasarkan atribut khusus yang mereka miliki, seperti memilih semua tautan dengan atribut target="_blank".

    contoh `Attribute Selector` :
    ```
    a[target="_blank"] {
        text-decoration: underline;
    }

    ```
</details>

<br />

<details>
<summary>  2. Jelaskan HTML5 Tag yang kamu ketahui </summary>

HTML5 (Hypertext Markup Language 5) adalah versi terbaru dari bahasa markup yang digunakan untuk membuat halaman web. Tentunya, HTML5 mengenalkan banyak elemen dan atribut baru yang memperluas kemampuan dan fungsionalitas HTML.

| Tag HTML5       | Deskripsi                                                     |
|-----------------|---------------------------------------------------------------|
| `<div>`         | Tag umum yang digunakan untuk mengelompokkan dan memformat elemen. |
| `<p>`           | Digunakan untuk menampilkan paragraf teks.                       |
| `<a>`           | Untuk membuat tautan atau hyperlink ke halaman lain.             |
| `<img>`         | Digunakan untuk menampilkan gambar pada halaman web.             |
| `<table>`         | Digunakan untuk Membuat tabel untuk menampilkan data.             |
| `<td>` dan `<tr>`         | Digunakan untuk Menunjukkan baris dan sel data dalam tabel.             |
| `<form>`         | Digunakan untuk Membuat formulir untuk mengumpulkan input dari pengguna.             |
| `<br>`         | Digunakan untuk  Menambahkan baris putus (line break) dalam teks.             |
| `<ul>` dan `<ol>`  | Untuk membuat daftar tak berurutan (unordered list) dan daftar terurut (ordered list). |
| `<li>`          | Digunakan dalam elemen `<ul>` dan `<ol>` untuk mendefinisikan item dalam daftar. |
| `<h1>`, `<h2>`, ... `<h6>` | Digunakan untuk menkitai judul atau heading dengan tingkat kepentingan yang berbeda. |
| `<form>`        | Untuk membuat formulir yang memungkinkan pengguna mengirimkan data. |
| `<input>`       | Digunakan dalam elemen `<form>` untuk membuat berbagai jenis elemen input, seperti teks, email, dan lainnya. |
| `<button>`      | Untuk membuat tombol interaktif yang dapat digunakan untuk tindakan pengguna. |

Selain HTML5 Tag di atas, masih banyak lagi HTML Tag lainnya yang dapat kita explore
</details>

<br />

<details>
<summary>  3. Jelaskan perbedaan antara margin dan padding! </summary>

Margin dan padding adalah dua properti CSS yang digunakan untuk mengatur ruang di sekitar elemen HTML, tetapi mereka memiliki perbedaan utama dalam cara mereka memengaruhi tata letak elemen dan ruang yang mereka tambahkan atau hilangkan.

- Margin
    
    Margin adalah ruang di luar elemen. Ini adalah jarak antara elemen yang kita atur dengan elemen-elemen lain di sekitarnya. Margin dapat digunakan untuk mengatur jarak elemen dari tepi area tampilan atau dari elemen lain yang ada di sekitarnya.
    
    contoh `Margin`:
    ```
    .product-card {
        margin: 50px;
    }
    ```
    Dalam contoh di atas, elemen dengan kelas `.product-card `akan memiliki margin `50 piksel` dari semua sisi. Selain itu, margin dapat kita atur juga sisi-sisinya, misalnya `margin-top`, `margin-right`,`margin-left`, dan lain lain.

- Padding

    Padding adalah ruang di dalam elemen. Ini adalah jarak antara batas elemen dan kontennya sendiri. Padding tidak memengaruhi elemen-elemen di sekitarnya, hanya konten di dalam elemen itu sendiri. Padding dapat digunakan untuk mengatur jarak antara konten elemen dan batasnya sendiri.

    contoh `Padding`:
    ```
    .product-card {
        padding: 20px;
    }
    ```
    Dalam contoh di atas, elemen dengan kelas `.product-card` akan memiliki padding `20 piksel` di dalamnya, di sekitar kontennya.


**PERBEDAAN UTAMA MARGIN DAN PADDING**
- `**Margin**` menambahkan ruang di luar elemen, mempengaruhi elemen-elemen di sekitarnya.
- `**Padding**` menambahkan ruang di dalam elemen, mempengaruhi tampilan dan posisi kontennya.
</details>

<br />

<details>
<summary>  4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya? </summary>

Berikut adalah perbandingan antara framework CSS Tailwind CSS dan Bootstrap dalam bentuk tabel yang dapat kita gunakan dalam README GitHub kita:

| Kriteria                               | Tailwind CSS                          | Bootstrap                             |
|----------------------------------------|--------------------------------------|---------------------------------------|
| **Filosofi**                           | Mendasarkan diri pada konsep "utility-first," dengan kelas CSS yang dapat digunakan untuk mengubah tampilan elemen. | Menggunakan komponen siap pakai dan gaya bawaan yang lebih kaku. |
| **Tingkat Kustomisasi**                | Tingkat kustomisasi tinggi. Dapat diubah sesuai kebutuhan dengan menentukan sendiri kelas-kelas CSS. | Tingkat kustomisasi sedang. Komponen Bootstrap memiliki gaya bawaan yang dapat disesuaikan, tetapi lebih sulit untuk membuat perubahan radikal. |
| **Ukuran**                             | Ukuran lebih kecil jika kita hanya menggunakan kelas yang diperlukan. | Ukuran lebih besar karena mengandung lebih banyak kode CSS dan komponen. |
| **Performa**                           | Lebih cepat dalam hal memuat halaman karena hanya mengirimkan kelas-kelas yang digunakan. | Lebih lambat dalam hal memuat halaman karena ukuran yang lebih besar, terutama jika kita tidak menggunakan komponen Bootstrap yang efisien. |
| **Kesulitan Penggunaan**               | Memiliki kurva belajar yang lebih curam untuk pemula, karena kita perlu mengingat banyak kelas. | Lebih mudah digunakan bagi pemula karena memiliki komponen siap pakai dengan gaya bawaan. |
| **Tampilan Akhir**                     | Tampilan akhir sering kali lebih unik dan tidak terlalu terlihat seperti "bootstrap." | Tampilan akhir sering kali lebih identik dengan gaya Bootstrap yang khas. |
| **Komunitas dan Ekosistem**            | Memiliki komunitas yang berkembang dengan berbagai plugin dan dukungan komunitas yang kuat. | Memiliki komunitas yang besar dan ekosistem yang luas dengan banyak sumber daya dan tutorial. |
| **Kapan Harus Digunakan**              | - Ketika kita ingin tingkat kustomisasi yang tinggi.<br>- Ketika kita ingin mengurangi ukuran file CSS.<br>- Ketika kita ingin tampilan yang unik dan tidak "terlihat seperti Bootstrap." | - Ketika kita ingin cepat membangun halaman web dengan gaya stkitar.<br>- Ketika kita ingin memiliki komponen siap pakai tanpa harus mengkodeknya sendiri.<br>- Ketika kita tidak memiliki banyak pengalaman dalam mengkustomisasi tampilan dengan CSS. |

Pemilihan antara Tailwind CSS dan Bootstrap tergantung pada proyek kita dan preferensi pribadi

**NOTES**
- Tailwind CSS  : Tailwind CSS lebih cocok untuk proyek-proyek di mana kita ingin tingkat kustomisasi yang tinggi dan tampilan yang unik
- Bootstrap     : Bootstrap lebih cocok untuk membangun situs dengan cepat menggunakan komponen siap pakai.
</details>

<br />

<details>
<summary>  5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). </summary>

Pada bagian ini, saya mengimplementasikan design atau style web saya menggunakan `CSS`, lebih tepatnya `Internal CSS` dan `Inline CSS`. Saya tidak menggunakan **framework** CSS karena agar saya dapat lebih *manually* mengatur dan meng-*custom* secara bebas. Berikut di bawah ini beberapa penjelasan bagian file html saya yang dipadukan dengan `CSS`.

### Kustomisasi Halaman Login (login.html):

1. **Background Gambar:** Saya mengatur gambar latar belakang pada halaman login. Ini dilakukan dengan menggunakan CSS `background-image` untuk mengatur latar belakang halaman.

```html
<style>
    body {
        background-image: url("https://i.pinimg.com/originals/b9/01/16/b901168260c3809094a71022b10e6f82.jpg");
    }
</style>
```

2. **Desain Form Login:** Form login dibuat lebih menarik dengan mengatur warna latar belakang, border radius, dan bayangan menggunakan CSS.

```html
<style>
    .login-container {
        background-color: #f5f5f5;
        max-width: 400px;
        padding: 60px;
        border-radius: 30px;
        box-shadow: 0 20px 300px rgba(0, 0, 0, 0.2);
        text-align: center;
        justify-content: center;
    }
</style>
```

3. **Tombol Login:** Tombol login dirancang dengan memberikan warna latar belakang yang sesuai dan efek hover untuk tombol.

```html
<style>
    .login-btn {
        background-color: #008CBA;
        color: #fff;
        border: none;
        padding: 12px 24px;
        border-radius: 20px;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s ease;
        font-weight: bold;
    }

    .login-btn:hover {
        background-color: #005f7f;
    }
</style>
```

### Kustomisasi Halaman Register (register.html):

1. **Background Gambar:** Sama seperti pada halaman login, Saya telah mengatur gambar latar belakang pada halaman registrasi menggunakan CSS `background-image`.

```html
<style>
    body {
        background-image: url("https://i.pinimg.com/originals/b9/01/16/b901168260c3809094a71022b10e6f82.jpg");
    }
</style>
```

2. **Desain Form Registrasi:** Form registrasi dibuat lebih menarik dengan mengatur warna latar belakang, border radius, dan bayangan menggunakan `CSS`.

```html
<style>
    .register-container {
        background-color: #f5f5f5;
        max-width: 400px;
        padding: 50px;
        border-radius: 20px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        text-align: center;
    }
</style>
```

3. **Tombol Register:** Tombol register dirancang dengan memberikan warna latar belakang yang sesuai dan efek hover untuk tombol.

```html
<style>
    .register-btn {
        background-color: #008CBA;
        color: #fff;
        border: none;
        padding: 11px;
        border-radius: 20px;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s ease;
        font-weight: bold;
    }

    .register-btn:hover {
        background-color: #005f7f;
    }
</style>
```

### Kustomisasi Halaman Utama (main.html):

1. **Desain Kartu Produk:** Kartu produk dibuat dengan bayangan dan border radius untuk memberikan tampilan yang lebih menarik. Pada hal ini saya juga menggunakan *approach* berupa `card` agar produk saya dapat ditampilkan lebih menarik seperti pada *e-commerce*.

```html
<style>
    .product-card {
        padding: 30px;
        border-radius: 50px;
        box-shadow: 2px 7px 25px rgba(0, 0, 0, 0.1);
    }
</style>
```

2. **Kustomisasi Tabel Produk:** Tabel produk dibuat dengan tampilan yang lebih menarik, termasuk header tabel, sel tabel, dan latar belakang baris yang berbeda secara bergantian. Pada hal ini saya juga mengerjakan soal **BONUS** berupa baris terakhir pada tabel yang diberikan warna berbeda, tapi saya menggunakan *approach* lain yaitu dengan mengganti table row yang genap menjadi warna lebih gelap.

```html
<style>
    th {
        background-color: #008CBA;
        color: #fff;
        text-align: left;
        padding: 12px;
        border-bottom: 2px solid #005f7f;
    }

    td {
        padding: 12px;
        border-bottom: 1px solid #ddd;
    }

    tr:nth-child(even) { 
        background-color: #f2f2f2;
    }
</style>
```

3. **Tombol-tombol:** Tombol-tombol pada tabel produk dan tombol logout dirancang dengan memberikan warna latar belakang yang sesuai dan efek hover.

```html
<style>
    .custom-button {
        background-color: #008CBA;
        color: #fff;
        border: none;
        padding: 12px 24px;
        border-radius: 10px;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s ease;
        margin-right: 5px;
    }

    .custom-button-delete {
        background-color: #E74C3C;
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 10px;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s ease;
        margin-right: 10px;
    }

    .custom-button:hover {
        background-color: #005f7f;
    }

    .custom-button-delete:hover {
        background-color: #C0392B;
    }
</style>
```

4. **Tampilan Tombol Logout:** Tombol logout juga diberi tampilan yang sesuai dengan CSS.

```html
<style>
    .logout-button {
        background-color: #E74C3C;
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 25px;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s ease;
        text-decoration: none;
        width: fit-content;
    }

    .

logout-button:hover {
        background-color: #C0392B;
    }
</style>
```

### Kustomisasi Halaman Edit Produk (edit_product.html) dan Tambah Produk (create_product.html):

1. **Desain Form Edit dan Tambah Produk:** Form di halaman edit produk dan tambah produk diberi tampilan yang lebih menarik dengan mengatur latar belakang, bayangan, dan border radius.

```html
<style>
    .product-form {
        background-color: #f5f5f5;
        max-width: 400px;
        padding: 50px;
        border-radius: 20px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        text-align: center;
    }
</style>
```

2. **Tombol "Edit Product" dan "Tambahkan Produk":** Tombol-tombol ini diberi warna latar belakang yang sesuai dan efek hover.

```html
<style>
    .edit-product-button {
        background-color: #008CBA;
        color: #fff;
        border: none;
        padding: 12px 24px;
        border-radius: 20px;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s ease;
        font-weight: bold;
    }

    .create-product-button {
        background-color: #008CBA;
        color: #fff;
        border: none;
        padding: 12px 24px;
        border-radius: 20px;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s ease;
        font-weight: bold;
    }

    .edit-product-button:hover {
        background-color: #005f7f;
    }

    .create-product-button:hover {
        background-color: #005f7f;
    }
</style>
```
</details>

<br />

# TUGAS 6 : JavaScript dan Asynchronous JavaScript

<br />

<details>
<summary> 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming! </summary>

<br />

### Perbedaan antara Asynchronous Programming dan Synchronous Programming
| Kriteria                                | Asynchronous Programming                                           | Synchronous Programming                                           |
|-----------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|
| Aliran Eksekusi                        | Tugas-tugas dieksekusi bersamaan (concurrently).                    | Tugas dieksekusi satu per satu (serially).                        |
| Responsifitas                         | Membuat aplikasi tetap responsif bahkan saat ada tugas berat.     | Aplikasi dapat menjadi tidak responsif saat ada tugas berat.      |
| Penghentian                           | Tidak harus menunggu tugas sebelumnya selesai untuk melanjutkan.  | Harus menunggu tugas sebelumnya selesai sebelum melanjutkan.      |
| Implementasi                         | Menggunakan konsep callback, Promise, async/await, event listener. | Menggunakan struktur berurutan (sequential) dan blokir eksekusi.   |
| Contoh                                | Penggunaan AJAX, pemrosesan data asinkron, menghindari freezing UI. | Pembacaan berkas besar, pemrosesan data secara berurutan.         |
| Kecepatan                             | Dapat mengoptimalkan penggunaan sumber daya dan mempercepat eksekusi tugas. | Tergantung pada seberapa cepat tugas berikutnya dapat dimulai setelah yang sebelumnya. |
| Skalabilitas                          | Lebih baik untuk mengelola banyak permintaan secara bersamaan.   | Tidak efisien jika harus mengelola banyak tugas secara bersamaan. |
| Manajemen Kesalahan                   | Memerlukan manajemen kesalahan yang baik, seperti penanganan Promise rejection. | Kesalahan dapat lebih mudah dikelola dalam struktur berurutan.   |
</details>

<br />

<details>
<summary> 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini. </summary>

<br />

Dalam konteks pengembangan web dengan `JavaScript` dan `AJAX`, paradigma **event-driven programming** mengacu pada pendekatan pemrograman di mana aliran eksekusi program terutama dikendalikan oleh kejadian (events) yang terjadi. Berbeda dengan pendekatan yang berpusat pada alur eksekusi linear (**synchronous**), paradigma event-driven programming mengizinkan program untuk menunggu dan merespons berbagai jenis kejadian tanpa harus terkunci dalam urutan tugas tertentu.

Dalam TUGAS 6 ini, salah satu contoh penerapan paradigma event-driven programming adalah ketika tombol` Add Product by AJAX` ketika diklik. Pada saat tombol ini diklik, terjadi kejadian *(event)* yang memicu pembukaan modal *(dialog)* untuk menambahkan produk baru. Pada kode ini, hal ini dinyatakan dengan menggunakan atribut `data-bs-toggle` dan `data-bs-target`, yang akan menampilkan modal ketika tombol diklik.

Selain itu, dalam implementasi JavaScript di kode saya, saya juga mengatur tombol tersebut dengan menggunakan `event listener`, tepatnya pada baris berikut:

```
document.getElementById("button_add").onclick = addProduct;
```

Potongan kode di atas adalah contoh lain dari paradigma *event-driven*, di mana saya menentukan bahwa saat tombol dengan ID `button_add` diklik, fungsi `addProduct` harus dijalankan. Dengan demikian, program program merespons event ini dan melakukan tindakan yang sesuai, yaitu menambahkan produk baru menggunakan AJAX. Secara keseluruhan, **paradigma event-driven programming** memungkinkan pengembang untuk membuat aplikasi yang lebih responsif dan interaktif dengan merespons berbagai kejadian pengguna atau kejadian lainnya yang terjadi dalam aplikasi web.
</details>

<br />

<details>
<summary> 3. Jelaskan penerapan asynchronous programming pada AJAX.</summary>

<br />

Pada **AJAX (Asynchronous JavaScript and XML)**, penerapan asynchronous programming adalah prinsip yang sangat penting. Ini memungkinkan aplikasi web untuk mengirim permintaan (*request*) ke server dan menerima respon (*response*) tanpa harus menunggu respon selesai sebelum melanjutkan tugas lain. Inilah yang memungkinkan aplikasi web untuk tetap responsif dan tidak terblokir saat menunggu data dari server.

Berikut adalah cara penerapan asynchronous programming pada AJAX dalam aplikasi `Rumah Kaos`:

- **Fetch API**

Dalam kode aplikasi `Rumah Kaos`, Fetch API digunakan untuk mengirim permintaan HTTP ke server dan menerima data dari server secara asinkron. Pada dasarnya, kode JavaScript dapat melanjutkan eksekusi selama permintaan ke server berlangsung. Contoh penggunaannya adalah saat mengambil data produk dari server dengan mengirim permintaan ke endpoint yang sesuai.

```
async function getProducts() {
    return fetch("{% url 'main:get_product_json' %}").then((res) => res.json());
}
```
- **Async/Await**

Dalam beberapa bagian kode, terdapat penggunaan kata kunci `async` dan `await`. Ini memungkinkan kode untuk menunggu hasil dari fungsi asynchronous sebelum melanjutkan. Ini sangat berguna saat aplikasi perlu mengambil data dari server dan menunggu hasilnya sebelum menampilkan atau memproses data tersebut.

```
async function refreshProducts() {
    const products = await getProducts();
    // ...
}
```

- **Callback Functions**

AJAX sering menggunakan callback functions untuk menangani respons dari server. Callback functions ini akan dieksekusi setelah respons dari server diterima, sehingga aplikasi dapat melakukan tindakan yang sesuai.

Contoh:

```
function deleteProduct(productId) {
    if (confirm("Apakah Anda yakin ingin menghapus produk ini?")) {
        fetch(`delete_product_ajax/${productId}`, {
            method: "DELETE",
            headers: {
                "X-CSRFToken": document.querySelector('input[name="csrfmiddlewaretoken"]').value,
            },
        })
        .then(refreshProducts) // Callback function
        .then(updateProducts);
    }
}
```

#### KESIMPULAN
Penerapan `asynchronous programming` pada `AJAX` memastikan bahwa aplikasi dapat tetap responsif dan tidak terblokir saat melakukan tugas-tugas seperti mengambil data dari server atau mengirim data ke server. Hal ini meningkatkan pengalaman pengguna dan efisiensi aplikasi web.
</details>

<br />

<details>
<summary> 4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan. </summary>

<br />

Fetch API dan jQuery adalah dua teknologi yang digunakan untuk mengimplementasikan AJAX dalam aplikasi web, sebagai contoh web saya yaitu `Rumah Kaos.` Berikut saya lampirkan tabel perbandingan untuk Fetch API dan JQuery

| Fitur/Poin           | Fetch API                      | jQuery                            |
|-----------------------|--------------------------------|----------------------------------|
| **Native JavaScript** | Ya, merupakan bagian dari JS    | Tidak, library eksternal          |
| **Promise-based**     | Ya, berbasis promise            | Tidak, berbasis callback          |
| **Kompatibilitas**    | Browser modern                 | Lintas browser, termasuk lama    |
| **Sintaks**           | Moderat, memerlukan penanganan khusus | Sederhana dan mudah dipahami   |
| **Fleksibilitas**     | Tinggi, pengendalian detail     | Terbatas, terutama dalam kontrol HTTP |
| **Plugin Ekosistem**  | Tidak ada, tetapi dapat digabungkan dengan library lain | Ekosistem plugin yang besar     |

<br />

Pemilihan antara` Fetch API` dan JQuery tergantung pada kebutuhan proyek dan preferensi pengembang.` Fetch API` lebih cocok untuk aplikasi modern yang ditargetkan pada browser modern, sementara `JQuery` masih berguna dalam situasi yang memerlukan kompatibilitas lintas browser dan pengembangan yang cepat dengan sintaks yang sederhana.

Dalam konteks aplikasi `Rumah Kaos`,** Fetch API adalah pilihan yang lebih baik ** dengan alasan sebagai berikut:

 - **Fetch API adalah Standar**
 
Fetch API adalah bagian dari spesifikasi standar JavaScript, sehingga ini adalah pilihan yang modern dan sesuai dengan perubahan di dunia web.

- Tidak Memerlukan *External Library* 

Menggunakan Fetch API berarti kita tidak perlu mengunduh atau memasang jQuery, yang akan membuat aplikasi lebih ringan.

- **Fleksibilitas dan Kontrol** 

Dalam kasus aplikasi yang lebih kompleks seperti `Rumah Kaos` kita mungkin memerlukan lebih banyak fleksibilitas dan kontrol dalam mengelola permintaan dan respons HTTP. `Fetch API` memberikan tingkat kontrol yang lebih besar dalam hal ini.

- **Promise-based**

Dengan `Fetch API`, kita dapat mengelola asinkronisitas dengan lebih baik menggunakan promise. Ini membuat kode lebih mudah dipahami dan dirawat.
</details>

<br />

<details>
<summary> 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). </summary>

<br />

Implementasi AJAX mencakup dua bagian: `AJAX GET` dan `AJAX POST`, serta penanganan BONUS penghapusan produk dengan `AJAX DELETE`.

## Langkah 1: AJAX GET

1. **Membuat Fungsi untuk Mengambil Produk dengan AJAX GET:**
   - Buat fungsi JavaScript bernama `getProducts()`.
   - Gunakan `fetch` untuk mengambil daftar produk dengan menggunakan URL `{% url 'main:get_product_json' %}`.
   - Fungsi ini akan mengembalikan promise yang berisi respons yang telah diubah menjadi JSON.

    ```javascript
    async function getProducts() {
        return fetch("{% url 'main:get_product_json' %}").then((res) => res.json());
    }
    ```

2. **Menyegarkan dan Menampilkan Produk dengan AJAX (TABEL):**
   - Buat fungsi `refreshProducts()` yang akan mereset dan mengisi tabel produk dengan data yang diterima melalui AJAX.
   - Perbarui konten dalam tabel produk dan tambahkan produk yang diterima dari server ke dalam tabel.

    ```javascript
    async function refreshProducts() {
        document.getElementById("product_table").innerHTML = "";
        const products = await getProducts();
        // ... (kode untuk menggambarkan data produk di dalam tabel)
    }
    ```

3. **Menampilkan Produk dengan AJAX (CARDS):**
   - Buat fungsi JavaScript bernama `updateProducts()` yang mengambil data produk melalui AJAX dan menampilkan produk dalam bentuk kartu.
   - Perbarui konten dalam tabel produk dan tambahkan produk yang diterima dari server ke dalam tabel.

    ```javascript
    async function updateProducts() {
        const products = await getProducts();
        const productContainer = document.getElementById("product-container");
        productContainer.innerHTML = "";
        // ... (kode untuk menggambarkan data produk di dalam kartu)
    }
    ```

## Langkah 2: AJAX POST

1. **Membuat Tombol untuk Membuka Modal:**
   - Saya telah memiliki tombol yang digunakan untuk membuka modal untuk menambahkan produk.

2. **Membuat Modal Form:**
   - Pastikan Saya memiliki form modal dengan elemen-elemen yang sesuai seperti input untuk nama, harga, jumlah, deskripsi, dan tautan gambar.

3. **Membuat Fungsi untuk Menambahkan Produk dengan AJAX POST:**
   - Buat fungsi JavaScript yang disebut `addProduct()`.
   - Gunakan `fetch` dengan metode **POST** untuk mengirim data formulir ke server.
   - Pastikan Saya menggunakan `FormData` untuk mengumpulkan data formulir.

    ```javascript
    function addProduct() {
        fetch("{% url 'main:add_product_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        })
        .then(refreshProducts)  // Menyegarkan data produk setelah menambah produk baru
        .then(updateProducts);

        document.getElementById("form").reset();  // Mengosongkan formulir
        return false;
    }
    ```

4. **Menghubungkan Tombol "Add Product" dengan Fungsi Add Product:**
   - Menghubungkan tombol "Add Product" pada modal dengan fungsi `addProduct()` dengan menambahkan event listener untuk mengatasi klik tombol.

    ```javascript
    document.getElementById("button_add").onclick = addProduct;
    ```

## Langkah 3: Penanganan Penghapusan Produk dengan AJAX

1. **Membuat Fungsi untuk Menghapus Produk dengan AJAX DELETE:**
   - Buat fungsi JavaScript yang disebut `deleteProduct(productId)`.
   - Gunakan `fetch` dengan metode DELETE untuk menghapus produk berdasarkan ID.
   - Pastikan Saya menyertakan token CSRF dalam header permintaan.

    ```javascript
    function deleteProduct(productId) {
        if (confirm("Apakah Anda yakin ingin menghapus produk ini?")) {
            fetch(`delete_product_ajax/${productId}`, {
                method: "DELETE",
                headers: {
                    "X-CSRFToken": document.querySelector('input[name="csrfmiddlewaretoken"]').value
                }
            })
            .then(refreshProducts)  // Menyegarkan data produk setelah menghapus produk
            .then(updateProducts);
        }
    }
    ```

2. **Menambahkan Tombol "Delete" pada Tabel Produk:**
   - Tambahkan tombol "Delete" pada setiap baris tabel produk yang akan memanggil fungsi `deleteProduct()` saat diklik.

    ```html
    <button title="Delete" class="custom-button-delete" onclick="deleteProduct(${item.pk})">Delete by AJAX</button>
    ```

## Langkah 4: Menjalankan Fungsi Awal dan Pengisian Produk

Terakhir, pastikan Saya menjalankan fungsi `updateProducts()` untuk mengisi produk awal dan `refreshProducts()` untuk mengambil produk menggunakan AJAX pada saat halaman dimuat.

```javascript
updateProducts();
refreshProducts();
```

Dengan langkah-langkah ini, Saya telah mengimplementasikan AJAX `GET`, AJAX `POST`, dan penanganan penghapusan (BONUS) produk dengan `AJAX DELETE` untuk aplikasi `Rumah Kaos`. Saya dapat menambahkan, menghapus, dan menyegarkan daftar produk secara asinkron menggunakan AJAX. 

## **NOTES**
Saya Telah mengerjakan juga bagian BONUS yaitu mengimplementasikan `AJAX` pada `Button Delete`      
</details>
