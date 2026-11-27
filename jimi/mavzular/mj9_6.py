from qlib import Topic
TOPICS = {}
LA = 'latam'; BK = 'balkan'; FE = 'fareast'; EU = 'europe'

# 18 Lotin Amerikasining boshqa davlatlari
t = Topic('e9j18', 9118); TOPICS['e9j18'] = t
t.B("Braziliyada qancha aholi yashagan?", "15 mln", "750 ming", "300 ming", "50 mln", "15 mln aholi.")
t.B("Braziliyada shakarqamish plantatsiyalaridagi qullar qo‘zg‘oloniga kim boshchilik qilgan?", "Bonifatsio", "Antonio Predo", "Pedru II", "Xose Marti", "Qul Bonifatsio.")
t.B("Qullarni ozod qilgan plantator, keyin davlat vaziri bo‘lgan shaxs kim?", "Antonio Predo", "Bonifatsio", "Pedru II", "Madero", "Antonio Predo.")
t.B("Qullarni ozod qilish haqidagi qonun qanday nom bilan mashhur?", "«Oltin qonun»", "«Ozodlik manifesti»", "«Yer va ozodlik»", "«Monro doktrinasi»", "«Oltin qonun».")
t.B("«Oltin qonun»ni kim imzolagan?", "malika Izabel", "imperator Pedru II", "Antonio Predo", "Bonifatsio", "Malika Izabel, 1888-yilda.")
t.B("1888-yilda Braziliyada qancha qul bo‘lgan?", "750 ming", "15 mln", "300 ming", "1,5 mln", "750 ming.")
t.B("Respublika tarafdorlarining katta namoyishi qayerda bo‘lgan?", "Rio-de-Janeyroda", "Buenos-Ayresda", "Mexikoda", "Lissabonda", "Rio-de-Janeyroda.")
t.B("Pedru II qachon taxtdan voz kechgan?", "1889-yil 19-noyabrda", "1888-yilda", "1891-yilda", "1876-yilda", "1889-yil 19-noyabrda; Portugaliyaga jo‘nab ketdi.")
t.B("1891-yilgi konstitutsiyaga ko‘ra Braziliya qanday ataladigan bo‘ldi?", "Braziliya Qo‘shma Shtatlari", "Braziliya imperiyasi", "Braziliya Federativ Respublikasi", "Janubiy Amerika Ittifoqi", "Braziliya Qo‘shma Shtatlari.")
t.B("Argentinada iqtisodiy hayot qaysi urush oqibatida deyarli to‘xtab qolgan?", "Paragvay bilan urush", "Braziliya bilan urush", "Ispaniya bilan urush", "AQSH bilan urush", "Paragvay bilan urush va ichki kurash oqibatida.")
t.B("Immigratsiya rag‘batlantirilgach, Argentinaga qancha kishi ko‘chib kelgan?", "300 ming", "15 mln", "750 ming", "25 mln", "300 ming kishi.")
t.B("Argentinada immigratsiya va kolonizatsiya to‘g‘risidagi qonun qachon qabul qilingan?", "1876-yilda", "1888-yilda", "1895-yilda", "1910-yilda", "1876-yilda.")
t.B("Qonunga ko‘ra davlat yerlari necha gektardan oshmaydigan maydonlarga bo‘linib sotilgan?", "80 gektardan", "10 gektardan", "500 gektardan", "1000 gektardan", "80 gektardan.")
t.B("Argentinada Sotsialistik partiya qachon tuzilgan?", "1895-yilda", "1876-yilda", "1888-yilda", "1910-yilda", "1895-yilda.")
t.B("Gonduras, Salvador va Nikaragua 1895–1896-yillarda qanday davlatga birlashgan?", "Buyuk Markaziy Amerika Respublikasi", "Panamerika ittifoqi", "Braziliya Qo‘shma Shtatlari", "Kolumbiya", "Buyuk Markaziy Amerika Respublikasi.")
t.B("Qora tanlilarni qullikdan ozod qilish harakati nima deyiladi?", "abolitsionizm", "segregatsiya", "kolonizatsiya", "panamerikanizm", "Abolitsionizm.")
t.NAT("Qulchilik bekor qilingach, respublika uchun kurash kuchaydi.", "Pedru II taxtdan voz kechib, mamlakat Respublika deb e’lon qilindi", "monarxiya mustahkamlandi", "qullik tiklandi", "Braziliya Portugaliyaga qo‘shildi", "1889-yilda Respublika e’lon qilindi.")
t.NAT("AQSH Markaziy Amerikada o‘z siyosatiga to‘g‘onoq bo‘ladigan ittifoqni istamadi.", "AQSH monopoliyalari Buyuk Markaziy Amerika Respublikasini tarqatib yuborishga erishdi", "ittifoq kuchaydi", "AQSH ittifoqqa qo‘shildi", "Meksika ittifoqqa kirdi", "Respublika tarqatib yuborildi.")
t.TF("Gvatemala ichki kurashlardan holdan toyib, AQSHga qaram bo‘lib qolgan.", True, "To‘g‘ri.")
t.TF("Braziliyada barcha fuqarolarga, savodsizlarga ham saylov huquqi berilgan.", False, "Noto‘g‘ri: faqat yozish va o‘qishni biluvchi fuqarolarga.")
t.MUL([("Argentinada hindularning hosildor yerlari tortib olinib, ofitser va askarlarga berilgan.", True),
       ("Buenos-Ayresda milliy bank, piyoda askarlar va harbiy dengiz maktabi ochilgan.", True),
       ("Bonifatsio qo‘shini hukumat qo‘shinlarini yengib, qullarni ozod qilgan.", False)],
      "III noto‘g‘ri: hukumat qo‘shinlari Bonifatsio qo‘shinini tor-mor etgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Argentinada kolonizatsiya qonuni", "«Oltin qonun»", "Pedru II taxtdan voz kechdi", "Braziliyaning yangi konstitutsiyasi", "Argentinada Sotsialistik partiya tuzildi"],
      "1876 → 1888 → 1889 → 1891 → 1895.")
