from qlib import Topic, PLACES, REG
TOPICS = {}

# 6-§ Shayboniylar davrida ichki va tashqi savdo
t = Topic('y9u6', 9006); TOPICS['y9u6'] = t
t.B("XVI asr o‘rtalarida Buxoroda bo‘lgan ingliz diplomati kim?", "Antoni Jenkinson", "Marko Polo", "Klavixo", "Vamberi", "Antoni Jenkinson.")
t.B("Jenkinson Buxoroda qaysi mamlakatlar savdogarlari yig‘ilishini qayd etgan?", "Hindiston, Eron, Balx, Rossiya", "Xitoy, Yaponiya, Koreya", "Angliya, Fransiya, Ispaniya", "Misr, Arabiston", "Hindiston, Eron, Balx, Rossiya va boshqalar.")
t.B("Bobur Samarqandning qaysi xususiyatini «qiziq rasm» deb ta’riflagan?", "har bir hunarmandning alohida bozori borligini", "shahar devorlarini", "suv ta’minotini", "madrasalarini", "Har hunarmandning alohida bozori bo‘lgan.")
t.B("Shayboniylar davrida oltin tanga qanday atalgan?", "ashrafiy", "tanga", "dinor", "pul", "Ashrafiy.")
t.B("Eng kichik mis tanga qanday atalgan?", "pul", "dinor", "tangacha", "xoniy", "Pul.")
t.B("Shayboniyxon zarb ettirgan kumush tanganing og‘irligi qancha bo‘lgan?", "5,2 gramm", "2,5 gramm", "10 gramm", "1 gramm", "5,2 gramm.")
t.B("Bir kumush tanga nechta mis tangaga teng bo‘lgan?", "20–21 ta", "10 ta", "40 ta", "100 ta", "20–21 mis tangaga.")
t.B("Abdullaxon II pul islohotidan keyin kumush tanga qiymati qanchaga oshgan?", "bir yarim barobar", "ikki barobar", "o‘n barobar", "uch barobar", "Bir yarim barobar.")
t.B("Abdullaxon II davrida asosiy zarbxona qayerda bo‘lgan?", "Buxoroda", "Samarqandda", "Balxda", "Toshkentda", "Buxoroda.")
t.B("Shayboniylar davrida asosiy yer solig‘i qanday atalgan?", "xiroj (mol)", "zakot", "tanobona", "tog‘ar", "Xiroj (mol).")
t.B("Bog‘ va polizlarning har tanobidan olingan soliq qanday atalgan?", "tanob puli", "alaf puli", "xiroj", "oshlig‘", "Tanob puli.")
t.B("Bedazorlardan olingan soliq qanday atalgan?", "alaf puli", "tanob puli", "zakot", "ixrojot", "Alaf puli.")
t.B("Tanob puli va alaf puli birgalikda qanday nom bilan atalgan?", "tanobona", "ixrojot", "xiroj", "tog‘ar", "Tanobona.")
t.B("Xon saroyi, boshqaruv va qo‘shinni ta’minlash uchun soliqlar to‘plami qanday atalgan?", "ixrojot", "tanobona", "zakot", "xiroj", "Ixrojot.")
t.B("Har bir musulmon zakot sifatida daromadining qancha qismini to‘lagan?", "1/40", "1/10", "1/5", "1/2", "1/40 qismini.")
t.B("Ot va tuyalar uchun yem-xashak solig‘i qanday atalgan?", "oshlig‘", "tog‘ar", "alaf puli", "tanobona", "Oshlig‘.")
t.NAT("Kumushning narxi asta-sekin oshib bordi.", "kumush tangalar davlat hududidan olib chiqib ketila boshladi", "kumush tangalar ko‘paydi", "mis tangalar bekor qilindi", "oltin tangalar taqiqlandi", "Kumush chetga chiqib ketdi.")
t.NAT("Zarbxonalarga kumush keltirilishi kamaydi.", "Abdullaxon II pul islohotini o‘tkazib, kichik oltin tanga zarb ettirdi", "tanga zarbi to‘xtadi", "Rossiya pullari joriy etildi", "kumush tanga qiymati tushdi", "Pul islohoti o‘tkazildi.")
t.NAT("Abdullaxon II pul islohotini o‘tkazdi.", "tanga zarb etish nisbatan markazlashtirildi", "har bir viloyat o‘z pulini chiqardi", "mis tangalar yo‘qoldi", "savdo to‘xtadi", "Zarb markazlashdi.")
t.NAT("Shayboniyxon turli og‘irlikdagi tangalar o‘rniga bir xil og‘irlikdagi tangalar zarb ettirdi.", "pul muomalasi tartibga solindi", "pul muomalasi buzildi", "savdogarlar ketdi", "oltin tanga bekor qilindi", "Tangalar bir xillashdi.")
t.TF("Ko‘chmanchi aholi zakotni tovar bilan, ya’ni 40 ta qo‘ydan bitta qo‘y to‘lagan.", True, "To‘g‘ri.")
t.TF("Tog‘ar soliq bog‘ va polizlardan undirilgan.", False, "Noto‘g‘ri: tog‘ar – qo‘shin ta’minoti uchun soliq.")
t.TF4([("Hindistonlik savdogarlar qimmatbaho toshlar va marvarid olib kelgan.", True), ("Balx, Samarqand va Toshkentda ham tanga zarb etilgan.", True),
       ("Shayboniyxon tangalarida «Eng buyuk sulton» unvoni yozilgan.", True), ("Shayboniylar davrida mis tangalar muomalada bo‘lmagan.", False)],
      "4-noto‘g‘ri: «mis dinor», «dinor» kabi mis tangalar bo‘lgan.")
