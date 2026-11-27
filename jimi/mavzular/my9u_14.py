from qlib import Topic, PLACES, REG
TOPICS = {}

# 29-§ Qo‘qon xonligida kiyinish madaniyati
t = Topic('y9u29', 9029); TOPICS['y9u29'] = t
t.B("Qo‘qon xonligida kosiblar to‘qigan qaysi matolarga talab yuqori bo‘lgan?", "atlas, beqasam, shoyi, adras", "baxmal va zarbof", "movut va shatirash", "alasha", "Ipak, yarimipak atlas, beqasam, shoyi, abr, adras.")
t.B("Ayollar marosim va bayramlarda qanday ro‘mollar o‘ragan?", "zar yoki kumush ip qo‘shib to‘qilgan", "doka ro‘mol", "chit ro‘mol", "jun ro‘mol", "Zar yoki kumush ipli ro‘mollar.")
t.B("Ayollar kundalik yumushlarda qanday ro‘mol tashlab yurgan?", "doka ro‘mol", "zar ro‘mol", "kashmir ro‘mol", "ipak ro‘mol", "Doka ro‘mol.")
t.B("Quyi tabaqa oila ayollari ko‘ylakni qanday matodan kiygan?", "chit", "ipak-shoyi", "baxmal", "atlas", "Chit matolardan.")
t.B("Ko‘ylak ustidan kiyiladigan, astar qo‘shib tikilgan ayollar kiyimi qanday atalgan?", "munisak", "jelak", "nimtan", "chakmon", "Munisak (va kamzul).")
t.B("Munisaklar o‘z o‘rnini qanday kiyimga bo‘shatib bergan?", "kamzul", "to‘n", "chopon", "joma", "Torroq, kalta kamzullarga.")
t.B("Qishda va namgarchilikda ayollar kiygan yog‘och poshnali kavush qanday atalgan?", "haqqar kavush", "mahsi", "etik", "kalish", "«Haqqar kavush».")
t.B("Qo‘qon xonligida erkaklar uchun ziynat hisoblangan bosh kiyim qaysi?", "do‘ppi", "salla", "kuloh", "telpak", "Do‘ppi.")
t.B("Kigizdan tikilgan konus shaklidagi bosh kiyim qanday ataladi?", "kuloh", "araqchin", "kallapo‘sh", "buruk", "Kuloh (23–26 sm).")
t.B("Baland kulohlarni kimlar kiygan?", "darvishlar", "mullalar", "qozilar", "mudarrislar", "Darvishlar.")
t.B("XIX asrda do‘ppilar qaysi bosh kiyim o‘rnini egallay boshlagan?", "kulohlar", "sallalar", "telpaklar", "qalpoqlar", "Kulohlar o‘rnini.")
t.B("Erkaklarning mavsumiy ko‘ylagi qanday atalgan?", "yaxtak", "munisak", "kamzul", "jegde", "Yaxtak.")
t.B("Erkaklarning ustki kiyimlari qanday rangda bo‘lgan?", "sokin, nimrang yo‘l-yo‘l", "qizil va yorqin", "faqat oq", "faqat qora", "Sokin rangda, nimrang yo‘l-yo‘l.")
t.NAT("Xonlikda jun, charm, ipak va paxta mahsulotlariga talab yuqori edi.", "ularni ishlab chiqarish rivojlandi", "ular chetdan keltirildi", "ular taqiqlandi", "narxi tushdi", "Ishlab chiqarish rivojlandi.")
t.NAT("Salla matosining rangi, o‘ralishi va bezagi har xil bo‘lgan.", "salla erkakning etnik, ijtimoiy kelib chiqishi va yoshini bildirib turgan", "salla faqat bezak bo‘lgan", "salla kiyish taqiqlangan", "sallalar bir xil bo‘lgan", "Salla – ijtimoiy belgi.")
t.NAT("Munisak yenglari qulaylik uchun kaltaroq tikildi.", "vaqt o‘tishi bilan tirsakkacha kalta munisaklar paydo bo‘ldi", "munisak yo‘qoldi", "yenglar uzaytirildi", "munisak erkaklar kiyimiga aylandi", "Kalta yengli munisak.")
t.NAT("XIX asrda do‘ppilar kulohlar o‘rnini egalladi.", "sallani do‘ppi ustidan o‘rash va araqchin qo‘yish urf bo‘ldi", "salla o‘rash to‘xtadi", "kuloh yana urfga kirdi", "telpak urf bo‘ldi", "Do‘ppi ustidan salla urf bo‘ldi.")
t.TF("Xonlikda to‘qilgan chit va bo‘z matolar qo‘shni hududlar ehtiyojini ham qondirgan.", True, "To‘g‘ri.")
t.TF("Pastroq kulohlarni darvishlar kiygan.", False, "Noto‘g‘ri: pastroqlarini mulla, qozi, ulamo, mudarrislar kiygan.")
t.TF4([("Farg‘ona, Chust, Toshkent, Namangan do‘ppilari o‘ziga xos bo‘lgan.", True), ("Kamzullar beqasam, adras, baxmal, duxoba matolardan tikilgan.", True),
       ("Erkaklar ustki kiyimlari oldi yopiq qilib tikilgan.", False), ("Ayollar mahsi va kavush kiygan.", True)],
      "3-noto‘g‘ri: to‘n, joma, chakmon va boshqalar oldi ochiq tikilgan.")
