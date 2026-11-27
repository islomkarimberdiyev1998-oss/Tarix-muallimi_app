from qlib import Topic, PLACES, REG
TOPICS = {}

# 8 Yangi din beshigi
t = Topic('y7j8', 7008); TOPICS['y7j8'] = t
t.B("Arablar qaysi til oilasiga mansub?", "somiy (semit) tillar", "hind-yevropa tillari", "turkiy tillar", "xitoy-tibet tillari", "Somiy (semit) tilli xalqlardan.")
t.B("Ko‘chmanchi arablar qanday atalgan?", "badaviylar", "ansorlar", "muhojirlar", "quraysh", "Badaviylar (sahroyilar).")
t.B("Tarixchilar ma’lumotiga ko‘ra teridan tayyorlanadigan suv idishi – meshni kimlar ixtiro qilgan?", "badaviylar", "finikiyaliklar", "ossuriylar", "yamanliklar", "Badaviylar.")
t.B("Arabistonning yuksak rivojlangan viloyatlari qaysilar bo‘lgan?", "Yaman va Xijoz", "Iroq va Suriya", "Misr va Falastin", "Ummon va Bahrayn", "Yaman va Xijoz.")
t.B("Arablarda «Yaman» so‘zi qanday ma’noni bildirgan?", "«haq», «baxtli»", "«o‘qish»", "«ko‘chish»", "«itoat etish»", "«Haq», «baxtli».")
t.B("Islomgacha Makkadagi umumiy ziyoratgoh qaysi bo‘lgan?", "Ka’ba", "Madina masjidi", "Qubbat as-Saxra", "Ayo Sofiya", "Ka’ba.")
t.B("Muhammad (s.a.v.) qachon tavallud topgan?", "570-yilda", "610-yilda", "622-yilda", "632-yilda", "570-yili Makkada.")
t.B("Muhammad (s.a.v.) qaysi qabila va urug‘dan bo‘lgan?", "quraysh qabilasining hoshimiylar urug‘idan", "Banu Sa’d qabilasidan", "Yamanlik badaviylardan", "Umaviylar urug‘idan", "Quraysh qabilasining hoshimiylar urug‘idan.")
t.B("Muhammad (s.a.v.)ni ko‘chmanchilar orasida tarbiya qilgan ayol kim?", "Halima", "Omina", "Xadicha", "Fotima", "Banu sa’dlik Halima.")
t.B("Bobosi vafotidan so‘ng Muhammad (s.a.v.)ni kim tarbiyalagan?", "amakisi Abu Tolib", "otasi Abdulloh", "bobosi Abdulmuttalib", "Abu Bakr", "Amakisi Abu Tolib.")
t.B("Muhammad (s.a.v.)ga ilohiy oyatlar qachondan nozil bo‘la boshlagan?", "610-yildan", "570-yildan", "622-yildan", "630-yildan", "610-yildan boshlab.")
t.B("Qur’on nechta suradan iborat?", "114 ta", "23 ta", "99 ta", "40 ta", "114 ta suradan.")
t.B("Hijrat qachon bo‘lgan?", "622-yilda", "610-yilda", "630-yilda", "632-yilda", "622-yili; musulmon yil hisobi boshlanishi.")
t.B("Hijratdan so‘ng Yasrib shahri qanday nom olgan?", "Madina", "Makka", "Damashq", "Xalab", "Madina (payg‘ambarlik shahri).")
t.B("Madinada islomni qabul qilganlar qanday atalgan?", "ansorlar", "muhojirlar", "badaviylar", "xorijiylar", "Ansorlar (tarafdorlar).")
t.B("«Islom» so‘zi qanday ma’noni anglatadi?", "«itoat etish», «bo‘ysunish»", "«o‘qish»", "«ko‘chish»", "«o‘rinbosar»", "«Itoat etish», «bo‘ysunish».")
t.B("Muhammad (s.a.v.) Makkani qachon jangsiz egallagan?", "630-yilda", "622-yilda", "632-yilda", "610-yilda", "630-yili.")
t.B("O‘zbekistonda qaysi mazhab keng yoyilgan?", "hanafiylik", "shofe’iylik", "molikiylik", "hanbaliylik", "Hanafiylik mazhabi.")
t.NAT("Makka zodagonlari Muhammad (s.a.v.)ning targ‘ibotlariga qarshi chiqdi.", "622-yilda hijrat – Yasribga ko‘chish amalga oshdi", "islom Makkada taqiqlandi va yo‘qoldi", "Makka Vizantiyaga qo‘shildi", "quraysh zodagonlari darhol islomni qabul qildi", "Muhammad (s.a.v.) va sahobalari Yasribga hijrat qildi.")
t.NAT("630-yilda Makka jangsiz egallandi.", "Ka’badan but va sanamlar chiqarildi, u musulmonlar uchun asosiy ziyoratgohga aylandi", "Makka vayron qilindi", "Ka’ba yopildi", "aholi shaharni tark etdi", "Ka’ba asosiy ziyoratgohga aylandi.")
t.NAT("Urushlarda olingan harbiy o‘ljalar sardorlarni boyitdi.", "mulkiy tabaqalanish kuchayib, urug‘chilik tuzumi inqirozi tezlashdi", "barcha arablar teng boyidi", "arablar ko‘chmanchilikni to‘xtatdi", "Yaman qashshoqlashdi", "Urug‘chilik tuzumi inqirozi tezlashdi.")
t.NAT("Arabiston shaharlari va ko‘chmanchi qabilalari islomni qabul qildi.", "VII asrda ular yagona davlatga birlashdi", "Arabiston parchalanib ketdi", "arablar Vizantiyaga bo‘ysundi", "Ka’ba tashlab ketildi", "VII asrda yagona davlat vujudga keldi.")
t.TF("Islom buddaviylik va xristianlikdan keyingi yana bir jahon dini bo‘lib vujudga kelgan.", True, "To‘g‘ri.")
t.TF("Musulmonlar uchun eng katta bayram – Qurbon hayiti Ramazondan oldin nishonlanadi.", False, "Noto‘g‘ri: eng katta bayram Ramazon hayiti; Qurbon hayiti undan 70 kun keyin.")
t.TF4([("Islom beshta asos (arkon)ga ega.", True), ("Sunniylik to‘rtta fiqhiy mazhabdan iborat.", True),
       ("Xorijiylar yo‘nalishi bugungi kunda musulmonlarning asosiy qismini tashkil etadi.", False), ("Muhammad (s.a.v.) 632-yili Madinada vafot etgan.", True)],
      "3-noto‘g‘ri: xorijiylar VII asr ikkinchi yarmida parchalanib, yo‘qolib ketgan; asosiy qism – sunniylar.")
