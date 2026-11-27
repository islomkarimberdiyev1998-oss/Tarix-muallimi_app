from qlib import Topic
TOPICS = {}

# 27 Qayta qurish va Farg'ona fojialari
t = Topic('e10u27', 10027); TOPICS['e10u27'] = t
t.B("Sovet jamiyatini chuqur isloh qilish yo‘lini qaysi plenum e’lon qilgan?", "KPSS MK Aprel (1985) plenumi", "O‘zbekiston Kompartiyasi XVI plenumi", "KPSS XX syezdi", "KPSS MK 1987-yil yanvar plenumi", "KPSS MK Aprel (1985-y.) plenumi.")
t.B("Qayta qurishning asosiy tarkibiy qismlari nimalar deb belgilangan?", "demokratlashtirish va tub iqtisodiy islohot", "kollektivlashtirish va industrlashtirish", "ruslashtirish va qatag‘on", "harbiylashtirish", "Ijtimoiy hayotni demokratlashtirish va tub iqtisodiy islohot.")
t.B("Qayta qurishning birinchi bosqichi qaysi yillarni o‘z ichiga oladi?", "1985–1986-yillar", "1987–1989-yillar", "1989–1991-yillar", "1982–1985-yillar", "1985–1986-yillar.")
t.B("Qayta qurishning ikkinchi bosqichi qaysi yillarni o‘z ichiga oladi?", "1987–1989-yillar", "1985–1986-yillar", "1990–1991-yillar", "1983–1985-yillar", "1987–1989-yillar.")
t.B("Ikkinchi bosqichning asosiy maqsadi nima deb ta’kidlangan?", "sovet jamiyatini to‘liq demokratlashtirish", "Ittifoqni tarqatish", "kommunizm qurish", "kollektivlashtirish", "Sovet jamiyatini to‘liq demokratlashtirish.")
t.B("Farg‘ona vodiysidagi millatlararo to‘qnashuv qaysi shahardagi bezorilikdan boshlangan?", "Quvasoy", "Qo‘qon", "Farg‘ona", "O‘sh", "1989-yil may–iyunda Quvasoyda.")
t.B("1989-yildagi to‘qnashuv qaysi xalq vakillari bilan mahalliy yoshlar o‘rtasida bo‘lgan?", "mesxeti turklari", "qrim tatarlari", "qirg‘izlar", "tojiklar", "Mesxeti turklari bilan.")
t.B("1989-yil 7–8-iyunda qaysi shaharda tinch namoyish o‘qqa tutilgan?", "Qo‘qonda", "Quvasoyda", "Farg‘onada", "Toshkentda", "Qo‘qonda; 50 dan ziyod namoyishchi halok bo‘lgan.")
t.B("Rasmiy ma’lumotlarga ko‘ra 1989-yil 3–12-iyunda Farg‘ona viloyatida necha kishi halok bo‘lgan?", "103 nafar", "50 nafar", "1011 nafar", "757 nafar", "103 nafar.")
t.B("Farg‘ona fojiasida nechta xonadonga o‘t qo‘yilgan?", "757 ta", "1011 ta", "103 ta", "50 ta", "757 ta.")
t.B("«O‘zbekiston yana bir Farg‘onaga chidab tura olmaydi» degan so‘zlar kimga tegishli?", "Islom Karimov", "Rafiq Nishonov", "Mixail Gorbachyov", "Inomjon Usmonxo‘jayev", "Islom Karimov.")
t.B("O‘zbek tiliga davlat tili maqomi qachon berilgan?", "1989-yil 21-oktyabrda", "1990-yil 20-iyunda", "1991-yil 31-avgustda", "1989-yil 23-iyunda", "1989-yil 21-oktyabrda.")
t.B("Davlat tili haqidagi qonun Oliy Sovetning qaysi sessiyasida qabul qilingan?", "XI sessiyasida", "VI sessiyasida", "I sessiyasida", "II sessiyasida", "Respublika Oliy Sovetining XI sessiyasida.")
t.B("1990-yil iyunda O‘sh va O‘zganda qaysi xalqlar o‘rtasida etnik mojaro bo‘lgan?", "qirg‘izlar va o‘zbeklar", "o‘zbeklar va mesxeti turklari", "tojiklar va qirg‘izlar", "qozoqlar va o‘zbeklar", "Qirg‘izlar va o‘zbeklar.")
t.NAT("Qayta qurishning aniq va ilmiy jihatdan puxta dasturi yo‘q edi, nomenklatura saqlanib qoldi.", "qayta qurish safsatabozlikka aylanib, mag‘lubiyatga uchradi", "qayta qurish to‘liq muvaffaqiyat qozondi", "SSSR mustahkamlandi", "KPSS kuchaydi", "Qayta qurish barbod bo‘ldi.")
t.NAT("Davlat tili haqidagi qonun qabul qilindi.", "o‘zbek tili va madaniyatining rivojlanishiga imkoniyat yaratildi", "boshqa tillar taqiqlandi", "rus tili davlat tili bo‘ldi", "lotin yozuvi bekor qilindi", "Boshqa xalqlar tillarini rivojlantirish imkoniyati ham belgilandi.")
t.TF("Qayta qurish davrida KPSSning rahbarlik mavqeyiga putur yetgan.", True, "To‘g‘ri.")
t.TF("Kreml ittifoqdosh respublikalarning mustaqil davlat tuzishini qo‘llab-quvvatlagan.", False, "Noto‘g‘ri: Kreml bunga qattiq qarshi turgan.")
t.MUL([("O‘sha paytdagi O‘zbekiston rahbariyati Markazga yaqinlashish yo‘lini tanlagan.", True),
       ("Navro‘z bayrami va milliy an’analarga munosabatda «internatsionalizm»ga yotlik izlangan.", True),
       ("O‘sh qirg‘inida o‘zbek xalqi ig‘volarga uchib, qasos urushini boshlagan.", False)],
      "III noto‘g‘ri: o‘zbek xalqi sabr-toqat va bag‘rikenglik ko‘rsatib, ig‘volarga uchmagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["KPSS MK Aprel plenumi", "Qayta qurishning ikkinchi bosqichi boshlandi", "Qo‘qonda namoyish o‘qqa tutildi", "O‘zbek tiliga davlat tili maqomi berildi", "O‘sh va O‘zgandagi etnik mojaro"],
      "1985-yil aprel → 1987 → 1989-yil iyun → 1989-yil oktyabr → 1990-yil iyun.")
