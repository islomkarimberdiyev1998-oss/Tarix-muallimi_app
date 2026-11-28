from qlib import Topic, PLACES, REG
TOPICS = {}

# 6-mavzu. Milliy iqtisodiyotning barpo etilishi
t = Topic('y11u6', 11006); TOPICS['y11u6'] = t
t.B("Islom Karimov yangi iqtisodiy tizimga o‘tish modeli haqida qachon yozgan?", "1993-yilda", "1991-yilda", "1996-yilda", "2001-yilda", "1993-yilda.")
t.B("«O‘zbek modeli» nechta tamoyildan iborat?", "beshta", "uchta", "o‘nta", "yettita", "Besh tamoyil.")
t.B("So‘m-kuponlar qachon muomalaga chiqarilgan?", "1993-yil 1-noyabrdan", "1994-yil 1-iyuldan", "1992-yil fevraldan", "1991-yil 18-noyabrdan", "1993-yil 1-noyabr.")
t.B("Milliy valyuta – so‘m qachon muomalaga kiritilgan?", "1994-yil 1-iyulda", "1993-yil 1-noyabrda", "1992-yilda", "1995-yilda", "1994-yil 1-iyul.")
t.B("«Mulkni davlat tasarrufidan chiqarish va xususiylashtirish to‘g‘risida»gi qonun qachon qabul qilingan?", "1991-yil 18-noyabrda", "1992-yil fevralda", "1995-yilda", "1996-yilda", "1991-yil 18-noyabr.")
t.B("Davlat mulkini boshqarish va xususiylashtirish davlat qo‘mitasi qachon tuzilgan?", "1992-yil fevralda", "1991-yil noyabrda", "1995-yilda", "2001-yilda", "1992-yil fevral.")
t.B("Ommaviy xususiylashtirish qachondan boshlangan?", "1995-yildan", "1991-yildan", "2001-yildan", "2017-yildan", "1995-yildan.")
t.B("1996-yilga kelib necha million oila shaxsiy tomorqaga ega bo‘lgan?", "3 million", "50 ming", "5 ming", "1 million", "3 million.")
t.B("2024-yilda O‘zbekiston ODIN reytingida nechanchi o‘ringa ko‘tarilgan?", "12-o‘ringa", "83-o‘ringa", "1-o‘ringa", "50-o‘ringa", "83 ball bilan 12-o‘rin.")
t.B("Yurtimizdagi nechta shahar aeroporti xalqaro maqomga ega bo‘lgan?", "11 ta", "5 ta", "20 ta", "3 ta", "11 ta.")
t.B("Tezyurar «Afrosiyob» poyezdi qachondan qatnay boshlagan?", "2011-yildan", "2016-yildan", "2001-yildan", "2020-yildan", "2011-yildan.")
t.B("«Afrosiyob» dastlab qaysi yo‘nalishda qatnagan?", "Toshkent–Samarqand", "Toshkent–Buxoro", "Toshkent–Andijon", "Samarqand–Qarshi", "Toshkent–Samarqand.")
t.B("Qamchiq tunneli qachon ochilgan?", "2016-yilda", "2011-yilda", "2001-yilda", "2020-yilda", "2016-yilda.")
t.B("Toshkent metrosi Yunusobod yo‘nalishining birinchi qismi qachon ishga tushgan?", "2001-yilda", "1977-yilda", "2020-yilda", "2011-yilda", "2001-yilda.")
t.B("«Uz-DaewooAuto» zavodi qachon va qayerda ishga tushirilgan?", "1996-yilda Andijonda", "2021-yilda Jizzaxda", "2023-yilda Toshkentda", "1991-yilda Samarqandda", "1996-yil, Andijon.")
t.B("Elektr va gibrid avtomobillar ishlab chiqaradigan korxona qaysi?", "«BYD Uzbekistan Factory»", "«GM Uzbekistan»", "«ADM Jizzakh»", "«Uz-DaewooAuto»", "BYD, 2023-yil.")
t.B("«Yer to‘g‘risida»gi qonun qachon qabul qilingan?", "1992-yilda", "1996-yilda", "1991-yilda", "2008-yilda", "1992-yilda.")
t.B("O‘zbekiston qachon g‘alla mustaqilligiga erishgan?", "1996-yilda", "1992-yilda", "2008-yilda", "2016-yilda", "1996-yilda.")
t.B("1 gektarda uzum yetishtirish paxtaga nisbatan necha baravar daromadliroq?", "7 baravar", "5 baravar", "6 baravar", "2 baravar", "7 baravar (gilos – 6, yong‘oq – 5).")
t.NAT("Rubl zonasida qolish inflyatsiya va narx beqarorligi xavfini tug‘dirardi.", "O‘zbekiston o‘z milliy valyutasini joriy qilish yo‘lini tanladi", "O‘zbekiston rubl zonasida qoldi", "dollar rasmiy pul qilindi", "pul islohoti bekor qilindi", "Milliy valyuta – so‘m.")
t.NAT("1996-yilda «Fermer xo‘jaliklari to‘g‘risida»gi qonun qabul qilindi.", "mayda shirkatlar tugatilib, fermer xo‘jaliklari tashkil etildi", "kolxozlar tiklandi", "yerlar xususiy mulk bo‘ldi", "g‘alla importi oshdi", "Fermer xo‘jaliklari tuzildi.")
t.NAT("2016-yildan agroklasterlar va kooperatsiyalar hamkorligi o‘rnatildi.", "paxta tolasini mamlakatda to‘liq qayta ishlash yo‘lga qo‘yildi", "paxta xomashyo sifatida eksport qilindi", "fermerlar tarqatildi", "eksport qisqardi", "To‘liq qayta ishlash.")
t.NAT("2021-yildan paxta va g‘alla maydonlari qisqartirildi.", "ularning o‘rniga daromadliroq eksportbop ekinlar – bog‘lar ekila boshlandi", "yerlar bo‘sh qoldi", "paxta maydonlari kengaydi", "chorvachilik to‘xtadi", "Bog‘dorchilik kengaydi.")
t.TF("1990-yilda aholiga kerakli g‘allaning 82 foizi chetdan olib kelinardi.", True, "To‘g‘ri.")
t.TF("«Yer to‘g‘risida»gi qonunga ko‘ra yerlar xususiy mulk deb belgilangan.", False, "Noto‘g‘ri: yerlar davlat mulki; fermerlarga uzoq muddatli ijara huquqi berilgan.")
t.TF4([("Eksport qilinadigan meva-sabzavot turlari 34 tadan 119 taga yetgan.", True), ("2025-yilga kelib yo‘llar uzunligi 184 ming km dan oshgan.", True),
       ("Toshkent–Andijon magistrali qatnov vaqtini 5 soatdan 3 soatga qisqartiradi.", True), ("«ADM Jizzakh» zavodi 1996-yilda ish boshlagan.", False)],
      "4-noto‘g‘ri: ADM Jizzakh – 2021-yil; 1996-yilda Andijonda Uz-DaewooAuto.")
