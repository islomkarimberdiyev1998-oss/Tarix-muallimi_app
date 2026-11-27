from qlib import Topic
TOPICS = {}

# 13 Xotin-qizlarni ozodlikka chiqarish
t = Topic('e10u13', 10013); TOPICS['e10u13'] = t
t.B("«Hujum» kompaniyasi qachon va qayerda e’lon qilingan?", "1926-yil sentyabrda O‘rta Osiyo xotin-qizlari kengashida", "1927-yil 8-martda Toshkentda", "1926-yil dekabrda Samarqandda", "1925-yil fevralda Buxoroda", "1926-yil sentyabrda O‘rta Osiyo xotin-qizlari kengashida.")
t.B("«Hujum» kompaniyasini qachondan boshlashga qaror qilingan?", "1927-yil 8-martdan", "1926-yil sentyabrdan", "1928-yil 1-maydan", "1926-yil dekabrdan", "1927-yil 8-martdan.")
t.B("«Hujum» kompaniyasini o‘tkazish uchun maxsus komissiyalar qachon tuzilgan?", "1926-yil dekabrda", "1926-yil sentyabrda", "1927-yil martda", "1928-yilda", "1926-yil dekabrda.")
t.B("1927-yil 8-martdagi mitinglarda qancha xotin-qiz paranjisini gulxanda yoqqan?", "100 000 dan ortiq", "2500 dan ortiq", "10 000", "5000", "100 000 dan ortiq.")
t.B("1927–1928-yillarda «Hujum» yo‘lida qancha faol xotin-qiz jonini qurbon qilgan?", "2500 dan ortiq", "100 000 dan ortiq", "814", "134", "2500 dan ortiq.")
t.B("Ozodlikka chiqarilgan xotin-qizlar dastlab qayerga jalb qilingan?", "hunarmandlik kooperatsiyasiga", "traktorchilar kursiga", "armiyaga", "og‘ir sanoatga", "Hunarmandlik kooperatsiyasiga.")
t.B("1926-yili O‘zbekistonda nechta yirik ayollar arteli bo‘lgan?", "16 ta", "50 dan ortiq", "134 ta", "814 ta", "16 ta, ularda 814 nafar ayol ishlagan.")
t.B("1930-yilda hunarmandchilik artellarida qancha mahalliy ayol ishlagan?", "5000 dan ko‘proq", "814", "2500", "100 000", "50 dan ortiq artelda 5000 dan ko‘proq ayol.")
t.B("1939-yilda qancha xotin-qiz traktorchilar kursiga majburan jalb qilingan?", "2500 nafar", "5000 nafar", "814 nafar", "139 000 nafar", "2500 nafar.")
t.B("1927-yili Andijondagi Eski shahar ayollar klubida nechta a’zo bo‘lgan?", "134 nafar", "814 nafar", "2500 nafar", "16 nafar", "134 nafar.")
t.B("1927-yili tuman ijroiya qo‘mitalari a’zolarining necha foizi ayollar edi?", "20 foizi", "17 foizi", "50 foizi", "5 foizi", "20 foizi; okrug qo‘mitalarida 17 foizi.")
t.B("O‘zSSR MIK Prezidiumi raisining o‘rinbosari bo‘lgan ayol kim?", "Jahon Obidova", "Tojixon Shodiyeva", "Halima Nosirova", "Zulfiya", "Jahon Obidova.")
t.B("O‘zSSR MIK Prezidiumi a’zosi bo‘lgan, keyin qatag‘on qilingan ayol kim?", "Tojixon Shodiyeva", "Tamaraxonim", "Mukarrama Turg‘unboyeva", "Oydin Sobirova", "Tojixon Shodiyeva.")
t.NAT("Bolsheviklar xotin-qizlarni ozodlikka chiqarishni tezlashtirdi.", "«Hujum»ga qarshi bo‘lganlar ayollarga nisbatan zulm o‘tkaza boshladi", "barcha ayollar xavfsiz yashadi", "kompaniya bekor qilindi", "paranji majburiy qilindi", "Ko‘plab xotin-qizlar o‘ldirildi.")
t.NAT("Ayollarni ishga tayinlashda ularning ojiza ekanligi e’tiborga olinmadi.", "bu ularning sog‘lig‘iga jiddiy shikast yetkazdi", "ish unumdorligi keskin oshdi", "ayollar rahbar bo‘ldi", "artellar yopildi", "Sog‘lig‘iga jiddiy shikast yetdi.")
t.TF("«Hujum»ning maqsadlaridan biri ayollarni arzon ishchi kuchi sifatida foydalanish edi.", True, "To‘g‘ri.")
t.TF("Traktorchilar kursini tugatgan xotin-qizlarning ko‘pchiligi traktorchi bo‘lib ishlagan.", False, "Noto‘g‘ri: ko‘pchiligi traktorchi bo‘lib ishlamagan.")
t.MUL([("Ayollar klublarida vrachlar maslahat bergan, bolalar vrach ko‘rigidan o‘tgan.", True),
       ("Xotin-qizlar klublarida ayollar do‘ppi va choyshablar tikkan.", True),
       ("Jahon Obidova va Tojixon Shodiyeva sovet hokimiyati tomonidan mukofotlanib, qatag‘ondan chetda qolgan.", False)],
      "III noto‘g‘ri: ikkalasi ham qatag‘on qilingan.")
