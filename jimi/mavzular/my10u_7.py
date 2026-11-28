from qlib import Topic, PLACES, REG
TOPICS = {}

# 13-mavzu. Ilm-fan va madaniyat
t = Topic('y10u13', 10013); TOPICS['y10u13'] = t
t.B("«Tarixi Turkiston» asarini kim yozgan?", "Mulla Olim Mahdum hoji", "Behbudiy", "Avloniy", "Ahmad Donish", "Mulla Olim Mahdum hoji.")
t.B("«Tarixi Turkiston» qanday shuhrat qozongan?", "o‘zbek tilidagi ilk tarixiy asar", "birinchi rus tilidagi tarix", "birinchi darslik", "birinchi gazeta", "O‘zbek tilidagi ilk tarixiy asar.")
t.B("Ulug‘bek rasadxonasi qoldiqlari qachon topilgan?", "1908-yilda", "1898-yilda", "1917-yilda", "1886-yilda", "1908-yilda.")
t.B("Hududni xaritalash va iqlimni o‘rganish uchun Toshkentda nima tashkil etilgan?", "meteorologiya stansiyasi", "rasadxona", "universitet", "muzey", "Meteorologiya stansiyasi.")
t.B("Pomir tog‘ tizimini o‘rgangan olim kim?", "N. A. Seversev", "P. P. Semyonov-Tyan-Shanskiy", "A. Middendorf", "V. Bartold", "N. A. Seversev.")
t.B("Tyanshan tog‘ tizimini o‘rgangan olim kim?", "P. P. Semyonov-Tyan-Shanskiy", "N. A. Seversev", "Middendorf", "Ostroumov", "Semyonov-Tyan-Shanskiy.")
t.B("Turkiston qishloq xo‘jaligi jamiyati qaysi jurnalni nashr ettirgan?", "«Turkistonning qishloq xo‘jaligi»", "«Oyina»", "«Shuhrat»", "«Izhor ul-Haq»", "«Turkistonning qishloq xo‘jaligi».")
t.B("Ayollarning huquqsiz ahvoli haqida yozgan shoira kim?", "Anbar otin", "Nodira", "Uvaysiy", "Zebuniso", "Anbar otin.")
t.B("Abdulla Qodiriy ilk nasriy asarlarini qachon e’lon qilgan?", "1910-yilda", "1926-yilda", "1898-yilda", "1917-yilda", "1910-yilda.")
t.B("1886-yilda Toshkentda Rossiya Xalq maorifi vazirligiga tegishli nechta ta’lim muassasasi bo‘lgan?", "9 ta", "14 ta", "90 ta", "1 ta", "9 ta (1889-yilda 14 ta).")
t.B("Xudoybergan Devonov qachon tug‘ilgan?", "1878-yilda", "1903-yilda", "1886-yilda", "1868-yilda", "1878-yilda.")
t.B("Xudoybergan Devonov qachondan Xivani suratga ola boshlagan?", "1903-yildan", "1878-yildan", "1910-yildan", "1920-yildan", "1903-yildan.")
t.B("Fotosuratchi Devonovni kim o‘z himoyasiga olgan?", "Muhammad Rahimxon II", "Asfandiyorxon", "Islomxo‘ja", "amir Olimxon", "Muhammad Rahimxon II.")
t.B("Sitorai Mohi Xosa qurilishida ganchkorlarga kim boshchilik qilgan?", "Usta Shirin Murodov", "Xudoybergan Devonov", "Ahmad Donish", "Abdulxoliq maxdum", "Usta Shirin Murodov.")
t.B("XIX asr oxirida qurilgan yuksak milliy me’morchilik namunasi qaysi?", "Andijon jome masjidi", "Sitorai Mohi Xosa", "Kaltaminor", "Chor Minor", "Andijon jome masjidi.")
t.B("Chang qaysi turdagi cholg‘u asbobi?", "torli-zarbli", "puflama nayli", "torli-kamonchali", "zarbli-membranali", "Torli-zarbli.")
t.B("Yaralarni tuzatuvchi an’anaviy tabiblar qanday atalgan?", "rishtachilar", "siniqchilar", "zulukchilar", "doyalar", "Rishtachilar.")
t.NAT("Mutaxassislar yetishmasdi.", "uzoq vaqt keng ko‘lamli ilmiy tadqiqotlar amalga oshirilmadi", "tadqiqotlar tez rivojlandi", "universitetlar ochildi", "olimlar ko‘paydi", "Tadqiqotlar sust bo‘ldi.")
t.NAT("Devonov Xivani suratga ola boshladi.", "bu diniy ulamolarning qattiq qarshiligiga uchradi, ammo xon uni himoya qildi", "ulamolar uni qo‘llab-quvvatladi", "xon uni surgun qildi", "suratga olish taqiqlandi", "Xon himoyasi.")
t.NAT("XIX asr ikkinchi yarmida Farg‘ona vodiysiga Yevropa me’moriy uslubi kirib keldi.", "Yevropa va Sharq me’morchilik an’analari uyg‘unlashdi", "milliy me’morchilik yo‘qoldi", "qurilish to‘xtadi", "faqat Yevropa binolari qurildi", "Uslublar uyg‘unlashdi.")
t.NAT("XX asr boshlarida devoriy naqshlarda yangi manzaralar paydo bo‘ldi.", "suzayotgan kema, temiryo‘llar va hayvonlar tasvirlari ishlatila boshlandi", "naqshlar taqiqlandi", "faqat geometrik naqsh qoldi", "naqshchilik yo‘qoldi", "Yangi tasvirlar.")
t.TF("Mahalliy iqlimga moslashgan O‘rta Osiyo paxta navidan dastlabki hosil olingan.", True, "To‘g‘ri.")
t.TF("Toshkentning Yangi shahar qismida qurilgan ma’muriy binolar sharqona uslubda bo‘lgan.", False, "Noto‘g‘ri: g‘arb muhiti va uslubida qurilgan.")
t.TF4([("Muqimiy, Furqat, Zavqiy bu davr adabiyoti namoyandalari.", True), ("Devonov arab, fors, rus va nemis tillarini o‘rgangan.", True),
       ("Tasviriy san’at Samarqand, Qo‘qon, Buxoro miniatyurachilari ijodida namoyon bo‘lgan.", True), ("1870-yilda o‘quv bo‘limi komissiyasi Samarqandda ish boshlagan.", False)],
      "4-noto‘g‘ri: komissiya Toshkentda ish boshlagan.")
