from qlib import Topic, PLACES, REG
TOPICS = {}
PLACES.update({'Mo‘ynoq': (59.0, 43.77), 'Quvasoy': (71.98, 40.3), 'Navoiy': (65.38, 40.1)})

# 25-§. Ekologik vaziyat va Orol fojiasi
t = Topic('e10u25', 10125); TOPICS['e10u25'] = t
t.B("Sovet hokimiyati va kommunistik partiya ekologiya muammosiga qanday munosabatda bo‘ldi?", "mamlakatimizda ekologiya muammosi yo‘q, deb hech qanday chora ko‘rmadi", "ekologiyani muhofaza qilish dasturini qabul qildi", "barcha kimyo zavodlarini yopdi", "olimlarga keng erkinlik berdi", "“Ekologiya muammosi yo‘q” deb chora ko‘rmadi.")
t.B("O‘zbekistondagi yirik og‘ir sanoat tarmoqlari kimning qaramog‘ida bo‘lgan?", "Ittifoq vazirliklari va mahkamalari", "O‘zSSR hukumati", "mahalliy Sovetlar", "kasaba uyushmalari", "Ittifoq vazirliklari va mahkamalari qaramog‘ida.")
t.B("Kimyo zavodlari asosan qaysi shaharlarda qurilgan edi?", "Navoiy, Chirchiq, Farg‘ona", "Xiva, Buxoro, Samarqand", "Nukus, Termiz, Qarshi", "Jizzax, Guliston, Andijon", "Aholisi ko‘p Navoiy, Chirchiq, Farg‘ona shaharlarida.")
t.B("XX asr 80-yillari o‘rtalarida respublikada qishloq xo‘jaligida qancha pestitsid qo‘llanildi?", "90 000 tonna", "9000 tonna", "900 000 tonna", "30 000 tonna", "90 000 tonna pestitsid.")
t.B("G‘o‘zani defoliatsiya qilishda ishlatilgan o‘ta zaharli kimyoviy modda qaysi?", "butifos", "pestitsid DDT", "selitra", "fosfat", "Butifos.")
t.B("Butifos O‘zbekistonda necha yil davomida ishlatildi?", "20 yil", "10 yil", "30 yil", "5 yil", "20 yil davomida.")
t.B("O‘zbekiston rahbariyati butifosdan foydalanishni qachon taqiqladi?", "1981-yili", "1986-yili", "1975-yili", "1991-yili", "1981-yili.")
t.B("“Defoliatsiya” nimani anglatadi?", "g‘o‘zaning bargini to‘kish", "zararkunandalarni yo‘qotish", "tuproqni o‘g‘itlash", "chigit ekish", "G‘o‘zani defoliatsiya qilish – bargini to‘kish.")
t.B("Orol dengizi hozirgi vaqtda nechta bo‘lakka bo‘lingan?", "3 ta", "2 ta", "4 ta", "5 ta", "Shimoliy, sharqiy va g‘arbiy qismlar.")
t.B("Orol dengizining qaysi qismi eng chuqur hisoblanadi?", "g‘arbiy qismi", "shimoliy qismi", "sharqiy qismi", "janubiy qismi", "Eng chuquri – g‘arbiy qismi.")
t.B("Qaysi daryolar suvining kamayishi Orolning qurishiga sabab bo‘ldi?", "Amudaryo va Sirdaryo", "Zarafshon va Qashqadaryo", "Chirchiq va Ohangaron", "Surxondaryo va Vaxsh", "Amudaryo va Sirdaryodan quyiladigan suv kamaydi.")
t.B("1980 – 1985-yillarda Orolbo‘yida paxtachilik va chorvachilik har yili qancha zarar ko‘rdi?", "30 mln rubldan ortiq", "90 mln rubl", "5 mln rubl", "1 mlrd rubl", "Har yili 30 mln rubldan ortiq.")
t.B("1986-yilda Orolbo‘yida bir yoshgacha bo‘lgan bolalar o‘limi har ming bolaga nisbatan nechaga yetdi?", "72 nafarga", "46,5 nafarga", "60 nafarga", "30 nafarga", "1980-yil – 46,5, 1986-yil – 72 nafar.")
t.B("Orolbo‘yida ayollarning necha foizi kamqonlik kasalligiga chalingan edi?", "60 foizi", "30 foizi", "72 foizi", "46,5 foizi", "60 foizi.")
t.B("Orolbo‘yida qorin tifi kasalligi necha marta ortdi?", "30 marta", "7 marta", "3 marta", "10 marta", "Qorin tifi 30 marta, yuqumli sariq 7 marta.")
t.B("Dunyodagi eng yosh cho‘l qanday nomlanadi?", "Orolqum", "Qizilqum", "Qoraqum", "Mirzacho‘l", "Orol cho‘li – Orolqum.")
t.B("Orol dengizining qancha qismi quruqlikka aylandi?", "40 000 km² dan ziyod", "4000 km²", "400 km²", "1 mln km²", "40 000 km² dan ziyod qismi.")
t.NAT("XX asr 60-yillaridan sug‘oriladigan ekin maydonlari kengaytirildi.", "Orolga quyiladigan suv kamayib, dengiz quriy boshladi", "Orol dengizi sathi ko‘tarildi", "baliqchilik rivojlandi", "Orolbo‘yi aholisi boyidi", "Suv kamayib, Orol quriy boshladi, sho‘rlanish kuchaydi.")
t.NAT("Orol dengizi qurishi natijasida Orolbo‘yida og‘ir ekologik vaziyat yuzaga keldi.", "baliqchilik, mo‘ynachilik, ovchilik xo‘jaliklari yo‘q bo‘lib ketdi", "yangi baliqchilik xo‘jaliklari ochildi", "aholi salomatligi yaxshilandi", "paxta hosildorligi oshdi", "Amudaryo quyi oqimida bu xo‘jaliklar yo‘q bo‘ldi.")
t.TF("Zaharli moddalar bilan ishlov berish maydonlarining taxminan yarmida samolyotlarda bajarildi.", True, "To‘g‘ri.")
t.TF("Butifos taqiqlangandan keyin hech bir xo‘jalik undan foydalanmadi.", False, "Noto‘g‘ri: ayrim xo‘jaliklar keyinchalik ham foydalandilar.")
t.MUL([("Orolbo‘yi ma’muriy jihatdan O‘zbekiston va Qozog‘iston hududlaridan iborat.", True),
       ("Butifos ko‘p hollarda belgilangan me’yordan 2 – 3 baravar ko‘p ishlatilgan.", True),
       ("Orol dengizining sayoz shimoliy qismi eng katta maydonga ega.", False)],
      "III noto‘g‘ri: shimoliy qismi kichik va sayoz; nisbatan kattarog‘i sharqiy qismi.")
