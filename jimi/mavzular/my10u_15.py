from qlib import Topic, PLACES, REG
TOPICS = {}

# 28-mavzu. Fan va madaniyat g‘alaba uchun
t = Topic('y10u28', 10028); TOPICS['y10u28'] = t
t.B("«Yovga o‘lim!» she’ri muallifi kim?", "Oybek", "Hamid Olimjon", "G‘afur G‘ulom", "Zulfiya", "Oybek.")
t.B("«Qo‘lingga qurol ol!» she’ri muallifi kim?", "Hamid Olimjon", "Oybek", "Maqsud Shayxzoda", "Mirtemir", "Hamid Olimjon.")
t.B("Urush yillarida qaysi almanax chop etilgan?", "«Biz yengamiz!»", "«Qirq birinchi yil olmasi»", "«Front bo‘ylab»", "«Urush yo‘llarida»", "«Biz yengamiz!».")
t.B("Oybekning «Navoiy» romani qachon chop etilgan?", "1944-yilda", "1941-yilda", "1943-yilda", "1945-yilda", "1944-yilda.")
t.B("Oybekning nasriy jangnomasi qanday ataladi?", "«Front bo‘ylab»", "«Yovga o‘lim!»", "«Navoiy»", "«Biz yengamiz!»", "«Front bo‘ylab».")
t.B("«Urush yo‘llarida» turkum asarlarini kim yaratgan?", "O‘rol Tansiqboyev", "Muxtor Ashrafiy", "Oybek", "Abror Hidoyatov", "O‘rol Tansiqboyev.")
t.B("Usmon Nosir qachon va qayerda vafot etgan?", "1944-yilda Kemerovodagi lagerda", "1941-yilda frontda", "1937-yilda Toshkentda", "1945-yilda Berlinda", "1944-yil, Kemerovo lageri.")
t.B("«Qahramonlik simfoniyasi»ni kim yaratgan?", "Muxtor Ashrafiy", "Yunus Rajabiy", "To‘xtasin Jalilov", "Mutavakkil Burhonov", "Muxtor Ashrafiy, 1942-yil.")
t.B("Konsert brigadalari frontdagi jangchilarga nechtadan ortiq konsert bergan?", "35 mingdan", "20 mingdan", "3 500 dan", "350 mingdan", "35 mingdan ortiq.")
t.B("O‘zbekiston SSR Fanlar akademiyasi qachon tashkil etilgan?", "1943-yil 4-noyabrda", "1932-yil 14-oktyabrda", "1945-yilda", "1941-yilda", "1943-yil 4-noyabr.")
t.B("Fanlar akademiyasining ilk prezidenti kim?", "Toshmuhammad Qori-Niyoziy", "Oybek", "Sharof Rashidov", "Eshon Boboxon", "Toshmuhammad Qori-Niyoziy.")
t.B("Fanlar akademiyasi mutaxassislari qaysi GES loyihasini ishlab chiqqan?", "Farhod GESi", "Chorvoq GESi", "Chirchiq GESi", "Norin GESi", "Farhod GESi.")
t.B("1945-yilga kelib Fanlar akademiyasida nechta ilmiy-tadqiqot instituti bo‘lgan?", "20 ta", "2 ta", "200 ta", "10 ta", "20 ta.")
t.B("Dinga qarshi targ‘ibot yuritgan qaysi tashkilot tugatilgan?", "«Jangovar xudosizlar ittifoqi»", "«Qo‘shchi»", "Komsomol", "«Hujum»", "«Jangovar xudosizlar ittifoqi».")
t.B("Toshkentda musulmon vakillari qurultoyi qachon bo‘lgan?", "1943-yil 20-oktyabrda", "1944-yil sentyabrda", "1943-yil 4-noyabrda", "1941-yil 23-iyunda", "1943-yil 20-oktyabr.")
t.B("O‘rta Osiyo va Qozog‘iston musulmonlari diniy boshqarmasining muftiysi etib kim saylangan?", "Eshon Boboxon", "Qori-Niyoziy", "Hasan Islomov", "Munavvarqori", "Eshon Boboxon.")
t.B("Dinga qarshi eski ta’qiblar qachon qayta boshlangan?", "1944-yil sentyabrda", "1943-yil oktyabrda", "1945-yil mayda", "1941-yil iyunda", "1944-yil sentyabr.")
t.NAT("G‘arb davlatlari ittifoq uchun dindorlarga qarshi siyosatni o‘zgartirishni talab qildi.", "sovet hukumati din siyosatini vaqtincha o‘zgartirdi", "ittifoq tuzilmadi", "dinga qarshi kurash kuchaydi", "masjidlar buzildi", "Diniy siyosat yumshadi.")
t.NAT("Muxtor Ashrafiy davlat mukofotiga sazovor bo‘ldi.", "u mukofot pulini samolyot va tank kolonnalari fondiga topshirdi", "u pulni o‘ziga oldi", "u xorijga ketdi", "u mukofotdan voz kechdi", "Pul fondga topshirildi.")
t.NAT("Urushda sovet hokimiyatining saqlanishi aniq bo‘lib qoldi.", "hukumat dinga nisbatan siyosatini yana o‘zgartirib, ta’qiblarni boshladi", "diniy erkinlik kengaydi", "diniy boshqarma kuchaydi", "cherkovlar ko‘paydi", "Ta’qiblar qaytdi.")
t.NAT("Front oldi hududlaridan yozuvchilar evakuatsiya qilindi.", "rus, ukrain, belorus yozuvchilari bilan adabiy hamkorlik olib borildi", "adabiy hayot to‘xtadi", "yozuvchilar Moskvaga qaytarildi", "kitob nashri to‘xtadi", "Adabiy hamkorlik.")
t.TF("Shuhrat va Sharof Rashidov jang maydonlarida dushmanga qarshi kurashgan.", True, "To‘g‘ri.")
t.TF("Urush yillarida «Bezbojnik» jurnali kengaytirilgan.", False, "Noto‘g‘ri: «Bezbojnik» jurnali yopilgan.")
t.TF4([("1944-yilda barcha dinlar uchun «Din ishlari bo‘yicha vakillik» tuzilgan.", True), ("Tamaraxonim va Halima Nosirova front konsert brigadalarida bo‘lgan.", True),
       ("Qori-Niyoziy mashhur matematik olim bo‘lgan.", True), ("Obidjon Abdurahmonov va Sulton Jo‘ra frontdan sog‘-omon qaytgan.", False)],
      "4-noto‘g‘ri: ular jang maydonlaridan qaytmagan.")
