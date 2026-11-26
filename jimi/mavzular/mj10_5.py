from qlib import Topic
TOPICS = {}
W = 'globe'; EU = 'europe'; EA = 'eastasia'; IN = 'india'; LA = 'latam'; AF = 'africa'

# 21 Britaniya va Fransiya 1946–1991
t = Topic('e10j21', 1021); TOPICS['e10j21'] = t
t.B("Urushdan keyingi dastlabki saylovlarda Britaniyada qaysi partiya g‘olib chiqqan?", "leyboristlar", "konservatorlar", "liberallar", "kommunistlar", "Leyboristlar partiyasi g‘olib chiqdi.")
t.B("Buyuk Britaniya NATOga qachon a’zo bo‘lgan?", "1949-yilda", "1951-yilda", "1955-yilda", "1946-yilda", "1949-yili.")
t.B("1951-yilgi saylovlardan so‘ng bosh vazir kim bo‘lgan?", "Uinston Cherchill", "Margaret Tetcher", "Klement Ettli", "Jon Meyjor", "Konservatorlar g‘alaba qozonib, Cherchill bosh vazir bo‘ldi.")
t.B("Margaret Tetcher qachon bosh vazir bo‘lgan?", "1979-yilda", "1970-yilda", "1990-yilda", "1964-yilda", "1979-yilgi saylovlardan so‘ng.")
t.B("1979–1990-yillar Britaniya tarixida qanday nom olgan?", "«Tetcher davri»", "«Cherchill davri»", "«turg‘unlik davri»", "«leyboristlar davri»", "«Tetcher davri».")
t.B("Tetcherdan keyin bosh vazir kim bo‘lgan?", "Jon Meyjor", "Toni Bler", "Garold Vilson", "Cherchill", "1990-yili Jon Meyjor.")
t.B("Britaniya Shimoliy Irlandiyaga qachon qo‘shin kiritgan?", "1969-yilda", "1982-yilda", "1949-yilda", "1979-yilda", "1969-yili.")
t.B("Britaniya Folklend orollari uchun qaysi davlat bilan urushgan?", "Argentina", "Braziliya", "Chili", "Ispaniya", "1982-yili Argentina bilan.")
t.B("Fransiyaning yangi konstitutsiyasi (To‘rtinchi respublika) qachon kuchga kirgan?", "1946-yilda", "1958-yilda", "1945-yilda", "1968-yilda", "1946-yili.")
t.B("1958-yilda To‘rtinchi respublikani tugatgan kim?", "Sharl de Goll", "Fransua Mitteran", "Pyer Laval", "Daladye", "Sharl de Goll Milliy majlisni tarqatib yubordi.")
t.B("De Goll Fransiya prezidenti etib qachon saylangan?", "1958-yil 21-dekabrda", "1958-yil sentabrda", "1946-yilda", "1960-yilda", "1958-yil 21-dekabrda.")
t.B("De Goll Afrikadagi deyarli barcha mustamlakalarga qachon mustaqillik bergan?", "1960-yilda", "1958-yilda", "1968-yilda", "1962-yilda", "1960-yili.")
t.B("Parij talabalarining namoyishi qachon boshlangan?", "1968-yil mayda", "1958-yilda", "1960-yilda", "1981-yilda", "1968-yil mayda.")
t.B("1970-yillar oxiridan keyin Fransiya prezidenti etib qaysi sotsialist saylangan?", "Fransua Mitteran", "Sharl de Goll", "Jak Shirak", "Jorj Pompidu", "Sotsialist Fransua Mitteran.")
t.B("Umumxalq ovoz berishi qanday ataladi?", "referendum", "plenum", "eksport", "retsessiya", "Referendum.")
t.NAT("Davlatning qat’iy tartibga solish siyosati ko‘p qatlamlarni norozi qildi.", "referendumda prezidentni qo‘llamaganlar ko‘p bo‘lib, de Goll iste’foga chiqdi", "de Goll qayta saylandi", "Fransiya monarxiya bo‘ldi", "Mitteran iste’foga chiqdi",
      "1968-yildagi voqealardan so‘ng de Goll iste’foga chiqishga majbur bo‘ldi.")
