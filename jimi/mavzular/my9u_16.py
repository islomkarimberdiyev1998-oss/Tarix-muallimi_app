from qlib import Topic, PLACES, REG
TOPICS = {}

# 34-§ O‘zbek davlatlarining harbiy salohiyati
t = Topic('y9u34', 9034); TOPICS['y9u34'] = t
t.B("Shayboniylar qo‘shinining asosini kimlar tashkil etgan?", "otliq askarlar", "piyodalar", "to‘pchilar", "yollanma askarlar", "Otliq askarlar.")
t.B("Uzun dastali jang boltasi qanday atalgan?", "tabarzin", "gurzi", "ilgak", "nayza", "Tabarzin.")
t.B("Qaysi hukmdor davrida o‘tsochar pilta miltiqlar va kichik to‘plardan foydalanilgan?", "Abdullaxon II", "Shayboniyxon", "Ubaydullaxon", "Abulxayrxon", "Abdullaxon II.")
t.B("XVIII–XIX asrlarda xon qo‘shinlari qanday tizimda tashkil qilingan?", "o‘nlik tizimi", "polk tizimi", "legion tizimi", "batalyon tizimi", "O‘nlik tizimi.")
t.B("XIX asr boshida Buxoroda muntazam qo‘shin qanday atalgan?", "navkariya", "qora cherik", "askariya", "sipoh", "«Navkariya».")
t.B("Buxoroda muntazam bo‘lmagan qo‘shin qanday atalgan?", "qora cherik", "navkariya", "sarboz", "askariya", "«Qora cherik».")
t.B("Amir Nasrulla qachon harbiy islohot o‘tkazgan?", "1837-yilda", "1842-yilda", "1810-yilda", "1868-yilda", "1837-yilda.")
t.B("Buxoroda piyodalar qanday atalgan?", "sarbozlar", "navkarlar", "sipohlar", "to‘pchilar", "Sarbozlar.")
t.B("Buxoro qo‘shinida piyodalar soni to‘pchilardan necha barobar ko‘p bo‘lgan?", "3,5 barobar", "2 barobar", "10 barobar", "5 barobar", "3,5 barobar.")
t.B("Muhammad Rahimxon I necha harbiydan iborat muntazam qo‘shin tuzgan?", "2000", "200", "20000", "12000", "2000 ta – xon navkarlari.")
t.B("Qo‘qon xonligida muntazam qo‘shin qanday atalgan?", "askariya", "navkariya", "qora cherik", "qilquyruq", "Askariya.")
t.B("Qo‘qon qo‘shini harbiy libosi qanday bo‘lgan?", "qizil va moviy chopon, sariq shim, oq salla", "qizil kamzul, oq shim, qorako‘l telpak", "maxsus kiyim bo‘lmagan", "qora chopon, oq shim", "Qizil-moviy chopon, sariq shim, oq salla.")
t.B("Parchin qatorlari faqat tashqaridan ko‘rinadigan zirh qanday atalgan?", "kuyak", "baktar", "jul", "ko‘krakpo‘sh", "Kuyak.")
t.B("Jangovar otlarning zirhli to‘shamasi qanday atalgan?", "jul", "kuyak", "baktar", "sovut", "Jul.")
t.B("Jangovar otlar zirh bilan qachondan himoyalana boshlagan?", "XIII asrdan so‘ng", "XVI asrdan", "X asrdan", "XIX asrdan", "XIII asrdan so‘ng.")
t.B("Qayerda to‘p, yadro va miltiq tayyorlaydigan katta ustaxona (zavod) bo‘lgan?", "O‘ratepada", "Xivada", "Buxoroda", "Samarqandda", "O‘ratepada.")
t.B("Xiva xonligida harbiy kuchlarga bosh qo‘mondonlikni kim amalga oshirgan?", "yasovulboshi", "mingboshi", "vaziri harb", "qushbegi", "Yasovulboshi.")
t.B("Qo‘qonda harbiy kuchlarga bosh qo‘mondonlikni kim amalga oshirgan?", "mingboshi", "yasovulboshi", "vaziri harb", "devonbegi", "Mingboshi.")
t.NAT("Temir sovutlar jangda tez qizib ketardi.", "askarlar jang liboslari ustidan chopon kiyishgan", "sovutlar taqiqlandi", "askarlar sovutsiz jang qildi", "sovutlar yog‘ochdan yasaldi", "Ustidan chopon kiyilgan.")
t.NAT("1837-yilda Amir Nasrulla harbiy islohot o‘tkazdi.", "piyoda, otliq va to‘pchilardan iborat muntazam qo‘shin tuzildi", "qo‘shin tarqatildi", "qora cherik kuchaydi", "Buxoro Rossiyaga bo‘ysundi", "Muntazam qo‘shin tuzildi.")
t.NAT("Himoya aslahalari mahalliy an’ana va Old Osiyo qurollari uyg‘unlashuvidan yaratildi.", "o‘rta osiyolik ustalar aslahalari qo‘shni davlatlarnikiga o‘xshab ketgan", "aslahalar butunlay boshqacha bo‘lgan", "aslaha yasash to‘xtagan", "faqat Yevropa qurollari ishlatilgan", "O‘xshashlik paydo bo‘lgan.")
t.NAT("Muntazam qo‘shinni kiyim va qurol bilan ta’minlash davlat zimmasida edi.", "Buxoro sarbozlari bir xil harbiy kiyimga ega bo‘lgan", "askarlar o‘zi qurollandi", "qo‘shin kiyimsiz qoldi", "kiyimni savdogarlar berdi", "Bir xil kiyim joriy etildi.")
t.TF("Xiva muntazam qo‘shinining maxsus kiyimlari bo‘lmagan.", True, "To‘g‘ri.")
t.TF("XVI–XIX asrlarda xonliklar qurolni faqat o‘zida tayyorlagan, chetdan keltirmagan.", False, "Noto‘g‘ri: Eron, Rossiya, Jung‘oriya va G‘arbiy Yevropadan ham keltirilgan.")
t.TF4([("Qo‘shinlar jangga bayroqlar va tug‘lar bilan kirgan.", True), ("Qo‘shinlarda karnaychi, surnaychi, nog‘orachi xizmat qilgan.", True),
       ("Buxoro sarbozlari qorako‘l telpak kiygan.", True), ("Barcha xonliklarda oliy bosh qo‘mondon mingboshi bo‘lgan.", False)],
      "4-noto‘g‘ri: oliy bosh qo‘mondon xonlar bo‘lgan.")
