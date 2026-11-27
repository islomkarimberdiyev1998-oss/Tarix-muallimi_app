from qlib import Topic, PLACES, REG
TOPICS = {}
W = 'globe'

# 26 Hindiston va Pokiston
t = Topic('y10j26', 10026); TOPICS['y10j26'] = t
t.B("Hindiston va Pokiston mustaqil davlatlari qachon tashkil topgan?", "1947-yil 15-avgustda", "1949-yilda", "1951-yilda", "1956-yilda", "1947-yil 15-avgust kuni.")
t.B("1947-yilda Hindiston hukumatini kim boshqargan?", "Javoharlal Neru", "Indira Gandi", "Lal Bahadur Shastri", "Narasimha Rao", "Javoharlal Neru.")
t.B("1947-yilda Pokiston hukumatini kim boshqargan?", "Liakat Alixon", "Zulfiqor Bhutto", "Ziyo ul-Haq", "M. Ayyubxon", "Liakat Alixon.")
t.B("Osiyo va Afrikadagi yangi mustaqil davlatlar ichida parlament demokratiyasini shakllantira olgan yagona davlat qaysi?", "Hindiston", "Pokiston", "Bangladesh", "Eron", "Hindiston.")
t.B("Hindistonning yangi konstitutsiyasi qachon qabul qilingan?", "1949-yilda", "1947-yilda", "1956-yilda", "1964-yilda", "1949-yili; Hindiston dunyoviy respublika deb e’lon qilindi.")
t.B("Hindiston qaysi belgiga qarab shtatlarga bo‘lingan?", "lingvistik belgiga", "diniy belgiga", "kasta belgisiga", "iqtisodiy belgiga", "Lingvistik belgiga qarab.")
t.B("1964-yili Neru vafotidan so‘ng uning o‘rnini kim egallagan?", "Lal Bahadur Shastri", "Indira Gandi", "Narasimha Rao", "Mahatma Gandi", "Lal Bahadur Shastri.")
t.B("«Toshkent deklaratsiyasi» qachon imzolangan?", "1966-yil yanvarda", "1964-yilda", "1971-yilda", "1947-yilda", "1966-yil yanvarda.")
t.B("Toshkentda to‘satdan vafot etgan Hindiston rahbari kim?", "Lal Bahadur Shastri", "Javoharlal Neru", "Indira Gandi", "Liakat Alixon", "L. B. Shastri.")
t.B("Indira Gandi kimning qizi edi?", "Javoharlal Neruning", "Mahatma Gandining", "Shastrining", "Narasimha Raoning", "J. Neruning qizi.")
t.B("Indira Gandi amalga oshirgan yangi agrar siyosat qanday atalgan?", "«yashil inqilob»", "«madaniy inqilob»", "«katta sakrash»", "«yangi kurs»", "«Yashil inqilob».")
t.B("«Yashil inqilob» natijasida qachon g‘alla va sholi hosildorligi keskin o‘sgan?", "1970-yilda", "1950-yilda", "1990-yilda", "1966-yilda", "1970-yili.")
t.B("1990-yillar boshida bozor islohotlarining yangi bosqichini qaysi hukumat boshlagan?", "Narasimha Rao hukumati", "Indira Gandi hukumati", "Neru hukumati", "Shastri hukumati", "Narasimha Rao hukumati.")
t.B("Sharqiy Bengaliya qanday davlat sifatida ajralib chiqqan?", "Bangladesh", "Pokiston", "Shri Lanka", "Nepal", "1971-yilda Bangladesh.")
t.B("Pokiston o‘z mustaqilligini qachon e’lon qilgan?", "1951-yilda", "1947-yilda", "1956-yilda", "1971-yilda", "1951-yili.")
t.B("Pokiston Respublikasi qachon tuzilganligi e’lon qilingan?", "1956-yilda", "1951-yilda", "1947-yilda", "1977-yilda", "1956-yili Ta’sis majlisi konstitutsiyasi bilan.")
t.B("1958-yilda Pokistonda kim boshchiligida harbiy to‘ntarish bo‘lgan?", "M. Ayyubxon", "Ziyo ul-Haq", "Zulfiqor Bhutto", "Liakat Alixon", "M. Ayyubxon boshchiligida.")
t.B("1977-yilgi to‘ntarishdan keyin Pokistonda nima tashkil qilingan?", "shariat sudi", "parlament demokratiyasi", "kasta tizimi", "erkin iqtisodiy zona", "Qonunlarning Qur’on va shariatga mosligini nazorat qiluvchi shariat sudi.")
t.B("1988-yili aviahalokatda halok bo‘lgan Pokiston harbiy diktatori kim?", "general Ziyo ul-Haq", "M. Ayyubxon", "Zulfiqor Bhutto", "Liakat Alixon", "General Ziyo ul-Haq.")
t.B("Ziyo ul-Haqdan keyingi saylovlar natijasida bosh vazir bo‘lgan kim?", "Benazir Bhutto", "Indira Gandi", "Zulfiqor Bhutto", "G‘ulom Is’hoqxon", "Benazir Bhutto.")
t.B("Hind jamoasiga xos tabaqalanishni ifodalovchi ijtimoiy tizim qanday ataladi?", "kasta tizimi", "feodal tizim", "sinfiy tizim", "klan tizimi", "Kasta tizimi.")
t.NAT("Hindistonning bo‘linishi paytida odamlar ommaviy o‘ldirildi.", "Hindiston va Pokiston o‘rtasida uzoq yillik o‘zaro dushmanlik hissi shakllandi", "ikki davlat birlashdi", "Britaniya qaytib keldi", "chegara muammolari yo‘qoldi", "Uzoq yillik dushmanlik hissi shakllandi.")
t.NAT("Benazir Bhutto bosh vazir bo‘ldi.", "harbiy rejim davrida qamalgan barcha siyosiy arboblarga amnistiya berildi", "shariat sudi kuchaytirildi", "favqulodda holat e’lon qilindi", "Bangladesh qayta qo‘shildi", "Barcha siyosiy arboblarga amnistiya berildi.")
t.TF("1949-yilgi konstitutsiya kastalar tengligi va hokimiyatning bo‘linishi tamoyillarini e’lon qilgan.", True, "To‘g‘ri.")
t.TF("Pokiston yagona, bir-biri bilan bog‘langan hududga ega bo‘lgan.", False, "Noto‘g‘ri: bir-biri bilan bog‘lanmagan bir qancha hududlarga ega bo‘lgan.")
t.MUL([("Neru hukumati modernizatsiya yo‘li sifatida iqtisodiyotda davlat rolini oshirishni tanlagan.", True),
       ("1977-yildan keyin Pokiston hududi 5 ta hududga bo‘linib, ularga harbiy rahbarlar tayinlangan.", True),
       ("Indira Gandi davrida g‘alla va sholi savdosi to‘liq xususiylashtirilgan.", False)],
      "III noto‘g‘ri: g‘alla, sholi va qandning ulgurji savdosi to‘liq natsionalizatsiya qilindi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Hindiston va Pokiston tashkil topdi", "Hindiston konstitutsiyasi qabul qilindi", "Pokiston mustaqilligini e’lon qildi", "Pokiston Respublikasi tuzildi", "«Toshkent deklaratsiyasi»", "Bangladesh ajralib chiqdi", "Ziyo ul-Haq halok bo‘ldi"],
      "1947 → 1949 → 1951 → 1956 → 1966 → 1971 → 1988.")
