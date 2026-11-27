from qlib import Topic, PLACES, REG
TOPICS = {}
FR = 'france'

# 1 Fransiyada markazlashgan davlat. General shtatlar
t = Topic('y8j1', 8001); TOPICS['y8j1'] = t
t.B("Karolinglarning so‘nggi vakili Lyudovik V vafotidan so‘ng qaysi sulola hokimiyatga kelgan?", "Kapetinglar", "Valualar", "Merovinglar", "Burbonlar", "987-yilda Kapetinglardan Gugo Kapet.")
t.B("Kapetinglar sulolasining dastlabki vakili kim?", "Gugo Kapet", "Filipp II Avgust", "Lyudovik VI", "Filipp IV", "Gugo Kapet.")
t.B("X asr oxirida Fransiya nechta mustaqil mulkka bo‘lingan edi?", "14 ta", "20 ta", "3 ta", "7 ta", "14 ta mustaqil mulkka.")
t.B("Yirik gersog va graflar qirolni qanday hisoblagan?", "«tenglarning birinchisi»", "«Osmon o‘g‘li»", "«xudoning soyasi»", "«oliy hakam»", "Qirolni «tenglarning birinchisi» deb hisoblashgan.")
t.B("Mehnatning hududiy taqsimotiga ko‘ra Normandiya qaysi sohaga ixtisoslashgan?", "temirchilik, tuz, qoramol va yilqi", "to‘qimachilik", "vinochilik", "movut ishlab chiqarish", "Normandiya – temirchilik, tuz, qoramol va yilqi.")
t.B("Parij shahriga qaysi qabila asos solgan?", "keltlarning parizi qabilasi", "franklar", "normannlar", "burgundlar", "Mil. avv. III asrda keltlarning parizi qabilasi Lyutetsiya hududida.")
t.B("Fransiyani birlashtirish jarayoni qaysi qirol davrida boshlangan?", "Lyudovik VI", "Filipp IV", "Gugo Kapet", "Karl VII", "Lyudovik VI; Burj va Sans shaharlarini bo‘ysundirgan.")
t.B("Filipp II Avgust inglizlardan qaysi hududni qo‘shib olgan?", "Normandiya", "Flandriya", "Burgundiya", "Navarra", "Normandiya, Men, Anju, Tyuren va Puatyening bir qismi.")
t.B("Filipp II Avgust islohotiga ko‘ra qirol mulklari nechta viloyatga bo‘lingan?", "20 ta", "14 ta", "3 ta", "10 ta", "20 viloyatga.")
t.B("Fransiya aholisi nechta toifaga bo‘lingan?", "uch toifaga", "ikki toifaga", "to‘rt toifaga", "besh toifaga", "Ruhoniylar, zodagonlar va uchinchi toifa.")
t.B("Qaysi toifa qirolga soliq to‘lashdan ozod bo‘lgan?", "ruhoniylar va zodagonlar", "boy shaharliklar", "dehqonlar", "hunarmandlar", "I va II toifa – ruhoniylar va zodagonlar.")
t.B("Filipp IV davrida Fransiyaning qancha qismi birlashtirilgan?", "3/4 qismi", "yarmi", "1/3 qismi", "to‘liq", "Shampan, Navarra, Lion qo‘shilib, 3/4 qismi birlashtirildi.")
t.B("Filipp IV bilan munosabati buzilgan Rim papasi kim?", "Bonifatsiy VIII", "Kliment V", "Urban II", "Innokentiy III", "Bonifatsiy VIII (1294–1303).")
t.B("Cherkovdan haydash va ibodat qilishni taqiqlash qanday ataladi?", "anafema", "indulgensiya", "selebat", "inkvizitsiya", "Anafema.")
t.B("«Papalarning Avinyon tutqunligi» qaysi yillarni o‘z ichiga oladi?", "1309–1377-yillarni", "1294–1303-yillarni", "1302–1357-yillarni", "1337–1453-yillarni", "1309–1377-yillar.")
t.B("General shtatlar birinchi marta qachon chaqirilgan?", "1302-yilda", "1357-yilda", "1285-yilda", "1309-yilda", "1302-yili Parijning bosh ibodatxonasida.")
t.B("General shtatlarning asosiy vazifasi nima edi?", "soliqlarni joriy etishga ruxsat berish", "qonunlarni qabul qilish", "qirolni saylash", "urush e’lon qilish", "Vazifasi soliqlarga ruxsat berish bilan cheklangan.")
t.NAT("Mehnatning hududiy taqsimoti rivojlanib bordi.", "viloyatlar savdoda bir-biriga bog‘lanib, feodal tarqoqlikka barham berila boshlandi", "viloyatlar bir-biridan uzildi", "savdo to‘xtadi", "qirol hokimiyati zaiflashdi", "Feodal tarqoqlikka barham berildi.")
t.NAT("Filipp II Avgust Normandiya, Men, Anju, Tyuren yerlarini qo‘shib oldi.", "Fransiya Atlantika okeani va La Mansh bo‘g‘oziga chiqdi", "Fransiya Angliyaga qo‘shildi", "Fransiya dengizdan uzildi", "Akvitaniya mustaqil bo‘ldi", "Atlantika va La Manshga chiqish ta’minlandi.")
t.NAT("Papa Bonifatsiy VIII qirol vakilining haqoratidan so‘ng vafot etdi.", "Fransiyalik arxiyepiskop Kliment V nomi bilan papa bo‘lib, Avinyonga ko‘chdi", "papalik tugatildi", "Filipp IV cherkovdan haydaldi", "papa qarorgohi Parijga ko‘chdi", "«Avinyon tutqunligi» boshlandi.")
t.NAT("1357-yilda General shtatlar vakolatlarini oshirishni talab qildi.", "dvoryanlar va shaharliklar orasida hamfikrlik yo‘qligi sabab talablar to‘la amalga oshmadi, qirol mavqeini tikladi", "General shtatlar qirolni ag‘dardi", "qirol hokimiyati butunlay cheklandi", "General shtatlar tarqatildi", "Qirol mavqeini qayta tiklab oldi.")
t.TF("General shtatlarda ruhoniylar va dvoryanlar bir ovozga qarshi ikki ovoz berish huquqiga ega bo‘lgan.", True, "To‘g‘ri.")
t.TF("General shtatlar qonunlarni qabul qilish huquqiga ega bo‘lgan.", False, "Noto‘g‘ri: qonun qabul qilish huquqi yo‘q edi, faqat soliqlarga ruxsat berardi.")
t.TF4([("Lyudovik VII Akvitaniya malikasi Eleonoraga uylangan.", True), ("Tuluza va Flandriya to‘qimachilikka ixtisoslashgan.", True),
       ("Filipp IV davrida Flandriya va Bretan Fransiyaga qo‘shib olingan.", False), ("General shtatlar uch palataga bo‘lingan.", True)],
      "3-noto‘g‘ri: Flandriya, Bretan, Akvitaniya, Burgundiya hali qo‘shib olinmagan edi.")
