from qlib import Topic
TOPICS = {}
CA2 = 'ca2'; FV = 'fargona'

# 16 Ijtimoiy-iqtisodiy ahvol
t = Topic('e9u16', 9016); TOPICS['e9u16'] = t
t.B("Kavkazdan qo‘shin tashish uchun temiryo‘l dastlab qayerdan qayergacha qurilgan?", "Krasnovodskdan Qizilarvatgacha", "Orenburgdan Toshkentgacha", "Samarqanddan Andijongacha", "Toshkentdan Verniygacha", "Krasnovodskdan Qizilarvatgacha, so‘ng Ashxobodgacha.")
t.B("Samarqandga dastlabki poyezd qachon kelgan?", "1888-yilda", "1899-yilda", "1905-yilda", "1881-yilda", "1888-yilda.")
t.B("Temiryo‘l Toshkent orqali Andijongacha qachon qurib bitkazilgan?", "1899-yilda", "1888-yilda", "1905-yilda", "1913-yilda", "1899-yilda.")
t.B("Orenburgdan Toshkentga temiryo‘l qachon qurib kelingan?", "1905-yilda", "1899-yilda", "1888-yilda", "1911-yilda", "1905-yilda.")
t.B("Krasnovodskdan Andijongacha masofa qancha bo‘lgan?", "3 ming kilometrdan ziyod", "500 kilometr", "10 ming kilometr", "1 ming kilometr", "3 ming km dan ziyod.")
t.B("Rossiya harbiy qurolli kuchlarining asosiy bazalari qayerda joylashgan?", "Kavkazda", "Sibirda", "Orenburgda", "Toshkentda", "Kavkazda; Kaspiy orqali kemada o‘tilgan.")
t.B("1867–1900-yillarda Turkistonda nechta sanoat korxonasi ishga tushirilgan?", "175 ta", "19 ta", "1300 ta", "25 ta", "175 ta, aksariyati qo‘l mehnatida.")
t.B("Korxonalarda ish kuni necha soat bo‘lgan?", "16 soat", "8 soat", "10 soat", "12 soat", "16 soat.")
t.B("Paxtadan tayyor mahsulot qayerda tayyorlangan?", "imperiyaning markaziy gubernalarida", "Toshkentda", "Farg‘onada", "Buxoroda", "O‘lkada faqat tozalash va yog‘ ishlab chiqarish yo‘lga qo‘yilgan.")
t.B("Turkistonda Amerika paxta navi qachon yetishtirila boshlagan?", "1884-yilda", "1888-yilda", "1867-yilda", "1911-yilda", "1884-yilda.")
t.B("Sirdaryo magistral kanalini qurish ishlari qachon boshlangan?", "1911-yilda", "1884-yilda", "1899-yilda", "1913-yilda", "1911-yilda boshlanib, 1913-yilda tugallangan.")
t.B("Mustamlakachi hukumat uchun paxta qaysi sohalardan keyingi o‘rinda turgan?", "neft va oltindan keyin", "g‘alla va chorvadan keyin", "temir va ko‘mirdan keyin", "ipak va jundan keyin", "Neft va oltindan keyingi o‘rinda.")
t.B("Qaysi viloyatlar paxta yetishtiriladigan eng muhim markazlar bo‘lgan?", "Farg‘ona, Sirdaryo va Samarqand", "Yettisuv va Kaspiyorti", "Sirdaryo va Yettisuv", "Kaspiyorti va Samarqand", "Farg‘ona, Sirdaryo va Samarqand viloyatlari.")
t.NAT("Imperiya to‘qimachilik sanoati uchun paxta yetishtirish ko‘paydi.", "boshqa ekinlar kamayib, g‘alla tanqisligi yuzaga keldi", "g‘alla ko‘paydi", "chorvachilik rivojlandi", "hunarmandchilik kengaydi", "Paxta ko‘payishi g‘alla tanqisligiga sabab bo‘ldi.")
t.NAT("Rossiyadan arzon zavod va fabrika mahsulotlari keltirildi.", "mahalliy hunarmandlar bozori kasodga uchrab, ko‘plab hunarmandlar ishsiz qoldi", "hunarmandlar boyidi", "mahalliy sanoat kuchaydi", "narxlar oshdi", "Arzon mahsulotlar hunarmandlar bozorini sindirdi.")
t.NAT("Yaylovlar paxta maydonlariga aylantirildi.", "chorvachilik va chorva mahsulotlari kamaydi, narxlar oshdi", "chorva ko‘paydi", "g‘alla eksporti boshlandi", "yaylovlar kengaydi", "Farg‘ona vodiysiga g‘alla va chorva mahsulotlari chetdan keltirila boshlandi.")
t.TF("Temiryo‘llar harbiy-strategik maqsadlarni ham ko‘zlab qurilgan.", True, "To‘g‘ri.")
t.TF("Rossiya sarmoyasi o‘lkada ishlab chiqarishni har tomonlama rivojlantirishga qaratilgan.", False, "Noto‘g‘ri: tabiiy boyliklarni o‘zlashtirish va xomashyoni tashib ketishga qaratilgan.")
t.MUL([("Mahalliy sanoat ishchilari xonavayron dehqonlar va ishsiz hunarmandlar hisobidan ortgan.", True),
       ("Ishchilarning huquqini himoya qiladigan tashkilotlar bo‘lmagan.", True),
       ("Sirdaryo magistral kanali qurilgach, barcha sug‘orish ishlari to‘liq bajarildi.", False)],
      "III noto‘g‘ri: Toshkent vohasi, Samarqand va Farg‘onada ishlarning ko‘pi bajarilmay qolgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Amerika paxta navi ekila boshlandi", "Samarqandga dastlabki poyezd keldi", "Temiryo‘l Andijongacha yetdi", "Orenburg–Toshkent temiryo‘li qurildi", "Sirdaryo magistral kanali tugallandi"],
      "1884 → 1888 → 1899 → 1905 → 1913.")