t.MATCH("Shaxslarni ularga oid ma’lumot bilan moslashtiring.", ["Javoharlal Neru", "Lal Bahadur Shastri", "Indira Gandi", "Benazir Bhutto"],
        ["1947-yilda Hindiston hukumati boshlig‘i", "Toshkentda vafot etgan", "«yashil inqilob» muallifi", "siyosiy arboblarga amnistiya bergan Pokiston bosh vaziri", "Pokistonning ilk bosh vaziri"], 'abcd',
        "Neru – 1947; Shastri – Toshkent; Indira Gandi – «yashil inqilob»; Benazir Bhutto – amnistiya.")
t.VENN("Hindiston", "Pokiston",
       [("dunyoviy respublika, parlament demokratiyasi", 1), ("«yashil inqilob»", 1),
        ("shariat sudi tashkil qilingan", 2), ("bir necha harbiy to‘ntarishlar", 2),
        ("1947-yil 15-avgustda tashkil topgan", 3)],
       "Hindiston – dunyoviy, yashil inqilob; Pokiston – shariat sudi, to‘ntarishlar; ikkalasi 1947.")
t.MAPMATCH('sasia', ['Toshkent', 'Pokiston', 'Bengaliya', 'Hindiston'],
           ["1966-yilda Hindiston va Pokiston deklaratsiya imzolagan shahar", "1956-yilda respublika deb e’lon qilingan, asosan musulmonlar yashaydigan davlat", "1971-yilda Bangladesh sifatida ajralib chiqqan hudud", "1949-yilda dunyoviy respublika deb e’lon qilingan davlat"],
           "1 – Toshkent; 2 – Pokiston; 3 – Sharqiy Bengaliya; 4 – Hindiston.")

