from qlib import Topic, PLACES, REG
TOPICS = {}

# 30-mavzu. 1980–1990-yillarda O‘zbekiston
t = Topic('y10u30', 10030); TOPICS['y10u30'] = t
t.B("Muammolarda «aybdorlar»ni topishga bel bog‘lagan sovet rahbari kim?", "Yuriy Andropov", "M. Gorbachyov", "L. Brejnev", "N. Xrushchyov", "Yuriy Andropov.")
t.B("Afg‘oniston urushida nechta o‘zbekistonlik halok bo‘lgan?", "1 515 nafar", "14 500 nafar", "100 000 nafar", "515 nafar", "1 515 nafar.")
t.B("Afg‘oniston urushida jami nechtadan ortiq sovet harbiysi halok bo‘lgan?", "14 500 dan", "1 515 dan", "100 000 dan", "50 000 dan", "14 500 dan ortiq.")
t.B("Maxsus tergov guruhlaridan biriga kimlar rahbarlik qilgan?", "T. Gdlyan va N. Ivanov", "Andropov va Gorbachyov", "Rashidov va Usmonxo‘jayev", "Kobozev va Tobolin", "T. Gdlyan va N. Ivanov.")
t.B("Gdlyan–Ivanov guruhi qachon tuzilgan?", "1983-yil aprelda", "1984-yil 23-iyunda", "1985-yil aprelda", "1989-yil iyunda", "1983-yil aprel.")
t.B("«Paxta ishi» qatag‘onlari qaysi plenum qarorlari bilan boshlangan?", "1984-yil 23-iyundagi XVI plenum", "1985-yil aprel plenumi", "1952-yil X plenum", "1986-yil XXVII syezd", "O‘zKP MK XVI plenumi, 1984-yil 23-iyun.")
t.B("1985–1990-yillarda «paxta ishi» bo‘yicha jami necha kishi tergov qilingan?", "40 000", "5 000", "1 515", "100 000", "40 000 kishi.")
t.B("«Paxta ishi» bo‘yicha necha kishi soxta ayblar bilan jinoiy javobgarlikka tortilgan?", "5 000", "40 000", "500", "50 000", "5 000 nafar.")
t.B("Sharof Rashidov qachon vafot etgan?", "1983-yil 31-oktyabrda", "1984-yil 23-iyunda", "1985-yilda", "1989-yilda", "1983-yil 31-oktyabr.")
t.B("1987-yilda nechta maktabda o‘qish ikki smenada bo‘lgan?", "5 596 ta (72,1%)", "30 ta", "150 ming", "560 ta", "5 596 ta.")
t.B("Respublikada jami nechta o‘quvchi uch smenada o‘qishga majbur bo‘lgan?", "150 ming", "5 596", "15 ming", "1,5 million", "150 ming.")
t.B("O‘zbek maktablarida rus tili va adabiyotiga necha soat ajratilgan?", "3 390 soat", "560 soat", "1 000 soat", "300 soat", "3 390 soat (rus maktablarida o‘zbek tiliga 560).")
t.B("Ateistik tarbiya haqidagi qaror qaysi syezdda qabul qilingan?", "1986-yil KPSS XXVII syezdi", "1977-yilgi syezd", "1952-yil X plenum", "1985-yil aprel plenumi", "KPSS XXVII syezdi, 1986.")
t.B("Qaysi qadimiy bayram diniy bayram sifatida taqiqlangan?", "Navro‘z", "Ramazon hayiti", "Mustaqillik kuni", "G‘alaba bayrami", "Navro‘z.")
t.B("Qayta qurish yo‘li qaysi plenumda e’lon qilingan?", "KPSS MK 1985-yil aprel plenumi", "1984-yil XVI plenum", "1986-yil XXVII syezd", "1989-yil iyun plenumi", "1985-yil aprel plenumi.")
t.B("Qayta qurishning birinchi bosqichi qaysi yillar?", "1985–1986", "1987–1989", "1982–1985", "1989–1991", "1985–1986.")
t.B("1989-yil may–iyunda millatlararo to‘qnashuv qayerda boshlangan?", "Quvasoyda", "Qo‘qonda", "Toshkentda", "Andijonda", "Quvasoyda.")
t.B("1989-yil 7–8-iyunda qaysi shaharda tinch namoyish o‘qqa tutilgan?", "Qo‘qonda", "Quvasoyda", "Toshkentda", "Farg‘onada", "Qo‘qonda, 50 dan ziyod kishi halok.")
t.B("Rasmiy ma’lumotlarga ko‘ra Farg‘ona viloyatidagi voqealarda necha kishi halok bo‘lgan?", "103 nafar", "50 nafar", "1 011 nafar", "757 nafar", "103 nafar.")
t.NAT("Markaz O‘zbekistonni «paxta ishi» uchun «tajriba maydoni» qilib tanladi.", "minglab kishilar nohaq jazolandi, paxta ishi «o‘zbeklar ishi»ga aylantirilmoqchi bo‘ldi", "korrupsiya butunlay yo‘qoldi", "O‘zbekiston mustaqillikka erishdi", "tergovchilar jazolandi", "Nohaq qatag‘on.")
t.NAT("1970–1980-yillarda ta’lim uchun byudjet mablag‘i 11 foizdan 8 foizga qisqardi.", "o‘quv binolari yetishmay, maktablar ikki-uch smenada ishladi", "yangi maktablar ko‘p qurildi", "o‘quvchilar kamaydi", "ta’lim bepul bo‘lmay qoldi", "Smenalar ko‘paydi.")
t.NAT("Sotsializm doirasidagi yakkapartiyaviy rahbarlik demokratiya bilan kelisha olmadi.", "qayta qurish safsatabozlikka aylanib, mag‘lubiyatga uchradi", "qayta qurish to‘liq g‘alaba qozondi", "SSSR mustahkamlandi", "demokratiya o‘rnatildi", "Qayta qurish muvaffaqiyatsiz.")
t.NAT("Quvasoydagi bezorilik millatlararo to‘qnashuvga aylandi.", "u Farg‘ona vodiysi va Toshkent viloyatiga tarqalib, xavfli tus oldi", "to‘qnashuv bir kunda tugadi", "voqea e’tiborsiz qoldi", "faqat Quvasoyda qoldi", "To‘qnashuv tarqaldi.")
t.TF("Afg‘onistondagi harbiylarni ta’minlashga o‘n yilda 100 mlrd rubldan ortiq sarflangan.", True, "To‘g‘ri.")
t.TF("«Paxta ishi» bo‘yicha hibsga olishlar faqat prokuror sanksiyasi bilan amalga oshirilgan.", False, "Noto‘g‘ri: aksariyati sanksiyasiz hibsga olingan.")
t.TF4([("Arab imlosidagi barcha kitoblar «reaksion» deb e’lon qilingan.", True), ("Janozaga borgan partiya a’zolari ta’qib qilingan.", True),
       ("1989-yilda Toshkentda 30 ta maktab uch smenada ishlagan.", True), ("Rashidov «paxta ishi»ni boshlagan.", False)],
      "4-noto‘g‘ri: Rashidov tazyiqni susaytirishga uringan, 1983-yilda vafot etgan; ish Markaz tomonidan boshlangan.")
