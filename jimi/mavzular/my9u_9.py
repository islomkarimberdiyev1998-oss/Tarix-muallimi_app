from qlib import Topic, PLACES, REG
TOPICS = {}

# 16-§ Mang‘itlar davrida ilm-fan va madaniyat
t = Topic('y9u16', 9016); TOPICS['y9u16'] = t
t.B("Mang‘itlar davrida ta’lim saviyasi ortda qolishining sababi nima edi?", "jahonda erishilgan marralardan xabarsizlik", "madrasalarning yopilishi", "urushlar", "kitoblar yo‘qligi", "Jahondagi yutuqlardan xabarsizlik.")
t.B("XIX asrning birinchi yarmida Buxoroda nechta masjid faoliyat ko‘rsatgan?", "360 ta", "36 ta", "1000 ta", "100 ta", "Ko‘chalar soniga mos – 360 ta.")
t.B("A. Byorns Buxoroda nechta madrasa borligini ko‘rsatgan?", "366 ta", "360 ta", "80 ta", "24 ta", "366 ta «katta va kichik» madrasa.")
t.B("Amir Shohmurod qaysi yillarda hukmronlik qilgan?", "1785–1800", "1800–1826", "1756–1785", "1826–1860", "1785–1800.")
t.B("Amir Haydar qaysi yillarda hukmronlik qilgan?", "1800–1826", "1785–1800", "1747–1756", "1842–1860", "1800–1826.")
t.B("Shohmurod xalq orasida qanday nom bilan tanilgan?", "«Amiri Jannatmakon»", "«Amiri Kabir»", "«Shohbaxt»", "«Nishoniy»", "«Amiri Jannatmakon».")
t.B("Shohmurod Samarqandda nechta mavze qurdirgan?", "24 ta", "12 ta", "6 ta", "360 ta", "24 ta mavze.")
t.B("Muhammad Sharif Buxoriyning qaysi asariga sharhlar yozilgan?", "«Mizan at-tibb»", "«Ihyo at-tibbi Subhoniy»", "«Tuhfat al-xoniy»", "«Dastur al-iloj»", "«Mizan at-tibb».")
t.B("Xalifa Xudoydod asli qayerlik bo‘lgan?", "Xorazm shahzodalaridan", "Samarqandlik", "Qarshilik", "Hirotlik", "Xorazm shahzodalaridan.")
t.B("Xalifa Xudoydod qaysi madrasada ta’lim olgan?", "Mir Arab", "Ulug‘bek", "Ko‘kaldosh", "Abdulazizxon", "Mir Arab madrasasida.")
t.B("Xalifa Xudoydod majmuasida nechta bir qavatli hujra qurilgan?", "39 ta", "114 ta", "24 ta", "6 ta", "39 ta.")
t.B("Xalifa Xudoydod madrasasida nechta talaba tahsil olgan?", "150–200", "20–30", "1000", "50", "150–200 talaba.")
t.B("Samarqanddagi olti qirrali Chorsu o‘sha davrda qanday nom olgan?", "Toqi musaddas", "Toqi Zargaron", "Tim", "Toqi Sarrofon", "Toqi musaddas.")
t.B("Chorsu yo‘laklarining 6 ta bo‘lishi nimaga ishora?", "shahar darvozalari soniga", "Registon madrasalariga", "hafta kunlariga", "amirlar soniga", "Shahar darvozalari soniga.")
t.B("«Chorsu» so‘zi fors tilidan qanday tarjima qilinadi?", "to‘rtta yo‘l", "to‘rt minora", "qumloq joy", "yopiq bozor", "«To‘rtta yo‘l».")
t.B("«Registon» so‘zining ma’nosi nima?", "qumloq joy", "to‘rt yo‘l", "shoh maydoni", "bozor", "«Qumloq joy».")
t.B("Usti yopiq bozor qanday ataladi?", "tim", "chorsu", "registon", "sardoba", "Tim.")
t.B("Chor Minor qachon qurilgan?", "1807-yilda", "1786-yilda", "1785-yilda", "1826-yilda", "1807-yilda.")
t.B("Chor Minor yana qanday nom bilan mashhur?", "Xalifa Niyoz madrasasi", "Xalifa Xudoydod madrasasi", "Bolohovuz", "Havzi Nav", "Xalifa Niyoz madrasasi.")
t.B("Chor Minor darvozaxonasining ikkinchi qavatida nima joylashgan?", "kutubxona", "masjid", "sardoba", "hujra", "Kutubxona.")
t.B("Chor Minor YUNESKO ro‘yxatiga qachon kiritilgan?", "1995-yilda", "2001-yilda", "1991-yilda", "2010-yilda", "1995-yilda.")
t.B("Qarshida qaysi madrasa «sut sotuvchi ayol Gulining mablag‘iga» qurilgan deb qayd etiladi?", "Amir Haydar davridagi madrasa", "Mir Arab", "Chor Minor", "Ko‘kaldosh", "Amir Haydar davrida qurilgan madrasa.")
t.NAT("Shohmurod Samarqandda 24 mavze qurdirib, sharqiy viloyatlardan oilalarni ko‘chirib keltirdi.", "shahar gavjumlashib, iqtisodiy va madaniy ahvol yaxshilandi", "Samarqand qishloqqa aylandi", "aholi Buxoroga ko‘chdi", "Samarqand vayron bo‘ldi", "Samarqand tiklandi.")
t.NAT("Sobiq Ittifoq davrida Chor Minordagi masjid tuz omborxonasi bo‘ldi.", "masjid yaroqsiz holga kelib, buzib tashlandi", "masjid ta’mirlandi", "masjid muzeyga aylandi", "masjid kengaytirildi", "Masjid buzildi.")
t.NAT("Byorns yozishicha talabalar 7–8 yillik kursni tugatdi.", "ular o‘z vatanlariga bilim zaxirasi va mashhurlik bilan qaytgan", "Buxoroda qolib ketgan", "Eronga ketgan", "o‘qishni tashlagan", "Bilim bilan qaytgan.")
t.NAT("Xalifa Xudoydod har bir bino uchun alohida vaqf ta’sis etdi.", "majmua binolari mustaqil ta’minlandi", "binolar sotib yuborildi", "majmua yopildi", "vaqflar bekor qilindi", "Binolar ta’minoti kafolatlangan.")
t.TF("Samarqanddagi Chorsu Registonning janubi-sharqida joylashgan.", True, "To‘g‘ri.")
t.TF("Mang‘itlar davrida madrasalar ta’lim saviyasi jahon darajasida bo‘lgan.", False, "Noto‘g‘ri: ta’lim saviyasi tobora ortda qolgan.")
t.TF4([("Shohmurod Mir Arab madrasasi hujrasida ilm olish bilan shug‘ullangan.", True), ("Chorsu o‘rnida dastlab XV asrda bozor bo‘lgan.", True),
       ("Chor Minor minoralari tepasi to‘rtburchak shaklda yakunlangan.", False), ("Shohmurod Samarqandni qayta qurish tarhini o‘zi chizgan.", True)],
      "3-noto‘g‘ri: minoralar tepasi gumbaz shaklida.")