t.MATCH("Raqamlarni ma’lumotlar bilan moslashtiring.", ["100 000 dan ortiq", "2500 dan ortiq", "814 nafar", "134 nafar"],
        ["1927-yil 8-martda paranjisini yoqqan ayollar", "1927–1928-yillarda qurbon bo‘lgan faol xotin-qizlar", "1926-yilda 16 ta artelda ishlagan ayollar", "Andijon Eski shahar ayollar klubi a’zolari", "1937-yilda savodini chiqargan ayollar"], 'abcd',
        "100 000 – paranji yoqqanlar; 2500 – qurbonlar; 814 – artel ishchilari; 134 – klub a’zolari.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["«Hujum» e’lon qilindi", "Maxsus komissiyalar tuzildi", "Ommaviy mitinglar boshlandi", "Artellarda 5000 dan ortiq ayol ishladi", "2500 ayol traktorchilar kursiga jalb qilindi"],
      "1926-yil sentyabr → 1926-yil dekabr → 1927-yil 8-mart → 1930 → 1939.")
t.VENN("«Hujum»ning salbiy oqibatlari", "«Hujum» davridagi ijobiy holatlar",
       [("2500 dan ortiq ayol qurbon bo‘lgan", 1), ("ayollar og‘ir vazifalarga qo‘yilgan", 1),
        ("ayollar maosh olish imkoniyatiga ega bo‘lgan", 2), ("ayollar orasidan olima va san’atkorlar yetishgan", 2),
        ("ayollarni ishlab chiqarishga jalb qilish bilan bog‘liq", 3)],
       "Salbiy — qurbonlar, og‘ir ishlar; ijobiy — maosh, iste’dodlar.")

