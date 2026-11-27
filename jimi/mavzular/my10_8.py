from qlib import Topic, PLACES, REG
TOPICS = {}
EU = 'europe'

# 21 Janubiy va Shimoliy Yevropa
t = Topic('y10j21', 10021); TOPICS['y10j21'] = t
t.B("XX asr boshiga kelib Ispaniya, Portugaliya va Gretsiya qanday hududlarga aylangan?", "«Yevropaning chekka hududlari»ga", "Yevropa sanoat markazlariga", "mustamlakachi imperiyalarga", "moliya markazlariga", "«Yevropaning chekka hududlari»ga aylandi.")
t.B("Ikkinchi jahon urushidan so‘ng Franko rejimi Ispaniyada yana qancha hokimiyatda turgan?", "o‘ttiz yil", "o‘n yil", "qirq yil", "besh yil", "Yana o‘ttiz yil hokimiyatda turdi.")
t.B("Franko hukumatini fashistik davlatlar yordamida hokimiyatga kelgani uchun qaysi konferensiya qoralagan?", "Potsdam konferensiyasi", "Yalta konferensiyasi", "Tehron konferensiyasi", "Vashington konferensiyasi", "Potsdam konferensiyasi.")
t.B("BMT Bosh Assambleyasi Ispaniyani xalqaro tashkilotlarga qabul qilmaslik haqida qachon qaror qabul qilgan?", "1946-yilda", "1945-yilda", "1955-yilda", "1975-yilda", "1946-yili.")
t.B("Ispaniyaning tashqi siyosiy ahvoli qachon yaxshi tomonga o‘zgargan?", "sovuq urush boshlanishi bilan", "Franko vafotidan so‘ng", "1982-yilda", "Ikkinchi jahon urushi davrida", "Faqat sovuq urush boshlanishi bilan.")
t.B("Franko qachon vafot etgan?", "1975-yilda", "1968-yilda", "1974-yilda", "1982-yilda", "1975-yili.")
t.B("1975-yili Ispaniya taxtiga kim o‘tirgan?", "Xuan Karlos I", "Antonio Salazar", "Marselu Kaetanu", "Konstantinos Saldaris", "Qirol Xuan Karlos I.")
t.B("Ispaniya NATOga qachon a’zo bo‘lgan?", "1982-yil mayda", "1985-yilda", "1975-yilda", "1949-yilda", "1982-yil mayda; 1985-yili YIHga.")
t.B("Portugaliyadagi Salazar rejimi rasman qanday atalgan?", "«yangi davlat»", "«ijtimoiy davlat»", "«ochiq iqtisod»", "«qora polkovniklar»", "«Yangi davlat».")
t.B("Yevropa yangi tarixida eng uzoq hokimiyatda o‘tirgan diktator kim?", "Antonio Salazar", "Franko", "Mussolini", "Saldaris", "Portugaliyani sal kam qirq yil boshqargan Salazar.")
t.B("Boshqa mamlakatlar bilan aloqalardan uzilgan biqiq xo‘jalik yuritish siyosati nima deb ataladi?", "avtarkiya", "integratsiya", "natsionalizatsiya", "konsentratsiya", "Avtarkiya.")
t.B("A. Salazar qachon vafot etgan?", "1968-yilda", "1974-yilda", "1975-yilda", "1976-yilda", "1968-yili.")
t.B("Salazardan keyin bosh vazir bo‘lgan kim?", "Marselu Kaetanu", "Antonio de Spinola", "Mariu Suaresh", "Xuan Karlos I", "Marselu Kaetanu.")
t.B("Kaetanu «yangi davlat» nomini qanday nomga almashtirgan?", "«ijtimoiy davlat»", "«xalq davlati»", "«korporativ davlat»", "«demokratik davlat»", "«Ijtimoiy davlat».")
t.B("Portugaliya armiyasida rejimga qarshi tuzilgan tashkilot qanday atalgan?", "«Kapitanlar harakati»", "«Qora polkovniklar»", "«Milliy qutqaruv kengashi»", "Gretsiya demokratik armiyasi", "«Kapitanlar harakati».")
t.B("1974-yilda Milliy qutqaruv kengashiga kim boshchilik qilgan?", "general Antonio de Spinola", "Marselu Kaetanu", "Mariu Suaresh", "Franko", "General Antonio de Spinola.")
t.B("1986-yili Portugaliya prezidenti etib saylangan birinchi fuqaroviy arbob kim?", "Mariu Suaresh", "Antonio de Spinola", "Marselu Kaetanu", "Xuan Karlos I", "Sobiq bosh vazir Mariu Suaresh.")
t.B("1967-yil mayda Gretsiyada o‘rnatilgan rejim qanday nom olgan?", "«qora polkovniklar» diktaturasi", "«yangi davlat»", "Franko rejimi", "«Kapitanlar harakati»", "«Qora polkovniklar» diktaturasi.")
t.B("Gretsiya YIHning teng huquqli a’zosiga qachon aylangan?", "1981-yilda", "1985-yilda", "1986-yilda", "1974-yilda", "1981-yili.")
t.NAT("1974-yili Gretsiya harbiylari Kiprda to‘ntarish qildi, Turkiya orolga qo‘shin kiritdi.", "«qora polkovniklar» xuntasi hokimiyatdan ketishga majbur bo‘ldi", "Kipr Gretsiyaga qo‘shildi", "xunta kuchaydi", "Gretsiya Turkiyaga urush e’lon qildi", "Inqiroz oqibatida xunta ketdi, konstitutsiya tiklandi.")
t.NAT("1974-yili ofitserlar Kaetanu hukumatini deyarli qonsiz ag‘dardi.", "Afrikadagi mustamlakalarga mustaqillik berildi, ko‘p korxonalar natsionalizatsiya qilindi", "Salazar hokimiyatga qaytdi", "Portugaliya monarxiyaga aylandi", "mustamlaka urushlari kuchaydi", "Diktaturadan keyingi o‘tish davri boshlandi.")
t.TF("1946-yilgi parlament saylovlari Gretsiyada fuqarolar urushining boshlanishiga olib kelgan.", True, "To‘g‘ri.")
t.TF("G‘arb «Marshall rejasi» bo‘yicha Ispaniyaga katta yordam ko‘rsatgan.", False, "Noto‘g‘ri: G‘arb yordam ko‘rsatishdan bosh tortgan.")
t.MUL([("Gretsiya fuqarolar urushida GDA SSSR yordamiga, hukumat esa AQSHga tayangan.", True),
       ("«Qora polkovniklar» islohotlari natijasida Gretsiya industrial-agrar mamlakatga aylangan.", True),
       ("1986-yilda Portugaliya NATOga, 1982-yilda YIHga a’zo bo‘lgan.", False)],
      "III noto‘g‘ri: 1986-yilda Portugaliya YIHga a’zo bo‘lgan; 1982-yilda NATOga Ispaniya kirgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["BMT Ispaniya haqida maxsus qaror qabul qildi", "Gretsiyada harbiylar hokimiyatni egalladi", "Salazar vafot etdi", "Portugaliyada Kaetanu hukumati ag‘darildi", "Franko vafot etdi", "Gretsiya YIH a’zosi bo‘ldi"],
      "1946 → 1967 → 1968 → 1974 → 1975 → 1981.")
