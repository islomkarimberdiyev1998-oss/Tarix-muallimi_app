from qlib import Topic, PLACES, REG
TOPICS = {}

# 15-mavzu. Yosh buxoroliklar va amirlikning tugatilishi
t = Topic('y10u15', 10015); TOPICS['y10u15'] = t
t.B("Yosh buxoroliklar faoliyatini qachondan boshlagan?", "1910-yildan", "1893-yildan", "1917-yildan", "1905-yildan", "1910-yildan.")
t.B("Yosh buxoroliklar harakatiga qaysi partiya katta ta’sir ko‘rsatgan?", "yosh turklarning «Ittihodi va taraqqiy»", "bolsheviklar", "kadetlar", "eserlar", "«Ittihodi va taraqqiy».")
t.B("Yosh buxoroliklar davlat tuzumini nimaga almashtirmoqchi bo‘lgan?", "yevropacha konstitutsion monarxiyaga", "respublikaga", "xalifalikka", "sovet hokimiyatiga", "Konstitutsion monarxiyaga.")
t.B("Amir Abdulahad qachon vafot etgan?", "1910-yil 10-dekabrda", "1917-yil aprelda", "1920-yil sentyabrda", "1893-yilda", "1910-yil 10-dekabr.")
t.B("Amir Abdulahaddan so‘ng taxtni kim egallagan?", "Said Olimxon", "Asfandiyorxon", "Said Abdulla", "Muzaffar", "O‘g‘li Said Olimxon.")
t.B("Sayid Olimxon qachon Peterburgga o‘qishga yuborilgan?", "1893-yilda", "1910-yilda", "1885-yilda", "1900-yilda", "1893-yilda, 3 yil o‘qigan.")
t.B("1917-yil 8-aprelda jadidlar qaysi shaharlarda namoyish o‘tkazgan?", "Karki va Buxoroda", "Toshkent va Samarqandda", "Xiva va Urganchda", "Qo‘qon va Andijonda", "Karki va Buxoroda.")
t.B("Buxoroda namoyishga nechta kishi to‘plangan?", "150 kishi", "1500 kishi", "30 kishi", "15 ming kishi", "150 kishi.")
t.B("Buxorodagi namoyishga kimlar boshchilik qilgan?", "Fayzulla Xo‘jayev va Abdurauf Fitrat", "Behbudiy va Mirzo G‘ulom", "Munavvarqori va Avloniy", "Usmon Xo‘ja va Ayniy", "F. Xo‘jayev va A. Fitrat.")
t.B("Namoyishdan keyin nechtadan ziyod kishi hibsga olingan?", "30 dan", "150 dan", "3 dan", "300 dan", "30 dan ziyod.")
t.B("1920-yil yanvarda Toshkentda qanday tashkilot tuzilgan?", "«Inqilobchi yosh buxoroliklarning Turkistondagi markaziy byurosi»", "«Sho‘royi islomiya»", "«Milliy ittihod»", "«Tarbiyai atfol»", "Inqilobchi yosh buxoroliklar markaziy byurosi.")
t.B("1920-yil avgustda Chorjo‘yda nima tuzilgan?", "Muvaqqat inqilobiy qo‘mita", "Xalq Nozirlar Kengashi", "Milliy markaz", "Majlis", "Muvaqqat inqilobiy qo‘mita.")
t.B("Amir Olimxon qayerga chekinishga majbur bo‘lgan?", "Afg‘onistonga", "Eronga", "Turkiyaga", "Xivaga", "Afg‘onistonga.")
t.B("Bolsheviklar armiyasi Buxoroga qachon kirgan?", "1920-yil 2-sentyabrda", "1920-yil 6-oktyabrda", "1917-yil 8-aprelda", "1918-yil 22-fevralda", "1920-yil 2-sentyabr.")
t.B("Buxoro Xalq Sovet Respublikasi qachon e’lon qilingan?", "1920-yil 6-oktyabrda", "1920-yil 2-sentyabrda", "1920-yil 27-aprelda", "1924-yilda", "1920-yil 6-oktyabr.")
t.B("BXSR birinchi hukumati – Xalq Nozirlar Kengashiga kim boshchilik qilgan?", "Fayzulla Xo‘jayev", "Fitrat", "Polvonniyoz Yusupov", "Usmon Xo‘ja", "Fayzulla Xo‘jayev.")
t.NAT("Amir Olimxon dastlab siyosiy kuchga ega emas edi.", "u yosh buxoroliklarga yon berib, islohot va’dalarini berdi", "yosh buxoroliklarni darhol qatl etdi", "taxtdan voz kechdi", "Rossiyaga qochdi", "Islohot va’dalari.")
t.NAT("1917-yil 8-aprelda namoyishchilar Arkka yetib keldi.", "amir sarbozlari ularni tarqatib, hibsga ola boshladi", "amir namoyishchilarni qabul qildi", "amir taxtdan voz kechdi", "namoyishchilar Arkni egalladi", "Namoyish tarqatildi.")
t.NAT("Yosh buxoroliklar va bolsheviklar birgalikda qo‘zg‘olon boshladi, sovet qo‘shinlari Buxoroga tashlandi.", "amir deyarli qarshilik ko‘rsata olmay, Afg‘onistonga chekindi", "amir g‘alaba qozondi", "Buxoro Xivaga qo‘shildi", "qo‘zg‘olon bostirildi", "Amirlik tugatildi.")
t.NAT("Amir farmonida amaldorlarga ustama haq olish taqiqlandi.", "buning o‘rniga davlat tomonidan qat’iy belgilangan maosh ta’sis etildi", "amaldorlar soliqdan ozod bo‘ldi", "maoshlar bekor qilindi", "amaldorlar ishdan bo‘shatildi", "Belgilangan maosh joriy etildi.")
t.TF("Namoyish shiorlarida «Hurriyat, Adolat, Musavvat!» da’vatlari bo‘lgan.", True, "To‘g‘ri.")
t.TF("Amir Olimxon taxtga o‘tirgach Buxoro davlat va diniy tizimini tubdan o‘zgartirgan.", False, "Noto‘g‘ri: bunday taraddudda bo‘lmagan.")
t.TF4([("Sadriddin Ayniy yosh buxoroliklar namoyandalaridan biri.", True), ("Farmonda bosmaxona ochish va’da qilingan.", True),
       ("Behbudiy farmonni vazmin, bosiq harakatlar bilan qo‘llab-quvvatlagan.", True), ("Inqilobchi yosh buxoroliklar byurosi Buxoroda tuzilgan.", False)],
      "4-noto‘g‘ri: Toshkentda tuzilgan.")
