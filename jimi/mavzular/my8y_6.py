from qlib import Topic, PLACES, REG
TOPICS = {}

# 19 O‘rta asrlar Yevropa aholisining kundalik hayoti
t = Topic('y8j19', 8019); TOPICS['y8j19'] = t
t.B("Zodagonlarning barcha mulklari va qasrlari jamlangan hudud qanday atalgan?", "manor", "gildiya", "graflik", "karantin", "Manor.")
t.B("Manorning markazi nima bo‘lgan?", "qal’a yoki qasr", "cherkov", "bozor", "dala", "Qal’a yoki qasr.")
t.B("Zodagonlar urushga ketganda manorni kim boshqargan?", "ularning xotinlari yoki qizlari", "ruhoniylar", "dehqonlar oqsoqoli", "qirol", "Xotinlari yoki qizlari.")
t.B("Qasrning birinchi qavatida nimalar joylashgan?", "oshxona va katta zal", "yotoqxonalar", "bazmlar zali", "xizmatkorlar xonasi", "Oshxona va katta zal.")
t.B("Dehqonlar g‘allani qaysi oylarda yig‘ib olishgan?", "avgust va sentyabrda", "fevral va martda", "noyabrda", "iyunda", "Avgust va sentyabrda.")
t.B("Dehqonlar chorva mollarini qaysi oyda so‘yib, go‘shtini tuzlashgan?", "noyabrda", "oktyabrda", "martda", "avgustda", "Noyabrda.")
t.B("Faqat qirollik sulolasiga qanday kiyim kiyishga ruxsat berilgan?", "binafsha ipak", "baxmal", "zig‘ir mato", "jun", "Oltin-kumush buyumlar va binafsha ipak.")
t.B("O‘rta asrlar G‘arbiy Yevropa bazmlarining qaynatilgan bug‘doydan tayyorlangan muhim taomi qaysi?", "frumentiy", "pitstsa", "paella", "sho‘rva", "Frumentiy.")
t.B("Oddiy xalqning asosiy taomi nima bo‘lgan?", "non", "go‘sht", "baliq", "frumentiy", "Non.")
t.B("Necha yoshdan oshgan yigitlar ritsarlik unvoniga sazovor bo‘lishi mumkin edi?", "o‘n olti", "o‘n ikki", "yigirma", "o‘n sakkiz", "O‘n olti yoshdan.")
t.B("Ritsarlar amal qilgan qoidalar qanday atalgan?", "ritsarlik kodeksi", "gildiya nizomi", "Magna Carta", "Salik haqiqati", "Ritsarlik kodeksi.")
t.B("Tinchlik davrida ritsarlar o‘rtasida o‘tkazilgan musobaqalar nima deb atalgan?", "turnirlar", "yarmarkalar", "birjalar", "festivallar", "Turnirlar.")
t.B("Shifokorlar tayyorlaydigan birinchi tibbiyot maktabi qayerda paydo bo‘lgan?", "Salernoda", "Parijda", "Bolonyada", "Oksfordda", "IX asrda Italiyadagi Salernoda.")
t.B("Salerno maktabi qachon universitet maqomini olgan?", "1213-yilda", "1347-yilda", "1088-yilda", "1406-yilda", "1213-yilda.")
t.B("«Karantin» so‘zi italyan tilida nimani bildiradi?", "qirq kun", "o‘n kun", "yopiq eshik", "kasallik", "Qirq kun.")
t.B("Karantin birinchi marta qachon joriy qilingan?", "XIV asrda", "IX asrda", "XII asrda", "XVI asrda", "XIV asrda Italiyaning port shaharlarida.")
t.B("G‘arbiy Yevropada rasmiy hujjatlar va ibodat tili qaysi bo‘lgan?", "lotin tili", "yunon tili", "fransuz tili", "nemis tili", "Lotin tili.")
t.B("Rus, ukrain, belarus tillari qaysi tillar guruhiga kiradi?", "slavyan", "roman", "german", "turkiy", "Slavyan tillari guruhiga.")
t.NAT("Lordning o‘rmonlarida oddiy aholiga ov qilish taqiqlangan, ko‘p dehqonlarda uy hayvonlari yo‘q edi.", "dehqonlar juda kam go‘sht iste’mol qilgan", "dehqonlar ko‘p go‘sht yegan", "dehqonlar shaharlarga ko‘chgan", "ov keng tarqalgan", "Dehqonlar kam go‘sht yegan.")
t.NAT("Kambag‘allar uchun pechkada yoqish uchun yog‘och qimmat edi.", "ular uzoq vaqt suvdan isitmay foydalanishgan", "ular hammomlarda yuvinishgan", "ular ko‘mir sotib olgan", "yog‘och narxi tushgan", "Shaxsiy gigiyena juda oddiy bo‘lgan.")
t.NAT("XII asrdan Ibn Sino va ar-Roziy asarlari lotin tiliga tarjima qilindi.", "ular Yevropa tibbiyotida foydalanila boshlandi", "Yevropada tibbiyot taqiqlandi", "Salerno maktabi yopildi", "arab tili rasmiy tilga aylandi", "Sharq tibbiyoti Yevropaga yoyildi.")
t.NAT("XIV–XV asrlarda hashamdor kiyimlar paydo bo‘ldi.", "urfga qarab kiyinish zodagonlar o‘rtasidagi raqobat ko‘rinishiga aylandi", "kiyim farqlari yo‘qoldi", "dehqonlar ipak kiya boshladi", "kiyinish qonunlari bekor qilindi", "Kiyinish raqobatga aylandi.")
t.TF("Kambag‘al dehqonlarning uylari bir xonali bo‘lgan.", True, "To‘g‘ri.")
t.TF("Kambag‘allar uchun operatsiya vaqtida giyohli tinchlantiruvchi dorilar berilgan.", False, "Noto‘g‘ri: ularga bir bo‘lak yog‘och tishlatilgan, dorilar badavlatlarga berilgan.")
t.TF4([("Dastlab qal’a va qasrlar yog‘ochdan qurilgan.", True), ("Bazmlarda zodagonlar boshqalardan balandroq joyda o‘tirishgan.", True),
       ("Ritsarlikka qabul qilinganga qilich, qalqon va dubulg‘a sovg‘a qilingan.", True), ("Ruhoniylar maktab va kasalxonalarni boshqarmagan.", False)],
      "4-noto‘g‘ri: ruhoniylar maktablar va kasalxonalarni boshqargan.")
