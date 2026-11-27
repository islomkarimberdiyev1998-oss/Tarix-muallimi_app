from qlib import Topic
TOPICS = {}
W = 'globe'; EU = 'europe'; RU = 'rus'

# 9 Germaniya
t = Topic('e8j9', 809); TOPICS['e8j9'] = t
t.B("Germaniya nechtadan ortiq mayda knyazliklarga bo‘lingan edi?", "300 dan ortiq", "30 ta", "1000 dan ortiq", "12 ta", "Germaniya 300 dan ortiq knyazlikka bo‘lingan edi.")
t.B("Germaniya qaysi mahsulot ishlab chiqarish bo‘yicha dunyoda birinchi o‘rinda bo‘lgan?", "mis", "temir", "oltin", "ipak", "Germaniya mis ishlab chiqarishda birinchi o‘rinda edi.")
t.B("Germaniya imperiyasi 1806-yilgacha qanday atalgan?", "Muqaddas Rim imperiyasi", "Prussiya qirolligi", "Avstriya imperiyasi", "Germaniya ittifoqi", "U «Muqaddas Rim imperiyasi» deb atalgan.")
t.B("Germaniya imperatori qaysi sulolaga mansub edi?", "gabsburglar", "gogensollernlar", "burbonlar", "styuartlar", "Imperator gabsburglar sulolasidan edi.")
t.B("Fransiya Germaniyadan qaysi shaharni egallab olgan?", "Strasburg", "Berlin", "Vena", "Myunxen", "Fransiya Strasburg va Reyn chap qirg‘og‘ini egalladi.")
t.B("Germaniya knyazliklari Turkiyaga qarshi birinchi marta yakdil qarorni qachon qabul qilgan?", "1683-yilda", "1648-yilda", "1701-yilda", "1740-yilda", "1683-yili yakdil qaror qabul qilindi.")
t.B("1683-yilda usmoniylar qo‘shini qayerda tor-mor qilingan?", "Vena ostonalarida", "Berlin yaqinida", "Strasburgda", "Budapeshtda", "Vena ostonalarida tor-mor qilindi.")
t.B("Brandenburgni qaysi sulola boshqargan?", "gogensollernlar", "gabsburglar", "romanovlar", "burbonlar", "Brandenburgni gogensollernlar boshqargan.")
t.B("Prussiya qirolligi qachon tashkil topgan?", "1701-yilda", "1683-yilda", "1740-yilda", "1806-yilda", "1701-yili Prussiya qirolligi tashkil topdi.")
t.B("Prussiyaning birinchi qiroli kim?", "Fridrix I", "Fridrix II", "Karl V", "Vilgelm I", "Brandenburg knyazi Fridrix I Prussiya qiroli deb e’lon qilindi.")
t.B("Fridrix II qaysi yillarda hukmronlik qilgan?", "1740–1786", "1701–1740", "1683–1701", "1786–1806", "Fridrix II (1740–1786).")
t.B("«Gegemonlik» so‘zi nimani anglatadi?", "bir davlatning boshqasi ustidan ustunligi", "tarqoqlik", "ittifoq", "betaraflik", "Gegemonlik – siyosiy, iqtisodiy, harbiy ustunlik.")
t.NAT("Germaniya siyosiy jihatdan tarqoq edi.", "yagona ichki bozor vujudga kelmadi", "sanoat tez rivojlandi", "Germaniya dengizlarda hukmron bo‘ldi", "manufakturalar qishloqqa yoyildi",
      "Siyosiy tarqoqlik yagona ichki bozor vujudga kelishiga imkon bermadi.")
t.NAT("Germaniya knyazliklari 1683-yilda Vena ostonasida g‘alaba qozondi.", "Markaziy Yevropa usmoniylar bosqinidan saqlab qolindi", "Germaniya birlashdi", "Fransiya Germaniyani egalladi", "Usmoniylar Venani egalladi",
      "Bu g‘alaba Markaziy Yevropani saqlab qoldi.")
