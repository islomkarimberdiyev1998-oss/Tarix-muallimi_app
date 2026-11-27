from qlib import Topic, PLACES, REG
TOPICS = {}
CA = 'ca'
PLACES.update({'Guliston (Mirzacho‘l)': (68.78, 40.49), 'Navoiy': (65.38, 40.1), 'Gazli': (63.45, 40.13), 'Muruntov': (64.57, 41.5),
               'Uchquduq': (63.55, 42.15), 'Mo‘ynoq': (59.0, 43.77)})

# 21-§. Ziyolilarning qatag‘on qilinishi va shaxsga sig‘inishning fosh qilinishi
t = Topic('e10u21', 10121); TOPICS['e10u21'] = t
t.B("XX asr 40-yillari oxiri – 50-yillari boshidagi qatag‘onlar asosan kimlarga qarshi qaratildi?", "madaniyat va fan arboblariga", "harbiylarga", "dehqonlarga", "ruhoniylarga", "Asosan madaniyat va fan arboblariga.")
t.B("O‘zKP MK byurosi “O‘zSSR Fanlar akademiyasining ishi to‘g‘risida”gi masalani qachon ko‘rdi?", "1950-yil 1-sentyabrda", "1952-yil fevralda", "1951-yilda", "1956-yil 25-fevralda", "1950-yil 1-sentyabrda.")
t.B("1950-yilda nohaq qoralangan sharqshunos va tarixchi olim kim?", "Abdusamad Boboxo‘jayev", "Vohid Zohidov", "Olim Usmonov", "Olim Aminov", "Sharqshunos va tarixchi – Abdusamad Boboxo‘jayev.")
t.B("O‘zKP MKning mafkuraviy masalalarga bag‘ishlangan X plenumi qachon bo‘ldi?", "1952-yil fevralda", "1950-yil sentyabrda", "1953-yil martda", "1956-yil fevralda", "1952-yil fevralda.")
t.B("X plenumda “Respublikada mafkuraviy ishning ahvoli...” mavzusida kim ma’ruza qildi?", "Amin Niyozov", "Usmon Yusupov", "Nuriddin Muhitdinov", "Sobir Kamolov", "O‘zKP MK birinchi sekretari Amin Niyozov.")
t.B("X plenumdan so‘ng qaysi xalq dostonini o‘qish taqiqlandi?", "“Alpomish”", "“Go‘ro‘g‘li”", "“Kuntug‘mish”", "“Rustamxon”", "“Alpomish” dostoni.")
t.B("Said Ahmad, Shukrullo, Shayxzoda va boshqalar (12 kishi) necha yilga ozodlikdan mahrum etildi?", "25 yilga", "10 yilga", "15 yilga", "5 yilga", "1951-yilda qamoqqa olinib, 25 yilga hukm qilindi.")
t.B("1951-yilda qamalgan ijodkorlar qachon oqlanib, ozod qilindi?", "1955-yili", "1953-yili", "1956-yili", "1961-yili", "1955-yili.")
t.B("I.V.Stalin qachon vafot etdi?", "1953-yil 5-martda", "1952-yil fevralda", "1956-yil 25-fevralda", "1954-yilda", "1953-yil 5-martda.")
t.B("Stalin vafotidan so‘ng SSSR Ministrlar Soveti raisi lavozimiga kim tayinlandi?", "Georgiy Malenkov", "Nikita Xrushchev", "Leonid Brejnev", "M.Suslov", "Georgiy Malenkov.")
t.B("Shaxsga sig‘inish to‘g‘risidagi ma’ruza qachon qilindi?", "1956-yil 25-fevralda KPSS XX syezdida", "1953-yil 5-martda", "1952-yil fevralda O‘zKP X plenumida", "1955-yilda", "1956-yil 25-fevralda KPSS XX syezdining yopiq majlisida.")
t.B("KPSS XX syezdida shaxsga sig‘inish to‘g‘risida kim ma’ruza qildi?", "Nikita Xrushchev", "Georgiy Malenkov", "Leonid Brejnev", "Amin Niyozov", "KPSS MK Birinchi sekretari N.Xrushchev.")
t.B("O‘zbekiston bo‘yicha otilgan va qamoqqa olinganlardan qancha kishi oqlandi?", "40 000 nafarga yaqin", "12 nafar", "5758 nafar", "100 000 nafar", "40 000 nafarga yaqin.")
t.B("1950-yil aprelda Usmon Yusupov qaysi lavozimga tayinlandi?", "SSSR Paxtachilik ministri", "O‘zSSR Ministrlar Soveti raisi", "sovxoz direktori", "KPSS MK sekretari", "Moskvaga SSSR Paxtachilik ministri lavozimiga.")
t.B("1954-yilda Usmon Yusupov qayerga direktor qilib jo‘natildi?", "Mirzacho‘ldagi “4-Boyovut” sovxoziga", "Toshkent traktor zavodiga", "Chirchiq kimyo kombinatiga", "Bekobod metallurgiya zavodiga", "Mirzacho‘ldagi “4-Boyovut” sovxoziga.")
t.B("1955 – 1957-yillarda O‘zKP MK birinchi sekretari kim bo‘lgan?", "Nuriddin Muhitdinov", "Amin Niyozov", "Sobir Kamolov", "Sharof Rashidov", "Nuriddin Muhitdinov.")
t.B("Amin Niyozov qayerda tug‘ilgan?", "Marg‘ilonda", "Toshkentda", "Jizzaxda", "Qo‘qonda", "Marg‘ilonda tug‘ilgan.")
t.B("Sobir Kamolov respublika partiya tashkilotini necha oy boshqargan?", "15 oy", "24 oy", "6 oy", "36 oy", "Atigi 15 oy.")
t.NAT("1952-yil fevraldagi O‘zKP MK X plenumida bir guruh ziyolilar millatchilikda ayblandi.", "bu O‘zbekistonning ma’naviy hayotiga kuchli zarba bo‘ldi", "ziyolilar mukofotlandi", "“Alpomish” dostoni nashr etildi", "FA institutlari kengaytirildi", "Plenum va qarorlari ma’naviy hayotga kuchli zarba bo‘ldi.")
t.NAT("Sobir Kamolov davrida kadrlarni mahalliylashtirish va islom diniga erkinliklar berildi.", "bu Markaz rahbariyatiga yoqmay, u lavozimidan olib tashlandi", "u KPSS MK Bosh sekretari bo‘ldi", "Markaz uni mukofotladi", "u Ministrlar Soveti raisi bo‘ldi", "N.Xrushchev, M.Suslovga yoqmay, lavozimidan olindi.")
t.TF("Nuriddin Muhitdinov paxta xarid narxini oshirishni Markaz oldiga qo‘yib, buni uddaladi.", True, "To‘g‘ri; u o‘zbek ziyolilari oqlanishida ham tashabbuskor bo‘lgan.")
t.TF("Oqlash jarayonida sovet rejimi qatag‘on qilinganlarning barchasini istisnosiz oqladi.", False, "Noto‘g‘ri: o‘ziga ma’qul bo‘lgan shaxslarnigina oqladi.")
t.MUL([("Stalin 1922 – 1953-yillarda kommunistik partiya va hukumatga rahbarlik qilgan.", True),
       ("Usmon Yusupov 1953 – 1954-yillarda O‘zSSR Ministrlar Soveti raisi bo‘lgan.", True),
       ("Amin Niyozov 1947 – 1950-yillarda O‘zKP MK birinchi sekretari bo‘lgan.", False)],
      "III noto‘g‘ri: 1947 – 1950-yillarda u O‘zSSR Oliy Soveti Prezidiumi raisi, 1950 – 1955-yillarda MK birinchi sekretari bo‘lgan.")