t.MUL([("Qayta qurishning ikkinchi bosqichi 1987–1989-yillarni o‘z ichiga oladi.", True),
       ("Farg‘ona voqealarida 757 xonadonga o‘t qo‘yilgan.", True),
       ("Qayta qurish davrida KPSSning yetakchi mavqei kuchaygan.", False)],
      "III noto‘g‘ri: KPSS mavqeiga putur yetgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Gdlyan–Ivanov guruhi tuzildi", "Rashidov vafot etdi", "XVI plenum – «paxta ishi»", "aprel plenumi – qayta qurish", "XXVII syezd – ateistik tarbiya", "Qo‘qonda namoyish o‘qqa tutildi"],
      "1983-04 → 1983-10-31 → 1984-06-23 → 1985-04 → 1986 → 1989-06.")
t.MATCH("Raqamlarni ma’noga moslashtiring.", ["40 000", "5 000", "1 515", "103"],
        ["«paxta ishi» bo‘yicha tergov qilinganlar", "soxta ayblar bilan javobgarlikka tortilganlar", "Afg‘onistonda halok bo‘lgan o‘zbekistonliklar", "1989-yil iyundagi Farg‘ona voqealari qurbonlari", "uch smenada o‘qigan o‘quvchilar"], 'abcd',
        "40 000 – tergov; 5 000 – javobgarlik; 1 515 – Afg‘oniston; 103 – Farg‘ona.")