t.MUL([("«Tuhfat al-xoniy» va «Tarixi amir Haydar» mang‘itlar davri tarixiy asarlari.", True),
       ("Havzi Nav ansamblini Abdulazizxon barpo ettirgan.", True),
       ("Chorsu binosi hozir faqat masjid sifatida foydalaniladi.", False)],
      "III noto‘g‘ri: hozir muzey va galereya sifatida ishlaydi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Shohmurod hukmronligi boshlandi", "Amir Haydar hukmronligi boshlandi", "Chor Minor qurildi", "Amir Haydar hukmronligi tugadi", "Chor Minor YUNESKO ro‘yxatiga kiritildi"],
      "1785 → 1800 → 1807 → 1826 → 1995.")
t.MATCH("Atamalarni ma’nosi bilan moslashtiring.", ["Chorsu", "Chor Minor", "Registon", "tim"],
        ["to‘rtta yo‘l", "to‘rt minora", "qumloq joy", "usti yopiq bozor", "olti qirrali toq"], 'abcd',
        "Chorsu – to‘rt yo‘l; Chor Minor – to‘rt minora; Registon – qumloq joy; tim – yopiq bozor.")
t.VENN("Xalifa Xudoydod majmuasi", "Chor Minor",
       [("39 ta bir qavatli hujra", 1), ("sardoba va qabriston bor", 1),
        ("to‘rt minorali darvozaxona", 2), ("1807-yilda qurilgan", 2),
        ("mang‘itlar davrida Buxoroda qurilgan", 3)],
       "Xudoydod – 39 hujra, sardoba; Chor Minor – to‘rt minora, 1807; ikkalasi Buxoroda.")
