from qlib import Topic, PLACES, REG
TOPICS = {}

# 26-§ Minglar hukmronligi davrida siyosat
t = Topic('y9u26', 9026); TOPICS['y9u26'] = t
t.B("Farg‘onada mustaqil hokimiyatni kim o‘rnatgan?", "ming urug‘idan Shohruxbiy", "Abdurahimxon", "Erdonaxon", "Olimxon", "Shohruxbiy.")
t.B("Shohruxbiy Farg‘onada qachon mustaqil hokimiyat o‘rnatgan?", "1709-yilda", "1733-yilda", "1740-yilda", "1758-yilda", "1709-yilda.")
t.B("1733-yilda Samarqand, Jizzax va Kattaqo‘rg‘onni boshqaruviga olgan minglar hukmdori kim?", "Abdurahimxon", "Shohruxbiy", "Abdukarimxon", "Norbo‘taxon", "Abdurahimxon.")
t.B("Abdurahimxon qayerda vafot etgan?", "Xo‘jandda", "Qo‘qonda", "Samarqandda", "Andijonda", "Xo‘jandda.")
t.B("Abdukarimxon qancha muddat hukmronlik qilgan?", "qariyb 9 oy", "30 yil", "3 yil", "bir hafta", "Qariyb 9 oy.")
t.B("Minglar orasida birinchi bo‘lib xon unvonini olgan kim?", "Erdona", "Shohruxbiy", "Abdurahim", "Olimxon", "Erdona.")
t.B("Erdonaxon Xo‘jand va O‘ratepani qachon egallagan?", "1758-yilda", "1709-yilda", "1733-yilda", "1763-yilda", "1758-yilda.")
t.B("1763-yilda Erdona xon sifatida tilga olingan maktub qayerga olib borilgan?", "Xitoyga", "Rossiyaga", "Buxoroga", "Istanbulga", "Xitoyga.")
t.B("Shohruxbiy kimlarning qiziga uylanib, kuch-qudratini mustahkamlagan?", "Chodak xo‘jalarining", "mang‘itlarning", "qipchoqlarning", "qirg‘izlarning", "Chodak xo‘jalaridan birining qiziga.")
t.B("Xo‘jagon sulolasining asoschisi kim?", "Maxdumi A’zam", "Shohruxbiy", "Xo‘ja Ahror", "Bahouddin Naqshband", "Maxdumi A’zam (Xo‘ja Ahmad).")
t.B("Minglarning kelib chiqishini Boburga bog‘lovchi afsona qanday ataladi?", "«Oltin beshik»", "«Oltin taxt»", "«Oq kigiz»", "«Oltin qamchi»", "«Oltin beshik» afsonasi.")
t.B("Shohruxbiy davlati tarkibiga dastlab qaysi shaharlar kirgan?", "Namangan, Marg‘ilon, Konibodom, Isfara", "Toshkent, Turkiston", "Samarqand, Jizzax", "O‘sh, O‘zgand", "Qo‘qondan tashqari Namangan, Marg‘ilon, Konibodom, Isfara.")
t.B("Eng uzoq muddat xonlikni boshqargan Qo‘qon xoni kim?", "Norbo‘taxon", "Olimxon", "Erdonaxon", "Xudoyorxon", "Norbo‘taxon.")
t.B("Xo‘jandda minglar hokimiyatini o‘rnatish kimga nasib etgan?", "Norbo‘taxonga", "Abdurahimxonga", "Olimxonga", "Sheralixonga", "Norbo‘taxonga.")
t.B("Harbiy islohot o‘tkazib, soxta tarxon hujjatlarini tekshirtirgan xon kim?", "Olimxon", "Norbo‘taxon", "Muhammad Alixon", "Sheralixon", "Olimxon.")
t.B("1831-yilgi Pekin bilan kelishuvga ko‘ra qayerdagi xalqaro savdo Qo‘qon nazoratiga o‘tgan?", "Koshg‘ar", "Xo‘jand", "Toshkent", "Oqmasjid", "Koshg‘ardagi.")
t.B("Muhammad Alixon davrida qaysi hududlar Qo‘qonga qo‘shib olingan?", "Qorategin, Ko‘lob, Darvoz, O‘ratepa", "Samarqand, Jizzax", "Toshkent, Sayram", "Xiva, Urganch", "Qorategin, Ko‘lob, Darvoz, O‘ratepa.")
t.B("«Ibrohim Xayol» laqabi bilan tanilgan kim?", "Ibrohim parvonachi", "Musulmonqul", "Muhammadyusuf", "Mallabek", "Mang‘it Ibrohim parvonachi.")
t.B("Sheralixonni taxtga ko‘targan va mingboshi bo‘lib olgan kim?", "Talas qirg‘izlari boshlig‘i Muhammadyusuf", "Musulmonqul", "Yusuf mingboshi", "To‘raqul", "Muhammadyusuf.")
t.B("1845-yilda O‘shdagi qo‘zg‘olonni bostirishga kim yuborilgan?", "qipchoq Musulmonqul", "Sarimsoqbek", "Murod", "Mallabek", "Musulmonqul.")
t.B("Sheralixonni o‘ldirib, o‘zini xon deb e’lon qilgan kim?", "Olimxonning o‘g‘li Murod", "Musulmonqul", "Xudoyor", "Mallabek", "Murod.")
t.B("Qo‘qonda qipchoqlar hukmronligiga qachon barham berilgan?", "1852-yilda", "1845-yilda", "1853-yilda", "1842-yilda", "1852-yilda Musulmonqul o‘ldirilgan.")
t.B("Oqmasjid qachon Perovskiy tomonidan bosib olingan?", "1853-yilda", "1852-yilda", "1839-yilda", "1865-yilda", "1853-yilda.")
t.B("Oqmasjid qal’asi hokimi kim edi?", "To‘raqul (Abdu Vali)", "Abdulg‘afurbek", "Mallabek", "Sarimsoqbek", "To‘raqul (Abdu Vali).")
t.NAT("Ashtarxoniy Ubaydullaxon davrida markaziy hokimiyat o‘ta zaiflashdi.", "mustaqillik ilinjidagi siyosiy guruhlar kuchayib, 1709-yilda Farg‘ona ajralib chiqdi", "Buxoro kuchaydi", "minglar Buxoroga bo‘ysundi", "mang‘itlar Farg‘onani oldi", "Qo‘qon xonligi tashkil topdi.")
t.NAT("Shohruxbiy Chingiz yoki Afrosiyob avlodidan emas edi.", "hokimiyatni asoslash uchun «Oltin beshik» afsonasi to‘qib chiqarildi", "u taxtdan voz kechdi", "Buxoro amirini xon deb tan oldi", "Xitoy uni xon qilib tayinladi", "Afsona yaratildi.")
t.NAT("Soxta tarxon hujjatlari ko‘payib, xazina daromadi kamaydi.", "Olimxon imtiyoz hujjatlarini qayta tekshirishga farmon berdi", "barcha soliqlar bekor qilindi", "sayyidlarga yangi imtiyozlar berildi", "xazina Buxoroga topshirildi", "Hujjatlar tekshirildi.")
t.NAT("1853-yilda Oqmasjid ruslar tomonidan bosib olindi.", "Qo‘qon–Rossiya munosabatlarining keskinlashuvi boshlandi", "Qo‘qon Rossiya bilan ittifoq tuzdi", "ruslar orqaga qaytdi", "Xudoyorxon kuchaydi", "Munosabatlar keskinlashdi.")
t.TF("Erdonaxon Qo‘qon xonligini Xitoy va Buxoro bilan tengma-teng kurasha oladigan davlatga aylantirgan.", True, "To‘g‘ri.")
t.TF("Abdukarimxon jung‘orlarning vodiyga bosqinini qaytara olmagan.", False, "Noto‘g‘ri: jung‘orlar bosqinini qaytarishga muvaffaq bo‘lgan.")
t.TF4([("Nodirshoh bosqinida Samarqand, Kattaqo‘rg‘on, Jizzax dushman ixtiyoriga o‘tgan.", True), ("Erdonaxon davrida O‘sh va O‘zgand bo‘ysundirilgan.", True),
       ("Ibrohim parvonachi Qo‘qonni ikki yil boshqargan.", False), ("Qipchoqlar talabi bilan Muhammadyusuf mingboshilikdan chetlashtirilgan.", True)],
      "3-noto‘g‘ri: Ibrohim parvonachi ikki oy hukmronlik qilgan.")
