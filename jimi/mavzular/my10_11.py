from qlib import Topic, PLACES, REG
TOPICS = {}
W = 'globe'; LA = 'latam'

# 28 Suriya, Iroq va Janubi-g‘arbiy Osiyo
t = Topic('y10j28', 10028); TOPICS['y10j28'] = t
t.B("Ikkinchi jahon urushidan oldin Suriya qaysi davlatning mandati ostida bo‘lgan?", "Fransiyaning", "Buyuk Britaniyaning", "Turkiyaning", "Italiyaning", "Fransiyaning mandati ostida edi.")
t.B("Suriya o‘z mustaqilligini qachon e’lon qilgan?", "1943-yilda", "1946-yilda", "1958-yilda", "1961-yilda", "1943-yili De Gollning qarshiligiga qaramasdan.")
t.B("Suriya real mustaqillikka qachon erishgan?", "1946-yilda", "1943-yilda", "1932-yilda", "1958-yilda", "1946-yili chet el qo‘shinlari olib chiqilgach.")
t.B("Suriya va Misr ittifoqi qanday nom bilan e’lon qilingan?", "Birlashgan Arab Respublikasi (BAR)", "Birlashgan Arab Amirliklari", "Arab ligasi", "Islom konferensiyasi", "1958-yil fevralda Birlashgan Arab Respublikasi.")
t.B("Suriya BAR tarkibidan qachon chiqqan?", "1961-yil sentabrda", "1958-yil fevralda", "1970-yil noyabrda", "1946-yilda", "1961-yil sentabrdagi harbiy to‘ntarishdan so‘ng.")
t.B("1970-yil noyabrdagi to‘ntarishdan so‘ng Suriyada hokimiyat kimga o‘tgan?", "general Hafiz Asad", "Saddam Husayn", "Abdul Karim Qosim", "Feysal", "Mudofaa vaziri general Hafiz Asad.")
t.B("1990-yilda Iroqning Kuvaytga tajovuzida Suriya kimni qo‘llagan?", "Kuvaytni", "Iroqni", "betaraf qolgan", "Eronni", "Suriya Kuvayt tomonida bo‘ldi.")
t.B("Iroq o‘z mustaqilligini qachon e’lon qilgan?", "1932-yilda", "1946-yilda", "1958-yilda", "1968-yilda", "1932-yili.")
t.B("1958-yili Iroqda qaysi generallar boshchiligida to‘ntarish bo‘lgan?", "Abdul Karim Qosim va Abdul Salim Aref", "Hafiz Asad va Saddam Husayn", "Kenan Evren va O‘zol", "Feysal va Abdulloh", "Abdul Karim Qosim va Abdul Salim Aref.")
t.B("1958-yilgi to‘ntarishda qaysi qirol o‘ldirilgan?", "qirol Feysal", "Abdulloh I", "Zohirshoh", "Faruq", "Qirol Feysal va uning oilasi a’zolari.")
t.B("Saddam Husayn rasman qachon Iroq prezidenti etib saylangan?", "1979-yilda", "1968-yilda", "1980-yilda", "1990-yilda", "1979-yili.")
t.B("Iroq Eronga qarshi urushni qachon boshlagan?", "1980-yil 22-sentabrda", "1979-yilda", "1988-yilda", "1990-yilda", "1980-yil 22-sentabrda.")
t.B("Kuvaytni ozod qilish bo‘yicha xalqaro operatsiya qanday atalgan?", "«Sahrodagi bo‘ron»", "«Barbarossa»", "«Oq inqilob»", "«Katta sakrash»", "1991-yil yanvarda «Sahrodagi bo‘ron».")
t.B("Janubi-g‘arbiy Osiyo mintaqasida nechta mustaqil davlat joylashgan?", "16 ta", "7 ta", "26 ta", "10 ta", "16 ta mustaqil davlat.")
t.B("Livan qachon «erkin mamlakat» deb e’lon qilingan?", "1948-yilda", "1958-yilda", "1975-yilda", "1946-yilda", "1948-yili.")
t.B("Livanda 1975-yilda boshlangan fuqarolar urushi qachongacha davom etgan?", "1990-yilgacha", "1980-yilgacha", "1985-yilgacha", "1991-yilgacha", "1990-yilgacha.")
t.B("Transiordaniya mustaqilligi qayerda e’lon qilingan?", "Londonda", "Ammanda", "Parijda", "Qohirada", "1946-yil 22-martda Londonda.")
t.B("Iordaniyaning birinchi podshohi (maliki) kim bo‘lgan?", "Amir Abdulloh I ibn Husayn", "Feysal", "Hafiz Asad", "Saddam Husayn", "Amir Abdulloh I ibn Husayn.")
t.B("Saudiya Arabistoni 1950-yili qaysi kompaniya bilan neft qazib olish kelishuviga erishgan?", "«Aramko»", "«Mitsubisi»", "«Sumitomo»", "«Bi-bi-si»", "Amerikaning «Aramko» kompaniyasi.")
t.B("Kimning taklifi bilan «Islom konferensiyasi» tashkiloti tuzilgan?", "Saudiya podshohi Feysal", "Hafiz Asad", "Abdulloh I", "Saddam Husayn", "Podshoh Feysalning taklifi bilan Rabotda.")
t.B("BAA federatsiyasi qachon tashkil qilingan?", "1971-yilda", "1958-yilda", "1973-yilda", "1946-yilda", "1971-yili ingliz qo‘shinlari chiqib ketgach.")
t.B("BAA tarkibiga nechta amirlik kirgan?", "7 ta", "5 ta", "16 ta", "4 ta", "7 ta amirlik; eng kattalari Abu Dabi va Dubay.")
t.B("Davlatlarga nisbatan qo‘llanadigan iqtisodiy, moliyaviy yoki harbiy jazo chorasi nima deb ataladi?", "sanksiya", "mandat", "direktiva", "anneksiya", "Sanksiya.")
t.NAT("1990-yili Iroq Kuvaytga bostirib kirdi.", "1991-yil yanvarda «Sahrodagi bo‘ron» operatsiyasi boshlanib, Iroq armiyasi tor-mor qilindi", "Kuvayt Iroqqa qo‘shildi", "BMT Iroqni qo‘llab-quvvatladi", "Suriya Iroq tomonida urushdi", "Xalqaro kuchlar Kuvaytni ozod qildi.")
t.NAT("1973-yildan boshlab neft narxi keskin ko‘tarildi.", "Saudiya Arabistoni boyligi mislsiz darajaga yetdi", "Saudiya Arabistoni qashshoqlashdi", "«Aramko» bilan kelishuv bekor qilindi", "Saudiya neft eksportini to‘xtatdi", "1990-yilga kelib saudiyaliklar jahon moliya resurslarining 1/3 qismini to‘pladi.")
t.TF("Eron-Iroq urushi XX asrning eng uzoq davom etgan hududiy to‘qnashuvi bo‘lgan.", True, "To‘g‘ri.")
t.TF("1988-yili Iordaniya G‘arbiy qirg‘oq bilan aloqalarini kuchaytirgan.", False, "Noto‘g‘ri: Iordaniya G‘arbiy qirg‘oq bilan har qanday aloqani uzdi.")
t.MUL([("1980–1988-yillardagi urushda Suriya Iroqni qo‘llagan.", True),
       ("Jahonda aniqlangan neft zaxiralarining 1/4 qismi Saudiya Arabistonida joylashgan.", True),
       ("1958-yil maydagi Livan fuqarolar urushi 30 ming kishining o‘limiga olib kelgan.", False)],
      "III noto‘g‘ri: 3 ming kishining o‘limiga olib kelgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Iroq mustaqilligini e’lon qildi", "Suriya mustaqilligini e’lon qildi", "Birlashgan Arab Respublikasi e’lon qilindi", "Suriya BAR tarkibidan chiqdi", "BAA tashkil qilindi", "Iroq Kuvaytga bostirib kirdi"],
      "1932 → 1943 → 1958 → 1961 → 1971 → 1990.")
