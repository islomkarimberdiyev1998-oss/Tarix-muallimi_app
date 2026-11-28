from qlib import Topic, PLACES, REG
TOPICS = {}

# 11-mavzu. Ilm-fanda erishilgan yutuqlar
t = Topic('y11u11', 11011); TOPICS['y11u11'] = t
t.B("Fanlar akademiyasi qachon qayta tashkil etilgan?", "1991-yilda", "1997-yilda", "2017-yilda", "1992-yilda", "1991-yilda.")
t.B("Xorazm Ma’mun akademiyasi qachon faoliyatini boshlagan?", "1997-yilda", "1991-yilda", "2007-yilda", "2018-yilda", "1997-yilda.")
t.B("Xalqaro matematika olimpiadasini o‘tkazish tashabbusi qayerda ilgari surilgan?", "Ostonadagi ITT ilm-fan sammitida", "BMT Bosh Assambleyasida", "Toshkentdagi forumda", "YUNESKO sessiyasida", "2017-yil sentyabr, Ostona.")
t.B("Muhammad al-Xorazmiy nomidagi xalqaro matematika olimpiadasi ilk bor qayerda o‘tkazilgan?", "Urganchda", "Toshkentda", "Samarqandda", "Xivada", "2018-yil, Urganch.")
t.B("2017-yilda necha yillik tanaffusdan so‘ng Fanlar akademiyasiga yangi haqiqiy a’zolar tasdiqlandi?", "22 yillik", "12 yillik", "32 yillik", "16 yillik", "22 yillik tanaffusdan so‘ng 32 nafar.")
t.B("2023-yilda Fanlar akademiyasining nechta yangi haqiqiy a’zosi tasdiqlangan?", "16 nafar", "32 nafar", "22 nafar", "30 nafar", "16 nafar.")
t.B("2025-yilda Fanlar akademiyasi tarkibida nechtadan ortiq ilmiy-tadqiqot muassasasi bor?", "30 dan", "16 dan", "100 dan", "300 dan", "30 dan ortiq.")
t.B("Oliy attestatsiya komissiyasi (OAK) qachon tashkil etilgan?", "1992-yilda", "1991-yilda", "1997-yilda", "2007-yilda", "1992-yilda.")
t.B("2007-yilda Maydanak rasadxonasida aniqlangan kichik sayyoraga qanday nom berilgan?", "«Samarqand»", "«Ulug‘bek»", "«Xorazm»", "«Turon»", "«Samarqand».")
t.B("«Olima» uyushmasi qachon tashkil etilgan?", "1992-yilda", "2007-yilda", "2016-yilda", "1997-yilda", "1992-yilda.")
t.B("YUNESKO ma’lumotiga ko‘ra O‘zbekistonda olimalar ulushi qancha?", "39 foiz", "30 foiz", "25 foiz", "50 foiz", "39 foiz (dunyoda 30 foiz).")
t.B("YUNESKOning Karlos Finley mukofotiga sazovor bo‘lgan olima kim?", "Dilfuza Egamberdiyeva", "Rahbarxon Murtazayeva", "Nafisa Mo‘minova", "Diyora Keldiyorova", "Mikrobiolog Dilfuza Egamberdiyeva.")
t.B("Xalqaro ilm-fan sohasidagi xotin-qizlar kuni qaysi sana?", "11-fevral", "16-noyabr", "8-mart", "22-dekabr", "11-fevral.")
t.B("«El-yurt umidi» jamg‘armasi qachon tashkil etilgan?", "2018-yilda", "2016-yilda", "1992-yilda", "2007-yilda", "2018-yilda.")
t.B("Fizika sohasida necha Kelvinda o‘ta o‘tkazuvchanlikka o‘tadigan materiallar yaratilgan?", "110–150", "10–15", "300–350", "1100–1500", "110–150 Kelvin, quyosh energiyasi yordamida.")
t.B("Innovatsion rivojlanish vazirligi keyinchalik nimaga aylantirildi?", "Innovatsion rivojlanish agentligiga", "Fanlar akademiyasiga", "OAKga", "IT parkiga", "Agentlikka.")
t.NAT("Akademiya olimlari paxtachilik sohasida tadqiqotlar olib bordi.", "turli iqlim sharoitlariga mos yuqori hosildor paxta navlari yaratildi", "paxta ekish to‘xtatildi", "paxta navlari chetdan olindi", "hosildorlik kamaydi", "Yangi navlar.")
t.NAT("Tilshunos va adabiyotshunoslar fundamental tadqiqotlar olib bordi.", "6 jildli «O‘zbek tilining izohli lug‘ati» nashr qilindi", "lug‘atlar taqiqlandi", "folklor yo‘q qilindi", "faqat rus tilida yozildi", "Izohli lug‘at.")
t.NAT("2007-yilda Maydanak rasadxonasida kuzatuvlar olib borildi.", "O‘zbekiston tarixida ilk bor yangi kichik sayyora aniqlandi", "rasadxona yopildi", "yangi kometa yo‘qoldi", "kuzatuv to‘xtatildi", "«Samarqand» sayyorasi.")
t.NAT("2018-yilda «El-yurt umidi» jamg‘armasi tashkil etildi.", "xorijdagi olim va mutaxassislar islohotlarga jalb qilindi, yoshlar chet elda ta’lim olmoqda", "chet elga chiqish taqiqlandi", "olimlar ishdan bo‘shatildi", "jamg‘arma tugatildi", "Xorijiy tajriba jalb qilindi.")
t.TF("«Bo‘lajak olim», «Olima ayollar», «Akademik harakatchanlik» tanlovlarini Innovatsion rivojlanish agentligi yo‘lga qo‘ygan.", True, "To‘g‘ri.")
t.TF("«Olima» uyushmasi faqat Toshkent shahridagi olimalarni birlashtiradi.", False, "Noto‘g‘ri: viloyatlar, Qoraqalpog‘iston, 100 ga yaqin OTM olimalarini birlashtiradi.")
t.TF4([("Temuriylar tarixi davlat muzeyi Fanlar akademiyasi tarkibida.", True), ("O‘zbek olimlari YUNESKO va MAGATE bilan hamkorlik qiladi.", True),
       ("Toshkentda Dasturiy mahsulotlar va axborot texnologiyalari parki ochilgan.", True), ("Xalqaro ilm-fan xotin-qizlar kuni 2006-yildan nishonlanadi.", False)],
      "4-noto‘g‘ri: 2016-yildan nishonlanadi (rezolyutsiya 2015-yil 22-dekabr).")