t.MUL([("Muhammad (s.a.v.) savdo ishlari bilan Xalab va Damashqqa borgan.", True),
       ("Muhammad (s.a.v.) Madinada sudxo‘rlik, ichkilik va qimorni taqiqlagan.", True),
       ("Muhammad (s.a.v.) yigirma yoshida payg‘ambar bo‘lgan.", False)],
      "III noto‘g‘ri: qirq yoshida payg‘ambar bo‘lgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Muhammad (s.a.v.) tavallud topdi", "Oyatlar nozil bo‘la boshladi", "Hijrat", "Makka jangsiz egallandi", "Muhammad (s.a.v.) vafot etdi"],
      "570 → 610 → 622 → 630 → 632.")
t.MATCH("Atamalarni ma’nolari bilan moslashtiring.", ["Qur’on", "hijrat", "mazhab", "muslim"],
        ["«qiroat», «o‘qish»", "«ko‘chib o‘tish»", "«yo‘nalish», «oqim»", "«islomni qabul qilgan», «itoatli»", "«o‘rinbosar»"], 'abcd',
        "Qur’on – o‘qish; hijrat – ko‘chish; mazhab – yo‘nalish; muslim – itoatli.")
t.VENN("Muhojirlar", "Ansorlar",
       [("Makkadan ko‘chib kelganlar", 1), ("622-yilda hijrat qilganlar", 1),
        ("Yasribning mahalliy aholisi", 2), ("Madinada islomni qabul qilganlar", 2),
        ("Madinadagi ilk musulmon jamoasi", 3)],
       "Muhojirlar – Makkadan ko‘chganlar; ansorlar – Madinaliklar; ikkalasi ilk musulmon jamoasi.")
t.MAPMATCH('arabia', ['Makka', 'Madina (Yasrib)', 'Yaman', 'Damashq'],
           ["Ka’ba joylashgan, savdo markazi bo‘lgan shahar", "622-yilda hijrat qilingan shahar", "unumdor yerlari bilan «baxtli» deb atalgan viloyat", "Muhammad (s.a.v.) Xalab bilan birga savdo safari qilgan Suriya shahri"],
           "1 – Makka; 2 – Madina; 3 – Yaman; 4 – Damashq.")