t.NAT("O‘ttiz yillik urush asosan nemis yerlarida bo‘ldi.", "Germaniya iqtisodiy va siyosiy tanazzulga yuz tutdi", "Germaniya Yevropada gegemon bo‘ldi", "Germaniya birlashdi", "savdo yo‘llari Germaniyaga qaytdi",
      "Gegemonlik Fransiyaga o‘tdi, Germaniya tanazzulga uchradi.")
t.TF("Germaniyada manufaktura qishloqqa ham keng yoyilgan.", False, "Noto‘g‘ri: manufaktura faqat shahar bilan cheklangan.")
t.TF("XVIII asr oxirida Prussiya maydoni bo‘yicha Yevropada uchinchi o‘rinda edi.", True, "To‘g‘ri; qo‘shini soni bo‘yicha to‘rtinchi.")
t.MUL([("Imperator Avstriyadan tashqarida real hokimiyatga ega bo‘lmagan.", True), ("Aholi imperiyaning emas, knyazliklarning fuqarosi edi.", True), ("Imperiya Reyxstagi qarorlari barcha knyazliklarda qat’iy bajarilgan.", False)],
      "III noto‘g‘ri: Reyxstag majburiy qaror qabul qila olmasdi.")
t.MATCH("Knyazliklarni sulola va poytaxt bilan moslashtiring.", ["Avstriya", "Brandenburg"], ["gabsburglar, Vena", "gogensollernlar, Berlin", "burbonlar, Parij"], 'ab',
        "Avstriya – gabsburglar, Vena; Brandenburg – gogensollernlar, Berlin.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Dehqonlar urushi", "O‘ttiz yillik urush", "Vena ostonasidagi g‘alaba", "Prussiya qirolligi tashkil topdi", "Fridrix II taxtga chiqdi"],
      "1524 → 1618 → 1683 → 1701 → 1740.")
t.MAPMATCH(EU, ['Vena', 'Berlin', 'Strasburg'],
           ["gabsburglar poytaxti, 1683-yilda usmoniylar tor-mor qilingan joy", "gogensollernlar poytaxti", "Fransiya egallab olgan shahar"], "1 – Vena; 2 – Berlin; 3 – Strasburg.")
t.VENN("Avstriya", "Prussiya",
       [("gabsburglar boshqargan", 1), ("poytaxti Vena", 1),
        ("1701-yilda qirollik bo‘lgan", 2), ("Fridrix II davrida mutlaq monarxiya", 2),
        ("Germaniyada gegemonlik uchun kurashgan", 3)],
       "Avstriya: gabsburglar, Vena. Prussiya: 1701, Fridrix II. Ikkalasi gegemonlik uchun kurashgan.")