t.MUL([("Libos ansambliga bosh kiyim, poyabzal va zargarlik buyumlari kirgan.", True),
       ("Qishki munisaklar paxta solib qavilgan.", True),
       ("Ayollar kiyinish madaniyatida bosh kiyim ahamiyatsiz bo‘lgan.", False)],
      "III noto‘g‘ri: bosh kiyim muhim o‘rin tutgan.")
t.CHR("Ayollar ustki kiyimlarining o‘zgarishini tartiblang.", ["uzun yengli munisak", "yengi kaltaroq munisak", "tirsakkacha kalta munisak", "torroq va kalta kamzul"],
      "Munisak → kalta yengli → tirsakkacha → kamzul.")
t.MATCH("Bosh kiyimlarni izohi bilan moslashtiring.", ["kuloh", "do‘ppi", "doka ro‘mol", "zar ro‘mol"],
        ["kigizdan konus shaklida", "erkaklar ziynati, XIX asrda keng tarqalgan", "kundalik yumushlarda", "marosim va bayramlarda", "qishda yog‘ochdan"], 'abcd',
        "Kuloh – kigiz konus; do‘ppi – ziynat; doka – kundalik; zar – bayram.")
t.VENN("Ayollar kiyimi", "Erkaklar kiyimi",
       [("munisak va kamzul", 1), ("haqqar kavush", 1),
        ("yaxtak va to‘n", 2), ("kuloh va salla", 2),
        ("do‘ppi", 3)],
       "Ayollar – munisak, haqqar kavush; erkaklar – yaxtak, salla; umumiy – do‘ppi.")
t.MAPN('fargona', ['Chust', 'Qo‘qon', 'O‘sh', 'Xo‘jand'], "Do‘ppilari o‘ziga xosligi bilan ajralib turgan, darslikda Farg‘ona, Toshkent, Namangan bilan birga tilga olingan shahar xaritada qaysi raqamda?",
       "Chust.")

