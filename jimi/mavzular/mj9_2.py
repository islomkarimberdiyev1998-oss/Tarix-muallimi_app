from qlib import Topic
TOPICS = {}
FR = 'france'; EU = 'europe'

# 3 Fransiya–Prussiya urushi
t = Topic('e9j3', 9103); TOPICS['e9j3'] = t
t.B("XIX asrning 60-yillari ikkinchi yarmidan qaysi imperatorning mavqeyiga putur yetdi?", "Napoleon III", "Napoleon I", "Vilgelm I", "Lui XVIII", "Fransiya imperatori Napoleon III.")
t.B("Fransiya hukmron doiralari qaysi yilgi savdo shartnomasidan norozi edi?", "1860-yilgi Britaniya–Fransiya shartnomasi", "1871-yilgi Frankfurt shartnomasi", "1815-yilgi Vena shartnomasi", "1856-yilgi Parij shartnomasi", "1860-yilgi Buyuk Britaniya–Fransiya savdo shartnomasidan.")
t.B("Urush boshlanishiga nima bahona bo‘ldi?", "Ispaniya taxtiga kimni o‘tqazish masalasi", "Elzasdagi qo‘zg‘olon", "Belgiyaning bosib olinishi", "Italiyaning birlashishi", "Ispaniya taxti masalasi.")
t.B("1868-yilda Ispaniyada inqilob natijasida qaysi qirolicha Fransiyaga qochgan?", "Izabella II", "Viktoriya", "Mariya Tereza", "Yevgeniya", "Qirolicha Izabella II.")
t.B("Bismark buzib talqin etgan xabar tarixga qanday nom bilan kirgan?", "«Ems depeshasi»", "«Sedan xati»", "«Frankfurt memorandumi»", "«Berlin xabari»", "«Ems depeshasi».")
t.B("Fransiya Prussiyaga qachon urush e’lon qilgan?", "1870-yil 17-iyulda", "1870-yil 1-sentabrda", "1871-yil 18-martda", "1870-yil 4-sentabrda", "1870-yil 17-iyulda.")
t.B("1870-yil 1-sentabrda Napoleon III qaysi qal’a yonida qurshab olingan?", "Sedan", "Mets", "Versal", "Verden", "Sedan qal’asi yonida.")
t.B("Sedanda Napoleon III boshchiligida qancha qo‘shin taslim bo‘lgan?", "80 ming kishi", "140 ming kishi", "100 ming kishi", "40 ming kishi", "80 ming kishilik qo‘shin.")
t.B("100 ming kishilik ikkinchi fransuz qo‘shini qayerda qurshovga tushgan?", "Mets qal’asida", "Sedan qal’asida", "Parijda", "Versalda", "Mets qal’asida.")
t.B("Shoshilinch xabar nima deb ataladi?", "depesha", "ultimatum", "memorandum", "manifest", "Depesha.")
t.B("Napoleon I qo‘shini tor-mor etilgan Vaterloo jangi qachon bo‘lgan?", "1815-yil 18-iyunda", "1870-yil 1-sentabrda", "1805-yilda", "1812-yilda", "1815-yil 18-iyunda.")
t.B("Prussiya qiroli kim edi?", "Vilgelm I", "Fridrix II", "Vilgelm II", "Napoleon III", "Vilgelm I.")
t.NAT("Napoleon III Sedanda taslim bo‘ldi.", "ikkinchi imperiya hokimiyati halok bo‘ldi", "Fransiya urushda g‘alaba qozondi", "Prussiya chekindi", "Ispaniyada qirollik tiklandi", "Bu mag‘lubiyat ikkinchi imperiyaning halokati bo‘ldi.")
t.NAT("Germaniya qiroli Fransiya elchisiga orqasini o‘girgan, degan xabar gazetada chiqdi.", "Fransiya buni haqorat deb hisoblab, urush e’lon qildi", "Fransiya Germaniya bilan ittifoq tuzdi", "Bismark iste’foga chiqdi", "Ispaniya taxti Fransiyaga o‘tdi", "Fransiya 17-iyulda urush e’lon qildi.")
t.TF("Prussiya ham bir necha yillardan beri Fransiyaga qarshi urushga tayyorlanib kelgan.", True, "To‘g‘ri.")
t.TF("Fransiya urushga yaxshi tayyorlangan va Prussiya qudratini to‘g‘ri baholagan.", False, "Noto‘g‘ri: Fransiya urushga tayyor emas, Prussiya qudratini yetarli baholamagan edi.")
t.MUL([("Napoleon III uchun g‘olibona urush mavqeyini tiklash uchun zarur edi.", True),
       ("Prussiyaning maqsadi Germaniyani birlashtirishni nihoyasiga yetkazish edi.", True),
       ("Vilgelm I Ispaniya taxtiga nomzod qo‘yishdan voz kechishga rozi bo‘lmagan.", False)],
      "III noto‘g‘ri: Vilgelm I bunga rozi bo‘lgan, lekin Fransiya qo‘shimcha talablar qo‘ygan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Vaterloo jangi", "Britaniya–Fransiya savdo shartnomasi", "Ispaniyada inqilob", "Fransiya urush e’lon qildi", "Sedandagi taslim bo‘lish"],
      "1815 → 1860 → 1868 → 1870-yil 17-iyul → 1870-yil 2-sentabr.")
