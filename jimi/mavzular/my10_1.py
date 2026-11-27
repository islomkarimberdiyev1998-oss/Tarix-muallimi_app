from qlib import Topic, PLACES, REG
TOPICS = {}
W = 'globe'; EU = 'europe'

# 1 Industrial sivilizatsiyaning qaror topishi
t = Topic('y10j1', 10001); TOPICS['y10j1'] = t
t.B("Sanoat to‘ntarishi qachon boshlangan?", "XVIII asrning oxirlarida", "XVI asr boshlarida", "XIX asr oxirida", "XX asr boshlarida", "Sanoat to‘ntarishi XVIII asrning oxirlarida boshlangan.")
t.B("Sanoat to‘ntarishi yo‘lidan birinchi bo‘lib qaysi mamlakat borgan?", "Angliya", "Fransiya", "AQSH", "Germaniya", "Dastlab Angliya, uning ortidan Fransiya, keyinroq AQSH, Germaniya va boshqalar.")
t.B("Industrial sivilizatsiyaning bosh qadriyatlari nimalar bo‘lgan?", "texnik taraqqiyot va inson erkinligi", "din va an’ana", "harbiy qudrat va hudud", "yer egaligi va feodal huquq", "Bosh qadriyatlari texnik taraqqiyot va inson erkinligi bo‘lgan.")
t.B("Industrial sivilizatsiya qachon va qayerda uzil-kesil qaror topgan?", "XIX asrda Yevropa va AQSHda", "XVIII asrda Osiyoda", "XX asrda Afrikada", "XVII asrda Lotin Amerikasida", "XIX asrda Yevropa va AQSHda uzil-kesil qaror topdi.")
t.B("Elektrdvigatel, elektrlampa va telefon qachon kashf etilgan?", "1870-yillarda", "1820-yillarda", "1900-yillarda", "1850-yillarda", "1870-yillari elektrdvigatel, elektrlampa, telefon, keyinroq radio kashf etildi.")
t.B("Po‘lat eritishning yangi usullarini kimlar joriy etgan?", "Pyer Marten va Henri Bessemer", "Sidney Tomas va Jeyms Uatt", "Edison va Bell", "Faradey va Maksvell", "Fransuz metallurgi Pyer Marten va ingliz ixtirochisi Henri Bessemer.")
t.B("Suyuq cho‘yanni tozalash usulini kim kashf etgan?", "Sidney Tomas", "Henri Bessemer", "Pyer Marten", "Jozef Kipling", "Ingliz metallurgi Sidney Tomas kashf etgan.")
t.B("Sidney Tomas usuli qanday imkon yaratgan?", "fosfatlarga boy temir rudalaridan foydalanish", "neftni qayta ishlash", "elektr energiyasini uzatish", "ko‘mirni gazga aylantirish", "Fosfatlarga boy temir rudalaridan foydalanish imkonini yaratdi.")
t.B("1870–1900-yillarda jahonda po‘lat ishlab chiqarish necha barobar o‘sgan?", "56 barobar", "10 barobar", "100 barobar", "5 barobar", "1870-yildan 1900-yilgacha 56 barobar o‘sdi.")
t.B("Katta mablag‘larni bir joyga to‘plash uchun nimalar tashkil qilingan?", "aksionerlik kompaniyalari", "gildiyalar", "sexlar", "jamoa xo‘jaliklari", "Aksionerlik kompaniyalari tashkil qilindi.")
t.B("Yirik banklar va sanoatchilardan tashkil topgan tor elita qatlami qanday atalgan?", "moliya oligarxiyasi", "aristokratiya", "burjuaziya", "zodagonlar", "Moliya oligarxiyasi jamiyatning tor elita qatlamiga aylandi.")
t.B("Hukumat va huquq manbalari dindan alohida bo‘lishi kerakligi haqidagi tushuncha nima?", "sekulyarlik", "ekspansiya", "oligarxiya", "absolyutizm", "Sekulyarlik – hukumat dinning har qanday turidan alohida bo‘lishi haqidagi tushuncha.")
t.B("Absolyut monarxiyalar o‘rnini nimalar egallagan?", "cheklangan (konstitutsion) monarxiyalar va respublikalar", "harbiy diktaturalar", "teokratik davlatlar", "feodal knyazliklar", "O‘rnini konstitutsion monarxiyalar va respublikalarga bo‘shatib berdi.")
t.B("Qonunchilik, ijro va sud hokimiyatlari ajratilgan davlat qanday ataladi?", "huquqiy davlat", "mustamlaka", "dominion", "imperiya", "Parlament faoliyati huquqiy davlatning shakllanishiga ko‘maklashdi.")
t.B("XX asrda ilm-fanni ishlab chiqaruvchi kuchga aylantirish jarayoni nimaga olib kelgan?", "ilmiy-texnik inqilobga", "sanoat to‘ntarishiga", "feodalizmga", "mustamlakachilikka", "XX asrda ilmiy-texnik inqilobga olib keldi.")
t.B("Industrial sivilizatsiya taxminan qancha vaqt jahon xalqlari taraqqiyotining mazmuniga aylangan?", "qariyb ikki asr", "bir asr", "besh asr", "o‘n yil", "Qariyb ikki asr mobaynida.")
t.NAT("Yevropa va Shimoliy Amerika shaharlari temiryo‘l tizimi bilan bog‘landi.", "sanoat va savdoning rivojlanishiga katta turtki berildi", "savdo to‘xtab qoldi", "yelkanli kemalar yo‘qoldi", "qishloq xo‘jaligi inqirozga uchradi", "Temiryo‘llar sanoat va savdoga katta turtki berdi.")
t.NAT("Marten va Bessemer po‘lat eritishning yangi usullarini joriy etdi.", "po‘lat ishlab chiqarish keskin oshib, tannarxi arzonlashdi", "po‘lat qimmatlashdi", "temir davri qaytdi", "metallurgiya pasaydi", "Ishlab chiqarish oshdi, tannarx arzonlashdi; po‘lat davri boshlandi.")
t.NAT("Kishilar dunyoviy ta’lim va fan yutuqlariga intildi.", "dinning inson ongiga ta’siri susaydi, ta’lim dindan ajratildi", "diniy muassasalar davlatga qo‘shildi", "ta’lim to‘xtadi", "fan rivoji to‘xtadi", "Dinning ta’siri susaydi, dunyoviy davlat, maktab va fan shakllandi.")
t.TF("Sanoatda temir davri o‘rniga po‘lat davri boshlangan.", True, "To‘g‘ri: po‘lat ishlab chiqarish 56 barobar o‘sdi.")
t.TF("Industrial davlatlar Osiyo, Afrika va Lotin Amerikasini ta’sir hududlariga bo‘lib olishdan voz kechgan.", False, "Noto‘g‘ri: ular mustamlaka imperiyalarini yaratib, bu hududlarni bo‘lib olishga intildi.")
t.MUL([("Huquqiy davlatda fuqarolarning qonun oldida tengligi prinsipi o‘rnatilgan.", True),
       ("Elektrotexnika va kimyo sanoati yangi sohalar sifatida paydo bo‘lgan.", True),
       ("Benzinda ishlaydigan ichki yonuv dvigatellari 1870-yillardan oldin yaratilgan.", False)],
      "III noto‘g‘ri: ular 1880-yillar – 1890-yillar boshlarida yaratildi.")
