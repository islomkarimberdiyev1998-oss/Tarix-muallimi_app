from qlib import Topic
TOPICS = {}

# 25 Ekologik vaziyat va Orol fojiasi
t = Topic('e10u25', 10025); TOPICS['e10u25'] = t
t.B("Ekologik muammo qaysi yillarda bashariyat uchun katta xavf tug‘dirgan?", "XX asr 60–80-yillarida", "XX asr 20–30-yillarida", "XIX asr oxirida", "XXI asr boshida", "XX asr 60–80-yillarida.")
t.B("Olimlar ekologik muvozanat buzilishi xavfini nimaga qiyoslagan?", "yadro urushi xavfiga", "zilzilaga", "ocharchilikka", "epidemiyaga", "Yadro urushi xavfidan qolishmaydi, degan.")
t.B("O‘zbekistondagi yirik og‘ir sanoat tarmoqlari kimning qaramog‘ida bo‘lgan?", "Ittifoq vazirliklari va mahkamalari", "respublika hukumati", "viloyat kengashlari", "xususiy kompaniyalar", "Ittifoq vazirliklari va mahkamalari.")
t.B("Kimyo zavodlari asosan qaysi shaharlarda qurilgan?", "Navoiy, Chirchiq, Farg‘ona", "Xiva, Buxoro, Samarqand", "Nukus, Termiz, Qarshi", "Jizzax, Guliston, Bekobod", "Aholisi ko‘p Navoiy, Chirchiq, Farg‘onada.")
t.B("80-yillar o‘rtalarida qishloq xo‘jaligida qancha pestitsid qo‘llanilgan?", "90 000 tonna", "9000 tonna", "900 000 tonna", "30 mln tonna", "90 000 tonna.")
t.B("G‘o‘zani defoliatsiya qilish uchun 20 yil ishlatilgan o‘ta zaharli modda qaysi?", "butifos", "pestitsid DDT", "selitra", "superfosfat", "Butifos.")
t.B("O‘zbekiston rahbariyati butifosdan foydalanishni qachon taqiqlagan?", "1981-yili", "1986-yili", "1977-yili", "1991-yili", "1981-yili.")
t.B("Butifos ko‘p hollarda me’yordan necha baravar ko‘p ishlatilgan?", "2–3 baravar", "10 baravar", "1,5 baravar", "5–6 baravar", "2–3 baravar.")
t.B("Orol dengiziga suv qaysi daryolardan quyilgan?", "Amudaryo va Sirdaryo", "Zarafshon va Qashqadaryo", "Chirchiq va Ohangaron", "Volga va Ural", "Amudaryo va Sirdaryo.")
t.B("Orol dengizi hozir nechta bo‘lakka bo‘lingan?", "3 ta", "2 ta", "4 ta", "5 ta", "3 ta: shimoliy, sharqiy, g‘arbiy.")
t.B("Orol dengizining eng chuqur qismi qaysi?", "g‘arbiy qismi", "shimoliy qismi", "sharqiy qismi", "janubiy qismi", "G‘arbiy qismi.")
t.B("1980–1985-yillarda paxtachilik va chorvachilik har yili qancha zarar ko‘rgan?", "30 mln rubldan ortiq", "3 mln rubl", "300 mln rubl", "90 mln rubl", "30 mln rubldan ortiq.")
t.B("Bir yoshgacha bo‘lgan bolalar o‘limi 1986-yilda har ming bolaga nechtaga yetgan?", "72 nafarga", "46,5 nafarga", "30 nafarga", "60 nafarga", "1980-yildagi 46,5 dan 72 ga.")
t.B("Orolbo‘yida ayollarning necha foizi kamqonlikka chalingan?", "60 foizi", "30 foizi", "72 foizi", "90 foizi", "60 foizi.")
t.B("Orolbo‘yida qorin tifi kasalligi necha marta ortgan?", "30 marta", "7 marta", "3 marta", "60 marta", "30 marta; yuqumli sariq 7 marta.")
t.B("Dunyodagi eng yosh cho‘l qaysi?", "Orolqum", "Qizilqum", "Qoraqum", "Mirzacho‘l", "Orolqum.")
t.B("Orol dengizining qancha qismi quruqlikka aylangan?", "40 000 km² dan ziyod", "4000 km²", "400 km²", "100 000 km²", "40 000 km² dan ziyod.")
t.NAT("60-yillardan sug‘oriladigan ekin maydonlari kengaytirildi.", "Orolga quyiladigan suv kamayib, dengiz quriy boshladi", "Orol sathi ko‘tarildi", "baliqchilik rivojlandi", "dengiz chuchuklashdi", "Suv sathi jadal pasaydi, sho‘rlanish kuchaydi.")
t.NAT("Amudaryoning quyi oqimida baliqchilik va mo‘ynachilik xo‘jaliklari yo‘q bo‘lib ketdi.", "mo‘ynoqliklarning ko‘pchiligi 10–15 yilda ishsiz va nochor ahvolga tushdi", "mo‘ynoqliklar boyib ketdi", "baliq eksporti oshdi", "aholi soni keskin ko‘paydi", "Ko‘pchilik ishsiz qoldi.")
t.TF("Sovet hokimiyati mamlakatda ekologiya muammosi yo‘q, deb chora ko‘rmagan.", True, "To‘g‘ri.")
t.TF("Butifos 1981-yildan keyin hech bir xo‘jalikda qo‘llanilmagan.", False, "Noto‘g‘ri: ayrim xo‘jaliklar keyinchalik ham foydalangan.")
t.MUL([("Zaharli moddalar bilan ishlov berish maydonlarning yarmida samolyotlarda bajarilgan.", True),
       ("Orolbo‘yi mintaqasi O‘zbekiston va Qozog‘iston hududlaridan iborat.", True),
       ("Orolqum XIX asr oxirida vujudga kelgan.", False)],
      "III noto‘g‘ri: Orolqum XX asr oxirida vujudga kelgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Sug‘oriladigan maydonlar kengayib, Orolga suv kamaya boshladi", "Bolalar o‘limi har ming bolaga 46,5 nafar", "Butifos taqiqlandi", "Bolalar o‘limi har ming bolaga 72 nafar"],
      "60-yillar → 1980 → 1981 → 1986.")