t.MUL([("OAK ilmiy daraja va unvonlar beruvchi davlat organidir.", True),
       ("«Alisher Navoiy ensiklopediyasi» nashr qilingan.", True),
       ("Xorazm Ma’mun akademiyasi 2017-yilda tashkil etilgan.", False)],
      "III noto‘g‘ri: 1997-yilda faoliyat boshlagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Fanlar akademiyasi qayta tashkil etildi", "OAK tashkil etildi", "Xorazm Ma’mun akademiyasi", "«Samarqand» sayyorasi aniqlandi", "akademiyaga 32 yangi a’zo", "al-Xorazmiy olimpiadasi Urganchda"],
      "1991 → 1992 → 1997 → 2007 → 2017 → 2018.")
t.MATCH("Raqamlarni ma’nosi bilan moslashtiring.", ["39 %", "30 %", "32 nafar", "16 nafar"],
        ["O‘zbekistonda olimalar ulushi", "dunyoda olimalar ulushi", "2017-yilda tasdiqlangan akademiklar", "2023-yilda tasdiqlangan akademiklar", "OAK a’zolari"], 'abcd',
        "39% – O‘zbekiston; 30% – dunyo; 32 – 2017; 16 – 2023.")
t.VENN("1991–2016-yillar", "2016-yildan keyin",
       [("Xorazm Ma’mun akademiyasi faoliyat boshladi", 1), ("«Samarqand» kichik sayyorasi aniqlandi", 1),
        ("«El-yurt umidi» jamg‘armasi", 2), ("al-Xorazmiy matematika olimpiadasi", 2),
        ("Fanlar akademiyasi ilmiy tadqiqotlari", 3)],
       "1991–2016 – Ma’mun akademiyasi (1997), sayyora (2007); keyin – El-yurt umidi, olimpiada; ikkalasi – akademiya tadqiqotlari.")
