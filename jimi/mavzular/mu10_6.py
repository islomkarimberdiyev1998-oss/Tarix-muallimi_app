from qlib import Topic, PLACES, REG
TOPICS = {}
CA = 'ca'
REG['ww2'] = [6, 42, 50, 61.5]
PLACES.update({'Bekobod': (69.27, 40.22), 'Gdansk': (18.65, 54.35), 'Guliston (Mirzacho‘l)': (68.78, 40.49), 'Farg‘ona shahri': (71.78, 40.38)})

# 17-§. Sanoat va qishloq xo‘jaligi front xizmatida
t = Topic('e10u17', 10117); TOPICS['e10u17'] = t
t.B("1941-yil dekabriga kelib respublikadagi nechta sanoat korxonasi mudofaa mahsulotlarini ishlab chiqara boshladi?", "230 ta", "63 ta", "100 dan ortiq", "308 ta", "Toshkentdagi 63 ta, respublikadagi 230 ta korxona.")
t.B("Harbiy korxonalardan o‘zboshimchalik bilan ketib qolganlarga qanday jazo belgilandi?", "5 yildan 8 yilgacha qamoq", "1 yilgacha qamoq", "jarima", "10 yilgacha surgun", "5 yildan 8 yilgacha qamoq jazosi.")
t.B("1943-yilda sanoatning respublika xalq xo‘jaligidagi salmog‘i necha foizgacha ortdi?", "75 foizgacha", "62,6 foizgacha", "37,4 foizgacha", "90 foizgacha", "75 foizgacha.")
t.B("Urush yillarida O‘zbekistonda nechta yirik GES qurildi?", "7 ta", "4 ta", "10 ta", "3 ta", "Oqqovoq, Qibray, Salor, Farhod va boshqalar – 7 ta.")
t.B("O‘rta Osiyodagi dastlabki zamonaviy metallurgiya kombinati qayerda ishga tushirildi?", "Bekobodda", "Toshkentda", "Chirchiqda", "Olmaliqda", "1944-yil martda Bekobodda.")
t.B("O‘zbekiston frontga nechadan ortiq samolyot yetkazib berdi?", "2000 dan ortiq", "500 dan ortiq", "22 000", "10 000", "2000 dan ortiq samolyot.")
t.B("1941-yili davlatga qancha paxta topshirildi?", "1,6 mln tonnadan ziyod", "4 mln tonna", "82 mln pud", "1,5 mln sentner", "1,6 mln tonnadan ziyod.")
t.B("1942-yil bahorida qancha qo‘shimcha yer o‘zlashtirildi?", "220 500 gektar", "160 000 gektar", "779 000 gektar", "1,5 mln gektar", "220 500 gektar.")
t.B("Urush yillarida O‘zbekiston butun mamlakatdagi qandning qancha qismini berardi?", "chorak qismini", "yarmini", "uchdan bir qismini", "o‘ndan bir qismini", "Chorak qismini.")
t.B("Urush yillarida qishloq xo‘jaligi ahli qancha paxta xomashyosi yetkazib berdi?", "4 mln tonnadan ziyod", "1,6 mln tonna", "82 mln tonna", "1,5 mln tonna", "4 mln tonnadan ziyod paxta va 82 mln pud don.")
t.B("Shaharlarda kartochka tizimida ishchi va xizmatchilarga kuniga qancha non berildi?", "400 – 500 gramm", "300 – 400 gramm", "200 gramm", "1 kg", "Ishchi va xizmatchilarga 400 – 500 g, oila a’zolariga 300 – 400 g.")
t.B("Kolxozlarda majburiy ish kuni normasi necha marta oshirildi?", "1,5 marta", "2 marta", "3 marta", "1,2 marta", "Kattalar va 12 yoshdan oshgan bolalar uchun 1,5 marta.")
t.B("O‘zbekistonga nechta bola evakuatsiya qilindi?", "200 000", "1 mln", "15 000", "30 000", "1 mln dan ortiq kishi, jumladan 200 000 bola.")
t.B("Toshkentlik temirchi Shoahmad Shomahmudov oilasi nechta bolani tarbiyaga oldi?", "15 ta", "13 ta", "10 ta", "20 ta", "15 bola; Hamid Samadov – 13, Fotima Qosimova – 10.")
t.B("Respublikaga urush davrida nechadan ortiq harbiy gospital joylashtirildi?", "30 dan ortiq", "100 dan ortiq", "10 ta", "63 ta", "30 dan ortiq gospital.")
t.B("Qrimdan O‘zSSRga nechta qrim tatari ko‘chirildi?", "151 604 nafar", "110 000 nafar", "175 000 nafar", "20 000 nafar", "151 604 nafar.")
t.B("Gruziyadan O‘zSSRga qaysi xalq vakillari ko‘chirildi?", "mesxeti turklari", "chechenlar", "bolqorlar", "ingushlar", "Gruziyadan 110 000 nafar mesxeti turklari.")
t.B("Qand lavlagini qayta ishlovchi qaysi zavod urush yillarida qurildi?", "Zirabuloq qand zavodi", "Bekobod metallurgiya zavodi", "Toshkent aviatsiya zavodi", "Chirchiq kimyo kombinati", "Zirabuloq, Krasnogvardeysk, Qo‘qon, Yangiyo‘l qand zavodlari.")
t.NAT("1941-yil 14-dekabrdan harbiy korxonalar xodimlari urushga safarbar qilinganlar qatoriga qo‘shildi.", "mehnat intizomini buzganlar qattiq jazolanadigan bo‘ldi", "ish kuni qisqartirildi", "xodimlar frontga jo‘natildi", "ish haqi ikki baravar oshirildi", "Intizom buzilganda qattiq jazo, ketib qolganlarga 5 – 8 yil qamoq.")
t.NAT("1943 – 1944-yillarda totalitar tuzum rahbarlari farmoyishi bilan Kavkaz xalqlari, qrim tatarlari, Volgabo‘yi nemislari ko‘chirildi.", "ularning katta qismi O‘zSSRga joylashtirildi, mahalliy aholi ularga yordam berdi", "ular Yevropaga jo‘natildi", "ular frontga safarbar qilindi", "ular o‘z yurtlariga qaytarildi", "O‘zSSRga ko‘chirildi; mahalliy aholi samimiy yordam berdi.")
t.TF("1942-yili O‘zbekistonda yangi sanoat mahsulotini ishlab chiqarish 2 baravar ko‘paydi.", True, "To‘g‘ri.")
t.TF("Kattaqo‘rg‘onlik urush nogironi Hamid Samadov 15 bolani tarbiyaga olgan.", False, "Noto‘g‘ri: Hamid Samadov 13 bolani, Shomahmudovlar 15 bolani olgan.")
t.MUL([("Urush yillarida Yuqori Chirchiq, Shimoliy Farg‘ona, So‘x-Shohimardon kanallari qurildi.", True),
       ("1943-yili 1,5 mln sentnerdan ortiq qand lavlagi davlatga topshirildi.", True),
       ("Shimoliy Kavkazdan O‘zSSRga 175 000 nafar ingush ko‘chirildi.", False)],
      "III noto‘g‘ri: 175 000 nafar chechenlar, 20 000 dan ortiq ingushlar ko‘chirildi.")
