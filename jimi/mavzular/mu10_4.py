from qlib import Topic, PLACES, REG
TOPICS = {}
CA = 'ca'
PLACES.update({'Chirchiq': (69.58, 41.47), 'Vobkent': (64.52, 40.03), 'Denov': (67.9, 38.27), 'Quva': (72.07, 40.52)})

# 11-§. Kollektivlashtirish va quloqlarning surgun qilinishi
t = Topic('e10u11', 10111); TOPICS['e10u11'] = t
t.B("Yer-suv islohotining ikkinchi bosqichi qaysi yillarda amalga oshirildi?", "1925 – 1929-yillarda", "1921 – 1922-yillarda", "1930 – 1932-yillarda", "1929 – 1935-yillarda", "Chegaralanishdan so‘ng 1925 – 1929-yillarda.")
t.B("“Agrar inqilob”ning strategiya va taktikasi qaysi syezdda tasdiqlandi?", "O‘zbekiston Kompartiyasining II syezdida (1925-yil noyabr)", "VKP(b) XIV syezdida", "O‘zbekiston Kompartiyasining I syezdida", "RKP(b) X syezdida", "O‘zKP II syezdi (1925-yil noyabr).")
t.B("Yer-suv islohotining ikkinchi bosqichi qaysi dekretlar bilan boshlandi?", "O‘zSSR MIKning 1925-yil 2-dekabrdagi dekretlari", "Lenin imzolagan yer to‘g‘risidagi dekret", "1930-yil 17-fevraldagi qaror", "1927-yil 8-yanvardagi qaror", "1925-yil 2-dekabrdagi suv va yer-suv islohoti to‘g‘risidagi dekretlar.")
t.B("Islohotning birinchi bosqichi (1925 – 1926) qaysi viloyatlarda o‘tkazildi?", "Farg‘ona, Toshkent, Samarqand", "Zarafshon viloyatida", "Qashqadaryo, Surxondaryo, Xorazm", "Xorazm va Qoraqalpog‘istonda", "Farg‘ona, Toshkent, Samarqand viloyatlarida.")
t.B("Islohotning uchinchi bosqichi (1928 – 1929) qaysi hududlarda o‘tkazildi?", "Qashqadaryo, Surxondaryo, Xorazm okruglarida", "Farg‘ona, Toshkent, Samarqand viloyatlarida", "Buxoro va O‘rta Zarafshon okruglarida", "Toshkent va Xo‘jand okruglarida", "Qashqadaryo, Surxondaryo, Xorazm okruglarida.")
t.B("Farg‘ona viloyatida necha desyatina va undan ortiq sug‘oriladigan yeri bor xo‘jaliklar tugatilishi kerak edi?", "40 desyatina", "50 desyatina", "10 desyatina", "100 desyatina", "Farg‘onada 40, Toshkent va Samarqandda 50 desyatina.")
t.B("1925 – 1929-yillardagi islohotlar natijasida nechaga yaqin boy xo‘jaliklar tugatildi?", "5000 ga yaqin", "23 000 dan ortiq", "1000 ga yaqin", "60 000", "5000 ga yaqin boy xo‘jalik tugatildi.")
t.B("O‘zKP MKning “Kollektivlashtirish va quloq xo‘jaliklarini tugatish to‘g‘risida”gi qarori qachon qabul qilindi?", "1930-yil 17-fevralda", "1930-yil 26-yanvarda", "1925-yil 2-dekabrda", "1932-yilda", "1930-yil 17-fevralda.")
t.B("1930-yili O‘zbekistonda Markaz tomonidan nechta yalpi kollektivlashtiriladigan tuman belgilandi?", "19 ta", "17 ta", "60 ta", "240 ta", "19 ta tuman.")
t.B("O‘zbekiston qishloq xo‘jaligini kollektivlashtirish rasman qachon tugallandi?", "1932-yili", "1930-yili", "1939-yili", "1935-yili", "1932-yili; dehqon xo‘jaliklarining 75 foizi birlashdi.")
t.B("1939-yilga kelib O‘zbekistonda qaysi xo‘jaliklarga butkul barham berildi?", "yakka dehqon xo‘jaliklariga", "kolxozlarga", "sovxozlarga", "artellarga", "1939-yilga kelib yakka dehqon xo‘jaliklari tugatildi.")
t.B("1930-yili qoramollar miqdori qancha kamayib ketdi?", "60 000 boshdan ziyod", "5000 bosh", "1 mln bosh", "23 000 bosh", "60 000 boshdan ziyodga kamaydi.")
t.B("Respublikada quloqlar uchun nechta majburiy mehnat posyolkasi tashkil qilindi?", "17 ta", "19 ta", "14 ta", "240 ta", "17 ta majburiy mehnat posyolkasi.")
t.B("1930-yil boshlarida Qashqadaryo okrugida dehqonlarning nechta norozilik chiqishi bo‘ldi?", "14 ta", "240 ta", "17 ta", "2000 ta", "14 ta chiqish, 3700 kishi qatnashgan.")
t.B("1933-yili O‘zbekistonda surgun qilingan quloq xo‘jaliklari soni qanchaga yetdi?", "5500 tagacha", "3871 ta", "1152 ta", "23 000 ta", "1933-yili 5500 tagacha yetgan.")
t.B("1 funt necha grammga teng?", "410 g", "1638 g", "100 g", "500 g", "1 funt – 410 g.")
t.B("“Natsionalizatsiya” nimani anglatadi?", "xususiy mulkni davlat ixtiyoriga olish", "yerlarni dehqonlarga bo‘lib berish", "mayda xo‘jaliklarni birlashtirish", "aholini ko‘chirish", "Xususiy mulkni davlat ixtiyoriga olish.")
t.NAT("NEP davrida xo‘jaligini tiklab olgan xo‘jaliklar quloq qilindi.", "1929-yili sovet jamiyatida bozor munosabatlari muhiti barham topdi", "qishloq xo‘jaligi gullab-yashnadi", "dehqonlar boyib ketdi", "kolxozlar tarqatildi", "Bozor munosabatlari muhiti 1929-yili barham topdi.")
t.NAT("Kollektivlashtirish va quloqlashtirish siyosati dehqonlarning noroziligini kuchaytirdi.", "1930-yil martda O‘zSSRda 240 ta qurolli chiqish qayd etildi", "kollektivlashtirish to‘xtatildi", "quloqlar qayta yer oldi", "Qo‘shchi ittifoqi tarqatildi", "1930-yil martda O‘zSSRda 240 ta, SSSRda 2000 dan ortiq qurolli chiqish.")
t.TF("Quloq deb ro‘yxatga olinganlarning oilalari Ukraina, Shimoliy Kavkaz, Sibir, Qozog‘iston, Uzoq Sharqqa surgun qilingan.", True, "To‘g‘ri.")
t.TF("Kolxozdan tashqarida qolgan yakka xo‘jaliklardan davlatga topshiriladigan mahsulot hajmi kolxozlarga nisbatan kamaytirildi.", False, "Noto‘g‘ri: 50 foizga ko‘paytirildi.")
t.MUL([("O‘zbekistonda boy xo‘jaliklar ikki toifaga bo‘lingan.", True),
       ("1932-yili respublikada 60 dan ziyod sovxoz bor edi.", True),
       ("Quloqlikka tortilganlarning yurtga qaytish jarayoni 1956 – 1970-yillarni o‘z ichiga oladi.", False)],
      "III noto‘g‘ri: bu jarayon taxminan 1934 – 1956-yillarni o‘z ichiga oladi.")