t.MAPMATCH('uzb', ['Samarqand', 'Buxoro', 'Qarshi', 'Xiva'],
           ["Toqi musaddas (Chorsu) qurilgan shahar", "Chor Minor va Xalifa Xudoydod majmuasi joylashgan shahar", "Amir Haydar davrida Gulining mablag‘iga madrasa qurilgan shahar", "Xalifa Xudoydod kelib chiqqan Xorazm poytaxti"],
           "1 – Samarqand; 2 – Buxoro; 3 – Qarshi; 4 – Xiva.")

# 17-§ Xiva xonligining tashkil topishi
t = Topic('y9u17', 9017); TOPICS['y9u17'] = t
t.B("Shayboniyxon Urganchni qachon egallagan?", "1505-yilda", "1510-yilda", "1511-yilda", "1500-yilda", "1505-yilda.")
t.B("1510-yilda Xorazmni kim bosib olgan?", "safaviylar", "shayboniylar", "qozoqlar", "temuriylar", "Safaviylar.")
t.B("1511-yilda safaviylarga qarshi xalq harakatiga kim boshchilik qilgan?", "Vazir shahri qozisi Umar Shayx", "Elbarsxon", "Ubaydullaxon", "Abulg‘ozixon", "Vazir qozisi Umar Shayx.")
t.B("Xorazm shayxlari taxtga kimni taklif qilgan?", "Elbarsxonni", "Ubaydullaxonni", "Dinmuhammadni", "Abdulazizxonni", "Berka sulton avlodi Elbarsxonni.")
t.B("Arabshohiylar sulolasining shajarasi kimga borib taqaladi?", "Jo‘jining beshinchi o‘g‘li Shaybonga", "Amir Temurga", "Chingizxonning to‘rtinchi o‘g‘liga", "Abulxayrxonga", "Shaybonga.")
t.B("Xiva xonligi qachon tashkil topgan?", "1511-yilda", "1505-yilda", "1538-yilda", "1770-yilda", "1511-yilda.")
t.B("Elbarsxon janubda qaysi daryogacha bo‘lgan yerlarni bo‘ysundirgan?", "Atrok daryosi", "Murg‘ob", "Amudaryo", "Sirdaryo", "Atrok daryosi va Saraxs atroflarigacha.")
t.B("1538-yilda Abdulazizni Xorazmdan qochishga majbur qilgan kim?", "Dinmuhammad sulton", "Elbarsxon", "Umar Shayx", "Abulg‘ozixon", "Dinmuhammad sulton.")
t.B("Abdullaxon II butun Xorazmni qachon bo‘ysundirgan?", "1593-yilda", "1575-yilda", "1598-yilda", "1558-yilda", "1593-yilda.")
t.B("Nodirshohning Xorazmga hujumi qachon bo‘lgan?", "1739–1740-yillarda", "1593-yilda", "1770-yilda", "1511-yilda", "1739–1740-yillarda.")
t.B("Muhammad Amin inoq 1762-yildan qanday lavozimni egallagan?", "otaliq", "qushbegi", "mehtar", "devonbegi", "Otaliq.")
t.B("Xorazmda qo‘ng‘irotlar sulolasining rasmiy hukmronligi qachon boshlangan?", "1770-yilda", "1762-yilda", "1740-yilda", "1804-yilda", "1770-yilda.")
t.B("Xiva xonligida taxt vorisi qanday atalgan?", "qolxon", "qolg‘a", "navvob", "sulton", "Qolxon (kolxon).")
t.B("Abulg‘ozixon Xorazm aholisini nechta asosiy bo‘linmaga (to‘pga) ajratgan?", "to‘rtta", "uchta", "oltita", "o‘nta", "To‘rtta to‘p.")
t.B("Abulg‘ozixon to‘plaridan biri qaysi?", "nukus-mang‘it", "kenagas-qatag‘on", "do‘rmon-burgut", "nayman-saroy", "Uyg‘ur-nayman, qiyot-qo‘ng‘irot, nukus-mang‘it, qang‘li-qipchoq.")
t.B("Muhammad Rahimxon I davrida davlat lavozimlari soni qanchaga qisqartirilgan?", "360 tadan 100 taga", "100 tadan 50 taga", "200 tadan 60 taga", "360 tadan 36 taga", "360 dan 100 taga.")
t.B("Xiva xonligida bosh vazir qanday atalgan?", "mehtar", "qushbegi", "devonbegi", "otaliq", "Mehtar (vaziri a’zam).")
t.B("Xiva xonligida soliqlar yig‘imi va qo‘shin shayligiga javobgar amaldor kim?", "qushbegi", "mehtar", "oqsoqol", "inoq", "Qushbegi.")
t.B("Quyi ma’muriyat vakili kim bo‘lgan?", "oqsoqol", "hokim", "qozi", "mehtar", "Oqsoqol.")
t.NAT("Elbarsxon vafotidan so‘ng arabshohiylar o‘rtasida hokimiyat uchun kurash kuchaydi.", "Ubaydullaxon Xorazmni markaziy hokimiyat izmiga qaytardi", "Xiva Rossiyaga qo‘shildi", "Elbarsxon avlodlari birlashdi", "Xorazm mustaqil bo‘ldi", "Buxoro Xorazmni bo‘ysundirdi.")
t.NAT("1558-yillardan siyosiy barqarorlik o‘rnatildi.", "Xiva shahrining poytaxt sifatidagi ahamiyati oshib bordi", "Urganch poytaxtga aylandi", "Xorazm parchalandi", "Eron Xivani oldi", "Xiva poytaxt mavqeini mustahkamladi.")
t.NAT("Muhammad Rahimxon I ma’muriy islohot o‘tkazdi.", "kent shakli o‘rniga masjid birliklari (masjid qavmi) joriy etildi", "bekliklar bekor qilindi", "xon hokimiyati cheklandi", "Oliy Kengash tarqatildi", "Masjid birliklari joriy etildi.")
t.NAT("Qipchoq dashtidan kelgan urug‘lar Xorazmda o‘troqlashdi.", "Abulg‘ozixon boshqaruvni qayta tashkil etib, aholini to‘rt to‘pga bo‘ldi", "urug‘lar Buxoroga ketdi", "xonlik bekliklarga bo‘linmadi", "Oliy Kengash tugatildi", "To‘plar tizimi joriy etildi.")
t.TF("Xiva xonligida jinoyatchilarni «oliy jazo»ga buyurish faqat oliy hukmdor vakolatida edi.", True, "To‘g‘ri.")
t.TF("Arabshohiylarda taxt otadan katta o‘g‘ilga meros bo‘lib o‘tgan.", False, "Noto‘g‘ri: chingiziy sultonlardan yoshi eng ulug‘iga o‘tgan.")
t.TF4([("Vazir shahri Ustyurtda, Ko‘hna Urganchdan 60 km uzoqlikda joylashgan.", True), ("Abdullaxon II 1575-yilda Urganchni egallagan.", True),
       ("Muhammad Rahimxon I davrida biy, otaliq, inoq mansablari bekor qilingan.", True), ("Xiva shahri bekliklardan biri sifatida hokim tomonidan boshqarilgan.", False)],
      "4-noto‘g‘ri: poytaxt Xiva bevosita oliy hukmdor boshqaruvida bo‘lgan.")
