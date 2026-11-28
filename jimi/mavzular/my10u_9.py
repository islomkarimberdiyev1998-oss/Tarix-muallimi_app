from qlib import Topic, PLACES, REG
TOPICS = {}

# 18-mavzu. Sovet boshqaruv tizimining o‘rnatilishi
t = Topic('y10u18', 10018); TOPICS['y10u18'] = t
t.B("O‘rta Osiyoning favqulodda komissari qilib Toshkentga kim jo‘natilgan?", "P. Kobozev", "I. Tobolin", "N. Korolkov", "F. Kolesov", "Bolshevik P. Kobozev.")
t.B("RSFSRning Turkiston Sovet Respublikasi haqidagi Nizomi qachon qabul qilingan?", "1918-yil 30-aprelda", "1918-yil 22-fevralda", "1920-yil 6-oktyabrda", "1924-yilda", "1918-yil 30-aprel.")
t.B("Nizomga ko‘ra qanday respublika tuzilgani e’lon qilingan?", "Turkiston ASSR", "O‘zbekiston SSR", "BXSR", "Turkiston Muxtoriyati", "Turkiston Avtonom Sovet Sotsialistik Respublikasi.")
t.B("Turkiston ASSR tarkibiga qaysi hududlar kirmagan?", "Buxoro amirligi va Xiva xonligi", "Farg‘ona viloyati", "Sirdaryo viloyati", "Samarqand viloyati", "Buxoro amirligi va Xiva xonligi.")
t.B("Turkiston ASSRdagi muhim masalalar qaysi Moskva idorasining roziligi bilan hal etilgan?", "Turkiston komissiyasi", "Kraymussovet", "Milliy markaz", "Turkiston komiteti", "Turkiston komissiyasi.")
t.B("1918–1920-yillar qanday nom bilan atalgan?", "«harbiy kommunizm»", "NEP", "«qayta qurish»", "«kollektivlashtirish»", "«Harbiy kommunizm».")
t.B("Dehqonlar ortiqcha mahsulotni davlatga topshirish tizimi nima deb atalgan?", "oziq-ovqat razvyorstkasi", "prodnalog", "kontraktatsiya", "kolxoz", "Oziq-ovqat razvyorstkasi (taqsimoti).")
t.B("Mehnatga yaroqli aholini majburiy mehnatga jalb qilish qanday atalgan?", "mehnat militarizatsiyasi", "kollektivlashtirish", "industrlashtirish", "korenizatsiya", "Mehnat militarizatsiyasi.")
t.B("Xususiy mulk egalari qanday deb e’lon qilingan?", "tekinxo‘rlar", "bosmachilar", "quloqlar", "burjuaziya", "Tekinxo‘rlar, fuqarolik huquqidan mahrum etilgan.")
t.B("NEP qanday ma’noni anglatadi?", "Yangi iqtisodiy siyosat", "Milliy iqtisodiy dastur", "Xalq xo‘jaligi rejasi", "Harbiy kommunizm", "Yangi iqtisodiy siyosat.")
t.B("NEPga o‘tish qachondan boshlangan?", "1921-yil ko‘klamidan", "1918-yildan", "1924-yildan", "1929-yildan", "1921-yil ko‘klamiga kelib.")
t.B("Yer-suv islohotining dastlabki natijasida yer tuzish jamg‘armasiga qancha yer qo‘shilgan?", "1 722 626 desyatina", "600 000 desyatina", "100 000 desyatina", "17 million desyatina", "1 722 626 desyatina.")
t.B("Mahalliy aholiga qancha yer ajratilgan?", "600 000 desyatina", "1 722 626 desyatina", "60 000 desyatina", "1 million desyatina", "Faqat 600 000 desyatina.")
t.B("O‘rta Osiyoda xususiy mulkni tugatish qachondan boshlangan?", "1921–1922-yillardan", "1918-yildan", "1925-yildan", "1930-yildan", "1921–1922-yillardan.")
t.NAT("«Harbiy kommunizm» davrida Turkistondan Markazga oziq-ovqat olib chiqib ketildi.", "xalq ochlikdan qirilayotgan bir paytda zaxiralar bolsheviklarning harbiy maqsadlariga sarflandi", "Turkistonda oziq-ovqat ko‘paydi", "ochlik tugadi", "dehqonlar boyidi", "Ocharchilik kuchaydi.")
t.NAT("Sovet hokimiyati barcha fabrika-zavodlarni egalaridan tortib oldi.", "ular avvalo mudofaa mahsulotlari ishlab chiqarishga yo‘naltirildi", "zavodlar yopildi", "zavodlar xorijga sotildi", "egalari boshqaruvda qoldi", "Mudofaa ishlab chiqarishi.")
t.NAT("NEP harbiy-kommunistik usullardan voz kechishni ko‘zda tutdi.", "ishlab chiqaruvchilarga, avvalo dehqonlarga bir qadar erkinlik berildi", "dehqonlar huquqlaridan mahrum bo‘ldi", "bozor butunlay yo‘qotildi", "razvyorstka kuchaydi", "Dehqonlarga erkinlik.")
t.NAT("Yer-suv islohoti o‘tkazildi.", "boy xo‘jaliklari va katta yer egaligi tugatilib, yerlar kam yerli dehqonlar, batraklarga taqsimlandi", "yer egalari kuchaydi", "vaqf yerlari ko‘paydi", "ko‘chmanchilik kuchaydi", "Yerlar qayta taqsimlandi.")
t.TF("«Harbiy kommunizm» davrida pul muomalasi natura bilan almashtirilgan.", True, "To‘g‘ri.")
t.TF("Yer-suv islohoti jarayonida vaqf yerlari saqlab qolingan va ko‘paytirilgan.", False, "Noto‘g‘ri: vaqf yerlari ham tugatila boshlagan.")
t.TF4([("Turkiston Markaziy Ijroiya Komiteti va XKS tuzilgan.", True), ("Banklar va temiryo‘l transporti davlat hisobiga o‘tkazilgan.", True),
       ("«Harbiy kommunizm» davrida bozor munosabatlari rag‘batlantirilgan.", False), ("Moskvadan Turkistonga ko‘plab partiya xodimlari yuborilgan.", True)],
      "3-noto‘g‘ri: bozor yo‘qotilgan, munosabatlari rad etilgan.")
