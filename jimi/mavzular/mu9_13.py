from qlib import Topic
TOPICS = {}
UZ = 'uzb'; CA = 'ca'

# 26 Jadidlarning dasturiy maqsad va vazifalari
t = Topic('e9u26', 9026); TOPICS['e9u26'] = t
t.B("Taraqqiyparvarlar nimalarga qarshi kurashga alohida ahamiyat bergan?", "mutaassiblik, loqaydlik, qoloqlikka", "savdo-sotiqqa", "hunarmandchilikka", "dehqonchilikka", "Mutaassiblik, loqaydlik, qoloqlikka.")
t.B("Jadidlarning diqqat markaziga birinchi bosqichda qanday vazifa qo‘yilgan?", "ta’limni isloh etish", "qurolli qo‘zg‘olon", "milliy qo‘shin tuzish", "temiryo‘l qurish", "Birinchi bosqichda ta’limni isloh etish.")
t.B("Yangi usul maktablarida qaysi standartlar mezon qilib olingan?", "Yevropa standartlari", "Xitoy standartlari", "eski madrasa standartlari", "harbiy standartlar", "Yevropa standartlari.")
t.B("Dastlab yangi usul maktablarida qayerda nashr etilgan darsliklardan foydalanilgan?", "Qozon va Orenburgda", "Istanbul va Qohirada", "Moskva va Kiyevda", "Tehron va Kobulda", "Qozon va Orenburgda nashr etilganlardan.")
t.B("1911-yilga kelib yangi usul maktablari soni nechtaga yetgan?", "63 taga", "24 taga", "100 ga", "12 taga", "63 ta maktab, 4106 o‘quvchi.")
t.B("1911-yilda yangi usul maktablarida necha o‘quvchi bo‘lgan?", "4106 nafar", "1740 nafar", "200 nafar", "40 ming nafar", "4106 nafar.")
t.B("1910-yilda Toshkentning o‘zida nechta jadid maktabi bo‘lgan?", "24 ta", "63 ta", "100 ta", "4 ta", "24 ta maktabda 1740 bola.")
t.B("1917-yilga kelib o‘lkada nechta yangi usul maktabi mavjud edi?", "100 ga yaqin", "24 ta", "63 ta", "1000 dan ortiq", "100 ga yaqin.")
t.B("Jadidlar o‘g‘il va qiz bolalarni o‘qitishda qanday tashabbus ko‘rsatgan?", "ularni birga o‘qitish", "qizlarni o‘qitmaslik", "faqat qizlarni o‘qitish", "faqat uyda o‘qitish", "O‘g‘il va qiz bolalarni birga o‘qitishda tashabbuskor bo‘lgan.")
t.B("Jadidlarning siyosiy maqsadlaridan biri nima edi?", "konstitutsion, parlament idora usulidagi jamiyat qurish", "xonliklarni tiklash", "Rossiya tarkibida qolish", "monarxiyani mustahkamlash", "Konstitutsion, parlament idora usulidagi ozod va farovon jamiyat.")
t.B("Jadidlar qaysi tillarga davlat tili maqomini berishni maqsad qilgan?", "turkiy tillarga", "rus tiliga", "arab tiliga", "fors tiliga", "Turkiy tillarga.")
t.NAT("Ma’rifatparvarlar xorijga chiqib, turli mamlakatlar madaniyati va ta’limini solishtirdi.", "yoshlarda jahon yutuqlarini Turkistonga keltirish istagi paydo bo‘ldi", "ular Turkistonga qaytmadi", "yangi usul maktablari yopildi", "eski usul kuchaydi", "Natijada ta’limni isloh etish birinchi vazifaga aylandi.")
t.NAT("Toshkent, Buxoro, Samarqand va boshqa shaharlarda madaniy-ma’rifiy jamiyat va uyushmalar ochildi.", "jadidchilik Turkistonda keng yoyildi", "jadidchilik tugadi", "maktablar yopildi", "matbuot taqiqlandi", "Bu jadidchilikning keng yoyilishiga olib keldi.")
t.TF("Yangi usul maktablarida islom ta’limoti asoslarini o‘rganishga ham katta e’tibor berilgan.", True, "To‘g‘ri.")
t.TF("Jadidlar islom ayollarning ma’rifatli bo‘lishiga to‘sqinlik qiladi, deb hisoblagan.", False, "Noto‘g‘ri: ular islom bunga to‘sqinlik qilmaydi, deb ta’kidlagan.")
t.MUL([("Jadidlar qobiliyatli yoshlarni chet elga o‘qishga yuborishni ustuvor deb bilgan.", True),
       ("Jadidlar milliy pul birligi va milliy qo‘shin tuzishni maqsad qilgan.", True),
       ("Jadidlar «usuli qadim»ni to‘liq qo‘llab-quvvatlagan.", False)],
      "III noto‘g‘ri: ular «usuli qadim»ni inkor etgan.")