t.MAPMATCH('fargona', ['Quvasoy', 'Qo‘qon', 'O‘sh'],
           ["1989-yil may–iyunda yoshlar o‘rtasidagi bezorilik millatlararo to‘qnashuvga sabab bo‘lgan shahar", "1989-yil 7–8-iyunda tinch namoyish o‘qqa tutilgan shahar", "1990-yil iyunda qirg‘izlar va o‘zbeklar o‘rtasida etnik mojaro bo‘lgan shahar"],
           "1 – Quvasoy; 2 – Qo‘qon; 3 – O‘sh.")
t.VENN("Qayta qurishning I bosqichi", "Qayta qurishning II bosqichi",
       [("1985–1986-yillar", 1), ("ma’muriy tadbirlar an’anaviy usullarda olib borilgan", 1),
        ("1987–1989-yillar", 2), ("jamiyatni kompleks isloh qilish kun tartibiga qo‘yilgan", 2),
        ("M. Gorbachyov rahbarligida o‘tkazilgan", 3)],
       "I — 1985–1986, an’anaviy usullar; II — 1987–1989, kompleks islohot.")

# 28 Mustaqillik ostonasida
t = Topic('e10u28', 10028); TOPICS['e10u28'] = t
t.B("Islom Karimov O‘zbekiston Kompartiyasi MK birinchi sekretari etib qachon saylangan?", "1989-yil 23-iyunda", "1990-yil 24-martda", "1991-yil 29-dekabrda", "1988-yil noyabrda", "1989-yil 23-iyunda.")
t.B("1990-yil mart – oktyabrda O‘zSSR Ministrlar Sovetiga kim raislik qilgan?", "Shukurulla Mirsaidov", "Mirahmad Mirqosimov", "Rafiq Nishonov", "Abdurahim Po‘latov", "Shukurulla Mirsaidov.")
t.B("«Birlik» xalq harakati qachon tashkil topgan?", "1988-yil noyabrda", "1990-yil 30-aprelda", "1989-yil 23-iyunda", "1991-yil avgustda", "1988-yil noyabrda.")
t.B("«Birlik» xalq harakatining rahbari kim edi?", "professor Abdurahim Po‘latov", "Muhammad Solih", "Islom Karimov", "Shukurulla Mirsaidov", "Professor Abdurahim Po‘latov.")
t.B("«Birlik» huzurida faoliyat ko‘rsatgan ayollar harakati qanday nomlangan?", "«To‘maris»", "«Erk»", "«Hujum»", "«Qo‘shchi»", "«To‘maris».")
t.B("«Erk» demokratik partiyasining ta’sis qurultoyi qachon bo‘lgan?", "1990-yil 30-aprelda", "1988-yil noyabrda", "1991-yil 31-avgustda", "1990-yil 20-iyunda", "1990-yil 30-aprelda.")
t.B("«Erk» partiyasi kimning boshchiligida tuzilgan?", "Muhammad Solih", "Abdurahim Po‘latov", "Mirahmad Mirqosimov", "Rafiq Nishonov", "Shoir Muhammad Solih (Saloy Madaminov).")
t.B("«Birlik» va «Erk» qachondan O‘zbekiston hududida siyosiy faoliyatini to‘xtatgan?", "1992-yildan", "1990-yildan", "1991-yildan", "1995-yildan", "1992-yildan.")
t.B("O‘zbekistonda prezidentlik boshqaruvi qachon ta’sis etilgan?", "1990-yil 24-martda", "1991-yil 29-dekabrda", "1990-yil 20-iyunda", "1990-yil 1-noyabrda", "1990-yil 24-martda.")
t.B("SSSR Prezidenti lavozimi qachon ta’sis etilgan?", "1990-yil 12–15-martda", "1990-yil 24-martda", "1991-yil 17-martda", "1985-yil 11-martda", "SSSR Xalq deputatlarining III syezdida, 1990-yil 12–15-mart.")
t.B("O‘zbekiston Mustaqillik Deklaratsiyasi qachon qabul qilingan?", "1990-yil 20-iyunda", "1991-yil 31-avgustda", "1990-yil 24-martda", "1990-yil 14-dekabrda", "1990-yil 20-iyunda.")
t.B("Qoraqalpog‘iston ASSR suvereniteti to‘g‘risidagi Deklaratsiya qachon qabul qilingan?", "1990-yil 14-dekabrda", "1990-yil 20-iyunda", "1991-yil 31-avgustda", "1990-yil 12-iyunda", "1990-yil 14-dekabrda.")
t.B("SSSRda birinchi marta umumxalq referendumi qachon o‘tkazilgan?", "1991-yil 17-martda", "1991-yil 23-aprelda", "1990-yil 12-iyunda", "1991-yil 19-avgustda", "1991-yil 17-martda.")
t.B("«9+1» qo‘shma bayonoti qayerda qabul qilingan?", "Novo-Ogaryovoda", "Minskda", "Toshkentda", "Olmaotada", "1991-yil 23-aprelda Moskva yaqinidagi Novo-Ogaryovoda.")
t.B("GKChPga kim boshchilik qilgan?", "vitse-prezident Gennadiy Yanayev", "Boris Yelsin", "Mixail Gorbachyov", "Y.K. Ligachev", "Gennadiy Yanayev.")
t.B("GKChP isyonini kim rahbarligidagi kuchlar bostirgan?", "Boris Yelsin", "Gennadiy Yanayev", "Andrey Gromiko", "Islom Karimov", "RSFSR prezidenti Boris Yelsin.")
t.B("«O‘zbekiston Respublikasining Davlat Mustaqilligi asoslari to‘g‘risida»gi Qonun qachon qabul qilingan?", "1991-yil 31-avgustda", "1990-yil 20-iyunda", "1991-yil 29-dekabrda", "1991-yil 25-dekabrda", "1991-yil 31-avgustda.")
t.B("Mustaqillik asoslari to‘g‘risidagi qonun necha moddadan iborat?", "17 moddadan", "15 moddadan", "9 moddadan", "25 moddadan", "17 moddadan.")
t.B("SSSR xalqaro huquq subyekti sifatida qachon barham topgan?", "1991-yil 25-dekabrda", "1991-yil 29-avgustda", "1991-yil 31-avgustda", "1992-yil 4-yanvarda", "1991-yil 25-dekabrda.")
t.NAT("1990-yil 1-noyabrda prezidentlik hokimiyati bilan Ministrlar Sovetining ijroiya hokimiyati qo‘shildi.", "Ministrlar Soveti Prezident huzuridagi Vazirlar Mahkamasiga aylantirildi", "Ministrlar Soveti kuchaydi", "Prezident lavozimi tugatildi", "vitse-prezident lavozimi ta’sis etildi", "Islom Karimov Vazirlar Mahkamasining raisi ham bo‘ldi.")
t.TF("Ittifoqdosh respublikalar o‘rtasida birinchi bo‘lib O‘zbekistonda prezidentlik boshqaruvi joriy qilingan.", True, "To‘g‘ri.")
t.TF("Yangi Ittifoq shartnomasi 1991-yil 20-avgustda imzolangan.", False, "Noto‘g‘ri: 20-avgustda imzolanishi kerak edi, ammo GKChP voqealari tufayli imzolanmadi.")
t.MUL([("1991-yil 29-dekabrda Islom Karimov 5 yil muddatga Prezident etib saylangan.", True),
       ("1992-yil 4-yanvarda vitse-prezident lavozimi tugatilib, Bosh vazir lavozimi ta’sis etilgan.", True),
       ("KPSS 1991-yil 25-dekabrda o‘z faoliyatini to‘xtatgan.", False)],
      "III noto‘g‘ri: KPSS 1991-yil 29-avgustda faoliyatini to‘xtatgan.")
