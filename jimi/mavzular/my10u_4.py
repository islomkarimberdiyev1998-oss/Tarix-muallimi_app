from qlib import Topic, PLACES, REG
TOPICS = {}

# 8-mavzu. Buxoro amirligi XIX asr 2-yarmi – XX asr boshi
t = Topic('y10u8', 10008); TOPICS['y10u8'] = t
t.B("XIX asr oxirida Buxorodan tashqari amirlikning yirik savdo-hunarmandchilik markazlari qaysilar?", "Chorjo‘y, Kitob, Shahrisabz, Denov", "Xiva, Urganch", "Qo‘qon, Andijon", "Toshkent, Chimkent", "Chorjo‘y, Kitob, Shahrisabz, Denov.")
t.B("Baljuvonlik dehqonlar mo‘l hosilni qaysi yili yig‘ib olgan?", "1885-yilda", "1888-yilda", "1873-yilda", "1898-yilda", "1885-yilda.")
t.B("Baljuvon qo‘zg‘oloni qachon ko‘tarilgan?", "1885-yil iyul oxirida", "1888-yilda", "1892-yil iyunda", "1916-yilda", "1885-yil iyul oyining oxirgi kunlarida.")
t.B("Baljuvon qo‘zg‘olonchilari qaysi amirning lashkari bilan jang qilgan?", "amir Muzaffar", "amir Olimxon", "amir Abdulahadxon", "amir Nasrulla", "Amir Muzaffar.")
t.B("1888-yilda qaysi viloyatda dehqonlarning norozilik harakati boshlangan?", "Ko‘lob", "Baljuvon", "Chorjo‘y", "Hisor", "Ko‘lob viloyatida.")
t.B("Ichki va tashqi bozorda talab katta bo‘lgan Buxoro mahsuloti qaysi?", "gilamlar", "paxta tolasi", "neft", "ko‘mir", "Buxoro gilamlari.")
t.B("Amirlik hududi orqali dastlabki temiryo‘l qachon o‘tkazilgan?", "1888-yilda", "1873-yilda", "1898-yilda", "1906-yilda", "1888-yilda.")
t.B("Yangi Buxoro stansiyasi Buxorodan qancha masofada qurilgan?", "15 kilometr", "50 kilometr", "1 kilometr", "100 kilometr", "15 km.")
t.B("Yangi Buxoroda nimalar barpo etilgan?", "amir saroyi va Rossiya siyosiy agenti qarorgohi", "Ark va Minorayi kalon", "madrasa va masjid", "zavod va kon", "Amir saroyi va siyosiy agent qarorgohi.")
t.B("Eski Buxorodagi qo‘shbegi uyi va siyosiy agentlik nima orqali bog‘langan?", "telefon aloqasi", "telegraf", "temiryo‘l", "kanal", "Ilk telefon aloqasi.")
t.B("Bu davrda Buxoroda nechtaga yaqin an’anaviy maktab bo‘lgan?", "350 ga yaqin", "35 ga yaqin", "3500 ga yaqin", "100 ga yaqin", "350 ga yaqin.")
t.B("Buxoroda maktabxonaga qabul qilish yoshi qanday bo‘lgan?", "5 yoshdan 12 yoshgacha", "7 yoshdan 13 yoshgacha", "10 yoshdan 40 yoshgacha", "3 yoshdan 5 yoshgacha", "5–12 yosh.")
t.B("Maktabxonada ta’lim necha yil davom etgan?", "7–10 yilgacha", "2–3 yil", "1 yil", "15–20 yil", "7–10 yil.")
t.B("Qizlarning o‘qishi necha yoshda boshlanib, necha yoshda tugagan?", "7 yoshda boshlanib, 13 yoshda", "5 yoshda boshlanib, 12 yoshda", "10 yoshda boshlanib, 20 yoshda", "6 yoshda boshlanib, 16 yoshda", "7–13 yosh.")
t.B("Buxoro musulmon aholisining savodxonligini Rossiyaga namuna qilib ko‘rsatgan rus olimi kim?", "A. Middendorf", "N. Ostroumov", "V. Bartold", "N. Korolkov", "A. Middendorf.")
t.NAT("Soliq yig‘uvchilar o‘tgan kamhosil yillar uchun ham xiroj talab qildi.", "baljuvonlik dehqonlar soliqni to‘lashdan bosh tortib, qo‘zg‘olon ko‘tardi", "dehqonlar soliqni ikki baravar to‘ladi", "amir soliqni bekor qildi", "dehqonlar ko‘chib ketdi", "1885-yilgi Baljuvon qo‘zg‘oloni.")
t.NAT("Hunarmandlar daromadining aksariyati behisob soliqlarga ketardi.", "ustaxonalarni rivojlantirish uchun qo‘shimcha mablag‘ qolmadi", "hunarmandchilik tez rivojlandi", "fabrikalar qurildi", "hunarmandlar boyidi", "Rivojlanish uchun mablag‘ yo‘q edi.")
t.NAT("1888-yilda amirlik orqali temiryo‘l o‘tkazildi.", "Buxoro Toshkent, Orenburg va Moskva bilan temiryo‘l orqali bog‘landi", "savdo to‘xtadi", "Buxoro Rossiyadan uzildi", "karvon yo‘llari kengaydi", "Temiryo‘l aloqasi.")
t.NAT("Tayyorgarliksiz, mehnat qurollari bilan chiqqan dehqonlar amir lashkariga qarshi jang qildi.", "qo‘zg‘olonchilar mag‘lub bo‘lib, qatl etildi", "dehqonlar g‘alaba qozondi", "amir taxtdan voz kechdi", "soliqlar bekor qilindi", "Mag‘lubiyat.")
t.TF("Buxoroda Rossiya davlat banki bo‘limi va paxta tozalash zavodi barpo etilgan.", True, "To‘g‘ri.")
t.TF("Buxoroda qizlarning darslari kechgacha davom etgan.", False, "Noto‘g‘ri: qizlar maktabida darslar tushlikkacha davom etgan.")
t.TF4([("Amirlik iqtisodining asosiy qismini qishloq xo‘jaligi tashkil etgan.", True), ("O‘g‘il bolalar maktablarining aksariyati masjidlar qoshida bo‘lgan.", True),
       ("Maktablarning moddiy asosini vaqf mulklari tashkil etgan.", True), ("Buxoro hududi tranzit savdo uchun noqulay bo‘lgan.", False)],
      "4-noto‘g‘ri: tranzit savdo uchun qulay bo‘lgan.")