t.MUL([("Gospital va harbiy qismlarga 20 mingta konsert berilgan.", True),
       ("Frontdagi o‘zbek gazetalarida Jalolxon Azizxonov faoliyat yuritgan.", True),
       ("Fanlar akademiyasi 1950-yilda tashkil etilgan.", False)],
      "III noto‘g‘ri: 1943-yil 4-noyabrda tashkil etilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["«Qahramonlik simfoniyasi» yaratildi", "musulmonlar qurultoyi", "Fanlar akademiyasi tashkil etildi", "«Navoiy» romani chop etildi", "dinga qarshi ta’qiblar qayta boshlandi"],
      "1942 → 1943-10-20 → 1943-11-04 → 1944 → 1944-09.")
t.MATCH("Ijodkorlarni asari bilan moslashtiring.", ["Oybek", "Hamid Olimjon", "Muxtor Ashrafiy", "O‘rol Tansiqboyev"],
        ["«Yovga o‘lim!»", "«Qo‘lingga qurol ol!»", "«Qahramonlik simfoniyasi»", "«Urush yo‘llarida»", "«Biz yengamiz!»"], 'abcd',
        "Oybek – Yovga o‘lim; Olimjon – Qo‘lingga qurol ol; Ashrafiy – simfoniya; Tansiqboyev – Urush yo‘llarida.")
t.VENN("1943-yildagi diniy siyosat", "1944-yil sentyabrdan keyingi siyosat",
       [("musulmonlar diniy boshqarmasi tuzildi", 1), ("«Bezbojnik» yopildi", 1),
        ("dinga qarshi ta’qiblar qayta boshlandi", 2), ("hukumat sovet hokimiyati saqlanishiga ishonch hosil qildi", 2),
        ("kommunistik partiya nazoratidagi siyosat", 3)],
       "1943 – yumshash; 1944 – ta’qiblar; ikkalasi partiya nazoratida.")
t.MAPN('uzb', ['Toshkent', 'Samarqand', 'Buxoro', 'Qo‘qon'], "1943-yil 20-oktyabrda musulmonlar qurultoyi o‘tgan va Fanlar akademiyasi tashkil etilgan shahar xaritada qaysi raqamda?",
       "Toshkent.")

