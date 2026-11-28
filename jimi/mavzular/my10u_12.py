from qlib import Topic, PLACES, REG
TOPICS = {}

# 23-mavzu. Sovet madaniy siyosati
t = Topic('y10u23', 10023); TOPICS['y10u23'] = t
t.B("Sovet hokimiyati dastlabki yillarda qaysi maktablarni yopdi?", "jadid, eski usul va vaqf maktablarini", "sovet maktablarini", "texnikumlarni", "universitetlarni", "Jadid, eski usul va vaqf maktablari.")
t.B("O‘zbekiston SSR Fanlar komiteti qachon tuzilgan?", "1932-yil 14-oktyabrda", "1940-yil 8-mayda", "1929-yil 1-dekabrda", "1936-yilda", "1932-yil 14-oktyabr.")
t.B("O‘rta Osiyoda oliy ta’limning beshigi deb qaysi o‘quv yurti ataladi?", "Turkiston xalq dorilfununi", "Toshkent konservatoriyasi", "Samarqand universiteti", "Buxoro madrasasi", "Turkiston xalq dorilfununi (hozirgi O‘zMU).")
t.B("1940-yilda respublikada nechta oliy o‘quv yurti bo‘lgan?", "30 ta", "100 ta", "3 ta", "300 ta", "30 ta oliy, 100 ga yaqin o‘rta maxsus.")
t.B("Majburiy yetti yillik ta’limga necha yoshli bolalarni tortish taklif qilingan?", "8 yoshdan 15 yoshgacha", "6 yoshdan 13 yoshgacha", "7 yoshdan 17 yoshgacha", "10 yoshdan 18 yoshgacha", "8–15 yosh.")
t.B("Ikkinchi besh yillikda umumta’lim maktablari o‘quvchilari soni qanchaga yetgan?", "931 800 nafar", "139 000 nafar", "725 000 nafar", "100 000 nafar", "931 800 nafar.")
t.B("Respublika maktablarida o‘qish nechta tilda olib borilgan?", "18 tilda", "3 tilda", "10 tilda", "2 tilda", "18 tilda.")
t.B("1937-yilda nechta xotin-qiz o‘qish va yozishni o‘rgangan?", "139 000", "931 800", "13 900", "1 million", "139 000 nafar.")
t.B("Sovet hokimiyatining dastlabki o‘n yilliklarida imlo necha marta o‘zgartirilgan?", "3 marta", "1 marta", "5 marta", "2 marta", "3 marta.")
t.B("Lotin grafikasiga o‘tish haqida qaror qayerda qabul qilingan?", "1929-yil may, Samarqanddagi konferensiyada", "1940-yil 8-mayda Toshkentda", "1925-yilda Buxoroda", "1932-yilda Moskvada", "1929-yil may, Samarqand.")
t.B("O‘zbekistonda arab alifbosidan lotin yozuviga qachon o‘tildi?", "1929-yil 1-dekabrda", "1940-yil 8-mayda", "1932-yil 14-oktyabrda", "1927-yil 8-martda", "1929-yil 1-dekabr.")
t.B("Kirill yozuviga o‘tish to‘g‘risidagi qaror qachon qabul qilingan?", "1940-yil 8-mayda", "1929-yil 1-dekabrda", "1936-yilda", "1932-yilda", "1940-yil 8-may, O‘zSSR Oliy Soveti III sessiyasi.")
t.B("Toshkentda davlat konservatoriyasi qachon ochilgan?", "1936-yilda", "1940-yilda", "1927-yilda", "1932-yilda", "1936-yilda.")
t.B("«Hujum» kampaniyasi qachon boshlangan?", "1927-yil 8-martda", "1926-yil sentyabrda", "1929-yil mayda", "1930-yilda", "1927-yil 8-mart.")
t.B("1927-yil 8-martdagi mitinglarda nechtadan ortiq ayol paranjisini yoqdi?", "100 000 dan", "10 000 dan", "2 500 dan", "1 million", "100 000 dan ortiq.")
t.B("1927–1928-yillarda nechtadan ortiq faol xotin-qiz fojiali halok bo‘lgan?", "2 500 dan", "250 dan", "25 000 dan", "100 dan", "2 500 dan ortiq.")
t.B("O‘zSSR MIK Prezidiumi raisi o‘rinbosari bo‘lgan o‘zbek ayoli kim?", "Jahon Obidova", "Tojixon Shodiyeva", "Halima Nosirova", "Zulfiya", "Jahon Obidova.")
t.NAT("Imlo uch marta o‘zgartirildi.", "bu mahalliy aholini savodsiz qilish va qadriyatlardan mahrum qilishga xizmat qildi", "savodxonlik keskin oshdi", "milliy qadriyatlar mustahkamlandi", "ruslashtirish to‘xtadi", "Savodsizlik va ruslashtirish.")
t.NAT("«Hujum» kompaniyasida milliy qadriyatlar inobatga olinmadi.", "1927–1928-yillarda 2 500 dan ortiq faol ayol halok bo‘ldi", "ayollar to‘liq ozod bo‘ldi", "qarshilik bo‘lmadi", "kampaniya bekor qilindi", "Fojiali oqibatlar.")
t.NAT("Sovet hukumati ayollardan arzon ishchi kuchi sifatida foydalanishni ko‘zladi.", "xotin-qizlar artellar va yirik sanoat korxonalariga jalb qilindi", "ayollar ishdan ozod qilindi", "ayollar maktabdan chetlashtirildi", "ayollar faqat uyda ishladi", "Ayollar ishga jalb qilindi.")
t.NAT("Fitrat, Cho‘lpon, Qodiriy o‘z asarlari bilan milliy qadriyatlarni himoya qildi.", "adabiyot milliylik, insonparvarlik, xalqchillik tamoyillariga sodiq qoldi", "adabiyot faqat sovet tashviqotiga aylandi", "milliy adabiyot yo‘qoldi", "yozuvchilar xorijga ketdi", "Milliy tamoyillar saqlandi.")
t.TF("O‘zbek tilida o‘qitiladigan maktablar soni o‘n yilda 10 marta oshgan.", True, "To‘g‘ri.")
t.TF("Universitet va institutlarda talaba va o‘qituvchilarning ko‘pchiligi mahalliy millat vakillari edi.", False, "Noto‘g‘ri: mahalliy millatlar vakillari ozchilikni tashkil qilgan.")
t.TF4([("1930-yilda 50 dan ortiq artelda 5 000 dan ko‘p mahalliy ayol ishlagan.", True), ("1927-yilda tuman ijroiya qo‘mitalari a’zolarining 20 foizi ayollar edi.", True),
       ("Jahon Obidova va Tojixon Shodiyeva keyinchalik qatag‘on qilingan.", True), ("Kirill yozuviga faqat O‘zbekiston o‘tkazilgan.", False)],
      "4-noto‘g‘ri: O‘rta Osiyoning boshqa respublikalari va Ozarbayjon ham o‘tkazilgan.")