t.MUL([("Musulmonqul qizini Xudoyorga berib, Murodni taxtdan ag‘dargan.", True),
       ("Musulmonqul mingboshi – bosh vazir lavozimini egallagan.", True),
       ("Xudoyorxon Musulmonquldan qutulgach, to‘liq mustaqil hukm surgan.", False)],
      "III noto‘g‘ri: Abdulg‘afurbek va Mallabek unga qarshi chiqqan, mustaqil hukm sura olmagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Shohruxbiy mustaqil hokimiyat o‘rnatdi", "Abdurahimxon Samarqandni egalladi", "Nodirshoh bosqini", "Erdona Xo‘jand va O‘ratepani egalladi", "Pekin bilan kelishuv", "Amir Nasrulla Qo‘qonni bo‘ysundirdi", "Oqmasjid bosib olindi"],
      "1709 → 1733 → 1740 → 1758 → 1831 → 1842 → 1853.")
t.MATCH("Hukmdorlarni ular davridagi voqea bilan moslashtiring.", ["Shohruxbiy", "Erdonaxon", "Olimxon", "Muhammad Alixon"],
        ["1709-yilda Farg‘onada mustaqil hokimiyat", "1758-yilda Xo‘jand va O‘ratepani egallash", "harbiy islohot va soxta hujjatlarni tekshirish", "Pekin bilan Koshg‘ar savdosi kelishuvi", "Oqmasjid himoyasi"], 'abcd',
        "Shohruxbiy – 1709; Erdona – 1758; Olimxon – islohot; Muhammad Alixon – 1831 kelishuv.")