t.MUL([("Xorazm me’morchiligida arabiy yozuvlar binolar bezagiga uyg‘unlashtirilgan.", True),
       ("Tabiblar oltingugurt va azot kislotasi tayyorlashni bilgan.", True),
       ("Maqomlar yozma notalar asosida o‘rganilgan.", False)],
      "III noto‘g‘ri: maqomlar og‘zaki an’ana xazinasi bo‘lgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["mustamlakachilar rus maktablari loyihasi bo‘yicha ko‘rsatma berdi", "Toshkentda o‘quv bo‘limi komissiyasi ish boshladi", "Toshkentda 9 ta rus ta’lim muassasasi", "Devonov Xivani suratga ola boshladi", "Ulug‘bek rasadxonasi qoldiqlari topildi", "Qodiriy ilk nasriy asarlarini e’lon qildi"],
      "1868 → 1870 → 1886 → 1903 → 1908 → 1910.")
t.MATCH("Cholg‘ularni turi bilan moslashtiring.", ["g‘ijjak", "dutor", "karnay", "doira"],
        ["torli-kamonchali", "torli-noxunli", "munshtuk-puflamali", "zarbli-membranali", "torli-zarbli"], 'abcd',
        "G‘ijjak – kamonchali; dutor – noxunli; karnay – munshtukli; doira – membranali.")
t.VENN("Fan (tadqiqotlar)", "Adabiyot",
       [("Seversev – Pomir", 1), ("Ulug‘bek rasadxonasi qoldiqlari topildi", 1),
        ("Anbar otin she’rlari", 2), ("Qodiriyning ilk nasriy asarlari", 2),
        ("XIX asr oxiri – XX asr boshi Turkiston madaniyati", 3)],
       "Fan – Seversev, rasadxona; adabiyot – Anbar otin, Qodiriy; ikkalasi davr madaniyati.")
t.MAPMATCH('uzb', ['Samarqand', 'Buxoro', 'Andijon', 'Xiva'],
           ["1908-yilda Ulug‘bek rasadxonasi qoldiqlari topilgan shahar", "Sitorai Mohi Xosa qurilgan shahar", "XIX asr oxirida qurilgan jome masjidi mashhur shahar", "Xudoybergan Devonov suratga olgan minoralar shahri"],
           "1 – Samarqand; 2 – Buxoro; 3 – Andijon; 4 – Xiva.")

