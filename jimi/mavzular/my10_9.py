from qlib import Topic, PLACES, REG
TOPICS = {}
W = 'globe'; EA = 'eastasia'

# 24 Osiyo, Afrika va Lotin Amerikasi
t = Topic('y10j24', 10024); TOPICS['y10j24'] = t
t.B("Malayyada milliy-ozodlik harakatini qaysi davlat bostirgan?", "Buyuk Britaniya", "Fransiya", "Portugaliya", "Gollandiya", "Buyuk Britaniya Malayyada.")
t.B("Fransiya qayerlarda milliy-ozodlik harakatlarini shafqatsizlarcha bostirgan?", "Hindixitoy va Jazoirda", "Angola va Mozambikda", "Malayya va Hindistonda", "Koreya va Filippinda", "Fransiya Hindixitoy va Jazoirda.")
t.B("Portugaliya qaysi mamlakatlarda ozodlik harakatlarini bostirgan?", "Angola va Mozambikda", "Jazoir va Tunisda", "Malayya va Birmada", "Vyetnam va Laosda", "Angola va Mozambikda.")
t.B("Qaysi yil tarixga «Afrika yili» sifatida kirgan?", "1960-yil", "1975-yil", "1947-yil", "1949-yil", "1960-yil.")
t.B("«Afrika yili»da nechta mustamlaka mustaqilligini e’lon qilgan?", "17 ta", "10 ta", "27 ta", "7 ta", "17 ta mustamlaka mamlakat.")
t.B("Tarixdagi oxirgi mustamlakachi imperiya qaysi?", "Portugaliya", "Buyuk Britaniya", "Fransiya", "Ispaniya", "Portugaliya 1975-yili quladi.")
t.B("Hindiston qachon diniy belgi asosida ikki davlatga ajralgan?", "1947-yilda", "1949-yilda", "1960-yilda", "1975-yilda", "1947-yili Hindiston Ittifoqi va Pokistonga.")
t.B("Yaqin Sharqda doimiy tanglik o‘chog‘ini nima vujudga keltirgan?", "1947-yilda Falastinning arab va yahudiy davlatlariga bo‘linishi", "Eron inqilobi", "Hindistonning bo‘linishi", "XXRning tuzilishi", "1947-yilda Falastinning bo‘linishi.")
t.B("Xitoy Xalq Respublikasi qachon e’lon qilingan?", "1949-yil 1-oktyabrda", "1947-yilda", "1931-yilda", "1960-yilda", "1949-yil 1-oktyabrda.")
t.B("1950-yillarda Lotin Amerikasidagi demokratik hukumatlar nimaga qarshi kurashgan?", "chet el, avvalo AQSH kapitali ta’siriga", "SSSR ta’siriga", "Ispaniya monarxiyasiga", "Britaniya mustamlakachiligiga", "Chet el, avvalo AQSH kapitali ta’sirini kamaytirish uchun.")
t.B("1960–1970-yillarda Lotin Amerikasining ko‘pchilik mamlakatlarida kim hokimiyatga kelgan?", "harbiy xuntalar", "kommunistlar", "monarxlar", "din peshvolari", "Davlat to‘ntarishlari orqali harbiy xuntalar.")
t.B("Ba’zi mamlakatlarda ishga yaroqli aholining qancha qismi qishloq xo‘jaligida band edi?", "90% gacha", "10% gacha", "50% gacha", "30% gacha", "Ba’zi mamlakatlarda 90% gacha.")
t.B("1979-yilda qaysi mamlakatda an’anaviy islom qadriyatlariga qaytish shiori ostida harakat boshlangan?", "Eronda", "Turkiyada", "Misrda", "Pokistonda", "Eronda.")
t.B("Eron inqilobi natijasida qaysi shoh chet elga qochgan?", "Muhammad Rizo Pahlaviy", "Muzaffariddin", "Rizo Pahlaviy", "Abdulhamid II", "Shoh Muhammad Rizo Pahlaviy.")
t.B("Bitta shaxs (guruh) hokimiyatining almashmasligiga asoslangan nodemokratik rejim nima deb ataladi?", "avtoritarizm", "liberalizm", "parlamentarizm", "federalizm", "Avtoritarizm.")
t.B("Avtoritar rejim sharoitida o‘rtacha rivojlanish darajasiga yetgan mamlakatlar qaysilar?", "Braziliya, Argentina, Chili", "Angola, Mozambik, Jazoir", "Eron, Afg‘oniston, Iroq", "Vyetnam, Koreya, Filippin", "Braziliya, Argentina, Chili.")
t.B("Davlat to‘ntarishi orqali hokimiyatga kelgan harbiylar hokimiyati nima deb ataladi?", "harbiy xunta", "imperiya", "koalitsiya", "parlament", "Harbiy xunta.")
t.B("«Modernizatsiya» so‘zi fransuz tilida qanday ma’noni anglatadi?", "«eng yangi», «zamonaviy»", "«birlashish»", "«egallash»", "«ijtimoiy»", "Fransuzcha moderne – «eng yangi», «zamonaviy».")
t.NAT("1947-yilda Hindiston diniy belgi asosida ikki davlatga ajraldi.", "millionlab kishilar qochoqqa aylandi, ikki davlat o‘rtasida bir necha marta harbiy mojarolar bo‘ldi", "Hindiston va Pokiston birlashdi", "Hindiston Britaniyaga qaytdi", "mojarolar butunlay to‘xtadi", "Millionlab qochoqlar, bir necha mojarolar.")
t.NAT("Eronda modernizatsiya diniy omilni inobatga olmasdan amalga oshirildi.", "1979-yilgi harakat butun mamlakatni qamrab olib, hokimiyat din peshvolari qo‘liga o‘tdi", "Eron dunyoviy respublika bo‘ldi", "shoh hokimiyati mustahkamlandi", "Eron G‘arbga yaqinlashdi", "Shoh qochdi, hokimiyat din peshvolariga o‘tdi.")
t.TF("Aksariyat musulmon mamlakatlarida diniy urf-odatlarni hisobga olgan modernizatsiya katta qarshiliksiz qabul qilingan.", True, "To‘g‘ri.")
t.TF("Mustamlakalarning ozod bo‘lish jarayoni barcha mamlakatlarda tinch yo‘l bilan amalga oshgan.", False, "Noto‘g‘ri: barcha mamlakatlarda tinch yo‘l bilan amalga oshmagan.")
t.MUL([("Ko‘plab yangi davlatlarning chegaralari etnik va diniy chegaralarga mos tushmagan.", True),
       ("Filippin, Koreya, Vyetnam mustaqillikning dastlabki davrlarida urushlarni boshdan kechirgan.", True),
       ("Osiyo va Afrikadagi aksariyat avtoritar rejimlar iqtisodiy gullab-yashnashga olib kelgan.", False)],
      "III noto‘g‘ri: ular jamiyat inqirozi, iqtisodiy tanazzul va ko‘plab odamlar o‘limiga olib kelgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Hindiston va Pokiston vujudga keldi", "XXR tashkil topdi", "«Afrika yili»", "Portugaliya mustamlaka imperiyasi quladi", "Eronda islom inqilobi"],
      "1947 → 1949 → 1960 → 1975 → 1979.")