t.MUL([("Qo‘shin bilan birga hunarmand, savdogar va ko‘prik quruvchilar ham borgan.", True),
       ("XVI asrdan piltali, so‘ng burama kertikli miltiqlar qo‘llanilgan.", True),
       ("Harbiy harakatda avangard qo‘shinning eng orqasida borgan.", False)],
      "III noto‘g‘ri: avangard oldinda, aryergard uning ortidan borgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Jangovar otlar zirh bilan himoyalana boshladi", "Abdullaxon II davrida pilta miltiq va to‘plar qo‘llandi", "Muhammad Rahimxon I muntazam qo‘shin tuzdi", "Amir Nasrulla harbiy islohot o‘tkazdi"],
      "XIII asrdan so‘ng → XVI asr → XIX asr boshi → 1837.")
t.MATCH("Xonliklarni harbiy bosh qo‘mondon lavozimi bilan moslashtiring.", ["Buxoro amirligi", "Xiva xonligi", "Qo‘qon xonligi", "barcha xonliklarda oliy bosh qo‘mondon"],
        ["vaziri harb", "yasovulboshi", "mingboshi", "xon", "qushbegi"], 'abcd',
        "Buxoro – vaziri harb; Xiva – yasovulboshi; Qo‘qon – mingboshi; oliy – xon.")
t.VENN("Buxoro muntazam qo‘shini", "Qo‘qon muntazam qo‘shini",
       [("navkariya, sarbozlar", 1), ("qizil-qora-sariq kamzul, oq shim", 1),
        ("askariya, sipohlar", 2), ("qizil-moviy chopon, oq salla", 2),
        ("piyoda, otliq va to‘pchilardan iborat", 3)],
       "Buxoro – navkariya, kamzul; Qo‘qon – askariya, chopon; ikkalasida piyoda, otliq, to‘pchi.")
t.MAPMATCH('uzb', ['Buxoro', 'Xiva', 'Qo‘qon', 'O‘ratepa'],
           ["qo‘shin vaziri harb qo‘mondonligida bo‘lgan poytaxt", "2000 kishilik xon navkarlari tuzilgan poytaxt", "mingboshi qo‘shinga qo‘mondonlik qilgan poytaxt", "to‘p va yadro tayyorlaydigan zavod bo‘lgan shahar"],
           "1 – Buxoro; 2 – Xiva; 3 – Qo‘qon; 4 – O‘ratepa.")

