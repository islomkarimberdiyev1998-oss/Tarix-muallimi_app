from qlib import Topic, PLACES, REG
TOPICS = {}
CA = 'ca'
PLACES.update({'Vilnyus': (25.28, 54.69), 'Viborg': (28.75, 60.71)})

# 14-§. Sovet hokimiyatining madaniy siyosati
t = Topic('e10u14', 10114); TOPICS['e10u14'] = t
t.B("“Tarbiya bizlar uchun yo hayot – yo mamot, yo najot – yo halokat...” degan so‘zlar kimga tegishli?", "Abdulla Avloniy", "Abdurauf Fitrat", "Mahmudxo‘ja Behbudiy", "Munavvarqori", "Ma’rifatparvar adib Abdulla Avloniy.")
t.B("O‘zbekiston SSR Fanlar komiteti qachon tuzildi?", "1932-yil 14-oktyabrda", "1934-yilda", "1940-yil 9-yanvarda", "1936-yilda", "1932-yil 14-oktyabrda.")
t.B("1934-yili O‘zSSR Fanlar komitetiga kim rais qilib saylandi?", "Otajon Hoshimov", "Toshmuhammad Qori-Niyozov", "Fayzulla Xo‘jayev", "Akmal Ikromov", "Otajon Hoshimov.")
t.B("O‘zSSR Fanlar komiteti qachon SSSR FA O‘zbekiston filiali (O‘zFAN)ga aylantirildi?", "1940-yil 9-yanvarda", "1932-yil 14-oktyabrda", "1943-yilda", "1940-yil 8-mayda", "1940-yil 9-yanvarda.")
t.B("1940-yili respublikada nechta oliy o‘quv yurti ishlab turdi?", "30 ta", "100 ga yaqin", "539 ta", "18 ta", "30 ta oliy va 100 ga yaqin o‘rta maxsus o‘quv yurti.")
t.B("O‘zSSR Sovetlarining V qurultoyi necha yoshdagi bolalarni majburiy yetti yillik ta’limga tortishni taklif qildi?", "8 yoshdan 15 yoshgacha", "7 yoshdan 14 yoshgacha", "6 yoshdan 16 yoshgacha", "10 yoshdan 17 yoshgacha", "8 yoshdan 15 yoshgacha.")
t.B("Ikkinchi besh yillik davrida nechta yangi maktab qurildi?", "539 ta", "413 ta", "289 ta", "30 ta", "35 000 o‘quvchi sig‘adigan 539 ta maktab.")
t.B("Respublika maktablarida o‘qish nechta tilda olib borilgan?", "18 tilda", "10 tilda", "5 tilda", "3 tilda", "18 tilda.")
t.B("1937-yili savodsizlikni tugatish maktablarining soni nechtaga yetdi?", "413 taga", "539 taga", "139 taga", "100 taga", "413 ta maktab, 28 700 kishi o‘qigan.")
t.B("1937-yili nechta xotin-qiz o‘qish va yozishni o‘rganib oldi?", "139 000 nafar", "28 700 nafar", "931 800 nafar", "35 000 nafar", "139 000 nafar.")
t.B("Sovet hokimiyatining dastlabki o‘n yilliklarida O‘zbekistonda imlo necha marta o‘zgartirildi?", "3 marta", "2 marta", "4 marta", "5 marta", "3 marta.")
t.B("O‘zbek yozuvini lotin grafikasiga o‘tkazish haqidagi qaror qachon va qayerda qabul qilindi?", "1929-yil mayda Samarqandda", "1940-yil 8-mayda Toshkentda", "1921-yilda Toshkentda", "1929-yil 1-dekabrda Buxoroda", "1929-yil mayda Samarqanddagi konferensiyada.")
t.B("O‘zbekistonda arab alifbosidan lotin yozuviga qachon o‘tildi?", "1929-yil 1-dekabrda", "1929-yil 10-avgustda", "1940-yil 8-mayda", "1922-yilda", "1929-yil 1-dekabrda.")
t.B("Lotin yozuvidan kirillga o‘tish to‘g‘risidagi qaror qachon qabul qilindi?", "1940-yil 8-mayda", "1929-yil 1-dekabrda", "1940-yil 9-yanvarda", "1936-yilda", "1940-yil 8-mayda O‘zSSR Oliy Soveti III sessiyasida.")
t.B("Kirill yozuviga o‘tish to‘g‘risida ma’ruza qilgan matematik olim kim?", "Toshmuhammad Qori-Niyozov", "Otajon Hoshimov", "Fayzulla Xo‘jayev", "Muxtor Ashrafiy", "Toshmuhammad Qori-Niyozov.")
t.B("Toshkentda davlat konservatoriyasi qachon ochildi?", "1936-yili", "1940-yili", "1929-yili", "1932-yili", "1936-yili.")
t.B("Quyidagilardan qaysi biri o‘zbek kompozitori sifatida tilga olingan?", "Muxtor Ashrafiy", "Mannon Uyg‘ur", "Komil Yormatov", "Abror Hidoyatov", "To‘xtasin Jalilov, Yunus Rajabiy, Muxtor Ashrafiy, Mutavakkil Burhonov.")
t.B("Qaysi shaxs kinematografiya arbobi sifatida tilga olingan?", "Komil Yormatov", "Yunus Rajabiy", "Mannon Uyg‘ur", "Karim Zokirov", "Komil Yormatov, Nabi G‘aniyev, Rahim Pirmuhammedov.")
t.NAT("Sovet hokimiyati lotin grafikasiga o‘tishni amalga oshirdi.", "arab yozuvidagi Qur’on, hadislar va boshqa kitoblardan xalqni uzoqlashtirish ko‘zlandi", "xalq savodxonligi bir zumda oshdi", "Turkiya bilan aloqalar uzildi", "rus tili taqiqlandi", "Arab tilidagi diniy va boshqa kitoblarni yo‘qotish ko‘zlangan.")
t.NAT("1940-yilda kirill yozuviga o‘tildi.", "turkiy respublikalar lotin yozuvidagi Turkiya ta’siridan uzoqlashtirildi, ruslashtirish so‘nggi bosqichga o‘tdi", "arab yozuvi tiklandi", "o‘zbek tili taqiqlandi", "O‘zFAN tuzildi", "Turkiya bilan aloqalarni yo‘qotish va ruslashtirish ko‘zlangan.")
t.TF("Oliy o‘quv yurtlaridagi talabalar orasida o‘zbeklar kamchilikni tashkil qilgan.", True, "To‘g‘ri: asosan slavyan tillariga mansub kishilar o‘qigan.")
t.TF("Birinchi besh yillikda xalq maorifiga ikkinchi besh yillikka nisbatan ko‘proq mablag‘ ajratildi.", False, "Noto‘g‘ri: birinchisida 395,5 mln rubl, ikkinchisida 1,16 mlrd rubl.")
t.MUL([("Ikkinchi besh yillikda o‘quvchilar soni 931 800 nafarga yetdi.", True),
       ("O‘zbek tilida o‘qitiladigan maktablar soni o‘n yilda 10 marta oshgan.", True),
       ("1921 – 1922-yillarda o‘zbek yozuvi to‘g‘ridan-to‘g‘ri kirillga o‘tkazildi.", False)],
      "III noto‘g‘ri: 1921 – 1922-yillarda arab imlosi isloh qilinib soddalashtirildi.")