t.MAPN('uzb', ['Urganch', 'Samarqand', 'Toshkent', 'Buxoro'], "2018-yilda ilk bor al-Xorazmiy nomidagi xalqaro matematika olimpiadasi o‘tkazilgan shahar xaritada qaysi raqamda?",
       "Urganch.")

# 12-mavzu. Jismoniy tarbiya va sport
t = Topic('y11u12', 11012); TOPICS['y11u12'] = t
t.B("O‘zbekiston FIFAga qachon a’zo bo‘lgan?", "1994-yilda", "1992-yilda", "1998-yilda", "2003-yilda", "1994-yilda.")
t.B("Mamlakat ichki futbol chempionatiga qachon start berilgan?", "1992-yildan", "1994-yildan", "1991-yildan", "2000-yildan", "1992-yildan.")
t.B("Maktablarda o‘tkazilgan sport bellashuvlari qaysi?", "«Alpomish» va «Barchinoy»", "«Umid nihollari» va «Universiada»", "«Sabanto‘y» va «Sayil»", "«Barkamol avlod» va «Kurash»", "«Alpomish» va «Barchinoy».")
t.B("Rustam Qosimjonov shaxmat bo‘yicha jahon chempioni bo‘lgan musobaqa qayerda o‘tgan?", "Tripolida (Liviya)", "Varshavada", "Chennayda", "Toshkentda", "2004-yil 13-iyul, Tripoli.")
t.B("2022-yilgi 44-jahon shaxmat olimpiadasida O‘zbekiston finalda qaysi jamoani yengdi?", "Niderlandiya", "Hindiston", "Xitoy", "AQSH", "Niderlandiya jamoasini.")
t.B("Nodirbek Abdusattorov tezkor shaxmat bo‘yicha jahon chempioni bo‘lgan shahar qaysi?", "Varshava", "Tripoli", "Chennay", "Parij", "2021-yil, Varshava (Polsha).")
t.B("O‘zbekiston tarixida ayollar o‘rtasida birinchi xalqaro grossmeyster kim?", "Nafisa Mo‘minova", "Oksana Chusovitina", "Diyora Keldiyorova", "Lina Cheryazova", "2013-yil, Nafisa Mo‘minova.")
t.B("O‘zbekistonning birinchi olimpiada oltin medalini kim qo‘lga kiritgan?", "Lina Cheryazova", "Muhammadqodir Abdullayev", "Oksana Chusovitina", "Hasanboy Do‘smatov", "1994-yil qishki Olimpiada, Lina Cheryazova.")
t.B("Sidney Olimpiadasida oltin medal olgan bokschi kim?", "Muhammadqodir Abdullayev", "Bahodir Jalolov", "Ruslan Chagayev", "Fazliddin G‘oibnazarov", "Muhammadqodir Abdullayev.")
t.B("Parij-2024 Olimpiadasida O‘zbekiston nechta oltin medal oldi?", "8 ta", "13 ta", "10 ta", "5 ta", "8 ta oltin, jami 13 ta medal.")
t.B("Parij-2024 Olimpiadasida O‘zbekiston nechanchi o‘rinni egalladi?", "13-o‘rin", "8-o‘rin", "16-o‘rin", "21-o‘rin", "206 mamlakat orasida 13-o‘rin.")
t.B("Olimpiadada 8 marta ishtirok etib, Ginnes rekordlar kitobiga kirgan gimnastikachi kim?", "Oksana Chusovitina", "Lina Cheryazova", "Nafisa Mo‘minova", "Asila Mirzayorova", "Oksana Chusovitina (1992–2020).")
t.B("Milliy paralimpiya qo‘mitasi qachon tashkil etilgan?", "2007-yilda", "2004-yilda", "2012-yilda", "1998-yilda", "2007-yilda.")
t.B("O‘zbekistonning ilk paralimpiya medalini kim qo‘lga kiritgan?", "Sharif Xalilov", "Husniddin Norbekov", "Boburjon Omonov", "Nozimaxon Qayumova", "2012-yil London, paradzyudo, kumush.")
t.B("Parij-2024 Paralimpiya o‘yinlarida O‘zbekiston jami nechta medal oldi?", "26 ta", "19 ta", "13 ta", "10 ta", "26 ta (10 oltin, 9 kumush, 7 bronza).")
t.B("Kurash xalqaro assotsiatsiyasi qachon tuzilgan?", "1998-yilda", "1999-yilda", "2003-yilda", "1994-yilda", "1998-yilda.")
t.B("Kurash bo‘yicha 1-jahon chempionati qayerda o‘tkazilgan?", "Toshkentda", "Antaliyada", "Kuvaytda", "Samarqandda", "1999-yil, Toshkent, 48 mamlakat.")
t.B("O‘zbek kurashi qachon Osiyo o‘yinlari dasturiga kiritilgan?", "2003-yilda", "1999-yilda", "2000-yilda", "1998-yilda", "2003-yil, Kuvayt, OOK XXII Bosh assambleyasi.")
t.B("2025-yilda Toshkentdagi Olimpiya shaharchasida necha o‘rinli stadion bor?", "12 ming", "5 ming", "15 ming", "50 ming", "12 ming o‘rinli.")
t.NAT("2023-yilda Toshkentda boks bo‘yicha jahon chempionati o‘tkazildi.", "O‘zbekiston 9 ta medal (5 oltin) bilan umumjamoa hisobida 1-o‘rinni egalladi", "O‘zbekiston medalsiz qoldi", "chempionat bekor qilindi", "O‘zbekiston 13-o‘rinni oldi", "1-o‘rin.")
t.NAT("2003-yilda o‘zbek kurashi Osiyo o‘yinlari dasturiga kiritildi.", "«chala», «dakki», «halol» kabi so‘zlar xalqaro sport atamalari bo‘ldi", "kurash taqiqlandi", "atamalar ingliz tiliga o‘zgartirildi", "kurash Olimpiadadan chiqarildi", "O‘zbek atamalari xalqaro bo‘ldi.")
t.NAT("2025-yilda 17 yoshgacha futbolchilar Osiyo chempionati finalida 9 kishi bo‘lib o‘ynadi.", "Saudiya Arabistonini 2:0 hisobida yengib, qit‘a chempioni bo‘ldi", "finalda yutqazdi", "o‘yindan chetlatildi", "durang o‘ynadi", "Qit‘a chempioni.")
t.NAT("2025-yilda O‘zbekiston terma jamoasi saralash o‘yinlarida muvaffaqiyat qozondi.", "tarixda ilk bor 2026-yilgi jahon chempionati final bosqichi yo‘llanmasini oldi", "yana saralashda qoldi", "FIFAdan chiqarildi", "Osiyo kubogini bekor qildi", "2026 JCh yo‘llanmasi.")
t.TF("1994-yilda O‘zbekiston futbol terma jamoasi yozgi Osiyo o‘yinlarida chempion bo‘lgan.", True, "To‘g‘ri, Yaponiyada (Xirosima).")
t.TF("Diyora Keldiyorova Parij-2024 Olimpiadasida boks bo‘yicha oltin medal olgan.", False, "Noto‘g‘ri: dzyudo bo‘yicha.")
t.TF4([("Rio-2016 da Hasanboy Do‘smatov, Shahobiddin Zoirov va Fazliddin G‘oibnazarov oltin olgan.", True), ("2018-yilda U-23 terma jamoasi Xitoyda Osiyo chempioni bo‘lgan.", True),
       ("Husniddin Norbekov 2016, 2020 va 2024 Paralimpiya chempioni.", True), ("O‘zbekiston ilk bor 2008-yilda Paralimpiyada mustaqil qatnashgan.", False)],
      "4-noto‘g‘ri: 2004-yil Afinada.")