# 30-§ Ichki va tashqi savdo. Soliq tizimi
t = Topic('y9u30', 9030); TOPICS['y9u30'] = t
t.B("Qo‘qon xonligining yirik iqtisodiy markazi qaysi shahar edi?", "Qo‘qon", "Toshkent", "Marg‘ilon", "Xo‘jand", "Qo‘qon.")
t.B("Toshkentdan Farg‘ona vodiysiga har yili nechtadan ortiq tuyada g‘alla va metall keltirilgan?", "10 mingdan", "1 mingdan", "100 mingdan", "500 dan", "10 mingdan ortiq tuyada.")
t.B("Qaysi xon davridan Xitoy mollarini Turonga yo‘naltirishda vodiylik savdogarlar vositachilikni qo‘lga olgan?", "Erdonaxon", "Olimxon", "Umarxon", "Xudoyorxon", "Erdonaxon hukmronligidan.")
t.B("Xitoy choyi savdosini o‘z nazoratiga olgan xon kim?", "Muhammad Alixon", "Olimxon", "Erdonaxon", "Sheralixon", "Muhammad Alixon.")
t.B("Farg‘onalik savdogarlar Buxoroga yiliga necha tuyada ipak jo‘natgan?", "1000 tuyada", "100 tuyada", "10 ming tuyada", "50 tuyada", "1000 tuyada (12 ming pud).")
t.B("1860-yilda 1 pud ipak necha oltin tanga turgan?", "22", "197", "12", "50", "22 oltin tanga (197 rubl).")
t.B("Turonda qog‘oz asosan qaysi shaharlarda ishlab chiqarilgan?", "Samarqand va Qo‘qon", "Buxoro va Xiva", "Toshkent va Xo‘jand", "Marg‘ilon va Andijon", "Samarqand va Qo‘qon.")
t.B("Qo‘qon savdogarlari Buxoroga qaysi navli qog‘ozni keltirgan?", "«Ishtarxoniy»", "«Abrisham»", "«Chilla»", "«Sultoniy»", "«Ishtarxoniy».")
t.B("Hindistonda juda mashhur bo‘lgan Qo‘qon ipagi navi qaysi?", "«Chilla»", "«Ishtarxoniy»", "«Abrisham»", "«Banoras»", "«Chilla».")
t.B("Hindistondan Qo‘qonga keltirilgan mato qaysi?", "banoras kimxobi", "chit", "bo‘z", "adras", "Banoras kimxobi, kashmir ro‘mollari.")
t.B("1813-yilgi Qo‘qon–Xitoy shartnomasiga ko‘ra Qo‘qon xoni qanday huquq olgan?", "Koshg‘arda savdogarlardan boj yig‘ish", "Pekinda savdo qilish", "Xitoy qo‘shinini olish", "choyni bojsiz olish", "Koshg‘arda boj yig‘ish huquqi.")
t.B("Qo‘qon xonligida davlat g‘aznasiga tushadigan asosiy soliqlar qaysilar?", "xiroj, tanobona, zakot", "salg‘ut, ushur", "tog‘ar, oshlig‘", "ixrojot", "Xiroj, tanobona, zakot.")
t.B("1/10 miqdorida undirilgan soliq qanday atalgan?", "ushr", "xiroj", "zakot", "tanobona", "Ushr.")
t.B("Xiroj hosilning qancha miqdorida undirilgan?", "1/3 va 1/5", "1/40", "1/10", "1/2", "1/3 va 1/5 miqdorida.")
t.B("Tanobona solig‘i qaysi yerlardan olingan?", "mevali bog‘lar va polizlardan", "g‘alla dalalaridan", "yaylovlardan", "vaqf yerlaridan", "Bog‘ va polizlardan, pul hisobida.")
t.B("Zakot mol-mulkning necha foizini tashkil etgan?", "2,5%", "10%", "20%", "33%", "1/40 – 2,5%.")
t.B("Viloyatda soliq yig‘uvchilarni nazorat qilgan amaldor kim?", "sarkor", "mingboshi", "qozi", "shig‘ovul", "Sarkor (mirzaboshi).")
t.NAT("Farg‘ona ipagi Turon bozorlaridagi ehtiyojni ta’minlay olmadi.", "ehtiyojni qondirish uchun Xitoydan katta hajmda ipak keltirildi", "ipak savdosi taqiqlandi", "ipak narxi tushdi", "Buxoro ipak ishlab chiqarishni to‘xtatdi", "Xitoy ipagi keltirildi.")
t.NAT("Qo‘qon xonligi Koshg‘ardagi xalqaro savdoni to‘liq nazorat qildi.", "vodiylik savdogarlar Xitoy mollarini Turonga yo‘naltirishda vositachiga aylandi", "Xitoy savdosi to‘xtadi", "Koshg‘ar Qo‘qonni bosib oldi", "choy savdosi yo‘qoldi", "Qo‘qon vositachiga aylandi.")
t.NAT("Soliqlarning asosiy qismi viloyatlarda to‘planib, xazinaga yuborildi.", "xonlik soliqchiligi mahalliy boshqaruv tizimi bilan chambarchas bog‘liq bo‘ldi", "soliqlar markazda yig‘ildi", "viloyatlar soliqdan ozod bo‘ldi", "soliq daftarlari yuritilmadi", "Soliq – mahalliy boshqaruv bilan bog‘liq.")
t.NAT("Hukmdorlar ichki savdoni qo‘llab-quvvatladi.", "yangi bozorlar, savdo majmualari, karvonsaroylar qurildi", "bozorlar yopildi", "savdogarlar haydaldi", "faqat tashqi savdo qoldi", "Savdo infratuzilmasi kengaydi.")
t.TF("Davlat hujjatlari va chet ellarga maktublar Samarqand va Qo‘qon qog‘oziga yozilgan.", True, "To‘g‘ri.")
t.TF("Tanobona solig‘i xiroj kabi tovar shaklida undirilgan.", False, "Noto‘g‘ri: tanobona pul hisobida undirilgan.")
t.TF4([("Qo‘qondan Toshkentga paxta, xom ipak, Koshg‘ar va Xitoy mollari keltirilgan.", True), ("Xitoydan choy, chinni, kumush yombi, mushk keltirilgan.", True),
       ("XIX asrda Turon bozorlarida xitoy qog‘ozi sotilmagan.", False), ("Qo‘qondan Afg‘onistonga echki momig‘i jo‘natilgan.", True)],
      "3-noto‘g‘ri: XIX asrda xitoy qog‘ozi ham sotilgan.")
