from qlib import Topic
TOPICS = {}
XR = 'xorazm'; UZ = 'uzb'

# 24 Qoraqalpoqlar madaniyati
t = Topic('e9u24', 9024); TOPICS['e9u24'] = t
t.B("Qoraqalpoq xalq og‘zaki ijodidagi kulgi qahramoni kim?", "O‘mirbek laqqi", "Guloyim", "Arslon", "Olloyor", "O‘mirbek laqqi.")
t.B("Maqollar, hikmatlar, laparlar, nasihat qo‘shiqlarda ifoda etilgan janr qanday atalgan?", "«otalar so‘zi»", "«termalar»", "«o‘lanlar»", "«dostonlar»", "«Otalar so‘zi».")
t.B("Qoraqalpoqlarning ozodlik uchun kurashi tasvirlangan doston qaysi?", "«Qirqqiz»", "«Alpomish»", "«Bo‘zatov»", "«Ahmoq podshoh»", "«Qirqqiz» dostoni.")
t.B("«Qirqqiz» dostonida Sarkub hukmdori kim?", "Olloyor", "Arslon", "O‘mirbek", "Berdaq", "Olloyor.")
t.B("Olloyor qizi Guloyimga qaysi yerlarni tortiq qilgan?", "Muyeli", "Sarkub", "Orolbo‘yi", "Bo‘zatov", "Muyeli degan hosildor yerlarni.")
t.B("Guloyimga yordam bergan xorazmlik bahodir kim?", "Arslon", "Olloyor", "Ernazarbiy", "O‘mirbek", "Uning oshig‘i Arslon.")
t.B("Qoraqalpoqlardagi eng katta madrasalar qaysilar?", "Qoraqum eshon va Tosh madrasalari", "Sherg‘ozixon va Muhammad Aminxon", "Baroqxon va Ko‘kaldosh", "Hokim Oyim va Sulton Murodbek", "Qoraqum eshon va Tosh madrasalari.")
t.B("Tosh madrasani kim qurdirgan?", "Mang‘it hokimi Xo‘janiyoz", "Muhammad Rahimxon I", "Berdaq", "Said Muhammadxon", "1841-yil Mang‘it hokimi Xo‘janiyoz.")
t.B("Madrasada birinchi bosqichda nima o‘rganilgan?", "arab tili grammatikasi", "diniy-huquqiy bilimlar", "astronomiya", "rus tili", "Birinchi bosqichda arab tili grammatikasi.")
t.B("Ajiniyozning taxallusi nima bo‘lgan?", "Zevar", "Munis", "Ogahiy", "Berdaq", "Zevar.")
t.B("Ajiniyoz Xivadagi qaysi madrasada o‘qigan?", "Sherg‘ozixon madrasasida", "Qoraqum eshon madrasasida", "Tosh madrasada", "Muhammad Rahimxon madrasasida", "Sherg‘ozixon madrasasida.")
t.B("Ajiniyoz qaysi dostonida qoraqalpoqlarning yurtma-yurt ko‘chishini tasvirlagan?", "«Bo‘zatov»", "«Qirqqiz»", "«Ernazarbiy»", "«Avlodlar»", "«Bo‘zatov» dostonida.")
t.B("«Ajiniyoz» romanini kim yozgan?", "K. Sultonov", "Berdaq", "Kunxo‘ja", "Ajiniyoz", "Qoraqalpoq yozuvchisi K. Sultonov.")
t.B("Berdaq qaysi yillarda yashagan?", "1827–1900", "1799–1880", "1824–1878", "1788–1875", "1827–1900.")
t.B("Berdaq qayerda tug‘ilgan?", "Orolbo‘yida", "Xivada", "Nukusda", "Chimboyda", "Orolbo‘yida.")
t.B("Berdaqning she’rlaridan biri qanday nomlangan?", "«Xalq uchun»", "«Qish»", "«Bo‘zatov»", "«Qiz Mengesh bilan aytishuv»", "«Xalq uchun».")
t.B("Berdaqning tarixiy mavzudagi asarlari qaysilar?", "«Avlodlar», «Omongeldi», «Oydo‘stbiy», «Ernazarbiy»", "«Bo‘zatov», «Qirqqiz»", "«Riyoz ud-davla», «Gulshani davlat»", "«Firdavs ul-iqbol»", "«Avlodlar», «Omongeldi», «Oydo‘stbiy», «Ernazarbiy».")
t.NAT("Qoraqalpoqlar tinch hayot izlab asrlar davomida bir joydan ikkinchi joyga ko‘chib yurdi.", "moddiy madaniyat yodgorliklarini to‘liq saqlab qolish imkoniyati bo‘lmadi", "ko‘plab saroylar qurildi", "yozma adabiyot erta rivojlandi", "shaharlar ko‘paydi", "Ko‘chib yurish yodgorliklarni saqlashga imkon bermadi.")
t.TF("«Qirqqiz» dostonining bosh g‘oyasi — yuksak vatanparvarlik va Vatanga fidoyilarcha muhabbat.", True, "To‘g‘ri.")
t.TF("Kunxo‘ja o‘z ijodini saroy hayotiga bag‘ishlagan.", False, "Noto‘g‘ri: u ijodini ovullarning oddiy ahliga, ularning mehnati va turmushiga bag‘ishlagan.")
t.MUL([("Ajiniyoz o‘zbek, qozoq, turkman tillarini yaxshi bilgan.", True),
       ("Ajiniyoz adabiy merosidan 100 ga yaqin she’r va dostonlar yetib kelgan.", True),
       ("Berdaq faqat 5 yil davomida she’r yozgan.", False)],
      "III noto‘g‘ri: Berdaq 20 yoshidan boshlab yarim asr davomida ijod qilgan.")
