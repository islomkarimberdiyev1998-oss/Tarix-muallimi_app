from qlib import Topic, PLACES, REG
TOPICS = {}

# 8-mavzu. Ijtimoiy siyosat
t = Topic('y11u8', 11008); TOPICS['y11u8'] = t
t.B("1991-yilda O‘zbekiston aholisi qancha bo‘lgan?", "20,6 million", "37,1 million", "32 million", "11,5 million", "20,6 million.")
t.B("2024-yil 1-iyul holatiga O‘zbekiston doimiy aholisi qancha?", "37 million 134 ming 200", "32 million", "20,6 million", "18,9 million", "37 134 200 kishi.")
t.B("Mustaqillik arafasida kishi boshiga yalpi ijtimoiy mahsulot bo‘yicha O‘zbekiston 15 respublika ichida nechanchi o‘rinda edi?", "12-o‘rinda", "1-o‘rinda", "5-o‘rinda", "15-o‘rinda", "12-o‘rinda.")
t.B("1991–2016-yillarda aholi taxminan qanchaga ko‘paygan?", "11,5 million kishiga", "5 million kishiga", "20 million kishiga", "1 million kishiga", "11,5 million.")
t.B("Qonunga ko‘ra yoshlar necha yoshdagi shaxslar?", "14 yoshga to‘lgan va 30 yoshdan oshmagan", "18–35 yosh", "16–25 yosh", "12–28 yosh", "14–30 yosh.")
t.B("«Ijtimoiy himoya yagona reestri» qachon joriy etilgan?", "2022-yilga kelib", "2017-yilda", "2007-yilda", "2024-yilda", "2022-yilga kelib.")
t.B("Ijtimoiy himoya milliy agentligi qachon tashkil etilgan?", "2023-yilda", "2022-yilda", "2017-yilda", "1996-yilda", "2023-yilda.")
t.B("Har bir tuman va shaharda qanday ijtimoiy xizmatlar markazlari ochilgan?", "«Inson»", "«Mehr»", "«Saxovat»", "«Yuksalish»", "«Inson» markazlari.")
t.B("2024-yildan haftaning qaysi kuni «Mehr va saxovat kuni» deb belgilangan?", "juma", "dushanba", "shanba", "yakshanba", "Juma.")
t.B("Kambag‘allik darajasi necha foizdan necha foizgacha qisqartirilgan?", "35 dan 6,6 foizgacha", "50 dan 20 foizgacha", "20 dan 10 foizgacha", "12 dan 3 foizgacha", "35% dan 6,6% gacha.")
t.B("«Fuqarolar sog‘lig‘ini saqlash to‘g‘risida»gi qonun qachon qabul qilingan?", "1996-yilda", "2001-yilda", "1991-yilda", "2021-yilda", "1996-yilda.")
t.B("1990-yilda o‘rtacha umr ko‘rish davomiyligi qancha bo‘lgan?", "67 yosh atrofida", "74 yosh", "60 yosh", "80 yosh", "67 yosh atrofida.")
t.B("Gematologiya va bolalar onkologiyasi markazlari alohida muassasa sifatida qachon tashkil etilgan?", "2021-yilda", "2001-yilda", "2017-yilda", "2024-yilda", "2021-yilda.")
t.B("Shoshilinch tibbiy yordam brigadalari soni nechtagacha ko‘paytirilgan?", "1666 tagacha", "818 tagacha", "1500 tagacha", "5300 tagacha", "818 tadan 1666 tagacha.")
t.B("Tibbiy kadrlar tayyorlash uchun nechta xorijiy universitet bilan hamkorlik boshlangan?", "22 ta", "16 ta", "100 ta", "14 ta", "22 ta universitet.")
t.B("Bandlikka ko‘maklashish markazlari qachondan tashkil qilingan?", "2007-yildan", "1996-yildan", "2017-yildan", "2023-yildan", "2007-yildan.")
t.NAT("1990-yillar oxirida byudjet kamomadi yuzaga keldi.", "ta’lim, tibbiyot va ijtimoiy himoya sohalariga salbiy ta’sir ko‘rsatdi", "maoshlar keskin oshdi", "pensiyalar ikki baravar ko‘paydi", "byudjet profitsiti yuzaga keldi", "Ijtimoiy sohalarga salbiy ta’sir.")
t.NAT("Oilaviy tadbirkorlik va YaTT faoliyati rivojlantirildi, byurokratik to‘siqlar bekor qilindi.", "kambag‘allik darajasi 35 foizdan 6,6 foizgacha qisqardi", "ishsizlik oshdi", "kambag‘allik ko‘paydi", "tadbirkorlar kamaydi", "Kambag‘allik qisqardi.")
t.NAT("Sog‘liqni saqlash sohasida islohotlar o‘tkazildi.", "o‘rtacha umr ko‘rish 67 yoshdan 2023-yilda 74 yoshga yaqinlashdi", "umr ko‘rish qisqardi", "kasalxonalar yopildi", "tibbiyot pullik bo‘ldi", "Umr ko‘rish oshdi.")
t.NAT("Kam ta’minlangan oilalarni aniqlash uchun yagona reestr joriy etildi.", "ehtiyojmand oilalarga manzilli yordam ko‘rsatish boshlandi", "yordam to‘xtatildi", "barchaga bir xil yordam berildi", "mahallalar tugatildi", "Manzilli yordam.")
t.TF("«Temir daftar», «Ayollar daftari», «Yoshlar daftari» ijtimoiy masalalarni hal etishga xizmat qilmoqda.", True, "To‘g‘ri.")
t.TF("Sovet davrida O‘zbekiston aholisi go‘sht va sutni Ittifoq o‘rtachasidan ikki baravar ko‘p iste’mol qilgan.", False, "Noto‘g‘ri: ikki barobar kam iste’mol qilgan.")
t.TF4([("2001-yilda 1700 ta xususiy tibbiyot muassasasi ruxsat olgan.", True), ("O‘zbekistonda ilk bor allogen transplantatsiya amaliyoti yo‘lga qo‘yilgan.", True),
       ("1500 dan ortiq tez yordam mashinasi xarid qilingan.", True), ("O‘qituvchilar maoshi o‘rtacha daromaddan ikki baravar yuqori bo‘lgan.", False)],
      "4-noto‘g‘ri: o‘rtacha daromadning 60–65 foizini tashkil qilgan.")