t.MUL([("2018–2024-yillarda 1 milliondan ortiq yangi tadbirkorlik subyekti tashkil etilgan.", True),
       ("2030-yilgacha YaIMni 160 mlrd dollarga yetkazish ko‘zda tutilgan.", True),
       ("«O‘zbek modeli»da iqtisodiyot siyosatga bo‘ysundirilgan.", False)],
      "III noto‘g‘ri: iqtisodiyotning siyosatdan ustunligi tamoyili belgilangan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["xususiylashtirish to‘g‘risidagi qonun", "so‘m-kuponlar muomalaga chiqdi", "milliy valyuta so‘m kiritildi", "Uz-DaewooAuto ishga tushdi, g‘alla mustaqilligi", "«Afrosiyob» qatnay boshladi", "Qamchiq tunneli ochildi"],
      "1991-11-18 → 1993-11-01 → 1994-07-01 → 1996 → 2011 → 2016.")
t.MATCH("Avtomobil zavodlarini ochilgan yili bilan moslashtiring.", ["Uz-DaewooAuto (Andijon)", "ADM Jizzakh", "BYD Uzbekistan Factory", "Toshkent metrosi Yunusobod yo‘nalishi"],
        ["1996", "2021", "2023", "2001", "2011"], 'abcd',
        "Uz-Daewoo – 1996; ADM – 2021; BYD – 2023; Yunusobod – 2001.")
t.VENN("Service point", "Service area",
       [("kichik obyektlar majmuasi", 1), ("asosiy xizmatlar: yonilg‘i, kafe, dorixona", 1),
        ("TIR park va motel", 2), ("bolalar maydonchasi, Wi-Fi", 2),
        ("avtomobil yo‘llari bo‘yidagi xizmat obyekti", 3)],
       "Point – kichik; area – TIR park, motel; ikkalasi yo‘l bo‘yi xizmat obyekti.")
t.MAPMATCH('uzb', ['Andijon', 'Jizzax', 'Toshkent', 'Buxoro'],
           ["1996-yilda Uz-DaewooAuto zavodi ishga tushgan shahar", "2021-yilda ADM avtomobil zavodi ish boshlagan shahar", "2001-yilda metroning Yunusobod yo‘nalishi ochilgan poytaxt", "«Afrosiyob» keyinchalik qatnay boshlagan g‘arbiy shahar"],
           "1 – Andijon; 2 – Jizzax; 3 – Toshkent; 4 – Buxoro.")

