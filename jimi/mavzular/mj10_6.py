from qlib import Topic
TOPICS = {}
W = 'globe'; EU = 'europe'; EA = 'eastasia'; IN = 'india'; LA = 'latam'; AF = 'africa'; OA = 'oldasia'

# 24 XXR 1946–1991
t = Topic('e10j24', 1024); TOPICS['e10j24'] = t
t.B("1945-yilda Xitoyning katta qismini kimning hukumati nazorat qilgan?", "Chan Kayshi (Gomindan)", "Mao Szedun", "Den Syaopin", "Sun Yatsen", "Gomindanchi Chan Kayshi hukumati.")
t.B("Chan Kayshi hukumati BMTda qanday o‘rinni egallagan?", "Xavfsizlik Kengashining doimiy a’zosi", "kuzatuvchi", "a’zo bo‘lmagan", "Bosh kotib", "Xavfsizlik Kengashining beshta doimiy a’zosidan biri.")
t.B("Xitoyda fuqarolar urushi qachon qaytadan boshlangan?", "1946-yil iyunda", "1945-yil avgustda", "1947-yil iyulda", "1949-yilda", "1946-yil iyunda.")
t.B("1947-yilda Chan Kayshi armiyasi kommunistlarning qaysi poytaxtini egallagan?", "Yanan", "Nankin", "Pekin", "Shanxay", "Yanan shahrini.")
t.B("Xalq-ozodlik armiyasi qachon hujumga o‘tgan?", "1947-yil iyulda", "1946-yil iyunda", "1949-yil sentabrda", "1945-yilda", "1947-yil iyulda.")
t.B("Xitoy Xalq Respublikasi qachon e’lon qilingan?", "1949-yil 1-oktabrda", "1949-yil sentabrda", "1952-yil dekabrda", "1946-yilda", "1949-yil 1-oktabr kuni.")
t.B("Kommunistlarga kim katta yordam ko‘rsatgan?", "SSSR", "AQSH", "Yaponiya", "Britaniya", "SSSR iqtisodiy yordam va qurol berdi.")
t.B("«Sotsializm qurish» to‘g‘risidagi qaror qachon qabul qilingan?", "1952-yil dekabrda", "1949-yilda", "1960-yilda", "1981-yilda", "1952-yil dekabrda, 15 yilga mo‘ljallangan.")
t.B("1960-yillardagi ziddiyatli siyosat qanday nomlangan?", "«Katta sakrash»", "«Madaniy inqilob»", "«Qayta qurish»", "«Yangi kurs»", "1960-yillarda «Katta sakrash».")
t.B("Mao vafotidan keyin islohotlar strategiyasini ishlab chiqqan rahbar kim?", "Den Syaopin", "Chan Kayshi", "Sun Yatsen", "Lyu Shaotsi", "Den Syaopin va boshqa pragmatiklar.")
t.B("Xitoyda qishloq xo‘jaligini qayta qurish qachon boshlangan?", "1981-yildan", "1976-yildan", "1989-yildan", "1952-yildan", "1981-yildan.")
t.B("Tyananmin maydonidagi namoyish qachon kuch bilan tarqatilgan?", "1989-yil mayda", "1981-yilda", "1976-yilda", "1991-yilda", "1989-yil mayda Pekinda favqulodda holat e’lon qilindi.")
t.B("BMTda uzoq yillar Xitoy o‘rnini kim egallab turgan?", "Tayvandagi gomindanchilar", "SSSR", "Yaponiya", "Gonkong", "Tayvandagi Chan Kayshi boshchiligidagi gomindanchilar.")
t.B("Xitoy yadro quroliga ega davlatga qachon aylangan (darslik bo‘yicha)?", "1980-yillarda", "1950-yillarda", "1949-yilda", "1990-yillarda", "1980-yillarda.")
t.NAT("1981-yildan qishloq xo‘jaligi keng miqyosda qayta qurildi.", "Xitoy o‘zini oziq-ovqat bilan ta’minlab, eksport qila boshladi", "ocharchilik boshlandi", "kolxozlar kuchaydi", "Xitoy g‘alla import qildi",
      "Oziq-ovqat muammosi hal qilindi.")