t.MAPMATCH(CA2, ['Krasnovodsk', 'Ashxobod', 'Samarqand', 'Andijon'],
           ["temiryo‘l boshlangan Kaspiy bo‘yidagi shahar", "Qizilarvatdan keyin temiryo‘l yetkazilgan shahar", "1888-yilda dastlabki poyezd kelgan shahar", "1899-yilda temiryo‘l yetib borgan shahar"],
           "1 – Krasnovodsk; 2 – Ashxobod; 3 – Samarqand; 4 – Andijon.")
t.VENN("Rossiya sanoatining manfaati", "Mahalliy aholining ahvoli",
       [("arzon paxta xomashyosi olish", 1), ("o‘z mahsulotlarini o‘lkada sotish", 1),
        ("hunarmandlarning ishsiz qolishi", 2), ("g‘alla va chorva narxining oshishi", 2),
        ("paxta maydonlarining kengayishi bilan bog‘liq", 3)],
       "Paxta yakkahokimligi Rossiyaga foyda, mahalliy aholiga zarar keltirdi.")

# 17 Milliy-ozodlik harakatlarining boshlanishi
t = Topic('e9u17', 9017); TOPICS['e9u17'] = t
t.B("Yer-mulkning boylar qo‘lida to‘planishi kimlarning ko‘payishiga sabab bo‘lgan?", "kam yerli dehqonlar va chorakorlarning", "hunarmandlarning", "savdogarlarning", "amaldorlarning", "Kam yerli dehqonlar, chorakorlar ko‘paydi.")
t.B("Paxtani sotib oluvchilar dehqonlarga qanday qarz bergan?", "kelasi yil hosiliga juda past narx belgilab", "foizsiz", "davlat kafolati bilan", "yer evaziga bepul", "Kelasi yil hosiliga past narx belgilab.")
t.B("Qo‘zg‘olonlarning harakatlantiruvchi kuchi kimlar bo‘lgan?", "dehqonlar va shahar hunarmand-kosiblari", "amaldorlar", "rus ko‘chmanchilari", "harbiylar", "Asosan dehqonlar va kambag‘al hunarmand-kosiblar.")
t.B("1878-yilda Mingtepada kim boshchiligida qo‘zg‘olon ko‘tarilgan?", "Yetimxon", "Darvishxon", "Rahmonqulihoji", "Dukchi eshon", "Yetimxon boshchiligida.")
t.B("Mingtepa hozirgi qaysi tumanda joylashgan?", "Marhamat tumani", "Marg‘ilon tumani", "Chust tumani", "Shahrixon tumani", "Hozirgi Marhamat tumani.")
t.B("1879-yil kuzida aholi qaysi binoning oldiga norozilik bildirib yig‘ilgan?", "Farg‘ona viloyat boshqarmasi binosi", "Toshkent shahar dumasi", "Namangan uyezd mahkamasi", "Xo‘jand qal’asi", "Farg‘ona viloyat boshqarmasi binosi oldiga.")
t.B("1879-yildagi norozilik qaysi uyezddagi noqonuniy soliq yig‘imiga qarshi bo‘lgan?", "Marg‘ilon uyezdi", "Namangan uyezdi", "Xo‘jand uyezdi", "Andijon uyezdi", "Marg‘ilon uyezdida.")
t.B("1880-yil noyabrida Xo‘jand va O‘ratepa aholisidan qanday soliq olinishi e’lon qilingan?", "qo‘shimcha yer solig‘i", "zakot", "suv solig‘i", "savdo puli", "Qo‘shimcha yer solig‘i.")
t.B("1880-yilda Xo‘jandda namoyishga kimlar boshchilik qilgan?", "Rahmonqulihoji va Mirkarimboy", "Yetimxon va Darvishxon", "Jo‘rabek va Bobobek", "Po‘latxon va Nasriddinbek", "Rahmonqulihoji va Mirkarimboy.")
t.B("1882-yil boshlarida qaysi shahar aholisi uyezd boshlig‘ining uyini o‘rab olgan?", "Namangan", "Andijon", "Marg‘ilon", "Xo‘jand", "Namangan aholisi.")
t.B("1885-yil yozida Andijonda kim boshchiligida qo‘zg‘olon ko‘tarilgan?", "Darvishxon", "Yetimxon", "Mirkarimboy", "Rahmonqulihoji", "Darvishxon boshchiligida.")
t.B("1896-yilda Naymanchi, Ko‘hna mozor, Langarbob qishloqlarida norozilik nimadan boshlangan?", "mingboshilar saylovidan", "yer solig‘idan", "vabo karantinidan", "suv taqsimotidan", "Mingboshilar saylovlaridagi norozilikdan.")
t.B("Qaysi yildan oddiy fuqarolar ma’murlarga qarshilik ko‘rsatsa harbiy dala sudiga berila boshlagan?", "1892-yildan", "1878-yildan", "1885-yildan", "1898-yildan", "1892-yildan.")
t.NAT("Komissiya 1879-yildagi norozilik sababini o‘rgandi.", "paxta ekishning keng avj oldirilishi va boshqa ekinlarning kamaygani sabab ekani aniqlandi", "soliqlar bekor qilindi", "qo‘zg‘olonchilar mukofotlandi", "Marg‘ilon uyezdi tugatildi", "Komissiya paxta ekishning kengayishini sabab deb ko‘rsatdi.")
t.NAT("1880-yilda Xo‘jandda aholi adolatsiz soliqni bekor qilishni talab qildi.", "uyezd boshlig‘i namoyish rahbarlarini hibsga olishni buyurdi", "soliq bekor qilindi", "uyezd boshlig‘i ishdan olindi", "aholiga yer berildi", "Boshliq mirshablarga rahbarlarni hibsga olishni buyurdi.")
t.NAT("Dehqonlar sudxo‘rlar changaliga tushib qoldi.", "ular xo‘jalik mustaqilligidan mahrum bo‘lib, yerlarini sotishga majbur bo‘ldi", "ular boyib ketdi", "sudxo‘rlik taqiqlandi", "davlat qarzlarni kechirdi", "Qarzlar tufayli yerlarini sotishga majbur bo‘ldilar.")
t.TF("1885-yilda qo‘zg‘olonchilar boylar va volost boshliqlarining qarorgohlariga hujum uyushtirgan.", True, "To‘g‘ri.")
t.TF("Mustamlakachi hukumat ko‘chirilganlar qishloqlari va mahalliy qishloqlarni birlashtirgan volostlarga faqat mahalliy aholidan rahbar qo‘ygan.", False, "Noto‘g‘ri: mahalliy aholiga mansub bo‘lmagan shaxslarni qo‘ya boshlagan.")
t.MUL([("Harakatlarda vatanparvar ruhoniylar, mulkdorlar va savdogarlar ham ishtirok etgan.", True),
       ("Maxsus bo‘lim boshlig‘i «isyonga moyil»larni harbiy sudga berishni taklif qilgan.", True),
       ("Yetimxon qo‘zg‘oloni mustamlakachilar bilan sulh tuzish bilan yakunlangan.", False)],
      "III noto‘g‘ri: qo‘zg‘olon kuch bilan bostirilgan.")