# 9 Arab xalifaligi
t = Topic('y7j9', 7009); TOPICS['y7j9'] = t
t.B("«Xulafoi roshidin» qanday ma’noni anglatadi?", "«to‘g‘ri yo‘ldan boruvchi xalifalar»", "«arab amirlari»", "«payg‘ambar sahobalari»", "«ajralib chiqqanlar»", "«To‘g‘ri yo‘ldan boruvchi xalifalar».")
t.B("Umaviylar sulolasi qaysi yillarda hukmronlik qilgan?", "661–750-yillarda", "750–1258-yillarda", "632–661-yillarda", "786–809-yillarda", "661–750-yillar.")
t.B("«Xalifa» so‘zi qanday ma’noni anglatadi?", "«o‘rinbosar»", "«podsho»", "«hokim»", "«yo‘lboshchi»", "Xalifa – «o‘rinbosar».")
t.B("Birinchi xalifa kim bo‘lgan?", "Abu Bakr", "Umar", "Usmon", "Ali", "Abu Bakr (632–634).")
t.B("Abu Bakr davrida har bir viloyatga kim tayinlangan?", "voliy (hokim)", "sherif", "graf", "vasilevs", "Voliy (hokim).")
t.B("Hijriy yil taqvimi qachon joriy etilgan?", "637-yil aprelda", "622-yilda", "644-yilda", "661-yilda", "637-yil aprelda Umar davrida.")
t.B("Musulmonlar qaysi xalifani «Umari odil» deb atagan?", "Umar", "Usmon", "Abu Bakr", "Muoviya I", "Xalifa Umar.")
t.B("Qaysi xalifa davrida Qur’on matni bir butun kitob shakliga keltirilgan?", "Usmon", "Umar", "Ali", "Abu Bakr", "Usmon (644–656) buyrug‘i bilan.")
t.B("Umaviylar sulolasining asoschisi kim?", "Muoviya I", "Ali ibn Abu Tolib", "Horun ar-Rashid", "Jabal at-Tariq", "661-yilda hokimiyatni Muoviya I egalladi.")
t.B("Umaviylar davrida poytaxt qaysi shahar bo‘lgan?", "Damashq", "Bag‘dod", "Madina", "Kordova", "Damashq.")
t.B("Pireney yarimorolidagi Vestgot qirolligini bo‘ysundirgan qo‘shin boshlig‘i kim?", "Jabal at-Tariq", "Sa’d ibn Abu Vaqqos", "Muoviya I", "Xuloku", "711–714-yillarda Jabal at-Tariq.")
t.B("Arablarning shimolga siljishlari qaysi jangda to‘xtatilgan?", "732-yilgi Puate jangida", "1055-yilda Bag‘dodda", "637-yilda Tustarda", "756-yilda Kordovada", "732-yilgi Puate jangida.")
t.B("Abbosiylar qarorgohini qaysi shaharga ko‘chirgan?", "Bag‘dodga", "Damashqqa", "Qohiraga", "Makkaga", "Bag‘dodga («Xudoning in’omi»).")
t.B("Abbosiylarning eng mashhur xalifasi kim?", "Horun ar-Rashid", "Muoviya I", "Umar", "Abu Bakr", "Horun ar-Rashid (786–809).")
t.B("Xalifalikdan ilk mustaqil amirlik qachon va qayerda ajralib chiqqan?", "756-yilda Ispaniyada", "1055-yilda Bag‘dodda", "711-yilda Misrda", "661-yilda Suriyada", "756-yili Ispaniyada; X asrdan Qurdoba amirligi.")
t.B("Saljuqiy turklar Bag‘dodni qachon egallagan?", "1055-yilda", "1258-yilda", "756-yilda", "750-yilda", "1055-yili.")
t.B("Arab xalifaligi kimning Bag‘dodni egallashi bilan barham topgan?", "mo‘g‘ul xoni Xuloku", "saljuqiylar", "Muoviya I", "Horun ar-Rashid", "1258-yilda Xuloku.")
t.B("Dastlabki to‘rt xalifa forscha qanday atalgan?", "choryorlar", "ansorlar", "muhojirlar", "voliylar", "Choryorlar – «to‘rt do‘st».")
t.NAT("Ali ibn Abu Tolib xalifaligini barcha tan olmadi.", "Ali xorijiylar tomonidan o‘ldirilib, hokimiyatni Muoviya I egalladi", "Ali umrbod hukmronlik qildi", "xalifalik bekor qilindi", "Abbosiylar hokimiyatga keldi", "661-yilda Umaviylar sulolasi boshlandi.")
t.NAT("Umaviylarga qarshi bir necha bor xalq qo‘zg‘olonlari bo‘ldi.", "ularning hokimiyati zaiflashib, Abbosiylar hokimiyatga keldi", "Umaviylar kuchaydi", "xalifalik Vizantiyaga qo‘shildi", "poytaxt Madinaga ko‘chirildi", "Abbosiylar hokimiyat tepasiga keldi.")
t.NAT("Musulmon bo‘lmaganlar davlat xizmatiga olinmay, ko‘proq soliq to‘ladi.", "ko‘pchilik islomni qabul qilib, arab tilini o‘rgandi", "aholi xalifalikdan qochib ketdi", "soliqlar bekor qilindi", "xristianlik davlat dini bo‘ldi", "Aholining asosiy qismi musulmon bo‘ldi.")
t.NAT("IX asrdan Misr, Eron, Movarounnahr va Xuroson mustaqillikka erishdi.", "Abbosiylar tasarrufida faqat Yaqin Sharq va Arabiston qoldi", "xalifalik kengaydi", "Bag‘dod poytaxtlikdan mahrum bo‘ldi", "Umaviylar qaytib keldi", "Xalifalik qisqardi.")
t.TF("Umaviylar davrida arab tili davlat tili deb e’lon qilingan.", True, "To‘g‘ri.")
t.TF("Umaviylar davrida xalifa lavozimi saylanadigan lavozimga aylantirilgan.", False, "Noto‘g‘ri: xalifa lavozimi nasliy merosga aylantirilgan.")
t.TF4([("Abu Bakr davrida arablar Iroq va Suriyani fath etgan.", True), ("Umar davrida davlat xizmatchilariga maosh to‘lash joriy etilgan.", True),
       ("Usmon davrida Eron Sosoniylari davlatini fath etish tugallangan.", True), ("Abbosiylar Muhammad (s.a.v.)ning o‘g‘li avlodlari bo‘lgan.", False)],
      "4-noto‘g‘ri: Abbosiylar Muhammad (s.a.v.)ning amakisi Abbosning avlodlari.")