t.MUL([("Yosh buxoroliklar harbiy maktablar ochishni ko‘zlagan.", True),
       ("Farmonni amalga oshirish uchun Yosh buxoroliklar qo‘mitasi tuzilgan.", True),
       ("Sovet qo‘shinlari Buxoroga aviatsiyasiz, kam qurol bilan kirgan.", False)],
      "III noto‘g‘ri: yaxshi qurollangan, harbiy aviatsiyali qo‘shin tashlangan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Olimxon Peterburgga o‘qishga ketdi", "Said Olimxon taxtga o‘tirdi", "Karki va Buxorodagi namoyish", "Toshkentda markaziy byuro tuzildi", "bolsheviklar Buxoroga kirdi", "BXSR e’lon qilindi"],
      "1893 → 1910 → 1917 → 1920-yanvar → 1920-sentyabr → 1920-oktyabr.")
t.MATCH("Shaxslarni ma’lumot bilan moslashtiring.", ["Fayzulla Xo‘jayev", "Said Olimxon", "Abdulahad", "Fitrat"],
        ["BXSR birinchi hukumati boshlig‘i", "Afg‘onistonga chekingan so‘nggi amir", "1910-yilda vafot etgan amir", "namoyish rahbarlaridan, adib", "Xiva xoni"], 'abcd',
        "Xo‘jayev – BXSR; Olimxon – so‘nggi amir; Abdulahad – 1910; Fitrat – namoyish rahbari.")
t.VENN("Yosh buxoroliklar", "Diniy mutaassiblar",
       [("demokratik islohotlar tarafdori", 1), ("konstitutsion monarxiya g‘oyasi", 1),
        ("har qanday yangilik dushmani", 2), ("islohotlarga qarshi", 2),
        ("XX asr boshidagi Buxoro ijtimoiy kuchi", 3)],
       "Yosh buxoroliklar – islohot; mutaassiblar – yangilikka qarshi; ikkalasi Buxoro kuchlari.")