t.MATCH("Mehribon oilalarni ular tarbiyalagan bolalar soni bilan moslashtiring.", ["Shoahmad Shomahmudov", "Hamid Samadov", "Fotima Qosimova"],
        ["13 bola", "10 bola", "15 bola"], "cab", "Shomahmudov – 15; Samadov – 13; Qosimova – 10.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["Toshkent aviatsiya zavodining barpo etilishi", "Harbiy korxonalar xodimlarining safarbar qilinganlar qatoriga qo‘shilishi", "Qo‘shimcha 220 500 gektar yer o‘zlashtirilishi", "1,5 mln sentnerdan ortiq lavlagi topshirilishi", "Bekobod metallurgiya zavodi birinchi navbatining ishga tushishi"],
      "1941-yil oktyabr → 1941-yil 14-dekabr → 1942-yil bahor → 1943 → 1944-yil mart.")
t.MAPMATCH('uzb', ['Bekobod', 'Zirabuloq', 'Toshkent'],
           ["1944-yil martda O‘rta Osiyodagi dastlabki zamonaviy metallurgiya kombinati ishga tushgan shahar", "urush yillarida qand zavodi qurilgan joy", "1941-yil dekabrida 63 ta korxonasi mudofaa mahsuloti chiqargan shahar"],
           "1 – Bekobod; 2 – Zirabuloq; 3 – Toshkent.")