t.MATCH("Yer-suv islohoti bosqichlarini davrlari bilan moslashtiring.", ["Birinchi bosqich", "Ikkinchi bosqich", "Uchinchi bosqich"],
        ["1927-yil", "1928 – 1929-yillar", "1925 – 1926-yillar"], "cab",
        "Birinchi – 1925 – 1926; ikkinchi – 1927; uchinchi – 1928 – 1929.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["Yer-suv islohoti to‘g‘risidagi dekretlar", "VKP(b) MK Siyosiy byurosining quloq xo‘jaliklarini tugatish to‘g‘risidagi qarori", "O‘zKP MKning kollektivlashtirish to‘g‘risidagi qarori",
       "Kollektivlashtirishning rasman tugallanishi", "Yakka dehqon xo‘jaliklariga butkul barham berilishi"],
      "1925-yil 2-dekabr → 1930-yil 26-yanvar → 1930-yil 17-fevral → 1932-yil → 1939-yil.")
t.MAPN('uzb', ['G‘ijduvon', 'Toshkent', 'Xiva', 'Termiz'], "Quloqlar uchun majburiy mehnat posyolkalari tuzilgan tumanlardan biri qaysi raqam bilan belgilangan?",
       "Posyolkalar Qo‘qon, Chust-Pop, Oqdaryo, G‘ijduvon, Vobkent, Denov, Quva va boshqa tumanlarda tuzilgan.")
