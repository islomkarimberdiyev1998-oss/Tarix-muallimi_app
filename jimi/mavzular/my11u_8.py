from qlib import Topic, PLACES, REG
TOPICS = {}

# 18-mavzu. Markaziy Osiyo – tashqi siyosatning ustuvor yo‘nalishi
t = Topic('y11u18', 11018); TOPICS['y11u18'] = t
t.B("«Markaziy Osiyo» iborasi siyosiy va hududiy atama sifatida qachon ishlatilgan?", "1993-yilda Toshkentdagi anjumanda", "1991-yilda Olmaotada", "2017-yilda BMTda", "1994-yilda Ostonada", "1993-yil, Toshkent.")
t.B("Mustaqillikning ilk yillarigacha mintaqa qanday nomlangan?", "O‘rta Osiyo", "Turkiston", "Movarounnahr", "Turon", "O‘rta Osiyo.")
t.B("1994-yilda tashkil etilgan iqtisodiy hamjamiyat 2002-yilda nimaga aylantirildi?", "Markaziy Osiyo hamkorligi tashkilotiga", "Yevrosiyo iqtisodiy hamjamiyatiga", "MDHga", "ShHTga", "Markaziy Osiyo hamkorligi tashkiloti.")
t.B("Markaziy Osiyo hamkorligi tashkiloti qachon faoliyatini to‘xtatgan?", "2006-yilda", "2002-yilda", "1994-yilda", "2017-yilda", "2006-yil, YevrAzESga qo‘shilib.")
t.B("Markaziy Osiyo davlatlari rahbarlarining birinchi Maslahat uchrashuvi qayerda o‘tgan?", "Ostonada", "Toshkentda", "Bishkekda", "Dushanbeda", "2018-yil, Ostona.")
t.B("Ikkinchi Maslahat uchrashuvi qachon va qayerda o‘tgan?", "2019-yilda Toshkentda", "2018-yilda Ostonada", "2017-yilda Samarqandda", "2020-yilda Ashxobodda", "2019-yil, Toshkent.")
t.B("2025-yilda «Do‘stlik» stelasi qayerda ochilgan?", "Xo‘jand shahrida", "Toshkentda", "O‘sh shahrida", "Turkistonda", "Uch davlat chegarasi tutashgan hududda – Xo‘jand.")
t.B("O‘zbekiston va Qozog‘iston o‘rtasida do‘stlik va hamkorlik shartnomasi qayerda imzolangan?", "Turkiston shahrida", "Ostonada", "Toshkentda", "Olmaotada", "1992-yil, Turkiston.")
t.B("O‘zbekiston va Qozog‘iston Strategik sheriklik to‘g‘risidagi shartnomani qachon imzolagan?", "2013-yilda", "1998-yilda", "1992-yilda", "2018-yilda", "2013-yilda.")
t.B("Qozog‘iston O‘zbekistonning nechanchi yirik tashqi savdo hamkori?", "uchinchi", "birinchi", "beshinchi", "o‘ninchi", "Uchinchi.")
t.B("Shavkat Mirziyoyev Qozog‘istonning qaysi ordeni bilan taqdirlangan?", "«Oltin Qiron» («Oltin burgut»)", "«Do‘stlik»", "«Manas»", "«Ismoil Somoniy»", "«Oltin Qiron».")
t.B("O‘zbekistonda nechta qozoq milliy madaniy markazi bor?", "14 ta", "4 ta", "40 ta", "140 ta", "14 ta.")
t.B("O‘zbekiston va Qirg‘iziston o‘rtasida Abadiy do‘stlik shartnomasi qachon imzolangan?", "1996-yilda", "1993-yilda", "1998-yilda", "2024-yilda", "1996-yilda.")
t.B("2018-yilda qaysi qirg‘iz yozuvchisi tavalludining 90 yilligi nishonlangan?", "Chingiz Aytmatov", "Abay Qo‘nonboyev", "Maxtumquli Firog‘iy", "Abdurahmon Jomiy", "Chingiz Aytmatov.")
t.B("2024-yilda O‘zbekiston va Tojikiston qanday shartnoma imzoladi?", "Ittifoqchilik munosabatlari to‘g‘risida", "Abadiy do‘stlik to‘g‘risida", "Strategik sheriklik to‘g‘risida", "Erkin savdo to‘g‘risida", "Ittifoqchilik shartnomasi, Dushanbe.")
t.B("2018-yilda Samarqand va Dushanbeda qaysi mutafakkirlar haykallari o‘rnatildi?", "Navoiy va Jomiy", "Navoiy va Maxtumquli", "Abay va Navoiy", "Aytmatov va Jomiy", "Navoiy va Jomiy.")
t.B("Shavkat Mirziyoyev Prezident sifatida ilk xorijiy tashrifini qaysi davlatdan boshlagan?", "Turkmaniston", "Qozog‘iston", "Tojikiston", "Rossiya", "Turkmaniston.")
t.B("2018-yilda Urganchda nima ochilgan?", "«O‘zbek – turkman do‘stlik uyi»", "«Ashxobod» bog‘i", "Maxtumquli ko‘chasi", "turkman teatri", "«O‘zbek – turkman do‘stlik uyi».")
t.NAT("2006-yilda Markaziy Osiyo hamkorligi tashkiloti faoliyatini to‘xtatdi.", "uzoq vaqt davomida mintaqada integratsiya sustlashib qoldi", "integratsiya kuchaydi", "yangi davlat tuzildi", "chegaralar yo‘qotildi", "Integratsiya sustlashdi.")
t.NAT("2017-yildan chegaralarni belgilash bo‘yicha ijobiy kelishuvlarga erishildi.", "o‘nlab o‘tkazish punktlari tiklanib, borib-kelish yengillashdi", "chegaralar yopildi", "vizalar kuchaytirildi", "savdo to‘xtadi", "Punktlar tiklandi.")
t.NAT("2017-yilda BMTning 72-sessiyasida Mirziyoyev rahbarlar uchrashuvlarini muntazam o‘tkazishni taklif qildi.", "Maslahat uchrashuvlari an’anaviy muloqot platformasiga aylandi", "taklif rad etildi", "uchrashuvlar to‘xtatildi", "MDH tarqatildi", "Maslahat uchrashuvlari.")
t.NAT("2021–2022-yillardan Toshkent–Dushanbe aviaparvozlari va Samarqand–Dushanbe avtobus qatnovlari tiklandi.", "ikki xalq o‘rtasida borib-kelish va aloqalar kengaydi", "chegara yopildi", "savdo to‘xtadi", "aloqalar uzildi", "Aloqalar kengaydi.")
t.TF("O‘zbekiston Markaziy Osiyoning barcha mamlakatlari va Afg‘oniston bilan chegaradosh.", True, "To‘g‘ri.")
t.TF("O‘zbekiston va Turkmaniston o‘rtasida diplomatik munosabatlar 1992-yilda o‘rnatilgan.", False, "Noto‘g‘ri: 1993-yilda (1992 – Tojikiston bilan).")
t.TF4([("O‘zbekiston va Qozog‘iston chegaralarni huquqiy rasmiylashtirishni yakunladi.", True), ("Ostona shahrida Alisher Navoiy haykali o‘rnatilgan.", True),
       ("Toshkentda Maxtumquli Firog‘iy nomidagi ko‘cha ochilgan.", True), ("2018-yil O‘zbekistonda «Qozog‘iston yili» deb e’lon qilingan.", False)],
      "4-noto‘g‘ri: 2018 – Qozog‘istonda «O‘zbekiston yili», 2019 – O‘zbekistonda «Qozog‘iston yili».")
