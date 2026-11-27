from qlib import Topic
TOPICS = {}
AF = 'africa'; EU = 'europe'

# 33 Shimoliy Afrika mamlakatlari
t = Topic('e9j33', 9133); TOPICS['e9j33'] = t
t.B("Shimoliy Afrikada aholining ko‘pchiligini kimlar tashkil etgan?", "arablar", "barbarlar", "habashlar", "yevropaliklar", "Arablar.")
t.B("XIX asr oxiri – XX asr boshida Misr va Sudan kimning mustamlakasiga aylangan?", "Buyuk Britaniyaning", "Fransiyaning", "Italiyaning", "Ispaniyaning", "Buyuk Britaniyaning.")
t.B("Al-Azhar madrasasi mudarrisi bo‘lgan milliy ozodlik harakati arbobi kim?", "Jamoliddin al-Afg‘oniy", "Ahmad Orabibey", "Saad Zaglul", "Muhammad Ahmad", "Jamoliddin al-Afg‘oniy.")
t.B("1871-yilda Jamoliddin al-Afg‘oniy qanday partiya tuzgan?", "«Xizb ul-Vatan» («Vatan partiyasi»)", "«Yosh Jazoir»", "«Birlik va taraqqiyot»", "«Ittihodi Muhammadi»", "«Xizb ul-Vatan».")
t.B("«Vatan partiyasi» qanday shior ostida kurashgan?", "«Misr misrliklarniki»", "«Ozodlik yoki o‘lim»", "«Yer va ozodlik»", "«Svaraj»", "«Misr misrliklarniki».")
t.B("Britaniya 1882-yilda qaysi shaharni to‘plardan o‘qqa tutgan?", "Iskandariyani", "Qohirani", "Xartumni", "Suvayshni", "Iskandariyani.")
t.B("Qohirada Muvaqqat kengash tuzgan Misr qo‘shini rahbari kim?", "Ahmad Orabibey", "Saad Zaglul", "Abdul Qodir", "Jamoliddin al-Afg‘oniy", "Ahmad Orabibey.")
t.B("Ahmad Orabibey qayerga umrbod surgun qilingan?", "Seylon oroliga", "Kiprga", "Maltaga", "Madagaskarga", "Seylon oroliga.")
t.B("Suvaysh kanalidan foydalanish bo‘yicha konvensiya qachon va qayerda imzolangan?", "1888-yilda Istanbulda", "1882-yilda Qohirada", "1869-yilda Parijda", "1904-yilda Londonda", "1888-yilda Istanbulda.")
t.B("1881-yilda o‘zini mahdiy deb e’lon qilgan sudanlik yetakchi kim?", "Muhammad Ahmad", "Abdulloh", "Samori Ture", "Menelik", "Muhammad Ahmad.")
t.B("Sudanga yuborilgan ingliz qo‘shini qaysi generallar boshchiligida yo‘q qilingan?", "Xiks va Gordon", "Kitchener va Rods", "Shliffen va Mak-Magon", "Troshyu va Dafferin", "Xiks va Gordon qo‘shinlari.")
t.B("Mustaqil mahdiylar davlati qachon tuzilgan?", "1885-yilda", "1881-yilda", "1889-yilda", "1898-yilda", "1885-yilda.")
t.B("Mahdiylar davlatining poytaxti qaysi shahar edi?", "Omdurman", "Xartum", "Qohira", "Iskandariya", "Omdurman.")
t.B("1912-yilda Jazoirda qanday partiya tuzilgan?", "«Yosh Jazoir»", "«Xizb ul-Vatan»", "«Yosh turklar»", "«Ansorlar»", "«Yosh Jazoir».")
t.B("Italiya Liviyaga qachon bosqinchilik urushi boshlagan?", "1911-yil 29-sentabrda", "1912-yilda", "1896-yilda", "1907-yilda", "1911-yil 29-sentabrda.")
t.NAT("1907-yilda Marokash shahrida fransuz shifokori o‘ldirildi.", "Fransiya urush boshlab, Marokashning barcha asosiy shaharlarini bosib oldi", "Fransiya Marokashdan chiqdi", "Marokash mustaqil bo‘ldi", "Ispaniya Fransiyaga urush e’lon qildi", "Bu urushga bahona bo‘ldi.")
t.NAT("Mahdiylar davlatida ichki nizo kuchaydi.", "Britaniya Efiopiyani Sudanga qarshi gijgijlab, 1889-yilda Sudanning asosiy qismini bosib oldi", "mahdiylar butun Afrikani egalladi", "Efiopiya Sudanga qo‘shildi", "Misr mustaqil bo‘ldi", "Nizo mahdiylarni kuchsizlantirdi.")
t.TF("Britaniya Misrda Usmonli imperiyasi hokimiyatini rasman tugatmagan.", True, "To‘g‘ri: hadivlar sulolasi nomiga saqlangan.")
t.TF("1888-yilgi konvensiyaga ko‘ra Suvaysh kanalidan faqat Britaniya kemalari foydalanishi mumkin edi.", False, "Noto‘g‘ri: barcha davlatlar urushda ham, tinchlikda ham erkin foydalanish huquqini oldi.")
t.MUL([("1882-yilgi qonunga ko‘ra hukumat Deputatlar palatasiga bo‘ysunadigan bo‘ldi.", True),
       ("XIX asr oxirida Jazoirda 300 mingdan ortiq fransuz yashagan.", True),
       ("Ahmad Orabibey qo‘shini inglizlarni Misrdan quvib chiqargan.", False)],
      "III noto‘g‘ri: Misr qo‘shinlari yengilgan, Orabibey surgun qilingan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["«Xizb ul-Vatan» tuzildi", "Muhammad Ahmad o‘zini mahdiy deb e’lon qildi", "Iskandariya o‘qqa tutildi", "Mahdiylar davlati tuzildi", "Suvaysh kanali konvensiyasi", "Italiya Liviyaga hujum qildi"],
      "1871 → 1881 → 1882 → 1885 → 1888 → 1911.")