t.MUL([("Buxoro zargarlik mahsulotlari nozik naqshlar bilan bezatilgan.", True),
       ("Ko‘lobdagi norozilik harakati amir tomonidan bostirilgan.", True),
       ("Boshlang‘ich maktablarda asosan lotin alifbosida savod chiqarilgan.", False)],
      "III noto‘g‘ri: arab tili va alifbosida.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Gandimiyon shartnomasi", "Baljuvon qo‘zg‘oloni", "amirlik orqali birinchi temiryo‘l", "XX asr boshi – Buxoroda 350 ga yaqin maktab"],
      "1873 → 1885 → 1888 → XX asr boshi.")
t.MATCH("Atamalarni izohi bilan moslashtiring.", ["Yangi Buxoro", "xiroj", "vaqf", "maktabxona"],
        ["Buxorodan 15 km da qurilgan stansiya", "yer solig‘i", "maktablarning moddiy asosi", "boshlang‘ich ta’lim maskani", "oliy o‘quv yurti"], 'abcd',
        "Yangi Buxoro – stansiya; xiroj – soliq; vaqf – moddiy asos; maktabxona – boshlang‘ich ta’lim.")
t.VENN("O‘g‘il bolalar maktabi", "Qizlar maktabi",
       [("aksariyati masjidlar qoshida", 1), ("5–12 yoshda qabul", 1),
        ("darslar tushlikkacha", 2), ("7 yoshdan 13 yoshgacha", 2),
        ("an’anaviy boshlang‘ich ta’lim", 3)],
       "O‘g‘il – masjid, 5–12; qiz – tushlikkacha, 7–13; ikkalasi an’anaviy ta’lim.")
