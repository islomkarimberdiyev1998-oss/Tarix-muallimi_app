from qlib import Topic, PLACES, REG
TOPICS = {}

# 4-§ Shayboniylar davrida davlat boshqaruvi
t = Topic('y9u4', 9004); TOPICS['y9u4'] = t
t.B("Shayboniylar davrida davlat boshqaruvining oliy organi nima hisoblangan?", "dargoh", "devon", "qurultoy", "kengash", "Dargoh.")
t.B("Xonlikka nomzod qanday marosim bilan taxtga o‘tqazilgan?", "oq kigizga solib ko‘tarish orqali", "toj kiydirish orqali", "qilich topshirish orqali", "qasamyod orqali", "Oq kigizga solib ko‘tarilgan.")
t.B("Taxt vorisi qanday atalgan?", "navvob, qolg‘a, kichik xon", "otaliq", "naqib", "ko‘kaldosh", "«Navvob», «qolg‘a», «kichik xon».")
t.B("Ko‘chkunchixon davrida «qolg‘a» etib kim belgilangan?", "ukasi Suyunchxo‘ja", "Jonibek sulton", "Abu Said", "Ubaydulla", "Ukasi Suyunchxo‘ja.")
t.B("Abdullaxon II tartibiga ko‘ra valiahdga qaysi viloyat berilgan?", "Balx", "Samarqand", "Toshkent", "Hisor", "Balx viloyati.")
t.B("Oliy hukmdorning eng yaqin va ishonchli kishisi, asosiy maslahatchisi kim bo‘lgan?", "naqib", "dodxoh", "parvonachi", "mirshab", "Naqib.")
t.B("Shahzodalar tarbiyasiga mutasaddi amaldor kim bo‘lgan?", "otaliq", "naqib", "miroxur", "qushbegi", "Otaliq.")
t.B("Xon hukmlarini ijrochilarga yetkazgan va urushda qo‘shinga qo‘mondonlik qilgan amaldor kim?", "parvonachi", "dodxoh", "ko‘kaldosh", "mushrif", "Parvonachi.")
t.B("Aholining arz-dodlarini qabul qilgan va elchilarni kutib olgan amaldor kim?", "dodxoh", "naqib", "mirshab", "to‘qsoba", "Dodxoh.")
t.B("Hukmron sulola vakili bilan bir onani emgan shaxs egallagan lavozim qaysi?", "ko‘kaldosh", "otaliq", "naqib", "eshik og‘asi", "Ko‘kaldosh.")
t.B("Bosh vazir qanday atalgan?", "devonbegi", "qozikalon", "naqib", "shayxulislom", "Devonbegi.")
t.B("Sulolaga tegishli yer-suv va mol-mulkni boshqargan tuzilma qanday atalgan?", "devoni sarkorixossa", "dargoh", "qozixona", "devonbegi", "Devoni sarkorixossa.")
t.B("Tungi qo‘riqlash boshlig‘i qanday atalgan?", "mirshab", "miroxur", "mushrif", "shig‘ovul", "Mirshab.")
t.B("Xonning yilqi va ot-ulovlariga javobgar amaldor kim?", "miroxur", "qushbegi", "mirshab", "to‘qsoba", "Miroxur.")
t.B("Xorijlik elchilarni qabul qilishga mutasaddi amaldor kim?", "shig‘ovul", "miroxur", "jarchi", "mehtar", "Shig‘ovul.")
t.B("Ov qurollari, ov qushlari va itlariga mas’ul amaldor kim?", "qushbegi", "miroxur", "to‘qsoba", "eshik og‘asi", "Qushbegi.")
t.B("Buxoro bosh qozisi qanday atalgan?", "qozikalon", "qozi askar", "muftiy", "shayxulislom", "Qozikalon.")
t.B("Qozilarni kim tayinlagan?", "oliy hukmdor – xon", "shayxulislom", "devonbegi", "aholi", "Xon tomonidan.")
t.NAT("Devonlarning ish vazifalari dargoh huzuridagi xizmatlar zimmasiga yuklatildi.", "devonlarning boshqaruv tizimidagi o‘rni yo‘qolib bordi", "devonlar kuchaydi", "dargoh tugatildi", "qozilar hokimiyati oshdi", "Devonlar ahamiyati pasaydi.")
t.NAT("Shayboniy hukmdorlar sulola vakillari va qarindoshlarini mulk bilan ta’minladi.", "ular ajratilgan viloyatlarning hokimlari bo‘ldi", "mulklar musodara qilindi", "shahzodalar taxtdan voz kechdi", "viloyatlar tugatildi", "Shahzodalar viloyat hokimlari bo‘ldi.")
t.NAT("Abdullaxon II davriga kelib taxtni otadan o‘g‘ilga o‘tkazish an’anasi shakllana boshladi.", "taxt endi faqat yoshi katta shayboniyga o‘tishi shart bo‘lmay qoldi", "taxt saylov orqali berildi", "qolg‘a lavozimi Samarqandga berildi", "xonlik bekor qilindi", "Vorislik tartibi o‘zgardi.")
t.NAT("XVI asrning ikkinchi yarmidan Usmonli va Rossiyadan pilta miltiq va zambaraklar keltirildi.", "qo‘shin o‘qotar qurollar bilan qurollantirila boshlandi", "qo‘shin tarqatildi", "manjaniqlar ko‘paydi", "otliq qo‘shin tugatildi", "Qo‘shin qurollanishi yangilandi.")
t.TF("Abdullaxon II davrida mamlakat hududi Qashqardan Orol va Kaspiy dengizlari sohillarigacha bo‘lgan.", True, "To‘g‘ri.")
t.TF("Shayboniylarda taxt dastlab otadan bolaga o‘tgan.", False, "Noto‘g‘ri: dastlab shayboniylar orasidagi yoshi katta shaxsga nasib etgan.")
t.TF4([("Eshik og‘asi saroy xavfsizligi va tartibiga mas’ul bo‘lgan.", True), ("To‘qsoba ovqat suzuvchi va ichimlik quyuvchi bo‘lgan.", True),
       ("Mushrif tungi qo‘riqlash boshlig‘i bo‘lgan.", False), ("Qo‘shinda qozi askar lavozimi bo‘lgan.", True)],
      "3-noto‘g‘ri: tungi qo‘riqlash boshlig‘i – mirshab; mushrif xiroj va tortiqlarni yozib borgan.")