t.MATCH("Orolbo‘yidagi kasalliklar o‘sishini ko‘rsatkichlar bilan moslashtiring.", ["qorin tifi", "yuqumli sariq", "kamqonlik (ayollar)"],
        ["7 marta ortdi", "60 foiz ayollar chalingan", "30 marta ortdi"], "cab", "Qorin tifi – 30 marta; sariq – 7 marta; kamqonlik – 60 % ayollar.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["Orolga quyiladigan suvning kamaya boshlashi (60-yillar)", "Bolalar o‘limining 1000 taga 46,5 nafarga yetishi", "Butifosning taqiqlanishi", "Bolalar o‘limining 1000 taga 72 nafarga yetishi"],
      "1960-yillar → 1980 → 1981 → 1986.")
t.MAPN('uzb', ['Mo‘ynoq', 'Navoiy', 'Toshkent', 'Termiz'], "Baliqchilik bilan nom chiqargan, aholisining ko‘pchiligi Orol qurishi tufayli 10 – 15 yilda ishsiz qolgan shahar qaysi raqam bilan belgilangan?",
       "Mo‘ynoqliklarning ko‘pchiligi 10 – 15 yil ichida ishsiz va nochor ahvolga tushdi.")
t.VENN("Sanoat ifloslanishi", "Qishloq xo‘jaligidagi ifloslanish",
       [("kimyo kombinatlarining zaharli gaz va chiqindilari", 1), ("Navoiy, Chirchiq, Farg‘ona kimyo zavodlari", 1),
        ("90 000 tonna pestitsid qo‘llanishi", 2), ("butifos bilan defoliatsiya", 2),
        ("aholi salomatligiga jiddiy zarar yetkazgan", 3)],
       "Sanoat – kimyo zavodlari; qishloq xo‘jaligi – pestitsid, butifos; ikkalasi aholi salomatligiga zarar yetkazgan.")