t.MUL([("Nozimaxon Qayumova nayza uloqtirish bo‘yicha ikki karra paralimpiya chempioni.", True),
       ("Boburjon Omonov yadro uloqtirishda paralimpiya rekordini yangilagan.", True),
       ("Toshkentda Lina Cheryazova nomidagi gimnastika maktabi ochilgan.", False)],
      "III noto‘g‘ri: Oksana Chusovitina nomidagi sport maktabi ochilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["FIFAga a’zolik va Lina Cheryazova oltini", "Kurash xalqaro assotsiatsiyasi tuzildi", "Toshkentda kurash bo‘yicha 1-jahon chempionati", "kurash Osiyo o‘yinlari dasturiga kiritildi", "R. Qosimjonov jahon chempioni", "Milliy paralimpiya qo‘mitasi"],
      "1994 → 1998 → 1999 → 2003 → 2004 → 2007.")
t.MATCH("Sportchilarni sport turi bilan moslashtiring.", ["Lina Cheryazova", "Oksana Chusovitina", "Diyora Keldiyorova", "Nafisa Mo‘minova"],
        ["fristayl (qishki Olimpiada)", "sport gimnastikasi", "dzyudo", "shaxmat", "boks"], 'abcd',
        "Cheryazova – qishki Olimpiada; Chusovitina – gimnastika; Keldiyorova – dzyudo; Mo‘minova – shaxmat.")
