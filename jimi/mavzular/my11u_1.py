from qlib import Topic, PLACES, REG
TOPICS = {}

# 1-mavzu. Mustaqil O‘zbekistonning tashkil topishi
t = Topic('y11u1', 11001); TOPICS['y11u1'] = t
t.B("O‘zbekiston SSRning Mustaqillik deklaratsiyasi qachon qabul qilingan?", "1990-yil 20-iyunda", "1991-yil 31-avgustda", "1990-yil 24-martda", "1992-yil 8-dekabrda", "1990-yil 20-iyun.")
t.B("Mustaqillik deklaratsiyasi Oliy Sovetning qaysi sessiyasida qabul qilingan?", "II sessiyasida", "VI sessiyasida", "III sessiyasida", "I sessiyasida", "O‘zSSR Oliy Sovetining II sessiyasi.")
t.B("Mustaqillik qaysi sessiyada e’lon qilingan?", "Oliy Kengash XII chaqiriq navbatdan tashqari VI sessiyasi", "Oliy Sovet II sessiyasi", "Oliy Majlis I sessiyasi", "Senat yig‘ilishi", "XII chaqiriq VI sessiyasi, 1991-yil 31-avgust.")
t.B("«Davlat mustaqilligi asoslari to‘g‘risida»gi qonun nechta moddadan iborat?", "17", "64", "128", "7", "17 moddadan.")
t.B("Mustaqillik asoslari to‘g‘risidagi qonunni qanday ta’riflash mumkin?", "«Muvaqqat kichik konstitutsiya»", "«Buyuk xartiya»", "«Deklaratsiya»", "«Manifest»", "«Muvaqqat kichik konstitutsiya».")
t.B("Mustaqillik kuni qaysi sana deb belgilangan?", "1-sentyabr", "31-avgust", "8-dekabr", "20-iyun", "1-sentyabr.")
t.B("Davlat madhiyasi tanlovining birinchi bosqichida nechtadan ortiq madhiya tanlangan?", "70 dan", "3 ta", "7 ta", "100 dan", "70 dan ortiq.")
t.B("Davlat madhiyasi mualliflari kimlar?", "Abdulla Oripov va Mutal Burhonov", "Mirpo‘lat Mirzo va Rustam Abdullayev", "Abdulla Oripov va Baxtiyor Aliyev", "Erkin Vohidov va Mutal Burhonov", "Abdulla Oripov (so‘z) va Mutal Burhonov (musiqa).")
t.B("Konstitutsiya loyihasini tayyorlash komissiyasi necha a’zodan iborat bo‘lgan?", "64", "17", "150", "100", "64 a’zo.")
t.B("O‘zbekiston Respublikasi Konstitutsiyasi qachon qabul qilingan?", "1992-yil 8-dekabrda", "1991-yil 31-avgustda", "1992-yil 2-iyulda", "1990-yil 20-iyunda", "1992-yil 8-dekabr.")
t.B("Davlat bayrog‘i to‘g‘risidagi qonun qachon qabul qilingan?", "1991-yil 18-noyabrda", "1992-yil 2-iyulda", "1992-yil 10-dekabrda", "1992-yil 8-dekabrda", "1991-yil 18-noyabr.")
t.B("Davlat gerbi to‘g‘risidagi qonun qachon qabul qilingan?", "1992-yil 2-iyulda", "1991-yil 18-noyabrda", "1992-yil 10-dekabrda", "1991-yil 1-sentyabrda", "1992-yil 2-iyul.")
t.B("Davlat madhiyasi to‘g‘risidagi qonun qachon qabul qilingan?", "1992-yil 10-dekabrda", "1992-yil 2-iyulda", "1991-yil 18-noyabrda", "1992-yil 8-dekabrda", "1992-yil 10-dekabr.")
t.B("O‘zbekiston SSRda Prezident lavozimi qachon ta’sis etilgan?", "1990-yil 24-martda", "1991-yil 29-dekabrda", "1990-yil 20-iyunda", "1992-yil 8-dekabrda", "1990-yil 24-mart.")
t.B("1991-yil 29-dekabrdagi saylovda Islom Karimov necha foiz ovoz olgan?", "86 foiz", "88,61 foiz", "95 foiz", "64 foiz", "86 foiz.")
t.B("1995-yil 26-martdagi referendum bilan Prezident vakolatlari qachongacha uzaytirildi?", "2000-yilgacha", "2007-yilgacha", "1997-yilgacha", "2016-yilgacha", "2000-yilgacha.")
t.B("Islom Karimov qachon vafot etgan?", "2016-yil 2-sentyabrda", "2016-yil 8-sentyabrda", "2016-yil 4-dekabrda", "2015-yilda", "2016-yil 2-sentyabr.")
t.B("2016-yil 4-dekabrdagi saylovda Shavkat Mirziyoyev necha foiz ovoz olgan?", "88,61 foiz", "86 foiz", "90 foiz", "75 foiz", "88,61 foiz.")
t.B("2016-yilgi saylovda nechta davlatdan kuzatuvchilar qatnashgan?", "46 ta", "32 ta", "193 ta", "143 ta", "46 davlatdan 600 ga yaqin kuzatuvchi.")
t.NAT("Mustaqillik deklaratsiyasi qabul qilindi.", "bu O‘zbekiston mustaqilligi uchun tashlangan ulkan qadam bo‘ldi", "O‘zbekiston darhol BMTga a’zo bo‘ldi", "SSSR mustahkamlandi", "Konstitutsiya qabul qilindi", "Mustaqillik sari ulkan qadam.")
t.NAT("Davlat mustaqilligi asoslari to‘g‘risidagi qonun qabul qilindi.", "O‘zbekistonning huquqiy holati tubdan o‘zgardi, suverenitet asoslari belgilandi", "O‘zbekiston SSSR tarkibida qoldi", "Prezident lavozimi bekor qilindi", "Oliy Kengash tarqatildi", "Suverenitet asoslari.")
t.NAT("Islom Karimov vafotidan so‘ng Oliy Majlis palatalarining qo‘shma qarori qabul qilindi.", "Prezident vazifalarini vaqtincha bajarish Bosh vazir Shavkat Mirziyoyevga yuklandi", "Senat raisi Prezident bo‘ldi", "saylov bekor qilindi", "Vazirlar Mahkamasi tarqatildi", "Vazifa Sh. Mirziyoyevga yuklandi.")
t.NAT("Madhiya tanlovining yakuniy bosqichida deputatlar yashirin ovoz berdi.", "Abdulla Oripov va Mutal Burhonov madhiyasi g‘olib deb topildi", "tanlov bekor qilindi", "eski madhiya qoldirildi", "uch variant birlashtirildi", "Oripov–Burhonov madhiyasi g‘olib.")
t.TF("Ittifoqdosh respublikalar orasida birinchi bo‘lib O‘zSSRda prezidentlik boshqaruvi joriy qilingan.", True, "To‘g‘ri.")
t.TF("Islom Karimov Toshkentdagi qabristonga dafn etilgan.", False, "Noto‘g‘ri: Samarqanddagi Hazrati Xizr qabristoniga dafn etilgan.")
t.TF4([("Konstitutsiya loyihasi 1992-yil 26-sentyabr va 21-noyabrda e’lon qilingan.", True), ("Madhiya tanlovida ijodkorlar taxallus bilan qatnashgan.", True),
       ("2016-yilgi saylovda YXHT kuzatuvchilari birinchi marta to‘laqonli ishtirok etgan.", True), ("Konstitutsiya komissiyasi 1992-yilda tuzilgan.", False)],
      "4-noto‘g‘ri: komissiya 1990-yil 20-iyundayoq tuzilgan.")
