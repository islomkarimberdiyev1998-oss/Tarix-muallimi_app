from qlib import Topic
TOPICS = {}
W = 'globe'; EU = 'europe'; LA = 'latam'; AS = 'asia'; EA = 'eastasia'; IN = 'india'

# 25 Lotin Amerikasi
t = Topic('e8j25', 825); TOPICS['e8j25'] = t
t.B("Lotin Amerikasiga dastlab ko‘chib kelgan ispan va portugallarning avlodlari qanday atalgan?", "kreollar", "metislar", "mulatlar", "hindular", "Kreollar – ispan va portugal avlodlari.")
t.B("Oq tanli va hindular nikohidan tug‘ilgan avlod qanday atalgan?", "metis", "mulat", "kreol", "sambo", "Metis – oq tanli va hindu nikohidan.")
t.B("Oq tanli va qora tanli kishilar nikohidan tug‘ilgan avlod qanday atalgan?", "mulat", "metis", "kreol", "abolitsionist", "Mulat – oq va qora tanlilar avlodi.")
t.B("Braziliya qaysi davlat mustamlakasi edi?", "Portugaliya", "Ispaniya", "Fransiya", "Angliya", "Braziliya Portugaliya mustamlakasi edi.")
t.B("Mustamlakalarda ommaviy qo‘zg‘olon qachon boshlangan?", "1810-yilda", "1821-yilda", "1811-yilda", "1822-yilda", "1810-yili ommaviy qo‘zg‘olon boshlandi.")
t.B("Meksikada 1810-yilda qo‘zg‘olonga chaqirgan qishloq ruhoniysi kim?", "Migel Idalgo", "Xose Morelos", "Simon Bolivar", "San-Martin", "Qishloq ruhoniysi Idalgo.")
t.B("Idalgo qatl etilgach, uning ishini kim davom ettirgan?", "Xose Morelos", "Sukre", "Bolivar", "San-Martin", "Eng yaqin safdoshi Morelos.")
t.B("Meksika qachon mustaqillikka erishgan?", "1821-yilda", "1810-yilda", "1811-yilda", "1822-yilda", "1821-yili Meksika mustaqil bo‘ldi.")
t.B("Venesuelada mustaqillik urushiga kim rahbarlik qilgan?", "Simon Bolivar", "Idalgo", "San-Martin", "Morelos", "Simon Bolivar.")
t.B("Bolivar qanday faxriy nomni olgan?", "«Xaloskor»", "«Ota»", "«Buyuk»", "«Qahramon»", "General unvoni va «Xaloskor» degan faxriy nom.")
t.B("Venesuela qachon mustaqil deb e’lon qilingan?", "1811-yilda", "1810-yilda", "1821-yilda", "1819-yilda", "1811-yili Venesuela mustaqil deb e’lon qilindi.")
t.B("Venesuela va Yangi Grenada birlashuvidan qanday davlat tuzilgan?", "Buyuk Kolumbiya", "Boliviya", "Argentina", "Peru", "Kolumb sharafiga Buyuk Kolumbiya deb nomlandi.")
t.B("Bolivar qachon iste’foga chiqishga majbur bo‘lgan?", "1830-yilda", "1821-yilda", "1811-yilda", "1840-yilda", "1830-yili iste’foga chiqdi.")
t.B("Argentina xalqining milliy bayrami qaysi sana?", "25-may", "4-iyul", "14-iyul", "19-fevral", "Kurash boshlangan 25-may milliy bayram bo‘ldi.")
t.B("Argentinani ozod qilgan inqilobiy qo‘shin qo‘mondoni kim?", "Xose San-Martin", "Bolivar", "Sukre", "Idalgo", "Xose San-Martin.")
t.B("Braziliya Portugaliyadan qachon mustaqil deb e’lon qilingan?", "1822-yilda", "1821-yilda", "1810-yilda", "1830-yilda", "1822-yili.")
t.B("Yuqori Peru kimning sharafiga Boliviya deb atalgan?", "Simon Bolivar", "Sukre", "San-Martin", "Kolumb", "Bolivar sharafiga.")
t.B("Ispaniya qaysi mustamlakalarini saqlab qolgan?", "Kuba va Puerto-Riko", "Meksika va Peru", "Braziliya va Chili", "Argentina va Urugvay", "Faqat Kuba va Puerto-Riko.")
t.NAT("Ispaniya amaldorlari kreollarni oliy lavozimlarga yo‘latmadi, savdoni cheklab, og‘ir soliq soldi.", "mustamlakachilikka qarshi ozodlik harakati vujudga keldi", "kreollar Ispaniyaga ko‘chib ketdi", "savdo kengaydi", "Ispaniya kuchaydi",
      "Bu omillar ozodlik harakatini keltirib chiqardi.")