t.MUL([("Frumentiy dastlab dehqonlarning taomi bo‘lgan.", True),
       ("Ingliz, fransuz, ispan tillari hind-yevropa tillari oilasiga mansub.", True),
       ("Jarrohlik asboblari tibbiy tozalangan.", False)],
      "III noto‘g‘ri: ularning hech biri tibbiy tozalanmagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Salernoda tibbiyot maktabi paydo bo‘ldi", "«Kasalliklarni davolash to‘g‘risida» risolasi yozildi", "Salerno maktabi universitet maqomini oldi", "Italiya port shaharlarida karantin joriy qilindi"],
      "IX asr → XII asr → 1213 → XIV asr.")
t.MATCH("Oylarni dehqon ishlari bilan moslashtiring.", ["avgust–sentyabr", "oktyabr", "noyabr", "fevral–mart"],
        ["g‘alla yig‘ish", "kuzgi ekinlarga zamin tayyorlash", "mol so‘yib go‘shtni tuzlash", "suli, arpa ekish uchun shudgor", "qo‘y junini qirqish"], 'abcd',
        "Avgust–sentyabr – o‘rim; oktyabr – kuzgi ekin; noyabr – go‘sht; fevral–mart – shudgor.")
t.VENN("Zodagonlar", "Dehqonlar",
       [("qasr va manorlarda yashagan", 1), ("ov va shaxmat bilan shug‘ullangan", 1),
        ("loy suvalgan yoki yog‘och uylarda yashagan", 2), ("jun yoki zig‘irdan qo‘pol kiyim kiygan", 2),
        ("katolik cherkovi bilan bog‘liq kundalik hayot", 3)],
       "Zodagonlar – qasr, ov; dehqonlar – oddiy uy, qo‘pol kiyim; umumiy – cherkov.")
t.MAPN('italy', ['Salerno', 'Rim', 'Florensiya', 'Venetsiya'], "Xaritada IX asrda shifokorlar tayyorlaydigan birinchi tibbiyot maktabi paydo bo‘lgan shahar qaysi raqam bilan belgilangan?",
       "Salerno – Italiya janubida.")