t.MATCH("Rahbarlarni mamlakati bilan moslashtiring.", ["Hafiz Asad", "Saddam Husayn", "Abdulloh I ibn Husayn", "Feysal (Saudiya podshohi)"],
        ["Suriya", "Iroq", "Iordaniya", "Saudiya Arabistoni", "Livan"], 'abcd',
        "Asad – Suriya; Saddam – Iroq; Abdulloh I – Iordaniya; Feysal – Saudiya Arabistoni.")
t.VENN("Suriya", "Iroq",
       [("1958-yilda Misr bilan BAR tuzgan", 1), ("Hafiz Asad yakkahukmronligi", 1),
        ("Saddam Husayn prezidentligi", 2), ("«Sahrodagi bo‘ron»da armiyasi tor-mor qilingan", 2),
        ("hokimiyat harbiy to‘ntarishlar orqali almashgan", 3)],
       "Suriya – BAR, Asad; Iroq – Saddam, «Sahrodagi bo‘ron»; ikkalasida harbiy to‘ntarishlar.")
t.MAPMATCH('swasia', ['Suriya', 'Quvayt', 'Iordaniya', 'BAA'],
           ["1958-yilda Misr bilan birlashib BAR tuzgan davlat", "1990-yilda Iroq bostirib kirgan davlat", "1946-yilda mustaqilligi Londonda e’lon qilingan davlat", "1971-yilda 7 ta amirlikdan tashkil topgan federatsiya"],
           "1 – Suriya; 2 – Kuvayt; 3 – Iordaniya; 4 – BAA.")