# 35-§ Turkistonning uch xonlikka bo‘linib ketishi va uning oqibatlari
t = Topic('y9u35', 9035); TOPICS['y9u35'] = t
t.B("Temuriylar saltanati XVIII asr boshida nechta o‘zbek xonligiga bo‘linib ketgan?", "uchta", "ikkita", "to‘rtta", "beshta", "Uchta (1709).")
t.B("Uchinchi o‘zbek xonligi qachon paydo bo‘lgan?", "1709-yilda", "1511-yilda", "1756-yilda", "1770-yilda", "1709-yilda.")
t.B("Buxoro amirligida qaysi urug‘ vakillari hukmronlik qilgan?", "mang‘it", "qo‘ng‘irot", "ming", "qipchoq", "Mang‘it.")
t.B("Xiva xonligida qaysi urug‘ vakillari hukmronlik qilgan?", "qo‘ng‘irot", "mang‘it", "ming", "nayman", "Qo‘ng‘irot.")
t.B("Qo‘qon xonligida qaysi urug‘ vakillari hukmronlik qilgan?", "ming", "mang‘it", "qo‘ng‘irot", "kenagas", "Ming.")
t.B("Sanoat to‘ntarishi XVIII asrda qaysi mamlakatda yuz bergan?", "Buyuk Britaniya", "Fransiya", "Rossiya", "Germaniya", "Buyuk Britaniyada.")
t.B("Dunyoda ilk temiryo‘l qachon qurilgan?", "1825-yilda", "1709-yilda", "1837-yilda", "1868-yilda", "1825-yilda.")
t.B("XIX asr insoniyat tarixiga qanday asr bo‘lib kirgan?", "bug‘ mashinalari asri", "elektr asri", "atom asri", "kompyuter asri", "Bug‘ mashinalari asri.")
t.B("Qishloq xo‘jaligida mashina va kimyoviy o‘g‘itlardan foydalanish qachon boshlangan?", "XIX asrning 40-yillarida", "XVIII asr boshida", "XVI asrda", "XX asrda", "XIX asrning 40-yillarida.")
t.B("XIX asr boshida Yevropa Osiyodan aholi jon boshiga daromad bo‘yicha necha barobar o‘zib ketgan?", "2 barobar", "10 barobar", "5 barobar", "1,5 barobar", "2 barobar.")
t.B("Buyuk ipak yo‘lini ahamiyatsiz qilib qo‘ygan omil nima?", "XVI asrda dengiz savdo yo‘llarining ochilishi", "temiryo‘l qurilishi", "mo‘g‘ul bosqini", "qora o‘lat", "Dengiz yo‘llarining ochilishi.")
t.B("Osiyoda texnika qo‘llanilmagani tufayli qanday rivojlanish usuli yetakchilik qilgan?", "ekstensiv", "intensiv", "industrial", "innovatsion", "Ekstensiv usul.")
t.B("G‘arbiy Yevropada yer mulki kimga meros qolgan?", "katta farzandga", "barcha merosxo‘rlarga teng", "davlatga", "cherkovga", "Katta farzandga.")
t.NAT("Buxoro amiri Qo‘qon xonligi tuzilganini tan olmadi.", "urushlar va hudud talashishlar boshlandi", "Buxoro va Qo‘qon birlashdi", "Qo‘qon Buxoroga qo‘shildi", "tinchlik o‘rnatildi", "Urushlarga sabab bo‘ldi.")
t.NAT("Turkistonda yerga xususiy mulkchilik to‘la qaror topmadi.", "hunarmandchilik fabrika ishlab chiqarishi darajasiga ko‘tarila olmadi", "fabrikalar ko‘paydi", "sanoat to‘ntarishi yuz berdi", "temiryo‘l qurildi", "Fabrika ishlab chiqarishi shakllanmadi.")
t.NAT("Turkiston uch xonlikka bo‘linib ketdi.", "mintaqada yagona ichki bozor shakllanmadi", "yagona bozor tez rivojlandi", "savdo yo‘llari kengaydi", "xonliklar birlashdi", "Yagona bozor yo‘q edi.")
t.NAT("Xalqni yagona maqsad yo‘lida birlashtiradigan yo‘lboshchi chiqmadi.", "bu Turkistonning XIX asr ikkinchi yarmida Rossiya mustamlakasiga aylanishiga zamin yaratdi", "Turkiston Yevropaga qo‘shildi", "xonliklar kuchaydi", "Rossiya Turkistonni tark etdi", "Mustamlakaga aylanish.")
t.TF("Temiryo‘l qurilishi cho‘yan, temir va po‘latga ehtiyojni oshirib yuborgan.", True, "To‘g‘ri.")
t.TF("Osiyoda ota yer-mulkini faqat katta o‘g‘liga meros qoldirgan.", False, "Noto‘g‘ri: merosxo‘rlarga teng bo‘lib bergan.")
t.TF4([("XV asr oxirida Yevropada markazlashgan kuchli davlatlar qaror topgan.", True), ("Davlat yerini ijaraga olgan dehqon yer unumdorligini oshirishga qiziqmagan.", True),
       ("Xonliklar sanoat to‘ntarishida faol ishtirok etgan.", False), ("Tijorat banklari xalqaro miqyosda faoliyat ko‘rsata boshlagan.", True)],
      "3-noto‘g‘ri: Turkiston xonliklari bu jarayonlardan chetda qolgan.")
