from qlib import Topic, PLACES, REG
TOPICS = {}

# 4-mavzu. Harakatlar strategiyasidan Taraqqiyot strategiyasi sari
t = Topic('y11u4', 11004); TOPICS['y11u4'] = t
t.B("Harakatlar strategiyasi qaysi yillarni qamragan?", "2017–2021", "2022–2026", "2016–2020", "2023–2030", "2017–2021.")
t.B("Harakatlar strategiyasi nechta ustuvor yo‘nalishni qamragan?", "beshta", "uchta", "o‘nta", "yettita", "Beshta.")
t.B("2017-yil qanday nomlangan?", "«Xalq bilan muloqot va inson manfaatlari yili»", "«Faol investitsiyalar yili»", "«Ilm-ma’rifat yili»", "«Yoshlarni qo‘llab-quvvatlash yili»", "«Xalq bilan muloqot va inson manfaatlari yili».")
t.B("2020-yil qanday nomlangan?", "«Ilm-ma’rifat va raqamli iqtisodiyotni rivojlantirish yili»", "«Faol tadbirkorlik yili»", "«Xalq bilan muloqot yili»", "«Faol investitsiyalar yili»", "«Ilm-ma’rifat va raqamli iqtisodiyot yili».")
t.B("Harakatlar strategiyasi yillarida nechtaga yaqin yangi qonun qabul qilingan?", "300 ga yaqin", "30 ga yaqin", "3000 ga yaqin", "100 ga yaqin", "300 ga yaqin.")
t.B("«O‘zbekiston – 2030» strategiyasi qachon qabul qilingan?", "2023-yilda", "2021-yilda", "2017-yilda", "2030-yilda", "2023-yilda.")
t.B("«O‘zbekiston – 2030» strategiyasi nechta ustuvor yo‘nalishdan iborat?", "5 ta", "3 ta", "10 ta", "7 ta", "5 ta.")
t.B("Konstitutsiyaviy komissiya qachon tuzilgan?", "2022-yil 20-mayda", "2023-yil 30-aprelda", "2021-yilda", "2023-yil 9-iyulda", "2022-yil 20-may.")
t.B("Umumxalq muhokamasida nechtadan ortiq uchrashuv o‘tkazilgan?", "20 mingdan", "2 mingdan", "200 mingdan", "193 dan", "20 mingdan ortiq.")
t.B("Konstitutsiya loyihasida nechta davlat tajribasi o‘rganilgan?", "193", "143", "46", "20", "193 davlat.")
t.B("Yangi tahrirdagi Konstitutsiya bo‘yicha referendum qachon o‘tkazilgan?", "2023-yil 30-aprelda", "2023-yil 1-mayda", "2023-yil 9-iyulda", "2022-yil 20-mayda", "2023-yil 30-aprel.")
t.B("Yangi Konstitutsiya qachon kuchga kirgan?", "2023-yil 1-maydan", "2023-yil 30-apreldan", "2023-yil 9-iyuldan", "2024-yil 1-yanvardan", "1-maydan.")
t.B("Yangi Konstitutsiyada davlatning ijtimoiy majburiyatlari necha barobar ko‘paytirilgan?", "3 barobar", "2 barobar", "10 barobar", "5 barobar", "3 barobar.")
t.B("Muddatidan ilgari Prezident saylovi Konstitutsiyaning qaysi moddasiga asosan o‘tkazilgan?", "128-moddasi", "17-moddasi", "150-moddasi", "1-moddasi", "128-modda.")
t.B("Muddatidan ilgari Prezident saylovi qachon bo‘lgan?", "2023-yil 9-iyulda", "2021-yilda", "2023-yil 30-aprelda", "2016-yil 4-dekabrda", "2023-yil 9-iyul.")
t.NAT("Harakatlar strategiyasi asosida har yili alohida davlat dasturlari qabul qilindi.", "parlament roli kuchayib, partiyalar faollashdi, saylovlar ochiq va raqobatli bo‘ldi", "islohotlar to‘xtadi", "parlament tarqatildi", "saylovlar bekor qilindi", "Siyosiy hayot jonlandi.")
t.NAT("Mamlakat taraqqiyotining yangi bosqichida Konstitutsiyani takomillashtirish dolzarb bo‘ldi.", "2022-yil 20-mayda Konstitutsiyaviy komissiya tuzildi", "Konstitutsiya bekor qilindi", "eski Konstitutsiya o‘zgarishsiz qoldi", "referendum taqiqlandi", "Komissiya tuzildi.")
t.NAT("Umumxalq muhokamasida 10 minglab taklif kelib tushdi.", "bu xalq davlat boshqaruvida faol ishtirok etayotganini ko‘rsatdi", "xalq befarqligini ko‘rsatdi", "muhokama bekor qilindi", "takliflar inobatga olinmadi", "Xalq faolligi.")
t.NAT("Prezident 128-moddaga asosan muddatidan ilgari saylov tashabbusini ilgari surdi.", "tashabbus partiyalar va jamoatchilik tomonidan qo‘llab-quvvatlanib, 2023-yil 9-iyulda saylov o‘tkazildi", "tashabbus rad etildi", "saylov 2026-yilga qoldirildi", "Prezident lavozimi bekor qilindi", "Muddatidan ilgari saylov.")
t.TF("Yangi Konstitutsiyada «O‘zbekiston – suveren, demokratik, huquqiy, ijtimoiy va dunyoviy davlat» tamoyili mustahkamlangan.", True, "To‘g‘ri.")
t.TF("2021-yilda Shavkat Mirziyoyev birinchi marta Prezident etib saylangan.", False, "Noto‘g‘ri: 2021-yilda qayta saylangan; birinchi marta 2016-yilda.")
t.TF4([("Prezident konstitutsiyaviy islohot ijrosini uch bosqichda belgilagan.", True), ("2018-yil «Faol tadbirkorlik, innovatsion g‘oyalar va texnologiyalarni qo‘llab-quvvatlash yili» deb nomlangan.", True),
       ("«O‘zbekiston – 2030» suv resurslarini tejashni ko‘zda tutadi.", True), ("2021-yil «Faol investitsiyalar va ijtimoiy rivojlanish yili» deb nomlangan.", False)],
      "4-noto‘g‘ri: 2021 – «Yoshlarni qo‘llab-quvvatlash va aholi salomatligini mustahkamlash yili»; 2019 – «Faol investitsiyalar».")
