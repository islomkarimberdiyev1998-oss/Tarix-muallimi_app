from qlib import Topic
TOPICS = {}
UZ = 'uzb'; BA = 'buxamir'

# 32 1916-yilgi voqealarning oqibatlari va ahamiyati
t = Topic('e9u32', 9032); TOPICS['e9u32'] = t
t.B("1916-yilgi qo‘zg‘olon xarakteriga ko‘ra qanday ko‘rinishda yuz bergan?", "milliy-ozodlik", "saroy to‘ntarishi", "diniy urush", "fuqarolar urushi", "Asosiy kuchi xalq ommasi bo‘lgani uchun milliy-ozodlik ko‘rinishida.")
t.B("Rus amaldorlaridan biri qo‘zg‘olonlarga qanday baho bergan?", "«Urush frontlariga yangi bir Turkiston fronti qo‘shildi»", "«Turkiston tinchidi»", "«Bu oddiy g‘alayon»", "«Turkiston mustaqil bo‘ldi»", "«Urush frontlariga yangi bir Turkiston fronti qo‘shildi».")
t.B("Qo‘zg‘olonchilar asosan qanday qurollar bilan jang qilgan?", "oddiy ish qurollari bilan", "pulemyotlar bilan", "to‘plar bilan", "zamonaviy miltiqlar bilan", "Oddiy ish qurollari bilan.")
t.B("Ayrim ma’lumotlarga ko‘ra 1916-yilgi qo‘zg‘olon oqibatida Turkistonda necha kishi o‘ldirilgan?", "673 ming kishi", "300 ming kishi", "3 ming kishi", "87 ming kishi", "673 ming kishi.")
t.B("1916-yilgi voqealardan keyin qancha aholi xorijga chiqib ketgan?", "300 mingdan ziyod", "673 ming", "11 ming", "1 million", "300 mingdan ziyod.")
t.B("Jizzax qo‘zg‘oloni tarixda qanday nom qoldirgan?", "«Jizzax fojiasi»", "«Toshotar voqeasi»", "«Vabo isyoni»", "«Qonli juma»", "«Jizzax fojiasi».")
t.B("«Jizzax qo‘zg‘oloni» dostonini kim yaratgan?", "Fozil Yo‘ldosh o‘g‘li", "Berdaq", "Ajiniyoz", "Ogahiy", "Fozil Yo‘ldosh o‘g‘li.")
t.B("Qo‘zg‘olon qaysi faslda bo‘lgani uchun ekinzorlar nobud bo‘lgan?", "yozda", "qishda", "bahorda", "kuzda", "Yoz faslida.")
t.B("Aholi qaysi yillar qishi uchun oziq-ovqat zaxirasining katta qismidan ayrilgan?", "1916–1917-yillar", "1914–1915-yillar", "1917–1918-yillar", "1898–1899-yillar", "1916–1917-yillar qishi uchun.")
t.NAT("Qo‘zg‘olonda qatnashgan Jizzax atrofidagi qishloqlar yondirib yuborildi.", "ko‘pchilik uy-joysiz qoldi", "qishloqlar qayta qurildi", "aholi boyidi", "soliqlar kamaydi", "Ko‘pchilik uy-joysiz qoldi.")
t.NAT("Qo‘zg‘olon mustamlakachi hukumatni qattiq sarosimaga soldi.", "podsho hukumati ba’zi yengilliklar yaratib, aholi bilan murosa qilishga majbur bo‘ldi", "hukumat Turkistonni tark etdi", "mardikorlik ikki baravar oshirildi", "Turkiston mustaqil bo‘ldi", "Hukumat ba’zi choralar ko‘rib, murosaga majbur bo‘ldi.")
t.NAT("Turkiston aholisi mardikorlikka safarbar qilindi.", "mahalliy aholining katta qismi boquvchisiz qoldi, oziq-ovqat taqchil bo‘ldi", "aholi farovonligi oshdi", "narxlar tushdi", "qishloq xo‘jaligi rivojlandi", "Boquvchisiz qolish, taqchillik va qimmatchilik yuzaga keldi.")
t.TF("Qo‘zg‘olonda qariyalar va ayollar ham ishtirok etgan.", True, "To‘g‘ri: barcha tabaqalar qatnashgan.")
t.TF("Qo‘zg‘olonchilar harbiy sohani yaxshi bilgan va birdamlikda harakat qilgan.", False, "Noto‘g‘ri: ular harbiy ishdan bexabar edi, birdamlikda harakat qilmadi.")
t.TF("1916-yilgi qo‘zg‘olon butun mustamlakachilik davomida Turkistondagi eng qudratli va uyushgan qo‘zg‘olon edi.", True, "To‘g‘ri.")
t.MUL([("Qo‘zg‘olonchilarning taktik va strategik uquvsizligi mag‘lubiyatga sabab bo‘lgan.", True),
       ("100 minglab kishining mol-mulki musodara qilinib, talon-toroj etilgan.", True),
       ("Qo‘zg‘olon podsho hukumati tomonidan tinch yo‘l bilan hal qilingan.", False)],
      "III noto‘g‘ri: qo‘zg‘olonlar ayovsiz bostirilgan.")
