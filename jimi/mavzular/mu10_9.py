from qlib import Topic
TOPICS = {}

# 17 Sanoat va qishloq xo'jaligi front xizmatida
t = Topic('e10u17', 10017); TOPICS['e10u17'] = t
t.B("1941-yil dekabriga kelib respublika hududida nechta sanoat korxonasi mudofaa mahsulotlari ishlab chiqara boshlagan?", "230 ta", "63 ta", "100 ta", "308 ta", "230 ta, shundan Toshkentda 63 ta.")
t.B("1941-yil dekabrida Toshkentdagi nechta korxona mudofaa mahsulotlari ishlab chiqargan?", "63 ta", "230 ta", "50 ta", "7 ta", "63 ta.")
t.B("O‘zboshimchalik bilan korxonadan ketib qolganlarga qanday jazo belgilangan?", "5 yildan 8 yilgacha qamoq", "1 yil majburiy mehnat", "jarima", "otish", "5 yildan 8 yilgacha qamoq.")
t.B("1943-yilda sanoatning respublika xalq xo‘jaligidagi salmog‘i necha foizgacha ortgan?", "75 foizgacha", "62,6 foizgacha", "37,4 foizgacha", "90 foizgacha", "75 foizgacha.")
t.B("Urush yillarida O‘zbekistonda nechta yirik GES qurilgan?", "7 ta", "4 ta", "12 ta", "2 ta", "7 ta: Oqqovoq, Qibray, Salor, Farhod va b.")
t.B("O‘rta Osiyodagi dastlabki zamonaviy metallurgiya kombinati qayerda ishga tushirilgan?", "Bekobodda", "Chirchiqda", "Toshkentda", "Olmaliqda", "1944-yil martda Bekobodda.")
t.B("O‘zbekiston frontga nechta samolyot yetkazib bergan?", "2000 dan ortiq", "500", "22 000", "200", "2000 dan ortiq samolyot.")
t.B("1941-yili davlatga qancha paxta topshirilgan?", "1,6 mln tonnadan ziyod", "4 mln tonna", "82 mln pud", "1,5 mln sentner", "1,6 mln tonnadan ziyod.")
t.B("1942-yil bahorida qancha qo‘shimcha yer o‘zlashtirilgan?", "220 500 gektar", "1,5 mln gektar", "50 000 gektar", "1 mln gektar", "220 500 gektar.")
t.B("Urush yillarida O‘zbekiston mamlakatda ishlab chiqariladigan qandning qancha qismini bergan?", "chorak qismini", "yarmini", "uchdan birini", "o‘ndan birini", "Chorak qismini.")
t.B("Urush yillarida O‘zbekiston qancha paxta xomashyosi yetkazib bergan?", "4 mln tonnadan ziyod", "1,6 mln tonna", "82 mln tonna", "220 ming tonna", "4 mln tonnadan ziyod paxta va 82 mln pud don.")
t.B("Shaharlarda ishchi va xizmatchilarga kuniga qancha non berilgan?", "400–500 gramm", "300–400 gramm", "1 kg", "200 gramm", "400–500 gramm, oila a’zolariga 300–400 gramm.")
t.B("Kolxozlarda majburiy ish kuni normasi necha marta oshirilgan?", "1,5 marta", "2 marta", "3 marta", "1,2 marta", "1,5 marta.")
t.B("O‘zbekistonga qancha bola evakuatsiya qilingan?", "200 000", "1 mln", "15 000", "30 000", "1 mln dan ortiq kishi, jumladan, 200 000 bola.")
t.B("15 bolani farzandlikka olgan toshkentlik temirchi kim?", "Shoahmad Shomahmudov", "Hamid Samadov", "Hasan Islomov", "Usmon Yusupov", "Shoahmad Shomahmudov va Bahri Akramova.")
t.B("Samarqandlik kolxozchi ayol Fotima Qosimova nechta bolani tarbiyalagan?", "10 ta", "13 ta", "15 ta", "5 ta", "10 bolani.")
t.B("Respublikaga urush davrida nechtadan ortiq harbiy gospital joylashtirilgan?", "30 dan", "100 dan", "10 dan", "300 dan", "30 dan ortiq.")
t.B("Qrimdan O‘zSSRga qancha qrim tatarlari ko‘chirilgan?", "151 604 nafar", "110 000 nafar", "175 000 nafar", "20 000 nafar", "151 604 nafar.")
t.NAT("1941-yil 14-dekabrdan harbiy korxonalar xodimlari safarbar qilinganlar qatoriga qo‘shildi.", "mehnat intizomini buzganlar qattiq jazolanadigan bo‘ldi", "ishchilar erkin ketishi mumkin bo‘ldi", "ish kuni qisqartirildi", "korxonalar yopildi", "Qattiq jazolar joriy etildi.")
t.TF("1943-yilda Kavkaz xalqlari, qrim tatarlari va Volgabo‘yi nemislari sharqqa majburan ko‘chirilgan.", True, "To‘g‘ri (1943–1944-yillarda).")
t.TF("Urush yillarida ocharchilik faqat qishloqlarda bo‘lib, shaharlarga tarqalmagan.", False, "Noto‘g‘ri: yirik sanoat markazlariga ham tarqalgan.")
t.MUL([("Gruziyadan 110 000 nafar mesxeti turklari O‘zSSRga ko‘chirilgan.", True),
       ("Shimoliy Kavkazdan 175 000 nafar chechenlar ko‘chirilgan.", True),
       ("Rahbar xodimlar ham oddiy kartochka bo‘yicha non olgan.", False)],
      "III noto‘g‘ri: rahbar xodimlar maxsus payok bilan ta’minlangan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Harbiy korxonalar xodimlari safarbar qilindi", "Qo‘shimcha 220 500 gektar yer o‘zlashtirildi", "1,5 mln sentner lavlagi topshirildi", "Bekobod metallurgiya zavodining birinchi navbati ishga tushdi"],
      "1941-yil dekabr → 1942-yil bahor → 1943 → 1944-yil mart.")