t.MATCH("Shaxslarni mamlakati bilan moslashtiring.", ["Franko", "Antonio Salazar", "Konstantinos Saldaris", "Xuan Karlos I"],
        ["Ispaniya diktatori", "Portugaliyadagi «yangi davlat» rahbari", "Gretsiyada monarxiyani tiklashga kirishgan", "1975-yilda taxtga o‘tirgan Ispaniya qiroli", "Portugaliya prezidenti Suaresh"], 'abcd',
        "Franko – Ispaniya; Salazar – Portugaliya; Saldaris – Gretsiya; Xuan Karlos I – Ispaniya qiroli.")
t.VENN("Ispaniya", "Portugaliya",
       [("Franko rejimi", 1), ("qirol Xuan Karlos I", 1),
        ("Salazar rejimi", 2), ("«Kapitanlar harakati»", 2),
        ("diktaturadan demokratiyaga o‘tgan", 3)],
       "Ispaniya – Franko, Xuan Karlos; Portugaliya – Salazar, kapitanlar; ikkalasi demokratiyaga o‘tgan.")
t.MAPMATCH(EU, ['Ispaniya', 'Portugaliya', 'Gretsiya', 'Kipr'],
           ["Franko rejimi hukm surgan davlat", "Salazar «yangi davlat»i joylashgan mamlakat", "1967-yilda «qora polkovniklar» hokimiyatni egallagan davlat", "1974-yilda harbiy to‘ntarish bo‘lgan, Turkiya qo‘shin kiritgan orol"],
           "1 – Ispaniya; 2 – Portugaliya; 3 – Gretsiya; 4 – Kipr.")

