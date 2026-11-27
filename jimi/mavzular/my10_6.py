from qlib import Topic, PLACES, REG
TOPICS = {}
W = 'globe'; EU = 'europe'

# 15 G‘arbiy Yevropa va Shimoliy Amerika
t = Topic('y10j15', 10015); TOPICS['y10j15'] = t
t.B("Ikkinchi jahon urushidan keyin Markaziy va G‘arbiy Yevropada nima tiklangan?", "parlament demokratiyasi", "absolyut monarxiya", "harbiy diktatura", "feodal tuzum", "Parlament demokratiyasi tiklandi.")
t.B("G‘arb mamlakatlarida demokratiya deganda qanday demokratiya tushunila boshlagan?", "liberal demokratiya", "xalq demokratiyasi", "sotsialistik demokratiya", "boshqariladigan demokratiya", "Liberal demokratiya.")
t.B("Qaysi biri liberal demokratiya uchun xarakterli?", "hokimiyatning bo‘linishi", "yagona partiya hukmronligi", "senzura", "rejali iqtisodiyot", "Erkin saylovlar, qonun ustuvorligi, hokimiyatning bo‘linishi, shaxs erkinliklari.")
t.B("G‘arbiy Yevropa va Shimoliy Amerikada shakllangan sivilizatsiya XX asrda qanday nom olgan?", "«Yevroatlantik sivilizatsiya»", "«industrial sivilizatsiya»", "«postindustrial jamiyat»", "«Pax Britanica»", "«Yevroatlantik sivilizatsiya».")
t.B("1950-yillarda qaysi mamlakatlar o‘z «iqtisodiy mo‘jiza»sini namoyish qilgan?", "Italiya, GFR, Shvetsiya", "SSSR, Polsha, Vengriya", "Ispaniya, Portugaliya, Gretsiya", "Xitoy, Hindiston, Pokiston", "Italiya, Germaniya Federativ Respublikasi, Shvetsiya.")
t.B("«Umumiy farovonlik jamiyati»ni qurish g‘oyasi qachon paydo bo‘lgan?", "1960-yillarda", "1940-yillarda", "1980-yillarda", "1920-yillarda", "1960-yillarda.")
t.B("Qaysi imtiyoz «umumiy farovonlik» siyosatiga kiradi?", "bepul maktab ta’limi", "yagona partiya", "majburiy mehnat", "soliqlarni bekor qilish", "Bolali oilalarga nafaqa, bepul maktab, qarilik pensiyasi, ishsizlik nafaqasi.")
t.B("Sotsializmning «skandinav modeli» qaysi mamlakatlarda amalga oshirilgan?", "Daniya, Norvegiya, Shvetsiya", "Fransiya, Italiya, Ispaniya", "AQSH, Kanada, Meksika", "Polsha, Vengriya, Chexoslovakiya", "Daniya, Norvegiya va Shvetsiya.")
t.B("XX asrning 60-yillari qanday davr sifatida tarixga kirgan?", "liberal islohotchilikning eng avj pallasi", "neokonservativ inqilob", "jahon iqtisodiy inqirozi", "sovuq urush tugashi", "Liberal islohotchilikning eng avj pallasi.")
t.B("1960-yillarda AQSHda qanday harakat qizg‘in tus olgan?", "fuqarolar tengligi uchun harakat", "monarxiyani tiklash harakati", "izolyatsionizm harakati", "mustamlakachilik harakati", "Fuqarolar tengligi uchun harakat; qora tanlilar namoyishlari.")
t.B("Parij talabalarining namoyishi qachon boshlangan?", "1968-yil mayda", "1960-yilda", "1980-yilda", "1956-yilda", "1968-yil mayda.")
t.B("Referendumda qo‘llab-quvvatlanmagach, qaysi fransuz prezidenti iste’foga chiqqan?", "Sharl de Goll", "Fransua Mitteran", "Jorj Pompidu", "Valeri Jiskar d’Esten", "Sharl de Goll iste’foga chiqishga majbur bo‘ldi.")
t.B("Fuqarolarning muhim masalalar bo‘yicha bevosita ovoz berishi nima deb ataladi?", "referendum", "saylov kampaniyasi", "impichment", "parlament", "Referendum.")
t.B("1980-yili AQSHda hokimiyatga kim kelgan?", "Ronald Reygan", "Jon Kennedi", "Franklin Ruzvelt", "Daniel Bell", "Ronald Reygan; 1984-yili qayta saylandi.")
t.B("Buyuk Britaniyada qatorasiga uch marta g‘alaba qozongan konservativ partiyaga kim boshchilik qilgan?", "Margaret Tetcher", "Uinston Cherchill", "Nevill Chemberlen", "Tony Bler", "Margaret Tetcher.")
t.B("Ilmiy-texnik taraqqiyotning birinchi to‘lqini qachon bo‘lgan?", "1940-yillar oxiri – 1950-yillar", "1970-yillar ikkinchi yarmi", "1920-yillar", "1990-yillar", "1940-yillar oxiri – 1950-yillar.")
t.B("1970-yillar ikkinchi yarmida boshlangan ilmiy-texnik taraqqiyot to‘lqini qanday nom olgan?", "informatsion (telekommunikatsion) inqilob", "sanoat to‘ntarishi", "yashil inqilob", "madaniy inqilob", "Informatsion yoki telekommunikatsion inqilob.")
t.B("«Postindustrial jamiyat» atamasini kim muomalaga kiritgan?", "Daniel Bell", "Ronald Reygan", "Margaret Tetcher", "Sharl de Goll", "1962-yili amerikalik sotsiolog Daniel Bell.")
t.B("Postindustrial jamiyatda nima ustuvor?", "axborot ishlab chiqarish", "sanoat ishlab chiqarish", "qishloq xo‘jaligi", "harbiy sanoat", "Sanoat emas, axborot ishlab chiqarish ustuvor.")
t.NAT("1968-yilda Fransiyada prezident tashabbusi bilan referendum o‘tkazildi.", "saylovchilarning ko‘pchiligi prezidentni qo‘llamadi va de Goll iste’foga chiqdi", "de Goll umrbod prezident bo‘ldi", "talabalar namoyishi taqiqlandi", "Fransiya NATOdan chiqdi", "Sharl de Goll iste’foga chiqishga majbur bo‘ldi.")
t.NAT("1970–1980-yillardagi neokonservativ to‘lqin.", "so‘l partiyalar mavqeini yo‘qotib, o‘ng va konservativ kuchlar g‘alaba qozondi", "so‘l partiyalar hokimiyatga keldi", "liberal islohotlar avj oldi", "umumiy farovonlik jamiyati qurildi", "Reygan va Tetcher g‘alabasi bunga misol.")
t.TF("Ilmiy-texnik taraqqiyotning birinchi to‘lqinida aviakosmik va robot texnikasi kabi sohalar paydo bo‘lgan.", True, "To‘g‘ri.")
t.TF("1960-yillarda D. Bellning postindustrial jamiyat haqidagi g‘oyasi hamma tomonidan darhol amaliy deb tan olingan.", False, "Noto‘g‘ri: o‘shanda u odamlarga utopiya bo‘lib tuyulgan.")
t.MUL([("Urushdan keyingi davr uchun harbiy-sanoat kompleksining keng rivojlanishi xos bo‘lgan.", True),
       ("«Umumiy farovonlik» siyosatining maqsadi ijtimoiy tengsizlikni bartaraf qilish edi.", True),
       ("G‘arbda qaror topgan rivojlanish modeli 1950-yillar boshida inqirozga kirgan.", False)],
      "III noto‘g‘ri: 1970-yillar oxiri – 1980-yillar boshlarida inqirozga kirgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["«Iqtisodiy mo‘jiza»lar davri", "«Postindustrial jamiyat» atamasi kiritildi", "Parij talabalari namoyishi", "Reygan hokimiyatga keldi", "Reygan qayta saylandi"],
      "1950-yillar → 1962 → 1968 → 1980 → 1984.")