t.MATCH("O‘zKP MK birinchi sekretarlarini faoliyat davri bilan moslashtiring.", ["Amin Niyozov", "Nuriddin Muhitdinov", "Sobir Kamolov"],
        ["1955 – 1957-yillar", "1957-yil dekabr – 1959-yil mart", "1950 – 1955-yillar"], "cab",
        "Niyozov – 1950 – 1955; Muhitdinov – 1955 – 1957; Kamolov – 1957 – 1959.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["O‘zKP MK byurosining FA ishi to‘g‘risidagi qarori", "12 nafar ijodkorning qamoqqa olinishi", "O‘zKP MK X plenumi", "Stalinning vafoti", "KPSS XX syezdi"],
      "1950-yil 1-sentyabr → 1951 → 1952-yil fevral → 1953-yil 5-mart → 1956-yil 25-fevral.")
t.MAPMATCH(CA, ['Marg‘ilon', 'Guliston (Mirzacho‘l)', 'Toshkent'],
           ["Amin Niyozov tug‘ilgan shahar", "1954-yilda Usmon Yusupov sovxoz direktori qilib jo‘natilgan hudud", "Sobir Kamolov tug‘ilgan shahar"],
           "1 – Marg‘ilon; 2 – Mirzacho‘l (Guliston); 3 – Toshkent.")
