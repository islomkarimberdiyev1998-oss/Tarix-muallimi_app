from qlib import Topic
TOPICS = {}
UZ = 'uzb'; CA = 'ca'

# 28 Jadidchilikning ijtimoiy-siyosiy va madaniy hayotga ta’siri
t = Topic('e9u28', 9028); TOPICS['e9u28'] = t
t.B("Behbudiy islom tarixiga oid asarini qachon yaratgan?", "1909-yilda", "1910-yilda", "1915-yilda", "1917-yilda", "1909-yilda; Avloniy — 1910, Fitrat — 1915.")
t.B("Fitratning to‘liq ismi qanday?", "Abdurauf Abdurahim o‘g‘li", "Abdulla Avloniy", "Ubaydullaxo‘ja Asadullaxo‘ja o‘g‘li", "Munavvarqori Abdurashidxonov", "Abdurauf Abdurahim o‘g‘li Fitrat.")
t.B("Jadidlar ilm-fanni nima deb hisoblagan?", "taraqqiyotning asosiy yo‘naltiruvchi kuchi", "zararli narsa", "faqat boylar uchun kerakli", "diniy ta’limga zid", "Taraqqiyot va farovonlikning asosiy kuchi, jaholatga qarshi vosita.")
t.B("Jadidlar yoshlarni qaysi rivojlangan davlatga o‘qishga yuborish g‘oyasini ilgari surgan?", "Germaniyaga", "Xitoyga", "Hindistonga", "Afg‘onistonga", "Jumladan, Germaniyaga.")
t.B("Birinchi oliy ma’lumotli o‘zbek advokati kim bo‘lgan?", "Ubaydullaxo‘ja Asadullaxo‘ja o‘g‘li", "Munavvarqori", "Behbudiy", "Fitrat", "Toshkentning Qoryog‘di mahallasidan Ubaydullaxo‘ja.")
t.B("Ubaydullaxo‘ja qaysi rus yozuvchisi bilan yozishmalar olib borgan?", "Lev Tolstoy", "Pushkin", "Dostoyevskiy", "Chexov", "Lev Tolstoy bilan.")
t.B("Birinchi jahon urushidan keyin jadidlar qanday boshqaruv uchun kurashgan?", "parlamentar monarxiya", "absolyut monarxiya", "harbiy diktatura", "xonlik", "Parlamentar monarxiya uchun.")
t.B("1917-yilda tuzilgan milliy-siyosiy tashkilotlar qaysilar?", "«Sho‘roi Islomiya», «Ittifoq»", "«Tarbiyai atfol», «Ma’rifat»", "«Tarjimon», «Shuhrat»", "Antanta", "«Sho‘roi Islomiya», «Ittifoq».")
t.B("1917-yil mart oyida Toshkentda qanday yagona tashkilot tuzilgan?", "«Musulmon markaziy sho‘rosi»", "«Tarbiyai atfol»", "«Sho‘roi Ulamo»", "«Yosh buxoroliklar»", "«Musulmon markaziy sho‘rosi».")
t.B("«Musulmon markaziy sho‘rosi» ta’sis syezdida necha delegat qatnashgan?", "350", "72", "100", "1000", "350 delegat.")
t.B("Syezd bo‘lajak davlat qanday nomlanishini ma’qulladi?", "Turkiston", "Buxoro", "Turon", "O‘zbekiston", "Turkiston; tarkibiga Buxoro, Xiva va general-gubernatorlik.")
t.B("Turkiston muxtoriyatining markazi qaysi shahar edi?", "Qo‘qon", "Toshkent", "Samarqand", "Buxoro", "Qo‘qon.")
t.B("Turkiston muxtoriyati necha kun yashagan?", "72 kun", "350 kun", "40 kun", "1 yil", "72 kun.")
t.B("Jadidlar qaysi yillarda qatag‘on qurboni bo‘lgan?", "1937–1938-yillarda", "1917–1918-yillarda", "1916-yilda", "1924-yilda", "1937–1938-yillarda.")
t.B("Biror hududning qonun bilan chegaralangan hokimiyatni mustaqil amalga oshirish huquqi qanday ataladi?", "avtonomiya", "federatsiya", "protektorat", "absolyutizm", "Avtonomiya.")
t.NAT("Jadidlar yer, suv va boyliklarni xalq boyligi deb e’lon qilish, mahalliy kadrlar tayyorlashni zarur deb bildi.", "ular iqtisodiy mustaqilliksiz siyosiy erkinlikka erishib bo‘lmaydi, degan xulosaga keldi", "ular sanoatni rad etdi", "ular Rossiyaga bo‘ysunishni yoqladi", "ular dehqonchilikni taqiqladi", "Iqtisodiy mustaqillik siyosiy erkinlik sharti deb bilingan.")
t.NAT("1917-yildagi oktabr voqealarida bolsheviklar hokimiyatni egalladi.", "jadidlar maqsadlarini oxirigacha amalga oshira olmadi", "Turkiston mustaqil davlatga aylandi", "jadidlar hukumat tuzdi", "xonliklar tiklandi", "Bu jadidlarning maqsadlarini amalga oshirishga imkon bermadi.")
t.TF("Jadidlar barcha muammolarni tinch yo‘l bilan hal etishga intilgan.", True, "To‘g‘ri: ular qonli to‘qnashuvlarga qarshi edi.")
t.TF("Jadidlar islomning asosiy ta’limotini o‘zgartirishga intilgan.", False, "Noto‘g‘ri: ular islomga sodiq bo‘lib, uni to‘g‘ri talqin qilgan.")
t.MUL([("Jadidlar fanga salbiy munosabatdagi ruhoniylarni qoralagan.", True),
       ("«Musulmon markaziy sho‘rosi» syezdida ozarbayjon, tatar, turkman, boshqird vakillari ham bo‘lgan.", True),
       ("Turkiston muxtoriyati sovet hokimiyati tomonidan tan olingan.", False)],
      "III noto‘g‘ri: u sovet hokimiyati tomonidan tor-mor etilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Behbudiyning islom tarixiga oid asari", "Avloniyning islom tarixiga oid asari", "Fitratning islom tarixiga oid asari", "«Musulmon markaziy sho‘rosi» tuzildi", "Jadidlarning qatag‘on qilinishi"],
      "1909 → 1910 → 1915 → 1917 → 1937–1938.")