# 10 Rossiya
t = Topic('e8j10', 810); TOPICS['e8j10'] = t
t.B("Rossiya tarixida birinchi bo‘lib podsholik tojini kiygan hukmdor kim?", "Ivan IV", "Pyotr I", "Boris Godunov", "Mixail Romanov", "1547-yili Ivan IV podsholik tojini kiydi.")
t.B("Ivan IV qachon taxtga o‘tirgan?", "1547-yilda", "1549-yilda", "1565-yilda", "1598-yilda", "1547-yili taxtga o‘tirdi.")
t.B("Birinchi Zemstvo sobori qachon chaqirilgan?", "1549-yilda", "1547-yilda", "1613-yilda", "1565-yilda", "1549-yili birinchi Zemstvo sobori chaqirildi.")
t.B("Zemstvo sobori qabul qilgan qonunlar to‘plami qanday atalgan?", "Sudebnik", "Russkaya pravda", "Ulojeniye", "Manifest", "Yangi qonunlar to‘plami – Sudebnik.")
t.B("Sudebnikka ko‘ra krepostnoy dehqonlar qaysi kuni boshqa yer egasiga o‘tishi mumkin edi?", "26-noyabr", "1-yanvar", "1-may", "14-iyul", "Yiliga bir kun – 26-noyabr.")
t.B("Ivan IV tomonidan ajratib olingan yerlar qanday atalgan?", "oprichnina", "zemshina", "votchina", "pomeste", "Bu yerlar oprichnina (ajratib olingan) deb ataldi.")
t.B("Oprichnina qachon bekor qilingan?", "1572-yilda", "1565-yilda", "1598-yilda", "1584-yilda", "Ivan IV 1572-yili oprichninani bekor qildi.")
t.B("Ryuriklar sulolasi qachon barham topgan?", "1598-yilda", "1613-yilda", "1584-yilda", "1572-yilda", "1598-yili Fyodor vafot etib, ryuriklar sulolasi tugadi.")
t.B("1598-yilda Zemstvo sobori kimni podsho etib saylagan?", "Boris Godunov", "Mixail Romanov", "Fyodor Ivanovich", "Kuzma Minin", "Boris Godunov podsho etib saylandi.")
t.B("1612-yilda xalq lashkariga kimlar yetakchilik qilgan?", "Kuzma Minin va Dmitriy Pojarskiy", "Ivan IV va Godunov", "Pyotr I va Menshikov", "Lomonosov va Polzunov", "Minin va Pojarskiy xalq lashkarini to‘pladi.")
t.B("Romanovlar sulolasining birinchi podshosi kim?", "Mixail Fyodorovich Romanov", "Pyotr I", "Aleksey Mixaylovich", "Boris Godunov", "1613-yili Mixail Fyodorovich Romanov saylandi.")
t.B("Pyotr I qachon taxtga o‘tirgan?", "1689-yilda", "1700-yilda", "1721-yilda", "1613-yilda", "Pyotr I 1689-yilda taxtga o‘tirdi.")
t.B("Rossiya–Shvetsiya tinchlik shartnomasi qayerda imzolangan?", "Nishtadtda", "Peterburgda", "Moskvada", "Stokgolmda", "1721-yili Finlandiyaning Nishtadt shahrida imzolandi.")
t.B("Moskva universiteti qachon tashkil qilingan?", "1755-yilda", "1721-yilda", "1700-yilda", "1801-yilda", "1755-yili Lomonosov tashabbusi bilan.")
t.B("Osiyoning eng shimoliy chekkasini kim kashf etgan?", "S.I. Chelyuskin", "Bering", "Laptevlar", "Kulibin", "S.I. Chelyuskin – Chelyuskin burni.")
t.B("Rus milliy teatrining asoschisi kim?", "F.G. Volkov", "D.I. Fonvizin", "G.D. Derjavin", "I.A. Krilov", "Savdogar F.G. Volkov.")
t.NAT("Ivan IV ga podsholik unvoni berildi.", "u G‘arbiy Yevropa qirollari bilan tenglashdi", "boyarlar kuchaydi", "Zemstvo bekor qilindi", "Rossiya Oltin O‘rdaga qaram bo‘ldi",
      "Podsholik unvoni uni Yevropa qirollari bilan tenglashtirdi.")
t.NAT("Shimoliy urush Rossiya g‘alabasi bilan tugadi (1721).", "Rossiya Boltiq dengiziga chiqdi va imperiyaga aylandi", "Shvetsiya Moskvani oldi", "Rossiya Qora dengizni oldi", "Polsha Rossiyani bosib oldi",
      "Pyotr I imperator deb e’lon qilindi.")
t.NAT("Rossiyalik olimlar ilg‘or mashinalar yaratdi.", "qoloq krepostnoy Rossiyada ular deyarli qo‘llanilmadi", "Rossiya sanoati Yevropadan oshib ketdi", "mashinalar eksport qilindi", "krepostnoylik bekor qilindi",
      "Krepostnoy Rossiyada bu mashinalarga talab yo‘q edi.")