t.MUL([("«O‘zbekiston – 2030» daromadi o‘rtachadan yuqori davlatlar qatoriga kirishni ko‘zlaydi.", True),
       ("«O‘zbekiston – 2030» ni amalga oshirish barcha davlat organlarining eng ustuvor vazifasi.", True),
       ("Yangi Konstitutsiya Oliy Majlis qarori bilan, referendumsiz qabul qilingan.", False)],
      "III noto‘g‘ri: 2023-yil 30-aprel referendumida qabul qilingan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Harakatlar strategiyasi e’lon qilindi", "Sh. Mirziyoyev qayta saylandi, Taraqqiyot strategiyasi", "Konstitutsiyaviy komissiya tuzildi", "Konstitutsiya referendumi", "muddatidan ilgari Prezident saylovi"],
      "2017 → 2021 → 2022-05-20 → 2023-04-30 → 2023-07-09.")
t.MATCH("Yillarni nomi bilan moslashtiring.", ["2017", "2018", "2019", "2021"],
        ["Xalq bilan muloqot va inson manfaatlari yili", "Faol tadbirkorlik, innovatsion g‘oyalar va texnologiyalarni qo‘llab-quvvatlash yili", "Faol investitsiyalar va ijtimoiy rivojlanish yili", "Yoshlarni qo‘llab-quvvatlash va aholi salomatligini mustahkamlash yili", "Ilm-ma’rifat va raqamli iqtisodiyot yili"], 'abcd',
        "2017 – muloqot; 2018 – tadbirkorlik; 2019 – investitsiyalar; 2021 – yoshlar.")
t.VENN("Harakatlar strategiyasi", "«O‘zbekiston – 2030»",
       [("2017–2021-yillar", 1), ("har yilga nom berilgan", 1),
        ("2023-yilda qabul qilingan", 2), ("daromadi o‘rtachadan yuqori davlatlar qatoriga kirish", 2),
        ("beshta ustuvor yo‘nalish", 3)],
       "Harakatlar – 2017–2021; 2030 – 2023-yil; ikkalasida 5 yo‘nalish.")
t.MAPN('uzb', ['Toshkent', 'Samarqand', 'Buxoro', 'Nukus'], "Yangi tahrirdagi Konstitutsiya qabul qilingan O‘zbekiston Respublikasining poytaxti xaritada qaysi raqamda?",
       "Toshkent.")