# 26-§. Paxta ishi va uning oqibatlari
t = Topic('e10u26', 10126); TOPICS['e10u26'] = t
t.B("Leonid Brejnev qachon vafot etdi?", "1982-yil noyabrda", "1983-yil oktyabrda", "1985-yil 11-martda", "1984-yilda", "1982-yil noyabrda.")
t.B("Brejnev mamlakat va partiyani necha yil boshqargan?", "18 yil", "25 yil", "10 yil", "30 yil", "18 yil davomida.")
t.B("1982 – 1984-yillarda Sovet Ittifoqiga kim rahbarlik qildi?", "Yuriy Andropov", "Konstantin Chernenko", "Mixail Gorbachyov", "Andrey Gromiko", "Yuriy Andropov.")
t.B("1984 – 1985-yillarda SSSRga kim rahbarlik qildi?", "Konstantin Chernenko", "Yuriy Andropov", "Leonid Brejnev", "Mixail Gorbachyov", "Konstantin Chernenko.")
t.B("Mixail Gorbachyov KPSS MK Bosh sekretari qachon saylandi?", "1985-yil 11-martda", "1985-yil 2-iyulda", "1982-yil noyabrda", "1984-yil 23-iyunda", "1985-yil 11-martda.")
t.B("1985-yil 2-iyulda SSSR Oliy Soveti Prezidiumi raisi lavozimiga kim saylandi?", "Andrey Gromiko", "Mixail Gorbachyov", "Y.K.Ligachev", "Yuriy Andropov", "Andrey Gromiko.")
t.B("Sharof Rashidov qachon vafot etdi?", "1983-yil oktyabrda", "1982-yil noyabrda", "1984-yil 23-iyunda", "1985-yilda", "1983-yil oktyabrda.")
t.B("1983 – 1988-yillarda O‘zbekistonga kim rahbarlik qildi?", "Inomjon Usmonxo‘jayev", "Rafiq Nishonov", "Islom Karimov", "Sharof Rashidov", "Inomjon Usmonxo‘jayev; 1988 – 1989 – Rafiq Nishonov.")
t.B("“Paxta ishi”ni boshlab bergan O‘zKP MK XVI plenumi qachon bo‘ldi?", "1984-yil 23-iyunda", "1983-yil oktyabrda", "1985-yil aprelda", "1989-yil 23-iyunda", "1984-yil 23-iyunda.")
t.B("XVI plenumda Moskvadan maxsus yuborilgan KPSS MK sekretari kim edi?", "Y.K.Ligachev", "T.X.Gdlyan", "N.V.Ivanov", "A.Gromiko", "KPSS MK sekretari Y.K.Ligachev.")
t.B("Asosiy maxsus tergov guruhlaridan biri kimlar rahbarligida tuzilgan?", "T.X.Gdlyan va N.V.Ivanov", "Y.K.Ligachev va A.Gromiko", "Y.Andropov va K.Chernenko", "R.Nishonov va I.Usmonxo‘jayev", "T.X.Gdlyan va N.V.Ivanov rahbarligida 1983-yil aprelda.")
t.B("1983 – 1987-yillarda O‘zbekistonga nechaga yaqin “desantchi” yuborildi?", "1000 nafarga yaqin", "3000 nafardan ortiq", "40 000 nafar", "5000 nafar", "1000 nafarga yaqin.")
t.B("1985 – 1990-yillarda “paxta ishi” bo‘yicha jami qancha kishi tergov qilindi?", "40 000 kishi", "5000 kishi", "3000 kishi", "1000 kishi", "40 000 kishi tergov qilindi.")
t.B("“Paxta ishi” bo‘yicha nechta kishi soxta ayblar bilan jinoiy javobgarlikka tortildi?", "5000 nafar", "40 000 nafar", "1000 nafar", "3000 nafar", "5000 nafar.")
t.B("Markaziy matbuotda “paxta ishi” qanday nomga aylantirildi?", "“o‘zbeklar ishi”", "“Rashidov ishi”", "“oltin ishi”", "“Farg‘ona ishi”", "“O‘zbeklar ishi”ga aylantirildi.")
t.B("Sh.Rashidovni o‘limidan so‘ng badnom qilish uchun qaysi sun’iy ibora o‘ylab topildi?", "“Sharof Rashidovchilik”", "“qosimovchilik”", "“inog‘omovchilik”", "“badriddinovchilik”", "“Sharof Rashidovchilik”.")
t.B("“Sanksiya” atamasi nimani anglatadi?", "hujjat, qarorning oliy organ tomonidan tasdiqlanishi", "jinoyatchini ajratib qo‘yish xonasi", "qamoq muddati", "tergov guruhi", "Oliy organ tomonidan tasdiqlanib, qonuniy kuchga kirishi.")
t.NAT("1984-yil 23-iyunda O‘zKP MK XVI plenumi bo‘lib o‘tdi.", "O‘zbekistonda “paxta ishi” deb atalgan siyosiy qatag‘onlar boshlandi", "Sharof Rashidov oqlandi", "paxta xarid narxi oshirildi", "O‘zbekiston mustaqil bo‘ldi", "Plenum o‘zbek xalqini asossiz badnom qilish kompaniyasini boshlab berdi.")
t.NAT("Qo‘shib yozish va korrupsiya deyarli barcha hududlarda bo‘lsa-da, “tajriba maydoni” sifatida O‘zbekiston tanlandi.", "ko‘plab odamlar aybsiz jazoga tortildi", "korrupsiya butunlay tugatildi", "O‘zbekiston rahbarlari mukofotlandi", "faqat aybdorlar jazolandi", "Minglab kishilar nohaq jazolandi.")
t.TF("“Desantchilar” va 3000 dan ortiq tergovchilarga ba’zi mahalliy rahbarlar va huquq-tartibot xodimlari yordam bergan.", True, "To‘g‘ri.")
t.TF("“Paxta ishi” bo‘yicha tergov qilinganlarning barchasi prokuror sanksiyasi bilan qamalgan.", False, "Noto‘g‘ri: aksariyati prokuror sanksiyasisiz tergov izolyatorlarida o‘tirgan.")
t.MUL([("1985-yildan mamlakatda qayta qurish siyosati boshlandi.", True),
       ("Sharof Rashidov respublikani qariyb chorak asr boshqargan.", True),
       ("Maxsus tergov guruhlarining dastlabkisi O‘zbekistonga 1986-yilda yuborilgan.", False)],
      "III noto‘g‘ri: dastlabkisi 1983-yil boshlarida yuborilgan.")
