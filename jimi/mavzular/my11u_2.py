from qlib import Topic, PLACES, REG
TOPICS = {}

# 3-mavzu. Fuqarolik jamiyati
t = Topic('y11u3', 11003); TOPICS['y11u3'] = t
t.B("Fuqarolik jamiyatini shakllantirishning birinchi bosqichi qaysi yillarni qamraydi?", "1991–2000", "2001–2010", "2011–2016", "2016-yildan", "1991–2000.")
t.B("«Kuchli davlatdan kuchli fuqarolik jamiyati sari» o‘tish qaysi bosqichning maqsadi edi?", "2001–2010-yillar", "1991–2000-yillar", "2011–2016-yillar", "2016-yildan keyin", "Ikkinchi bosqich, 2001–2010.")
t.B("NNTlar davlatning hamkori sifatida yuzaga chiqqan bosqich qaysi?", "2011–2016-yillar", "1991–2000-yillar", "2001–2010-yillar", "1990-yillar", "Uchinchi bosqich.")
t.B("To‘rtinchi bosqich qaysi tamoyilga asoslangan?", "«Inson manfaatlari – ustuvor»", "«Kuchli davlat»", "«Bo‘lib tashla»", "«Yagona partiya»", "«Inson manfaatlari – ustuvor».")
t.B("2017–2024-yillarda fuqarolik jamiyatini qo‘llashga qaratilgan nechtadan ortiq hujjat qabul qilingan?", "60 dan", "6 dan", "600 dan", "150 dan", "60 dan ortiq.")
t.B("NNTlar uchun ishga tushirilgan elektron portal qaysi?", "e-ngo.uz", "my.gov.uz", "lex.uz", "edu.uz", "e-ngo.uz.")
t.B("O‘zbekistonda faoliyati yo‘lga qo‘yilgan birinchi siyosiy partiya qaysi?", "Xalq demokratik partiyasi", "O‘zLiDeP", "«Adolat»", "«Milliy tiklanish»", "XDP, 1991-yil.")
t.B("«Vatan taraqqiyoti» partiyasi qachon tashkil topgan?", "1992-yilda", "1991-yilda", "1995-yilda", "1999-yilda", "1992-yilda.")
t.B("O‘zbekistondagi ilk sotsial-demokratik partiya qaysi?", "«Adolat»", "«Fidokorlar»", "O‘zLiDeP", "XDP", "«Adolat», 1995-yil.")
t.B("«Fidokorlar» milliy demokratik partiyasi qachon tashkil etilgan?", "1999-yilda", "1995-yilda", "2003-yilda", "1992-yilda", "1999-yilda.")
t.B("2008-yilda «Fidokorlar» qaysi partiya bilan birlashtirildi?", "«Milliy tiklanish»", "«Adolat»", "XDP", "O‘zLiDeP", "«Milliy tiklanish».")
t.B("O‘zLiDeP qachon tuzilgan?", "2003-yil noyabrda", "1999-yilda", "2008-yilda", "1995-yilda", "2003-yil noyabr, Ta’sis qurultoyi.")
t.B("Ekologik partiya qachon rasmiy ro‘yxatdan o‘tgan?", "2019-yilda", "2008-yilda", "2003-yilda", "2023-yilda", "2019-yilda.")
t.B("Birinchi referendum qachon o‘tkazilgan?", "1991-yil martda", "1991-yil dekabrda", "1995-yilda", "2002-yilda", "1991-yil mart.")
t.B("1991-yil dekabrdagi referendumda qanday savol qo‘yilgan?", "«O‘zbekiston Respublikasining davlat mustaqilligini ma’qullaysizmi?»", "Ittifoq tarkibida qolish", "Prezident muddatini uzaytirish", "Konstitutsiyani yangilash", "Mustaqillikni ma’qullash.")
t.B("Ikki palatali parlament masalasi qaysi referendumda hal qilingan?", "2002-yilgi", "1995-yilgi", "2023-yilgi", "1991-yilgi", "2002-yilgi referendum.")
t.B("Markaziy saylov komissiyasi qachondan mustaqil organ sifatida faoliyat ko‘rsatadi?", "1998-yildan", "1991-yildan", "2002-yildan", "2024-yildan", "1998-yildan.")
t.B("Beshinchi referendum qachon o‘tkazilgan?", "2023-yil aprelida", "2002-yilda", "2019-yilda", "2016-yilda", "2023-yil aprel – yangi tahrirdagi Konstitutsiya.")
t.NAT("Ikkinchi bosqichda siyosiy partiyalarni moliyalashtirish tizimi shakllandi, muxolifat maqomi belgilandi.", "siyosiy maydon jonlanib, parlament demokratik tamoyillarga moslashdi", "partiyalar tarqatildi", "parlament bir palatali bo‘ldi", "muxolifat taqiqlandi", "Siyosiy maydon jonlandi.")
t.NAT("«Fidokorlar» va «Milliy tiklanish» g‘oyalari bir-biriga o‘xshash edi.", "2008-yilda ular yagona kuchliroq partiyaga birlashtirildi", "ikkalasi tarqatildi", "ular raqobatlashdi", "biri taqiqlandi", "Birlashtirildi.")
t.NAT("Ko‘ppartiyaviylik qaror topdi.", "saylovlarda xalqning tanlovi kengayib, sog‘lom raqobat shakllandi", "tanlov qisqardi", "saylovlar bekor qilindi", "bitta partiya qoldi", "Tanlov kengaydi.")
t.NAT("1991-yil mart referendumida ko‘pchilik yangilangan ittifoqda qolishga rozi bo‘ldi.", "odamlar mustaqillikni xohlasa-da, SSSR bilan aloqani uzishga hali tayyor emasligi ko‘rindi", "SSSR darhol tarqaldi", "mustaqillik rad etildi", "referendum bekor qilindi", "Aloqani uzishga tayyor emaslik.")
t.TF("Konstitutsiyaga birinchi marta «mahalla» tushunchasi kiritilgan.", True, "To‘g‘ri.")
t.TF("Referendum byulletenida «Ma’qullaysizmi?» shaklida savol qo‘yiladi.", False, "Noto‘g‘ri: aynan «Qabul qilasizmi?» ko‘rinishida qo‘yiladi.")
t.TF4([("«Vatan taraqqiyoti» 2000-yilda «Fidokorlar»ga qo‘shilgan.", True), ("2024-yil sentyabrdan MSK 9 kishilik tarkibda ishlamoqda.", True),
       ("Har bir viloyatda «Do‘stlik va nodavlat tashkilotlar uylari» ochilgan.", True), ("O‘zLiDeP asosan ishchilar manfaatini ifodalash uchun tuzilgan.", False)],
      "4-noto‘g‘ri: mulkdorlar, kichik biznes, fermerlar, ishbilarmonlar manfaatini ifodalaydi.")