t.MUL([("XIV asrda Fransiyada toifaviy monarxiya vujudga kelgan.", True),
       ("Gugo Kapet davridan Parij poytaxt maqomini olgan.", True),
       ("Uchinchi toifani ruhoniylar tashkil etgan.", False)],
      "III noto‘g‘ri: uchinchi toifani boy shaharliklar, dehqonlar, hunarmandlar va kambag‘allar tashkil etgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Verden shartnomasi", "Gugo Kapet hokimiyatga keldi", "General shtatlar chaqirildi", "«Avinyon tutqunligi» boshlandi", "General shtatlar vakolatlarini oshirishni talab qildi"],
      "843 → 987 → 1302 → 1309 → 1357.")
t.MATCH("Viloyatlarni ixtisosligi bilan moslashtiring.", ["Flandriya", "Normandiya", "Shampan", "Parij"],
        ["to‘qimachilik", "temirchilik va tuz ishlab chiqarish", "movut va vinochilik", "eng yirik savdo va iqtisodiy markaz", "kemasozlik"], 'abcd',
        "Flandriya – to‘qimachilik; Normandiya – temirchilik; Shampan – movut, vino; Parij – savdo markazi.")
t.VENN("Imtiyozli tabaqalar", "Uchinchi toifa",
       [("ruhoniylar", 1), ("soliqdan ozod", 1),
        ("dehqonlar va hunarmandlar", 2), ("soliqlarning butun og‘irligi ular bo‘yniga tushgan", 2),
        ("General shtatlarda vakillari bo‘lgan", 3)],
       "Imtiyozlilar – ruhoniylar, soliqdan ozod; uchinchi toifa – dehqonlar, soliq og‘irligi; ikkalasi General shtatlarda.")
