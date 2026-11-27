from qlib import Topic
TOPICS = {}

# 11 Kollektivlashtirish va quloqlarning surgun qilinishi
t = Topic('e10u11', 10011); TOPICS['e10u11'] = t
t.B("Yer-suv islohotining ikkinchi bosqichi qaysi yillarda amalga oshirilgan?", "1925–1929-yillarda", "1921–1922-yillarda", "1930–1932-yillarda", "1929–1935-yillarda", "1925–1929-yillarda.")
t.B("«Agrar inqilob»ning strategiya va taktikasi qayerda tasdiqlangan?", "O‘zbekiston Kompartiyasining II syezdida", "VKP(b) XIV syezdida", "O‘zSSR Sovetlarining I qurultoyida", "SSSR MIQ III sessiyasida", "1925-yil noyabrdagi II syezdda.")
t.B("«Suv va suvni natsionalizatsiya qilish to‘g‘risida»gi dekret qachon qabul qilingan?", "1925-yil 2-dekabrda", "1930-yil 17-fevralda", "1925-yil 13-fevralda", "1927-yil 30-martda", "O‘zSSR MIKning 1925-yil 2-dekabrdagi dekreti.")
t.B("Farg‘ona viloyatida necha desyatina va undan ortiq yeri bor katta yer egalarining xo‘jaliklari tugatilgan?", "40 desyatina", "50 desyatina", "10 desyatina", "100 desyatina", "Farg‘onada 40, Toshkent va Samarqandda 50 desyatina.")
t.B("1925–1929-yillarda qancha boy xo‘jaliklar tugatilgan?", "5000 ga yaqin", "23 000 dan ortiq", "500 ga yaqin", "60 000", "5000 ga yaqin boy xo‘jalik.")
t.B("Har bir boy va o‘ziga to‘q xo‘jalikka qancha yer qoldirilishi mumkin edi?", "7–10 desyatina", "40–50 desyatina", "1–2 desyatina", "20–30 desyatina", "7–10 desyatinagacha.")
t.B("«Kollektivlashtirish va quloq xo‘jaliklarini tugatish to‘g‘risida»gi qaror qachon qabul qilingan?", "1930-yil 17-fevralda", "1930-yil 26-yanvarda", "1925-yil 2-dekabrda", "1932-yilda", "O‘zbekiston Kompartiyasi MK, 1930-yil 17-fevral.")
t.B("1930-yili O‘zbekistonda nechta tuman yalpi kollektivlashtiriladigan deb belgilangan?", "19 ta", "17 ta", "14 ta", "240 ta", "19 ta tuman.")
t.B("Kollektivlashtirish rasman qachon tugallangan?", "1932-yili", "1930-yili", "1939-yili", "1935-yili", "1932-yili.")
t.B("1932-yilga kelib dehqon xo‘jaliklarining necha foizi kolxoz va sovxozlarga birlashgan?", "75 foizi", "50 foizi", "90 foizi", "60 foizi", "75 foizi.")
t.B("Yakka dehqon xo‘jaliklariga qachon butkul barham berilgan?", "1939-yilga kelib", "1932-yilga kelib", "1930-yilda", "1935-yilda", "1939-yilga kelib.")
t.B("1930-yili qoramollar soni qanchaga kamaygan?", "60 000 boshdan ziyod", "6000 bosh", "600 000 bosh", "3700 bosh", "60 000 boshdan ziyodga.")
t.B("G‘alla tayyorlashni «urush degandek gap» deb ta’riflagan Shahrisabz tumani vakili kim?", "Jalilov", "Kirpanov", "Ikromov", "Ivanov", "Jalilov.")
t.B("Respublikada quloqlar uchun nechta majburiy mehnat posyolkasi tashkil qilingan?", "17 ta", "19 ta", "14 ta", "240 ta", "17 ta.")
t.B("Faqat Qashqadaryo okrugida 1930-yil boshlarida dehqonlarning nechta norozilik chiqishlari yuz bergan?", "14 ta", "240 ta", "19 ta", "2000 ta", "14 ta, 3700 kishi ishtirokida.")
t.B("1930-yil mart oyida O‘zSSRda nechta qurolli chiqish qayd etilgan?", "240 ta", "2000 dan ortiq", "14 ta", "17 ta", "240 ta.")
t.B("1933-yili O‘zbekistonda surgun qilingan quloq xo‘jaliklari soni qanchaga yetgan?", "5500", "3871", "1152", "23 000", "5500 tagacha.")
t.NAT("Mahalliy rahbarlar kolxozga kirmaganlarni suvdan mahrum qilish, surgun qilish bilan dag‘dag‘a qildi.", "ko‘pchilik tumanlarda kollektivlashtirish bir necha hafta ichida amalga oshirildi", "dehqonlar kolxozlardan chiqib ketdi", "kollektivlashtirish to‘xtatildi", "yakka xo‘jaliklar ko‘paydi", "Kollektivlashtirish bir necha haftada o‘tkazildi.")
t.NAT("Quloqlar sifatida ro‘yxatga olingan xo‘jaliklarning mol-mulki to‘liq musodara qilindi.", "ularning oilalari Ukraina, Sibir, Qozog‘iston kabi o‘zga yurtlarga surgun qilindi", "ular kolxoz raisi etib tayinlandi", "ularga qo‘shimcha yer berildi", "ular soliqdan ozod qilindi", "Oilalar o‘zga yurtlarga surgun qilindi.")
t.TF("Yakka xo‘jaliklar davlatga majburan topshiradigan mahsulot hajmi kolxozlarga nisbatan 50 foizga ko‘paytirilgan.", True, "To‘g‘ri.")
t.TF("Yer-suv islohotida faqat yer musodara qilinib, ishchi hayvonlar egasida qoldirilgan.", False, "Noto‘g‘ri: ishchi hayvonlar va asbob-uskunalar ham musodara qilingan.")
t.MUL([("Ikkinchi bosqich (1927) Zarafshon viloyatida o‘tkazilgan.", True),
       ("Uchinchi bosqich (1928–1929) Qashqadaryo, Surxondaryo, Xorazm okruglarida o‘tkazilgan.", True),
       ("Birinchi bosqich Xorazm viloyatida boshlangan.", False)],
      "III noto‘g‘ri: birinchi bosqich Farg‘ona, Toshkent, Samarqand viloyatlarida o‘tkazilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Yer-suv islohoti dekretlari", "VKP(b) MK Siyosiy byurosining quloq xo‘jaliklarini tugatish qarori", "O‘zbekiston Kompartiyasi MKning kollektivlashtirish qarori", "Kollektivlashtirish rasman tugallandi", "Yakka xo‘jaliklarga butkul barham berildi"],
      "1925-yil dekabr → 1930-yil 26-yanvar → 1930-yil 17-fevral → 1932 → 1939.")