t.MUL([("Aholi sug‘orish tizimlarini qurish va ta’mirlash majburiyatiga jalb etilgan.", True),
       ("XVI asrning birinchi choragida turli qiymatdagi mis tangalar chiqarilgan.", True),
       ("Antoni Jenkinson fransuz sayyohi bo‘lgan.", False)],
      "III noto‘g‘ri: Jenkinson – ingliz sayyohi va diplomati.")
t.CHR("Pul muomalasidagi o‘zgarishlarni tartiblang.", ["Shayboniyxon bir xil og‘irlikdagi tangalar zarb ettirdi", "kumush narxi oshib, tangalar chetga chiqdi", "Abdullaxon II pul islohotini o‘tkazdi"],
      "Shayboniyxon islohoti → kumush tanqisligi → Abdullaxon II islohoti.")
t.MATCH("Soliqlarni ta’rifi bilan moslashtiring.", ["xiroj", "zakot", "ixrojot", "oshlig‘"],
        ["asosiy yer solig‘i", "daromadning 1/40 qismi", "saroy va qo‘shin uchun soliqlar to‘plami", "ot-tuyalar uchun yem-xashak", "bedazorlardan olingan soliq"], 'abcd',
        "Xiroj – yer solig‘i; zakot – 1/40; ixrojot – saroy ta’minoti; oshlig‘ – yem-xashak.")
t.VENN("Kumush tangalar", "Mis tangalar",
       [("tanga, tangacha, xoniy", 1), ("Shayboniyxon davrida 5,2 gramm", 1),
        ("eng kichigi «pul» deb atalgan", 2), ("mis dinor, dinor", 2),
        ("Shayboniylar davrida muomalada bo‘lgan", 3)],
       "Kumush – tanga, 5,2 g; mis – dinor, pul; ikkalasi muomalada bo‘lgan.")
t.MAPMATCH('uzb', ['Buxoro', 'Balx', 'Samarqand', 'Toshkent'],
           ["asosiy zarbxona joylashgan poytaxt", "savdogarlari Buxoroga kelgan, tanga zarb etilgan janubiy shahar", "Bobur har hunarmandning alohida bozori borligini yozgan shahar", "tanga zarb etilgan shimoli-sharqiy shahar"],
           "1 – Buxoro; 2 – Balx; 3 – Samarqand; 4 – Toshkent.")