t.MAPMATCH(LA, ['Rio-de-Janeyro', 'Buenos-Ayres', 'Gvatemala'],
           ["respublika tarafdorlarining katta namoyishi bo‘lgan Braziliya shahri", "milliy bank va harbiy maktablar ochilgan Argentina shahri", "ichki kurashlardan holdan toyib AQSHga qaram bo‘lgan Markaziy Amerika davlati"],
           "1 – Rio-de-Janeyro; 2 – Buenos-Ayres; 3 – Gvatemala.")
t.VENN("Braziliya", "Argentina",
       [("1888-yilda «Oltin qonun» qabul qilingan", 1), ("1889-yilda Respublika e’lon qilingan", 1),
        ("1876-yilda kolonizatsiya qonuni", 2), ("1895-yilda Sotsialistik partiya tuzilgan", 2),
        ("chet el monopoliyalari hal qiluvchi tarmoqlarni egallagan", 3)],
       "Braziliya — Oltin qonun, Respublika; Argentina — kolonizatsiya, Sotsialistik partiya.")

# 19 Rossiya imperiyasining ijtimoiy-siyosiy va iqtisodiy ahvoli
t = Topic('e9j19', 9119); TOPICS['e9j19'] = t
t.B("Rossiya bu davrda qanday davlat edi?", "cheklanmagan monarxiya", "konstitutsiyaviy monarxiya", "respublika", "federatsiya", "Hokimiyat imperator qo‘lida to‘plangan cheklanmagan monarxiya.")
t.B("Imperator hokimiyatining asosiy tayanchi kimlar edi?", "pomeshiklar va Pravoslav cherkovi", "burjuaziya", "ishchilar", "dehqonlar", "Pomeshiklar va Pravoslav cherkovi.")
t.B("Imperator xonadoni qancha yerga egalik qilgan?", "7 mln desyatina", "1 mln desyatina", "70 mln desyatina", "700 ming desyatina", "7 mln desyatina.")
t.B("1 desyatina necha gektarga teng?", "1,1 gektar", "1 gektar", "2,5 gektar", "0,5 gektar", "1,1 gektar.")
t.B("Rossiya qaysi mahsulotni qazib chiqarishda dunyoda birinchi o‘ringa chiqqan?", "neft", "ko‘mir", "temir", "oltin", "Neft — AQSHni ortda qoldirdi.")
t.B("Rossiya qora metallurgiyasidagi yirik monopoliya qaysi?", "«Prodamet»", "«Produgol»", "«Med»", "«Standart oyl»", "«Prodamet»; ko‘mirda — «Produgol».")
t.B("Rossiya sanoatiga qo‘yilgan chet el kapitalining asosiy qismi qaysi davlatniki edi?", "Fransiya", "Germaniya", "Britaniya", "AQSH", "Fransiya kapitali.")
t.B("Rossiyaning asosiy eksport qishloq xo‘jaligi mahsuloti nima edi?", "g‘alla", "paxta", "jun", "qand", "G‘alla.")
t.B("Rossiya imperiyasi tarkibida nechtadan ortiq millat va xalq yashagan?", "100 dan ortiq", "10 dan ortiq", "50 ta", "1000 dan ortiq", "100 dan ortiq.")
t.B("Birinchi rus inqilobi qachon yuz bergan?", "1905-yilda", "1904-yilda", "1906-yilda", "1917-yilda", "1905-yilda.")
t.B("Agrar islohot haqidagi farmon qachon chiqarilgan?", "1906-yilda", "1905-yilda", "1911-yilda", "1907-yilda", "1906-yilda.")
t.B("Agrar islohot kimning tashabbusi bilan bog‘liq?", "P. A. Stolipin", "Nikolay II", "Plexanov", "Lenin", "Bosh vazir P. A. Stolipin.")
t.B("Badavlat dehqonlar qanday atalgan?", "quloqlar", "pomeshiklar", "yunkerlar", "fermerlar", "Quloqlar.")
t.B("Stolipin qachon otib o‘ldirilgan?", "1911-yilda", "1906-yilda", "1905-yilda", "1914-yilda", "1911-yilda.")
t.NAT("1904-yildagi Rossiya-Yaponiya urushi xalq turmushini yanada og‘irlashtirdi.", "1905-yilda birinchi rus inqilobi yuz berdi", "Rossiya boyidi", "monarxiya kuchaydi", "agrar islohot bekor qilindi", "Urush inqilobga olib keldi.")
t.NAT("Ko‘chirish siyosatida Turkistondagi eng yaxshi yerlar ko‘chib kelganlarga berildi.", "milliy chekka o‘lkalardagi siyosiy vaziyat keskinlashdi", "mahalliy aholi boyidi", "ko‘chirish to‘xtadi", "Turkiston mustaqil bo‘ldi", "Yerli aholi og‘ir yerlarga surib chiqarildi.")
t.TF("Rossiyada chetga kapital chiqarishdan ko‘ra chetdan kapital kiritish ustun edi.", True, "To‘g‘ri.")
t.TF("Stolipin agrar islohoti pomeshik yer egaligini butunlay tugatgan.", False, "Noto‘g‘ri: islohot pomeshik yer egaligini tugata olmadi.")
t.MUL([("Islohotga ko‘ra jamoa yer egaligi bekor qilinib, dehqonga o‘z yerini sotish huquqi berildi.", True),
       ("Dehqonlarga «Dehqonlar banki» orqali yer sotib olishda yordam berildi.", True),
       ("Islohotga ko‘ra dehqonlar Sibirdan markaziy mintaqalarga ko‘chirildi.", False)],
      "III noto‘g‘ri: markaziy mintaqalardan Sibir, Turkiston, Uzoq Sharqqa ko‘chirildi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Rossiya-Yaponiya urushi", "Birinchi rus inqilobi", "Agrar islohot farmoni", "«Med» jamiyati", "Stolipin o‘ldirildi"],
      "1904 → 1905 → 1906 → 1907 → 1911.")