t.MAPMATCH('uzb', ['Samarqand', 'Buxoro', 'Xiva'],
           ["yer-suv islohoti 1925–1926-yillarda (birinchi bosqich) o‘tkazilgan viloyat markazi", "yer-suv islohoti 1927-yilda (ikkinchi bosqich) o‘tkazilgan Zarafshon viloyati markazi", "yer-suv islohoti 1928–1929-yillarda (uchinchi bosqich) o‘tkazilgan Xorazmdagi shahar"],
           "1 – Samarqand; 2 – Buxoro; 3 – Xiva.")
t.VENN("Boy xo‘jaliklar", "O‘ziga to‘q dehqon xo‘jaliklari",
       [("40–50 desyatina va undan ortiq yeri bo‘lgan", 1), ("5000 ga yaqini butunlay tugatilgan", 1),
        ("10–40 desyatinagacha yeri bo‘lgan", 2), ("keyinchalik «quloqlar» deb nomlangan", 2),
        ("yerlari tortib olingan", 3)],
       "Boy — 40–50 desyatina, tugatilgan; o‘ziga to‘q — 10–40 desyatina, «quloqlar».")

# 12 Industrlashtirish va kadrlar masalasi
t = Topic('e10u12', 10012); TOPICS['e10u12'] = t
t.B("SSSRda sotsialistik industrlashtirishga o‘tish qayerda e’lon qilingan?", "VKP(b) XIV syezdida", "O‘zbekiston Kompartiyasining II syezdida", "SSSR MIQ III sessiyasida", "O‘zSSR Sovetlarining II syezdida", "1925-yil dekabrdagi VKP(b) XIV syezdida.")
t.B("1927-yilda O‘zSSR xalq xo‘jaligida qishloq xo‘jaligining salmog‘i qancha bo‘lgan?", "62,6 %", "37,4 %", "90 %", "75 %", "62,6 %, sanoatniki 37,4 %.")
t.B("Sanoat ishlab chiqarishining necha foizi qishloq xo‘jalik xomashyosini qayta ishlashga asoslangan edi?", "90 foizi", "62,6 foizi", "37,4 foizi", "50 foizi", "90 foizi.")
t.B("1928-yil kuzigacha xalq xo‘jaligi qanday rejalar asosida boshqarilgan?", "bir yillik", "besh yillik", "yetti yillik", "uch yillik", "Bir yillik rejalar asosida.")
t.B("Birinchi besh yillik reja qachon yakunlangan?", "1932-yil dekabrda", "1933-yil oktyabrda", "1930-yil sentyabrda", "1931-yil dekabrda", "1932-yil dekabrda, muddatidan 9 oy oldin.")
t.B("Birinchi besh yillikda O‘zbekistonda nechta yangi sanoat korxonasi qurilgan?", "289 ta", "79 ta", "482 ta", "60 ta", "289 ta.")
t.B("O‘rta Osiyoda paxtachilik va mashinasozlik sanoatining to‘ng‘ichi qaysi korxona?", "Toshkent qishloq xo‘jaligi mashinasozligi zavodi", "Chirchiq elektr kimyo kombinati", "Toshkent to‘qimachilik kombinati", "Chirchiq-Bo‘zsuv GESi", "Toshkent qishloq xo‘jaligi mashinasozligi zavodi.")
t.B("XX asr 30-yillarida qaysi GESlar kaskadi barpo etilgan?", "Chirchiq-Bo‘zsuv", "Farhod", "Chorvoq", "Norak", "Chirchiq-Bo‘zsuv GESlar kaskadi.")
t.B("Industrlashtirish siyosati asosan kimning hisobidan amalga oshirildi?", "qishloq hisobidan", "xorijiy kreditlar hisobidan", "neft savdosi hisobidan", "oltin zaxiralari hisobidan", "Qishloq hisobidan: xarid narxlari pasaytirildi.")
t.B("Davlat apparatini mahalliylashtirish Markaziy komissiyasi qachon tuzilgan?", "1925-yil 3-martda", "1927-yil 8-yanvarda", "1928-yil 18-fevralda", "1931-yil 11-dekabrda", "1925-yil 3-martda.")
t.B("Mahalliylashtirish Markaziy komissiyasining raisi kim bo‘lgan?", "Bobon Mavlonbekov", "Fayzulla Xo‘jayev", "Akmal Ikromov", "Rahim Inog‘omov", "Bobon Mavlonbekov.")
t.B("Mahalliy kadrlar tayyorlashda jonbozlik ko‘rsatgan O‘zSSR XKS raisi kim?", "Fayzulla Xo‘jayev", "Yo‘ldosh Oxunboboyev", "Bobon Mavlonbekov", "Vladimir Ivanov", "Fayzulla Xo‘jayev.")
t.B("O‘zbekiston Kompartiyasining II syezdi qayerda o‘tgan?", "Samarqandda", "Toshkentda", "Buxoroda", "Moskvada", "1925-yil 22–30-noyabrda Samarqandda.")
t.B("Komissiya qachon «Davlat apparati va sanoatni O‘zbeklashtirish Markaziy komissiyasi» deb qayta nomlangan?", "1927-yil 8-yanvarda", "1925-yil 3-martda", "1928-yil 18-fevralda", "1927-yil 6-iyunda", "1927-yil 8-yanvarda.")
t.B("«Davlat apparatini o‘zbeklashtirish to‘g‘risida»gi qo‘shma qaror qachon qabul qilingan?", "1928-yil 18-fevralda", "1927-yil 16-noyabrda", "1931-yil 11-dekabrda", "1929-yilda", "O‘zSSR MIK va XKS, 1928-yil 18-fevral.")
t.B("O‘zbeklashtirish Markaziy komissiyasi faoliyati qaysi qaror bilan to‘xtatilgan?", "SSSR MIKning 1931-yil 11-dekabrdagi qarori", "VKP(b) XIV syezdi qarori", "O‘zSSR MIKning 1927-yilgi qarori", "Kompartiyaning III syezdi qarori", "SSSR MIKning 1931-yil 11-dekabrdagi qarori.")
t.NAT("Markaz O‘zbekistonda ham mahalliylashtirishni to‘xtatib, uni «burjua millatchiligi» deb e’lon qildi.", "ruslashtirish jarayoni yangi bosqichga qadam qo‘ydi", "o‘zbek tili davlat tili bo‘ldi", "milliy kadrlar ko‘paydi", "ish yuritish o‘zbek tiliga o‘tdi", "Rus tilining mavqeyi oshirildi.")
t.NAT("Qishloq xo‘jalik mahsulotlarining xarid narxlari pasaytirildi.", "dehqonlar qashshoqlashib, oziq-ovqat muammosi keskinlashdi", "dehqonlar boyib ketdi", "oziq-ovqat mo‘l bo‘ldi", "sanoat qisqardi", "Oziq-ovqat muammosi keskinlashdi.")
t.TF("Sanoat korxonalariga malakali xodimlar RSFSRning markaziy shaharlaridan olib kelingan.", True, "To‘g‘ri.")
t.TF("Bu davrda davlat apparatida ish yuritish asosan o‘zbek tilida olib borilgan.", False, "Noto‘g‘ri: rus tilida olib borilgan.")
t.MUL([("Birinchi besh yillikda 79 ta korxona qayta tashkil etilgan.", True),
       ("O‘zbekistonga ko‘chirib keltirilgan yevropaliklar navbatsiz kvartira bilan ta’minlangan.", True),
       ("Qishloqdan kelgan o‘zbek yoshlari imtiyozli asosda universitetlarga qabul qilingan.", False)],
      "III noto‘g‘ri: imtiyozlar ko‘chirib keltirilganlarga berilgan, o‘zbek yoshlari «qora ishlar»da ishlagan.")
