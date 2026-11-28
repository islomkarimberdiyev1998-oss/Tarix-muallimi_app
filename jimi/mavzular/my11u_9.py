from qlib import Topic, PLACES, REG
TOPICS = {}

# 20-mavzu. O‘zbekiston va Sharqning rivojlangan davlatlari aloqalari
t = Topic('y11u20', 11020); TOPICS['y11u20'] = t
t.B("Islom Karimov Yaponiyaga qaysi yillarda rasmiy tashrif bilan borgan?", "1994 va 2002-yillarda", "1992 va 1999-yillarda", "2004 va 2019-yillarda", "1996 va 2006-yillarda", "1994 va 2002-yillar.")
t.B("«O‘zbekiston – Yaponiya» do‘stlik jamiyati qachon ta’sis etilgan?", "1999-yilda", "1992-yilda", "2004-yilda", "2019-yilda", "1999-yil, Toshkent.")
t.B("2004-yilda Alisher Navoiy haykali qaysi universitetda o‘rnatilgan?", "Soka universitetida", "Vaseda universitetida", "Nagoya universitetida", "Sukuba universitetida", "Soka universiteti.")
t.B("Shavkat Mirziyoyev qaysi Yaponiya universitetining faxriy doktori?", "Nagoya universiteti", "Soka universiteti", "Vaseda universiteti", "Tokio universiteti", "Nagoya universiteti.")
t.B("Mirziyoyev Yaponiyaga qachon rasmiy tashrif buyurgan?", "2019-yilda", "2017-yilda", "2022-yilda", "2004-yilda", "2019-yilda.")
t.B("O‘zbekiston va Koreya Strategik sherikchilik deklaratsiyasini qachon imzolagan?", "2006-yilda", "1992-yilda", "2008-yilda", "2017-yilda", "2006-yilda.")
t.B("Koreya bilan hamkorlikda tashkil etilgan avtomobilsozlik korxonasi qaysi?", "«UzDaewoo»", "«SamKochAvto»", "«General Motors»", "«Volkswagen»", "«UzDaewoo».")
t.B("«Korean Air» 2008-yildan qaysi aeroport orqali yuk tashimoqda?", "Navoiy xalqaro aeroporti", "Toshkent xalqaro aeroporti", "Samarqand aeroporti", "Urganch aeroporti", "Navoiy.")
t.B("2023-yilda «KIA» bilan hamkorlikda qayerda avtomobil ishlab chiqarish yo‘lga qo‘yildi?", "Jizzax viloyatida", "Andijon viloyatida", "Samarqandda", "Navoiyda", "Jizzax viloyatida.")
t.B("O‘zbekiston Koreyaning nechtadan ortiq ilmiy-tadqiqot muassasasi bilan hamkorlik qiladi?", "30 dan", "10 dan", "100 dan", "300 dan", "30 dan ortiq.")
t.B("1995-yilda Toshkentda kimning nomidagi Hind madaniyati markazi tashkil etilgan?", "La’l Bahodir Shastri", "Mahatma Gandi", "Narendra Modi", "Javoharlal Neru", "La’l Bahodir Shastri.")
t.B("2017-yilda Dehlidagi qaysi universitetda o‘zbek tili va madaniyati markazi ochilgan?", "Jamiya Milliya Islamiya universitetida", "Amiti universitetida", "Sharda universitetida", "Dehli universitetida", "Jamiya Milliya Islamiya.")
t.B("2022-yilda Narendra Modi qaysi tadbir uchun O‘zbekistonga kelgan?", "SHHT sammiti", "«Sharq taronalari» festivali", "BMT sessiyasi", "«C5+1» uchrashuvi", "SHHT sammiti.")
t.B("O‘zbekiston va Turkiya Abadiy do‘stlik va hamkorlik shartnomasini qachon imzolagan?", "1996-yilda", "1992-yilda", "1999-yilda", "2018-yilda", "1996-yilda.")
t.B("1999-yilda Samarqandda qaysi qo‘shma korxona ishga tushirilgan?", "«SamKochAvto»", "«UzDaewoo»", "«KIA»", "«Hyundai»", "«SamKochAvto» (Turkiya bilan).")
t.B("2024-yilda Anqarada Mirziyoyev qaysi mukofot bilan taqdirlangan?", "«Turkiya Respublikasi nishoni»", "«Oltin Qiron»", "Nagoya faxriy doktori", "«Do‘stlik» ordeni", "«Turkiya Respublikasi nishoni».")
t.NAT("Yaponiya bilan hamkorlik yo‘lga qo‘yildi.", "Buxoro neftni qayta ishlash zavodi, Sho‘rtan gaz-kimyo majmuasi qurildi", "zavodlar yopildi", "temir yo‘llar buzildi", "aeroportlar yopildi", "Yirik loyihalar.")
t.NAT("Koreya bilan savdo aloqalari rivojlandi.", "O‘zbekiston tabiiy resurs va qishloq xo‘jaligi mahsulotlarini eksport, transport va elektron uskunalarni import qilmoqda", "savdo to‘xtatildi", "faqat import qilinmoqda", "Koreya bilan chegara yopildi", "Eksport–import.")
t.NAT("2018-yilda Mirziyoyev Hindistonga rasmiy tashrif buyurdi.", "o‘zaro munosabatlarning yangi davri boshlandi", "aloqalar uzildi", "Hind madaniyati markazi yopildi", "filiallar yopildi", "Yangi davr.")
t.NAT("2018–2022-yillarda Rejep Tayyip Erdo‘g‘an O‘zbekistonga davlat tashriflari bilan keldi.", "ikki davlat aloqalari yanada rivojlandi", "aloqalar uzildi", "SamKochAvto yopildi", "turk kompaniyalari ketdi", "Aloqalar rivojlandi.")
t.TF("O‘zbekistonda Koreyaning Inha, Adju, Puchon universitetlari faoliyat yuritadi.", True, "To‘g‘ri.")
t.TF("Toshkentdagi Seul bog‘i O‘zbekiston–Yaponiya do‘stligi ramzi.", False, "Noto‘g‘ri: Koreya bilan do‘stlik ramzi.")
t.TF4([("Yaponiyaning Sukuba universitetida o‘zbek tili o‘qitiladi.", True), ("O‘zbekistonda Amiti va Sharda universitetlari filiallari bor.", True),
       ("O‘zbekiston va Turkiya Turkiy davlatlar tashkiloti doirasida hamkorlik qiladi.", True), ("Islom Karimovga Nagoya universiteti faxriy doktori unvoni berilgan.", False)],
      "4-noto‘g‘ri: Karimovga Vaseda va Soka, Mirziyoyevga Nagoya.")
