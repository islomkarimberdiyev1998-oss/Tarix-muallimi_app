from qlib import Topic
TOPICS = {}
BA = 'buxamir'; XR = 'xorazm'

# 34 Yosh buxoroliklar faoliyati va Buxoro amirligining tugatilishi
t = Topic('e9u34', 9034); TOPICS['e9u34'] = t
t.B("Yosh buxoroliklar siyosiy harakat sifatida qachondan faoliyat ko‘rsatgan?", "1910-yildan", "1893-yildan", "1917-yildan", "1920-yildan", "1910-yildan.")
t.B("Yosh buxoroliklar qanday tuzum o‘rnatishga harakat qilgan?", "respublika tuzumi", "mutlaq monarxiya", "xonlik", "protektorat", "Buxoroni mustabid amirdan qutqarib, respublika tuzumini o‘rnatishga.")
t.B("Yosh buxoroliklar qaysi gazetalarni nashr qilgan?", "«Buxoroi sharif» va «Turon»", "«Tarjimon» va «Shuhrat»", "«Tong» va «Uchqun»", "«Oyina» va «Sadoi Turkiston»", "«Buxoroi sharif» va «Turon».")
t.B("Amir Abdulahaddan so‘ng taxtni kim egallagan?", "Sayid Olimxon", "Amir Muzaffar", "Abdumalik to‘ra", "Amir Nasrullo", "Uning o‘g‘li Sayid Olimxon (1910–1920).")
t.B("Sayid Olimxon qachon Peterburgga o‘qishga jo‘natilgan?", "1893-yilda", "1910-yilda", "1885-yilda", "1917-yilda", "1893-yilda; 3 yil harbiy ish va davlat boshqaruvini o‘rgandi.")
t.B("1917-yil bahorida amir farmonini kim o‘qib eshittirgan?", "bosh qozi", "qo‘shbegi", "Fayzulla Xo‘jayev", "Fitrat", "Bosh qozi amir qabulxonasida.")
t.B("Farmonni amalga oshirish uchun tuzilgan qo‘mita qanday atalgan?", "Yosh buxoroliklar qo‘mitasi", "Musulmon markaziy sho‘rosi", "Muvaqqat inqilobiy qo‘mita", "Xalq Nozirlar Kengashi", "Yosh buxoroliklar qo‘mitasi.")
t.B("Radikal harakat tarafdorlari kimlar bo‘lgan?", "Fayzulla Xo‘jayev, Abdurauf Fitrat, Usmon Xo‘ja", "Behbudiy, Mullaxon o‘g‘li, Mirzo G‘ulom", "Munavvarqori, Avloniy", "Sayid Olimxon, bosh qozi", "Fayzulla Xo‘jayev, Fitrat, Usmon Xo‘ja.")
t.B("Jadidlar qachon Karki va Buxoroda namoyish o‘tkazgan?", "1917-yil 8-aprelda", "1920-yil 29-avgustda", "1917-yil mart boshida", "1910-yilda", "1917-yil 8-aprelda.")
t.B("Buxorodagi namoyishga necha kishi to‘plangan?", "150 kishi", "7 ming kishi", "500 kishi", "25 ming kishi", "150 kishi; rahbarlari Fayzulla Xo‘jayev va Fitrat.")
t.B("Ark ostonasini islohotlarga qarshi chiqqan nechta mulla egallagan?", "7 mingdan ziyod", "150", "500", "30", "7 mingdan ziyod uyushgan mullalar.")
t.B("1920-yil yanvarda Toshkentda qanday tashkilot tuzilgan?", "«Inqilobchi yosh buxoroliklarning Turkistondagi markaziy byurosi»", "«Musulmon markaziy sho‘rosi»", "«Tarbiyai atfol»", "«Sho‘roi Islomiya»", "Fayzulla Xo‘jayev rahbarligida markaziy byuro.")
t.B("Tashviqot uchun qaysi nashrlar chiqarilgan?", "«Tong» jurnali va «Uchqun» gazetasi", "«Buxoroi sharif» va «Turon»", "«Tarjimon»", "«Shuhrat»", "«Tong» jurnali va «Uchqun» gazetasi.")
t.B("1920-yil 29-avgustda qayerda qo‘zg‘olon uyushtirilgan?", "Chorjo‘yda", "Buxoroda", "Karkida", "Kogonda", "Chorjo‘yda.")
t.B("Bolsheviklar armiyasi Buxoroga qachon kirgan?", "1920-yil 2-sentabrda", "1920-yil 29-avgustda", "1920-yil 6-oktabrda", "1917-yil 8-aprelda", "1920-yil 2-sentabrda.")
t.B("Buxoro Xalq Sovet Respublikasi qachon e’lon qilingan?", "1920-yil 6-oktabrda", "1920-yil 2-sentabrda", "1917-yil aprelda", "1924-yilda", "1920-yil 6-oktabrda.")
t.B("Amir Sayid Olimxon qaysi tomonga qochib o‘tgan?", "Afg‘oniston", "Eron", "Hindiston", "Rossiya", "Afg‘oniston tomonga.")
t.NAT("1917-yilgi Rossiyadagi fevral voqealari Buxoro siyosiy hayotini jonlantirdi.", "amir ayrim islohotlar o‘tkazish haqida farmon berishga majbur bo‘ldi", "amir taxtdan voz kechdi", "jadidlar hukumat tuzdi", "Buxoro Rossiyaga qo‘shildi", "Amir islohot va’da qilgan farmon chiqardi.")
t.NAT("Mullalar namoyishchilarga toshlar yog‘dirib, sarbozlar ularni hibsga oldi.", "Sayid Olimxonning xalq orasida hurmati qolmadi, jadidlar boshqa shaharlarga qochdi", "islohotlar amalga oshdi", "amir jadidlarni mukofotladi", "Buxoro respublika bo‘ldi", "30 dan ziyod namoyishchi hibsga olindi, jadidlar qochdi.")
t.TF("Farmonda amaldorlarning qo‘shimcha ustama haq olishi taqiqlanib, qat’iy maosh ta’sis etilgan.", True, "To‘g‘ri.")
t.TF("Behbudiy radikal harakat tarafdori bo‘lib, zudlik bilan namoyish o‘tkazishga chaqirgan.", False, "Noto‘g‘ri: Behbudiy vazmin, bosiq harakatlar bilan farmonni qo‘llab-quvvatlagan.")
t.MUL([("Namoyishda «Hurriyat, Adolat, Musavvat!» shiorlari bo‘lgan.", True),
       ("Chorjo‘yda Muvaqqat inqilobiy qo‘mita tuzilib, Rossiyadan yordam so‘ragan.", True),
       ("Amir qo‘shinlari bolsheviklarga kuchli qarshilik ko‘rsatgan.", False)],
      "III noto‘g‘ri: amir qo‘shinlari deyarli qarshilik ko‘rsata olmagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Sayid Olimxon taxtga o‘tirdi", "Buxoro va Karkida jadidlar namoyishi", "Toshkentda markaziy byuro tuzildi", "Chorjo‘yda qo‘zg‘olon", "BXSR e’lon qilindi"],
      "1910 → 1917-yil 8-aprel → 1920-yil yanvar → 29-avgust → 6-oktabr.")