t.MUL([("Ijtimoiy siyosat bosqichma-bosqich amalga oshiriladi.", True),
       ("Mahalliy o‘zini o‘zi boshqarish idoralari orqali manzilli yordam ko‘rsatiladi.", True),
       ("Shahar aholisi qishloq aholisidan ancha kam.", False)],
      "III noto‘g‘ri: shahar aholisi 18,9 mln, qishloq – 18,2 mln.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["sog‘liqni saqlash qonuni", "1700 xususiy tibbiyot muassasasi", "Bandlik markazlari", "gematologiya markazi alohida", "Ijtimoiy himoya yagona reestri", "Ijtimoiy himoya milliy agentligi"],
      "1996 → 2001 → 2007 → 2021 → 2022 → 2023.")
t.MATCH("Atamalarni izohi bilan moslashtiring.", ["yoshlar", "yosh oila", "YaTT", "«Inson» markazlari"],
        ["14–30 yoshdagi shaxslar", "er-xotin 30 yoshdan oshmagan oila", "yakka tartibdagi tadbirkorlik", "tuman va shahardagi ijtimoiy xizmatlar markazi", "manzilli yordam reestri"], 'abcd',
        "Yoshlar – 14–30; yosh oila – 30 yoshgacha; YaTT – yakka tadbirkorlik; «Inson» – ijtimoiy markaz.")
t.VENN("Ijtimoiy himoya", "Sog‘liqni saqlash",
       [("«Inson» ijtimoiy xizmatlar markazlari", 1), ("«Ijtimoiy himoya yagona reestri»", 1),
        ("shoshilinch yordam brigadalari 1666 ta", 2), ("skrining markazlari", 2),
        ("ijtimoiy siyosatning ustuvor yo‘nalishi", 3)],
       "Himoya – Inson markazlari, reestr; sog‘liq – brigadalar, skrining; ikkalasi ijtimoiy siyosat.")
t.MAPN('uzb', ['Toshkent', 'Nukus', 'Termiz', 'Andijon'], "Ijtimoiy himoya milliy agentligi faoliyat yuritadigan O‘zbekiston poytaxti xaritada qaysi raqamda?",
       "Toshkent.")