# 22 Sovet Ittifoqida islohotlar va inqiroz
t = Topic('y10j22', 10022); TOPICS['y10j22'] = t
t.B("Ikkinchi jahon urushida qancha sovet fuqarosi halok bo‘lgan?", "26,5 mln", "6,5 mln", "65 mln", "3 mln", "26,5 mln sovet fuqarosi halok bo‘ldi.")
t.B("1946-yilgi qurg‘oqchilik va ocharchilikda qancha kishi vafot etgan?", "bir million", "26,5 mln", "100 ming", "7 mln", "Bir million kishi ochlikdan vafot etdi.")
t.B("SSSRda sanoat ishlab chiqarishi qachon urushdan oldingi darajaga yetgan?", "1948-yilda", "1946-yilda", "1953-yilda", "1950-yilda", "1948-yilga kelib.")
t.B("Urushdan keyin SSSR sanoatida uskunalar xarajatining yarmini nima ta’minlagan?", "Germaniya to‘lagan reparatsiya", "«Marshall rejasi»", "AQSH krediti", "neft eksporti", "Germaniya to‘lagan reparatsiya.")
t.B("I. Stalin qachon vafot etgan?", "1953-yil 5-martda", "1956-yil fevralda", "1964-yil oktyabrda", "1949-yilda", "1953-yil 5-mart kuni.")
t.B("1953-yilgi yangi iqtisodiy dastur qaysi soha ustuvorligini birinchi marta belgilagan?", "yengil sanoat", "og‘ir sanoat", "harbiy sanoat", "kosmik sanoat", "Yengil sanoatning xalq iste’moli mollari ishlab chiqarishdagi ustuvorligi.")
t.B("XX syezddagi Xrushchyov nutqining mavzusi qanday edi?", "«Shaxsga sig‘inish va uning oqibatlari to‘g‘risida»", "«Qayta qurish va partiyaning kadrlar siyosati»", "«Rivojlangan sotsializm»", "«Yangi marralar»", "«Shaxsga sig‘inish va uning oqibatlari to‘g‘risida».")
t.B("Yuriy Gagarin qachon koinotga parvoz qilgan?", "1961-yil 12-aprelda", "1957-yilda", "1963-yilda", "1956-yil fevralda", "1961-yil 12-aprelda.")
t.B("SSSR qachondan chetdan g‘alla sotib olishni boshlagan?", "1963-yildan", "1953-yildan", "1946-yildan", "1977-yildan", "1963-yildan.")
t.B("1964-yil oktyabrda KPSS MK Birinchi sekretari etib kim tayinlangan?", "Leonid Brejnev", "Aleksey Kosigin", "Yuriy Andropov", "Mixail Gorbachyov", "Leonid Brejnev; Ministrlar Soveti Raisi – Aleksey Kosigin.")
t.B("«Rivojlangan sotsializm» konstitutsiyasi qachon qabul qilingan?", "1977-yilda", "1937-yilda", "1964-yilda", "1985-yilda", "1977-yili.")
t.B("L. Brejnev qachon vafot etgan?", "1982-yilda", "1984-yilda", "1985-yilda", "1977-yilda", "1982-yili.")
t.B("Brejnevdan keyin Bosh kotib etib kim saylangan?", "Yuriy Andropov", "Konstantin Chernenko", "Mixail Gorbachyov", "Aleksey Kosigin", "Yuriy Andropov.")
t.B("Saylanishi «tugab borayotgan SSSRning ramzi» bo‘lgan rahbar kim?", "Konstantin Chernenko", "Yuriy Andropov", "Nikita Xrushchyov", "Leonid Brejnev", "Keksa va kasalmand Konstantin Chernenko.")
t.B("Mixail Gorbachyov qachon Bosh kotib etib saylangan?", "1985-yil martda", "1984-yil fevralda", "1987-yil yanvarda", "1991-yil avgustda", "1985-yil 10-martdan bir kun so‘ng.")
t.B("1987-yil yanvar plenumida Gorbachyov qanday kursni e’lon qilgan?", "oshkoralik kursini", "«harbiy kommunizm»ni", "YISni", "kollektivlashtirishni", "Demokratizatsiyalash va oshkoralik kursini.")
t.B("O‘zini KPSSga muxolifatdagi partiya deb e’lon qilgan tashkilot qaysi?", "Demokratik ittifoq", "xalq frontlari", "GKCHP", "Gomindan", "Demokratik ittifoq.")
t.B("Xalq frontlari dastlab qayerda paydo bo‘lgan?", "Boltiqbo‘yi respublikalarida", "O‘rta Osiyoda", "Kavkazortida", "Moskvada", "Dastlab Boltiqbo‘yi respublikalarida.")
t.B("GKCHP qachon tuzilganligi e’lon qilingan?", "1991-yil 19-avgustga o‘tar kechasi", "1991-yil 8-dekabrda", "1987-yil yanvarda", "1985-yil aprelda", "1991-yil 19-avgustga o‘tar kechasi.")
t.B("MDH qayerda tuzilganligi e’lon qilingan?", "Minsk shahrida", "Moskvada", "Kiyevda", "Almatida", "8-dekabr kuni Minsk shahrida.")
t.B("Markazlashgan tizimdan markazlashmagan tizimga o‘tish nima deb ataladi?", "desentralizatsiyalash", "demokratizatsiyalash", "natsionalizatsiya", "integratsiya", "Desentralizatsiyalash.")
t.NAT("1960-yillar boshida oziq-ovqat tanqisligi, namoyishlar shafqatsiz bostirildi.", "1964-yil oktyabr plenumi Xrushchyovni barcha lavozimlaridan ozod qildi", "Xrushchyov mavqei mustahkamlandi", "SSSR g‘alla eksport qila boshladi", "Stalin rejimi tiklandi", "Xrushchyovning mavqei tushdi va u ozod qilindi.")
t.NAT("1991-yil avgustdagi GKCHP harakati muvaffaqiyatsiz tugadi.", "KPSS faoliyati to‘xtatildi, ko‘p respublikalar Ittifoq shartnomasini imzolashdan bosh tortdi", "SSSR mustahkamlandi", "Gorbachyov obro‘si keskin oshdi", "1977-yilgi konstitutsiya kuchaydi", "GKCHP a’zolari qamaldi, KPSS faoliyati to‘xtatildi.")
t.TF("1977-yilgi konstitutsiya KPSSning siyosiy tizimdagi yakkahukmronligini mustahkamlagan.", True, "To‘g‘ri: bunday modda 1937-yilgi konstitutsiyada ham yo‘q edi.")
t.TF("1948–1952-yillarda SSSR iqtisodiyotni «Marshall rejasi» yordamida tiklagan.", False, "Noto‘g‘ri: SSSR to‘liq ichki resurslar hisobiga tikladi.")
t.MUL([("1985-yil maydan ichkilikbozlikka qarshi keng kampaniya boshlangan.", True),
       ("MDHni Rossiya, Ukraina va Belarus rahbarlari tuzgan.", True),
       ("Y. Andropov boshqaruvda liberal, demokratik usullardan foydalangan.", False)],
      "III noto‘g‘ri: u qattiqqo‘llik, avtoritar, buyruqbozlik usullaridan foydalangan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Stalin vafot etdi", "KPSS XX syezdi", "Gagarin koinotga parvoz qildi", "Xrushchyov lavozimlaridan ozod qilindi", "Yangi konstitutsiya qabul qilindi", "Gorbachyov Bosh kotib bo‘ldi", "MDH tuzildi"],
      "1953 → 1956 → 1961 → 1964 → 1977 → 1985 → 1991.")