t.MUL([("Muhammad Alixon saroyi omborlarida katta miqdorda xitoy choyi saqlangan.", True),
       ("Soliq tizimida ariq oqsoqoli, mirob, amin va oqsoqollar yordam bergan.", True),
       ("Zakot faqat ruhoniylardan olingan.", False)],
      "III noto‘g‘ri: har bir musulmon zakot to‘lagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["vodiylik savdogarlar Xitoy mollari vositachiligini qo‘lga oldi", "Qo‘qon–Xitoy shartnomasi imzolandi", "Pekin bilan Koshg‘ar savdosi kelishuvi", "1 pud ipak narxi 22 oltin tanga bo‘ldi"],
      "XVIII asr o‘rtasi → 1813 → 1831 → 1860.")
t.MATCH("Soliqlarni miqdori yoki shakli bilan moslashtiring.", ["xiroj", "ushr", "tanobona", "zakot"],
        ["hosilning 1/3–1/5 qismi", "hosilning 1/10 qismi", "bog‘ va polizdan pul hisobida", "mol-mulkning 1/40 qismi", "ot-tuyalar uchun yem"], 'abcd',
        "Xiroj – 1/3–1/5; ushr – 1/10; tanobona – pul; zakot – 1/40.")
t.VENN("Qo‘qondan Hindistonga", "Hindistondan Qo‘qonga",
       [("xom ipak, «Chilla» navi", 1), ("echki momig‘i", 1),
        ("kashmir ro‘mollari", 2), ("murch-ziravorlar", 2),
        ("Qo‘qon–Hindiston savdosi mahsuloti", 3)],
       "Qo‘qondan – ipak, momiq; Hindistondan – ro‘mol, ziravor; ikkalasi savdo mahsuloti.")
t.MAPMATCH('ca', ['Qashqar', 'Toshkent', 'Buxoro', 'Qo‘qon'],
           ["1813-yilgi shartnomaga ko‘ra Qo‘qon xoni boj yig‘ish huquqini olgan shahar", "har yili 10 ming tuyada g‘alla va metall jo‘natilgan shahar", "farg‘onaliklar yiliga 1000 tuyada ipak yuborgan shahar", "xonlikning yirik iqtisodiy markazi"],
           "1 – Koshg‘ar; 2 – Toshkent; 3 – Buxoro; 4 – Qo‘qon.")