t.MATCH("Raqamlarni ularning ma’nosi bilan moslashtiring.", ["673 ming", "300 mingdan ziyod", "3 ming", "11 ming"],
        ["Jizzaxda hibsga olinganlar", "Jizzax uyezdidan mardikorlikka belgilanganlar", "o‘ldirilgan Turkiston aholisi", "xorijga chiqib ketganlar"], "cdab",
        "673 ming — o‘ldirilgan; 300 ming — xorijga ketgan; 3 ming — hibsga olingan; 11 ming — Jizzax uyezdidan belgilangan.")
t.MAPN(UZ, ['Toshkent', 'Jizzax', 'Andijon', 'Buxoro'], "Qaysi raqam bilan tarixda «fojia» nomini qoldirgan 1916-yilgi qo‘zg‘olon markazi belgilangan?",
       "2 – Jizzax («Jizzax fojiasi»).", ask_idx=1)
t.VENN("Qo‘zg‘olonning yengilish sabablari", "Qo‘zg‘olonning ahamiyati",
       [("oddiy ish qurollari bilan jang qilish", 1), ("ahillik va birdamlik yo‘qligi", 1),
        ("ozodlik tuyg‘ulari so‘nmaganini ko‘rsatgan", 2), ("hukumatni murosaga majbur qilgan", 2),
        ("1916-yilgi milliy-ozodlik qo‘zg‘oloni bilan bog‘liq", 3)],
       "Yengilish — qurol, tarqoqlik; ahamiyat — ozodlik ruhi, murosa.")