t.VENN("Yer-suv islohoti II bosqichi (1925 – 1929)", "Yalpi kollektivlashtirish (1930 – 1932)",
       [("katta yer egalarining xo‘jaliklari tugatilgan", 1), ("uch bosqichda o‘tkazilgan", 1),
        ("dehqon xo‘jaliklarining 75 foizi kolxoz va sovxozlarga birlashgan", 2), ("19 ta tuman yalpi kollektivlashtirishga belgilangan", 2),
        ("o‘ziga to‘q dehqon xo‘jaliklariga zarba bergan", 3)],
       "Islohot – katta yer egaliklarini tugatish, 3 bosqich; kollektivlashtirish – 75 %, 19 tuman; ikkalasi o‘ziga to‘q xo‘jaliklarga zarba bergan.")

# 12-§. Industrlashtirish va kadrlar masalasi
t = Topic('e10u12', 10112); TOPICS['e10u12'] = t
t.B("Sotsialistik industrlashtirishga o‘tish qaysi syezdda e’lon qilindi?", "VKP(b) XIV syezdida (1925-yil dekabr)", "RKP(b) X syezdida", "O‘zKP II syezdida", "O‘zKP III syezdida", "1925-yil dekabrdagi VKP(b) XIV syezdida.")
t.B("1927-yilda O‘zSSR xalq xo‘jaligida qishloq xo‘jaligining salmog‘i qancha edi?", "62,6 %", "37,4 %", "90 %", "75 %", "Qishloq xo‘jaligi 62,6 %, sanoat 37,4 %.")
t.B("O‘sha davrda sanoat ishlab chiqarishining necha foizi qishloq xo‘jaligi xomashyosini qayta ishlashga asoslangan edi?", "90 foizi", "62,6 foizi", "37,4 foizi", "50 foizi", "90 foizi.")
t.B("Birinchi besh yillik reja qachon boshlandi?", "1928-yil oktyabrda", "1925-yil dekabrda", "1932-yil dekabrda", "1927-yil yanvarda", "1928-yil oktyabrda boshlanib, 1932-yil dekabrda yakunlandi.")
t.B("Birinchi besh yillik reja muddatidan necha oy oldin yakunlandi?", "9 oy", "6 oy", "1 yil", "3 oy", "Muddatidan 9 oy oldin.")
t.B("Birinchi besh yillikda O‘zbekistonda nechta yangi sanoat korxonasi qurildi?", "289 ta", "79 ta", "482 ta", "60 ta", "289 ta yangi korxona qurildi, 79 tasi qayta tashkil etildi.")
t.B("O‘rta Osiyoda paxtachilik mashinasozligining to‘ng‘ichi bo‘lgan korxona qaysi?", "Toshkent qishloq xo‘jaligi mashinasozligi zavodi", "Chirchiq elektr kimyo kombinati", "Toshkent to‘qimachilik kombinati", "Chirchiq-Bo‘zsuv GESlari", "Toshkent qishloq xo‘jaligi mashinasozligi zavodi.")
t.B("XX asr 30-yillarida qaysi GESlar kaskadi barpo etildi?", "Chirchiq-Bo‘zsuv", "Farhod", "Norak", "Chorvoq", "Chirchiq-Bo‘zsuv GESlar kaskadi.")
t.B("“Davlat apparatini mahalliylashtirish Markaziy komissiyasi” qachon tuzildi?", "1925-yil 3-martda", "1927-yil 8-yanvarda", "1928-yil 18-fevralda", "1931-yil 11-dekabrda", "1925-yil 3-martda O‘zSSR MIK huzurida.")
t.B("Mahalliylashtirish Markaziy komissiyasiga kim raislik qildi?", "Bobon Mavlonbekov", "Fayzulla Xo‘jayev", "Akmal Ikromov", "Rahim Inog‘omov", "Bobon Mavlonbekov raisligida.")
t.B("O‘zbekiston Kommunistik partiyasining II syezdi qachon va qayerda bo‘ldi?", "1925-yil 22 – 30-noyabrda Samarqandda", "1925-yil 6 – 12-fevralda Buxoroda", "1927-yil 16 – 24-noyabrda Samarqandda", "1925-yil dekabrda Moskvada", "1925-yil 22 – 30-noyabrda Samarqandda.")
t.B("Mahalliylashtirish komissiyasi qachon “O‘zbeklashtirish Markaziy komissiyasi” deb qayta nomlandi?", "1927-yil 8-yanvarda", "1927-yil 6-iyunda", "1928-yil 18-fevralda", "1925-yil 3-martda", "1927-yil 8-yanvarda.")
t.B("O‘zbeklashtirish Markaziy komissiyasining Nizomi qachon kuchga kirdi?", "1927-yil 6-iyunda", "1927-yil 8-yanvarda", "1928-yil 18-fevralda", "1929-yilda", "1927-yil 6-iyunda.")
t.B("O‘zSSR MIK va XKSning “Davlat apparatini o‘zbeklashtirish to‘g‘risida”gi qo‘shma qarori qachon qabul qilindi?", "1928-yil 18-fevralda", "1927-yil 6-iyunda", "1931-yil 11-dekabrda", "1925-yil 3-martda", "1928-yil 18-fevralda.")
t.B("SSSR MIKning qaysi qarori bilan O‘zbeklashtirish Markaziy komissiyasi faoliyati to‘xtatildi?", "1931-yil 11-dekabrdagi qarori", "1928-yil 18-fevraldagi qarori", "1925-yil 3-martdagi qarori", "1930-yil 17-fevraldagi qarori", "1931-yil 11-dekabrdagi qaror bilan.")
t.B("Markaz mahalliylashtirish jarayonini to‘xtatib, uni qanday deb e’lon qildi?", "“burjua millatchiligi”", "“panislomizm”", "“trotskizm”", "“o‘ng og‘machilik”", "Mahalliylashtirish “burjua millatchiligi” deb e’lon qilindi.")
t.B("“GESlar kaskadi” atamasi nimani anglatadi?", "bir daryo oqimida o‘zaro bog‘langan bir nechta gidroelektrostansiya", "bir nechta daryodagi bitta GES", "issiqlik elektr stansiyalari tizimi", "suv omborlari tarmog‘i", "Bir daryo oqimidagi o‘zaro bog‘langan bir nechta GES.")
t.NAT("Industrlashtirish siyosati qishloq hisobidan amalga oshirildi, qishloq xo‘jaligi mahsulotlari xarid narxlari pasaytirildi.", "dehqonlar qashshoqlashib, oziq-ovqat muammosi keskinlashdi", "dehqonlar boyidi", "qishloq xo‘jaligi salmog‘i oshdi", "oziq-ovqat mo‘l bo‘ldi", "Dehqonlar qashshoqlashdi, oziq-ovqat muammosi keskinlashdi.")
t.NAT("1931-yil 11-dekabrda SSSR MIK “O‘zSSR apparatini o‘zbeklashtirish to‘g‘risida”gi qarorni qabul qildi.", "o‘zbeklashtirish siyosatiga zarba berilib, ruslashtirish yangi bosqichga o‘tdi", "o‘zbek tili davlat tiliga aylandi", "milliy kadrlar ko‘paydi", "O‘zSSR mustaqil bo‘ldi", "Ruslashtirish jarayoni yangi bosqichga qadam qo‘ydi.")
t.TF("Sanoat korxonalariga malakali xodimlar asosan RSFSRning markaziy shaharlaridan olib kelingan.", True, "To‘g‘ri: bu usul butun sovet davri davom ettirildi.")
t.TF("1928-yil kuzigacha xalq xo‘jaligi besh yillik rejalar asosida boshqarilgan.", False, "Noto‘g‘ri: 1928-yil kuzigacha bir yillik rejalar asosida boshqarilgan.")
t.MUL([("Mahalliylashtirish komissiyasiga Akmal Ikromov va Rahim Inog‘omov a’zo bo‘lgan.", True),
       ("O‘zbeklashtirish komissiyasi o‘zbeklar ko‘p tumanlarda ish yuritishni o‘zbek tilida olib borishi shart edi.", True),
       ("O‘zKP III syezdi 1925-yil noyabrda Samarqandda bo‘lgan.", False)],
      "III noto‘g‘ri: O‘zKP III syezdi 1927-yil 16 – 24-noyabrda bo‘lgan; 1925-yil noyabrda II syezd bo‘lgan.")