# 29 Lotin Amerikasi
t = Topic('y10j29', 10029); TOPICS['y10j29'] = t
t.B("Urushdan keyin Lotin Amerikasi mamlakatlari uchun qanday qulay sharoit vujudga kelgan?", "katta valyuta zaxirasi va jahon savdosidagi ulush oshishi", "mustamlakalarning ko‘payishi", "AQSH yordamining to‘xtashi", "aholining kamayishi", "Ular katta valyuta zaxirasiga ega bo‘ldi, savdodagi ulushi oshdi.")
t.B("1979-yili qaysi mamlakatda inqilob bo‘lgan?", "Nikaraguada", "Kubada", "Chilida", "Meksikada", "1979-yili Nikaraguada.")
t.B("Lotin Amerikasida modernizatsiyalashning nechta varianti yaqqol ko‘zga tashlangan?", "uchta", "ikkita", "to‘rtta", "beshta", "Inqilobiy, neokonservativ va islohotchilik variantlari.")
t.B("Kuba modernizatsiyaning qaysi variantini tanlagan?", "inqilobiy", "neokonservativ", "islohotchilik", "liberal", "Kuba – inqilobiy variant.")
t.B("Kuba inqilobi qachon g‘alaba qozongan?", "1959-yil 1-yanvarda", "1962-yilda", "1958-yilda", "1970-yilda", "1959-yil 1-yanvar kuni.")
t.B("Kuba inqilobiga kim boshchilik qilgan?", "Fidel Kastro", "Salvador Alyende", "Avgusto Pinochet", "Patrisio Eylvin", "Fidel Kastro.")
t.B("1959-yilda qo‘zg‘olonchilar qaysi shaharga kirib kelgan?", "Gavanaga", "Mexikoga", "Santyagoga", "Managuaga", "Gavanaga.")
t.B("Kuba hukumatining SSSR bilan kelishuvi qanday inqirozga olib kelgan?", "1962-yilgi «Karib inqirozi»", "1980-yillardagi qarz inqirozi", "1929-yilgi jahon inqirozi", "Folklend inqirozi", "1962-yilgi «Karib inqirozi».")
t.B("Kubani qanday mamlakatga aylantirish kursi tanlangan?", "agrar-industrial", "postindustrial", "sof agrar", "xomashyo", "Sof agrar Kubani agrar-industrial mamlakatga aylantirish.")
t.B("Chili modernizatsiyaning qaysi variantiga misol?", "neokonservativ", "inqilobiy", "islohotchilik", "sotsialistik", "Chili – neokonservativ variant.")
t.B("1970-yili Chili prezidenti etib kim saylangan?", "Salvador Alyende", "Avgusto Pinochet", "Patrisio Eylvin", "Fidel Kastro", "Xalq birligi nomzodi Salvador Alyende.")
t.B("Salvador Alyende qaysi blok nomzodi bo‘lgan?", "Xalq birligi", "Xalq fronti", "Milliy blok", "Xristian-demokratik partiya", "Xalq birligi bloki.")
t.B("1973-yili Chilida hokimiyatga kim boshchiligidagi harbiy xunta kelgan?", "general Avgusto Pinochet", "Salvador Alyende", "Fidel Kastro", "Patrisio Eylvin", "General Avgusto Pinochet.")
t.B("1989-yilgi Chili prezidentlik saylovlarida kim g‘olib chiqqan?", "Patrisio Eylvin", "Avgusto Pinochet", "Salvador Alyende", "Fidel Kastro", "XDP yetakchisi Patrisio Eylvin.")
t.B("Meksika modernizatsiyaning qaysi variantiga misol?", "islohotchilik", "inqilobiy", "neokonservativ", "harbiy", "Meksika – islohotchilik varianti.")
t.B("Meksika qachon sanoat mahsulotlari hajmi bo‘yicha Lotin Amerikasida birinchi o‘ringa chiqqan?", "1958-yilda", "1959-yilda", "1970-yilda", "1980-yilda", "1958-yili.")
t.B("Meksikaning muvaffaqiyatli iqtisodiy rivojlanishida nima asosiy rol o‘ynagan?", "qudratli davlat sektori", "chet el harbiy bazalari", "qulchilik", "SSSR yordami", "Ancha qudratli davlat sektori.")
t.B("Butun hokimiyat harbiylarga tegishli bo‘lgan boshqaruv shakli nima deb ataladi?", "harbiy rejim", "parlament respublikasi", "konstitutsion monarxiya", "federatsiya", "Harbiy rejim.")
t.NAT("1973-yili Chilida Pinochet boshchiligida davlat to‘ntarishi bo‘ldi.", "konstitutsiya va deyarli barcha demokratik erkinliklar bekor qilindi", "demokratiya mustahkamlandi", "Alyende islohotlari davom ettirildi", "Chili SSSR bilan ittifoq tuzdi", "Konstitutsiya va erkinliklar bekor qilindi.")
t.NAT("1980-yillardagi jahon iqtisodiy inqirozi Meksikaga ta’sir qildi.", "ishsizlik va tashqi qarz keskin oshdi, AQSHga qaramlik ortdi", "Meksika qarzlarini to‘liq to‘ladi", "Meksika AQSH bilan aloqani uzdi", "Meksikada inqilob bo‘ldi", "Ishsizlik, tashqi qarz va AQSHga qaramlik ortdi.")
t.NAT("SSSR parchalanib ketdi.", "Kuba uchun juda katta zarba bo‘ldi", "Kuba iqtisodi gullab-yashnadi", "Kastro rejimi darhol quladi", "Kuba AQSH bilan ittifoq tuzdi", "SSSRning parchalanishi Kubaga katta zarba bo‘ldi.")
t.TF("Ekvador, Peru, Boliviya, Argentina, Braziliya va Urugvayda harbiy rejimlar fuqarolik hukumatlari bilan almashtirilgan.", True, "To‘g‘ri.")
t.TF("1990-yillarda Kubada Fidel Kastro rejimi qulagan.", False, "Noto‘g‘ri: ko‘pchilik bashorat qilgan bo‘lsa-da, rejim qulamadi.")
t.MUL([("Xalq birligi blokiga kommunistlar, sotsialistlar va radikallar kirgan.", True),
       ("Pinochet islohotlarining dastlabki yillarida ishsizlik keskin oshgan.", True),
       ("Kuba inqilobi Meksika rahbarlarini liberal-islohotchilik yo‘lidan butunlay voz kechishga undagan.", False)],
      "III noto‘g‘ri: Meksika hukmron doiralari liberal-islohotchilik yo‘lidan chekinmadi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Meksika sanoatda birinchi o‘ringa chiqdi", "Kuba inqilobi g‘alaba qozondi", "«Karib inqirozi»", "Alyende prezident bo‘ldi", "Chilida Pinochet to‘ntarishi", "Nikaraguada inqilob", "Eylvin saylandi"],
      "1958 → 1959 → 1962 → 1970 → 1973 → 1979 → 1989.")