t.MUL([("Mirziyoyev «Jo‘shqin Gujarat» va «Global Janub ovozi» sammitlarida qatnashgan.", True),
       ("O‘zbekiston «Markaziy Osiyo + Yaponiya» muloqoti doirasida hamkorlik qiladi.", True),
       ("«Samsung», «LG», «Hyundai» – Yaponiya kompaniyalari.", False)],
      "III noto‘g‘ri: Koreya Respublikasi kompaniyalari.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Hind madaniyati markazi tashkil etildi", "Turkiya bilan Abadiy do‘stlik shartnomasi", "«SamKochAvto» ishga tushirildi", "Soka universitetida Navoiy haykali", "Koreya bilan Strategik sherikchilik deklaratsiyasi", "Jizzaxda KIA avtomobillari"],
      "1995 → 1996 → 1999 → 2004 → 2006 → 2023.")
t.MATCH("Hamkorlik ramzlarini davlat bilan moslashtiring.", ["Soka universitetidagi Navoiy haykali", "Seul bog‘i va Seul ko‘chasi", "La’l Bahodir Shastri markazi", "«SamKochAvto»"],
        ["Yaponiya", "Koreya Respublikasi", "Hindiston", "Turkiya", "Xitoy"], 'abcd',
        "Soka – Yaponiya; Seul bog‘i – Koreya; Shastri – Hindiston; SamKochAvto – Turkiya.")