# 9-mavzu. Millatlararo totuvlik va diniy bag‘rikenglik
t = Topic('y11u9', 11009); TOPICS['y11u9'] = t
t.B("O‘zbekistonda nechtadan ortiq millat va elat vakillari yashaydi?", "130 dan", "13 dan", "1300 dan", "50 dan", "130 dan ortiq.")
t.B("Respublika Baynalmilal madaniyat markazi qachon tashkil etilgan?", "1992-yilda", "1990-yilda", "2006-yilda", "2017-yilda", "1992-yilda.")
t.B("Bugungi kunda nechtadan ortiq milliy-madaniy markaz mavjud?", "150 dan", "10 dan", "40 dan", "1500 dan", "150 dan ortiq (dastlab 10 ta).")
t.B("Turli millatlar bayramlari haqida yoritadigan jurnal qaysi?", "«Yagona oilada»", "«Ziyo»", "«Vaqf»", "«Do‘stlik»", "«Yagona oilada».")
t.B("Tatar va boshqirdlarning bayrami qaysi?", "«Sabanto‘y»", "«Maslennitsa»", "«Sayil»", "«Chunjie»", "«Sabanto‘y».")
t.B("Uyg‘urlarning bayrami qaysi?", "«Sayil»", "«Soller»", "«Sabanto‘y»", "«Maslennitsa»", "«Sayil».")
t.B("2025-yilga kelib do‘stlik jamiyatlari soni nechtadan oshgan?", "40 dan", "150 dan", "10 dan", "130 dan", "40 dan oshgan.")
t.B("Millatlararo totuvlik va bag‘rikenglik ilmiy markazi kimning tashabbusi bilan tashkil etilgan?", "professor Rahbarxon Murtazayeva", "Sh. Mirziyoyev", "I. Karimov", "Abdulla Oripov", "Rahbarxon Murtazayeva, 2006-yil.")
t.B("Bag‘rikenglik tamoyillari deklaratsiyasi qachon qabul qilingan?", "1995-yil 16-noyabrda", "1992-yilda", "2017-yilda", "2006-yilda", "1995-yil 16-noyabr, YUNESKO.")
t.B("Xalqaro bag‘rikenglik kuni qaysi sana?", "16-noyabr", "1-sentyabr", "8-dekabr", "21-mart", "16-noyabr.")
t.B("Din ishlari bo‘yicha qo‘mita qachon tashkil etilgan?", "1992-yilda", "1990-yilda", "2018-yilda", "1995-yilda", "1992-yilda.")
t.B("«Ma’rifat va diniy bag‘rikenglik» rezolyutsiyasi BMT tomonidan qachon qabul qilingan?", "2018-yilda", "2017-yilda", "2020-yilda", "1995-yilda", "2017-yilda taklif qilingan, 2018-yilda yakdillik bilan qabul qilingan.")
t.B("O‘zbekiston xalqaro islom akademiyasi 2025-yildan qanday nomlandi?", "O‘zbekiston xalqaro islomshunoslik akademiyasi", "Toshkent islom universiteti", "Imom Buxoriy markazi", "Mir Arab akademiyasi", "Xalqaro islomshunoslik akademiyasi.")
t.B("Masjidlarning umumiy soni nechtaga yetdi?", "2066 taga", "206 taga", "20 mingtaga", "150 taga", "2066 ta.")
t.B("Imom Moturidiy xalqaro ilmiy-tadqiqot markazi qachon tashkil etilgan?", "2020-yilda", "2018-yilda", "2006-yilda", "2025-yilda", "2020-yilda.")
t.B("Abu Muin Nasafiyning qaysi kitobi o‘zbek tilida nashr etilgan?", "«Tabsiratul adilla»", "«Al-Jome as-sahih»", "«Shamoili Muhammadiya»", "«Ta’vilot»", "«Tabsiratul adilla».")
t.B("2025-yilda qaysi shaharga Islom madaniyati poytaxti maqomi berilgan?", "Samarqand", "Buxoro", "Toshkent", "Termiz", "Samarqand.")
t.NAT("1990-yilda musulmonlar haj ziyoratiga imkon oldi, hayitlar dam olish kuni deb e’lon qilindi.", "diniy e’tiqodga hurmat tiklandi", "dinga qarshi kurash kuchaydi", "masjidlar yopildi", "haj taqiqlandi", "Diniy erkinlik.")
t.NAT("Qur’oni karim, Imom Buxoriy va Imom Termiziy to‘plamlari o‘zbek tiliga tarjima qilindi.", "yoshlar va jamoatchilik diniy bilimlarni chuqurroq tushuna boshladi", "diniy kitoblar taqiqlandi", "faqat arab tilida qoldi", "kitoblar yo‘q qilindi", "Diniy bilim oshdi.")
t.NAT("2019-yildan Umra ziyoratchilari soni bo‘yicha cheklovlar olib tashlandi.", "fuqarolar uchun ziyorat imkoniyati kengaydi", "ziyorat taqiqlandi", "cheklovlar kuchaydi", "faqat ruhoniylar bordi", "Ziyorat erkinlashdi.")
t.NAT("Viloyatlar va Toshkentda «Do‘stlik uylari» tashkil etildi.", "milliy madaniy markazlar faoliyat yuritib, davlat tomonidan qo‘llab-quvvatlanmoqda", "markazlar yopildi", "millatlar ajratildi", "bayramlar taqiqlandi", "Markazlar qo‘llab-quvvatlanmoqda.")
t.TF("O‘zbekistonda gazetalar o‘zbek, rus, qoraqalpoq, tojik, qozoq, turkman, ingliz va koreys tillarida chiqadi.", True, "To‘g‘ri.")
t.TF("O‘zbekistonda diniy qarashlarni majburan singdirishga yo‘l qo‘yiladi.", False, "Noto‘g‘ri: vijdon erkinligi kafolatlangan, majburlashga yo‘l qo‘yilmaydi.")
t.TF4([("Termizda Imom Termiziy nomidagi islom instituti faoliyat yuritadi.", True), ("Toshkentda pravoslav va xristian seminariyalari bor.", True),
       ("Koreyslarning «Soller» va «Ovol-tano» bayramlari bor.", True), ("Millatlararo totuvlik ilmiy markazi Samarqand universitetida tashkil etilgan.", False)],
      "4-noto‘g‘ri: O‘zbekiston Milliy universitetida tashkil etilgan.")