t.MUL([("Yettisuv, Sirdaryo, Farg‘ona, Samarqand viloyatlarida katta yer egaligi yo‘qotilgan.", True),
       ("Islohot ko‘chmanchi aholini o‘troqlashtirishni ham ko‘zlagan.", True),
       ("«Harbiy kommunizm» sotsializm qurishning samarali usuli bo‘lgan.", False)],
      "III noto‘g‘ri: xalqqa qarshi qaratilgan va yaroqsiz usul bo‘lgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Turkiston ASSR haqidagi Nizom qabul qilindi", "«harbiy kommunizm» davri (1918–1920)", "NEPga o‘tish", "yer-suv islohoti – xususiy mulkni tugatish"],
      "1918-aprel → 1918–1920 → 1921 bahor → 1921–1922.")
t.MATCH("Atamalarni izohi bilan moslashtiring.", ["razvyorstka", "mehnat militarizatsiyasi", "NEP", "Turkiston komissiyasi"],
        ["ortiqcha mahsulotni davlatga topshirish", "majburiy mehnatga jalb qilish", "Yangi iqtisodiy siyosat", "Moskvaning nazorat idorasi", "milliy hukumat"], 'abcd',
        "Razvyorstka – topshirish; militarizatsiya – majburiy mehnat; NEP – yangi siyosat; komissiya – nazorat.")
t.VENN("«Harbiy kommunizm»", "NEP",
       [("bozor yo‘qotilgan", 1), ("oziq-ovqat razvyorstkasi", 1),
        ("dehqonlarga bir qadar erkinlik", 2), ("1921-yil ko‘klamidan", 2),
        ("sovet hokimiyatining iqtisodiy siyosati", 3)],
       "Harbiy kommunizm – bozorsiz, razvyorstka; NEP – erkinlik, 1921; ikkalasi sovet siyosati.")
t.MAPN('uzb', ['Toshkent', 'Samarqand', 'Buxoro', 'Xiva'], "Favqulodda komissar P. Kobozev yuborilgan, Turkiston ASSR boshqaruvi joylashgan shahar xaritada qaysi raqamda?",
       "Toshkent.")