t.TF("XVI asr ikkinchi yarmida Qozon, Ashtarxon va Sibir xonliklari bosib olingan.", True, "To‘g‘ri.")
t.TF("Romanovlar sulolasi Rossiyani 1991-yilgacha boshqargan.", False, "Noto‘g‘ri: 1917-yil fevralgacha boshqargan.")
t.MUL([("Polsha g‘alayonlar davrida Moskvani egallab olgan.", True), ("Laptevlar ekspeditsiyasi Shimoliy Muz okeanini o‘rgangan.", True), ("Oprichnina mamlakat xo‘jaligiga foyda keltirgan.", False)],
      "III noto‘g‘ri: oprichnina xo‘jalikka katta talafot yetkazdi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Ivan IV podsho bo‘ldi", "Oprichnina joriy etildi", "Ryuriklar sulolasi tugadi", "Moskva polyaklardan ozod qilindi", "Romanovlar taxtga keldi", "Pyotr I imperator bo‘ldi"],
      "1547 → 1565 → 1598 → 1612 → 1613 → 1721.")
t.MAPMATCH(RU, ['Moskva', 'Qozon', 'Nishtadt', 'Ashtarxon'],
           ["1612-yilda polyaklardan ozod qilingan poytaxt", "XVI asrda bosib olingan Volga bo‘yidagi xonlik poytaxti", "1721-yilgi tinchlik shartnomasi imzolangan shahar", "Volga quyi oqimidagi bosib olingan xonlik"],
           "1 – Moskva; 2 – Qozon; 3 – Nishtadt; 4 – Ashtarxon.")
t.VENN("Ivan IV", "Pyotr I",
       [("birinchi bo‘lib «sar» unvonini olgan", 1), ("oprichnina joriy etgan", 1),
        ("Shimoliy urushda g‘alaba qozongan", 2), ("1721-yilda imperator deb e’lon qilingan", 2),
        ("Rossiya hukmdori", 3)],
       "Ivan IV: sar, oprichnina. Pyotr I: Shimoliy urush, imperator. Ikkalasi Rossiya hukmdori.")