t.VENN("«Paxta ishi»", "Farg‘ona fojialari",
       [("Gdlyan–Ivanov guruhi", 1), ("40 000 kishi tergov qilindi", 1),
        ("Quvasoydan boshlangan to‘qnashuv", 2), ("103 kishi halok bo‘ldi", 2),
        ("1980-yillar O‘zbekistonidagi fojiali voqea", 3)],
       "Paxta ishi – Gdlyan, 40 000; Farg‘ona – Quvasoy, 103; ikkalasi 80-yillar fojiasi.")
t.MAPMATCH('uzb', ['Quvasoy', 'Qo‘qon', 'Toshkent'],
           ["1989-yil may–iyunda millatlararo to‘qnashuv boshlangan joy", "1989-yil 7–8-iyunda tinch namoyish o‘qqa tutilgan shahar", "1989-yilda 30 ta maktab uch smenada ishlagan poytaxt"],
           "1 – Quvasoy; 2 – Qo‘qon; 3 – Toshkent.")

# 31-mavzu. Sharof Rashidov
t = Topic('y10u31', 10031); TOPICS['y10u31'] = t
t.B("1941-yil noyabrda Sharof Rashidov qaysi harbiy bilim yurtini tugatgan?", "Frunze piyodalar harbiy bilim yurtini", "Toshkent piyodalar bilim yurtini", "Moskva harbiy akademiyasini", "Samarqand harbiy maktabini", "Frunze (hozirgi Bishkek) piyodalar harbiy bilim yurti.")
t.B("Frunze shahrining hozirgi nomi nima?", "Bishkek", "Almati", "Dushanbe", "O‘sh", "Bishkek.")
t.B("Rashidov urushda qanday harbiy unvon bilan frontga jo‘natilgan?", "kichik politruk", "general-mayor", "polkovnik", "serjant", "Kichik politruk.")
t.B("Rashidov qaysi frontga jo‘natilgan?", "Kalinin frontiga", "Stalingrad frontiga", "Uzoq Sharq frontiga", "Kavkaz frontiga", "Kalinin frontiga.")
t.B("Politruk kim?", "shaxsiy tarkibning siyosiy tayyorgarligi bilan shug‘ullanuvchi komandir", "tank haydovchisi", "harbiy shifokor", "uchuvchi", "Siyosiy tayyorgarlik komandiri.")
t.B("Toshkent zilzilasi qachon bo‘lgan?", "1966-yil 26-aprelda", "1977-yil noyabrda", "1983-yil 31-oktyabrda", "1959-yil 15-martda", "1966-yil 26-aprel, tonggi 5:23.")
t.B("Zilzila Rixter shkalasi bo‘yicha necha ball kuchda bo‘lgan?", "8–9 ball", "5–6 ball", "10–12 ball", "3–4 ball", "8–9 ball.")
t.B("Yerning qattiq qimirlashi necha sekund davom etgan?", "10–12 sekund", "1–2 sekund", "60 sekund", "5 daqiqa", "10–12 sekund.")
t.B("Zilzilada necha kishi halok bo‘lgan?", "8 kishi", "800 kishi", "300 ming kishi", "78 kishi", "8 kishi.")
t.B("Zilzila natijasida necha kishi boshpanasiz qolgan?", "300 ming kishi (78 ming oila)", "8 ming kishi", "3 million kishi", "30 ming kishi", "78 ming oila – 300 ming kishi.")
t.B("Zilzilaning ertasi kuni Toshkentga kim yetib kelgan?", "L. Brejnev va A. Kosigin", "M. Gorbachyov", "Y. Andropov", "N. Xrushchyov", "Brejnev va Kosigin.")
t.B("Zilziladan so‘ng butun yil davomida necha ballgacha silkinishlar takrorlangan?", "7 ballgacha", "3 ballgacha", "9 ballgacha", "12 ballgacha", "7 ballgacha.")
t.B("Zilzilada nechta o‘quv yurti binosi buzilgan?", "181 ta", "236 ta", "245 ta", "36 ta", "181 ta.")
t.B("Zilzila nechta kvadrat kilometr maydondagi binolarni vayron qilgan?", "10 km²", "100 km²", "1 km²", "50 km²", "10 km².")
t.B("Ushbu ma’lumotlar qaysi kitobdan olingan?", "Sh. Ergashevning «Erk istar ko‘ngil»", "«Boburnoma»", "«Qirq birinchi yil olmasi»", "«Navoiy»", "«Erk istar ko‘ngil».")
t.NAT("Yer qimirlashi gorizontal emas, vertikal holda yuz berdi.", "vayronagarchilik va qurbonlar nisbatan kam bo‘ldi", "shahar butunlay yo‘q bo‘ldi", "minglab kishi halok bo‘ldi", "zilzila sezilmadi", "Qurbonlar kam bo‘lgan.")
t.NAT("1941-yilda urush boshlandi.", "Rashidovning hayotiy rejalari o‘zgarib, u frontga jo‘natildi", "Rashidov Moskvaga o‘qishga ketdi", "Rashidov yozuvchilikni boshladi", "Rashidov hukumat raisi bo‘ldi", "Frontga ketdi.")
t.NAT("Rashidov poytaxtdagi ahvol bo‘yicha axborot berdi.", "mutaxassislar ishtirokida Toshkentni qayta tiklash qarori qabul qilindi", "Toshkent tashlab ketildi", "poytaxt boshqa shaharga ko‘chirildi", "qurilish to‘xtatildi", "Qayta tiklash qarori.")
t.TF("Rashidov urush davridagi hayoti haqida ko‘p gapirishni yoqtirmagan.", True, "To‘g‘ri.")
t.TF("Toshkent zilzilasi kechqurun soat 23 da yuz bergan.", False, "Noto‘g‘ri: tongda soat 5 dan 23 daqiqa o‘tganda.")
t.TF4([("Zilzilada 2 mln m² dan ziyod turarjoy buzilgan.", True), ("245 ta sanoat korxonasi binosi buzilgan.", True),
       ("185 ta tibbiyot binosi buzilgan.", True), ("Zilziladan keyin silkinishlar bir hafta ichida to‘xtagan.", False)],
      "4-noto‘g‘ri: butun yil davomida 7 ballgacha silkinishlar takrorlangan.")
