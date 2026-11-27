from qlib import Topic
TOPICS = {}
UZ = 'uzb'

# 40 Teatr va musiqa san’ati
t = Topic('e9u40', 9040); TOPICS['e9u40'] = t
t.B("Xorazm an’anaviy teatrida qanday ikki turkum tomoshalar shakllangan?", "kulgili va xatarli o‘yinlar", "opera va balet", "drama va tragediya", "qo‘g‘irchoq va soya", "Kulgili va xatarli o‘yin turlari.")
t.B("XIX asr ikkinchi yarmida Qo‘qondagi mashhur an’anaviy teatr uyushmasi kimniki edi?", "Zokir eshon", "To‘la masxara", "Hamza", "Mannon Uyg‘ur", "Qo‘qonda Zokir eshon uyushmasi.")
t.B("Buxorodagi mashhur an’anaviy teatr uyushmasi kimniki edi?", "To‘la masxara", "Zokir eshon", "Abdulla Avloniy", "Behbudiy", "Buxoroda To‘la masxara.")
t.B("Qo‘g‘irchoq teatrlarining markazida qaysi obraz turgan?", "Kachal Polvon", "O‘mirbek laqqi", "Nasriddin afandi", "Alpomish", "Kachal Polvon.")
t.B("1870-yilda Turkiston general-gubernatori qaysi teatrni taklif qilgan?", "Samara teatrini", "Moskva Katta teatrini", "Qozon teatrini", "Boku teatrini", "Samara teatrini.")
t.B("1910-yilda Samarqand va Toshkentda kimning truppasi gastrol qilgan?", "V. F. Komissarjevskaya", "U. Gajibekov", "Mannon Uyg‘ur", "Hamza", "Rus aktrisasi V. F. Komissarjevskaya truppasi.")
t.B("«Arshin mol olon» musiqali pyesasi muallifi kim?", "U. Gajibekov", "Behbudiy", "Hamza", "Fitrat", "U. Gajibekov.")
t.B("«Teatr — bu ibratxonadir» degan ma’rifatparvar kim?", "Mahmudxo‘ja Behbudiy", "Abdulla Avloniy", "Hamza", "Munavvarqori", "Mahmudxo‘ja Behbudiy.")
t.B("Dastlabki yozma milliy sahna asarlari qachon yaratilgan?", "1911-yilda", "1914-yilda", "1916-yilda", "1870-yilda", "1911-yilda.")
t.B("«Mahramlar» asari muallifi kim?", "A. Samadov", "Behbudiy", "Fitrat", "Hamza", "A. Samadov.")
t.B("Birinchi o‘zbek milliy teatri qaysi shaharda tashkil etilgan?", "Samarqandda", "Toshkentda", "Qo‘qonda", "Buxoroda", "Samarqandda Behbudiy rahbarligida.")
t.B("1914-yil boshlarida Toshkentda «Turon» teatr truppasini kim tashkil etgan?", "Abdulla Avloniy", "Hamza", "Behbudiy", "Mannon Uyg‘ur", "Abdulla Avloniy.")
t.B("1916-yilda Qo‘qonda havaskorlar teatrini kim tashkil etgan?", "Hamza Hakimzoda Niyoziy", "Abdulla Avloniy", "Zokir eshon", "Behbudiy", "Hamza rahbarligida.")
t.B("Hamza teatrida namoyish etilgan birinchi spektakl qaysi?", "«Zaharli hayot yoxud ishq qurbonlari»", "«Padarkush»", "«Mahramlar»", "«To‘y»", "Hamzaning «Zaharli hayot yoxud ishq qurbonlari».")
t.B("O‘zbek teatrining birinchi aktrisasi kim?", "Ma’suma Qoriyeva", "Anbar otin", "Rizvonbibi", "Tamaraxonim", "Ma’suma Qoriyeva.")
t.B("Birinchi o‘zbek kino va fotooperatori kim?", "Xudoybergan Devonov", "Mannon Uyg‘ur", "Vilgelm Penner", "Hamza", "Xudoybergan Devonov (1878–1940).")
t.B("Xudoybergan Devonov qachon suratga ola boshlagan?", "1903-yilda", "1878-yilda", "1910-yilda", "1882-yilda", "1903-yilda Xivada.")
t.B("Xorazm maqomlarini xalqning daxlsiz mulki deb e’lon qilgan farmon qachon chiqarilgan?", "1882-yilda", "1903-yilda", "1910-yilda", "1873-yilda", "1882-yilda Muhammad Rahimxon II (Feruz) farmoni.")
t.B("Muhammad Rahimxon II qanday taxallus bilan ma’lum?", "Feruz", "Munis", "Ogahiy", "Zevar", "Feruz.")
t.NAT("Tatar va ozarbayjon truppalari 1910–1912-yillarda Turkistonda gastrollarda bo‘ldi.", "bu mahalliy teatr rivojlanishiga katta ta’sir ko‘rsatdi", "mahalliy teatr yopildi", "teatr taqiqlandi", "jadidlar teatrdan voz kechdi", "Gajibekov pyesalari iliq kutib olinib, mahalliy teatrga ta’sir qildi.")
t.TF("Xalq teatri tomoshalarida xasis boylar, chalasavod mullalar, amalparast beklarning kirdikorlari fosh etilgan.", True, "To‘g‘ri.")
t.TF("Xalq dostonlari musiqasida nota yozuvi keng qo‘llanilgan.", False, "Noto‘g‘ri: bu musiqada nota yozuvi qo‘llanilmagan.")
t.MUL([("Avloniyning «Turon» truppasi sahnalashtirgan birinchi asar «Padarkush» bo‘lgan.", True),
       ("Karnay, nog‘ora, doira an’anaviy bayram va to‘ylarda jo‘rovoz bo‘lgan.", True),
       ("Chang puflama nayli cholg‘u asbobi hisoblanadi.", False)],
      "III noto‘g‘ri: chang torli-zarbli cholg‘u asbobi.")