t.NAT("1989-yilda Tyananmin namoyishiga qarshi qurolli kuch ishlatildi.", "AQSH Kongressi Xitoyga qarshi sanksiya e’lon qildi", "Xitoy islohotlardan voz kechdi", "Den Syaopin iste’foga chiqdi", "Xitoy BMTdan chiqarildi",
      "Sanksiyaga qaramay islohotlar davom etdi.")
t.TF("1970-yillardan Xitoy Tayvan o‘rniga BMTda o‘z o‘rnini egallagan.", True, "To‘g‘ri.")
t.TF("«Katta sakrash» va «Madaniy inqilob» Xitoyga katta iqtisodiy foyda keltirgan.", False, "Noto‘g‘ri: ular hech qanday foyda keltirmay, ahvolni og‘irlashtirdi.")
t.MUL([("1980-yillar ikkinchi yarmidan SSSR bilan munosabatlar yaxshilangan.", True), ("AQSH Chan Kayshi armiyasini qo‘llab-quvvatlagan.", True), ("1952-yilgi rejalar 15 yilda to‘liq bajarilgan.", False)],
      "III noto‘g‘ri: aksariyati amalga oshmay qoldi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Fuqarolar urushi qayta boshlandi", "Yanan egallandi", "XXR e’lon qilindi", "«Sotsializm qurish» qarori", "Qishloq xo‘jaligi islohoti", "Tyananmin voqealari"],
      "1946 → 1947 → 1949 → 1952 → 1981 → 1989.")
t.MAPMATCH(EA, ['Yanan', 'Pekin', 'Tayvan'],
           ["1947-yilda gomindanchilar egallagan kommunistlar poytaxti", "1949-yilda XXR e’lon qilingan, 1989-yilda Tyananmin voqealari bo‘lgan shahar", "gomindanchilar joylashib olgan orol"], "1 – Yanan; 2 – Pekin; 3 – Tayvan.")
t.VENN("Mao Szedun davri", "Den Syaopin davri",
       [("XXR e’lon qilingan", 1), ("«Katta sakrash» va «Madaniy inqilob»", 1),
        ("1981-yildan qishloq xo‘jaligi islohoti", 2), ("Tyananmin namoyishi tarqatilgan", 2),
        ("kommunistik rejim saqlangan", 3)],
       "Mao – XXR, Katta sakrash. Den – islohotlar, Tyananmin. Ikkalasida kommunistik rejim.")