t.MATCH("San’at arboblarini sohalari bilan moslashtiring.", ["Yunus Rajabiy", "Mannon Uyg‘ur", "Nabi G‘aniyev", "Tamaraxonim"],
        ["raqs va xonandalik", "kinematografiya", "kompozitor", "teatr rejissyori"], "cdba",
        "Rajabiy – kompozitor; Uyg‘ur – teatr; G‘aniyev – kino; Tamaraxonim – raqs.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["Arab imlosining isloh qilinishi", "Lotin yozuviga o‘tilishi", "O‘zSSR Fanlar komitetining tuzilishi", "Toshkent davlat konservatoriyasining ochilishi", "Kirill yozuviga o‘tish qarori"],
      "1921 – 1922 → 1929-yil 1-dekabr → 1932-yil 14-oktyabr → 1936 → 1940-yil 8-may.")
t.MAPN('uzb', ['Samarqand', 'Toshkent', 'Xiva', 'Andijon'], "1929-yil mayda o‘zbek yozuvini lotin grafikasiga o‘tkazish haqida qaror qabul qilingan konferensiya o‘tgan shahar qaysi raqam bilan belgilangan?",
       "Konferensiya 1929-yil mayda Samarqandda o‘tgan.")
t.VENN("Lotin yozuviga o‘tish (1929)", "Kirill yozuviga o‘tish (1940)",
       [("Samarqanddagi konferensiyada qaror qabul qilingan", 1), ("arab grafikasidan voz kechilgan", 1),
        ("Toshmuhammad Qori-Niyozov ma’ruzasi asosida qabul qilingan", 2), ("Turkiya ta’siridan uzoqlashtirish ko‘zlangan", 2),
        ("sovet hokimiyatining alifbo islohoti", 3)],
       "1929 – Samarqand, arab yozuvidan voz kechish; 1940 – Qori-Niyozov, Turkiya ta’siri; ikkalasi alifbo islohoti.")