t.VENN("Stolipin agrar islohotining natijalari", "Islohotning kamchiliklari",
       [("qishloqda kapitalizm rivojiga yo‘l ochildi", 1), ("quloqlar mavqeyi mustahkamlandi", 1),
        ("pomeshik yer egaligi tugatilmadi", 2), ("ko‘chirish moddiy jihatdan ta’minlanmadi", 2),
        ("qishloq aholisining tabaqalanishi kuchaydi", 3)],
       "Islohot kapitalizmga yo‘l ochdi, lekin pomeshik yerini tugatmadi.")

# 20 Rossiya imperiyasining tashqi siyosati
t = Topic('e9j20', 9120); TOPICS['e9j20'] = t
t.B("Rossiya mustamlakachilik imperiyasining Britaniya va Fransiyanikidan farqi nima edi?", "bosib olingan hududlar imperiya tarkibiga bevosita qo‘shib olingan", "uning dengizorti mustamlakalari ko‘p edi", "u mustamlakalarni sotgan", "u faqat Afrikada mustamlaka olgan", "Hududlar bevosita imperiyaga qo‘shilgan.")
t.B("Xiva xonligi qachon vassal davlatga aylantirilgan?", "1873-yilda", "1885-yilda", "1868-yilda", "1876-yilda", "1873-yilda.")
t.B("O‘rta Osiyo qachon to‘la bo‘ysundirilgan?", "1885-yilda", "1873-yilda", "1891-yilda", "1867-yilda", "1885-yilda.")
t.B("1875-yilda qayerda Usmonli davlatiga qarshi qo‘zg‘olon ko‘tarilgan?", "Bosniya va Gersegovinada", "Serbiyada", "Ruminiyada", "Kiprda", "Bosniya va Gersegovinada.")
t.B("Rossiya Usmonli davlatiga qachon urush e’lon qilgan?", "1877-yil 24-aprelda", "1878-yil 13-iyunda", "1876-yilda", "1875-yilda", "1877-yil 24-aprelda.")
t.B("Rossiya–Usmonli shartnomasi 1878-yilda qayerda imzolangan?", "San-Stefanoda", "Berlinda", "Parijda", "Istanbulda", "San-Stefanoda.")
t.B("San-Stefano shartnomasiga ko‘ra qaysi davlatlar to‘la mustaqil deb tan olingan?", "Chernogoriya, Serbiya, Ruminiya", "Bolgariya, Gretsiya", "Bosniya, Gersegovina", "Kipr, Krit", "Chernogoriya, Serbiya va Ruminiya.")
t.B("Berlin kongressi qachon ochilgan?", "1878-yil 13-iyunda", "1877-yil 24-aprelda", "1885-yilda", "1891-yilda", "1878-yil 13-iyunda.")
t.B("Berlin kongressida Bosniya va Gersegovina kimga in’om etilgan?", "Avstriya-Vengriyaga", "Rossiyaga", "Serbiyaga", "Britaniyaga", "Avstriya-Vengriyaga.")
t.B("Berlin kongressida Rossiyaga Kavkazning qaysi hududlari berilgan?", "Batumi, Kars va Ardagan", "Tiflis va Boku", "Kipr va Krit", "Bosfor va Dardanell", "Batumi, Kars va Ardagan.")
t.B("1875-yilgi shartnomaga ko‘ra Kuril orollarining shimoliy qismi kimga berilgan?", "Yaponiyaga", "Rossiyaga", "Xitoyga", "AQSHga", "Janubiy Saxalinga da’vodan voz kechish evaziga Yaponiyaga.")
t.B("Rossiya va Britaniya O‘rta Osiyodagi ta’sir doiralari haqidagi bitimni qachon tuzgan?", "1873-yilda", "1885-yilda", "1891-yilda", "1907-yilda", "1873-yilda.")
t.B("1885-yilda qaysi shahar egallangan?", "Kushka", "Ashxobod", "Marv", "Hirot", "Kushka.")
t.B("O‘rta Osiyo va Afg‘oniston chegarasining Pomirdan o‘tishi haqidagi shartnoma qachon imzolangan?", "1891-yilda", "1885-yilda", "1873-yilda", "1902-yilda", "1891-yilda.")
t.B("Yaponiya–Britaniya bitimi qachon imzolangan?", "1902-yilda", "1904-yilda", "1905-yilda", "1891-yilda", "1902-yilda.")
t.B("1905-yilda rus floti qayerda yakson qilingan?", "Susima yonida", "Port-Arturda", "Vladivostokda", "Sevastopolda", "Susima yonida.")
t.B("Rossiya–Yaponiya tinchlik shartnomasi qachon imzolangan?", "1905-yil 23-avgustda", "1904-yilda", "1902-yilda", "1907-yilda", "1905-yil 23-avgustda, AQSH vositachiligida.")
t.NAT("Berlin kongressida «Berlin traktati» imzolandi.", "Rossiyaning San-Stefanodagi muvaffaqiyatlari ahamiyati kamaydi", "Rossiya Istanbulni oldi", "Usmonli davlati tugatildi", "Bolgariya to‘liq mustaqil bo‘ldi", "Bolgariya ikkiga bo‘lindi, Kipr Britaniyaga o‘tdi.")
t.NAT("Yaponiya floti urush e’lon qilmay Port-Arturdagi rus flotiga hujum qildi.", "Rossiya mag‘lub bo‘lib, Port-Artur taslim bo‘ldi", "Yaponiya mag‘lub bo‘ldi", "Koreya Rossiyaga o‘tdi", "AQSH Rossiyaga yordam berdi", "Rossiya dengizda va quruqlikda yengildi.")
t.TF("Shartnomaga ko‘ra Rossiya Koreyani Yaponiya ta’sir doirasi deb tan olgan.", True, "To‘g‘ri.")
t.TF("Rus-yapon urushidan keyin Saxalinning janubiy qismi Rossiyada qolgan.", False, "Noto‘g‘ri: u Yaponiyaga berilgan.")
t.MUL([("San-Stefano shartnomasiga ko‘ra Bolgariya amalda mustaqil davlatga aylangan.", True),
       ("Britaniya Rossiyaning muvaffaqiyatlaridan tashvishlanib, harbiy kemalarini Marmar dengiziga kiritgan.", True),
       ("Berlin kongressida Kipr oroli Rossiyaga berilgan.", False)],
      "III noto‘g‘ri: Kipr Buyuk Britaniyaga berilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Xiva vassalga aylantirildi", "Rossiya Usmonli davlatiga urush e’lon qildi", "Berlin kongressi", "Kushka egallandi", "Pomir chegarasi shartnomasi", "Susima jangi"],
      "1873 → 1877 → 1878 → 1885 → 1891 → 1905.")
