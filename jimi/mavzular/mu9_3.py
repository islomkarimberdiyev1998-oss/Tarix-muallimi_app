from qlib import Topic
TOPICS = {}
CA = 'ca'

# 6 Istilochilik harakatlarining boshlanishi
t = Topic('e9u6', 9006); TOPICS['e9u6'] = t
t.B("Pyotr I davrida O‘rta Osiyoga kim boshchiligida harbiy ekspeditsiya jo‘natilgan?", "Aleksandr Bekovich-Cherkasskiy", "M. Chernyayev", "N. Veryovkin", "K. Kaufman", "Aleksandr Bekovich-Cherkasskiy boshchiligida.")
t.B("1718-yilda Irtish daryosi sohilida nechta istehkom qurib bitkazilgan?", "yettita", "uchta", "o‘nta", "beshta", "Yettita istehkom.")
t.B("Angliya bilan aloqalarni yo‘lga qo‘yish uchun 1825-yilda O‘rta Osiyoga kim yuborilgan?", "M. Murkroft", "A. Byorns", "J. Abbot", "I. Volf", "1825-yilda M. Murkroft.")
t.B("1832-yilda Buxoroga kim yuborilgan?", "A. Byorns", "M. Murkroft", "Ch. Stoddart", "J. Abbot", "1832-yilda A. Byorns.")
t.B("1843-yilda Xiva va Buxoroga yuborilgan ingliz zobiti kim?", "kapitan J. Abbot", "mayor I. Volf", "A. Konnoli", "M. Murkroft", "Kapitan J. Abbot.")
t.B("Ost-Indiya kompaniyasi vakillari Ch. Stoddart va A. Konnoli qachon qatl qilingan?", "1842-yilda", "1832-yilda", "1855-yilda", "1847-yilda", "1842-yilda amir tomonidan qatl qilingan.")
t.B("1855-yilda Amudaryoning janubiy sohilidagi hududlar qaysi davlat viloyatiga aylantirildi?", "Afg‘oniston", "Eron", "Rossiya", "Angliya", "Afg‘oniston viloyatiga.")
t.B("Raim qal’asi qachon bunyod etilgan?", "1847-yilda", "1853-yilda", "1864-yilda", "1718-yilda", "1847-yilda Sirdaryoning Orolga quyilish joyida.")
t.B("Qaysi urushdagi mag‘lubiyat Rossiyani O‘rta Osiyoni bosib olishni tezlashtirishga undagan?", "Qrim urushi (1853–1856)", "Rus-yapon urushi", "Birinchi jahon urushi", "Napoleon bilan urush", "Qrim urushidagi mag‘lubiyat.")
t.B("Qaysi voqea tufayli Rossiyada paxta xomashyosiga taqchillik vujudga kelgan?", "AQSHdagi fuqarolar urushi (1861–1865)", "Qrim urushi", "Hindistondagi qo‘zg‘olon", "Fransiya–Prussiya urushi", "AQSHdagi fuqarolar urushi tufayli.")
t.B("O‘rta Osiyoni bosib olishning birinchi bosqichi qaysi yillarni qamragan?", "1847–1865-yillar", "1865–1868-yillar", "1873–1879-yillar", "1880–1885-yillar", "1847–1865-yillar.")
t.B("Turkmanlarning bo‘ysundirilishi qaysi bosqichga to‘g‘ri keladi?", "to‘rtinchi (1880–1885)", "birinchi (1847–1865)", "ikkinchi (1865–1868)", "uchinchi (1873–1879)", "To‘rtinchi bosqich — 1880–1885-yillar.")
t.B("Oqmachit qal’asi himoyachilari necha kun qarshilik ko‘rsatgan?", "20 kun", "3 kun", "40 kun", "7 kun", "400 himoyachi 3 mingdan ortiq qo‘shinga 20 kun qarshilik ko‘rsatdi.")
t.B("Oqmachit qal’asi egallangach qanday nom berilgan?", "Perovskiy forti", "Verniy", "Raim", "Niyozbek", "Perovskiy forti.")
t.B("1864-yil 4-iyunda Chernyayev qo‘shini qaysi shaharni bosib oldi?", "Avliyoota (Taroz)", "Chimkent", "Turkiston", "Toshkent", "Talas daryosi bo‘yidagi Avliyoota.")
t.B("Turkiston va Chimkent mudofaasiga Qo‘qon xoni kimni yuborgan?", "amirlashkar Aliquli (Alimqul)", "Solihbek dodxoh", "Hakim xo‘ja", "Abulqosim eshon", "Amirlashkar Aliquli.")
t.NAT("Veryovkin taslim bo‘lmasa Turkistonni qirib, Ahmad Yassaviy maqbarasini yakson qilishini ultimatum qilib qo‘ydi.", "Aliquli qo‘shinini Turkistondan olib chiqib, Chimkent mudofaasiga chekindi", "Turkiston himoyachilari g‘alaba qozondi", "Veryovkin chekindi", "maqbara buzib tashlandi", "Aliquli Chimkentga chekindi; 12-iyulda Turkiston bosib olindi.")
t.NAT("XIX asr birinchi yarmida xonliklar o‘rtasida uzoq vaqt o‘zaro urushlar davom etdi.", "xonliklar iqtisodiy va harbiy jihatdan zaiflashdi, istilo osonlashdi", "xonliklar birlashib kuchaydi", "Angliya xonliklarni bosib oldi", "Rossiya istilodan voz kechdi", "O‘zaro urushlar xonliklarni zaiflashtirib, istiloni osonlashtirdi.")
t.TF("1842-yildagi qatlga javoban Angliya Afg‘oniston bilan sulh tuzib, uni Buxoroga qarshi qurollantirgan.", True, "To‘g‘ri.")
t.TF("Oqmachit qal’asi 1852-yildagi birinchi hujumdayoq egallangan.", False, "Noto‘g‘ri: 1852-yilgi harakat mag‘lubiyatga uchradi, qal’a 1853-yilda egallandi.")
t.MUL([("Rossiyaga sanoat xomashyosi, iste’mol bozorlari va arzon paxta tolasi kerak edi.", True),
       ("Toshkentga boradigan asosiy yo‘l Orenburg yo‘li bo‘lgan.", True),
       ("1864–1885-yillardagi bosqinchilik urushlari 5 yil davom etgan.", False)],
      "III noto‘g‘ri: 20 yildan ortiq davom etgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Irtish bo‘yida 7 ta istehkom qurildi", "Murkroft O‘rta Osiyoga yuborildi", "Stoddart va Konnoli qatl qilindi", "Raim qal’asi qurildi", "Oqmachit egallandi", "Turkiston shahri bosib olindi"],
      "1718 → 1825 → 1842 → 1847 → 1853 → 1864.")