t.MATCH("Prezidentlik boshqaruvi bosqichlarini davrlari bilan moslashtiring.", ["Birinchi bosqich", "Ikkinchi bosqich", "Uchinchi bosqich"],
        ["1990-yil mart – oktyabr", "1990-yil noyabr – 1991-yil avgust", "1991-yil sentyabr – 1992-yil yanvar", "1989-yil iyun – 1990-yil mart"], 'abc',
        "I – 1990-yil mart–oktyabr; II – 1990-yil noyabr–1991-yil avgust; III – 1991-yil sentyabr–1992-yil yanvar.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["«Birlik» tashkil topdi", "I. Karimov birinchi sekretar etib saylandi", "O‘zSSR Prezidenti lavozimi ta’sis etildi", "Mustaqillik Deklaratsiyasi", "«9+1» bayonoti", "Davlat Mustaqilligi asoslari to‘g‘risidagi Qonun"],
      "1988-yil noyabr → 1989-yil iyun → 1990-yil mart → 1990-yil iyun → 1991-yil aprel → 1991-yil 31-avgust.")
t.VENN("«Birlik» xalq harakati", "«Erk» demokratik partiyasi",
       [("1988-yil noyabrda tashkil topgan", 1), ("rahbari Abdurahim Po‘latov", 1),
        ("1990-yil 30-aprelda ta’sis qurultoyi bo‘lgan", 2), ("rahbari Muhammad Solih", 2),
        ("1992-yildan O‘zbekistonda faoliyatini to‘xtatgan", 3)],
       "«Birlik» — 1988, Po‘latov; «Erk» — 1990, Muhammad Solih.")