t.VENN("Amin Niyozov", "Nuriddin Muhitdinov",
       [("davrida ziyolilarga nisbatan qatag‘onchilik siyosati olib borildi", 1), ("X plenumda mafkuraviy ish to‘g‘risida ma’ruza qildi", 1),
        ("o‘zbek ziyolilari oqlanishida tashabbuskor bo‘ldi", 2), ("KPSS MK ideologiya sekretari bo‘lgan", 2),
        ("O‘zKP MK birinchi sekretari bo‘lgan", 3)],
       "Niyozov – qatag‘on, X plenum; Muhitdinov – oqlash, KPSS MK sekretari; ikkalasi O‘zKP MK birinchi sekretari bo‘lgan.")

# 22-§. Sanoatning bir tomonlama rivojlanishi
t = Topic('e10u22', 10122); TOPICS['e10u22'] = t
t.B("To‘rtinchi besh yillik qaysi yillarni o‘z ichiga olgan?", "1946 – 1950-yillar", "1951 – 1955-yillar", "1941 – 1945-yillar", "1956 – 1960-yillar", "To‘rtinchi – 1946 – 1950, beshinchi – 1951 – 1955.")
t.B("Urushdan keyingi besh yilliklarda kapital mablag‘larning aksariyati qaysi sohaga sarflandi?", "og‘ir sanoatga", "yengil sanoatga", "qishloq xo‘jaligiga", "madaniyatga", "Aksariyati og‘ir sanoatga sarflandi.")
t.B("O‘zbekistonda og‘ir sanoat asosan nimaga xizmat qilgan?", "paxtachilikni rivojlantirishga, ya’ni Markaz manfaatlariga", "aholining iste’mol mollariga", "eksportga", "turizmga", "Paxtachilikni rivojlantirishga – Markaz manfaatlariga.")
t.B("Aholi qalin yashaydigan joyda qurilib, atrof-muhitni ifloslantirgan korxonalardan biri qaysi?", "Navoiy kimyo kombinati", "Toshkent to‘qimachilik kombinati", "Tashselmash", "Toshkent aviatsiya zavodi", "Chirchiq elektrkimyo, Navoiy kimyo kombinati, Yangiyo‘l biokimyo zavodi.")
t.B("1947-yilda qurilgan Chorjo‘y – Qo‘ng‘irot temir yo‘li uzunligi qancha bo‘lgan?", "600 km", "170 km", "1000 km", "300 km", "600 km.")
t.B("Toshkentda ilk marta trolleybuslar qachon qatnay boshladi?", "1947-yilda", "1959-yilda", "1966-yilda", "1977-yilda", "1947-yilda.")
t.B("Qaysi temir yo‘l magistrali Qoraqalpog‘istonni Qozog‘iston bilan to‘g‘ri bog‘ladi?", "Qo‘ng‘irot – Beynov", "Chorjo‘y – Qo‘ng‘irot", "Toshkent – Orenburg", "Krasnovodsk – Toshkent", "Qo‘ng‘irot – Beynov temir yo‘li.")
t.B("Toshkent katta halqa avtomobil yo‘li qaysi yillarda qurildi?", "1959 – 1968-yillarda", "1947 – 1950-yillarda", "1966 – 1977-yillarda", "1951 – 1955-yillarda", "1959 – 1968-yillarda.")
t.B("XX asr 50-yillari o‘rtalaridan O‘zbekiston havo yo‘llarida qaysi samolyotlar paydo bo‘ldi?", "TU-104", "IL-86", "AN-2", "YAK-40", "TU-104 rusumli yo‘lovchi samolyotlari.")
t.B("1959-yilda respublika aholisi tarkibida o‘zbeklar salmog‘i qancha edi?", "62 foizdan ortiq", "43 foiz", "75 foiz", "50 foiz", "62 % dan ortiq; o‘zbek ishchilari esa atigi 43 %.")
t.B("1959-yilda respublika ishchilari orasida o‘zbeklar necha foizni tashkil etgan?", "43 foizni", "62 foizni", "25 foizni", "75 foizni", "Atigi 43 foiz.")
t.B("Ittifoqqa bo‘ysunadigan korxonalarda ish haqi mahalliy korxonalardagiga qaraganda necha marta ko‘p bo‘lgan?", "2 – 3 marta va undan ko‘p", "1,5 marta", "10 marta", "bir xil bo‘lgan", "2 – 3 marta va undan ham ko‘p.")
t.B("O‘zKP MK ikkinchi sekretarlari, DXK rahbarlari asosan kimlardan iborat bo‘lgan?", "Moskvadan yuborilgan vakillardan", "mahalliy millat vakillaridan", "saylangan deputatlardan", "harbiylardan", "Moskvadan yuborilgan (asosan slavyan va armanlar) vakillardan.")
t.B("Mahalliy millatdan tayinlanadigan rahbarlar nomzodini kim tavsiya qilar edi?", "Kreml", "O‘zSSR Oliy Soveti", "xalq", "kasaba uyushmalari", "Nomzodlarni Kreml tavsiya qilardi.")
t.NAT("Yirik kimyo korxonalari aholi qalin yashaydigan joylarda qurildi.", "atrof-muhit ifloslanib, ekologik vaziyat murakkablashdi", "aholining salomatligi yaxshilandi", "yengil sanoat rivojlandi", "qishloq xo‘jaligi hosildorligi oshdi", "Ekologik vaziyat murakkablashdi, eng katta zararni insonlar ko‘rdi.")
t.NAT("Temir va avtomobil yo‘llari Turkmaniston, Tojikiston, Qozog‘iston hududlaridan o‘tkazildi.", "respublikalar iqtisodiy jihatdan Markazga qaram qilib qo‘yildi", "O‘zbekiston transport mustaqilligiga erishdi", "yo‘llar qisqardi", "xalqaro savdo to‘xtadi", "Iqtisodiy jihatdan Markazga qaramlik vujudga keldi.")
t.TF("Yengil sanoatda aholini iste’mol mollari bilan ta’minlash darajasi Ittifoqqa nisbatan bir necha marta kam bo‘lgan.", True, "To‘g‘ri.")
t.TF("Temir yo‘llarni elektrlashtirish va avtomatlashtirilgan boshqaruv tizimini yaratish ishlari tez sur’atlarda olib borildi.", False, "Noto‘g‘ri: bu ishlar sekinlik bilan olib borildi.")
t.MUL([("Qo‘ng‘irot – Beynov temir yo‘li O‘rta Osiyodan Markazga olib boradigan ikkinchi poyezd yo‘lini vujudga keltirdi.", True),
       ("Sanoat qurilishida rivojlangan mamlakatlardagi yangi texnologiyalardan keng foydalanildi.", False),
       ("Yangiyo‘l biokimyo zavodi atrof-muhitni ifloslantirgan korxonalardan biri bo‘lgan.", True)],
      "II noto‘g‘ri: avvalgi ko‘rsatmalar saqlanib, yangi texnologiyalardan foydalanish ko‘zda tutilmagan.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["To‘rtinchi besh yillikning boshlanishi", "Chorjo‘y – Qo‘ng‘irot temir yo‘lining qurilishi", "Beshinchi besh yillikning boshlanishi", "Toshkent katta halqa yo‘li qurilishining boshlanishi"],
      "1946 → 1947 → 1951 → 1959.")
