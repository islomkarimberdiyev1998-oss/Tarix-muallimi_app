from qlib import Topic
TOPICS = {}

# 23 Siyosiy hayotdagi o'zgarishlar
t = Topic('e10u23', 10023); TOPICS['e10u23'] = t
t.B("Sovet jamiyati siyosiy tizimining asosiy ustuni nima hisoblangan?", "partiya", "Sovetlar", "kasaba uyushmalari", "komsomol", "Partiya.")
t.B("Sharof Rashidov O‘zbekiston Kompartiyasi MK birinchi sekretari etib qachon saylangan?", "1959-yil 15-martda", "1950-yilda", "1966-yilda", "1977-yil noyabrda", "1959-yil 15-martda.")
t.B("Sharof Rashidov qayerda tug‘ilgan?", "Jizzaxda", "Samarqandda", "Toshkentda", "Qo‘qonda", "1917-yil 7-noyabrda Jizzaxda.")
t.B("Sharof Rashidov 1950–1959-yillarda qaysi lavozimda ishlagan?", "O‘zSSR Oliy Soveti Prezidiumi raisi", "Ministrlar Soveti raisi", "KPSS MK sekretari", "Fanlar akademiyasi prezidenti", "O‘zSSR Oliy Soveti Prezidiumi raisi.")
t.B("Toshkent metropolitenining birinchi navbati qachon ishga tushirilgan?", "1977-yil noyabrda", "1966-yilda", "1959-yilda", "1983-yilda", "1977-yil noyabrda, 9 ta bekat.")
t.B("Metropolitenning birinchi navbatida nechta bekat bo‘lgan?", "9 ta", "12 ta", "5 ta", "15 ta", "9 ta bekat.")
t.B("1959–1970-yillarda O‘zSSR Oliy Soveti Prezidiumi raisi kim bo‘lgan?", "Yodgor Nasriddinova", "Nazar Matchonov", "Inomjon Usmonxo‘jayev", "Orif Alimov", "Yodgor Nasriddinova.")
t.B("Butun Sharqda parlament raisi bo‘lgan birinchi ayol kim?", "Yodgor Nasriddinova", "Zebo G‘aniyeva", "Jahon Obidova", "Tojixon Shodiyeva", "Yodgor Nasriddinova.")
t.B("Yodgor Nasriddinova qayerda tug‘ilgan?", "Qo‘qonda", "Jizzaxda", "Marg‘ilonda", "Toshkentda", "Qo‘qonda.")
t.B("Yo. Nasriddinova 1970–1974-yillarda qaysi lavozimda ishlagan?", "SSSR Oliy Soveti Millatlar Sovetining raisi", "O‘zSSR Ministrlar Soveti raisi", "KPSS MK Bosh sekretari", "BMTdagi elchi", "SSSR Oliy Soveti Millatlar Sovetining raisi.")
t.B("1961–1971-yillarda O‘zSSR Ministrlar Soveti raisi kim bo‘lgan?", "Rahmonqul Qurbonov", "Orif Alimov", "Normuhammadi Xudoyberdiyev", "Nazar Matchonov", "Rahmonqul Qurbonov.")
t.B("1971–1984-yillarda O‘zSSR Ministrlar Soveti raisi kim bo‘lgan?", "Normuhammadi Xudoyberdiyev", "Rahmonqul Qurbonov", "Inomjon Usmonxo‘jayev", "Orif Alimov", "Normuhammadi Xudoyberdiyev.")
t.B("1978–1983-yillarda O‘zSSR Oliy Soveti Prezidiumi raisi kim bo‘lgan?", "Inomjon Usmonxo‘jayev", "Nazar Matchonov", "Yodgor Nasriddinova", "Sharof Rashidov", "Inomjon Usmonxo‘jayev.")
t.B("KPSSning yetakchilik roli SSSR Konstitutsiyasining qaysi moddasida mustahkamlangan?", "6-moddasida", "1-moddasida", "10-moddasida", "72-moddasida", "6-moddasida.")
t.B("SSSRning yangi Konstitutsiyasi qachon qabul qilingan?", "1977-yil 7-oktyabrda", "1977-yil noyabrda", "1959-yil 15-martda", "1966-yilda", "1977-yil 7-oktyabrda.")
t.B("1977-yilgi Konstitutsiya kimning rahbarligida tayyorlangan?", "Leonid Brejnev", "Nikita Xrushchev", "Sharof Rashidov", "Georgiy Malenkov", "Leonid Ilich Brejnev.")
t.B("Partiya organlari bilan kelishib tayinlanadigan lavozimlar tartibi qanday atalgan?", "partiya nomenklaturasi", "mahalliylashtirish", "kollektivlashtirish", "shaxsga sig‘inish", "Partiya nomenklaturasi.")
t.NAT("1977-yilgi Konstitutsiya Markazga keng vakolatlar olib berdi.", "milliy respublikalar huquqi rasman cheklandi", "respublikalar mustaqil bo‘ldi", "partiyaning roli kamaydi", "Sovetlar kuchaydi", "Milliy respublikalar huquqi cheklandi.")
t.NAT("Mahalliy Sovetlar ikkinchi darajali masalalarni ham partiya komitetlarisiz hal qila olmas edi.", "xo‘jalik rahbarlari Sovetlarni chetlab o‘tib partiya organlariga murojaat qildi", "Sovetlar mustaqil qaror qabul qildi", "partiya komitetlari tugatildi", "aholi shikoyatlari Sovetlarda ko‘rildi", "Partiya organlari hal qiluvchi bo‘ldi.")
t.TF("Nomenklatura qoidasiga ko‘ra mas’ul lavozimlarga faqat kommunistlar tayinlangan.", True, "To‘g‘ri.")
t.TF("60–80-yillarda xalqning turmush darajasi avvalgi davrlarga nisbatan yomonlashgan.", False, "Noto‘g‘ri: nisbatan yaxshilangan.")
t.MUL([("Mirzacho‘l, Surxon-Sherobod va Qarshi cho‘lining o‘zlashtirilishi bilan ekin maydonlari kengaygan.", True),
       ("Toshkent metropoliteni qurilishi Sharof Rashidov tashabbusi bilan boshlangan.", True),
       ("Sharof Rashidov 1966-yildagi zilziladan keyin lavozimidan ozod qilingan.", False)],
      "III noto‘g‘ri: u Toshkentni qayta tiklashga ko‘p kuch sarflagan va umrining oxirigacha lavozimda bo‘lgan.")
