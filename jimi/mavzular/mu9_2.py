from qlib import Topic
TOPICS = {}
CA = 'ca'; FV = 'fargona'

# 3 Xonliklarning ijtimoiy-iqtisodiy hayoti
t = Topic('e9u3', 9003); TOPICS['e9u3'] = t
t.B("XIX asrda O‘rta Osiyo xonliklari qanday davlatlar edi?", "agrar davlatlar", "sanoat davlatlari", "ko‘chmanchi davlatlar", "dengiz savdosi davlatlari", "Xonliklar agrar davlatlar edi.")
t.B("Ijaraga yer olgan dehqonlar odatda hosilning qancha qismini xiroj sifatida to‘lagan?", "1/5 yoki 1/3 qismini", "1/10 qismini", "to‘liq hosilni", "3/4 qismini", "Ko‘p hollarda hosilning 1/5 yoki 1/3 qismini.")
t.B("Xiva xonligida ijaraga yer olgan dehqonlar qanday atalgan?", "yarimchi", "mardikor", "chorakor", "mirob", "Hosilning yarmini to‘lagani uchun yarimchi deyilgan.")
t.B("Davlat yerlari qanday atalgan?", "amlok", "mulk", "vaqf", "tanho", "Amlok — davlat yerlari.")
t.B("Masjid, madrasa va diniy muassasalarga qarashli yerlar qanday atalgan?", "vaqf", "amlok", "mulk", "iqto", "Vaqf yerlari.")
t.B("Vaqf yerlaridan olinadigan foyda hisob-kitobi va taqsimoti bilan kim shug‘ullangan?", "mutavalli", "mirob", "mushrif", "sadr", "Mutavalli.")
t.B("Aholining majburiy mehnat qilib berishi qanday nomlangan?", "begar", "hashar", "xiroj", "zakot", "Mehnat majburiyati begar deb ham nomlangan.")
t.B("Xiva xonligida asosiy soliq qanday atalgan?", "solg‘ut", "xiroj", "zakot", "tanobona", "Xivada asosiy soliq solg‘ut deb atalgan.")
t.B("Chorvador aholi chorva mollaridan qanday soliq to‘lagan?", "zakot", "solg‘ut", "tarozi puli", "do‘kon puli", "Chorva mollaridan zakot solig‘i to‘langan.")
t.B("Sug‘orish ishlarini yuritish va nazorat qilish bilan qaysi mutaxassislar shug‘ullangan?", "miroblar", "mutavallilar", "mushriflar", "dodxohlar", "Miroblar.")
t.B("Suv chiqishi qiyin bo‘lgan joylarga suv qanday qurilma yordamida chiqarilgan?", "chig‘ir", "kariz", "to‘g‘on", "sardoba", "Maxsus qurilmalar — chig‘irlar yordamida.")
t.B("Marg‘ilonda qaysi hunarlar rivojlangan?", "atlas to‘qish, do‘ppichilik", "kulolchilik", "pichoqchilik, duradgorlik", "me’morchilik, ganchkorlik", "Marg‘ilonda atlas to‘qish, do‘ppichilik.")
t.B("Rishton qaysi hunari bilan mashhur bo‘lgan?", "kulolchilik", "atlas to‘qish", "zargarlik", "ganchkorlik", "Rishtonda kulolchilik rivojlangan.")
t.B("Xivada qaysi hunarlar rivojlangan?", "me’morchilik, ganchkorlik", "atlas to‘qish", "pichoqchilik", "kulolchilik", "Xivada me’morchilik, ganchkorlik.")
t.B("O‘rta Osiyodagi ichki va tashqi savdo rivojlanishiga nima salbiy ta’sir ko‘rsatgan?", "uchta davlat o‘rtasidagi kelishmovchiliklar, ichki nizolar", "hunarmandchilikning rivoji", "sug‘orish tizimining kengayishi", "Rossiya bilan savdo", "Uch davlat o‘rtasidagi kelishmovchiliklar va notinchliklar.")
t.NAT("Xazinaga tushadigan asosiy daromadni dehqonlardan yig‘iladigan soliqlar tashkil qildi.", "sug‘orish va suv ta’minoti davlat ahamiyati darajasiga ko‘tarildi", "sug‘orish tizimi tashlab qo‘yildi", "dehqonlar soliqdan ozod qilindi", "hunarmandchilik taqiqlandi", "Shuning uchun sug‘orish sohasi davlat ahamiyatiga ega bo‘ldi.")
t.NAT("Xonliklarda temir mahsulotlariga ehtiyoj katta bo‘ldi.", "metallga ishlov beruvchi mahalliy temirchilik rivojlandi", "temir chetdan to‘liq olib kelindi", "kulolchilik yo‘qoldi", "zargarlik taqiqlandi", "Shu bois mahalliy temirchilik sohasi rivojlangan.")
t.TF("Farg‘ona vodiysida Shahrixonsoy, Andijonsoy, Marg‘ilonsoy, Yangiariq kabi yirik sug‘orish inshootlari bo‘lgan.", True, "To‘g‘ri.")
t.TF("Hunarmandchilik yirik fabrikalardan iborat bo‘lib, unda mashinalardan foydalanilgan.", False, "Noto‘g‘ri: xonadon va kasanachilik ko‘rinishidagi mayda ustaxonalar, qo‘l mehnati.")
t.MUL([("Sug‘orish ishlari asosan hashar yo‘li bilan bajarilgan.", True),
       ("Shahar aholisidan savdo puli, do‘kon puli, tarozi puli kabi soliqlar olingan.", True),
       ("O‘rta Osiyo savdogarlari faqat Rossiya bilan savdo qilgan.", False)],
      "III noto‘g‘ri: Eron, Xitoy, Hindiston, Afg‘oniston, Rossiya va qozoq juzlari bilan savdo qilganlar.")