t.CHR("Raqamlarni xronologik tartibda joylashtiring.", ["Toshkentda 24 ta jadid maktabi (1740 bola)", "O‘lkada 63 ta yangi usul maktabi", "O‘lkada 100 ga yaqin yangi usul maktabi"],
      "1910 → 1911 → 1917.")
t.MAPN(UZ, ['Xiva', 'Buxoro', 'Samarqand', 'Andijon'], "Toshkent, Buxoro, Samarqand, Andijon, Qo‘qon, Xiva jadidchilik markazlari bo‘lgan. Qaysi raqam bilan Xiva belgilangan?",
       "1 – Xiva; 2 – Buxoro; 3 – Samarqand; 4 – Andijon.", ask_idx=0)
t.VENN("Jadidlarning ma’rifiy maqsadlari", "Jadidlarning siyosiy maqsadlari",
       [("yangi usul maktablari tarmog‘ini kengaytirish", 1), ("gazeta va jurnallar chop etish", 1),
        ("milliy davlat bunyod etish", 2), ("milliy qo‘shin tuzish", 2),
        ("Turkistonni taraqqiyot yo‘liga olib chiqish", 3)],
       "Ma’rifiy — maktablar, matbuot; siyosiy — milliy davlat, qo‘shin; umumiy — taraqqiyot.")

# 27 Jadidchilik harakati namoyandalari
t = Topic('e9u27', 9027); TOPICS['e9u27'] = t
t.B("«O‘rta Osiyo jadidlarining otasi» deb kim tan olingan?", "Mahmudxo‘ja Behbudiy", "Munavvarqori", "Abdulla Avloniy", "Ismoil G‘aspirali", "Mahmudxo‘ja Behbudiy (1875–1919).")
t.B("Behbudiy qayerda tug‘ilgan?", "Samarqand yaqinidagi Baxshitepa qishlog‘ida", "Toshkentda", "Buxoroda", "Andijonda", "1875-yil 19-yanvarda Baxshitepada.")
t.B("Behbudiy qanday diniy darajaga ko‘tarilgan?", "muftiy", "shayxulislom", "qozikalon", "eshon", "Imom-xatib, qozi, keyin muftiy.")
t.B("Behbudiy tashabbusi bilan tashkil etilgan kutubxona qanday atalgan?", "«Behbudiya kutubxonasi»", "«Turon kutubxonasi»", "«Navoiy kutubxonasi»", "«Ma’rifat kutubxonasi»", "Otasi sharafiga «Behbudiya kutubxonasi».")
t.B("Munavvarqori Abdurashidxonov qaysi yillarda yashagan?", "1878–1931", "1875–1919", "1851–1914", "1878–1934", "1878–1931.")
t.B("Munavvarqori qaysi darsliklarni yaratgan?", "«Adibi avval», «Adibi soniy», «Yer yuzi»", "«Birinchi muallim», «Ikkinchi muallim»", "«Turkiy guliston yoxud axloq»", "«Rahbari muallimin»", "«Adibi avval», «Adibi soniy», «Yer yuzi».")
t.B("Abdulla Avloniy qachon va qayerda tug‘ilgan?", "1878-yil Toshkentda", "1875-yil Samarqandda", "1878-yil Buxoroda", "1884-yil Qrimda", "1878-yilda Toshkentda hunarmand oilasida.")
t.B("Abdulla Avloniy 1907-yilda qaysi gazetaga asos solgan?", "«Shuhrat»", "«Tarjimon»", "«Oyina»", "«Taraqqiy»", "«Shuhrat» gazetasiga.")
t.B("«Turkiy guliston yoxud axloq» darsligi muallifi kim?", "Abdulla Avloniy", "Munavvarqori", "Behbudiy", "Fitrat", "Abdulla Avloniy.")
t.B("Buxorodagi jadid namoyandalari kimlar bo‘lgan?", "Abdurauf Fitrat, Sadriddin Ayniy, Fayzulla Xo‘jayev", "Behbudiy, Shakuriy, Ajziy", "Hamza, Cho‘lpon, Ibrat", "Bobooxun Salimov, Polvonniyoz hoji", "Fitrat, Ayniy, Fayzulla Xo‘jayev.")
t.B("Xivadagi jadid namoyandalari kimlar bo‘lgan?", "Bobooxun Salimov, Polvonniyoz hoji Yusupov", "Munavvarqori, Avloniy", "Fitrat, Ayniy", "Hamza, Cho‘lpon", "Bobooxun Salimov, Polvonniyoz hoji Yusupov.")
t.B("Podsho yakkahukmronligi qanday ataladi?", "absolyutizm", "senzura", "protektorat", "konstitutsiya", "Absolyutizm.")
t.B("Matbuot ustidan hokimiyat nazorati qanday ataladi?", "senzura", "absolyutizm", "apellatsiya", "kontributsiya", "Senzura.")
t.B("Yoshlarni chet elda o‘qitish uchun o‘z hisobidan katta mablag‘ ajratgan andijonlik kim?", "Mirkomil Mirmo‘minboyev", "Hoji Rafiy", "Usmonxo‘ja", "Mirza Abduvohid", "Mirkomil Mirmo‘minboyev.")
t.B("«Tarbiyai atfol» jamiyati qachon va qayerda tashkil qilingan?", "1910-yilda Buxoroda", "1907-yilda Toshkentda", "1893-yilda Samarqandda", "1904-yilda Qo‘qonda", "1910-yilda Buxoroda.")
t.B("«Tarbiyai atfol» so‘zining ma’nosi nima?", "«Bolalar tarbiyasi»", "«Yangi usul»", "«Ma’rifat nuri»", "«Xalq uchun»", "«Bolalar tarbiyasi».")
t.B("«Tarbiyai atfol» 1912-yilda nechta talabani Turkiyaga o‘qishga yuborgan?", "30 nafar", "15 nafar", "100 nafar", "4 nafar", "1911-yilda 15, 1912-yilda 30 nafar.")
t.NAT("Jadidlar hukmron mafkuradan mustaqil xalq ta’limi tizimi va milliy matbuotga asos soldi.", "progressiv g‘oyalarni tarqatish uchun muhim vosita yaratildi", "jadidchilik to‘xtadi", "eski maktablar kuchaydi", "matbuot taqiqlandi", "Bu ilg‘or g‘oyalarni tarqatish vositasi bo‘ldi.")
t.TF("Jadidlar Alisher Navoiy, Mirzo Bedil va Boborahim Mashrab merosidan foydalangan.", True, "To‘g‘ri.")
t.TF("Turkiston ma’rifatparvarlari podsho yakkahukmronligini qo‘llab-quvvatlagan.", False, "Noto‘g‘ri: ular absolyutizmga qarshi kurashgan.")
t.MUL([("Munavvarqori jadid maktablari ochilishining tashabbuskori va milliy gazetalar asoschisi bo‘lgan.", True),
       ("Ma’rifatparvarlar jaholat va mutaassiblikni inson azob-uqubatlarining asl sabablari deb talqin etgan.", True),
       ("Behbudiy faqat Toshkent madrasalarida tahsil olgan.", False)],
      "III noto‘g‘ri: Behbudiy Samarqand, so‘ngra Buxoro madrasalarida tahsil olgan.")
