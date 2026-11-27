from qlib import Topic, PLACES, REG
TOPICS = {}
W = 'globe'; EU = 'europe'; ME = 'mideast'

# 7 Islom sivilizatsiyasi mamlakatlari
t = Topic('y10j7', 10007); TOPICS['y10j7'] = t
t.B("Islom sivilizatsiyasida intellektual tushkunlik qachondan boshlangan?", "XIII–XIV asrlardan", "XVI asrdan", "XVIII asrdan", "XI asrdan", "XIII–XIV asrlardan boshlangan tushkunlik XVI asrga kelib iqtisodiy-siyosiy inqirozni boshladi.")
t.B("Islom sivilizatsiyasi qachon chuqur intellektual inqirozga yuz tutgan?", "XVII asrga kelib", "XIII asrda", "XX asr boshida", "X asrda", "XVII asrga kelib.")
t.B("XIX asrning oxirgi choragiga kelib Turkiya qanday mamlakatga aylangan?", "yarim mustamlaka, chet el kapitaliga qaram", "dunyoning eng boy davlati", "respublika", "mustamlakachi imperiya", "Yarim mustamlaka, chet el kapitaliga qaram mamlakat.")
t.B("1865-yili Istanbulda tuzilgan maxfiy tashkilot a’zolari o‘zlarini qanday atagan?", "«yangi usmoniylar»", "«qojarlar»", "«ittihodchilar»", "«milliy mudofaa»", "«Yangi usmoniylar»; Yevropada «Yosh Turkiya» deb ataldi.")
t.B("1871-yili «yosh turklar»ning afv etilishiga kim erishgan?", "Mahmud Nadim posho", "Midhat posho", "Anvar posho", "Abdulhamid II", "Sulton Abdulazizning bosh vaziri Mahmud Nadim posho.")
t.B("1876-yili Turkiya taxtiga kim kelgan?", "Abdulhamid II", "Abdulaziz", "Muzaffariddin", "Midhat", "1876-yili Abdulhamid II taxtga keldi.")
t.B("Konstitutsiya loyihasini tayyorlagan buyuk vazir kim?", "Midhat posho", "Talʼat posho", "Jamol posho", "Mahmud Nadim posho", "Midhat posho; konstitutsiya uning nomi bilan ataldi.")
t.B("«Midhat konstitutsiyasi» qachon qabul qilingan?", "1876-yil dekabrda", "1865-yilda", "1878-yil martda", "1908-yilda", "1876-yil dekabrda.")
t.B("«Midhat konstitutsiyasi»da imperiyaning barcha fuqarolari qanday atalgan?", "usmoniylar", "turklar", "musulmonlar", "yangi usmoniylar", "Barcha fuqarolar usmoniylar deb atalib, qonun oldida teng hisoblandi.")
t.B("San-Stefano sulhi qachon imzolangan?", "1878-yil martda", "1877-yil bahorida", "1876-yil dekabrda", "1908-yilda", "1878-yil martda Istanbul yaqinida.")
t.B("San-Stefano sulhining asosiy sharti nima edi?", "mustaqil Bolgariya davlatini tuzish", "Serbiyani Avstriyaga berish", "Misrni Angliyaga berish", "Turkiyani respublika qilish", "Mustaqil Bolgariya davlatini tuzish.")
t.B("1913-yili Turkiyada hokimiyatga kelgan uchlikka kim kirmagan?", "Midhat posho", "Anvar posho", "Talʼat posho", "Jamol posho", "Uchlik: Anvar, Talʼat va Jamol poshlar.")
t.B("Turkiya Germaniya bilan maxfiy shartnomani qachon imzolagan?", "1914-yil avgustda", "1908-yilda", "1913-yilda", "1878-yilda", "1914-yil avgustda.")
t.B("Forsda XIX asr ikkinchi yarmida qaysi sulola hokimiyatda bo‘lgan?", "qojarlar", "usmoniylar", "safaviylar", "manchjurlar", "Qojarlar sulolasi.")
t.B("1879-yili Forsda rus ofitserlari boshchiligida nima tuzilgan?", "kazaklar polki", "majlis", "milliy gvardiya", "Yosh Turkiya", "Kazaklar polki, keyin brigadaga aylantirildi.")
t.B("Forsda burjua-demokratik inqilob qaysi yillarda bo‘lgan?", "1905–1911-yillarda", "1908-yilda", "1876–1878-yillarda", "1914–1918-yillarda", "1905–1911-yillarda.")
t.B("1870–1914-yillarda Turkiya, Misr va Yaqin Sharqqa kiritilgan investitsiyalar barcha investitsiyalarning qancha qismini tashkil qilgan?", "50–60% ini", "10–15% ini", "90% ini", "25% ini", "50–60% ini tashkil qildi.")
t.NAT("1877–1878-yillardagi Rossiya-Turkiya urushida Turkiya armiyasi tor-mor qilindi.", "Abdulhamid II parlamentni tarqatib, «Midhat konstitutsiyasi»ni bekor qildi", "Turkiya respublika bo‘ldi", "konstitutsiya mustahkamlandi", "Turkiya Bolgariyani egalladi", "Sulton vaziyatdan foydalanib yakka hokimiyat o‘rnatdi.")
t.NAT("1908-yili «Yosh turklar» partiyasidan bo‘lgan zobitlar qo‘zg‘olon ko‘tardi.", "feodal-mustabid tuzum ag‘darilib, konstitutsiya tiklandi", "sulton hokimiyati kuchaydi", "Turkiya Rossiyaga qo‘shildi", "parlament tarqatildi", "Yosh turklar inqilobi g‘alaba qozondi.")
t.NAT("Forsda 1905–1911-yillardagi inqilob.", "majlis tuzildi, konstitutsiya qabul qilindi, ammo qojarlar hokimiyati tiklanib, Fors yarim mustamlakaga aylandi", "Fors to‘liq mustaqil bo‘ldi", "Fors Turkiyaga qo‘shildi", "qojarlar butunlay ag‘darildi", "Rossiya va Angliya Forsni ta’sir hududlariga bo‘lib oldi.")
t.TF("Mustamlakachi hukumatlar islom mamlakatlarida qul savdosi, bolalar savdosi va ko‘pxotinlikni bekor qilgan.", True, "To‘g‘ri.")
t.TF("Islom mamlakatlarida Yaponiyadagi kabi an’anaviylik va modernizm uyg‘unlashgan muhit shakllangan.", False, "Noto‘g‘ri: islom mamlakatlarida G‘arbning madaniy ta’siriga qarshi kuchli harakatlar olib borildi.")
t.MUL([("«Midhat konstitutsiyasi»da ikki palatali parlament ko‘zda tutilgan.", True),
       ("Germaniya bilan shartnoma Usmoniylar imperiyasi halokatining muhim sabablaridan biri bo‘lgan.", True),
       ("Forsdagi kazaklar brigadasi shoh rejimining Angliyaga qaramligini kuchaytirgan.", False)],
      "III noto‘g‘ri: Rossiyaga qaramligini kuchaytirdi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["«Yangi usmoniylar» tashkiloti tuzildi", "«Midhat konstitutsiyasi» qabul qilindi", "San-Stefano sulhi", "Forsda kazaklar polki tuzildi", "Yosh turklar inqilobi", "Germaniya bilan maxfiy shartnoma"],
      "1865 → 1876 → 1878 → 1879 → 1908 → 1914.")
