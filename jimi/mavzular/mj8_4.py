from qlib import Topic
TOPICS = {}
W = 'globe'; EU = 'europe'; AS = 'asia'

# 13 Osiyo mamlakatlari rivojlanishi
t = Topic('e8j13', 813); TOPICS['e8j13'] = t
t.B("Yevropa tarix fanida sharqona taraqqiyot shakli qanday ataladi?", "«an’anaviy sivilizatsiya»", "«industrial sivilizatsiya»", "«ma’rifat jamiyati»", "«burjua jamiyati»", "Uni «an’anaviy sivilizatsiya», «an’anaviy jamiyat» deyishadi.")
t.B("Sharq mamlakatlarining qanday tashqi siyosat prinsipi ularni orqada qoldirgan?", "«yopiq eshiklar» prinsipi", "«ochiq eshiklar» prinsipi", "betaraflik", "mustamlakachilik", "Sharq mamlakatlari «yopiq eshiklar» prinsipiga asoslangan.")
t.B("XVI asrda dunyoning eng aholisi ko‘p va boy qismi qaysi sivilizatsiya edi?", "Xitoy-konfutsiylik", "Hind", "Yaponiya", "Islom", "Xitoy-konfutsiylik sivilizatsiyasi.")
t.B("Qaysi sivilizatsiya Xitoy sivilizatsiyasining bir tarmog‘i deyiladi?", "Yaponiya", "Hind", "Islom", "Yevropa", "Yaponiya Xitoydan yozuv tizimi va moddiy madaniyatni qabul qilgan.")
t.B("Yaponiyadagi Yevropa dvoryanlariga monand ritsarlar qanday atalgan?", "samuraylar", "kastalar", "mandarinlar", "shoguna", "Oliyhimmat ritsarlar – samuraylar.")
t.B("Yaponiyani xalqaro aloqalardan uzib qo‘ygan rejim qaysi?", "Tokugava rejimi", "Min sulolasi", "Mug‘ullar", "Chin sulolasi", "Tokugava rejimi jamiyat rivojini to‘xtatdi.")
t.B("Hind jamiyatida inson o‘rni nima bilan belgilangan?", "qaysi kastaga mansubligi bilan", "boyligi bilan", "ilmi bilan", "diniga ko‘ra", "Insonning o‘rni kastaga mansubligi bilan bog‘liq.")
t.B("Qaysi din barcha musulmonlar tengligiga asoslangani uchun keng tarqalgan?", "islom", "buddaviylik", "hinduizm", "konfutsiylik", "Islom barcha musulmonlarning tengligiga asoslangan.")
t.B("XVII asr o‘rtalarigacha Sharq qaysi sohalarda Yevropadan oldinda edi?", "harbiy ish va moddiy ne’matlar ishlab chiqarishda", "dengiz flotida", "kitob chop etishda", "temiryo‘l qurilishida", "Sharq harbiy ishda va ishlab chiqarishda oldinda edi.")
t.B("«Ekstensiv» rivojlanish nimani anglatadi?", "sifat emas, faqat son jihatidan o‘sishni", "sifatli o‘zgarishni", "sanoat inqilobini", "eksportni", "Ekstensiv – faqat son jihatdan ko‘payishga yo‘naltirilgan o‘sish.")
t.NAT("Sharqda an’anaviy tartiblar ideallashtirildi.", "rivojlanish sur’atlari sekinlashib, yangiliklarni tatbiq etish qiyinlashdi", "fan tez rivojlandi", "Sharq Yevropani bosib oldi", "an’analar yo‘qoldi",
      "Bu sivilizatsiya asoslarini saqlasa-da, rivojlanishni sekinlashtirdi.")
t.NAT("Sharqda tabiiy resurslardan uzoq vaqt ekstensiv foydalanildi.", "ijtimoiy-iqtisodiy inqiroz kelib chiqdi", "iqtisod tez o‘sdi", "aholi kamaydi", "sanoat inqilobi boshlandi",
      "Ekstensiv foydalanish ijtimoiy-iqtisodiy inqirozga olib keldi.")