t.MUL([("Osiyoda an’anaviylikka asoslangan, islohotlarga toqatsiz jamiyat hukm surgan.", True),
       ("Qurg‘oqchilik va haroratning pasayishi iqtisodiyotga salbiy ta’sir ko‘rsatgan.", True),
       ("Turkistonda yer xususiy mulk sifatida Yevropadan oldin qaror topgan.", False)],
      "III noto‘g‘ri: Turkistonda yer davlat mulki bo‘lib qolavergan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Yevropada markazlashgan davlatlar qaror topdi", "dengiz savdo yo‘llari ochildi", "Turkiston uchta xonlikka bo‘lindi", "Buyuk Britaniyada sanoat to‘ntarishi", "ilk temiryo‘l qurildi"],
      "XV asr oxiri → XVI asr → 1709 → XVIII asr → 1825.")
t.MATCH("Xonliklarni hukmron sulola bilan moslashtiring.", ["Buxoro amirligi", "Xiva xonligi", "Qo‘qon xonligi", "Temuriylar saltanati"],
        ["mang‘itlar", "qo‘ng‘irotlar", "minglar", "temuriylar", "safaviylar"], 'abcd',
        "Buxoro – mang‘it; Xiva – qo‘ng‘irot; Qo‘qon – ming; saltanat – temuriylar.")
t.VENN("G‘arbiy Yevropa", "Turkiston xonliklari",
       [("yerga xususiy mulkchilik", 1), ("sanoat to‘ntarishi", 1),
        ("yer davlat mulki", 2), ("ekstensiv rivojlanish", 2),
        ("XVII–XIX asrlarda mavjud davlatlar", 3)],
       "Yevropa – xususiy mulk, sanoat; Turkiston – davlat yeri, ekstensiv; ikkalasi o‘sha davr davlatlari.")
t.MAPMATCH('uzb', ['Buxoro', 'Xiva', 'Qo‘qon'],
           ["mang‘itlar hukmronlik qilgan amirlik poytaxti", "qo‘ng‘irotlar hukmronlik qilgan xonlik poytaxti", "minglar hukmronlik qilgan xonlik poytaxti"],
           "1 – Buxoro; 2 – Xiva; 3 – Qo‘qon.")