t.VENN("Huquqiy davlat", "Industrial texnika",
       [("hokimiyatlar bo‘linishi", 1), ("shaxs huquqi kafolati", 1),
        ("elektrlampa va telefon", 2), ("ichki yonuv dvigateli", 2),
        ("industrial sivilizatsiya mahsuli", 3)],
       "Huquqiy davlat – hokimiyatlar bo‘linishi, shaxs huquqi; texnika – lampa, telefon, dvigatel; ikkalasi industrial sivilizatsiya mahsuli.")
t.MAPMATCH(EU, ['Angliya', 'Fransiya', 'Germaniya'],
           ["sanoat to‘ntarishi yo‘lidan dastlab borgan mamlakat", "Angliya ortidan sanoat yo‘lidan borgan, Pyer Marten vatani", "AQSH bilan birga biroz keyinroq bu yo‘ldan borgan mamlakat"],
           "1 – Angliya; 2 – Fransiya; 3 – Germaniya.")

# 2 "Yanada Buyuk Britaniya" uchun
t = Topic('y10j2', 10002); TOPICS['y10j2'] = t
t.B("Angliya uzoq yillar qanday nom bilan atalgan?", "«jahon ustaxonasi»", "«Yevropa jandarmi»", "«jahon fabrikasi Germaniya»", "«quyosh chiqar mamlakat»", "Angliya «jahon ustaxonasi» degan nom oldi.")
t.B("XIX asr o‘rtalarida Angliya taraqqiyotning qaysi yo‘lini tanlagan?", "evolyutsion yo‘lni", "inqilobiy yo‘lni", "harbiy diktatura yo‘lini", "izolyatsiya yo‘lini", "Radikal kuchlar chetlatildi, Angliya evolyutsion yo‘lni tanladi.")
t.B("XIX asr 70-yillarida Angliya sanoat sur’atlarida qaysi mamlakatlardan ortda qola boshlagan?", "Germaniya va AQSHdan", "Fransiya va Rossiyadan", "Italiya va Ispaniyadan", "Yaponiya va Xitoydan", "Germaniya va AQSH kabi yosh sanoat mamlakatlaridan ortda qoldi.")
t.B("Angliya sanoati sekin rivojlanishining asosiy sababi nima edi?", "texnik qoloqlik – uskunalarning eskirib qolishi", "ishchi kuchining yetishmasligi", "xomashyoning yo‘qligi", "mustamlakalarning yo‘qligi", "Zavod va fabrikalar uskunalari eskirib qolgan edi.")
t.B("XX asr boshlariga kelib dunyoning birinchi sanoat mamlakati qaysi bo‘lgan?", "AQSH", "Angliya", "Germaniya", "Fransiya", "XX asr boshlariga kelib AQSH birinchi sanoat mamlakatiga aylandi.")
t.B("«Pax Britanica» atamasi qanday ma’noni bildiradi?", "«Britaniya dunyosi»", "«Britaniya tinchligi uchun urush»", "«Buyuk Britaniya qiroli»", "«Britaniya savdosi»", "Pax Britanica – «Britaniya dunyosi».")
t.B("Pax Britanica davri qaysi voqeadan boshlangan?", "1815-yilgi Vaterloo jangidan", "1868-yilgi saylov islohotidan", "1899-yilgi ingliz-bur urushidan", "1901-yilgi Viktoriya vafotidan", "1815-yilgi Vaterloo jangidan Birinchi jahon urushigacha.")
t.B("Birinchi jahon urushi arafasida moliya bozorida yetakchilik qilgan beshta yirik bank qayerda joylashgan?", "Londonning Siti dahasida", "Manchesterda", "Liverpulda", "Edinburgda", "Londonning markaziy dahasi – Sitida joylashgan.")
t.B("Banklar o‘z kapitallarini dunyo bo‘ylab foydali sohalarga joylashtirishi qanday atalgan?", "kapital eksporti", "moliya oligarxiyasi", "dominion", "kontributsiya", "Bu jarayon kapital eksporti deb ataldi.")
t.B("1884–1900-yillarda Britaniya imperiyasi hududi qanchaga kengaygan?", "30% ga", "10% ga", "50% ga", "ikki barobar", "Hudud 30% ga kengaydi, aholisi bir yarim marta ko‘paydi.")
t.B("Birinchi jahon urushi arafasida ingliz mustamlakalarida qancha kishi yashagan?", "400 mln", "100 mln", "40 mln", "1 mlrd", "Ingliz mustamlakalarida 400 mln kishi yashardi.")
t.B("Mustamlakalar uchun bo‘lgan urushlarning eng yirigi qaysi?", "1899–1902-yillardagi ingliz-bur urushi", "Qrim urushi", "Afyun urushi", "Yetti yillik urush", "1899–1902-yillardagi ingliz-bur urushi.")
t.B("Burlar Janubiy Afrikada qaysi respublikalarni tuzishgan?", "Transvaal va Oranj", "Kap va Natal", "Keniya va Uganda", "Rodeziya va Zambiya", "Transvaal va Oranj nomli ikki respublika.")
t.B("Burlar kimlarning avlodlari bo‘lgan?", "gollandiyalik mustamlakachilarning", "ispan konkistadorlarining", "fransuz gugenotlarining", "portugal dengizchilarining", "Burlar gollandiyalik mustamlakachilarning avlodlari edi.")
t.B("Ingliz qirolini davlat boshlig‘i deb tan oladigan, imperiya tarkibidagi davlat nima deb atalgan?", "dominion", "protektorat", "mandat", "koloniya-respublika", "Dominion (qaram yer).")
t.B("1868-yili Angliyada qanday o‘zgarish bo‘lgan?", "shaharlarda ishchilarning bir qismi saylov huquqini oldi", "lordlar palatasi tugatildi", "ayollar saylov huquqini oldi", "respublika e’lon qilindi", "1868-yili shaharlarda ishchilarning bir qismi saylov huquqiga ega bo‘ldi.")
t.B("Qirolicha Viktoriya imperiyaga necha yil hukmronlik qilgan?", "64 yil", "40 yil", "25 yil", "50 yil", "64 yil hukmronlik qilib, 1901-yili vafot etdi.")
t.B("«Ajoyib izolyatsiya» siyosatini kim tugatgan?", "Eduard VII", "qirolicha Viktoriya", "Sesil Rods", "Jon Sili", "Eduard VII bu siyosatni tugatdi.")
t.B("«Oq tanlilar yuki» she’rining muallifi kim?", "Jozef Redyard Kipling", "Charlz Dilk", "Jon Sili", "Sesil Rods", "Viktoriya davri yozuvchisi Jozef Redyard Kipling.")
t.NAT("Angliya 1902-yili Transvaal va Oranj respublikalarini bo‘ysundirdi.", "jahon jamoatchiligi qoraladi va Angliyaning xalqaro nufuzi tushib ketdi", "Angliyaning nufuzi oshdi", "burlar mustaqillikka erishdi", "Angliya mustamlakalardan voz kechdi", "Jahon jamoatchiligi qoraladi, nufuz tushdi.")
t.NAT("Germaniya va AQSH sanoatda Angliyani quvib o‘tdi, nemis tovarlari ingliz bozorlariga kirdi.", "Angliya birinchi sanoat mamlakati maqomini yo‘qotdi, Pax Britanica tugadi", "Angliya birinchi o‘ringa qaytdi", "Germaniya qashshoqlashdi", "AQSH Angliyaga qaram bo‘ldi", "Birinchi jahon urushi arafasida Pax Britanica tugadi.")
t.TF("XX asr boshlarida ham Angliya dunyoning eng boy mamlakati bo‘lib qolayotgan edi.", True, "To‘g‘ri: boshqa mamlakatlar Angliya singari yirik kapitalga ega emasdi.")
t.TF("Eduard VII davrida Angliya va Fransiya munosabatlari keskin yomonlashgan.", False, "Noto‘g‘ri: munosabatlar iliqlashdi, bu qirol siyosatining muvaffaqiyati edi.")
t.MUL([("Kanada, Yangi Zelandiya, Avstraliya dominionlar edi.", True),
       ("XX asr boshiga kelib jamoa palatasining ustuvorligi belgilab qo‘yilgan.", True),
       ("Eduard VII davri Angliya tarixida «qorong‘u davr» deb atalgan.", False)],
      "III noto‘g‘ri: Eduard VII davri «ajoyib davr» deb ataldi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Vaterloo jangi", "Shaharlarda ishchilarga saylov huquqi berildi", "Ingliz-bur urushi boshlandi", "Qirolicha Viktoriya vafot etdi", "Transvaal va Oranj bo‘ysundirildi"],
      "1815 → 1868 → 1899 → 1901 → 1902.")