t.MUL([("«Xitoy – Qirg‘iziston – O‘zbekiston» temir yo‘li bo‘yicha dastlabki kelishuvlarga erishildi.", True),
       ("O‘zbekiston va Turkmaniston o‘rtasida erkin savdo rejimi joriy etilgan.", True),
       ("1994-yilgi iqtisodiy hamjamiyatga dastlab Turkmaniston ham kirgan.", False)],
      "III noto‘g‘ri: O‘zbekiston, Qozog‘iston, Qirg‘iziston, keyinchalik Tojikiston.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Turkistonda O‘zbekiston–Qozog‘iston shartnomasi", "iqtisodiy hamjamiyat tuzildi", "Markaziy Osiyo hamkorligi tashkiloti", "tashkilot YevrAzESga qo‘shildi", "birinchi Maslahat uchrashuvi", "«Do‘stlik» stelasi ochildi"],
      "1992 → 1994 → 2002 → 2006 → 2018 → 2025.")
t.MATCH("Shartnomalarni davlat bilan moslashtiring.", ["1998-yil Abadiy do‘stlik va 2013-yil Strategik sheriklik", "1996-yil Abadiy do‘stlik", "2024-yil Ittifoqchilik munosabatlari", "1996-yil Do‘stlik, hamkorlik va o‘zaro yordam"],
        ["Qozog‘iston", "Qirg‘iziston", "Tojikiston", "Turkmaniston", "Afg‘oniston"], 'abcd',
        "Qozog‘iston – 1998, 2013; Qirg‘iziston – 1996; Tojikiston – 2024; Turkmaniston – 1996.")