t.MAPMATCH(AF, ['Misr', 'Sudan', 'Jazoir', 'Marokash'],
           ["1882-yilda Britaniya mustamlakasiga aylangan, Suvaysh kanali joylashgan davlat", "1885-yilda mustaqil mahdiylar davlati tuzilgan hudud", "1912-yilda «Yosh Jazoir» partiyasi tuzilgan Fransiya mustamlakasi", "1907-yildan Fransiya bosib olgan, bir qismi Ispaniyaga berilgan davlat"],
           "1 – Misr; 2 – Sudan; 3 – Jazoir; 4 – Marokash.")
t.VENN("Misrdagi ozodlik harakati", "Sudandagi mahdiylar harakati",
       [("«Vatan partiyasi» va Ahmad Orabibey", 1), ("«Misr misrliklarniki» shiori", 1),
        ("Muhammad Ahmad boshchiligida", 2), ("1885-yilda mustaqil davlat tuzgan", 2),
        ("Britaniya mustamlakachiligiga qarshi kurash", 3)],
       "Misr — Vatan partiyasi, Orabibey; Sudan — mahdiy, mustaqil davlat.")

# 34 Tropik va Janubiy Afrika
t = Topic('e9j34', 9134); TOPICS['e9j34'] = t
t.B("Janubiy Afrikada qaysi konlarning topilishi yevropaliklar oqimini tezlashtirgan?", "olmos va oltin", "neft va gaz", "ko‘mir va temir", "mis va qalay", "Olmos va oltin konlari.")
t.B("Janubiy Afrikani mustamlaka qilishda asosiy rolni qaysi davlat o‘ynagan?", "Buyuk Britaniya", "Germaniya", "Portugaliya", "Fransiya", "Buyuk Britaniya.")
t.B("Fransiya G‘arbiy Sudanni qachon bosib olgan?", "1892-yilda", "1898-yilda", "1883-yilda", "1910-yilda", "1892-yilda.")
t.B("G‘arbiy sudanliklarning ozodlik kurashida yorqin iz qoldirgan lashkarboshi kim?", "Samori Ture", "Ketchvayo", "Xendrik Vitboy", "Muhammad Ahmad", "Samori Ture; 1898-yilda taslim etilgan.")
t.B("Samori Ture qayerga surgun qilingan?", "Gabonga", "Seylonga", "Madagaskarga", "Kongoga", "Gabonga.")
t.B("Kongo havzasidagi yerlar qaysi davlat mustamlakasi deb e’lon qilingan?", "Belgiya", "Gollandiya", "Portugaliya", "Ispaniya", "Belgiya.")
t.B("Buganda Britaniya tuzgan qaysi protektorat tarkibiga kiritilgan?", "Uganda protektorati", "Zanzibar sultonligi", "Keniya", "Rodeziya", "Uganda protektorati.")
t.B("«De Rods» kompaniyasini tuzib, olmos konlarini egallagan ingliz siyosatchisi kim?", "Sesil Rods", "Gordon", "Lloyd-Jorj", "Dafferin", "Sesil Rods.")
t.B("«Britaniya-Janubiy Afrika imtiyozli kompaniyasi» qanday shior bilan harakat qilgan?", "«Keyptaundan Qohiragacha Britaniya mustamlakasi bo‘lishi kerak»", "«Afrika afrikaliklar uchun»", "«Misr misrliklarniki»", "«Dengizlarni boshqar»", "«Keyptaundan Qohiragacha».")
t.B("1910-yilda Transvaal, Oranj, Natal, Kap qanday nom ostida birlashtirilgan?", "Janubiy Afrika Ittifoqi", "Rodeziya", "Bur Respublikasi", "Kap koloniyasi", "«Janubiy Afrika Ittifoqi».")
t.B("Fransiya Madagaskarni qachon o‘z mustamlakasi deb e’lon qilgan?", "1896-yilda", "1883-yilda", "1892-yilda", "1910-yilda", "1896-yilda (1883-yilda urush e’lon qilgan).")
t.B("1879-yilda inglizlarning 20 ming kishilik qo‘shinini yakson qilgan zuluslar hukmdori kim?", "Ketchvayo", "Samori Ture", "Menelik", "Vitboy", "Ketchvayo.")
t.B("Suvaysh kanali qachon ochilgan?", "1869-yilda", "1882-yilda", "1888-yilda", "1875-yilda", "1869-yilda.")
t.B("1867-yilda inglizlarga qarshi urushda o‘zini o‘zi o‘ldirgan Efiopiya negusi kim?", "Feodor II", "Menelik", "Yo‘xonni", "Ketchvayo", "Feodor II.")
t.B("Gerero qabilalari qo‘zg‘oloniga kim boshchilik qilgan?", "Samuil Magarero", "Xendrik Vitboy", "Samori Ture", "Ketchvayo", "Samuil Magarero.")
t.B("Nama qabilalari qo‘zg‘oloniga kim boshchilik qilgan?", "Xendrik Vitboy", "Samuil Magarero", "Sesil Rods", "Feodor II", "Xendrik Vitboy; 1905-yilda halok bo‘ldi.")
t.B("Germaniya bosqinchilari namalardan qancha kishini qirib tashlagan?", "140 ming", "120 ming", "20 ming", "1 million", "140 ming kishi.")
t.NAT("Germaniyaga qarshi Sharqiy Afrikaning janubi va markazida (Tanganika) qo‘zg‘olon ikki yildan ortiq davom etdi.", "nemis qo‘shinlari 120 ming afrikalikni qirib, qo‘zg‘olonni bostirdi", "Tanganika mustaqil bo‘ldi", "Germaniya Afrikadan chiqdi", "qabilalar Britaniyaga qo‘shildi", "Katta qabilalar butunlay yo‘q bo‘lib ketdi.")
t.TF("Italiya Efiopiyani bosib olishga urinsa-da, Efiopiya mustaqilligini saqlab qolgan.", True, "To‘g‘ri.")
t.TF("Ingliz-bur urushidan keyin Bur respublikalari mustaqil qolgan.", False, "Noto‘g‘ri: 1902-yilda ular Britaniya mulklariga qo‘shib olingan.")
t.MUL([("Zanzibar arab sultonligi nemislar, fransuzlar va inglizlar tomonidan bo‘lib olingan.", True),
       ("1889–1913-yillarda Qizil dengiz bo‘yi va Somali Britaniya, Fransiya, Italiya o‘rtasida taqsimlangan.", True),
       ("Togo va Kamerun Fransiya mustamlakasi edi.", False)],
      "III noto‘g‘ri: Togo va Kamerun Germaniya mustamlakasi edi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Suvaysh kanali ochildi", "Ketchvayo inglizlarni yakson qildi", "Fransiya Madagaskarga urush e’lon qildi", "Fransiya G‘arbiy Sudanni bosib oldi", "Ingliz-bur urushi boshlandi", "Janubiy Afrika Ittifoqi tuzildi"],
      "1869 → 1879 → 1883 → 1892 → 1899 → 1910.")