# 14 Madaniy siyosat
t = Topic('e10u14', 10014); TOPICS['e10u14'] = t
t.B("«Tarbiya bizlar uchun yo hayot – yo mamot...» degan so‘zlar kimga tegishli?", "Abdulla Avloniy", "Fitrat", "Cho‘lpon", "Hamza", "Abdulla Avloniy.")
t.B("O‘zbekiston SSR Fanlar komiteti qachon tuzilgan?", "1932-yil 14-oktyabrda", "1940-yil 9-yanvarda", "1934-yilda", "1929-yil dekabrda", "1932-yil 14-oktyabrda.")
t.B("1934-yili Fanlar komitetiga kim rais qilib saylangan?", "Otajon Hoshimov", "Toshmuhammad Qori-Niyozov", "Fayzulla Xo‘jayev", "Akmal Ikromov", "Otajon Hoshimov.")
t.B("Fanlar komiteti qachon SSSR FA O‘zbekiston filiali (O‘zFAN)ga aylantirilgan?", "1940-yil 9-yanvarda", "1932-yil 14-oktyabrda", "1940-yil 8-mayda", "1936-yilda", "1940-yil 9-yanvarda.")
t.B("1940-yili respublikada nechta oliy o‘quv yurti ishlab turgan?", "30 ta", "100 ga yaqin", "18 ta", "539 ta", "30 ta oliy, 100 ga yaqin o‘rta maxsus.")
t.B("O‘rta Osiyoda oliy ta’limning beshigi deb qaysi o‘quv yurti ataladi?", "Turkiston davlat universiteti", "Toshkent konservatoriyasi", "Samarqand pedagogika instituti", "O‘zFAN", "Turkiston davlat universiteti (hozirgi O‘zMU).")
t.B("O‘zSSR Sovetlarining V qurultoyi necha yoshli bolalarni majburiy yetti yillik ta’limga tortishni taklif qilgan?", "8 yoshdan 15 yoshgacha", "7 yoshdan 14 yoshgacha", "6 yoshdan 12 yoshgacha", "10 yoshdan 17 yoshgacha", "8 yoshdan 15 yoshgacha.")
t.B("Ikkinchi besh yillik davrida xalq maorifiga qancha mablag‘ sarflangan?", "1,16 mlrd rubl", "395,5 mln rubl", "539 mln rubl", "35 mln rubl", "1,16 mlrd rubl.")
t.B("Ikkinchi besh yillik davrida nechta yangi maktab qurilgan?", "539 ta", "413 ta", "30 ta", "100 ta", "35 000 o‘quvchi sig‘adigan 539 ta maktab.")
t.B("Respublika maktablarida o‘qish necha tilda olib borilgan?", "18 tilda", "3 tilda", "10 tilda", "30 tilda", "18 tilda.")
t.B("1937-yili savodsizlikni tugatish maktablarining soni nechtaga yetgan?", "413 ta", "539 ta", "139 ta", "18 ta", "413 ta.")
t.B("1937-yili qancha xotin-qiz o‘qish va yozishni o‘rganib olgan?", "139 000 nafar", "28 700 nafar", "931 800 nafar", "35 000 nafar", "139 000 nafar.")
t.B("Sovet hokimiyatining dastlabki o‘n yilliklarida imlo necha marta o‘zgartirilgan?", "3 marta", "2 marta", "4 marta", "5 marta", "3 marta.")
t.B("Lotin grafikasiga o‘tish to‘g‘risidagi qaror qayerda qabul qilingan?", "1929-yil mayda Samarqanddagi konferensiyada", "1940-yil 8-mayda Toshkentda", "1921-yilda Buxoroda", "1936-yilda Moskvada", "1929-yil mayda Samarqandda.")
t.B("O‘zbekistonda arab alifbosidan lotin yozuviga qachon o‘tilgan?", "1929-yil 1-dekabrda", "1929-yil 10-avgustda", "1940-yil 8-mayda", "1922-yilda", "1929-yil 1-dekabrda.")
t.B("Kirill yozuviga o‘tish qaroriga kimning ma’ruzasi asos bo‘lgan?", "Toshmuhammad Qori-Niyozov", "Otajon Hoshimov", "Fayzulla Xo‘jayev", "Hamid Olimjon", "Matematik olim Toshmuhammad Qori-Niyozov.")
t.B("Toshkentda davlat konservatoriyasi qachon ochilgan?", "1936-yili", "1940-yili", "1932-yili", "1929-yili", "1936-yili.")
t.NAT("1940-yil 8-mayda O‘zSSR Oliy Soveti III sessiyasi qaror qabul qildi.", "lotin yozuvidan kirill asosidagi o‘zbek yozuviga o‘tildi", "arab yozuvi tiklandi", "lotin yozuvi joriy qilindi", "imlo soddalashtirildi", "Kirill (rus grafikasi)ga o‘tildi.")
t.NAT("Ikkinchi besh yillikda maorifga katta mablag‘ ajratildi.", "umumta’lim maktablarida o‘quvchilar soni 931 800 nafarga yetdi", "maktablar soni kamaydi", "o‘zbek maktablari yopildi", "savodsizlik oshdi", "O‘quvchilar soni 931 800 ga yetdi.")
t.TF("1921–1922-yillarda arab imlosi isloh qilinib, soddalashtirilgan.", True, "To‘g‘ri.")
t.TF("Universitet va institutlar talabalarining ko‘pchiligini o‘zbeklar tashkil qilgan.", False, "Noto‘g‘ri: asosan slavyan tillariga mansub kishilar o‘qigan.")
t.MUL([("To‘xtasin Jalilov, Yunus Rajabiy, Muxtor Ashrafiy — kompozitorlar.", True),
       ("Komil Yormatov, Nabi G‘aniyev — kinematografiya arboblari.", True),
       ("Mannon Uyg‘ur — mashhur raqqosa.", False)],
      "III noto‘g‘ri: Mannon Uyg‘ur — rejissyor.")
t.MATCH("San’at arboblarini sohalari bilan moslashtiring.", ["Muxtor Ashrafiy", "Abror Hidoyatov", "Komil Yormatov", "Tamaraxonim"],
        ["kompozitor", "teatr aktyori", "kinematografiya arbobi", "raqs va xonandalik", "matematik olim"], 'abcd',
        "Ashrafiy – kompozitor; Hidoyatov – aktyor; Yormatov – kino; Tamaraxonim – raqs.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Arab imlosi isloh qilindi", "Lotin yozuviga o‘tildi", "O‘zSSR Fanlar komiteti tuzildi", "Toshkent konservatoriyasi ochildi", "O‘zFAN tuzildi", "Kirill yozuviga o‘tish qarori"],
      "1921–1922 → 1929 → 1932 → 1936 → 1940-yil yanvar → 1940-yil may.")
t.VENN("Lotin yozuviga o‘tish (1929)", "Kirill yozuviga o‘tish (1940)",
       [("arab tilidagi diniy kitoblarni yo‘qotishni ko‘zlagan", 1), ("Samarqand konferensiyasida qaror qilingan", 1),
        ("Turkiya ta’siridan saqlashni ko‘zlagan", 2), ("Qori-Niyozov ma’ruzasi asosida qabul qilingan", 2),
        ("sovet davridagi alifbo o‘zgarishi", 3)],
       "Lotin — diniy kitoblar, Samarqand; kirill — Turkiya ta’siri, Qori-Niyozov.")