t.NAT("Bolivar qullik bekor etilganini e’lon qildi.", "qora tanli qullarning bir qismi uning qo‘shiniga qo‘shildi", "qullar Ispaniyaga qochdi", "kreollar uni qo‘llab-quvvatladi", "urush to‘xtadi",
      "Qora tanli qullarning bir qismi qo‘shinga jalb etildi.")
t.TF("Braziliyadan tashqari barcha Lotin Amerikasi mamlakatlarida respublika tuzumi o‘rnatilgan.", True, "To‘g‘ri.")
t.TF("Bolivarning yirik pomeshiklar yerini musodara qilish loyihasi amalga oshgan.", False, "Noto‘g‘ri: pomeshiklar qarshiligi tufayli amalga oshmay qoldi.")
t.MUL([("Bolivarga yordamga irland, ingliz, nemis, polyak va rus ko‘ngillilari kelgan.", True), ("General Sukre Bolivarning safdoshi bo‘lgan.", True), ("Lotin Amerikasida 1860-yildan oldin sanoat jadal rivojlangan.", False)],
      "III noto‘g‘ri: iqtisodning sezilarli o‘sishi faqat 1860-yildan kuzatiladi.")
t.MATCH("Qahramonlarni mamlakatlari bilan moslashtiring.", ["Migel Idalgo", "Simon Bolivar", "Xose San-Martin", "Sukre"],
        ["Meksika", "Venesuela", "Argentina", "Yuqori Peru (Boliviya)", "Braziliya"], 'abcd', "Idalgo – Meksika; Bolivar – Venesuela; San-Martin – Argentina; Sukre – Yuqori Peru.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Ommaviy qo‘zg‘olon boshlandi", "Venesuela mustaqilligi e’lon qilindi", "Meksika mustaqillikka erishdi", "Braziliya mustaqil deb e’lon qilindi", "Bolivar iste’foga chiqdi"],
      "1810 → 1811 → 1821 → 1822 → 1830.")
t.MAPMATCH(LA, ['Meksika', 'Venesuela', 'Argentina', 'Braziliya'],
           ["Idalgo va Morelos vatani", "Bolivar vatani", "San-Martin ozod qilgan mamlakat", "Portugaliyadan mustaqil bo‘lgan mamlakat"],
           "1 – Meksika; 2 – Venesuela; 3 – Argentina; 4 – Braziliya.")
t.VENN("Ispaniya mustamlakalari", "Portugaliya mustamlakasi (Braziliya)",
       [("Bolivar, San-Martin boshchiligida ozod bo‘lgan", 1), ("respublika tuzumi o‘rnatilgan", 1),
        ("1822-yilda mustaqil deb e’lon qilingan", 2), ("respublika o‘rnatilmagan yagona davlat", 2),
        ("mustamlakachilik zulmidan ozod bo‘lgan", 3)],
       "Ispaniya mustamlakalari – respublikalar. Braziliya – 1822, respublika emas. Hammasi ozod bo‘ldi.")

