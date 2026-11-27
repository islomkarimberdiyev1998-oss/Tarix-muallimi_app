from qlib import Topic
TOPICS = {}

# 15 Qatag'onlik siyosati
t = Topic('e10u15', 10015); TOPICS['e10u15'] = t
t.B("«Qosimovchilik» ishi kimning nomi bilan bog‘liq?", "O‘zSSR Oliy sudi raisi Sa’dulla Qosimov", "Maorif xalq komissari Rahim Inog‘omov", "prokuror Shamsutdin Badriddinov", "Mannon Ramziy", "O‘zSSR Oliy sudi raisi Sa’dulla Qosimov.")
t.B("«Botir gapchilar» ishi qaysi shaharda to‘qilgan?", "Qo‘qonda", "Samarqandda", "Toshkentda", "Buxoroda", "Qo‘qonda, Ashurali Zohiriy boshchiligidagi 19 kishi.")
t.B("«Tozalash» natijasida O‘zbekiston Kompartiyasi a’zolarining necha foizi firqadan chiqarildi?", "25,6 foizi", "17 foizi", "50 foizi", "10 foizi", "25,6 foizi.")
t.B("O‘zbekiston Kompartiyasining IV syezdi qachon va qayerda o‘tgan?", "1929-yil 17-fevral – 2-martda Samarqandda", "1925-yil noyabrda Samarqandda", "1934-yil yanvarda Toshkentda", "1927-yil noyabrda Toshkentda", "1929-yil 17-fevral – 2-mart, Samarqand.")
t.B("Sa’dulla Qosimov qachon qamoqqa olingan?", "1929-yil mart oyida", "1930-yil avgustda", "1932-yil mayda", "1937-yil yozida", "1929-yil martda.")
t.B("Qosimov va Badriddinov ishlarida prokuror kim bo‘lgan?", "R. Katanyan", "Vasilyev-Yujin", "Botu", "Kirpanov", "Turkiy xalqlarga nafrati bilan tanilgan R. Katanyan.")
t.B("Badriddinov ishi bo‘yicha sud jarayoni qayerda o‘tgan?", "Toshkentda", "Samarqandda", "Moskvada", "Qo‘qonda", "1932-yil 5-may – 15-iyunda Toshkentda.")
t.B("Shamsutdin Badriddinovning o‘lim hukmi nimaga almashtirilgan?", "10 yil qamoq jazosiga", "surgunga", "oqlovga", "5 yil qamoqqa", "10 yil qamoq jazosiga.")
t.B("«Narkompros» ishi bo‘yicha qachon va qayerda rahbar xodimlar hibsga olingan?", "1930-yil avgustda Samarqandda", "1929-yil noyabrda Toshkentda", "1937-yil yozida Toshkentda", "1932-yil mayda Qo‘qonda", "1930-yil avgustda Samarqandda.")
t.B("O‘zSSR Maorif xalq komissari Mannon Ramziyning o‘rinbosari kim edi?", "Botu (Mahmud Hodiyev)", "Oltoy (Bois Qoriyev)", "Nodir Saidov", "Rahim Inog‘omov", "Botu – Mahmud Hodiyev.")
t.B("Munavvarqori boshchiligidagi 38 kishi qachon qamoqqa olingan?", "1929-yil 5-noyabrda", "1931-yil 25-aprelda", "1930-yil avgustda", "1937-yil yozida", "1929-yil 5-noyabrda Toshkentda.")
t.B("1931-yil 25-aprelda Moskvadagi sudda «Milliy Istiqlol»ning nechta a’zosi otib o‘ldirishga hukm qilingan?", "15 nafari", "87 nafari", "72 nafari", "38 nafari", "15 nafari; 72 nafari uzoq muddatli qamoqqa.")
t.B("Fitrat, Cho‘lpon va Abdulla Qodiriy qachon otib tashlangan?", "1938-yil 4-oktyabrda", "1938-yil 10-oktyabrda", "1937-yil 28-oktyabrda", "1931-yil 25-aprelda", "Bir kunda – 1938-yil 4-oktyabrda.")
t.B("Mirkomil Mirsharopov qayerda qamoqqa olingan?", "Maykopda", "Toshkentda", "Moskvada", "Samarqandda", "1937-yil 28-oktyabrda Maykopda.")
t.B("1937–1938-yillarda O‘zbekistonda necha kishi otib o‘ldirishga hukm qilingan?", "6920 nafar", "41 000 nafar", "37 000 nafar", "4811 nafar", "6920 nafar.")
t.B("«Shahidlar xotirasi» yodgorlik majmuasi qachon ochilgan?", "2000-yil 12-mayda", "2002-yil 31-avgustda", "2001-yil 31-avgustda", "1991-yil 1-sentyabrda", "2000-yil 12-mayda.")
t.B("«Qatag‘on qurbonlari xotirasi» muzeyi qachon ochilgan?", "2002-yil 31-avgustda", "2000-yil 12-mayda", "2001-yil 31-avgustda", "2005-yilda", "2002-yil 31-avgustda.")
t.NAT("Mirsharopov O‘zbek diviziyasini milliylashtirish va O‘zbekistonni SSSRdan ajratishga urinishda ayblandi.", "u boshliq 18 nafar o‘zbek harbiysi 1938-yil 10-oktyabrda otib tashlandi", "diviziya kengaytirildi", "u oqlandi", "u Afg‘onistonga qochdi", "Diviziya tarqatildi, 18 kishi otib tashlandi.")
t.TF("2001-yildan har yili 31-avgust qatag‘on qurbonlarini yod etish kuni sifatida o‘tkaziladi.", True, "To‘g‘ri.")
t.TF("Usmon Nosir 1938-yil 4-oktyabrda Toshkentda otib tashlangan.", False, "Noto‘g‘ri: u qamoqxonada vafot etgan.")
t.MUL([("Qosimov va uning 3 safdoshi otib o‘ldirishga hukm qilingan.", True),
       ("Botu va tarafdorlari 10 yilga hukm qilinib, keyin qamoqxonada otib tashlangan.", True),
       ("Munavvarqori ishi bo‘yicha tergov oxirigacha Toshkentda olib borilgan.", False)],
      "III noto‘g‘ri: tergov Moskvaga ko‘chirilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Kompartiyaning IV syezdi", "Munavvarqori va safdoshlari qamoqqa olindi", "«Narkompros» xodimlari hibsga olindi", "Moskvada «Milliy Istiqlol» a’zolari ustidan sud", "Badriddinov ustidan sud", "Fitrat, Cho‘lpon, Qodiriy otib tashlandi"],
      "1929-yil fevral → 1929-yil noyabr → 1930-yil avgust → 1931-yil aprel → 1932-yil may → 1938-yil oktyabr.")