# 27 Turkiya, Eron va Afg‘oniston
t = Topic('y10j27', 10027); TOPICS['y10j27'] = t
t.B("Ikkinchi jahon urushidan so‘ng Otaturk yo‘lini davom ettirgan Turkiya prezidenti kim?", "Ismet Inyonyu", "Kenan Evren", "Turg‘ut O‘zol", "Sulaymon Demirel", "Ismet Inyonyu.")
t.B("Sovuq urush yillarida Turkiya kim bilan birga bo‘lgan?", "G‘arb bilan", "SSSR bilan", "betaraf qolgan", "Xitoy bilan", "G‘arb bilan; «Marshall rejasi»ga kiritildi, NATOga a’zo bo‘ldi.")
t.B("1980-yil sentabrda Turkiyada harbiy to‘ntarishni kim o‘tkazgan?", "general Kenan Evren", "Turg‘ut O‘zol", "Ismet Inyonyu", "Sulaymon Demirel", "General Kenan Evren.")
t.B("Turkiyaning yangi konstitutsiyasi qachon referendumda tasdiqlangan?", "1982-yil noyabrda", "1980-yil sentabrda", "1983-yilda", "1989-yilda", "1982-yil noyabrda.")
t.B("1983-yili Turkiya bosh vaziri bo‘lgan islohotchi kim?", "Turg‘ut O‘zol", "Sulaymon Demirel", "Kenan Evren", "Ismet Inyonyu", "Turg‘ut O‘zol.")
t.B("T. O‘zol qachon Turkiya prezidenti etib saylangan?", "1989-yilda", "1983-yilda", "1990-yilda", "1982-yilda", "1989-yilgi saylovlarda.")
t.B("1990-yildan Turkiya bosh vaziri lavozimini kim egallagan?", "Sulaymon Demirel", "Turg‘ut O‘zol", "Kenan Evren", "Ismet Inyonyu", "Sulaymon Demirel.")
t.B("Ingliz va sovet qo‘shinlari Erondan qachon olib chiqilgan?", "1946-yilda", "1953-yilda", "1963-yilda", "1979-yilda", "1946-yili.")
t.B("1950-yillar birinchi yarmida Eron siyosati asosan nimaga qaratilgan?", "neft sanoatini natsionalizatsiya qilishga", "Iroq bilan urushga", "NATOga kirishga", "monarxiyani tugatishga", "Neft sanoatini natsionalizatsiya qilishga.")
t.B("Eron shohining islohotlari umumiy nom bilan qanday atalgan?", "«Oq inqilob»", "«Yashil inqilob»", "«Madaniy inqilob»", "«Savr inqilobi»", "«Oq inqilob».")
t.B("«Oq inqilob» islohotlari haqidagi referendum qachon o‘tkazilgan?", "1963-yilda", "1953-yilda", "1979-yilda", "1946-yilda", "1963-yili.")
t.B("Eron Islom Respublikasi qachon e’lon qilingan?", "1979-yilda", "1963-yilda", "1980-yilda", "1988-yilda", "1979-yil fevralda shoh rejimi ag‘darilgach.")
t.B("Eron-Iroq urushi qachongacha davom etgan?", "1988-yilgacha", "1980-yilgacha", "1990-yilgacha", "1985-yilgacha", "1980–1988-yillar.")
t.B("Afg‘oniston shohi Muhammad Zohirshoh qachon taxtdan ag‘darilgan?", "1973-yilda", "1978-yilda", "1964-yilda", "1979-yilda", "1973-yili.")
t.B("Zohirshoh ag‘darilgach prezident deb kim e’lon qilingan?", "Muhammad Dovudxon", "Nur Muhammad Taraqqiy", "Hafizullo Amin", "Muhammad Najibullo", "Muhammad Dovudxon.")
t.B("1977-yilgi konstitutsiyaga ko‘ra M. Dovud qanday prezident deb e’lon qilingan?", "umrbod prezident", "muvaqqat prezident", "faxriy prezident", "vitse-prezident", "Umrbod prezident.")
t.B("1978-yil 27-apreldagi to‘ntarishdan so‘ng Inqilobiy kengashga kim boshchilik qilgan?", "Nur Muhammad Taraqqiy", "Hafizullo Amin", "Muhammad Dovudxon", "Muhammad Najibullo", "Nur Muhammad Taraqqiy.")
t.B("Afg‘onistonga sovet qo‘shinlari qachon kiritilgan?", "1979-yil dekabrda", "1978-yil aprelda", "1986-yilda", "1989-yilda", "1979-yil dekabrda.")
t.B("1986-yili Afg‘onistonda hokimiyatga kim kelgan?", "Muhammad Najibullo", "Hafizullo Amin", "Muhammad Dovudxon", "Zohirshoh", "Muhammad Najibullo.")
t.B("SSSR Afg‘onistondan qo‘shinlarini qachon olib chiqqan?", "1989-yilda", "1986-yilda", "1979-yilda", "1991-yilda", "1989-yili.")
t.NAT("Turg‘ut O‘zol iqtisodiy islohotlarni boshladi: davlat sektori xususiylashtirildi, erkin iqtisodiy zonalar tuzildi.", "Turkiya jadal rivojlanish yo‘liga tushdi", "iqtisodiy o‘sish to‘xtadi", "Turkiya NATOdan chiqdi", "davlat sektori kengaydi", "Davlat sektori ustunligiga chek qo‘yildi.")
t.NAT("1979-yilda Eronda shoh rejimi ag‘darildi.", "G‘arb sanksiyalar e’lon qildi, iqtisodiy ahvol og‘irlashdi", "Eron G‘arb bilan ittifoq tuzdi", "«Oq inqilob» davom ettirildi", "Iroq Eron bilan birlashdi", "G‘arb sanksiyalari, keyin Iroq bostirib kirdi.")
t.TF("«Oq inqilob»ning o‘n yilida Eron iqtisodiy o‘sish bo‘yicha dunyoda eng yuqori ko‘rsatkichlarga erishgan.", True, "To‘g‘ri.")
t.TF("1980-yillargacha Turkiyada iqtisodiy o‘sish sur’atlari juda yuqori bo‘lgan.", False, "Noto‘g‘ri: 1980-yillargacha o‘sish sur’atlari past bo‘lgan.")
t.MUL([("Hafizullo Amin SSSRga murojaat qilib, sovet qo‘shinlarini kiritishni so‘ragan.", True),
       ("M. Dovudning muhim tadbirlaridan biri savodsizlikni tugatish bo‘yicha davlat boshqarmasini tuzish bo‘lgan.", True),
       ("Eron-Iroq urushini Eron qo‘shinlari Iroqqa bostirib kirib boshlagan.", False)],
      "III noto‘g‘ri: 1980-yili Iroq qo‘shinlari Eronga bostirib kirgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["«Oq inqilob» referendumi", "Zohirshoh taxtdan ag‘darildi", "Afg‘onistonda harbiy to‘ntarish (27-aprel)", "Eron Islom Respublikasi e’lon qilindi", "Turkiyada Kenan Evren to‘ntarishi", "T. O‘zol bosh vazir bo‘ldi", "SSSR qo‘shinlari Afg‘onistondan chiqarildi"],
      "1963 → 1973 → 1978 → 1979 → 1980 → 1983 → 1989.")