# 26 Hindiston 1800–1870
t = Topic('e8j26', 826); TOPICS['e8j26'] = t
t.B("Britaniya hukumati Hindistonni boshqarish uchun qanday kengash tuzgan?", "«Hindiston ishlari bo‘yicha nazorat kengashi»", "«Oliy Kengash»", "«Ost-Indiya kengashi»", "«Lordlar palatasi»", "«Hindiston ishlari bo‘yicha nazorat kengashi» tashkil etildi.")
t.B("Britaniyaning Hindistondagi barcha mustamlakalari general-gubernatori kim etib tayinlangan?", "Ost-Indiya kompaniyasining Kalkuttadagi gubernatori", "Hindiston podshosi", "Bahodirshoh II", "Britaniya bosh vaziri", "Kompaniyaning Kalkutta shahridagi gubernatori.")
t.B("Hindlardan tuzilgan yollanma askarlar qanday atalgan?", "sipohiylar", "yanicharlar", "samuraylar", "kreollar", "Ular sipohiy deb atalgan.")
t.B("Sipohiylar qo‘zg‘oloniga bevosita nima turtki bo‘lgan?", "yog‘langan qog‘ozli patronli miltiqning joriy etilishi", "soliq oshirilishi", "maosh kamaytirilishi", "Dehli bosib olinishi", "Patron yog‘i haqidagi gap qo‘zg‘olonga sabab bo‘ldi.")
t.B("Sipohiylar qo‘zg‘oloni qachon boshlangan?", "1857-yilda", "1858-yilda", "1850-yilda", "1840-yilda", "Qo‘zg‘olon 1857-yili boshlandi.")
t.B("Sipohiylar qaysi shaharni egallagan?", "Dehli", "Kalkutta", "Bombey", "Agra", "Sipohiylar tez orada Dehlini egalladi.")
t.B("Qo‘zg‘olonchilar chaqiriqni imzolashga majbur qilgan hukmdor kim?", "Bahodirshoh II", "Akbar", "Avrangzeb", "Shoh Jahon", "Bahodirshoh II.")
t.B("Hindiston qachon Buyuk Britaniya mulki deb e’lon qilingan?", "1858-yilda", "1857-yilda", "1757-yilda", "1876-yilda", "1858-yili.")
t.B("Qo‘zg‘olondan keyin qaysi kompaniya tugatilgan?", "Ost-Indiya kompaniyasi", "Moskva kompaniyasi", "Levant kompaniyasi", "Gudzon kompaniyasi", "Ost-Indiya kompaniyasi tugatildi.")
t.NAT("Britaniya to‘qimachilik mahsulotlari Hindistonda sotila boshladi.", "mahalliy to‘quvchilar xonavayron bo‘lib, ochlikka mahkum etildi", "hind to‘qimachiligi rivojlandi", "Hindiston eksportni ko‘paytirdi", "narxlar oshdi",
      "Mahalliy hunarmandlar raqobat qila olmay xonavayron bo‘ldi.")
t.NAT("Mustamlakachilar Dehliga to‘plarni fillarga ortib olib kirdi.", "jang taqdiri hal bo‘lib, qo‘zg‘olon bostirildi", "sipohiylar g‘alaba qozondi", "Dehli mustaqil bo‘ldi", "inglizlar chekindi",
      "Bu tadbir jang taqdirini hal qildi.")
t.NAT("Britaniya qo‘zg‘olondan xulosa chiqarib, hindlarga ta’lim yo‘lini ochdi.", "mahalliy ziyolilar qatlami shakllandi", "ta’lim taqiqlandi", "ingliz tili yo‘qoldi", "milliy harakat to‘xtadi",
      "Maktab va kollejlar ochilib, ziyolilar qatlami shakllana bordi.")
t.TF("Qo‘zg‘olondan so‘ng yer egalarining soliqlarni oshirishi taqiqlangan.", True, "To‘g‘ri.")
t.TF("Hinduiylikda cho‘chqa muqaddas hisoblanadi.", False, "Noto‘g‘ri: hinduiylikda sigir muqaddas hisoblanadi.")
t.MUL([("Sipohiylar qo‘shini hindlarning yagona uyushgan tashkiloti edi.", True), ("Mahalliy rojalarning yerga egalik huquqi daxlsiz deb e’lon qilingan.", True), ("Qo‘zg‘olonni bostirishda Britaniya qo‘shini tinch aholiga rahm qilgan.", False)],
      "III noto‘g‘ri: dahshatli vahshiyliklar qilindi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Bengaliya bosib olindi", "Sipohiylar qo‘zg‘oloni boshlandi", "Hindiston Britaniya mulki deb e’lon qilindi"], "1757 → 1857 → 1858.")