t.NAT("Tetcher hukumati xususiy tadbirkorlikni rivojlantirib, soliqlarni kamaytirdi.", "Yevropada eng ko‘p ish o‘rinlari yaratildi", "ishsizlik keskin oshdi", "davlat sektori kengaydi", "Britaniya inqirozga uchradi",
      "Tetcher davrida Yevropada eng ko‘p ish o‘rinlari yaratildi.")
t.TF("1946-yilgi Fransiya konstitutsiyasi Yevropadagi eng demokratik konstitutsiyalardan biri bo‘lgan.", True, "To‘g‘ri.")
t.TF("Mitteran hukumati inflatsiya va ishsizlikni butunlay to‘xtatgan.", False, "Noto‘g‘ri: inflatsiyani to‘xtatishning iloji bo‘lmadi, ishsizlik oshdi.")
t.MUL([("Britaniya «Marshall rejasi»da ishtirok etgan.", True), ("Konservatorlar 1951-yildan Britaniyani 13 yil boshqargan.", True), ("Folklend urushida Britaniya mag‘lub bo‘lgan.", False)],
      "III noto‘g‘ri: Britaniya g‘alaba qozongan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Fransiya yangi konstitutsiyasi", "Britaniya NATOga kirdi", "Cherchill yana bosh vazir", "De Goll prezident bo‘ldi", "Parij talabalari namoyishi", "Folklend urushi"],
      "1946 → 1949 → 1951 → 1958 → 1968 → 1982.")
t.MAPN('globe2', ['Folklend orollari', 'Shimoliy Irlandiya', 'Hindiston', 'Avstraliya'], "1982-yilda Britaniya Argentina bilan urushgan Janubiy Atlantikadagi orollar qaysi raqam bilan belgilangan?", "Folklend orollari – 1.", ask_idx=0)
t.MAPN('globe2', ['Folklend orollari', 'Shimoliy Irlandiya', 'Hindiston', 'Avstraliya'], "1969-yilda Britaniya qo‘shin kiritgan hudud qaysi raqam bilan belgilangan?", "Shimoliy Irlandiya – 2.", ask_idx=1)
t.VENN("Margaret Tetcher", "Sharl de Goll",
       [("Britaniya konservatorlari yetakchisi", 1), ("soliqlarni kamaytirgan, davlat sektorini qisqartirgan", 1),
        ("Beshinchi respublika asoschisi", 2), ("Afrika mustamlakalariga mustaqillik bergan", 2),
        ("mamlakatining kuchli rahbari bo‘lgan", 3)],
       "Tetcher – konservator, islohot. De Goll – V respublika, dekolonizatsiya.")