# 31-§ Qo‘qon xonligida ta’lim va madaniyat
t = Topic('y9u31', 9031); TOPICS['y9u31'] = t
t.B("XIX asr o‘rtalarida xonlikda jami nechtadan ortiq madrasa faoliyat ko‘rsatgan?", "350 dan", "35 dan", "1000 dan", "80 dan", "350 dan ortiq.")
t.B("Qo‘qon xonligida ta’lim tizimi nechta an’anaviy bosqichdan iborat bo‘lgan?", "ikki – maktab va madrasa", "uch", "to‘rt", "bir", "Maktab va madrasa.")
t.B("Quyi maktab necha yil davom etgan?", "ikki-besh yil", "sakkiz yil", "bir yil", "o‘n yil", "2–5 yil.")
t.B("Quyi maktab nechta o‘quvchini qamrab olgan?", "10 dan 30 gacha", "100 dan ortiq", "2–3 ta", "50–60 ta", "10–30 nafar.")
t.B("Qiz bolalarga kim dars bergan?", "otinoyilar", "mudarrislar", "domlalar", "qozilar", "Otinoyilar.")
t.B("Qo‘qondagi mashhur madrasalardan biri qaysi?", "Norbo‘tabiy", "Muslihiddin", "Sayidahmadxo‘ja", "Baroqxon", "Norbo‘tabiy, Jome, Chalpak va boshqalar.")
t.B("Xo‘janddagi mashhur madrasa qaysi?", "Muslihiddin madrasasi", "Norbo‘tabiy", "Mo‘yi Muborak", "Chalpak", "Muslihiddin madrasasi.")
t.B("Marg‘ilondagi mashhur madrasa qaysi?", "Sayidahmadxo‘ja", "Muslihiddin", "Beklarbegi", "Oliy", "Sayidahmadxo‘ja madrasasi.")
t.B("Toshkentdagi qaysi madrasalar xonlik davridan oldin qurilgan?", "Ko‘kaldosh va Baroqxon", "Beklarbegi va Mo‘yi Muborak", "Yunusxon va Eshonquli dodxoh", "Normuhammad qushbegi", "Ko‘kaldosh va Baroqxon.")
t.B("Maktab va madrasalar nima hisobidan moliyalashtirilgan?", "vaqf mulklari", "xon xazinasi", "o‘quvchilar to‘lovi", "savdogarlar", "Vaqf mulklari.")
t.B("Minglar davri tarixini tadqiq etgan tarixchi, manbashunos kim?", "Kamol qozi", "Munis", "Ogahiy", "Hofiz Tanish", "Kamol qozi.")
t.B("Minglar davrida nazm va nasrda nechtaga yaqin tarixiy asar yaratilgan?", "40 ga yaqin", "4 ta", "400 ga yaqin", "100 ga yaqin", "40 ga yaqin.")
t.B("Maktabxonalarda So‘fi Olloyor asaridan keyin qaysi asarlar o‘rganilgan?", "Sa’diyning «Bo‘ston» va «Guliston»", "«Boburnoma»", "«Shohnoma»", "«Qutadg‘u bilig»", "Sa’diy Sheroziyning «Bo‘ston» va «Guliston»i.")
t.B("BMT binosi peshtoqiga qaysi asardan misralar bitilgan?", "«Guliston»", "«Bo‘ston»", "Hofiz «Devon»i", "«Xamsa»", "Sa’diyning «Guliston»idan.")
t.B("O‘quvchilar axloqiy tarbiyasida asosiy qo‘llanma sanalgan Hofiz Sheroziyning asari qaysi?", "«Devon»", "«Guliston»", "«Bo‘ston»", "«Masnaviy»", "Hofiz Sheroziy «Devon»i.")
t.B("Hofiz Sheroziy qaysi yillarda yashagan?", "1326–1389", "1207–1273", "1441–1501", "1483–1530", "1326–1389.")
t.B("Manbadagi shoira o‘zi necha yil maktabdorlik qilganini yozgan?", "ellik bir yil", "o‘n yil", "yigirma yil", "besh yil", "51 yil, 890 ta qizning savodini chiqargan.")
t.NAT("Madrasalarda tabiiy va aniq fanlar o‘qitilgan, lekin saviyasi past edi.", "bu fanlar saviyasi dunyoning ilg‘or mamlakatlaridan ancha orqada qoldi", "Qo‘qon olimlari Yevropadan o‘zib ketdi", "aniq fanlar taqiqlandi", "madrasalar yopildi", "Ilg‘or mamlakatlardan orqada qolish.")
t.NAT("Qiz bolalar maktablarida otinoyilar dars berdi.", "ko‘plab qizlar savodli bo‘lib, ularning bir qismi shoira bo‘ldi", "qizlar o‘qitilmadi", "otinoyilar taqiqlandi", "qizlar madrasaga o‘tkazildi", "Qizlar savodxonligi oshdi.")
t.NAT("Minglar hukmronligi davrida tarixchilik o‘sib bordi.", "nazm va nasrda 40 ga yaqin tarixiy asar yaratildi", "tarix yozish taqiqlandi", "faqat diniy asarlar yozildi", "tarixchilar Buxoroga ketdi", "Tarixiy asarlar ko‘paydi.")
t.NAT("«Guliston» misralari insonlar yaxlit bir vujud ekanini ta’kidlaydi.", "bu misralar BMT binosi peshtoqiga bitilgan", "asar taqiqlangan", "misralar unutilgan", "asar faqat Qo‘qonda o‘qilgan", "BMT binosida.")
t.TF("Yuqori maktablar faqat shaharlarda va katta qishloqlarda faoliyat yuritgan.", True, "To‘g‘ri.")
t.TF("Qiz bolalar o‘g‘il bolalar bilan bir maktabda birga o‘qigan.", False, "Noto‘g‘ri: qiz bolalar maktabi alohida bo‘lgan.")
t.TF4([("Madrasada tajvid, aqida, fiqh, hadis o‘qitilgan.", True), ("Maktabxonalarda husnixat va arifmetika ham o‘qitilgan.", True),
       ("Sa’diy Sheroziy XVIII asrda yashagan.", False), ("Maktabxonalarda Alisher Navoiy she’riy to‘plamlari o‘qitilgan.", True)],
      "3-noto‘g‘ri: Sa’diy XIII asrda yashagan.")