t.VENN("O‘zbekiston – Yaponiya", "O‘zbekiston – Koreya",
       [("Sho‘rtan gaz-kimyo majmuasi", 1), ("Soka universitetidagi Navoiy haykali", 1),
        ("«UzDaewoo» korxonasi", 2), ("«Korean Air» Navoiy aeroportida", 2),
        ("1992-yilda diplomatik munosabat o‘rnatilgan", 3)],
       "Sho‘rtan, Soka – Yaponiya; UzDaewoo, Korean Air – Koreya; ikkalasi bilan 1992-yilda.")
t.MAPMATCH('uzb', ['Jizzax', 'Navoiy', 'Samarqand', 'Buxoro'],
           ["2023-yilda KIA bilan avtomobil ishlab chiqarish yo‘lga qo‘yilgan viloyat markazi", "2008-yildan «Korean Air» yuk tashiyotgan aeroport shahri", "1999-yilda «SamKochAvto» ishga tushirilgan shahar", "Yaponiya bilan neftni qayta ishlash zavodi qurilgan shahar"],
           "1 – Jizzax; 2 – Navoiy; 3 – Samarqand; 4 – Buxoro.")

# 21-mavzu. O‘zbekiston va BMT
t = Topic('y11u21', 11021); TOPICS['y11u21'] = t
t.B("BMT qachon tashkil etilgan?", "1945-yilda", "1919-yilda", "1992-yilda", "1948-yilda", "1945-yilda.")
t.B("BMT shtab-kvartirasi qayerda joylashgan?", "Nyu-Yorkda", "Jenevada", "Parijda", "Vashingtonda", "Nyu-York.")
t.B("O‘zbekiston BMTga qachon a’zo bo‘lgan?", "1992-yil 2-martda", "1991-yil 31-avgustda", "1993-yilda", "1992-yil 8-dekabrda", "1992-yil 2-mart.")
t.B("Toshkentda BMT vakolatxonasi qachon ochilgan?", "1993-yilda", "1992-yilda", "1995-yilda", "2017-yilda", "1993-yilda.")
t.B("2002-yilda O‘zbekistonga tashrif buyurgan BMT Bosh kotibi kim?", "Kofi Annan", "Pan Gi Mun", "Antoniu Guterrish", "Butros Gali", "Kofi Annan.")
t.B("Markaziy Osiyoni yadro qurolidan xoli hudud deb e’lon qilish tashabbusi qachon ilgari surilgan?", "1993-yilda BMT BAning 48-sessiyasida", "2006-yilda", "2017-yilda 72-sessiyada", "1997-yilda", "1993-yil, 48-sessiya, I. Karimov.")
t.B("Markaziy Osiyo rasman yadro qurolidan xoli hudud deb qachon e’lon qilingan?", "2006-yilda", "1993-yilda", "1997-yilda", "2018-yilda", "2006-yilda.")
t.B("Afg‘oniston muammosi bo‘yicha «6+2» muloqot guruhi qachon tuzilgan?", "1997-yilda", "1993-yilda", "2006-yilda", "2017-yilda", "1997-yilda.")
t.B("Shavkat Mirziyoyev 2017–2025-yillarda BMT Bosh Assambleyasida necha marta nutq so‘zlagan?", "besh marta", "uch marta", "o‘n marta", "bir marta", "Besh marotaba.")
t.B("Xalqaro sivilizatsiyalar o‘rtasidagi muloqot kuni qaysi sana?", "10-iyun", "16-noyabr", "18-may", "11-fevral", "10-iyun.")
t.B("BMTning Orolbo‘yi mintaqasi uchun maxsus trest fondi qachon tashkil etilgan?", "2018-yilda", "2006-yilda", "2021-yilda", "1993-yilda", "2018-yilda.")
t.B("O‘zbekiston qachon ilk bor BMT Inson huquqlari kengashi a’zosi bo‘lgan?", "2021–2023-yillarda", "2015–2017-yillarda", "1992–1994-yillarda", "2024–2026-yillarda", "2021–2023-yillar.")
t.B("YUNESKOga «insoniyat vijdoni» ta’rifini bergan kim?", "Javoharlal Neru", "Kofi Annan", "Odri Azule", "Pan Gi Mun", "Javoharlal Neru.")
t.B("O‘zbekiston YUNESKO a’zoligiga qachon qabul qilingan?", "1993-yilda", "1992-yilda", "1995-yilda", "1945-yilda", "1993-yilda.")
t.B("YUNESKO qarorgohi qayerda joylashgan?", "Parijda", "Nyu-Yorkda", "Jenevada", "Rimda", "Parij.")
t.B("YUNESKOning Markaziy Osiyo tadqiqotlari xalqaro instituti qayerda tashkil etilgan?", "Samarqandda", "Toshkentda", "Buxoroda", "Xivada", "1995-yil, Samarqand.")
t.B("2024-yilda YUNESKO hamkorligida kimning 1050 yilligi nishonlangan?", "Abu Rayhon Beruniy", "Imom Buxoriy", "Mirzo Ulug‘bek", "Ibn Sino", "Beruniy.")
t.B("2023-yilda qaysi shahar YUNESKOning «Ijodkor shaharlar tarmog‘i»ga kiritilgan?", "Buxoro", "Samarqand", "Xiva", "Marg‘ilon", "Buxoro.")
t.B("YUNESKO Bosh direktori kim?", "Odri Azule", "Antoniu Guterrish", "Kofi Annan", "Frederik Starr", "Odri Azule.")
t.NAT("1993-yilda Islom Karimov BMT Bosh Assambleyasida yadrosiz hudud tashabbusini ilgari surdi.", "uzoq jarayonlardan so‘ng 2006-yilda Markaziy Osiyo yadro qurolidan xoli hudud deb e’lon qilindi", "tashabbus rad etildi", "yadro qurollari ko‘paydi", "O‘zbekiston BMTdan chiqdi", "Yadrosiz hudud.")
t.NAT("O‘zbekiston BMTni Orol fojiasi oqibatlarini yumshatishga da’vat etdi.", "BMT Markaziy Osiyoga moliyaviy va texnik yordam berdi", "BMT muammoni e’tiborsiz qoldirdi", "Orol to‘ldi", "konferensiyalar taqiqlandi", "Moliyaviy va texnik yordam.")
t.NAT("O‘zbekiston Afg‘onistondagi mojaroni tinch hal qilishga da’vat etdi.", "1997-yilda «6+2» muloqot guruhi tuzildi", "Afg‘oniston bilan chegara ochildi", "harbiy ittifoq tuzildi", "BMT Afg‘onistonni chiqardi", "«6+2» guruhi.")
t.NAT("1997-yildan O‘zbekiston tashabbusi bilan YUNESKO hamkorligida festival o‘tkazila boshlandi.", "har ikki yilda Samarqandda «Sharq taronalari» xalqaro musiqa festivali o‘tkaziladi", "festival bekor qilindi", "faqat Toshkentda konsert bo‘ldi", "musiqa taqiqlandi", "«Sharq taronalari».")
t.TF("Usmon mus’hafi YUNESKOning «Jahon xotirasi» dasturiga kiritilgan.", True, "To‘g‘ri.")
t.TF("Mirziyoyev tashabbusi bilan BMT BAning ikkitadan kam rezolyutsiyasi qabul qilingan.", False, "Noto‘g‘ri: o‘ndan ortiq rezolyutsiya qabul qilingan.")
t.TF4([("«Shashmaqom», «Askiya», «Palov», «Lazgi» Nomoddiy madaniy meros ro‘yxatida.", True), ("YUNESKO 1945-yil 16-noyabrda tashkil topgan.", True),
       ("Pan Gi Mun 2010 va 2015-yillarda O‘zbekistonga kelgan.", True), ("Marg‘ilonda YUNESKO bilan «Ipak va ziravorlar» festivali o‘tkaziladi.", False)],
      "4-noto‘g‘ri: Marg‘ilonda «Atlas bayrami», Buxoroda «Ipak va ziravorlar».")