t.MAPN('xorazm', ['Mo‘ynoq', 'Qo‘ng‘irot', 'Chimboy', 'Xiva'],
       "Baliqchilik bilan nom chiqargan, aholisi 10–15 yilda ishsiz qolgan Orol bo‘yidagi shahar qaysi raqam bilan belgilangan?",
       "Mo‘ynoq.", 0)
t.VENN("Orolbo‘yi ekologik fojiasi", "Sanoat shaharlari ekologiyasi",
       [("Orolqum cho‘li vujudga kelgan", 1), ("qorin tifi 30 marta ortgan", 1),
        ("kimyo zavodlari zaharli gazlar chiqargan", 2), ("Chirchiq, Navoiy, Olmaliqda vaziyat yomon", 2),
        ("Markaz aholi salomatligini emas, daromadni o‘ylagan", 3)],
       "Orol — Orolqum, kasalliklar; sanoat — kimyo zavodlari, shaharlar.")

# 26 Paxta ishi
t = Topic('e10u26', 10026); TOPICS['e10u26'] = t
t.B("Leonid Brejnev qachon vafot etgan?", "1982-yil noyabrda", "1983-yil oktyabrda", "1985-yil martda", "1984-yilda", "1982-yil noyabrda.")
t.B("Brejnev mamlakat va partiyani necha yil boshqargan?", "18 yil", "25 yil", "10 yil", "30 yil", "18 yil.")
t.B("1982–1984-yillarda Sovet Ittifoqiga kim rahbarlik qilgan?", "Yuriy Andropov", "Konstantin Chernenko", "Mixail Gorbachyov", "Andrey Gromiko", "Yuriy Andropov.")
t.B("1984–1985-yillarda Sovet Ittifoqiga kim rahbarlik qilgan?", "Konstantin Chernenko", "Yuriy Andropov", "Mixail Gorbachyov", "Leonid Brejnev", "Konstantin Chernenko.")
t.B("Mixail Gorbachyov KPSS MK Bosh sekretari etib qachon saylangan?", "1985-yil 11-martda", "1985-yil 2-iyulda", "1984-yil 23-iyunda", "1982-yil noyabrda", "1985-yil 11-martda.")
t.B("1985-yil 2-iyulda SSSR Oliy Soveti Prezidiumi raisi etib kim saylangan?", "Andrey Gromiko", "Mixail Gorbachyov", "Y.K. Ligachev", "Rafiq Nishonov", "Andrey Gromiko.")
t.B("Sharof Rashidov qachon vafot etgan?", "1983-yil oktyabrda", "1982-yil noyabrda", "1984-yil iyunda", "1985-yil martda", "1983-yil oktyabrda.")
t.B("1983–1988-yillarda O‘zbekistonga kim rahbarlik qilgan?", "Inomjon Usmonxo‘jayev", "Rafiq Nishonov", "Sharof Rashidov", "Normuhammadi Xudoyberdiyev", "Inomjon Usmonxo‘jayev.")
t.B("1988–1989-yillarda O‘zbekistonga kim rahbarlik qilgan?", "Rafiq Nishonov", "Inomjon Usmonxo‘jayev", "Islom Karimov", "Nazar Matchonov", "Rafiq Nishonov.")
t.B("O‘zbekiston Kompartiyasi MKning XVI plenumi qachon bo‘lgan?", "1984-yil 23-iyunda", "1983-yil aprelda", "1985-yil 11-martda", "1986-yilda", "1984-yil 23-iyunda.")
t.B("XVI plenumda Moskvadan yuborilgan qaysi KPSS MK sekretari qatnashgan?", "Y.K. Ligachev", "M. Suslov", "A. Gromiko", "Y. Andropov", "Y.K. Ligachev.")
t.B("T.X. Gdlyan va N.V. Ivanov rahbarligidagi tergov guruhi qachon tuzilgan?", "1983-yil aprelda", "1984-yil 23-iyunda", "1985-yilda", "1982-yil noyabrda", "1983-yil aprelda.")
t.B("1983–1987-yillarda O‘zbekistonga qancha «desantchi» yuborilgan?", "1000 nafarga yaqin", "3000 nafardan ortiq", "40 000 nafar", "5000 nafar", "1000 nafarga yaqin.")
t.B("«Desantchilar»ga qancha tergovchi yordam bergan?", "3000 nafardan ortiq", "1000 nafar", "500 nafar", "40 000 nafar", "3000 nafardan ortiq tergovchi.")
t.B("1985–1990-yillarda «paxta ishi» bo‘yicha jami qancha kishi tergov qilingan?", "40 000 kishi", "5000 kishi", "1000 kishi", "4000 kishi", "40 000 kishi.")
t.B("«Paxta ishi» bo‘yicha qancha kishi jinoiy javobgarlikka tortilgan?", "5000 nafar", "40 000 nafar", "3000 nafar", "500 nafar", "5000 nafar.")
t.B("Sharof Rashidov xotirasini badnom qilish uchun o‘ylab topilgan ibora qaysi?", "«Sharof Rashidovchilik»", "«qosimovchilik»", "«inog‘omovchilik»", "«badriddinovchilik»", "«Sharof Rashidovchilik».")
t.NAT("Markaziy matbuotda o‘zbek xalqi badnom etilib, paxta ishiga siyosiy tus berildi.", "«paxta ishi» «o‘zbeklar ishi»ga aylantirildi", "paxta ishi to‘xtatildi", "o‘zbek rahbarlari mukofotlandi", "tergovchilar jazolandi", "«O‘zbeklar ishi»ga aylantirildi.")
t.TF("Qo‘shib yozish va korrupsiya SSSRning deyarli barcha hududlarida bo‘lsa ham «tajriba maydoni» sifatida O‘zbekiston tanlangan.", True, "To‘g‘ri.")
t.TF("1985-yildan mamlakatda qayta qurish siyosati boshlangan.", True, "To‘g‘ri.")
t.MUL([("Tergov jarayonida tutqunlarga jismoniy va ruhiy tazyiq o‘tkazilgan.", True),
       ("Tergov qilinganlarning aksariyati prokuror sanksiyasisiz izolyatorlarda o‘tirgan.", True),
       ("«Paxta ishi» qatag‘oni O‘zbekiston rahbarlariga daxl qilmagan.", False)],
      "III noto‘g‘ri: qatag‘on sobiq va birinchi rahbarlarni ham chetlab o‘tmagan.")