t.MAPMATCH('buxamir', ['Buxoro', 'Karki', 'Chorjo‘y'],
           ["150 kishilik namoyish Arkka yetib kelgan shahar", "1917-yil 8-aprelda Buxoro bilan birga namoyish bo‘lgan shahar", "1920-yil avgustda Muvaqqat inqilobiy qo‘mita tuzilgan shahar"],
           "1 – Buxoro; 2 – Karki; 3 – Chorjo‘y.")

# 16-mavzu. Xiva xonligining tugatilishi
t = Topic('y10u16', 10016); TOPICS['y10u16'] = t
t.B("Muhammad Rahimxon II dan so‘ng taxtni kim egallagan?", "Asfandiyorxon", "Said Abdulla", "Junaydxon", "Said Olimxon", "Asfandiyorxon (1910–1918).")
t.B("Yosh xivaliklar Asfandiyorxondan nima talab qilgan?", "islohotlar manifestini imzolashni", "taxtdan voz kechishni", "Rossiyaga qo‘shilishni", "Buxoro bilan birlashishni", "Islohotlar manifestini.")
t.B("Islohotlar qanday boshqaruv shaklini ko‘zda tutgan?", "konstitutsiyaviy monarxiya", "respublika", "mutlaq monarxiya", "sovet hokimiyati", "Konstitutsiyaviy monarxiya.")
t.B("1917-yil 4-aprelda xon devonxonasi ro‘parasida nima bo‘lgan?", "bir necha ming kishilik namoyish", "qurultoy", "to‘ntarish", "jang", "Ming kishilik namoyish.")
t.B("Xon qabul qilgan delegatsiyaga kimlar boshchilik qilgan?", "Polvonniyoz Hoji Yusupov va Husaynbek Matmurodov", "Fitrat va Xo‘jayev", "Junaydxon va Said Abdulla", "Bobooxun va Islomxo‘ja", "Polvonniyoz Yusupov va Husaynbek Matmurodov.")
t.B("Xon manifestni qachon imzolagan?", "1917-yil 5-aprelda", "1917-yil 26-aprelda", "1918-yil oktyabrda", "1920-yil 27-aprelda", "1917-yil 5-aprel.")
t.B("Majlisning birinchi sessiyasi qachon bo‘lgan?", "1917-yil 26-aprelda", "1917-yil 5-aprelda", "1920-yil 30-aprelda", "1918-yil yanvarda", "1917-yil 26-aprel.")
t.B("Majlisning birinchi sessiyasida nechta xivalik deputat qatnashgan?", "30 nafar", "7 nafar", "15 nafar", "150 nafar", "30 nafar xivalik va 7 turkman vakili.")
t.B("Asfandiyorxon bosh qo‘mondon etib kimni tayinlagan?", "Junaydxon", "Polvonniyoz Yusupov", "Said Abdulla", "Husaynbek Matmurodov", "Yovmut sardori Junaydxon.")
t.B("Junaydxon qaysi qabila sardori bo‘lgan?", "turkmanlarning yovmut qabilasi", "qoraqalpoqlar", "qozoqlar", "mang‘itlar", "Yovmut qabilasi.")
t.B("Junaydxon Asfandiyorxonga qachon suiqasd uyushtirgan?", "1918-yil oktyabrda", "1917-yil aprelda", "1920-yil fevralda", "1910-yilda", "1918-yil oktyabr, Nurullaboy saroyida.")
t.B("Asfandiyorxondan so‘ng taxtga kim o‘tirgan?", "akasi Said Abdulla", "Junaydxon", "Muhammad Rahimxon III", "Polvonniyoz", "Said Abdulla.")
t.B("Xorazm Xalq Sovet Respublikasi qachon e’lon qilingan?", "1920-yil 27–30-aprelda", "1920-yil 6-oktyabrda", "1917-yil 26-aprelda", "1924-yilda", "1920-yil 27–30-aprel, Butunxorazm qurultoyi.")
t.B("XXSR Xalq Nozirlar Kengashi necha kishidan iborat bo‘lgan?", "15 kishi", "30 kishi", "7 kishi", "50 kishi", "15 kishi.")
t.B("XXSR Xalq Nozirlar Kengashining birinchi raisi kim?", "Polvonniyoz Yusupov", "Fayzulla Xo‘jayev", "Junaydxon", "Husaynbek Matmurodov", "Polvonniyoz Yusupov.")
t.NAT("Majlis tuzilganiga ikki oy o‘tmasdan konservativ kuchlar to‘ntarish qildi.", "Majlis tarqatilib, yosh xivaliklar hibsga olindi, bir qismi otib tashlandi", "Majlis kuchaydi", "xon taxtdan ketdi", "yosh xivaliklar hokimiyatni oldi", "Majlis tarqatildi.")
t.NAT("Asfandiyorxon sovetlar xavfidan qo‘rqib Junaydxonni bosh qo‘mondon qildi.", "Junaydxon saroyda mavqeyini oshirib, 1918-yilda to‘ntarish qildi", "Junaydxon sovetlarga qo‘shildi", "xon hokimiyati mustahkamlandi", "Junaydxon Afg‘onistonga ketdi", "Amalda hokimiyat Junaydxonda.")
t.NAT("1920-yil yanvardan sovetlar Xivaga hujum qilib, bir qator shaharlarni egalladi.", "Said Abdullaxon taxtdan voz kechdi", "Junaydxon g‘alaba qozondi", "xonlik mustahkamlandi", "Rossiya chekindi", "Xonlik tugatildi.")
t.TF("Manifestga muvofiq Xorazm konstitutsiyaviy monarxiya etib belgilangan.", True, "To‘g‘ri.")
t.TF("Butunxorazm qurultoyi XXSRning doimiy Konstitutsiyasini qabul qilgan.", False, "Noto‘g‘ri: muvaqqat Konstitutsiyasini qabul qilgan.")
t.TF4([("Yosh xivaliklar yangi usul maktablari uchun qo‘mita tuzishni talab qilgan.", True), ("Ular temiryo‘l va pochta-telegraf qurilishini talab qilgan.", True),
       ("Majlis Vazirlar kengashini saylagan.", True), ("Asfandiyorxon 1918-yilda Buxoroga qochib ketgan.", False)],
      "4-noto‘g‘ri: Junaydxon unga Nurullaboy saroyida suiqasd uyushtirgan.")