t.MATCH("Hunarmandchilik markazlarini ularning hunarlari bilan moslashtiring.", ["Marg‘ilon", "Rishton", "Shahrixon", "Xiva"],
        ["kulolchilik", "me’morchilik, ganchkorlik", "atlas to‘qish, do‘ppichilik", "pichoqchilik, duradgorlik"], "cadb",
        "Marg‘ilon — atlas; Rishton — kulolchilik; Shahrixon — pichoqchilik; Xiva — me’morchilik.")
t.MAPMATCH(FV, ['Marg‘ilon', 'Rishton', 'Chust'],
           ["atlas to‘qish va do‘ppichilik markazi", "kulolchilik markazi", "do‘ppichilik va pichoqchilik markazi"],
           "1 – Marg‘ilon; 2 – Rishton; 3 – Chust.")
t.VENN("Amlok yerlari", "Vaqf yerlari",
       [("davlat yerlari", 1), ("yirik amaldor va sarkardalarga in’om etilgan", 1),
        ("masjid va madrasalarga qarashli", 2), ("foydasini mutavalli taqsimlagan", 2),
        ("yer egaligining uch turidan biri", 3)],
       "Amlok — davlat yerlari; vaqf — diniy muassasalarniki, mutavalli boshqargan; ikkalasi yer egaligi turlari.")

