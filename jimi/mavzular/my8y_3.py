from qlib import Topic, PLACES, REG
TOPICS = {}
EU = 'europe'

# 9 Rus knyazliklari
t = Topic('y8j9', 8009); TOPICS['y8j9'] = t
t.B("Kiyev Rusi kimning vafotidan keyin mustaqil knyazliklarga bo‘linib ketgan?", "Mstislav I", "Yaroslav Donishmand", "Vladimir Monomax", "Aleksandr Nevskiy", "Vladimir Monomaxning o‘g‘li Mstislav I vafotidan keyin.")
t.B("XII asr birinchi yarmida Kiyev Rusi nechtadan ortiq knyazlikka bo‘lingan?", "10 dan ortiq", "3 ta", "20 dan ortiq", "5 ta", "10 dan ortiq mustaqil knyazlikka.")
t.B("Shimoli-g‘arbiy o‘lkalarda qanday boshqaruv o‘rnatilgan?", "veche hal qiluvchi zodagonlar respublikasi", "mutlaq monarxiya", "teokratiya", "harbiy diktatura", "Veche hal qiluvchi rolga ega zodagonlar respublikasi.")
t.B("Novgorodda respublika boshqaruvi qachon paydo bo‘lgan?", "1136-yilda", "1147-yilda", "1263-yilda", "1478-yilda", "1136-yilda knyaz Vsevolod ag‘darilgach.")
t.B("Novgoroddagi oliy hokimiyat qanday atalgan?", "xalq vechesi", "Duma", "kortes", "seym", "Xalq vechesi.")
t.B("«Veche» so‘zi qanday ma’noni bildiradi?", "kengash", "qo‘ng‘iroq", "knyaz", "shahar", "Qadimgi slavyancha – kengash.")
t.B("Novgorod mustaqilligi qachon tugatilgan?", "1478-yilda", "1380-yilda", "1240-yilda", "1547-yilda", "1478-yilda Ivan III yurishi natijasida.")
t.B("Moskva shahriga kim asos solgan?", "Yuriy Dolgorukiy", "Ivan Kalita", "Daniil Aleksandrovich", "Dmitriy Donskoy", "1147-yilda Yuriy Dolgorukiy.")
t.B("Moskva knyazligiga kim asos solgan?", "Daniil Aleksandrovich", "Yuriy Dolgorukiy", "Ivan III", "Aleksandr Nevskiy", "1263-yilda knyaz Daniil Aleksandrovich.")
t.B("Mo‘g‘ullar Botuxon boshchiligida rus yerlariga qachon hujum qilgan?", "1237-yilda", "1240-yilda", "1227-yilda", "1380-yilda", "1237-yilda.")
t.B("Mo‘g‘ullar Kiyevni qachon egallagan?", "1240-yilda", "1237-yilda", "1242-yilda", "1263-yilda", "1240-yilda.")
t.B("1240-yilda Neva daryosi bo‘yida kim mag‘lub bo‘lgan?", "shvedlar", "Livoniya ritsarlari", "mo‘g‘ullar", "litvaliklar", "Shvedlar; knyaz Aleksandr Nevskiy deb ataldi.")
t.B("«Muz ustidagi jang» qachon bo‘lgan?", "1242-yil 5-aprelda", "1240-yilda", "1380-yilda", "1395-yilda", "1242-yil 5-aprel kuni Chud ko‘li ustida.")
t.B("1327-yilda Oltin O‘rdadan rus yerlarida soliq yig‘ish huquqini olgan knyaz kim?", "Ivan Kalita", "Dmitriy Donskoy", "Ivan III", "Aleksandr Nevskiy", "Moskva knyazi Ivan Kalita.")
t.B("Kulikovo jangi qachon bo‘lgan?", "1380-yilda", "1382-yilda", "1395-yilda", "1480-yilda", "1380-yilda Don daryosi bo‘yida.")
t.B("Kulikovo jangida rus qo‘shiniga qarshi kurashgan Oltin O‘rda tumanboshisi kim?", "Mamay", "To‘xtamishxon", "Botuxon", "Ivan Kalita", "Tumanboshi Mamay.")
t.B("Amir Temur To‘xtamishxonni qaysi jangda to‘liq yenggan?", "1395-yil Tarak daryosi bo‘yida", "1380-yil Kulikovoda", "1389-yil Kosovoda", "1242-yil Chud ko‘lida", "1395-yil Shimoliy Kavkazda Tarak daryosi bo‘yida.")
t.B("Ruslar Oltin O‘rdaga soliq to‘lashni qachon butunlay to‘xtatgan?", "1480-yilda", "1380-yilda", "1395-yilda", "1547-yilda", "1480-yilda.")
t.B("Moskva knyazi Ivan IV qachon podshoh unvonini olgan?", "1547-yilda", "1480-yilda", "1478-yilda", "1514-yilda", "1547-yilda.")
t.NAT("Mo‘g‘ullar rus yerlarini istilo qildi.", "rus knyazliklari Oltin O‘rdaga bo‘ysundirilib, har yili soliq to‘ladi", "rus knyazliklari birlashib mo‘g‘ullarni haydadi", "Kiyev mo‘g‘ullar poytaxti bo‘ldi", "Novgorod Oltin O‘rdani yengdi", "Knyazlar mo‘g‘ul hukmdoridan yorliq olgan.")
t.NAT("1380-yilda Kulikovo maydonida Moskva knyazligi g‘alaba qozondi.", "knyaz Dmitriy Donskoy deb ataldi, Moskva nufuzi oshdi", "Oltin O‘rda darhol tugatildi", "Moskva Oltin O‘rdaga qo‘shildi", "Mamay xon bo‘ldi", "Moskva nufuzi yanada oshdi.")
t.NAT("1382-yilda To‘xtamishxon rus yerlariga hujum qilib, Moskvani egalladi.", "ruslar Oltin O‘rdaga yana soliq to‘lay boshladi", "ruslar mustaqil bo‘ldi", "Oltin O‘rda parchalandi", "Moskva poytaxtlikdan mahrum bo‘ldi", "Soliq to‘lash qayta boshlandi.")
t.NAT("Amir Temur To‘xtamishxon ustidan g‘alaba qozondi.", "ruslarning mo‘g‘ullar zulmidan xalos bo‘lishi tezlashdi", "Oltin O‘rda kuchaydi", "ruslar Temurga soliq to‘ladi", "Moskva vayron bo‘ldi", "Amir Temur Yevropa xalqlariga xolis xizmat ko‘rsatdi.")
t.TF("Novgorodda pravoslav cherkovi boshlig‘i – yepiskop ham vecheda saylangan.", True, "To‘g‘ri.")
t.TF("Novgorodda knyaz shahar hokimiyati ishlariga cheksiz aralasha olgan.", False, "Noto‘g‘ri: knyaz aralashishga haqli emas edi, kelishuvni buzsa haydalgan.")
t.TF4([("Yuriy Dolgorukiy poytaxtni Rostovdan Suzdalga ko‘chirgan.", True), ("1383-yilda Moskva knyazligi Vladimir knyazligi bilan birlashgan.", True),
       ("Livoniya ritsarlari Izborsk va Pskovni egallagan.", True), ("Smolensk 1404-yildan beri doim Moskva tarkibida bo‘lgan.", False)],
      "4-noto‘g‘ri: 1404-yilda Litva egallagan, 1514-yilda Rossiya tarkibiga kirgan.")