t.VENN("Turkiya", "Fors",
       [("«Midhat konstitutsiyasi»", 1), ("Yosh turklar inqilobi", 1),
        ("qojarlar sulolasi", 2), ("kazaklar brigadasi", 2),
        ("yarim mustamlakaga aylangan", 3)],
       "Turkiya – Midhat, yosh turklar; Fors – qojarlar, kazaklar; ikkalasi yarim mustamlaka.")
t.MAPMATCH(ME, ['Istanbul', 'Bolgariya', 'Tehron', 'Misr'],
           ["1865-yilda «yangi usmoniylar» tashkiloti tuzilgan shahar", "San-Stefano sulhi bilan mustaqil davlat tuzilgan hudud", "chet el kapitali qarz bergan Fors poytaxti", "Turkiya va Yaqin Sharq bilan birga investitsiyalarning 50–60% i kiritilgan mamlakat"],
           "1 – Istanbul; 2 – Bolgariya; 3 – Tehron; 4 – Misr.")

# 8 Afrika mamlakatlarida mustamlakachilik
t = Topic('y10j8', 10008); TOPICS['y10j8'] = t
t.B("Qul savdosini taqiqlagan Bryussel konferensiyasi qachon bo‘lgan?", "1889–1890-yillarda", "1884–1885-yillarda", "1876-yilda", "1900-yilda", "1889–1890-yillarda.")
t.B("Qariyb to‘rt asr ichida yevropaliklar Amerikaga qancha qul olib kelgan?", "15–16 million", "60–70 million", "1–2 million", "100 million", "15–16 million qul.")
t.B("Atlantika qul savdosi jarayonida taxminan qancha kishi halok bo‘lgan?", "60–70 million", "15–16 million", "6 million", "1 million", "Taxminan 60–70 million kishi halok bo‘ldi.")
t.B("Qul savdosi qachongacha davom etgan?", "XIX asrning 70-yillarigacha", "XVIII asr oxirigacha", "XX asr boshigacha", "1945-yilgacha", "XIX asrning 70-yillarigacha davom etdi.")
t.B("Qulchilikning eng g‘ayriinsoniy ko‘rinishi qanday mafkura bo‘lgan?", "rasizm (irqchilik)", "liberalizm", "sekulyarlik", "panamerikanizm", "Rasizm (irqchilik) mafkurasi.")
t.B("Qaysi shahar rivojlanishi qul savdosi bilan bog‘liq bo‘lgan?", "Liverpul", "Berlin", "Vena", "Praga", "Bristol, Liverpul, Manchester, London, Nant va boshqalar.")
t.B("Berlin konferensiyasi qaysi yillarda bo‘lgan?", "1884–1885-yillarda", "1889–1890-yillarda", "1876-yilda", "1900-yilda", "1884–1885-yillarda.")
t.B("Berlin konferensiyasi kimlarning tashabbusi bilan chaqirilgan?", "Germaniya va Fransiya", "Angliya va AQSH", "Belgiya va Portugaliya", "Turkiya va Italiya", "Germaniya va Fransiya tashabbusi bilan.")
t.B("Berlin konferensiyasida nechta Yevropa davlati qatnashgan?", "12 ta", "27 ta", "9 ta", "5 ta", "12 Yevropa davlati, AQSH va Turkiya.")
t.B("1885-yilda Berlin konferensiyasini qoralagan Tropik Afrika gazetasi qaysi?", "«Lagos observer»", "«Tayms»", "«Pravda»", "«Gitanjali»", "«Lagos observer» gazetasi.")
t.B("1876-yilgacha Yevropa davlatlari Afrikaning qancha qismini egallagan?", "10% ini", "50% ini", "9/10 qismini", "uchdan birini", "Faqat 10% i egallangan edi.")
t.B("1900-yilga kelib Afrikaning qancha qismi mustamlakachilar qo‘liga o‘tgan?", "9/10 qismi", "10% i", "yarmi", "1/3 qismi", "9/10 qismi.")
t.B("Afrika aholisining qariyb yarmi qaysi davlat bosib olgan hududlarda yashagan?", "Buyuk Britaniya", "Fransiya", "Belgiya", "Germaniya", "Buyuk Britaniya hududlarida.")
t.B("Fransiya mustamlakalarining asosiy qismi qayerda joylashgan?", "G‘arbiy va Ekvatorial Afrikada", "Janubiy Afrikada", "Sharqiy Afrikada", "Madagaskarda", "G‘arbiy va Ekvatorial Afrikada, ancha qismi Sahroyi Kabirda.")
t.B("Mustamlakachilikka qarshi kurashda mashhur bo‘lgan afrikalik rahbar kim?", "Samori", "Sesil Rods", "Kipling", "Vivekananda", "Samori, Behanzin, Raboh, Muhammad ibn Abdulla.")
t.B("Qaysi biri qul savdosidan oldingi Afrika sivilizatsiyasi?", "Monomotapa", "Transvaal", "Oranj", "Lagos", "Gana, Songay, Benin, Monomotapa.")
t.NAT("Qul savdosi to‘rt asr davom etdi.", "Afrika xalqlarining «notarixiyligi» haqidagi g‘ayriilmiy konsepsiyalar paydo bo‘ldi", "Afrika iqtisodi gullab-yashnadi", "rasizm yo‘qoldi", "Afrika sivilizatsiyalari mashhur bo‘ldi", "Yevropaliklar bu konsepsiyalardan bosqinchilikni oqlash uchun foydalandi.")
t.NAT("Tropik Afrikada yangi o‘qimishli qatlam paydo bo‘ldi.", "milliy intelligensiya (ziyolilar) shakllanib bordi", "qabilaviy aloqalar kuchaydi", "qul savdosi qayta tiklandi", "Afrika mustaqil bo‘ldi", "Ana shu qatlam doirasida milliy intelligensiya shakllandi.")
t.TF("Berlin konferensiyasida Afrikaga Yevropa ekspansiyasining obyekti sifatida qaralgan.", True, "To‘g‘ri.")
t.TF("Qul savdosi Buyuk Britaniyada faqat XX asr boshida taqiqlangan.", False, "Noto‘g‘ri: XIX asrning birinchi yarmidayoq rasman taqiqlangan.")
t.MUL([("Berlin konferensiyasi «Qora qit’a» taqdiriga bag‘ishlangan birinchi maxsus yig‘ilish bo‘lgan.", True),
       ("Afrika aholisining qariyb uchdan biri Fransiya mustamlakalarida yashagan.", True),
       ("Birinchi jahon urushi arafasida Afrikani bo‘lib olish hali boshlanmagan edi.", False)],
      "III noto‘g‘ri: urush arafasida bo‘lib olish jarayoni yakunlandi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Afrikaning faqat 10% i egallangan davr tugadi", "Berlin konferensiyasi ochildi", "«Lagos observer» konferensiyani qoraladi", "Bryussel konferensiyasi", "Afrikaning 9/10 qismi egallandi"],
      "1876 → 1884 → 1885 → 1889–1890 → 1900.")
t.VENN("Berlin konferensiyasi", "Bryussel konferensiyasi",
       [("1884–1885-yillarda o‘tgan", 1), ("Germaniya va Fransiya tashabbusi", 1),
        ("1889–1890-yillarda o‘tgan", 2), ("qul savdosini taqiqlagan", 2),
        ("Afrika taqdiriga oid xalqaro yig‘ilish", 3)],
       "Berlin – 1884–1885, Germaniya va Fransiya; Bryussel – 1889–1890, qul savdosi taqiqi; ikkalasi Afrikaga oid.")
t.MAPMATCH(EU, ['Berlin', 'Bryussel', 'Liverpul', 'Nant'],
           ["1884–1885-yillarda Afrika taqdiri muhokama qilingan konferensiya shahri", "1889–1890-yillarda qul savdosini taqiqlagan konferensiya shahri", "qul savdosi hisobiga gullagan ingliz porti (Bristol bilan)", "qul savdosi hisobiga gullagan fransuz shahri (Ruan bilan)"],
           "1 – Berlin; 2 – Bryussel; 3 – Liverpul; 4 – Nant.")