t.VENN("Olimpiada", "Paralimpiada",
       [("Lina Cheryazova – birinchi oltin", 1), ("Parij-2024 da 8 ta oltin", 1),
        ("Sharif Xalilov – ilk medal", 2), ("Parij-2024 da 26 ta medal", 2),
        ("Parij-2024 da 13-o‘rin", 3)],
       "Ikkala o‘yinda ham Parij-2024 da O‘zbekiston 13-o‘rinni egallagan.")
t.MAPMATCH('uzb', ['Qo‘qon', 'Buxoro', 'Namangan', 'Toshkent'],
           ["Nafisa Mo‘minova tug‘ilgan shahar", "Oksana Chusovitina tug‘ilgan shahar", "Nozimaxon Qayumova tug‘ilgan viloyat markazi", "2025-yilda Olimpiya shaharchasi bunyod etilgan shahar"],
           "1 – Qo‘qon; 2 – Buxoro; 3 – Namangan; 4 – Toshkent.")

# 13-mavzu. Yoshlarga oid davlat siyosati
t = Topic('y11u13', 11013); TOPICS['y11u13'] = t
t.B("Milliy qonunchiligimizda necha yoshdagi shaxslar yoshlar hisoblanadi?", "14 yoshdan 30 yoshgacha", "17 yoshdan 25 yoshgacha", "13 yoshdan 29 yoshgacha", "10 yoshdan 30 yoshgacha", "14 yosh to‘lgan va 30 yoshdan oshmagan.")
t.B("YUNESKO me’yorlariga ko‘ra necha yoshlilar yoshlar hisoblanadi?", "17–25 yoshlilar", "14–30 yoshlilar", "13–29 yoshlilar", "10–14 yoshlilar", "17–25 yosh.")
t.B("O‘zbekiston aholisining qancha qismini yoshlar tashkil etadi?", "60 foizini", "30 foizini", "40 foizini", "80 foizini", "60 foizini.")
t.B("Zulfiya nomidagi davlat mukofoti qachon ta’sis etilgan?", "1999-yilda", "1991-yilda", "2001-yilda", "2017-yilda", "1999-yilda.")
t.B("1999–2020-yillarda Zulfiya mukofoti bilan necha nafar qiz taqdirlangan?", "322 nafar", "8 ming", "60 nafar", "1000 nafar", "322 nafar.")
t.B("2014–2020-yillarda nechtadan ortiq yosh oila imtiyozli uy-joy bilan ta’minlangan?", "8 mingdan", "322 dan", "80 mingdan", "800 dan", "8 mingdan ortiq.")
t.B("Yoshlar akademiyasi qaysi tashkilot huzurida tashkil etilgan?", "Innovatsion rivojlanish agentligi", "Oliy Majlis Senati", "Fanlar akademiyasi", "Yoshlar ishlari agentligi", "Innovatsion rivojlanish agentligi huzurida.")
t.B("Yoshlar kunini nishonlash tashabbusi qachon ilgari surilgan?", "2017-yil 30-iyunda", "1991-yilda", "2016-yilda", "2020-yilda", "2017-yil 30-iyun.")
t.B("1996-yilda Yoshlar ittifoqi o‘rniga nima tashkil etilgan?", "«Kamolot» jamg‘armasi", "Yoshlar ishlari agentligi", "«Kamalak» tashkiloti", "Yoshlar parlamenti", "«Kamolot» jamg‘armasi.")
t.B("«Kamalak» tashkiloti necha yoshli bolalar uchun tuzilgan?", "10–14 yoshli", "14–30 yoshli", "6–10 yoshli", "17–25 yoshli", "10–14 yoshli.")
t.B("«Yoshlarga oid davlat siyosati to‘g‘risida»gi qonun qachon yangi tahrirda qabul qilingan?", "2016-yilda", "2017-yilda", "2020-yilda", "1991-yilda", "2016-yilda.")
t.B("Yoshlar ishlari agentligi qachon tashkil etilgan?", "2020-yilda", "2017-yilda", "2016-yilda", "2001-yilda", "2020-yilda.")
t.B("«Yosh kitobxon» tanlovi g‘olibiga bosh sovrin sifatida nima beriladi?", "avtomobil", "uy-joy", "pul mukofoti", "kompyuter", "Avtomobil.")
t.B("Qaysi shahar 2022-yilda birinchi «Turkiy dunyo yoshlar tashabbuslari poytaxti» deb e’lon qilingan?", "Buxoro", "Toshkent", "Samarqand", "Xiva", "Buxoro.")
t.B("2024-yilda qaysi shahar birinchi «MDH yoshlar poytaxti» bo‘lgan?", "Toshkent", "Buxoro", "Samarqand", "Nukus", "Toshkent.")
t.B("Navro‘z umumxalq bayrami deb qachon e’lon qilingan?", "1990-yil 3-mayda", "1991-yil 20-iyunda", "1992-yil 27-martda", "1999-yil 2-martda", "1990-yil 3-may.")
t.B("9-may qachon Xotira va qadrlash kuni deb e’lon qilingan?", "1999-yil 2-martda", "1990-yil 3-mayda", "2020-yil 9-mayda", "1996-yil 18-oktyabrda", "1999-yil 2-mart.")
t.NAT("Yoshlar ittifoqi yoshlarning manfaatlari va ehtiyojlarini to‘la aks ettira olmadi.", "1996-yilda tugatilib, o‘rniga «Kamolot» jamg‘armasi tashkil etildi", "ittifoq kengaytirildi", "Yoshlar ishlari agentligi tuzildi", "barcha yoshlar tashkilotlari taqiqlandi", "«Kamolot» jamg‘armasi.")
t.NAT("2017-yil 30-iyunda «Kamolot» harakatining IV qurultoyi bo‘lib o‘tdi.", "O‘zbekiston Yoshlar ittifoqi tashkil etildi", "«Kamolot» jamg‘armasi tuzildi", "«Kamalak» tugatildi", "Yoshlar parlamenti yopildi", "Yoshlar ittifoqi.")
t.NAT("2017-yilda Prezident BMTning 72-sessiyasida so‘zladi.", "Yoshlar huquqlari to‘g‘risidagi xalqaro konvensiyani ishlab chiqish taklif etildi", "BMTdan chiqish e’lon qilindi", "yoshlar siyosati bekor qilindi", "Yoshlar ittifoqi tugatildi", "Konvensiya taklifi.")
t.NAT("2023-yilda Yoshlar taraqqiyoti indeksi e’lon qilindi.", "O‘zbekiston yoshlar siyosatida eng tez rivojlanayotgan mamlakat deb e’tirof etildi", "O‘zbekiston oxirgi o‘rinni oldi", "indeks bekor qilindi", "yoshlar soni kamaydi", "Eng tez rivojlanayotgan mamlakat.")
t.TF("O‘zbekiston Yoshlar ittifoqi rahbari ayni vaqtda Prezidentning yoshlar siyosati bo‘yicha davlat maslahatchisi hisoblanadi.", True, "To‘g‘ri, u Senat a’zosi etib ham tayinlanadi.")
t.TF("«Yosh kitobxon» tanlovida faqat 14–18 yoshli o‘quvchilar qatnashadi.", False, "Noto‘g‘ri: 10 yoshdan 30 yoshgacha.")
t.TF4([("«Bunyodkor» yoshlar mehnat harakatini «Kamolot» tuzgan.", True), ("2025-yilda O‘zbekiston «Yoshlar – 2030» strategiyasini amalga oshirayotgan 10 davlat qatoriga kirdi.", True),
       ("Senatda Yoshlar, madaniyat va sport masalalari qo‘mitasi tuzilgan.", True), ("«Kamolot» yoshlar ijtimoiy harakati 1991-yilda ta’sis etilgan.", False)],
      "4-noto‘g‘ri: 2001-yilda ta’sis etilgan.")