# 25 Hindiston va Pokiston
t = Topic('e10j25', 1025); TOPICS['e10j25'] = t
t.B("Hindistonda Ta’sis majlisi qachon ochilgan?", "1946-yil 9-dekabrda", "1947-yil 15-avgustda", "1949-yilda", "1945-yilda", "1946-yil 9-dekabrda.")
t.B("Hindistonni ikki davlatga bo‘lishda nima asos qilib olingan?", "aholining hind va musulmon diniy jamoalariga mansubligi", "til farqi", "iqtisodiy rayonlar", "kasta tizimi", "Diniy jamoalarga mansublik.")
t.B("Hindiston va Pokiston qachon mustaqil davlat deb e’lon qilingan?", "1947-yil 15-avgustda", "1946-yil 9-dekabrda", "1949-yilda", "1950-yilda", "1947-yil 15-avgust kuni.")
t.B("Mustaqil Hindiston hukumatini kim boshqargan?", "Javaharlal Neru", "Maxatma Gandi", "Indira Gandi", "Liyoqat Alixon", "Javaharlal Neru.")
t.B("Mustaqil Pokiston hukumatini kim boshqargan?", "Liyoqat Alixon", "Ziyo ul-Haq", "Benazir Bxutto", "Neru", "Liyoqat Alixon.")
t.B("Maxatma Gandi kim tomonidan o‘ldirilgan?", "hind-mutaassib", "ingliz zobiti", "musulmon", "pokistonlik askar", "Musulmonlarni himoya qilganlikda ayblangan Gandi hind-mutaassibi tomonidan o‘ldirildi.")
t.B("Hindistonning yangi Konstitutsiyasi qachon qabul qilingan?", "1949-yilda", "1947-yilda", "1950-yilda", "1966-yilda", "1949-yili.")
t.B("Hindiston–Pokiston urushi qachon boshlangan?", "1965-yilda", "1947-yilda", "1971-yilda", "1977-yilda", "1965-yili.")
t.B("Hindiston va Pokiston o‘rtasida muzokaralar qayerda o‘tgan?", "Toshkentda (1966)", "Dehlida", "Islomobodda", "Moskvada", "1966-yili Toshkentda; Toshkent deklaratsiyasi qabul qilindi.")
t.B("1970-yillarda islohotlar o‘tkazgan Hindiston bosh vaziri kim?", "Indira Gandi", "Javaharlal Neru", "Maxatma Gandi", "Rajiv Gandi", "Indira Gandi.")
t.B("Hindiston qachondan g‘alla bilan o‘zini o‘zi ta’minlay boshlagan?", "1980-yillar o‘rtalaridan", "1950-yillardan", "1966-yildan", "1990-yillardan", "1980-yillar o‘rtalaridan.")
t.B("Buyuk davlatlar mojarolaridan chetda turish siyosati qanday nomlangan?", "«J. Neru kursi»", "«Gandizm»", "«Yangi kurs»", "«Katta sakrash»", "1950-yillarda «J. Neru kursi» shakllandi.")
t.B("Pokistonda 1977-yilgi harbiy to‘ntarishdan keyin hokimiyatga kim kelgan?", "general Ziyo ul-Haq", "Benazir Bxutto", "Liyoqat Alixon", "Pervez Musharraf", "General Ziyo ul-Haq.")
t.B("1988-yilgi saylovlardan so‘ng Pokiston bosh vaziri kim bo‘lgan?", "Benazir Bxutto", "Ziyo ul-Haq", "Indira Gandi", "Liyoqat Alixon", "Benazir Bxutto.")
t.NAT("Hindiston bo‘linishi paytida odamlar ommaviy o‘ldirildi.", "Hindiston va Pokiston o‘rtasida uzoq yillik o‘zaro dushmanlik shakllandi", "ikki davlat birlashdi", "Britaniya qaytib keldi", "Gandi bosh vazir bo‘ldi",
      "Bu dushmanlik hissini shakllantirdi.")
t.NAT("Indira Gandi iqtisodga davlat aralashuvini kamaytiruvchi islohotlar o‘tkazdi.", "sanoat va qishloq xo‘jaligining yillik o‘sishi keskin oshdi", "ocharchilik kuchaydi", "investitsiyalar kamaydi", "inflatsiya to‘xtadi",
      "Natijalar yomon bo‘lmadi, o‘sish keskin oshdi.")
t.TF("Hindiston Osiyo va Afrikada muqim parlament demokratiyasini shakllantira olgan yagona davlat bo‘lgan.", True, "To‘g‘ri.")
t.TF("Agrar islohotdan so‘ng Hindistonda oziq-ovqat muammosi darhol hal bo‘lgan.", False, "Noto‘g‘ri: oziq-ovqat muammosi uzoq vaqt saqlanib qolgan.")
t.MUL([("1949-yilgi Konstitutsiya kastalar tengligini e’lon qilgan.", True), ("Neru Qo‘shilmaslik harakati tashabbuskorlaridan biri edi.", True), ("1990-yilgi saylovda Benazir Bxutto g‘alaba qozongan.", False)],
      "III noto‘g‘ri: 1990-yilgi saylovda Bxutto mag‘lub bo‘lgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Ta’sis majlisi ochildi", "Hindiston va Pokiston mustaqil bo‘ldi", "Hindiston konstitutsiyasi", "Hindiston–Pokiston urushi", "Toshkent deklaratsiyasi", "Pokistonda harbiy to‘ntarish"],
      "1946 → 1947 → 1949 → 1965 → 1966 → 1977.")
t.MAPMATCH('sasia', ['Toshkent', 'Hindiston', 'Pokiston'],
           ["1966-yilda Hindiston va Pokiston deklaratsiyasi qabul qilingan shahar", "hukumatini J. Neru boshqargan davlat", "hukumatini Liyoqat Alixon boshqargan davlat"], "1 – Toshkent; 2 – Hindiston; 3 – Pokiston.")