t.MUL([("Xiva xonligi O‘rta Osiyoda ikkinchi o‘zbek davlati edi.", True),
       ("Markaziy boshqaruvda Oliy va Kichik Kengash tashkil etilgan.", True),
       ("Arabshohiylar Abdullaxon II vafotidan oldin hokimiyatni qaytarib olgan.", False)],
      "III noto‘g‘ri: Abdullaxon II vafotidan (1598) keyingina qaytarib olgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Shayboniyxon Urganchni egalladi", "Arabshohiylar hukmronligi boshlandi", "Dinmuhammad Abdulazizni quvdi", "Abdullaxon II butun Xorazmni bo‘ysundirdi", "Nodirshoh Xorazmga hujum qildi", "Qo‘ng‘irotlar hukmronligi boshlandi"],
      "1505 → 1511 → 1538 → 1593 → 1739 → 1770.")
t.MATCH("Xiva xonligi lavozimlarini vazifasi bilan moslashtiring.", ["mehtar", "qushbegi", "oqsoqol", "qolxon"],
        ["bosh vazir (vaziri a’zam)", "soliq yig‘imi va qo‘shin shayligi", "quyi ma’muriyat vakili", "taxt vorisi", "shahzodalar tarbiyachisi"], 'abcd',
        "Mehtar – bosh vazir; qushbegi – soliq; oqsoqol – quyi ma’muriyat; qolxon – valiahd.")