# 22 Germaniya va Italiya 1946–1991
t = Topic('e10j22', 1022); TOPICS['e10j22'] = t
t.B("Germaniya Federativ Respublikasi qachon tashkil qilingan?", "1949-yil mayda", "1949-yil 7-oktabrda", "1955-yilda", "1990-yil 3-oktabrda", "1949-yil mayda.")
t.B("GFRning birinchi kansleri kim?", "Konrad Adenauer", "Gelmut Kol", "Villi Brandt", "Gindenburg", "Konrad Adenauer.")
t.B("Germaniya Demokratik Respublikasi qachon tashkil qilingan?", "1949-yil 7-oktabrda", "1949-yil mayda", "1945-yilda", "1961-yilda", "1949-yil 7-oktabrda.")
t.B("GDRning poytaxti qaysi shahar edi?", "Sharqiy Berlin", "Bonn", "Leypsig", "Drezden", "Sharqiy Berlin.")
t.B("GFR NATOga qachon a’zo bo‘lgan?", "1955-yilda", "1949-yilda", "1957-yilda", "1990-yilda", "1955-yili.")
t.B("1960–1970-yillardagi GFR iqtisodining jadal o‘sishi qanday nom olgan?", "«nemis iqtisodiy mo‘jizasi»", "«Reyganomika»", "«Yangi kurs»", "«Tetcher davri»", "«Nemis iqtisodiy mo‘jizasi».")
t.B("1982-yilda GFR kansleri etib kim saylangan?", "Gelmut Kol", "Konrad Adenauer", "Villi Brandt", "Gerxard Shryoder", "Xristian-demokrat Gelmut Kol.")
t.B("Berlin devori qachon buzib tashlangan?", "1989-yilda", "1990-yilda", "1985-yilda", "1991-yilda", "1989-yili GDRda inqilob boshlanib, devor buzildi.")
t.B("Yagona Germaniya davlati qachon tashkil topgan?", "1990-yil 3-oktabrda", "1989-yil noyabrda", "1991-yilda", "1949-yilda", "1990-yil 3-oktabrda.")
t.B("Italiyaning yangi konstitutsiyasi qachon kuchga kirgan?", "1948-yil 1-yanvardan", "1946-yildan", "1957-yildan", "1950-yildan", "1948-yil 1-yanvardan.")
t.B("Yevropa iqtisodiy hamkorligini tuzish to‘g‘risidagi shartnoma qaysi?", "1957-yilgi Rim shartnomasi", "Parij ahdlashuvi", "Versal shartnomasi", "Maastrixt shartnomasi", "1957-yilgi Rim shartnomasi.")
t.B("Italiyada chuqur iqtisodiy inqiroz qachon boshlangan?", "1974-yilda", "1957-yilda", "1968-yilda", "1980-yilda", "1974-yili.")
t.B("Germaniya va Avstriyada hukumat boshlig‘i qanday ataladi?", "kansler", "prezident", "premyer", "dyuk", "Kansler.")
t.B("Uyushgan jinoyatchilik tashkiloti qanday ataladi?", "mafiya", "koalitsiya", "defitsit", "konsern", "Mafiya.")
t.NAT("«Marshall rejasi» yordami, kam harbiy xarajat va arzon ishchi kuchi GFRda birlashdi.", "GFR xo‘jaligi jadal tiklanib, qarzlardan qutuldi", "GFR inqirozga uchradi", "GFR GDRga qo‘shildi", "GFR NATOdan chiqdi",
      "GFR barcha qarzlaridan qutulib, oltin-valuta zaxirasini yaratdi.")
t.NAT("Parij ahdlashuvi kuchga kirdi (1955).", "GFR uchun okkupatsiya davri tugadi", "Germaniya bo‘lindi", "GDR tashkil topdi", "Berlin devori qurildi",
      "GFR NATOga kirib, okkupatsiya davri tugadi.")
t.NAT("Italiyada mafiya korrupsiyalashgan davlat unsurlari bilan qo‘shilib ketdi.", "1980–1990-yillar boshi mafiyaga qarshi kurash davri bo‘ldi", "mafiya qonuniylashtirildi", "Italiya monarxiya bo‘ldi", "iqtisod tez o‘sdi",
      "Mafiyaga qarshi kurash davri boshlandi.")
t.TF("Germaniyaning ikkita davlatga bo‘linishi qariyb yarim asr davom etgan.", True, "To‘g‘ri.")
t.TF("Italiyada hukumatlarning barqarorligi uning an’anasiga aylangan.", False, "Noto‘g‘ri: hukumatning tez-tez almashishi an’anaga aylangan.")
t.MUL([("Italiya hududida AQSHning harbiy bazalari joylashtirilgan.", True), ("Ish tashlash harakati bo‘yicha Italiya boshqa mamlakatlardan oldinlab ketgan.", True), ("1990-yil dekabr saylovlarida G. Kol koalitsiyasi mag‘lub bo‘lgan.", False)],
      "III noto‘g‘ri: G. Kol koalitsiyasi yana g‘alaba qozongan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Italiya yangi konstitutsiyasi", "GFR tashkil qilindi", "GFR NATOga kirdi", "Rim shartnomasi", "Gelmut Kol kansler bo‘ldi", "Berlin devori buzildi", "Germaniya birlashdi"],
      "1948 → 1949 → 1955 → 1957 → 1982 → 1989 → 1990.")