t.MATCH("Shaxslarni mamlakati bilan moslashtiring.", ["Turg‘ut O‘zol", "Muhammad Rizo Pahlaviy", "Muhammad Dovudxon", "Kenan Evren"],
        ["Turkiya bosh vaziri, islohotchi", "Eron shohi, «Oq inqilob»", "Afg‘oniston umrbod prezidenti", "1980-yilgi Turkiya to‘ntarishi rahbari", "Afg‘oniston Inqilobiy kengashi raisi"], 'abcd',
        "O‘zol – Turkiya; Pahlaviy – Eron; Dovudxon – Afg‘oniston; Evren – Turkiya to‘ntarishi.")
t.VENN("Turkiya", "Eron",
       [("Kenan Evren to‘ntarishi", 1), ("NATO a’zosi", 1),
        ("«Oq inqilob»", 2), ("1980–1988-yillarda Iroq bilan urush", 2),
        ("XX asrda modernizatsiya yo‘lidan borgan mamlakat", 3)],
       "Turkiya – Evren, NATO; Eron – Oq inqilob, Iroq; ikkalasi modernizatsiya yo‘lidan borgan.")
t.MAPMATCH('nearest', ['Anqara', 'Tehron', 'Kobul', 'Iroq'],
           ["T. O‘zol islohotlari o‘tkazilgan Turkiya poytaxti", "1979-yilda Islom Respublikasi e’lon qilingan davlat poytaxti", "1979-yil dekabrda sovet qo‘shinlari kiritilgan mamlakat poytaxti", "1980-yilda Eronga bostirib kirgan davlat"],
           "1 – Anqara; 2 – Tehron; 3 – Kobul; 4 – Iroq.")
