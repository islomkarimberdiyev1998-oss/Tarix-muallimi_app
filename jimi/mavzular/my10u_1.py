from qlib import Topic, PLACES, REG
TOPICS = {}

# 1-mavzu. Bosqin arafasida xonliklar
t = Topic('y10u1', 10001); TOPICS['y10u1'] = t
t.B("XIX asr o‘rtalarida Buxoro amirligi tarkibida nechta viloyat bo‘lgan?", "40 ta", "18 ta", "12 ta", "4 ta", "40 ta viloyat.")
t.B("Buxoro amirligining aholisi qancha bo‘lgan?", "2 million atrofida", "3 millionga yaqin", "500 ming", "10 million", "2 million atrofida.")
t.B("Qo‘qon xonligi aholisi qancha bo‘lgan?", "3 millionga yaqin", "2 million", "1 million", "800 ming", "3 millionga yaqin.")
t.B("Xiva xonligi nechta beklik va noiblikka bo‘lingan?", "18 ta beklik, 2 ta noiblik", "40 ta viloyat", "4 ta daha", "12 ta beklik", "18 beklik va 2 noiblik.")
t.B("Buxoro amirligida ijro hokimiyati kimning qo‘lida bo‘lgan?", "qo‘shbegi (bosh vazir)", "devonbegi", "otaliq", "mirshabboshi", "Qo‘shbegi.")
t.B("Buxoro amirligida tashqi aloqalarni yuritish kimga yuklatilgan?", "devonbegi", "qo‘shbegi", "dodxoh", "ko‘kaldosh", "Devonbegiga.")
t.B("Buxoroda soliqlarni o‘z vaqtida yig‘ishga javobgar amaldor kim?", "mushrif", "mirzaboshi", "parvonachi", "to‘pchiboshi", "Mushrif.")
t.B("Buxoro amiri qo‘shinlarining bosh qo‘mondoni kim bo‘lgan?", "to‘pchiboshi", "otaliq", "yasovulboshi", "amirlashkar", "To‘pchiboshi.")
t.B("Buxoroda mamlakat xavfsizligi va ma’lumot to‘plash bilan kim shug‘ullangan?", "ko‘kaldosh", "dodxoh", "mushrif", "shayxulislom", "Ko‘kaldosh.")
t.B("Xiva xonligida oliy amaldor kim hisoblangan?", "devonbegi", "mehtar", "qo‘shbegi", "yasovulboshi", "Devonbegi.")
t.B("Xiva xon qo‘shinlarining bosh qo‘mondoni kim bo‘lgan?", "yasovulboshi", "to‘pchiboshi", "amirlashkar", "mingboshi", "Yasovulboshi.")
t.B("Xivada suv ta’minoti va taqsimotiga kim mas’ul bo‘lgan?", "mirobboshi", "mirshabboshi", "mehtar", "otaliq", "Mirobboshi.")
t.B("Qo‘qon xonligida eng yuqori harbiy lavozim qaysi?", "amirlashkar", "mingboshi", "to‘pchiboshi", "yasovulboshi", "Amirlashkar – harbiy vazir.")
t.B("Qo‘qon xonligida xazina ishlarini kim nazorat qilgan?", "mehtar", "qozikalon", "muhtasib", "mirshab", "Mehtar.")
t.B("Xiva xonligida asosiy soliq qanday atalgan?", "solg‘ut", "xiroj", "zakot", "tanob", "Solg‘ut.")
t.B("Rishton qaysi hunar bilan mashhur bo‘lgan?", "kulolchilik", "pichoqchilik", "atlas to‘qish", "ganchkorlik", "Kulolchilik.")
t.B("Madrasalarda o‘qish mavsumi ko‘pincha necha oy bo‘lgan?", "6 oy", "9 oy", "3 oy", "12 oy", "Sentyabr ikkinchi yarmidan mart oxirigacha, 6 oy.")
t.B("Maktabda o‘quvchilar «Haftiyak»dan so‘ng qaysi kitobni o‘qigan?", "«Chor kitob»", "«Boburnoma»", "«Xamsa»", "«Qutadg‘u bilig»", "«Chor kitob».")
t.NAT("Qo‘qon xonligining janubiy chegarasidagi Qorategin, Ko‘lob, Darvoz uchun da’volar bo‘ldi.", "bu hududlar uchun Buxoro amirligi bilan tez-tez to‘qnashuvlar bo‘ldi", "hududlar Xivaga berildi", "Rossiya bu hududlarni sotib oldi", "Qo‘qon bu hududlardan voz kechdi", "Buxoro bilan to‘qnashuvlar.")
t.NAT("Xonliklarda temir mahsulotlariga ehtiyoj katta edi.", "mahalliy temirchilik sohasi rivojlandi", "temir chetdan olib kelinmadi", "temirchilik taqiqlandi", "temir narxi tushdi", "Temirchilik rivojlandi.")
t.NAT("Ingliz tovarlari O‘rta Osiyoga kirib keldi, Angliyaning qiziqishi ortdi.", "Rossiya hukumatining istilochilik harakatlari tezlashdi", "Rossiya mintaqadan voz kechdi", "xonliklar Angliyaga qo‘shildi", "savdo to‘xtadi", "Istilo tezlashdi.")
t.NAT("Domlaning ayoli ichkari hovlida xotin-qizlarga xat-savod o‘rgatdi.", "ta’lim yangiliklari xotin-qizlarga ham yetib bordi", "qizlar ta’limdan mahrum bo‘ldi", "maktablar yopildi", "domla ishdan bo‘shatildi", "Xotin-qizlar savodxonligi.")
t.TF("Xiva xonligida askarlik xizmatida bo‘lganlar soliqlardan ozod qilingan.", True, "To‘g‘ri.")
t.TF("Uchala xonlik aholisining asosiy qismi tojiklardan iborat bo‘lgan.", False, "Noto‘g‘ri: asosan o‘zbeklardan iborat bo‘lgan.")
t.TF4([("Buxoro amirligi Zarafshon vodiysi markaziy qism hisoblangan.", True), ("Qo‘qon xonligini minglar sulolasi boshqargan.", True),
       ("Madrasaga 10 yoshdan 40 yoshgacha talabalar qabul qilingan.", True), ("Xiva xonligini mang‘itlar sulolasi boshqargan.", False)],
      "4-noto‘g‘ri: Xivani qo‘ng‘irotlar sulolasi boshqargan.")