t.MAPMATCH(AF, ['Madagaskar', 'Kongo', 'Keyptaun', 'Efiopiya'],
           ["1896-yilda Fransiya mustamlakasi deb e’lon qilingan orol", "havzasidagi yerlar Belgiya mustamlakasi bo‘lgan hudud", "«Qohiragacha» shiorining boshlang‘ich nuqtasi", "Italiya bosib ololmagan, mustaqilligini saqlagan davlat"],
           "1 – Madagaskar; 2 – Kongo; 3 – Keyptaun; 4 – Efiopiya.")
t.VENN("Gerero qo‘zg‘oloni", "Nama qo‘zg‘oloni",
       [("Samuil Magarero boshchiligida", 1), ("tirik qolganlar shimolga qochgan", 1),
        ("Xendrik Vitboy boshchiligida", 2), ("140 ming kishi qirib tashlangan", 2),
        ("Germaniya bosqinchilariga qarshi", 3)],
       "Gerero — Magarero; Nama — Vitboy, 140 ming qurbon.")

# 35 Birinchi jahon urushining boshlanishi va borishi
t = Topic('e9j35', 9135); TOPICS['e9j35'] = t
t.B("Birinchi jahon urushining bosh sababi nima edi?", "bo‘lingan dunyoni qayta bo‘lib olish uchun kurash", "diniy nizolar", "Frans Ferdinandning o‘limi", "AQSHning hujumi", "Ikki harbiy-siyosiy guruh o‘rtasidagi dunyoni qayta bo‘lish kurashi.")
t.B("Frans Ferdinand qachon va qayerda o‘ldirilgan?", "1914-yil 28-iyulda Sarayevoda", "1914-yil 1-avgustda Venada", "1914-yil 3-avgustda Belgradda", "1913-yilda Sofiyada", "Sarayevoda, serbiyalik G. Prinsip tomonidan.")
t.B("Frans Ferdinandni kim o‘ldirgan?", "G. Prinsip", "Anvar poshsho", "Shliffen", "Sushan", "Serbiyalik millatchi G. Prinsip.")
t.B("Germaniya Rossiyaga qachon urush e’lon qilgan?", "1-avgustda", "3-avgustda", "4-avgustda", "23-avgustda", "1-avgustda; Fransiyaga — 3-avgustda.")
t.B("Germaniya qaysi davlatning betaraflik maqomini buzib hujum qilgan?", "Belgiyaning", "Shveytsariyaning", "Gollandiyaning", "Daniyaning", "Belgiyaning.")
t.B("Britaniya Germaniyaga qachon urush e’lon qilgan?", "4-avgustda", "1-avgustda", "3-avgustda", "23-avgustda", "4-avgustda.")
t.B("Yaponiya Germaniyaga qachon urush e’lon qilgan?", "23-avgustda", "4-avgustda", "2-noyabrda", "1-avgustda", "23-avgustda.")
t.B("Yashin tezligida g‘alaba rejasini kim ishlab chiqqan?", "general fon Shliffen", "Bismark", "Anvar poshsho", "Lloyd-Jorj", "General fon Shliffen.")
t.B("Rossiya Germaniya va Avstriya-Vengriyaga qarshi hujumni qachon boshlagan?", "17-avgustda", "1-avgustda", "9-sentabrda", "2-noyabrda", "17-avgustda, Fransiya iltimosiga ko‘ra.")
t.B("Marna jangida har ikki tomondan qancha jangchi qatnashgan?", "2 mln ga yaqin", "200 ming", "10 mln", "500 ming", "2 mln ga yaqin.")
t.B("Usmonli davlati flotiga qaysi nemis admirali qo‘mondonlik qilgan?", "Sushan", "Shliffen", "Tirpits", "Lyudendorf", "Admiral Sushan.")
t.B("Rossiya Usmonli davlatiga qachon urush e’lon qilgan?", "2-noyabrda", "5-noyabrda", "23-avgustda", "1-avgustda", "2-noyabrda; Kavkaz fronti vujudga keldi.")
t.B("1915-yildagi rus armiyasining og‘ir talafotlar bilan chekinishi qanday nom olgan?", "«Buyuk chekinish»", "«Verden qirg‘ini»", "«Marna mo‘jizasi»", "«Qonli yakshanba»", "«Buyuk chekinish».")
t.B("Buyuk chekinishda rus armiyasidan qancha soldat va zobit halok bo‘lgan?", "850 ming", "2 mln", "15 ming", "140 ming", "850 ming.")
t.B("Germaniya suvosti kemalari qaysi yo‘lovchi kemasini cho‘ktirgan?", "«Luzitaniya»", "«Titanik»", "«Potyomkin»", "«Avrora»", "«Luzitaniya» — 2000 ga yaqin yo‘lovchi bilan.")
t.B("Germaniya birinchi marta kimyoviy qurol — xlor gazini qaysi jangda ishlatgan?", "Ipr jangida", "Marna jangida", "Verden jangida", "Somma jangida", "1915-yil aprelida Ipr jangida.")
t.B("Italiya Antanta bilan shartnomani qachon va qayerda imzolagan?", "1915-yil aprelida Londonda", "1914-yilda Rimda", "1915-yil mayida Parijda", "1916-yilda Venada", "1915-yil aprelida Londonda.")
t.B("Italiya Avstriya-Vengriyaga qachon urush e’lon qilgan?", "1915-yil 23-mayda", "1915-yil aprelida", "1914-yil avgustida", "1916-yilda", "23-mayda.")
t.B("Bolgariya qachon «To‘rtlar ittifoqi»ga qo‘shilgan?", "1915-yil 15-sentabrda", "1915-yil 14-oktabrda", "1914-yil 2-avgustda", "1915-yil 8-mayda", "1915-yil 15-sentabrda.")
t.NAT("Avstriya-Vengriya ultimatumining bir talabini Serbiya rad etdi.", "Avstriya-Vengriya 28-iyulda Serbiyaga urush e’lon qildi", "Serbiya Avstriyaga qo‘shildi", "Rossiya Serbiyaga urush e’lon qildi", "urush to‘xtatildi", "Bu urushga bahona bo‘ldi.")
t.NAT("1914-yil sentabrida Marna jangida Britaniya va Fransiya qo‘shini ustun keldi.", "Germaniyaning yashin tezligida g‘alaba rejasi barbod bo‘ldi", "Parij Germaniyaga taslim bo‘ldi", "Rossiya urushdan chiqdi", "Italiya Germaniyaga qo‘shildi", "Nemislar 9-sentabrda chekinishga majbur bo‘ldi.")
t.TF("Germaniya Belgiyaning betarafligi to‘g‘risidagi hujjatni «bir parcha qog‘oz» deb atagan.", True, "To‘g‘ri.")
t.TF("Xlor gazi Antanta qo‘shinlariga uzoq vaqt hal qiluvchi zarar yetkazdi, chunki himoya vositasi topilmadi.", False, "Noto‘g‘ri: Antanta tez orada protivogaz bilan ta’minlandi.")
t.MUL([("Britaniya Italiyaga 50 mln funt sterling qarz berishni va’da qilgan.", True),
       ("Yaponiya 1915-yilda Xitoyga Shandun viloyatini o‘z ta’sir doirasiga o‘tkazish talabini qo‘ygan.", True),
       ("Italiya urush boshidan «Uchlar ittifoqi» tarafida jang qilgan.", False)],
      "III noto‘g‘ri: Italiya kutib turib, 1915-yilda Antanta tomoniga o‘tgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Avstriya-Vengriya Serbiyaga urush e’lon qildi", "Germaniya Rossiyaga urush e’lon qildi", "Britaniya Germaniyaga urush e’lon qildi", "Marna jangi", "Rossiya Usmonli davlatiga urush e’lon qildi", "Italiya Avstriya-Vengriyaga urush e’lon qildi"],
      "1914-yil 28-iyul → 1-avgust → 4-avgust → sentabr → 2-noyabr → 1915-yil 23-may.")
t.MAPMATCH(EU, ['Sarayevo', 'Ipr', 'Dardanell'],
           ["Frans Ferdinand o‘ldirilgan shahar", "1915-yil aprelida birinchi marta xlor gazi ishlatilgan joy", "Antanta dengiz kuchlari Usmonli davlatiga qarshi operatsiya boshlagan bo‘g‘oz"],
           "1 – Sarayevo; 2 – Ipr; 3 – Dardanell.")
t.VENN("Antanta", "To‘rtlar ittifoqi",
       [("Britaniya, Fransiya, Rossiya", 1), ("1915-yildan Italiya qo‘shilgan", 1),
        ("Germaniya, Avstriya-Vengriya, Usmonli davlati", 2), ("1915-yilda Bolgariya qo‘shilgan", 2),
        ("Birinchi jahon urushi qatnashchisi bo‘lgan harbiy-siyosiy blok", 3)],
       "Antanta — Britaniya, Fransiya, Rossiya, Italiya; To‘rtlar — Germaniya, Avstriya-Vengriya, Usmonli, Bolgariya.")