t.MUL([("Amir Temur va To‘xtamishxon o‘rtasida uch marotaba jang bo‘lgan.", True),
       ("Ivan III davrida Moskva knyazligi Rossiya davlatiga aylangan.", True),
       ("Novgorodning veche qo‘ng‘irog‘i Kiyevga olib ketilgan.", False)],
      "III noto‘g‘ri: qo‘ng‘iroq Moskvaga olib ketilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Moskvaga asos solindi", "Mo‘g‘ullar Kiyevni egalladi", "«Muz ustidagi jang»", "Ivan Kalita soliq yig‘ish huquqini oldi", "Kulikovo jangi", "Tarak jangi", "Oltin O‘rdaga soliq to‘lash to‘xtatildi"],
      "1147 → 1240 → 1242 → 1327 → 1380 → 1395 → 1480.")
t.MATCH("Knyazlarni ularga oid ma’lumot bilan moslashtiring.", ["Aleksandr Nevskiy", "Ivan Kalita", "Dmitriy Donskoy", "Ivan III"],
        ["Neva va Chud ko‘lidagi g‘olib", "Oltin O‘rdadan soliq yig‘ish huquqini olgan", "Kulikovo jangi g‘olibi", "Novgorod mustaqilligini tugatgan", "Moskvaga asos solgan"], 'abcd',
        "Nevskiy – Neva, Chud; Kalita – soliq; Donskoy – Kulikovo; Ivan III – Novgorod.")
t.VENN("Novgorod", "Moskva knyazligi",
       [("veche boshqargan zodagonlar respublikasi", 1), ("1136-yildan respublika", 1),
        ("1263-yilda tashkil topgan", 2), ("rus yerlarini birlashtirishga boshchilik qilgan", 2),
        ("Kiyev Rusi parchalanishidan so‘ng mavjud rus o‘lkasi", 3)],
       "Novgorod – veche, 1136; Moskva – 1263, birlashtirish; ikkalasi rus o‘lkasi.")