# 5-mavzu. Qurolli kuchlar va milliy armiya
t = Topic('y11u5', 11005); TOPICS['y11u5'] = t
t.B("Chegara qo‘shinlari boshqarmasi qachon tashkil etilgan?", "1992-yilda", "1991-yilda", "1995-yilda", "2001-yilda", "1992-yilda.")
t.B("Konstitutsiyada Qurolli Kuchlarning Oliy Bosh Qo‘mondoni kim deb belgilangan?", "Prezident", "Mudofaa vaziri", "Bosh vazir", "Senat raisi", "Prezident.")
t.B("Vatan himoyachilari kuni qaysi sana?", "14-yanvar", "1-sentyabr", "25-oktyabr", "26-sentyabr", "14-yanvar (1993-yildan).")
t.B("Harbiy doktrina qachon qabul qilingan?", "1995-yilda", "2003-yilda", "2018-yilda", "1992-yilda", "1995-yilda.")
t.B("2003-yilda Harbiy doktrina qanday nom oldi?", "Mudofaa doktrinasi", "Xavfsizlik doktrinasi", "Harbiy strategiya", "Milliy konsepsiya", "Mudofaa doktrinasi.")
t.B("«Mudofaa doktrinasi to‘g‘risida»gi qonun qachon imzolangan?", "2018-yil 9-yanvarda", "2003-yilda", "1995-yilda", "2018-yil 10-yanvarda", "2018-yil 9-yanvar.")
t.B("Harbiy litseylar qanday nom oldi?", "«Temurbeklar maktabi»", "«Mard o‘g‘lon»", "«Vatan himoyachisi»", "«Kadetlar»", "«Temurbeklar maktabi».")
t.B("Jasorat ko‘rsatgan yoshlarga beriladigan davlat mukofoti qaysi?", "«Mard o‘g‘lon»", "«Shon-sharaf»", "«Jasorat»", "«Do‘stlik»", "«Mard o‘g‘lon».")
t.B("2018-yilda Qurolli Kuchlarning jangovar shayligi necha soatga tushirilgan?", "3 soatga", "5 kunga", "24 soatga", "1 soatga", "5 kundan 3 soatga.")
t.B("Ichki ishlar xodimlari kuni qaysi sana?", "25-oktyabr", "14-yanvar", "26-sentyabr", "1-sentyabr", "25-oktyabr (2006-yildan).")
t.B("Chet elda xizmat qilgan o‘zbek ofitserlari qaysi yillarda vatanga qayta boshlagan?", "1991–1994", "2001–2005", "1985–1990", "2017–2021", "1991–1994.")
t.B("«Xavfsiz shahar» va «Xavfsiz hudud» loyihalari qaysi yillarda joriy etilgan?", "2019–2021", "2001–2005", "1995–1999", "2010–2015", "2019–2021.")
t.B("O‘zbekiston Milliy xavfsizlik xizmati (MXX) qachon tashkil etilgan?", "1991-yil 26-sentyabrda", "1991-yil 31-avgustda", "1995-yilda", "2018-yilda", "1991-yil 26-sentyabr.")
t.B("Prezident huzurida Xavfsizlik kengashi qachon tuzilgan?", "1995-yilda", "1991-yilda", "2018-yilda", "1999-yilda", "1995-yilda.")
t.B("Favqulodda vaziyatlar vazirligi qachon tashkil etilgan?", "1996-yilda", "1991-yilda", "2005-yilda", "2019-yilda", "1996-yilda.")
t.B("Andijon voqealari qachon yuz bergan?", "2005-yilda", "1999-yilda", "2000-yilda", "2018-yilda", "2005-yilda.")
t.B("MXX qachon Davlat xavfsizlik xizmati (DXX) sifatida qayta tashkil etilgan?", "2018-yilda", "2005-yilda", "2021-yilda", "1995-yilda", "2018-yilda.")
t.B("DXX xodimlarining kasb bayrami qaysi sana?", "26-sentyabr", "25-oktyabr", "14-yanvar", "31-avgust", "26-sentyabr (2021-yildan belgilangan).")
t.NAT("Mustaqillikdan so‘ng Ichki ishlar va DXQ O‘zbekiston tasarrufiga o‘tdi, Mudofaa vazirligi tashkil etildi.", "O‘zbekiston o‘z harbiy siyosatini yuritishiga zamin yaratildi", "armiya tarqatildi", "SSSR qo‘shinlari kuchaydi", "xavfsizlik zaiflashdi", "Mustaqil harbiy siyosat.")
t.NAT("1999–2000-yillarda terrorchilik xavfi kuchaydi.", "«Terrorizmga qarshi kurash to‘g‘risida»gi qonun qabul qilindi", "chegaralar ochildi", "armiya qisqartirildi", "Xavfsizlik kengashi tugatildi", "Terrorizmga qarshi qonun.")
t.NAT("2019-yildan vazirliklar tarkibida yangi akademik litseylar tashkil etildi.", "Samarqand va Urganchdagi «Temurbeklar maktabi» faoliyati tugatildi", "barcha harbiy litseylar yopildi", "litseylar xorijga ko‘chirildi", "Temurbeklar maktabi kengaydi", "Temurbeklar maktabi qisman tugatildi.")
t.NAT("2017-yilda ichki ishlar organlari faoliyati tubdan qayta ko‘rildi.", "tizim yanada samarali, tezkor va zamon talablariga mos bo‘ldi", "tizim tugatildi", "xodimlar qisqartirildi", "tizim harbiylarga topshirildi", "Samaradorlik oshdi.")
t.TF("Konstitutsiyada Vatan himoyasi har bir fuqaroning muqaddas burchi deb belgilangan.", True, "To‘g‘ri.")
t.TF("DXX MXX ning faqat nomini o‘zgartirish natijasida tuzilgan, vazifalari o‘zgarmagan.", False, "Noto‘g‘ri: nomi bilan birga mazmuni o‘zgarib, vazifalari kengaygan.")
t.TF4([("2001-yildan serjantlar tayyorlash maktablari ochilgan.", True), ("Mudofaa doktrinasi axborot xavfsizligini ham o‘z ichiga oladi.", True),
       ("Qurolli Kuchlar akademiyasi mustaqillikning ilk yillarida ochilgan.", True), ("DXX chegaralarni qo‘riqlash vazifasini bajarmaydi.", False)],
      "4-noto‘g‘ri: davlat chegaralarini qo‘riqlash DXX vazifalaridan biri.")