# 20 XIII–XV asrlarda Yevropa iqtisodiyoti
t = Topic('y8j20', 8020); TOPICS['y8j20'] = t
t.B("O‘rta asrlarda G‘arbiy Yevropa shaharlarining odatdagi aholisi qancha bo‘lgan?", "ming nafardan besh ming nafargacha", "20–30 ming", "80–100 ming", "yarim million", "1–5 ming kishi.")
t.B("XIV–XV asrlarda qancha aholisi bo‘lgan shahar yirik hisoblangan?", "20–30 ming", "1–5 ming", "200 ming", "1 million", "20–30 ming.")
t.B("Aholisi 80–100 ming kishidan oshgan shahar qaysi?", "Florensiya", "Bryugge", "Trua", "Salerno", "Konstantinopol, Parij, Milan, Florensiya, Kordova, Sevilya.")
t.B("Bubon vabosi qanday nom bilan ham atalgan?", "qora o‘lat", "qizil vabo", "oq o‘lat", "chechak", "Qora o‘lat.")
t.B("Qora o‘lat nimadan tarqalgan?", "qora kalamushlardan", "chivinlardan", "qushlardan", "suvdan", "Qora kalamushlardan.")
t.B("Italiya savdogarlari o‘latni qaysi shahardan olib kelgan?", "Kaffa", "Konstantinopol", "Iskandariya", "Venetsiya", "Qora dengizdagi Kaffadan Sitsiliyaga.")
t.B("Vabo qachon Sitsiliya oroliga keltirilgan?", "1347-yil oktyabrida", "1350-yil oxirida", "1351-yilda", "1406-yilda", "1347-yil oktyabrida.")
t.B("1347–1351-yillarda Yevropa aholisining qancha qismi vabodan qirildi?", "uchdan bir qismi", "yarmi", "o‘ndan bir qismi", "to‘rtdan uch qismi", "75 million aholining uchdan biri.")
t.B("Birgina Angliyada vabo tufayli nechta qishloq yo‘q bo‘ldi?", "mingga yaqin", "yuzga yaqin", "o‘n mingga yaqin", "ellikka yaqin", "Mingga yaqin.")
t.B("Vabodan so‘ng Yevropa aholisining tiklanishiga qancha vaqt kerak bo‘ldi?", "taxminan 250 yil", "50 yil", "10 yil", "500 yil", "Taxminan 250 yil.")
t.B("Hunarmand yoki savdogarlar uyushmasi nima deb atalgan?", "gildiya", "manor", "birja", "yarmarka", "Gildiya.")
t.B("Hunarmandlar gildiyalarini qachondan tashkil qila boshlagan?", "XI asrdan", "XIV asrdan", "VIII asrdan", "XVI asrdan", "XI asrdan.")
t.B("Shogird shartnomadagi muddatni o‘tagach qanday maqomga yetgan?", "xalfa", "usta", "gildiya boshlig‘i", "sarrof", "Xalfalik maqomiga.")
t.B("Eng yirik o‘rta asr yarmarkasi qaysi?", "Shampan yarmarkasi", "Bryugge yarmarkasi", "London yarmarkasi", "Genuya yarmarkasi", "XII–XIV asrlardagi Shampan yarmarkasi.")
t.B("Pullarni yarmarka pullariga almashtirib bergan kishilar kimlar?", "sarroflar", "xalfalar", "gildiyalar", "ritsarlar", "Sarroflar – dastlabki bankirlar.")
t.B("Yevropada dastlabki zamonaviy bankka qachon asos solingan?", "1407-yilda Italiyada", "1406-yilda Bryuggeda", "1347-yilda", "1213-yilda", "1407-yilda Italiyada.")
t.B("Germaniyadagi yirik bankir oila qaysi?", "Fuggerlar", "Medichilar", "Jak Kyor", "Burselar", "Fuggerlar.")
t.B("Ilk birja qaysi shaharda bo‘lib o‘tgan?", "Bryugge", "Venetsiya", "London", "Trua", "Bryuggeda (hozirgi Belgiya).")
t.B("Birinchi birja qachon tashkil etilgan?", "1406-yilda", "1407-yilda", "1347-yilda", "1500-yilda", "1406-yilda.")
t.B("Savdogarlar pulni bir hududdan ikkinchisiga o‘tkazish uchun nimadan foydalangan?", "veksel", "gildiya", "kredit karta", "frumentiy", "Vekseldan.")
t.NAT("Shahar uylarining asosiy qismi yog‘ochdan qurilgan edi.", "yong‘in chiqqanda juda katta talafot ko‘rilgan", "shaharlar yong‘indan himoyalangan", "uylar ko‘p asr saqlangan", "tosh qurilish taqiqlangan", "Yong‘inda katta talafot.")
t.NAT("Qora o‘latdan so‘ng ishchi kuchi kamayib qoldi.", "ish haqi keskin oshdi", "ish haqi tushdi", "qaram dehqonlar ko‘paydi", "savdo kengaydi", "Ish haqi oshdi, erkin dehqonlar ko‘paydi.")
t.NAT("Aholining kamayishi oziq-ovqatga talabni kamaytirdi.", "oziq-ovqat narxi tushdi", "narx oshdi", "ocharchilik boshlandi", "dehqonlar ko‘paydi", "Narx tushdi.")
t.NAT("XVI asr boshida yirik boylar dastlabki fabrikalarni tashkil qildi.", "gildiyalar raqobatlasha olmay, bu tizim asta-sekin yo‘qoldi", "gildiyalar kuchaydi", "fabrikalar yopildi", "hunarmandlar boyidi", "Gildiya tizimi yo‘qoldi.")
t.TF("Burselar oilasining gerbida uchta charm hamyon tasvirlangan.", True, "To‘g‘ri; shundan «birja» nomi kelib chiqqan.")
t.TF("Gildiyalarda shogirdlarga maosh to‘langan.", False, "Noto‘g‘ri: shogirdlarga maosh berilmagan, yotoqjoy va ovqat bilan ta’minlangan.")
t.TF4([("Vabo 1350-yil oxiriga kelib butun Yevropaga yoyildi.", True), ("Qora o‘lat feodal tuzumni zaiflashtirdi.", True),
       ("Shampan yarmarkalari Trua, Provans, Lan, Bar shaharlarida o‘tgan.", True), ("O‘rta asrlarda pullar erkin almashtirilgan.", False)],
      "4-noto‘g‘ri: pullar erkin almashtirilmagan.")