t.VENN("Urush yillarida sanoat", "Urush yillarida qishloq xo‘jaligi",
       [("2000 dan ortiq samolyot ishlab chiqarilgan", 1), ("7 ta yirik GES qurilgan", 1),
        ("4 mln tonnadan ziyod paxta topshirilgan", 2), ("ish kuni normasi 1,5 marta oshirilgan", 2),
        ("og‘ir mehnat yuki ayollar, qariyalar va o‘smirlarga tushgan", 3)],
       "Sanoat – samolyotlar, GESlar; qishloq xo‘jaligi – paxta, ish kuni normasi; ikkalasida yuk ayollar, qariya va o‘smirlarga tushgan.")

# 18-§. Frontdagi jasorat
t = Topic('e10u18', 10118); TOPICS['e10u18'] = t
t.B("1941-yil yozida 19-O‘zbek tog‘-otliq diviziyasi asosida qaysi diviziya tashkil qilindi?", "221-motorlashtirilgan diviziya", "17-mexanizatsiyalashgan korpus", "5-kavaleriya diviziyasi", "19-o‘qchilar brigadasi", "Samarqandda 221-motorlashtirilgan diviziya.")
t.B("DMQning “Milliy harbiy qo‘shilmalar tashkil etish to‘g‘risida”gi qarori qachon chiqdi?", "1941-yil 13-noyabrda", "1941-yil 30-iyunda", "1942-yil 27-martda", "1941-yil 22-iyunda", "1941-yil 13-noyabrda.")
t.B("Bu qarorga ko‘ra O‘zbekistonda nechta kavaleriya diviziyasi tashkil qilinishi kerak edi?", "5 ta", "9 ta", "3 ta", "26 ta", "5 ta kavaleriya diviziyasi va 9 ta o‘qchilar brigadasi.")
t.B("Snayperchi Zebo G‘aniyeva nechta fashistni otib o‘ldirgan?", "28 nafar", "26 nafar", "52 nafar", "75 nafar", "28 nafar fashistni.")
t.B("Zebo G‘aniyeva qaysi orden bilan mukofotlandi?", "Qizil Bayroq ordeni", "Lenin ordeni", "“Shuhrat” ordeni", "Qizil Yulduz ordeni", "Qizil Bayroq ordeni.")
t.B("“Moskva mudofaasi uchun” medali bilan nechta o‘zbekistonlik jangchi mukofotlandi?", "1 753 kishi", "1 706 kishi", "280 kishi", "120 000 kishi", "1 753 kishi.")
t.B("Birinchi o‘zbek Sovet Ittifoqi Qahramoni kim?", "andijonlik Qo‘chqor Turdiyev", "Sobir Rahimov", "Sharif Ergashev", "Botir Boboyev", "1942-yil 27-martda andijonlik Qo‘chqor Turdiyev.")
t.B("Urush yillarida nechta o‘zbekistonlik fashizmga qarshi janglarda qatnashgan?", "1,5 mln nafar", "6,5 mln nafar", "500 000 nafar", "120 000 nafar", "1,5 mln nafar.")
t.B("Urushda jang maydonlarida halok bo‘lgan yoki bedarak yo‘qolgan o‘zbekistonliklar soni qancha?", "500 000 kishi", "1,5 mln kishi", "27 mln kishi", "400 000 kishi", "500 000 kishi.")
t.B("General-mayor Sobir Rahimov qachon va qayerda halok bo‘ldi?", "1945-yil 26-martda Gdansk (Dansig)ni shturm qilishda", "1943-yil noyabrda Gomel yaqinida", "1945-yil 9-mayda Berlinda", "1942-yilda Stalingradda", "1945-yil 26-martda Polshadagi Gdanskda.")
t.B("Sobir Rahimovga Sovet Ittifoqi Qahramoni unvoni qachon berildi?", "1965-yil 9-mayda", "1945-yil 9-mayda", "1942-yil 27-martda", "1995-yilda", "1965-yil 9-mayda.")
t.B("Dnepr uchun janglarda nechta o‘zbek yigitiga Sovet Ittifoqi Qahramoni unvoni berildi?", "26 nafar", "75 nafar", "52 nafar", "280 nafar", "26 nafar, jumladan Sharif Ergashev va Xalloq Aminov.")
t.B("Iste’dodli shoir Sulton Jo‘ra qayerda halok bo‘ldi?", "Gomel shahri atrofida", "Moskva ostonasida", "Stalingradda", "Berlinda", "1943-yil noyabrda Gomel atrofida, 33 yoshida.")
t.B("“Berlinni ishg‘ol etganligi uchun” medali bilan nechta o‘zbekistonlik taqdirlandi?", "1 706 nafar", "1 753 nafar", "280 nafar", "52 nafar", "1 706 nafar.")
t.B("Nechta o‘zbekistonlik jangchi Sovet Ittifoqi Qahramoni unvoniga sazovor bo‘ldi?", "280 nafar", "75 nafar", "120 000 nafar", "52 nafar", "280 nafar, ulardan 75 nafari o‘zbek.")
t.B("Yaponiya so‘zsiz taslim bo‘lganligi haqidagi hujjatga qachon qo‘l qo‘ydi?", "1945-yil 2-sentyabrda", "1945-yil 9-mayda", "1945-yil avgustda", "1945-yil 26-martda", "1945-yil 2-sentyabrda.")
t.B("Turkiston legioniga qachon asos solindi?", "1942-yil martda", "1941-yil yozida", "1943-yil noyabrda", "1945-yil mayda", "1942-yil martda M.Cho‘qay va Vali Qayumxon tashabbusi bilan.")
t.B("Milliy Turkiston Birligi Qo‘mitasining prezidenti kim edi?", "Vali Qayumxon", "Mustafo Cho‘qay", "Boymirza Hayit", "Abdulla Rasulov", "Vali Qayumxon.")
t.B("Toshkentda Xotira va Qadrlash maydoni qachon barpo etildi?", "1999-yil mayda", "1995-yilda", "2000-yil 12-mayda", "2002-yil 31-avgustda", "1999-yil mayda.")
t.NAT("Stalingrad jangi bo‘lib o‘tdi.", "Ikkinchi jahon urushida tub burilish boshlandi", "Germaniya taslim bo‘ldi", "Yaponiya urushga kirdi", "Moskva mudofaasi boshlandi", "Stalingrad jangi tub burilishni boshlab berdi.")
t.NAT("Urush tugagach, SSSRga harbiy asirlar qaytarildi.", "ularning ko‘pchiligi maxsus lagerlarga joylashtirilib, qiynoqlarga duchor qilindi", "barchasi qahramon deb e’lon qilindi", "ular oliy lavozimlarga tayinlandi", "ular xorijga jo‘natildi", "Ko‘pchiligi maxsus lagerlarda qiynoqqa solindi.")
t.TF("1939-yili respublika aholisi 6,5 mln bo‘lib, har to‘rt o‘zbekistonlikning bittasi armiya safida xizmat qilgan.", True, "To‘g‘ri.")
t.TF("Urushning dastlabki oylarida o‘zbek diviziyalari qurol-yarog‘ bilan to‘liq ta’minlangan.", False, "Noto‘g‘ri: qurol-yarog‘ mutlaqo yetishmagan, hatto oddiy miltiq ham bo‘lmagan.")
t.MUL([("52 nafar o‘zbekistonlik uchala darajadagi “Shuhrat” ordeni bilan taqdirlangan.", True),
       ("1995-yili 33 jildli “Xotira” kitobi nashr etildi.", True),
       ("Ikkinchi jahon urushida SSSR 50 mln kishidan ajraldi.", False)],
      "III noto‘g‘ri: urushda jami 50 mln dan ziyod kishi halok bo‘lgan; SSSR 27 mln kishidan ajralgan.")