t.MATCH("Bosqichlarni voqealar bilan moslashtiring.", ["Birinchi bosqich", "Ikkinchi bosqich", "Uchinchi bosqich", "To‘rtinchi bosqich"],
        ["1873–1879: Xiva va Qo‘qon yerlari", "1880–1885: turkmanlar bo‘ysundirildi", "1847–1865: Qo‘qonning shimoli-g‘arbi va Toshkent", "1865–1868: Qo‘qon va Buxoroga qarshi yurish"], "cdab",
        "1 — 1847–1865; 2 — 1865–1868; 3 — 1873–1879; 4 — 1880–1885.")
t.MAPMATCH(CA, ['Raim', 'Oqmachit', 'Avliyoota', 'Turkiston'],
           ["1847-yilda Sirdaryoning Orolga quyilish joyida qurilgan qal’a", "1853-yilda egallanib, Perovskiy forti deb nomlangan qal’a", "1864-yil 4-iyunda Chernyayev bosib olgan shahar (Taroz)", "1864-yil 12-iyulda Veryovkin bosib olgan shahar"],
           "1 – Raim; 2 – Oqmachit; 3 – Avliyoota; 4 – Turkiston.")
t.VENN("Sirdaryo istehkom chizig‘i", "Sibir istehkom chizig‘i",
       [("Raim qal’asidan boshlangan", 1), ("Perovskiy fortigacha cho‘zilgan", 1),
        ("Semipalatinskdan boshlangan", 2), ("Verniy shahrigacha cho‘zilgan", 2),
        ("Rossiya imperiyasining harbiy istehkom chizig‘i", 3)],
       "Sirdaryo chizig‘i — Raimdan Perovskiy fortigacha; Sibir chizig‘i — Semipalatinskdan Verniygacha.")