# 36-§ O‘zbek davlatlari tarixi bo‘yicha manbalar
t = Topic('y9u36', 9036); TOPICS['y9u36'] = t
t.B("Tarixiy hujjatlar saqlanadigan joy nima deyiladi?", "arxiv", "muzey", "kutubxona", "devonxona", "Arxiv.")
t.B("Hasanbek Rumluning asari qanday ataladi?", "«Eng go‘zal tarix»", "«Shajarayi turk»", "«Shohidi iqbol»", "«Saralangan tarixlar»", "«Eng go‘zal tarix».")
t.B("Turkiy qabilalar shajarasi haqidagi «Shajarayi turk» muallifi kim?", "Abulg‘ozi Bahodirxon", "Munis", "Ogahiy", "Bayoniy", "Abulg‘ozi Bahodirxon.")
t.B("Munisning «Firdavs ul-iqbol» asari kimning topshirig‘i bilan yozilgan?", "Eltuzarxon", "Asfandiyorxon", "Umarxon", "Abulg‘ozixon", "1806-yilda Eltuzarxon topshirig‘i bilan.")
t.B("«Firdavs ul-iqbol»da Xorazmning necha yillik o‘tmishi yoritilgan?", "250 yillik", "2500 yillik", "100 yillik", "40 yillik", "250 yillik.")
t.B("Ogahiyning «Shohidi iqbol» asari qaysi yilgacha bo‘lgan tarixni aks ettiradi?", "1872-yilgacha", "1806-yilgacha", "1911-yilgacha", "1825-yilgacha", "1872-yilgacha.")
t.B("Xiva xonligining 1872–1911-yillar tarixini kim yozgan?", "Yusufbek Bayoniy", "Ogahiy", "Munis", "Hasanbek Rumlu", "Yusufbek Bayoniy.")
t.B("Bayoniy asarini qaysi xon topshirig‘i bilan yaratgan?", "Asfandiyorxon", "Eltuzarxon", "Muhammad Rahimxon", "Olloqulixon", "1912-yilda Asfandiyorxon topshirig‘i bilan.")
t.B("«Xorazmning sug‘orilish tarixi» kim boshchiligida yaratilgan?", "akademik I. Mo‘minov", "akademik M. Yo‘ldoshev", "D. Alimova", "A. Ziyo", "Akademik I. Mo‘minov.")
t.B("«Xiva – ming gumbaz shahri» kitobi qachon chop etilgan?", "1997-yilda", "1990-yilda", "2001-yilda", "1912-yilda", "1997-yilda, Xivaning 2500 yilligi munosabati bilan.")
t.B("«Umarnoma» («Shohnomayi Umarxon») muallifi kim?", "Abdulkarim Namangoniy", "Muhammad Hakimxon", "Mirzo Olim Toshkandiy", "Ibrat", "Abdulkarim Namangoniy, 1820-yil.")
t.B("«Saralangan tarixlar» muallifi Muhammad Hakimxon Umarxon saroyida qanday lavozimda bo‘lgan?", "naqib", "mingboshi", "qushbegi", "shig‘ovul", "Naqib.")
t.B("Muhammad Hakimxonning onasi Oftoboyim kimning singlisi edi?", "Umarxonning", "Muhammad Alixonning", "Norbo‘taxonning", "Nodiraning", "Umarxonning singlisi.")
t.B("«Farg‘ona tarixi» kitobining muallifi kim?", "Is’hoqxon Ibrat", "Mirzo Olim Toshkandiy", "Mirzo Olim Maxdum hoji", "Abdulkarim Namangoniy", "Is’hoqxon Junaydullo o‘g‘li Ibrat.")
t.B("Muhammad Kamoliddin Binoiy qayerda tug‘ilgan?", "Hirotda", "Samarqandda", "Buxoroda", "Andijonda", "1453-yilda Hirotda.")
t.B("Binoiy qachon va qayerda halok bo‘lgan?", "1512-yilda Qarshi egallanganda", "1510-yilda Marvda", "1501-yilda Samarqandda", "1526-yilda Panipatda", "1512-yilda Qarshida.")
t.B("«Tarixi Rashidiy» muallifi kim?", "Mirzo Muhammad Haydar", "Binoiy", "Hofiz Tanish", "Abdurahmon Tole", "Mirzo Muhammad Haydar.")
t.B("Muhammad Haydar 1507-yildan qayerda Bobur saroyida yashagan?", "Kobulda", "Andijonda", "Samarqandda", "Hirotda", "Kobulda.")
t.B("«Gulshan ul-mulk» asarining muallifi kim?", "Muhammad Yoqub", "Abdurahmon Tole", "Hofiz Tanish", "Muhammad Haydar", "Doniyolbiyning o‘g‘li Muhammad Yoqub.")
t.B("«Tarixi Abulfayzxon»da kimning o‘ldirilishi batafsil yozilgan?", "Ubaydullaxonning", "Abulfayzxonning", "Nadr Muhammadxonning", "Shayboniyxonning", "Ashtarxoniy Ubaydullaxonning.")
t.NAT("Abdulkarim Namangoniy «Umarnoma»ni yozdi.", "Umarxonning kelib chiqishi «Oltin beshik»ka bog‘lanib, hokimiyati qonuniyligi asoslandi", "Umarxon taxtdan ag‘darildi", "asar taqiqlandi", "minglar sulolasi tugadi", "Hokimiyat qonuniyligi asoslandi.")
t.NAT("Oftoboyim o‘g‘illaridan birini taxtga o‘tqazishga urindi.", "Muhammad Hakimxon Namangan hokimligidan ozod etilib, mol-mulki musodara qilindi", "Hakimxon xon bo‘ldi", "Oftoboyim taxtga chiqdi", "Muhammad Alixon taxtdan voz kechdi", "Hakimxon lavozimidan ayrildi.")
t.NAT("Hofiz Tanish voqealarni guvohlar og‘zidan yozib oldi, ko‘plariga o‘zi shohid bo‘ldi.", "«Abdullanoma» XVI asr tarixini o‘rganishda katta o‘rin tutadi", "asar ishonchsiz deb topildi", "asar yo‘qolib ketdi", "asar faqat she’rlardan iborat", "Qimmatli manba.")
t.NAT("Ubaydullaxonning o‘limidan so‘ng Buxoro va Samarqandda qo‘shhokimiyatchilik vujudga keldi.", "Abdullaxon II Navro‘z Ahmad vafotidan keyin qonli kurashlar bilan davlatni birlashtirdi", "davlat butunlay parchalanib ketdi", "Eron Buxoroni oldi", "Bobur qaytib keldi", "Davlat birlashtirildi.")
t.TF("O‘zbekiston davlat arxivida uch o‘zbek davlati tarixiga oid hujjatlar saqlanmoqda.", True, "To‘g‘ri.")
t.TF("«Umarnoma» nasriy uslubda yozilgan.", False, "Noto‘g‘ri: she’riy uslubda bitilgan.")
t.TF4([("«Shayboniynoma»da Shayboniyxonning Ko‘hak daryosiga ko‘prik qurishi haqida ma’lumot bor.", True), ("Muhammad Haydar 1511-yilda Andijonga qaytgan.", True),
       ("Binoiy faqat Shayboniyxonga xizmat qilgan, Boburga xizmat qilmagan.", False), ("Ubaydullaxon suiqasdiga Javshan qalmiq boshchilik qilgan.", True)],
      "3-noto‘g‘ri: Binoiy dastlab Boburga, so‘ng Shayboniyxonga xizmat qilgan.")