t.MAPMATCH('uzb', ['Bekobod', 'Kattaqo‘rg‘on', 'Qo‘qon'],
           ["1944-yilda O‘zbekiston metallurgiya zavodi ishga tushgan shahar", "urush yillarida suv ombori suvga to‘ldirila boshlangan shahar", "urush yillarida qand zavodi qurilgan Farg‘ona vodiysidagi shahar"],
           "1 – Bekobod; 2 – Kattaqo‘rg‘on; 3 – Qo‘qon.")
t.VENN("Urush yillaridagi sanoat", "Urush yillaridagi qishloq xo‘jaligi",
       [("7 ta yirik GES qurilgan", 1), ("2000 dan ortiq samolyot ishlab chiqarilgan", 1),
        ("4 mln tonnadan ziyod paxta topshirilgan", 2), ("Kosonsoy va Rudasoy suv omborlari qurilgan", 2),
        ("og‘ir mehnat asosan ayollar, qariyalar va o‘smirlar zimmasida", 3)],
       "Sanoat — GES, samolyot; qishloq xo‘jaligi — paxta, suv omborlari.")

# 18 Frontdagi jasorat
t = Topic('e10u18', 10018); TOPICS['e10u18'] = t
t.B("1941-yil yozida Samarqandda 19-O‘zbek tog‘-otliq diviziyasi asosida qaysi diviziya tuzilgan?", "221-motorlashtirilgan diviziya", "17-mexanizatsiyalashgan korpus", "Turkiston legioni", "5-kavaleriya diviziyasi", "221-motorlashtirilgan diviziya.")
t.B("221-diviziya jangchilari ilk marta qayerda janglarda qatnashgan?", "Yelna yaqinida", "Stalingradda", "Kurskda", "Brestda", "17-mexanizatsiyalashgan korpus tarkibida Yelna yaqinida.")
t.B("DMQning 1941-yil 13-noyabrdagi qaroriga ko‘ra O‘zbekistonda nechta kavaleriya diviziyasi tuzilishi kerak edi?", "5 ta", "9 ta", "3 ta", "14 ta", "5 ta kavaleriya diviziyasi va 9 ta o‘qchilar brigadasi.")
t.B("Moskva mudofaasida 28 fashistni otib o‘ldirgan snayperchi kim?", "Zebo G‘aniyeva", "Tamaraxonim", "Fotima Qosimova", "Halima Nosirova", "Zebo G‘aniyeva; Qizil Bayroq ordeni bilan mukofotlangan.")
t.B("«Moskva mudofaasi uchun» medali bilan nechta o‘zbekistonlik mukofotlangan?", "1753 kishi", "1706 kishi", "280 kishi", "120 000 kishi", "1753 kishi.")
t.B("Birinchi o‘zbek Sovet Ittifoqi Qahramoni kim?", "andijonlik Qo‘chqor Turdiyev", "Sobir Rahimov", "Sharif Ergashev", "Botir Boboyev", "Andijonlik Qo‘chqor Turdiyev, 1942-yil 27-mart.")
t.B("Urush yillarida qancha o‘zbekistonlik fashizmga qarshi janglarda qatnashgan?", "1,5 mln", "6,5 mln", "500 000", "120 000", "1,5 mln nafar.")
t.B("O‘zbekistonliklardan qanchasi jang maydonlarida halok bo‘lgan yoki bedarak yo‘qolgan?", "500 000", "1,5 mln", "27 mln", "1,7 mln", "500 000 kishi.")
t.B("Sobir Rahimov qayerda halok bo‘lgan?", "Gdansk (Dansig)da", "Berlinda", "Stalingradda", "Gomelda", "1945-yil 26-martda Gdanskni shturm qilishda.")
t.B("Sobir Rahimovga Sovet Ittifoqi Qahramoni unvoni qachon berilgan?", "1965-yil 9-mayda", "1945-yil 26-martda", "1942-yil 27-martda", "1945-yil 9-mayda", "1965-yil 9-mayda.")
t.B("Dnepr uchun janglarda nechta o‘zbek yigitiga Sovet Ittifoqi Qahramoni unvoni berilgan?", "26 nafar", "75 nafar", "280 nafar", "52 nafar", "26 nafar.")
t.B("Shoir Sulton Jo‘ra qayerda halok bo‘lgan?", "Gomel shahri atrofida", "Moskva ostonasida", "Berlinda", "Kurskda", "1943-yil noyabrda Gomel atrofida, 33 yoshida.")
t.B("Nechta o‘zbekistonlik jangchi «Berlinni ishg‘ol etganligi uchun» medali bilan taqdirlangan?", "1706 nafari", "1753 nafari", "280 nafari", "52 nafari", "1706 nafari.")
t.B("Yaponiya so‘zsiz taslim bo‘lganligi haqidagi hujjatga qachon qo‘l qo‘ygan?", "1945-yil 2-sentyabrda", "1945-yil 9-mayda", "1945-yil avgustda", "1945-yil 26-martda", "1945-yil 2-sentyabrda.")
t.B("O‘zbekistonlik nechta jangchi Sovet Ittifoqi Qahramoni unvoniga sazovor bo‘lgan?", "280 nafar", "75 nafar", "52 nafar", "120 000 nafar", "280 nafar, ulardan 75 nafari o‘zbek.")
t.B("Turkiston legioniga kimlar tashabbusi bilan asos solingan?", "Mustafo Cho‘qay va Vali Qayumxon", "Boymirza Hayit va Abdulla Rasulov", "Usmon Yusupov va Sobir Rahimov", "Stalin va Molotov", "1942-yil martda Mustafo Cho‘qay va Vali Qayumxon tashabbusi bilan.")
t.B("33 jildli «Xotira» kitobi qachon nashr etilgan?", "1995-yili", "1999-yili", "1991-yili", "2017-yili", "1995-yili.")
t.B("Toshkentda Xotira va Qadrlash maydoni qachon barpo etilgan?", "1999-yil mayda", "1995-yilda", "2000-yil 12-mayda", "1991-yilda", "1999-yil mayda.")
t.NAT("Sovet rejimi mahalliy, ayniqsa turkiy va musulmon xalqlarga ishonchsizlik bilan qaradi.", "o‘zbek jangchilarining hammasida dastlab hatto oddiy miltiq ham bo‘lmagan", "o‘zbek diviziyalari eng yaxshi qurollangan", "o‘zbeklar armiyaga olinmagan", "o‘zbek diviziyalari frontga yuborilmagan", "Qurol-yarog‘ mutlaqo yetishmagan.")
t.TF("Boymirza Hayit fikricha, 1941-yil yozidan 1942-yil bahorigacha 1,7 mln turkistonlik nemislarga asir tushgan.", True, "To‘g‘ri.")
t.TF("SSSRga qaytarilgan harbiy asirlar ozod qilinib, uylariga qaytarilgan.", False, "Noto‘g‘ri: ko‘pchiligi maxsus lagerlarga joylashtirilgan.")
t.MUL([("Ikkinchi jahon urushida 50 mln nafardan ziyod kishi halok bo‘lgan.", True),
       ("SSSR urushda 27 mln kishidan ajralgan.", True),
       ("52 nafar o‘zbekistonlik uchala darajadagi «Shuhrat» ordeni bilan taqdirlangan.", True)],
      "Uchala fikr ham to‘g‘ri.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Milliy harbiy qo‘shilmalar to‘g‘risida DMQ qarori", "Qo‘chqor Turdiyevga Qahramon unvoni", "Kursk va Oryol janglari", "Sulton Jo‘ra halok bo‘ldi", "Sobir Rahimov halok bo‘ldi", "Yaponiya taslim bo‘ldi"],
      "1941-yil noyabr → 1942-yil 27-mart → 1943-yil yoz → 1943-yil noyabr → 1945-yil mart → 1945-yil sentyabr.")
t.MAPMATCH('europe', ['Gdansk', 'Gomel', 'Berlin', 'Yelna'],
           ["Sobir Rahimov halok bo‘lgan shahar", "atrofida shoir Sulton Jo‘ra halok bo‘lgan shahar", "Botir Boboyev, Solih Umarov, Tojiali Boboyev zabt etgan poytaxt", "221-diviziya ilk marta jangga kirgan joy"],
           "1 – Gdansk; 2 – Gomel; 3 – Berlin; 4 – Yelna.")
t.VENN("Sobir Rahimov", "Qo‘chqor Turdiyev",
       [("general-mayor bo‘lgan", 1), ("Gdanskni shturm qilishda halok bo‘lgan", 1),
        ("andijonlik", 2), ("birinchi o‘zbek qahramoni (1942)", 2),
        ("Sovet Ittifoqi Qahramoni", 3)],
       "Rahimov — general, Gdansk; Turdiyev — andijonlik, birinchi qahramon.")