t.MUL([("Nyu-York va Jenevada O‘zbekistonning BMTdagi vakolatxonalari bor.", True),
       ("«Sharq taronasi», Ibn Sino, Beruniy nomidagi YUNESKO–O‘zbekiston mukofotlari ta’sis etilgan.", True),
       ("1998-yilda YUNESKO bilan Amir Temurning 660 yilligi nishonlangan.", False)],
      "III noto‘g‘ri: 1998 – Imom Buxoriyning 1225 yilligi; Temurning 660 yilligi 1996-yilda.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["O‘zbekiston BMTga a’zo bo‘ldi", "YUNESKOga a’zolik", "Samarqandda MOTXI tashkil etildi", "«6+2» muloqot guruhi", "Markaziy Osiyo yadrosiz hudud deb e’lon qilindi", "Orolbo‘yi trest fondi"],
      "1992 → 1993 → 1995 → 1997 → 2006 → 2018.")
t.MATCH("BMT Bosh kotiblarini tashrif yillari bilan moslashtiring.", ["Kofi Annan", "Pan Gi Mun", "Antoniu Guterrish", "Odri Azule"],
        ["2002-yil", "2010 va 2015-yillar", "2017 va 2024-yillar", "2019 va 2022-yillar (YUNESKO)", "1993-yil"], 'abcd',
        "Annan – 2002; Pan Gi Mun – 2010, 2015; Guterrish – 2017, 2024; Azule – 2019, 2022.")