t.VENN("O‘zbekiston – Qirg‘iziston", "O‘zbekiston – Tojikiston",
       [("Chingiz Aytmatovning 90 yilligi", 1), ("Farg‘ona va Namanganda quyosh stansiyalari loyihasi", 1),
        ("Navoiy va Jomiy haykallari", 2), ("Ittifoqchilik munosabatlari shartnomasi", 2),
        ("2025-yil Xo‘janddagi «Do‘stlik» stelasi", 3)],
       "Aytmatov, quyosh stansiyalari – Qirg‘iziston; Navoiy–Jomiy, ittifoqchilik – Tojikiston; stela – uchala davlat.")
t.MAPMATCH('tsent', ['Astana', 'Turkiston', 'Dushanbe', 'Bishkek'],
           ["2018-yilda birinchi Maslahat uchrashuvi o‘tgan, Navoiy haykali o‘rnatilgan shahar", "1992-yilda O‘zbekiston–Qozog‘iston do‘stlik shartnomasi imzolangan shahar", "2024-yilda Ittifoqchilik shartnomasi imzolangan, Jomiy haykali o‘rnatilgan shahar", "O‘sh bilan birga O‘zbekiston madaniyati kunlari o‘tkazilgan poytaxt"],
           "1 – Ostona; 2 – Turkiston; 3 – Dushanbe; 4 – Bishkek.")