t.MAPN(IN, ['Dehli', 'Kalkutta', 'Bombey', 'Kobul'], "1857-yilda sipohiylar egallagan shahar qaysi raqam bilan belgilangan?", "Dehli – 1.", ask_idx=0)
t.MAPN(IN, ['Dehli', 'Kalkutta', 'Bombey', 'Kobul'], "Ost-Indiya kompaniyasi gubernatori joylashgan shahar qaysi raqam bilan belgilangan?", "Kalkutta – 2.", ask_idx=1)
t.VENN("Sipohiylar qo‘zg‘olonigacha", "Qo‘zg‘olondan keyin",
       [("Hindistonni Ost-Indiya kompaniyasi boshqargan", 1), ("hindlarga ta’lim yo‘li yopiq", 1),
        ("Hindiston Britaniya mulki deb e’lon qilingan", 2), ("maktab va kollejlar ochilgan", 2),
        ("Hindiston Buyuk Britaniya mustamlakasi", 3)],
       "Avval – kompaniya boshqaruvi; keyin – toj mulki, ta’lim. Har ikki davrda mustamlaka.")

# 27 Xitoy 1800–1870
t = Topic('e8j27', 827); TOPICS['e8j27'] = t
t.B("Xitoy imperatori bandargohlarni tashqi savdo uchun qachon yopgan?", "1757-yilda", "1840-yilda", "1644-yilda", "1856-yilda", "1757-yili bandargohlar yopiq deb e’lon qilindi.")
t.B("Xitoyni tashqi dunyodan ajratish siyosati qanday atalgan?", "«yopiq eshiklar»", "«ochiq eshiklar»", "«qit’a qamali»", "«yangi kurs»", "«Yopiq eshiklar» siyosati.")
t.B("Tashqi savdo qaysi port orqali olib borilgan?", "Guanchjou", "Shanxay", "Gonkong", "Nankin", "Faqat Guanchjou porti orqali.")
t.B("Britaniya savdogarlari Hindistondan Xitoyga noqonuniy nima kiritgan?", "afyun", "paxta", "choy", "ipak", "Afyun (qora dori) kiritildi.")
t.B("Birinchi afyun urushi qaysi yillarda bo‘lgan?", "1840–1842", "1856–1860", "1850–1864", "1757–1760", "Birinchi afyun urushi 1840–1842-yillarda.")
t.B("Birinchi afyun urushidan keyin Britaniya qaysi orolni bosib olgan?", "Gonkong", "Tayvan", "Xaynan", "Okinava", "Britaniya Gonkong orolini bosib oldi.")
t.B("Ikkinchi afyun urushi qaysi yillarda bo‘lgan?", "1856–1860", "1840–1842", "1850–1864", "1860–1870", "Ikkinchi afyun urushi 1856–1860-yillarda.")
t.B("Ikkinchi afyun urushida Xitoyga qarshi qaysi davlatlar urushgan?", "Buyuk Britaniya va Fransiya", "Rossiya va Yaponiya", "AQSH va Germaniya", "Portugaliya va Ispaniya", "Britaniya va Fransiyaning birlashgan qo‘shinlari.")
t.B("Taypinlar qo‘zg‘oloniga kim boshchilik qilgan?", "Xun Syutsyuan", "Van Yanmin", "Shunchji", "Abaxay", "Maktab o‘qituvchisi Xun Syutsyuan.")
t.B("Taypinlar davlati qanday nomlangan?", "«Samoviy mo‘l-ko‘lchilik davlati»", "«Chin davlati»", "«Osmon osti»", "«Kunchiqar davlat»", "«Taypin tyango» – Samoviy mo‘l-ko‘lchilik davlati.")
t.B("Taypinlar davlatining markazi qaysi shahar bo‘lgan?", "Nankin", "Pekin", "Guanchjou", "Shanxay", "Markazi Nankin shahri.")
t.B("Taypinlar davlati qaysi yillarda mavjud bo‘lgan?", "1850–1864", "1840–1842", "1856–1860", "1864–1870", "1850–1864-yillarda.")
t.NAT("Mahalliy ma’murlar afyun karvonlarini musodara qildi.", "Britaniya 1840-yilda Xitoyga qarshi urush boshladi", "afyun savdosi to‘xtadi", "Britaniya uzr so‘radi", "Xitoy Hindistonni bosib oldi",
      "Bunga javoban Birinchi afyun urushi boshlandi.")
