from qlib import Topic
TOPICS = {}
XR = 'xorazm'; ST = 'steppe'

# 22 Soliq va majburiyatlar. Xalq qo‘zg‘olonlari
t = Topic('e9u22', 9022); TOPICS['e9u22'] = t
t.B("Qoraqalpoqlardan olingan yer solig‘i qanday atalgan?", "solg‘ut", "ushr", "zakot", "qozon puli", "Yer solig‘i — solg‘ut.")
t.B("Ruhoniylar foydasiga qanday soliq undirilgan?", "ushr", "solg‘ut", "zakot", "tarozi puli", "Ushr solig‘i.")
t.B("Urush paytlarida qoraqalpoqlar qanday soliq to‘lagan?", "qozon puli", "ushr", "solg‘ut", "do‘kon puli", "Qozon puli solig‘i.")
t.B("Chorvador oila chorva mollarining qancha qismini zakot sifatida to‘lagan?", "qirqdan bir qismini", "o‘ndan bir qismini", "yarmini", "beshdan bir qismini", "Qirqdan bir qismini.")
t.B("XIX asr ikkinchi yarmida 40 bosh qoramol uchun qancha zakot olingan?", "9 so‘m", "2 so‘m 50 tiyin", "40 so‘m", "1 so‘m", "9 so‘m; 40 bosh qo‘y-echki uchun 2 so‘m 50 tiyin.")
t.B("Eng og‘ir majburiyat qanday bo‘lgan?", "har oiladan bir erkakning 12 kun ariq qazishi", "har yili 1000 askar berish", "xonga sovg‘a yuborish", "karvonlarni qo‘riqlash", "Har oiladan bitta erkakning 12 kun ariq qazishi.")
t.B("Urush holatida har bir jamoa necha askar berishi lozim bo‘lgan?", "1000 tadan 2000 tagacha", "100 tadan 200 tagacha", "10 ta", "5000 ta", "1000 tadan 2000 tagacha askar.")
t.B("Askar bera olmagan jamoalardan safarbarlik paytida qancha pul yig‘ilgan?", "180 mingdan 250 ming so‘mgacha", "9 ming so‘m", "1 million so‘m", "500 so‘m", "180 ming so‘mdan 250 ming so‘mgacha.")
t.B("1855-yilda qoraqalpoqlar qo‘zg‘oloniga kim boshchilik qilgan?", "Ernazarbiy", "Bobo Go‘klan", "Otamurodxon", "Zarliq", "Qo‘ldovli qabilasidan Ernazarbiy.")
t.B("Ernazarbiy qaysi qozoq urug‘ boshlig‘ini xon qilib ko‘tarishga intilgan?", "Zarliqni", "Otamurodxonni", "Muhammadniyozni", "Bobo Go‘klanni", "Zarliqni.")
t.B("Ernazarbiy qo‘zg‘olonini bostirishga qaysi Xiva xoni qo‘shin yuborgan?", "Said Muhammadxon", "Muhammad Aminxon", "Muhammad Rahimxon I", "Muhammad Rahimxon II", "1856-yilda taxtga o‘tirgan Said Muhammadxon.")
t.B("Ernazarbiy qaysi qo‘rg‘onda mudofaaga tayyorlangan?", "Qozoqdaryo qo‘rg‘onida", "Oqmachit qal’asida", "Qo‘ng‘irot qal’asida", "Niyozbek qo‘rg‘onida", "O‘zi qurdirgan Qozoqdaryo qo‘rg‘onida.")
t.B("Ernazarbiy tarafdorlari qal’adan chiqib qayerdan panoh topgan?", "Oqmachit qal’asidan", "Xivadan", "Buxorodan", "Nukusdan", "1853-yilda ruslar bosib olgan Oqmachitdan.")
t.B("1858–1859-yillardagi qo‘zg‘olon markazi qaysi shahar bo‘lgan?", "Qo‘ng‘irot", "Nukus", "Chimboy", "Xiva", "Qo‘ng‘irot shahri.")
t.B("1858–1859-yillardagi qo‘zg‘olonni bostirish kimga topshirilgan?", "Otamurodxonga", "Muhammadniyozga", "Kaufmanga", "Ernazarbiyga", "Turkman jangovar kuchlari boshlig‘i Otamurodxonga.")
t.B("Biybozor va Nukus volostida qo‘zg‘olonga kim boshchilik qilgan?", "Bobo Go‘klan", "Ernazarbiy", "Zarliq", "Otamurodxon", "Bobo Go‘klan; qariyb o‘n yil (1881–1891) davom etdi.")
t.NAT("Xiva xoni mudofaani kuchaytirish uchun ko‘p xarajat qildi.", "xazinani to‘ldirish uchun aholiga soliqlar miqdori oshirildi", "soliqlar kamaydi", "xon taxtdan voz kechdi", "Rossiya yordam berdi", "Bo‘shagan xazinani to‘ldirish uchun soliqlar oshirildi.")
t.NAT("Qozoqdaryo qo‘rg‘onini katta qo‘shin qamal qila boshladi.", "qo‘zg‘olonchilar orasida kelishmovchilik chiqib, Ernazarbiy otib tashlandi", "Ernazarbiy g‘alaba qozondi", "Xiva qo‘shini chekindi", "qo‘rg‘on Rossiyaga topshirildi", "Kelishmovchilik natijasida Ernazarbiy otib tashlandi.")
t.TF("Majburiyatlarning butun og‘irligi urug‘ jamoasining oddiy a’zolari zimmasiga tushgan.", True, "To‘g‘ri.")
t.TF("Ko‘pchilik qoraqalpoqlar Rossiya imperiyasi tarkibiga qo‘shilishni istagan.", False, "Noto‘g‘ri: ko‘pchilik o‘zbeklar bilan birga yashashni istagan.")
t.MUL([("Rossiya urug‘ boshliqlarini katta pul evaziga sotib olish siyosatini yurgizgan.", True),
       ("1900-yilda Nukus volosti va Qo‘ng‘irot bekligida norozilik harakatlari bo‘lgan.", True),
       ("1858–1859-yilgi qo‘zg‘olon g‘alaba bilan tugab, Qo‘ng‘irot mustaqil bo‘lgan.", False)],
      "III noto‘g‘ri: qo‘zg‘olon ayovsiz bostirilib, Qo‘ng‘irot vayron etilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Ernazarbiy qo‘zg‘oloni boshlandi", "Said Muhammadxon Xiva taxtiga o‘tirdi", "Qo‘ng‘irot qo‘zg‘olon markaziga aylandi", "Bobo Go‘klan qo‘zg‘oloni boshlandi", "Nukus volosti va Qo‘ng‘irot bekligida norozilik"],
      "1855 → 1856 → 1858–1859 → 1881 → 1900.")