t.MATCH("Rahbarlarni ularga oid ma’lumot bilan moslashtiring.", ["Nikita Xrushchyov", "Leonid Brejnev", "Yuriy Andropov", "Mixail Gorbachyov"],
        ["XX syezdda shaxsga sig‘inishni qoralagan", "1977-yilgi konstitutsiya davri rahbari", "illatlarga qarshi qattiqqo‘l usullar bilan kurashgan", "qayta qurish va oshkoralikni e’lon qilgan", "keksa va kasalmand, 1984-yilda saylangan"], 'abcd',
        "Xrushchyov – XX syezd; Brejnev – 1977; Andropov – qattiqqo‘l kurash; Gorbachyov – qayta qurish.")
t.VENN("Xrushchyov davri", "Brejnev davri",
       [("«iliqlik» davri", 1), ("Gagarinning parvozi", 1),
        ("«rivojlangan sotsializm» konstitutsiyasi", 2), ("shaxsga sig‘inish tanqidini to‘xtatish", 2),
        ("KPSS rahbarligi", 3)],
       "Xrushchyov – iliqlik, Gagarin; Brejnev – 1977, tanqidni to‘xtatish; ikkalasi KPSS rahbari.")
t.MAPMATCH(EU, ['Moskva', 'Minsk', 'Ukraina', 'Litva'],
           ["1991-yil avgustda GKCHP qo‘shin kiritgan shahar", "1991-yil 8-dekabrda MDH tuzilganligi e’lon qilingan shahar", "Rossiya va Belarus bilan MDHni tuzgan respublika", "xalq frontlari dastlab paydo bo‘lgan Boltiqbo‘yi respublikalaridan biri"],
           "1 – Moskva; 2 – Minsk; 3 – Ukraina; 4 – Litva.")