t.MUL([("O‘zbekiston ekologik harakati 2008-yilda vujudga kelgan.", True),
       ("Saylovda ovoz berish ham huquq, ham fuqarolik burchi hisoblanadi.", True),
       ("1995-yilgi referendum ikki palatali parlamentni joriy etgan.", False)],
      "III noto‘g‘ri: 1995-yilda Prezident muddati uzaytirilgan; ikki palatali parlament – 2002-yil.")
t.CHR("Partiyalarni tashkil topgan yili bo‘yicha tartiblang.", ["Xalq demokratik partiyasi", "«Vatan taraqqiyoti»", "«Adolat» va «Milliy tiklanish»", "«Fidokorlar»", "O‘zLiDeP", "Ekologik partiya"],
      "1991 → 1992 → 1995 → 1999 → 2003 → 2019.")
t.MATCH("Referendumlarni masalasi bilan moslashtiring.", ["1991-yil mart", "1991-yil dekabr", "1995-yil", "2023-yil aprel"],
        ["yangilangan ittifoqda qolish", "davlat mustaqilligini ma’qullash", "Prezident vakolatini 2000-yilgacha uzaytirish", "yangi tahrirdagi Konstitutsiya", "ikki palatali parlament"], 'abcd',
        "1991-mart – ittifoq; 1991-dekabr – mustaqillik; 1995 – muddat; 2023 – Konstitutsiya.")
t.VENN("Saylov", "Referendum",
       [("bir necha nomzod taqdim etiladi", 1), ("munosib nomzod tanlanadi", 1),
        ("muhim masala umumxalq so‘roviga qo‘yiladi", 2), ("byulletenda «Qabul qilasizmi?» savoli", 2),
        ("xalq hokimiyatining asosiy ko‘rinishi", 3)],
       "Saylov – nomzodlar; referendum – masala; ikkalasi xalq hokimiyati.")
t.MAPN('uzb', ['Nukus', 'Toshkent', 'Samarqand', 'Qo‘qon'], "Fuqarolar vakillari – Jo‘qorg‘i Kenges a’zolari faoliyat yuritadigan Qoraqalpog‘iston Respublikasi poytaxti xaritada qaysi raqamda?",
       "Nukus.")