t.MAPMATCH(XR, ['Xiva', 'Qo‘ng‘irot', 'Nukus'],
           ["Ernazarbiyga qarshi qo‘shin yuborilgan xonlik poytaxti", "1858–1859-yillardagi qo‘zg‘olon markazi, vayron etilgan shahar", "Bobo Go‘klan qo‘zg‘oloni bo‘lgan volost markazi"],
           "1 – Xiva; 2 – Qo‘ng‘irot; 3 – Nukus.")
t.VENN("Ernazarbiy qo‘zg‘oloni", "Bobo Go‘klan qo‘zg‘oloni",
       [("1855-yilda boshlangan", 1), ("Qozoqdaryo qo‘rg‘onida mudofaa", 1),
        ("Biybozor va Nukus volostida", 2), ("qariyb o‘n yil davom etgan", 2),
        ("qoraqalpoqlar qo‘zg‘oloni", 3)],
       "Ernazarbiy — 1855, Qozoqdaryo; Bobo Go‘klan — Nukus, 1881–1891.")

# 23 Qoraqalpoqlar Turkiston general-gubernatorligi tarkibida
t = Topic('e9u23', 9023); TOPICS['e9u23'] = t
t.B("XIX asrning 70-yillariga kelib qoraqalpoqlar qanday turmush kechira boshlagan?", "deyarli o‘troq", "to‘liq ko‘chmanchi", "dengizchilik", "faqat ovchilik", "Deyarli o‘troq turmush.")
t.B("Qoraqalpoqlar qanday ekinlar yetishtirgan?", "sholi, bug‘doy, arpa va paxta", "choy va kofe", "faqat uzum", "qand lavlagi", "Sholi, bug‘doy, arpa va paxta.")
t.B("Amudaryoning o‘ng qirg‘og‘idagi yerlarda qanday ma’muriy birlik tashkil etilgan?", "Amudaryo bo‘limi", "Zarafshon okrugi", "Kaspiyorti viloyati", "Qoraqalpoq ulusi", "Sirdaryo viloyati tarkibidagi Amudaryo bo‘limi.")
t.B("Amudaryo bo‘limida qoraqalpoqlar soni qancha bo‘lgan?", "qariyb 70 ming kishi", "25 ming kishi", "100 ming kishi", "1 ming kishi", "Qariyb 70 ming — aholining 48,6% i.")
t.B("Xiva xonligi hududida qoraqalpoqlar qancha bo‘lgan?", "qariyb 25 ming kishi (3,8%)", "70 ming kishi", "100 ming kishi", "5 ming kishi", "Qariyb 25 ming, 3,8%.")
t.B("1875-yilda Amudaryo bo‘limiga surgun qilib ko‘chirilganlar kimlar edi?", "Ural kazaklari", "Sibir kazaklari", "polyaklar", "ukrain dehqonlari", "Orolda baliq ovlash nizomiga bo‘ysunmagan Ural kazaklari.")
t.B("Ural kazaklari asosan nima bilan shug‘ullangan?", "baliq ovlash", "paxtachilik", "savdo", "hunarmandchilik", "Asosan baliq ovlash.")
t.B("Qoraqalpoqlarning qancha qismi yersiz dehqonlar bo‘lgan?", "70% dan ziyodi", "10%", "48,6%", "3,8%", "70% dan ziyodi yersiz bo‘lib, yollanib ishlagan.")
t.B("Qaysi sohalarda dastlabki sanoat korxonalari paydo bo‘lgan?", "paxta tozalash va baliqchilik", "metallurgiya", "neft qazib olish", "kemasozlik", "Paxta tozalash va baliqchilik.")
t.B("Qaysi shaharda iqtisodiy jihatdan birlashtiruvchi shahar bozori vujudga kelgan?", "Chimboyda", "Nukusda", "Qo‘ng‘irotda", "To‘rtko‘lda", "Chimboyda.")
t.B("1914-yilda qoraqalpoqlar yashaydigan joylarda nechta umumta’lim maktabi bo‘lgan?", "to‘rtta", "yigirmata", "bitta", "o‘nta", "Atigi to‘rtta maktabda 200 o‘quvchi.")
t.B("1 tanob necha kvadrat metrga teng?", "2500 kv. m", "1000 kv. m", "10 000 kv. m", "500 kv. m", "1 tanob — 2500 kv. m.")
t.B("Ayrim biy, yuzboshi, mulla va eshonlarning yer mulklari necha tanobgacha bo‘lgan?", "15 ming tanobgacha", "1–2 tanob", "100 tanob", "1 million tanob", "15 ming tanobgacha; oddiy xalqniki 1–2 tanob.")
t.B("Yerni hosilning teng yarmi sharti bilan berish qanday atalgan?", "«jarmshi»", "«yarimchi»", "«ushr»", "«solg‘ut»", "«Jarmshi».")
t.NAT("Gandimiyon shartnomasidan keyin qoraqalpoqlar yashaydigan o‘ng qirg‘oq yerlari Rossiyaga qo‘shib olindi.", "podsho hukumatining O‘rta Osiyodagi ta’sir doirasi yanada kengaydi", "qoraqalpoqlar mustaqil bo‘ldi", "Xiva xonligi kengaydi", "Amudaryo bo‘limi tugatildi", "Rossiyaning ta’sir doirasi kengaydi.")
t.NAT("Qoraqalpoqlar yashagan hududlarga Rossiya kapitali kirib keldi.", "tovar-pul munosabatlari o‘zgarib, dastlabki sanoat korxonalari paydo bo‘ldi", "savdo to‘xtadi", "dehqonchilik yo‘qoldi", "chorvachilik kengaydi", "Paxta tozalash va baliqchilik korxonalari paydo bo‘ldi.")
t.TF("Qoraqalpoqlarning Amudaryoning chap qirg‘og‘idagi kamroq qismi Xiva xonligi tarkibida qolgan.", True, "To‘g‘ri.")
t.TF("1914-yilda qoraqalpoqlar yashaydigan joylarda tibbiy xizmat yetarli bo‘lgan.", False, "Noto‘g‘ri: ikkita kasalxona va feldsherlik punktida atigi uch shifokor ishlagan.")
t.MUL([("Rossiyadan ko‘chib kelganlar Petro-Aleksandrovsk, Uralskiy posyolkasi va Nukusda yashagan.", True),
       ("1871–1872-yillarda ayrim boylar ming boshgacha qoramolga ega bo‘lgan.", True),
       ("Urug‘ning oddiy a’zolari ko‘p chorvaga ega bo‘lgan.", False)],
      "III noto‘g‘ri: oddiy a’zolarning aksariyati chorvaga ega bo‘lmagan.")
t.MAPMATCH(XR, ['Chimboy', 'Nukus', 'Petro-Aleksandrovsk (To‘rtko‘l)'],
           ["shahar bozori va yirik karvonsaroy vujudga kelgan iqtisodiy markaz", "Rossiyadan ko‘chib kelganlar yashagan qishloq", "Amudaryo bo‘limining markazi, hozirgi To‘rtko‘l"],
           "1 – Chimboy; 2 – Nukus; 3 – Petro-Aleksandrovsk.")
t.VENN("Amudaryo bo‘limidagi qoraqalpoqlar", "Xiva xonligidagi qoraqalpoqlar",
       [("qariyb 70 ming kishi", 1), ("Amudaryoning o‘ng qirg‘og‘ida", 1),
        ("qariyb 25 ming kishi", 2), ("Amudaryoning chap qirg‘og‘ida", 2),
        ("70% dan ziyodi yersiz dehqonlar", 3)],
       "O‘ng qirg‘oq — 70 ming, Rossiya; chap qirg‘oq — 25 ming, Xiva; ikkalasida ko‘pchilik yersiz.")