t.MATCH("Shoirlarni yashagan yillari bilan moslashtiring.", ["Kunxo‘ja", "Otash Olshinboy", "Ajiniyoz", "Berdaq"],
        ["1824–1878", "1827–1900", "1799–1880", "1788–1875"], "cdab",
        "Kunxo‘ja 1799–1880; Otash 1788–1875; Ajiniyoz 1824–1878; Berdaq 1827–1900.")
t.MAPMATCH(XR, ['Mo‘ynoq', 'Xiva', 'Mang‘it'],
           ["Ajiniyoz dastlab eski maktabda o‘qigan joy", "Ajiniyoz Sherg‘ozixon madrasasida o‘qigan shahar", "hokimi Xo‘janiyoz 1841-yilda Tosh madrasani qurdirgan joy"],
           "1 – Mo‘ynoq; 2 – Xiva; 3 – Mang‘it.")
t.VENN("Ajiniyoz", "Berdaq",
       [("taxallusi Zevar", 1), ("«Bo‘zatov» dostoni muallifi", 1),
        ("«Ahmoq podshoh» dostoni muallifi", 2), ("Qoraqum eshon madrasasida o‘qigan", 2),
        ("qoraqalpoq shoiri", 3)],
       "Ajiniyoz — Zevar, «Bo‘zatov»; Berdaq — «Ahmoq podshoh», Qoraqum eshon madrasasi.")