t.MATCH("Sanalarni voqealar bilan moslashtiring.", ["1925-yil 3-mart", "1927-yil 8-yanvar", "1928-yil 18-fevral", "1931-yil 11-dekabr"],
        ["O‘zbeklashtirish komissiyasi faoliyatining to‘xtatilishi", "“Davlat apparatini o‘zbeklashtirish to‘g‘risida”gi qo‘shma qaror", "komissiyaning “O‘zbeklashtirish Markaziy komissiyasi” deb nomlanishi", "Mahalliylashtirish Markaziy komissiyasining tuzilishi"],
        "dcba", "1925 – komissiya tuzildi; 1927 – nomi o‘zgardi; 1928 – qo‘shma qaror; 1931 – faoliyat to‘xtatildi.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["Mahalliylashtirish Markaziy komissiyasining tuzilishi", "VKP(b) XIV syezdi", "O‘zbeklashtirish komissiyasi Nizomining kuchga kirishi", "Birinchi besh yillikning boshlanishi", "Birinchi besh yillikning yakunlanishi"],
      "1925-yil mart → 1925-yil dekabr → 1927-yil iyun → 1928-yil oktyabr → 1932-yil dekabr.")
t.MAP1('fargona', 'Chirchiq', "Birinchi besh yilliklarda elektr kimyo kombinati qurilgan, nomi bilan GESlar kaskadi atalgan shahar qaysi?", "Chirchiq", ["Qo‘qon", "Andijon", "Namangan"],
       "Chirchiq elektr kimyo kombinati va Chirchiq-Bo‘zsuv GESlar kaskadi.")