t.MAPN('ca2', ['Qo‘ng‘irot', 'Chorjo‘y', 'Xiva', 'Nukus'], "1947-yilda Chorjo‘y bilan temir yo‘l orqali bog‘langan, keyinchalik u yerdan Beynovga yo‘l qurilgan shahar qaysi raqam bilan belgilangan?",
       "Chorjo‘y – Qo‘ng‘irot (600 km) va Qo‘ng‘irot – Beynov temir yo‘llari.")
t.VENN("Og‘ir sanoat (1946 – 1955)", "Yengil sanoat (1946 – 1955)",
       [("kapital mablag‘larning aksariyati sarflangan", 1), ("asosan paxtachilikka xizmat qilgan", 1),
        ("ishlab chiqarish rejalari bajarilmagan", 2), ("iste’mol mollari bilan ta’minlash Ittifoqqa nisbatan bir necha marta kam", 2),
        ("Markazda ishlab chiqilgan iqtisodiy siyosat asosida rivojlangan", 3)],
       "Og‘ir sanoat – ko‘p mablag‘, paxtachilikka xizmat; yengil sanoat – rejalar bajarilmagan; ikkalasi Markaz siyosati asosida.")

# 23-§. Siyosiy hayotdagi o‘zgarishlar
t = Topic('e10u23', 10123); TOPICS['e10u23'] = t
t.B("Sharof Rashidov O‘zKP MK birinchi sekretari lavozimiga qachon saylandi?", "1959-yil 15-martda", "1957-yil dekabrda", "1966-yilda", "1977-yil 7-oktyabrda", "1959-yil 15-martda.")
t.B("Sharof Rashidov qachon va qayerda tug‘ilgan?", "1917-yil 7-noyabrda Jizzaxda", "1917-yil 7-noyabrda Samarqandda", "1910-yilda Toshkentda", "1917-yilda Qo‘qonda", "1917-yil 7-noyabrda Jizzaxda.")
t.B("Sh.Rashidov 1950 – 1959-yillarda qaysi lavozimda ishlagan?", "O‘zSSR Oliy Soveti Prezidiumi raisi", "O‘zSSR Ministrlar Soveti raisi", "O‘zKP MK ikkinchi sekretari", "SSSR Paxtachilik ministri", "O‘zSSR Oliy Soveti Prezidiumi raisi.")
t.B("Toshkent metropolitenining birinchi navbati qachon ishga tushirildi?", "1977-yil noyabrda", "1966-yilda", "1959-yilda", "1983-yilda", "1977-yil noyabrda (9 ta bekat).")
t.B("Toshkent metropolitenining birinchi navbatida nechta bekat bo‘lgan?", "9 ta", "12 ta", "6 ta", "15 ta", "9 ta bekat.")
t.B("Toshkentda kuchli zilzila qachon bo‘lgan?", "1966-yilda", "1977-yilda", "1959-yilda", "1947-yilda", "1966-yildagi zilziladan so‘ng Toshkent qayta tiklandi.")
t.B("1959 – 1970-yillarda O‘zSSR Oliy Soveti Prezidiumi raisi kim bo‘lgan?", "Yodgor Nasriddinova", "Nazar Matchonov", "Inomjon Usmonxo‘jayev", "Orif Alimov", "Yodgor Nasriddinova.")
t.B("Butun Sharqda parlament raisi bo‘lgan birinchi ayol kim?", "Yodgor Nasriddinova", "Jahon Obidova", "Tojixon Shodiyeva", "Zulfiya", "Yodgor Nasriddinova.")
t.B("Yodgor Nasriddinova qayerda tug‘ilgan?", "Qo‘qonda", "Jizzaxda", "Marg‘ilonda", "Toshkentda", "Qo‘qonda tug‘ilgan.")
t.B("Yo.Nasriddinova 1970 – 1974-yillarda qaysi lavozimda ishlagan?", "SSSR Oliy Soveti Millatlar Sovetining raisi", "O‘zSSR Ministrlar Soveti raisi", "O‘zKP MK birinchi sekretari", "KPSS MK sekretari", "SSSR Oliy Soveti Millatlar Sovetining raisi.")
t.B("1971 – 1984-yillarda O‘zSSR Ministrlar Soveti raisi kim bo‘lgan?", "Normuhammadi Xudoyberdiyev", "Rahmonqul Qurbonov", "Orif Alimov", "Nazar Matchonov", "Normuhammadi Xudoyberdiyev.")
t.B("1961 – 1971-yillarda O‘zSSR Ministrlar Soveti raisi kim edi?", "Rahmonqul Qurbonov", "Orif Alimov", "Normuhammadi Xudoyberdiyev", "Inomjon Usmonxo‘jayev", "Rahmonqul Qurbonov.")
t.B("1978 – 1983-yillarda O‘zSSR Oliy Soveti Prezidiumi raisi kim bo‘lgan?", "Inomjon Usmonxo‘jayev", "Nazar Matchonov", "Yodgor Nasriddinova", "Sharof Rashidov", "Inomjon Usmonxo‘jayev.")
t.B("SSSR Konstitutsiyasining qaysi moddasida KPSSning yetakchilik roli mustahkamlab qo‘yilgan?", "6-moddasida", "1-moddasida", "10-moddasida", "72-moddasida", "6-moddasida.")
t.B("SSSRning yangi Konstitutsiyasi qachon qabul qilindi?", "1977-yil 7-oktyabrda", "1959-yil 15-martda", "1936-yil 5-dekabrda", "1966-yilda", "1977-yil 7-oktyabrda.")
t.B("1977-yilgi SSSR Konstitutsiyasi kimning rahbarligida tayyorlandi?", "Leonid Brejnev", "Nikita Xrushchev", "Georgiy Malenkov", "Sharof Rashidov", "KPSS MK Bosh sekretari L.I.Brejnev.")
t.B("Partiya organlari bilan kelishib tayinlanadigan lavozimlar tartibi qanday atalgan?", "partiya nomenklaturasi", "partiya plenumi", "kadrlar rotatsiyasi", "partiya byurosi", "Partiya nomenklaturasi.")
t.NAT("1977-yil 7-oktyabrda SSSRning yangi Konstitutsiyasi qabul qilindi.", "milliy respublikalar huquqi rasman cheklanib, Markazga keng vakolatlar berildi", "respublikalar mustaqil bo‘ldi", "KPSSning roli bekor qilindi", "O‘zSSR SSSRdan chiqdi", "Milliy respublikalar huquqi cheklandi.")
t.NAT("Mirzacho‘l, Surxon-Sherobod va Qarshi cho‘llari o‘zlashtirildi.", "ekin maydonlari kengaydi", "ekin maydonlari qisqardi", "sanoat korxonalari yopildi", "aholi kamaydi", "Ekin maydonlari kengaygan.")
t.TF("XX asrning 60 – 80-yillarida xalqning turmush darajasi avvalgi davrlarga nisbatan yaxshilandi.", True, "To‘g‘ri: uylarda televizor, muzlatkich, avtomobillar paydo bo‘ldi.")
t.TF("Sovet davrida Sovetlar ikkinchi darajali masalalarni partiya komitetlaridan ruxsatsiz mustaqil hal qilgan.", False, "Noto‘g‘ri: ular partiya komitetlaridan ruxsat olmasdan hal qila olmas edi.")
t.MUL([("Toshkent metropoliteni qurilishi Sh.Rashidov tashabbusi bilan boshlangan.", True),
       ("1970 – 1978-yillarda O‘zSSR Oliy Soveti Prezidiumi raisi Nazar Matchonov bo‘lgan.", True),
       ("1959 – 1961-yillarda O‘zSSR Ministrlar Soveti raisi Rahmonqul Qurbonov bo‘lgan.", False)],
      "III noto‘g‘ri: 1959 – 1961-yillarda Orif Alimov raisi bo‘lgan.")