t.MAPMATCH(FR, ['Parij', 'Sedan', 'Mets'],
           ["Fransiya poytaxti", "1870-yil 1-sentabrda Napoleon III qurshab olingan qal’a", "100 ming kishilik qo‘shin qurshovga tushgan qal’a"],
           "1 – Parij; 2 – Sedan; 3 – Mets.")
t.VENN("Fransiyaning urushdagi maqsadi", "Prussiyaning urushdagi maqsadi",
       [("Germaniyaning birlashishiga yo‘l qo‘ymaslik", 1), ("Napoleon III mavqeyini tiklash", 1),
        ("Germaniyani birlashtirishni nihoyasiga yetkazish", 2), ("Germaniyada Prussiya hukmronligini mustahkamlash", 2),
        ("urush uchun bahona izlash", 3)],
       "Fransiya — birlashuvga to‘sqinlik; Prussiya — birlashtirishni yakunlash.")

# 4 Uchinchi Respublika va 1871-yil 18-mart
t = Topic('e9j4', 9104); TOPICS['e9j4'] = t
t.B("Parij aholisi mag‘lubiyat haqidagi xabardan keyin qachon qo‘zg‘olon ko‘targan?", "1870-yil 3-sentabrda", "1870-yil 17-iyulda", "1871-yil 18-martda", "1871-yil 28-mayda", "3-sentabrda.")
t.B("Fransiya qachon Respublika deb e’lon qilingan?", "1870-yil 4-sentabrda", "1871-yil 26-martda", "1875-yilda", "1870-yil 19-sentabrda", "4-sentabrda — Uchinchi Respublika.")
t.B("Muvaqqat milliy-mudofaa hukumatini kim boshqargan?", "general Troshyu", "Tyer", "Mak-Magon", "Gambetta", "General Troshyu.")
t.B("Prussiya Fransiyadan qaysi viloyatlarni tortib olishga intilgan?", "Elzas va Lotaringiya", "Normandiya va Bretan", "Savoyya va Nitstsa", "Burgundiya va Provans", "Elzas va Lotaringiya.")
t.B("Parij Prussiya qo‘shini tomonidan qachon qurshab olingan?", "1870-yil 19-sentabrda", "1870-yil 4-sentabrda", "1871-yil 18-martda", "1871-yil 21-mayda", "19-sentabrda.")
t.B("1871-yil fevralida kim boshchiligida yangi hukumat tuzilgan?", "Tyer", "Troshyu", "Napoleon III", "Mak-Magon", "Tyer boshchiligida.")
t.B("Hukumat qarorgohi etib qaysi shahar tanlangan?", "Versal", "Bordo", "Lion", "Marsel", "Versal.")
t.B("18-mart kechasi hukumat qo‘shini kimga hujum qilgan?", "Milliy gvardiyaga", "Prussiya qo‘shiniga", "Kommuna Kengashiga", "Versalga", "Milliy gvardiyaga.")
t.B("Parij Kommunasiga saylov qachon o‘tkazilgan?", "1871-yil 26-martda", "1871-yil 18-martda", "1871-yil 10-mayda", "1870-yil 4-sentabrda", "26-martda.")
t.B("Kommuna Kengashi nechta komissiya (vazirlik) tashkil etgan?", "10 ta", "5 ta", "20 ta", "72 ta", "10 ta komissiya.")
t.B("Bismark Tyer hukumatiga nechta fransuz askar va zobitini asirlikdan bo‘shatib bergan?", "40 ming", "80 ming", "30 ming", "100 ming", "40 ming.")
t.B("Parij Kommunasi qachon to‘la tor-mor etilgan?", "1871-yil 28-mayda", "1871-yil 21-mayda", "1871-yil 10-mayda", "1871-yil 18-martda", "28-mayda.")
t.B("Parij Kommunasi necha kun yashagan?", "72 kun", "100 kun", "30 kun", "10 kun", "72 kun.")
t.B("Frankfurt sulh shartnomasi qachon imzolangan?", "1871-yil 10-mayda", "1871-yil 28-mayda", "1870-yil 2-sentabrda", "1873-yilda", "1871-yil 10-mayda.")
t.B("Frankfurt shartnomasiga ko‘ra Fransiya qancha tovon to‘lashi kerak edi?", "5 mlrd. frank", "13 mlrd. frank", "1 mlrd. frank", "24 mlrd. frank", "5 mlrd. frank.")
t.NAT("Kommuna Parijdan qochgan Tyer hukumatini ta’qib qilmadi.", "Tyer kuch to‘plab, Parijni qamalga olishga muvaffaq bo‘ldi", "Tyer taslim bo‘ldi", "Kommuna butun Fransiyani egalladi", "Prussiya Kommunani qo‘llab-quvvatladi", "Bu Kommunaning birinchi xatosi edi.")
t.NAT("Parij Kommunasi ag‘darildi.", "Fransiyada inqiloblar davri nihoyasiga yetdi", "Ikkinchi imperiya tiklandi", "Fransiya Germaniyaga qo‘shildi", "inqiloblar kuchaydi", "Kommuna halokati inqiloblar davrini yakunladi.")
t.TF("Parij Kommunasi majburiy va bepul ta’limni joriy etib, maktabni cherkovdan ajratgan.", True, "To‘g‘ri.")
t.TF("Kommuna davlat xazinasi va banklarni to‘la o‘z qo‘liga olgan.", False, "Noto‘g‘ri: bu uning xatolaridan biri edi.")
t.MUL([("Egalari tashlab ketgan korxonalar ishchilarga topshirildi.", True),
       ("Asir olingan 30 mingga yaqin kommunachi otib tashlandi.", True),
       ("Mamlakatning qolgan qismi Kommunani to‘liq qo‘llab-quvvatladi.", False)],
      "III noto‘g‘ri: mamlakatning qolgan qismi Kommunani qo‘llab-quvvatlamadi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Fransiya Respublika deb e’lon qilindi", "Parij qurshab olindi", "18-mart qo‘zg‘oloni", "Kommunaga saylov", "Frankfurt sulhi", "Kommuna tor-mor etildi"],
      "1870-yil 4-sentabr → 19-sentabr → 1871-yil 18-mart → 26-mart → 10-may → 28-may.")