t.MUL([("Rashidov Frunze bilim yurtini tezlashtirilgan dastur asosida tugatgan.", True),
       ("Zilzilada 236 ta ma’muriy bino buzilgan.", True),
       ("Zilziladan keyin Toshkentni tiklash Moskvada rad etilgan.", False)],
      "III noto‘g‘ri: tiklash bo‘yicha qaror qabul qilingan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Rashidov tug‘ildi", "Frunze bilim yurtini tugatib frontga ketdi", "MK birinchi sekretari bo‘ldi", "Toshkent zilzilasi", "Rashidov vafot etdi"],
      "1917 → 1941 → 1959 → 1966 → 1983.")
t.MATCH("Zilzila oqibatlarini raqami bilan moslashtiring.", ["halok bo‘lganlar", "boshpanasiz oilalar", "buzilgan o‘quv yurtlari", "buzilgan ma’muriy binolar"],
        ["8 kishi", "78 ming oila", "181 ta", "236 ta", "700 ta"], 'abcd',
        "Halok – 8; oilalar – 78 ming; o‘quv yurtlari – 181; ma’muriy binolar – 236.")
t.VENN("Rashidov – harbiy", "Rashidov – davlat arbobi",
       [("Frunze bilim yurtini tugatgan", 1), ("Kalinin frontida kichik politruk", 1),
        ("zilziladan keyin Toshkentni tiklagan", 2), ("metro qurilishi tashabbuskori", 2),
        ("Sharof Rashidov hayot yo‘li", 3)],
       "Harbiy – Frunze, Kalinin fronti; arbob – Toshkentni tiklash, metro; ikkalasi Rashidov hayoti.")
t.MAPMATCH('ca', ['Pishpak', 'Jizzax', 'Toshkent'],
           ["Rashidov harbiy bilim yurtini tugatgan Frunze (Bishkek)", "Rashidov tug‘ilgan shahar", "1966-yil 26-aprelda zilzila bo‘lgan poytaxt"],
           "1 – Frunze (Bishkek); 2 – Jizzax; 3 – Toshkent.")