t.MAPMATCH(FR, ['Parij', 'Avinon', 'Normandiya', 'Navarra'],
           ["1302-yilda General shtatlar chaqirilgan poytaxt", "1309–1377-yillarda papalar qarorgohi bo‘lgan shahar", "Filipp II Avgust inglizlardan qo‘shib olgan, temirchilikka ixtisoslashgan hudud", "Filipp IV qo‘shib olgan, Ispaniya bilan chegaradosh hudud"],
           "1 – Parij; 2 – Avinyon; 3 – Normandiya; 4 – Navarra.")

# 2 Yuz yillik urush
t = Topic('y8j2', 8002); TOPICS['y8j2'] = t
t.B("Yuz yillik urush qaysi yillarda bo‘lgan?", "1337–1453-yillarda", "1302–1357-yillarda", "1415–1453-yillarda", "1453–1558-yillarda", "1337–1453-yillar.")
t.B("Urushning asosiy sababi bo‘lgan, Angliyaga qaram viloyat qaysi?", "Akvitaniya", "Normandiya", "Burgundiya", "Shampan", "Akvitaniya.")
t.B("Fransiya taxtiga da’vogarlik qilgan Angliya qiroli kim?", "Eduard III", "Genrix II", "Vilgelm I", "Ioann Saxiy", "Filipp IV ning nabirasi Eduard III.")
t.B("Fransuz huquqshunoslari Eduard III ning da’vosini qaysi qonunlar to‘plamiga asosan rad etgan?", "«Sali haqiqati»", "«Rus haqiqati»", "«Alfred haqiqati»", "«Buyuk erkinliklar xartiyasi»", "«Sali haqiqati»: ayol tomonidan avlod taxtga da’vo qila olmaydi.")
t.B("1340-yilda inglizlar nimaga erishgan?", "fransuz flotini tor-mor etib, dengizda hukmron bo‘ldi", "Parijni egalladi", "Orleanni qamal qildi", "Kaleni egalladi", "Fransuz flotini tor-mor keltirdi.")
t.B("Kresi jangi qachon bo‘lgan?", "1346-yilda", "1356-yilda", "1415-yilda", "1340-yilda", "1346-yilda.")
t.B("Inglizlarning erkin dehqonlardan iborat piyoda askarlari qanday atalgan?", "yomenlar", "jaklar", "ritsarlar", "burgundlar", "Yomenlar.")
t.B("Ingliz kamonchilari o‘qni qancha masofagacha ota olgan?", "600 qadamgacha", "200 qadamgacha", "1000 qadamgacha", "100 qadamgacha", "600 qadamgacha; 200 qadamdan ritsarni teshib o‘tgan.")
t.B("Eduard III qaysi portni 1347-yilda bosib olgan?", "Kale", "Bordo", "Ruan", "Marsel", "Kale porti.")
t.B("1356-yilgi Puatye jangida qaysi fransuz qiroli asir tushgan?", "Ioann Saxiy", "Karl V", "Karl VII", "Filipp VI", "Qirol Ioann Saxiy va o‘g‘li Filipp.")
t.B("Jakeriya qo‘zg‘oloni qachon boshlangan?", "1358-yilda", "1356-yilda", "1360-yilda", "1429-yilda", "1358-yil Bove viloyatida.")
t.B("Jakeriya qo‘zg‘oloniga kim boshchilik qilgan?", "Gilyom Kal", "Uot Tayler", "Janna d’Ark", "Karl V", "Dehqon Gilyom Kal.")
t.B("Qo‘zg‘olonchilar bayrog‘ida qanday tasvir bo‘lgan?", "qirol gerbi – oq nilufar", "qizil xoch", "burgut", "sher", "Qirol gerbi – oq nilufar.")
t.B("1420-yilda imzolangan, Fransiya uchun haqoratomuz shartnoma qaysi?", "Trua shartnomasi", "Verden shartnomasi", "Bretinyi sulhi", "Arras shartnomasi", "Trua shartnomasi.")
t.B("Orlean qamali necha kun davom etgan?", "ikki yuz kun", "yuz kun", "bir yil", "o‘ttiz kun", "Ikki yuz kun.")
t.B("Janna d’Ark qaysi qishloqda tug‘ilgan?", "Domremi", "Orlean", "Reyms", "Ruan", "Domremi qishlog‘ida.")
t.B("Janna d’Ark qachon gulxanda yoqilgan?", "1431-yil 30-mayda", "1429-yilda", "1430-yilda", "1456-yilda", "1431-yil 30-may kuni Ruanda.")
t.B("Angliya Kale portini qachongacha qo‘lda tutib qolgan?", "1558-yilgacha", "1453-yilgacha", "1436-yilgacha", "1600-yilgacha", "1558-yilgacha.")
t.NAT("Kresi jangida ingliz kamonchilari minglab o‘q yog‘dirdi.", "fransuzlar mag‘lub bo‘lib, uzun kamon Yevropada urush uslubini o‘zgartirdi", "fransuz ritsarlari g‘alaba qozondi", "Angliya urushdan chiqdi", "kamonchilar taqiqlandi", "Jangni yomenning uzun kamoni yutdi.")
t.NAT("1356-yilda Puatye jangida fransuzlar tor-mor etildi.", "Fransiyaning g‘arbiy va shimoliy qismi inglizlarga o‘tib, toifalar ziddiyati keskinlashdi", "Fransiya Angliyani bosib oldi", "Yuz yillik urush tugadi", "Ioann Saxiy taxtini mustahkamladi", "Siyosiy tanglik yuzaga keldi.")
t.NAT("1429-yilda Orlean qamaldan ozod qilindi.", "Yuz yillik urushda tub burilish yasaldi", "inglizlar Parijni egalladi", "Janna d’Ark qatl etildi", "Trua shartnomasi imzolandi", "Urush oqimi Fransiya foydasiga o‘zgardi.")
t.NAT("1453-yilda inglizlar Bordoda so‘zsiz taslim bo‘ldi.", "Yuz yillik urush tugab, Fransiya barcha hududlarini qaytarib oldi (Kaledan tashqari)", "Angliya Fransiyani egalladi", "urush yana 100 yil davom etdi", "Fransiya Akvitaniyani yo‘qotdi", "Markazlashgan fransuz davlati qaror topdi.")
t.TF("Janna d’Ark 1456-yilda oqlangan.", True, "To‘g‘ri: sud qarori noqonuniy deb topilgan.")
t.TF("Karl VII Janna d’Arkni asirlikdan qutqarish uchun katta to‘lov to‘lagan.", False, "Noto‘g‘ri: uni qutqarishga harakat ham qilmagan.")
t.TF4([("Jakeriyada 100 mingdan ortiq dehqon ishtirok etgan.", True), ("Karl V 1360-yilda inglizlar bilan sulh imzolagan.", True),
       ("1415-yilda Azenkur jangida fransuzlar g‘alaba qozongan.", False), ("Karl VII Reyms shahrida taxtga o‘tirgan.", True)],
      "3-noto‘g‘ri: Azenkurda fransuzlar qaqshatqich mag‘lubiyatga uchragan.")