t.VENN("Arabshohiylar", "Qo‘ng‘irotlar",
       [("1511-yilda hokimiyatga kelgan", 1), ("Elbarsxon asos solgan", 1),
        ("1770-yildan rasmiy hukmronlik", 2), ("Muhammad Rahimxon I islohotlari", 2),
        ("Xiva xonligini boshqargan sulola", 3)],
       "Arabshohiylar – 1511, Elbarsxon; qo‘ng‘irotlar – 1770, islohotlar; ikkalasi Xiva sulolasi.")
t.MAPMATCH('xorazm2', ['Ko‘hna Urganch', 'Xiva', 'Orol dengizi'],
           ["1505-yilda Shayboniyxon egallagan shahar", "1558-yildan ahamiyati oshgan poytaxt", "Elbarsxon davrida shimoliy chegara"],
           "1 – Ko‘hna Urganch; 2 – Xiva; 3 – Orol dengizi.")

# 18-§ Tashqi siyosat
t = Topic('y9u18', 9018); TOPICS['y9u18'] = t
t.B("Pyotr I harbiy kuchlarini birinchilardan bo‘lib qarshi olgan Xiva xoni kim?", "Sherg‘ozixon", "Abulg‘ozixon", "Arab Muhammadxon", "Elbarsxon", "Sherg‘ozixon.")
t.B("Bekovich-Cherkasskiy yurishi qaysi yillarda uyushtirilgan?", "1714–1717-yillarda", "1839-yilda", "1603–1623-yillarda", "1739–1740-yillarda", "1714–1717-yillarda.")
t.B("Bekovich-Cherkasskiy qo‘shini necha askardan iborat bo‘lgan?", "6000", "5000", "1000", "60000", "6000 askar.")
t.B("Sherg‘ozixon Bekovich qo‘shiniga qarshi qanday reja tuzgan?", "dushmanni mayda bo‘laklarga ajratib yo‘q qilish", "ochiq maydonda jang qilish", "sulh tuzish", "qal’ada qamalda turish", "Bo‘laklarga ajratib yo‘q qilish.")
t.B("Ruslar qaysi yo‘l orqali Xiva bilan savdoni kuchaytirishga harakat qilgan?", "Kaspiy-Volga yo‘li", "Buyuk ipak yo‘li", "Sibir yo‘li", "Qora dengiz yo‘li", "Kaspiy-Volga yo‘li.")
t.B("Arab Muhammadxon davrida Urganchgacha kelib, talon-toroj qilgan kimlar?", "Yoyiq kazak otliqlari", "qalmoqlar", "eroniylar", "qozoqlar", "Ming nafar Yoyiq kazaklari.")
t.B("Arab Muhammad sulton qaysi yillarda xonlik qilgan?", "1603–1623", "1511–1518", "1714–1717", "1770–1790", "1603–1623.")
t.B("XVI–XIX asrlarda Xivadan Rossiyaga necha marta elchilik yuborilgan?", "50 marta", "17 marta", "10 marta", "100 marta", "50 marta.")
t.B("Rossiyadan Turkiston siyosiy markazlariga nechta elchilik yuborilgan?", "17 ta", "50 ta", "5 ta", "100 ta", "17 ta.")
t.B("Qojarlar Eronni qaysi yillarda boshqargan?", "1795–1925-yillarda", "1501–1736-yillarda", "1736–1747-yillarda", "1812–1852-yillarda", "1795–1925-yillarda.")
t.B("1812–1852-yillarda Xiva–Eron elchilik aloqalari asosan qaysi masalalarga qaratilgan?", "asirlarni ozod qilish, qul savdosini to‘xtatish", "chegarani belgilash", "harbiy ittifoq", "savdo bojlari", "Asirlar va qul savdosi.")
t.B("Usmonli davlatini Turon bilan bog‘lashda o‘tar hudud sifatida qaysi yo‘l ishlatilgan?", "«Xorazm yo‘li»", "«Sibir yo‘li»", "«Hind yo‘li»", "«Volga yo‘li»", "«Xorazm yo‘li».")
t.B("Hindiston bilan do‘stlik maqsadida boburiylar bilan elchilar almashgan Xiva xoni kim?", "Arab Muhammadxon", "Sherg‘ozixon", "Elbarsxon", "Muhammad Rahimxon", "Arab Muhammadxon.")
t.B("Rossiya Kichik qozoq juzidagi xon boshqaruvini qachon tugatgan?", "1824-yilda", "1839-yilda", "1812-yilda", "1795-yilda", "1824-yilda.")
t.B("1839-yil kuzida Orenburgdan Xivaga yuborilgan qo‘shinga kim boshchilik qilgan?", "V. Perovskiy", "Bekovich-Cherkasskiy", "Yermak", "Kaufman", "V. Perovskiy.")
t.B("Perovskiy qo‘shini necha kishidan iborat bo‘lgan?", "5 ming", "6 ming", "1 ming", "50 ming", "5 ming kishilik.")
t.NAT("Qattiq qish va qalin qor Perovskiy qo‘shinining harakatini deyarli imkonsiz qildi.", "rus hukumati xonlikni harbiy yo‘l bilan bo‘ysundirish mushkulligini anglab, muzokaralarga o‘tdi", "Xiva Rossiyaga bo‘ysundi", "Perovskiy Xivani egalladi", "Xiva Eron bilan ittifoq tuzdi", "Muzokaralar yo‘liga o‘tildi.")
t.NAT("Nodirshoh 1739–1740-yillarda Turkistonga yurishlar uyushtirdi.", "Xiva–Eron o‘rtasidagi iliq aloqalar buzildi", "Xiva Eronni bosib oldi", "qojarlar hokimiyatga keldi", "aloqalar yanada yaxshilandi", "Munosabatlar buzildi.")
t.NAT("Kichik qozoq juzi va Sirdaryo bo‘yidagi urug‘lar rus fuqaroligini qabul qildi.", "Xiva bu yerlarga da’vo qilib, zakot olishni va aralashishni davom ettirdi", "Xiva qozoqlarni butunlay tark etdi", "qozoqlar Xivani bosib oldi", "Rossiya Xivaga yer berdi", "Xiva–Rossiya ziddiyati.")
t.NAT("Qozoq dashtida Rossiya harbiy harakatlari faollashdi.", "milliy-ozodlik kurashlari avj oldi, qozoqlar xorazmliklarni ittifoqchi deb bildi", "qozoqlar Rossiyaga sodiq bo‘ldi", "Xiva qozoqlarga qarshi chiqdi", "kurashlar to‘xtadi", "Xiva–qozoq birdamligi.")
t.TF("Yoyiq kazaklari asirlar va boyliklarni olib ketayotganda xorazmliklar tomonidan qirib tashlangan.", True, "To‘g‘ri.")
t.TF("Xiva–Rossiya muzokaralari o‘zaro yuqori bojlar o‘rnatishga qaratilgan.", False, "Noto‘g‘ri: «bojsiz savdo»ni yo‘lga qo‘yishga qaratilgan.")
t.TF4([("Pyotr I Turon orqali Hindistonga yuzlanishni maqsad qilgan.", True), ("Asirlarni ozod qilish katta miqdordagi to‘lov evaziga amalga oshirilgan.", True),
       ("Qo‘ng‘irotlar qozoq juzlari bilan hech qanday aloqa qilmagan.", False), ("Rossiya uchun xonlikning xomashyosi juda muhim edi.", True)],
      "3-noto‘g‘ri: qozoq juzlari bilan uzluksiz elchilar almashgan.")