# 32-mavzu. Mustaqillik sari
t = Topic('y10u32', 10032); TOPICS['y10u32'] = t
t.B("Sovet maxsus xizmatlari qaysi joylarda millatlararo mojarolar chiqarishga urindi?", "Farg‘ona, Qo‘qon, Quvasoy, Guliston, Parkent, Bo‘ka", "Samarqand, Buxoro", "Xiva, Nukus", "Termiz, Qarshi", "Farg‘ona, Qo‘qon, Quvasoy, Guliston, Parkent, Bo‘ka.")
t.B("Islom Karimov O‘zbekiston SSR rahbarligiga qachon kelgan?", "1989-yil 23-iyunda", "1991-yil 31-avgustda", "1990-yil martda", "1991-yil 19-avgustda", "1989-yil 23-iyun.")
t.B("Moskvadagi davlat to‘ntarishiga urinish qachon bo‘lgan?", "1991-yil 19-avgustda", "1991-yil 31-avgustda", "1991-yil 25-avgustda", "1989-yil 23-iyunda", "1991-yil 19-avgust.")
t.B("Avgust to‘ntarishi necha kun davom etib muvaffaqiyatsizlikka uchradi?", "uch kundan oshmay", "bir oy", "bir yil", "bir hafta", "Uch kundan oshmay.")
t.B("Prezidentning qaysi kungi farmoni bilan ichki ishlar va DXQ respublika tasarrufiga olindi?", "25-avgust", "31-avgust", "19-avgust", "1-sentyabr", "1991-yil 25-avgust.")
t.B("O‘zbekiston mustaqilligi qachon e’lon qilingan?", "1991-yil 31-avgustda", "1991-yil 1-sentyabrda", "1991-yil 19-avgustda", "1990-yil 20-iyunda", "1991-yil 31-avgust.")
t.B("Mustaqillik qaysi sessiyada e’lon qilingan?", "Oliy Sovet o‘n ikkinchi chaqiriq navbatdan tashqari 6-sessiyasi", "Oliy Sovet III sessiyasi", "KPSS XXVII syezdi", "Butuno‘zbek qurultoyi", "12-chaqiriq, navbatdan tashqari 6-sessiya.")
t.B("31-avgustda qabul qilingan qonun qanday nomlanadi?", "«O‘zbekiston Respublikasining Davlat mustaqilligi asoslari to‘g‘risida»", "«Davlat tili to‘g‘risida»", "«Ta’lim to‘g‘risida»", "«Konstitutsiya»", "Davlat mustaqilligi asoslari to‘g‘risidagi Qonun.")
t.B("O‘zbek xalqi va davlatchiligi kamida necha yillik o‘tmishga ega?", "3 500 yillik", "500 yillik", "1 000 yillik", "100 yillik", "Kamida 3 500 yillik.")
t.B("Mustaqillik xalqimizning qaysi asrdagi eng yuksak yutug‘i deb baholanadi?", "XX asr", "XIX asr", "XXI asr", "XVIII asr", "XX asr.")
t.B("SSSR Ichki ishlar vazirligining ichki qo‘shinlari kimga bo‘ysundirildi?", "O‘zbekiston SSR Prezidentiga", "SSSR Prezidentiga", "Mudofaa vaziriga", "Oliy Sovetga", "O‘zbekiston SSR Prezidentiga.")
t.NAT("Sovet rahbariyati millatlararo mojarolar chiqarishga urindi.", "maqsad odamlar diqqatini chalg‘itib, milliy-ozodlik harakatini so‘ndirish edi", "maqsad tinchlikni mustahkamlash edi", "mojarolar mustaqillikni tezlashtirdi", "xalqlar do‘stlashdi", "Milliy harakatni so‘ndirish.")
t.NAT("1989-yil 23-iyunda Islom Karimov respublika rahbarligiga keldi.", "mustaqillikni tiklash jarayoniga ilg‘or boshqaruvchilarni uyushtirish imkoni tug‘ildi", "SSSR mustahkamlandi", "mustaqillik kechiktirildi", "partiya kuchaydi", "Mustaqillik sari jipslashuv.")
t.NAT("1991-yil 19-avgustdagi to‘ntarish muvaffaqiyatsizlikka uchradi.", "O‘zbekistonda mustaqillik sari intilishlar yanada avj oldi", "SSSR saqlanib qoldi", "respublikalar Moskvaga bo‘ysundi", "to‘ntarishchilar hokimiyatni oldi", "Mustaqillik intilishi kuchaydi.")
t.NAT("1991-yil 31-avgustda Davlat mustaqilligi asoslari to‘g‘risidagi Qonun qabul qilindi.", "dunyo siyosiy xaritasida O‘zbekiston Respublikasi paydo bo‘ldi", "O‘zbekiston SSSR tarkibida qoldi", "respublika tugatildi", "yangi ittifoq tuzildi", "Mustaqil davlat paydo bo‘ldi.")
t.TF("O‘zbek xalqi bir asrdan ortiq qaramlikdan so‘ng milliy davlatchiligini tikladi.", True, "To‘g‘ri.")
t.TF("Mustaqillik 1991-yil 19-avgustda e’lon qilingan.", False, "Noto‘g‘ri: 19-avgust – Moskvadagi to‘ntarish; mustaqillik 31-avgustda.")
t.TF4([("25-avgust farmoni bilan DXQ respublika tasarrufiga olindi.", True), ("Mustaqillik bilan birga Oliy Kengash bayonoti qabul qilindi.", True),
       ("Partiya va harbiy tuzilmalarda ham O‘zbekistonni ozod ko‘rish istagidagi shaxslar bo‘lgan.", True), ("To‘ntarish SSSRni saqlab qolishga muvaffaq bo‘lgan.", False)],
      "4-noto‘g‘ri: uch kundan oshmay muvaffaqiyatsizlikka uchragan.")