# 23 Markaziy va Sharqiy Yevropa
t = Topic('y10j23', 10023); TOPICS['y10j23'] = t
t.B("Urushdan keyin MSHY mamlakatlarida kuchlar o‘rtasidagi kurashning hal qiluvchi yillari qaysilar?", "1947–1948-yillar", "1945–1946-yillar", "1956–1957-yillar", "1989–1990-yillar", "1947–1948-yillar.")
t.B("Polshada faoliyat yuritgan sobiq Krayova armiyasi qanday ma’noni anglatadi?", "Vatan armiyasi", "Qizil armiya", "Xalq armiyasi", "Ozodlik armiyasi", "Krayova armiyasi (Vatan armiyasi).")
t.B("Chexoslovakiyada tub burilish qachon yuz bergan?", "1948-yil fevralda", "1949-yil oktyabrda", "1956-yilda", "1945-yil mayda", "1948-yil fevralda.")
t.B("Chexoslovakiya hukumatini boshqargan kommunistik partiya vakili kim?", "Klement Gotvald", "Imre Nad", "Aleksandr Dubchek", "Sali Berisha", "Klement Gotvald; 1948-yil iyunda prezident etib saylandi.")
t.B("1949-yilga kelib qaysi davlatda kommunistlar to‘liq hokimiyatni egallagan?", "Bolgariya", "Gretsiya", "Avstriya", "Finlandiya", "Albaniya, Bolgariya, Vengriya, Polsha, Ruminiya, Chexoslovakiya, Yugoslaviya.")
t.B("Qaysi mamlakatlar hududida sovet qo‘shinlari joylashmagan?", "Albaniya va Yugoslaviya", "Polsha va Vengriya", "Ruminiya va Bolgariya", "GDR va Chexoslovakiya", "Albaniya va Yugoslaviyadan tashqari barchasida sovet qo‘shinlari bor edi.")
t.B("1940-yillar oxirida MSHYda o‘rnatilgan tuzum dastlab qanday atalgan?", "«xalq-demokratik»", "«liberal-demokratik»", "«yangi davlat»", "«ijtimoiy davlat»", "Dastlab «xalq-demokratik», keyin «sotsialistik».")
t.B("1956-yili Vengriyada yangi hukumatga kim boshchilik qilgan?", "Imre Nad", "Klement Gotvald", "Aleksandr Dubchek", "Nikolae Chaushesku", "Imre Nad.")
t.B("Vengriyadagi 1956-yilgi qo‘zg‘olonning asosiy janglari qayerda bo‘lgan?", "Budapeshtda", "Pragada", "Varshavada", "Buxarestda", "Budapeshtda.")
t.B("Poznanda ishchilar nimaga qarshi ish tashlash e’lon qilgan?", "ish me’yorlari oshirilishi va ish haqi pasaytirilishiga", "kollektivlashtirishga", "sovet qo‘shinlariga", "Imre Nad hukumatiga", "Ish me’yorlari oshirilishi va ish haqi pasaytirilishiga qarshi.")
t.B("«Praga bahori» davrida Chexoslovakiya kommunistik partiyasiga kim boshchilik qilgan?", "Aleksandr Dubchek", "Klement Gotvald", "Imre Nad", "Sali Berisha", "Aleksandr Dubchek.")
t.B("1970-yillarning birinchi yarmida MSHYda sanoat o‘sishi yiliga qancha bo‘lgan?", "6–8%", "1–2%", "15–20%", "50%", "Yiliga 6–8% darajasida.")
t.B("Polsha ishchilari tuzgan mustaqil ommaviy kasaba uyushmasi qanday atalgan?", "«Birdamlik»", "«Kapitanlar harakati»", "«Krayova armiyasi»", "Demokratik ittifoq", "«Birdamlik».")
t.B("Polshada «Birdamlik» vakillari qachon hokimiyatga kelgan?", "1989-yilda", "1991-yilda", "1956-yilda", "1980-yilda", "1989-yili.")
t.B("Vengriya Xalq Respublikasi qachon Vengriya Respublikasi deb o‘zgartirilgan?", "1990-yilda", "1989-yilda", "1956-yilda", "1991-yilda", "1990-yili.")
t.B("Qaysi mamlakatda kommunistik rejim qo‘zg‘olon va harbiy to‘qnashuv natijasida qulagan?", "Ruminiya", "Polsha", "Vengriya", "Bolgariya", "Ruminiyada; diktator Chaushesku otib tashlandi.")
t.B("Ruminiyaga uzoq yillar rahbarlik qilgan diktator kim?", "Nikolae Chaushesku", "Imre Nad", "Sali Berisha", "Klement Gotvald", "Nikolae Chaushesku.")
t.B("1992-yilgi saylovlarda Albaniya prezidenti etib kim saylangan?", "Sali Berisha", "Nikolae Chaushesku", "Aleksandr Dubchek", "Imre Nad", "Demokratik lider Sali Berisha.")
t.B("O‘IYK va Varshava shartnomasi tashkiloti qachon tarqalib ketgan?", "1991-yilda", "1989-yilda", "1985-yilda", "1956-yilda", "1991-yili.")
t.NAT("1956-yili SSSRda Stalin shaxsiga sig‘inish qoralandi.", "Sharqiy Yevropada Stalin qo‘llab-quvvatlagan rahbarlar almashina boshladi", "Stalin rahbarlari mustahkamlandi", "O‘IYK tuzildi", "Varshava shartnomasi tarqaldi", "Ko‘plab mamlakatlarda rahbarlar almashdi.")
t.NAT("Vengriyada 1956-yilgi qo‘zg‘olon sovet qo‘shinlari tomonidan bostirildi.", "I. Nad va safdoshlari sud qilinib, o‘lim jazosiga hukm qilindi", "Vengriya NATOga kirdi", "Imre Nad prezident bo‘ldi", "ko‘ppartiyaviylik o‘rnatildi", "Nad va uning safdoshlari o‘limga hukm qilindi.")
t.NAT("Varshava shartnomasi qo‘shinlari Chexoslovakiyaga kiritildi.", "«Praga bahori» bostirildi, Dubchek boshchiligidagi rahbarlar qamoqqa olindi", "Chexoslovakiya Varshava shartnomasidan chiqdi", "Dubchek prezident bo‘ldi", "Chexoslovakiya NATOga kirdi", "«Praga bahori» bostirildi.")
t.TF("Albaniya, Vengriya, Ruminiya va Yugoslaviyada bittadan partiya faoliyat yuritgan.", True, "To‘g‘ri.")
t.TF("MSHYdagi o‘zgarishlar Yugoslaviyaga eng kuchli ta’sir ko‘rsatgan.", False, "Noto‘g‘ri: Yugoslaviyaga ta’siri kam bo‘lgan.")
t.MUL([("Albaniya demokratik partiyasi 1989-yilda tuzilgan.", True),
       ("1980-yillarda barcha sotsialistik mamlakatlarda aholining yashash darajasi sezilarli pasaygan.", True),
       ("Bolgariyada 1991-yilda kommunistlar hokimiyatni mustahkamlagan.", False)],
      "III noto‘g‘ri: 1991-yili Bolgariyada muxolifat kuchlar hokimiyatga keldi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Chexoslovakiyada tub burilish yuz berdi", "Kommunistlar MSHY mamlakatlarida to‘liq hokimiyatni egalladi", "Vengriyada Imre Nad hukumati harakati", "Polshada «Birdamlik» hokimiyatga keldi", "Vengriya Respublikasi nomi berildi", "O‘IYK tarqaldi"],
      "1948 → 1949 → 1956 → 1989 → 1990 → 1991.")