# 25 Jadidchilik harakatining vujudga kelishi
t = Topic('e9u25', 9025); TOPICS['e9u25'] = t
t.B("Ziyolilar xalqni ozodlikka eltuvchi yo‘l deb nimani bilgan?", "xalqni ma’rifatli qilishni", "qurolli kurashni", "Rossiyaga ko‘chishni", "savdoni rivojlantirishni", "Xalqni ma’rifatli qilish.")
t.B("Butun turkiy xalqlar orasidagi jadidchilik harakatining asoschisi kim?", "Ismoil G‘aspirali", "Mahmudxo‘ja Behbudiy", "Munavvar qori", "Abdulhamid Cho‘lpon", "Qrim-tatar ma’rifatparvari Ismoil G‘aspirali (1851–1914).")
t.B("Ismoil G‘aspirali birinchi jadid maktabiga qachon va qayerda asos solgan?", "1884-yilda Boqchasaroyda", "1893-yilda Buxoroda", "1898-yilda Qo‘qonda", "1888-yilda Toshkentda", "1884-yilda Qrimdagi Boqchasaroyda.")
t.B("G‘aspirali usulida necha kunda 12 o‘quvchining savodi chiqarilgan?", "40 kunda", "10 kunda", "100 kunda", "1 yilda", "40 kunda.")
t.B("Yangi usul qanday nom bilan tarqalgan?", "«usuli savtiya» — «usuli jadid»", "«usuli qadim»", "«zullisonayn»", "«usuli harbiy»", "«Usuli savtiya» — harf tovushi usuli, ya’ni «usuli jadid».")
t.B("«Rahbari muallimin yoki muallimlarga yo‘ldosh» kitobi qachon chop etilgan?", "1888-yilda", "1884-yilda", "1893-yilda", "1910-yilda", "1888-yilda.")
t.B("«Jadid» so‘zi qanday ma’noni anglatadi?", "«yangi»", "«eski»", "«bilim»", "«ozodlik»", "Arabcha «yangi».")
t.B("Jadidchilik g‘oyalarining yoyilishida qaysi gazeta muhim o‘rin tutgan?", "«Tarjimon»", "«Oyina»", "«Sadoi Turkiston»", "«Turon»", "«Tarjimon» gazetasi.")
t.B("Ismoil G‘aspirali Toshkent, Samarqand va Buxoroga qachon tashrif buyurgan?", "1893-yilda", "1884-yilda", "1898-yilda", "1910-yilda", "1893-yilda.")
t.B("1910-yilda O‘rta Osiyo jadidlarining eng yoshi kim bo‘lgan?", "Abdulhamid Cho‘lpon (13 yosh)", "Mahmudxo‘ja Behbudiy", "Ismoil G‘aspirali", "Mannon qori", "Cho‘lpon — 13 yoshda; eng kattasi Behbudiy — 36 yoshda.")
t.B("Taraqqiyparvarlik harakati 1917-yilga kelib qanday bosqichga o‘tgan?", "siyosiy ko‘rinishdagi harakatga", "qurolli kurashga", "diniy harakatga", "iqtisodiy harakatga", "Ikkinchi bosqich — siyosiy ko‘rinishdagi harakat.")
t.B("Buxoroda jadidchilik qachondan siyosiy tashkilot sifatida shakllana boshlagan?", "1910-yildan", "1893-yildan", "1884-yildan", "1917-yildan", "1910-yildan.")
t.B("Xiva jadidlarining o‘ng oqimiga kim boshchilik qilgan?", "Bosh vazir Islom xo‘ja", "Bobooxun Salimov", "Mahmudxo‘ja Behbudiy", "Salohiddin domla", "Bosh vazir Islom xo‘ja.")
t.B("Xiva jadidlarining so‘l oqimiga kim rahbarlik qilgan?", "qozikalon Bobooxun Salimov", "Islom xo‘ja", "Munavvar qori", "Shamsiddin domla", "Qozikalon Bobooxun Salimov.")
t.B("1898-yilda Qo‘qonda ikkinchi jadid maktabini kim ochgan?", "Salohiddin domla", "Shamsiddin domla", "Mannon qori", "Ismoil G‘aspirali", "Salohiddin domla.")
t.B("1899-yilda Toshkentda jadid maktabini kim ochgan?", "Mannon qori", "Shamsiddin domla", "Salohiddin domla", "Behbudiy", "Mannon qori; Andijonda — Shamsiddin domla.")
t.NAT("Ismoil G‘aspirali 1893-yilda Toshkent, Samarqand va Buxoroga tashrif buyurdi.", "ma’rifatparvarlik g‘oyalarining rivojiga turtki berildi, Buxoroda birinchi yangi usul maktabi ochildi", "jadid maktablari yopildi", "G‘aspirali surgun qilindi", "«Tarjimon» taqiqlandi", "Tashrif turtki berdi; 1893-yilda Buxoroda birinchi yangi usul maktabi ochildi.")
t.TF("Buxoro jadidchiligi ayrim mutaassib mullalar qarshiligiga uchragan.", True, "To‘g‘ri.")
t.TF("Xiva jadidlarining o‘ng oqimi xon hokimiyatini tugatishni maqsad qilgan.", False, "Noto‘g‘ri: o‘ng oqim xon hokimiyatini saqlab qolgan holda islohotlar o‘tkazishni maqsad qilgan.")
t.MUL([("Jadidlar maktablarda diniy ta’lim bilan birga tibbiyot, kimyo kabi fanlarni o‘qitishni zarur deb bilgan.", True),
       ("Buxoro jadidlari tarkibi asosan mayda do‘kondorlar, o‘qituvchilar, hunarmandlar, savdogarlardan iborat edi.", True),
       ("Jadidchilik harakati mustamlakachi hukumat tomonidan to‘liq qo‘llab-quvvatlangan.", False)],
      "III noto‘g‘ri: u mustamlakachi hukumat va mutaassib ruhoniylar qarshiligiga uchragan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Boqchasaroyda birinchi jadid maktabi", "«Rahbari muallimin» kitobi chop etildi", "Buxoroda birinchi yangi usul maktabi", "Qo‘qonda Salohiddin domla maktabi", "Buxoroda jadidchilik siyosiy tashkilot sifatida shakllana boshladi"],
      "1884 → 1888 → 1893 → 1898 → 1910.")
t.MAPMATCH(UZ, ['Buxoro', 'Qo‘qon', 'Toshkent'],
           ["1893-yilda birinchi yangi usul maktabi ochilgan joy", "1898-yilda Salohiddin domla ikkinchi jadid maktabini ochgan shahar", "1899-yilda Mannon qori jadid maktabini ochgan shahar"],
           "1 – Buxoro; 2 – Qo‘qon; 3 – Toshkent.")
t.VENN("Xiva jadidlarining o‘ng oqimi", "Xiva jadidlarining so‘l oqimi",
       [("Bosh vazir Islom xo‘ja boshchiligida", 1), ("xon hokimiyatini saqlagan holda islohot", 1),
        ("qozikalon Bobooxun Salimov rahbarligida", 2), ("yangi usul maktablari orqali xalq faolligiga erishish", 2),
        ("Xiva xonligidagi taraqqiyparvarlik harakati", 3)],
       "O‘ng — Islom xo‘ja, xonni saqlash; so‘l — Bobooxun Salimov, maktablar orqali.")