t.MATCH("Shaxslarni ularga oid ma’lumotlar bilan moslashtiring.", ["Viktoriya", "Eduard VII", "Kipling", "Sesil Rods"],
        ["64 yil hukmronlik qilgan qirolicha", "«ajoyib izolyatsiya»ni tugatgan qirol", "«Oq tanlilar yuki» she’ri muallifi", "imperiya maddohlaridan biri", "Vaterloo g‘olibi"], 'abcd',
        "Viktoriya – 64 yil; Eduard VII – izolyatsiyani tugatgan; Kipling – she’r; Rods – imperiya maddohi.")
t.MAPN(W, ['Transvaal', 'Kanada', 'Avstraliya', 'London'], "Qaysi raqam bilan burlarning 1902-yilda Angliyaga bo‘ysundirilgan respublikasi belgilangan?",
       "1 – Transvaal (burlar respublikasi); 2, 3 – dominionlar: Kanada, Avstraliya; 4 – London.")

# 3 Fransiya va Germaniya
t = Topic('y10j3', 10003); TOPICS['y10j3'] = t
t.B("Fransiyada Ikkinchi imperiya qachongacha mavjud bo‘lgan?", "1870-yilgacha", "1848-yilgacha", "1875-yilgacha", "1914-yilgacha", "Ikkinchi imperiya 1870-yilgacha yashadi.")
t.B("Fransiya-Prussiya urushida qaysi imperator asir olingan?", "Napoleon III", "Vilgelm I", "Vilgelm II", "Lui XVI", "Fransuzlar taslim bo‘ldi, Napoleon III asir olindi.")
t.B("Napoleon III asir olingach, hokimiyat qanday hukumat qo‘liga o‘tgan?", "«milliy mudofaa hukumati»", "Parij kommunasi", "Direktoriya", "Milliy majlis", "O‘zlarini «milliy mudofaa hukumati» deb atagan siyosatchilar va harbiylar qo‘liga.")
t.B("Parij aholisi qachon qo‘zg‘olon boshlagan?", "1871-yil martda", "1870-yil sentabrda", "1871-yil mayda", "1875-yilda", "1871-yil martda qo‘zg‘olon boshlandi.")
t.B("Kommunani kimlar ta’sis qilgan?", "Milliy gvardiyaga birlashgan proletariat", "burjua partiyalari", "monarxistlar", "pruss armiyasi", "Milliy gvardiyaga birlashgan proletariat Kommunani ta’sis qildi.")
t.B("Parij kommunasi necha kun faoliyat ko‘rsatgan?", "72 kun", "100 kun", "30 kun", "6 oy", "72 kunlik faoliyatdan so‘ng 28-may kuni quladi.")
t.B("Parij kommunasi qachon qulagan?", "1871-yil 28-mayda", "1871-yil 18-martda", "1870-yil 4-sentabrda", "1875-yilda", "28-may kuni quladi.")
t.B("Kommuna qulashi bilan Parij qancha o‘g‘il-qizidan ayrilgan?", "100 ming", "10 ming", "1 mln", "72 ming", "Umumiy hisobda Parij 100 ming o‘g‘il-qizidan ayrildi.")
t.B("Fransiyada Uchinchi respublika qachon e’lon qilingan?", "1870-yil 4-sentabrda", "1871-yil 18-martda", "1875-yilda", "1871-yil yanvarda", "1870-yil 4-sentabrda e’lon qilindi.")
t.B("Uchinchi respublika qachongacha mavjud bo‘lgan?", "Ikkinchi jahon urushigacha", "Birinchi jahon urushigacha", "1875-yilgacha", "1900-yilgacha", "Ikkinchi jahon urushigacha mavjud bo‘ldi.")
t.B("XIX asr davomida Fransiya sanoat ishlab chiqarishi bo‘yicha nechanchi o‘rinda bo‘lgan?", "Angliyadan keyin ikkinchi", "birinchi", "to‘rtinchi", "beshinchi", "Angliyadan keyin ikkinchi o‘rinni egallab keldi.")
t.B("Vilgelm I qayerda Germaniya imperatori deb e’lon qilingan?", "Versal saroyining oynaband zalida", "Berlinda reyxstagda", "Myunxenda", "Venada", "1871-yil yanvarda Versal saroyining oynaband zalida.")
t.B("Germaniyani birlashtirishni kim uddalagan?", "Bismark", "Vilgelm II", "Napoleon III", "Gabsburglar", "Bismark mamlakatni birlashtirishni uddaladi.")
t.B("Birinchi imperiya reyxstagi konstitutsiyani qachon qabul qilgan?", "1871-yil bahorida", "1870-yil kuzida", "1875-yilda", "1890-yilda", "1871-yil bahorida.")
t.B("1913-yili Germaniya sanoat hajmi bo‘yicha jahonda nechanchi o‘ringa chiqqan?", "AQSHdan keyingi ikkinchi", "birinchi", "uchinchi", "to‘rtinchi", "1870 – to‘rtinchi, 1880 – uchinchi, 1913 – AQSHdan keyin ikkinchi.")
t.B("1910-yilga kelib Germaniya aholisining qancha qismi shaharlarda yashagan?", "2/3 qismi", "1/3 qismi", "yarmi", "1/4 qismi", "1871 – 1/3, 1910 – 2/3 qismi.")
t.B("«Yangi kurs»ni kim e’lon qilgan?", "Vilgelm II", "Vilgelm I", "Bismark", "Napoleon III", "Imperator Vilgelm II «yangi kurs»ni e’lon qildi.")
t.B("Oliy hokimiyat chiqargan, qonun kuchiga ega qaror qanday ataladi?", "dekret", "konsentratsiya", "reyxstag", "kommuna", "Dekret – qonun kuchiga ega muhim qaror.")
t.NAT("Germaniya birlashtirildi.", "yagona ichki bozor shakllandi: bojxona chegaralari yo‘qoldi, yagona pul va o‘lchov tizimi joriy qilindi", "bojxona chegaralari ko‘paydi", "sanoat pasaydi", "Germaniya mustamlakalardan voz kechdi", "Yagona ichki bozor – muvaffaqiyat siri.")
t.NAT("Germaniya mustamlakalar «adolatsiz» bo‘lingan deb hisobladi va ulush talab qildi.", "katta urushga tayyorgarlik ko‘ra boshladi", "mustamlakalardan voz kechdi", "Fransiya bilan ittifoq tuzdi", "qishloq xo‘jaligiga qaytdi", "Buni katta urushsiz hal qilib bo‘lmasdi.")
t.TF("Parij kommunasi cherkovni davlatdan ajratgan.", True, "To‘g‘ri: Kommuna doimiy armiyani, burjua sudini bekor qildi, cherkovni davlatdan ajratdi.")
t.TF("XIX asr oxirida Fransiya sanoatda AQSH va Germaniyadan o‘zib ketgan.", False, "Noto‘g‘ri: asr oxirida AQSH va Germaniyadan ham ortda qoldi.")
t.MUL([("1871–1875-yillarda Germaniyada juda ko‘plab sanoat kompaniyalari va banklar paydo bo‘lgan.", True),
       ("Fransiya banklari asr oxirida juda katta moliya kapitaliga egalik qilgan.", True),
       ("1871-yilgi konstitutsiya Bavariyaning imperiyadagi yetakchiligini mustahkamlagan.", False)],
      "III noto‘g‘ri: konstitutsiya Prussiyaning yetakchilik rolini mustahkamladi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Uchinchi respublika e’lon qilindi", "Vilgelm I Germaniya imperatori deb e’lon qilindi", "Parijda qo‘zg‘olon boshlandi", "Parij kommunasi quladi", "Fransiya konstitutsiyasi qabul qilindi"],
      "1870-yil 4-sentabr → 1871-yil yanvar → 1871-yil mart → 1871-yil 28-may → 1875.")