t.CHR("Qo‘zg‘olonlarni xronologik ketma-ketlikda joylashtiring.", ["Mingtepada Yetimxon qo‘zg‘oloni", "Xo‘jandda Rahmonqulihoji namoyishi", "Namanganda uyezd boshlig‘ining uyini o‘rab olish", "Andijonda Darvishxon qo‘zg‘oloni", "Oqsuv-Shahrixon volostidagi qo‘zg‘olon"],
      "1878 → 1880 → 1882 → 1885 → 1896.")
t.MAPMATCH(FV, ['Mingtepa', 'Marg‘ilon', 'Xo‘jand', 'Namangan'],
           ["1878-yilda Yetimxon qo‘zg‘oloni bo‘lgan joy", "1879-yilda noqonuniy soliq yig‘imiga qarshi chiqilgan uyezd markazi", "1880-yilda qo‘shimcha yer solig‘iga qarshi namoyish bo‘lgan shahar", "1882-yilda aholi uyezd boshlig‘ining uyini o‘rab olgan shahar"],
           "1 – Mingtepa; 2 – Marg‘ilon; 3 – Xo‘jand; 4 – Namangan.")
t.VENN("Yetimxon qo‘zg‘oloni", "Darvishxon qo‘zg‘oloni",
       [("1878-yilda bo‘lgan", 1), ("Mingtepada ko‘tarilgan", 1),
        ("1885-yil yozida bo‘lgan", 2), ("boylar va volost boshliqlari qarorgohlariga hujum", 2),
        ("Farg‘ona vodiysidagi mustamlakachilikka qarshi chiqish", 3)],
       "Yetimxon — 1878, Mingtepa; Darvishxon — 1885, Andijon, boylarga hujum.")
