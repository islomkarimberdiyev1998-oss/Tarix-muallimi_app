from qlib import Topic
TOPICS = {}
CA = 'ca'; FV = 'fargona'

# 18 Toshkentda «Vabo isyoni»
t = Topic('e9u18', 9018); TOPICS['e9u18'] = t
t.B("1892-yil mart oyida vabo kasalligi qayerda tarqalgan?", "Afg‘onistonda", "Eronda", "Hindistonda", "Rossiyada", "Afg‘onistonda.")
t.B("Vabo Toshkentda qachon qayd qilingan?", "1892-yil 7-iyunda", "1892-yil 24-iyunda", "1892-yil 18-iyunda", "1892-yil mart oyida", "7-iyunda.")
t.B("Toshkent ma’muriyati vaboga qarshi nechta qabristonni yopib qo‘ygan?", "12 ta", "4 ta", "1 ta", "20 ta", "Shahardagi 12 ta qabriston yopildi.")
t.B("Shifokorlar yetishmasligi sababli bemorlar odatda nechanchi kuni tekshirilgan?", "uchinchi yo to‘rtinchi kuni", "birinchi kuni", "bir haftadan keyin", "o‘sha kuni", "Ko‘pincha uchinchi yo to‘rtinchi kuni.")
t.B("«Harbiy holatda deb e’lon qilingan joylar haqida Qoida» qachon kuchga kirgan?", "1892-yil 18-iyundan", "1892-yil 24-iyundan", "1886-yil 12-iyuldan", "1881-yildan", "1892-yil 18-iyundan.")
t.B("Lavozimidan chetlashtirilgan Eski shaharning xalqparvar oqsoqoli kim?", "Inog‘om xo‘ja Umriyoxo‘jayev", "Muhammad Yoqub", "Hakim xo‘ja", "Solihbek dodxoh", "Inog‘om xo‘ja Umriyoxo‘jayev.")
t.B("«Vabo isyoni» yana qanday nom bilan atalgan?", "«Toshotar voqeasi»", "«Qonli yakshanba»", "«Mardikorlar qo‘zg‘oloni»", "«Dukchi eshon qo‘zg‘oloni»", "«Toshotar voqeasi».")
t.B("«Vabo isyoni» qachon boshlangan?", "1892-yil 24-iyunda", "1892-yil 7-iyunda", "1898-yil 17-mayda", "1892-yil 18-iyunda", "1892-yil 24-iyunda.")
t.B("Qo‘zg‘olonchilar asosan kimlardan iborat edi?", "mardikorlar va hunarmand-kosiblardan", "boylar va savdogarlardan", "amaldorlardan", "rus ko‘chmanchilaridan", "Mardikorlar va hunarmand-kosiblardan.")
t.B("Toshkent shahar boshlig‘i kim bo‘lgan?", "S. Putinsev", "N. Korolkov", "A. Vrevskiy", "S. Duxovskoy", "S. Putinsev.")
t.B("Olomon taxminan necha kishidan iborat bo‘lgan?", "400 kishi", "4000 kishi", "40 kishi", "20 ming kishi", "Taxminan 400 kishi, o‘qotar qurollarsiz.")
t.B("Olomondan qo‘rqib shahar boshlig‘i huzuriga borgan Eski shahar oqsoqoli kim?", "Muhammad Yoqub", "Inog‘om xo‘ja", "Abulqosim eshon", "Ziyovuddin maxsum", "Muhammad Yoqub.")
t.B("Qo‘zg‘olonni bostirish uchun kimlar chaqirilgan?", "kazaklar polki va bir rota askar", "Buxoro qo‘shini", "mirshablar", "Kavkaz armiyasi", "Kazaklar polki va bir rota askar.")
t.NAT("Yangi oqsoqol pora olish uchun boshqa kasallikdan vafot etganlarni ham vabo qabristoniga ko‘mishni buyurdi.", "xalqning keskin noroziligi qo‘zg‘olon boshlanishiga sabab bo‘ldi", "vabo to‘xtadi", "qabristonlar ochildi", "oqsoqol mukofotlandi", "Bu holat qo‘zg‘olon boshlanishiga sabab bo‘ldi.")
t.NAT("Putinsev muzokara o‘rniga kuch ishlatishni afzal ko‘rdi.", "xalq hokimga hujum qilib, uni kaltakladi va mahkamani ostin-ustun qildi", "xalq tarqalib ketdi", "oqsoqol xalqqa topshirildi", "vabo qabristoni yopildi", "Sabr kosasi to‘lgan xalq hokimga hujum qildi.")
t.NAT("Sankt-Peterburg general-gubernatorning iltimosini qondirdi.", "o‘lkada «mirshablik holati» joriy etildi", "politsiya qisqartirildi", "Toshkent mustaqil bo‘ldi", "qo‘zg‘olonchilar ozod qilindi", "«Mirshablik holati»ga ruxsat berildi.")
t.TF("Shahardan tashqarida vabodan vafot etganlar uchun faqat bitta qabriston ochilgan.", True, "To‘g‘ri.")
t.TF("Sanitariya tadbirlari xalqqa ishonarli qilib tushuntirilgan.", False, "Noto‘g‘ri: tadbirlar xalqqa ishonarli tushuntirilmagan.")
t.MUL([("«Kuchli muhofaza»dagi joylarda general-gubernator majlislarni tarqatish, matbuotni taqiqlash huquqini olgan.", True),
       ("«Favqulodda muhofaza»da butun hokimiyat general-gubernator yoki bosh noib qo‘liga o‘tgan.", True),
       ("Qo‘zg‘olonchilar zamonaviy o‘qotar qurollar bilan qurollangan.", False)],
      "III noto‘g‘ri: olomonda o‘qotar yoki zamonaviy qurollar yo‘q edi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Afg‘onistonda vabo tarqaldi", "Vabo Toshkentda qayd qilindi", "Harbiy holat haqidagi Qoida kuchga kirdi", "«Vabo isyoni» boshlandi"],
      "1892-yil mart → 7-iyun → 18-iyun → 24-iyun.")
