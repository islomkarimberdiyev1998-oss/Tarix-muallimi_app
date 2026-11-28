from qlib import Topic, PLACES, REG
TOPICS = {}

# 25-mavzu. O‘zbekiston Ikkinchi jahon urushi yillarida
t = Topic('y10u25', 10025); TOPICS['y10u25'] = t
t.B("Germaniya SSSRga qachon hujum qilgan?", "1941-yil 22-iyunda", "1941-yil 23-iyunda", "1939-yil 1-sentyabrda", "1941-yil 30-iyunda", "1941-yil 22-iyun.")
t.B("Toshkentda ko‘p ming kishilik miting qachon bo‘lgan?", "1941-yil 23-iyunda", "1941-yil 22-iyunda", "1941-yil dekabrda", "1945-yil 9-mayda", "1941-yil 23-iyun.")
t.B("Davlat mudofaa komiteti qachon tuzilgan?", "1941-yil 30-iyunda", "1941-yil 22-iyunda", "1941-yil dekabrda", "1942-yilda", "1941-yil 30-iyun.")
t.B("Front hududlaridan O‘zbekistonga necha kishi evakuatsiya qilingan?", "1 million 500 ming", "200 ming", "15 million", "500 ming", "1,5 mln, jumladan 200 mingdan ziyod yetim bola.")
t.B("Shoahmad Shomahmudov va Bahri Akromova nechta bolani tarbiyaga olgan?", "14 nafar", "13 nafar", "10 nafar", "20 nafar", "14 nafar.")
t.B("Kattaqo‘rg‘onlik Hamid Samadov nechta bolani asrab olgan?", "13 nafar", "14 nafar", "10 nafar", "5 nafar", "13 nafar.")
t.B("Samarqandlik Fotima Qosimova nechta bolani asrab olgan?", "10 nafar", "13 nafar", "14 nafar", "7 nafar", "10 nafar.")
t.B("O‘zbekistonda nechtadan ortiq evakuatsiya gospitali faoliyat yuritgan?", "120 dan", "12 dan", "1200 dan", "50 dan", "120 dan ortiq.")
t.B("Aholi mudofaa jamg‘armasiga qancha pul topshirgan?", "649,9 mln rubl", "3 mlrd rubl", "22 mln rubl", "1 mlrd rubl", "649,9 mln rubl.")
t.B("1941-yil dekabrda Toshkentdan Moskvaga yuborilgan eshelon haqida qaysi film ishlangan?", "«Qirq birinchi yil olmasi»", "«Sen yetim emassan»", "«Mahallada duv-duv gap»", "«Toshkent – non shahri»", "«Qirq birinchi yil olmasi».")
t.B("Frontga delegatsiyaning bir guruhiga kim boshchilik qilgan?", "Yo‘ldosh Oxunboboyev", "Sharof Rashidov", "Usmon Yusupov", "Sobir Rahimov", "Yo‘ldosh Oxunboboyev (ikkinchisiga Hasan Islomov).")
t.B("Front hududlaridan O‘zbekistonga nechta zavod ko‘chirib keltirilgan?", "151 ta", "300 ta", "230 ta", "51 ta", "151 ta.")
t.B("1941-yil dekabrga kelib nechta korxona mudofaa mahsulotlarini bera boshlagan?", "230 ta", "151 ta", "300 ta", "120 ta", "230 ta.")
t.B("Urush yillarida O‘zbekiston uchun qanday yangi ekin joriy etilgan?", "qand lavlagi", "paxta", "bug‘doy", "sholi", "Qand lavlagi.")
t.B("Qand lavlagisini qayta ishlovchi zavodlardan biri qayerda qurilgan?", "Zirabuloqda", "Chirchiqda", "Nukusda", "Termizda", "Zirabuloq, Krasnogvardeysk, Qo‘qon, Yangiyo‘l.")
t.B("1945-yilda topshirilgan lavlagi SSSR qandining qancha qismini tashkil etgan?", "chorak qismini", "yarmini", "o‘ndan birini", "uchdan birini", "Chorak qismini.")
t.B("O‘zbekiston aholisi davlatga qancha paxta topshirgan?", "4 mln tonnadan ziyod", "1 mln tonna", "400 ming tonna", "10 mln tonna", "4 mln tonnadan ziyod.")
t.NAT("Davlat mudofaa komiteti tuzildi.", "mamlakatdagi butun hokimiyat uning qo‘liga o‘tib, qarorlari urush qonunlari kuchiga ega bo‘ldi", "hokimiyat Sovetlarga qaytdi", "urush tugadi", "partiya tarqatildi", "Butun hokimiyat DMKda.")
t.NAT("Minglab yetim bolalar O‘zbekistonga evakuatsiya qilindi.", "yetimlarga g‘amxo‘rlik umumxalq harakatiga aylandi", "bolalar qaytarib yuborildi", "bolalar faqat bolalar uylarida qoldi", "bolalarga e’tibor berilmadi", "Umumxalq harakati.")
t.NAT("Frontga safarbarlik tufayli ishchi kuchi yetishmay qoldi.", "urushga ketganlar o‘rnini qariyalar, ayollar va o‘smirlar egalladi", "zavodlar yopildi", "ishchilar chetdan olindi", "ishlab chiqarish to‘xtadi", "Qariyalar, ayollar, o‘smirlar ishladi.")
t.NAT("Aholi mudofaa jamg‘armasiga pul va qimmatbaho buyumlar topshirdi.", "mablag‘larning bir qismiga zirhli poyezd, samolyot, tanklar qurilib frontga yuborildi", "mablag‘ xorijga ketdi", "jamg‘arma bekor qilindi", "pul aholiga qaytarildi", "Qurol-aslaha qurildi.")
t.TF("Toshkentdan Moskvaga yuborilgan eshelon bombardimonga qaramay G‘arbiy frontga yetib borgan.", True, "To‘g‘ri.")
t.TF("Gospitallarda davolanganlarning asosiy qismi uyiga qaytarilgan.", False, "Noto‘g‘ri: asosiy qismi jangovar safga qaytgan.")
t.TF4([("Respublikadagi 300 ga yaqin korxonada harbiy mahsulot ishlab chiqarilgan.", True), ("Ayollar meros zargarlik buyumlarini ham jamg‘armaga topshirgan.", True),
       ("Qashqadaryoda qand lavlagi 1943-yildan ekila boshlagan.", True), ("O‘zbekistonliklar Sovet–Finlyandiya urushida qatnashmagan.", False)],
      "4-noto‘g‘ri: Sovet–Finlyandiya urushida ham ishtirok etgan.")