t.MUL([("«Tarixi Rashidiy»da Boburning Ismoil Safaviy bilan 1510-yildan keyingi munosabatlari yoritilgan.", True),
       ("Muhammad Yoqub mang‘it amirlari davridagi voqealarga shaxsan guvoh bo‘lgan.", True),
       ("«Shohidi iqbol» Munisning asari.", False)],
      "III noto‘g‘ri: «Shohidi iqbol» – Ogahiy asari.")
t.CHR("Asarlarni yozilgan vaqti bo‘yicha tartiblang.", ["Munisning «Firdavs ul-iqbol»i boshlandi", "«Umarnoma» yozildi", "Bayoniy Xiva tarixini yozdi", "«Xiva – ming gumbaz shahri» chop etildi"],
      "1806 → 1820 → 1912 → 1997.")
t.MATCH("Asarlarni mualliflari bilan moslashtiring.", ["«Shajarayi turk»", "«Shohidi iqbol»", "«Saralangan tarixlar»", "«Gulshan ul-mulk»"],
        ["Abulg‘ozi Bahodirxon", "Ogahiy", "Muhammad Hakimxon to‘ra", "Muhammad Yoqub", "Hasanbek Rumlu"], 'abcd',
        "Shajarayi turk – Abulg‘ozi; Shohidi iqbol – Ogahiy; Saralangan tarixlar – Hakimxon; Gulshan ul-mulk – Muhammad Yoqub.")
t.VENN("Xiva tarixiga oid asarlar", "Qo‘qon tarixiga oid asarlar",
       [("«Firdavs ul-iqbol»", 1), ("«Shohidi iqbol»", 1),
        ("«Umarnoma»", 2), ("«Farg‘ona tarixi»", 2),
        ("mahalliy tarixchilar yozgan manbalar", 3)],
       "Xiva – Firdavs ul-iqbol, Shohidi iqbol; Qo‘qon – Umarnoma, Farg‘ona tarixi; ikkalasi mahalliy manba.")
t.MAPMATCH('ca', ['Hirot', 'Kobul', 'Qarshi', 'Andijon'],
           ["1453-yilda Binoiy tug‘ilgan shahar", "1507-yildan Muhammad Haydar Bobur saroyida yashagan shahar", "1512-yilda Binoiy halok bo‘lgan shahar", "1511-yilda Muhammad Haydar qaytgan shahar"],
           "1 – Hirot; 2 – Kobul; 3 – Qarshi; 4 – Andijon.")