# 7-mavzu. Ishlab chiqarish salohiyati va integratsiya
t = Topic('y11u7', 11007); TOPICS['y11u7'] = t
t.B("Samarqandda qanday avtobus zavodi ishga tushgan?", "«SamKochAvto»", "«Uz-Daewoo»", "«ADM»", "«BYD»", "«SamKochAvto».")
t.B("Sovet respublikalari orasida qaysi yildan faqat O‘zbekistonda izchil iqtisodiy o‘sish ta’minlangan?", "1996-yildan", "1991-yildan", "2004-yildan", "2016-yildan", "1996-yildan.")
t.B("1996–2003-yillarda o‘rtacha iqtisodiy o‘sish qancha bo‘lgan?", "4,3 foiz", "7,5 foiz", "6 foiz", "12 foiz", "4,3 foiz.")
t.B("2004-yildan o‘rtacha yillik o‘sish qancha bo‘lgan?", "7,5 foiz", "4,3 foiz", "2 foiz", "10 foiz", "7,5 foiz.")
t.B("Mustaqillik yillarida ish boshlagan yirik maskanlardan biri qaysi?", "Sho‘rtan gazkimyo majmuasi", "Toshkent traktor zavodi", "Chirchiq elektrokimyo kombinati", "Farhod GESi", "Sho‘rtan, Buxoro NQIZ, Qo‘ng‘irot soda, Dehqonobod kaliy.")
t.B("Korxonalar to‘laydigan ijtimoiy soliq stavkasi necha foizgacha tushirilgan?", "12 foizgacha", "25 foizgacha", "5 foizgacha", "20 foizgacha", "25 foizdan 12 foizga.")
t.B("Jismoniy shaxslarga valyutani banklarda erkin sotish va sotib olish huquqi qachondan berilgan?", "2017-yildan", "2016-yildan", "2020-yildan", "1994-yildan", "2017-yildan.")
t.B("Ipoteka bo‘yicha dastlabki badal uchun qancha subsidiya berilgan?", "32 million so‘m", "10 million so‘m", "100 million so‘m", "3,2 million so‘m", "32 million so‘m (2020-yildan).")
t.B("«Doing Business» reytingida O‘zbekiston 2020-yilda necha ball olgan?", "58", "44", "83", "12", "2016 – 44, 2020 – 58 ball.")
t.B("«Doing Business» hisobotini qaysi tashkilot chiqaradi?", "Jahon banki", "BMT", "Osiyo taraqqiyot banki", "JST", "Jahon banki.")
t.B("Xorijiy va mahalliy fuqarolarni ro‘yxatga olishning elektron tizimi qanday ataladi?", "«e-MEHMON»", "«e-ngo»", "«my.gov»", "«Tashabbusli byudjet»", "«e-MEHMON».")
t.B("«Tashabbusli byudjet» orqali 2025-yilgacha nechta loyiha amalga oshirilgan?", "2215 ta", "221 ta", "1,1 trillion", "30 ta", "2215 ta loyiha, 1,1 trln so‘m.")
t.B("O‘zbekistonga kelayotgan sayyohlar soni necha barobar ortgan?", "2,5 barobar", "10 barobar", "2 barobar", "5 barobar", "2,5 barobar.")
t.B("«Erkin iqtisodiy zonalar to‘g‘risida»gi qonun qachon qabul qilingan?", "1996-yilda", "2016-yilda", "2019-yilda", "1991-yilda", "1996-yilda.")
t.B("2019-yilda qaysi erkin iqtisodiy zona ish boshlagan?", "«Termiz»", "«Urgut»", "«Navoiy»", "«Angren»", "«Termiz».")
t.B("Farmatsevtika sohasi uchun barpo etilgan hududlardan biri qaysi?", "«Zomin-farm»", "«Navoiy»", "«Jizzax»", "«Hazorasp»", "«Nukus-farm», «Zomin-farm», «Kosonsoy-farm».")
t.B("JSTga a’zo bo‘lish jarayoni qachon boshlangan?", "1994-yilda", "2005-yilda", "2018-yilda", "2003-yilda", "1994-yilda (2005-yilda to‘xtagan, 2018-yildan faollashgan).")
t.B("O‘zbekiston Islom taraqqiyot bankiga qachon a’zo bo‘lgan?", "2003-yilda", "1994-yilda", "2018-yilda", "1996-yilda", "2003-yilda.")
t.B("O‘zbekiston birinchi bor suveren kredit reytingini qachon olgan?", "2018-yilda", "2019-yilda", "2003-yilda", "2024-yilda", "2018-yilda.")
t.NAT("Avvallari valyuta faqat «qora bozor»dan olinardi; 2017-yildan valyuta siyosati liberallashtirildi.", "aholi banklarda valyutani bemalol sotib olish va sotish imkoniga ega bo‘ldi", "valyuta savdosi taqiqlandi", "qora bozor kengaydi", "so‘m muomaladan chiqdi", "Valyuta erkinlashdi.")
t.NAT("Soliq turlari va tekshiruvlar kamaytirildi, stavkalar pasaytirildi.", "tadbirkorlarning soliq yuki yengillashib, faolligi oshdi", "tadbirkorlar kamaydi", "byudjet tushumi to‘xtadi", "biznes muhiti yomonlashdi", "Tadbirkorlik faollashdi.")
t.NAT("Erkin iqtisodiy zonalarda loyihalar amalga oshirildi.", "2024-yilda iqtisodiyot 6 foizdan ortiq o‘sishiga muhim hissa qo‘shildi", "iqtisodiyot qisqardi", "eksport kamaydi", "investorlar ketdi", "Iqtisodiy o‘sish.")
t.NAT("2018-yildan JSTga a’zolik jarayoni yana faollashtirildi.", "global savdo qoidalariga moslashish va xalqaro bozorga erkin chiqish imkoni kengaymoqda", "tashqi savdo to‘xtadi", "bojlar oshirildi", "importlar taqiqlandi", "Xalqaro bozorga chiqish.")
t.TF("Mamlakat hududida tovar va xizmatlar uchun chet el valyutasida to‘lovlar taqiqlangan.", True, "To‘g‘ri – milliy valyuta yagona to‘lov vositasi.")
t.TF("2021-yilga kelib mamlakatda faqat uchta erkin iqtisodiy zona bo‘lgan.", False, "Noto‘g‘ri: yigirmadan ortiq EIZ va 300 dan ortiq kichik sanoat zonasi bo‘lgan.")
t.TF4([("2016-yilda «Urgut», «G‘ijduvon», «Qo‘qon», «Hazorasp» EIZlari ish boshlagan.", True), ("IsDB doirasida 2,5 mlrd dollardan ortiq 30 ta loyiha ma’qullangan.", True),
       ("2019-yilda O‘zbekiston xalqaro moliyaviy statistik tizimlarda o‘z sahifasiga ega bo‘lgan.", True), ("«Doing Business» reytingidagi ball 2016–2020-yillarda kamaygan.", False)],
      "4-noto‘g‘ri: 44 balldan 58 ballga oshgan.")