t.MUL([("Feodal urushlar va tashqi xavf yangi shaharlar paydo bo‘lishiga sabab bo‘lgan.", True),
       ("Xalfa usta bo‘lish uchun imtihondan o‘tgan.", True),
       ("Gildiya nizomlari zamonaviy dastgohlar joriy etishga yordam bergan.", False)],
      "III noto‘g‘ri: nizomlar ishlab chiqarishni ko‘paytirishga to‘sqinlik qilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Hunarmandlar gildiyalar tuza boshladi", "Vabo Sitsiliyaga keltirildi", "Vabo butun Yevropaga yoyildi", "Bryuggeda birinchi birja tashkil etildi", "Italiyada dastlabki zamonaviy bank ochildi"],
      "XI asr → 1347 → 1350 → 1406 → 1407.")
t.MATCH("Bankir oilalarni mamlakati bilan moslashtiring.", ["Medichilar", "Fuggerlar", "Jak Kyor", "Van der Burse"],
        ["Italiya", "Germaniya", "Fransiya", "Bryugge (Belgiya)", "Angliya"], 'abcd',
        "Medichilar – Italiya; Fuggerlar – Germaniya; Jak Kyor – Fransiya; Burselar – Bryugge.")
t.VENN("Gildiyalar", "Fabrikalar",
       [("XI asrdan tuzila boshlagan", 1), ("shogird–xalfa–usta pog‘onalari", 1),
        ("XVI asr boshida boylar tashkil etgan", 2), ("keng ko‘lamli samarali ishlab chiqarish", 2),
        ("shaharlarda mahsulot ishlab chiqarish shakli", 3)],
       "Gildiyalar – XI asr, pog‘onalar; fabrikalar – XVI asr, samaradorlik; umumiy – ishlab chiqarish.")
t.MAPMATCH('europe', ['Kaffa', 'Sitsiliya', 'Bryugge', 'Trua'],
           ["o‘lat olib kelingan Qora dengiz shahri", "1347-yil vabo keltirilgan orol", "1406-yilda birinchi birja tashkil etilgan shahar", "Shampan yarmarkasi o‘tkazilgan shahar"],
           "1 – Kaffa; 2 – Sitsiliya; 3 – Bryugge; 4 – Trua.")