# 33 Buxoro amirligining davlat tuzumi va ijtimoiy-iqtisodiy hayoti
t = Topic('e9u33', 9033); TOPICS['e9u33'] = t
t.B("«Rossiya imperatorining siyosiy agentligi» qaysi yillarda faoliyat yuritgan?", "1886–1917", "1868–1873", "1873–1920", "1885–1898", "1885-yilgi farmon asosida, 1886–1917.")
t.B("XIX asr oxirida Buxoro amirligi aholisi qancha bo‘lgan?", "2 million atrofida", "800 ming", "5,2 million", "3 million", "2 million kishi atrofida.")
t.B("Buxoro amirligida davlat ishlarini boshqaruvchi oliy amaldor kim?", "qo‘shbegi", "devonbegi", "bosh qozi", "rais", "Qo‘shbegi.")
t.B("Xazina va zakot yig‘imini kim boshqargan?", "devonbegi", "qo‘shbegi", "rais", "to‘pchiboshi", "Devonbegi.")
t.B("Bozordagi tarozi va o‘lchovlar ustidan nazoratni kim boshqargan?", "rais", "devonbegi", "qo‘shbegi", "amin", "Rais; u bosh qoziga bo‘ysungan.")
t.B("Amirning xos lashkariga kim rahbarlik qilgan?", "to‘pchiboshi", "qo‘shbegi", "devonbegi", "bek", "To‘pchiboshi (to‘pchilashkar).")
t.B("Har yili Peterburgga imperator huzuriga katta sovg‘alar bilan qatnagan amir kim?", "Amir Abdulahad", "Amir Muzaffar", "Amir Nasrullo", "Amir Olimxon", "Amir Abdulahad.")
t.B("Buxoro amirligida asosiy soliqlarni aholining qancha qismini tashkil etuvchi dehqonlar to‘lagan?", "90% ga yaqinini", "50% ini", "10% ini", "25% ini", "90% ga yaqinini.")
t.B("Ayrim viloyatlarda xiroj miqdori hosilning qancha qismiga yetgan?", "40–50% iga", "1/5 qismiga", "10% iga", "2,5% iga", "40–50% iga.")
t.B("Bog‘ va polizlardan olingan daromad uchun qanday yig‘im to‘langan?", "tanobona", "kafsan", "dorug‘ayi muzd", "zakot", "Tanobona.")
t.B("Xirmonlarni xatga olgani uchun amaldorga to‘lanadigan qo‘shimcha maosh qanday atalgan?", "dorug‘ayi muzd", "tanobona", "xiroj", "kafsan", "Dorug‘ayi muzd.")
t.B("1885-yilda Baljuvon bekligidagi qo‘zg‘olonga kim rahnamolik qilgan?", "Vose", "Bobo Go‘klan", "Darvishxon", "Ernazarbiy", "Vose.")
t.B("1888-yilda qaysi beklikda yirik dehqonlar qo‘zg‘oloni boshlangan?", "Ko‘lob", "Baljuvon", "Kalif", "Shahrisabz", "Ko‘lob bekligida.")
t.B("Buxoro amirligi hududi orqali dastlabki temiryo‘l qachon o‘tkazilgan?", "1887-yilda", "1888-yilda", "1899-yilda", "1905-yilda", "1887-yilda.")
t.B("Buxorodan 15 km masofada qaysi stansiya qurilishi boshlangan?", "Yangi Buxoro", "Chorjo‘y", "Karki", "Termiz", "Yangi Buxoro (Kogon).")
t.B("Rossiya Buxoro orqali Afg‘onistonga qanday mahsulotlar chiqargan?", "movut, chinni, baxmal, chit, gugurt, kerosin", "paxta va ipak", "gilam va namat", "qurol-yarog‘", "Movut, chinni buyumlar, baxmal, chit, gugurt, kerosin.")
t.NAT("1885-yilda baljuvonlik dehqonlardan o‘tgan kamhosil yillar uchun ham xiroj talab qilindi.", "minglab dehqonlar Vose atrofida uyushib qo‘zg‘olon ko‘tardi", "dehqonlar soliqni to‘ladi", "amir soliqni bekor qildi", "dehqonlar ko‘chib ketdi", "Adolatsiz soliq Vose qo‘zg‘oloniga sabab bo‘ldi.")
t.NAT("Hunarmandlarning daromadlari behisob soliqlarni to‘lashga ketardi.", "ular ustaxonalarini rivojlantirish uchun mablag‘ga ega bo‘lmadi", "hunarmandchilik tez rivojlandi", "ular boyib ketdi", "soliqlar kamaydi", "Rivojlanish uchun qo‘shimcha mablag‘ qolmadi.")
t.TF("Buxoro gilamlariga chet ellarda, jumladan, Rossiyada ham talab katta bo‘lgan.", True, "To‘g‘ri.")
t.TF("XIX asr oxirida amir lashkari zamonaviy qurollangan va yaxshi o‘qitilgan bo‘lgan.", False, "Noto‘g‘ri: lashkar yomon o‘qitilgan, sodda qurollangan dehqonlardan iborat edi.")
t.MUL([("Qo‘shbegi, devonbegi va bosh qozi har doim Buxoroda bo‘lishi shart edi.", True),
       ("Buxoroda Rossiya davlat banki bo‘limi va ikkita paxta tozalash zavodi ochilgan.", True),
       ("Barcha amaldorlarni amirning o‘zi tayinlagan.", False)],
      "III noto‘g‘ri: barcha amaldorlarni qo‘shbegi, faqat oliy amaldorlarni amir tayinlagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Baljuvonda Vose qo‘zg‘oloni", "Amirlik orqali dastlabki temiryo‘l o‘tkazildi", "Ko‘lob bekligida dehqonlar qo‘zg‘oloni", "Kalif bekligida qo‘zg‘olon"],
      "1885 → 1887 → 1888 → 1889.")
t.MAPMATCH(BA, ['Baljuvon', 'Kalif', 'Chorjo‘y'],
           ["1885-yilda Vose qo‘zg‘oloni bo‘lgan beklik", "1889-yil mayda qo‘zg‘olon bo‘lgan beklik", "Rossiya firmalari idoralari bo‘lgan yirik savdo shahri"],
           "1 – Baljuvon; 2 – Kalif; 3 – Chorjo‘y.")
t.VENN("Qo‘shbegi", "Devonbegi",
       [("davlat ishlarini boshqaruvchi oliy amaldor", 1), ("har kuni amirga ahvol haqida ma’lumot bergan", 1),
        ("xazina va zakot yig‘imini boshqargan", 2), ("mavqeyi qo‘shbegidan keyin turgan", 2),
        ("har doim Buxoroda bo‘lishi shart bo‘lgan", 3)],
       "Qo‘shbegi — oliy amaldor, amirga hisobot; devonbegi — xazina, zakot; ikkalasi Buxoroda bo‘lishi shart.")