t.MATCH("Qahramonlarni ular bilan bog‘liq ma’lumotlar bilan moslashtiring.", ["Qo‘chqor Turdiyev", "Zebo G‘aniyeva", "Sobir Rahimov", "Sulton Jo‘ra"],
        ["Gdanskni shturm qilishda halok bo‘lgan general-mayor", "Gomel atrofida halok bo‘lgan shoir", "birinchi o‘zbek Sovet Ittifoqi Qahramoni", "28 fashistni o‘ldirgan snayperchi"],
        "cdab", "Turdiyev – birinchi qahramon; G‘aniyeva – snayper; Rahimov – Gdansk; Sulton Jo‘ra – Gomel.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["DMQning milliy harbiy qo‘shilmalar to‘g‘risidagi qarori", "Q.Turdiyevga Sovet Ittifoqi Qahramoni unvoni berilishi", "Sulton Jo‘raning halok bo‘lishi", "Sobir Rahimovning halok bo‘lishi", "Yaponiyaning taslim bo‘lishi"],
      "1941-yil 13-noyabr → 1942-yil 27-mart → 1943-yil noyabr → 1945-yil 26-mart → 1945-yil 2-sentyabr.")
t.MAPMATCH('ww2', ['Moskva', 'Stalingrad', 'Gdansk', 'Berlin'],
           ["Zebo G‘aniyeva mudofaasida qatnashgan shahar", "urushda tub burilishni boshlab bergan jang bo‘lgan shahar", "Sobir Rahimov shturm vaqtida halok bo‘lgan shahar", "Botir Boboyev, Solih Umarov zabt etishda qatnashgan shahar"],
           "1 – Moskva; 2 – Stalingrad; 3 – Gdansk; 4 – Berlin.")
