from qlib import Topic
TOPICS = {}
EU = 'europe'

# 36 1916–1917-yillardagi urush harakatlari
t = Topic('e9j36', 9136); TOPICS['e9j36'] = t
t.B("Germaniya Fransiyaning qaysi qal’asiga hujum uyushtirgan?", "Verden", "Mets", "Sedan", "Ipr", "Verden — Parijning yo‘lini to‘sib turgan qal’a.")
t.B("Germaniyaning Verdenga hujumi qachon boshlangan?", "1916-yil 21-fevralda", "1916-yil 21-dekabrda", "1915-yil aprelida", "1917-yil 6-aprelda", "1916-yil 21-fevralda.")
t.B("Verden yo‘nalishida nemis qo‘shini atigi qancha oldinga siljigan?", "7 km", "70 km", "700 m", "30 km", "Atigi 7 km.")
t.B("Inglizlar birinchi bor tankni qaysi jangda ishga solgan?", "Somma daryosi bo‘yidagi jangda", "Verden jangida", "Marna jangida", "Ipr jangida", "Somma jangida.")
t.B("Verden jangi qachon nihoyasiga yetgan?", "1916-yil 21-dekabrda", "1916-yil 21-martda", "1917-yil aprelida", "1916-yil noyabrida", "21-dekabrda.")
t.B("Verden va Somma janglarida har ikki tomondan qancha jangchi halok bo‘lgan?", "2 milliondan ortiq", "200 ming", "850 ming", "10 million", "2 milliondan ortiq.")
t.B("Verden jangi tarixga qanday nom bilan kirgan?", "«Verden qirg‘ini»", "«Nevel qirg‘ini»", "«Buyuk chekinish»", "«Marna mo‘jizasi»", "«Verden qirg‘ini».")
t.B("Galitsiyadagi Avstriya-Vengriya frontini qaysi rus generali yorib o‘tgan?", "A. A. Brusilov", "Gindenburg", "Fosh", "Nevel", "General A. A. Brusilov.")
t.B("Brusilov hujumida Avstriya-Vengriya qo‘shinidan qancha jangchi halok bo‘lgan?", "1 milliondan ortiq", "400 ming", "850 ming", "100 ming", "1 milliondan ortiq; 400 mingdan ortig‘i asir olindi.")
t.B("Ruminiya Avstriya-Vengriyaga qachon urush e’lon qilgan?", "1916-yil 28-avgustda", "1914-yil oktabrida", "1917-yil aprelida", "1915-yil mayida", "1916-yil 28-avgustda.")
t.B("Ruminiyaga qaysi hududlar va’da qilingan?", "Transilvaniya, Bukovina va Banatning katta qismi", "Bosniya va Gersegovina", "Galitsiya", "Bolgariya", "Transilvaniya, Bukovina va Banat.")
t.B("1917-yilda Antanta qurolli kuchlarining son jihatidan ustunligi qancha edi?", "40%", "10%", "2 baravar", "5%", "40%.")
t.B("1916-yil avgustida Germaniya qo‘shini qo‘mondoni etib kim tayinlangan?", "fon Gindenburg", "fon Shliffen", "Brusilov", "Fosh", "General-feldmarshal fon Gindenburg.")
t.B("1915-yilda AQSH Britaniya va Fransiyaga qancha qarz berish shartnomasini imzolagan?", "500 mln dollar", "10 mlrd dollar", "50 mln funt", "6 mlrd marka", "500 mln dollar.")
t.B("Yevropadagi 20 davlatning AQSHdan qarzi qanchani tashkil etgan?", "10 mlrd dollar", "500 mln dollar", "132 mlrd marka", "1 mlrd dollar", "10 mlrd dollar.")
t.B("AQSH Germaniyaga qachon urush e’lon qilgan?", "1917-yil 6-aprelda", "1916-yil 28-avgustda", "1918-yil martda", "1914-yil avgustida", "1917-yil 6-aprelda.")
t.NAT("1917-yil fevralidan Germaniya cheklanmagan suvosti urushi e’lon qildi va bu AQSH manfaatlariga zarar yetkazdi.", "AQSH Germaniyaga urush e’lon qildi", "AQSH betaraf qoldi", "AQSH Germaniya bilan ittifoq tuzdi", "Britaniya urushdan chiqdi", "AQSHning urushga kirishi urush taqdirini Antanta foydasiga hal etdi.")
t.NAT("Germaniya 1916-yil fevralida G‘arbiy frontda hujumga o‘tgach, Fransiya Rossiyadan yordam so‘radi.", "Brusilov qo‘mondonligidagi rus qo‘shini may oyida hujumga o‘tdi", "Rossiya urushdan chiqdi", "Fransiya taslim bo‘ldi", "Italiya urushga kirmadi", "Brusilov yorib o‘tishi boshlandi.")
t.TF("Harbiy jihatdan tayyor bo‘lmagan Ruminiya armiyasi tezda tor-mor etilgan.", True, "To‘g‘ri.")
t.TF("Urush boshidanoq AQSH Germaniya tarafida urushga kirgan.", False, "Noto‘g‘ri: AQSH betaraflik e’lon qilgan, keyin Antantaga yordam berib, 1917-yilda Germaniyaga urush e’lon qilgan.")
t.MUL([("1914-yil oktabridagi shartnomaga ko‘ra Rossiya Ruminiyaning hududiy yaxlitligini kafolatlagan.", True),
       ("Bir yildan so‘ng G‘arbiy frontdagi AQSH qo‘shinlari soni 2 mln kishiga yetgan.", True),
       ("Gindenburg rejasi front chizig‘ini kengaytirishni nazarda tutgan.", False)],
      "III noto‘g‘ri: reja front chizig‘ini kamaytirishni nazarda tutgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Rossiya–Ruminiya shartnomasi", "AQSHning 500 mln dollarlik qarz shartnomasi", "Verdenga hujum boshlandi", "Ruminiya urush e’lon qildi", "Verden jangi tugadi", "AQSH Germaniyaga urush e’lon qildi"],
      "1914 → 1915 → 1916-yil fevral → 28-avgust → 21-dekabr → 1917-yil 6-aprel.")