t.MUL([("Flandriya ingliz jun xomashyosisiz ish ko‘ra olmasdi.", True),
       ("Janna d’Arkni burgundlar inglizlarga sotgan.", True),
       ("Karl VII 1456-yilda Parijga kirib kelgan.", False)],
      "III noto‘g‘ri: Karl VII 1436-yilda Parijga kirib kelgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Kresi jangi", "Puatye jangi", "Jakeriya", "Azenkur jangi", "Trua shartnomasi", "Orlean ozod qilindi", "Urushning tugashi"],
      "1346 → 1356 → 1358 → 1415 → 1420 → 1429 → 1453.")
t.MATCH("Shaxslarni ularga oid ma’lumot bilan moslashtiring.", ["Eduard III", "Ioann Saxiy", "Gilyom Kal", "Janna d’Ark"],
        ["Fransiya taxtiga da’vogar ingliz qiroli", "Puatye jangida asir tushgan fransuz qiroli", "Jakeriya rahbari", "«Orlean qizi»", "Trua shartnomasini imzolagan"], 'abcd',
        "Eduard III – da’vogar; Ioann Saxiy – asir; Gilyom Kal – Jakeriya; Janna d’Ark – Orlean qizi.")
t.VENN("Kresi jangi", "Orlean qamali",
       [("1346-yilda bo‘lgan", 1), ("ingliz kamonchilari g‘alabasi", 1),
        ("1429-yilda ozod qilingan", 2), ("Janna d’Ark boshchilik qilgan", 2),
        ("Yuz yillik urush voqeasi", 3)],
       "Kresi – 1346, kamonchilar; Orlean – 1429, Janna d’Ark; ikkalasi Yuz yillik urush voqeasi.")