t.TF("Sharq davlatlarida harbiy xarajatlar G‘arbnikidan ancha yuqori bo‘lgan.", True, "To‘g‘ri.")
t.TF("Yaponiya jamiyatida, Xitoydan farqli ravishda, shaxsning erkin hayot yo‘lini tanlash huquqi rad etilgan.", False, "Noto‘g‘ri: Yaponiyada bu huquq rad etilmaydi.")
t.MUL([("Ko‘plab Sharq yangiliklari Yevropada 300–1000 yil keyin paydo bo‘lgan.", True), ("Sharqda shaharlarning iqtisodiy roli past bo‘lgan.", True), ("XVI–XVII asrlardan Sharqda transport va kommunikatsiya G‘arbdan tezroq rivojlangan.", False)],
      "III noto‘g‘ri: rivojlanish sur’atlari G‘arbga nisbatan pasaygan.")
t.MATCH("Sivilizatsiyalarni o‘ziga xos belgisi bilan moslashtiring.", ["Xitoy-konfutsiylik", "Yaponiya", "Hind", "Islom"],
        ["kamtarona hayot, davlat tartibga solgan turmush", "samuraylar va knyazlar mavjudligi", "kastalarga bo‘linish", "din hayot tarzini ham belgilaydi", "parlament boshqaruvi"], 'abcd',
        "Xitoy – kamtarona hayot; Yaponiya – samuraylar; Hind – kastalar; Islom – din va hayot tarzi.")
t.MAPMATCH(AS, ['Xitoy', 'Yaponiya', 'Hindiston'],
           ["Xitoy-konfutsiylik sivilizatsiyasi markazi", "samuraylar mamlakati", "kastalarga bo‘lingan jamiyat mamlakati"], "1 – Xitoy; 2 – Yaponiya; 3 – Hindiston.")
t.VENN("Xitoy sivilizatsiyasi", "Yaponiya sivilizatsiyasi",
       [("XVI asrda dunyoning eng aholisi ko‘p qismi", 1), ("shaxsning erkin tanlovi cheklangan", 1),
        ("samuraylar va knyazlar mavjud", 2), ("Tokugava rejimi xalqaro aloqalardan uzgan", 2),
        ("Sharq an’anaviy sivilizatsiyasi", 3)],
       "Xitoy – ko‘p aholi; Yaponiya – samuraylar, Tokugava. Ikkalasi Sharq sivilizatsiyasi.")