t.MATCH("SSSR rahbarlarini boshqaruv davri bilan moslashtiring.", ["Yuriy Andropov", "Konstantin Chernenko", "Mixail Gorbachyov"],
        ["1985-yil 11-martdan", "1982 – 1984-yillar", "1984 – 1985-yillar"], "bca",
        "Andropov – 1982 – 1984; Chernenko – 1984 – 1985; Gorbachyov – 1985-yil 11-martdan.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["Brejnevning vafoti", "Gdlyan va Ivanov tergov guruhining tuzilishi", "Sharof Rashidovning vafoti", "O‘zKP MK XVI plenumi", "Gorbachyovning Bosh sekretar etib saylanishi"],
      "1982-yil noyabr → 1983-yil aprel → 1983-yil oktyabr → 1984-yil 23-iyun → 1985-yil 11-mart.")
t.VENN("1930-yillar qatag‘oni", "“Paxta ishi” (1980-yillar)",
       [("Fitrat, Cho‘lpon, Qodiriy otib tashlangan", 1), ("“qosimovchilik”, “inog‘omovchilik” ishlari to‘qilgan", 1),
        ("“desantchilar” O‘zbekistonga yuborilgan", 2), ("“Sharof Rashidovchilik” iborasi o‘ylab topilgan", 2),
        ("Markaz tomonidan uyushtirilgan siyosiy qatag‘on", 3)],
       "30-yillar – Fitrat, Cho‘lpon, Qodiriy, qosimovchilik; 80-yillar – desantchilar, Rashidovchilik; ikkalasi Markaz qatag‘oni.")