# 15-§. Qatag‘onlik siyosati
t = Topic('e10u15', 10115); TOPICS['e10u15'] = t
t.B("“Inog‘omovchilik” ishi kimning nomi bilan bog‘liq?", "O‘zSSR Maorif xalq komissari Rahim Inog‘omov", "O‘zSSR Oliy sudi raisi Sa’dulla Qosimov", "prokuror Shamsutdin Badriddinov", "Mannon Ramziy", "Rahim Inog‘omov – Maorif xalq komissari.")
t.B("“Botir gapchilar” ishi qaysi shaharda to‘qilgan?", "Qo‘qonda", "Samarqandda", "Toshkentda", "Buxoroda", "Qo‘qonda Ashurali Zohiriy boshchiligidagi 19 nafar kishi.")
t.B("Partiya saflarini “tozalash” natijasida O‘zKP a’zolarining necha foizi chiqarildi?", "25,6 foizi", "17 foizi", "50 foizi", "10 foizi", "25,6 foizi.")
t.B("O‘zKP IV syezdi qachon va qayerda o‘tkazildi?", "1929-yil 17-fevral – 2-martda Samarqandda", "1925-yil noyabrda Samarqandda", "1934-yil yanvarda Toshkentda", "1927-yil noyabrda Toshkentda", "1929-yil 17-fevral – 2-martda Samarqandda.")
t.B("O‘zSSR Oliy sudi raisi Sa’dulla Qosimov qachon qamoqqa olindi?", "1929-yil martda", "1930-yil avgustda", "1932-yil mayda", "1929-yil 5-noyabrda", "1929-yil martda.")
t.B("“Qosimovchilik” ishida qancha kishi otib o‘ldirishga hukm qilindi?", "4 kishi", "15 kishi", "6 kishi", "3 kishi", "S.Qosimov, B.Sharipov, N.Alimov, Spiridinov – 4 kishi; 3 kishi 10 yilga.")
t.B("“Badriddinovchilik” ishi bo‘yicha sud qachon va qayerda o‘tdi?", "1932-yil 5-may – 15-iyunda Toshkentda", "1930-yilda Samarqandda", "1931-yil 25-aprelda Moskvada", "1938-yil 4-oktyabrda Toshkentda", "1932-yil 5-may – 15-iyunda Toshkentda.")
t.B("Qosimov va Badriddinov ishlarida prokuror kim bo‘lgan?", "R.Katanyan", "Vasilyev-Yujin", "Mannon Ramziy", "Botu", "Ikkala ishda ham prokuror R.Katanyan bo‘lgan.")
t.B("“Narkompros” ishi bo‘yicha qachon rahbar xodimlar hibsga olindi?", "1930-yil avgustda", "1929-yil martda", "1932-yil mayda", "1937-yil yozida", "1930-yil avgustda Samarqandda.")
t.B("Munavvarqori boshchiligidagi guruh qachon qamoqqa olindi?", "1929-yil 5-noyabrda", "1931-yil 25-aprelda", "1930-yil avgustda", "1937-yil yozida", "1929-yil 5-noyabrda Toshkentda 38 kishi.")
t.B("Munavvarqori guruhiga qanday tashkilotlar a’zoligi ayb qilib qo‘yildi?", "“Milliy Ittihod” va “Milliy Istiqlol”", "“Sho‘roi Islomiya” va “Sho‘roi Ulamo”", "“Ittifoqi muslimin”", "“Yosh buxoroliklar”", "“Milliy Ittihod” va “Milliy Istiqlol”.")
t.B("1931-yil 25-aprelda Moskvada Munavvarqori boshchiligidagi nechta kishi otib o‘ldirishga hukm qilindi?", "15 nafar", "87 nafar", "72 nafar", "38 nafar", "15 nafari otishga, 72 nafari qamoqqa.")
t.B("Fitrat, Cho‘lpon va Abdulla Qodiriy qachon otib tashlandi?", "1938-yil 4-oktyabrda", "1938-yil 10-oktyabrda", "1937-yil 28-oktyabrda", "1931-yil 25-aprelda", "1938-yil 4-oktyabrda Toshkent atrofida.")
t.B("Qaysi iste’dodli shoir qamoqxonada vafot etdi?", "Usmon Nosir", "Cho‘lpon", "Hamid Olimjon", "Oybek", "Usmon Nosir qamoqxonada vafot etdi.")
t.B("Mirkomil Mirsharopov qachon va qayerda qamoqqa olindi?", "1937-yil 28-oktyabrda Maykopda", "1938-yil 10-oktyabrda Toshkentda", "1937-yil yozida Samarqandda", "1930-yil avgustda Moskvada", "1937-yil 28-oktyabrda Maykopda.")
t.B("1937 – 1938-yillarda O‘zbekistonda nechadan ortiq kishi hibsga olindi?", "41 000 dan ortiq", "37 000 dan ortiq", "6920", "5758", "41 000 dan ortiq hibsga olinib, 37 000 dan ko‘prog‘i jazolandi.")
t.B("“Shahidlar xotirasi” yodgorlik majmuasi qachon ochildi?", "2000-yil 12-mayda", "2002-yil 31-avgustda", "2001-yil 31-avgustda", "1991-yil 31-avgustda", "2000-yil 12-mayda.")
t.B("“Qatag‘on qurbonlari xotirasi” muzeyi qachon ochildi?", "2002-yil 31-avgustda", "2000-yil 12-mayda", "2001-yil 31-avgustda", "2016-yilda", "2002-yil 31-avgustda.")
t.B("2001-yildan qatag‘on qurbonlarini yod etish kuni qaysi sana?", "31-avgust", "9-may", "1-sentyabr", "4-oktyabr", "31-avgust.")
t.NAT("1937-yil yozida siyosiy qatag‘onlik avjiga chiqdi.", "F.Xo‘jayev, A.Ikromov va ko‘plab rahbarlar qamoqqa olinib, otib tashlandi", "qatag‘on qurbonlari oqlandi", "O‘zKP saflari kengaydi", "jadidlar hukumatga keldi", "F.Xo‘jayev va A.Ikromov otib tashlandi.")
t.NAT("O‘zbekiston mustaqillikka erishdi.", "qatag‘on qilinganlarning ko‘pchiligi huquqiy jihatdan oqlanib, nomlari tiklandi", "qatag‘onlar kuchaydi", "Munavvarqori ishi qayta ochildi", "O‘zbek diviziyasi tarqatildi", "Ko‘pchilik oqlanib, porloq nomlari tiklandi.")
t.TF("Sh.Badriddinovga avval o‘lim hukmi chiqarilib, keyin u 10 yil qamoq bilan almashtirildi.", True, "To‘g‘ri.")
t.TF("Botu va uning tarafdorlari 10 yillik qamoq jazosini o‘tab, ozodlikka chiqdi.", False, "Noto‘g‘ri: ular keyinchalik qamoqxonada otib tashlandi.")
t.MUL([("M.Mirsharopov boshchiligida 18 nafar o‘zbek harbiylari 1938-yil 10-oktyabrda otib tashlangan.", True),
       ("“Shahidlar xotirasi” majmuasi Bo‘zsuv kanali bo‘yida joylashgan.", True),
       ("1937 – 1938-yillarda 4811 nafar kishi otib o‘ldirishga hukm qilingan.", False)],
      "III noto‘g‘ri: umumiy 6920 nafar otishga hukm qilingan; 4811 nafari – davlat arboblari, yozuvchi, shoir va olimlardan.")
