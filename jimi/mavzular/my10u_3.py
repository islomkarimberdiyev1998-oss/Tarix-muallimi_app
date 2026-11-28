from qlib import Topic, PLACES, REG
TOPICS = {}

# 5-mavzu. Milliy-ozodlik harakatlari
t = Topic('y10u5', 10005); TOPICS['y10u5'] = t
t.B("Rossiya sanoat mahsulotlari bozorni to‘ldirgach, qaysi soha inqirozga uchradi?", "hunarmandchilikning ko‘plab turlari", "paxtachilik", "chorvachilik", "savdo", "Hunarmandchilik.")
t.B("1878-yilda Mingtepada qo‘zg‘olonga kim boshchilik qilgan?", "Yetimxon", "Darvishxon", "Dukchi eshon", "Po‘latxon", "Yetimxon.")
t.B("Mingtepa hozirgi qaysi viloyatda joylashgan?", "Andijon viloyati", "Namangan viloyati", "Farg‘ona viloyati", "Toshkent viloyati", "Andijon viloyati, Marhamat tumani.")
t.B("1885-yilda Andijonda kim boshchiligida qo‘zg‘olon ko‘tarilgan?", "Darvishxon", "Yetimxon", "Ziyovuddin maxsum", "Damin kulol", "Darvishxon.")
t.B("1892-yildan qarshilik ko‘rsatgan fuqarolar qaysi sudga berila boshlagan?", "harbiy dala sudiga", "qozi sudiga", "Duma sudiga", "Peterburg sudiga", "Harbiy dala sudiga.")
t.B("1892-yilda vabo qayerdan tarqaldi?", "Afg‘onistondan", "Erondan", "Xitoydan", "Rossiyadan", "1892-yil martda Afg‘onistonda tarqaldi.")
t.B("Toshkent ma’muriyati vabo sababli nechta qabristonni yopgan?", "12 ta", "4 ta", "1 ta", "20 ta", "12 ta qabriston.")
t.B("Toshkent shahar boshlig‘i kim edi?", "S. Putinsev", "N. Korolkov", "Kaufman", "Muhammad Yoqub", "S. Putinsev.")
t.B("«Vabo isyoni» qanday nom bilan ham atalgan?", "«Toshotar voqeasi»", "«Jizzax fojiasi»", "«Andijon voqeasi»", "«Mingtepa qo‘zg‘oloni»", "«Toshotar voqeasi».")
t.B("«Vabo isyoni» qachon boshlangan?", "1892-yil 24-iyunda", "1898-yilda", "1916-yil iyulda", "1885-yil yozida", "1892-yil 24-iyun.")
t.B("1898-yilgi Andijon qo‘zg‘oloniga kim rahbarlik qilgan?", "Dukchi eshon (Muhammad Ali)", "Yetimxon", "Darvishxon", "Damin kulol", "Dukchi eshon.")
t.B("Dukchi eshon qo‘zg‘olonchilarining bir qismiga kim boshchilik qilgan?", "Ziyovuddin maxsum", "Muhammad Yoqub", "Po‘latxon", "Yetimxon", "Ziyovuddin maxsum.")
t.B("Qo‘zg‘olonchilar Andijonda nimaga hujum qilgan?", "harbiy kazarmaga", "bankka", "qozixonaga", "temiryo‘l stansiyasiga", "Harbiy kazarmaga.")
t.B("Jazo ekspeditsiyasiga shaxsan rahbarlik qilgan general-gubernator kim?", "N. Korolkov", "Kaufman", "Putinsev", "Skobelev", "N. Korolkov.")
t.B("1891-yilda Rossiyadan ko‘plab aholi qaysi viloyatga ko‘chirilgan?", "Farg‘ona", "Samarqand", "Sirdaryo", "Yettisuv", "Farg‘ona viloyatiga.")
t.NAT("Vabo davrida shifokorlar yetishmasdi, sanitariya tadbirlari xalqqa tushuntirilmadi.", "ma’murlar suvni, shifokorlar bemorlarni zaharlayapti degan mish-mishlar tarqaldi", "aholi tinchlandi", "vabo darhol to‘xtadi", "qabristonlar ko‘paydi", "Mish-mishlar tarqaldi.")
t.NAT("Putinsev muzokara o‘rniga kuch ishlatishni afzal ko‘rdi.", "norozilik kuchayib, olomon Putinsevni kaltakladi va mahkamani ostin-ustun qildi", "xalq tarqalib ketdi", "Putinsev talablarni bajardi", "oqsoqol xalqqa topshirildi", "Isyon kuchaydi.")
t.NAT("1891-yilda Farg‘onaga ko‘p rus aholisi ko‘chirildi.", "yer taqchil vodiyning ahvoli yomonlashib, mahalliy aholi noroziligi ortdi", "mahalliy aholi yer oldi", "vodiyda yer ko‘paydi", "norozilik kamaydi", "Norozilik kuchaydi.")
t.NAT("Toshkentdagi vabo qo‘zg‘olonidan keyin o‘lkada mirshablik holati joriy etildi.", "general-gubernator majlislarni tarqatish, surgun qilish kabi huquqlarni oldi", "majlislar erkinlashdi", "general-gubernator vakolati cheklandi", "mahalliy aholi o‘zini o‘zi boshqardi", "Repressiv vakolatlar kengaydi.")
t.TF("Vaqf yerlarining katta qismi davlat mulkiga aylantirilgan.", True, "To‘g‘ri.")
t.TF("1898-yilgi Andijon qo‘zg‘oloni g‘alaba bilan tugagan.", False, "Noto‘g‘ri: tor-mor etilgan, rahbarlari jazolangan.")
t.TF4([("1880-yil noyabrda Xo‘jand va O‘ratepada xalq harakatlari bo‘lgan.", True), ("Vabo isyonida olomon soni taxminan 400 kishi edi.", True),
       ("1886-yilgi Nizomga ko‘ra ko‘chib kelganlar uchun yer fondi tashkil etildi.", True), ("«Favqulodda muhofaza» joylarida hokimiyat qozikalonga o‘tgan.", False)],
      "4-noto‘g‘ri: general-gubernator yoki u tayinlagan bosh noib qo‘liga o‘tgan.")