t.MAPMATCH('rus', ['Novgorod', 'Chud ko‘li', 'Kulikovo', 'Kiyev'],
           ["1478-yilda mustaqilligi tugatilgan veche respublikasi", "1242-yilda «Muz ustidagi jang» bo‘lgan joy", "1380-yilda Mamay mag‘lub bo‘lgan maydon", "1240-yilda mo‘g‘ullar egallagan shahar"],
           "1 – Novgorod; 2 – Chud ko‘li; 3 – Kulikovo; 4 – Kiyev.")

# 10 Bolqon, Markaziy va Sharqiy Yevropa
t = Topic('y8j10', 8010); TOPICS['y8j10'] = t
t.B("Bolgariyaning Vizantiyaga qaramligi qaysi yillarda bo‘lgan?", "1018–1187-yillarda", "1187–1396-yillarda", "1331–1355-yillarda", "960–1385-yillarda", "1018–1187-yillar.")
t.B("Ikkinchi Bolgariya podshohligining birinchi hukmdori kim?", "Asen", "Asen II", "Stefan Dushan", "Ishtvan", "1187-yilda qo‘zg‘olon ko‘targan Asen.")
t.B("Qaysi hukmdor davrida Bolgariyada birinchi marta oltin pul zarb qilingan?", "Asen II", "Asen", "Simeon", "Stefan II", "Asen II davrida.")
t.B("Ikkinchi Bolgariya podshohligi qachon tugatilgan?", "1396-yilda", "1389-yilda", "1459-yilda", "1419-yilda", "1396-yilda; Usmoniylarga qaram bo‘ldi.")
t.B("Serbiyani boshqargan sulola qaysi?", "Nemanya", "Piastlar", "Arpadlar", "Anjuylar", "Nemanya sulolasi.")
t.B("Serbiya qaysi qirol davrida eng qudratli davlatga aylangan?", "Stefan Dushan", "Stefan II", "Milosh Obilich", "Murod I", "Stefan Dushan (1331–1355).")
t.B("Kosovo jangi qachon bo‘lgan?", "1389-yilda", "1396-yilda", "1459-yilda", "1415-yilda", "1389-yilda.")
t.B("Kosovo jangida turk sultoni Murod I ni kim o‘ldirgan?", "Milosh Obilich", "Stefan Dushan", "Yan Gus", "Asen", "Serb askari Milosh Obilich.")
t.B("XIII asrda Chexiya yana qanday atalgan?", "Bogemiya", "Moraviya", "Sileziya", "Pomorye", "Bogemiya.")
t.B("Indulgensiya savdosini qoralagan Praga universiteti professori kim?", "Yan Gus", "Jon Viklif", "Kazimir III", "Sigizmund", "Yan Gus.")
t.B("Yan Gus qachon gulxanda yoqilgan?", "1415-yilda", "1419-yilda", "1434-yilda", "1402-yilda", "1415-yilda Konstansada.")
t.B("Chexiya qachon Germaniya imperiyasidan ajralib, mustaqil bo‘lgan?", "1419-yilda", "1415-yilda", "1434-yilda", "1396-yilda", "1419-yilda.")
t.B("Guschilar harakati qachon bostirilgan?", "1434-yilda", "1419-yilda", "1415-yilda", "1459-yilda", "1434-yilda.")
t.B("960–1385-yillarda Polshani qaysi sulola idora qilgan?", "Piastlar", "Arpadlar", "Nemanya", "Anjuylar", "Piastlar sulolasi.")
t.B("Polshaning Boltiq dengiziga chiqish yo‘lini kim to‘sib qo‘ygan?", "Tevton ordeni", "Usmoniylar", "mo‘g‘ullar", "Litva", "Tevton ordeni Prussiya va Pomoryeni bosib olgan.")
t.B("XV asrda Polshada tashkil etilgan ikki palatali umumtoifa yig‘ini qanday atalgan?", "seym", "kortes", "veche", "parlament", "Seym.")
t.B("Vengerlar yana qanday atalgan?", "mojorlar", "chexlar", "polyaklar", "serblar", "Mojorlar.")
t.B("Vengriyaning birinchi qiroli kim?", "Ishtvan Buyuk", "Andrash II", "Layosh", "Arpad", "Arpad sulolasidan Ishtvan Buyuk (milodiy 1000-yil).")
t.B("Vengriyada «Erkinlikning buyuk xartiyasi»ga qiyoslanadigan hujjat qaysi?", "Oltin bulla", "Kumush bulla", "Huquqning yetti bo‘limi", "Sali haqiqati", "Andrash II davridagi Oltin bulla.")
t.NAT("XIV asrda Bolgariya uchta mustaqil davlatga bo‘lindi.", "1396-yilda Ikkinchi Bolgariya podshohligi tugatilib, Usmoniylarga qaram bo‘ldi", "Bolgariya kuchayib Vizantiyani egalladi", "Bolgariya Serbiyaga qo‘shildi", "Bolgariya mustaqil respublika bo‘ldi", "Turk hukmronligi XIX asr ikkinchi yarmigacha davom etdi.")
t.NAT("Yan Gus himoya yorlig‘iga qaramay qamalib, 1415-yilda yoqildi.", "Chexiyada ommaviy norozilik boshlanib, 1419-yilda Pragada qo‘zg‘olon ko‘tarildi", "Chexiya papaga bo‘ysundi", "guschilar harakati to‘xtadi", "Sigizmund qo‘zg‘olonni darhol bostirdi", "Guschilar harakati boshlandi.")
t.NAT("Tevton ordeni Prussiya va Pomoryeni bosib oldi.", "Polshaning Boltiq dengiziga chiqish yo‘li to‘sildi", "Polsha Boltiqqa chiqdi", "Polsha Tevton ordeniga qo‘shildi", "Polsha kuchaydi", "Mamlakatni birlashtirish eng muhim vazifaga aylandi.")
t.NAT("1240-yilda Vengriya Botuxon boshliq mo‘g‘ullar tomonidan ishg‘ol etildi.", "ko‘plab shahar va qishloqlar vayron qilindi", "Vengriya mo‘g‘ullarni yengdi", "Vengriya hududi kengaydi", "Arpadlar sulolasi kuchaydi", "Shahar va qishloqlar vayron bo‘ldi.")
t.TF("Yan Gus chex tili grammatikasini ishlab chiqqan.", True, "To‘g‘ri: ibodatlarni chex tilida o‘tkazishni taklif qilgan.")
t.TF("XIII–XIV asrlarda Polsha shaharlari boshqa Yevropa mamlakatlariga qaraganda ancha rivojlangan edi.", False, "Noto‘g‘ri: Polsha shaharlari hali uncha rivojlanmagan edi.")
t.TF4([("Bolgar terilaridan ishlangan oyoq kiyimlar G‘arb bozorlarida xaridorgir bo‘lgan.", True), ("1459-yilda Serbiyaning oxirgi hududi turklar tomonidan ishg‘ol etilgan.", True),
       ("Kazimir III davrida Polshada qirollik eng qudratli hokimiyatga aylangan.", True), ("1301-yilda Anjuy sulolasi barham topgan.", False)],
      "4-noto‘g‘ri: 1301-yilda Arpadlar sulolasi barham topgan, 1308-yilda Anjuylar taxtga kelgan.")
