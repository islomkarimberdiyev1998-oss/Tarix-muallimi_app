from qlib import Topic, PLACES, REG
TOPICS = {}

# 3-mavzu. Buxoro va Xivaning vassalga aylanishi
t = Topic('y10u3', 10003); TOPICS['y10u3'] = t
t.B("Mustamlakachilar xonliklarning birlashishiga yo‘l qo‘ymaslik uchun qaysi tamoyilga asoslangan?", "«Bo‘lib tashla va hukmronlik qil»", "«Kuch – adolatda»", "«Bir bo‘lsak – yagona xalqmiz»", "«Tinchlik va do‘stlik»", "«Bo‘lib tashla va hukmronlik qil».")
t.B("1866-yil 8-mayda Rossiya va Buxoro qo‘shinlari qayerda to‘qnashgan?", "Yerjar qishlog‘i yaqinida", "Zirabuloqda", "Jizzaxda", "Cho‘ponotada", "Yerjar qishlog‘i yaqinida.")
t.B("Xo‘jand qal’asi qamali necha kun davom etgan?", "ikki kun", "yigirma kun", "bir oy", "bir hafta", "Ikki kun.")
t.B("Krijanovskiy Buxoro amiridan necha kun ichida 100 ming rubl tovon talab qilgan?", "10 kun", "20 kun", "30 kun", "5 kun", "10 kun.")
t.B("Jizzax uchun jangda ikki tomondan qancha kishi halok bo‘lgan?", "6 mingdan ko‘proq", "600", "60 ming", "1 ming", "6 mingdan ko‘proq.")
t.B("1868-yilda Kaufman necha kishilik otryad bilan Samarqandga bostirib kirgan?", "4 mingdan ziyod", "40 ming", "400", "12 ming", "4 mingdan ziyod.")
t.B("Samarqandda kurashgan Kitob begi kim edi?", "Jo‘rabek", "Bobobek", "Aliquli", "Po‘latxon", "Jo‘rabek.")
t.B("Samarqandda kurashgan Shahrisabz begi kim edi?", "Bobobek", "Jo‘rabek", "Solihbek", "Nasriddinbek", "Bobobek.")
t.B("Yangi bosib olingan Samarqand va Kattaqo‘rg‘ondan qanday okrug tuzilgan?", "Zarafshon okrugi", "Sirdaryo okrugi", "Amudaryo okrugi", "Farg‘ona okrugi", "Zarafshon okrugi.")
t.B("Istilochilik yurishlarining ikkinchi bosqichini yakunlagan shartnoma qanday nom bilan kirgan?", "Zirabuloq shartnomasi", "Gandimiyon shartnomasi", "Toshkent sulhi", "Tehron shartnomasi", "«Zirabuloq shartnomasi».")
t.B("Buxoro amirligidagi Rossiyaning birinchi vakili kim bo‘lgan?", "P. Lessar", "Kaufman", "Krijanovskiy", "Skobelev", "P. Lessar.")
t.B("Buxoro–Eron chegarasi qachon maxfiy shartnomada belgilangan?", "1881-yil 10-dekabrda", "1873-yilda", "1868-yilda", "1887-yilda", "1881-yil 10-dekabrda.")
t.B("Xivaga yurish qilgan qo‘shinlar nechta harbiy okrugdan yo‘lga chiqqan?", "to‘rtta", "ikkita", "oltita", "bitta", "Mang‘ishloq, Orenburg, Turkiston, Krasnovodsk.")
t.B("Kaufman qo‘shinlari Xivani qaysi darvoza orqali egallagan?", "Hazorasp darvozasi", "Polvon darvoza", "Ota darvoza", "Kamolon darvozasi", "Hazorasp darvozasi.")
t.B("Gandimiyon shartnomasi qachon imzolangan?", "1873-yil 12-avgustda", "1875-yil 22-sentyabrda", "1868-yil 2-iyunda", "1866-yil 8-mayda", "1873-yil 12-avgust.")
t.B("Gandimiyon shartnomasini qaysi Xiva xoni imzolagan?", "Muhammad Rahimxon II", "Muhammad Aminxon", "Olloqulixon", "Asfandiyorxon", "Muhammad Rahimxon II.")
t.B("Gandimiyon shartnomasiga ko‘ra Xiva qancha tovon to‘lashi kerak edi?", "2 million 200 ming rubl", "100 ming rubl", "2 million rubl", "500 ming rubl", "2 mln 200 ming rubl, 20 yil davomida.")
t.B("1875-yilda Xudoyorxon o‘rniga taxtga kim o‘tirgan?", "Nasriddinbek", "Po‘latxon", "Muhammad Alixon", "Sheralixon", "Nasriddinbek.")
t.B("«Po‘latxon» nomi bilan qo‘zg‘olonga rahbarlik qilgan kim?", "Mulla Is’hoq Mullo Hasan o‘g‘li", "Nasriddinbek", "Abdurahmon oftobachi", "Dukchi eshon", "Mulla Is’hoq.")
t.B("Qo‘qon xonligi o‘rnida qaysi viloyat tashkil qilingan?", "Farg‘ona viloyati", "Sirdaryo viloyati", "Samarqand viloyati", "Yettisuv viloyati", "Farg‘ona viloyati, 1876-yil.")
t.NAT("Krijanovskiy Buxoro amiri talablarni bajarmadi deb bahona qildi.", "qo‘shinlar O‘ratepa va Jizzaxni egalladi", "sulh tuzildi", "amir Rossiyaga ketdi", "qo‘shinlar Toshkentga qaytdi", "Hujum boshlandi.")
t.NAT("Zirabuloq jangida amir Muzaffar mag‘lub bo‘ldi.", "u Kaufmanning yangi chegaralar haqidagi taklifini qabul qilishga majbur bo‘ldi", "amir Samarqandni qaytarib oldi", "Buxoro mustaqil qoldi", "Kaufman chekindi", "Buxoro protektoratga aylandi.")
t.NAT("Xiva xazinasida tovon uchun yetarli pul yo‘q edi.", "tovon aholidan yig‘ib olinadigan bo‘ldi", "tovon bekor qilindi", "Rossiya kreditga berdi", "Buxoro to‘lab berdi", "Aholi zimmasiga tushdi.")
t.NAT("Nasriddinbek imzolagan shartnomadan aholi norozi bo‘ldi.", "Po‘latxon boshchiligida qo‘zg‘olon ko‘tarildi", "aholi shartnomani qo‘llab-quvvatladi", "Xudoyorxon qaytdi", "Skobelev ketdi", "Qo‘zg‘olon boshlandi.")
t.TF("Xudoyorxon Makkadan qaytayotganda Afg‘onistonda vafot etgan.", True, "To‘g‘ri.")
t.TF("Qo‘qon xonligi taslim bo‘lgan shartnomaga ko‘ra Namangan va Chust xonlikda qolgan.", False, "Noto‘g‘ri: Rossiya ixtiyoriga o‘tgan; Namangan bo‘limiga Skobelev boshliq bo‘lgan.")
t.TF4([("Gandimiyon shartnomasiga ko‘ra Amudaryoning o‘ng sohili xonlik tasarrufidan chiqdi.", True), ("Kaufman Xiva xazinasini musodara qilib Sankt-Peterburgga jo‘natgan.", True),
       ("O‘rta Osiyo bosib olinishining to‘rtinchi bosqichida turkmanlar bo‘ysundirilgan.", True), ("1868-yil 2-iyunda Samarqand himoyachilari qal’ani to‘liq egallab qolishgan.", False)],
      "4-noto‘g‘ri: garnizonga yordam kelgach, himoyachilar tog‘ tomonga chekingan.")