t.MATCH("Siyosiy ishlarni ularga aloqador shaxslar bilan moslashtiring.", ["qosimovchilik", "badriddinovchilik", "“narkompros” ishi", "“botir gapchilar”"],
        ["Ashurali Zohiriy", "Shamsutdin Badriddinov", "Sa’dulla Qosimov", "Mannon Ramziy va Botu"],
        "cbda", "Qosimovchilik – Qosimov; badriddinovchilik – Badriddinov; narkompros – Ramziy, Botu; botir gapchilar – Zohiriy.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["O‘zKP IV syezdi", "Munavvarqori guruhining qamoqqa olinishi", "“Narkompros” ishi bo‘yicha hibslar", "Munavvarqori guruhi ustidan Moskvadagi sud", "Fitrat, Cho‘lpon va Qodiriyning otib tashlanishi"],
      "1929-yil fevral – mart → 1929-yil 5-noyabr → 1930-yil avgust → 1931-yil 25-aprel → 1938-yil 4-oktyabr.")
t.MAPN(CA, ['Samarqand', 'Toshkent', 'Qo‘qon', 'Buxoro'], "“Botir gapchilar” ishi to‘qilgan shahar qaysi raqam bilan belgilangan?",
       "Qo‘qonda Ashurali Zohiriy boshchiligidagi 19 nafar kishi “botir gapchilar” deb ayblangan.", ask_idx=2)
