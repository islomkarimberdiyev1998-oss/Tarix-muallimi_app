from qlib import Topic, PLACES, REG
TOPICS = {}

# 14-§ Mang‘itlar boshqaruvi davri
t = Topic('y9u14', 9014); TOPICS['y9u14'] = t
t.B("Mang‘itlar sulolasi Buxoroda qachon hokimiyatga kelgan?", "1756-yilda", "1740-yilda", "1747-yilda", "1785-yilda", "1756-yilda.")
t.B("Mang‘itlar sulolasi davlatni qachongacha idora qilgan?", "1920-yilgacha", "1868-yilgacha", "1756-yilgacha", "1917-yilgacha", "1920-yilgacha.")
t.B("XVIII asr boshida Buxoro xonligidan qaysi hudud ajralib chiqqan?", "Farg‘ona vodiysi", "Xorazm", "Balx", "Marv", "Farg‘ona vodiysi.")
t.B("Ashtarxoniylar saroyida dastlab miroxur va parvonachi bo‘lgan mang‘it yo‘lboshchisi kim?", "Muhammad Hakimbiy", "Muhammad Rahimbiy", "Doniyolbiy", "Shohmurod", "Muhammad Hakimbiy.")
t.B("Muhammad Hakimbiy qaysi urug‘larga qarshi kurash olib borgan?", "qatag‘on va kenagas", "mang‘it va qo‘ng‘irot", "ming va qipchoq", "nayman va qushchi", "Qatag‘on va kenagas urug‘lariga.")
t.B("Muhammad Hakimbiy qachon vafot etgan?", "1743-yilda", "1747-yilda", "1756-yilda", "1740-yilda", "1743-yilda.")
t.B("Muhammad Rahimbiyning Buxoro taxtini egallashiga nima yo‘l ochgan?", "1747-yilda Nodirshohning o‘ldirilishi", "Abulfayzxonning hajga ketishi", "qozoqlar hujumi", "Rossiya yordami", "Nodirshohning o‘ldirilishi.")
t.B("Muhammad Rahimbiy nima uchun o‘zini xon emas, amir deb e’lon qilgan?", "mang‘itlar chingiziy bo‘lmagani uchun", "xon unvoni taqiqlangani uchun", "Eron talabi bilan", "Rossiya talabi bilan", "Chingiziy bo‘lmagani uchun.")
t.B("Muhammad Rahimbiydan so‘ng hokimiyat kimga o‘tgan?", "amakisi Doniyolbiyga", "o‘g‘li Shohmurodga", "Nasrullaga", "Haydarga", "Amakisi Doniyolbiyga.")
t.B("Chingizxon davrida mang‘itlar qayerga ko‘chirilgan?", "Amudaryoning chap sohiliga", "Sirdaryo bo‘yiga", "Farg‘onaga", "Qrimga", "Amudaryoning chap sohiliga.")
t.B("Buxoro xonligida mang‘itlar qayerda o‘rnashgan?", "Qarshi atrofida", "Nurotada", "Hisorda", "Toshkentda", "Qarshi atrofida.")
t.B("1785-yilgi Buxoro qo‘zg‘olonidan keyin hokimiyatga kim keldi?", "amir Shohmurod", "Doniyolbiy", "amir Nasrulla", "Muhammad Rahimbiy", "Amir Shohmurod.")
t.B("Shohmurod Buxoro aholisiga qanday yorliq bergan?", "tarxon yorlig‘i", "suyurg‘ol yorlig‘i", "vaqf yorlig‘i", "iqto yorlig‘i", "Soliqlardan ozod etuvchi tarxon yorlig‘i.")
t.B("Shohmurod davrida qaysi shahar Erondan qaytarib olingan?", "Marv", "Hirot", "Mashhad", "Balx", "Marv.")
t.B("Yekaterina II Buxoroda madrasa qurish uchun qancha xayriya qilgan?", "50 ming oltin rubl", "5 ming rubl", "1 million rubl", "500 rubl", "50 ming oltin rubl.")
t.B("Shahrisabz necha yurishdan keyin Buxoroga qo‘shib olingan?", "yigirma yilda o‘ttiz ikki yurish", "uch yurish", "o‘n yurish", "bir yurish", "20 yil davomida 32 yurish.")
t.B("Amir Nasrulla Qo‘qonni qachon zabt etgan?", "1842-yilda", "1785-yilda", "1756-yilda", "1868-yilda", "1842-yilda.")
t.B("Amir Nasrulla Qo‘qonda kimni boshqaruvchi etib tayinlagan?", "Ibrohim parvonachini", "Sheralini", "Olloqulixonni", "Muhammad Rahimni", "Ibrohim parvonachini.")
t.B("Mang‘itlar davrida oliy hukmdordan keyingi ikkinchi shaxs kim bo‘lgan?", "qushbegi", "devonbegi", "otaliq", "inoq", "Qushbegi – bosh vazir.")
t.B("Devonbegini yana qanday atashgan?", "quyi qushbegi", "katta otaliq", "to‘pchiboshi", "bayroqdor", "Quyi qushbegi.")
t.B("Davlat bayrog‘ining saqlanishiga javobgar lavozim qaysi?", "to‘qsabo (bayroqdor)", "qo‘rchiboshi", "kutvol", "udaychi", "To‘qsabo.")
t.B("Qurilish ishlariga mas’ul amaldor qanday atalgan?", "kutvol", "udaychi", "inoq", "shig‘ovul", "Kutvol.")
t.NAT("Nodirshoh Buxoro va Samarqandni egallab taladi.", "siyosiy vaziyat yanada murakkablashdi", "Buxoro kuchaydi", "Farg‘ona qaytarib olindi", "ashtarxoniylar mustahkamlandi", "Inqiroz chuqurlashdi.")
t.NAT("Shohmurod Zarafshon vohasida egallanmagan yerlarni tekinga tarqatdi.", "vohada ko‘plab aholi o‘troqlashdi", "urug‘lar isyonlari kuchaydi", "yerlar bo‘sh qoldi", "soliqlar kamaydi", "Aholi o‘troqlashdi.")
t.NAT("Ibrohim parvonachi Qo‘qon aholisiga nisbatan zulm o‘tkazdi.", "ikki oydan so‘ng Sherali uni ag‘dardi va Buxoro–Qo‘qon birlashuvi imkoni qo‘ldan ketdi", "Qo‘qon Buxoroga butunlay qo‘shildi", "Nasrulla Qo‘qonda qoldi", "Rossiya Qo‘qonni oldi", "Buxoro noibi ag‘darildi.")
t.NAT("Muhammad Rahimbiy davlatni qattiqqo‘llik asosida boshqardi.", "Hisor va Shahrisabz bekliklari amirlik tasarrufiga o‘tkazildi", "davlat parchalandi", "u taxtdan ag‘darildi", "Eron Buxoroni oldi", "Isyonchilar ustidan g‘alaba.")
t.TF("Mang‘itlar Buxoro va Xorazm davlatlarining tashkil topishida qatnashgan.", True, "To‘g‘ri.")
t.TF("Amir Shohmurod dabdabali hayot kechirgan.", False, "Noto‘g‘ri: darveshona hayot kechirgan, kundalik xarajati bir tangadan oshmagan.")
t.TF4([("Muftiylarni tayinlash huquqi Buxoro qozikaloniga berilgan.", True), ("Lashkar to‘pchiboshisi harbiy vazir bo‘lgan.", True),
       ("Otaliq mang‘itlar davrida faqat elchilarni qabul qilgan.", False), ("Qushbegi poytaxt va uning viloyati hokimi ham sanalgan.", True)],
      "3-noto‘g‘ri: otaliq shahzodalar tarbiyasi va Samarqand–Buxoro oralig‘i suv ta’minotiga mas’ul bo‘lgan.")
