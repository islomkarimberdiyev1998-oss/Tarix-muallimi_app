from qlib import Topic
TOPICS = {}
XR = 'xorazm'; BA = 'buxamir'; IA = 'iranafg'

# 7 Xiva xonligi va XXSR
t = Topic('e10u7', 10007); TOPICS['e10u7'] = t
t.B("Asfandiyorxon Yosh xivaliklar manifestiga qachon imzo chekkan?", "1917-yil 5-aprelda", "1917-yil 8-aprelda", "1918-yil 30-oktyabrda", "1919-yil 9-aprelda", "1917-yil 5-aprelda.")
t.B("Yosh xivaliklar partiyasi qachon tashkil topgan?", "1914-yilda", "1917-yilda", "1910-yilda", "1920-yilda", "1914-yilda.")
t.B("Islohotlarni nazorat qilish uchun tuzilgan 30 kishilik organ qanday atalgan?", "Idorai mashruta", "Nozirlar Sho‘rosi", "Majlis", "Revkom", "Idorai mashruta.")
t.B("1917-yil 8-aprelda Majlisga kim boshchilik qilgan?", "qozikalon Bobooxun Salimov", "Husaynbek Matmurodov", "Polvonniyoz Yusupov", "Junaidxon", "Qozikalon Bobooxun Salimov.")
t.B("Nozirlar Sho‘rosiga kim raislik qilgan?", "Husaynbek devonbegi Matmurodov", "Bobooxun Salimov", "Ortiq Oxun", "Davlatmurod mahram", "Husaynbek devonbegi Matmurodov.")
t.B("Muvaqqat hukumatning Xivadagi vakili kim edi?", "general Mirbadalov", "Kolesov", "Frunze", "Perfilev", "General Mirbadalov.")
t.B("Majlisning nechta sobiq a’zosi qamoqqa olinib, qatl etilgan?", "17 nafar", "30 nafar", "7 nafar", "100 nafar", "Husaynbek boshchiligidagi 17 nafar.")
t.B("Junaidxon qachon xonlik qurolli kuchlari qo‘mondoni qilib tayinlangan?", "1918-yilda", "1917-yilda", "1919-yilda", "1920-yilda", "1918-yilda.")
t.B("Junaidxonning asl ismi nima bo‘lgan?", "Qurbon Mamed Sardor", "Said Abdullaxon", "Davlatmurod", "Qo‘shmamedxon", "Qurbon Mamed Sardor, yovmut urug‘idan.")
t.B("Asfandiyorxon qachon o‘ldirilgan?", "1918-yil 30-oktyabrda", "1917-yil noyabrda", "1919-yil 9-aprelda", "1920-yil 1-fevralda", "1918-yil 30-oktyabrda saroy fitnasi oqibatida.")
t.B("Asfandiyorxondan keyin taxtga kim o‘tirgan?", "Said Abdullaxon", "Junaidxon", "Polvonniyoz Yusupov", "Davlatmurod mahram", "Uning katta akasi Said Abdullaxon.")
t.B("Taxta shartnomasi qachon imzolangan?", "1919-yil 9-aprelda", "1918-yil noyabrda", "1919-yil 4-noyabrda", "1920-yil 2-fevralda", "1919-yil 9-aprelda.")
t.B("Taxta shartnomasida nima tan olingan?", "Xiva xonligining mustaqilligi", "XXSR", "Junaidxonning xonligi", "Rossiya protektorati", "Xiva xonligi mustaqilligi sovet hokimiyati tomonidan tan olindi.")
t.B("Xiva qachon bosib olingan?", "1920-yil 1-fevralda", "1920-yil 2-fevralda", "1919-yil 4-noyabrda", "1920-yil 26-aprelda", "1920-yil 1-fevralda.")
t.B("XXSR qachon tuzilganligi e’lon qilingan?", "1920-yil 26–30-aprelda", "1920-yil 1-fevralda", "1921-yil 6-martda", "1923-yil oktyabrda", "1920-yil 26–30-aprelda I qurultoyda.")
t.B("XXSR Nozirlar Sho‘rosining raisi kim bo‘lgan?", "Polvonniyoz Yusupov", "Bobooxun Salimov", "Junaidxon", "Fayzulla Xo‘jayev", "Polvonniyoz Yusupov.")
t.B("Bobooxun Salimov boshchiligidagi elchilik qaysi davlatga jo‘natilgan?", "Afg‘onistonga", "Turkiyaga", "Eronga", "Germaniyaga", "1921-yil 24-noyabrda Afg‘onistonga.")
t.B("P. Yusupov hukumati qachon ag‘darilgan?", "1921-yil 6-martda", "1920-yil 1-fevralda", "1923-yil oktyabrda", "1922-yil dekabrda", "1921-yil 6-martda.")
t.B("Xivada xalq dorilfununi qachon ochilgan?", "1921-yil sentyabrda", "1920-yil bahorida", "1923-yil iyunda", "1922-yil dekabrda", "1921-yil sentyabrda.")
t.B("XXSR qachon XSSRga aylantirilgan?", "1923-yil 17–20-oktyabrda", "1921-yilda", "1924-yil sentyabrda", "1920-yil aprelda", "IV qurultoyda, 1923-yil oktyabr.")
t.NAT("Asfandiyorxon general Mirbadalov kuchlariga tayanib, iyunda Majlisni tarqatdi.", "Yosh xivaliklardan o‘ch olinib, ular mamlakatdan chiqib ketdi", "konstitutsion monarxiya mustahkamlandi", "Yosh xivaliklar hokimiyatga keldi", "Junaidxon taxtga chiqdi", "Majlis a’zolari qatl etildi.")
t.NAT("Sovet Rossiyasi XXSR ichki ishlariga aralashib, qizil askarlarni saqlab turdi.", "XXSR rahbarlari qariyb 5 yilda 10 martadan o‘zgartirildi", "XXSR mustaqil rivojlandi", "qizil armiya chiqib ketdi", "Junaidxon hukumatga kirdi", "Ko‘plab asl farzandlar qatag‘on qilindi.")
t.TF("1917-yil aprelda Xiva xonligida qisqa muddatga konstitutsion monarxiya o‘rnatilgan.", True, "To‘g‘ri.")
t.TF("Xiva xonligi ichki kuchlar tomonidan tinch yo‘l bilan tugatilgan.", False, "Noto‘g‘ri: u qizil armiya tomonidan zo‘ravonlik bilan tugatilgan.")
t.MUL([("1922-yil dekabrda qishloq xo‘jaligida yagona soliq tizimi joriy qilingan.", True),
       ("XSSR Konstitutsiyasiga ko‘ra vaqf mulklari maorif nozirligiga berilgan.", True),
       ("Said Abdullaxon davlat ishlarini faol boshqargan.", False)],
      "III noto‘g‘ri: u davlat ishlari bilan shug‘ullanmagan, hokimiyat Junaidxon qo‘lida edi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Asfandiyorxon manifestni imzoladi", "Asfandiyorxon o‘ldirildi", "Taxta shartnomasi", "Xiva bosib olindi", "XXSR e’lon qilindi", "P. Yusupov hukumati ag‘darildi", "XSSRga aylantirildi"],
      "1917-yil aprel → 1918-yil oktyabr → 1919-yil aprel → 1920-yil fevral → 1920-yil aprel → 1921-yil mart → 1923-yil oktyabr.")