t.MAPMATCH(FR, ['Kresi', 'Orlean', 'Ruan', 'Bordo'],
           ["1346-yilda ingliz kamonchilari g‘alaba qozongan joy", "1429-yilda Janna d’Ark ozod qilgan shahar", "1431-yilda Janna d’Ark gulxanda yoqilgan shahar", "1453-yilda inglizlar so‘zsiz taslim bo‘lgan shahar"],
           "1 – Kresi; 2 – Orlean; 3 – Ruan; 4 – Bordo.")

# 3 Fransiyani birlashtirishning tugallanishi
t = Topic('y8j3', 8003); TOPICS['y8j3'] = t
t.B("Yuz yillik urushdan so‘ng Fransiya shimolidan janubga nimalar keltirilgan?", "surp, jun, temir va tuz", "zaytun moyi va vino", "ipak va chinni", "ziravorlar", "Shimoldan – surp, jun, temir, tuz; janubdan – zaytun moyi, vino.")
t.B("Frank-Burgund urushlari qaysi yillarda bo‘lgan?", "1471–1475-yillarda", "1461–1483-yillarda", "1337–1453-yillarda", "1453–1461-yillarda", "1471–1475-yillar.")
t.B("Lyudovik XI qaysi yillarda hukmronlik qilgan?", "1461–1483-yillarda", "1422–1461-yillarda", "1285–1314-yillarda", "1471–1475-yillarda", "1461–1483-yillar.")
t.B("Lyudovik XI ning asosiy raqibi – Burgundiya gersogi kim edi?", "Karl Jasur", "Karl VII", "Filipp IV", "Gugo Kapet", "Burgundiya gersogi Karl Jasur.")
t.B("Lyudovik XI ga qarshi zodagonlar ittifoqi qanday atalgan?", "«Jamiyat baxt-saodati»", "«Erkin merganlar»", "«Muqaddas ittifoq»", "«General shtatlar»", "«Jamiyat baxt-saodati» ittifoqi.")
t.B("«Men Fransiyani shu qadar yaxshi ko‘ramanki, bitta qirol o‘rniga oltita qirol bo‘lishini xohlayman» degan kim?", "Karl Jasur", "Lyudovik XI", "Karl VII", "Janna d’Ark", "Karl Jasur.")
t.B("«Siyosat va uddaburonlikni yaxshi bilmagan kishi qirol bo‘la olmaydi» g‘oyasi bilan ish ko‘rgan qirol kim?", "Lyudovik XI", "Karl Jasur", "Filipp II", "Lyudovik VI", "Lyudovik XI.")
t.B("Lyudovik XI davrida qaysi gersoglik o‘z mustaqilligini saqlab qolgan?", "Bretan", "Burgundiya", "Normandiya", "Akvitaniya", "Birgina Bretan gersogligi.")
t.B("Fransiyani birlashtirish jarayoni qachon yakunlangan?", "XV asr oxirida", "XIV asr boshida", "XVI asr o‘rtasida", "XIII asrda", "XV asr oxiriga kelib.")
t.B("Lyudovik XI qanday qo‘shin tuzgan?", "ritsarlar va yollanma askarlardan doimiy qo‘shin", "faqat dehqon lashkari", "faqat flot", "faqat ritsarlar", "Ritsarlar va yollanma askarlardan iborat doimiy qo‘shin.")
t.B("Lyudovik XI General shtatlarni necha marta chaqirgan?", "bir marta", "har yili", "o‘n marta", "hech qachon", "Faqat bir marotaba.")
t.B("«Men hamma maslahatchilarni otimning egarida olib yuraman» deb kim aytgan?", "Lyudovik XI", "Karl Jasur", "Filipp IV", "Karl V", "Lyudovik XI.")
t.B("Italiyalik ipak to‘quvchi ustalar qaysi shaharga joylashtirilgan?", "Lion", "Parij", "Marsel", "Orlean", "Lion – shoyi ishlab chiqarish markaziga aylandi.")
t.B("Butun mamlakatning yagona hokimiyat qo‘l ostida birlashtirilishi qanday ataladi?", "markazlashgan davlat", "feodal tarqoqlik", "toifaviy monarxiya", "siyosiy parokandalik", "Markazlashgan davlat.")
t.B("Davlatning mayda mustaqil mulklarga bo‘linib ketishi nima deb ataladi?", "feodal tarqoqlik", "markazlashuv", "mutlaq monarxiya", "toifaviy monarxiya", "Feodal tarqoqlik yoki siyosiy parokandalik.")
t.NAT("Lyudovik XI Karl Jasurning qo‘shinlari va ishonchli kishilarini o‘z tarafiga og‘dirdi.", "Karl Jasur o‘ldirildi va qirol urushda to‘liq g‘alaba qozondi", "Karl Jasur Fransiya qiroli bo‘ldi", "Burgundiya mustaqil qoldi", "Lyudovik XI taxtdan voz kechdi", "Qirol raqiblaridan birin-ketin o‘ch oldi.")
t.NAT("Karl Jasur halok bo‘ldi.", "uning katta yer-mulklari qirolga o‘tdi, Marsel ham qirolga bo‘ysundirildi", "Burgundiya Angliyaga o‘tdi", "Bretan mustaqillikni yo‘qotdi", "General shtatlar hokimiyatni oldi", "Karl Jasurning mulklari qirol ixtiyoriga o‘tdi.")
t.NAT("Davlat ishlarini qirol o‘z amaldorlari orqali boshqardi.", "General shtatlarni chaqirishga ehtiyoj qolmadi", "General shtatlar har yili chaqirildi", "qirol hokimiyati zaiflashdi", "feodallar mustaqil bo‘ldi", "Lyudovik XI General shtatlarni bir marta chaqirdi.")
t.NAT("Fransiyada feodal tarqoqlikka barham berildi.", "savdogarlar butun mamlakat bo‘ylab xavfsiz savdo qila boshladi", "savdo to‘xtadi", "feodallar shaharlarni talay boshladi", "yagona pul bekor qilindi", "Xavfsiz savdo-sotiq yo‘lga qo‘yildi.")
t.TF("Fransiyada yagona pul, o‘lchov va og‘irlik birliklari joriy etilgan.", True, "To‘g‘ri.")
t.TF("Frank-Burgund urushida Lyudovik XI dastlab g‘alaba qozonib, Karl Jasurga shartlarni o‘zi qo‘ygan.", False, "Noto‘g‘ri: qirol dastlab sharmandalarcha mag‘lub bo‘lgan, sulh Karl Jasur shartlari asosida imzolangan.")
t.TF4([("Qo‘shin ta’minoti uchun yillik soliq joriy qilingan.", True), ("Gersog va graflar siyosiy mustaqilligini saqlab qolgan.", False),
       ("Mamlakatda ulkan savdo floti tashkil qilingan.", True), ("Fransiya toifaviy monarxiyadan mutlaq monarxiyaga aylangan.", True)],
      "2-noto‘g‘ri: ular mulklarini saqlagan bo‘lsa-da, siyosiy mustaqilligi yo‘q edi.")