t.MUL([("1402-yilda Yan Gus chexlar orasida birinchi bo‘lib Praga universiteti rektori bo‘lgan.", True),
       ("Oltin bullaga ko‘ra harbiy ritsarlar soliqlardan ozod etilgan.", True),
       ("Vengerlar slavyan tillari guruhiga mansub.", False)],
      "III noto‘g‘ri: vengerlar ugro-fin (ural) tillari guruhiga mansub.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Ishtvan Buyuk toj kiydi", "Ikkinchi Bolgariya podshohligi tuzildi", "Mo‘g‘ullar Vengriyani ishg‘ol etdi", "Kosovo jangi", "Yan Gus yoqildi", "Pragada qo‘zg‘olon", "Guschilar harakati bostirildi"],
      "1000 → 1187 → 1240 → 1389 → 1415 → 1419 → 1434.")
t.MATCH("Hukmdor va shaxslarni mamlakati bilan moslashtiring.", ["Asen II", "Stefan Dushan", "Yan Gus", "Ishtvan Buyuk"],
        ["Bolgariya", "Serbiya", "Chexiya", "Vengriya", "Polsha"], 'abcd',
        "Asen II – Bolgariya; Stefan Dushan – Serbiya; Yan Gus – Chexiya; Ishtvan – Vengriya.")
t.VENN("Chexiya", "Vengriya",
       [("guschilar harakati", 1), ("Praga – yirik savdo markazi", 1),
        ("Oltin bulla", 2), ("birinchi qiroli Ishtvan Buyuk", 2),
        ("Markaziy Yevropa davlati", 3)],
       "Chexiya – guschilar, Praga; Vengriya – Oltin bulla, Ishtvan; ikkalasi Markaziy Yevropa davlati.")