t.MUL([("Asfandiyorxon taxtni imperiya hukumati yordamida egallagan.", True),
       ("Said Abdulla davrida amalda hokimiyat Junaydxon qo‘lida bo‘lgan.", True),
       ("XXSR Toshkentda e’lon qilingan.", False)],
      "III noto‘g‘ri: Xivadagi Butunxorazm qurultoyida e’lon qilingan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Asfandiyorxon taxtga chiqdi", "xon devonxonasi oldida namoyish", "manifest imzolandi", "Majlisning birinchi sessiyasi", "Junaydxon to‘ntarishi", "XXSR e’lon qilindi"],
      "1910 → 1917-04-04 → 05 → 26 → 1918-oktyabr → 1920-aprel.")
t.MATCH("Shaxslarni ma’lumot bilan moslashtiring.", ["Asfandiyorxon", "Junaydxon", "Said Abdulla", "Polvonniyoz Yusupov"],
        ["1917-yilda manifestni imzolagan xon", "yovmut sardori, 1918-yilgi to‘ntarish", "1920-yilda taxtdan voz kechgan xon", "XXSR hukumatining birinchi raisi", "BXSR rahbari"], 'abcd',
        "Asfandiyorxon – manifest; Junaydxon – to‘ntarish; Said Abdulla – voz kechish; Polvonniyoz – XXSR raisi.")
t.VENN("BXSR", "XXSR",
       [("1920-yil 6-oktyabrda e’lon qilingan", 1), ("hukumat rahbari Fayzulla Xo‘jayev", 1),
        ("1920-yil aprelda Butunxorazm qurultoyida e’lon qilingan", 2), ("hukumat rahbari Polvonniyoz Yusupov", 2),
        ("xalq sovet respublikasi, hukumati Xalq Nozirlar Kengashi", 3)],
       "BXSR – oktyabr, Xo‘jayev; XXSR – aprel, Yusupov; ikkalasi XSR.")
t.MAPN('xorazm2', ['Xiva', 'Ko‘hna Urganch', 'Chimboy', 'Mo‘ynoq'], "1920-yil 27–30-aprelda Butunxorazm qurultoyi o‘tib, XXSR e’lon qilingan shahar xaritada qaysi raqamda?",
       "Xiva.")