t.MUL([("Madrasalarda meros, faroiz, tabobat ham o‘qitilgan.", True),
       ("Toshkentdagi Beklarbegi madrasasi xonlik davrida qurilgan.", True),
       ("Quyi maktablar faqat madrasalar qoshida bo‘lgan.", False)],
      "III noto‘g‘ri: quyi maktablar masjidlar qoshida bo‘lgan.")
t.CHR("Maktabxonadagi o‘qish tartibini ketma-ket joylashtiring.", ["So‘fi Olloyor asari", "Sa’diyning «Bo‘ston» va «Guliston»i", "Hofiz Sheroziy «Devon»i"],
      "So‘fi Olloyor → Sa’diy → Hofiz.")
t.MATCH("Madrasalarni shahri bilan moslashtiring.", ["Norbo‘tabiy", "Muslihiddin", "Sayidahmadxo‘ja", "Beklarbegi"],
        ["Qo‘qon", "Xo‘jand", "Marg‘ilon", "Toshkent", "Andijon"], 'abcd',
        "Norbo‘tabiy – Qo‘qon; Muslihiddin – Xo‘jand; Sayidahmadxo‘ja – Marg‘ilon; Beklarbegi – Toshkent.")
t.VENN("Maktab", "Madrasa",
       [("masjidlar qoshida, 2–5 yil", 1), ("qizlarga otinoyilar dars bergan", 1),
        ("fiqh, mantiq, falsafa o‘qitilgan", 2), ("350 dan ortiq bo‘lgan", 2),
        ("vaqf mulklari hisobidan moliyalashtirilgan", 3)],
       "Maktab – masjid qoshida, otinoyilar; madrasa – fiqh, 350 ta; ikkalasi vaqf hisobidan.")
t.MAPMATCH('fargona', ['Qo‘qon', 'Xo‘jand', 'Marg‘ilon', 'Toshkent'],
           ["Norbo‘tabiy, Jome, Chalpak madrasalari shahri", "Muslihiddin madrasasi shahri", "Sayidahmadxo‘ja madrasasi shahri", "Beklarbegi va Mo‘yi Muborak madrasalari shahri"],
           "1 – Qo‘qon; 2 – Xo‘jand; 3 – Marg‘ilon; 4 – Toshkent.")