t.MUL([("1869–1870-yillarda Rossiya Angliya bilan chegaralar haqida muzokara olib borgan.", True),
       ("1885–1887-yillardagi komissiya Buxoro–Afg‘on chegarasini belgilagan.", True),
       ("Uchinchi bosqich 1847–1865-yillarni o‘z ichiga oladi.", False)],
      "III noto‘g‘ri: 1847–1865 – birinchi bosqich; uchinchi bosqich 1873–1879.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Yerjar jangi", "Samarqandga bostirib kirildi", "Gandimiyon shartnomasi", "Qo‘qon xonligi taslim shartnomasi", "Qo‘qon xonligi tugatildi", "Buxoro–Eron chegarasi belgilandi"],
      "1866 → 1868 → 1873 → 1875 → 1876 → 1881.")
t.MATCH("Bosqichlarni voqealar bilan moslashtiring.", ["1847–1865", "1865–1868", "1873–1879", "1880–1885"],
        ["Toshkent va Qo‘qonning shimoli-g‘arbi istilosi", "Buxoro va Qo‘qonga qarshi yurishlar", "Xiva yerlari qismi va Qo‘qon to‘liq bosib olindi", "turkmanlar bo‘ysundirildi", "Buxoro amirligi tugatildi"], 'abcd',
        "I – Toshkent; II – Buxoro, Qo‘qon; III – Xiva, Qo‘qon; IV – turkmanlar.")