t.MAPMATCH(FE, ['Port-Artur', 'Susima', 'Saxalin', 'Kuril orollari'],
           ["Yaponiya floti urush e’lon qilmay hujum qilgan rus harbiy-dengiz bazasi", "1905-yilda rus floti yakson qilingan joy", "janubiy qismi Yaponiyaga berilgan orol", "shimoliy qismi 1875-yilda Yaponiyaga berilgan orollar"],
           "1 – Port-Artur; 2 – Susima; 3 – Saxalin; 4 – Kuril orollari.")
t.VENN("San-Stefano shartnomasi", "Berlin traktati",
       [("Bolgariya amalda mustaqil bo‘lgan", 1), ("Usmonli davlati katta tovon to‘lashi belgilangan", 1),
        ("Bolgariya ikkiga bo‘lingan", 2), ("Bosniya va Gersegovina Avstriya-Vengriyaga berilgan", 2),
        ("Chernogoriya, Serbiya, Ruminiya mustaqilligi tan olingan", 3)],
       "San-Stefano — Bolgariya mustaqil; Berlin — Bolgariya bo‘lingan; ikkalasida uch davlat mustaqilligi.")

# 21 Rossiyada Davlat dumasining tashkil etilishi
t = Topic('e9j21', 9121); TOPICS['e9j21'] = t
t.B("Rossiya korxonalarida ish vaqti o‘rtacha qancha bo‘lgan?", "12–14 soat", "8 soat", "10 soat", "16–18 soat", "12–14 soat.")
t.B("«Mehnatni ozod qilish» guruhiga kim rahbarlik qilgan?", "G. V. Plexanov", "V. I. Lenin", "Stolipin", "Nikolay II", "G. V. Plexanov; 1883-yilda tuzilgan.")
t.B("«Ishchilar sinfini ozod qilish uchun kurash ittifoqi» qachon tuzilgan?", "1895-yilda", "1883-yilda", "1898-yilda", "1903-yilda", "1895-yilda Peterburgda.")
t.B("RSDRP qachon tuzilgan?", "1898-yilda", "1895-yilda", "1903-yilda", "1905-yilda", "1898-yilda.")
t.B("1903-yildan RSDRPga kim rahbarlik qilgan?", "V. I. Ulyanov (Lenin)", "G. V. Plexanov", "Stolipin", "Gapon", "V. I. Ulyanov (Lenin) — bolsheviklar oqimi.")
t.B("Birinchi rus inqilobi qachon boshlangan?", "1905-yil 9-yanvarda", "1905-yil 23-avgustda", "1906-yil aprelda", "1907-yil 3-iyunda", "1905-yil 9-yanvarda.")
t.B("9-yanvar kuni Peterburgda qancha ishchi tinch namoyishga chiqqan?", "250 ming", "350 ming", "25 ming", "1 million", "250 ming kishi.")
t.B("9-yanvar voqeasi tarixga qanday nom bilan kirgan?", "«Qonli yakshanba»", "«Qonli juma»", "«Toshotar voqeasi»", "«Potyomkin qo‘zg‘oloni»", "«Qonli yakshanba».")
t.B("1905-yil yozida qaysi bronenosets matroslari qo‘zg‘olon ko‘targan?", "«Potyomkin»", "«Avrora»", "«Varyag»", "«Kutuzov»", "Qora dengiz flotidagi «Potyomkin».")
t.B("1-Davlat dumasi qachon ish boshlagan?", "1906-yil aprelda", "1905-yil dekabrda", "1907-yil yanvarda", "1907-yil 3-iyunda", "1906-yil aprelda.")
t.B("1-Davlat dumasida deputatlarning qancha qismi dehqonlar vakillari edi?", "1/4 qismiga yaqini", "yarmi", "1/10 qismi", "3/4 qismi", "1/4 qismiga yaqini.")
t.B("Nikolay II 2-Davlat dumasini qachon tarqatib yuborgan?", "1907-yil 3-iyunda", "1906-yilda", "1905-yilda", "1911-yilda", "1907-yil 3-iyunda.")
t.B("Yangi saylov qonuniga ko‘ra bir pomeshchikning ovozi necha ishchining ovoziga teng edi?", "543 nafar", "260 nafar", "4 nafar", "100 nafar", "543 ishchi (260 dehqon, 4 yirik burjua).")
t.B("Rossiya parlamentining yuqori palatasi qanday atalgan?", "Davlat Kengashi", "Davlat dumasi", "Senat", "Bundesrat", "Davlat Kengashi.")
t.B("Davlat Kengashi a’zolarining qancha qismini imperator tayinlagan?", "50 foizini", "25 foizini", "hammasini", "10 foizini", "50 foizini.")
t.NAT("Nikolay II tinch namoyishni o‘qqa tutishni buyurdi.", "Moskva, Riga, Varshava, Boku va boshqa shaharlarda ish tashlash va namoyishlar boshlandi", "inqilob to‘xtadi", "ishchilar talablari bajarildi", "imperator taxtdan voz kechdi", "«Qonli yakshanba»ga javoban inqilobiy harakat kengaydi.")
t.NAT("Inqilobiy harakat keng tus olib, hatto harbiy qismlarga ta’sir qildi.", "Nikolay II Manifest e’lon qilib, Davlat dumasini joriy etishga va’da berdi", "inqilob g‘alaba qozondi", "Rossiya respublika bo‘ldi", "Stolipin iste’fo berdi", "Imperator yon berishga majbur bo‘ldi.")
t.TF("«Mehnatni ozod qilish» guruhi hokimiyatni qurolli qo‘zg‘olon yo‘li bilan olishga qarshi edi.", True, "To‘g‘ri.")
t.TF("1907-yilgi saylov qonuni dehqon va ishchilar manfaatini to‘la aks ettirgan.", False, "Noto‘g‘ri: u hukmron tabaqa manfaatini aks ettirgan.")
t.MUL([("Bolsheviklar barcha mulk davlatniki bo‘ladigan jamiyat qurmoqchi edi.", True),
       ("Ishchilarga kasaba uyushmalariga birlashish huquqi berilgan.", True),
       ("1-Davlat dumasini Nikolay II mamnuniyat bilan qo‘llab-quvvatlagan.", False)],
      "III noto‘g‘ri: Duma «yuvosh» chiqmagani uchun u uni tarqatib yuborgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["«Mehnatni ozod qilish» guruhi", "Kurash ittifoqi tuzildi", "RSDRP tuzildi", "Lenin RSDRPga rahbar bo‘ldi", "«Qonli yakshanba»", "1-Davlat dumasi ish boshladi", "Yangi saylov qonuni"],
      "1883 → 1895 → 1898 → 1903 → 1905 → 1906 → 1907.")
t.MAPN(EU, ['Moskva', 'Riga', 'Peterburg', 'Varshava'], "1905-yil 9-yanvarda 250 ming ishchining tinch namoyishi o‘qqa tutilgan shahar qaysi raqam bilan belgilangan?",
       "3 – Peterburg; Moskva, Riga, Varshava ishchilari javoban ish tashlagan.", ask_idx=2)
t.VENN("1-Davlat dumasi", "2-Davlat dumasi",
       [("1906-yil aprelda ish boshlagan", 1), ("deputatlarning 1/4 qismi dehqonlar", 1),
        ("1907-yil yanvarida saylangan", 2), ("3-iyunda tarqatib yuborilgan", 2),
        ("asosiy masala agrar masala bo‘lgan", 3)],
       "1-Duma — 1906; 2-Duma — 1907, 3-iyunda tarqatilgan; ikkalasida agrar masala.")