t.MUL([("«Ziyo» media markazi va «Vaqf» xayriya fondi tashkil etilgan.", True),
       ("«Jaholatga qarshi – ma’rifat» tamoyili asosida yoshlar tarbiyalanmoqda.", True),
       ("Rezolyutsiya BMTda ko‘pchilik ovoz bilan, qarshilik bilan qabul qilingan.", False)],
      "III noto‘g‘ri: barcha a’zo davlatlar tomonidan yakdillik bilan qabul qilingan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["haj ziyorati imkoni, hayitlar bayram qilindi", "Din ishlari qo‘mitasi tuzildi", "Bag‘rikenglik deklaratsiyasi (YUNESKO)", "totuvlik ilmiy markazi", "«Ma’rifat va diniy bag‘rikenglik» rezolyutsiyasi qabul qilindi", "Imom Moturidiy markazi"],
      "1990 → 1992 → 1995 → 2006 → 2018 → 2020.")
t.MATCH("Bayramlarni xalq bilan moslashtiring.", ["«Maslennitsa»", "«Sabanto‘y»", "«Sayil»", "«Chunjie»"],
        ["ruslar", "tatar va boshqirdlar", "uyg‘urlar", "xitoylar", "koreyslar"], 'abcd',
        "Maslennitsa – ruslar; Sabanto‘y – tatar-boshqirdlar; Sayil – uyg‘urlar; Chunjie – xitoylar.")
t.VENN("Millatlararo totuvlik", "Diniy bag‘rikenglik",
       [("150 dan ortiq milliy-madaniy markaz", 1), ("«Do‘stlik uylari»", 1),
        ("2066 ta masjid", 2), ("«Ma’rifat va diniy bag‘rikenglik» rezolyutsiyasi", 2),
        ("Konstitutsiya va qonunlar bilan kafolatlangan", 3)],
       "Totuvlik – markazlar; bag‘rikenglik – masjidlar, rezolyutsiya; ikkalasi qonun bilan kafolatlangan.")