# 7 Toshkentning bosib olinishi
t = Topic('e9u7', 9007); TOPICS['e9u7'] = t
t.B("Toshkent nechta dahaga bo‘lingan?", "to‘rtta", "uchta", "oltita", "o‘nta", "Beshyog‘och, Ko‘kcha, Sebzor, Shayxontohur.")
t.B("Toshkent mudofaa devori ortidagi xandaqlar qaysi ariq suvi bilan to‘ldirilgan?", "Kaykovus arig‘i", "Bo‘zsuv", "Anhor", "Chirchiq", "Kaykovus arig‘i suvi bilan.")
t.B("XIX asr o‘rtalarida Toshkent aholisi qancha bo‘lgan?", "80 mingga yaqin", "2 million", "800 ming", "20 ming", "80 mingga yaqin kishi.")
t.B("Toshkent qal’a devori necha kilometr bo‘lgan?", "20 kilometr", "5 kilometr", "50 kilometr", "2 kilometr", "20 kilometrlik qal’a devori bilan o‘ralgan.")
t.B("Chernyayev Toshkentga birinchi marta qachon hujum qilgan?", "1864-yil 1-oktabrda", "1865-yil mayda", "1865-yil 17-iyunda", "1864-yil 12-iyulda", "1864-yil 1-oktabrda.")
t.B("Birinchi hujum muvaffaqiyatsiz bo‘lgach, Chernyayev qayerga chekingan?", "Chimkentga", "Turkistonga", "Oqmachitga", "Verniyga", "70 dan ziyod askaridan ajralib, Chimkentga chekindi.")
t.B("Qaysi qal’a «Toshkent darvozasi» deb nom olgan?", "Niyozbek qo‘rg‘oni", "Oqmachit", "Raim", "Perovskiy forti", "Chirchiq bo‘yidagi Niyozbek qo‘rg‘oni.")
t.B("Niyozbek qal’asi Toshkentdan qancha uzoqlikda joylashgan?", "25 km", "5 km", "100 km", "60 km", "Toshkentdan 25 km uzoqlikda.")
t.B("Toshkent mudofaasiga kim boshchilik qilgan?", "amirlashkar Aliquli", "Solihbek dodxoh", "Hakim xo‘ja", "Xudoyorxon", "Amirlashkar Aliquli boshchiligida.")
t.B("Chernyayev qo‘shinlari shaharga qaysi darvoza yonidan devorni buzib kirgan?", "Kamolon darvozasi", "Ko‘kcha darvozasi", "Beshyog‘och darvozasi", "Labzak darvozasi", "Kamolon darvozasi yonidan.")
t.B("Chernyayev dahalar oqsoqollarini qachon chaqirgan?", "1865-yil 17-iyunda", "1865-yil 6-avgustda", "1864-yil 1-oktabrda", "1865-yil 1-mayda", "17-iyunda.")
t.B("Nechta oqsoqol shaharni «ixtiyoriy topshirish» sulhini imzolashga majbur bo‘lgan?", "9 nafari", "4 nafari", "20 nafari", "2 nafari", "Oqsoqollardan 9 nafari.")
t.B("Turkiston viloyatiga kim gubernator etib tayinlangan?", "general-mayor M. Chernyayev", "N. Veryovkin", "K. Kaufman", "Aleksandr II", "M. Chernyayev.")
t.B("«Turkiston viloyatini boshqarish to‘g‘risidagi Muvaqqat Nizom» qachon qabul qilingan?", "1865-yil 6-avgustda", "1865-yil 17-iyunda", "1867-yilda", "1864-yil 1-oktabrda", "1865-yil 6-avgustda.")
t.B("Turkiston viloyati qaysi general-gubernatorlik tarkibida tashkil etilgan?", "Orenburg", "Turkiston", "Dasht", "G‘arbiy Sibir", "Orenburg general-gubernatorligi tarkibida.")
t.NAT("Niyozbek qal’asi qo‘lga kiritilib, Chirchiq daryosidagi to‘g‘on buzib tashlandi.", "Toshkent suv ta’minotidan uzildi, yong‘inlarni o‘chirish imkoni bo‘lmadi", "shaharga suv ko‘proq keldi", "Chernyayev chekindi", "Buxoro qo‘shini g‘alaba qozondi", "Toshkent suvsiz qoldi, yong‘inlar o‘chirilmadi.")
t.NAT("Ayovsiz janglarda Aliquli yaralanib vafot etdi.", "himoyachilar sarosimaga tushib, istilochilarning qo‘li ustun keldi", "himoyachilar g‘alaba qozondi", "Chernyayev sulh so‘radi", "Buxoro qo‘shini shaharni egalladi", "Yagona harbiy boshliqsiz qolish mag‘lubiyatga olib keldi.")
t.NAT("Solihbek dodxoh, Abulqosim eshon, Hakim xo‘ja soxta xat yozilishiga qarshi chiqdi.", "ular Sibirga surgun qilindi", "ular Toshkent hokimi etib tayinlandi", "xat bekor qilindi", "Chernyayev ishdan olindi", "Bu vatanparvarlar Sibirga surgun qilingan.")
t.TF("Toshkent himoyasiga Buxoro amirligidan kechikib kelgan qo‘shinlarning foydasi tegmadi.", True, "To‘g‘ri.")
t.TF("Toshkent aholisi shahar darvozalarini ixtiyoriy ravishda ochib bergan.", False, "Noto‘g‘ri: shahar qurol kuchi bilan egallangan; «ixtiyoriy taslim» haqidagi xat soxta edi.")
t.MUL([("Toshkentni egallash O‘rta Osiyodagi harbiy yurishlar uchun tayanch nuqtani ta’minlar edi.", True),
       ("Himoyachilar shaharni o‘qqa tutilishidan saqlash uchun qal’aga o‘t qo‘yishgan.", True),
       ("Asosiy jang Ko‘kcha darvozasidan Chorsu bozoriga boradigan ko‘chada bo‘lgan.", False)],
      "III noto‘g‘ri: asosiy jang Kamolon darvozasidan Xadradagi markaziy bozorga boradigan ko‘chada bo‘lgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Chernyayevning Toshkentga birinchi hujumi", "Niyozbek qal’asining egallanishi", "Chernyayev dahalar oqsoqollarini chaqirdi", "Muvaqqat Nizom qabul qilindi"],
      "1864-yil 1-oktabr → 1865-yil aprel–may → 1865-yil 17-iyun → 1865-yil 6-avgust.")
t.MAPN(CA, ['Buxoro', 'Qo‘qon', 'Toshkent', 'Xiva'], "Xaritada 1865-yilda Chernyayev qo‘shinlari egallagan, Turkiston o‘lkasining markaziga aylantirilgan shahar qaysi raqam bilan belgilangan?",
       "Toshkent — Turkiston o‘lkasining harbiy, siyosiy va ma’muriy markazi.", ask_idx=2)
t.VENN("Toshkent himoyachilari", "Chernyayev qo‘shinlari",
       [("amirlashkar Aliquli boshchiligida jang qilgan", 1), ("mahalla ko‘chalarida to‘siqlar qurgan", 1),
        ("Chirchiqdagi to‘g‘onni buzgan", 2), ("Kamolon darvozasi yonidan shaharga kirgan", 2),
        ("1865-yil Toshkent janglarida qatnashgan", 3)],
       "Himoyachilar — Aliquli, to‘siqlar; Chernyayev — to‘g‘onni buzdi, Kamolondan kirdi.")