t.MUL([("Amir Nasrullaning portreti Buxoro amirlarining dastlabki musavvir chizgan portreti.", True),
       ("Devonbegi Qorako‘ldagi suv ta’minotiga ham mas’ul bo‘lgan.", True),
       ("Mang‘itlar chingiziylar avlodi bo‘lgan.", False)],
      "III noto‘g‘ri: mang‘itlar chingiziy bo‘lmagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Muhammad Hakimbiy vafot etdi", "Nodirshoh o‘ldirildi", "Muhammad Rahimbiy hokimiyatni to‘la egalladi", "Buxoroda qo‘zg‘olon, Shohmurod hokimiyatga keldi", "Amir Nasrulla Qo‘qonni zabt etdi"],
      "1743 → 1747 → 1756 → 1785 → 1842.")
t.MATCH("Mang‘itlar davri lavozimlarini vazifasi bilan moslashtiring.", ["qushbegi", "devonbegi", "inoq", "udaychi"],
        ["bosh vazir, poytaxt hokimi", "moliya vaziri, zakot yig‘ish", "hukmdor buyrug‘ini xizmatchilarga yetkazuvchi", "urushda harbiylarni turiga qarab taqsimlovchi", "elchilar qabulini uyushtiruvchi"], 'abcd',
        "Qushbegi – bosh vazir; devonbegi – moliya; inoq – buyruq ijrosi; udaychi – harbiylarni taqsimlash.")