t.MUL([("O‘zbekiston Transafg‘on temiryo‘li loyihasida ishtirok etmoqda.", True),
       ("Dastlab «Navoiy» logistika markazi ochilgan.", True),
       ("Sovet davrida O‘zbekiston iqtisodiyoti har tomonlama rivojlangan edi.", False)],
      "III noto‘g‘ri: asosan biryoqlama xomashyo yetkazishga ixtisoslashgan edi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["JSTga a’zolik jarayoni boshlandi", "EIZ to‘g‘risidagi qonun", "Islom taraqqiyot bankiga a’zolik", "valyuta erkinlashtirildi", "birinchi suveren kredit reytingi", "«Termiz» EIZ ish boshladi"],
      "1994 → 1996 → 2003 → 2017 → 2018 → 2019.")
t.MATCH("Korxonalarni joylashgan shahri bilan moslashtiring.", ["SamKochAvto", "soda zavodi", "kaliy zavodi", "neftni qayta ishlash zavodi"],
        ["Samarqand", "Qo‘ng‘irot", "Dehqonobod", "Buxoro", "Andijon"], 'abcd',
        "SamKochAvto – Samarqand; soda – Qo‘ng‘irot; kaliy – Dehqonobod; NQIZ – Buxoro.")
t.VENN("Erkin iqtisodiy zona", "Maxsus iqtisodiy zona",
       [("1996-yilgi qonun bilan ta’riflangan", 1), ("«Urgut», «Hazorasp» kabi", 1),
        ("maxsus ajratilgan chegaralangan hudud", 2), ("chet el investitsiyasi va boshqaruv tajribasini jalb etish", 2),
        ("alohida huquqiy tartibga ega hudud", 3)],
       "EIZ – 1996-yil qonuni, Urgut; MIZ – maxsus hudud, investitsiya; ikkalasi alohida huquqiy tartib.")
t.MAPMATCH('uzb', ['Samarqand', 'Qo‘ng‘irot', 'Termiz', 'Navoiy'],
           ["SamKochAvto avtobus zavodi joylashgan shahar", "soda zavodi qurilgan Qoraqalpog‘iston shahri", "2019-yilda erkin iqtisodiy zona ish boshlagan shahar", "dastlabki logistika markazi ochilgan shahar"],
           "1 – Samarqand; 2 – Qo‘ng‘irot; 3 – Termiz; 4 – Navoiy.")