EA = 'eastasia'; IN = 'india'
# 14 Xitoy
t = Topic('e8j14', 814); TOPICS['e8j14'] = t
t.B("XVI asr oxiri – XVII asr boshlarida Xitoyda qaysi sulola hukmron edi?", "min sulolasi", "chin sulolasi", "xan sulolasi", "tan sulolasi", "Min sulolasi siyosatidan norozilik kuchaydi.")
t.B("Manjur qabilalari ittifoqi qaysi daryodan janubda paydo bo‘lgan?", "Amur", "Xuanxe", "Yanszi", "Ganga", "XVI asr oxirida Amur daryosidan janubda.")
t.B("Manjurlar sardori Abaxay o‘zini xon deb qachon e’lon qilgan?", "1636-yilda", "1644-yilda", "1616-yilda", "1911-yilda", "1636-yili Abaxay yangi davlatni Chin deb atadi.")
t.B("«Chin» so‘zi qanday ma’noni anglatadi?", "«sof», «toza»", "«buyuk»", "«sharq»", "«osmon»", "Chin – «sof», «toza».")
t.B("Manjurlar Pekinga qachon kirib kelgan?", "1644-yilda", "1636-yilda", "1662-yilda", "1683-yilda", "1644-yili manjurlar Pekinga kirib keldi.")
t.B("Xitoy imperatori deb e’lon qilingan manjur hukmdori kim?", "Shunchji", "Abaxay", "Kansi", "Van Yanmin", "1644-yilda Shunchji imperator deb e’lon qilindi.")
t.B("Chin sulolasi Xitoyda qachongacha hukmronlik qilgan?", "1911-yilgacha", "1644-yilgacha", "1840-yilgacha", "1949-yilgacha", "Chin sulolasi 1911-yilgacha hukmronlik qildi.")
t.B("Xitoy dehqonlarining asosiy oziq-ovqat mahsuloti nima edi?", "sholi", "bug‘doy", "makkajo‘xori", "kartoshka", "Aholining asosiy oziq-ovqati – sholi.")
t.B("Ijara haqi hosilning qancha qismini tashkil etgan?", "50 foizini", "10 foizini", "25 foizini", "75 foizini", "Ijara haqi hosilning 50 foizi edi.")
t.B("XVII asrda Tayvanning bir qismini qaysi yevropaliklar egallagan?", "gollandlar", "inglizlar", "ispanlar", "portugallar", "Golland kemalari Tayvan orollarining bir qismini egalladi.")
t.B("Inglizlar Xitoyning qaysi hududida savdo qilish ruxsatini olgan?", "Guanchjou", "Pekin", "Nankin", "Tayvan", "Inglizlar Guanchjou hududiga o‘rnashdi.")
t.B("Yevropaliklar Xitoydan nimalarni olib ketgan?", "ipak va chinni", "tamaki va qurol", "paxta va jun", "oltin va kumush", "Ipak va chinni olib ketib, tamaki va qurol olib kelishgan.")
t.B("Konfutsiylikni yangicha sharhlagan minlar davri olimi kim?", "Van Yanmin", "Abaxay", "Shunchji", "Konfutsiy", "Van Yanmin konfutsiylikni yangicha sharhladi.")
t.B("Xitoylik ruhoniyning Hindistonga safari tasvirlangan roman qaysi?", "«G‘arbga sayohat»", "«Ramayana»", "«Gulliver»", "«Kunsyuy»", "«G‘arbga sayohat» romani.")
t.B("Aktyorlar niqob kiyib o‘ynaydigan umummilliy teatr turi qanday atalgan?", "kunsyuy", "kabuki", "no", "opera", "XVI–XVII asrlarda kunsyuy teatri mashhur edi.")
t.NAT("Xitoyda xalq qo‘zg‘olonlari avj oldi, qo‘zg‘olonchilar Pekinni egalladi.", "manjurlar Xitoyni egallashi osonlashdi", "min sulolasi kuchaydi", "Xitoy Yaponiyaga qaram bo‘ldi", "manjurlar chekindi",
      "Qo‘zg‘olonlar chinlarga yordam berdi, 1644-yil Pekin olindi.")
t.NAT("Xitoyda dehqonlar yerlari yirik yer egalari qo‘liga o‘tdi va soliqlar oshdi.", "butun imperiyani qamragan dehqon qo‘zg‘olonlari ko‘tarildi", "dehqonlar boyidi", "shaharlar ko‘paydi", "Yevropaga ko‘chish boshlandi",
      "Qiyinchiliklar dehqon qo‘zg‘olonlariga olib keldi.")
t.TF("XVIII asr oxirigacha Xitoy iqtisodiy jihatdan dunyoning eng qudratli davlatlaridan biri bo‘lgan.", True, "To‘g‘ri.")
t.TF("Xitoyda soliqlar XVI asrgacha faqat kumush tanga bilan to‘langan.", False, "Noto‘g‘ri: soliqlar sholi bilan olingan, XVI asrdan kumush bilan to‘lana boshlandi.")
t.MUL([("Chinlar Koreya, Vyetnam va Qashqarni bo‘ysundirgan.", True), ("Kunsyuy asosida Pekin operasi shakllangan.", True), ("Islohotchilar XVII asr boshida hokimiyatni uzoq saqlab qolgan.", False)],
      "III noto‘g‘ri: saroy asilzodalari qarshiligi tufayli ular chetlatilib, qatag‘on qilindi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Abaxay o‘zini xon deb e’lon qildi", "Manjurlar Pekinga kirdi", "Rossiya Xitoy bilan aloqa o‘rnatishga urindi", "Chin sulolasi hukmronligi tugadi"],
      "1636 → 1644 → XVIII asr 70-yillari → 1911.")