t.VENN("Sobir Rahimov", "Qo‘chqor Turdiyev",
       [("general-mayor bo‘lgan", 1), ("Gdanskda halok bo‘lgan", 1),
        ("andijonlik", 2), ("1942-yil 27-martda unvon olgan", 2),
        ("Sovet Ittifoqi Qahramoni", 3)],
       "Rahimov – general-mayor, Gdansk; Turdiyev – andijonlik, 1942; ikkalasi Sovet Ittifoqi Qahramoni.")

# 19-§. Fan va madaniyat – g‘alaba uchun xizmatda
t = Topic('e10u19', 10119); TOPICS['e10u19'] = t
t.B("Urush yillarida O‘zbekiston san’at ustalari nechta konsert brigadasiga bo‘lindi?", "30 ta", "35 ta", "26 ta", "31 ta", "30 ta konsert brigadasi.")
t.B("San’atkorlar frontdagi jangchilarga nechta konsert ko‘rsatdi?", "35 000 ta", "26 000 ta", "30 000 ta", "3 500 ta", "Frontda 35 000, gospitallarda 26 000 konsert.")
t.B("Gospitallarda nechta konsert ko‘rsatildi?", "26 000 ta", "35 000 ta", "375 ta", "200 ta", "26 000 ta.")
t.B("“Muqanna” dramatik asari muallifi kim?", "Hamid Olimjon", "Oybek", "Maqsud Shayxzoda", "Uyg‘un", "Hamid Olimjonning “Muqanna”si.")
t.B("“Jaloliddin Manguberdi” dramasi muallifi kim?", "Maqsud Shayxzoda", "Oybek", "Hamid Olimjon", "Izzat Sulton", "Maqsud Shayxzoda.")
t.B("“Mahmud Torobiy” dramasini kim yozgan?", "Oybek", "Uyg‘un", "G‘afur G‘ulom", "Abdulla Qahhor", "Oybekning “Mahmud Torobiy”si.")
t.B("“Alisher Navoiy” dramasi mualliflari kimlar?", "Uyg‘un va Izzat Sulton", "Hamid Olimjon va Sobir Abdulla", "Oybek va G‘afur G‘ulom", "Maqsud Shayxzoda va Oydin", "Uyg‘un va Izzat Sulton.")
t.B("O‘zbekiston SSR Fanlar akademiyasi qachon tashkil topdi?", "1943-yil 4-noyabrda", "1943-yil sentyabrda", "1940-yil 9-yanvarda", "1945-yil 9-mayda", "1943-yil 4-noyabrda Toshkentda.")
t.B("O‘zSSR Fanlar akademiyasining birinchi prezidenti kim?", "Toshmuhammad Qori-Niyoziy", "Otajon Hoshimov", "Usmon Yusupov", "Sadriddin Ayniy", "Matematik olim T.N.Qori-Niyoziy.")
t.B("O‘zSSR FA qaysi tashkilot negizida tuzildi?", "SSSR FA O‘zbekiston filiali (O‘zFAN)", "Turkiston davlat universiteti", "O‘zSSR Maorif xalq komissarligi", "Til, adabiyot va tarix instituti", "O‘zFAN negizida.")
t.B("Til, adabiyot va tarix instituti qaysi institutlarga ajratildi?", "O‘zbek tili va adabiyoti hamda Tarix va arxeologiya institutlariga", "Sharqshunoslik va Falsafa institutlariga", "Tarix va Iqtisodiyot institutlariga", "Pedagogika va Psixologiya institutlariga", "O‘zbek tili va adabiyoti hamda Tarix va arxeologiya institutlariga.")
t.B("Toshkentga mamlakatning taniqli ilmiy xodimlaridan necha kishi kelgan?", "375 nafar", "200 nafar", "31 nafar", "1000 nafar", "375 nafar.")
t.B("Respublikaga nechta oliy o‘quv yurti evakuatsiya qilindi?", "31 ta", "7 ta", "30 ta", "100 ta", "31 ta OTM va 7 ta harbiy akademiya.")
t.B("Respublikaga nechta harbiy akademiya evakuatsiya qilindi?", "7 ta", "31 ta", "3 ta", "10 ta", "7 ta harbiy akademiya.")
t.B("O‘zbekistonga kelgan yozuvchilardan biri kim?", "Anna Axmatova", "Lev Tolstoy", "Maksim Gorkiy", "Sergey Yesenin", "Anna Axmatova, Aleksey Tolstoy, Yakub Kolas, Yanka Kupala va boshqalar.")
t.B("O‘zbek va ko‘chib kelgan shoirlar hamkorlikda qaysi almanaxni yaratdi?", "“Biz g‘alaba qozonamiz”", "“O‘zbekiston qilichi”", "“Xotira”", "“Hamma narsa front uchun”", "“Biz g‘alaba qozonamiz” almanaxi.")
t.B("Hamkorlikda yaratilgan antologiya qanday nomlangan?", "“O‘zbekiston shoirlari frontga”", "“Biz g‘alaba qozonamiz”", "“Muqanna”", "“O‘zbekiston qilichi”", "“O‘zbekiston shoirlari frontga”.")
t.NAT("SSSR XKS raisi I.V.Stalinning 1943-yil sentyabrdagi qarori qabul qilindi.", "O‘zFAN negizida O‘zSSR Fanlar akademiyasi tashkil topdi", "O‘zFAN tugatildi", "olimlar frontga jo‘natildi", "Turkiston universiteti yopildi", "1943-yil 4-noyabrda O‘zSSR FA tashkil topdi.")
t.NAT("Respublikaga ko‘plab oliy o‘quv yurtlari va ilmiy-tadqiqot institutlari ko‘chirib keltirildi.", "O‘zbekiston OTMlarining faoliyati Markaz darajasiga yaqinlashdi", "mahalliy OTMlar yopildi", "o‘zbek tili ta’limdan chiqarildi", "fan rivojlanishi to‘xtadi", "O‘quv va ilmiy faoliyatni Markaz darajasiga yaqinlashtirish imkoni tug‘ildi.")
t.TF("Urush yillarida fashistlar bosib olgan hududlardan 200 dan ortiq taniqli yozuvchi va shoirlar O‘zbekistonga kelgan.", True, "To‘g‘ri.")
t.TF("“O‘zbekiston qilichi” dramasini yolg‘iz Oybek yozgan.", False, "Noto‘g‘ri: uning mualliflari Hamid Olimjon, Uyg‘un va Sobir Abdulla.")
t.MUL([("Front brigadalari tarkibida Tamaraxonim va Halima Nosirova bo‘lgan.", True),
       ("Teatrlar repertuarida harbiy va tarixiy asarlar ustun bo‘lgan.", True),
       ("O‘zSSR FA Samarqand shahrida tashkil topgan.", False)],
      "III noto‘g‘ri: O‘zSSR FA Toshkentda tashkil topgan.")