t.VENN("Kuba", "Chili",
       [("inqilobiy variant", 1), ("Fidel Kastro", 1),
        ("neokonservativ variant", 2), ("Pinochet harbiy xuntasi", 2),
        ("Lotin Amerikasida modernizatsiya yo‘lini tanlagan", 3)],
       "Kuba – inqilobiy, Kastro; Chili – neokonservativ, Pinochet; ikkalasi Lotin Amerikasi modernizatsiyasi.")
t.MAPMATCH(LA, ['Kuba', 'Chili', 'Meksika', 'Nikaragua'],
           ["modernizatsiyaning inqilobiy varianti", "modernizatsiyaning neokonservativ varianti", "modernizatsiyaning islohotchilik varianti", "1979-yilda inqilob bo‘lgan mamlakat"],
           "1 – Kuba; 2 – Chili; 3 – Meksika; 4 – Nikaragua.")

# 30 Afrikada mustaqillik
t = Topic('y10j30', 10030); TOPICS['y10j30'] = t
t.B("Qaysi davlat Mag‘rib davlatlariga kiradi?", "Marokash", "Misr", "Sudan", "Liviya", "Mag‘rib – Jazoir, Tunis, Marokash va Mavritaniya.")
t.B("1952-yilgi Misr inqilobida hokimiyatga kim boshchiligidagi «Yosh ofitserlar» kelgan?", "Jamol Abdul Nosir", "Anvar Sadat", "Husni Muborak", "Muammar Qazzofiy", "Jamol Abdul Nosir boshchiligida.")
t.B("Misrda yangi rejimning tayanchiga aylangan yagona siyosiy uyushma qanday atalgan?", "«Ozodlik tashkiloti»", "«Musulmon birodarlar»", "«Yosh ofitserlar»", "Afrika milliy kongressi", "«Ozodlik tashkiloti».")
t.B("Nosir hukumatiga qarshi chiqqan diniy-mutaassiblik tashkiloti qaysi?", "«Musulmon birodarlar»", "«Ozodlik tashkiloti»", "«Ozod ofitserlar»", "«Yosh ofitserlar»", "«Musulmon birodarlar».")
t.B("J. A. Nosir hukumati Misrni rivojlantirishda kimning yordamiga tayangan?", "SSSRning", "AQSHning", "Britaniyaning", "Fransiyaning", "SSSR yordamiga.")
t.B("Nosirdan keyin SSSR bilan aloqalarni uzib, AQSH bilan yaqinlashgan Misr prezidenti kim?", "Anvar Sadat", "Husni Muborak", "Jamol Abdul Nosir", "Ja’far Nimeyri", "Anvar Sadat.")
t.B("Anvar Sadat qachon o‘ldirilgan?", "1981-yil 6-oktyabrda", "1970-yilda", "1952-yilda", "1985-yilda", "1981-yil 6-oktyabrda.")
t.B("Sudan qachon mustaqil bo‘lgan?", "1956-yilda", "1951-yilda", "1960-yilda", "1969-yilda", "1956-yili.")
t.B("1969-yilda Sudanda hokimiyat kim boshchiligidagi Inqilobiy kengashga o‘tgan?", "polkovnik Ja’far Nimeyri", "Muammar Qazzofiy", "Anvar Sadat", "Nelson Mandela", "Polkovnik Ja’far Nimeyri.")
t.B("Liviya podshohligi qaysi hududlar birlashtirilib tuzilgan?", "Fessan, Kirenaika va Tripolitaniya", "Misr va Sudan", "Jazoir va Tunis", "Kongo va Angola", "Italiyaning sobiq mustamlakalari – Fessan, Kirenaika, Tripolitaniya.")
t.B("Liviya qachon mustaqil davlat deb e’lon qilingan?", "1951-yilda", "1949-yilda", "1956-yilda", "1969-yilda", "1951-yili.")
t.B("1969-yilda Liviyada monarxiyani kim ag‘dargan?", "Muammar Qazzofiy", "Jamol Abdul Nosir", "Ja’far Nimeyri", "Husni Muborak", "29 yoshli Muammar Qazzofiy boshchiligidagi «Yosh ofitserlar».")
t.B("V Panafrika kongressi qachon va qayerda bo‘lgan?", "1945-yil oktyabrda Manchesterda", "1900-yilda Londonda", "1960-yilda Akkrada", "1919-yilda Parijda", "1945-yil oktyabrda Manchester shahrida.")
t.B("Oltin Qirg‘oq mustaqillikka erishgach o‘zini qanday atagan?", "Gana", "Gvineya", "Keniya", "Kamerun", "Gana davlati.")
t.B("«Afrika yili»da jahon xaritasida nechta yangi Afrika davlati paydo bo‘lgan?", "17 ta", "7 ta", "27 ta", "50 ta", "1960-yilda 17 ta.")
t.B("Aholi guruhlarini irqi, millati, diniga ko‘ra qirib yuborishga qaratilgan xalqaro jinoyat nima deb ataladi?", "genotsid", "aparteid", "anneksiya", "sanksiya", "Genotsid.")
t.B("Irqiy kamsitishning eng ashaddiy ko‘rinishi nima?", "aparteid", "genotsid", "avtoritarizm", "sekulyarlik", "Aparteid.")
t.B("JAR tarixidagi birinchi qora tanli prezident kim?", "Nelson Mandela", "Muammar Qazzofiy", "Husni Muborak", "Ja’far Nimeyri", "1994-yildan so‘ng Nelson Mandela.")
t.NAT("1950-yili Liviya hududida neft va gazning katta zaxiralari aniqlandi.", "qishloq aholisi keskin kamaydi, an’anaviy hayot tarzi buzilib, armiyaning roli ortdi", "Liviya qashshoqlashdi", "monarxiya mustahkamlandi", "Liviya Italiyaga qaytdi", "Bu 1969-yilgi to‘ntarishga olib keldi.")
t.NAT("BMT va xalqaro jamoatchilik aparteid rejimini boykot qildi.", "JAR hukumati partiyalardan taqiqni olib tashladi, siyosiy mahbuslarni ozod qildi", "aparteid kuchaydi", "JAR BMTdan chiqdi", "qora tanlilar saylov huquqidan mahrum etildi", "Demokratik choralar ko‘rildi, 1994-yilda Mandela prezident bo‘ldi.")
t.TF("Aparteid rejimining ag‘darilishi bilan Afrikada mustamlakachilik to‘liq yakunlangan.", True, "To‘g‘ri.")
t.TF("Sudan XX asr oxirida mintaqaning eng rivojlangan mamlakatiga aylangan.", False, "Noto‘g‘ri: Sudan mintaqaning eng qoloq mamlakati bo‘lib qoldi.")
t.MUL([("1954-yili Misrda «Musulmon birodarlar» tashkiloti tor-mor qilingan.", True),
       ("Liviyadagi neft boyliklarini birinchi o‘rinda AQSH kompaniyalari o‘zlashtirgan.", True),
       ("JARda qora tanlilar saylovlarda erkin qatnashish huquqiga ega bo‘lgan.", False)],
      "III noto‘g‘ri: qora tanlilar saylovlarda qatnashish huquqiga ega emasdilar.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["V Panafrika kongressi", "Liviya mustaqilligi", "Misrda inqilob", "Sudan mustaqilligi", "«Afrika yili»", "Qazzofiy monarxiyani ag‘dardi", "Anvar Sadat o‘ldirildi"],
      "1945 → 1951 → 1952 → 1956 → 1960 → 1969 → 1981.")