t.MUL([("2018-yil 10-yanvarda Xavfsizlik kengashining ilk ochiq videokonferensiya yig‘ilishi bo‘lgan.", True),
       ("Chirchiq va Samarqandda harbiy bilim yurtlari tashkil etilgan.", True),
       ("Vatan himoyachilari kuni 2006-yildan nishonlanadi.", False)],
      "III noto‘g‘ri: 1993-yildan; 2006-yildan – Ichki ishlar xodimlari kuni.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["MXX tashkil etildi", "Chegara qo‘shinlari boshqarmasi", "Harbiy doktrina qabul qilindi", "Favqulodda vaziyatlar vazirligi", "Mudofaa doktrinasi deb o‘zgartirildi", "MXX DXXga aylantirildi"],
      "1991 → 1992 → 1995 → 1996 → 2003 → 2018.")
t.MATCH("Kasb bayramlarini sanasi bilan moslashtiring.", ["Vatan himoyachilari kuni", "Ichki ishlar xodimlari kuni", "DXX xodimlari kuni", "Mustaqillik kuni"],
        ["14-yanvar", "25-oktyabr", "26-sentyabr", "1-sentyabr", "8-dekabr"], 'abcd',
        "14-yanvar; 25-oktyabr; 26-sentyabr; 1-sentyabr.")
t.VENN("Qurolli Kuchlar", "Davlat xavfsizlik xizmati",
       [("Oliy Bosh Qo‘mondon – Prezident", 1), ("Mudofaa doktrinasi asosida", 1),
        ("razvedka va kontrrazvedka", 2), ("1991-yil 26-sentyabrda asos solingan", 2),
        ("mamlakat xavfsizligini ta’minlaydi", 3)],
       "Qurolli Kuchlar – Oliy Bosh Qo‘mondon; DXX – razvedka, 26-sentyabr; ikkalasi xavfsizlik.")
t.MAPMATCH('uzb', ['Chirchiq', 'Samarqand', 'Urganch', 'Andijon'],
           ["harbiy bilim yurti tashkil etilgan, Toshkent yaqinidagi shahar", "harbiy bilim yurti va «Temurbeklar maktabi» bo‘lgan Zarafshon vodiysi shahri", "«Temurbeklar maktabi» faoliyati tugatilgan Xorazm shahri", "2005-yilda tartibsizliklar yuz bergan shahar"],
           "1 – Chirchiq; 2 – Samarqand; 3 – Urganch; 4 – Andijon.")