t.MUL([("Marg‘ilon atlas to‘qish va do‘ppichilik bilan mashhur bo‘lgan.", True),
       ("Madrasa va maktablar vaqf mulkidan moliyalashtirilgan.", True),
       ("Buxoroda viloyat beklari xalq tomonidan saylangan.", False)],
      "III noto‘g‘ri: amir tomonidan, qo‘shbegi tavsiyasi bilan tayinlangan.")
t.CHR("Maktab va madrasa ta’limi bosqichlarini tartiblang.", ["«Haftiyak»ni o‘qish", "«Chor kitob»ni o‘qish", "maktabni tugatish", "madrasaga qabul qilinish"],
      "Haftiyak → Chor kitob → maktabni tugatish → madrasa.")
t.MATCH("Buxoro amirligi lavozimlarini vazifasi bilan moslashtiring.", ["qo‘shbegi", "dodxoh", "parvonachi", "mirshabboshi"],
        ["bosh vazir, ijro hokimiyati", "xalq shikoyatlari bilan shug‘ullangan", "hukmdor farmonlarini e’lon qilgan", "shaharlarda tinchlik va tartib", "valiahd tarbiyasi"], 'abcd',
        "Qo‘shbegi – bosh vazir; dodxoh – shikoyatlar; parvonachi – farmonlar; mirshabboshi – tartib.")
t.VENN("Buxoro amirligi", "Xiva xonligi",
       [("40 ta viloyat, mang‘itlar", 1), ("to‘pchiboshi – bosh qo‘mondon", 1),
        ("18 beklik, qo‘ng‘irotlar", 2), ("asosiy soliq – solg‘ut", 2),
        ("devonbegi lavozimi bo‘lgan", 3)],
       "Buxoro – 40 viloyat, to‘pchiboshi; Xiva – 18 beklik, solg‘ut; ikkalasida devonbegi.")
t.MAPMATCH('uzb', ['Buxoro', 'Xiva', 'Qo‘qon', 'Samarqand'],
           ["mang‘itlar boshqargan amirlik markazi", "qo‘ng‘irotlar boshqargan xonlik markazi", "minglar boshqargan xonlik markazi", "Zarafshon vodiysidagi, zargarlik rivojlangan amirlik shahri"],
           "1 – Buxoro; 2 – Xiva; 3 – Qo‘qon; 4 – Samarqand.")