# 4-5 Madaniy hayot
t = Topic('e9u4-5', 9004); TOPICS['e9u4-5'] = t
t.B("XIX asrda nechtaga yaqin doston ma’lum bo‘lgan?", "qirqqa yaqin", "o‘ntaga yaqin", "yuzga yaqin", "beshta", "Qirqqa yaqin doston ma’lum bo‘lgan.")
t.B("XIX asrdagi eng mashhur dostonlar qaysilar?", "«Alpomish», «Go‘ro‘g‘li», «Kuntug‘mish», «Shirin va Shakar»", "«Shohnoma», «Layli va Majnun»", "«Qutadg‘u bilig», «Devonu lug‘otit turk»", "«Boburnoma», «Xamsa»", "«Alpomish», «Go‘ro‘g‘li», «Kuntug‘mish», «Shirin va Shakar».")
t.B("Madrasalar ta’limini nazorat qiluvchi mansab qanday atalgan?", "olimlar yasovuli", "shayxulislom", "mutavalli", "mudarris", "Olimlar yasovuli (XVI asrda paydo bo‘lgan).")
t.B("Madrasalarda o‘qish mavsumi necha oy davom etgan?", "6 oy", "9 oy", "3 oy", "12 oy", "Sentabr ikkinchi yarmidan mart oxirigacha — 6 oy.")
t.B("Madrasalarda haftada necha kun o‘qilgan?", "to‘rt kun", "olti kun", "besh kun", "uch kun", "Shanba, yakshanba, dushanba, seshanba.")
t.B("Xorazmning 1812-yilgacha bo‘lgan tarixini kim yozgan?", "Shermuhammad Munis", "Ogahiy", "Ahmad Donish", "Muhammad Yunus", "Eltuzar farmoyishi bilan Munis yozgan.")
t.B("Munis 1819-yilda qaysi asarni o‘zbek tiliga tarjima qila boshlagan?", "Mirxondning «Ravzat us-safo» asarini", "«Shohnoma»ni", "«Zafarnoma»ni", "«Boburnoma»ni", "Mirxondning «Ravzat us-safo» («Soflik bog‘i»).")
t.B("Munisning «Firdavs ul-iqbol» asarini kim nihoyasiga yetkazgan?", "Ogahiy", "Ahmad Donish", "Turdi Ali", "Muhammad Yunus", "Shogirdi va jiyani Ogahiy.")
t.B("Ogahiyning asl ismi nima bo‘lgan?", "Muhammad Rizo Ernazarbiy o‘g‘li", "Shermuhammad Amir Avazbiy o‘g‘li", "Ahmad Donish", "Mirzo Mahmud", "Muhammad Rizo Ernazarbiy o‘g‘li.")
t.B("Ogahiy nechta tarixiy, ma’rifiy, tarjima asarlar muallifi?", "16 ta", "40 ta", "5 ta", "100 ta", "16 ta asar muallifi.")
t.B("Ogahiyning xalqparvarligi qaysi g‘azalida yorqin ifodasini topgan?", "«Qish»", "«Bahor»", "«Vatan»", "«Navro‘z»", "«Qish» g‘azalida.")
t.B("Ahmad Donish qaysi yili Rossiya shaharlari bo‘ylab sayohat qilgan?", "1857-yilda", "1865-yilda", "1819-yilda", "1873-yilda", "Amir Nasrullo elchilari bilan 1857-yilda.")
t.B("Ahmad Donishning astronomiyaga oid kitobi qaysi?", "«Manozir ul-kavokib»", "«Navodir ul-voqoe’»", "«Riyoz ud-davla»", "«Xudoyqul anvar»", "1865-yilda «Manozir ul-kavokib» yozgan.")
t.B("Muhammad Alixon davri tarixi yoritilgan «Xudoyqul anvar» asarini kim yozgan?", "Muhammad Yunus", "Ogahiy", "Turdi Ali", "Munis", "Saroy tarixchisi Muhammad Yunus, 1859-yil.")
t.B("Qo‘qon xonligidagi eng mashhur xattot kim bo‘lgan?", "Turdi Ali", "Mirzo Mahmud", "Muhammad Yunus", "Ahmad Donish", "Turdi Ali.")
t.B("Yuzdan ortiq xonadan iborat noyob arxitektura yodgorligi qaysi?", "Xudoyorxon saroyi", "Muhammad Aminxon madrasasi", "Baroqxon madrasasi", "Tillashayx masjidi", "Xudoyorxon saroyi (1863–1870).")
t.B("Ikki tilda (o‘zbek va fors) ijod qilish qanday atalgan?", "zullisonayn", "epos", "xonaqoh", "truppa", "Zullisonayn.")
t.NAT("Mart oyi oxiridan dala ishlari boshlanib, sentabr oxirida hosil yetilar edi.", "madrasalarda o‘quv mavsumi sentabrdan martgacha belgilandi", "madrasalar yil bo‘yi ishladi", "talabalar dala ishlaridan ozod qilindi", "madrasalar yopildi", "Talaba 6 oy dala ishlarida oilasiga yordam bera olgan.")
t.TF("Buxoro amirligidagi ta’lim tizimi Xiva va Qo‘qon xonliklarida ham joriy etilgan.", True, "To‘g‘ri.")
t.TF("Muhammad Aminxon madrasasi Qo‘qonda qurilgan.", False, "Noto‘g‘ri: u Xivadagi Ichan qal’ada (1851–1855).")
t.MUL([("Madrasalar maktablar uchun mullalar, masjidlar uchun imomlar, qozilar, mirzalar tayyorlagan.", True),
       ("Xiva binolari tiniq zangori rang ustidan oq va yashil gullar tushirilgan koshinlar bilan bezatilgan.", True),
       ("Madrasalarda ta’lim olish muddati qat’iy 4 yil bilan cheklangan.", False)],
      "III noto‘g‘ri: ta’lim muddati ko‘p hollarda cheklanmagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Munis «Ravzat us-safo»ni tarjima qila boshladi", "Ahmad Donish Rossiyaga sayohat qildi", "«Xudoyqul anvar» yozildi", "Ahmad Donish «Manozir ul-kavokib»ni yozdi", "Muhammad Rahimxon madrasasi qurildi"],
      "1819 → 1857 → 1859 → 1865 → 1871.")
t.MATCH("Yodgorliklarni shaharlar bilan moslashtiring.", ["Muhammad Aminxon madrasasi", "Xudoyorxon saroyi", "Baroqxon madrasasi"],
        ["Toshkent", "Xiva", "Qo‘qon"], "bca", "Muhammad Aminxon — Xiva; Xudoyorxon saroyi — Qo‘qon; Baroqxon — Toshkent.")
t.MAPMATCH(CA, ['Xiva', 'Qo‘qon', 'Toshkent'],
           ["Muhammad Aminxon va Muhammad Rahimxon madrasalari", "Xudoyorxon saroyi, Hokim Oyim madrasasi", "Baroqxon madrasasi, Tillashayx jome masjidi"],
           "1 – Xiva; 2 – Qo‘qon; 3 – Toshkent.")
t.VENN("Munis", "Ogahiy",
       [("Eltuzar farmoyishi bilan Xorazm tarixini yozgan", 1), ("1819-yilda «Ravzat us-safo»ni tarjima qila boshlagan", 1),
        ("«Riyoz ud-davla», «Gulshani davlat» asarlari muallifi", 2), ("«Qish» g‘azali muallifi", 2),
        ("Xiva xonligi tarixchisi", 3)],
       "Munis — Eltuzar topshirig‘i, tarjima boshlagan; Ogahiy — «Riyoz ud-davla», «Qish»; ikkalasi Xiva tarixchilari.")