t.VENN("Parij kommunasi", "Germaniya imperiyasi",
       [("doimiy armiyani bekor qilgan", 1), ("72 kun faoliyat ko‘rsatgan", 1),
        ("Vilgelm I imperator deb e’lon qilingan", 2), ("Bismark birlashtirgan", 2),
        ("1871-yilda vujudga kelgan", 3)],
       "Kommuna – armiyani bekor qilish, 72 kun; imperiya – Vilgelm I, Bismark; ikkalasi 1871-yilda vujudga kelgan.")
t.MAPMATCH(EU, ['Parij', 'Prussiya', 'Angliya'],
           ["1871-yilda kommuna tuzilgan shahar", "imperatori 1871-yilda Germaniya imperatori deb e’lon qilingan davlat", "XIX asrda sanoatda Fransiyadan oldinda turgan mamlakat"],
           "1 – Parij; 2 – Prussiya; 3 – Angliya.")

# 4 Sharqiy Yevropa va Rossiya
t = Topic('y10j4', 10004); TOPICS['y10j4'] = t
t.B("XIX asr oxirida Sharqiy Yevropaga qaysi hududlar kirgan?", "Bolqon mamlakatlari, Avstriya-Vengriya va Rossiyaning bir qismi", "Fransiya va Ispaniya", "Skandinaviya mamlakatlari", "Angliya va Irlandiya", "Bolqon mamlakatlari, Avstriya-Vengriya va Rossiya imperiyalarining bir qismi.")
t.B("Bolqonda Usmoniylar hukmronligi qachon o‘rnatilgan?", "XIV–XV asrlarda", "XII asrda", "XVII asrda", "XVIII asrda", "XIV–XV asrlarda o‘rnatilgan.")
t.B("Serbiya qachon mustaqilligini e’lon qilgan?", "1878-yilda", "1867-yilda", "1908-yilda", "1912-yilda", "1878-yili Rossiya yordamiga tayanib.")
t.B("Bosniya va Gersegovina 1908-yili kim tomonidan anneksiya qilingan?", "Avstriya", "Rossiya", "Usmoniylar", "Serbiya", "1908-yili Avstriya tomonidan anneksiya qilindi.")
t.B("Avstriya-Vengriya imperiyasi qachon tashkil topgan?", "1867-yilda", "1878-yilda", "1848-yilda", "1908-yilda", "1867-yili ikki davlat kelishuvi asosida.")
t.B("Gabsburglar sulolasi qachongacha taxtda bo‘lgan?", "1918-yilgacha", "1867-yilgacha", "1908-yilgacha", "1945-yilgacha", "1918-yilgacha taxtda o‘tirdi.")
t.B("Qaysi hudud Vengriya tarkibiga kirgan?", "Xorvatiya", "Chexiya", "Galitsiya", "Moraviya", "Slovakiya, Xorvatiya va Transilvaniya Vengriya tarkibida edi.")
t.B("Qaysi hudud Avstriya tarkibiga kirgan?", "Chexiya", "Slovakiya", "Xorvatiya", "Transilvaniya", "Chexiya, Moraviya, Galitsiya va Bukovina Avstriya tarkibida edi.")
t.B("Avstriya-Vengriyada sanoat taraqqiyotiga nima to‘siq bo‘lgan?", "saqlanib qolgan feodal munosabatlar", "mustamlakalarning ko‘pligi", "dengizga chiqish yo‘qligi", "ishchilar ko‘pligi", "Saqlanib qolgan feodal munosabatlar to‘siq edi.")
t.B("Avstriya-Vengriyada iqtisodiy inqiroz qachon boshlangan?", "1912-yilda", "1905-yilda", "1867-yilda", "1918-yilda", "1912-yili boshlangan inqiroz ahvolni og‘irlashtirdi.")
t.B("Rossiyada krepostnoy huquq bekor qilingan islohotlar qachon o‘tkazilgan?", "XIX asrning 60–70-yillarida", "XIX asr boshida", "XX asr boshida", "XVIII asr oxirida", "XIX asrning 60–70-yillarida.")
t.B("Rossiyada sanoat to‘ntarishi qachon yakunlangan?", "XIX asrning 90-yillarida", "XIX asrning 60-yillarida", "1905-yilda", "1917-yilda", "90-yillarga kelib yakunlandi.")
t.B("Birinchi rus inqilobi qaysi yillarda bo‘lgan?", "1905–1907-yillarda", "1917-yilda", "1861-yilda", "1912–1914-yillarda", "1905–1907-yillarda.")
t.B("Birinchi rus inqilobi o‘z vazifalariga ko‘ra qanday inqilob bo‘lgan?", "burjua inqilobi", "sotsialistik inqilob", "milliy-ozodlik inqilobi", "diniy inqilob", "Burjua inqilobi, krepostnoylik qoldiqlarini yo‘q qilishga qaratilgan.")
t.B("Rossiyada podshoning cheklanmagan mustabid hokimiyati qanday atalgan?", "samoderjaviye", "byurokratiya", "anneksiya", "reyxstag", "Samoderjaviye.")
t.B("Boshqa davlat hududini egallab olish yoki qo‘shib olish siyosati nima deb ataladi?", "anneksiya", "kontributsiya", "mandat", "dominion", "Anneksiya.")
t.B("Qaysi biri XIX asr rus kompozitori?", "P. I. Chaykovskiy", "L. N. Tolstoy", "A. P. Chexov", "F. M. Dostoyevskiy", "Musorgskiy, Chaykovskiy, Rimskiy-Korsakov – kompozitorlar.")
t.NAT("1905–1907-yillardagi inqilob.", "samoderjaviye Davlat Kengashi va Davlat Dumasi bilan cheklandi, ish vaqti 9–10 soatga qisqartirildi", "podsho hokimiyatdan ketdi", "byurokratiya yo‘q bo‘ldi", "Rossiya respublikaga aylandi", "Samoderjaviye cheklandi, siyosiy erkinliklar berildi, ish vaqti qisqardi.")
t.NAT("Rossiya Birinchi jahon urushida ishtirok etdi.", "demokratik rivojlanish imkoniyati yo‘qqa chiqib, 70 yillik kommunistik rejimga yo‘l ochildi", "demokratiya mustahkamlandi", "samoderjaviye kuchaydi", "Rossiya imperiyasi kengaydi", "Kommunistik rejimga yo‘l ochildi.")
t.TF("Birinchi rus inqilobi 1917-yilgi fevral inqilobi uchun muqaddima bo‘lgan.", True, "To‘g‘ri: ikkinchi inqilob natijalari birinchisining davomi edi.")
t.TF("1905–1907-yillardagi inqilobdan so‘ng korrupsiya butunlay yo‘qolgan.", False, "Noto‘g‘ri: korrupsiya yanada kuchaydi, inqilob yakunlanmay qoldi.")
t.MUL([("XIX asr oxirida Avstriya-Vengriya aholisining faqat uchdan bir qismi shaharlarda yashagan.", True),
       ("XIX asr 90-yillarida Rossiya dunyoning beshta eng yirik industrial davlatlari qatoriga qo‘shilgan.", True),
       ("1867-yilgi konstitutsiyaga ko‘ra Vengriya qiroli birlashgan imperiya hukmdori bo‘lgan.", False)],
      "III noto‘g‘ri: Avstriya imperatori birlashgan imperiya hukmdori bo‘ldi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Avstriya-Vengriya tashkil topdi", "Serbiya mustaqilligini e’lon qildi", "Birinchi rus inqilobi boshlandi", "Bosniya va Gersegovina anneksiya qilindi", "Avstriya-Vengriyada iqtisodiy inqiroz boshlandi"],
      "1867 → 1878 → 1905 → 1908 → 1912.")
t.MATCH("Shaxslarni sohasi bilan moslashtiring.", ["L. N. Tolstoy", "M. P. Musorgskiy", "Gabsburglar", "A. P. Chexov"],
        ["yozuvchi", "kompozitor", "Avstriya-Vengriya sulolasi", "adib, dramaturg daho", "Serbiya qiroli"], 'abcd',
        "Tolstoy – yozuvchi; Musorgskiy – kompozitor; Gabsburglar – sulola; Chexov – adabiyot dahosi.")
t.MAPMATCH(EU, ['Serbiya', 'Bosniya va Gersegovina', 'Chexiya', 'Xorvatiya'],
           ["1878-yilda mustaqillik e’lon qilgan davlat", "1908-yilda Avstriya anneksiya qilgan viloyatlar", "Avstriya tarkibiga kirgan hudud (Moraviya bilan)", "Vengriya tarkibiga kirgan hudud (Slovakiya bilan)"],
           "1 – Serbiya; 2 – Bosniya va Gersegovina; 3 – Chexiya; 4 – Xorvatiya.")