t.MAPMATCH(EU, ['Kosovo', 'Praga', 'Konstansa', 'Krakov'],
           ["1389-yilda serblar va turklar o‘rtasida jang bo‘lgan maydon", "1419-yilda guschilar qo‘zg‘oloni boshlangan shahar", "1415-yilda Yan Gus yoqilgan shahar", "Gnezno va Poznan bilan birga Polshaning savdo markazi"],
           "1 – Kosovo; 2 – Praga; 3 – Konstansa; 4 – Krakov.")

# 11 Usmoniy turklar davlati
t = Topic('y8j11', 8011); TOPICS['y8j11'] = t
t.B("Usmon beyligining ilk hukmdori kim bo‘lgan?", "Erto‘g‘rul", "Usmon I", "O‘rxon", "Murod I", "Erto‘g‘rul; o‘g‘li Usmon davrida mustaqil bo‘ldi.")
t.B("Usmonning ajdodlari qaysi qabiladan bo‘lgan?", "o‘g‘uz", "qipchoq", "qarluq", "mo‘g‘ul", "O‘g‘uz qabilasidan; O‘rta Osiyodan kelgan.")
t.B("Erto‘g‘rul qabilasi saljuqiy sultondan ruxsat olib qayerga joylashgan?", "Eskishaharga", "Bursaga", "Nikeyaga", "Edirnaga", "Vizantiya chegarasidagi Eskishaharga.")
t.B("Usmon Vizantiyaga qarshi dastlabki muvaffaqiyatli yurishda 1291-yilda qaysi shaharchani zabt etgan?", "Melangiya", "Bursa", "Nikeya", "Nikomediya", "Melangiyani.")
t.B("Usmon qachon o‘z beyligini mustaqil davlat deb e’lon qilgan?", "1299-yilda", "1291-yilda", "1326-yilda", "1362-yilda", "1299-yilda.")
t.B("O‘rxon davrida qaysi shaharlar bosib olingan?", "Nikeya va Nikomediya", "Bursa va Melangiya", "Adrianopol va Sofiya", "Konstantinopol va Anqara", "Nikeya va Nikomediya.")
t.B("Usmoniylarda piyoda bo‘linma qanday atalgan?", "yayov", "musallam", "yanichar", "tumori", "Piyoda – yayov, otliq – musallam.")
t.B("Otliq suvoriyga beriladigan yer-mulk qanday atalgan?", "tumori", "iqto", "vaqf", "benefitsiy", "Tumori.")
t.B("Yanichar qo‘shini qachon tuzilgan?", "1365-yilda", "1299-yilda", "1389-yilda", "1453-yilda", "1365-yilda Murod I tomonidan.")
t.B("«Yanichar» so‘zi qanday ma’noni anglatadi?", "«yangi qo‘shin»", "«sultonning qo‘riqchisi»", "«otliq askar»", "«dengizchi»", "«Yangi qo‘shin».")
t.B("Yevropadagi yangi viloyat qanday nomlangan?", "Rum eli (Rumeliya)", "Anatoliya", "Garmiyon", "Edirna", "Rum eli (Rumeliya).")
t.B("Adrianopol qachon egallanib, Edirna deb nomlangan?", "1362-yilda", "1389-yilda", "1352-yilda", "1453-yilda", "1362-yilda; poytaxtga aylantirildi.")
t.B("Anqara jangi qachon bo‘lgan?", "1402-yil iyulda", "1389-yilda", "1453-yilda", "1413-yilda", "1402-yil iyulda.")
t.B("Konstantinopolni egallagan sulton kim?", "Mehmed II", "Murod II", "Mehmed I", "Boyazid", "Mehmed II (1451–1481).")
t.B("Konstantinopol qachon egallangan?", "1453-yil 29-mayda", "1402-yilda", "1362-yilda", "1389-yilda", "1453-yil 29-may kuni ikki oylik qamaldan so‘ng.")
t.B("Usmoniylar davlatida birinchi kumush tanga qachon va qayerda zarb qilingan?", "1327-yilda Bursada", "1362-yilda Edirnada", "1453-yilda Istanbulda", "1299-yilda Eskishaharda", "1327-yilda Bursada.")
t.B("Qaysi hukmdor davridan boshlab Usmoniy hukmdorlar sulton deb atala boshlagan?", "Murod I", "Usmon I", "O‘rxon", "Mehmed II", "Murod I davridan.")
t.B("Misr bosib olingach, Qohiradagi xalifa taxtni qaysi sultonga topshirgan?", "Salim I", "Mehmed II", "Murod I", "Boyazid", "Sulton Salim I ga.")
t.NAT("1389-yilda Kosovo maydonidagi jangda Murod I g‘alaba qozondi.", "turklar Bolqonning yakka xo‘jayiniga aylandi", "Serbiya mustaqil bo‘ldi", "turklar Bolqondan haydaldi", "Vizantiya kuchaydi", "Taxtga Boyazid o‘tirdi.")
t.NAT("Boyazid Amir Temurga qarshi ayirmachilarni qo‘llab-quvvatladi.", "1402-yilda Anqara jangida Boyazid yengilib, asir olindi", "Temur Usmoniylarga bo‘ysundi", "Boyazid Samarqandni egalladi", "ikki hukmdor ittifoq tuzdi", "Sohibqiron mulklarni Boyazid o‘g‘illariga bo‘lib berdi.")
t.NAT("1453-yil 29-mayda Konstantinopol egallandi.", "Sharqiy Rim imperiyasi quladi, shahar Istanbul nomi bilan poytaxtga aylandi", "Vizantiya qayta tiklandi", "Usmoniylar Bursaga qaytdi", "Konstantinopol vayron qilinib tashlandi", "Ayo Sofiya masjidga aylantirildi.")
t.NAT("Sultonlar bosib olingan yerlarni harbiylarga iqto tarzida taqsimladi.", "qishloq aholisi yangi yer egalari – turk harbiy zodagonlariga qaram bo‘lib qoldi", "dehqonlar ozod bo‘ldi", "vaqf yerlari yo‘qoldi", "soliqlar bekor qilindi", "Dehqonlar yer egalariga qaram bo‘ldi.")
t.TF("Yanicharlar Bolqon aholisining 8–16 yoshli xristian bolalaridan tashkil etilgan.", True, "To‘g‘ri.")
t.TF("Vaqf mulklari sultonlikdagi ekin yerlarining yarmidan ko‘pini tashkil qilgan.", False, "Noto‘g‘ri: uchdan bir qismini tashkil qilgan.")
t.TF4([("O‘rxon davrida ilk bor vazir lavozimi ta’sis etilgan.", True), ("Otliq qo‘shin soni 150 minggacha yetgan.", True),
       ("Turklar Yevropadagi dastlabki yurishlarini 1352–1354-yillarda boshlagan.", True), ("Mehmed I Konstantinopolni egallagan.", False)],
      "4-noto‘g‘ri: Konstantinopolni Mehmed II egallagan.")