t.MAPMATCH(EA, ['Pekin', 'Nankin', 'Tayvan', 'Guanchjou'],
           ["1644-yilda manjurlar kirib kelgan poytaxt", "vatanparvarlar chinlarga qarshi front tuzmoqchi bo‘lgan shahar", "gollandlar qisman egallagan orol", "inglizlar savdo ruxsatini olgan hudud"],
           "1 – Pekin; 2 – Nankin; 3 – Tayvan; 4 – Guanchjou.")
t.VENN("Min sulolasi", "Chin sulolasi",
       [("davrida madaniyat gullab-yashnagan, Van Yanmin yashagan", 1), ("islohotchilar qatag‘on qilingan", 1),
        ("manjurlar sulolasi", 2), ("1644–1911-yillarda hukmronlik qilgan", 2),
        ("Xitoyni boshqargan sulola", 3)],
       "Min: madaniyat, islohotchilar. Chin: manjurlar, 1911-yilgacha. Ikkalasi Xitoy sulolasi.")

# 15 Hindiston
t = Topic('e8j15', 815); TOPICS['e8j15'] = t
t.B("Hindistonni egallash uchun yurish boshlagan Kobul hukmdori kim?", "Zahiriddin Muhammad Bobur", "Humoyun", "Akbar", "Sherxon", "Kobul hukmdori Bobur harbiy yurish boshladi.")
t.B("Panipat jangi qachon bo‘lgan?", "1526-yil 21-aprelda", "1530-yilda", "1540-yilda", "1556-yilda", "1526-yil 21-aprelda Panipat jangi bo‘ldi.")
t.B("Panipat jangida halok bo‘lgan Dehli sultoni kim?", "Ibrohim Lo‘di", "Sherxon", "Humoyun", "Avrangzeb", "Lo‘diylar sulolasidan Ibrohim Lo‘di halok bo‘ldi.")
t.B("Bobur qachon vafot etgan?", "1530-yilda", "1526-yilda", "1540-yilda", "1555-yilda", "Bobur 1530-yili vafot etdi.")
t.B("Humoyun 1540-yilda mag‘lub bo‘lgach, kimning saroyida panoh topgan?", "Eron shohi Taxmasp I", "Akbar", "Sherxon", "Ibrohim Lo‘di", "Humoyun Eron shohi Taxmasp I saroyida panoh topdi.")
t.B("1540-yilda Hindiston taxtini kim egallagan?", "Sherxon", "Akbar", "Ibrohim Lo‘di", "Jahongir", "Afg‘onlarning sur qabilasi sardori Sherxon.")
t.B("Humoyun Dehlini qachon qaytarib olgan?", "1555-yilda", "1540-yilda", "1556-yilda", "1530-yilda", "Humoyun 1555-yili Dehlini qaytarib oldi.")
t.B("Akbar qaysi yillarda Hindistonni boshqargan?", "1556–1605", "1526–1530", "1658–1707", "1605–1627", "Akbar 1556–1605-yillarda boshqardi.")
t.B("Akbar joriy etgan yagona taqvim kimning tizimiga asoslangan?", "Mirzo Ulug‘bek", "Beruniy", "Bobur", "Umar Xayyom", "Taqvim Mirzo Ulug‘bek tizimiga asoslangan.")
t.B("Akbar qaysi soliqni bekor qilgan?", "jizya (jon solig‘i)", "savdo solig‘i", "yer solig‘i", "boj", "Musulmon bo‘lmaganlardan olinadigan jizyani bekor qildi.")
t.B("Akbarning qanday nomlari bo‘lgan?", "«Milliy podshoh», «Xalq hukmdori»", "«Olamgir»", "«Sohibqiron»", "«Jahongir»", "Akbar «Milliy podshoh», «Xalq hukmdori» nomlariga sazovor bo‘ldi.")
t.B("Taxtga kelib Akbar islohotlarini bekor qilgan o‘g‘li kim?", "Jahongir Mirzo", "Shoh Jahon", "Avrangzeb", "Humoyun", "Jahongir Mirzo ko‘p islohotlarni bekor qildi.")
t.B("Avrangzeb Olamgir qaysi yillarda hukmronlik qilgan?", "1658–1707", "1556–1605", "1605–1627", "1707–1757", "Avrangzeb 1658–1707-yillarda hukmronlik qildi.")
t.B("Buyuk Britaniya Bengaliyani qachon bosib olgan?", "1757-yilda", "1707-yilda", "1658-yilda", "1600-yilda", "1757-yili Bengaliya bosib olindi.")
t.B("Hindistonni bo‘ysundirishda yetakchilik qilgan ingliz kompaniyasi qaysi?", "Ost-Indiya kompaniyasi", "Moskva kompaniyasi", "Gudzon kompaniyasi", "Levant kompaniyasi", "Ost-Indiya kompaniyasi.")
t.B("Tojmahal kimning xotirasiga bag‘ishlangan?", "Mumtoz Mahal", "Nodira", "Bobur", "Akbar", "Shoh Jahon sevimli xotini Mumtoz Mahalga bag‘ishlab qurdirgan.")
t.B("«Ramaning jasoratlari» poemasini kim yaratgan?", "Tulsidas", "Surdas", "Bedil", "Akbar", "Tulsidas «Ramayana» sujeti asosida yaratdi.")
t.NAT("Avrangzeb jizyani tiklab, hindlarga soliqlarni ikki hissaga oshirdi.", "mamlakat bo‘ylab xalq qo‘zg‘olonlari boshlandi", "imperiya mustahkamlandi", "hindlar islomni qabul qildi", "Yevropaliklar quvildi",
      "Bu siyosat xalq qo‘zg‘olonlariga sabab bo‘ldi.")