t.NAT("Ikkinchi afyun urushida Xitoy yengildi.", "ingliz va fransuzlar Xitoy qonunlari va sudiga bo‘ysunishdan ozod qilindi", "Xitoy portlari yopildi", "Fransiya Xitoyni tark etdi", "Xitoy kuchaydi",
      "Teng bo‘lmagan shartnomalar bilan chet elliklarga imtiyozlar berildi.")
t.NAT("Taypinlar yerni oila a’zolari soniga qarab teng bo‘lmoqchi bo‘ldi.", "mulkdor tabaqalar qo‘zg‘olondan uzoqlashib, rahbarlar orasida nizo chiqdi", "barcha dehqonlar qo‘llab-quvvatladi", "qo‘zg‘olon g‘alaba qozondi", "chin sulolasi taslim bo‘ldi",
      "Bu reja mulkdorlarni uzoqlashtirib, mag‘lubiyatga yo‘l ochdi.")
t.TF("Taypinlarga qarshi chin hukumatiga Britaniya, Fransiya va AQSH yordam bergan.", True, "To‘g‘ri.")
t.TF("Birinchi afyun urushidan so‘ng Xitoy afyun olib kirishni qonuniy deb tan olgan.", False, "Noto‘g‘ri: Xitoy buni tan olmadi.")
t.MUL([("Ikkinchi afyun urushida imperatorning yozgi saroyi talangan.", True), ("1864-yilda hukumat qo‘shinlari Nankinni ishg‘ol qilgan.", True), ("Xun Syutsyuan asir olinib, Britaniyaga olib ketilgan.", False)],
      "III noto‘g‘ri: Xun Syutsyuan o‘z joniga qasd qilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Bandargohlar yopildi", "Birinchi afyun urushi boshlandi", "Taypinlar qo‘zg‘oloni boshlandi", "Ikkinchi afyun urushi boshlandi", "Nankin hukumat qo‘liga o‘tdi"],
      "1757 → 1840 → 1850 → 1856 → 1864.")
t.MAPMATCH(EA, ['Gonkong', 'Nankin', 'Pekin'],
           ["1842-yilda Britaniya bosib olgan orol", "taypinlar davlati markazi", "yaqinida imperatorning yozgi saroyi talangan poytaxt"],
           "1 – Gonkong; 2 – Nankin; 3 – Pekin.")
t.VENN("Birinchi afyun urushi", "Ikkinchi afyun urushi",
       [("1840–1842-yillarda bo‘lgan", 1), ("Britaniya Gonkongni bosib olgan", 1),
        ("Britaniya va Fransiya birgalikda urushgan", 2), ("yozgi saroy talangan", 2),
        ("Xitoy yengilib, teng bo‘lmagan shartnoma imzolagan", 3)],
       "I urush – 1840, Gonkong. II urush – Britaniya va Fransiya, yozgi saroy. Ikkalasida Xitoy yengilgan.")