# 2-mavzu. Rossiya imperiyasining yurishi va Turkiston general-gubernatorligi
t = Topic('y10u2', 10002); TOPICS['y10u2'] = t
t.B("Qo‘qon xonligini bosib olishni davom ettirish haqida 1859-yilda ko‘rsatma bergan imperator kim?", "Aleksandr II", "Nikolay I", "Pyotr I", "Aleksandr III", "Aleksandr II.")
t.B("Toshkentni bosib olishda qaysi qal’a harbiy harakatlarning tayanchiga aylandi?", "Oqmachit", "Niyozbek", "Chimkent", "Avliyoota", "Oqmachit qal’asi.")
t.B("Oqmachitni egallash uchun ikkinchi hujum qachon boshlangan?", "1853-yilda", "1852-yilda", "1864-yilda", "1865-yilda", "1853-yilda.")
t.B("Oqmachit qal’asining nechta himoyachisi bo‘lgan?", "400 kishi", "3000 kishi", "40 kishi", "4000 kishi", "400 kishi 20 kun qarshilik ko‘rsatgan.")
t.B("Oqmachit egallangach unga qanday nom berilgan?", "Perovskiy forti", "Verniy", "Raim", "Kaufman forti", "Perovskiy forti.")
t.B("1864-yilda Talas daryosi bo‘yida bosib olingan shahar qaysi?", "Avliyoota", "Turkiston", "Chimkent", "Xo‘jand", "Avliyoota (hozirgi Taroz).")
t.B("Turkiston va Chimkent mudofaasiga kim rahbarlik qilgan?", "amirlashkar Aliquli", "Chernyayev", "Hakimxo‘ja", "Solihbek dodxoh", "Amirlashkar Aliquli (Alimqul).")
t.B("Toshkentni bosib olishga kim qo‘mondon etib tayinlangan?", "M. Chernyayev", "K. Kaufman", "V. Perovskiy", "Skobelev", "M. Chernyayev.")
t.B("Toshkent shahri qal’a devorining uzunligi qancha bo‘lgan?", "20 kilometr", "6 kilometr", "12 kilometr", "50 kilometr", "20 km.")
t.B("XIX asr ikkinchi yarmida Toshkentning nechta darvozasi bo‘lgan?", "12 ta", "6 ta", "4 ta", "8 ta", "12 ta darvoza.")
t.B("Toshkent nechta dahaga bo‘lingan?", "to‘rtta", "oltita", "o‘n ikkita", "ikkita", "Beshyog‘och, Ko‘kcha, Sebzor, Shayxontohur.")
t.B("Toshkent mudofaa xandaqlari qaysi ariq suvi bilan to‘ldirilgan?", "Kaykovus", "Bo‘zsuv", "Anhor", "Salor", "Kaykovus arig‘i.")
t.B("Chirchiq daryosi chap sohilidagi qaysi qal’a egallanib, Toshkent suvdan uzib qo‘yilgan?", "Niyozbek", "Oqmachit", "Raim", "Chinoz", "Niyozbek qal’asi.")
t.B("Toshkent qachon egallangan?", "1865-yil iyunda", "1864-yil oktyabrda", "1867-yilda", "1853-yilda", "1865-yil iyunda.")
t.B("Sulhga qarshi bo‘lgani uchun Sibirga surgun qilinganlardan biri kim?", "Solihbek dodxoh", "Aliquli", "Chernyayev", "Kaufman", "Solihbek dodxoh, Abulqosim eshon, Hakimxo‘ja.")
t.B("Turkiston general-gubernatorligi qachon tashkil qilingan?", "1867-yilda", "1865-yilda", "1864-yilda", "1876-yilda", "1867-yilda.")
t.B("Turkistonning birinchi general-gubernatori kim?", "fon Kaufman", "Chernyayev", "Perovskiy", "Skobelev", "General fon Kaufman.")
t.B("Dastlab Yettisuv viloyatining markazi qaysi shahar bo‘lgan?", "Verniy", "Toshkent", "Avliyoota", "Semipalatinsk", "Verniy (Almati).")
t.NAT("1864-yil 1-oktyabrda Chernyayev Toshkentni tezlik bilan olmoqchi bo‘ldi.", "shahar himoyachilari uni Chimkentga chekinishga majbur qildi", "Toshkent darhol taslim bo‘ldi", "Chernyayev halok bo‘ldi", "Buxoro Toshkentni egalladi", "Hujum qaytarildi.")
t.NAT("Niyozbek qal’asi bosib olinib, Chirchiqdagi to‘g‘on buzildi.", "Toshkent shahri suvsiz qoldi", "Toshkent suv bilan to‘ldi", "Chirchiq quridi", "shahar taslim bo‘lishdan bosh tortmadi va g‘alaba qozondi", "Shahar suvdan uzildi.")
t.NAT("Toshkent mudofaasida amirlashkar Aliquli halok bo‘ldi.", "shahar himoyachilari sarosimaga tushdi", "himoyachilar kuchaydi", "Buxoro qo‘shini g‘alaba qildi", "Chernyayev chekindi", "Sarosima boshlandi.")
t.NAT("Orenburg general-gubernatorligi O‘rta Osiyodan uzoqda edi, boshqaruvda qiyinchiliklar tug‘ildi.", "1867-yilda Turkiston general-gubernatorligi tashkil qilindi", "Orenburg Toshkentga ko‘chirildi", "hududlar xonlarga qaytarildi", "boshqaruv Buxoroga berildi", "Alohida general-gubernatorlik tuzildi.")
t.TF("Toshkent general-gubernatorlikning markazi qilib belgilangan.", True, "To‘g‘ri.")
t.TF("Buxoro amirligi qo‘shinlari Toshkent himoyasiga o‘z vaqtida yetib kelib, shaharni saqlab qolgan.", False, "Noto‘g‘ri: kechikib kelgan, foydasi tegmagan.")
t.TF4([("Oqmachitni egallashga 1852-yilgi urinish mag‘lubiyatga uchragan.", True), ("Kaufman bir vaqtda Turkiston harbiy okrugi qo‘mondoni bo‘lgan.", True),
       ("Asosiy jang Kamolon darvozasidan markaziy bozorga boruvchi ko‘chada bo‘lgan.", True), ("Turkiston general-gubernatorligi dastlab beshta viloyatga bo‘lingan.", False)],
      "4-noto‘g‘ri: dastlab ikkita – Sirdaryo va Yettisuv viloyatiga bo‘lingan.")