t.MAPN(EU, ['Berlin', 'Rim', 'Parij', 'London'], "1989-yilda devori buzilgan, sharqiy qismi GDR poytaxti bo‘lgan shahar qaysi raqam bilan belgilangan?", "Berlin – 1.", ask_idx=0)
t.MAPN(EU, ['Berlin', 'Rim', 'Parij', 'London'], "1957-yilda Yevropa iqtisodiy hamkorligi to‘g‘risidagi shartnoma imzolangan shahar qaysi raqam bilan belgilangan?", "Rim – 2.", ask_idx=1)
t.VENN("GFR", "GDR",
       [("AQSH, Britaniya va Fransiya zonalarida tuzilgan", 1), ("«nemis iqtisodiy mo‘jizasi»", 1),
        ("sovetlar okkupatsiya zonasida tuzilgan", 2), ("poytaxti Sharqiy Berlin", 2),
        ("1949-yilda tashkil topgan nemis davlati", 3)],
       "GFR – G‘arb zonalari; GDR – sovet zonasi. Ikkalasi 1949-yilda tuzilgan.")

# 23 Yaponiya va Osiyoning yangi industrial mamlakatlari
t = Topic('e10j23', 1023); TOPICS['e10j23'] = t
t.B("Ikkinchi jahon urushida qancha yapon halok bo‘lgan?", "6,5 mln.", "27 mln.", "1 mln.", "15 mln.", "6,5 mln. yapon halok bo‘ldi.")
t.B("Okkupatsiya qilingan Yaponiyada hokimiyat kimning shtabiga o‘tgan?", "general Duglas Makartur", "Edvards Deming", "Garri Trumen", "Eyzenxauer", "General Duglas Makartur boshchiligidagi AQSH shtabiga.")
t.B("Yaponiya hukumati qachongacha AQSH shtabi nazoratida bo‘lgan?", "1952-yilgacha", "1946-yilgacha", "1960-yilgacha", "1970-yilgacha", "1952-yilgacha.")
t.B("Yaponiyada kasaba uyushmalari to‘g‘risidagi qonun qachon qabul qilingan?", "1946-yilda", "1950-yilda", "1952-yilda", "1956-yilda", "1946-yili.")
t.B("Yaponiyada mahsulot sifati haqida ma’ruzalar qilgan amerikalik iqtisodchi kim?", "Edvards Deming", "Duglas Makartur", "Jorj Marshall", "Adam Smit", "Edvards Deming.")
t.B("«Yapon iqtisodiy mo‘jizasi» qaysi yillarni o‘z ichiga oladi?", "1956–1970", "1946–1952", "1970–1980", "1980–1991", "1956–1970-yillar.")
t.B("«Iqtisodiy mo‘jiza» davrida Yaponiya iqtisodi yiliga qancha o‘sgan?", "11 % dan", "3 %", "25 %", "1 %", "Yiliga 11 %dan.")
t.B("1960-yillar oxirida Yaponiya YAIM hajmi bo‘yicha dunyoda nechanchi o‘ringa chiqqan?", "ikkinchi (AQShdan keyin)", "birinchi", "uchinchi", "beshinchi", "AQShdan keyin ikkinchi o‘ringa.")
t.B("Yaponiya yutuqlarini namoyish etgan ko‘rgazma qaysi?", "«EKSPO–70» (Tokio)", "«EKSPO–58»", "Olimpiada–64", "«Osiyo–80»", "Tokioda bo‘lgan «EKSPO–70».")
t.B("1980-yillardan Yaponiyada nechta texnopolis tashkil qilingan?", "26 ta", "10 ta", "100 ta", "5 ta", "26 ta texnopolis.")
t.B("Qaysi davlatlar «Osiyo yo‘lbarslari» deb atalgan?", "Janubiy Koreya, Tayvan, Singapur, Gonkong", "Xitoy, Hindiston, Pokiston, Eron", "Tayland, Malayziya, Indoneziya, Filippin", "Yaponiya, Xitoy, Koreya, Vyetnam", "Janubiy Koreya, Tayvan, Singapur, Gonkong.")
t.B("Yaponiya modeli asosida rivojlanayotgan «ikkinchi to‘lqin» davlatlari qaysilar?", "Tayland, Malayziya, Indoneziya, Filippin", "Janubiy Koreya, Tayvan", "Hindiston, Pokiston", "Xitoy, Vyetnam", "Tayland, Malayziya, Indoneziya, Filippin.")
t.B("Texnologik yangiliklarni qo‘llash uchun tashkil qilingan erkin iqtisodiy hudud qanday ataladi?", "texnopolis", "konsern", "korporatsiya", "kolxoz", "Texnopolis.")
t.NAT("1970-yillarda neft inqirozi yuz berdi.", "Yaponiya ilmtalab ishlab chiqarishga o‘tib, postindustrial model shakllandi", "Yaponiya iqtisodi yanada arzon neftga tayandi", "Yaponiya qashshoqlashdi", "Yaponiya qayta qurollandi",
      "Arzon neftga asoslangan model o‘zgartirildi.")