t.MATCH("Dramatik asarlarni mualliflari bilan moslashtiring.", ["“Muqanna”", "“Mahmud Torobiy”", "“Jaloliddin Manguberdi”"],
        ["Maqsud Shayxzoda", "Hamid Olimjon", "Oybek"], "bca", "“Muqanna” – Hamid Olimjon; “Mahmud Torobiy” – Oybek; “Jaloliddin Manguberdi” – Shayxzoda.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["O‘zSSR Fanlar komitetining tuzilishi", "O‘zFANning tashkil etilishi", "Germaniyaning SSSRga hujumi", "O‘zSSR Fanlar akademiyasining tashkil topishi"],
      "1932-yil 14-oktyabr → 1940-yil 9-yanvar → 1941-yil 22-iyun → 1943-yil 4-noyabr.")
t.MAPN(CA, ['Toshkent', 'Samarqand', 'Buxoro', 'Qo‘qon'], "1943-yil 4-noyabrda O‘zbekiston SSR Fanlar akademiyasi tashkil topgan shahar qaysi raqam bilan belgilangan?",
       "O‘zSSR FA 1943-yil 4-noyabrda Toshkentda tashkil topdi.")
t.VENN("O‘zbek yozuvchilari", "Ko‘chib kelgan yozuvchilar",
       [("Hamid Olimjon", 1), ("Maqsud Shayxzoda", 1),
        ("Anna Axmatova", 2), ("Yakub Kolas", 2),
        ("“Biz g‘alaba qozonamiz” almanaxini yaratishda qatnashgan", 3)],
       "O‘zbek yozuvchilari va ko‘chib kelganlar hamkorlikda almanax va antologiya yaratdilar.")