t.MUL([("Otaliqlar odatda qabilalarning yoshi katta amirlaridan tayinlangan.", True),
       ("Qozilarni tayinlashda qozilar avlodidan ekaniga e’tibor berilgan.", True),
       ("Devonbegi faqat harbiy masalalar bilan shug‘ullangan.", False)],
      "III noto‘g‘ri: devonbegi mol-mulk, moliya, soliq, yer-suv, tayinlash ishlariga mas’ul bo‘lgan.")
t.CHR("Shayboniylar taxt vorislari (qolg‘a)ning navbatini tartiblang.", ["Suyunchxo‘ja", "Jonibek sulton", "Abu Said", "Abdulla"],
      "Suyunchxo‘ja → Jonibek sulton (1529-yilda vafot) → Abu Said → Abdulla.")
t.MATCH("Lavozimlarni vazifasi bilan moslashtiring.", ["naqib", "dodxoh", "parvonachi", "devonbegi"],
        ["xonning asosiy maslahatchisi", "arz-dodlarni qabul qiluvchi, elchilarni kutib oluvchi", "xon yorliqlarini yetkazuvchi, urushda qo‘mondon", "bosh vazir", "ov qushlariga mas’ul"], 'abcd',
        "Naqib – maslahatchi; dodxoh – arz-dod; parvonachi – yorliq; devonbegi – bosh vazir.")
t.VENN("Dargoh amaldorlari", "Diniy-huquqiy lavozimlar",
       [("miroxur", 1), ("qushbegi", 1), ("qozikalon", 2), ("muftiy", 2),
        ("Shayboniylar davri boshqaruv tizimiga kirgan", 3)],
       "Miroxur, qushbegi – dargoh; qozikalon, muftiy – shariat lavozimlari; hammasi boshqaruv tizimida.")
t.MAPMATCH('ca', ['Qashqar', 'Orol dengizi', 'Balx', 'Buxoro'],
           ["Abdullaxon II davri hududining sharqiy chegarasi", "hudud shimoli-g‘arbda yetgan dengiz", "valiahdga boshqarish uchun berilgan viloyat", "qozikalon faoliyat yuritgan poytaxt"],
           "1 – Qashqar; 2 – Orol dengizi; 3 – Balx; 4 – Buxoro.")