t.VENN("Hindiston", "Pokiston",
       [("muqim parlament demokratiyasi shakllangan", 1), ("Neru, Indira Gandi rahbarligi", 1),
        ("islom millatni jipslashtiruvchi omil", 2), ("1977-yilda harbiy to‘ntarish bo‘lgan", 2),
        ("1947-yil 15-avgustda mustaqil bo‘lgan", 3)],
       "Hindiston – demokratiya; Pokiston – islom, to‘ntarish. Ikkalasi 1947-yilda mustaqil.")

# 26 Turkiya, Eron, Afg'oniston 1946–1991
t = Topic('e10j26', 1026); TOPICS['e10j26'] = t
t.B("Urushdan keyin Otaturk yo‘lini davom ettirgan Turkiya prezidenti kim?", "Ismet Inyonyu", "Turg‘ut O‘zol", "Kenan Evren", "Sulaymon Demirel", "Ismet Inyonyu.")
t.B("1980-yil sentabrda harbiy to‘ntarishni kim o‘tkazgan?", "general Kenan Evren", "Turg‘ut O‘zol", "Ismet Inyonyu", "Sulaymon Demirel", "General Kenan Evren.")
t.B("Turkiyada yangi konstitutsiya referendumda qachon tasdiqlangan?", "1982-yil noyabrda", "1980-yilda", "1983-yilda", "1989-yilda", "1982-yil noyabrda.")
t.B("1983-yilda Turkiya bosh vaziri bo‘lib, iqtisodiy islohotlar boshlagan kim?", "Turg‘ut O‘zol", "Kenan Evren", "Sulaymon Demirel", "Ismet Inyonyu", "Turg‘ut O‘zol.")
t.B("Turg‘ut O‘zol prezident etib qachon saylangan?", "1989-yilda", "1983-yilda", "1990-yilda", "1980-yilda", "1989-yilgi saylovlarda.")
t.B("1990-yildan Turkiya bosh vaziri kim bo‘lgan?", "Sulaymon Demirel", "Turg‘ut O‘zol", "Kenan Evren", "Bulent Ejevit", "Sulaymon Demirel.")
t.B("Ingliz va sovet qo‘shinlari Erondan qachon olib chiqilgan?", "1946-yilda", "1941-yilda", "1953-yilda", "1979-yilda", "1946-yili.")
t.B("Eron shohining 1963-yilgi islohotlari umumiy nom bilan qanday atalgan?", "«oq inqilob»", "«yashil inqilob»", "«islom inqilobi»", "«qayta qurish»", "«Oq inqilob».")
t.B("Eron Islom Respublikasi qachon e’lon qilingan?", "1979-yil fevralda", "1963-yilda", "1980-yilda", "1989-yilda", "1979-yil fevralda.")
t.B("Eron-Iroq urushi qaysi yillarda bo‘lgan?", "1980–1988", "1979–1989", "1963–1973", "1988–1991", "1980–1988-yillarda.")
t.B("Eron Islom Respublikasi diniy rahbari kim edi?", "Oyatilloh Ruhulloh Humayniy", "Muhammad Rizo Pahlaviy", "Rizoxon", "Muhammad Dovud", "Oyatilloh Ruhulloh Humayniy.")
t.B("Afg‘oniston shohi Zohirshoh qachon taxtdan ag‘darilgan?", "1973-yilda", "1978-yilda", "1979-yilda", "1963-yilda", "1973-yili; Muhammad Dovud prezident bo‘ldi.")
t.B("1978-yil 27-apreldagi to‘ntarishdan so‘ng Inqilobiy kengashga kim boshchilik qilgan?", "Nur Muhammad Tarakiy", "Hafizullo Amin", "Muhammad Najibullo", "Abdul Qodir", "Nur Muhammad Tarakiy.")
t.B("Afg‘onistonga sovet qo‘shinlarini kiritishni so‘ragan rahbar kim?", "Hafizullo Amin", "Tarakiy", "Muhammad Dovud", "Najibullo", "Hafizullo Amin.")
t.B("1986-yilda Afg‘onistonda hokimiyatga kim kelgan?", "Muhammad Najibullo", "Hafizullo Amin", "Zohirshoh", "Tarakiy", "Muhammad Najibullo.")
t.B("SSSR Afg‘onistondan qo‘shinlarini qachon olib chiqqan?", "1989-yilda", "1986-yilda", "1991-yilda", "1985-yilda", "1989-yili.")
t.NAT("Turg‘ut O‘zol davlat sektorini xususiylashtirib, eksportni rag‘batlantirdi.", "Turkiya jadal rivojlanish yo‘liga tushdi", "Turkiya inqirozga uchradi", "harbiylar hokimiyatni oldi", "Turkiya NATOdan chiqdi",
      "Islohotlar natijasida Turkiya jadal rivojlandi.")