t.MATCH("Rahbarlarni mamlakati bilan moslashtiring.", ["Jamol Abdul Nosir", "Ja’far Nimeyri", "Muammar Qazzofiy", "Nelson Mandela"],
        ["Misr", "Sudan", "Liviya", "JAR", "Gana"], 'abcd',
        "Nosir – Misr; Nimeyri – Sudan; Qazzofiy – Liviya; Mandela – JAR.")
t.VENN("Misr", "Liviya",
       [("1952-yilgi inqilob", 1), ("«Musulmon birodarlar» bilan kurash", 1),
        ("Fessan, Kirenaika va Tripolitaniyadan tuzilgan", 2), ("Qazzofiy hukmronligi", 2),
        ("«Yosh ofitserlar» hokimiyatga kelgan", 3)],
       "Misr – 1952, «Musulmon birodarlar»; Liviya – Fessan, Qazzofiy; ikkalasida «Yosh ofitserlar».")
t.MAPMATCH('africa', ['Misr (Afrika)', 'Liviya (Afrika)', 'Gana (Oltin Qirg‘oq)', 'Janubiy Afrika Respublikasi'],
           ["1952-yilda «Yosh ofitserlar» inqilobi bo‘lgan davlat", "1969-yilda Qazzofiy monarxiyani ag‘dargan davlat", "Oltin Qirg‘oq o‘rnida tuzilgan davlat", "aparteid rejimi hukm surgan davlat"],
           "1 – Misr; 2 – Liviya; 3 – Gana; 4 – JAR.")