t.MATCH("O‘zSSR Ministrlar Soveti raislarini faoliyat davri bilan moslashtiring.", ["Orif Alimov", "Rahmonqul Qurbonov", "Normuhammadi Xudoyberdiyev"],
        ["1971 – 1984-yillar", "1959 – 1961-yillar", "1961 – 1971-yillar"], "bca",
        "Alimov – 1959 – 1961; Qurbonov – 1961 – 1971; Xudoyberdiyev – 1971 – 1984.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["Sharof Rashidovning birinchi sekretar etib saylanishi", "Toshkentdagi zilzila", "Yo.Nasriddinovaning SSSR Millatlar Soveti raisi bo‘lishi", "SSSRning yangi Konstitutsiyasining qabul qilinishi", "Toshkent metropolitenining birinchi navbati ishga tushirilishi"],
      "1959-yil mart → 1966 → 1970 → 1977-yil 7-oktyabr → 1977-yil noyabr.")
t.MAPMATCH(CA, ['Jizzax', 'Qo‘qon', 'Toshkent'],
           ["Sharof Rashidov tug‘ilgan shahar", "Yodgor Nasriddinova tug‘ilgan shahar", "1977-yil noyabrda metropolitenning birinchi navbati ishga tushgan shahar"],
           "1 – Jizzax; 2 – Qo‘qon; 3 – Toshkent.")