t.MUL([("Oliy Majlis palatalari huzurida Yoshlar parlamenti tashkil etildi.", True),
       ("Yoshlar press-klubi faoliyati yo‘lga qo‘yildi.", True),
       ("Ramazon hayiti 1990-yil 3-mayda bayram deb e’lon qilingan.", False)],
      "III noto‘g‘ri: 1992-yil 27-martda.")
t.CHR("Yoshlar tashkilotlarini paydo bo‘lish tartibida joylashtiring.", ["Yoshlar ittifoqi (birinchi)", "«Kamolot» jamg‘armasi", "«Kamolot» yoshlar ijtimoiy harakati", "O‘zbekiston Yoshlar ittifoqi", "Yoshlar ishlari agentligi"],
      "1991 → 1996 → 2001 → 2017 → 2020.")
t.MATCH("Sanalarni voqealar bilan moslashtiring.", ["1991-yil 20-iyun", "1996-yil 18-oktyabr", "2020-yil 9-may", "2024-yil 1-yanvar"],
        ["Qurbon hayiti dam olish kuni deb e’lon qilindi", "Temuriylar tarixi davlat muzeyi ochildi", "«G‘alaba bog‘i» majmuasi ochildi", "«Jadid» gazetasining ilk soni", "Navro‘z bayram deb e’lon qilindi"], 'abcd',
        "1991 – Qurbon hayiti; 1996 – Temuriylar muzeyi; 2020 – G‘alaba bog‘i; 2024 – «Jadid».")
t.VENN("«Kamolot» harakati", "Yoshlar ishlari agentligi",
       [("«Kamalak» tashkiloti", 1), ("«Bunyodkor» mehnat harakati", 1),
        ("«Yosh kitobxon» tanlovi", 2), ("yagona davlat yoshlar siyosatini yuritish", 2),
        ("yoshlar manfaatlarini himoya qilish", 3)],
       "Kamolot – Kamalak, Bunyodkor; Agentlik – Yosh kitobxon, davlat siyosati; ikkalasi yoshlar manfaati uchun.")
t.MAPN('uzb', ['Buxoro', 'Samarqand', 'Nukus', 'Andijon'], "2022-yilda birinchi «Turkiy dunyo yoshlar tashabbuslari poytaxti» deb e’lon qilingan shahar xaritada qaysi raqamda?",
       "Buxoro.")