t.MAPMATCH('buxamir', ['Baljuvon', 'Chorjo‘y', 'Denov', 'Buxoro'],
           ["1885-yilda dehqonlar qo‘zg‘oloni ko‘tarilgan joy", "Amudaryo bo‘yidagi yirik savdo markazi", "amirlik janubi-sharqidagi savdo-hunarmandchilik markazi", "yaqinida Yangi Buxoro stansiyasi qurilgan poytaxt"],
           "1 – Baljuvon; 2 – Chorjo‘y; 3 – Denov; 4 – Buxoro.")

# 9-mavzu. Xiva xonligi XIX asr 2-yarmi – XX asr boshi
t = Topic('y10u9', 10009); TOPICS['y10u9'] = t
t.B("1873-yildan so‘ng Xiva xonligi xarajatlarni qanday qoplay boshladi?", "yangi soliqlar joriy etib yoki eskilarini oshirib", "Rossiyadan qarz olib", "oltin konlaridan", "savdoni to‘xtatib", "Soliqlarni oshirib.")
t.B("Xiva xonligida qishloq xo‘jaligining asosiy tarmog‘i nima bo‘lgan?", "g‘alla yetishtirish", "paxtachilik", "pillachilik", "bog‘dorchilik", "G‘alla yetishtirish.")
t.B("Rossiya bilan savdo rivojlanishi natijasida qaysi ixtisoslashuv jadal kechdi?", "paxta yetishtirish", "uzumchilik", "sholikorlik", "chorvachilik", "Paxta yetishtirish.")
t.B("XX asr boshida vujudga kelgan yangi shaharlar qaysilar?", "Bog‘ot, Mo‘ynoq, Taxta", "Xiva, Hazorasp", "Qo‘ng‘irot, Gurlan", "Urganch, Shovot", "Bog‘ot, Mo‘ynoq, Taxta.")
t.B("Qoraqalpoq urug‘larini boshqarish uchun Xivada qaysi lavozim joriy etilgan?", "beklarbegi", "mingboshi", "qo‘shbegi", "devonbegi", "Beklarbegi.")
t.B("Qoraqalpoq urug‘larini kim boshqargan?", "biy va oqsoqollar", "beklar", "pristavlar", "mingboshilar", "Biy va oqsoqollar.")
t.B("Urug‘ biylariga tasdiqlovchi yorliqni kim bergan?", "Xiva xonlari", "Buxoro amiri", "Rossiya imperatori", "general-gubernator", "Xiva xonlari.")
t.B("XIX asr o‘rtalarida Yangi Urganchda nechta masjid bo‘lgan?", "15 ta", "6 ta", "10 ta", "4 ta", "15 ta masjid va 2 madrasa.")
t.B("Hazoraspda qaysi madrasa faoliyat yuritgan?", "Qutlug‘ Inoq madrasasi", "Sherg‘ozixon madrasasi", "Muhammad Aminxon madrasasi", "Mir Arab", "Qutlug‘ Inoq madrasasi.")
t.B("Xivada masjid imomi qanday qo‘shimcha vazifalarni bajargan?", "soliq hisobi, soliq yig‘ish, suv taqsimoti", "qo‘shinga qo‘mondonlik", "elchilarni kutib olish", "tanga zarb etish", "Soliq hisobi va yig‘ish, ba’zan suv taqsimoti.")
t.B("Kaufman Xiva saroy kutubxonasidan nechta qo‘lyozmani musodara qilgan?", "300 dona", "30 dona", "3000 dona", "18 dona", "300 dona qo‘lyozma, 18 Qur’oni karim, 50 dan ortiq nodir kitob.")
t.B("Biybozor va Nukus volostida qo‘zg‘olonga kim boshchilik qilgan?", "Bobo Go‘klan", "Oydo‘stbiy", "Dukchi eshon", "Damin kulol", "Bobo Go‘klan.")
t.NAT("Hosildor yerlarning katta qismi Rossiya tasarrufiga o‘tdi.", "xonlik ma’muriyati yangi soliqlar joriy etdi va eskilarini oshirdi", "soliqlar bekor qilindi", "xonlik boyidi", "dehqonlar yer oldi", "Soliq yuki oshdi.")
t.NAT("Rossiya, qozoq juzlari, Kavkaz, Eron bilan savdo rivojlandi.", "ichki savdo jonlanib, tovar-pul munosabatlari o‘sdi", "ichki savdo to‘xtadi", "shaharlar qisqardi", "bozorlar yopildi", "Tovar-pul munosabatlari o‘sdi.")
t.NAT("Bozor munosabatlari rivojlanib, shaharlarning ahamiyati ortdi.", "yangi shaharlar vujudga kelib, eskilarining rivojlanishi tezlashdi", "aholi qishloqlarga ko‘chdi", "shaharlar vayron bo‘ldi", "hunarmandchilik yo‘qoldi", "Shaharlashuv tezlashdi.")
t.NAT("Amudaryo bo‘limidagi qoraqalpoqlarga jabr-zulm kuchaydi.", "Bobo Go‘klan boshchiligida xalq qo‘zg‘oloni bo‘ldi", "qoraqalpoqlar Rossiyaga ko‘chdi", "zulm kamaydi", "beklarbegi lavozimi bekor qilindi", "Qo‘zg‘olon ko‘tarildi.")
t.TF("Har bir dehqon xo‘jaligi yordamchi daromad sifatida uy hunarmandchiligi bilan shug‘ullangan.", True, "To‘g‘ri.")
t.TF("Mahalliy tadbirkorlar faoliyati Rossiya bozoridan mutlaqo mustaqil bo‘lgan.", False, "Noto‘g‘ri: Rossiya bozori mahsulotlariga bevosita bog‘langan.")
t.TF4([("Qoraqalpoqlar tuya junidan guldor namatlar to‘qigan.", True), ("Gurlanda 6 ta masjid va 2 maktab bo‘lgan.", True),
       ("XX asr boshida Toshhovuz ijtimoiy-iqtisodiy markazga aylangan.", True), ("Xiva xonligida uy hunarmandchiligi butunlay yo‘qolgan.", False)],
      "4-noto‘g‘ri: uy hunarmandchiligi hanuz saqlanib kelgan.")
