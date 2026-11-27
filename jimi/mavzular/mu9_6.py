from qlib import Topic
TOPICS = {}
CA = 'ca'; FV = 'fargona'

# 12 Qo‘qon xonligining bosib olinishi
t = Topic('e9u12', 9012); TOPICS['e9u12'] = t
t.B("Kaufman Qo‘qon xoni bilan qachon shartnoma tuzgan?", "1868-yilda", "1875-yilda", "1873-yilda", "1876-yilda", "1868-yilda; Rossiya savdogarlariga katta imkoniyatlar berildi.")
t.B("1875-yilgi qo‘zg‘olonga kim «Po‘latxon» nomi bilan rahbarlik qilgan?", "Mulla Is’hoq Mullo Hasan o‘g‘li", "Abdurahmon Oftobachi", "Iso Avliyo", "Nasriddinbek", "Mulla Is’hoq Mullo Hasan o‘g‘li.")
t.B("Xudoyorxon qo‘zg‘olonni bostirish uchun kimlar boshchiligida qo‘shin yuborgan?", "Abdurahmon Oftobachi va Iso Avliyo", "Skobelev va Kaufman", "Jo‘rabek va Bobobek", "Nasriddinbek va Po‘latxon", "Ular 17-iyulda qo‘zg‘olonchilar tomoniga o‘tib ketdi.")
t.B("Xudoyorxon qachon Kaufmandan yordam so‘rashga majbur bo‘lgan?", "1875-yil 20-iyulda", "1875-yil 17-iyulda", "1875-yil 22-sentabrda", "1876-yil 19-fevralda", "20-iyulda.")
t.B("Kaufman Xudoyorxonni qayerga jo‘natgan?", "Orenburgga", "Peterburgga", "Sibirga", "Makkaga", "Orenburgga.")
t.B("Xudoyorxon qayerda vafot etgan?", "Afg‘onistonda", "Orenburgda", "Makkada", "Hindistonda", "1882-yilda Afg‘onistonda.")
t.B("Xudoyorxondan so‘ng taxtga kim o‘tirgan?", "Nasriddinbek", "Po‘latxon", "Abdurahmon Oftobachi", "Muhammad Alixon", "Uning o‘g‘li Nasriddinbek.")
t.B("Nasriddinbek qachon taslim bo‘lib, Kaufman bilan shartnoma imzolagan?", "1875-yil 22-sentabrda", "1875-yil 20-iyulda", "1876-yil 19-fevralda", "1875-yil 18-oktabrda", "1875-yil 22-sentabrda.")
t.B("Nasriddinbek shartnomasiga ko‘ra qancha tovon to‘lanishi kerak edi?", "ikki million rubl", "500 ming rubl", "100 ming rubl", "2 mln 200 ming rubl", "Ikki million rubl.")
t.B("Shartnomaga ko‘ra Rossiyaga o‘tgan Namangan va Chust yerlarida qanday bo‘lim tuzilgan?", "Namangan bo‘limi", "Amudaryo bo‘limi", "Zarafshon okrugi", "Farg‘ona viloyati", "Namangan bo‘limi, boshlig‘i M. Skobelev.")
t.B("Andijonga hujumga kim boshchilik qilgan?", "general M. Skobelev", "K. Kaufman", "I. Lazerev", "N. Veryovkin", "General M. Skobelev.")
t.B("Andijon qachon qiyinchilik bilan egallangan?", "1876-yil yanvarda", "1875-yil oktabrda", "1876-yil 19-fevralda", "1875-yil 22-sentabrda", "1876-yil yanvarda uyushtirilgan ikkinchi hujumda.")
t.B("Skobelev qo‘shinlari Namanganga qachon joylashgan?", "1875-yil 18-oktabrda", "1876-yil yanvarda", "1875-yil 20-iyulda", "1876-yil 19-fevralda", "1875-yil 18-oktabrda.")
t.B("Qo‘qon xonligining tugatilganligi to‘g‘risidagi farmon qachon e’lon qilingan?", "1876-yil 19-fevralda", "1875-yil 22-sentabrda", "1876-yil yanvarda", "1877-yilda", "1876-yil 19-fevralda.")
t.B("Farg‘ona viloyatiga kim harbiy gubernator etib tayinlangan?", "M. Skobelev", "K. Kaufman", "I. Lazerev", "F. Romanovskiy", "General M. Skobelev.")
t.B("Turkmanlarga qarshi 1879-yil iyulda Krasnovodskdan kim boshchiligida qo‘shin jo‘natilgan?", "I. Lazerev", "M. Skobelev", "K. Kaufman", "V. Perovskiy", "I. Lazerev.")
t.B("Turkmanlarning qaysi qal’asi 1881-yilda uch oylik janglardan so‘ng qo‘lga olingan?", "Go‘ktepa", "Marv", "Ashxobod", "Krasnovodsk", "Go‘ktepa.")
t.NAT("Nasriddinbek imzolagan shartnomadan aholi norozi bo‘lib, yana qo‘zg‘olon ko‘tardi.", "Po‘latxon Nasriddinbekni siqib chiqarib, hokimiyatni qo‘lga oldi", "Xudoyorxon taxtga qaytdi", "qo‘zg‘olon tezda tinchidi", "xonlik mustaqil bo‘ldi", "Po‘latxon tarafdorlari ko‘payib, u hokimiyatni egalladi.")
t.NAT("1879-yil iyulda Angliya Afg‘oniston hududining bir qismini bosib oldi.", "Rossiya turkmanlar yerlariga qo‘shin jo‘natdi", "Rossiya O‘rta Osiyodan chiqib ketdi", "Buxoro mustaqil bo‘ldi", "Xiva xonligi tugatildi", "Inglizlar uchun yo‘l ochilgani sabab Lazerev qo‘shini jo‘natildi.")
t.TF("Qo‘qon xonligi Buxoro va Xivadan farqli ravishda davlat sifatida butunlay tugatilgan.", True, "To‘g‘ri.")
t.TF("Turkmanlar 1881-yilda Go‘ktepa olinishi bilan batamom bo‘ysundirilgan.", False, "Noto‘g‘ri: batamom bo‘ysundirish 1885-yilda amalga oshirildi.")
t.MUL([("Mag‘lubiyat sabablaridan biri — uch davlat o‘rtasida do‘stona munosabat va birdamlik yo‘qligi.", True),
       ("Urush vaqtida xonlar bir-biriga yordam ko‘rsatmay, befarq qarab turgan.", True),
       ("Xonliklar harbiy jihatdan Rossiyadan ustun bo‘lgan.", False)],
      "III noto‘g‘ri: ular harbiy va iqtisodiy jihatdan ancha orqada edi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Abdurahmon Oftobachi qo‘zg‘olonchilarga o‘tdi", "Nasriddinbek Kaufman bilan shartnoma imzoladi", "Skobelev Namanganga joylashdi", "Qo‘qon xonligini tugatish farmoni", "Go‘ktepa qo‘lga olindi"],
      "1875-yil 17-iyul → 22-sentabr → 18-oktabr → 1876-yil 19-fevral → 1881.")