t.MAPMATCH('uzb', ['Samarqand', 'Qo‘qon', 'Toshkent'],
           ["Kompartiyaning IV syezdi o‘tgan, Qosimov ustidan sud bo‘lgan shahar", "«botir gapchilar» ishi to‘qilgan shahar", "Munavvarqori va safdoshlari qamoqqa olingan, «Shahidlar xotirasi» joylashgan shahar"],
           "1 – Samarqand; 2 – Qo‘qon; 3 – Toshkent.")
t.VENN("Sa’dulla Qosimov", "Shamsutdin Badriddinov",
       [("O‘zSSR Oliy sudi raisi bo‘lgan", 1), ("Samarqanddagi sudda otishga hukm qilingan", 1),
        ("O‘zSSR Oliy sudining prokurori bo‘lgan", 2), ("o‘lim hukmi 10 yil qamoq bilan almashtirilgan", 2),
        ("ishida R. Katanyan prokuror bo‘lgan", 3)],
       "Qosimov — Oliy sud raisi, otilgan; Badriddinov — prokuror, 10 yil qamoq.")

# 16 Ikkinchi jahon urushining boshlanishi
t = Topic('e10u16', 10016); TOPICS['e10u16'] = t
t.B("SSSR va Germaniya o‘rtasida hujum qilmaslik to‘g‘risidagi bitim qachon imzolangan?", "1939-yil 23-avgustda", "1939-yil 1-sentyabrda", "1939-yil 28-sentyabrda", "1941-yil 22-iyunda", "1939-yil 23-avgustda Moskvada.")
t.B("Hujum qilmaslik bitimi necha yil muddatga tuzilgan?", "10 yil", "5 yil", "20 yil", "25 yil", "10 yil muddatga.")
t.B("Hujum qilmaslik bitimi tarixda qanday nom bilan mashhur?", "Molotov-Ribbentrop pakti", "Myunxen bitimi", "Brest tinchligi", "Antikomintern pakti", "Molotov-Ribbentrop pakti.")
t.B("Ikkinchi jahon urushi qanday boshlangan?", "Germaniyaning Polshaga hujumi bilan", "Germaniyaning SSSRga hujumi bilan", "SSSRning Finlyandiyaga hujumi bilan", "Yaponiyaning Xitoyga hujumi bilan", "1939-yil 1-sentyabrda Germaniyaning Polshaga hujumi bilan.")
t.B("SSSR qo‘shinlari Polsha hududiga qachon bostirib kirgan?", "1939-yil 17-sentyabrda", "1939-yil 1-sentyabrda", "1939-yil 3-sentyabrda", "1940-yil iyulda", "1939-yil 17-sentyabrda.")
t.B("Sovet va nemis qo‘shinlarining qo‘shma paradi qayerda o‘tkazilgan?", "Brest-Litovskda", "Varshavada", "Vilnyusda", "Moskvada", "1939-yil 22-sentyabrda Brest-Litovskda.")
t.B("SSSR va Germaniya o‘rtasida do‘stlik va chegaralar to‘g‘risidagi shartnoma qachon imzolangan?", "1939-yil 28-sentyabrda", "1939-yil 23-avgustda", "1939-yil 22-sentyabrda", "1940-yil 12-martda", "1939-yil 28-sentyabrda.")
t.B("Latviya, Litva va Estoniya qachon SSSR tarkibiga majburan kiritilgan?", "1940-yil iyulda", "1939-yil sentyabrda", "1941-yil iyunda", "1940-yil martda", "1940-yil iyulda.")
t.B("Moldaviya SSR mamlakat tarkibidagi nechanchi ittifoqdosh respublika bo‘lgan?", "15-", "12-", "16-", "11-", "15-ittifoqdosh respublika.")
t.B("Sovet-fin urushi qaysi sanalarda bo‘lib o‘tgan?", "1939-yil 30-noyabr – 1940-yil 12-mart", "1939-yil 1-sentyabr – 1940-yil 12-mart", "1940-yil iyul – avgust", "1941-yil 22-iyun – dekabr", "1939-yil 30-noyabr – 1940-yil 12-mart.")
t.B("Millatlar Ligasi SSSRni agressor deb e’lon qilib, a’zolikdan qachon chiqargan?", "1939-yil 14-dekabrda", "1940-yil 12-martda", "1939-yil 30-noyabrda", "1941-yil 22-iyunda", "1939-yil 14-dekabrda.")
t.B("Sovet-fin urushi natijasida SSSR qaysi hududlarni qo‘lga kiritgan?", "Viborg shahri va Ladoga ko‘li atrofini", "Xelsinkini", "Bessarabiyani", "G‘arbiy Ukrainani", "Viborg va Ladoga ko‘li atrofini.")
t.B("Davlat Mudofaa Qo‘mitasi qachon tuzilgan?", "1941-yil 30-iyunda", "1941-yil 22-iyunda", "1941-yil 19-iyulda", "1941-yil 8-avgustda", "1941-yil 30-iyunda.")
t.B("Stalin SSSR Qurolli kuchlari Oliy Bosh qo‘mondoni lavozimini qachon egallagan?", "1941-yil 8-avgustda", "1941-yil 19-iyulda", "1941-yil 30-iyunda", "1941-yil 22-iyunda", "1941-yil 8-avgustda.")
t.B("Urush yillarida O‘zbekiston Kompartiyasi MK birinchi sekretari kim bo‘lgan?", "Usmon Yusupov", "Akmal Ikromov", "Fayzulla Xo‘jayev", "Yo‘ldosh Oxunboboyev", "Usmon Yusupov.")
t.B("Urushning dastlabki kunlarida harbiy komissarliklarga ko‘ngillilardan qancha ariza tushgan?", "14 mingdan ortiq", "100 mingdan ortiq", "1400", "50 ming", "14 mingdan ortiq.")
t.B("Urush yillarida O‘zbekiston aholisi mudofaa jamg‘armasiga jami qancha pul topshirgan?", "649,9 mln rubl", "30 mln rubl", "1,16 mlrd rubl", "50 ming so‘m", "649,9 mln rubl va 22 kg oltin-kumush.")
t.B("Mudofaa fondiga 50 ming so‘m topshirgan mashhur raqqosa kim?", "Tamaraxonim", "Halima Nosirova", "Mukarrama Turg‘unboyeva", "Sora Eshonto‘rayeva", "Tamaraxonim.")
t.B("Evakuatsiya qilingan 308 korxonadan nechtasi O‘zbekistonga joylashtirilgan?", "100 dan ortig‘i", "50 tasi", "308 tasi", "20 tasi", "100 dan ortig‘i; 1941-yil oxirigacha 50 tasi ishga tushdi.")
t.B("Toshkent aviatsiya zavodi qaysi shahardan ko‘chirilgan zavod asosida barpo etilgan?", "Ximki (Moskva viloyati)", "Leningrad", "Kiyev", "Xarkov", "Ximki shahridan, 1941-yil oktyabrda.")
t.NAT("1939-yil 14-dekabrda Millatlar Ligasi SSSRni agressor deb e’lon qildi.", "SSSR Liga a’zoligidan chiqarildi", "SSSR Ligaga rais bo‘ldi", "Finlyandiya Ligadan chiqarildi", "urush to‘xtatildi", "SSSR Ligadan chiqarildi.")
t.TF("Molotov-Ribbentrop paktining maxfiy qismida ikki davlatning ta’sir doiralari belgilangan.", True, "To‘g‘ri.")
t.TF("1939-yil 3-sentyabrda SSSR Germaniyaga qarshi urush e’lon qilgan.", False, "Noto‘g‘ri: Fransiya va Angliya urush e’lon qilgan.")
t.MUL([("1939-yil 19-sentyabrda qizil armiya Vilnyusni bosib olgan.", True),
       ("A. Tolstov, V. Russkix sovet-fin urushida qatnashgan.", True),
       ("Toshkent aviatsiya zavodi bombardimonchi samolyotlar ishlab chiqargan.", False)],
      "III noto‘g‘ri: qiruvchi samolyotlar ishlab chiqargan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Molotov-Ribbentrop pakti", "Germaniya Polshaga hujum qildi", "SSSR qo‘shinlari Polshaga kirdi", "Sovet-fin urushi boshlandi", "Boltiqbo‘yi SSSRga qo‘shildi", "Germaniya SSSRga hujum qildi"],
      "1939-yil 23-avgust → 1-sentyabr → 17-sentyabr → 30-noyabr → 1940-yil iyul → 1941-yil 22-iyun.")
t.MAPMATCH('europe', ['Brest', 'Vilnyus', 'Viborg', 'Moskva'],
           ["1939-yil 22-sentyabrda sovet-nemis qo‘shma paradi o‘tgan shahar", "1939-yil 19-sentyabrda qizil armiya bosib olgan shahar", "sovet-fin urushi natijasida SSSR qo‘lga kiritgan shahar", "1939-yil 23-avgustda hujum qilmaslik bitimi imzolangan shahar"],
           "1 – Brest; 2 – Vilnyus; 3 – Viborg; 4 – Moskva.")
t.VENN("1939-yilgi sovet-nemis munosabatlari", "1941-yilgi sovet-nemis munosabatlari",
       [("hujum qilmaslik bitimi imzolangan", 1), ("Polsha birgalikda bo‘lib olingan", 1),
        ("Germaniya SSSRga to‘satdan bostirib kirgan", 2), ("Davlat Mudofaa Qo‘mitasi tuzilgan", 2),
        ("Gitler boshchiligidagi Germaniya bilan bog‘liq", 3)],
       "1939 — pakt, Polshani bo‘lish; 1941 — hujum, DMQ.")
