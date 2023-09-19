# Rumah Kaos

#### Nama : Afsar Rakha Farrasandi
#### NPM : 2206028636
#### Kelas : PBP C

Link Adaptable : - (Dikarenakan terdapat kendala dalam deploy dengan adaptable)

# TUGAS 2

<details>
> <summary> 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). </summary>

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

<details>
<summary>
> 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. </summary>

![Bagan Request Client](bagan_request_client.png)
</details>

<details>
<summary>
> 3.  Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Menggunakan virtual environment adalah praktik yang sangat direkomendasikan dalam pengembangan perangkat lunak, termasuk membuat aplikasi web berbasis python Django. Terdapat beberapa alasan mengapa kita perlu menggunakan virtual envoronment, yaitu:

- `Isolasi Lingkungan`: Virtual environment memungkinkan kita untuk membuat lingkungan kerja yang terisolasi dari sistem operasi utama. Hal ini tentunya dapat memasatikan bahwa dependensi dan paket-paket yang diperlukan untuk proyek tidak akan berinteraksi dan bertabrakan satu sama lain. Melalui virtual environment, konflik yang mungkin terjadi saat mengelola berbagai proyek akan terhindar.

- `Manajemen Dependensi`: Dengan virtual environment, kita dapat mengelola dependensi dan paket Python yang dibutuhkan oleh proyek secara terpisah. Kita dapat menginstall, menghapus, ataupun mengupgrade paket-paket ini tanpa memengaruhi proyek lain.

Sekarang, apabila terdapat pertanyaan "Apakah saya dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?". Jawabannya YA. Namun, sangat disarankan untuk menggunakan virtual environment karena akan membuat pengelolaan proyek lebih mudah dan mengurangi potensi masalah yang mungkin terjadi. Dengan virtual environment, kita dapat membuat lingkungan terisolasi khusus untuk proyek Django, menginstal semua dependensi yang diperlukan, dan mengelolanya dengan lebih baik.

</details>

<details>
<summary>
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

# TUGAS 3

<details>
<summary>
> 1. Apa perbedaan antara form POST dan form GET dalam Django?

Dalam Django, perbedaan antara form POST dan form GET terletak pada cara data dikirim dari halaman web ke server. Metode POST digunakan untuk mengirim data dengan cara yang lebih aman, dengan data tidak terlihat dalam URL, sehingga lebih cocok untuk operasi yang mengubah atau menyimpan data di server seperti mengirim formulir. Sementara itu, metode GET mengirim data melalui URL yang terlihat, yang cocok untuk operasi pencarian atau permintaan data yang tidak mengubah data di server. Penggunaan yang tepat antara keduanya sangat penting untuk menjaga keamanan, ukuran data, dan fungsionalitas aplikasi Django Anda. Dalam Django, kita dapat mengetahui metode permintaan yang digunakan dengan menggunakan `request.META.get('REQUEST_METHOD')`

Referensi :
- https://docs.djangoproject.com/en/4.2/topics/forms/
- https://stackoverflow.com/questions/15017339/get-vs-post-django-forms

</details>

<details>
<summary>
> 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

- XML (eXtensible Markup Language):
    - **Struktur dan Tujuan**: 
    XML adalah bahasa markup yang digunakan untuk menyusun data dalam struktur hierarki yang dapat disesuaikan. XML tidak memiliki tujuan tertentu dan sering digunakan untuk pertukaran data antara aplikasi yang berbeda dan untuk menyimpan data konfigurasi.
    - **Notasi dan Struktur Data**:  
    XML menggunakan tag yang mendefinisikan struktur data. Ini dapat menggambarkan data yang sangat kompleks dengan baik, tetapi memiliki overhead dalam hal jumlah karakter yang digunakan.
    - **Tipe Data**: 
    Mendukung berbagai tipe data, termasuk teks, angka, tanggal, dan data yang kompleks. Anda dapat mendefinisikan tipe data kustom menggunakan DTD atau XML Schema.
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

<details>
<summary>
> 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
- Ringan dan Efisien karena memiliki format yang ringan dan *compact*
- Mudah dipahami oleh manusia karena menggunakan notasi objek dan array yang mirip seperti `JavaScript`
- Kompatibilitas dengan JavaScript
- Dukungan pada berbagai bahasa pemrograman
- Dapat *Cross-Platform* dengan banyak platform lain, hal ini membuat JSON sangat *Versatile*

</details>

<details>
<summary>
> 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

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