# 20-§. Urushdan keyingi xalq xo‘jaligi
t = Topic('e10u20', 10120); TOPICS['e10u20'] = t
t.B("Markazning rejalarida O‘zbekistonga qanday o‘lka sifatida qaraldi?", "faqat xomashyo yetkazib beruvchi chekka o‘lka", "sanoati rivojlangan o‘lka", "harbiy markaz", "turizm markazi", "Faqat xomashyo yetkazib beruvchi chekka o‘lka sifatida.")
t.B("O‘zbekiston metallurgiya zavodida yangi prokat sexi qachon ishga tushirildi?", "1946-yili", "1944-yili", "1948-yili", "1956-yili", "1946-yili.")
t.B("Urushdan keyingi yillarda qaysi neft konlari ochildi?", "Polvontosh va Janubiy Olamushuk", "Gazli va Muborak", "Olmaliq va Angren", "Ko‘kdumaloq va Shurtan", "Polvontosh va Janubiy Olamushuk.")
t.B("Neftni qayta ishlash zavodi qayerda foydalanishga topshirildi?", "Farg‘onada", "Toshkentda", "Buxoroda", "Bekobodda", "Farg‘onada.")
t.B("SSSR hukumatining paxtachilikni tiklash va rivojlantirish to‘g‘risidagi qarori qachon qabul qilindi?", "1946-yil 5-fevralda", "1956-yil 6-avgustda", "1947-yil dekabrda", "1948-yilda", "1946-yil 5-fevralda.")
t.B("1946-yili O‘zSSR uchun paxta ekin maydoni qancha qilib belgilandi?", "779 000 gektar", "218 000 gektar", "200 000 gektar", "160 000 gektar", "779 000 gektar.")
t.B("1946-yili qancha sug‘oriladigan maydon faqat paxta ekish uchun bo‘shatildi?", "218 000 gektar", "779 000 gektar", "100 000 gektar", "220 500 gektar", "218 000 gektar.")
t.B("“Tashselmash” zavodi paxta terish mashinalarining dastlabki partiyasini qachon ishlab chiqardi?", "1948-yili", "1946-yili", "1949-yili", "1969-yili", "1948-yili.")
t.B("Toshkent traktor zavodi (TTZ) qachon barpo etildi?", "1969-yili", "1949-yili", "1948-yili", "1956-yili", "“Tashavtomash” bazasida 1969-yili.")
t.B("Kartochka tizimi qachon bekor qilindi?", "1947-yil dekabrda", "1945-yil mayda", "1946-yil fevralda", "1953-yilda", "1947-yil dekabrda.")
t.B("Mirzacho‘lning qo‘riq yerlarini sug‘orish to‘g‘risidagi qaror qachon qabul qilindi?", "1956-yil 6-avgustda", "1946-yil 5-fevralda", "1955-yilda", "1961-yilda", "1956-yil 6-avgustda.")
t.B("Mirzacho‘l qarori bo‘yicha O‘zSSRda paxta maydonlarini qanchaga kengaytirish rejalashtirildi?", "200 000 gektar", "100 000 gektar", "160 000 gektar", "779 000 gektar", "O‘zSSRda 200 000, Qozog‘iston SSRda 100 000 gektar.")
t.B("Mirzacho‘lni o‘zlashtirishga rahbarlik qilish uchun qaysi tashkilot tuzildi?", "“Glavgolodnostepstroy”", "“Tashselmash”", "“Tashavtomash”", "MTS", "“Glavgolodnostepstroy”.")
t.B("1955 – 1959-yillarda O‘zbekistonda qancha yangi yer o‘zlashtirildi?", "160 000 gektardan ziyod", "200 000 gektar", "218 000 gektar", "1 mln gektar", "160 000 gektardan ziyod.")
t.B("Mirzacho‘l shaharchasi qachon Guliston shahriga aylantirildi?", "1961-yili", "1956-yili", "1959-yili", "1969-yili", "1961-yili.")
t.B("1956-yili MTSlarga to‘lanadigan natura haqi stavkalari necha foizga kamaytirildi?", "40 %", "50 %", "25 %", "75 %", "40 % kamaytirildi.")
t.B("“Monokultura” atamasi nimani anglatadi?", "almashlab ekishga amal qilmay, faqat bir xil ekinni yetishtirish", "bir necha ekinni almashlab ekish", "faqat sabzavot yetishtirish", "qo‘riq yerlarni o‘zlashtirish", "Faqat bir xil ekinni muttasil yetishtirish.")
t.NAT("1946-yil 5-fevraldagi qaror bilan oziq-ovqat ekinlari maydonlari chigit ekish uchun ajratildi.", "oziq-ovqat muammosi o‘tkirlashdi, ekologiya buzilib, aholi salomatligi yomonlashdi", "oziq-ovqat mo‘l bo‘ldi", "paxta xarid narxi keskin oshdi", "paxta maydonlari qisqardi", "Oziq-ovqat muammosi, ekologik va sog‘liq muammolari kelib chiqdi.")
t.NAT("Barcha texnika mashina-traktor stansiyalari (MTS) qo‘lida to‘plandi.", "salbiy oqibatlarga olib keldi", "kolxozlar boyib ketdi", "paxta terish to‘liq mexanizatsiyalashdi", "traktor ishlab chiqarish to‘xtadi", "Texnikaning MTSlarda to‘planishi salbiy oqibatlarga olib keldi.")
t.TF("Urushdan keyin yakka tartibda hunarmandchilik bilan shug‘ullanish man etildi.", True, "To‘g‘ri: hunarmandlar kooperativ artellarga birlashtirildi.")
t.TF("1946-yildan keyin paxta yetishtirish ko‘paygani sababli paxtaning xarid narxi muntazam oshirildi.", False, "Noto‘g‘ri: paxtaning xarid narxi oshirilmadi.")
t.MUL([("1945-yil oxirida mashinasozlik qishloq xo‘jaligi va irrigatsiya ehtiyojlari uchun mashinalar ishlab chiqarishga o‘tkazildi.", True),
       ("1956-yili suv uchun to‘lanadigan haq bekor qilindi.", True),
       ("“Tashavtomash” zavodi 1946-yili ishga tushirildi.", False)],
      "III noto‘g‘ri: “Tashavtomash” Tashselmash mashinalaridan bir yil keyin, ya’ni 1949-yili ishga tushirildi.")