t.MUL([("Yoshlardan ishchilar tayyorlashda fabrika-zavod ta’limi va hunar maktablari muhim bo‘lgan.", True),
       ("O‘zbekiston kungaboqar, zig‘ir, kanop yetishtirishni ham yo‘lga qo‘ygan.", True),
       ("Urush yillarida O‘zbekistonga hech qanday zavod ko‘chirilmagan.", False)],
      "III noto‘g‘ri: 151 ta zavod ko‘chirib keltirilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Germaniya SSSRga hujum qildi", "Toshkentda miting", "Davlat mudofaa komiteti tuzildi", "230 korxona mudofaa mahsuloti bera boshladi", "Qashqadaryoda qand lavlagi ekila boshladi", "lavlagi SSSR qandining choragini berdi"],
      "1941-06-22 → 06-23 → 06-30 → 1941-12 → 1943 → 1945.")
t.MATCH("Shaxslarni asrab olgan bolalar soni bilan moslashtiring.", ["Shomahmudovlar oilasi", "Hamid Samadov", "Fotima Qosimova", "evakuatsiya qilingan yetim bolalar"],
        ["14 nafar", "13 nafar", "10 nafar", "200 mingdan ziyod", "1,5 million"], 'abcd',
        "Shomahmudovlar – 14; Samadov – 13; Qosimova – 10; yetimlar – 200 mingdan ziyod.")
t.VENN("Front orqasidagi yordam", "Mudofaa jamg‘armasi",
       [("evakuatsiya qilinganlarni joylashtirish", 1), ("151 zavodni ishga tushirish", 1),
        ("649,9 mln rubl pul", 2), ("55 kg dan ziyod qimmatbaho metall", 2),
        ("O‘zbekiston xalqining g‘alabaga hissasi", 3)],
       "Front orti – evakuatsiya, zavodlar; jamg‘arma – pul, metall; ikkalasi g‘alabaga hissa.")
t.MAPMATCH('uzb', ['Toshkent', 'Samarqand', 'Zirabuloq', 'Qo‘qon'],
           ["1941-yil 23-iyunda miting bo‘lgan, temirchi Shomahmudov yashagan shahar", "Fotima Qosimova 10 bolani asrab olgan shahar", "qand lavlagi zavodi qurilgan Zarafshon bo‘yidagi joy", "qand zavodi qurilgan Farg‘ona vodiysi shahri"],
           "1 – Toshkent; 2 – Samarqand; 3 – Zirabuloq; 4 – Qo‘qon.")