# 28 Yaponiya 1800–1870
t = Topic('e8j28', 828); TOPICS['e8j28'] = t
t.B("Yaponiyani ochilishga kim majbur etgan?", "AQSH harbiy-dengiz floti", "Britaniya armiyasi", "Rossiya floti", "Fransiya qo‘shini", "1854-yili AQSH floti majbur etdi.")
t.B("AQSH va Yaponiya «Tinchlik va do‘stlik to‘g‘risida»gi Shartnomani qachon imzolagan?", "1854-yilda", "1858-yilda", "1867-yilda", "1868-yilda", "1854-yili imzolandi.")
t.B("1854-yilgi shartnomaga ko‘ra Yaponiya AQShga nechta port ochgan?", "ikkita", "bitta", "beshta", "o‘nta", "Yaponiya AQShga ikkita portini ochdi.")
t.B("AQSH fuqarolariga qachon eksterritoriallik huquqi berilgan?", "1858-yilda", "1854-yilda", "1867-yilda", "1872-yilda", "1858-yili.")
t.B("Eksterritoriallik huquqi nimani anglatadi?", "chet elliklarning mahalliy sud qila olmasligi va daxlsizligi", "bojsiz savdo", "yer sotib olish", "harbiy baza qurish", "Chet el fuqarolari daxlsizligi va mahalliy sudga bo‘ysunmasligi.")
t.B("Syogun hokimiyatini ag‘darish harakatining asosiy kuchi kimlar edi?", "samuraylar", "dehqonlar", "chet elliklar", "daymyolar", "Asosiy kuch samuraylar edi.")
t.B("Oxirgi syogun kimning foydasiga hokimiyatdan voz kechgan?", "imperator Mutsuxito", "Tokugava Ieyasu", "Yosimune", "AQSH konsuli", "1867-yili imperator Mutsuxito foydasiga.")
t.B("«Meydzi» so‘zi qanday ma’noni bildiradi?", "«ma’rifatli boshqaruv»", "«quyosh xudosi»", "«yangi davr»", "«harbiy hukmdor»", "Meydzi – «ma’rifatli boshqaruv».")
t.B("Agrar islohotdan keyin yer solig‘i daromadning qancha qismini tashkil etgan?", "50 foizini", "10 foizini", "25 foizini", "75 foizini", "Soliq daromadning 50 foiziga teng edi.")
t.B("Islohotdan 10 yil o‘tib yer olgan dehqonlarning qancha qismi yerini saqlab qolgan?", "1/3 qismi", "yarmi", "hammasi", "1/10 qismi", "Atigi 1/3 qismi saqlab qoldi.")
t.B("Ma’muriy islohotdan keyin joylarda hokimiyat kimga o‘tgan?", "imperator tayinlaydigan gubernatorlarga", "knyazlarga", "samuraylarga", "syogunga", "Imperator tayinlaydigan gubernatorlarga.")
t.B("Yangi qo‘shin uchun qaysi davlatdan harbiy mutaxassislar taklif etilgan?", "Fransiya", "AQSH", "Rossiya", "Xitoy", "Fransiyadan mutaxassislar taklif etildi.")
t.B("Yaponiyaning quyosh xudosi qanday atalgan?", "Amaterasu", "Meydzi", "Mutsuxito", "Budda", "Quyosh xudosi Amaterasu.")
t.B("Yaponiyada joriy etilgan yagona pul birligi qanday?", "iyena", "yuan", "von", "rupiya", "Yagona pul birligi – iyena.")
t.B("Meydzi islohotlari tarixga qanday nom bilan kirgan?", "«Meydzi inqilobi»", "«Sharafli inqilob»", "«Tokugava islohoti»", "«Yopiq eshiklar»", "«Meydzi inqilobi» nomi bilan.")
t.NAT("Yaponiya bozorlari chet el tovarlariga to‘ldi.", "manufaktura va hunarmandchilikka zarba berilib, chet elliklarga qarshi harakat kuchaydi", "Yaponiya sanoati gullab-yashnadi", "syogun hokimiyati mustahkamlandi", "samuraylar boyidi",
      "Bu iqtisodga zarar berdi, chet elliklarni quvish talabi kuchaydi.")
t.NAT("Agrar islohot yerni sotish va xususiy mulkka aylantirishga ruxsat berdi.", "qishloq xo‘jaligida kapitalistik munosabatlar rivojlandi", "feodal tartiblar kuchaydi", "dehqonlar yerga ega bo‘lmadi", "soliq bekor qilindi",
      "Islohot kapitalistik munosabatlarni ta’minladi.")