t.MUL([("Yunus Rajabiy va Muxtor Ashrafiy milliy musiqa rivojiga hissa qo‘shgan.", True),
       ("«Hujum» kompaniyasi 1926-yil sentyabrda e’lon qilingan.", True),
       ("Kirill yozuviga 1929-yilda o‘tilgan.", False)],
      "III noto‘g‘ri: 1929-yilda lotin yozuviga o‘tilgan; kirillga o‘tish qarori 1940-yilda.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["«Hujum» kompaniyasi e’lon qilindi", "ommaviy mitinglar – paranji yoqish", "lotin yozuviga o‘tildi", "Fanlar komiteti tuzildi", "Toshkent konservatoriyasi ochildi", "kirill yozuviga o‘tish qarori"],
      "1926-09 → 1927-03-08 → 1929-12-01 → 1932-10-14 → 1936 → 1940-05-08.")
t.MATCH("San’atkorlarni sohasi bilan moslashtiring.", ["Muxtor Ashrafiy", "Mannon Uyg‘ur", "Komil Yormatov", "Halima Nosirova"],
        ["kompozitor", "teatr rejissyori", "kinematografiya arbobi", "xonanda", "shoir"], 'abcd',
        "Ashrafiy – kompozitor; Uyg‘ur – rejissyor; Yormatov – kino; Nosirova – xonanda.")
t.VENN("Lotin yozuviga o‘tish", "Kirill yozuviga o‘tish",
       [("1929-yil Samarqand konferensiyasi qarori", 1), ("1929-yil 1-dekabrdan", 1),
        ("1940-yil 8-may qarori", 2), ("Ozarbayjon ham o‘tkazilgan", 2),
        ("sovet davridagi imlo o‘zgarishi", 3)],
       "Lotin – 1929; kirill – 1940; ikkalasi imlo o‘zgarishi.")
t.MAPN('uzb', ['Samarqand', 'Toshkent', 'Buxoro', 'Xiva'], "1929-yil mayda lotin grafikasiga o‘tish haqida qaror qabul qilingan konferensiya o‘tgan shahar xaritada qaysi raqamda?",
       "Samarqand.")