t.NAT("Shoh islohotlari mamlakatni zamonaviylashtirib, dindor mutaassiblarni tashvishga soldi.", "dindorlar boshchiligidagi g‘alayonlar natijasida 1979-yilda shoh rejimi ag‘darildi", "shoh hokimiyati mustahkamlandi", "Eron NATOga kirdi", "oq inqilob davom etdi",
      "Eron Islom Respublikasi e’lon qilindi.")
t.NAT("Afg‘onistonga 1979-yil dekabrda sovet qo‘shinlari kiritildi.", "ahvol og‘irlashib, millionlab kishilar qochoqqa aylandi", "Afg‘oniston gullab-yashnadi", "mujohidlar tarqaldi", "Amin hokimiyatda qoldi",
      "Deyarli ocharchilik boshlandi, millionlab qochoqlar paydo bo‘ldi.")
t.TF("«Oq inqilob»ning o‘n yilida Eron iqtisodiy o‘sish bo‘yicha dunyoda eng yuqori ko‘rsatkichlarga erishgan.", True, "To‘g‘ri.")
t.TF("Turkiya NATO a’zosi bo‘lgani uchun Yevropa Ittifoqiga tezda qabul qilingan.", False, "Noto‘g‘ri: hamon Yevropa Ittifoqiga qabul qilinmagan.")
t.MUL([("Turkiya «Marshall rejasi»ga kiritilgan va NATOga a’zo bo‘lgan.", True), ("1977-yilgi konstitutsiyaga ko‘ra M. Dovud umrbod prezident deb e’lon qilingan.", True), ("Humayniy 1979-yilda vafot etgan.", False)],
      "III noto‘g‘ri: Humayniy 1989-yilda vafot etgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["«Oq inqilob» referendumi", "Zohirshoh ag‘darildi", "Afg‘onistonda aprel to‘ntarishi", "Eron Islom Respublikasi e’lon qilindi", "Eron-Iroq urushi boshlandi", "Sovet qo‘shinlari Afg‘onistondan chiqdi"],
      "1963 → 1973 → 1978 → 1979 → 1980 → 1989.")
t.MAPMATCH('nearest', ['Turkiya', 'Eron', 'Iroq', 'Afg‘oniston'],
           ["1983-yildan O‘zol islohotlari o‘tkazilgan davlat", "1979-yilda Islom Respublikasi e’lon qilingan davlat", "1980-yilda Eronga bostirib kirgan davlat", "1979-yilda sovet qo‘shinlari kiritilgan davlat"],
           "1 – Turkiya; 2 – Eron; 3 – Iroq; 4 – Afg‘oniston.")
t.VENN("Turg‘ut O‘zol islohotlari", "«Oq inqilob»",
       [("Turkiyada 1983-yildan o‘tkazilgan", 1), ("davlat sektori xususiylashtirilgan", 1),
        ("Eronda 1963-yilgi referendum bilan boshlangan", 2), ("dindor mutaassiblar qarshiligiga uchragan", 2),
        ("mamlakatni modernizatsiya qilishga qaratilgan", 3)],
       "O‘zol – Turkiya, xususiylashtirish. Oq inqilob – Eron, mutaassiblar qarshiligi. Ikkalasi modernizatsiya.")