t.MUL([("Tadbirkorlar qo‘shma bank uyushmalarini tuzishga harakat qilgan.", True),
       ("Shovotda 4 ta masjid va 1 madrasa bo‘lgan.", True),
       ("Biylar Xiva xonining ishonchini qozonsa, vakolatlari qisqartirilgan.", False)],
      "III noto‘g‘ri: ishonch qozongan biylar vakolati kengaytirilgan.")
t.CHR("Voqealarni ketma-ket joylashtiring.", ["Gandimiyon shartnomasi – Xiva Rossiya vassali", "Kaufman saroy kutubxonasidan qo‘lyozmalarni musodara qildi", "XX asr boshida Bog‘ot, Mo‘ynoq, Taxta shaharlari vujudga keldi"],
      "1873 → 1873-yildan keyin → XX asr boshi.")
t.MATCH("Shaharlarni ma’lumot bilan moslashtiring.", ["Yangi Urganch", "Gurlan", "Hazorasp", "Mo‘ynoq"],
        ["15 masjid, 2 madrasa", "6 masjid, 2 maktab", "10 masjid, Qutlug‘ Inoq madrasasi", "XX asr boshida vujudga kelgan yangi shahar", "Xiva poytaxti"], 'abcd',
        "Yangi Urganch – 15 masjid; Gurlan – 6 masjid; Hazorasp – 10 masjid; Mo‘ynoq – yangi shahar.")
t.VENN("Qoraqalpoq hunarmandlari", "Xiva qishloq hunarmandlari",
       [("o‘tov eshiklari, guldor namatlar", 1), ("yog‘och va suyakka ishlov", 1),
        ("ko‘nchi, etikchi, bo‘zchi, juvozchi", 2), ("deyarli har bir qishloqda", 2),
        ("gilam to‘qish", 3)],
       "Qoraqalpoq – o‘tov, namat; Xiva qishlog‘i – ko‘nchi, bo‘zchi; ikkalasi gilam to‘qigan.")
t.MAPMATCH('xorazm2', ['Xiva', 'Mo‘ynoq', 'Nukus'],
           ["xonlik poytaxti, saroy kutubxonasi musodara qilingan shahar", "XX asr boshida vujudga kelgan yangi shahar", "Bobo Go‘klan qo‘zg‘oloni bo‘lgan volost"],
           "1 – Xiva; 2 – Mo‘ynoq; 3 – Nukus.")