t.NAT("Umumiy harbiy majburiyat joriy etildi.", "samuraylar doimiy harbiy xizmat imtiyozidan mahrum bo‘ldi", "samuraylar kuchaydi", "qo‘shin tarqatildi", "knyazlar qo‘shini tiklandi",
      "Samuraylar avvalgi qiyofasini yo‘qotdi.")
t.TF("Yaponiya an’anaviy sivilizatsiya mamlakatlari ichida birinchi bo‘lib industrial taraqqiyot yo‘liga kirgan.", True, "To‘g‘ri.")
t.TF("Meydzi islohotlarida Yaponiya milliy an’analaridan butunlay voz kechgan.", False, "Noto‘g‘ri: milliy an’analardan voz kechmagan holda zamonaviylashtirildi.")
t.MUL([("Davlat sanoat korxonalarini qurib, keyin firmalarga imtiyozli asosda sotgan.", True), ("Harbiylar ongiga imperatorga muhabbat va o‘limni pisand qilmaslik singdirilgan.", True), ("Yaponiya bilan Yevropa davlatlari teng huquqli shartnomalar tuzgan.", False)],
      "III noto‘g‘ri: shartnomalar Yaponiyani kamsituvchi, teng bo‘lmagan edi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Tokugava syogunligi o‘rnatildi", "AQSH floti Yaponiyani ochdi", "Yana bir nechta port ochildi", "Syogun hokimiyatdan voz kechdi"],
      "1603 → 1854 → 1858 → 1867.")
t.MAP1(EA, 'Yaponiya', "XIX asr o‘rtalarida AQSH floti «ochilish»ga majbur etgan, keyin Meydzi islohotlarini o‘tkazgan mamlakatni aniqlang.", "Yaponiya", ["Koreya", "Xitoy", "Filippin"], "1 – Yaponiya.")
t.VENN("Tokugava syogunligi", "Meydzi davri",
       [("syogun amalda hokimiyatda bo‘lgan", 1), ("mamlakat chet elliklar uchun yopiq", 1),
        ("imperator hokimiyati tiklangan", 2), ("Yevropacha qo‘shin, iyena joriy etilgan", 2),
        ("imperator ilohiy deb hisoblangan", 3)],
       "Tokugava – syogun, yopiqlik. Meydzi – imperator, islohotlar. Ikkala davrda imperator muqaddas.")

# 29 Koreya 1800–1870
t = Topic('e8j29', 829); TOPICS['e8j29'] = t
t.B("XIX asr boshida Li sulolasiga qarshi eng yirik qo‘zg‘olonga kim boshchilik qilgan?", "Xon Gyon Ne", "Li Xa In", "Kojon", "Li Son Ge", "Boy zamindor Xon Gyon Ne.")
t.B("Jejudo orolida dehqon va baliqchilar qo‘zg‘oloni qachon bo‘lgan?", "1813-yilda", "1831-yilda", "1863-yilda", "1832-yilda", "1813-yili Jejudo orolida qo‘zg‘olon bo‘ldi.")
t.B("Rim papasi Koreya yepiskopligi tuzilganini qachon e’lon qilgan?", "1831-yilda", "1832-yilda", "1813-yilda", "1863-yilda", "1831-yili.")
t.B("1832-yilda Koreyaga savdo munosabatlarini taklif qilgan kema qaysi davlat nomidan kelgan?", "Buyuk Britaniya", "Fransiya", "AQSH", "Rossiya", "Buyuk Britaniya nomidan; rad javobini oldi.")
t.B("Koreyaga yashirin kirgan missionerlar asosan qaysi millat vakillari edi?", "fransuzlar", "inglizlar", "amerikaliklar", "nemislar", "Asosan fransuz missionerlari.")
t.B("1863-yilda 12 yoshida Kojon nomi bilan taxtga o‘tqazilgan kim?", "Li Sze Xvan", "Li Xa In", "Xon Gyon Ne", "Li Son Ge", "Li Sze Xvan qirol Kojon bo‘ldi.")
t.B("Hokimiyatni vaqtincha egallagan qirolning otasi qanday unvon bilan mashhur?", "tevongun (hokim)", "syogun", "imperator", "noron", "Li Xa In tevongun (hokim) bo‘ldi.")
t.B("Muhim lavozimlarni egallagan asilzodalar partiyasi qanday atalgan?", "noron (oqsoqollar)", "taypin", "samuray", "daymyo", "Noron (oqsoqollar) partiyasi.")
t.B("Tevongun qaysi saroyni tiklagan?", "Kyonbokkun", "To‘pqopi", "Ali Kapa", "Toshhovli", "XVI asrda yonib ketgan Kyonbokkun saroyini tikladi.")
t.B("Oddiy kishilar to‘laydigan harbiy soliq nima bilan almashtirilgan?", "barcha uchun uy boshi solig‘i", "jizya", "yer solig‘i", "boj", "Majburiy uy boshi solig‘i bilan almashtirildi.")
t.NAT("Missionerlar va xristian koreyslar qatl etildi.", "Fransiya Koreyaga harbiy kemalar yubordi", "Fransiya Koreya bilan ittifoq tuzdi", "Koreya xristianlikni qabul qildi", "missionerlar ko‘paydi",
      "Bu fransuz harbiy kemalari yuborilishiga bahona bo‘ldi.")