t.MUL([("Kuchli qirol hokimiyati feodallarning qaram dehqonlar ustidan hukmronligini mustahkamlagan.", True),
       ("Lyudovik XI vorislari davrida Bretan ham qirol yer-mulklariga kiritilgan.", True),
       ("Lyudovik XI davrida General shtatlar qonun chiqaruvchi oliy organga aylangan.", False)],
      "III noto‘g‘ri: General shtatlar faqat bir marta chaqirilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Yuz yillik urush tugadi", "Lyudovik XI taxtga o‘tirdi", "Frank-Burgund urushlari boshlandi", "Lyudovik XI hukmronligi tugadi"], "1453 → 1461 → 1471 → 1483.")
t.VENN("Lyudovik XI", "Karl Jasur",
       [("Fransiya qiroli", 1), ("doimiy qo‘shin tuzgan", 1),
        ("Burgundiya gersogi", 2), ("«Jamiyat baxt-saodati» ittifoqi rahbari", 2),
        ("Frank-Burgund urushlari ishtirokchisi", 3)],
       "Lyudovik XI – qirol, doimiy qo‘shin; Karl Jasur – gersog, ittifoq rahbari; ikkalasi urush ishtirokchisi.")
t.MAPMATCH(FR, ['Burgundiya', 'Bretan', 'Lion', 'Marsel'],
           ["gersogi Karl Jasur bo‘lgan hudud", "Lyudovik XI davrida mustaqilligini saqlab qolgan gersoglik", "Italiyalik ipak ustalari joylashtirilgan shahar", "Karl Jasur halokatidan so‘ng qirolga butunlay bo‘ysundirilgan janubiy shahar"],
           "1 – Burgundiya; 2 – Bretan; 3 – Lion; 4 – Marsel.")