t.VENN("BMT", "YUNESKO",
       [("Markaziy Osiyo yadrosiz hudud rezolyutsiyasi", 1), ("Orolbo‘yi trest fondi", 1),
        ("«Jahon xotirasi» dasturi", 2), ("«Ijodkor shaharlar tarmog‘i»", 2),
        ("1945-yilda tashkil topgan", 3)],
       "Rezolyutsiya, trest fondi – BMT; Jahon xotirasi, Ijodkor shaharlar – YUNESKO; ikkalasi 1945-yilda tuzilgan.")
t.MAPMATCH('uzb', ['Buxoro', 'Marg‘ilon', 'Shahrisabz', 'Toshkent'],
           ["2023-yilda «Ijodkor shaharlar tarmog‘i»ga kirgan, «Ipak va ziravorlar» festivali shahri", "«Atlas bayrami» festivali o‘tkaziladigan shahar", "Xalqaro maqom san’ati forumi o‘tkaziladigan shahar", "1993-yilda BMT vakolatxonasi ochilgan shahar"],
           "1 – Buxoro; 2 – Marg‘ilon; 3 – Shahrisabz; 4 – Toshkent.")

# 22-mavzu. Mintaqaviy tashkilotlar doirasida ko‘ptomonlama munosabatlar
t = Topic('y11u22', 11022); TOPICS['y11u22'] = t
t.B("Rossiya, Belarus va Ukraina rahbarlari hamdo‘stlik tuzish bitimini qachon imzolagan?", "1991-yil 8-dekabrda", "1991-yil 21-dekabrda", "1993-yilda", "1992-yil 2-martda", "1991-yil 8-dekabr.")
t.B("MDH qachon va qayerda tashkil etilgan?", "1991-yil 21-dekabrda Olmaotada", "1991-yil 8-dekabrda Minskda", "1993-yilda Moskvada", "1992-yilda Toshkentda", "Olmaota, 1991-yil 21-dekabr.")
t.B("MDHni nechta mustaqil davlat rahbarlari tashkil qilgan?", "o‘n bitta", "uchta", "o‘nta", "o‘n beshta", "11 ta davlat.")
t.B("MDH Ijroiya qo‘mitasining qarorgohi qayerda?", "Minskda", "Moskvada", "Olmaotada", "Kiyevda", "Minsk.")
t.B("MDH nizomi qachon qabul qilingan?", "1993-yilda Minskda", "1991-yilda Olmaotada", "2020-yilda Toshkentda", "1996-yilda Shanxayda", "1993-yil, Minsk.")
t.B("O‘zbekiston MDHga qachon raislik qilgan?", "2020-yilda", "2017-yilda", "2001-yilda", "2009-yilda", "2020-yilda.")
t.B("«Shanxay beshligi» qachon shakllangan?", "1996-yilda", "2001-yilda", "1991-yilda", "2009-yilda", "1996-yilda.")
t.B("SHHT qachon tashkil etilgan?", "2001-yilda", "1996-yilda", "2009-yilda", "2017-yilda", "2001-yil, O‘zbekiston a’zo bo‘lishi bilan.")
t.B("SHHTning rasmiy tillari qaysi?", "xitoy va rus", "ingliz va xitoy", "rus va ingliz", "xitoy va hind", "Xitoy va rus.")
t.B("SHHT qarorgohi qayerda joylashgan?", "Pekinda", "Shanxayda", "Moskvada", "Toshkentda", "Pekin.")
t.B("SHHTning Mintaqaviy aksilterror tuzilmasi qayerda faoliyat yuritadi?", "Toshkentda", "Pekinda", "Moskvada", "Ostonada", "Toshkent.")
t.B("SHHT davlatlari hududi Yevrosiyoning necha foizini tashkil qiladi?", "65 foizini", "50 foizini", "30 foizini", "80 foizini", "65 foizini.")
t.B("Hindiston va Pokiston SHHTga rasman qachon a’zo bo‘lgan?", "2017-yilda Ostona sammitida", "2016-yilda Toshkent sammitida", "2022-yilda Samarqandda", "2001-yilda Shanxayda", "2017-yil, Ostona.")
t.B("SHHTning Xalq diplomatiyasi markazi qachon tashkil etilgan?", "2018-yilda", "2016-yilda", "2022-yilda", "2009-yilda", "2018-yil, Toshkent.")
t.B("SHHTning 2022-yilgi sammiti qayerda o‘tgan?", "Samarqandda", "Toshkentda", "Tyanszinda", "Ostonada", "Samarqand.")
t.B("Turkiy tilli davlatlar kengashi qachon tashkil etilgan?", "2009-yilda", "2019-yilda", "2021-yilda", "2001-yilda", "2009-yilda.")
t.B("O‘zbekiston TDTga qachon a’zo bo‘lgan?", "2019-yilda", "2009-yilda", "2021-yilda", "2022-yilda", "2019-yilda.")
t.B("2020-yilda qaysi shahar «Turkiy dunyo madaniyati poytaxti» deb e’lon qilingan?", "Xiva", "Samarqand", "Buxoro", "Turkiston", "Xiva.")
t.B("TDT doirasidagi Alisher Navoiy nomidagi mukofot ilk bor kimga berilgan?", "Chingiz Aytmatov", "Aziz Sanjar", "Abay Qo‘nonboyev", "Maxtumquli Firog‘iy", "2022-yil, Chingiz Aytmatov.")
t.B("2025-yilda Navoiy mukofotiga sazovor bo‘lgan Nobel mukofoti sovrindori kim?", "Aziz Sanjar", "Chingiz Aytmatov", "Frederik Starr", "Odri Azule", "Turk biokimyogari Aziz Sanjar.")
t.B("2023-yilda Samarqand qanday maqom oldi?", "«Turkiy sivilizatsiya poytaxti»", "«Turkiy dunyo madaniyati poytaxti»", "«Islom madaniyati poytaxti»", "«MDH yoshlar poytaxti»", "«Turkiy sivilizatsiya poytaxti».")
t.NAT("2009-yilda O‘zbekiston SHHTga raislik qildi.", "BMT va SHHT hamkorligi to‘g‘risidagi rezolyutsiya qabul qilindi", "O‘zbekiston SHHTdan chiqdi", "SHHT tarqatildi", "Hindiston a’zo bo‘ldi", "BMT–SHHT rezolyutsiyasi.")
t.NAT("2016-yilda O‘zbekiston raisligida Toshkent sammiti o‘tdi.", "Hindiston va Pokistonning a’zo maqomini olishi bo‘yicha hujjatlar imzolandi", "SHHT tarqatildi", "Xitoy tashkilotdan chiqdi", "Eron chetlatildi", "Hindiston va Pokiston hujjatlari.")
t.NAT("2022-yilda SHHTning Samarqand sammiti o‘tkazildi.", "«Shanxay ruhi» va «Samarqand ruhi» tushunchalari uyg‘unlashtirildi", "sammit bekor qilindi", "O‘zbekiston chetlatildi", "Samarqand deklaratsiyasi rad etildi", "Ikki ruh uyg‘unlashdi.")
t.NAT("2021-yilda Mirziyoyev TDT doirasida tashabbus bildirdi.", "Alisher Navoiy nomidagi xalqaro mukofot ta’sis etildi", "TDT nomi o‘zgartirildi", "O‘zbekiston kuzatuvchi bo‘ldi", "mukofot bekor qilindi", "Navoiy mukofoti.")
t.TF("100 jildli «Turkiy adabiyot durdonalari» to‘plami o‘zbek tilida nashr qilingan.", True, "To‘g‘ri.")
t.TF("Vengriya va Turkmaniston TDTning to‘laqonli a’zolari.", False, "Noto‘g‘ri: ular kuzatuvchi a’zolar.")
t.TF4([("2025-yilda SHHTga o‘nta davlat a’zo.", True), ("Mo‘g‘uliston va Afg‘oniston SHHTda kuzatuvchi.", True),
       ("TDT ishchi tillari qatorida o‘zbek va ingliz tillari bor.", True), ("O‘zbekiston 2001–2025-yillarda SHHTga bir marta raislik qilgan.", False)],
      "4-noto‘g‘ri: to‘rt marotaba raislik qilgan.")