t.MUL([("Isyonchilar Toshkent oqsoqolining uyiga o‘t qo‘ygan.", True),
       ("Qo‘zg‘olonni bostirish uchun kazaklar polki va bir rota askar chaqirilgan.", True),
       ("Shahar tashqarisida va’da qilingan barcha qabristonlar ochilgan.", False)],
      "III noto‘g‘ri: amalda faqat bitta qabriston ochilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Mingtepa qo‘zg‘oloni", "Xo‘jand va O‘ratepadagi harakatlar", "Darvishxon qo‘zg‘oloni", "Farg‘onaga ommaviy ko‘chirish", "Vabo isyoni", "Andijon qo‘zg‘oloni"],
      "1878 → 1880 → 1885 → 1891 → 1892 → 1898.")
t.MATCH("Qo‘zg‘olonlarni rahbari bilan moslashtiring.", ["Mingtepa (1878)", "Andijon (1885)", "Andijon (1898)", "Jizzax (1916)"],
        ["Yetimxon", "Darvishxon", "Dukchi eshon", "Damin kulol", "Po‘latxon"], 'abcd',
        "Mingtepa – Yetimxon; 1885 – Darvishxon; 1898 – Dukchi eshon; Jizzax – Damin kulol.")
t.VENN("Vabo isyoni (1892)", "Andijon qo‘zg‘oloni (1898)",
       [("Toshkentda bo‘lgan", 1), ("S. Putinsev kaltaklangan", 1),
        ("Dukchi eshon rahbarlik qilgan", 2), ("harbiy kazarmaga hujum", 2),
        ("kuch bilan bostirilgan", 3)],
       "1892 – Toshkent, Putinsev; 1898 – Dukchi eshon, kazarma; ikkalasi bostirilgan.")
t.MAPMATCH('fargona', ['Mingtepa', 'Xo‘jand', 'Namangan', 'Toshkent'],
           ["1878-yilda Yetimxon qo‘zg‘oloni bo‘lgan joy", "1880-yil noyabrda O‘ratepa bilan birga harakatlar bo‘lgan joy", "1882-yil boshida xalq harakati avj olgan shahar", "1892-yilgi «Vabo isyoni» shahri"],
           "1 – Mingtepa; 2 – Xo‘jand; 3 – Namangan; 4 – Toshkent.")