# 5-§ Shayboniylar davrida ijtimoiy-iqtisodiy hayot
t = Topic('y9u5', 9005); TOPICS['y9u5'] = t
t.B("Shayboniylar davrida iqtisodiyotning asosiy sohasi qaysi bo‘lgan?", "dehqonchilik", "savdo", "chorvachilik", "konchilik", "Dehqonchilik.")
t.B("Lalmi yerlarda yashab, chorvachilik bilan ham shug‘ullangan urug‘lar qaysilar?", "abdal, qarluq, qang‘li, barlos, jaloyir", "shayboniylar", "mang‘itlar", "qo‘ng‘irotlar", "Yarimko‘chmanchi urug‘lar.")
t.B("Shayboniyxon qochib ketgan dehqonlarga qanday imtiyoz bergan?", "soliq to‘lashda imtiyoz", "yer sovg‘a qilgan", "harbiy xizmatdan ozod qilgan", "qarzlarini kechgan", "Joylariga qaytarib, soliq imtiyozi bergan.")
t.B("Shayboniyxon Zarafshonning qayerida suvtaqsimlagich qurdirgan?", "Oqdaryo va Qoradaryoga ayrilish yerida", "Chorjo‘y yaqinida", "Jizzaxda", "Marvda", "Oqdaryo–Qoradaryo ayrilishida.")
t.B("Oqchob darasida qurilgan to‘g‘on qanday nom olgan?", "Abdullaxon bandi", "Puli Karmina", "Puli Mehtar", "Hovuzixon", "Abdullaxon bandi.")
t.B("Zarafshondan Jizzax vohasigacha tortilgan ariq qaysi?", "Tuyatortar", "Afshona", "Hovuzixon", "Konigil", "Tuyatortar arig‘i.")
t.B("Murg‘ob vohasidagi suv ombori qanday atalgan?", "Hovuzixon", "Abdullaxon bandi", "Tuyatortar", "Puli Jondor", "Hovuzixon.")
t.B("Abdullaxon bandi qoldiqlari hozir qaysi viloyatda saqlangan?", "Navoiy viloyati Nurota tumanida", "Samarqandda", "Jizzaxda", "Buxoroda", "Nurota tumanidagi Beklarsoy darasida.")
t.B("Abdullaxon 1582-yil kuzida kimga qarshi jangdan qaytayotib band qurdirgan?", "Bobo Sulton", "Ismoil Safaviy", "Bobur", "Ubaydulla", "Qipchoq dashtidagi Bobo Sultonga qarshi.")
t.B("Abdullaxon bandining qancha qismi saqlanib qolgan?", "uchdan ikki qismi", "yarmi", "to‘liq", "o‘ndan bir qismi", "Uchdan ikki qismi.")
t.B("Samarqand qozilik hujjatlarida nechtadan ortiq hunar turi keltirilgan?", "oltmishdan", "o‘ndan", "yuzdan", "o‘ttizdan", "Oltmishdan ortiq.")
t.B("Hunarmandchilikning eng rivojlangan sohalaridan biri qaysi?", "to‘qimachilik", "kemasozlik", "shishasozlik", "konchilik", "To‘qimachilik.")
t.B("Bobur «atrof va yiroq-yaqinlarga eltadilar» deb maqtagan Samarqand matosi qaysi?", "qirmizi baxmal", "kimxob", "atlas", "chit", "Qirmizi baxmal.")
t.B("Samarqand qog‘oz juvozlariga suv qayerdan kelgan?", "Konigildan", "Oqdaryodan", "Sangzordan", "Chirchiqdan", "Konigildan.")
t.B("Samarqandlik qog‘ozgarlar qog‘ozni nimadan tayyorlagan?", "ipak, yarimipak va paxtadan", "papirusdan", "teridan", "bambukdan", "Ipak (qog‘ozi abrishumi), yarimipak, paxtadan.")
t.B("Ip gazlamalar qatoriga qaysi biri kiradi?", "zandanachi", "kimxob", "zarbof", "tafta", "Bo‘z, olacha, zandanachi, chit.")
t.NAT("Yangi sug‘orish tizimlari barpo etildi, eskilari ta’mirlandi.", "dehqonchilik nisbatan jonlandi", "dehqonchilik inqirozga uchradi", "aholi ko‘chib ketdi", "soliqlar kamaydi", "Dehqonchilik jonlandi.")
t.NAT("Oqchob darasida bahorgi yog‘ingarchilikdan keyin ko‘p suv to‘planar, undan foydalanilmasdi.", "Abdullaxon II u yerda band qurdirishga buyruq berdi", "dara ko‘mib tashlandi", "aholi daradan ko‘chirildi", "suv Zarafshonga burildi", "Abdullaxon bandi qurildi.")
t.NAT("Shayboniyxon qochgan dehqonlarni qaytarib, soliq imtiyozlari berdi.", "davlat xazinasiga tushadigan soliqlar pasayib ketmadi", "xazina bo‘shab qoldi", "dehqonlar qo‘zg‘olon ko‘tardi", "yerlar tashlandiq qoldi", "Soliq tushumi saqlandi.")
t.NAT("Mamlakatda xilma-xil gazlamalar ishlab chiqarildi.", "bu matolarga xorijda ham talab katta bo‘ldi", "matolar faqat saroyda ishlatildi", "gazlama olib kirish ko‘paydi", "to‘qimachilik taqiqlandi", "Xorijda talab yuqori bo‘lgan.")
t.TF("Abdullaxon II 1582-yilda Amir Temurdan o‘rnak olib, toshlardan masjid qurdirgan.", True, "To‘g‘ri.")
t.TF("Tuyatortar arig‘i Murg‘ob daryosidan Marvga chiqarilgan.", False, "Noto‘g‘ri: Tuyatortar Zarafshondan Jizzax vohasiga tortilgan.")
t.TF4([("Puli Karmina XVI asrning ikkinchi yarmida qurilgan.", True), ("Samarqandda rangli qog‘ozlar ham tayyorlangan.", True),
       ("Amudaryodan Chorjo‘ygacha ariq Abdullaxon II davrida chiqarilgan.", True), ("Shayboniylar davrida kemasozlik bo‘lmagan.", False)],
      "4-noto‘g‘ri: kemasozlik ham rivojlangan.")