t.VENN("Mahalliylashtirish komissiyasi (1925)", "O‘zbeklashtirish Markaziy komissiyasi (1927)",
       [("raisi – Bobon Mavlonbekov", 1), ("1925-yil 3-martda tuzilgan", 1),
        ("Nizomi 1927-yil 6-iyunda kuchga kirgan", 2), ("1931-yil 11-dekabrda faoliyati to‘xtatilgan", 2),
        ("O‘zSSR MIK huzurida faoliyat ko‘rsatgan", 3)],
       "Ikkalasi bir komissiya bo‘lib, O‘zSSR MIK huzurida ishlagan; 1927-yil nomi o‘zgartirilgan.")

# 13-§. Xotin-qizlarni ozodlikka chiqarish
t = Topic('e10u13', 10113); TOPICS['e10u13'] = t
t.B("“Hujum” kompaniyasi qachon va qayerda e’lon qilindi?", "1926-yil sentyabrda O‘rta Osiyo xotin-qizlari kengashida", "1927-yil 8-martda Toshkentda", "1926-yil dekabrda Samarqandda", "1925-yil noyabrda O‘zKP II syezdida", "1926-yil sentyabrda O‘rta Osiyo xotin-qizlari kengashida.")
t.B("“Hujum” kompaniyasini qachondan boshlashga qaror qilindi?", "1927-yil 8-martdan", "1926-yil sentyabrdan", "1926-yil dekabrdan", "1928-yil 1-maydan", "1927-yil 8-martdan.")
t.B("“Hujum”ni o‘tkazish uchun maxsus komissiyalar qachon tuzildi?", "1926-yil dekabrda", "1926-yil sentyabrda", "1927-yil 8-martda", "1927-yil yanvarda", "1926-yil dekabrda.")
t.B("1927-yil 8-martdagi mitinglarda nechadan ortiq xotin-qizlar paranjilarini gulxanda yoqdi?", "100 000 dan ortiq", "2500 dan ortiq", "5000 dan ortiq", "10 000 dan ortiq", "100 000 dan ortiq xotin-qizlar.")
t.B("1927 – 1928-yillarda “Hujum” davrida nechadan ortiq faol xotin-qizlar qurbon bo‘ldi?", "2500 dan ortiq", "100 000 dan ortiq", "814 nafar", "5000 dan ortiq", "2500 dan ortiq faol xotin-qizlar.")
t.B("Chachvon nimadan to‘qilgan?", "otning dumi qilidan", "ipak ipdan", "paxta ipidan", "jun ipdan", "Otning dumi qilidan to‘qilgan to‘r parda.")
t.B("1926-yili O‘zbekistonda nechta yirik ayollar arteli bo‘lgan?", "16 ta", "50 dan ortiq", "134 ta", "20 ta", "16 ta artel, 814 nafar ayol.")
t.B("1926-yili ayollar artellarida nechta mahalliy xotin-qiz ishlagan?", "814 nafar", "5000 nafar", "2500 nafar", "134 nafar", "814 nafar.")
t.B("1930-yilda hunarmandchilik kooperatsiyasi artellarida nechadan ko‘proq mahalliy ayollar ishlagan?", "5000 nafardan", "814 nafardan", "2500 nafardan", "100 000 nafardan", "50 dan ortiq artelda 5000 dan ko‘proq ayol.")
t.B("1939-yilda nechta xotin-qiz traktorchilar kursiga majburan jalb qilindi?", "2500 nafar", "5000 nafar", "814 nafar", "134 nafar", "1939-yilda 2500 nafar.")
t.B("1927-yili Andijondagi Eski shahar ayollar klubida nechta a’zo bo‘lgan?", "134 nafar", "814 nafar", "2500 nafar", "16 nafar", "134 nafar a’zo.")
t.B("1927-yili tuman ijroiya qo‘mitalari a’zolarining necha foizi ayollar edi?", "20 foizi", "17 foizi", "75 foizi", "50 foizi", "Tuman ijroqo‘mlarida 20 %, okrug ijroqo‘mlarida 17 %.")
t.B("O‘zSSR MIK Prezidiumi raisining o‘rinbosari bo‘lgan o‘zbek ayoli kim?", "Jahon Obidova", "Tojixon Shodiyeva", "Halima Nosirova", "Tamaraxonim", "Jahon Obidova.")
t.B("“Artel” atamasi nimani anglatadi?", "kasb-hunar egalarining jamoa bo‘lib ishlash uchun uyushmasi", "davlat xo‘jaligi", "jamoa xo‘jaligi", "ayollar klubi", "Hunarmandlarning birgalashib ishlash uyushmasi.")
t.B("XX asr 30-yillarida iste’dodi ko‘zga tashlangan o‘zbek qizlaridan biri kim?", "Halima Nosirova", "Jahon Obidova", "Tojixon Shodiyeva", "Nodira qiz", "Halima Nosirova, Tamaraxonim, Sora Eshonto‘rayeva, Mukarrama Turg‘unboyeva.")
t.NAT("Bolsheviklar xotin-qizlarni ozodlikka chiqarishni shoshilinch tezlashtirdi.", "“Hujum”ga qarshilar ayollarga zulm qilib, ko‘plab qurbonlar bo‘ldi", "barcha ayollar sanoatga jalb qilindi", "ayollar klublari yopildi", "paranji qonun bilan majburiy qilindi", "Ko‘plab xotin-qizlar o‘ldirildi, 2500 dan ortiq faol qurbon bo‘ldi.")
t.NAT("Kolxoz va sovxozlar tashkil qilingach, ayollarni traktorchilikka o‘rgatish avj oldi.", "kursni tugatganlarning ko‘pchiligi traktorchi bo‘lib ishlamadi", "barcha ayollar traktorchi bo‘ldi", "erkaklar traktorchilikdan chetlatildi", "ayollar artellari yopildi", "Ko‘pchilik traktorchi bo‘lib ishlamasdi.")
t.TF("Jahon Obidova va Tojixon Shodiyeva keyinchalik sovet hokimiyati tomonidan qatag‘on qilindi.", True, "To‘g‘ri.")
t.TF("Ayollarni ishga tayinlashda ularning sog‘lig‘i va jismoniy imkoniyatlari doimo hisobga olingan.", False, "Noto‘g‘ri: ayollar ko‘pincha og‘ir vazifalarga qo‘yilgan, bu sog‘lig‘iga shikast yetkazgan.")
t.MUL([("“Hujum”dan maqsadlardan biri ayollarni arzon ishchi kuchi sifatida foydalanish edi.", True),
       ("Xotin-qizlar dastlab hunarmandlik kooperatsiyasiga jalb qilindi.", True),
       ("Tojixon Shodiyeva O‘zSSR MIK Prezidiumi raisi lavozimini egallagan.", False)],
      "III noto‘g‘ri: Tojixon Shodiyeva Prezidium a’zosi bo‘lgan.")