t.MAPN(CA, ['Xiva', 'Jizzax', 'Toshkent', 'Qo‘qon'], "Qaysi raqam bilan 1892-yilda «Vabo isyoni» (Toshotar voqeasi) bo‘lgan shahar belgilangan?",
       "3 – Toshkent; 2 – Jizzax uyezdida ham vabo qayd qilingan.", ask_idx=2)
t.VENN("«Kuchli muhofaza» holati", "«Favqulodda muhofaza» holati",
       [("majlislarni tarqatish, matbuotni taqiqlash huquqi", 1), ("korxonalarni yopish, surgun qilish, jarima solish", 1),
        ("butun hokimiyat general-gubernator yoki bosh noib qo‘liga o‘tgan", 2),
        ("qo‘zg‘olondan keyin mustamlakachilarga keng vakolat bergan", 3)],
       "Kuchli muhofaza — taqiqlar, surgun; favqulodda — butun hokimiyat bosh noibga.")

# 19 Andijon qo‘zg‘oloni
t = Topic('e9u19', 9019); TOPICS['e9u19'] = t
t.B("1891-yilda Farg‘ona viloyatiga nima ko‘plab amalga oshirildi?", "Rossiyadan aholi ko‘chirib keltirildi", "temiryo‘l qurildi", "vaqf yerlari ko‘paydi", "yangi madrasalar ochildi", "Rossiyadan aholi ko‘plab ko‘chirib keltirildi.")
t.B("1898-yilgi Andijon qo‘zg‘oloniga kim rahbarlik qilgan?", "Dukchi eshon (Muhammad Ali)", "Darvishxon", "Yetimxon", "Po‘latxon", "Dukchi eshon nomini olgan Muhammad Ali.")
t.B("Dukchi eshon qaysi yillarda yashagan?", "1846–1898", "1809–1874", "1827–1897", "1778–1829", "1846–1898.")
t.B("Muhammad Ali qachon qo‘zg‘olon boshlash vaqti kelganini e’lon qilgan?", "1898-yil 17-mayda", "1898-yil 20-mayda", "1899-yil 20-iyunda", "1892-yil 24-iyunda", "1898-yil 17-mayda.")
t.B("Qo‘zg‘olon qaysi qishloqdagi telegraf simlarining qirqilishi bilan boshlangan?", "Tojikqishloq", "Qutchi", "Qo‘yli", "Mingtepa", "Tojikqishloqda.")
t.B("Qo‘zg‘olonchilar yo‘lda kimni o‘ldirgan?", "Asaka pristavini", "Konshevskiyni", "Putinsevni", "Korolkovni", "Asaka pristavini.")
t.B("Qo‘zg‘olonchilarning ikkinchi qismiga kim boshchilik qilgan?", "Ziyovuddin maxsum", "G‘oyibnazar", "Chibil bo‘lisi", "Muhammad Yoqub", "Ziyovuddin maxsum.")
t.B("Qo‘yli qishlog‘ida qo‘zg‘olonchilarga kim qo‘shilgan?", "mingboshi G‘oyibnazar", "Ziyovuddin maxsum", "Chibil bo‘lisi", "Konshevskiy", "Mingboshi G‘oyibnazar.")
t.B("Qo‘zg‘olonchilar Andijonda nimaga hujum qilgan?", "harbiy kazarmaga", "shahar dumasiga", "bankka", "temiryo‘l stansiyasiga", "Harbiy kazarmaga.")
t.B("Kazarma to‘qnashuvida harbiylardan nechtasi o‘ldirilgan?", "22 tasi", "11 tasi", "380 tasi", "8 tasi", "22 tasi o‘ldirildi, 22 tasi yarador.")
t.B("Andijon tumanboshisi kim edi?", "polkovnik Konshevskiy", "N. Korolkov", "S. Putinsev", "A. Vrevskiy", "Polkovnik Konshevskiy.")
t.B("Qo‘zg‘olondan keyin lavozimidan chetlatilgan Turkiston general-gubernatori kim?", "A. Vrevskiy", "S. Duxovskoy", "N. Korolkov", "K. Kaufman", "General-leytenant A. Vrevskiy.")
t.B("Jazo ekspeditsiyasiga kim rahbarlik qilgan?", "N. Korolkov", "A. Kuropatkin", "S. Duxovskoy", "Konshevskiy", "Sirdaryo viloyati harbiy gubernatori N. Korolkov.")
t.B("Qo‘zg‘olon bostirilgach necha kishi hibsga olingan?", "ikki ming kishi", "380 kishi", "22 kishi", "400 kishi", "Ikki ming kishi.")
t.B("Manbalarga ko‘ra jami necha kishi o‘lim jazosiga mahkum qilingan?", "380 kishi", "22 kishi", "2000 kishi", "11 kishi", "380 kishi; keyin 22 kishining jazosi kuchda qoldi.")
t.B("O‘lim jazosini ko‘paytirmaslik haqida telegramma yuborgan harbiy vazir kim?", "A. N. Kuropatkin", "N. Korolkov", "A. Vrevskiy", "Nikolay II", "Harbiy vazir A. N. Kuropatkin.")
t.B("Andijon qo‘zg‘olonidan bir yil o‘tib qachon Farg‘onada yangi qo‘zg‘olon boshlangan?", "1899-yil 20-iyunda", "1898-yil 20-mayda", "1900-yilda", "1916-yilda", "1899-yil 20-iyunda.")
t.NAT("Kuropatkin Duxovskoyga telegramma jo‘natdi.", "o‘lim jazosi katorga va qamoqqa almashtirildi, 22 kishiniki kuchda qoldi", "barcha qo‘zg‘olonchilar ozod qilindi", "o‘lim jazosi ko‘paytirildi", "Dukchi eshon afv etildi", "Jazolar katorga va qamoqqa almashtirildi.")
t.NAT("Chibil bo‘lisi Dukchi eshonga qo‘shilish o‘rniga atrofdagi mustamlakachilarga qarshi kurashdi.", "bu taktik xato qo‘zg‘olon mag‘lubiyatiga sabab bo‘ldi", "qo‘zg‘olon g‘alaba qozondi", "Andijon ozod bo‘ldi", "Korolkov chekindi", "Tarqoqlik mag‘lubiyat sabablaridan biri.")
t.TF("Qo‘zg‘olon ruslar yashaydigan Yangi shaharda vahima uyg‘otgan.", True, "To‘g‘ri.")
t.TF("Andijon qo‘zg‘oloni butun o‘lka bo‘ylab keng yoyilib, barcha tabaqalar qatnashgan.", False, "Noto‘g‘ri: keng yoyilmagani va barcha tabaqalar qatnashmagani mag‘lubiyat sababi bo‘ldi.")
t.MUL([("Qo‘zg‘olonga aniq reja ishlab chiqilmagan, hamma bir vaqtda ko‘tarilmagan.", True),
       ("Harbiy kuchlar uch soat ichida Andijonga yetib kelgan.", True),
       ("Korolkov Farg‘ona viloyat harbiy gubernatorini mukofotlagan.", False)],
      "III noto‘g‘ri: Korolkov 20-mayda uni lavozimidan bo‘shatgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Farg‘onaga Rossiyadan ko‘plab aholi ko‘chirildi", "Dukchi eshon qo‘zg‘olon boshlanganini e’lon qildi", "Korolkov amaldorlarni lavozimidan bo‘shatdi", "Farg‘ona vodiysida yangi qo‘zg‘olon boshlandi"],
      "1891 → 1898-yil 17-may → 1898-yil 20-may → 1899-yil 20-iyun.")
t.MAPN(FV, ['Namangan', 'Qo‘qon', 'Andijon', 'Marg‘ilon'], "Qaysi raqam bilan 1898-yilda Dukchi eshon qo‘zg‘olonchilari harbiy kazarmaga hujum qilgan shahar belgilangan?",
       "3 – Andijon.", ask_idx=2)
t.VENN("«Vabo isyoni» (1892)", "Andijon qo‘zg‘oloni (1898)",
       [("Toshkentda bo‘lgan", 1), ("shahar boshlig‘i Putinsev kaltaklangan", 1),
        ("Dukchi eshon rahbarlik qilgan", 2), ("harbiy kazarmaga hujum qilingan", 2),
        ("mustamlakachi hukumat tomonidan bostirilgan", 3)],
       "1892 — Toshkent, Putinsev; 1898 — Dukchi eshon, kazarma; ikkalasi bostirilgan.")