t.MATCH("Shaxslarni mamlakati bilan moslashtiring.", ["Klement Gotvald", "Imre Nad", "Nikolae Chaushesku", "Sali Berisha"],
        ["Chexoslovakiya", "Vengriya", "Ruminiya", "Albaniya", "Bolgariya"], 'abcd',
        "Gotvald – Chexoslovakiya; Nad – Vengriya; Chaushesku – Ruminiya; Berisha – Albaniya.")
t.VENN("1956-yil Vengriya", "«Praga bahori»",
       [("Imre Nad hukumati", 1), ("asosiy janglar Budapeshtda", 1),
        ("Aleksandr Dubchek rahbarligi", 2), ("Varshava shartnomasi qo‘shinlari kiritilgan", 2),
        ("kuch bilan bostirilgan harakat", 3)],
       "Vengriya – Nad, Budapesht; Praga – Dubchek, VSh qo‘shinlari; ikkalasi bostirilgan.")
t.MAPMATCH(EU, ['Budapesht', 'Polsha', 'Ruminiya', 'Albaniya'],
           ["1956-yilgi qo‘zg‘olonning asosiy janglari bo‘lgan shahar", "«Birdamlik» kasaba uyushmasi tuzilgan mamlakat", "Chaushesku rejimi qo‘zg‘olon bilan qulagan mamlakat", "1992-yilda Sali Berisha prezident bo‘lgan mamlakat"],
           "1 – Budapesht; 2 – Polsha; 3 – Ruminiya; 4 – Albaniya.")