# 7-§ Shayboniylar davrida madaniy hayot
t = Topic('y9u7', 9007); TOPICS['y9u7'] = t
t.B("Abdullaxon II davrida bunyod etilgan me’morchilik obidalari soni manbalarga ko‘ra qancha?", "1000 dan oshadi", "100 ga yaqin", "500 ta", "50 ta", "1000 dan oshadi.")
t.B("Hasanxo‘ja Nisoriyning «Muzakkiri ahbob» asari nomi qanday tarjima qilinadi?", "«Do‘stlar yodnomasi»", "«Hidoyat dengizi»", "«Yetti iqlim»", "«Shohlar sharafi»", "«Do‘stlar yodnomasi».")
t.B("Buxoroga qo‘shilgan Sumiton qishlog‘i munosabati bilan qanday darvoza qurilgan?", "Darvozayi nav (Yangi darvoza)", "Talipoch", "Samarqand darvozasi", "Qorako‘l darvozasi", "Darvozayi nav.")
t.B("Samarqanddagi Xoniya madrasasini kim qurdirgan?", "Shayboniyxon", "Abdullaxon II", "Ubaydullaxon", "Qulbobo Ko‘kaldosh", "Shayboniyxon.")
t.B("Toshkentdagi Baroqxon madrasasi hozir qanday ansambl tarkibida?", "Hazrati Imom", "Registon", "Shohizinda", "Poyi Kalon", "Hazrati Imom.")
t.B("Turkistonda Shayboniylar davrida qaysi inshoot qurilgan?", "Shayboniyxon masjidi", "Ko‘kaldosh madrasasi", "Qosim Shayx masjidi", "Mir Arab madrasasi", "Shayboniyxon masjidi.")
t.B("Qosim Shayx masjidi qaysi shaharda?", "Karmanada", "Buxoroda", "Toshkentda", "Balxda", "Karmanada.")
t.B("1502-yilda Konigilda o‘tkazilgan majlisda qanday qaror qabul qilingan?", "qarovsiz qolgan mulk yerlaridan foydalanish haqida", "poytaxtni ko‘chirish haqida", "urush e’lon qilish haqida", "soliqlarni bekor qilish haqida", "Qarovsiz yerlardan foydalanish haqida.")
t.B("Shayboniyxon buyrug‘i bilan qaysi tildagi asarlar turkiy tilga tarjima qilingan?", "fors tilida va mo‘g‘ul yozuvida", "arab tilida", "lotin tilida", "xitoy tilida", "Fors tilida va mo‘g‘ul yozuvida.")
t.B("Abdullaxon II portreti qachon ishlangan?", "1570-yilda", "1557-yilda", "1598-yilda", "1502-yilda", "1570-yilda.")
t.B("Abdulazizxon kutubxonasida «kotiblar podshohi» deb kim atalgan?", "Amir Ali Husayniy", "Sulton Mirak Munshiy", "Mutribiy", "Muhammad Solih", "Amir Ali Husayniy.")
t.B("Shayboniyxon devoni hozir qayerda saqlanadi?", "Istanbuldagi To‘pqopi saroyi muzeyida", "Britaniya muzeyida", "Buxoroda", "Sankt-Peterburgda", "To‘pqopi saroyi muzeyida.")
t.B("«Bahr ul-hido» asari hozir qayerda saqlanadi?", "Britaniya muzeyida", "To‘pqopi saroyida", "Luvrda", "Samarqandda", "Britaniya muzeyida.")
t.B("«Shayboniynoma» muallifi kim?", "Muhammad Solih", "Hofiz Tanish", "Nisoriy", "Bobur", "Muhammad Solih.")
t.B("«Dastur al-iloj» risolasini kim yozgan?", "tabib Sulton Ali", "Muhammad Yusuf", "Mutribiy", "Nisoriy", "Tabib va olim Sulton Ali.")
t.B("Shayboniyxon islohotiga ko‘ra bolalar maktabga necha yoshdan qabul qilingan?", "6 yoshdan", "7 yoshdan", "10 yoshdan", "4 yoshdan", "6 yoshdan.")
t.B("Madrasada har bir bosqichda necha yil o‘qilgan?", "8 yildan", "2 yildan", "4 yildan", "3 yildan", "8 yildan; jami o‘qish 26 yil.")
t.B("Shayboniyxon islohotiga ko‘ra o‘qish jami necha yil davom etgan?", "26 yil", "8 yil", "12 yil", "20 yil", "26 yil.")
t.NAT("Amaldorlar qatlamini shakllantirish va ularni jamiyat tayanchiga aylantirish zarurati paydo bo‘ldi.", "Shayboniyxon ko‘p bosqichli o‘qitish tizimini joriy etdi", "madrasalar yopildi", "faqat harbiy ta’lim qoldi", "maktablar bekor qilindi", "Ta’lim islohoti o‘tkazildi.")
t.NAT("Abdullaxon II Xuroson va Mashhadga yurishlar qildi.", "Buxoro kutubxonasi to‘ldirilib, safaviylar miniatyura an’analari kirib keldi", "kutubxona yonib ketdi", "miniatyura taqiqlandi", "kitoblar Eronga olib ketildi", "Kutubxona boyidi.")
t.NAT("O‘zbek davlatining Hindiston bilan munosabatlari mustahkamlandi.", "Buxoro qo‘lyozmalarida hind uslubidagi miniatyuralar chizila boshlandi", "Hindiston bilan savdo to‘xtadi", "miniatyura yo‘qoldi", "hind tili rasmiy til bo‘ldi", "Hind uslubi kirib keldi.")
t.NAT("Mutribiy Abdullaxon II bergan uchta savolga to‘g‘ri javob berdi.", "xon uni movut chakmon va tilla tangalar bilan mukofotladi", "xon uni saroydan haydadi", "Mutribiy vazir etib tayinlandi", "Mutribiy Hindistonga ketdi", "Mukofotlandi.")
t.TF("Shayboniylar davri miniatyuralarida oddiy xalq vakillari – baliqchilar, bog‘bonlar ham aks ettirilgan.", True, "To‘g‘ri.")
t.TF("Shayboniylar davrida madaniy hayotning asosiy markazlari Xiva va Urganch bo‘lgan.", False, "Noto‘g‘ri: an’anaviy markazlar Samarqand va Buxoro bo‘lgan.")
t.TF4([("Shayboniyxon davrida tarixiy va badiiy adabiyotda o‘zbek tilining mavqeyi kuchaygan.", True), ("Yazdiyning «Zafarnoma»si o‘zbek tiliga o‘girilgan.", True),
       ("«Shayboniynoma» nasriy uslubda yozilgan.", False), ("Buxoroda Abdullaxon kutubxonasi tashkil qilingan.", True)],
      "3-noto‘g‘ri: «Shayboniynoma» she’riy uslubda yozilgan.")