# 19-mavzu. Sovet hokimiyatiga qarshi qurolli harakatlar
t = Topic('y10u19', 10019); TOPICS['y10u19'] = t
t.B("Turkistonda sovet hokimiyatiga qarshi kurash qachon boshlangan?", "1918-yil fevral oxirida", "1917-yil oktyabrda", "1920-yil sentyabrda", "1924-yil kuzida", "1918-yil fevral oxirlarida.")
t.B("Istiqlolchilik harakatining bosh g‘oyasi nima edi?", "Turkiston mustaqilligi", "amirlikni tiklash", "Rossiyaga qo‘shilish", "xonliklarni birlashtirish", "Turkiston mustaqilligi.")
t.B("Farg‘ona muvaqqat muxtoriyat hukumati qachon tuzilgan?", "1919-yil 12-oktyabrda", "1920-yil 6-martda", "1918-yil fevralda", "1921-yil martda", "1919-yil 12-oktyabr.")
t.B("Farg‘ona muvaqqat muxtoriyat hukumati qayerda tuzilgan?", "Pomirning Ergashtom ovulida", "Qo‘qonda", "Skobelevda", "Andijonda", "Ergashtom ovulida.")
t.B("Farg‘ona muvaqqat hukumatiga kim boshchilik qilgan?", "Madaminbek", "Shermuhammadbek", "Katta Ergash", "Ibrohimbek", "Madaminbek.")
t.B("1919-yil kech kuzida Madaminbek qo‘l ostida qancha yigit bo‘lgan?", "30 000 ga yaqin", "20 000", "8 000", "3 000", "30 000 ga yaqin.")
t.B("Madaminbek bilan yarash bitimi qachon imzolangan?", "1920-yil 6-martda", "1919-yil 12-oktyabrda", "1920-yil mayda", "1921-yil martda", "1920-yil 6-mart, Skobelev shahri.")
t.B("Yarash bitimini Madaminbek bilan kim imzolagan?", "N. Veryovkin-Roxalskiy", "Frunze", "Kobozev", "Tobolin", "2-Turkiston o‘qchi diviziyasi boshlig‘i Veryovkin-Roxalskiy.")
t.B("Sobiq amir Olimxon qachon Afg‘onistonga o‘tib ketgan?", "1921-yil martda", "1920-yil sentyabrda", "1922-yil avgustda", "1924-yil iyunda", "1921-yil mart.")
t.B("G‘arbiy Buxoroda harakatga kim rahbarlik qilgan?", "Mulla Abdulqahhor", "Ibrohimbek", "Davlatmandbek", "Junaydxon", "Mulla Abdulqahhor.")
t.B("Mulla Abdulqahhor qo‘l ostida nechta qo‘rboshi birlashgan?", "20 nafar", "200 nafar", "5 nafar", "50 nafar", "20 nafar.")
t.B("Anvar Posho qayerdan kelgan general edi?", "Turkiyadan", "Afg‘onistondan", "Erondan", "Rossiyadan", "Turkiyadan.")
t.B("Anvar Posho qachon halok bo‘lgan?", "1922-yil avgustda", "1921-yil kuzida", "1924-yil oxirida", "1920-yil mayda", "1922-yil avgust, Obidara qishlog‘i.")
t.B("Junaydxon 1924-yil 17-iyunda qaysi shaharga yetib kelgan?", "Hirot", "Kobul", "Mashhad", "Xiva", "Afg‘onistondagi Hirot.")
t.B("Qurolli kurashning ikkinchi davri qaysi yillarni o‘z ichiga oladi?", "1925–1935", "1918–1924", "1920–1922", "1935–1941", "1925–1935.")
t.B("Sovet davrida istiqlolchilar qanday atalgan?", "«bosmachilar»", "«jadidlar»", "«quloqlar»", "«tekinxo‘rlar»", "«Bosmachilar».")
t.NAT("Farg‘ona vodiysiga bolsheviklar qo‘shimcha kuchlar tashladi.", "1920-yil yanvar o‘rtalariga kelib jangovar tashabbus qizil armiya qo‘liga o‘tdi", "istiqlolchilar Toshkentni oldi", "Madaminbek kuchaydi", "qizil armiya chekindi", "Tashabbus qizil armiyaga o‘tdi.")
t.NAT("Katta Ergash qo‘rboshining qo‘shini mag‘lubiyatga uchradi.", "Shermuhammadbek asosiy kuchlarini olib Oloy vohasiga chekindi", "Shermuhammadbek taslim bo‘ldi", "Madaminbek halok bo‘ldi", "qizil armiya Oloyga ketdi", "Oloyga chekinish.")
t.NAT("BXSRning ko‘plab milliy rahbarlari lavozimlarini tark etdi.", "ular muxolifatdagi qurolli harakat saflariga o‘tib ketdi", "ular Moskvaga ko‘chdi", "ular qizil armiyaga qo‘shildi", "ular siyosatdan ketdi", "Istiqlolchilarga qo‘shildi.")
t.NAT("Harakat yagona markaz ostida to‘liq birlasha olmadi, harbiy tayyorgarlik yetarli emasdi.", "bu istiqlolchilik harakatining eng zaif tomoni bo‘lib, 1935-yilga kelib u mag‘lubiyatga uchradi", "harakat g‘alaba qildi", "Turkiston mustaqil bo‘ldi", "qizil armiya chiqib ketdi", "Mag‘lubiyat.")
t.TF("Madaminbek 1920-yil mayda noaniq vaziyatda o‘ldirilgan.", True, "To‘g‘ri.")
t.TF("Ibrohimbek G‘arbiy Buxoroda harakatga rahbarlik qilgan.", False, "Noto‘g‘ri: Sharqiy Buxoroda; G‘arbiy Buxoroda – Mulla Abdulqahhor.")
t.TF4([("Shermuhammadbek qo‘l ostida 20 000 askar bo‘lgan.", True), ("Anvar Posho Mulla Nafis qo‘rboshi bilan uchrashgan.", True),
       ("Mulla Abdulqahhor 1924-yil oxirida Qizilqumda halok bo‘lgan.", True), ("Junaydxon 1918-yilgacha qizil askarlar safida jang qilgan.", False)],
      "4-noto‘g‘ri: avval Rossiya imperiyasi va Xiva xonligiga qarshi kurashgan, 1918-yil o‘rtasidan qizil askarlarga qarshi.")