t.MAPMATCH(EU, ['Parij', 'Frankfurt', 'Elzas'],
           ["1871-yilda 72 kun Kommuna hukm surgan shahar", "1871-yil 10-mayda sulh imzolangan nemis shahri", "Frankfurt sulhiga ko‘ra Germaniyaga berilgan viloyat"],
           "1 – Parij; 2 – Frankfurt; 3 – Elzas.")
t.VENN("Tyer hukumati", "Parij Kommunasi",
       [("qarorgohi Versal", 1), ("Bismarkdan 40 ming asirni qaytarib olgan", 1),
        ("10 ta komissiya tashkil etgan", 2), ("maktabni cherkovdan ajratgan", 2),
        ("1871-yil bahorida Fransiyada hokimiyat uchun kurashgan", 3)],
       "Tyer — Versal, Bismark yordami; Kommuna — 10 komissiya, ta’lim islohoti.")

# 5 Fransiyada iqtisodiy va siyosiy hayot
t = Topic('e9j5', 9105); TOPICS['e9j5'] = t
t.B("XIX asr so‘nggi choragida Fransiya sanoat hajmi bo‘yicha qaysi o‘ringa tushib qolgan?", "to‘rtinchi", "ikkinchi", "birinchi", "uchinchi", "Ikkinchidan to‘rtinchi o‘ringa.")
t.B("Prussiya bilan urushda Fransiya qancha zarar ko‘rgan?", "13 mlrd. frank", "5 mlrd. frank", "24 mlrd. frank", "1 mlrd. frank", "13 mlrd. frank.")
t.B("Germaniyaga tovon qachon to‘lab bo‘lingan?", "1873-yilda", "1871-yilda", "1875-yilda", "1880-yilda", "1873-yilda.")
t.B("Uchinchi Respublika Konstitutsiyasi qachon qabul qilingan?", "1875-yilda", "1871-yilda", "1870-yilda", "1884-yilda", "1875-yilda.")
t.B("Konstitutsiyaga ko‘ra parlament necha palatali bo‘lgan?", "ikki palatali", "bir palatali", "uch palatali", "palatasiz", "Deputatlar palatasi va Senat.")
t.B("Parlamentning vakolat muddati necha yil etib belgilangan?", "4 yil", "7 yil", "5 yil", "2 yil", "4 yil.")
t.B("Prezident necha yil muddatga saylangan?", "7 yil", "4 yil", "5 yil", "umrbod", "Parlamentning qo‘shma yig‘ilishi 7 yilga saylagan.")
t.B("Fransiya madhiyasi etib qaysi qo‘shiq belgilangan?", "«Marselyeza»", "«Internatsional»", "«Karmanola»", "«Ode to Joy»", "«Marselyeza».")
t.B("Fransiya xalqining Milliy bayram kuni qaysi sana?", "14-iyul", "4-sentabr", "18-mart", "1-may", "1789-yil Buyuk fransuz inqilobi boshlangan 14-iyul.")
t.B("Saylanadigan qonun chiqaruvchi oliy davlat organi nima?", "parlament", "monarxiya", "respublika", "kommuna", "Parlament.")
t.B("Yakka hukmronlik qanday ataladi?", "monarxiya", "respublika", "oligarxiya", "anarxiya", "Monarxiya.")
t.NAT("Sarmoyadorlar kapitalni chetga katta foiz evaziga chiqarishni afzal ko‘rdi.", "Fransiya iqtisodiy taraqqiyoti sekinlashdi", "Fransiya sanoatda birinchi o‘ringa chiqdi", "ichki bozor kengaydi", "tovon tez to‘landi", "Kapitalning chetga chiqishi iqtisodiy sekinlashuv sabablaridan biri.")
t.NAT("Fransiya aholisining katta qismi monarxiyaga qarshi edi.", "keskin kurashda respublikachilar g‘alaba qozondi", "monarxiya tiklandi", "parlament tarqatildi", "Napoleon III qaytdi", "Monarxiyachilarning urinishlari natijasiz tugadi.")
t.TF("Konstitutsiyaga ko‘ra hukumat a’zolari parlament oldida javobgar bo‘lgan.", True, "To‘g‘ri.")
t.TF("1875-yilgi Konstitutsiya xotin-qizlarga saylov huquqini bergan.", False, "Noto‘g‘ri: xotin-qizlarga saylov huquqi berilmagan.")
t.MUL([("Respublikachilar Milliy Majlisda ozchilikni tashkil etgan.", True),
       ("Prezident urush e’lon qilish, sulh tuzish, umumiy afv e’lon qilish vakolatiga ega edi.", True),
       ("Fransiya tabiiy boyliklarga juda boy davlat edi.", False)],
      "III noto‘g‘ri: Fransiya tabiiy boyliklari kam davlat edi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Buyuk fransuz inqilobi boshlandi", "Frankfurt sulhi", "Tovon to‘lab bo‘lindi", "Uchinchi Respublika Konstitutsiyasi"],
      "1789 → 1871 → 1873 → 1875.")