t.MUL([("Turkiy tilli davlatlar kengashi 2021-yilda Turkiy davlatlar tashkiloti deb nomlandi.", True),
       ("2022-yili Samarqandda TDT sammiti o‘tib, Samarqand deklaratsiyasi qabul qilindi.", True),
       ("2025-yilda TDT norasmiy sammiti Tyanszinda o‘tgan.", False)],
      "III noto‘g‘ri: Budapeshtda; Tyanszinda SHHT yig‘ilishi o‘tgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Olmaotada MDH tashkil etildi", "Minskda MDH nizomi qabul qilindi", "«Shanxay beshligi»", "SHHT tashkil etildi", "Turkiy tilli davlatlar kengashi", "O‘zbekiston TDTga a’zo bo‘ldi"],
      "1991 → 1993 → 1996 → 2001 → 2009 → 2019.")
t.MATCH("Tashkilotlarni qarorgoh yoki asos shahri bilan moslashtiring.", ["MDH Ijroiya qo‘mitasi", "SHHT qarorgohi", "SHHT Mintaqaviy aksilterror tuzilmasi", "«Shanxay beshligi» bitimi"],
        ["Minsk", "Pekin", "Toshkent", "Shanxay", "Olmaota"], 'abcd',
        "MDH – Minsk; SHHT – Pekin; aksilterror tuzilma – Toshkent; beshlik bitimi – Shanxay.")
t.VENN("SHHT", "TDT",
       [("rasmiy tillari xitoy va rus", 1), ("Mintaqaviy aksilterror tuzilmasi Toshkentda", 1),
        ("Alisher Navoiy nomidagi xalqaro mukofot", 2), ("Vengriya kuzatuvchi a’zo", 2),
        ("O‘zbekiston, Qozog‘iston va Qirg‘iziston a’zo", 3)],
       "Tillar, aksilterror – SHHT; Navoiy mukofoti, Vengriya – TDT; O‘zbekiston, Qozog‘iston, Qirg‘iziston ikkalasiga ham a’zo.")
t.MAPMATCH('eurasia2', ['Minsk', 'Olmaota', 'Shanxay', 'Budapesht'],
           ["MDH Ijroiya qo‘mitasi qarorgohi, nizom qabul qilingan shahar", "1991-yil 21-dekabrda MDH tashkil etilgan shahar", "1996-yilda «Shanxay beshligi» bitimi imzolangan shahar", "2025-yilda TDT norasmiy sammiti o‘tgan shahar"],
           "1 – Minsk; 2 – Olmaota; 3 – Shanxay; 4 – Budapesht.")