t.MUL([("Abdullaxon II ning «oltin dubulg‘a»si temirchilar mahoratidan darak beradi.", True),
       ("Aholining asosiy qismi sug‘orma dehqonchilikka qulay vohalarda yashagan.", True),
       ("Abdullaxon bandi Zarafshonning Oqdaryo va Qoradaryoga ayrilish joyida qurilgan.", False)],
      "III noto‘g‘ri: band Oqchob darasida; ayrilish joyidagi suvtaqsimlagichni Shayboniyxon qurdirgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Shayboniyxon Zarafshonda suvtaqsimlagich qurdirdi", "Abdullaxon II Ulug‘tog‘ yodgorlik masjidini qurdirdi", "Oqchob darasida band qurishga buyruq berildi"],
      "XVI asr boshi → 1582-yil may → 1582-yil kuzi.")
t.MATCH("Inshootlarni joylashuvi bilan moslashtiring.", ["Abdullaxon bandi", "Tuyatortar", "Hovuzixon", "suvtaqsimlagich"],
        ["Oqchob darasi (Nurota)", "Zarafshondan Jizzax vohasiga ariq", "Murg‘ob vohasidagi suv ombori", "Oqdaryo va Qoradaryo ayrilishi", "Chirchiq daryosi"], 'abcd',
        "Band – Oqchob; Tuyatortar – Jizzax; Hovuzixon – Murg‘ob; suvtaqsimlagich – Zarafshon ayrilishi.")
t.VENN("Ip gazlamalar", "Ipak gazlamalar",
       [("bo‘z", 1), ("chit", 1), ("atlas", 2), ("kimxob", 2),
        ("xorijda talab katta bo‘lgan matolar", 3)],
       "Bo‘z, chit – ip; atlas, kimxob – ipak; ikkalasiga xorijda talab bo‘lgan.")
t.MAPMATCH('buxamir', ['Nurota', 'Samarqand', 'Chorjo‘y', 'Marv'],
           ["Abdullaxon bandi qoldiqlari saqlangan tuman", "eng yaxshi qog‘oz va qirmizi baxmal shahri", "Amudaryodan ariq chiqarilgan shahar", "Murg‘ob daryosidan ariqlar chiqarilgan shahar"],
           "1 – Nurota; 2 – Samarqand; 3 – Chorjo‘y; 4 – Marv.")