t.MUL([("2000, 2007 va 2015-yillarda I. Karimov Prezidentlikka qayta saylangan.", True),
       ("Sh. Mirziyoyev 2016-yilgi saylovda O‘zLiDeP nomzodi bo‘lgan.", True),
       ("Mustaqillik asoslari to‘g‘risidagi qonun 128 moddadan iborat.", False)],
      "III noto‘g‘ri: 17 moddadan iborat.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Prezident lavozimi ta’sis etildi", "Mustaqillik deklaratsiyasi", "Mustaqillik e’lon qilindi", "bayroq to‘g‘risidagi qonun", "gerb to‘g‘risidagi qonun", "Konstitutsiya qabul qilindi"],
      "1990-03-24 → 1990-06-20 → 1991-08-31 → 1991-11-18 → 1992-07-02 → 1992-12-08.")
t.MATCH("Hujjatlarni qabul qilingan sanasi bilan moslashtiring.", ["Mustaqillik deklaratsiyasi", "bayroq to‘g‘risidagi qonun", "Konstitutsiya", "madhiya to‘g‘risidagi qonun"],
        ["1990-yil 20-iyun", "1991-yil 18-noyabr", "1992-yil 8-dekabr", "1992-yil 10-dekabr", "1992-yil 2-iyul"], 'abcd',
        "Deklaratsiya – 1990-06-20; bayroq – 1991-11-18; Konstitutsiya – 1992-12-08; madhiya – 1992-12-10.")