t.MAPMATCH(EU, ['Verden', 'Galitsiya', 'Ruminiya'],
           ["1916-yilda «qirg‘in» bo‘lgan, Parij yo‘lini to‘sgan qal’a", "Brusilov Avstriya-Vengriya frontini yorib o‘tgan hudud", "1916-yil 28-avgustda Avstriya-Vengriyaga urush e’lon qilgan davlat"],
           "1 – Verden; 2 – Galitsiya; 3 – Ruminiya.")
t.VENN("Verden jangi", "Somma jangi",
       [("Germaniya hujumi bilan boshlangan", 1), ("nemislar atigi 7 km siljigan", 1),
        ("fransuz va ingliz qo‘shinlari hujumi", 2), ("birinchi marta tank ishlatilgan", 2),
        ("1916-yilgi qirg‘inbarot jang", 3)],
       "Verden — nemis hujumi; Somma — Antanta hujumi, tank; ikkalasi 1916-yilda.")

# 37 Birinchi jahon urushining yakunlari va oqibatlari
t = Topic('e9j37', 9137); TOPICS['e9j37'] = t
t.B("Urush davrida oziq-ovqat tanqisligi sababli hukumatlar nima joriy etgan?", "kartochka tartibi", "erkin savdo", "bojsiz savdo", "oltin standart", "Kartochka tartibi.")
t.B("1917-yil fevralda Rossiyada nima yuz bergan?", "inqilob, imperator taxtdan voz kechgan", "Brest shartnomasi", "davlat to‘ntarishi va bolsheviklar hokimiyati", "Germaniya bilan ittifoq", "Fevral inqilobi.")
t.B("Muvaqqat hukumat qachon ag‘darilgan?", "1917-yil 7-noyabrda", "1917-yil fevralda", "1918-yil 3-martda", "1917-yil 8-noyabrda", "7-noyabrda.")
t.B("Sovet davlati «Sulh to‘g‘risida»gi dekretni qachon qabul qilgan?", "1917-yil 8-noyabrda", "1917-yil 7-noyabrda", "1918-yil 3-martda", "1917-yil dekabrida", "8-noyabrda.")
t.B("1917-yil aprelida Antanta hujumi kimning nomi bilan «qirg‘in» deb atalgan?", "Nevel", "Verden", "Fosh", "Brusilov", "«Nevel qirg‘ini».")
t.B("1917-yil noyabrida Germaniya qanday yangi qurol qo‘llagan?", "ognemyot", "tank", "xlor gazi", "suvosti kemasi", "Ognemyot.")
t.B("Inglizlar Bag‘dod shahrini qachon egallagan?", "1917-yil martida", "1918-yil martida", "1916-yilda", "1917-yil noyabrida", "1917-yil martida.")
t.B("Brest tinchlik shartnomasi qachon imzolangan?", "1918-yil 3-martda", "1917-yil dekabrida", "1918-yil 11-noyabrda", "1919-yil 28-iyunda", "1918-yil 3-martda.")
t.B("Brest shartnomasiga ko‘ra Rossiya Germaniyaga qancha reparatsiya to‘lashi kerak edi?", "6 mlrd marka", "132 mlrd marka", "5 mlrd frank", "10 mlrd dollar", "6 mlrd marka.")
t.B("Brest shartnomasiga ko‘ra Kars, Ardagan va Batumi kimga berilgan?", "Usmonli davlatiga", "Germaniyaga", "Ukrainaga", "Britaniyaga", "Usmonli davlatiga.")
t.B("1918-yil yanvarida AQSH prezidentining nuqtayi nazari tarixga qanday nom bilan kirgan?", "«Vilson tinchlik dasturi»", "«Monro doktrinasi»", "«Ochiq eshiklar»", "«Dollar diplomatiyasi»", "«Vilson tinchlik dasturi».")
t.B("Birlashgan kuchlar qo‘mondoni etib kim tayinlangan?", "marshal Fosh", "Nevel", "Gindenburg", "Brusilov", "Fransiya marshali Fosh.")
t.B("Avstriya-Vengriya Antanta bilan yarash shartnomasini qachon imzolagan?", "3-noyabrda", "9-noyabrda", "11-noyabrda", "sentabrda", "1918-yil 3-noyabrda.")
t.B("Germaniya imperiyasi qachon qulagan?", "1918-yil 9-noyabrda", "1918-yil 11-noyabrda", "1918-yil 3-noyabrda", "1919-yil 28-iyunda", "9-noyabrda; Vilgelm II taxtdan voz kechdi.")
t.B("Germaniyaning taslim bo‘lishi haqidagi bitim qayerda imzolangan?", "Kompyen o‘rmonida, Fosh vagonida", "Versal saroyida", "Brestda", "Parijda", "Kompyen o‘rmonida, 11-noyabrda.")
t.B("Versalda sulh shartnomasi qachon imzolangan?", "1919-yil 28-iyunda", "1918-yil 11-noyabrda", "1918-yil 3-martda", "1920-yilda", "1919-yil 28-iyunda.")
t.B("Versal shartnomasiga ko‘ra Germaniya qancha reparatsiya to‘lashi kerak edi?", "132 mlrd marka", "6 mlrd marka", "5 mlrd frank", "10 mlrd dollar", "132 mlrd marka.")
t.B("Birinchi jahon urushida nechta davlat ishtirok etgan?", "38 ta", "8 ta", "20 ta", "100 ta", "38 davlat, 1,5 mlrd dan ortiq aholi.")
t.B("Urushda jami qancha kishi halok bo‘lgan?", "10 mln ga yaqin", "74 mln", "20 mln", "2 mln", "10 mln ga yaqin; 20 mln dan ortiq yarador.")
t.NAT("Sovet hukumati qo‘shini jangovar ruhini yo‘qotgan sharoitda separat sulh tuzishga intildi.", "1918-yil 3-martda og‘ir shartli Brest tinchlik shartnomasi imzolandi", "Rossiya urushni g‘alaba bilan tugatdi", "Antanta Rossiyaga yordam berdi", "Germaniya Rossiyaga hududlarini qaytardi", "Rossiya Boltiqbo‘yi, Polsha, Finlandiya, Ukrainadan voz kechdi.")
t.NAT("Urush Germaniyada inqilobiy vaziyatni vujudga keltirdi.", "Germaniya imperiyasi quladi, Vilgelm II mamlakatdan qochdi", "Vilgelm II kuchaydi", "Germaniya g‘alaba qozondi", "Bolsheviklar Germaniyani egalladi", "9-noyabrda imperiya quladi.")
t.TF("Urushning asosiy ishtirokchilari o‘z milliy boyliklarining uchdan bir qismini yo‘qotgan.", True, "To‘g‘ri.")
t.TF("Urush davrida parlamentlar qonli qirg‘inga qarshi doimiy norozilik bildirgan.", False, "Noto‘g‘ri: bironta ham parlament norozilik bildirmagan.")
t.MUL([("Urushga 74 mln ga yaqin kishi safarbar etilgan.", True),
       ("Brest shartnomasi Ukraina va Finlandiyani mustaqil davlatlar deb tan olgan.", True),
       ("Bolgariya urushdan oxirgi bo‘lib chiqqan.", False)],
      "III noto‘g‘ri: Bolgariya sentabrda birinchilardan bo‘lib urushdan chiqdi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Bolsheviklar hokimiyatni egalladi", "«Sulh to‘g‘risida»gi dekret", "Brest tinchlik shartnomasi", "Avstriya-Vengriya urushdan chiqdi", "Germaniya imperiyasi quladi", "Kompyen bitimi", "Versal shartnomasi"],
      "1917-yil 7-noyabr → 8-noyabr → 1918-yil 3-mart → 3-noyabr → 9-noyabr → 11-noyabr → 1919-yil 28-iyun.")
t.MAPN(EU, ['Versal', 'Vena', 'Brest', 'Berlin'], "Qaysi raqam bilan 1918-yil 3-martda Sovet Rossiyasi To‘rtlar ittifoqi bilan tinchlik shartnomasini imzolagan joy belgilangan?",
       "3 – Brest; 1 – Versal: 1919-yil 28-iyunda sulh shartnomasi imzolangan.", ask_idx=2)
t.VENN("Brest tinchlik shartnomasi", "Versal shartnomasi",
       [("Sovet Rossiyasi va To‘rtlar ittifoqi o‘rtasida", 1), ("6 mlrd marka reparatsiya", 1),
        ("1919-yil 28-iyunda imzolangan", 2), ("132 mlrd marka reparatsiya", 2),
        ("mag‘lub tomonga og‘ir shartlar qo‘yilgan", 3)],
       "Brest — Rossiya, 6 mlrd; Versal — Germaniya, 132 mlrd.")