t.NAT("Janubiy Koreyada 1970-yillardan og‘ir sanoat va elektronika rivojlantirildi.", "1990-yillarga kelib Janubiy Koreya rivojlangan industrial davlatga aylandi", "Koreya qoloq agrar davlat bo‘lib qoldi", "Koreya Yaponiyaga qo‘shildi", "Koreya eksportdan voz kechdi",
      "Janubiy Koreya po‘lat, kema, avtomobil eksportida yetakchiga aylandi.")
t.TF("Amerikaliklar yaponlarning jangovarlik ruhini sindirishni maqsad qilgan.", True, "To‘g‘ri.")
t.TF("Yaponiyada okkupatsiya davrida matbuot senzurasi kuchaytirilgan.", False, "Noto‘g‘ri: matbuotda senzura bekor qilingan.")
t.MUL([("1950-yildan kadrlar tayyorlashning amerikacha standartlari joriy qilingan.", True), ("Yangi industrial davlatlarni parlament demokratiyasi va erkin bozor birlashtiradi.", True), ("Yaponiya urushdan keyin barcha mustamlakalarini saqlab qolgan.", False)],
      "III noto‘g‘ri: Yaponiya barcha mustamlakalaridan ayrildi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Kasaba uyushmalari qonuni", "Amerikacha kadrlar standarti", "AQSH nazorati tugadi", "«Iqtisodiy mo‘jiza» boshlandi", "«EKSPO–70»"],
      "1946 → 1950 → 1952 → 1956 → 1970.")
t.MAPN('seasia', ['Janubiy Koreya', 'Yaponiya', 'Indoneziya', 'Tayland'], "1970-yillardan og‘ir sanoat va elektronikani rivojlantirib, «Osiyo yo‘lbarslari»dan biriga aylangan davlat qaysi raqam bilan belgilangan?", "Janubiy Koreya – 1.", ask_idx=0)
t.MAPN('seasia', ['Janubiy Koreya', 'Yaponiya', 'Indoneziya', 'Tayland'], "1956–1970-yillarda «iqtisodiy mo‘jiza»ni boshdan kechirgan davlat qaysi raqam bilan belgilangan?", "Yaponiya – 2.", ask_idx=1)
t.VENN("Yaponiya", "Janubiy Koreya",
       [("1956–1970-yillardagi «iqtisodiy mo‘jiza»", 1), ("26 ta texnopolis tashkil qilingan", 1),
        ("«Osiyo yo‘lbarslari»dan biri", 2), ("1970-yillardan og‘ir sanoat rivojlantirilgan", 2),
        ("postindustrial taraqqiyot elementlariga ega", 3)],
       "Yaponiya – mo‘jiza, texnopolis. Koreya – yo‘lbars, 1970-yillar. Ikkalasi postindustrial elementli.")