# 24-mavzu. Qatag‘onlik siyosati
t = Topic('y10u24', 10024); TOPICS['y10u24'] = t
t.B("«O‘n sakkizlar guruhi» ishiga kimlar tortilgan?", "Abdurahim Hojiboyev, Inomjon Xidiraliyev, Muxtorjon Saidjonov", "Rahim Inog‘omov", "Sa’dulla Qosimov", "Mannon Ramziy", "Hojiboyev, Xidiraliyev, Saidjonov va b.")
t.B("«Inog‘omovchilik» ishi kimning nomi bilan bog‘liq?", "Maorif xalq komissari Rahim Inog‘omov", "Oliy sud raisi Qosimov", "prokuror Badriddinov", "Munavvarqori", "Rahim Inog‘omov.")
t.B("«Qosimovchilik» ishi kimning nomi bilan bog‘liq?", "O‘zSSR Oliy sudi raisi Sa’dulla Qosimov", "Rahim Inog‘omov", "Shamsutdin Badriddinov", "Ashurali Zohiriy", "Sa’dulla Qosimov.")
t.B("«Botir gapchilar» ishi qayerda kim boshchiligidagi guruhga qo‘yilgan?", "Qo‘qonda Ashurali Zohiriy boshchiligidagi 19 kishiga", "Toshkentda Munavvarqoriga", "Samarqandda Inog‘omovga", "Buxoroda Qosimovga", "Qo‘qon, Ashurali Zohiriy, 19 kishi.")
t.B("Partiyani «tozalash» natijasida O‘zbekiston kompartiyasi a’zolarining necha foizi chiqarilgan?", "25,6 foizi", "50 foizi", "10 foizi", "75 foizi", "25,6 foizi.")
t.B("Munavvarqori boshchiligidagi 38 kishi qachon qamoqqa olingan?", "1929-yil 5-noyabrda", "1931-yil 25-aprelda", "1937-yil 28-oktyabrda", "1938-yil 4-oktyabrda", "1929-yil 5-noyabr, Toshkent.")
t.B("«Milliy ittihod» va «Milliy istiqlol» ishida jami nechta kishi qamalgan?", "87 kishi", "38 kishi", "15 kishi", "72 kishi", "87 kishi.")
t.B("1931-yil 25-aprelda Moskvadagi sud nechta kishini otib o‘ldirishga hukm qildi?", "15 nafar", "72 nafar", "87 nafar", "38 nafar", "15 nafar.")
t.B("Sa’dulla Qosimov qachon lavozimidan bo‘shatilib, qamoqqa olingan?", "1929-yil martda", "1932-yil mayda", "1937-yilda", "1931-yilda", "1929-yil mart.")
t.B("«Qosimovchilik» ishida sud qanday jazo tayinlagan?", "10 yil qamoq va mol-mulk musodarasi", "otib o‘ldirish", "surgun", "jarima", "10 yil qamoq, musodara.")
t.B("Badriddinov ustidan sud jarayoni qachon o‘tkazilgan?", "1932-yil 5-may – 15-iyunda", "1929-yil martda", "1938-yil oktyabrda", "1931-yil aprelda", "1932-yil 5-may – 15-iyun.")
t.B("Qamoqqa olingan ko‘plab yurtdoshlarimiz ommaviy ravishda qachon qatl etilgan?", "1938-yil 4-oktyabrda", "1937-yil 28-oktyabrda", "1931-yil 25-aprelda", "1940-yil 8-mayda", "1938-yil 4-oktyabr.")
t.B("Mirkomil Mirsharopov qayerda qamoqqa olingan?", "Maykopda", "Toshkentda", "Moskvada", "Xivada", "Maykopda, 1937-yil 28-oktyabr.")
t.B("Mirsharopov va 18 nafar o‘zbek komandirlari qachon otib tashlangan?", "1938-yil 10-oktyabrda", "1938-yil 4-oktyabrda", "1937-yil 28-oktyabrda", "1931-yil 25-aprelda", "1938-yil 10-oktyabr.")
t.B("«Shahidlar xotirasi» yodgorlik majmuasi qachon ochilgan?", "2000-yil 12-mayda", "1991-yil 31-avgustda", "1999-yilda", "2002-yilda", "2000-yil 12-may.")
t.B("«Shahidlar xotirasi» majmuasi qayerda joylashgan?", "Toshkentning Yunusobod tumanida, Bo‘zsuv kanali bo‘yida", "Samarqandda", "Moskva atrofida", "Qo‘qonda", "Toshkent, Bo‘zsuv bo‘yi.")
t.NAT("Tergov jarayoni Moskvaga ko‘chirildi.", "bu sovetlarning milliy-ma’naviy hayotga zug‘umidan dalolat berdi", "ayblanuvchilar oqlandi", "ish yopildi", "tergov tezlashdi", "Milliy hayotga zug‘um.")
t.NAT("Mirsharopov O‘zbek diviziyasini milliylashtirishda ayblandi.", "dastlabki O‘zbek diviziyasi tarqatildi va u 18 nafar komandir bilan otib tashlandi", "diviziya kengaytirildi", "Mirsharopov oqlandi", "diviziya mustaqil bo‘ldi", "Diviziya tarqatildi.")
t.NAT("O‘zbekiston mustaqillikka erishdi.", "qatag‘on qilinganlarning ko‘pchiligi oqlanib, pok nomlari tiklandi", "qatag‘onlar davom etdi", "arxivlar yopildi", "yodgorliklar buzildi", "Oqlanish.")
t.NAT("Sovet rejimi milliy rahbar xodimlarni lavozimlaridan chetlatdi.", "20-yillar oxiridan millat yetakchilarini jismonan yo‘qotishga kirishdi", "milliy kadrlar ko‘paydi", "rahbarlar Moskvaga ko‘tarildi", "rejim yumshadi", "Jismoniy qatag‘on.")
t.TF("Bu davrda ko‘plab madrasa, masjid va xonaqohlar buzib tashlangan.", True, "To‘g‘ri.")
t.TF("Moskvada otib tashlanganlardan ko‘pchiligi Toshkentga qaytib kelgan.", False, "Noto‘g‘ri: qamoqdan ham deyarli hech kim qaytib kelmagan.")
t.TF4([("«Narkompros» ishi Maorif xalq komissari Mannon Ramziyga tegishli.", True), ("Mirsharopov 19-tog‘li otliq O‘zbek diviziyasiga qo‘mondonlik qilgan.", True),
       ("Buzilmagan masjidlar ombor va garnizon manzilgohlariga aylantirilgan.", True), ("Munavvarqori ishi Toshkentda yakunlanib, hamma oqlangan.", False)],
      "4-noto‘g‘ri: tergov Moskvaga ko‘chirilib, 15 kishi otib tashlangan.")
