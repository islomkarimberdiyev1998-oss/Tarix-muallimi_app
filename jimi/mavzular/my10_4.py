from qlib import Topic, PLACES, REG
TOPICS = {}
W = 'globe'; EU = 'europe'

# 9 Birinchi jahon urushi
t = Topic('y10j9', 10009); TOPICS['y10j9'] = t
t.B("Uchlar ittifoqi qachon tashkil qilingan?", "1882-yilda", "1904–1907-yillarda", "1914-yilda", "1871-yilda", "1882-yili.")
t.B("Uchlar ittifoqiga qaysi davlatlar kirgan?", "Germaniya, Avstriya-Vengriya, Italiya", "Angliya, Fransiya, Rossiya", "Germaniya, Turkiya, Yaponiya", "AQSH, Angliya, Fransiya", "Germaniya, Avstriya-Vengriya va Italiya.")
t.B("Antanta qaysi yillarda shakllangan?", "1904–1907-yillarda", "1882-yilda", "1914-yilda", "1918-yilda", "1904–1907-yillari.")
t.B("Antantaga qaysi davlatlar kirgan?", "Buyuk Britaniya, Fransiya, Rossiya", "Germaniya, Avstriya-Vengriya, Italiya", "AQSH, Yaponiya, Xitoy", "Turkiya, Bolgariya, Germaniya", "Buyuk Britaniya, Fransiya va Rossiya.")
t.B("XIX asrning oxirgi 30 yilida qaysi davlatlar ilg‘or industrial davlatlar qatoriga kirib olgan?", "AQSH va Germaniya", "Angliya va Fransiya", "Rossiya va Italiya", "Yaponiya va Xitoy", "AQSH va Germaniya.")
t.B("Frans Ferdinand qachon o‘ldirilgan?", "1914-yil 28-iyunda", "1914-yil 28-iyulda", "1914-yil 1-avgustda", "1914-yil 23-iyulda", "1914-yil 28-iyunda Sarayevoda.")
t.B("Frans Ferdinandni kim otib o‘ldirgan?", "Gavrilo Prinsip", "Vilgelm II", "Anvar posho", "Sun Yatsen", "«Mlada Bosna» a’zosi Gavrilo Prinsip.")
t.B("Gavrilo Prinsip qaysi tashkilot a’zosi bo‘lgan?", "«Mlada Bosna» («Yosh Bosniya»)", "«Yosh Turkiya»", "Gomindan", "Antanta", "«Mlada Bosna» («Yosh Bosniya»).")
t.B("Avstriya-Vengriya Serbiyaga qachon urush e’lon qilgan?", "1914-yil 28-iyulda", "1914-yil 23-iyulda", "1914-yil 28-iyunda", "1914-yil 4-avgustda", "23-iyulda ultimatum, 28-iyulda urush.")
t.B("Germaniya Rossiyaga qachon urush e’lon qilgan?", "1-avgustda", "3-avgustda", "4-avgustda", "28-iyulda", "1-avgustda Rossiyaga, 3-avgustda Fransiyaga.")
t.B("Angliya Germaniyaga qachon urush e’lon qilgan?", "1914-yil 4-avgustda", "1914-yil 1-avgustda", "1914-yil 3-avgustda", "1915-yilda", "4-avgust kuni.")
t.B("Germaniya va uning ittifoqchilari tomonida qaysi davlat urushga qo‘shilgan?", "Turkiya", "Yaponiya", "AQSH", "Italiya", "Germaniya tomonida Turkiya qo‘shildi; Yaponiya Germaniyaga urush e’lon qildi.")
t.B("Nemislar Verdenda hujumni qachon boshlagan?", "1916-yil fevralda", "1914-yil avgustda", "1917-yil bahorda", "1918-yil avgustda", "1916-yil fevralda.")
t.B("Verden jangida Germaniya qancha kishidan ayrilgan?", "600 ming", "360 ming", "1 mln", "74 mln", "Germaniya 600 ming, fransuzlar 360 ming kishini yo‘qotdi.")
t.B("1918-yil o‘rtalariga kelib AQSH Yevropaga qancha qo‘shin kiritgan?", "1 mln ga yaqin", "100 ming", "5 mln", "13 mln", "1 mln ga yaqin qo‘shin.")
t.B("Germaniya delegatsiyasi Antanta shartlarini qachon imzolagan?", "1918-yil 11-noyabrda", "1919-yil 28-iyunda", "1918-yil avgustda", "1917-yil fevralda", "1918-yil 11-noyabr kuni.")
t.B("Birinchi jahon urushida nechta davlat qatnashgan?", "38 ta", "27 ta", "12 ta", "74 ta", "38 ta davlat.")
t.B("Birinchi jahon urushida qancha kishi safarbar qilingan?", "74 mln dan ortiq", "1,5 mlrd", "38 mln", "600 ming", "74 mln dan ortiq kishi safarbar qilindi.")
t.NAT("Rossiya Germaniya ultimatumiga javob bermadi.", "Germaniya Rossiyaga, so‘ng Fransiyaga urush e’lon qildi", "Rossiya safarbarlikni to‘xtatdi", "Germaniya Rossiya bilan ittifoq tuzdi", "Serbiya taslim bo‘ldi", "1-avgustda Rossiyaga, 3-avgustda Fransiyaga urush e’lon qilindi.")
t.NAT("G‘oliblar Germaniyani talab, tiz cho‘ktirishga harakat qildi.", "revanshizm paydo bo‘lib, fashistlarning hokimiyatga kelishi osonlashdi", "Germaniya tinchliksevar bo‘ldi", "Antanta tarqaldi", "Germaniya mustamlakalari ko‘paydi", "Revanshizm fashistlarga yo‘l ochdi.")
t.TF("Verdendagi o‘n oylik jang maqsadsiz qirg‘inning ramziga aylangan.", True, "To‘g‘ri.")
t.TF("Serbiya Avstriya-Vengriya ultimatumining barcha talablarini qat’iyan rad etgan.", False, "Noto‘g‘ri: Serbiya deyarli barcha talablarni qondirishga rozi bo‘ldi.")
t.MUL([("1914-yil avgustda Yaponiya Germaniyaga urush e’lon qilgan.", True),
       ("1917-yil yozda Fransiya armiyasida tartibsizliklar boshlangan.", True),
       ("Birinchi jahon urushi Serbiya va Belgiya uchun ham bosqinchilik xarakteridagi urush bo‘lgan.", False)],
      "III noto‘g‘ri: Serbiya, Chernogoriya, Belgiya va ozodlik uchun kurashgan xalqlar bundan mustasno edi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Uchlar ittifoqi tuzildi", "Antanta shakllandi", "Frans Ferdinand o‘ldirildi", "Avstriya-Vengriya Serbiyaga urush e’lon qildi", "Verden jangi boshlandi", "Germaniya taslim shartlarini imzoladi"],
      "1882 → 1904–1907 → 1914-yil 28-iyun → 1914-yil 28-iyul → 1916 → 1918.")