t.VENN("Gandimiyon shartnomasi", "Qo‘qon taslim shartnomasi (1875)",
       [("Muhammad Rahimxon II imzolagan", 1), ("2 mln 200 ming rubl, 20 yilda", 1),
        ("Nasriddinbek imzolagan", 2), ("Namangan va Chust Rossiyaga o‘tdi", 2),
        ("tovon to‘lash majburiyati", 3)],
       "Gandimiyon – Xiva, 2,2 mln; Qo‘qon – Nasriddinbek, Namangan; ikkalasida tovon.")
t.MAPMATCH('uzb', ['Erjar', 'Zirabuloq', 'Xiva', 'Namangan'],
           ["1866-yil 8-mayda amir qo‘shini mag‘lub bo‘lgan joy", "ikkinchi bosqichni yakunlagan jang va shartnoma joyi", "1873-yilda Kaufman egallagan poytaxt", "Skobelev boshliq bo‘lgan bo‘lim markazi"],
           "1 – Yerjar; 2 – Zirabuloq; 3 – Xiva; 4 – Namangan.")

# 4-mavzu. Turkiston o‘lkasida boshqaruv tizimi
t = Topic('y10u4', 10004); TOPICS['y10u4'] = t
t.B("Turkistondagi boshqaruv tizimi qanday nom bilan atalgan?", "«harbiy-xalq boshqaruvi»", "«fuqarolik boshqaruvi»", "«o‘zini o‘zi boshqarish»", "«protektorat»", "«Harbiy-xalq boshqaruvi».")
t.B("General-gubernatorlikning katta vakolatli asosiy ijrochi organi nima edi?", "general-gubernatorlik devoni", "Duma", "volost", "Kengash", "Devon.")
t.B("Viloyatlarni kimlar boshqargan?", "harbiy gubernatorlar", "xonlar", "qozilar", "mingboshilar", "Harbiy gubernatorlar.")
t.B("Uchastkalarni kimlar boshqargan?", "uchastka pristavlari", "oqsoqollar", "biylar", "gubernatorlar", "Uchastka pristavlari.")
t.B("Volost boshlig‘i qanday atalgan?", "mingboshi", "oqsoqol", "ellikboshi", "pristav", "Mingboshi.")
t.B("Ko‘chmanchi aholida xalq sudyalari kimlar bo‘lgan?", "biylar", "qozilar", "miroblar", "pristavlar", "Biylar; o‘troqlarda – qozilar.")
t.B("Toshkentda «Shahar nizomi» qachon joriy etilgan?", "1877-yilda", "1886-yilda", "1867-yilda", "1865-yilda", "1877-yilda.")
t.B("Shahar nizomiga ko‘ra boshqaruv qaysi organga o‘tgan?", "Dumaga", "Kengashga", "volostga", "qozixonaga", "Dumaga.")
t.B("Toshkent Dumasiga 80 minglik mahalliy aholidan nechta deputat saylangan?", "21 ta", "48 ta", "80 ta", "12 ta", "21 nafar.")
t.B("3900 kishilik Yangi shahar aholisidan nechta deputat bo‘lgan?", "48 ta", "21 ta", "39 ta", "100 ta", "48 nafar.")
t.B("«Turkiston o‘lkasini boshqarish haqidagi Nizom»ni qachon kim tasdiqlagan?", "1886-yilda Aleksandr III", "1867-yilda Aleksandr II", "1877-yilda Kaufman", "1865-yilda Chernyayev", "1886-yil, Aleksandr III.")
t.B("1886-yilgi Nizomga ko‘ra Zarafshon okrugi nimaga aylantirildi?", "Samarqand viloyatiga", "Farg‘ona viloyatiga", "Sirdaryo viloyatiga", "Buxoro amirligiga", "Samarqand viloyatiga.")
t.B("Qurama uyezdining nomi nimaga o‘zgartirildi?", "Toshkent uyezdi", "Chimkent uyezdi", "Xo‘jand uyezdi", "Jizzax uyezdi", "Toshkent uyezdi.")
t.B("Buxoroda Rossiya imperatorining siyosiy agentligi qachondan faoliyat yuritgan?", "1885-yildan", "1868-yildan", "1873-yildan", "1920-yildan", "1885-yildan.")
t.B("Ko‘chib kelganlar necha yil soliqlardan to‘liq ozod etilgan?", "5 yil", "10 yil", "2 yil", "20 yil", "5 yil, keyingi 5 yil yarmini to‘lagan.")
t.B("1886-yilgi Nizom bilan qanday yangi boshqaruv idorasi qo‘shilgan?", "General-gubernator Kengashi", "Duma", "Sud palatasi", "Volost kengashi", "Turkiston general-gubernatori Kengashi.")
t.NAT("Imperiyaning markaziy hududlaridan aholi O‘rta Osiyoga ko‘chirib keltirildi.", "mustamlakachilik siyosati uchun qo‘shimcha tayanch kuchlar paydo bo‘ldi va ruslashtirish kuchaydi", "mahalliy aholi yer oldi", "ko‘chib kelganlar soliqni ko‘p to‘ladi", "mustamlaka boshqaruvi zaiflashdi", "Tayanch kuch va ruslashtirish.")
t.NAT("Vaqf mulklarini nazorat qilish mustamlakachi hukumat qo‘liga o‘tdi.", "masjid va maktablarning moddiy ahvoli yomonlashdi", "maktablar boyidi", "vaqflar ko‘paydi", "madrasalar soliqdan ozod bo‘ldi", "Moddiy ahvol yomonlashdi.")
t.NAT("1885-yildan Buxoroda Rossiya siyosiy agentligi ish boshladi.", "amir uning ruxsatisiz tashqi va ichki siyosatda mustaqil ish olib bora olmadi", "amir to‘liq mustaqil bo‘ldi", "Buxoro tugatildi", "agentlik amirga bo‘ysundi", "Amir mustaqilligi cheklandi.")
t.NAT("Toshkent Dumasi a’zolarining 2/3 qismi Yangi shahardan saylandi.", "aholisi ozchilik bo‘lgan ruslar shahar boshqaruvida ustunlikka ega bo‘ldi", "mahalliy aholi ko‘pchilik o‘rin oldi", "Duma tarqatildi", "Eski shahar mustaqil bo‘ldi", "Ruslar ustunligi.")
t.TF("Bo‘lim boshliqlari bir vaqtning o‘zida harbiy komendant ham hisoblangan.", True, "To‘g‘ri.")
t.TF("Yangi vaqf hujjatlari general-gubernator roziligisiz tasdiqlangan.", False, "Noto‘g‘ri: faqat general-gubernator roziligi bilan tasdiqlangan.")
t.TF4([("Viloyatlar uyezdlarga bo‘lingan.", True), ("Duma rahbarini harbiy vazir tasdiqlagan.", True),
       ("Ko‘chib kelganlar uchun maktab va cherkovlar qurishga mablag‘ ajratilgan.", True), ("Quyi boshqaruvda mahalliy aholi vakillari ishlamagan.", False)],
      "4-noto‘g‘ri: mingboshi, oqsoqol, qozi, mirob kabi lavozimlarda mahalliy aholi ishlagan.")