t.VENN("Erdonaxon", "Olimxon",
       [("minglarda birinchi xon unvoni", 1), ("1758-yilda Xo‘jandni egallagan", 1),
        ("qattiq harbiy intizom joriy qilgan", 2), ("tarxon hujjatlarini tekshirtirgan", 2),
        ("Qo‘qon xonligi hukmdori", 3)],
       "Erdona – birinchi xon, Xo‘jand; Olimxon – harbiy islohot, tekshiruv; ikkalasi Qo‘qon xoni.")
t.MAPMATCH('fargona', ['Qo‘qon', 'Xo‘jand', 'O‘sh', 'Namangan'],
           ["minglar davlati poytaxti", "Abdurahimxon vafot etgan, 1758-yilda egallangan shahar", "1845-yilda qo‘zg‘olon ko‘tarilgan shahar", "Shohruxbiy davlati dastlabki tarkibidagi vodiy shimolidagi shahar"],
           "1 – Qo‘qon; 2 – Xo‘jand; 3 – O‘sh; 4 – Namangan.")

# 27-§ Qo‘qon xonligida davlat boshqaruvi
t = Topic('y9u27', 9027); TOPICS['y9u27'] = t
t.B("Qo‘qon xonligida davlat boshqaruvining oliy idorasi nima hisoblangan?", "dargoh", "devon", "qurultoy", "Oliy Kengash", "Dargoh.")
t.B("1810-yilga qadar Qo‘qonda bosh vazir vazifasini kim bajargan?", "qushbegi", "mingboshi", "devonbegi", "mehtar", "Qushbegi.")
t.B("Qaysi xon davrida bosh vazir lavozimi mingboshiga o‘zgartirilgan?", "Umarxon", "Olimxon", "Muhammad Alixon", "Norbo‘taxon", "Umarxon davrida.")
t.B("Mingboshi lavozimi egasiga qanday vakolat ham yuklatilgan?", "lashkarboshilik", "qozilik", "xazinachilik", "elchilik", "Lashkarboshilik vakolati.")
t.B("Beklarbegi unvoni qachon joriy qilingan?", "1831-yilda", "1810-yilda", "1842-yilda", "1709-yilda", "1831-yilda Muhammad Alixon tomonidan.")
t.B("Beklarbegi unvoni kimga berilgan?", "faqat Toshkent hokimiga", "barcha viloyat hokimlariga", "Xo‘jand hokimiga", "mingboshiga", "Faqat Toshkent hokimiga.")
t.B("Beklarbegi qaysi hududlar ustidan nazorat qilgan?", "Turkiston, Chimkent, Avliyoota", "Andijon, O‘sh", "Xo‘jand, O‘ratepa", "Qorategin, Ko‘lob", "Turkiston, Chimkent, Avliyoota.")
t.B("Manbaga ko‘ra Qo‘qon xonligi Xivaga nisbatan necha baravar katta bo‘lgan?", "besh baravar", "uch baravar", "to‘rt baravar", "ikki baravar", "Besh baravar.")
t.B("Moliya vazirining yordamchisi qanday atalgan?", "mehtar", "inoq", "shig‘ovul", "dasturxonchi", "Mehtar.")
t.B("Xonning xos va sirdosh mulozimi kim bo‘lgan?", "inoq", "mehtar", "sarkor", "boturboshi", "Inoq.")
t.B("Fiqh olimi lavozimi qanday atalgan?", "xojakalon", "qozikalon", "shayxulislom", "qozi askar", "Xojakalon.")
t.B("Viloyat hokimining asosiy yordamchilari kimlar bo‘lgan?", "sarkor (mirzaboshi) va boturboshi", "mehtar va inoq", "qozi va muftiy", "shig‘ovul va dasturxonchi", "Sarkor va boturboshi.")
t.B("XIX asrning 50-yillarida Qo‘qonda qancha aholi bo‘lgan?", "30 mingga yaqin", "3 ming", "100 ming", "8 ming", "30 mingga yaqin (8 ming xonadon).")
t.B("Xonlik ma’muriy tizimining eng quyi bo‘g‘ini qaysi?", "oqsoqollik", "viloyat", "sarkorlik", "beklik", "Oqsoqollik.")
t.B("Qo‘qon shahrini kim boshqargan?", "xonning o‘zi", "mingboshi", "beklarbegi", "qozikalon", "Xonning o‘zi.")
t.B("Toshkent bekligini xonlikka kim qo‘shib olgan?", "Olimxon", "Umarxon", "Erdonaxon", "Abdurahimxon", "Olimxon.")
t.B("Farg‘ona vodiysi hududi qancha bo‘lgan?", "22,2 ming km²", "80 ming km²", "300 km²", "170 ming km²", "22,2 ming km² (tog‘lar bilan 80 ming km²).")
t.NAT("Davlat siyosatida harbiy masala ustuvor bo‘ldi, xonlikning uch tomonida xavf yuzaga keldi.", "bosh vazir lavozimi mingboshiga o‘zgartirilib, unga lashkarboshilik yuklandi", "qo‘shin tarqatildi", "qushbegi kuchaydi", "Toshkent Buxoroga berildi", "Mingboshi lavozimi joriy etildi.")
t.NAT("Poytaxtdan uzoqdagi Toshkent va Qipchoq dashti hududlarini boshqarish murakkablashdi.", "1831-yilda Toshkent hokimiga beklarbegi unvoni berildi", "Toshkent mustaqil bo‘ldi", "hududlar Rossiyaga berildi", "poytaxt Toshkentga ko‘chirildi", "Beklarbegi unvoni joriy etildi.")
t.NAT("Olimxon Toshkent bekligini qo‘shib oldi, Umarxon Qipchoq dashti yerlarini qo‘shdi.", "xonlik hududi yanada kengaydi", "xonlik qisqardi", "Qo‘qon Buxoroga bo‘ysundi", "Farg‘ona ajralib chiqdi", "Hudud kengaydi.")
t.NAT("Shayboniyxon davrida ko‘chib kelgan ko‘chmanchi urug‘lar XVII asr oxiri – XVIII asr boshida o‘troqlashdi.", "xonlik aholisining asosiy qismini o‘zbeklar tashkil etdi", "aholi kamaydi", "ko‘chmanchilik kuchaydi", "urug‘lar vodiyni tark etdi", "O‘zbeklar asosiy aholi.")
t.TF("Mamlakat xazinasiga tushgan mablag‘ va sarf-xarajat devonbegi nazoratida bo‘lgan.", True, "To‘g‘ri.")
t.TF("Qo‘qon xonligida devonlar tizimi to‘liq saqlanib, kuchaygan.", False, "Noto‘g‘ri: devonlar tizimi deyarli saqlanmagan, vazifalari dargohga yuklangan.")
t.TF4([("XIX asrning 20-yillarida Qo‘qonda oltita bozor bo‘lgan.", True), ("Erdonaxon O‘sh va O‘zganni xonlik tarkibiga kiritgan.", True),
       ("Viloyatlarga hokim tayinlash mingboshi izmida bo‘lgan.", False), ("Farg‘ona vodiysiga qoraqalpoqlar ham kelib o‘rnashgan.", True)],
      "3-noto‘g‘ri: hokim tayinlash xon izmida bo‘lgan.")