t.MAPMATCH(BA, ['Buxoro', 'Karki', 'Chorjo‘y'],
           ["150 kishilik namoyish Ark oldida to‘xtatilgan shahar", "1917-yil 8-aprelda Buxoro bilan birga namoyish bo‘lgan shahar", "1920-yil 29-avgustda qo‘zg‘olon uyushtirilgan shahar"],
           "1 – Buxoro; 2 – Karki; 3 – Chorjo‘y.")
t.VENN("Vazmin jadidlar", "Radikal jadidlar",
       [("Behbudiy, Mullaxon o‘g‘li, Mirzo G‘ulom", 1), ("farmonni bosiq harakatlar bilan qo‘llagan", 1),
        ("Fayzulla Xo‘jayev, Fitrat, Usmon Xo‘ja", 2), ("zudlik bilan namoyish o‘tkazishga da’vat etgan", 2),
        ("Yosh buxoroliklar qo‘mitasi a’zolari", 3)],
       "Vazminlar — Behbudiy va boshqalar; radikallar — Xo‘jayev, Fitrat, namoyish.")

# 35-36 Xiva xonligining davlat tuzumi va ijtimoiy-iqtisodiy ahvoli
t = Topic('e9u35-36', 9035); TOPICS['e9u35-36'] = t
t.B("Xiva xoni ustidan nazorat uchun tuzilgan Kengash (devon) necha kishidan iborat bo‘lgan?", "7 kishi", "4 kishi", "18 kishi", "12 kishi", "7 kishi, ulardan 4 nafari podsho vakillari.")
t.B("Xiva xonligini qaysi urug‘ vakillari boshqargan?", "qo‘ng‘irotlar", "mang‘itlar", "minglar", "qipchoqlar", "Qo‘ng‘irot urug‘i sulolasi.")
t.B("Xonning muntazam qo‘shini necha kishidan iborat bo‘lgan?", "1,5 ming kishi", "15 ming kishi", "500 kishi", "40 ming kishi", "Yasovulboshi boshqargan 1,5 ming kishi.")
t.B("Xonning bosh vaziri qanday atalgan?", "mehtar", "qo‘shbegi", "devonbegi", "yasovulboshi", "Mehtar — bosh vazir.")
t.B("Xivada nechta masjid bo‘lgan?", "160 dan ortiq", "60", "1,5 ming", "64", "160 dan ortiq masjid, 60 dan ziyod avliyo daxmasi.")
t.B("Xonlikda nechtaga yaqin maktab faoliyat yuritgan?", "1,5 mingga yaqin", "160", "64", "81", "1,5 mingga yaqin maktab.")
t.B("Madrasada necha yilgacha ta’lim olingan?", "10 yilgacha", "3 yilgacha", "1 yil", "20 yil", "10 yilgacha.")
t.B("Xonlikda qishloq xo‘jaligining asosiy tarmog‘i nima edi?", "g‘alla yetishtirish", "pillachilik", "uzumchilik", "chorvachilik", "G‘alla — sholi, jo‘xori, suli.")
t.B("Sug‘oriladigan yerlarning qancha qismi masjidlar mulki bo‘lgan?", "40% i", "5% i", "90% i", "25% i", "40% i.")
t.B("Xiva xonligida soliqlarning qariyb nechta turi bo‘lgan?", "25 turi", "5 turi", "100 turi", "12 turi", "Qariyb 25 turi.")
t.B("O‘tloqlardan foydalanganlik uchun soliq qanday atalgan?", "cho‘p puli", "afanak puli", "solg‘ut", "tanobona", "Cho‘p puli.")
t.B("Xon farmonlarini e’lon qiluvchi jarchi o‘z foydasiga qanday pul yig‘gan?", "afanak puli", "cho‘p puli", "qozon puli", "tarozi puli", "Afanak puli.")
t.B("Dehqonlar aholining 90% ini tashkil etsa-da, sug‘oriladigan yerlarning qancha qismiga egalik qilgan?", "atigi 5% iga", "40% iga", "50% iga", "90% iga", "Atigi 5% iga.")
t.B("1909-yilga kelib Xiva xonligida nechta sanoat korxonasi ishlagan?", "81 ta", "40 ta", "175 ta", "11 ta", "81 ta.")
t.B("Yangi Urganchda nechta paxta tozalash zavodi bo‘lgan?", "o‘n bitta", "ikkita", "to‘qqizta", "yigirmata", "O‘n bitta (oltitasi mahalliy tadbirkorlarniki).")
t.B("1909-yilda Rossiya-Osiyo banki va Madiyorov-Baqqolov kapitalini birlashtirgan sindikat qaysi?", "«A-Meta»", "«Tarjimon»", "«Turon»", "«Buxoroi sharif»", "«A-Meta» sindikati.")
t.B("Amudaryo flotiliyasi qachon ta’sis etilgan?", "1887-yil oxirlarida", "1885-yilda", "1873-yilda", "1909-yilda", "1887-yil oxirlarida; Kaspiyorti temiryo‘li — 1885-yilda.")
t.NAT("1873-yildan so‘ng hosildor yerlarning katta qismi Rossiya tasarrufiga o‘tdi.", "xonlik yangi soliqlar joriy etdi yoki mavjudlarini oshirdi", "soliqlar bekor qilindi", "xonlik boyidi", "dehqonlarga yer berildi", "Xarajatlar yangi soliqlar hisobidan qoplandi.")
t.NAT("Rossiyadan arzon sanoat tovarlari kirib kelishi ko‘paydi.", "mahalliy matolar, kulolchilik, mis buyumlar ishlab chiqarilishi keskin kamaydi", "hunarmandchilik rivojlandi", "mahalliy mahsulotlarga talab oshdi", "xonlik eksportchiga aylandi", "Mahalliy korxonalar buyumlariga talab pasaydi.")
t.TF("1873-yildan Xiva qo‘shini faqat ichki tartibni saqlash vazifasini bajargan.", True, "To‘g‘ri.")
t.TF("Xon va uning amaldorlari, qarindoshlari barcha soliqlarni to‘lagan.", False, "Noto‘g‘ri: ular soliqlardan ozod etilgan.")
t.MUL([("Kasanachilikdagi sex birlashmalariga usta, xalfa va shogird kirgan.", True),
       ("Gilam va kigizlar Porsu, Alieli, Ko‘hna Urganch, G‘azovotda ishlab chiqarilgan.", True),
       ("Xalfa avansni to‘lamasdan ham ustaxonadan bemalol ketishi mumkin edi.", False)],
      "III noto‘g‘ri: xalfa avansni to‘lamaguncha ustaxonadan keta olmagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Gandimiyon shartnomasi", "Kaspiyorti temiryo‘li qurildi", "Amudaryo flotiliyasi ta’sis etildi", "«A-Meta» sindikati tashkil qilindi"],
      "1873 → 1885 → 1887 → 1909.")
t.MAPMATCH(XR, ['Yangi Urganch', 'Mo‘ynoq', 'Qo‘ng‘irot'],
           ["11 ta paxta tozalash zavodi, bank bo‘limlari bo‘lgan shahar", "XX asr boshida vujudga kelgan yangi shahar", "Hazorasp, Xo‘jayli qatori xonlikning eng yirik bekliklaridan biri"],
           "1 – Yangi Urganch; 2 – Mo‘ynoq; 3 – Qo‘ng‘irot.")
t.VENN("Xiva xonligidagi masjid va madrasalar", "Xiva xonligidagi dehqonlar",
       [("sug‘oriladigan yerlarning 40% iga egalik", 1), ("64 tasi 205 ming tanobdan ziyod yerga ega", 1),
        ("aholining 90% ga yaqini", 2), ("yerlarning atigi 5% iga egalik", 2),
        ("Xiva xonligi ijtimoiy hayotining qismi", 3)],
       "Diniy muassasalar — 40% yer; dehqonlar — 90% aholi, 5% yer.")