t.MATCH("Cholg‘u asboblarini turlari bilan moslashtiring.", ["g‘ijjak", "chang", "surnay", "doira"],
        ["zarbli-membranali", "torli-zarbli", "torli-kamonchali", "puflama nayli"], "cbda",
        "G‘ijjak — torli-kamonchali; chang — torli-zarbli; surnay — puflama nayli; doira — zarbli-membranali.")
t.MAPMATCH(UZ, ['Samarqand', 'Toshkent', 'Qo‘qon'],
           ["Behbudiy rahbarligida birinchi o‘zbek milliy teatri tashkil etilgan shahar", "1914-yilda Avloniy «Turon» truppasini tuzgan shahar", "1916-yilda Hamza havaskorlar teatrini tuzgan shahar"],
           "1 – Samarqand; 2 – Toshkent; 3 – Qo‘qon.")
t.VENN("Abdulla Avloniy", "Hamza Hakimzoda Niyoziy",
       [("«Turon» truppasini tashkil etgan", 1), ("Toshkentda faoliyat yuritgan", 1),
        ("Qo‘qonda havaskorlar teatrini tuzgan", 2), ("«Zaharli hayot» pyesasi muallifi", 2),
        ("o‘zbek milliy teatri rivojiga katta hissa qo‘shgan", 3)],
       "Avloniy — «Turon», Toshkent; Hamza — Qo‘qon, «Zaharli hayot».")