t.NAT("XVIII asrda Boburiylar imperiyasi parchalandi.", "yevropaliklarning kirib kelishi uchun qulay sharoit yaratildi", "imperiya kuchaydi", "Eron Hindistonni boshqardi", "Akbar islohotlari tiklandi",
      "Feodal tarqoqlik yevropaliklarga yo‘l ochdi.")
t.TF("Akbar mamlakatni boshqarishga musulmonlar bilan birga hindlarni ham jalb etgan.", True, "To‘g‘ri.")
t.TF("Surdas «Mahabharata»ni yozgan.", False, "Noto‘g‘ri: Surdas Krishna haqidagi poemalar muallifi; «Mahabharata» Akbar saroyida tarjima qilingan.")
t.MUL([("Akbar imperiyani viloyatlarga ajratib, noiblar tayinlagan.", True), ("Bedil ham shu davrda Hindistonda ijod qilgan.", True), ("Humoyun Boburning kichik o‘g‘li bo‘lgan.", False)],
      "III noto‘g‘ri: Humoyun Boburning katta o‘g‘li edi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Panipat jangi", "Bobur vafot etdi", "Humoyun taxtdan ag‘darildi", "Humoyun Dehlini qaytarib oldi", "Akbar vafot etdi", "Bengaliya inglizlar qo‘liga o‘tdi"],
      "1526 → 1530 → 1540 → 1555 → 1605 → 1757.")
t.MAPMATCH(IN, ['Kobul', 'Panipat', 'Bengaliya'],
           ["Boburning Hindistonga yurishdan oldingi poytaxti", "1526-yilgi jang bo‘lgan joy", "1757-yilda Buyuk Britaniya bosib olgan boy hudud"], "1 – Kobul; 2 – Panipat; 3 – Bengaliya.")