t.VENN("“Qosimovchilik”", "“Milliy Istiqlol” ishi",
       [("O‘zSSR Oliy sudi raisi ayblangan", 1), ("sud 1930-yilda Samarqandda bo‘lgan", 1),
        ("Munavvarqori boshchiligidagi 87 kishi ayblangan", 2), ("sud Moskvada bo‘lgan", 2),
        ("ayblanuvchilarning bir qismi otishga hukm qilingan", 3)],
       "Qosimovchilik – Oliy sud raisi, Samarqand; Milliy Istiqlol – Munavvarqori, Moskva; ikkalasida otish hukmlari chiqarilgan.")

# 16-§. Ikkinchi jahon urushining boshlanishi
t = Topic('e10u16', 10116); TOPICS['e10u16'] = t
t.B("SSSR va Germaniya o‘rtasida hujum qilmaslik to‘g‘risidagi bitim qachon imzolandi?", "1939-yil 23-avgustda", "1939-yil 1-sentyabrda", "1939-yil 28-sentyabrda", "1941-yil 22-iyunda", "1939-yil 23-avgustda Moskvada.")
t.B("1939-yil 23-avgustdagi bitim tarixda qanday nom bilan mashhur?", "Molotov-Ribbentrop pakti", "Myunxen bitimi", "Brest tinchligi", "Rapallo shartnomasi", "Molotov-Ribbentrop pakti.")
t.B("Molotov-Ribbentrop pakti necha yil muddatga tuzilgan?", "10 yil", "5 yil", "20 yil", "25 yil", "10 yil muddatga.")
t.B("Ikkinchi jahon urushi qachon boshlandi?", "1939-yil 1-sentyabrda", "1939-yil 3-sentyabrda", "1941-yil 22-iyunda", "1939-yil 17-sentyabrda", "Germaniyaning Polshaga hujumi bilan 1939-yil 1-sentyabrda.")
t.B("SSSR qo‘shinlari Polsha hududiga qachon bostirib kirdi?", "1939-yil 17-sentyabrda", "1939-yil 1-sentyabrda", "1939-yil 22-sentyabrda", "1939-yil 28-sentyabrda", "17-sentyabrda.")
t.B("Sovet va nemis qo‘shinlarining qo‘shma paradi qayerda o‘tkazildi?", "Brest-Litovskda", "Vilnyusda", "Varshavada", "Moskvada", "22-sentyabrda Brest-Litovskda.")
t.B("SSSR va Germaniya o‘rtasida do‘stlik va chegaralar to‘g‘risidagi shartnoma qachon imzolandi?", "1939-yil 28-sentyabrda", "1939-yil 23-avgustda", "1939-yil 22-sentyabrda", "1940-yil iyulda", "28-sentyabrda.")
t.B("Moldaviya SSR SSSR tarkibidagi nechanchi ittifoqdosh respublika edi?", "15-", "11-", "16-", "12-", "15-ittifoqdosh respublika.")
t.B("Sovet-fin urushi qaysi sanalarda bo‘lib o‘tdi?", "1939-yil 30-noyabr – 1940-yil 12-mart", "1939-yil 1-sentyabr – 1940-yil iyul", "1940-yil 12-mart – 1941-yil 22-iyun", "1939-yil 17-sentyabr – 28-sentyabr", "1939-yil 30-noyabr – 1940-yil 12-mart.")
t.B("Millatlar Ligasi SSSRni qachon agressor deb e’lon qilib, a’zolikdan chiqardi?", "1939-yil 14-dekabrda", "1940-yil 12-martda", "1939-yil 30-noyabrda", "1941-yil 22-iyunda", "1939-yil 14-dekabrda.")
t.B("Sovet-fin urushi natijasida SSSR qaysi hududlarni qo‘lga kiritdi?", "Viborg shahri va Ladoga ko‘li atrofidagi hududlar", "Bessarabiya", "G‘arbiy Ukraina", "Latviya va Litva", "Viborg shahri va Ladoga ko‘li atroflari.")
t.B("Davlat Mudofaa Qo‘mitasi (DMQ) qachon tuzildi?", "1941-yil 30-iyunda", "1941-yil 22-iyunda", "1941-yil 19-iyulda", "1941-yil 8-avgustda", "1941-yil 30-iyunda Stalin raisligida.")
t.B("Stalin SSSR Qurolli kuchlari Oliy Bosh qo‘mondoni lavozimini qachon egalladi?", "1941-yil 8-avgustda", "1941-yil 19-iyulda", "1941-yil 30-iyunda", "1941-yil 22-iyunda", "8-avgustda; 19-iyulda esa Mudofaa xalq komissari bo‘ldi.")
t.B("Urush yillarida O‘zKP MK birinchi sekretari kim bo‘lgan?", "Usmon Yusupov", "Akmal Ikromov", "Yo‘ldosh Oxunboboyev", "Fayzulla Xo‘jayev", "Usmon Yusupov.")
t.B("Urushning dastlabki kunlarida harbiy komissarliklarga ko‘ngillilardan nechadan ortiq ariza tushdi?", "14 mingdan ortiq", "30 mingdan ortiq", "100 mingdan ortiq", "5 mingdan ortiq", "14 mingdan ortiq ariza.")
t.B("Urush yillarida O‘zbekiston aholisi mudofaa jamg‘armasiga jami qancha pul topshirdi?", "649,9 mln rubl", "30 mln rubl", "1,16 mlrd rubl", "395,5 mln rubl", "649,9 mln rubl, 22 kg oltin va kumush.")
t.B("Mashhur raqqosa Tamaraxonim mudofaa fondiga qancha mablag‘ topshirdi?", "50 ming so‘m", "100 ming so‘m", "30 ming so‘m", "1 mln so‘m", "50 ming so‘m.")
t.B("O‘rta Osiyo va Qozog‘istonga evakuatsiya qilingan 308 korxonaning nechadan ortig‘i O‘zbekistonga joylashtirildi?", "100 dan ortig‘i", "50 dan ortig‘i", "200 dan ortig‘i", "308 tasi", "100 dan ortig‘i.")
t.B("Toshkent aviatsiya zavodi qaysi shahardan ko‘chirib keltirilgan zavod asosida barpo etildi?", "Moskva viloyati Ximki shahridan", "Leningraddan", "Kiyevdan", "Xarkovdan", "Ximki shahridan ko‘chirilgan zavod asosida 1941-yil oktyabrda.")
t.NAT("1941-yil 22-iyunda Germaniya to‘satdan SSSRga bostirib kirdi.", "mamlakatda harbiy holat joriy etildi", "SSSR Millatlar Ligasidan chiqarildi", "sovet-fin urushi boshlandi", "Molotov-Ribbentrop pakti imzolandi", "O‘sha kuni harbiy holat joriy etilganligi haqida farmon e’lon qilindi.")
t.NAT("SSSR Finlyandiyaga hujum qildi.", "Millatlar Ligasi SSSRni agressor deb e’lon qilib, a’zolikdan chiqardi", "Finlyandiya SSSRga qo‘shildi", "Angliya SSSRga urush e’lon qildi", "Germaniya SSSRga hujum qildi", "1939-yil 14-dekabrda SSSR Ligadan chiqarildi.")
t.TF("1940-yil iyulda Latviya, Litva va Estoniya majburiy ravishda SSSR tarkibiga kiritildi.", True, "To‘g‘ri.")
t.TF("1939-yil 3-sentyabrda AQSH va Fransiya Germaniyaga urush e’lon qildi.", False, "Noto‘g‘ri: 3-sentyabrda Fransiya va Angliya urush e’lon qildi.")
t.MUL([("1941-yil oxirigacha ko‘chirib keltirilgan korxonalardan 50 tasi ishga tushirildi.", True),
       ("Toshkent aviatsiya zavodi front uchun qiruvchi samolyotlar ishlab chiqargan.", True),
       ("Urushning dastlabki kunlarida aholidan 649,9 mln rubl mablag‘ tushdi.", False)],
      "III noto‘g‘ri: dastlabki kunlarda 30 mln rubl tushgan; 649,9 mln rubl – butun urush yillaridagi jami.")