# 19-mavzu. O‘zbekiston va dunyoning yetakchi mamlakatlari hamkorligi
t = Topic('y11u19', 11019); TOPICS['y11u19'] = t
t.B("O‘zbekiston va Rossiya o‘rtasida diplomatik munosabat qachon o‘rnatilgan?", "1992-yilda", "1991-yilda", "2000-yilda", "2004-yilda", "1992-yilda.")
t.B("2000-yilda xorijga ilk rasmiy tashrifini O‘zbekistondan boshlagan Rossiya Prezidenti kim?", "Vladimir Putin", "Boris Yelsin", "Dmitriy Medvedev", "Mixail Gorbachyov", "Vladimir Putin.")
t.B("O‘zbekiston va Rossiya Strategik sheriklik to‘g‘risidagi shartnomani qachon imzolagan?", "2004-yilda", "2005-yilda", "1992-yilda", "2022-yilda", "2004-yilda.")
t.B("O‘zbekiston va Rossiya Ittifoqchilik munosabatlari to‘g‘risidagi shartnomani qachon imzolagan?", "2005-yilda", "2004-yilda", "2001-yilda", "2022-yilda", "2005-yilda.")
t.B("2022-yilda O‘zbekiston va Rossiya qanday hujjat imzoladi?", "Keng qamrovli strategik sheriklik to‘g‘risidagi deklaratsiya", "Ittifoqchilik shartnomasi", "Do‘stlik asoslari shartnomasi", "Erkin savdo bitimi", "Keng qamrovli strategik sheriklik deklaratsiyasi.")
t.B("Rossiya O‘zbekistonning nechanchi eng yirik savdo sherigi?", "ikkinchi", "birinchi", "uchinchi", "beshinchi", "Ikkinchi.")
t.B("Xitoy hamkorligida barpo etilgan yirik loyiha qaysi?", "Pop – Angren temir yo‘li va Qamchiq tunneli", "Toshkent metrosi", "Navoiy kon-metallurgiya kombinati", "Chorvoq GESi", "Pop–Angren va Qamchiq.")
t.B("O‘zbekiston va Xitoy o‘rtasida necha kungacha vizasiz rejim joriy etilgan?", "30 kungacha", "10 kungacha", "60 kungacha", "90 kungacha", "30 kungacha.")
t.B("Konfutsiy instituti qaysi shaharlarda ochilgan?", "Toshkent va Samarqandda", "Buxoro va Xivada", "Toshkent va Namanganda", "Samarqand va Termizda", "Toshkent va Samarqand.")
t.B("Vashingtonda O‘zbekiston elchixonasi qachon ochilgan?", "1993-yilda", "1992-yilda", "1996-yilda", "2018-yilda", "1993-yilda (1992 – Toshkentda AQSH elchixonasi).")
t.B("Shavkat Mirziyoyevning AQSHga birinchi rasmiy tashrifi qachon bo‘lgan?", "2018-yilda", "2017-yilda", "2025-yilda", "1996-yilda", "2018-yilda.")
t.B("Markaziy Osiyo va AQSH qaysi formatda hamkorlik qiladi?", "«C5+1»", "«Bir makon – bir yo‘l»", "SHHT", "MDH", "«C5+1».")
t.B("Toshkentda qaysi AQSH universiteti filiali ish boshlagan?", "Vebster universiteti", "Garvard universiteti", "Turin universiteti", "Piza universiteti", "Vebster universiteti.")
t.B("«Unutilgan ma’rifat» kitobining muallifi kim?", "Frederik Starr", "Donald Tramp", "Emmanuel Makron", "Konfutsiy", "Amerikalik olim Frederik Starr.")
t.B("O‘zbekiston va Yevropa Ittifoqi o‘rtasida sheriklik va hamkorlik bitimi qayerda imzolangan?", "Florensiyada", "Brusselda", "Rimda", "Parijda", "1996-yil, Florensiya.")
t.B("«Markaziy Osiyo – Yevropa Ittifoqi» birinchi sammiti qayerda o‘tgan?", "Samarqandda", "Toshkentda", "Florensiyada", "Berlinda", "2025-yil, Samarqand.")
t.B("O‘zbekistonning Yevropa Ittifoqidagi eng yirik savdo hamkori qaysi?", "Germaniya", "Fransiya", "Italiya", "Vengriya", "Germaniya.")
t.B("Shavkat Mirziyoyev Yevropaga ilk tashrifini qaysi davlatdan boshlagan?", "Fransiya", "Germaniya", "Italiya", "Vengriya", "Fransiya.")
t.B("2022-yilda qaysi muzeyda Markaziy Osiyo tarixiga oid ko‘rgazma o‘tkazilgan?", "Luvr", "Britaniya muzeyi", "Ermitaj", "Prado", "Luvr muzeyi.")
t.NAT("O‘zbekistonda Rossiyaning nufuzli OTMlari filiallari ochildi.", "Lomonosov nomidagi MDU, Gubkin nomidagi universitet kabi filiallarda yoshlar ta’lim olmoqda", "rus tilidagi ta’lim to‘xtatildi", "OTMlar yopildi", "talabalar Rossiyaga chiqarib yuborildi", "Filiallar faoliyati.")
t.NAT("2018-yilda Mirziyoyev AQSHga birinchi rasmiy tashrif buyurdi.", "Strategik sheriklikning yangi davri haqida qo‘shma bayonot qabul qilindi", "aloqalar uzildi", "elchixona yopildi", "sanksiya joriy etildi", "Qo‘shma bayonot.")
t.NAT("2025-yilda Mirziyoyev Fransiyaga davlat tashrifi bilan bordi.", "ikki mamlakat strategik sheriklik munosabatlarini o‘rnatish to‘g‘risida tarixiy qarorga keldi", "aloqalar to‘xtatildi", "Fransuz alyansi yopildi", "investitsiyalar qaytarildi", "Strategik sheriklik.")
t.NAT("2025-yilda Samarqandda «Markaziy Osiyo – Yevropa Ittifoqi» birinchi sammiti o‘tdi.", "o‘zaro hamkorlikning yangi bosqichlari boshlandi", "YI bilan aloqalar uzildi", "Florensiya bitimi bekor qilindi", "sammit qoldirildi", "Yangi bosqich.")
t.TF("O‘zbekiston 2020-yildan Venetsiya biyennalelarida ishtirok etmoqda.", True, "To‘g‘ri.")
t.TF("Islom Karimov AQSHga 2018-yilda rasmiy tashrif buyurgan.", False, "Noto‘g‘ri: 1996-yil iyunda; 2018-yilda Sh. Mirziyoyev tashrif buyurgan.")
t.TF4([("O‘zbekistonda Turin va Piza universitetlari filiallari bor.", True), ("Toshkentda Gyote instituti faoliyat yuritadi.", True),
       ("2023-yilda Emmanuel Makron O‘zbekistonga rasmiy tashrif buyurgan.", True), ("«Volkswagen», «Siemens», «Knauf» – AQSH kompaniyalari.", False)],
      "4-noto‘g‘ri: ular Germaniya kompaniyalari.")