# 41 Me’morchilik va tasviriy san’at
t = Topic('e9u41', 9041); TOPICS['e9u41'] = t
t.B("XX asr boshlarida barpo etilgan Buxoro amirining yozgi saroyi qaysi?", "Sitorai Mohi Xosa", "Nurullaboy saroyi", "Xudoyorxon saroyi", "Ark", "Sitorai Mohi Xosa.")
t.B("Sitorai Mohi Xosa Buxoro markazidan qancha masofada joylashgan?", "2,5 km janubda", "15 km g‘arbda", "25 km shimolda", "1 km sharqda", "Buxoro markazidan 2,5 km janubda.")
t.B("Sitorai Mohi Xosaning Oq zaliga pardoz berish ishiga kim boshchilik qilgan?", "Usta Shirin Murodov", "Odina Muhammad Murod", "Obloqul Hofizov", "Nurmuhammad", "Usta Shirin Murodov.")
t.B("Xorazm me’morchilik maktabining sarkori kim bo‘lgan?", "Odina Muhammad Murod", "Shirin Murodov", "Mo‘minjon Solihov", "Ibrohim Hofizov", "Odina Muhammad Murod.")
t.B("Islom xo‘ja minorasi qachon tiklangan?", "1908–1910-yillarda", "1904–1912-yillarda", "1851–1855-yillarda", "1882-yilda", "1908–1910-yillarda.")
t.B("Islom xo‘ja minorasining tashabbuskori va homiysi kim?", "Asfandiyorxonning bosh vaziri Islom xo‘ja", "Muhammad Rahimxon II", "Amir Olimxon", "Junaidxon", "Bosh vazir Islom xo‘ja.")
t.B("Nurullaboy saroyini kim qurdirgan?", "Muhammad Rahimxon II", "Asfandiyorxon", "Amir Olimxon", "Islom xo‘ja", "Muhammad Rahimxon II (1904–1912).")
t.B("Nurullaboy saroyi necha xonadan iborat?", "yetti xonadan", "yuzdan ortiq xonadan", "uch xonadan", "o‘n ikki xonadan", "Yetti xona.")
t.B("Nurullaboy saroyiga ikkita qandil va nurquvvat uskunasini kim sovg‘a qilgan?", "Nikolay II", "Aleksandr III", "Kaufman", "Amir Olimxon", "Rus podshosi Nikolay II.")
t.B("XIX asr oxirida qurilgan qaysi masjid yuksak milliy me’morchilik namunasi bo‘lib qoldi?", "Andijon jome masjidi", "Tillashayx masjidi", "Bolo hovuz masjidi", "Juma masjidi", "Andijon jome masjidi.")
t.B("Naqsh amaliy san’atining markazi qaysi shahar edi?", "Buxoro", "Xiva", "Samarqand", "Qo‘qon", "Buxoro.")
t.B("Buxoro naqshlarida oq rang nimaning ramzi bo‘lgan?", "baxt-saodat va omad", "quvonch va salomatlik", "motam", "kuch-qudrat", "Oq — baxt-saodat va omad; qizil — quvonch va salomatlik.")
t.B("Tasviriy san’atda qaysi miniaturachilar ijodi ajralib turgan?", "Ahmad Donish, Abdulxoliq maxdum, S. Siddiqov", "Muqimiy, Zavqiy", "Behbudiy, Avloniy", "Berdaq, Ajiniyoz", "Ahmad Donish, Abdulxoliq maxdum, S. Siddiqov.")
t.NAT("XX asr boshlarida devoriy naqshlarga yangi manzaralar kirib keldi.", "suzib borayotgan kema, temiryo‘llar va hayvonlar tasvirlana boshlandi", "naqqoshlik butunlay yo‘qoldi", "faqat arabiy yozuvlar qoldi", "naqshlar taqiqlandi", "Ilgari uchramagan manzaralar paydo bo‘ldi.")
t.NAT("Turkistonda iqtisodiy tanazzul, o‘zaro urushlar va Rossiya yurishlari bo‘ldi.", "bu madaniy taraqqiyotga, jumladan me’morchilikka ham salbiy ta’sir ko‘rsatdi", "me’morchilik tez rivojlandi", "yangi shaharlar qurildi", "madaniyat gullab-yashnadi", "Ular madaniy taraqqiyotga salbiy ta’sir ko‘rsatdi.")
t.TF("Xorazm me’morchiligida peshtoq, ship va burjlar arabiy yozuvlar bilan bezatilgan.", True, "To‘g‘ri.")
t.TF("Sitorai Mohi Xosaning Oq zali faqat sharqona uslubda qurilgan.", False, "Noto‘g‘ri: Oq zal qurilishida Yevropacha uslub ustunlik qiladi.")
t.MUL([("Qurilishda paxsa, guvala, xom g‘isht bilan birga faner, tunuka, oyna ishlatila boshlandi.", True),
       ("Toshkentning Yangi shahar qismida g‘arb uslubidagi ma’muriy binolar qad ko‘tardi.", True),
       ("Amir Olimxon chet el elchilarini faqat Arkda qabul qilgan.", False)],
      "III noto‘g‘ri: amir elchilarni Sitorai Mohi Xosada ham qabul qilgan.")
t.MATCH("Inshootlarni ularga oid ma’lumotlar bilan moslashtiring.", ["Sitorai Mohi Xosa", "Nurullaboy saroyi", "Islom xo‘ja minorasi", "Andijon jome masjidi"],
        ["1908–1910-yillarda Xivada tiklangan", "XIX asr oxiridagi yuksak milliy me’morchilik namunasi", "Buxoro amirining yozgi qarorgohi", "yetti xonali, Nikolay II qandil sovg‘a qilgan"], "cdab",
        "Sitorai Mohi Xosa — amir qarorgohi; Nurullaboy — 7 xona; minora — 1908–1910; Andijon jome masjidi — milliy namuna.")
t.MAPMATCH(UZ, ['Buxoro', 'Xiva', 'Andijon'],
           ["Sitorai Mohi Xosa joylashgan, naqsh amaliy san’ati markazi", "Islom xo‘ja minorasi va Nurullaboy saroyi joylashgan shahar", "XIX asr oxirida jome masjidi qurilgan Farg‘ona vodiysi shahri"],
           "1 – Buxoro; 2 – Xiva; 3 – Andijon.")
t.VENN("Sitorai Mohi Xosa", "Nurullaboy saroyi",
       [("Buxoro amirining yozgi qarorgohi", 1), ("Oq zali Shirin Murodov boshchiligida bezatilgan", 1),
        ("Muhammad Rahimxon II qurdirgan", 2), ("yetti xonadan iborat", 2),
        ("Yevropa me’morchiligi uslublari ko‘zga tashlanadi", 3)],
       "Sitorai Mohi Xosa — Buxoro, Oq zal; Nurullaboy — Xiva, 7 xona; ikkalasida Yevropa uslubi.")