t.MATCH("Sanalarni voqealar bilan moslashtiring.", ["1946-yil 5-fevral", "1947-yil dekabr", "1956-yil 6-avgust", "1961-yil"],
        ["Mirzacho‘lning Guliston shahriga aylantirilishi", "kartochka tizimining bekor qilinishi", "paxtachilikni rivojlantirish to‘g‘risidagi qaror", "Mirzacho‘l qo‘riq yerlarini sug‘orish to‘g‘risidagi qaror"],
        "cbda", "1946 – paxtachilik qarori; 1947 – kartochka bekor; 1956 – Mirzacho‘l qarori; 1961 – Guliston.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["Paxtachilikni rivojlantirish to‘g‘risidagi qaror", "Kartochka tizimining bekor qilinishi", "Tashselmashning dastlabki paxta terish mashinalari", "Mirzacho‘l qo‘riq yerlarini sug‘orish to‘g‘risidagi qaror", "Toshkent traktor zavodining barpo etilishi"],
      "1946 → 1947 → 1948 → 1956 → 1969.")
t.MAPMATCH(CA, ['Guliston (Mirzacho‘l)', 'Farg‘ona shahri', 'Toshkent'],
           ["1961-yili shahar maqomini olgan, qo‘riq yerlari o‘zlashtirilgan hudud markazi", "urushdan keyin neftni qayta ishlash zavodi ishga tushgan shahar", "“Tashselmash” va TTZ joylashgan shahar"],
           "1 – Guliston (Mirzacho‘l); 2 – Farg‘ona; 3 – Toshkent.")
t.VENN("1946-yil 5-fevraldagi qaror", "1956-yil 6-avgustdagi qaror",
       [("O‘zSSRda paxta maydoni 779 000 gektar etib belgilangan", 1), ("218 000 gektar sug‘oriladigan yer paxtaga bo‘shatilgan", 1),
        ("Mirzacho‘l qo‘riq yerlarini sug‘orish ko‘zda tutilgan", 2), ("Qozog‘iston SSRda 100 000 gektar kengaytirish rejalashtirilgan", 2),
        ("paxta ekin maydonlarini kengaytirishga qaratilgan", 3)],
       "1946 – 779 ming ga, 218 ming ga; 1956 – Mirzacho‘l, Qozog‘iston; ikkalasi paxta maydonini kengaytirishga qaratilgan.")