t.MAPMATCH('uzb', ['Buxoro', 'Termiz', 'Namangan', 'Samarqand'],
           ["Mir Arab madrasasi va Bahouddin Naqshband ziyoratgohi shahri", "Imom Termiziy nomidagi islom instituti joylashgan shahar", "Sulton Uvays Qaraniy ziyoratgohi ta’mirlangan shahar", "2025-yilda Islom madaniyati poytaxti maqomini olgan shahar"],
           "1 – Buxoro; 2 – Termiz; 3 – Namangan; 4 – Samarqand.")

# 10-mavzu. Ta’lim tizimidagi islohotlar
t = Topic('y11u10', 11010); TOPICS['y11u10'] = t
t.B("«Ta’lim to‘g‘risida»gi qonun qachon qabul qilingan?", "1992-yil 2-iyulda", "1997-yil 29-avgustda", "2017-yilda", "1991-yilda", "1992-yil 2-iyul.")
t.B("Kadrlar tayyorlash milliy dasturi qachon qabul qilingan?", "1997-yil 29-avgustda", "1992-yil 2-iyulda", "2001-yilda", "2017-yilda", "1997-yil 29-avgust.")
t.B("Kadrlar tayyorlash milliy dasturiga ko‘ra qanday majburiy ta’lim tizimi yo‘lga qo‘yilgan?", "9+3", "11 yillik", "12 yillik", "8+4", "9+3 tizimi.")
t.B("To‘liq 11 yillik ta’limga qachon o‘tilgan?", "2017-yilda", "1997-yilda", "2020-yilda", "2023-yilda", "2017-yilda.")
t.B("Milliy test tizimi qachondan joriy etila boshlagan?", "2020-yildan", "2017-yildan", "2023-yildan", "1997-yildan", "2020-yildan.")
t.B("Maktabgacha va maktab ta’limi vazirligi qachon tashkil etilgan?", "2023-yilda", "2017-yilda", "2019-yilda", "1992-yilda", "2023-yilda.")
t.B("2024-yilda bolalarni bog‘chaga qamrab olish darajasi qanchaga yetgan?", "76 foiz", "74 foiz", "34,6 foiz", "100 foiz", "76 foiz (2023-yilda 74 foiz).")
t.B("Prezident maktablarini tashkil etish haqida qaror qachon qabul qilingan?", "2019-yil 20-fevralda", "2017-yilda", "2020-yilda", "2023-yilda", "2019-yil 20-fevral.")
t.B("Prezident maktablariga o‘quvchilar necha sinfdan keyin tanlanadi?", "4-sinfni tugatgach", "9-sinfdan keyin", "1-sinfdan", "7-sinfdan keyin", "4-sinfni tugatgan o‘quvchilar.")
t.B("2018/2019-o‘quv yilida xususiy maktablarda nechtadan ortiq o‘quvchi o‘qigan?", "13 mingdan", "130 mingdan", "1,3 mingdan", "1 milliondan", "13 mingdan ortiq.")
t.B("2016-yilda bitiruvchilarning qancha qismi oliy ta’limda o‘qishni davom ettirish imkoniga ega edi?", "9 foizga yaqin", "50 foiz", "25 foiz", "76 foiz", "9 foizga yaqin.")
t.B("2025-yilda oliy ta’lim muassasalari soni nechtaga yetgan?", "202 taga", "53 taga", "23 taga", "100 taga", "202 taga.")
t.B("2025-yilda nechta OTM QS reytingining Markaziy Osiyo ro‘yxatidan o‘rin olgan?", "23 ta", "53 ta", "7 ta", "10 ta", "23 ta.")
t.B("THE Impact Rankings 2024 bo‘yicha nechta OTM global reytingga kiritilgan?", "53 ta", "23 ta", "202 ta", "10 ta", "53 ta (7 tasi 1000 talikda).")
t.B("O‘zbekistonda magistratura bosqichi necha yillik?", "2 yillik", "1 yillik", "3 yillik", "4 yillik", "2 yillik.")
t.B("«O‘zbekiston – 2030»da kamida nechta qo‘shma ta’lim dasturi asosida ikki diplomli tizim belgilangan?", "50 ta", "10 ta", "100 ta", "23 ta", "Kamida 50 ta.")
t.NAT("Bog‘chalar soni yetarli emas edi.", "xususiy sektor va oilaviy bog‘chalar faoliyati kengaytirildi", "bog‘chalar yopildi", "bolalar maktabga erta yuborildi", "qamrov kamaydi", "Xususiy sektor kengaydi.")
t.NAT("Kasb-hunar kollejlari bitiruvchilarining ish bilan ta’minlanishida muammolar yuzaga keldi.", "9+3 tizimidan to‘liq 11 yillik ta’limga o‘tildi", "kollejlar ko‘paytirildi", "maktablar yopildi", "oliy ta’lim bekor qilindi", "11 yillik ta’lim.")
t.NAT("2019-yildan xususiy maktablar uchun soliq imtiyozlari berildi.", "xususiy maktablar tashkil etish va davlat-xususiy sheriklik kengaydi", "xususiy maktablar taqiqlandi", "o‘quvchilar kamaydi", "davlat maktablari yopildi", "Xususiy maktablar ko‘paydi.")
t.NAT("2016-yildan oliy ta’limda tub islohotlar boshlandi.", "2019-yilda qabul parametrlari 2016-yilga nisbatan 2,5 barobar o‘sdi", "qabul qisqardi", "OTMlar yopildi", "xorijiy filiallar yopildi", "Qabul oshdi.")
t.TF("Maktabgacha ta’lim xodimlarining oliy ma’lumotlilar ulushi 34,6 foizga yetkazilgan.", True, "To‘g‘ri.")
t.TF("Prezident maktablari dastlab barcha viloyatlarda bir vaqtda ochilgan.", False, "Noto‘g‘ri: dastlab Toshkent, Namangan, Xiva va Nukusda ochilgan.")
t.TF4([("Kadrlar tayyorlash dasturining birinchi bosqichi 1997–2001-yillar.", True), ("Ijod maktablari Abdulla Qodiriy, Zulfiya, Erkin Vohidov nomlari bilan ochilgan.", True),
       ("Ixtisoslashtirilgan maktablarda O‘zbekiston tarixi chuqurlashtirib o‘qitiladi.", True), ("O‘zbekistonda oilaviy bog‘chalar ochishga ruxsat berilmagan.", False)],
      "4-noto‘g‘ri: nodavlat muassasalar doirasida oilaviy bog‘chalarga ruxsat berilgan.")