# 11 Shimoliy Amerika, AQSH
t = Topic('e8j11', 811); TOPICS['e8j11'] = t
t.B("Shimoliy Amerikani asosan qaysi davlatlar egallagan?", "Angliya va Fransiya", "Ispaniya va Portugaliya", "Gollandiya va Rossiya", "Shvetsiya va Daniya", "Shimoliy Amerika asosan Angliya va Fransiya tomonidan egallandi.")
t.B("Angliyaning Virjiniyadagi ilk manzilgohi qanday atalgan?", "Jeymstaun", "Filadelfiya", "Boston", "Nyu-York", "1607-yili Jeymstaun tashkil qilindi.")
t.B("Jeymstaun qachon tashkil qilingan?", "1607-yilda", "1620-yilda", "1774-yilda", "1585-yilda", "1607-yili tashkil qilindi.")
t.B("Birinchi Qit’a Kongressi qachon va qayerda yig‘ilgan?", "1774-yil sentabrda Filadelfiyada", "1776-yilda Bostonda", "1787-yilda Nyu-Yorkda", "1775-yilda Virjiniyada", "1774-yil sentabrda Filadelfiyada.")
t.B("Birinchi Qit’a Kongressida qaysi mustamlaka qatnashmagan?", "Jorjiya", "Virjiniya", "Pensilvaniya", "Massachusets", "Jorjiyadan tashqari barcha mustamlakalar qatnashdi.")
t.B("Ikkinchi Qit’a Kongressi qachon boshlangan?", "1775-yil mayda", "1774-yil sentabrda", "1776-yil iyulda", "1783-yilda", "1775-yil may oyida boshlandi.")
t.B("Amerika qurolli kuchlarining bosh qo‘mondoni kim etib tayinlangan?", "Jorj Vashington", "Tomas Jefferson", "Benjamin Franklin", "Jon Adams", "Virjiniyalik polkovnik Jorj Vashington.")
t.B("Mustaqillik Deklaratsiyasi asosan kimning zakovati mahsuli?", "Tomas Jefferson", "Jorj Vashington", "Jeyms Medison", "Aleksandr Gamilton", "Deklaratsiya asosan T. Jefferson zakovatining mahsuli.")
t.B("Mustaqillik Deklaratsiyasi qachon qabul qilingan?", "1776-yil 4-iyulda", "1774-yil sentabrda", "1783-yilda", "1787-yil 17-sentabrda", "1776-yil 4-iyulda qabul qilindi.")
t.B("Mustaqillik urushida Amerikaga qaysi davlat qurol bilan yordam bergan?", "Fransiya", "Ispaniya", "Rossiya", "Gollandiya", "Fransiya qurol-yarog‘ bilan yordam berdi.")
t.B("Britaniya AQSH mustaqilligini qaysi sulh bilan tan olgan?", "1783-yilgi Parij sulhi", "1774-yilgi sulh", "1787-yilgi Konstitutsiya", "Vestfal sulhi", "1783-yili Parij sulhi imzolandi.")
t.B("AQSH Konstitutsiyasi qachon qabul qilingan?", "1787-yil 17-sentabrda", "1776-yil 4-iyulda", "1789-yilda", "1783-yilda", "1787-yil 17-sentabrda qabul qilindi.")
t.B("AQSH prezidenti necha yil muddatga saylanadi?", "4 yil", "6 yil", "2 yil", "7 yil", "Prezident 4 yil muddatga saylanadi.")
t.B("AQShning birinchi prezidenti kim?", "Jorj Vashington", "Tomas Jefferson", "Jon Adams", "Benjamin Franklin", "1789-yili Jorj Vashington saylandi.")
t.NAT("Britaniya parlamenti Amerika tadbirkorlariga cheklovlar o‘rnatib, soliqlarni oshirdi.", "amerikaliklarning norozilik chiqishlari boshlandi", "Amerika iqtisodi gullab-yashnadi", "mustamlakalar Fransiyaga qo‘shildi", "Britaniya mustamlakalardan voz kechdi",
      "Dastlabki norozilik chiqishlari cheklovlar va soliqlarga qarshi bo‘ldi.")
t.NAT("Amerika va Fransiya «Do‘stlik va Tijorat Bitimi»ni imzoladi.", "1782-yilda ingliz qo‘shinlarining asosiy qismi taslim bo‘ldi", "Amerika urushda yengildi", "Fransiya Amerikani egalladi", "Britaniya Fransiyani bosib oldi",
      "Fransiya–Amerika ittifoqi yaxshi natija berdi.")
t.TF("Amerika inqilobi milliy-ozodlik urushi shaklida o‘tgan.", True, "To‘g‘ri.")
t.TF("Mustamlakalarda XVII asrdan Afrikadan qora tanli qullar keltirilmagan.", False, "Noto‘g‘ri: XVII asrdan ko‘plab qullar keltirilgan.")
t.MUL([("Parij muzokaralarida Franklin, Adams va Jey qatnashgan.", True), ("4-iyul AQShda Mustaqillik kuni sifatida nishonlanadi.", True), ("Harbiy harakatlar asosan mamlakat janubida bo‘lgan.", False)],
      "III noto‘g‘ri: harbiy harakatlar asosan mamlakat shimolida bo‘lgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Jeymstaun tashkil qilindi", "Birinchi Qit’a Kongressi", "Mustaqillik Deklaratsiyasi", "Parij sulhi", "AQSH Konstitutsiyasi", "Vashington prezident bo‘ldi"],
      "1607 → 1774 → 1776 → 1783 → 1787 → 1789.")