t.MUL([("Sulton hukumat rahbari, bosh qo‘mondon va oliy qozi hisoblangan.", True),
       ("XVI asr boshida Usmoniylar hududi deyarli ikki barobar kengaygan.", True),
       ("Yanicharlar faqat jang qilgan, boshqa vazifa bajarmagan.", False)],
      "III noto‘g‘ri: ular mirshablik, xavfsizlik, o‘t o‘chirish vazifalarini ham bajargan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Melangiya zabt etildi", "Usmoniylar davlatiga asos solindi", "Bursada kumush tanga zarb qilindi", "Adrianopol egallandi", "Yanicharlar qo‘shini tuzildi", "Anqara jangi", "Konstantinopol egallandi"],
      "1291 → 1299 → 1327 → 1362 → 1365 → 1402 → 1453.")
t.MATCH("Sultonlarni ularga oid ma’lumot bilan moslashtiring.", ["Usmon I", "O‘rxon", "Murod I", "Mehmed II"],
        ["1299-yilda davlatga asos solgan", "piyoda va otliq doimiy qo‘shin tuzgan", "yanichar qo‘shinini tuzgan", "Konstantinopolni egallagan", "Anqarada asir tushgan"], 'abcd',
        "Usmon I – asos; O‘rxon – doimiy qo‘shin; Murod I – yanicharlar; Mehmed II – Konstantinopol.")
t.VENN("Boyazid", "Mehmed II",
       [("Anqara jangida asir tushgan", 1), ("Bolgariyani bo‘ysundirgan", 1),
        ("Konstantinopolni egallagan", 2), ("Istanbulni poytaxt qilgan", 2),
        ("Usmoniylar sultoni", 3)],
       "Boyazid – Anqara, Bolgariya; Mehmed II – Konstantinopol, Istanbul; ikkalasi sulton.")
t.MAPMATCH('oldasia', ['Bursa', 'Adrianopol', 'Anqara', 'Istanbul'],
           ["1327-yilda kumush tanga zarb qilingan ilk poytaxt", "1362-yilda egallanib, Adrianopol o‘rniga berilgan nom", "1402-yilda Boyazid yengilgan joy", "1453-yildan Usmoniylar poytaxti"],
           "1 – Bursa; 2 – Edirna (Adrianopol); 3 – Anqara; 4 – Istanbul.")