t.VENN("Mustaqillik deklaratsiyasi", "Mustaqillik asoslari to‘g‘risidagi qonun",
       [("1990-yil 20-iyun, Oliy Sovet II sessiyasi", 1), ("mustaqillik uchun dastlabki qadam", 1),
        ("1991-yil 31-avgust, 17 modda", 2), ("«Muvaqqat kichik konstitutsiya»", 2),
        ("O‘zbekiston davlat mustaqilligiga oid hujjat", 3)],
       "Deklaratsiya – 1990; qonun – 1991, 17 modda; ikkalasi mustaqillik hujjati.")
t.MAPN('uzb', ['Samarqand', 'Toshkent', 'Buxoro', 'Xiva'], "Birinchi Prezident Islom Karimov dafn etilgan Hazrati Xizr qabristoni joylashgan shahar xaritada qaysi raqamda?",
       "Samarqand.")

# 2-mavzu. Davlat boshqaruvi tizimi
t = Topic('y11u2', 11002); TOPICS['y11u2'] = t
t.B("BMTga a’zo 193 davlatdan nechtasida Prezident lavozimi ta’sis etilgan?", "143 tasida", "100 tasida", "193 tasida", "50 tasida", "143 tasida.")
t.B("Ministrlar Soveti o‘rniga birinchi bo‘lib qayerda Vazirlar Mahkamasi ta’sis etilgan?", "O‘zbekistonda", "Rossiyada", "Qozog‘istonda", "Ukrainada", "O‘zbekistonda.")
t.B("AQSH va Braziliyada qanday boshqaruv shakli mavjud?", "prezidentlik respublikasi", "parlament respublikasi", "aralash", "monarxiya", "Prezidentlik respublikasi.")
t.B("Germaniya va Italiyada qanday boshqaruv shakli mavjud?", "parlament respublikasi", "prezidentlik respublikasi", "aralash", "konstitutsiyaviy monarxiya", "Parlament respublikasi.")
t.B("Fransiya va Rossiyada qanday boshqaruv shakli mavjud?", "aralash", "parlament", "prezidentlik", "mutlaq monarxiya", "Aralash boshqaruv.")
t.B("1990–1992-yillarda vitse-prezident lavozimiga kim tayinlangan?", "Shukrullo Mirsaidov", "Shavkat Mirziyoyev", "Islom Karimov", "Abdulla Oripov", "Shukrullo Mirsaidov.")
t.B("Vitse-prezidentlik lavozimi qachon tugatilib, Bosh vazir lavozimi joriy etilgan?", "1992-yilda", "1995-yilda", "2003-yilda", "1990-yilda", "1992-yilda.")
t.B("Ikki palatali parlament qaysi referendumdan so‘ng tuzilgan?", "2002-yilgi", "1995-yilgi", "1991-yilgi", "2023-yilgi", "2002-yilgi referendum.")
t.B("Prezidentning hukumat raisi sifatidagi vakolati qachon qonundan bekor qilingan?", "2003-yilda", "2007-yilda", "2011-yilda", "1992-yilda", "2003-yilda (Konstitutsiyadan 2007-yilda).")
t.B("2011-yilgi o‘zgarishlarga ko‘ra Bosh vazir nomzodini kim ko‘rsatadi?", "parlamentda eng ko‘p o‘rin olgan partiya(lar)", "Prezident", "Senat raisi", "Oliy sud", "Eng ko‘p o‘rin olgan partiya.")
t.B("2015-yilda Bosh vazir nomzodini qaysi partiya ilgari surgan?", "O‘zLiDeP", "XDP", "«Milliy tiklanish»", "Ekologik partiya", "O‘zLiDeP.")
t.B("1990–1994-yillarda parlament qanday atalgan?", "Oliy Kengash", "Oliy Majlis", "Senat", "Qurultoy", "Oliy Kengash.")
t.B("Qonunchilik palatasiga 2019-yil 22-dekabrdagi saylov qaysi shior ostida o‘tgan?", "«Yangi O‘zbekiston. Yangi saylovlar»", "«Xalq davlat organlariga emas»", "«Inson qadri uchun»", "«Bir bo‘lsak – yagona xalqmiz»", "«Yangi O‘zbekiston. Yangi saylovlar».")
t.B("Prezident Oliy Majlisga murojaatnomani qachon yo‘llagan?", "2020-yil 24-yanvarda", "2019-yil 22-dekabrda", "2016-yil 8-sentyabrda", "2017-yilda", "2020-yil 24-yanvar.")
t.B("2017-yildan sud qarorlarini ko‘rib chiqish necha bosqichli tizimga o‘tkazildi?", "uch bosqichli", "olti bosqichli", "ikki bosqichli", "besh bosqichli", "Olti bosqichdan uch bosqichga.")
t.B("Oliy sud va Oliy xo‘jalik sudi birlashtirilib qanday organ tuzildi?", "Oliy sud", "Konstitutsiyaviy sud", "Sudyalar oliy kengashi", "Ma’muriy sud", "Yagona oliy organ – Oliy sud.")
t.B("Murdani dafn etilgan joyidan qazib olish qanday ataladi?", "eksgumatsiya", "mediatsiya", "ekspertiza", "sanksiya", "Eksgumatsiya.")
t.B("Nizoni mediator ko‘magida taraflar roziligi bilan hal qilish usuli qanday ataladi?", "mediatsiya", "eksgumatsiya", "arbitraj", "apellyatsiya", "Mediatsiya.")
t.B("Mahkumlarni afv etish to‘g‘risida Sh. Mirziyoyev ilk bor qachon farmon e’lon qilgan?", "2017-yilda", "2016-yilda", "2019-yilda", "2020-yilda", "2017-yilda.")
t.NAT("2017-yilda «Bir sud – bir instansiya» tamoyili joriy etildi.", "har bir ish faqat tegishli instansiyada ko‘rilib, takroriy ko‘rib chiqishlar kamaydi", "sud ishlari ko‘paydi", "nazorat instansiyasi kuchaydi", "sudlar soni kamaydi", "Takroriy ko‘rib chiqish kamaydi.")
t.NAT("Sanksiya berish huquqi prokurorlardan sudlarga o‘tkazildi.", "sudlar eksgumatsiya, lavozimdan chetlashtirish kabi sanksiyalarni bera boshladi", "prokurorlar vakolati kengaydi", "sudlar tugatildi", "advokatlar huquqi cheklandi", "Sudlarga yangi vakolatlar.")
t.NAT("Sudlarda «yagona darcha» tartibi joriy etildi.", "arizalar qaysi sudga taalluqli bo‘lishidan qat’i nazar yagona tartibda qabul qilinadi", "arizalar rad etiladi", "faqat jinoiy ishlar qabul qilinadi", "sudlar yopildi", "Fuqarolarga qulaylik.")
t.NAT("2011-yilda Konstitutsiyaga Bosh vazir nomzodi haqida o‘zgartish kiritildi.", "parlament va siyosiy partiyalarning vakolatlari kengaydi", "Prezident vakolati kengaydi", "partiyalar tugatildi", "Bosh vazir lavozimi bekor qilindi", "Parlament vakolati kengaydi.")
t.TF("O‘zbekistonda uch hokimiyat – qonun chiqaruvchi, ijro etuvchi va sud – mustaqil faoliyat yuritadi.", True, "To‘g‘ri.")
t.TF("2002-yilgi referendumdan so‘ng parlament bir palatali bo‘lib qolgan.", False, "Noto‘g‘ri: ikki palatali bo‘lgan.")
t.TF4([("Senat hududiy deputatlar tomonidan saylanadi.", True), ("Nazorat instansiyasi butunlay bekor qilingan.", True),
       ("Ushlangan shaxsga advokat bilan xoli uchrashuv ta’minlanishi shart.", True), ("1995–2004-yillarda Oliy Majlis ikki palatali bo‘lgan.", False)],
      "4-noto‘g‘ri: 1995–2004-yillarda bir palatali, 250 deputat.")