t.MUL([("Qo‘qon xonligi Buxoroga nisbatan uch baravar katta bo‘lgan.", True),
       ("Shig‘ovul chet ellik elchilarni kutib olishga javobgar bo‘lgan.", True),
       ("Qozi askar oliy diniy mansab bo‘lgan.", False)],
      "III noto‘g‘ri: oliy diniy mansab – shayxulislom; qozi askar – harbiy ishlar qozisi.")
t.CHR("Xonlik hududining kengayishini tartiblang.", ["Abdurahimxon Xo‘jandni bo‘ysundirdi", "Erdonaxon O‘sh va O‘zganni qo‘shdi", "Olimxon Toshkent bekligini qo‘shdi", "Muhammad Alixon Qorategin, Ko‘lob, Darvozni bo‘ysundirdi"],
      "Abdurahimxon → Erdonaxon → Olimxon → Muhammad Alixon.")
t.MATCH("Lavozimlarni vazifasi bilan moslashtiring.", ["mingboshi", "beklarbegi", "shig‘ovul", "xojakalon"],
        ["bosh vazir va lashkarboshi", "Toshkent hokimi unvoni", "elchilarni kutib oluvchi", "fiqh olimi", "tungi qo‘riqchi"], 'abcd',
        "Mingboshi – bosh vazir; beklarbegi – Toshkent hokimi; shig‘ovul – elchilar; xojakalon – fiqh olimi.")