t.VENN("Amir Shohmurod", "Amir Nasrulla",
       [("Buxoroga tarxon yorlig‘i bergan", 1), ("Marvni qaytarib olgan", 1),
        ("Shahrisabzni qo‘shib olgan", 2), ("1842-yilda Qo‘qonni zabt etgan", 2),
        ("mang‘itlar sulolasi amiri", 3)],
       "Shohmurod – tarxon, Marv; Nasrulla – Shahrisabz, Qo‘qon; ikkalasi mang‘it amiri.")
t.MAPMATCH('ca2', ['Marv', 'Qarshi', 'Shahrisabz', 'Qo‘qon'],
           ["Shohmurod davrida qaytarib olingan shahar", "mang‘itlar Buxoro xonligida o‘rnashgan hudud", "20 yilda 32 yurishdan so‘ng qo‘shib olingan beklik", "1842-yilda amir Nasrulla zabt etgan shahar"],
           "1 – Marv; 2 – Qarshi; 3 – Shahrisabz; 4 – Qo‘qon.")

# 15-§ Mang‘itlar davrida ijtimoiy-iqtisodiy hayot
t = Topic('y9u15', 9015); TOPICS['y9u15'] = t
t.B("Mang‘itlar davrida naymanlar qayerda yashagan?", "Ziyovuddinda", "Shahrisabzda", "Nurda", "G‘ijduvonda", "Ziyovuddinda.")
t.B("Qipchoqlar qayerda yashagan?", "Kattaqo‘rg‘on va Samarqandda", "Mirzacho‘lda", "G‘ijduvonda", "Karmanada", "Kattaqo‘rg‘on va Samarqandda.")
t.B("Shahrisabzda qaysi urug‘ yashagan?", "kenagaslar", "do‘rmonlar", "burgutlar", "saroylar", "Kenagaslar.")
t.B("G‘ijduvon atrofida qaysi urug‘ yashagan?", "do‘rmonlar", "burgutlar", "naymanlar", "xitoylar", "Do‘rmonlar.")
t.B("Mirzacho‘lda qaysi urug‘ yashagan?", "saroylar", "qo‘ng‘irotlar", "mang‘itlar", "kenagaslar", "Saroylar.")
t.B("Bozorlarga qora va kulrang qorako‘l yetkazib bergan aholi kimlar?", "arablar", "forslar", "qalmiqlar", "tatarlar", "Vardanza, Samarqand, Qarshi atrofidagi arablar.")
t.B("1832-yilda Buxoro qovunlarini maqtagan ingliz elchisi kim?", "Aleksandr Byorns", "Antoni Jenkinson", "Arminiy Vamberi", "Konolli", "Aleksandr Byorns.")
t.B("XVIII asrning 50-yillarida qaysi ariqdagi suvayirg‘ich qayta tiklangan?", "Darg‘om", "Tuyatortar", "Afshona", "Shohrud", "Darg‘om arig‘idagi to‘g‘on.")
t.B("Sun’iy sug‘orishga asoslangan dehqonchilik yerlari qanday atalgan?", "suvli yer", "lalmi yer", "to‘qay yer", "vaqf yer", "Suvli yer.")
t.B("Suvli yerlardan yiliga necha marta hosil olingan?", "ikki marta", "bir marta", "uch marta", "to‘rt marta", "Ikki marta.")
t.B("Ravoq yordamida qancha yerni sug‘orishga yetadigan suv taqsimlangan?", "100 tanob", "10–15 tanob", "1000 tanob", "50 tanob", "100 tanob.")
t.B("Zarafshon suvini taqsimlash uchun Samarqand yaqinida nechta ravoq bo‘lgan?", "21 ta", "12 ta", "100 ta", "7 ta", "21 ravoq.")
t.B("Qaysi hududlarda yetishtirilgan sholi nihoyatda yuqori baholangan?", "Miyonqol va Shahrisabz", "Qarshi va Nurota", "Buxoro va Qorako‘l", "Jizzax va Zomin", "Miyonqol va Shahrisabz.")
t.B("Bedona navli anor qaysi shahar bilan mashhur?", "Shahrisabz", "Samarqand", "Buxoro", "Qarshi", "Shahrisabz anorlari.")
t.B("Qayerda yetishtirilgan tamaki yuqori baholangan?", "Qarshi atrofi, Urgut, Kattaqo‘rg‘on", "Buxoro va Qorako‘l", "Miyonqol", "Nurota", "Qarshi atrofi, Urgut, Kattaqo‘rg‘on.")
t.B("Buzg‘unch Buxorodan qayerga olib borilgan?", "Hirotga", "Rossiyaga", "Xitoyga", "Istanbulga", "Hirotga.")
t.B("Buxoro amirlarining rus podshosiga hadya qilgan harbiy chodiri qayerda saqlanmoqda?", "Ermitajda", "Luvrda", "Britaniya muzeyida", "To‘pqopi saroyida", "Ermitajda.")
t.B("Mang‘itlar davrida pul islohoti qachon o‘tkazilgan?", "1785-yilda", "1708-yilda", "1756-yilda", "1842-yilda", "1785-yilda.")
t.B("1785-yilgi islohotda muomalada qoldirilgan tanga qaysi?", "miri", "ashrafiy", "dinor", "pul", "Muhammad Rahim chiqargan miri.")
t.B("Usmonli sultoni Buxoroga yuborgan elchi kim?", "Olamgir Mehmed Sayidog‘a", "Mustafo", "Mulla Farrux", "Ibrohim parvonachi", "Olamgir Mehmed Sayidog‘a.")
t.B("Mang‘itlar Istanbulga nechtadan ortiq elchi yuborgan?", "o‘ndan", "beshdan", "yuzdan", "ikkidan", "O‘ndan ortiq.")
t.B("1863-yilda Turkistonda bo‘lgan vengriyalik sayyoh kim?", "Arminiy Vamberi", "Aleksandr Byorns", "Murkroft", "Stoddart", "Arminiy Vamberi.")
t.NAT("Urushqoq urug‘lar ishlov berilmagan yerlarga ko‘chirildi.", "turli urug‘larning o‘troqlashuviga sabab bo‘ldi", "urug‘lar Rossiyaga ketdi", "dehqonchilik qisqardi", "isyonlar kuchaydi", "O‘troqlashuv kuchaydi.")
t.NAT("Rossiyada paxtaga ehtiyoj ortdi.", "mamlakatda paxta ekiladigan maydonlar kengaydi", "paxta ekish taqiqlandi", "paxta narxi tushdi", "g‘allachilik kengaydi", "Paxta maydonlari kengaydi.")
t.NAT("Mulkdorlar savdodan orttirgan boyliklarini ishlab chiqarishga sarflamadi.", "boylik mamlakatning iqtisodiy taraqqiyotiga xizmat qilmadi", "sanoat tez rivojlandi", "fabrikalar qurildi", "savdo to‘xtadi", "Iqtisodiy taraqqiyot sustlashdi.")
t.NAT("Mang‘itlar usmonlilardan qurol, ustalar va kitoblar so‘radi.", "usmonlilar faqat kitoblar yuborish bilan chegaralandi", "usmonlilar katta qo‘shin yubordi", "usmonlilar Buxoroni bosib oldi", "Buxoro usmonlilarga qarshi chiqdi", "Amaliy yordam ko‘rsatilmadi.")
t.TF("Murkroft, Trebek, Byorns, Konolli va Stoddart Ost-Indiya kompaniyasining maxfiy topshiriqlarini bajargan.", True, "To‘g‘ri.")
t.TF("Mang‘itlar davrida lalmi yerlar maydoni suvli yerlardan katta bo‘lgan.", False, "Noto‘g‘ri: suvli yerlar maydoni katta bo‘lgan.")
t.TF4([("Qrim Rossiya tarkibiga 1783-yilda o‘tgan.", True), ("Marvlik oilalar Samarqand atrofiga ko‘chib kelgan.", True),
       ("Shohmurod qurol yetkazib berilsa, harbiy harakat boshlashini bildirgan.", True), ("1785-yilgi kumush tangalar katta va to‘rtburchak shaklda bo‘lgan.", False)],
      "4-noto‘g‘ri: kichkina, yumaloq va yuqori soflikda bo‘lgan.")