t.VENN("Sharof Rashidov", "Yodgor Nasriddinova",
       [("O‘zKP MK birinchi sekretari (1959 – 1983)", 1), ("Jizzaxda tug‘ilgan", 1),
        ("SSSR Oliy Soveti Millatlar Sovetining raisi bo‘lgan", 2), ("Qo‘qonda tug‘ilgan", 2),
        ("O‘zSSR Oliy Soveti Prezidiumi raisi bo‘lgan", 3)],
       "Rashidov – MK birinchi sekretari, Jizzax; Nasriddinova – Millatlar Soveti raisi, Qo‘qon; ikkalasi Oliy Sovet Prezidiumi raisi bo‘lgan.")

# 24-§. Yoqilg‘i va tog‘-kon sanoati, aholi milliy tarkibi
t = Topic('e10u24', 10124); TOPICS['e10u24'] = t
t.B("Ittifoq korxonalari O‘zbekiston yer osti boyliklaridan olingan foydaning necha foizini mahalliy byudjetga o‘tkazgan?", "atigi 1 foizini", "10 foizini", "20 foizini", "50 foizini", "Atigi 1 foizini.")
t.B("XX asr 50-yillari boshida ochilgan gaz konlaridan biri qaysi?", "Jarqo‘rg‘on", "Gazli", "Muruntov", "Uchquduq", "Jarqo‘rg‘on, Qorovulbozor, Sariqtosh konlari.")
t.B("Dunyodagi eng yirik Gazli neft-gaz koni qachon topildi?", "1956-yili", "1958-yili", "1961-yili", "1950-yili", "1956-yili Buxoro viloyatida.")
t.B("Gazli konining umumiy zaxirasi qancha bo‘lgan?", "500 mlrd m³", "33,7 mlrd m³", "50 mlrd m³", "1 trln m³", "500 mlrd m³ gaz.")
t.B("1975-yilga kelib O‘zbekistonda qancha tabiiy gaz ishlab chiqarildi?", "33,7 mlrd m³", "0,4 mlrd m³", "500 mlrd m³", "5,5 mlrd m³", "1960-yil – 0,4, 1975-yil – 33,7 mlrd m³.")
t.B("1975-yilda Butunittifoq gaz qazib chiqarishda O‘zbekistonning ulushi necha foizga yetdi?", "20 foizga", "1 foizga", "50 foizga", "10 foizga", "1960-yildagi 1 foizdan 1975-yilda 20 foizga.")
t.B("Navoiy kon-metallurgiya kombinatiga qachon poydevor qo‘yildi?", "1958-yil 3-sentyabrda", "1956-yilda", "1961-yilda", "1982-yil aprelda", "1958-yil 3-sentyabrda; shu bilan Navoiy shahriga asos solindi.")
t.B("Dunyodagi eng yirik Muruntov oltin koni qachon ishga tushirildi?", "1961-yili", "1963-yili", "1958-yili", "1956-yili", "1961-yili.")
t.B("Muruntovda dastlabki sof quyma oltin (999,9 probali) qachon tayyorlandi?", "1963-yili", "1961-yili", "1958-yili", "1970-yili", "1963-yili.")
t.B("Navoiy viloyati qachon tashkil qilindi?", "1982-yil aprelda", "1958-yil sentyabrda", "1963-yilda", "1977-yilda", "1982-yil aprelda.")
t.B("XX asr 70 – 80-yillarida respublikada har yili taxminan qancha sof oltin quymasi tayyorlangan?", "50 tonna atrofida", "5 tonna", "500 tonna", "10 tonna", "Taxminan 50 tonna.")
t.B("O‘sha davrda oltin zaxiralari bo‘yicha yurtimiz dunyoda nechanchi o‘rinni egallagan?", "yettinchi", "birinchi", "uchinchi", "o‘ninchi", "Yettinchi o‘rinni.")
t.B("Har yili O‘zbekistonda qancha qiymatdagi foydali qazilmalar olingan?", "taxminan 5,5 mlrd dollar", "1 mlrd dollar", "50 mlrd dollar", "500 mln dollar", "Taxminan 5,5 mlrd dollar bahosida.")
t.B("Mahalliy hokimiyatga bo‘ysunmagan, Markazga hisob bergan shaharlar qanday atalgan?", "“yopiq shaharlar”", "“yangi shaharlar”", "“sanoat markazlari”", "“erkin iqtisodiy zonalar”", "Navoiy, Zarafshon, Uchquduq kabi “yopiq shaharlar”.")
t.B("XX asr 60 – 80-yillarida O‘zbekistonda nechta millat va elat yashagan?", "127 ta", "100 ta", "130 ta", "18 ta", "127 ta millat va elat.")
t.B("Navoiy kombinati negizida asos solingan shaharlardan biri qaysi?", "Uchquduq", "Gazli", "Guliston", "Chirchiq", "Navoiy, Sovetobod (Nurobod), Zarafshon, Uchquduq.")
t.NAT("Ittifoq hukumati O‘zbekistonda gaz ishlab chiqarishni keskin oshirdi.", "gaz asosan respublikadan tashqariga jo‘natildi, uy-joylarni gazlashtirish past bo‘lib qoldi", "barcha qishloqlar gazlashtirildi", "gaz eksporti to‘xtatildi", "gaz narxi oshdi", "Gaz asosan tashqariga jo‘natilib, ichki gazlashtirish past bo‘lgan.")
t.NAT("“Yopiq shaharlar”ga boshqa mintaqalardan ishchi kuchi olib kelindi.", "mahalliy aholi bu shaharlardan chiqarilib, ijtimoiy adolat buzildi", "mahalliy yoshlar imtiyoz oldi", "o‘zbek ishchilari soni ko‘paydi", "shaharlar mahalliy hokimiyatga bo‘ysundi", "Kelgindilarga imtiyozlar, mahalliy yoshlar kamsitilgan.")
t.TF("O‘zSSR mamlakat oltinining yarmidan ko‘pini bergan.", True, "To‘g‘ri.")
t.TF("Gaz yetkazib beradigan Buxoro viloyatining o‘zida uy-joy fondi to‘liq gazlashtirilgan edi.", False, "Noto‘g‘ri: Buxoro viloyatining o‘zida ham ahvol nihoyatda achinarli bo‘lgan.")
t.MUL([("Oltin, uran va gaz favqulodda maxfiylik niqobi ostida O‘zbekistondan amalda tekinga olib ketilardi.", True),
       ("Hisor tog‘larining janubi-g‘arbida Odamtosh kondensat koni topilgan.", True),
       ("Gazli koni Navoiy viloyatida 1961-yili topilgan.", False)],
      "III noto‘g‘ri: Gazli koni 1956-yili Buxoro viloyatida topilgan.")