t.MUL([("Xo‘jand, Jizzax, Kattaqo‘rg‘on, Samarqand uyezdlari Samarqand viloyatiga kiritilgan.", True),
       ("Rossiyadan ko‘chib kelganlar asosan qishloq aholisi bo‘lgan.", True),
       ("Shahar xo‘jaligiga oid ishlar qozixonada hal qilingan.", False)],
      "III noto‘g‘ri: shahar xo‘jaligi ishlari Duma qo‘lida bo‘lgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Turkiston general-gubernatorligi tuzildi", "Toshkentda Shahar nizomi joriy etildi", "Buxoroda siyosiy agentlik tashkil etildi", "Aleksandr III yangi Nizomni tasdiqladi"],
      "1867 → 1877 → 1885 → 1886.")
t.MATCH("Boshqaruv bo‘g‘inlarini rahbari bilan moslashtiring.", ["viloyat", "uyezd", "uchastka", "volost"],
        ["harbiy gubernator", "harbiy zobit (uyezd boshlig‘i)", "uchastka pristavi", "mingboshi", "qozikalon"], 'abcd',
        "Viloyat – harbiy gubernator; uyezd – zobit; uchastka – pristav; volost – mingboshi.")
t.VENN("Eski shahar (Toshkent)", "Yangi shahar (Toshkent)",
       [("80 ming mahalliy aholi", 1), ("Dumada 21 deputat", 1),
        ("3900 kishilik asosan rus aholisi", 2), ("Dumada 48 deputat", 2),
        ("Toshkent shahar Dumasida vakillikka ega", 3)],
       "Eski – 80 ming, 21; Yangi – 3900, 48; ikkalasi Dumada.")
t.MAPMATCH('uzb', ['Toshkent', 'Samarqand', 'Buxoro', 'Xo‘jand'],
           ["1877-yilda Shahar nizomi va Duma joriy etilgan shahar", "Zarafshon okrugi o‘rnida tuzilgan viloyat markazi", "1885-yildan imperator siyosiy agentligi ishlagan shahar", "Samarqand viloyatiga kiritilgan uyezd markazi (Sirdaryo bo‘yida)"],
           "1 – Toshkent; 2 – Samarqand; 3 – Buxoro; 4 – Xo‘jand.")