# 12 O‘rta asrlarda Eron
t = Topic('y8j12', 8012); TOPICS['y8j12'] = t
t.B("Xorazmshohlar Eronni qachon egallab, Xorazmga qo‘shib olgan?", "1194-yilda", "1256-yilda", "1220-yilda", "1337-yilda", "1194-yilda.")
t.B("Eronga bostirib kirgan mo‘g‘ul qo‘shiniga Chingizxonning qaysi o‘g‘li boshchilik qilgan?", "Tulu", "Jo‘ji", "Chig‘atoy", "O‘qtoy", "To‘rtinchi o‘g‘il Tulu.")
t.B("Huloku Eronni qachon to‘liq bosib olgan?", "1256-yilda", "1194-yilda", "1295-yilda", "1337-yilda", "1256-yilda 70 ming qo‘shin bilan.")
t.B("«Elxon» unvoni qanday ma’noni anglatadi?", "ulus xoni", "ulug‘ xon", "sulton", "xalifa", "Elxon – ulus xoni.")
t.B("Islohot o‘tkazgan yettinchi elxon kim?", "G‘ozonxon", "Abu Said", "Huloku", "Munke", "G‘ozonxon (1295–1304).")
t.B("G‘ozonxonning vaziri, qomusiy olim kim?", "Rashiduddin", "Nizomulmulk", "Beruniy", "Vojihiddin Mas’ud", "Rashiduddin.")
t.B("G‘ozonxon islomni qachon davlat dini deb e’lon qilgan?", "1295-yilda", "1304-yilda", "1256-yilda", "1337-yilda", "1295-yili qurultoyda.")
t.B("G‘ozonxon islohotida kumush dirham og‘irligi qancha bo‘lgan?", "2,15 gramm", "12,9 gramm", "4,25 gramm", "1 gramm", "Kumush dirham – 2,15 g, oltin dinor – 12,9 g.")
t.B("Sarbadorlar qo‘zg‘oloni qachon boshlangan?", "1337-yilda", "1353-yilda", "1381-yilda", "1295-yilda", "1337-yilda Boshtin qishlog‘ida.")
t.B("«Sarbadorlar» so‘zi qanday ma’noni anglatadi?", "boshini dorga tikkanlar", "ozodlik uchun kurashchilar", "dehqonlar ittifoqi", "qora bayroqlilar", "Boshini dorga tikkanlar.")
t.B("Sarbadorlar yetakchisi sifatida sulton unvonini olgan kim?", "Vojihiddin Mas’ud", "Hasan Buzurg", "Uzun Hasan", "Qora Yusuf", "Vojihiddin Mas’ud.")
t.B("Amir Temur Sabzavorni qachon egallagan?", "1381-yilda", "1387-yilda", "1393-yilda", "1337-yilda", "1381-yilda; Sarbadorlar davlatiga barham berdi.")
t.B("Muzaffariylar davlatining poytaxti qaysi shahar bo‘lgan?", "Sheroz", "Tabriz", "Bag‘dod", "Sabzavor", "Sheroz.")
t.B("Jaloyiriylar davlatiga kim asos solgan?", "shayx Hasan Buzurg", "Uzun Hasan", "Qora Yusuf", "Muboriziddin Muhammad", "1340-yilda shayx Hasan Buzurg.")
t.B("Jaloyiriylar davlati poytaxti qaysi shahar bo‘lgan?", "Bag‘dod", "Sheroz", "Tabriz", "Isfahon", "Bag‘dod.")
t.B("Qora qo‘yunlilar davlatiga kim asos solgan?", "Qora Yusuf", "Uzun Hasan", "Hasan Buzurg", "Iskandar", "1410-yilda Qora Yusuf.")
t.B("Oq qo‘yunlilar davlatiga kim asos solgan?", "Uzun Hasan", "Qora Yusuf", "Hasan Buzurg", "Abu Said", "Uzun Hasan (1453–1478).")
t.NAT("Mo‘g‘ullar Eronni istilo qildi.", "shaharlar va suv inshootlari vayron bo‘ldi, dehqonchilik yerlari yaylovga aylandi", "Eron iqtisodi gullab-yashnadi", "soliqlar bekor qilindi", "shaharlar kengaydi", "Aholi og‘ir soliqlarga tortildi.")
t.NAT("G‘ozonxon islomni davlat dini deb e’lon qildi.", "elxon musulmon a’yonlari tomonidan qo‘llab-quvvatlandi", "musulmonlar qo‘zg‘olon ko‘tardi", "Hulokuiylar davlati quladi", "mo‘g‘ul zodagonlari Eronni tark etdi", "Musulmon a’yonlar qo‘llab-quvvatladi.")
t.NAT("Elxon Abu Said vafot etdi, yagona hukmdor qolmadi.", "Hulokuiylar davlati Muzaffariylar, Jaloyiriylar va boshqa davlatlarga bo‘linib ketdi", "Eron birlashdi", "Temuriylar davlati quladi", "Usmoniylar Eronni egalladi", "Davlat bir necha mustaqil davlatlarga bo‘lindi.")
t.NAT("1469-yilgi jangda Uzun Hasan g‘alaba qozondi.", "temuriy sulton Abu Said halok bo‘ldi", "Uzun Hasan asir tushdi", "Qora qo‘yunlilar kuchaydi", "Temuriylar Tabrizni egalladi", "Oq qo‘yunlilarning temuriylar bilan munosabati keskinlashdi.")
t.TF("Sarbadorlar xiroj solig‘ini hosilning 1/3 qismi miqdorida belgilagan.", True, "To‘g‘ri.")
t.TF("Hulokuiylar davlatiga Hindiston va Xitoy ham kirgan.", False, "Noto‘g‘ri: Eron, Afg‘oniston, Turkmanistonning katta qismi, Kavkazorti, Iroq va Kichik Osiyoning sharqi kirgan.")
t.TF4([("G‘ozonxon pul tizimi keyinchalik Chig‘atoy ulusida ham joriy qilingan.", True), ("Vojihiddin Mas’ud dehqonlardan 12 ming kishilik qo‘shin tuzgan.", True),
       ("1435-yilda Shohrux Mirzo Qora qo‘yunlilarni tor-mor keltirgan.", True), ("Muzaffariylar davlatini Usmoniylar tugatgan.", False)],
      "4-noto‘g‘ri: 1387–1393-yillarda Amir Temur Muzaffariylar davlatini tugatgan.")