t.VENN("Prezident vakolatlari", "Parlament vakolatlari",
       [("vazirlarni tayinlash", 1), ("respublika nomidan tashqi siyosat yuritish", 1),
        ("qo‘shma yig‘ilishda prezidentni saylash", 2), ("ikki palatadan iborat bo‘lish", 2),
        ("1875-yilgi Konstitutsiyada belgilangan", 3)],
       "Prezident — vazirlar, tashqi siyosat; parlament — prezidentni saylash, ikki palata.")

# 6 Fransiyaning ichki siyosati
t = Topic('e9j6', 9106); TOPICS['e9j6'] = t
t.B("Ta’lim to‘g‘risidagi qonun qachon qabul qilingan?", "1881–1882-yillarda", "1875-yilda", "1884-yilda", "1906-yilda", "1881–1882-yillarda; maktab cherkovdan ajratildi.")
t.B("Necha yoshgacha bo‘lgan bolalar uchun majburiy bepul ta’lim joriy etilgan?", "13 yoshgacha", "10 yoshgacha", "16 yoshgacha", "18 yoshgacha", "13 yoshgacha.")
t.B("O‘g‘il bolalar uchun qaysi predmet majburiy deb belgilangan?", "gimnastika", "lotin tili", "musiqa", "din", "Gimnastika — bo‘lajak harbiy xizmatga tayyorlash uchun.")
t.B("Kasaba uyushmalari va ish tashlashga ruxsat etuvchi qonun qachon qabul qilingan?", "1884-yilda", "1881-yilda", "1910-yilda", "1897-yilda", "1884-yilda.")
t.B("1885-yilda mustamlakalar haqida nutq so‘zlagan hukumat boshlig‘i kim?", "J. Ferri", "Tyer", "Mak-Magon", "Sadi Karno", "J. Ferri.")
t.B("1876-yilgi saylovlardan keyin iste’fo bergan monarxiya tarafdori prezident kim?", "Mak-Magon", "Tyer", "Sadi Karno", "Troshyu", "Mak-Magon.")
t.B("1894-yilda o‘ldirilgan Fransiya prezidenti kim?", "Sadi Karno", "Mak-Magon", "Tyer", "J. Ferri", "Sadi Karno.")
t.B("Josuslikda nohaq ayblangan kapitan kim?", "A. Dreyfus", "Estergazi", "Troshyu", "Bulanje", "Kapitan A. Dreyfus.")
t.B("Haqiqiy josus kim bo‘lib chiqqan?", "mayor Estergazi", "kapitan Dreyfus", "general Troshyu", "Mak-Magon", "Bosh shtab mayori Estergazi.")
t.B("A. Dreyfus qachon to‘la oqlangan?", "1906-yilda", "1897-yilda", "1894-yilda", "1910-yilda", "1906-yilda.")
t.B("Fransiya eksportida birinchi o‘rinda nima turgan?", "jun", "vino", "shoyi", "ip-gazlama", "Jun, keyin ip-gazlama, shoyi, vino.")
t.B("1914-yilga kelib Fransiya qancha kapital chiqargan?", "24 mlrd. frank", "5 mlrd. frank", "13 mlrd. frank", "100 mlrd. frank", "24 mlrd. frank.")
t.B("«Fransiya ishchi partiyasi» qachon tuzilgan?", "1880-yilda", "1889-yilda", "1871-yilda", "1906-yilda", "1880-yilda.")
t.B("1910-yilgi qonunga ko‘ra Fransiyada pensiya yoshi qancha belgilangan?", "65 yosh", "70 yosh", "60 yosh", "55 yosh", "65 yosh (Germaniya va Britaniyada 70).")
t.B("Har qanday hokimiyatni rad etuvchi ta’limot qanday ataladi?", "anarxizm", "shovinizm", "monarxizm", "liberalizm", "Anarxizm.")
t.B("O‘taketgan millatchilik qanday ataladi?", "shovinizm", "anarxizm", "reaksiya", "imperializm", "Shovinizm.")
t.NAT("Haqiqiy josus aniqlangani 1897-yilda matbuotda e’lon qilindi.", "demokratik kuchlar Dreyfus ishini qayta ko‘rishni talab qildi", "Dreyfus qatl etildi", "Estergazi mukofotlandi", "ish yopib qo‘yildi", "Demokratik kuchlar ishni qayta ko‘rishni talab etdi.")
t.NAT("XIX asr 90-yillari o‘rtalaridan iqtisodiy yuksalish boshlandi.", "XX asr boshida mamlakatda siyosiy barqarorlik ta’minlandi", "Fransiya inqirozga tushdi", "Kommuna tiklandi", "eksport to‘xtadi", "Iqtisodiy yuksalish barqarorlikni ta’minladi.")
t.TF("Temir rudasi qazib chiqarish bo‘yicha Fransiya AQSH va Germaniyani ortda qoldirgan.", True, "To‘g‘ri.")
t.TF("Chetga kapital chiqarish bo‘yicha Fransiya dunyoda birinchi o‘rinda bo‘lgan.", False, "Noto‘g‘ri: Buyuk Britaniyadan keyin ikkinchi o‘rinda.")
t.MUL([("Mamlakatda radikallar, sotsialistlar va respublikachilar partiyalari yetakchi nufuzga ega edi.", True),
       ("Mehnat Kodeksiga ko‘ra haftada bir kun dam olish kuni joriy etildi.", True),
       ("Anarxistlar islohotlar yo‘lini tanlab, terrorni rad etgan.", False)],
      "III noto‘g‘ri: anarxistlar kurashning terror usulini qo‘llagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Ta’lim to‘g‘risidagi qonun", "Kasaba uyushmalari haqidagi qonun", "Prezident Sadi Karno o‘ldirildi", "Haqiqiy josus haqida matbuotda e’lon qilindi", "Dreyfus to‘la oqlandi", "Pensiya haqidagi qonun"],
      "1881–1882 → 1884 → 1894 → 1897 → 1906 → 1910.")
t.VENN("Dreyfus", "Estergazi",
       [("nohaq umrbod surgunga hukm qilingan", 1), ("1906-yilda to‘la oqlangan", 1),
        ("haqiqiy josus bo‘lib chiqqan", 2), ("Fransiyadan qochib ketgan", 2),
        ("Fransiya armiyasi zobiti", 3)],
       "Dreyfus — nohaq ayblangan, oqlangan; Estergazi — haqiqiy josus, qochgan.")