t.MATCH("Raqamlarni ma’lumotlar bilan moslashtiring.", ["100 000 dan ortiq", "2500 dan ortiq", "814 nafar", "134 nafar"],
        ["1926-yili 16 ta artelda ishlagan ayollar", "1927-yil 8-martda paranjisini yoqqan ayollar", "Andijon Eski shahar ayollar klubi a’zolari", "1927 – 1928-yillarda qurbon bo‘lgan faol ayollar"],
        "bdac", "100 000 – paranji yoqqanlar; 2500 – qurbonlar; 814 – artellarda; 134 – Andijon klubi.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["“Hujum” kompaniyasining e’lon qilinishi", "“Hujum” uchun maxsus komissiyalar tuzilishi", "Ommaviy mitinglarda paranjilarning yoqilishi", "Artellarda 5000 dan ortiq ayolning ishlashi", "2500 xotin-qizning traktorchilar kursiga jalb qilinishi"],
      "1926-yil sentyabr → 1926-yil dekabr → 1927-yil 8-mart → 1930-yil → 1939-yil.")
t.MAPN('fargona', ['Andijon', 'Qo‘qon', 'Namangan', 'Toshkent'], "1927-yili Eski shahar ayollar klubida 134 nafar a’zo bo‘lgan shahar qaysi raqam bilan belgilangan?",
       "Andijondagi Eski shahar ayollar klubida 134 nafar a’zo bo‘lgan.")
t.VENN("“Hujum” harakatining ijobiy tomonlari", "“Hujum” harakatining salbiy tomonlari",
       [("ayollar klublari, kutubxonalar, bog‘chalar ochildi", 1), ("ayollar maosh olish imkoniyatiga ega bo‘ldi", 1),
        ("2500 dan ortiq faol ayol qurbon bo‘ldi", 2), ("milliy an’ana va qadriyatlarga zarba berildi", 2),
        ("ayollarni ishlab chiqarishga jalb qilish", 3)],
       "Ishlab chiqarishga jalb qilish o‘zi ijobiy bo‘lsa-da, ayollar og‘ir ishlarga qo‘yilgani salbiy oqibat berdi.")