# 29-mavzu. Urushdan keyingi xalq xo‘jaligi
t = Topic('y10u29', 10029); TOPICS['y10u29'] = t
t.B("O‘zbekiston urush yillarida aholisining qancha qismini yo‘qotgan?", "10 foiziga yaqinini", "50 foizini", "1 foizini", "30 foizini", "10 foizga yaqin.")
t.B("O‘zbekiston iqtisodining necha foizi urush xarajatlariga yo‘naltirilgan?", "60 foizi", "10 foizi", "90 foizi", "30 foizi", "60 foizi.")
t.B("Qaysi yillarda paxta reja topshiriqlari bajarilmagan?", "1949- va 1950-yillarda", "1946- va 1947-yillarda", "1955-yilda", "1960-yilda", "1949–1950-yillarda.")
t.B("To‘rtinchi besh yillikda paxta maydoni qanchaga ko‘paygan?", "148 ming gektarga", "14 ming gektarga", "1 million gektarga", "48 ming gektarga", "148 ming gektar.")
t.B("Kolxozlarni yiriklashtirish siyosati qachon boshlangan?", "1950-yilda", "1930-yilda", "1945-yilda", "1966-yilda", "1950-yilda.")
t.B("1952-yil fevraldagi X plenumda qaysi xalq dostoni jaholatparastlikda ayblangan?", "«Alpomish»", "«Go‘ro‘g‘li»", "«Qirq qiz»", "«Kuntug‘mish»", "«Alpomish».")
t.B("«Feodal o‘tmishni ideallashtirgan»likda ayblanib qatag‘on qilinganlardan biri kim?", "Oybek", "Sharof Rashidov", "Qori-Niyoziy", "Muxtor Ashrafiy", "Oybek, Shayxzoda, Shukrullo va b.")
t.B("Sharof Rashidov qachon Kompartiya MK birinchi sekretari etib saylangan?", "1959-yil 15-martda", "1950-yilda", "1966-yilda", "1977-yilda", "1959-yil 15-mart.")
t.B("Sharof Rashidov qayerda tug‘ilgan?", "Jizzaxda", "Toshkentda", "Samarqandda", "Buxoroda", "1917-yil 8-noyabr, Jizzax.")
t.B("Rashidov 1950–1959-yillarda qanday lavozimda ishlagan?", "O‘zSSR Oliy Soveti Prezidiumi raisi", "XKS raisi", "Fanlar akademiyasi prezidenti", "Toshkent meri", "Oliy Sovet Prezidiumi raisi.")
t.B("Toshkent metropoliteni birinchi navbati qachon ishga tushirilgan?", "1977-yil noyabrda", "1966-yilda", "1983-yilda", "1970-yilda", "1977-yil noyabr, 9 bekat.")
t.B("Toshkent metropoliteni birinchi navbatida nechta bekat bo‘lgan?", "9 ta", "19 ta", "29 ta", "5 ta", "9 ta.")
t.B("SSSRning yangi Konstitutsiyasi qachon qabul qilingan?", "1977-yil 7-oktyabrda", "1978-yilda", "1936-yilda", "1966-yilda", "1977-yil 7-oktyabr.")
t.B("O‘zSSR o‘z Konstitutsiyasini qachon qabul qilgan?", "1978-yilda", "1977-yilda", "1927-yilda", "1991-yilda", "1978-yilda.")
t.B("Mas’ul lavozimlarga faqat partiya a’zolarini tayinlash tartibi qanday atalgan?", "partiya nomenklaturasi", "mahalliylashtirish", "kollektivlashtirish", "razvyorstka", "Partiya nomenklaturasi.")
t.B("60–80-yillarda O‘zbekistonda nechta millat va elat yashagan?", "127 ta", "18 ta", "100 ta", "50 ta", "127 ta.")
t.B("Ittifoqqa bo‘ysunuvchi «yopiq shaharlar»dan biri qaysi?", "Navoiy", "Samarqand", "Jizzax", "Qo‘qon", "Navoiy, Zarafshon, Uchquduq.")
t.NAT("Moskva paxtachilik bo‘yicha juda baland reja qo‘ydi.", "1949–1950-yillarda reja topshiriqlari bajarilmadi", "reja oshirib bajarildi", "paxta ekish to‘xtadi", "reja bekor qilindi", "Reja bajarilmadi.")
t.NAT("XX asrning 60-yillaridan sug‘oriladigan maydonlar kengaydi.", "Orolga quyiladigan suv kamayib, dengiz quriy boshladi", "Orol sathi ko‘tarildi", "baliq ko‘paydi", "ekologiya yaxshilandi", "Orol fojiasi.")
t.NAT("1977-yilgi SSSR Konstitutsiyasi qabul qilindi.", "milliy respublikalar huquqi rasmiy cheklanib, Markazga keng vakolatlar berildi", "respublikalar mustaqil bo‘ldi", "partiya hokimiyati cheklandi", "Markaz vakolati qisqardi", "Respublikalar huquqi cheklandi.")
t.NAT("Yopiq shaharlarga boshqa mintaqalardan ishchi kuchi olib kelindi.", "bu shaharlar mahalliy hokimiyatga bo‘ysunmay, faqat Markazga hisob berdi", "shaharlar mahalliy hokimiyatga topshirildi", "korxonalar yopildi", "mahalliy aholi ko‘chirildi", "Markazga bo‘ysungan.")
t.TF("Rashidov 1966-yilgi zilziladan so‘ng Toshkentni tiklashga ko‘p kuch sarflagan.", True, "To‘g‘ri.")
t.TF("1970–1980-yillarda ruslashtirish siyosati susaygan.", False, "Noto‘g‘ri: yanada kuchaygan.")
t.TF4([("Paxta maydonlari kolxozchilarning shaxsiy yerlari hisobidan kengaytirilgan.", True), ("Mirzacho‘l, Surxon-Sherobod, Qarshi cho‘llari o‘zlashtirilgan.", True),
       ("Oliy Sovet masalalarni partiya komitetisiz mustaqil hal qilgan.", False), ("Toshkent metropoliteni Rashidov tashabbusi bilan qurila boshlangan.", True)],
      "3-noto‘g‘ri: Oliy Sovet partiya komitetlari ruxsatisiz hech qaysi masalani hal qila olmagan.")