# 27-§. Qayta qurish siyosati va Farg‘ona fojialari
t = Topic('e10u27', 10127); TOPICS['e10u27'] = t
t.B("Sovet jamiyatini chuqur isloh qilish yo‘lini e’lon qilgan plenum qaysi?", "KPSS MK Aprel (1985-y.) plenumi", "O‘zKP MK XVI plenumi", "O‘zKP MK X plenumi", "KPSS XX syezdi", "KPSS MK 1985-yil Aprel plenumi.")
t.B("Qayta qurishning asosiy tarkibiy qismlari deb nimalar belgilandi?", "ijtimoiy hayotni demokratlashtirish va tub iqtisodiy islohot", "kollektivlashtirish va industrlashtirish", "qatag‘on va tozalash", "harbiy islohot va qurollanish", "Demokratlashtirish va tub iqtisodiy islohot.")
t.B("Qayta qurishning birinchi bosqichi qaysi yillarni o‘z ichiga oladi?", "1985 – 1986-yillar", "1987 – 1989-yillar", "1989 – 1991-yillar", "1982 – 1985-yillar", "1985 – 1986-yillar.")
t.B("Qayta qurishning ikkinchi bosqichi qaysi yillarni o‘z ichiga oladi?", "1987 – 1989-yillar", "1985 – 1986-yillar", "1990 – 1991-yillar", "1983 – 1987-yillar", "1987 – 1989-yillar.")
t.B("Qayta qurishning ikkinchi bosqichida asosiy maqsad nima ekanligi ta’kidlandi?", "sovet jamiyatini to‘liq demokratlashtirish", "kollektivlashtirishni yakunlash", "SSSRni tarqatish", "markazlashtirishni kuchaytirish", "Sovet jamiyatini to‘liq demokratlashtirish.")
t.B("1989-yil may – iyunda millatlararo to‘qnashuv qayerda boshlandi?", "Quvasoyda", "Qo‘qonda", "O‘shda", "Toshkentda", "Quvasoyda yoshlar o‘rtasidagi bezorilikdan.")
t.B("Farg‘ona voqealarida kimlar o‘rtasida to‘qnashuv bo‘ldi?", "mesxeti turklari bilan mahalliy yoshlar", "qirg‘izlar bilan o‘zbeklar", "tojiklar bilan o‘zbeklar", "ruslar bilan o‘zbeklar", "Mesxeti turklari bilan mahalliy yoshlar.")
t.B("1989-yil 7 – 8-iyunda Qo‘qonda tinch namoyish o‘qqa tutilishi natijasida nechadan ziyod kishi halok bo‘ldi?", "50 dan ziyod", "103 nafar", "1011 nafar", "757 nafar", "50 dan ziyod namoyishchi.")
t.B("1989-yil 3 – 12-iyunda Farg‘ona viloyatidagi to‘qnashuvlarda rasmiy ma’lumotlarga ko‘ra necha kishi halok bo‘ldi?", "103 nafar", "50 nafar", "1011 nafar", "757 nafar", "103 halok, 1011 jarohatlangan, 757 xonadonga o‘t qo‘yilgan.")
t.B("“O‘zbekiston yana bir Farg‘onaga chidab tura olmaydi” degan so‘zlar kimga tegishli?", "Islom Karimov", "Rafiq Nishonov", "Mixail Gorbachyov", "Inomjon Usmonxo‘jayev", "Islom Karimov.")
t.B("“O‘zbekiston SSR davlat tili haqida”gi Qonun qachon qabul qilindi?", "1989-yil 21-oktyabrda", "1990-yil 20-iyunda", "1991-yil 31-avgustda", "1989-yil 23-iyunda", "1989-yil 21-oktyabrda.")
t.B("“Davlat tili haqida”gi Qonun respublika Oliy Sovetining qaysi sessiyasida qabul qilindi?", "XI sessiyasida", "VI sessiyasida", "II sessiyasida", "I sessiyasida", "Oliy Sovetning XI sessiyasida.")
t.B("1990-yil iyunda O‘sh va O‘zgan shaharlarida kimlar o‘rtasida etnik mojaro kelib chiqdi?", "qirg‘izlar bilan o‘zbeklar", "mesxeti turklari bilan o‘zbeklar", "tojiklar bilan qirg‘izlar", "ruslar bilan qirg‘izlar", "Qirg‘izlar bilan o‘zbeklar (O‘sh qirg‘ini).")
t.B("“Partokratik” atamasi nimani anglatadi?", "partiya hukmronligiga asoslangan", "ko‘ppartiyaviylik", "partiyasiz boshqaruv", "demokratik saylov", "Partiya hukmronligiga asoslangan.")
t.NAT("Qayta qurish siyosati amalga oshirildi.", "oshkoralik, demokratiya va fikrlar xilma-xilligi ma’lum ma’noda kuchaydi", "KPSS mavqeyi mustahkamlandi", "SSSR kuchaydi", "qatag‘onlar kuchaydi", "Oshkoralik va demokratiya kuchayishiga imkoniyat yaratildi.")
t.NAT("1989-yil 21-oktyabrda o‘zbek tiliga davlat tili maqomi berildi.", "o‘zbek tili va madaniyatining rivojlanishiga imkoniyat yaratildi", "boshqa tillar taqiqlandi", "rus tili davlat tiliga aylandi", "Farg‘ona fojiasi boshlandi", "O‘zbek tili va madaniyati rivojiga imkon yaratildi.")
t.TF("Qayta qurishning aniq, izchil, ilmiy jihatdan puxta ishlab chiqilgan dasturi yo‘q edi.", True, "To‘g‘ri, bu uning barbod bo‘lish sabablaridan biri.")
t.TF("Qayta qurish davrida Kreml ittifoqdosh respublikalarning SSSRdan ajralib chiqishini qo‘llab-quvvatladi.", False, "Noto‘g‘ri: Kreml bunga jon-jahdi bilan qarshi turdi.")
t.MUL([("O‘sha paytdagi O‘zbekiston rahbariyati Markazga yaqinlashish yo‘lini tanladi.", True),
       ("Qayta qurish davrida saylov tizimini o‘zgartirish to‘g‘risida qonun qabul qilindi.", True),
       ("Farg‘ona voqealarida 1011 kishi halok bo‘lgan.", False)],
      "III noto‘g‘ri: 103 kishi halok bo‘lgan, 1011 kishi jarohatlangan.")