t.VENN("Uchlar ittifoqi", "Antanta",
       [("Germaniya", 1), ("Avstriya-Vengriya", 1),
        ("Buyuk Britaniya", 2), ("Rossiya", 2),
        ("harbiy-siyosiy blok", 3)],
       "Uchlar ittifoqi – Germaniya, Avstriya-Vengriya, Italiya; Antanta – Britaniya, Fransiya, Rossiya; ikkalasi harbiy-siyosiy blok.")
t.MAPMATCH(EU, ['Sarayevo', 'Verden', 'Serbiya', 'Belgiya'],
           ["1914-yil 28-iyunda Frans Ferdinand o‘ldirilgan shahar", "1916-yilda o‘n oylik jang bo‘lgan joy", "1914-yil 28-iyulda Avstriya-Vengriya urush e’lon qilgan davlat", "urush bosqinchilik xarakteriga ega bo‘lmagan, ozodlik uchun kurashgan davlat (Chernogoriya bilan)"],
           "1 – Sarayevo; 2 – Verden; 3 – Serbiya; 4 – Belgiya.")

# 10 Liberal-demokratik mamlakatlar
t = Topic('y10j10', 10010); TOPICS['y10j10'] = t
t.B("Birinchi jahon urushidan so‘ng qaysi imperiyalar tarqalib ketgan?", "Germaniya, Avstriya-Vengriya, Rossiya va Usmoniylar", "Britaniya va Fransiya", "Yaponiya va Xitoy", "AQSH va Ispaniya", "To‘rt imperiya tarqalib ketdi.")
t.B("Parij tinchlik konferensiyasi qayerda o‘tgan?", "Versal saroyida", "Vashingtonda", "Londonda", "Berlinda", "Parij yaqinidagi Versal saroyida.")
t.B("Parij tinchlik konferensiyasi qachon o‘tgan?", "1919-yil 18-yanvar – 1920-yil 21-yanvar", "1918-yil 11-noyabr", "1921-yil noyabr – 1922-yil fevral", "1919-yil 28-iyun", "1919-yil 18-yanvardan 1920-yil 21-yanvargacha.")
t.B("Parij konferensiyasida nechta davlat vakillari qatnashgan?", "27 ta", "38 ta", "12 ta", "4 ta", "27 davlat vakillari.")
t.B("Germaniya Versal tinchlik shartnomasini qachon imzolagan?", "1919-yil 28-iyunda", "1919-yil 18-yanvarda", "1920-yil 21-yanvarda", "1918-yil 11-noyabrda", "1919-yil 28-iyunda.")
t.B("Millatlar Ligasi qachon tashkil qilingan?", "1919-yilda", "1921-yilda", "1933-yilda", "1918-yilda", "1919-yili.")
t.B("Mag‘lublar mustamlakalarini bo‘lib olishni qonunlashtirish uchun Liga Ustaviga qanday tushuncha kiritilgan?", "mandat", "izolyatsionizm", "reparatsiya", "dominion", "Mandat tushunchasi kiritildi.")
t.B("Vashington konferensiyasi qachon bo‘lgan?", "1921-yil noyabr – 1922-yil fevral", "1919–1920-yillarda", "1929-yilda", "1933-yilda", "1921-yil noyabr – 1922-yil fevral.")
t.B("1919–1923-yillardagi xalqaro munosabatlar tizimi qanday nom olgan?", "Versal-Vashington tizimi", "Vena tizimi", "Antanta", "Panamerika tizimi", "Versal-Vashington tizimi.")
t.B("Jahon iqtisodiy inqirozi qachon va qayerda boshlangan?", "1929-yil 24-oktyabrda Nyu-York fond birjasida", "1932-yil noyabrda Vashingtonda", "1930-yilda Parijda", "1934-yilda Londonda", "1929-yil 24-oktyabrda Nyu-York fond birjasida.")
t.B("1929–1932-yillarda AQSHda sanoat ishlab chiqarish hajmi qanchaga qisqargan?", "50% ga", "10% ga", "90% ga", "25% ga", "50% ga qisqardi.")
t.B("Inqiroz yillarida AQSHda qancha kishi ish joyidan mahrum bo‘lgan?", "13 millionga yaqin", "1 million", "74 million", "600 ming", "13 millionga yaqin kishi.")
t.B("1932-yil noyabrdagi saylovlarda kim g‘olib chiqqan?", "Franklin Ruzvelt", "Teodor Ruzvelt", "Vudro Vilson", "Uinston Cherchill", "«Yangi kurs» va’da qilgan Franklin Ruzvelt.")
t.B("AQSH SSSR bilan diplomatik munosabatlarni qachon o‘rnatgan?", "1933-yilda", "1929-yilda", "1935-yilda", "1922-yilda", "1933-yili.")
t.B("Boshqa davlatlar ishlariga aralashmaslik g‘oyasiga asoslangan tashqi siyosat nima deb ataladi?", "izolyatsionizm", "revanshizm", "panamerikanizm", "mandat", "Izolyatsionizm.")
t.B("Buyuk Britaniya qachondan inqirozdan chiqa boshlagan?", "1934-yildan", "1929-yildan", "1937-yildan", "1940-yildan", "1934-yildan.")
t.B("1937–1940-yillarda Britaniya hukumatini kim boshqargan?", "Nevill Chemberlen", "Uinston Cherchill", "Lloyd Jorj", "Franklin Ruzvelt", "Konservatorlar yetakchisi Nevill Chemberlen.")
t.B("Versal shartnomasiga binoan Fransiya qaysi hududlarni qaytarib olgan?", "Elzas va Lotaringiya", "Saar va Rur", "Bosniya va Gersegovina", "Transvaal va Oranj", "Elzas va Lotaringiya; Saar havzasini egalladi.")
t.NAT("1938-yili Myunxen kelishuvi imzolandi.", "Chemberlen 1940-yili iste’foga chiqdi, hukumatni Uinston Cherchill boshqardi", "Chemberlen mavqei kuchaydi", "Britaniya izolyatsionizmga o‘tdi", "Fransiya Germaniyaga qo‘shildi", "Myunxen kelishuvi Chemberlenning iste’fosiga sabab bo‘ldi.")
t.NAT("Franklin Ruzvelt «yangi kurs»ni amalga oshirdi.", "1930-yillar ikkinchi yarmida AQSH va kapitalistik dunyo inqirozdan chiqdi", "inqiroz chuqurlashdi", "AQSH izolyatsiyadan chiqib urushga kirdi", "ishsizlar soni 13 mln ga yetdi", "«Yangi kurs» Amerika kapitalizmi xarakterini o‘zgartirdi.")
t.TF("Versal shartnomasiga ko‘ra Germaniya urush boshlanishi uchun yagona javobgar davlat deb e’lon qilingan.", True, "To‘g‘ri.")
t.TF("Fransiyada sanoat ishlab chiqarishi 1930-yillar oxirida inqirozdan oldingi darajadan oshib ketgan.", False, "Noto‘g‘ri: inqirozdan oldingi darajasiga ham yetmadi.")
t.MUL([("1935–1936-yillarda AQSHda neytralitet haqida qonunlar qabul qilingan.", True),
       ("Jahon iqtisodiy inqirozi Britaniya iqtisodiyotiga unchalik katta ta’sir qilmagan.", True),
       ("Vashington konferensiyasida AQSH, Britaniya, Fransiya va Germaniya o‘rtasida shartnoma imzolangan.", False)],
      "III noto‘g‘ri: AQSH, Britaniya, Fransiya va Yaponiya o‘rtasida.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Versal shartnomasi imzolandi", "Vashington konferensiyasi boshlandi", "Nyu-York fond birjasida inqiroz boshlandi", "Franklin Ruzvelt saylandi", "AQSH SSSR bilan diplomatik aloqa o‘rnatdi", "Myunxen kelishuvi"],
      "1919 → 1921 → 1929 → 1932 → 1933 → 1938.")
t.VENN("Parij konferensiyasi", "Vashington konferensiyasi",
       [("Versal saroyida o‘tgan", 1), ("27 davlat qatnashgan", 1),
        ("Uzoq Sharq va Tinch okean muammolari", 2), ("dengizdagi qurollarni cheklash", 2),
        ("Versal-Vashington tizimini shakllantirgan", 3)],
       "Parij – Versal, 27 davlat; Vashington – Tinch okeani, dengiz qurollari; ikkalasi Versal-Vashington tizimi.")
t.MAPMATCH(EU, ['Versal', 'Elzas', 'Saar', 'Myunxen'],
           ["1919–1920-yillarda tinchlik konferensiyasi bo‘lgan joy", "Lotaringiya bilan birga Fransiyaga qaytarilgan hudud", "Fransiya egallagan ko‘mir havzasi", "1938-yilgi kelishuv imzolangan shahar"],
           "1 – Versal; 2 – Elzas; 3 – Saar; 4 – Myunxen.")