t.MATCH("Sanalarni voqealar bilan moslashtiring.", ["1925-yil 3-mart", "1927-yil 8-yanvar", "1928-yil 18-fevral", "1931-yil 11-dekabr"],
        ["Mahalliylashtirish Markaziy komissiyasi tuzildi", "Komissiya O‘zbeklashtirish komissiyasi deb qayta nomlandi", "«Davlat apparatini o‘zbeklashtirish to‘g‘risida» qo‘shma qaror", "O‘zbeklashtirish komissiyasi faoliyati to‘xtatildi", "Kompartiyaning II syezdi"], 'abcd',
        "1925-yil 3-mart – komissiya; 1927-yil 8-yanvar – qayta nomlash; 1928-yil 18-fevral – qo‘shma qaror; 1931-yil 11-dekabr – to‘xtatildi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Mahalliylashtirish Markaziy komissiyasi tuzildi", "VKP(b) XIV syezdi", "O‘zbeklashtirish komissiyasi Nizomi kuchga kirdi", "Birinchi besh yillik boshlandi", "Birinchi besh yillik yakunlandi"],
      "1925-yil mart → 1925-yil dekabr → 1927-yil iyun → 1928-yil oktyabr → 1932-yil dekabr.")
t.VENN("Mahalliylashtirish siyosati", "Ruslashtirish siyosati",
       [("milliy kadrlarni yuqori lavozimlarga ko‘tarish", 1), ("ish yuritishni o‘zbek tilida olib borish", 1),
        ("rus tilining mavqeyini oshirish", 2), ("1931-yildan keyin kuchaygan", 2),
        ("davlat apparatiga oid siyosat", 3)],
       "Mahalliylashtirish — milliy kadrlar, o‘zbek tili; ruslashtirish — rus tili, 1931-yildan.")