t.MAPN('usa_e', ['Jeymstaun', 'Filadelfiya', 'Boston', 'Nyu-York'], "1774-yilda Birinchi Qit’a Kongressi yig‘ilgan va 1787-yilda Konstitutsiya qabul qilingan shahar qaysi raqam bilan belgilangan?", "Filadelfiya – 2.", ask_idx=1)
t.MAPN('usa_e', ['Jeymstaun', 'Filadelfiya', 'Boston', 'Nyu-York'], "1607-yilda Virjiniyada tashkil qilingan ilk ingliz manzilgohi qaysi raqam bilan belgilangan?", "Jeymstaun – 1.", ask_idx=0)
t.VENN("Mustaqillik Deklaratsiyasi (1776)", "AQSH Konstitutsiyasi (1787)",
       [("asosan T. Jefferson yozgan", 1), ("xalq suvereniteti prinsipini e’lon qilgan", 1),
        ("prezident lavozimini joriy qilgan", 2), ("Filadelfiyadagi Federal Konventda qabul qilingan", 2),
        ("AQSHning asosiy hujjati", 3)],
       "Deklaratsiya – Jefferson, suverenitet. Konstitutsiya – prezident, Federal Konvent.")

# 12 Ma'rifat asri
t = Topic('e8j12', 812); TOPICS['e8j12'] = t
t.B("XVIII asr Yevropa tarixiga qanday nom bilan kirgan?", "«Ma’rifat asri»", "«Uyg‘onish davri»", "«Reformatsiya davri»", "«Sanoat asri»", "XVIII asr «Ma’rifat asri» nomi bilan kirdi.")
t.B("Ingliz ma’rifatparvari kim?", "Adam Smit", "Volter", "Russo", "Didro", "Ingliz ma’rifatparvari – Adam Smit.")
t.B("Ma’rifatparvarlarning shiori nima bo‘lgan?", "«fan va taraqqiyot»", "«Duo o‘qi va ishla!»", "«Ozodlik, Tenglik, Birodarlik!»", "«Vatan xavf ostida!»", "«Fan va taraqqiyot» shiorga aylandi.")
t.B("«Robinzon Kruzo» romanining muallifi kim?", "Daniyel Defo", "Jonatan Svift", "Gyote", "Volter", "Ingliz yozuvchisi Daniyel Defo.")
t.B("«Gulliverning sayohatlari» romanining muallifi kim?", "Jonatan Svift", "Daniyel Defo", "Gyote", "Russo", "Dublin ibodatxonasi rahbari Jonatan Svift.")
t.B("Doktor Faust haqidagi falsafiy dramani kim yozgan?", "Iogann Volfgang Gyote", "Svift", "Defo", "Betxoven", "Gyote dramaga 60 yil sarflagan.")
t.B("«Qirolning birinchi tasvirchisi» deb atalgan rassom kim?", "Fransua Bushe", "Antuan Vatto", "Rembrandt", "Rafael", "Fransua Bushe.")
t.B("«Qiyin taklif», «Beparvo» asarlarining muallifi kim?", "Antuan Vatto", "Fransua Bushe", "Leonardo", "Rembrandt", "Vatto chizgan mashhur asarlar.")
t.B("«Matto bayon etgan buyuk musibat» asarining muallifi kim?", "Iogann Sebastyan Bax", "Motsart", "Betxoven", "Gyote", "Bax yozgan xor, solist va orkestr uchun asar.")
t.B("Motsart qayerda tug‘ilgan?", "Zalsburgda", "Venada", "Milanda", "Berlinda", "Motsart Avstriyaning Zalsburg shaharchasida tug‘ilgan.")
t.B("Motsartni juda mashhur qilgan opera qaysi?", "«Figaroning uylanishi»", "«Rekviyem»", "«Oydin sonata»", "«Faust»", "«Figaroning uylanishi» operasi.")
t.B("Motsartning so‘nggi asari qaysi?", "«Rekviyem»", "«Figaroning uylanishi»", "«Qahramonona simfoniya»", "«Buyuk musibat»", "So‘nggi asari – «Rekviyem».")
t.B("«Oydin» sonatasining muallifi kim?", "Lyudvig van Betxoven", "Motsart", "Bax", "Gyote", "«Fantaziya yo‘lida sonata» («Oydin») – Betxoven.")
t.B("Betxovenning «Qahramonona» simfoniyasi dastlab kimga bag‘ishlangan?", "Bonapartga", "Lyudovik XVI ga", "Vashingtonga", "Motsartga", "Simfoniya dastlab Bonapartga bag‘ishlangan edi.")
t.NAT("Napoleon o‘zini imperator deb e’lon qildi.", "Betxoven simfoniyasini uning nomidan ajratib, «Qahramonnoma» deb atadi", "Betxoven simfoniyani yoqib yubordi", "Betxoven Parijga ko‘chdi", "simfoniya taqiqlandi",
      "Kompozitor asarini Bonapart nomi bilan bog‘lamadi.")