# 14-mavzu. 1917-yil fevral–oktyabr
t = Topic('y10u14', 10014); TOPICS['y10u14'] = t
t.B("Turkiston jadidlari taraqqiyotga qanday yo‘l bilan erishishni mo‘ljallagan?", "tinchlik yo‘li bilan, parlament orqali", "qurolli qo‘zg‘olon orqali", "Rossiyaga qo‘shilish orqali", "xonlarni tiklash orqali", "Tinch, parlament yo‘li.")
t.B("«Rusiyada bosh ko‘targan yangi bir balo – bolshevik balosi» deb kim yozgan?", "Abdurauf Fitrat", "Behbudiy", "Munavvarqori", "Avloniy", "Abdurauf Fitrat.")
t.B("«Haq olinur, berilmas!» shiorini kim o‘rtaga tashlagan?", "Mahmudxo‘ja Behbudiy", "Fitrat", "Munavvarqori", "Cho‘qayev", "Behbudiy.")
t.B("Nikolay II taxtdan qachon voz kechgan?", "1917-yil 15-martda", "1917-yil 25-oktyabrda", "1916-yilda", "1918-yilda", "1917-yil 15-mart.")
t.B("Nikolay II dan so‘ng hokimiyatga kim keldi?", "Muvaqqat hukumat", "bolsheviklar", "Duma", "Sovetlar", "Muvaqqat hukumat.")
t.B("Eski ma’muriyat o‘rniga qanday qo‘mitalar tuzilgan?", "jamoat xavfsizligi qo‘mitalari", "inqilobiy qo‘mitalar", "kambag‘allar qo‘mitasi", "harbiy qo‘mitalar", "Jamoat xavfsizligi qo‘mitalari.")
t.B("«Sho‘royi islomiya»ga kim rahbarlik qilgan?", "Munavvarqori Abdurashidxonov", "Behbudiy", "Fitrat", "Avloniy", "Munavvarqori.")
t.B("«Sho‘royi islomiya» qachon tashkil topgan?", "1917-yil mart oyida", "1917-yil iyunda", "1917-yil iyulda", "1917-yil oktyabrda", "1917-yil mart.")
t.B("1917-yil iyunda «Sho‘royi islomiya»dan qaysi tashkilot ajralib chiqqan?", "«Sho‘royi ulamo»", "«Turk adami markaziyat firqasi»", "«Ittifoq»", "«Tarbiyai atfol»", "«Sho‘royi ulamo».")
t.B("«Turkiston federalistlar partiyasi» qanday nom bilan ham atalgan?", "«Turk adami markaziyat firqasi»", "«Sho‘royi ulamo»", "«Milliy markaz»", "«Ittifoq»", "«Turk adami markaziyat firqasi».")
t.B("Butunturkiston musulmonlarining birinchi o‘lka qurultoyi qachon bo‘lgan?", "1917-yil 16–23-aprelda", "1917-yil 26–28-noyabrda", "1917-yil 15-martda", "1917-yil 25-oktyabrda", "1917-yil 16–23-aprel, Toshkent.")
t.B("Birinchi o‘lka qurultoyida nechtaga yaqin delegat qatnashgan?", "150 ga yaqin", "15 ga yaqin", "1500 ga yaqin", "500 ga yaqin", "150 ga yaqin.")
t.B("Qurultoyda tuzishga kelishilgan Markaziy Sho‘ro keyinchalik qanday shaklda amalga oshirildi?", "Milliy markaz", "Kraykom", "Turkkomissiya", "Sovnarkom", "Milliy markaz (Kraymussovet).")
t.B("Bolsheviklar Rossiyada qachon to‘ntarish yasab hokimiyatni egallagan?", "1917-yil 25-oktyabrda", "1917-yil 15-martda", "1917-yil 16-aprelda", "1918-yil fevralda", "1917-yil 25-oktyabr.")
t.NAT("1917-yil fevralda Rossiyada davlat to‘ntarishi bo‘ldi.", "Turkiston musulmon aholisi siyosiy jihatdan uyg‘ondi, jadidlar milliy demokratik kuchlar o‘zagiga aylandi", "Turkistonda hech narsa o‘zgarmadi", "jadidlar tarqatildi", "xonliklar tiklandi", "Siyosiy uyg‘onish.")
t.NAT("Birinchi o‘lka qurultoyi 20 ga yaqin masalani ko‘rib chiqdi.", "mustamlakachilikni tugatish va musodara qilingan yerlarni qaytarish haqida qaror qabul qilindi", "qurultoy bolsheviklarni qo‘llab-quvvatladi", "qurultoy tarqatildi", "Rossiyaga qo‘shilish qarori qabul qilindi", "Mustamlakachilikni tugatish qarori.")
t.NAT("Urushdagi muvaffaqiyatsizlik, iqtisodiy inqiroz va ocharchilik boshlandi.", "ommaning noroziligi kuchayib, bolsheviklar hokimiyatni egalladi", "Muvaqqat hukumat kuchaydi", "Nikolay II qaytdi", "urush g‘alaba bilan tugadi", "Bolsheviklar to‘ntarishi.")
t.NAT("Muvaqqat hukumat, Sovetlar va jadidlarning Milliy markazi bir vaqtda faoliyat yuritdi.", "Turkistonda uch hokimiyatchilik paydo bo‘ldi", "yagona hokimiyat o‘rnatildi", "ikki hokimiyatchilik bo‘ldi", "hokimiyat Buxoroga o‘tdi", "Uch hokimiyatchilik.")
t.TF("«Haq olinur, berilmas!» shiori butun millatning jangovar chaqirig‘iga aylandi.", True, "To‘g‘ri.")
t.TF("Turkistonda ham Rossiyadagi kabi ikki hokimiyatchilik vujudga kelgan.", False, "Noto‘g‘ri: uch hokimiyatchilik paydo bo‘lgan.")
t.TF4([("Uch hokimiyatchilikdan biri Muvaqqat hukumatning Turkiston komiteti edi.", True), ("Ishchi va askar deputatlarining Sovetlari ham hokimiyat da’vo qilgan.", True),
       ("«Turk adami markaziyat firqasi» 1917-yil iyulda ajralib chiqqan.", True), ("Birinchi o‘lka qurultoyi Samarqandda o‘tgan.", False)],
      "4-noto‘g‘ri: qurultoy Toshkentda o‘tgan.")