# 6-mavzu. Birinchi jahon urushi va Turkiston
t = Topic('y10u6', 10006); TOPICS['y10u6'] = t
t.B("Birinchi jahon urushi munosabati bilan Rossiya nimani e’lon qildi?", "ommaviy safarbarlik", "mustaqillik", "konstitutsiya", "yer islohoti", "Ommaviy safarbarlik.")
t.B("Turkistondan urushga dastlab aholining qaysi qismi chaqirilgan?", "yevropalik qismi", "mahalliy erkaklar", "ayollar", "bolalar", "19–43 yoshli yevropalik aholi.")
t.B("Turkistondan urushga necha yoshli yevropalik aholi chaqirilgan?", "19 yoshdan 43 yoshgacha", "18 yoshdan 30 yoshgacha", "25 yoshdan 50 yoshgacha", "16 yoshdan 60 yoshgacha", "19–43 yosh.")
t.B("1914-yilda Turkistonda qanday holat e’lon qilindi?", "favqulodda muhofaza holati", "harbiy holat", "mustaqillik", "karantin", "Favqulodda muhofaza holati.")
t.B("Harbiy xarajatlarni qoplash uchun paxtaga qanday narx joriy etildi?", "o‘zgarmas davlat narxi", "erkin bozor narxi", "ikki baravar oshirilgan narx", "jahon narxi", "O‘zgarmas davlat narxi.")
t.B("Imperiya tub aholidan qayerdagi ishlarda foydalanishga qaror qildi?", "front orqasidagi ishlarda", "frontning oldingi chizig‘ida", "dengiz flotida", "zavodlarda xorijda", "Front orqasidagi ishlarda.")
t.B("Front ortidagi ishlarga Turkistondan tashqari yana qaysi hududlar tub aholisi jalb qilindi?", "Sibir va Kavkaz", "Polsha va Finlyandiya", "Ukraina va Belarus", "Boltiqbo‘yi", "Sibir va Kavkaz.")
t.NAT("Ishchi kuchi bo‘lgan erkaklar urushga olindi.", "oilalar asosiy boquvchisidan ajralib, og‘ir ahvolga tushdi", "oilalar boyidi", "ishsizlik kamaydi", "soliqlar kamaydi", "Oilalar boquvchisiz qoldi.")
t.NAT("Narxlar umumiy o‘sib borayotganda paxtaga o‘zgarmas narx belgilandi.", "bu narx paxtakorlarning xarajatlarini qoplay olmadi", "paxtakorlar boyidi", "paxta ekish to‘xtatildi", "narxlar tushdi", "Paxtakorlar zarar ko‘rdi.")
t.NAT("1914-yilda noodatiy favqulodda muhofaza holati e’lon qilindi.", "Turkistonda turli ziddiyatlar kelib chiqa boshladi", "aholi bunga darhol ko‘nikdi", "urush tugadi", "Turkiston mustaqil bo‘ldi", "Ziddiyatlar paydo bo‘ldi.")
t.NAT("Urushga oziq-ovqat va qurol tayyorlash, yetkazish ishlari izdan chiqdi.", "imperiya tub aholidan front orqasidagi ishlarda foydalanishga qaror qildi", "urush to‘xtatildi", "ishlar xorijga topshirildi", "front kengaytirildi", "Mardikorlikka safarbarlik.")
t.TF("Birinchi jahon urushi yillarida davlat moliyasi inqirozga yuz tutgan.", True, "To‘g‘ri.")
t.TF("Safarbarlik Rossiyaning mustamlakalariga tegishli bo‘lmagan.", False, "Noto‘g‘ri: mustamlakalarga, jumladan Turkistonga ham tegishli edi.")
t.TF4([("Mahalliy aholidan arzon mehnat kuchi sifatida foydalanishga harakat qilindi.", True), ("Mudofaa inshootlarini qurish katta muammoga aylandi.", True),
       ("Paxta narxi erkin qo‘yilib, keskin oshdi.", False), ("Erkaklar front ortidagi ishlarga safarbar qilina boshlandi.", True)],
      "3-noto‘g‘ri: paxtaga o‘zgarmas davlat narxi joriy etilgan.")
t.MUL([("Ommaviy safarbarlik Turkistonga ham tegishli edi.", True),
       ("Front ortidagi ishlarni boshqarish izdan chiqqan edi.", True),
       ("Urush Turkiston iqtisodiyotiga hech qanday ta’sir ko‘rsatmagan.", False)],
      "III noto‘g‘ri: moliyaviy inqiroz, narxlar, safarbarlik kabi og‘ir ta’sir ko‘rsatgan.")
t.CHR("Jarayonlarni ketma-ket joylashtiring.", ["Rossiya urushga kirib, ommaviy safarbarlik e’lon qildi", "Turkistonda favqulodda muhofaza holati e’lon qilindi", "paxtaga o‘zgarmas davlat narxi joriy etildi", "tub aholini front ortidagi ishlarga safarbar qilish boshlandi"],
      "Safarbarlik → 1914 favqulodda holat → o‘zgarmas narx → mardikorlik.")