t.MUL([("1865-yilda Turkiston viloyati tuzilib, Chernyayev gubernator bo‘lgan.", True),
       ("Toshkent oqsoqollari shaharni «ixtiyoriy topshirish» sulhini imzolashga majbur qilingan.", True),
       ("Sirdaryo viloyatining markazi Verniy bo‘lgan.", False)],
      "III noto‘g‘ri: Sirdaryo viloyati markazi – Toshkent.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Oqmachitga birinchi hujum", "Oqmachit egallandi", "Aleksandr II ko‘rsatmasi", "Chimkent egallandi", "Toshkent egallandi", "Turkiston general-gubernatorligi tuzildi"],
      "1852 → 1853 → 1859 → 1864 → 1865 → 1867.")
t.MATCH("Shaxslarni ular haqidagi ma’lumot bilan moslashtiring.", ["Aliquli", "M. Chernyayev", "fon Kaufman", "Solihbek dodxoh"],
        ["Qo‘qon xonining amirlashkari", "Toshkentni bosib olgan qo‘mondon", "birinchi general-gubernator", "Sibirga surgun qilingan Toshkent himoyachisi", "Buxoro amiri"], 'abcd',
        "Aliquli – amirlashkar; Chernyayev – Toshkent; Kaufman – general-gubernator; Solihbek – surgun.")
t.VENN("Sirdaryo viloyati", "Yettisuv viloyati",
       [("markazi Toshkent", 1), ("Turkiston viloyati yerlari kirgan", 1),
        ("markazi Verniy", 2), ("Sergiopol, Kopal okruglari kirgan", 2),
        ("Turkiston general-gubernatorligi tarkibida", 3)],
       "Sirdaryo – Toshkent; Yettisuv – Verniy; ikkalasi general-gubernatorlik tarkibida.")
t.MAPMATCH('syr', ['Oqmachit', 'Turkiston', 'Toshkent', 'Verniy (Almati)'],
           ["1853-yilda egallanib Perovskiy forti deb atalgan qal’a", "Aliquli himoya qilgan, imperiya qo‘shini ishg‘ol qilgan shahar", "1865-yil iyunda egallangan, general-gubernatorlik markazi", "Yettisuv viloyati markazi"],
           "1 – Oqmachit; 2 – Turkiston; 3 – Toshkent; 4 – Verniy.")