# 4 Angliyada markazlashgan davlat
t = Topic('y8j4', 8004); TOPICS['y8j4'] = t
t.B("«Angliya» so‘zi qanday ma’noni bildiradi?", "«angllar yeri»", "«oq qoyalar yurti»", "«orol mamlakati»", "«ritsarlar yurti»", "England – «angllar yeri».")
t.B("Nima uchun shaharliklar va dehqonlar qirolni qo‘llab-quvvatlagan?", "yuzta xo‘jayindan bitta xo‘jayinni afzal bilgan", "qirol soliqlarni bekor qilgan", "qirol ularga yer bergan", "qirol papaga bo‘ysungan", "Yuzta xo‘jayindan bitta xo‘jayinni afzal deb bilgan.")
t.B("Feodallarga hujum qilgan dehqonlarni xalq qanday atagan?", "«erkin merganlar»", "«yomenlar»", "«jaklar»", "«lordlar»", "«Erkin merganlar».")
t.B("Ingliz balladalarining mazlum xalq sevimli qahramoni kim?", "Robin Gud", "qirol Artur", "Simon de Monfor", "Richard Sheryurak", "Robin Gud.")
t.B("Genrix II ning vorislari kimlar bo‘lgan?", "Richard I Sheryurak va Ioann", "Eduard I va Eduard II", "Genrix III va Eduard", "Vilgelm I va Vilgelm II", "Richard I Sheryurak va Ioann.")
t.B("Qirol Ioann qaysi papa bilan munosabatlari buzilgan?", "Innokentiy III", "Bonifatsiy VIII", "Urban II", "Kliment V", "Kenterberi arxiyepiskopi masalasida Innokentiy III bilan.")
t.B("Qirol Ioann papa xazinasiga har yili qancha to‘lash majburiyatini olgan?", "ming funt sterling", "yuz funt sterling", "o‘n ming marka", "ming oltin", "Ming funt sterling.")
t.B("Qirolga qarshi qo‘zg‘olon qachon ko‘tarilgan?", "1215-yilda", "1265-yilda", "1295-yilda", "1343-yilda", "1215-yilda.")
t.B("«Erkinlikning buyuk xartiyasi» nechta moddadan iborat bo‘lgan?", "63 ta", "100 ta", "12 ta", "40 ta", "63 moddadan; lotin tilida yozilgan.")
t.B("Xartiyaga ko‘ra qirol kimning roziligisiz soliq yig‘a olmagan?", "Buyuk kengashning", "papaning", "Londonning", "lordlar palatasining", "Buyuk kengash roziligisiz.")
t.B("Norozilik harakatiga boshchilik qilib, qirol Genrix III ni asir olgan kim?", "Simon de Monfor", "Robin Gud", "Uot Tayler", "shahzoda Eduard", "Yirik mulkdor Simon de Monfor.")
t.B("Jahon tarixiga parlament nomi bilan kirgan majlis qachon chaqirilgan?", "1265-yilda", "1215-yilda", "1295-yilda", "1343-yilda", "1265-yilda Simon de Monfor chaqirgan.")
t.B("Parlament qachondan doimiy chaqirib turiladigan bo‘lgan?", "1295-yildan", "1265-yildan", "1297-yildan", "1343-yildan", "Eduard davrida 1295-yildan.")
t.B("Parlamentga soliqlarni tasdiqlash huquqi qachon berilgan?", "1297-yilda", "1295-yilda", "1215-yilda", "1343-yilda", "1297-yilda.")
t.B("Parlament qachon ikki palataga bo‘lingan?", "1343-yilda", "1297-yilda", "1265-yilda", "1215-yilda", "1343-yilda.")
t.B("Parlamentning yuqori palatasi qanday atalgan?", "lordlar palatasi", "umumpalata", "General shtatlar", "Buyuk kengash", "Lordlar palatasi.")
t.NAT("Papa qirol Ioanni cherkovdan quvib, Angliyada ibodatni taqiqladi.", "qirol papaning vassali ekanini tan olib, har yili ming funt sterling to‘lashga majbur bo‘ldi", "qirol papani taxtdan tushirdi", "Angliya katolik cherkovidan chiqdi", "papa Angliyaga qo‘shin yubordi", "Qirol Ioann taslim bo‘ldi.")
t.NAT("1215-yilgi qo‘zg‘olonda qirol Ioann asir olindi.", "u «Erkinlikning buyuk xartiyasi»ni imzolashga majbur bo‘ldi", "u taxtdan voz kechdi", "parlament tarqatildi", "Angliya respublikaga aylandi", "Xartiya qirol vakolatlarini chekladi.")
t.NAT("Genrix III Xartiyaga rioya qilmay, soliqlarni yanada oshirdi.", "Simon de Monfor boshchiligida norozilik harakati boshlanib, qirol asir olindi", "aholi soliqlarni xushnudlik bilan to‘ladi", "papa Genrix III ni himoya qildi", "parlament bekor qilindi", "Simon de Monfor boshqaruvni qo‘lga oldi.")
t.NAT("Angliyada toifalar o‘rtasida nizolar Fransiyadagidek keskin emas edi.", "parlamentning davlat ishlariga ta’siri General shtatlarnikidan kuchliroq bo‘ldi", "parlament General shtatlardan kuchsiz bo‘ldi", "qirol parlamentni tarqatdi", "toifalar birlashib qirolni ag‘dardi", "Quyi palata soliqlarga rozilik huquqini oldi.")
t.TF("«Erkinlikning buyuk xartiyasi» huquqiy davlat tarixidagi muhim hujjat hisoblanadi.", True, "To‘g‘ri.")
t.TF("Qirol Ioann «Erkinlikning buyuk xartiyasi» shartlarini sidqidildan bajargan.", False, "Noto‘g‘ri: u shartlarni bajarishni xohlamagan.")
t.TF4([("Ingliz shaharlarining ko‘pchiligi qirolga qarashli yerlarda joylashgan.", True), ("London aholisi qo‘zg‘olonchilarga shahar darvozasini ochib bergan.", True),
       ("Umumpalatada yepiskop va abbatlar majlis o‘tkazgan.", False), ("Shahzoda Eduard asirlikdan qochib, taxtga o‘tirgan.", True)],
      "3-noto‘g‘ri: yepiskop va abbatlar lordlar palatasida; umumpalatada ritsarlar va shaharlar vakillari bo‘lgan.")