t.MATCH("Choralarni maqsadi bilan moslashtiring.", ["ommaviy safarbarlik", "paxtaga o‘zgarmas narx", "favqulodda muhofaza holati", "tub aholini front ortiga safarbar etish"],
        ["urushga askar to‘plash", "harbiy xarajatlarni qoplash", "o‘lkada qattiq nazorat", "front ortidagi ishlarni bajarish", "savdoni erkinlashtirish"], 'abcd',
        "Safarbarlik – askar; o‘zgarmas narx – xarajat; favqulodda holat – nazorat; mardikorlik – front orti.")
t.VENN("Yevropalik aholi", "Tub (mahalliy) aholi",
       [("19–43 yoshda urushga chaqirilgan", 1), ("frontga yuborilgan", 1),
        ("front orqasidagi ishlarga safarbar etilgan", 2), ("arzon mehnat kuchi sifatida qaralgan", 2),
        ("urush og‘irligini his qilgan Turkiston aholisi", 3)],
       "Yevropalik – front; tub aholi – front orti ishlari; ikkalasi urush ta’sirida.")
t.MAPN('uzb', ['Toshkent', 'Buxoro', 'Xiva', 'Samarqand'], "1914-yilda favqulodda muhofaza holati e’lon qilingan Turkiston general-gubernatorligining markazi xaritada qaysi raqamda?",
       "Toshkent.")

# 7-mavzu. 1916-yilgi qo‘zg‘olon
t = Topic('y10u7', 10007); TOPICS['y10u7'] = t
t.B("Farg‘ona viloyatida mardikorlikka qanday tartibda odam olingan?", "har beshta xonadondan bir kishi", "har bir xonadondan bir kishi", "har o‘nta xonadondan bir kishi", "faqat boylardan", "Har beshta xonadondan bir kishi.")
t.B("Mardikorlikka qarshi chiqishlar Samarqanddagi qaysi qishloqdan boshlangan?", "Urgut", "Dahbed", "Siyob", "Angor", "Urgut qishlog‘idan.")
t.B("1916-yil iyulida qaysi joyda ham norozilik bo‘lgan?", "Dahbedda", "Mingtepada", "Chimkentda", "Xivada", "Dahbedda.")
t.B("Jizzaxda hunarmandlarga kim boshchilik qilgan?", "Damin kulol", "Dukchi eshon", "Yetimxon", "Darvishxon", "Damin kulol.")
t.B("Jizzaxdagi hunarmandlar oqsoqoldan nimani talab qilgan?", "mardikorlikka olish ro‘yxatini", "soliqni kamaytirishni", "yer berishni", "masjid qurishni", "Ro‘yxatni.")
t.B("Qo‘zg‘olonchilar nimalar bilan qurollangan edi?", "ketmon va tayoqlar", "to‘plar", "miltiqlar", "qilich va sovutlar", "Ketmon, tayoqlar – oddiy ish qurollari.")
t.B("Jizzax qo‘zg‘olonidan keyin Turkistonda qanday holat e’lon qilindi?", "harbiy holat", "favqulodda muhofaza", "karantin", "tinchlik holati", "Harbiy holat.")
t.B("1916-yilgi qo‘zg‘olon tarixda qanday nom bilan muhrlangan?", "«Jizzax fojiasi»", "«Toshotar voqeasi»", "«Andijon qirg‘ini»", "«Vabo isyoni»", "«Jizzax fojiasi».")
t.B("1916-yilgi qo‘zg‘olon mustamlakachilik davridagi qanday qo‘zg‘olon sifatida baholanadi?", "eng yirik qo‘zg‘olon", "eng kichik qo‘zg‘olon", "birinchi qo‘zg‘olon", "muvaffaqiyatli qo‘zg‘olon", "Eng yirik qo‘zg‘olon.")
t.B("«Jannatdin nishona bo‘lg‘on buyuk Turkiston qit’asida g‘alla yetishmay…» degan fikr muallifi kim?", "Miyon Buzruk", "Behbudiy", "Munavvar qori", "Fitrat", "Miyon Buzruk.")
t.NAT("Badavlat xonadon vakillari pora evaziga ro‘yxatga kiritilmadi, kambag‘allar ro‘yxatga olindi.", "xalq ommasining noroziligi yanada kuchaydi", "aholi tinchlandi", "ro‘yxat bekor qilindi", "boylar mardikorlikka ketdi", "Norozilik kuchaydi.")
t.NAT("Jizzax oqsoqoli ro‘yxatni bermay, odamlarni haqorat qildi.", "qo‘zg‘olonchilar Jizzaxning yangi shahar qismiga yo‘l oldi", "odamlar tarqalib ketdi", "oqsoqol ro‘yxatni yirtdi", "qo‘zg‘olon to‘xtadi", "Qo‘zg‘olon boshlandi.")
t.NAT("Qo‘zg‘olonchilar asosan harbiy ishdan bexabar dehqon va hunarmandlar edi.", "qo‘zg‘olon mag‘lubiyatga uchradi", "qo‘zg‘olon g‘alaba qildi", "Rossiya chekindi", "mardikorlik bekor qilindi", "Mag‘lubiyat sabablaridan biri.")
t.NAT("Qo‘zg‘olon yoz faslida bo‘lib, ekinzorlar nobud bo‘ldi.", "oziq-ovqat taqchilligi va narxlar oshishi yuz berdi", "hosil mo‘l bo‘ldi", "narxlar tushdi", "eksport ko‘paydi", "Oziq-ovqat taqchilligi.")
t.TF("Namoyishchilar mahalliy boshqaruv vakillarini kaltaklab, ro‘yxatlarni yirtib tashlagan.", True, "To‘g‘ri.")
t.TF("Qo‘zg‘olon faqat Jizzaxda bo‘lib, boshqa shaharlarga yoyilmagan.", False, "Noto‘g‘ri: Toshkent, Samarqand va boshqa joylarga yoyilgan.")
t.TF4([("Qo‘zg‘olon rahbarlari o‘lim jazosiga hukm etilgan.", True), ("Qo‘zg‘olon ko‘tarilgan qishloqlarga o‘t qo‘yilgan.", True),
       ("Mustamlaka hukumati qo‘zg‘olondan keyin hech qanday yon bermagan.", False), ("Hukumatga yordam bermagan aholi cho‘lga haydalgan.", True)],
      "3-noto‘g‘ri: hukumat ba’zi yengilliklar yaratishga, murosaga majbur bo‘lgan.")