t.MUL([("Usmon davrida to‘plangan Qur’on nusxalaridan biri O‘zbekiston musulmonlari idorasida saqlanmoqda.", True),
       ("Umaviylar davrida davlat xazinasi va davlat arxivi tashkil etilgan.", True),
       ("Tustar qal’asi Xuloku tomonidan egallangan.", False)],
      "III noto‘g‘ri: Tustarni Sa’d ibn Abu Vaqqos boshchiligidagi arab lashkari Umar davrida egallagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Abu Bakr xalifa bo‘ldi", "Hijriy taqvim joriy etildi", "Umaviylar hokimiyatga keldi", "Puate jangi", "Ispaniyada mustaqil amirlik ajraldi", "Saljuqiylar Bag‘dodni egalladi", "Xuloku Bag‘dodni egalladi"],
      "632 → 637 → 661 → 732 → 756 → 1055 → 1258.")
t.MATCH("Xalifalarni ularga oid ma’lumot bilan moslashtiring.", ["Abu Bakr", "Umar", "Usmon", "Ali ibn Abu Tolib"],
        ["Maslahat kengashi tuzilgan", "hijriy taqvim joriy etilgan", "Qur’on bir butun kitob shakliga keltirilgan", "tarafdorlari shialar nomini olgan", "poytaxtni Bag‘dodga ko‘chirgan"], 'abcd',
        "Abu Bakr – kengash; Umar – hijriy taqvim; Usmon – Qur’on; Ali – shialar.")
t.VENN("Umaviylar", "Abbosiylar",
       [("poytaxti Damashq", 1), ("asoschisi Muoviya I", 1),
        ("qarorgohi Bag‘dod", 2), ("Horun ar-Rashid hukmronligi", 2),
        ("Arab xalifaligini boshqargan sulola", 3)],
       "Umaviylar – Damashq, Muoviya; Abbosiylar – Bag‘dod, Horun ar-Rashid; ikkalasi xalifalik sulolasi.")
t.MAPMATCH('mideast', ['Damashq', 'Bag‘dod', 'Kordova', 'Puate'],
           ["Umaviylar poytaxti", "Abbosiylar qarorgohi – «Xudoning in’omi»", "756-yilda ajralgan amirlik markazi", "732-yilda arablarning shimolga siljishi to‘xtatilgan joy"],
           "1 – Damashq; 2 – Bag‘dod; 3 – Kordova; 4 – Puate.")