t.MUL([("Mustaqillik ajdodlarimiz to‘kkan qonning mahsuli deb baholanadi.", True),
       ("O‘zbekiston qadimiy davlatchilik an’analariga ega.", True),
       ("Mustaqillikdan oldin ichki qo‘shinlar faqat Moskvaga bo‘ysungan va bu o‘zgarmagan.", False)],
      "III noto‘g‘ri: 25-avgustdan ichki qo‘shinlar O‘zSSR Prezidentiga bo‘ysundirilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Islom Karimov respublika rahbari bo‘ldi", "Moskvada to‘ntarishga urinish", "ichki ishlar va DXQ respublika tasarrufiga olindi", "Davlat mustaqilligi e’lon qilindi"],
      "1989-06-23 → 1991-08-19 → 1991-08-25 → 1991-08-31.")
t.MATCH("Sanalarni voqealar bilan moslashtiring.", ["1989-yil 23-iyun", "1991-yil 19-avgust", "1991-yil 25-avgust", "1991-yil 31-avgust"],
        ["I. Karimov respublika rahbarligiga keldi", "Moskvada davlat to‘ntarishiga urinish", "kuch tuzilmalari respublika tasarrufiga olindi", "mustaqillik e’lon qilindi", "Farg‘ona voqealari"], 'abcd',
        "23-iyun – Karimov; 19-avgust – to‘ntarish; 25-avgust – farmon; 31-avgust – mustaqillik.")
t.VENN("1991-yil 25-avgust farmoni", "1991-yil 31-avgust qonuni",
       [("ichki ishlar va DXQ respublika tasarrufiga olindi", 1), ("ichki qo‘shinlar Prezidentga bo‘ysundirildi", 1),
        ("Davlat mustaqilligi asoslari belgilandi", 2), ("Oliy Kengash bayonoti bilan birga qabul qilindi", 2),
        ("mustaqillik sari qo‘yilgan qadam", 3)],
       "25-avgust – kuch tuzilmalari; 31-avgust – mustaqillik qonuni; ikkalasi mustaqillik qadami.")
t.MAPMATCH('uzb', ['Toshkent', 'Qo‘qon', 'Quvasoy'],
           ["1991-yil 31-avgustda mustaqillik e’lon qilingan poytaxt", "millatlararo mojaro chiqarishga urinilgan, 1989-yilda namoyish bo‘lgan shahar", "millatlararo mojaro boshlangan Farg‘ona vodiysi shahri"],
           "1 – Toshkent; 2 – Qo‘qon; 3 – Quvasoy.")