t.MUL([("Mirzo Ulug‘bek va al-Xorazmiy nomidagi ixtisoslashtirilgan maktablar tashkil etilgan.", True),
       ("10 ta OTMni eng nufuzli 1000 ta universitet ro‘yxatiga kiritish rejalashtirilgan.", True),
       ("2017-yilda 11 yillik ta’limdan 9+3 tizimiga o‘tilgan.", False)],
      "III noto‘g‘ri: 9+3 dan to‘liq 11 yillik ta’limga o‘tilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["«Ta’lim to‘g‘risida»gi qonun", "Kadrlar tayyorlash milliy dasturi", "11 yillik ta’limga o‘tish", "Prezident maktablari to‘g‘risida qaror", "milliy test tizimi", "Maktabgacha va maktab ta’limi vazirligi"],
      "1992 → 1997 → 2017 → 2019 → 2020 → 2023.")
t.MATCH("Raqamlarni ma’nosi bilan moslashtiring.", ["202", "53", "23", "76 %"],
        ["2025-yildagi OTMlar soni", "THE reytingiga kirgan OTMlar", "QS Markaziy Osiyo ro‘yxatidagi OTMlar", "2024-yilda bog‘cha qamrovi", "kollejlar soni"], 'abcd',
        "202 – OTMlar; 53 – THE; 23 – QS; 76% – bog‘cha qamrovi.")
t.VENN("9+3 tizimi", "11 yillik ta’lim",
       [("1997-yil Kadrlar tayyorlash dasturi", 1), ("kasb-hunar kollejlari va akademik litseylar", 1),
        ("2017-yildan joriy etildi", 2), ("Prezident tashabbusi bilan", 2),
        ("majburiy ta’lim tizimi", 3)],
       "9+3 – 1997, kollejlar; 11 yillik – 2017; ikkalasi majburiy ta’lim.")
t.MAPN('uzb', ['Nukus', 'Termiz', 'Buxoro', 'Samarqand'], "2019-yilda dastlabki Prezident maktablari ochilgan shaharlardan biri xaritada qaysi raqamda?",
       "Nukus (shuningdek Toshkent, Namangan, Xiva).")