t.MATCH("Raqamlarni Farg‘ona voqealari bo‘yicha ma’lumotlar bilan moslashtiring.", ["103", "1011", "757"],
        ["o‘t qo‘yilgan xonadonlar", "halok bo‘lganlar", "jarohatlanganlar"], "bca", "103 – halok; 1011 – jarohatlangan; 757 – xonadon.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["KPSS MK Aprel plenumi", "Quvasoydagi to‘qnashuv", "Qo‘qonda namoyishning o‘qqa tutilishi", "Davlat tili haqidagi Qonun", "O‘sh va O‘zgandagi etnik mojaro"],
      "1985-yil aprel → 1989-yil may – iyun → 1989-yil 7 – 8-iyun → 1989-yil 21-oktyabr → 1990-yil iyun.")
t.MAPMATCH('fargona', ['Quvasoy', 'Qo‘qon', 'O‘sh'],
           ["1989-yil may – iyunda yoshlar o‘rtasidagi bezorilik millatlararo to‘qnashuvga sabab bo‘lgan joy", "1989-yil 7 – 8-iyunda tinch namoyish o‘qqa tutilgan shahar", "1990-yil iyunda qirg‘izlar va o‘zbeklar o‘rtasida etnik mojaro bo‘lgan shahar"],
           "1 – Quvasoy; 2 – Qo‘qon; 3 – O‘sh.")
t.VENN("Qayta qurishning I bosqichi (1985 – 1986)", "Qayta qurishning II bosqichi (1987 – 1989)",
       [("tadbirlar an’anaviy usullarda olib borilgan", 1), ("ilmiy-texnika taraqqiyoti asosida iqtisodiy taraqqiyotni jadallashtirish", 1),
        ("jamiyatning barcha jabhalarini kompleks isloh qilish", 2), ("sovet jamiyatini to‘liq demokratlashtirish maqsadi", 2),
        ("M.S.Gorbachyov rahbarligida o‘tkazilgan", 3)],
       "I bosqich – an’anaviy usullar, jadallashtirish; II bosqich – kompleks islohot, demokratlashtirish; ikkalasi Gorbachyov davrida.")