t.MATCH("Sanalarni voqealar bilan moslashtiring.", ["1956-yil", "1958-yil 3-sentyabr", "1961-yil", "1982-yil aprel"],
        ["Navoiy viloyatining tashkil qilinishi", "Muruntov oltin konining ishga tushirilishi", "Gazli konining topilishi", "Navoiy kombinatiga poydevor qo‘yilishi"],
        "cdba", "1956 – Gazli; 1958 – Navoiy kombinati; 1961 – Muruntov; 1982 – Navoiy viloyati.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["Gazli konining topilishi", "Navoiy kombinatiga poydevor qo‘yilishi", "Muruntov konining ishga tushirilishi", "Dastlabki sof quyma oltinning tayyorlanishi", "Navoiy viloyatining tashkil etilishi"],
      "1956 → 1958 → 1961 → 1963 → 1982.")
t.MAPMATCH('uzb', ['Gazli', 'Navoiy', 'Muruntov'],
           ["1956-yili topilgan, zaxirasi 500 mlrd m³ bo‘lgan neft-gaz koni", "1958-yil 3-sentyabrda kon-metallurgiya kombinatiga poydevor qo‘yilgan shahar", "1961-yili ishga tushgan dunyodagi eng yirik oltin koni"],
           "1 – Gazli; 2 – Navoiy; 3 – Muruntov.")
t.VENN("Tabiiy gaz sanoati", "Oltin qazib olish sanoati",
       [("Gazli koni zaxirasi 500 mlrd m³", 1), ("1975-yilda Ittifoq ishlab chiqarishidagi ulush 20 foiz", 1),
        ("Muruntov koni 1961-yili ishga tushgan", 2), ("har yili 50 tonnaga yaqin sof quyma tayyorlangan", 2),
        ("mahsuloti asosan Markaz manfaatlariga xizmat qilgan", 3)],
       "Gaz – Gazli, 20 %; oltin – Muruntov, 50 t; ikkalasi Markaz manfaatlariga xizmat qilgan.")