t.MATCH("Shaxslarni ular bilan bog‘liq ma’lumotlar bilan moslashtiring.", ["Mixail Gorbachyov", "Y.K. Ligachev", "T.X. Gdlyan", "Rafiq Nishonov"],
        ["1985-yilda KPSS MK Bosh sekretari", "XVI plenumda qatnashgan KPSS MK sekretari", "maxsus tergov guruhi rahbari", "1988–1989-yillarda O‘zbekiston rahbari", "SSSR Oliy Soveti Prezidiumi raisi (1985)"], 'abcd',
        "Gorbachyov – Bosh sekretar; Ligachev – XVI plenum; Gdlyan – tergov guruhi; Nishonov – O‘zbekiston rahbari.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Brejnev vafot etdi", "Gdlyan–Ivanov tergov guruhi tuzildi", "Sharof Rashidov vafot etdi", "XVI plenum", "Gorbachyov Bosh sekretar bo‘ldi", "R. Nishonov O‘zbekiston rahbari bo‘ldi"],
      "1982-yil noyabr → 1983-yil aprel → 1983-yil oktyabr → 1984-yil iyun → 1985-yil mart → 1988.")
t.VENN("Inomjon Usmonxo‘jayev", "Rafiq Nishonov",
       [("1983–1988-yillarda O‘zbekiston rahbari", 1), ("1978–1983-yillarda Oliy Sovet Prezidiumi raisi", 1),
        ("1988–1989-yillarda O‘zbekiston rahbari", 2), ("Usmonxo‘jayevdan keyin rahbar bo‘lgan", 2),
        ("«paxta ishi» davrida O‘zbekiston rahbari bo‘lgan", 3)],
       "Usmonxo‘jayev — 1983–1988; Nishonov — 1988–1989.")