t.VENN("Mingboshi", "Beklarbegi",
       [("Umarxon davrida joriy etilgan", 1), ("lashkarboshilik vakolati", 1),
        ("1831-yilda joriy etilgan", 2), ("faqat Toshkent hokimiga berilgan", 2),
        ("Qo‘qon xonligidagi yangi unvon/lavozim", 3)],
       "Mingboshi – Umarxon, lashkarboshi; beklarbegi – 1831, Toshkent; ikkalasi yangilik.")
t.MAPMATCH('tshim', ['Toshkent', 'Turkiston', 'Avliyoota', 'Qo‘qon'],
           ["beklarbegi unvoni berilgan hokim shahri", "beklarbegi nazoratidagi Yassaviy maqbarasi shahri", "beklarbegi nazoratidagi eng sharqiy shahar", "xonning o‘zi boshqargan poytaxt"],
           "1 – Toshkent; 2 – Turkiston; 3 – Avliyoota; 4 – Qo‘qon.")

# 28-§ Qo‘qon xonligida ijtimoiy-iqtisodiy hayot
t = Topic('y9u28', 9028); TOPICS['y9u28'] = t
t.B("Farg‘ona vodiysida kambag‘allarning asosiy iste’mol mahsuloti va chorva ozuqasi qaysi don bo‘lgan?", "jo‘xori", "bug‘doy", "sholi", "arpa", "Jo‘xori.")
t.B("Vodiyning janubi-g‘arbidagi Xo‘jand, Konibodom, Isfara qaysi mahsulotga ixtisoslashgan?", "o‘rik", "paxta", "sholi", "uzum", "O‘rik yetishtirishga.")
t.B("Ipakchilik uchun tut daraxtlari ko‘paytirilgan hududlar qaysilar?", "So‘x, Isfara, Namangan, Asht", "Xo‘jand, Konibodom", "Qo‘qon, O‘sh", "Toshkent, Chimkent", "So‘x, Isfara, Namangan, Asht.")
t.B("Qo‘qon xonligida yerga egalikning nechta asosiy turi bo‘lgan?", "to‘rt", "ikki", "olti", "uch", "Mulk, amlok, xususiy, vaqf.")
t.B("Xonga qarashli davlat yerlari qanday atalgan?", "amlok (zamini xos)", "vaqf", "mulk", "mulki huri xolis", "Amlok.")
t.B("Amlok yerni ijaraga olgan kishi hosilning qancha qismini soliq to‘lagan?", "1/5", "1/10", "1/2", "1/40", "1/5 qismini.")
t.B("Diniy muassasalarga qarashli yerlar qanday atalgan?", "vaqf", "amlok", "mulk", "xususiy", "Vaqf yerlari.")
t.B("Olimxon davrida So‘x daryosida nechta ariq qazilgan?", "oltita", "bitta", "o‘nta", "uchta", "Oltita.")
t.B("Yangiariq arig‘i qachon qazilgan?", "1800–1803-yillarda", "1819-yilda", "1868–1871-yillarda", "1709-yilda", "1800–1803-yillarda.")
t.B("Yangiariq qaysi daryodan suv olgan?", "Norin", "So‘x", "Isfara", "Qoradaryo", "Norin daryosidan.")
t.B("1819-yilda Umarxon farmoni bilan Yangiariq uzunligi qanchaga yetkazilgan?", "120 chaqirim", "12 chaqirim", "300 chaqirim", "60 chaqirim", "120 chaqirim.")
t.B("Farg‘ona vodiysidagi eng katta sug‘orish arig‘i qaysi?", "Ulug‘nahr", "Yangiariq", "Shahrixonsoy", "Andijonsoy", "1868–1871-yillarda qurilgan Ulug‘nahr.")
t.B("Ipakchilik tufayli shoyi matolari mashhur bo‘lgan shahar qaysi?", "Marg‘ilon", "Chust", "Shahrixon", "O‘sh", "Marg‘ilon.")
t.B("Pichoqchilik qaysi shaharlarda taraqqiy etgan?", "Chust va Shahrixon", "Qo‘qon va Marg‘ilon", "Xo‘jand va O‘sh", "Andijon va Namangan", "Chust va Shahrixon.")
t.B("Qo‘qon shahrida qaysi hunarlar yuqori darajaga ko‘tarilgan?", "yog‘och o‘ymakorligi va qog‘ozgarlik", "kemasozlik", "shishasozlik", "gilamdo‘zlik", "Yog‘och o‘ymakorligi va qog‘ozgarlik.")
t.B("Qo‘lyozma kitoblarni tayyorlash sohasi qanday ataladi?", "sahhoflik", "zargarlik", "miskarlik", "kashtachilik", "Sahhoflik.")
t.NAT("XIX asrda xonlikda paxtachilikka katta e’tibor berildi.", "paxta ekiladigan maydonlar to‘xtovsiz kengaydi", "paxta ekish to‘xtadi", "g‘alla maydonlari kengaydi", "ipakchilik yo‘qoldi", "Paxta maydonlari kengaydi.")
t.NAT("Shahrixonsoy, Namangan yangi arig‘i, Chinobod arig‘i qazildi.", "sug‘oriladigan yer maydonlari sezilarli kengaydi", "suv tanqisligi kuchaydi", "dehqonchilik qisqardi", "aholi ko‘chib ketdi", "Sug‘oriladigan yerlar kengaydi.")
t.NAT("Qo‘qonda yog‘och o‘ymakorligi bilan qog‘ozgarlik yuqori darajaga ko‘tarildi.", "Qo‘qon qog‘oziga Turonning boshqa hududlarida ham ehtiyoj oshdi", "qog‘oz chetdan keltirildi", "qog‘ozgarlik taqiqlandi", "Qo‘qon qog‘ozi sifatsiz bo‘ldi", "Qo‘qon qog‘ozi mashhur bo‘ldi.")
t.NAT("Shaharlarda muayyan hunar bilan shug‘ullanuvchi mahallalar shakllandi.", "mahallalar nomi hunar nomi bilan bog‘liq bo‘lib, aholining kasbini ifodaladi", "hunarmandlar shahardan chiqarildi", "mahallalar tugatildi", "hunarlar aralashib ketdi", "Hunar nomidagi mahallalar.")
t.TF("Qo‘qon va Marg‘ilonda ishlangan shoyi gazlamalar elchilik munosabatlarida noyob hadyalar qatorida bo‘lgan.", True, "To‘g‘ri.")
t.TF("Amlok yerlaridan keladigan daromad vaqf muassasalariga tushgan.", False, "Noto‘g‘ri: barcha daromad xon ixtiyorida bo‘lgan.")
t.TF4([("Xususiy yerlar xonning maxsus yorlig‘i bilan harbiylarga berilgan.", True), ("Qo‘qon sahhoflari tayyorlagan qo‘lyozmalar hozir dunyo kutubxonalarida saqlanmoqda.", True),
       ("Ulug‘nahr arig‘i 1800–1803-yillarda qurilgan.", False), ("Vodiy g‘arbining tabiiy sharoiti bog‘dorchilik va uzumchilikka qulay bo‘lgan.", True)],
      "3-noto‘g‘ri: Ulug‘nahr 1868–1871-yillarda qurilgan.")