t.MAPMATCH(FV, ['Qo‘qon', 'Andijon', 'Namangan', 'Chust'],
           ["Xudoyorxon hukmronlik qilgan xonlik poytaxti", "qo‘zg‘olonchilarning asosiy kuchlari joylashgan, 1876-yil yanvarda egallangan shahar", "1875-yil 18-oktabrda Skobelev qo‘shinlari joylashgan shahar", "Namangan bilan birga 1875-yilgi shartnoma bo‘yicha Rossiyaga o‘tgan yer"],
           "1 – Qo‘qon; 2 – Andijon; 3 – Namangan; 4 – Chust.")
t.VENN("Xudoyorxon", "Po‘latxon",
       [("Kaufmandan yordam so‘ragan", 1), ("1882-yilda Afg‘onistonda vafot etgan", 1),
        ("asl ismi Mulla Is’hoq", 2), ("qatl qilingan", 2),
        ("Qo‘qon xonligida hokimiyatni boshqargan", 3)],
       "Xudoyorxon — Kaufmandan yordam, Afg‘onistonda vafot; Po‘latxon — Mulla Is’hoq, qatl qilingan.")

# 13 Turkiston general-gubernatorligining boshqaruv tizimi
t = Topic('e9u13', 9013); TOPICS['e9u13'] = t
t.B("«Turkiston o‘lkasi ... alohida e’tibor berilishini talab qiladi» degan general-gubernator kim?", "S. M. Duxovskoy", "K. P. Kaufman", "K. Palen", "M. Skobelev", "S. M. Duxovskoy (1898–1901).")
t.B("1865-yilgi Muvaqqat Nizomdagi boshqaruv tizimi qanday nomlangan?", "«Harbiy-xalq boshqaruvi»", "«Fuqarolik boshqaruvi»", "«Shahar nizomi»", "«Duma boshqaruvi»", "«Harbiy-xalq boshqaruvi».")
t.B("1908–1910-yillarda Turkistonni taftish qilgan senator kim?", "K. Palen", "S. Duxovskoy", "K. Kaufman", "I. Lazerev", "Senator K. Palen.")
t.B("Mahalliy aholi vakillariga boshqaruvning qaysi bosqichidagi lavozimlar berilgan?", "eng quyi bosqichidagi", "eng yuqori bosqichidagi", "viloyat darajasidagi", "uyezd darajasidagi", "Volost boshliqlari, qishloq oqsoqollari, ovul boshliqlari, qozi, biy.")
t.B("Katta vakolatlarga ega asosiy ijrochi organ nima edi?", "general-gubernatorlik devoni", "shahar dumasi", "volost", "uchastka", "General-gubernatorlik devoni.")
t.B("Viloyatlar qanday birliklarga bo‘lingan?", "uyezdlarga", "beklik va tumanlarga", "okruglarga", "gubernalarga", "Viloyatlar uyezdlarga bo‘lingan.")
t.B("Uchastkalarni kim boshqargan?", "uchastka pristavlari", "mingboshilar", "oqsoqollar", "biylar", "Uchastka pristavlari.")
t.B("Har bir oqsoqollik necha xonadondan iborat bo‘lishi belgilangan?", "100–200 xonadon", "1000–2000 xonadon", "10–20 xonadon", "500 xonadon", "100–200 xonadon.")
t.B("Har bir volost necha o‘tovdan iborat bo‘lishi belgilangan?", "1000–2000 o‘tov", "100–200 o‘tov", "50 o‘tov", "5000 o‘tov", "1000–2000 o‘tov.")
t.B("Toshkentda «Shahar nizomi» qachon joriy etilgan?", "1877-yilda", "1867-yilda", "1886-yilda", "1865-yilda", "1877-yilda; boshqaruv Dumaga o‘tdi.")
t.B("Toshkent shahar dumasida 80 ming mahalliy aholidan nechta deputat bo‘lgan?", "21 ta", "48 ta", "69 ta", "10 ta", "21 ta; 3900 nafar asosan rus aholisidan 48 ta.")
t.B("1886-yilgi Nizomni qaysi imperator tasdiqlagan?", "Aleksandr III", "Aleksandr II", "Nikolay II", "Pyotr I", "1886-yil 12-iyulda Aleksandr III.")
t.B("1886-yilgi Nizomga ko‘ra Zarafshon okrugi nimaga aylantirildi?", "Samarqand viloyatiga", "Farg‘ona viloyatiga", "Sirdaryo viloyatiga", "Amudaryo bo‘limiga", "Samarqand viloyatiga.")
t.B("Qurama uyezdining nomi qanday o‘zgartirildi?", "Toshkent uyezdi", "Jizzax uyezdi", "Xo‘jand uyezdi", "Chimkent uyezdi", "Toshkent uyezdi.")
t.B("1886-yilda Turkiston general-gubernatorligi aholisi qancha bo‘lgan?", "5,2 million kishi", "1,7 million kishi", "400 ming kishi", "80 ming kishi", "Hududi 1,7 mln kv. km, aholisi 5,2 mln.")
t.B("Buxoroda Rossiya imperatorining siyosiy agentligi qachon faoliyat boshlagan?", "1885-yilda", "1873-yilda", "1868-yilda", "1886-yilda", "1885-yilda.")
t.NAT("Dastlab mahalliy aholi ichki hayotiga keskin aralashish salbiy oqibatlarga olib kelishi mumkin edi.", "mahalliy aholidan iborat quyi boshqaruv va soliq tizimi saqlab qolindi", "barcha lavozimlar ruslarga berildi", "boshqaruv butunlay bekor qilindi", "xonliklar tiklandi", "Shu sababli quyi boshqaruv saqlab qolingan.")
t.NAT("Imperiyaning markaziy rayonlaridan aholi ko‘chirib keltirildi.", "mustamlakachilik uchun tayanch kuchlar paydo bo‘ldi, ruslashtirish imkoniyati kengaydi", "mahalliy aholi soni kamaydi", "Turkiston mustaqil bo‘ldi", "harbiy boshqaruv bekor qilindi", "Ko‘chirilganlar mustamlaka siyosatiga tayanch bo‘ldi.")
t.TF("Shahar dumasiga rahbarlik qiluvchi shaxsni harbiy vazir tasdiqlagan.", True, "To‘g‘ri: general-gubernator tavsiyasi bilan harbiy vazir tasdiqlagan.")
t.TF("Duma a’zolarining 2/3 qismi Eski shahar qismidan saylangan.", False, "Noto‘g‘ri: 1/3 qismi Eski shahardan, 2/3 qismi Yangi shahardan.")
t.MUL([("O‘troq aholi bir bosqichli tizim — oqsoqolliklarga birlashtirilgan.", True),
       ("Chorvador aholi ikki bosqichli tizim — volost va ovullarga birlashtirilgan.", True),
       ("Uyezdlarni mahalliy aholi vakillari boshqargan.", False)],
      "III noto‘g‘ri: uyezdlar harbiy zobitlar boshqaruvida bo‘lgan.")
t.CHR("Hujjat va voqealarni xronologik tartibda joylashtiring.", ["«Muvaqqat Nizom»", "«Shahar nizomi»", "Buxoroda siyosiy agentlik", "«Turkiston o‘lkasini idora qilish to‘g‘risidagi Nizom»", "Palen taftishi"],
      "1865 → 1877 → 1885 → 1886 → 1908–1910.")
t.VENN("1865-yilgi Muvaqqat Nizom", "1886-yilgi Nizom",
       [("Aleksandr II tasdiqlagan", 1), ("«Harbiy-xalq boshqaruvi» joriy etilgan", 1),
        ("Aleksandr III tasdiqlagan", 2), ("Zarafshon okrugi Samarqand viloyatiga aylantirilgan", 2),
        ("mustamlaka boshqaruvini mustahkamlashga qaratilgan", 3)],
       "1865 — Aleksandr II, harbiy-xalq boshqaruvi; 1886 — Aleksandr III, Samarqand viloyati.")