# 28-§. O‘zbekiston mustaqillikka erishish ostonasida
t = Topic('e10u28', 10128); TOPICS['e10u28'] = t
t.B("Islom Karimov O‘zKP MK birinchi sekretari qachon saylandi?", "1989-yil 23-iyunda", "1990-yil 24-martda", "1991-yil 31-avgustda", "1988-yil noyabrda", "1989-yil 23-iyunda.")
t.B("“Birlik” xalq harakati qachon tashkil topdi?", "1988-yil noyabrda", "1990-yil 30-aprelda", "1989-yil iyunda", "1991-yil avgustda", "1988-yil noyabrda.")
t.B("“Birlik” xalq harakatining rahbari kim bo‘lgan?", "professor Abdurahim Po‘latov", "Muhammad Solih", "Shukurulla Mirsaidov", "Mirahmad Mirqosimov", "Professor Abdurahim Po‘latov.")
t.B("“Erk” demokratik partiyasining ta’sis qurultoyi qachon bo‘ldi?", "1990-yil 30-aprelda", "1988-yil noyabrda", "1990-yil 20-iyunda", "1991-yil 29-dekabrda", "1990-yil 30-aprelda.")
t.B("“Erk” partiyasini tuzish harakatini kim boshlagan?", "shoir Muhammad Solih (Saloy Madaminov)", "Abdurahim Po‘latov", "Islom Karimov", "Rafiq Nishonov", "Shoir Muhammad Solih.")
t.B("“Birlik” va “Erk” qachondan O‘zbekiston hududida siyosiy faoliyatini to‘xtatdi?", "1992-yildan", "1990-yildan", "1991-yildan", "1995-yildan", "1992-yildan.")
t.B("O‘zbekistonda prezidentlik boshqaruvi qachon ta’sis etildi?", "1990-yil 24-martda", "1990-yil 20-iyunda", "1991-yil 31-avgustda", "1991-yil 29-dekabrda", "1990-yil 24-martda.")
t.B("Ittifoqdosh respublikalar ichida birinchi bo‘lib qayerda prezidentlik boshqaruvi joriy qilindi?", "O‘zbekistonda", "RSFSRda", "Ukrainada", "Qozog‘istonda", "Birinchi bo‘lib O‘zbekistonda.")
t.B("SSSR Prezidenti lavozimi qayerda ta’sis etildi?", "SSSR Xalq deputatlarining III syezdida (1990-yil 12 – 15-mart)", "KPSS XXVIII syezdida", "SSSR Oliy Soveti sessiyasida 1991-yilda", "Novo-Ogaryovoda", "1990-yil 12 – 15-martda SSSR Xalq deputatlarining III syezdida.")
t.B("1990-yil mart – oktyabrda O‘zSSR Ministrlar Sovetiga kim raislik qildi?", "Shukurulla Mirsaidov", "Mirahmad Mirqosimov", "Rafiq Nishonov", "Islom Karimov", "1989 – 1990 – M.Mirqosimov, 1990-yil mart – oktyabr – Sh.Mirsaidov.")
t.B("O‘zbekistonning Mustaqillik Deklaratsiyasi qachon qabul qilindi?", "1990-yil 20-iyunda", "1990-yil 24-martda", "1991-yil 31-avgustda", "1990-yil 14-dekabrda", "1990-yil 20-iyunda.")
t.B("Qoraqalpog‘iston ASSR suvereniteti to‘g‘risida Deklaratsiya qachon qabul qilindi?", "1990-yil 14-dekabrda", "1990-yil 20-iyunda", "1991-yil 31-avgustda", "1990-yil 12-iyunda", "1990-yil 14-dekabrda.")
t.B("SSSRda birinchi umumxalq referendumi qachon o‘tkazildi?", "1991-yil 17-martda", "1991-yil 23-aprelda", "1990-yil 12-iyunda", "1991-yil 19-avgustda", "1991-yil 17-martda.")
t.B("“9+1” deb nomlangan qo‘shma bayonot qayerda qabul qilindi?", "Novo-Ogaryovoda", "Belovejda", "Toshkentda", "Olmaotada", "1991-yil 23-aprelda Moskva yaqinidagi Novo-Ogaryovoda.")
t.B("GKChPga kim boshchilik qildi?", "vitse-prezident Gennadiy Yanayev", "Boris Yelsin", "Mixail Gorbachyov", "Y.K.Ligachev", "Vitse-prezident G.Yanayev.")
t.B("“O‘zbekiston Respublikasining Davlat Mustaqilligi asoslari to‘g‘risida”gi Qonun qachon qabul qilindi?", "1991-yil 31-avgustda", "1991-yil 1-sentyabrda", "1990-yil 20-iyunda", "1991-yil 29-dekabrda", "1991-yil 31-avgustda.")
t.B("“Davlat Mustaqilligi asoslari to‘g‘risida”gi Qonun necha moddadan iborat?", "17 moddadan", "15 moddadan", "10 moddadan", "21 moddadan", "17 moddadan.")
t.B("SSSR xalqaro huquq subyekti sifatida qachon barham topdi?", "1991-yil 25-dekabrda", "1991-yil 29-avgustda", "1991-yil 31-avgustda", "1992-yil 4-yanvarda", "1991-yil 25-dekabrda.")
t.B("Islom Karimov qachon umumxalq saylovida O‘zbekiston Respublikasi Prezidenti etib saylandi?", "1991-yil 29-dekabrda", "1990-yil 24-martda", "1991-yil 31-avgustda", "1992-yil 4-yanvarda", "1991-yil 29-dekabrda, 5 yil muddatga.")
t.NAT("1991-yil 19 – 21-avgustda Moskvada GKChP tuzildi, ammo B.Yelsin boshchiligidagi kuchlar uni bostirdi.", "ittifoqdosh respublikalar o‘z mustaqilliklarini e’lon qildi", "SSSR mustahkamlandi", "yangi Ittifoq shartnomasi imzolandi", "KPSS kuchaydi", "Isyon barbod bo‘lgach, respublikalar mustaqillik e’lon qildi.")
t.NAT("1990-yil 1-noyabrda ijroiya hokimiyatni takomillashtirish to‘g‘risidagi Qonun qabul qilindi.", "Ministrlar Soveti Prezident huzuridagi Vazirlar Mahkamasiga aylantirildi", "Prezident lavozimi bekor qilindi", "Bosh vazir lavozimi ta’sis etildi", "Oliy Sovet tarqatildi", "I.Karimov bir vaqtda Vazirlar Mahkamasi raisi bo‘ldi.")
t.TF("Mustaqillik bilan Rossiya imperiyasi va SSSRning 125 yil davom etgan mustamlakachilik davriga chek qo‘yildi.", True, "To‘g‘ri.")
t.TF("KPSS 1991-yil 25-dekabrda siyosiy partiya sifatida faoliyatini to‘xtatdi.", False, "Noto‘g‘ri: KPSS 1991-yil 29-avgustda faoliyatini to‘xtatdi; 25-dekabrda SSSR barham topdi.")
t.MUL([("1990-yil 12-iyunda RSFSRning davlat suvereniteti to‘g‘risida Deklaratsiya qabul qilindi.", True),
       ("“9+1” bayonotida 9 ta ittifoqdosh respublika va Markaz ishtirok etgan.", True),
       ("Yangi Ittifoq shartnomasi 1991-yil 20-avgustda imzolandi.", False)],
      "III noto‘g‘ri: shartnoma 20-avgustda imzolanishi kerak edi, ammo imzolanmay qoldi.")