t.MUL([("XIV asrdan parlament qonunlar chiqarish huquqini qo‘lga kiritgan.", True),
       ("Eduard davridagi parlament «namunali parlament» nomini olgan.", True),
       ("1265-yilgi majlisga har bir graflikdan beshtadan ritsar chaqirilgan.", False)],
      "III noto‘g‘ri: har bir graflikdan ikkitadan ritsar chaqirilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["«Erkinlikning buyuk xartiyasi» imzolandi", "Simon de Monfor majlis chaqirdi", "Parlament doimiy chaqiriladigan bo‘ldi", "Parlamentga soliqlarni tasdiqlash huquqi berildi", "Parlament ikki palataga bo‘lindi"],
      "1215 → 1265 → 1295 → 1297 → 1343.")
t.MATCH("Shaxslarni ularga oid ma’lumot bilan moslashtiring.", ["qirol Ioann", "Simon de Monfor", "Robin Gud", "Innokentiy III"],
        ["«Erkinlikning buyuk xartiyasi»ni imzolagan", "1265-yilda parlament chaqirgan", "balladalardagi xalq qahramoni", "qirol Ioanni cherkovdan quvgan papa", "Yuz yillik urushni boshlagan"], 'abcd',
        "Ioann – xartiya; Monfor – parlament; Robin Gud – ballada; Innokentiy III – papa.")
t.VENN("Angliya parlamenti", "Fransiya General shtatlari",
       [("1265-yilda vujudga kelgan", 1), ("ikki palatali – lordlar va umumpalata", 1),
        ("1302-yilda chaqirilgan", 2), ("uch palatali, ovozlarda tenglik yo‘q", 2),
        ("toifa vakillaridan iborat organ", 3)],
       "Parlament – 1265, ikki palata; General shtatlar – 1302, uch palata; ikkalasi toifaviy vakillik organi.")
t.MAPMATCH('europe', ['London', 'Rim', 'Fransiya'],
           ["1215-yilda aholisi qo‘zg‘olonchilarga darvozani ochgan shahar", "qirol Ioanni cherkovdan quvgan papa qarorgohi", "qirol Ioann quruqlikda yangi urushga tayyorlangan raqib davlat"],
           "1 – London; 2 – Rim; 3 – Fransiya.")