t.MUL([("Ubaydullaxon va Abdullaxon II ning ham asarlari bizgacha yetib kelgan.", True),
       ("Muhammad Yusuf «Qon tomiri va peshob» asarini yaratgan.", True),
       ("Mir Arab madrasasi Samarqandda joylashgan.", False)],
      "III noto‘g‘ri: Mir Arab madrasasi Buxoroda.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Konigilda ilmiy majlis o‘tkazildi", "Abdulazizxon hukmronligi tugadi", "Abdullaxon II portreti ishlandi", "Abdullaxon II vafot etdi"],
      "1502 → 1550 → 1570 → 1598.")
t.MATCH("Asarlarni mualliflari bilan moslashtiring.", ["«Shayboniynoma»", "«Bahr ul-hido»", "«Dastur al-iloj»", "«Muzakkiri ahbob»"],
        ["Muhammad Solih", "Muhammad Shayboniyxon", "Sulton Ali", "Hasanxo‘ja Nisoriy", "Muhammad Yusuf"], 'abcd',
        "Shayboniynoma – Muhammad Solih; Bahr ul-hido – Shayboniyxon; Dastur al-iloj – Sulton Ali; Muzakkiri ahbob – Nisoriy.")
t.VENN("Samarqand", "Buxoro",
       [("Xoniya madrasasi", 1), ("Qulbobo Ko‘kaldosh madrasasi", 1),
        ("Mir Arab madrasasi", 2), ("Darvozayi nav", 2),
        ("Shayboniylar davri madaniy markazi", 3)],
       "Samarqand – Xoniya, Qulbobo Ko‘kaldosh; Buxoro – Mir Arab, Darvozayi nav; ikkalasi madaniy markaz.")
t.MAPMATCH('ca', ['Toshkent', 'Turkiston', 'Karmana', 'Hirot'],
           ["Baroqxon (Hazrati Imom) madrasasi joylashgan shahar", "Shayboniyxon masjidi qurilgan shahar", "Qosim Shayx masjidi joylashgan shahar", "Ko‘kaldosh madrasasi qurilgan Xuroson shahri"],
           "1 – Toshkent; 2 – Turkiston; 3 – Karmana; 4 – Hirot.")