t.MAPMATCH(XR, ['Xiva', 'Petro-Aleksandrovsk (To‘rtko‘l)', 'Taxta'],
           ["1920-yil 1-fevralda bosib olingan xonlik poytaxti", "sovet hokimiyati o‘rnatilgan, Yosh xivaliklar boshpana topgan Amudaryo bo‘limi markazi", "1919-yil 9-aprelda Junaidxon bilan shartnoma imzolangan qishloq"],
           "1 – Xiva; 2 – To‘rtko‘l; 3 – Taxta.")
t.VENN("Asfandiyorxon", "Said Abdullaxon",
       [("Yosh xivaliklar manifestini imzolagan", 1), ("1918-yilda saroy fitnasida o‘ldirilgan", 1),
        ("bo‘shang va irodasiz deb ta’riflangan", 2), ("1920-yilda taxtdan voz kechgan", 2),
        ("Xiva xoni bo‘lgan", 3)],
       "Asfandiyorxon — manifest, o‘ldirilgan; Said Abdullaxon — irodasiz, taxtdan voz kechgan.")

# 8 BXSR va XXSRda qizil armiyaga qarshi kurash
t = Topic('e10u8', 10008); TOPICS['e10u8'] = t
t.B("Sobiq amir Olimxon qachon Sharqiy Buxoroga kelgan?", "1920-yil sentyabrda", "1921-yil martda", "1920-yil avgustda", "1922-yil avgustda", "1920-yil sentyabrda.")
t.B("G‘arbiy Buxoroda harakatga kim rahbarlik qilgan?", "Mulla Abdulqahhor", "Ibrohimbek", "Davlatmandbek", "Anvar Posho", "Mulla Abdulqahhor.")
t.B("Sharqiy Buxoroda harakatga kimlar rahbarlik qilgan?", "Ibrohimbek va Davlatmandbek", "Mulla Abdulqahhor", "Junaidxon", "Madaminbek", "Ibrohimbek va Davlatmandbek.")
t.B("Olimxon Afg‘onistonga qachon o‘tib ketgan?", "1921-yil martda", "1920-yil sentyabrda", "1922-yil avgustda", "1924-yilda", "1921-yil martda.")
t.B("Mulla Abdulqahhor qo‘l ostida nechta qo‘rboshi birlashgan?", "20 nafar", "100 nafar", "5 nafar", "200 nafar", "Buxoroning g‘arbiy qismida 20 nafar.")
t.B("Mulla Abdulqahhor qachon va qayerda halok bo‘lgan?", "1924-yil oxirida Qizilqumda", "1922-yil avgustda Baljuvonda", "1921-yil martda Buxoroda", "1923-yilda Nurotada", "1924-yil oxirida Qizilqumda.")
t.B("Anvar Posho Buxoroga qachon kelgan?", "1921-yil oktyabrda", "1922-yil avgustda", "1920-yil sentyabrda", "1924-yilda", "1921-yil oktyabrda, Kavkazdan.")
t.B("Anvar Posho qaysi qo‘rboshi bilan Qarshi yaqinida uchrashgan?", "Mulla Nafis", "Ibrohimbek", "Mulla Abdulqahhor", "Junaidxon", "9-noyabrda Qiliko‘l atrofida Mulla Nafis bilan.")
t.B("Anvar Posho qachon va qayerda halok bo‘lgan?", "1922-yil avgustda Baljuvon atrofidagi Obidarada", "1921-yil noyabrda Qarshida", "1924-yilda Hirotda", "1923-yilda Kitobda", "1922-yil avgustda Obidara qishlog‘ida.")
t.B("Anvar Posho xotirasiga «Baljuvon» marsiyasini kim yozgan?", "Cho‘lpon", "Fitrat", "Hamza", "Avloniy", "Cho‘lpon.")
t.B("Qurolli harakatga o‘tib ketgan BXSR MIK raisi kim?", "Usmon Xo‘ja", "Fayzulla Xo‘jayev", "Porso Xo‘jayev", "Muhitdinov", "Usmon Xo‘ja.")
t.B("1922-yil ko‘klamida Junaidxon qo‘shini qancha yigitdan iborat bo‘lgan?", "15 000", "30 000", "2000", "100 000", "15 000 nafar.")
t.B("1922-yil aprelda Junaidxon qo‘shinlari qaysi shaharni ozod qilgan?", "Porsu", "Xiva", "To‘rtko‘l", "Chimboy", "Porsu shahri va atroflarini.")
t.B("Junaidxon qachon Hirotga yetib kelgan?", "1924-yil 17-iyunda", "1923-yil 12-yanvarda", "1922-yil aprelda", "1935-yilda", "1924-yil 17-iyunda, 20 hamrohi bilan.")
t.B("Istiqlolchilik harakatining ikkinchi davri qaysi yillarni o‘z ichiga oladi?", "1925–1935-yillar", "1918–1924-yillar", "1920–1922-yillar", "1935–1941-yillar", "1925–1935-yillar.")
t.B("Junaidxonni «Rossiya hukmronligi oldida bo‘yin egishni xohlamagan davlat qahramoni» deb ta’riflagan kim?", "Ahmad Zaki Validiy", "Frunze", "Cho‘lpon", "Fitrat", "Ahmad Zaki Validiy «Xotiralar»ida.")
t.NAT("1923-yil 12-yanvarda XXSR MIK hukumat «bosmachilik»ka qarshi kurashga ojiz ekanini tan oldi.", "RSFSR hukumatidan shoshilinch harbiy yordam so‘raldi", "Junaidxon hukumatga kirdi", "harakat to‘xtadi", "XXSR mustaqil bo‘ldi", "Markazdan harbiy yordam so‘raldi.")
t.NAT("Harakat yagona markaz ostida birlasha olmadi, yagona milliy dastur yaratilmadi.", "1935-yilga kelib istiqlolchilik harakati mag‘lubiyatga uchradi", "harakat g‘alaba qozondi", "sovet hokimiyati ag‘darildi", "Buxoro mustaqil bo‘ldi", "Tirik qolganlar xorijga muhojir bo‘ldi.")
t.TF("Junaidxon qo‘shinlari safida turkman va o‘zbeklardan tashqari qozoq va qoraqalpoqlar ham bo‘lgan.", True, "To‘g‘ri.")
t.TF("Barcha qo‘rboshilar doimo yagona qo‘mondonlikka bo‘ysungan.", False, "Noto‘g‘ri: Xolxo‘ja Eshon, G‘ulomalixon Bahodir kabilar bo‘ysunmagan.")
t.MUL([("Anvar Posho Sharqiy Buxoroda g‘arbcha qo‘mondonlik uslubini joriy qilgan.", True),
       ("Ibrohimbek Sharqiy Buxoroda amirlik davridagi boshqaruv usulini joriy qilgan.", True),
       ("Mulla Abdulqahhor faqat Xorazmda faoliyat ko‘rsatgan.", False)],
      "III noto‘g‘ri: u Buxoro, Karmana va Nurota viloyatlarida faoliyat ko‘rsatgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Olimxon Sharqiy Buxoroga keldi", "Olimxon Afg‘onistonga o‘tdi", "Anvar Posho Buxoroga keldi", "Junaidxon Porsuni ozod qildi", "Anvar Posho halok bo‘ldi", "Junaidxon Hirotga yetib keldi"],
      "1920-yil sentyabr → 1921-yil mart → 1921-yil oktyabr → 1922-yil aprel → 1922-yil avgust → 1924-yil iyun.")
t.MAPMATCH(BA, ['G‘ijduvon', 'Qarshi', 'Baljuvon'],
           ["Mulla Abdulqahhor yigitlari qizil askarlar bilan to‘qnashgan tuman markazi", "yaqinida Anvar Posho Mulla Nafis bilan uchrashgan shahar", "atrofida Anvar Posho halok bo‘lgan joy"],
           "1 – G‘ijduvon; 2 – Qarshi; 3 – Baljuvon.")
t.VENN("Ibrohimbek", "Junaidxon",
       [("Sharqiy Buxoroda kurashgan", 1), ("amirlik boshqaruv usulini joriy qilgan", 1),
        ("Xorazmda kurashgan", 2), ("1924-yilda Hirotga borgan", 2),
        ("qizil armiyaga qarshi kurashgan istiqlolchi", 3)],
       "Ibrohimbek — Sharqiy Buxoro; Junaidxon — Xorazm, Hirot.")