t.VENN("«Umumiy farovonlik jamiyati»", "Neokonservativ to‘lqin",
       [("1960-yillarda paydo bo‘lgan g‘oya", 1), ("bepul maktab va pensiya kafolati", 1),
        ("Reygan va Tetcher g‘alabasi", 2), ("o‘ng kuchlar g‘alabasi", 2),
        ("G‘arb mamlakatlaridagi rivojlanish", 3)],
       "Farovonlik – 1960-yillar, imtiyozlar; neokonservatizm – Reygan, Tetcher; ikkalasi G‘arb rivojlanishi.")
t.MAPMATCH('europeN', ['Parij', 'Shvetsiya', 'Angliya', 'Italiya'],
           ["1968-yil mayda talabalar namoyishi boshlangan shahar", "nomi bilan sotsializmning bir modeli atalgan mamlakat", "M. Tetcher boshchiligida konservatorlar uch marta g‘alaba qozongan mamlakat", "GFR va Shvetsiya bilan birga 1950-yillarda «iqtisodiy mo‘jiza» ko‘rsatgan mamlakat"],
           "1 – Parij; 2 – Shvetsiya; 3 – Angliya; 4 – Italiya.")

# 16 SSSR va Sharqiy Yevropa
t = Topic('y10j16', 10016); TOPICS['y10j16'] = t
t.B("Polsha, Chexoslovakiya, Vengriya jahon siyosiy xaritasida qachon paydo bo‘lgan?", "Birinchi jahon urushidan so‘ng", "Ikkinchi jahon urushidan so‘ng", "XIX asr boshida", "1955-yilda", "Birinchi jahon urushidan so‘ng.")
t.B("Fashizm tor-mor qilingach Sharqiy Yevropada qanday hukumatlar hokimiyatga kelgan?", "antifashist partiyalardan iborat koalitsion hukumatlar", "monarxistik hukumatlar", "harbiy xuntalar", "fashistik hukumatlar", "Kommunistlar, sotsial-demokratlar, liberallardan iborat koalitsion hukumatlar.")
t.B("Sharqiy Yevropada kommunistik qarashlarni yoqlamaganlar hukumatdan qachon chiqarilgan?", "1947–1948-yillarda", "1945-yilda", "1955-yilda", "1956-yilda", "1947–1948-yillari.")
t.B("«Marshall rejasi»ni qaysi davlat taklif qilgan?", "AQSH", "SSSR", "Buyuk Britaniya", "Fransiya", "1947-yili AQSH taklif qildi.")
t.B("«Marshall rejasi» qachon taklif qilingan?", "1947-yilda", "1949-yilda", "1955-yilda", "1945-yilda", "1947-yili.")
t.B("Yevropaning ikki guruhga bo‘linishi qachongacha davom etgan?", "1980-yillar oxirigacha", "1956-yilgacha", "1960-yillargacha", "1949-yilgacha", "1980-yillar oxirigacha.")
t.B("Ikki blok o‘rtasidagi qarama-qarshilik jahon tarixida qanday nom olgan?", "«sovuq urush»", "«qayta qurish»", "«neokonservativ to‘lqin»", "«yangi kurs»", "«Sovuq urush».")
t.B("O‘zaro Iqtisodiy Yordam Kengashi (O‘IYK) qachon tuzilgan?", "1949-yil yanvarda", "1949-yil aprelda", "1955-yilda", "1947-yilda", "1949-yil yanvarda.")
t.B("NATO qachon tuzilgan?", "1949-yil aprelda", "1949-yil yanvarda", "1955-yilda", "1947-yilda", "1949-yil aprelda.")
t.B("NATOga javob tariqasida qaysi tashkilot tuzilgan?", "Varshava Shartnomasi Tashkiloti", "O‘IYK", "BMT", "Millatlar Ligasi", "1955-yili Varshava Shartnomasi Tashkiloti.")
t.B("Varshava Shartnomasi Tashkiloti qachon tuzilgan?", "1955-yilda", "1949-yilda", "1956-yilda", "1947-yilda", "1955-yili.")
t.B("Harbiy-siyosiy va iqtisodiy ittifoqlar tizimining markazlariga qaysi davlatlar aylangan?", "AQSH va SSSR", "Britaniya va Fransiya", "Germaniya va Italiya", "Xitoy va Yaponiya", "Dunyoning eng katta davlatlari – AQSH va SSSR.")
t.B("KPSSning XX syezdi qachon bo‘lgan?", "1956-yil fevralda", "1955-yilda", "1949-yilda", "1947-yilda", "1956-yil fevralda.")
t.B("XX syezdda shaxsga sig‘inishni kim qoralagan?", "Nikita Xrushchyov", "Stalin", "Lenin", "Gorbachyov", "Nikita Xrushchyov.")
t.B("Kommunizm tamoyillarini qo‘llab-quvvatlaydigan odam nima deb ataladi?", "kommunist", "liberal", "konservator", "monarxist", "Kommunist.")
t.B("Hur fikrli, erkin shaxs, liberalizm tarafdori kim deb ataladi?", "liberal", "kommunist", "fashist", "monarxist", "Liberal.")
t.NAT("KPSSning XX syezdida shaxsga sig‘inish qoralandi.", "sovet totalitar davlatini anglash jarayoni va xalqaro kommunistik harakat inqirozi boshlandi", "Stalin obro‘si oshdi", "sovuq urush tugadi", "NATO tarqatildi", "Sotsialistik tizim bu inqirozdan chiqa olmadi.")
t.NAT("Qayta qurish yillarida oshkoralik kirib keldi.", "stalinizm jinoyatlari ochildi, ko‘pchilik tuzumdan voz kechish kerakligini angladi", "totalitar tuzum mustahkamlandi", "kommunistik mafkura kuchaydi", "senzura kuchaydi", "Oshkoralik sovet jamiyatining poklanishi yo‘lida katta qadam bo‘ldi.")
t.TF("SSSR sotsializm qurish yo‘liga kirgan mamlakatlarga moliyaviy va harbiy yordam ko‘rsatgan.", True, "To‘g‘ri.")
t.TF("SSSRdagi kommunistik mafkura inqirozi dunyodagi so‘l mafkuraning kuchayishiga olib kelgan.", False, "Noto‘g‘ri: butun dunyoda so‘l mafkuraning inqiroziga olib keldi.")
t.MUL([("Sharqiy Yevropa mamlakatlarining ko‘pchiligida sovet qo‘shinlari joylashgan edi.", True),
       ("Har bir blok o‘z dunyo modelini va yashash tarzini himoya qilgan.", True),
       ("O‘IYK G‘arb davlatlarining harbiy-siyosiy ittifoqi edi.", False)],
      "III noto‘g‘ri: O‘IYK SSSR va Sharqiy Yevropaning iqtisodiy ittifoqi edi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["«Marshall rejasi» taklif qilindi", "O‘IYK tuzildi", "NATO tuzildi", "Varshava Shartnomasi Tashkiloti tuzildi", "KPSS XX syezdi"],
      "1947 → 1949-yil yanvar → 1949-yil aprel → 1955 → 1956.")
t.VENN("NATO", "Varshava Shartnomasi Tashkiloti",
       [("1949-yil aprelda tuzilgan", 1), ("G‘arb davlatlari ittifoqi", 1),
        ("1955-yilda tuzilgan", 2), ("SSSR va Sharqiy Yevropa ittifoqi", 2),
        ("harbiy-siyosiy tashkilot", 3)],
       "NATO – 1949, G‘arb; VShT – 1955, SSSR; ikkalasi harbiy-siyosiy tashkilot.")
t.MAPN(EU, ['Varshava', 'Chexoslovakiya', 'Vengriya', 'Moskva'], "Qaysi raqam bilan 1955-yilda tuzilgan harbiy-siyosiy ittifoq nomini bergan shahar belgilangan?",
       "1 – Varshava (Varshava Shartnomasi Tashkiloti); 2 – Chexoslovakiya; 3 – Vengriya; 4 – Moskva.")