t.MATCH("Jadidlarni ular faoliyat ko‘rsatgan shaharlar bilan moslashtiring.", ["Mahmudxo‘ja Behbudiy", "Munavvarqori Abdurashidxonov", "Abdurauf Fitrat", "Bobooxun Salimov"],
        ["Buxoro", "Xiva", "Samarqand", "Toshkent"], "cdab",
        "Behbudiy — Samarqand; Munavvarqori — Toshkent; Fitrat — Buxoro; Salimov — Xiva.")
t.MAPMATCH(UZ, ['Samarqand', 'Toshkent', 'Buxoro', 'Xiva'],
           ["Behbudiy, Shakuriy, Ajziy faoliyat ko‘rsatgan shahar", "Munavvarqori, Avloniy faoliyat ko‘rsatgan shahar", "1910-yilda «Tarbiyai atfol» tuzilgan shahar", "Bobooxun Salimov faoliyat ko‘rsatgan shahar"],
           "1 – Samarqand; 2 – Toshkent; 3 – Buxoro; 4 – Xiva.")
t.VENN("Munavvarqori", "Abdulla Avloniy",
       [("«Adibi avval» darsligi muallifi", 1), ("1931-yilgacha yashagan", 1),
        ("«Shuhrat» gazetasi asoschisi", 2), ("«Turkiy guliston yoxud axloq» muallifi", 2),
        ("1878-yilda tug‘ilgan toshkentlik jadid", 3)],
       "Munavvarqori — «Adibi avval»; Avloniy — «Shuhrat», «Turkiy guliston»; ikkalasi 1878-yil tug‘ilgan.")