t.MUL([("Kon-metallurgiya sanoati O‘zbekistonning industrial qiyofasini o‘zgartirgan.", True),
       ("1970-yillarda «rivojlangan sotsialistik jamiyat» qurilgani e’lon qilingan.", True),
       ("Urushdan keyin iqtisodiyotning xomashyo yo‘nalishi kamaygan.", False)],
      "III noto‘g‘ri: xomashyo yo‘nalishi yanada mustahkamlangan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["kolxozlarni yiriklashtirish boshlandi", "X plenum «Alpomish»ni qoraladi", "Rashidov MK birinchi sekretari bo‘ldi", "Toshkent zilzilasi", "SSSR yangi Konstitutsiyasi", "metroning birinchi navbati"],
      "1950 → 1952-02 → 1959-03-15 → 1966 → 1977-10-07 → 1977-11.")
t.MATCH("Atamalarni izohi bilan moslashtiring.", ["partiya nomenklaturasi", "yopiq shaharlar", "paxta «fronti»", "Orol fojiasi"],
        ["partiya bilan kelishib tayinlanadigan lavozimlar", "Markazga bo‘ysunuvchi maxfiy korxonali shaharlar", "paxta rejalarini bajarishdagi zo‘riqish", "dengizning qurib borishi", "kolxozlarni yiriklashtirish"], 'abcd',
        "Nomenklatura – lavozimlar; yopiq shaharlar – maxfiy; paxta fronti – rejalar; Orol – qurish.")
t.VENN("Urushdan keyingi paxtachilik", "Urushdan keyingi sanoat",
       [("4-besh yillikda maydon 148 ming ga oshdi", 1), ("shaxsiy yerlar hisobidan kengaydi", 1),
        ("neft, ko‘mir, po‘lat ishlab chiqarish oshdi", 2), ("yopiq shaharlar qurildi", 2),
        ("xomashyo yo‘nalishidagi sovet iqtisodiyoti", 3)],
       "Paxta – 148 ming ga; sanoat – neft, yopiq shaharlar; ikkalasi xomashyo yo‘nalishi.")
t.MAPMATCH('uzb', ['Jizzax', 'Navoiy', 'Uchquduq', 'Toshkent'],
           ["1917-yilda Sharof Rashidov tug‘ilgan shahar", "ittifoqqa bo‘ysunuvchi kon-metallurgiya «yopiq shahri»", "Qizilqumdagi «yopiq shahar»", "1977-yilda metropoliten ochilgan poytaxt"],
           "1 – Jizzax; 2 – Navoiy; 3 – Uchquduq; 4 – Toshkent.")