t.MUL([("Sudyalar oliy kengashi va ma’muriy sudlar tashkil etilgan.", True),
       ("Jinoyat protsessida yarashuv instituti kengaytirilgan.", True),
       ("Vitse-prezidentni xalq to‘g‘ridan to‘g‘ri saylagan.", False)],
      "III noto‘g‘ri: Prezident tayinlagan, Oliy Sovet tasdiqlagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Vazirlar Mahkamasi va vitse-prezident lavozimi", "Bosh vazir lavozimi joriy etildi", "ikki palatali parlament haqida referendum", "Bosh vazir nomzodi haqidagi konstitutsiyaviy o‘zgarish", "sud tizimida uch bosqichli tartib", "Qonunchilik palatasiga «Yangi saylovlar»"],
      "1990 → 1992 → 2002 → 2011 → 2017 → 2019.")
t.MATCH("Mamlakatlarni boshqaruv shakli bilan moslashtiring.", ["AQSH", "Germaniya", "Fransiya", "O‘zbekiston (ilk bosqich)"],
        ["prezidentlik respublikasi", "parlament respublikasi", "aralash boshqaruv", "prezidentlik boshqaruv shakli tanlangan", "mutlaq monarxiya"], 'abcd',
        "AQSH – prezidentlik; Germaniya – parlament; Fransiya – aralash; O‘zbekiston – prezidentlik.")
t.VENN("Qonunchilik palatasi", "Senat",
       [("quyi palata", 1), ("xalq tomonidan saylanadi", 1),
        ("yuqori palata", 2), ("hududiy deputatlar tomonidan saylanadi", 2),
        ("Oliy Majlis tarkibi", 3)],
       "Qonunchilik palatasi – quyi, xalq; Senat – yuqori, hududiy deputatlar; ikkalasi Oliy Majlis.")
t.MAPMATCH('globe', ['Vashington', 'Berlin', 'Moskva', 'Toshkent'],
           ["prezidentlik respublikasi (AQSH) poytaxti", "parlament respublikasi (Germaniya) poytaxti", "aralash boshqaruv (Rossiya) poytaxti", "mustaqillikning ilk bosqichida prezidentlik boshqaruvini tanlagan davlat poytaxti"],
           "1 – Vashington; 2 – Berlin; 3 – Moskva; 4 – Toshkent.")