# 17-mavzu. Turkiston muxtoriyati
t = Topic('y10u17', 10017); TOPICS['y10u17'] = t
t.B("Butunturkiston o‘lka musulmonlarining favqulodda IV qurultoyi qayerda bo‘lgan?", "Qo‘qonda", "Toshkentda", "Samarqandda", "Buxoroda", "Qo‘qonda.")
t.B("Favqulodda IV qurultoy qachon bo‘lgan?", "1917-yil 26–28-noyabrda", "1917-yil 16–23-aprelda", "1918-yil 19–26-yanvarda", "1918-yil 22-fevralda", "1917-yil 26–28-noyabr.")
t.B("Turkiston Muxtoriyati qachon tashkil topgan?", "1917-yil 27-noyabrda", "1917-yil 25-oktyabrda", "1918-yil 31-yanvarda", "1917-yil 15-martda", "1917-yil 27-noyabr.")
t.B("Ta’sis majlisi chaqirilgunga qadar hokimiyat kimlar qo‘lida jamlangan?", "Muvaqqat kengash va Turkiston Milliy majlisi", "Toshkent Soveti", "Muvaqqat hukumat", "amir va xon", "Muvaqqat kengash va Milliy majlis.")
t.B("Bolsheviklar Orenburgni qachon qo‘lga olgan?", "1918-yil 19-yanvarda", "1917-yil 27-noyabrda", "1918-yil 22-fevralda", "1918-yil 31-yanvarda", "1918-yil 19-yanvar.")
t.B("Toshkent bolsheviklari Muxtoriyat hukumatini tarqatish haqida qachon qaror qabul qilgan?", "1918-yil 31-yanvarda", "1918-yil 19-yanvarda", "1917-yil 28-noyabrda", "1918-yil 22-fevralda", "1918-yil 31-yanvar.")
t.B("Toshkent Sovetiga kim rahbarlik qilgan?", "Ivan Tobolin", "Kaufman", "Kolesov", "Perovskiy", "Ivan Tobolin.")
t.B("Fitrat Muxtoriyat e’lon qilingan 27-noyabr tunini qanday atagan?", "«Milliy laylatulqadrimiz»", "«Ozodlik kuni»", "«Bayramimiz»", "«Muqaddas tun»", "«Milliy laylatulqadrimiz».")
t.B("Muxtoriyatni alqab she’rlar bitgan shoirlar kimlar?", "Fitrat, Cho‘lpon, Hamza", "Muqimiy, Furqat", "Berdaq, Ajiniyoz", "Navoiy, Bobur", "Fitrat, Cho‘lpon, Hamza.")
t.B("Turkiston Respublikasi XKS harbiy harakatlarni qachon boshlagan?", "1918-yil 30-yanvarda", "1918-yil 22-fevralda", "1917-yil 27-noyabrda", "1918-yil 19-yanvarda", "1918-yil 30-yanvar.")
t.B("«Tinchlik shartnomasi» qayerda imzolangan?", "Qo‘qondagi Rus–Osiyo banki binosida", "Toshkentda", "Samarqandda", "Moskvada", "Qo‘qon, Rus–Osiyo banki binosi.")
t.B("«Tinchlik shartnomasi» qachon imzolangan?", "1918-yil 22-fevralda", "1918-yil 31-yanvarda", "1918-yil 30-yanvarda", "1917-yil 28-noyabrda", "1918-yil 22-fevral.")
t.NAT("Qurultoy qatnashchilari muxtoriyat va mustaqillik fikrini qo‘llab-quvvatladi.", "27-noyabrda Turkiston Muxtoriyati hukumati tashkil topdi", "qurultoy tarqatildi", "bolsheviklar hokimiyati tan olindi", "Turkiston Rossiyaga qo‘shildi", "Muxtoriyat tuzildi.")
t.NAT("Bolsheviklar Orenburgni olib, Moskva bilan temiryo‘l qatnovini tikladi.", "Toshkentga qurol-yarog‘ yetkazib, Muxtoriyatni tugatishga kirishdi", "bolsheviklar Turkistondan chekindi", "Muxtoriyat kuchaydi", "temiryo‘l buzildi", "Qurol keltirildi.")
t.NAT("Bolsheviklar qizil gvardiyachilar va yollangan qurolli guruhlardan foydalandi.", "Qo‘qonda ko‘plab aholi halok bo‘lib, Muxtoriyat kuch bilan tugatildi", "Muxtoriyat g‘alaba qildi", "Qo‘qon zarar ko‘rmadi", "bolsheviklar mag‘lub bo‘ldi", "Muxtoriyat tugatildi.")
t.NAT("O‘lkada Turkiston Muxtoriyati va bolsheviklar hokimiyati bir vaqtda mavjud bo‘ldi.", "ikki hokimiyatchilik yuzaga keldi", "uch hokimiyatchilik yuzaga keldi", "yagona hokimiyat o‘rnatildi", "anarxiya tugadi", "Ikki hokimiyatchilik.")
t.TF("Turkiston Muxtoriyati o‘lkadagi ilk demokratik va xalqchil hukumat bo‘lgan.", True, "To‘g‘ri.")
t.TF("Turkiston Muxtoriyati qurolli to‘qnashuvsiz, tinch yo‘l bilan tugatilgan.", False, "Noto‘g‘ri: harbiy kuch ishlatish yo‘li bilan tugatilgan.")
t.TF4([("Muxtoriyat hukumati xalq o‘rtasida katta e’tibor qozongan.", True), ("Namoyishchilar bayroqlarida «Yashasin Muxtoriyatli Turkiston» yozilgan.", True),
       ("«Tinchlik shartnomasi»ga ko‘ra aholi sovet hokimiyatini tan oladi deb yozilgan.", True), ("Bolsheviklar Muxtoriyatga dastlabdanoq katta harbiy kuch bilan qarshi chiqa olgan.", False)],
      "4-noto‘g‘ri: dastlab yetarli harbiy kuchga ega bo‘lmagan.")