t.VENN("Akbar", "Avrangzeb",
       [("jizyani bekor qilgan", 1), ("diniy bag‘rikenglik siyosatini yuritgan", 1),
        ("jizyani qayta tiklagan", 2), ("hind ibodatxonalarini buzdirgan", 2),
        ("Boburiylar sulolasi hukmdori", 3)],
       "Akbar – bag‘rikenglik; Avrangzeb – qattiq diniy siyosat. Ikkalasi boburiy.")

# 16 Yaponiya va Koreya
t = Topic('e8j16', 816); TOPICS['e8j16'] = t
t.B("Yaponiya qanday nom bilan ataladi?", "«Kunchiqar mamlakat»", "«Osmon osti»", "«Tong tinchligi mamlakati»", "«Ming orol»", "Yaponiyani «Kunchiqar mamlakat» deb atashadi.")
t.B("Yaponiyada viloyatlarni nazorat qilgan feodallar qanday atalgan?", "daymyolar", "samuraylar", "syogunlar", "mandarinlar", "Viloyatlarni feodallar – daymyolar nazorat qilgan.")
t.B("Yaponiyada amalda siyosiy hokimiyat kimning qo‘lida edi?", "harbiy hukmdor – syogun", "imperator", "daymyolar kengashi", "budda ruhoniylari", "Hokimiyat amalda syogun qo‘lida edi.")
t.B("Tokugava Ieyasu syogun unvonini qachon qabul qilgan?", "1603-yilda", "1614-yilda", "1592-yilda", "1716-yilda", "1603-yili Tokugava Ieyasu syogun bo‘ldi.")
t.B("Tokugava syogunligining poytaxti qaysi shahar edi?", "Edo (hozirgi Tokio)", "Kioto", "Nagasaki", "Osaka", "Edo (hozirgi Tokio) poytaxt qilindi.")
t.B("Tokugavalar Yaponiyani qachongacha boshqargan?", "1867-yilgacha", "1745-yilgacha", "1911-yilgacha", "1603-yilgacha", "Tokugavalar 1867-yilgacha boshqardi.")
t.B("Syogun xristian dinini taqiqlovchi qonunni qachon chiqargan?", "1614-yilda", "1603-yilda", "1592-yilda", "1637-yilda", "1614-yili qonun chiqarildi.")
t.B("«100 moddali Farmon»ni joriy etgan syogun kim?", "Yosimune", "Tokugava Ieyasu", "Oda Nobunaga", "Toyotomi Xideyosi", "Yosimune (1716–1745) «100 moddali Farmon»ni joriy etdi.")
t.B("Yaponiya qo‘shini Koreyaga qachon bostirib kirgan?", "1592-yilda", "1593-yilda", "1627-yilda", "1637-yilda", "1592-yili Yaponiya qo‘shini Koreyaga bostirib kirdi.")
t.B("Yapon flotini tor-mor qilgan koreys qo‘mondoni kim?", "Li Sun Sin", "Yongjo", "Kim Xondo", "Chon Son", "Li Sun Sin floti yapon flotini tor-mor qildi.")
t.B("Xitoy-Koreya qo‘shinlari Pxenyan va Seulni qachon ozod qilgan?", "1593-yilda", "1592-yilda", "1627-yilda", "1637-yilda", "1593-yili ozod qilindi.")
t.B("Manjurlar Koreyaga birinchi marta qachon bostirib kirgan?", "1627-yilda", "1637-yilda", "1592-yilda", "1644-yilda", "1627-yili manjurlar Koreyaga bostirib kirdi.")
t.B("1637-yilgi shartnomaga ko‘ra Koreya qiroli o‘zini kimning vassali deb tan olgan?", "manjurlarning", "Yaponiyaning", "minlar sulolasining", "Rossiyaning", "Koreya qiroli manjurlarning vassali bo‘ldi.")
t.B("Koreyada islohot o‘tkazgan qirol Yongjo qaysi yillarda hukmronlik qilgan?", "1725–1776", "1592–1637", "1716–1745", "1785–1800", "Qirol Yongjo (1725–1776).")
t.B("«Qonunlarning buyuk to‘plami» qachon tuzilgan?", "1785-yilda", "1725-yilda", "1637-yilda", "1745-yilda", "1785-yili tuzilgan.")
t.B("Aktyorlari faqat erkaklar bo‘lgan yapon an’anaviy teatri qanday atalgan?", "kabuki", "kunsyuy", "no", "xokku", "XVII asrda kabuki teatri paydo bo‘ldi.")
t.B("Xokku janrining eng mashhur namoyandasi kim?", "Masuo Basyo", "Kim Xondo", "Li Sun Sin", "Yosimune", "Masuo Basyo.")
t.NAT("Yevropalik missionerlar Yaponiyani bosib olishni maqsad qilgani ma’lum bo‘ldi.", "missionerlar quvilib, Yaponiya o‘zini tashqi dunyodan ajratib qo‘ydi", "Yaponiya xristianlikni qabul qildi", "Yaponiya Portugaliya mustamlakasi bo‘ldi", "Yaponiya Koreyaga ittifoqchi bo‘ldi",
      "Bu siyosat mustamlakaga aylanish xavfining oldini olishni ham ko‘zlagan.")