t.MUL([("Shahrixonsoy arig‘i Norin va Qoradaryodan suv olgan.", True),
       ("Xonlikda «mulki huri xolis» yerlari ham bo‘lgan.", True),
       ("Farg‘ona vodiysida ipakchilik rivojlanmagan.", False)],
      "III noto‘g‘ri: ipakchilik rivojlangan, tut daraxtlari ko‘paytirilgan.")
t.CHR("Sug‘orish ishlarini xronologik tartiblang.", ["Yangiariq qazildi", "Yangiariq 120 chaqirimga uzaytirildi", "Ulug‘nahr arig‘i qurildi"],
      "1800–1803 → 1819 → 1868–1871.")
t.MATCH("Yer turlarini izohi bilan moslashtiring.", ["amlok", "xususiy", "vaqf", "mulk"],
        ["xonga qarashli davlat yerlari", "xon yorlig‘i bilan harbiylarga berilgan yer", "diniy muassasalarga qarashli yer", "shaxsiy mulk yerlari", "qozilarga berilgan yer"], 'abcd',
        "Amlok – xon yeri; xususiy – harbiylarga; vaqf – diniy; mulk – shaxsiy.")
t.VENN("Marg‘ilon", "Chust",
       [("ipakchilik, shoyi matolar", 1), ("shoyisi elchilik hadyasi bo‘lgan", 1),
        ("pichoqchilik markazi", 2), ("Shahrixon bilan birga pichoqchilik", 2),
        ("Farg‘ona vodiysidagi hunarmandchilik shahri", 3)],
       "Marg‘ilon – ipak; Chust – pichoq; ikkalasi vodiy hunarmandchilik shahri.")
t.MAPMATCH('fargona', ['Marg‘ilon', 'Chust', 'Namangan', 'Xo‘jand'],
           ["shoyi matolari bilan mashhur shahar", "pichoqchilik taraqqiy etgan shahar", "1800–1803-yillarda Yangiariq qazilgan viloyat markazi", "o‘rik yetishtirishga ixtisoslashgan vodiy janubi-g‘arbidagi shahar"],
           "1 – Marg‘ilon; 2 – Chust; 3 – Namangan; 4 – Xo‘jand.")