t.MUL([("Bolsheviklar Rossiya hukmronligini yangicha sharoitda saqlab qolishga intilgan.", True),
       ("Muxtoriyat millatlarning o‘z taqdirini o‘zi belgilash huquqini yoqlagan.", True),
       ("Muxtoriyat faoliyati bir necha yil davom etgan.", False)],
      "III noto‘g‘ri: faoliyati uzoqqa cho‘zilmagan – 1917-yil noyabrdan 1918-yil fevralgacha.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["favqulodda IV qurultoy boshlandi", "Turkiston Muxtoriyati tashkil topdi", "bolsheviklar Orenburgni oldi", "harbiy harakatlar boshlandi", "Muxtoriyatni tarqatish qarori", "«Tinchlik shartnomasi» imzolandi"],
      "1917-11-26 → 27 → 1918-01-19 → 30 → 31 → 02-22.")
t.MATCH("Shaxs/organni ma’lumot bilan moslashtiring.", ["Fitrat", "Ivan Tobolin", "Muvaqqat kengash", "XKS"],
        ["27-noyabrni «Milliy laylatulqadrimiz» deb atagan", "Toshkent Soveti rahbari", "Ta’sis majlisigacha hokimiyat organi", "1918-yil 30-yanvarda harbiy harakat boshlagan", "Buxoro amiri"], 'abcd',
        "Fitrat – laylatulqadr; Tobolin – Toshkent Soveti; Muvaqqat kengash – hokimiyat; XKS – harbiy harakat.")
t.VENN("Turkiston Muxtoriyati", "Toshkentdagi bolsheviklar",
       [("Qo‘qonda tashkil topgan", 1), ("milliy davlat mustaqilligini tiklashga intilgan", 1),
        ("Ivan Tobolin boshchiligidagi Sovet", 2), ("Rossiya hukmronligini saqlashga intilgan", 2),
        ("1917–1918-yillarda Turkistonda hokimiyat da’vosi qilgan", 3)],
       "Muxtoriyat – Qo‘qon, mustaqillik; bolsheviklar – Tobolin, imperiya; ikkalasi hokimiyat da’vogari.")
t.MAPN('uzb', ['Qo‘qon', 'Toshkent', 'Samarqand', 'Buxoro'], "1917-yil noyabrda Turkiston Muxtoriyati e’lon qilingan shahar xaritada qaysi raqamda?",
       "Qo‘qon.")