t.MUL([("Muzokaralarda qaroqchilar o‘g‘irlagan mollarni qaytarish nazarda tutilgan.", True),
       ("Haj ziyoratchilari Usmonli hududlaridagi yo‘llardan foydalangan.", True),
       ("Sherg‘ozixon Bekovich qo‘shini bilan ochiq maydonda jang qilishni afzal ko‘rgan.", False)],
      "III noto‘g‘ri: dushmanni bo‘laklarga ajratib yo‘q qilishni rejalagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Arab Muhammad sulton xonligi boshlandi", "Bekovich-Cherkasskiy yurishi", "Nodirshohning Xorazmga yurishi", "Qojarlar Eronda hokimiyatga keldi", "Kichik juzda xon boshqaruvi tugatildi", "Perovskiy yurishi"],
      "1603 → 1714 → 1739 → 1795 → 1824 → 1839.")
t.MATCH("Shaxslarni voqea bilan moslashtiring.", ["Bekovich-Cherkasskiy", "V. Perovskiy", "Sherg‘ozixon", "Arab Muhammadxon"],
        ["1714–1717-yillardagi rus yurishi", "1839-yilgi Orenburg yurishi", "Pyotr I qo‘shinini qarshi olgan xon", "boburiylar bilan elchilar almashgan xon", "qojarlar sulolasi asoschisi"], 'abcd',
        "Bekovich – 1714–1717; Perovskiy – 1839; Sherg‘ozixon – Pyotr I; Arab Muhammad – boburiylar.")
t.VENN("Bekovich-Cherkasskiy yurishi", "Perovskiy yurishi",
       [("Pyotr I topshirig‘i bilan", 1), ("6000 askar", 1),
        ("Orenburgdan, 1839-yil kuzi", 2), ("qattiq qish rejani barbod qildi", 2),
        ("Xivaga qarshi muvaffaqiyatsiz rus yurishi", 3)],
       "Bekovich – Pyotr I, 6000; Perovskiy – Orenburg, qish; ikkalasi muvaffaqiyatsiz.")
t.MAPMATCH('steppe', ['Orenburg', 'Ashtarxon', 'Xiva', 'Mashhad'],
           ["1839-yilda Perovskiy qo‘shini yo‘lga chiqqan shahar", "Kaspiy-Volga savdo yo‘lidagi Hoji Tarxon", "Sherg‘ozixon Bekovichni qarshi olgan xonlik poytaxti", "qojarlar bilan chegaradosh Xuroson shahri"],
           "1 – Orenburg; 2 – Ashtarxon (Hoji Tarxon); 3 – Xiva; 4 – Mashhad.")