t.MATCH("Rahbarlarni lavozimlari bilan moslashtiring.", ["Sharof Rashidov (1959–1983)", "Nazar Matchonov (1970–1978)", "Orif Alimov (1959–1961)", "Leonid Brejnev"],
        ["O‘zbekiston Kompartiyasi MK birinchi sekretari", "O‘zSSR Oliy Soveti Prezidiumi raisi", "O‘zSSR Ministrlar Soveti raisi", "KPSS MK Bosh sekretari", "SSSR Millatlar Soveti raisi"], 'abcd',
        "Rashidov – MK birinchi sekretari; Matchonov – Oliy Sovet Prezidiumi raisi; Alimov – Ministrlar Soveti raisi; Brejnev – KPSS Bosh sekretari.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Sh. Rashidov birinchi sekretar etib saylandi", "Toshkent zilzilasi", "Yo. Nasriddinova Millatlar Soveti raisi bo‘ldi", "SSSRning yangi Konstitutsiyasi qabul qilindi", "Toshkent metropoliteni ishga tushdi"],
      "1959 → 1966 → 1970 → 1977-yil oktyabr → 1977-yil noyabr.")
t.MAPMATCH('uzb', ['Jizzax', 'Qo‘qon', 'Toshkent'],
           ["Sharof Rashidov tug‘ilgan shahar", "Yodgor Nasriddinova tug‘ilgan shahar", "1977-yilda metropoliten ishga tushgan shahar"],
           "1 – Jizzax; 2 – Qo‘qon; 3 – Toshkent.")