t.MAPN(UZ, ['Toshkent', 'Samarqand', 'Qo‘qon', 'Buxoro'], "Qaysi raqam bilan 72 kun yashagan Turkiston muxtoriyatining markazi belgilangan?",
       "3 – Qo‘qon; 1 – Toshkent: «Musulmon markaziy sho‘rosi» tuzilgan.", ask_idx=2)
t.VENN("«Musulmon markaziy sho‘rosi»", "Turkiston muxtoriyati",
       [("1917-yil mart boshida Toshkentda tuzilgan", 1), ("ta’sis syezdida 350 delegat", 1),
        ("markazi Qo‘qon", 2), ("72 kun yashagan", 2),
        ("jadidlar tomonidan tashkil etilgan", 3)],
       "Sho‘ro — Toshkent, 350 delegat; muxtoriyat — Qo‘qon, 72 kun; ikkalasi jadidlar tashkilotlari.")

# 29 Birinchi jahon urushi va Turkiston
t = Topic('e9u29', 9029); TOPICS['e9u29'] = t
t.B("Birinchi jahon urushida Rossiya qaysi ittifoq tomonida qatnashgan?", "Antanta", "Uchlar ittifoqi", "Muqaddas ittifoq", "Shimoliy ittifoq", "Rossiya, Angliya, Fransiya — Antanta.")
t.B("Antanta qaysi davlatlardan iborat bo‘lgan?", "Rossiya, Angliya, Fransiya", "Germaniya, Avstriya-Vengriya, Italiya", "Rossiya, Germaniya, Yaponiya", "AQSH, Angliya, Italiya", "Rossiya, Angliya va Fransiya.")
t.B("Turkistondan urushga qaysi yoshdagi yevropalik aholi chaqirilgan?", "19 yoshdan 43 yoshgacha", "18 yoshdan 30 yoshgacha", "21 yoshdan 50 yoshgacha", "16 yoshdan 60 yoshgacha", "19 yoshdan 43 yoshgacha.")
t.B("1914-yilda Turkistonda qanday holat e’lon qilingan?", "«favqulodda muhofaza holati»", "«harbiy-xalq boshqaruvi»", "«mirshablik holati»", "«tinchlik holati»", "«Favqulodda muhofaza holati».")
t.B("«Favqulodda holat» tartiblarini buzganlar qancha jarima to‘lagan?", "50 so‘mgacha", "100 rubl", "5 so‘m", "1000 so‘m", "50 so‘mgacha jarima yoki 3 oygacha qamoq.")
t.B("Urushning bir yili davomida soliqlar miqdori qancha ko‘paygan?", "50 foizga", "10 foizga", "2 baravar", "5 foizga", "50 foizga.")
t.B("Turkistonda paxtaga o‘zgarmas davlat narxlari qachondan joriy etilgan?", "1915-yildan", "1914-yildan", "1916-yildan", "1911-yildan", "1915-yildan.")
t.B("Front ortidagi ishlarga safarbarlik haqidagi farmon qachon chiqarilgan?", "1916-yil 25-iyunda", "1914-yil avgustda", "1915-yilda", "1917-yil fevralda", "1916-yil 25-iyunda.")
t.B("1916-yil 25-iyun farmonini qaysi imperator chiqargan?", "Nikolay II", "Aleksandr III", "Aleksandr II", "Pyotr I", "Nikolay II (1894–1917).")
t.B("Farmonga ko‘ra qaysi hududlardan erkaklar safarbar qilingan?", "Turkiston, Sibir va Kavkaz", "faqat Turkiston", "Polsha va Finlyandiya", "Ukraina va Belorussiya", "Turkiston, Sibir va Kavkazdan.")
t.B("Front ortidagi ishlarga qaysi yoshdagi erkaklar safarbar qilingan?", "19 yoshdan 43 yoshgacha", "18 yoshdan 25 yoshgacha", "25 yoshdan 50 yoshgacha", "16 yoshdan 40 yoshgacha", "19 yoshdan 43 yoshgacha.")
t.NAT("Yevropalik erkaklarni urushga chaqirish hosil yig‘ish vaqtiga to‘g‘ri keldi.", "ko‘chirib keltirilganlarning oilalari qiyin ahvolga tushdi", "hosil ko‘paydi", "narxlar tushdi", "soliqlar kamaydi", "Oilalar asosiy boquvchisidan ajraldi.")
t.NAT("Paxtaga o‘zgarmas davlat narxlari joriy etildi.", "bu narx paxtakorlarning xarajatlarini qoplay olmadi", "paxtakorlar boyidi", "paxta eksporti to‘xtadi", "g‘alla narxi tushdi", "Narxlar umumiy o‘sishi sharoitida xarajat qoplanmadi.")
t.NAT("Rossiyaga talafotlar o‘rnini to‘ldirish va harbiy xarajatlarni qoplash kerak bo‘ldi.", "xarajatlarning katta qismi mustamlakalar, jumladan, Turkiston gardaniga yuklandi", "Rossiya urushdan chiqdi", "mustamlakalarga yordam berildi", "soliqlar bekor qilindi", "Chor hukumati mustamlaka o‘lkalarini talash yo‘lidan bordi.")
t.TF("Urush davomida maorif va madaniyatga xarajatlar kamayib ketdi.", True, "To‘g‘ri.")
t.TF("Urush yillarida Turkistonda qishloq xo‘jaligi gullab-yashnadi.", False, "Noto‘g‘ri: qishloq xo‘jaligi vayron bo‘ldi, ekin maydonlari qisqardi.")
t.MUL([("Urush tufayli Rossiyada ommaviy safarbarlik e’lon qilindi.", True),
       ("Temiryo‘l amalda harbiy davr yuklarini tashigan.", True),
       ("Rossiya iqtisodiyoti urushga kuchli tayyor ekani ayon bo‘ldi.", False)],
      "III noto‘g‘ri: Rossiya iqtisodiyoti bunday urush uchun zaif ekanligi ayon bo‘ldi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Turkistonda «favqulodda muhofaza holati» e’lon qilindi", "Paxtaga o‘zgarmas davlat narxlari joriy etildi", "Nikolay II ning mardikorlik haqidagi farmoni"],
      "1914 → 1915 → 1916-yil 25-iyun.")
t.VENN("1914-yilgi safarbarlik", "1916-yil 25-iyun farmoni",
       [("yevropalik aholi frontga chaqirilgan", 1), ("hosil yig‘ish vaqtiga to‘g‘ri kelgan", 1),
        ("tub aholi front ortidagi ishlarga olingan", 2), ("Turkiston, Sibir va Kavkazdan erkaklar", 2),
        ("19 yoshdan 43 yoshgacha bo‘lganlar", 3)],
       "1914 — yevropaliklar frontga; 1916 — tub aholi front ortiga; ikkalasida 19–43 yosh.")