t.MUL([("O‘zbekiston Xitoy bilan «Bir makon – bir yo‘l» formatida hamkorlik qiladi.", True),
       ("Shanxay xorijiy tillar universitetida o‘zbek tili kafedrasi bor.", True),
       ("Islom Karimov 2001-yilda Xitoyga davlat tashrifi bilan borgan.", False)],
      "III noto‘g‘ri: 2001-yilda Rossiyaga davlat tashrifi bilan borgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Vashingtonda O‘zbekiston elchixonasi ochildi", "Florensiyada YI bilan bitim", "Putinning O‘zbekistonga ilk tashrifi", "Rossiya bilan Ittifoqchilik shartnomasi", "Mirziyoyevning AQSHga birinchi tashrifi", "Luvrda Markaziy Osiyo ko‘rgazmasi"],
      "1993 → 1996 → 2000 → 2005 → 2018 → 2022.")
t.MATCH("Kompaniyalarni davlat bilan moslashtiring.", ["«General Motors», «Coca-Cola»", "«Volkswagen», «Siemens»", "Eksimbank, «Ipak yo‘li» jamg‘armasi", "Gubkin nomidagi universitet filiali"],
        ["AQSH", "Germaniya", "Xitoy", "Rossiya", "Fransiya"], 'abcd',
        "GM, Coca-Cola – AQSH; VW, Siemens – Germaniya; Eksimbank – Xitoy; Gubkin – Rossiya.")
t.VENN("O‘zbekiston – Rossiya", "O‘zbekiston – Xitoy",
       [("Ittifoqchilik munosabatlari shartnomasi (2005)", 1), ("MDH doirasidagi savdo kelishuvlari", 1),
        ("Konfutsiy instituti", 2), ("30 kungacha vizasiz rejim", 2),
        ("1992-yilda diplomatik munosabat o‘rnatilgan", 3)],
       "Rossiya – Ittifoqchilik, MDH; Xitoy – Konfutsiy, vizasiz rejim; ikkalasi bilan 1992-yilda aloqa.")
t.MAPMATCH('globe', ['Vashington', 'Moskva', 'Pekin', 'Florensiya'],
           ["1993-yilda O‘zbekiston elchixonasi ochilgan poytaxt", "Lomonosov nomidagi davlat universiteti joylashgan poytaxt", "Xitoy poytaxti", "1996-yilda O‘zbekiston–YI bitimi imzolangan shahar"],
           "1 – Vashington; 2 – Moskva; 3 – Pekin; 4 – Florensiya.")