t.MUL([("Junaydxon guruhlarida qozoq va qoraqalpoqlar ham bo‘lgan.", True),
       ("Olimxon Sharqiy Buxoroda kuch to‘plab, qizil armiyaga qarshi kurashgan.", True),
       ("Qurolli kurashning birinchi davri 1935-yilda tugagan.", False)],
      "III noto‘g‘ri: birinchi davr 1924-yil kuzida, milliy chegaralanish bilan yakunlangan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Farg‘ona muvaqqat hukumati tuzildi", "Skobelevda yarash bitimi", "Madaminbek o‘ldirildi", "Olimxon Afg‘onistonga o‘tdi", "Anvar Posho halok bo‘ldi", "Junaydxon Hirotga yetib keldi"],
      "1919-10 → 1920-03 → 1920-05 → 1921-03 → 1922-08 → 1924-06.")
t.MATCH("Qo‘rboshilarni faoliyat hududi bilan moslashtiring.", ["Madaminbek", "Mulla Abdulqahhor", "Ibrohimbek", "Junaydxon"],
        ["Farg‘ona vodiysi", "G‘arbiy Buxoro", "Sharqiy Buxoro", "Xorazm", "Samarqand"], 'abcd',
        "Madaminbek – Farg‘ona; Abdulqahhor – G‘arbiy Buxoro; Ibrohimbek – Sharqiy Buxoro; Junaydxon – Xorazm.")
t.VENN("Madaminbek", "Anvar Posho",
       [("Farg‘ona muvaqqat hukumati boshlig‘i", 1), ("Skobelevda yarash bitimi imzolagan", 1),
        ("Turkiyadan kelgan general", 2), ("Obidarada halok bo‘lgan", 2),
        ("sovet hokimiyatiga qarshi kurash rahbari", 3)],
       "Madaminbek – Farg‘ona; Anvar Posho – Turkiya, Obidara; ikkalasi istiqlolchi rahbar.")
t.MAPMATCH('ca', ['Farg‘ona', 'Baljuvon', 'Ko‘hna Urganch', 'Hirot'],
           ["1920-yil 6-martda yarash bitimi imzolangan Skobelev shahri", "atrofidagi Obidarada Anvar Posho halok bo‘lgan joy", "Junaydxon guruhlari harakat qilgan Xorazm shahri", "1924-yil iyunda Junaydxon yetib kelgan Afg‘oniston shahri"],
           "1 – Skobelev (Farg‘ona); 2 – Baljuvon; 3 – Ko‘hna Urganch; 4 – Hirot.")