t.MUL([("Jaloyiriylar Mo‘g‘ulistondagi Onon va Kerulen bo‘yida yashagan.", True),
       ("XVI asr boshida Safaviylar Eronni yagona davlatga birlashtirgan.", True),
       ("Qora qo‘yunlilar Dajla daryosining yuqori oqimida yashagan.", False)],
      "III noto‘g‘ri: Dajlaning yuqori oqimida Oq qo‘yunlilar yashagan; Qora qo‘yunlilar Van ko‘lining sharqida.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Xorazmshohlar Eronni egalladi", "Huloku Eronni bosib oldi", "G‘ozonxon islomni davlat dini qildi", "Sarbadorlar qo‘zg‘oloni", "Jaloyiriylar davlati tuzildi", "Amir Temur Sabzavorni egalladi", "Qora qo‘yunlilar davlati tuzildi"],
      "1194 → 1256 → 1295 → 1337 → 1340 → 1381 → 1410.")
t.MATCH("Davlatlarni asoschisi bilan moslashtiring.", ["Hulokuiylar", "Muzaffariylar", "Jaloyiriylar", "Oq qo‘yunlilar"],
        ["Huloku", "Muboriziddin Muhammad", "shayx Hasan Buzurg", "Uzun Hasan", "Qora Yusuf"], 'abcd',
        "Hulokuiylar – Huloku; Muzaffariylar – Muboriziddin; Jaloyiriylar – Hasan Buzurg; Oq qo‘yunlilar – Uzun Hasan.")
t.VENN("Qora qo‘yunlilar", "Oq qo‘yunlilar",
       [("asoschisi Qora Yusuf", 1), ("1435-yilda Shohrux tor-mor keltirgan", 1),
        ("asoschisi Uzun Hasan", 2), ("1469-yilda temuriy Abu Saidni yenggan", 2),
        ("poytaxti Tabriz bo‘lgan turkman davlati", 3)],
       "Qora qo‘yunlilar – Qora Yusuf, Shohrux; Oq qo‘yunlilar – Uzun Hasan, 1469; ikkalasi Tabrizda.")
t.MAPMATCH('iranafg', ['Sabzavor', 'Sheroz', 'Tabriz', 'Bag‘dod'],
           ["1337-yilda sarbadorlar qo‘zg‘oloni boshlangan shahar yaqini", "Muzaffariylar poytaxti", "Qora va Oq qo‘yunlilar poytaxti", "Jaloyiriylar poytaxti"],
           "1 – Sabzavor; 2 – Sheroz; 3 – Tabriz; 4 – Bag‘dod.")