t.NAT("Ma’rifatchilik g‘oyalari kishilar ongini egalladi.", "Yevropa sivilizatsiyasi qiyofasini o‘zgartirgan moddiy kuchga aylandi", "absolutizm kuchaydi", "cherkov ta’siri ortdi", "fan rivoji to‘xtadi",
      "G‘oyalar Amerika va Fransiyada ommaviy xarakter oldi.")
t.TF("Ma’rifatparvarlar feodal tartiblarga qarshi inqilobiy usullarni ma’qullagan.", False, "Noto‘g‘ri: ular inqilobiy usullarga salbiy munosabatda bo‘lgan.")
t.TF("Bax hayotligida mashhur bo‘lmagan.", True, "To‘g‘ri.")
t.MUL([("Motsart 14 yoshida Italiyadagi musiqa akademiyasining akademigi bo‘lgan.", True), ("Betxoven 22 yoshidan Venada yashagan.", True), ("Motsart «Rekviyem»ning birinchi ijrosini o‘zi tinglagan.", False)],
      "III noto‘g‘ri: birinchi ijrosigacha yashash unga nasib etmadi.")
t.MATCH("Asarlarni mualliflari bilan moslashtiring.", ["«Robinzon Kruzo»", "«Gulliverning sayohatlari»", "«Faust»", "«Figaroning uylanishi»"],
        ["Defo", "Svift", "Gyote", "Motsart", "Bax"], 'abcd', "Robinzon – Defo; Gulliver – Svift; Faust – Gyote; Figaro – Motsart.")
t.MATCH("Ma’rifatparvarlarni mamlakati bilan moslashtiring.", ["Volter", "Adam Smit", "Gyote"], ["Fransiya", "Angliya", "Germaniya", "Italiya"], 'abc',
        "Volter – fransuz; Smit – ingliz; Gyote – nemis.")
t.CHR("Kompozitorlarni tug‘ilgan yili bo‘yicha joylashtiring.", ["Iogann Sebastyan Bax", "Volfgang Amadey Motsart", "Lyudvig van Betxoven"], "1685 → 1756 → 1770.")
t.MAPMATCH(EU, ['Zalsburg', 'Dublin', 'Parij'],
           ["Motsart tug‘ilgan shahar", "Svift rahbarlik qilgan ibodatxona joylashgan shahar", "Volter va Russo vatani poytaxti"], "1 – Zalsburg; 2 – Dublin; 3 – Parij.")
t.VENN("Robinzon Kruzo", "Gulliver",
       [("Defo qahramoni", 1), ("kimsasiz orolda uy qurgan", 1),
        ("Svift qahramoni", 2), ("sayohatlari quvonchsiz yakun topgan", 2),
        ("Ma’rifat asri adabiy qahramoni", 3)],
       "Robinzon – Defo, orol. Gulliver – Svift, quvonchsiz sayohat. Ikkalasi Ma’rifat asri qahramoni.")