t.MATCH("Prezidentlik boshqaruvi bosqichlarini davrlari bilan moslashtiring.", ["Birinchi bosqich", "Ikkinchi bosqich", "Uchinchi bosqich"],
        ["1991-yil sentyabr – 1992-yil yanvar", "1990-yil mart – oktyabr", "1990-yil noyabr – 1991-yil avgust"], "bca",
        "I – 1990-yil mart – oktyabr; II – 1990-yil noyabr – 1991-yil avgust; III – 1991-yil sentyabr – 1992-yil yanvar.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["Prezidentlik boshqaruvining ta’sis etilishi", "Mustaqillik Deklaratsiyasining qabul qilinishi", "SSSRdagi birinchi umumxalq referendumi", "Davlat Mustaqilligi asoslari to‘g‘risidagi Qonun", "SSSRning barham topishi"],
      "1990-yil 24-mart → 1990-yil 20-iyun → 1991-yil 17-mart → 1991-yil 31-avgust → 1991-yil 25-dekabr.")
t.VENN("“Birlik” xalq harakati", "“Erk” demokratik partiyasi",
       [("1988-yil noyabrda tashkil topgan", 1), ("rahbari Abdurahim Po‘latov", 1),
        ("1990-yil 30-aprelda ta’sis qurultoyi bo‘lgan", 2), ("Muhammad Solih boshchiligida tuzilgan", 2),
        ("1992-yildan O‘zbekistonda faoliyatini to‘xtatgan", 3)],
       "“Birlik” – 1988, Po‘latov; “Erk” – 1990, M.Solih; ikkalasi 1992-yildan faoliyatini to‘xtatgan.")