t.MUL([("Samarqand mang‘itlar davrida ilgarigi mavqeyini tiklagan.", True),
       ("Shahrisabz yaqinidagi tog‘larda yetishtirilgan bodom mashhur edi.", True),
       ("Mang‘itlar davrida chorvachilik rivojlanmagan.", False)],
      "III noto‘g‘ri: chorvachilik ham rivojlangan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Miri tangasi chiqarila boshlandi", "Qrim Rossiya tarkibiga o‘tdi", "Mang‘itlar pul islohotini o‘tkazdi", "A. Byorns Buxoroda bo‘ldi", "A. Vamberi Turkistonga keldi"],
      "1753 → 1783 → 1785 → 1832 → 1863.")
t.MATCH("Urug‘larni yashagan joyi bilan moslashtiring.", ["kenagaslar", "do‘rmonlar", "naymanlar", "burgutlar"],
        ["Shahrisabz", "G‘ijduvon", "Ziyovuddin", "Nur", "Mirzacho‘l"], 'abcd',
        "Kenagaslar – Shahrisabz; do‘rmonlar – G‘ijduvon; naymanlar – Ziyovuddin; burgutlar – Nur.")
t.VENN("Paxta", "Tamaki",
       [("Rossiyada talab katta bo‘lgan", 1), ("Buxoro, Shahrisabz, Kattaqo‘rg‘on ixtisoslashgan", 1),
        ("Qarshi atrofi va Urgutda yuqori baholangan", 2), ("chekish mahsuloti", 2),
        ("mang‘itlar davrida yetishtirilgan ekin", 3)],
       "Paxta – Rossiya talabi; tamaki – Qarshi, Urgut; ikkalasi yetishtirilgan.")
t.MAPMATCH('zarafshon', ['Shahrisabz', 'G‘ijduvon', 'Kattaqo‘rg‘on', 'Panjikent'],
           ["kenagaslar yashagan, bedona anori bilan mashhur shahar", "do‘rmonlar yashagan hudud", "qipchoqlar yashagan, tamakisi mashhur shahar", "XVIII asr 50-yillarida ariqlari tozalangan Zarafshon yuqorisidagi shahar"],
           "1 – Shahrisabz; 2 – G‘ijduvon; 3 – Kattaqo‘rg‘on; 4 – Panjikent.")