t.MUL([("Bolsheviklar avombop shiorlar bilan omma e’tiborini qozongan.", True),
       ("Milliy tashkilotlar tarqoq kuchlarni jipslashtirishga ilk urinish bo‘lgan.", True),
       ("Fitrat bolsheviklarni xalq uchun najot deb baholagan.", False)],
      "III noto‘g‘ri: Fitrat ularni «bolshevik balosi» deb atagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Nikolay II taxtdan voz kechdi", "«Sho‘royi islomiya» tuzildi", "birinchi o‘lka qurultoyi", "«Sho‘royi ulamo» ajralib chiqdi", "«Turk adami markaziyat firqasi» ajralib chiqdi", "bolsheviklar to‘ntarishi"],
      "15-mart → mart → aprel → iyun → iyul → 25-oktyabr (1917).")
t.MATCH("Uch hokimiyatchilikni moslashtiring.", ["birinchisi", "ikkinchisi", "uchinchisi", "Milliy markaz"],
        ["Muvaqqat hukumatning Turkiston komiteti", "ishchi va askar deputatlari Sovetlari", "«Sho‘royi islomiya» va shu’balari", "Turkiston o‘lka musulmonlari soveti (Kraymussovet)", "amir hukumati"], 'abcd',
        "1 – Turkiston komiteti; 2 – Sovetlar; 3 – Sho‘royi islomiya; Milliy markaz – Kraymussovet.")
t.VENN("«Sho‘royi islomiya»", "«Sho‘royi ulamo»",
       [("1917-yil martda tuzilgan", 1), ("Munavvarqori rahbarligida", 1),
        ("1917-yil iyunda ajralib chiqqan", 2), ("ulamolar tashkiloti", 2),
        ("1917-yildagi milliy-siyosiy tashkilot", 3)],
       "Sho‘royi islomiya – mart, Munavvarqori; Sho‘royi ulamo – iyun, ulamolar; ikkalasi milliy tashkilot.")
t.MAPN('uzb', ['Toshkent', 'Samarqand', 'Qo‘qon', 'Buxoro'], "1917-yil 16–23-aprelda Butunturkiston musulmonlarining birinchi o‘lka qurultoyi o‘tgan shahar xaritada qaysi raqamda?",
       "Toshkent.")