t.NAT("Xitoy kuch bilan «ochildi», manjurlar G‘arbga taslim bo‘ldi.", "Seul hukmdorlari Koreyani tashqi dunyodan yanada qattiqroq ajratdi", "Koreya portlarini ochdi", "Koreya Xitoyni bosib oldi", "Koreya AQSH bilan shartnoma tuzdi",
      "Koreya yakkalanish siyosatini kuchaytirdi.")
t.NAT("Koreya zamonaviy islohotlar o‘tkazmay, o‘zini yakkalab qo‘ydi.", "iqtisodiyot nochor qolib, Koreya Yaponiya mustamlakasiga aylandi", "Koreya sanoatlashdi", "Koreya mustaqilligini mustahkamladi", "Koreya Xitoyga qo‘shildi",
      "Bu oxir-oqibat Yaponiya mustamlakasiga olib keldi.")
t.TF("Tevongun dvoryan bo‘lmagan qatlamlarga ham davlat xizmatiga kirish imkonini bergan.", True, "To‘g‘ri.")
t.TF("Amerikaliklar Koreya bilan teng bo‘lmagan shartnomalar tuzishga muvaffaq bo‘lgan.", False, "Noto‘g‘ri: ularning urinishlari koreyslarning qarshiligiga uchrab, amalga oshmadi.")
t.MUL([("Fransuz kemalaridan ikkitasi Koreya qirg‘oqlari yaqinida sayozlikka o‘tirib qolgan.", True), ("Xalqqa qora rangli oyoq kiyim kiyish taqiqlangan.", True), ("Xon Gyon Ne qo‘zg‘oloni g‘alaba qozongan.", False)],
      "III noto‘g‘ri: qo‘zg‘olon mag‘lub bo‘lib, Xon Gyon Ne qatl etildi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Jejudo qo‘zg‘oloni", "Koreya yepiskopligi e’lon qilindi", "Britaniya kemasi savdo taklif qildi", "Kojon taxtga o‘tqazildi"],
      "1813 → 1831 → 1832 → 1863.")
t.MAPMATCH(EA, ['Seul', 'Jejudo oroli', 'Yaponiya'],
           ["Koreya hukmdorlari poytaxti", "1813-yilda dehqon va baliqchilar qo‘zg‘oloni bo‘lgan orol", "keyinchalik Koreyani mustamlakaga aylantirgan davlat"], "1 – Seul; 2 – Jejudo; 3 – Yaponiya.")
t.VENN("Koreya (XIX asr)", "Yaponiya (XIX asr)",
       [("o‘zini tashqi dunyodan qattiq ajratgan", 1), ("keyinchalik mustamlakaga aylangan", 1),
        ("AQSH floti majbur qilib ochgan", 2), ("Meydzi islohotlari o‘tkazilgan", 2),
        ("G‘arb davlatlari bosimiga uchragan", 3)],
       "Koreya – yakkalanish, mustamlaka. Yaponiya – ochilish, islohot. Ikkalasiga G‘arb bosimi.")