t.MUL([("72 nafar kishi uzoq muddatli qamoq jazosiga hukm qilingan.", True),
       ("Qosimov va safdoshlari islom dinini himoya qilishda ayblangan.", True),
       ("«Botir gapchilar» Samarqandda faoliyat yuritgan.", False)],
      "III noto‘g‘ri: Qo‘qonda.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Qosimov qamoqqa olindi", "Munavvarqori va 38 kishi qamaldi", "Moskvada 15 kishi otishga hukm qilindi", "Badriddinov ustidan sud", "Mirsharopov qamoqqa olindi", "ommaviy qatl"],
      "1929-03 → 1929-11 → 1931-04 → 1932-05 → 1937-10 → 1938-10-04.")
t.MATCH("Siyosiy ishlarni shaxs bilan moslashtiring.", ["inog‘omovchilik", "qosimovchilik", "badriddinovchilik", "«narkompros» ishi"],
        ["Rahim Inog‘omov", "Sa’dulla Qosimov", "Shamsutdin Badriddinov", "Mannon Ramziy", "Munavvarqori"], 'abcd',
        "Inog‘omovchilik – Inog‘omov; qosimovchilik – Qosimov; badriddinovchilik – Badriddinov; narkompros – Ramziy.")
t.VENN("«Milliy istiqlol» ishi", "«Qosimovchilik»",
       [("Munavvarqori boshchiligida 87 kishi", 1), ("15 kishi Moskva atrofida otildi", 1),
        ("Oliy sud raisi va 6 safdoshi", 2), ("10 yil qamoq va musodara", 2),
        ("sovet rejimi o‘ylab topgan siyosiy ish", 3)],
       "Milliy istiqlol – Munavvarqori, 15 otilgan; qosimovchilik – Qosimov, 10 yil; ikkalasi soxta ish.")
t.MAPN('uzb', ['Qo‘qon', 'Toshkent', 'Samarqand', 'Buxoro'], "Ashurali Zohiriy boshchiligidagi 19 kishiga «botir gapchilar» ishi qo‘yilgan shahar xaritada qaysi raqamda?",
       "Qo‘qon.")