t.MUL([("Siyob, Mahalla, Xo‘ja Ahror, Angorda ham norozilik chiqishlari bo‘lgan.", True),
       ("Mardikorlik ko‘plab oilalarni boquvchisiz qoldirgan.", True),
       ("Qo‘zg‘olonchilar zamonaviy qurollar bilan qurollangan.", False)],
      "III noto‘g‘ri: oddiy ish qurollari bilan jang qilgan.")
t.CHR("Voqealarni ketma-ket joylashtiring.", ["mardikorlikka olish tartibi belgilandi", "Urgutda norozilik", "Dahbedda norozilik (iyul)", "Jizzaxda ommaviy qo‘zg‘olon", "Turkistonda harbiy holat e’lon qilindi"],
      "Tartib → Urgut → Dahbed → Jizzax → harbiy holat.")
t.MATCH("Qo‘zg‘olon oqibatlarini izohi bilan moslashtiring.", ["birinchidan", "ikkinchidan", "uchinchidan", "mardikorlik natijasi"],
        ["Jizzax atrofidagi qishloqlar yondirildi", "ekinzorlar nobud bo‘lib, narxlar oshdi", "aholi orasida ko‘plab qurbonlar", "oilalar boquvchisiz qoldi", "mustaqillik e’lon qilindi"], 'abcd',
        "1 – qishloqlar yondi; 2 – ekinlar nobud; 3 – qurbonlar; mardikorlik – boquvchisizlik.")
t.VENN("Andijon qo‘zg‘oloni (1898)", "Jizzax qo‘zg‘oloni (1916)",
       [("Dukchi eshon rahbarligi", 1), ("harbiy kazarmaga hujum", 1),
        ("mardikorlikka qarshi", 2), ("Damin kulol boshchiligida", 2),
        ("mustamlakachilikka qarshi, bostirilgan", 3)],
       "1898 – Dukchi eshon; 1916 – mardikorlik, Damin kulol; ikkalasi bostirilgan.")
t.MAPMATCH('zarafshon', ['Jizzax', 'Urgut', 'Samarqand'],
           ["Damin kulol boshchiligida ommaviy qo‘zg‘olon bo‘lgan shahar", "mardikorlikka qarshi chiqishlar boshlangan qishloq", "qo‘zg‘olon yoyilgan viloyat markazi"],
           "1 – Jizzax; 2 – Urgut; 3 – Samarqand.")