t.MATCH("Sanalarni voqealar bilan moslashtiring.", ["1939-yil 23-avgust", "1939-yil 1-sentyabr", "1941-yil 22-iyun", "1941-yil 30-iyun"],
        ["Germaniyaning SSSRga hujumi", "Davlat Mudofaa Qo‘mitasining tuzilishi", "Molotov-Ribbentrop pakti", "Germaniyaning Polshaga hujumi"],
        "cdab", "23-avgust – pakt; 1-sentyabr – Polshaga hujum; 22-iyun – SSSRga hujum; 30-iyun – DMQ.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["Molotov-Ribbentrop paktining imzolanishi", "Sovet qo‘shinlarining Polshaga bostirib kirishi", "Sovet-fin urushining boshlanishi", "Boltiqbo‘yi respublikalarining SSSRga qo‘shib olinishi", "Germaniyaning SSSRga hujumi"],
      "1939-yil 23-avgust → 17-sentyabr → 30-noyabr → 1940-yil iyul → 1941-yil 22-iyun.")
t.MAPMATCH('europe', ['Moskva', 'Brest-Litovsk', 'Vilnyus', 'Viborg'],
           ["1939-yil 23-avgustda hujum qilmaslik to‘g‘risidagi bitim imzolangan shahar", "1939-yil 22-sentyabrda sovet va nemis qo‘shinlarining qo‘shma paradi o‘tkazilgan shahar",
            "1939-yil 19-sentyabrda qizil armiya bosib olgan shahar", "sovet-fin urushi natijasida SSSR qo‘lga kiritgan shahar"],
           "1 – Moskva; 2 – Brest-Litovsk; 3 – Vilnyus; 4 – Viborg.")
t.VENN("Polsha bo‘linishi (1939)", "Sovet-fin urushi (1939 – 1940)",
       [("Brest-Litovskda qo‘shma parad o‘tkazilgan", 1), ("G‘arbiy Ukraina va G‘arbiy Belorusiya SSSRga qo‘shib olingan", 1),
        ("SSSR Millatlar Ligasidan chiqarilgan", 2), ("o‘zbekistonlik jangchilar A.Magalov, F.Uteshev qatnashgan", 2),
        ("SSSRning bosqinchilik siyosati natijasi", 3)],
       "Polsha – Brest-Litovsk paradi, G‘arbiy Ukraina va Belorusiya; fin urushi – Ligadan chiqarish, o‘zbekistonliklar; ikkalasi SSSR bosqinchiligi.")