t.VENN("Sharof Rashidov", "Yodgor Nasriddinova",
       [("O‘zbekiston Kompartiyasi MK birinchi sekretari", 1), ("mashhur yozuvchi", 1),
        ("Sharqda parlament raisi bo‘lgan birinchi ayol", 2), ("SSSR Millatlar Soveti raisi", 2),
        ("O‘zSSR Oliy Soveti Prezidiumi raisi bo‘lgan", 3)],
       "Rashidov — birinchi sekretar, yozuvchi; Nasriddinova — birinchi ayol parlament raisi; ikkalasi Oliy Sovet Prezidiumi raisi bo‘lgan.")

# 24 Yoqilg'i va tog'-kon sanoati
t = Topic('e10u24', 10024); TOPICS['e10u24'] = t
t.B("Ittifoq korxonalari olingan foydaning necha foizini mahalliy byudjetga o‘tkazgan?", "atigi 1 foizini", "10 foizini", "20 foizini", "50 foizini", "Atigi 1 foizini.")
t.B("50-yillar boshida qaysi gaz konlari ochilgan?", "Jarqo‘rg‘on, Qorovulbozor, Sariqtosh", "Gazli va Muborak", "Odamtosh va Ustyurt", "Uchqir va Kultak", "Jarqo‘rg‘on, Qorovulbozor, Sariqtosh.")
t.B("Gazli neft-gaz koni qachon topilgan?", "1956-yili", "1958-yili", "1961-yili", "1950-yili", "1956-yili Buxoro viloyatida.")
t.B("Gazli konining umumiy zaxirasi qancha bo‘lgan?", "500 mlrd m³", "33,7 mlrd m³", "50 mlrd m³", "5 trln m³", "500 mlrd m³.")
t.B("1975-yilda O‘zbekistonda qancha tabiiy gaz ishlab chiqarilgan?", "33,7 mlrd m³", "0,4 mlrd m³", "500 mlrd m³", "5,5 mlrd m³", "33,7 mlrd m³ (1960-yilda 0,4 mlrd m³).")
t.B("Butunittifoq gaz qazib chiqarishda O‘zbekistonning ulushi 1975-yilda necha foizga yetgan?", "20 foizga", "1 foizga", "50 foizga", "7 foizga", "1960-yildagi 1 foizdan 20 foizga.")
t.B("Hisor tog‘larining janubi-g‘arbida qaysi kondensat koni topilgan?", "Odamtosh", "Gazli", "Muborak", "Muruntov", "Odamtosh.")
t.B("Navoiy kon-metallurgiya kombinatiga qachon poydevor qo‘yilgan?", "1958-yil 3-sentyabrda", "1956-yilda", "1961-yilda", "1982-yil aprelda", "1958-yil 3-sentyabrda.")
t.B("Dunyoda eng yirik Muruntov oltin koni qachon ishga tushirilgan?", "1961-yili", "1963-yili", "1958-yili", "1956-yili", "1961-yili.")
t.B("Muruntovda dastlabki sof quyma oltin (999,9 proba) qachon tayyorlangan?", "1963-yil", "1961-yil", "1958-yil", "1975-yil", "1963-yil.")
t.B("Navoiy viloyati qachon tashkil qilingan?", "1982-yil aprelda", "1958-yil sentyabrda", "1963-yilda", "1975-yilda", "1982-yil aprelda.")
t.B("70–80-yillarda respublikada har yili taxminan qancha sof oltin quymasi tayyorlangan?", "50 tonna atrofida", "5 tonna", "500 tonna", "1 tonna", "50 tonna atrofida.")
t.B("Oltin zaxiralari bo‘yicha O‘zbekiston dunyoda nechanchi o‘rinni egallagan?", "yettinchi", "birinchi", "uchinchi", "o‘ninchi", "Yettinchi o‘rinni.")
t.B("Har yili O‘zbekistonda qancha qiymatda foydali qazilmalar olingan?", "taxminan 5,5 mlrd dollar", "500 mln dollar", "50 mlrd dollar", "1 mlrd dollar", "Taxminan 5,5 mlrd dollar.")
t.B("60–80-yillarda O‘zbekistonda nechta millat va elat yashagan?", "127 ta", "130 ta", "100 ta", "50 ta", "127 ta.")
t.B("Mahalliy hokimiyatga bo‘ysunmagan Navoiy, Zarafshon, Uchquduq kabi shaharlar qanday atalgan?", "yopiq shaharlar", "erkin iqtisodiy zonalar", "yangi tumanlar", "qo‘riq shaharlar", "«Yopiq shaharlar».")
t.NAT("Ittifoq hukumati O‘zbekistonda gaz ishlab chiqarishni keskin oshirdi.", "gaz asosan RSFSR sanoat markazlariga tashib ketildi", "barcha qishloqlar gazlashtirildi", "gaz narxi oshdi", "gaz qazib olish to‘xtatildi", "Uy-joyni gazlashtirish salmog‘i past qoldi.")
t.NAT("Yopiq shaharlarga Markazdan ko‘chirib keltirilgan kadrlar navbatsiz uy-joy bilan ta’minlandi.", "ijtimoiy adolat tamoyillari buzildi, mahalliy yoshlar kamsitildi", "mahalliy aholi imtiyoz oldi", "shaharlar ochiq bo‘ldi", "ishchi kuchi kamaydi", "Ijtimoiy adolat buzildi.")
t.TF("Oltin, uran va gaz favqulodda maxfiylik ostida O‘zbekistondan amalda tekinga olib ketilgan.", True, "To‘g‘ri.")
t.TF("Gaz yetkazib beruvchi Buxoro viloyatining o‘zi to‘liq gazlashtirilgan edi.", False, "Noto‘g‘ri: u yerda ham ahvol nihoyatda achinarli bo‘lgan.")
t.MUL([("Navoiy kombinati Navoiy, Zarafshon, Uchquduq kabi shaharlarga asos solgan.", True),
       ("O‘zSSR mamlakat oltinining yarmidan ko‘pini bergan.", True),
       ("Yopiq shaharlardagi korxonalar mahalliy hokimiyatga hisob bergan.", False)],
      "III noto‘g‘ri: ular faqat Markazga hisob bergan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Gazli koni topildi", "Navoiy shahriga asos solindi", "Muruntov oltin koni ishga tushdi", "Dastlabki sof quyma oltin tayyorlandi", "Gaz ishlab chiqarish 33,7 mlrd m³ ga yetdi", "Navoiy viloyati tashkil qilindi"],
      "1956 → 1958 → 1961 → 1963 → 1975 → 1982.")
t.MAPMATCH('uzb', ['Gazli', 'Navoiy', 'Uchquduq', 'Muborak'],
           ["1956-yilda dunyodagi eng yirik konlardan biri topilgan gazchilar shahri", "1958-yilda kon-metallurgiya kombinati bilan asos solingan shahar", "Navoiy kombinati asos solgan Qizilqumdagi «yopiq shahar»", "Shimoliy va Janubiy gaz konlari shu nom bilan atalgan joy"],
           "1 – Gazli; 2 – Navoiy; 3 – Uchquduq; 4 – Muborak.")
t.VENN("Tabiiy gaz", "Oltin",
       [("Gazli konining zaxirasi 500 mlrd m³", 1), ("1975-yilda Ittifoq qazib olishining 20 %", 1),
        ("Muruntov koni 1961-yilda ishga tushgan", 2), ("zaxirasi bo‘yicha dunyoda 7-o‘rin", 2),
        ("Markaz manfaatlariga xizmat qilgan boylik", 3)],
       "Gaz — Gazli, 20 %; oltin — Muruntov, 7-o‘rin.")