t.VENN("Lotin Amerikasi", "Islom mamlakatlari",
       [("1960–1970-yillarda harbiy xuntalar", 1), ("Braziliya, Argentina, Chili o‘rtacha rivojlanish darajasiga yetgan", 1),
        ("ozodlik harakatlari islom bayrog‘i ostida bo‘lgan", 2), ("Eronda hokimiyat din peshvolariga o‘tgan", 2),
        ("modernizatsiya yo‘lini tanlash muammosi", 3)],
       "Lotin Amerikasi – xuntalar, Braziliya; islom mamlakatlari – islom bayrog‘i, Eron; ikkalasida modernizatsiya muammosi.")
t.MAPMATCH(W, ['Angola', 'Jazoir', 'Malayziya', 'Eron'],
           ["Portugaliya ozodlik harakatini bostirgan mamlakat (Mozambik bilan)", "Fransiya ozodlik harakatini bostirgan mamlakat (Hindixitoy bilan)", "Buyuk Britaniya ozodlik harakatini bostirgan hudud (Malayya)", "1979-yilda islom qadriyatlariga qaytish harakati bo‘lgan mamlakat"],
           "1 – Angola; 2 – Jazoir; 3 – Malayya; 4 – Eron.")

# 25 Yaponiya, Xitoy va Janubiy Koreya
t = Topic('y10j25', 10025); TOPICS['y10j25'] = t
t.B("Urushdan keyin Yaponiyadagi AQSH okkupatsion qo‘shinlariga kim boshchilik qilgan?", "general Duglas Makartur", "Duayt Eyzenhauer", "Jon Kennedi", "Den Syaopin", "General Duglas Makartur.")
t.B("Makartur direktivasi bilan Yaponiyada qanday islohot o‘tkazilgan?", "agrar islohot", "harbiy islohot", "diniy islohot", "valyuta islohoti", "Agrar islohot: yer unda ishlaydiganlarga berildi.")
t.B("Yaponiyada bozor iqtisodiyoti infratuzilmasi qachon shakllangan?", "1950-yillar o‘rtalarida", "1945-yilda", "1970-yillarda", "1980-yillarda", "1950-yillar o‘rtalariga kelib.")
t.B("«Yapon iqtisodiy mo‘jizasi» davrida sanoat o‘sishi asosan qaysi sohalar evaziga yuz bergan?", "og‘ir sanoat va kimyo", "qishloq xo‘jaligi", "turizm", "to‘qimachilik", "Og‘ir sanoat va kimyo ishlab chiqarishi evaziga.")
t.B("1960-yillar oxirida Yaponiya YaIM hajmi bo‘yicha dunyoda nechanchi o‘ringa chiqqan?", "AQSHdan keyin ikkinchi", "birinchi", "uchinchi", "beshinchi", "AQSHdan keyin ikkinchi o‘ringa.")
t.B("1980-yillardan Yaponiyada nechta texnopolis tashkil qilingan?", "26 ta", "4 ta", "12 ta", "50 ta", "26 ta texnopolis.")
t.B("Yangi iqtisodiy tizimda savdo, xizmat, moliya, fan kabi sohalar qanday atalgan?", "uchinchi sektor", "birinchi sektor", "og‘ir sanoat", "agrar sektor", "Uchinchi sektor.")
t.B("XKP va Gomindan o‘rtasida fuqarolar urushi qachon qaytadan boshlangan?", "1946-yil iyunda", "1945-yil avgustda", "1949-yil sentabrda", "1950-yilda", "1946-yil iyunda.")
t.B("XXR e’lon qilingach Gomindan ma’muriyati qayerga ko‘chib o‘tgan?", "Tayvan oroliga", "Gonkongga", "Yaponiyaga", "Koreyaga", "Tayvan oroliga.")
t.B("XXR raisi lavozimini kim egallagan?", "Mao Szedun", "Den Syaopin", "Sun Yatsen", "Chan Kayshi", "Mao Szedun.")
t.B("Xitoy va SSSR o‘rtasida munosabatlar qachondan buzilgan?", "1956-yildan", "1950-yildan", "1966-yildan", "1976-yildan", "1956-yildan.")
t.B("Muddatidan oldin sotsializm qurishni nazarda tutgan 1958-yilgi siyosat qanday atalgan?", "«Katta sakrash»", "«Madaniy inqilob»", "«To‘rtta modernizatsiya»", "«Yangi kurs»", "«Katta sakrash».")
t.B("«Katta sakrash» davridagi shior qaysi?", "«Uch yil matonatli mehnat – uch ming yil baxt-saodat»", "«Boyinglar!»", "«Yangi marralar»", "«Yer – dehqonlarga»", "«Uch yil matonatli mehnat – uch ming yil baxt-saodat».")
t.B("Xitoyda «Madaniy inqilob» qachon boshlangan?", "1966-yilda", "1958-yilda", "1976-yilda", "1949-yilda", "1966-yili.")
t.B("Mao Szedun qachon vafot etgan?", "1976-yil 9-sentabrda", "1966-yilda", "1949-yil 1-oktyabrda", "1980-yilda", "1976-yil 9-sentabrda; «Madaniy inqilob» rasman yakunlandi.")
t.B("«To‘rtta modernizatsiya» konsepsiyasini kim ishlab chiqqan?", "Den Syaopin", "Mao Szedun", "Duglas Makartur", "Chan Kayshi", "Den Syaopin.")
t.B("Chet el kapitalini jalb qilish uchun Xitoy janubida nechta erkin iqtisodiy zona tashkil etilgan?", "4 ta", "26 ta", "12 ta", "2 ta", "4 ta erkin iqtisodiy zona.")
t.B("Koreya urushi tugagach chegara qaysi parallel bo‘ylab o‘tkazilgan?", "38-parallel", "17-parallel", "40-parallel", "49-parallel", "1953-yilda 38-parallel bo‘ylab.")
t.B("Janubiy Koreya po‘lat quyish bo‘yicha Osiyoda nechanchi o‘ringa chiqqan?", "Yaponiyadan keyin ikkinchi", "birinchi", "uchinchi", "Xitoydan keyin ikkinchi", "Yaponiyadan keyingi ikkinchi o‘ringa.")
t.B("Yuqori organlar bergan, bajarilishi majburiy rasmiy ko‘rsatma nima deb ataladi?", "direktiva", "dekret", "konsepsiya", "referendum", "Direktiva.")
t.NAT("1966-yilda Xitoyda «Madaniy inqilob» boshlandi.", "ziyolilarga qarshi qatag‘onlar avj oldi, ko‘plab madaniyat yodgorliklari yo‘q qilindi", "Xitoyda demokratiya o‘rnatildi", "SSSR bilan munosabatlar yaxshilandi", "Xitoyga investitsiyalar oqib keldi", "Madaniyat va ta’limga juda katta zarar yetdi, antisovetizm kuchaydi.")
t.NAT("1945-yil avgustda Yaponiyaning Koreyadagi qo‘shinlari taslim bo‘ldi.", "SSSR va AQSH Koreyani vaqtincha ikkiga bo‘lib oldi", "Koreya yagona mustaqil davlat bo‘ldi", "Koreya Xitoyga qo‘shildi", "Koreya Yaponiyada qoldi", "Janubiga AQSH, shimoliga SSSR qo‘shin kiritdi.")
t.TF("«Katta sakrash» siyosati muvaffaqiyatsiz yakunlangan.", True, "To‘g‘ri: rejalar asosan qog‘ozda qolib ketdi.")
t.TF("Koreya urushida Xitoy Janubiy Koreyaga yordam bergan.", False, "Noto‘g‘ri: AQSH Janubga, Xitoy KXDRga yordam bergan.")
t.MUL([("Yaponiya jahon bozoriga mikroprotsessorlar va sanoat robotlari bilan chiqqan.", True),
       ("1980-yillar oxiriga kelib Koreya Respublikasi dunyoning eng rivojlangan mamlakatlaridan biri bo‘lgan.", True),
       ("Den Syaopin islohotlarida chet el investitsiyalari taqiqlangan.", False)],
      "III noto‘g‘ri: chet el investitsiyalari oqib kela boshladi, erkin iqtisodiy zonalar tuzildi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Xitoyda fuqarolar urushi qayta boshlandi", "Koreya Respublikasi tashkil topdi", "XXR e’lon qilindi", "Koreya urushi tugadi", "«Katta sakrash» rejasi qabul qilindi", "«Madaniy inqilob» boshlandi", "Mao Szedun vafot etdi"],
      "1946 → 1948 → 1949 → 1953 → 1958 → 1966 → 1976.")
t.VENN("«Katta sakrash»", "«Madaniy inqilob»",
       [("1958-yilgi reja", 1), ("12 soatlik ish kuni", 1),
        ("ziyolilarga qarshi qatag‘onlar", 2), ("antisovetizm kuchaygan", 2),
        ("Mao Szedun davridagi siyosat", 3)],
       "Katta sakrash – 1958, 12 soat; Madaniy inqilob – qatag‘on, antisovetizm; ikkalasi Mao davri.")
t.MAPMATCH(EA, ['Tayvan', 'Yaponiya', 'Janubiy Koreya', 'Pekin'],
           ["1949-yilda Gomindan ma’muriyati ko‘chib o‘tgan orol", "1980-yillardan 26 ta texnopolis tashkil qilingan mamlakat", "po‘lat quyish bo‘yicha Osiyoda ikkinchi o‘ringa chiqqan respublika", "XXR poytaxti"],
           "1 – Tayvan; 2 – Yaponiya; 3 – Janubiy Koreya; 4 – Pekin.")