t.NAT("Koreya manjurlarga ulkan o‘lpon to‘lay boshladi.", "xonavayron aholining ahvoli yanada og‘irlashdi", "Koreya boyidi", "Koreya mustaqil bo‘ldi", "manjurlar Koreyadan chiqib ketdi",
      "O‘lpon og‘ir yuk bo‘lib, Koreya ahvolini og‘irlashtirdi.")
t.TF("Yaponlar uchun imperator Xudoning avlodi hisoblangan.", True, "To‘g‘ri: shuning uchun imperator hokimiyati daxlsiz saqlangan.")
t.TF("Koreyadagi islohotlar feodal tuzum inqirozini to‘xtatgan.", False, "Noto‘g‘ri: islohotlar inqirozni to‘xtata olmadi.")
t.MUL([("Yaponiyani birlashtirishda Oda Nobunaga, Toyotomi Xideyosi va Tokugava Ieyasu xizmat qilgan.", True), ("Yosimune yerni sotish va garovga qo‘yishni taqiqlagan.", True), ("Xitoy Koreyaga yordamga 5 ming kishilik qo‘shin yuborgan.", False)],
      "III noto‘g‘ri: ellik minglik Xitoy qo‘shini yordamga kelgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Yaponlar Koreyaga bostirib kirdi", "Tokugava Ieyasu syogun bo‘ldi", "Xristianlik taqiqlandi", "Manjurlar Koreyaga bostirib kirdi", "Koreya manjurlar vassali bo‘ldi"],
      "1592 → 1603 → 1614 → 1627 → 1637.")
t.MAPMATCH(EA, ['Edo (Tokio)', 'Seul', 'Pxenyan'],
           ["Tokugava syogunligi poytaxti", "1592-yilda yaponlar egallagan Koreya poytaxti", "1593-yilda ozod qilingan Koreya shahri (shimolda)"], "1 – Edo; 2 – Seul; 3 – Pxenyan.")
t.VENN("Yaponiya (XVI–XVIII)", "Koreya (XVI–XVIII)",
       [("Tokugava syogunligi o‘rnatilgan", 1), ("o‘zini tashqi dunyodan ajratib qo‘ygan", 1),
        ("manjurlar vassaliga aylangan", 2), ("qirol Yongjo islohotlari", 2),
        ("Xitoy madaniyati ta’siri sezilgan", 3)],
       "Yaponiya – Tokugava, yakkalanish. Koreya – manjur vassali, Yongjo. Ikkalasiga Xitoy ta’siri.")
