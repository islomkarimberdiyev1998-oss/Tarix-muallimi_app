from qlib import Topic, PLACES, REG
TOPICS = {}
EU = 'europe'

# 5 XIV–XV asrlarda Angliya
t = Topic('y8j5', 8005); TOPICS['y8j5'] = t
t.B("Angliya qaysi shaharlarga movut eksport qilgan?", "Flandriya va Florensiya", "Lyubek va Gamburg", "Venetsiya va Genuya", "Parij va Lion", "Flandriya va Florensiya shaharlariga.")
t.B("Angliyada birinchi marta jon solig‘i qachon joriy qilingan?", "1377-yilda", "1380-yilda", "1381-yilda", "1399-yilda", "1377-yili parlament joriy qildi.")
t.B("Jon solig‘i necha yoshdan yuqori kishilardan olingan?", "14 yoshdan", "18 yoshdan", "21 yoshdan", "12 yoshdan", "14 yoshdan yuqori barcha erkak va ayollardan.")
t.B("1380-yilda jon solig‘i necha barobar oshirilgan?", "3 barobar", "2 barobar", "5 barobar", "10 barobar", "3 barobarga.")
t.B("Injilni ingliz tiliga tarjima qilgan Oksford professori kim?", "Jon Viklif", "Jon Boll", "Uot Tayler", "Simon de Monfor", "Jon Viklif.")
t.B("«Odam Ato yer haydab, Momo Havo charx yigirgan paytda kim zodagon bo‘lgan?» deb targ‘ib qilgan kim?", "Jon Boll", "Jon Viklif", "Uot Tayler", "Richard II", "Jon Boll.")
t.B("Uot Tayler qo‘zg‘oloni qachon va qayerda boshlangan?", "1381-yil Esseks grafligida", "1358-yil Bove viloyatida", "1377-yil Londonda", "1399-yil Kentda", "1381-yil Esseks grafligida.")
t.B("«Tayler» so‘zi ingliz tilida qanday ma’noni bildiradi?", "tunukasoz", "temirchi", "dehqon", "to‘quvchi", "Tayler – tunukasoz.")
t.B("Qo‘zg‘olonda nechta graflikdan nechtasi qatnashgan?", "40 tadan 25 tasi", "40 tadan 10 tasi", "25 tadan 20 tasi", "100 tadan 40 tasi", "40 ta graflikdan 25 tasi.")
t.B("Qo‘rqib ketgan Richard II qayerga yashiringan?", "Tauer qal’asiga", "Vestminster abbatligiga", "Kenterberiga", "Oksfordga", "Londondagi Tauer qal’asiga.")
t.B("«Mayl End» dasturiga ko‘ra 1 akr yer uchun qancha ijara haqi belgilanishi kerak edi?", "4 pens", "1 funt", "10 pens", "1 shilling", "4 pens.")
t.B("Dehqonlarga cherkov yerlaridan ajratish talabi qaysi dasturda qo‘yilgan?", "«Smitfild»", "«Mayl End»", "«Buyuk xartiya»", "«Sali haqiqati»", "«Smitfild» dasturida.")
t.B("1399-yilda Angliya taxtiga qaysi sulola kelgan?", "Lankasterlar", "Yorklar", "Tyudorlar", "Plantagenetlar", "Lankasterlar sulolasi.")
t.B("«Oq va qizil gullar urushi» qaysi yillarda bo‘lgan?", "1455–1485-yillarda", "1337–1453-yillarda", "1381–1399-yillarda", "1485–1515-yillarda", "1455–1485-yillar, 30 yil.")
t.B("Lankasterlar bayrog‘ida qanday tasvir bo‘lgan?", "qizil atirgul", "oq atirgul", "oq nilufar", "sher", "Lankasterlar – qizil, Yorklar – oq atirgul.")
t.B("Yorklar xonadoni qaysi jangda mag‘lub bo‘lgan?", "1485-yil Bosvort jangida", "1381-yil London jangida", "1455-yil Azenkur jangida", "1415-yil Kresi jangida", "1485-yil Bosvort yaqinida.")
t.B("Yangi sulola asoschisi sifatida taxtga kim o‘tirgan?", "Genrix VII Tyudor", "Eduard IV", "Richard II", "Genrix III", "Genrix VII Tyudor.")
t.NAT("Yevropada qora o‘lat (vabo) tarqaldi.", "aholi katta qismi qirilib, ishchi kuchi kamaydi, rivojlanish to‘xtadi", "aholi tez ko‘paydi", "savdo jonlandi", "dehqonlar boyib ketdi", "Ishchi kuchi kamaydi.")
t.NAT("Qirol qo‘zg‘olonchilar bilan uchrashib, «Mayl End» dasturini qabul qildi.", "bir guruh qo‘zg‘olonchilar va’dalarga ishonib, shaharni tark etdi", "qirol taxtdan voz kechdi", "dehqonlar Londonni egallab qoldi", "parlament tarqatildi", "Bir guruh qo‘zg‘olonchilar ortga qaytdi.")
t.NAT("Ikkinchi muzokara vaqtida Uot Tayler o‘ldirildi.", "rahbarsiz qolgan qo‘zg‘olonchilar haydalib, qo‘zg‘olon bostirildi", "qo‘zg‘olonchilar g‘alaba qozondi", "Richard II asir olindi", "Jon Boll qirol bo‘ldi", "Qo‘zg‘olon bostirildi.")
t.NAT("Uot Tayler qo‘zg‘oloni mag‘lub bo‘lsa-da, dehqonlar taqdirida muhim ahamiyatga ega bo‘ldi.", "XV asr davomida dehqonlar ozodlikni qo‘lga kiritib, erkin dehqonlarga aylandi", "qaramlik kuchaydi", "jon solig‘i 10 barobar oshdi", "dehqonlar yerdan mahrum bo‘ldi", "Dehqonlarga qarshi qonunlar yumshatildi.")
t.TF("Genrix VII Tyudor gerbida qizil va oq atirgullarni birlashtirgan.", True, "To‘g‘ri: u Eduard IV ning qiziga uylangan.")
t.TF("Uot Tayler Yuz yillik urushda qatnashmagan, harbiy tajribasi bo‘lmagan.", False, "Noto‘g‘ri: u Yuz yillik urushda qatnashgan, harbiy qobiliyati bor edi.")
t.TF4([("Jon Viklif Angliyaning papaga soliq to‘lashiga qarshi chiqqan.", True), ("Jon Boll Kenterberi arxiyepiskopi buyrug‘i bilan qamalgan.", True),
       ("Shahar kambag‘allari qo‘zg‘olonchilarga London darvozasini ochmagan.", False), ("Gullar urushida aholining 1/4 qismi qirilib ketgan.", True)],
      "3-noto‘g‘ri: shahar kambag‘allari darvozani ochib bergan.")
t.MUL([("Lordlar ijara haqini pul ko‘rinishida ola boshlagan.", True),
       ("Kent grafligida dehqonlarning yerlari juda kam bo‘lgan.", True),
       ("Jon solig‘i Genrix VII hukmronligi davrida joriy qilingan.", False)],
      "III noto‘g‘ri: Richard II davrida joriy qilingan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Jon solig‘i joriy qilindi", "Jon solig‘i 3 barobar oshirildi", "Uot Tayler qo‘zg‘oloni", "Lankasterlar taxtga keldi", "Gullar urushi boshlandi", "Bosvort jangi"],
      "1377 → 1380 → 1381 → 1399 → 1455 → 1485.")
t.MATCH("Shaxslarni ularga oid ma’lumot bilan moslashtiring.", ["Jon Viklif", "Jon Boll", "Uot Tayler", "Genrix VII Tyudor"],
        ["Injilni ingliz tiliga tarjima qilgan", "«Odam Ato yer haydab...» deb targ‘ib qilgan", "1381-yilgi qo‘zg‘olon rahbari", "Tyudorlar sulolasi asoschisi", "Jakeriya rahbari"], 'abcd',
        "Viklif – Injil; Boll – targ‘ibot; Tayler – qo‘zg‘olon; Genrix VII – Tyudorlar.")
t.VENN("Jakeriya", "Uot Tayler qo‘zg‘oloni",
       [("1358-yilda Fransiyada", 1), ("rahbari Gilyom Kal", 1),
        ("1381-yilda Angliyada", 2), ("«Mayl End» va «Smitfild» dasturlari", 2),
        ("bostirilgan dehqonlar qo‘zg‘oloni", 3)],
       "Jakeriya – 1358, Gilyom Kal; Tayler – 1381, dasturlar; ikkalasi bostirilgan.")
t.MAPMATCH('britain', ['Esseks', 'London', 'Oksford', 'Bosvort'],
           ["1381-yilda qo‘zg‘olon boshlangan graflik", "Richard II Tauer qal’asiga yashiringan shahar", "Jon Viklif professor bo‘lgan universitet shahri", "1485-yilda Yorklar mag‘lub bo‘lgan joy"],
           "1 – Esseks; 2 – London; 3 – Oksford; 4 – Bosvort.")

# 6 Germaniya
t = Topic('y8j6', 8006); TOPICS['y8j6'] = t
t.B("Zamondoshlari «Jahon hayrati» deb atagan imperator kim?", "Fridrix II", "Fridrix I Barbarossa", "Rudolf Gabsburg", "Otton I", "Fridrix II (1194–1250).")
t.B("Fridrix II ning saroyi qaysi shaharda sharqona uslubda bezatilgan?", "Palermo", "Rim", "Axen", "Vena", "Palermodagi saroy.")
t.B("Fridrix II qanday kitob yozgan?", "«Qushlar bilan ov qilish san’ati»", "«Siyosatnoma»", "«Germaniya»", "«Sali haqiqati»", "«Qushlar bilan ov qilish san’ati».")
t.B("Fridrix II qaysi universitetga asos solgan?", "Neapol universiteti", "Boloniya universiteti", "Parij universiteti", "Oksford universiteti", "Neapol universiteti – hukmdor asos solgan birinchi universitet.")
t.B("Fridrix II ni yeretik deb e’lon qilgan papa kim?", "Grigoriy IX", "Innokentiy IV", "Bonifatsiy VIII", "Urban II", "Papa Grigoriy IX.")
t.B("Fridrix II qachon vafot etgan?", "1250-yilda", "1248-yilda", "1273-yilda", "1194-yilda", "1250-yilda.")
t.B("Germaniyada qaysi yillarda umuman imperator saylanmagan?", "1254–1273-yillarda", "1347–1437-yillarda", "1250–1254-yillarda", "1437–1806-yillarda", "1254–1273-yillarda.")
t.B("1273-yilda knyazlar kimni imperator qilib saylagan?", "Rudolf Gabsburgni", "Fridrix II ni", "Otton I ni", "Lyuksemburgni", "Rudolf Gabsburgni.")
t.B("Gabsburglar taxtni 1347-yilda qaysi xonadonga bo‘shatib bergan?", "Lyuksemburglar", "Shtaufenlar", "Tyudorlar", "Kapetinglar", "Lyuksemburglarga.")
t.B("Imperatorni saylagan yetti nafar oliy saylovchi qanday atalgan?", "kurfyurstlar", "lordlar", "konunglar", "markgraflar", "Kurfyurstlar.")
t.B("Gabsburglar Germaniyada qachongacha hukmronlik qilgan?", "1806-yilgacha", "1437-yilgacha", "1648-yilgacha", "1918-yilgacha", "1437–1806-yillar, 369 yil.")
t.B("XV asr 60-yillarida Prussiya kimning hukmronligiga o‘tgan?", "Polsha qirolining", "Daniyaning", "Chexiyaning", "Gabsburglarning", "Polsha qiroli hukmronligiga.")
t.B("Shimoliy Germaniya shaharlarining savdo ittifoqi qanday atalgan?", "Ganza", "Reyn ittifoqi", "Shvabiya ittifoqi", "Lombardiya ittifoqi", "Ganza savdo ittifoqi.")
t.B("XV asr boshlarida Ganza ittifoqi qancha shaharni birlashtirgan?", "160 ga yaqin", "90 ta", "70 ta", "300 ta", "160 ga yaqin shahar.")
t.B("Ganza ittifoqining asosiy raqobatchisi kim edi?", "Daniya qirolligi", "Angliya", "Polsha", "Rossiya", "Daniya qirolligi.")
t.B("Reyn savdo va sanoat ittifoqi qachon tashkil topgan?", "1254-yilda", "1331-yilda", "1370-yilda", "1273-yilda", "1254-yilda.")
t.B("Shvabiya ittifoqi qachon tashkil topgan?", "1331-yilda", "1254-yilda", "1370-yilda", "1437-yilda", "1331-yilda; 90 ta shahar.")
t.NAT("Papa va cherkov Fridrix II vorislarining taxtga da’vosini tan olmadi.", "Shtaufenlar sulolasi hukmronligi barham topdi", "Shtaufenlar yanada kuchaydi", "papa imperator bo‘ldi", "Germaniya Italiyaga qo‘shildi", "Shtaufenlar sulolasi tugadi.")
t.NAT("Germaniyada markaziy hokimiyat bo‘lmadi, siyosiy tarqoqlik hukm surdi.", "XV asrda imperiya o‘z yerlaridan birin-ketin ayrila boshladi", "Germaniya Yevropaning eng kuchli davlati bo‘ldi", "imperator mutlaq hukmdorga aylandi", "Ganza ittifoqi tarqaldi", "Prussiya, Shlezvig-Golshteyn ajraldi; Chexiya va Shveysariya mustaqil bo‘ldi.")
t.NAT("1370-yilda Ganza ittifoqi Daniyaga jiddiy zarba berdi.", "Daniya qiroli ittifoq ishlariga aralashmaslikka, boj kamaytirishga rozi bo‘ldi", "Ganza tarqatildi", "Daniya Ganzaga qo‘shildi", "Lyubek Daniyaga o‘tdi", "Tovarlardan olinadigan boj kamaytirildi.")
t.NAT("Fridrix II Sitsiliyada yashab, Germaniyada feodallar shartlariga yon bosdi.", "Germaniyada hokimiyat amalda yirik feodallar qo‘lida bo‘ldi", "Germaniya markazlashdi", "feodallar imperatorga to‘liq bo‘ysundi", "Germaniya Sitsiliyaga qo‘shildi", "Hokimiyat feodallar qo‘lida edi.")
t.TF("Ganza ittifoqi «Ko‘hna qit’a»ni iqtisodiy birlashtirgan dastlabki Yevropa ittifoqi edi.", True, "To‘g‘ri.")
t.TF("Germaniya imperatorida umumimperiya qo‘shini, soliqlar va markaziy sud tizimi bo‘lgan.", False, "Noto‘g‘ri: bularning hech biri yo‘q edi.")
t.TF4([("Kurfyurstlarning to‘rt nafari dunyoviy knyazlar bo‘lgan.", True), ("Gabsburglar Ispaniya toj-taxtini nikoh diplomatiyasi orqali qo‘lga kiritgan.", True),
       ("Shvabiya ittifoqi Shimoliy dengizdagi port shaharlardan iborat bo‘lgan.", False), ("Fridrix II arab va yunon tillarida so‘zlasha olgan.", True)],
      "3-noto‘g‘ri: Shvabiya ittifoqi Yuqori Dunay bo‘yidagi 90 ta shahardan iborat edi.")
t.MUL([("Fridrix II 1248-yilda papa bilan urushda mag‘lub bo‘lgan.", True),
       ("Lyuksemburglar sulolasi vakili Chexiya imperatori ham bo‘lgan.", True),
       ("Reyn ittifoqiga Lyubek, Gamburg va Bremen kirgan.", False)],
      "III noto‘g‘ri: Reyn ittifoqiga Frankfurt, Mayns, Kyoln, Vorms, Strasburg kirgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Fridrix II vafot etdi", "Reyn ittifoqi tuzildi", "Rudolf Gabsburg imperator bo‘ldi", "Shvabiya ittifoqi tuzildi", "Lyuksemburglar taxtga keldi", "Ganza Daniyaga zarba berdi", "Gabsburglar taxtga qaytdi"],
      "1250 → 1254 → 1273 → 1331 → 1347 → 1370 → 1437.")
t.MATCH("Ittifoqlarni ularga kirgan shaharlar bilan moslashtiring.", ["Ganza", "Reyn ittifoqi", "Shvabiya ittifoqi"],
        ["Lyubek, Gamburg, Bremen", "Frankfurt, Mayns, Kyoln", "Augsburg, Ulm, Nyurnberg", "Milan, Genuya, Venetsiya"], 'abc',
        "Ganza – Lyubek; Reyn – Kyoln; Shvabiya – Augsburg.")
t.VENN("Ganza ittifoqi", "Shvabiya ittifoqi",
       [("Shimoliy Germaniya port shaharlari", 1), ("Daniya bilan raqobat", 1),
        ("Yuqori Dunay bo‘yidagi 90 shahar", 2), ("Venetsiyada savdo markazlari", 2),
        ("Germaniya shaharlari ittifoqi", 3)],
       "Ganza – shimoliy portlar, Daniya; Shvabiya – Dunay, Venetsiya; ikkalasi shaharlar ittifoqi.")
t.MAPMATCH(EU, ['Lyubek', 'Kyoln', 'Augsburg', 'Palermo'],
           ["Ganza savdo ittifoqining shimoliy shahri", "Reyn savdo va sanoat ittifoqi shahri", "Shvabiya ittifoqining gazlama va qurol ishlab chiqargan shahri", "Fridrix II ning sharqona saroyi joylashgan shahar"],
           "1 – Lyubek; 2 – Kyoln; 3 – Augsburg; 4 – Palermo.")

# 7 Italiya
t = Topic('y8j7', 8007); TOPICS['y8j7'] = t
t.B("Italiyaning eng yirik savdo markazlari bo‘lgan shahar-respublikalar qaysilar?", "Genuya va Venetsiya", "Milan va Florensiya", "Rim va Neapol", "Palermo va Piza", "Genuya va Venetsiya.")
t.B("«Sitsiliya oqshomi» qachon bo‘lgan?", "1282-yilda", "1298-yilda", "1378-yilda", "1252-yilda", "1282-yili sitsiliyaliklar ajnabiylarni qirib tashladi.")
t.B("Venetsiyani qanday atashgan?", "«Adriatika malikasi»", "«Italiya Afinasi»", "«boqiy shahar»", "«oltin ko‘prik»", "«Adriatika malikasi».")
t.B("XIII asrda Venetsiyada qancha aholi yashagan?", "200 ming", "90 ming", "1 mln", "50 ming", "200 ming aholi.")
t.B("Venetsiya respublikasini kim boshqargan?", "saylab qo‘yiladigan doj", "qirol", "papa", "adolat bayroqdori", "Saylab qo‘yiladigan doj.")
t.B("Venetsiyaning Yevropada xalqaro pul vazifasini bajargan tangasi qaysi?", "oltin dukat", "florin", "numisma", "dinor", "Oltin dukatlar.")
t.B("Venetsiya Genuya flotini qachon tamomila mag‘lub qilgan?", "1380-yilda", "1298-yilda", "1282-yilda", "1409-yilda", "1380-yilda.")
t.B("Dojlar saroyi qaysi yillarda hozirgi ko‘rinishga keltirilgan?", "1309–1424-yillarda", "IX asrda", "1252–1282-yillarda", "1418–1500-yillarda", "1309–1424-yillarda.")
t.B("Florensiya qaysi daryo sohilida joylashgan?", "Arno", "Po", "Tibr", "Dunay", "Arno daryosi sohillarida.")
t.B("Florensiyani qanday ta’riflashgan?", "«Italiya Afinasi»", "«Adriatika malikasi»", "«Yevropa ustaxonasi»", "«oltin ko‘prik»", "«Italiya Afinasi».")
t.B("Florensiya sanoatining asosiy boyligi nima edi?", "movut", "shisha", "qurol", "tuz", "Movut.")
t.B("Florensiya birinchi bo‘lib oltin tanga zarb qilishni qachon boshlagan?", "1252-yilda", "1330-yilda", "1282-yilda", "1380-yilda", "1252-yilda.")
t.B("Florensiya respublikasining oliy organi qanday atalgan?", "sinyoriya", "senat", "kortes", "parlament", "Sinyoriya.")
t.B("Sinyoriya boshlig‘i qanday atalgan?", "adolat bayroqdori", "doj", "konsul", "senator", "Adolat bayroqdori; qo‘shinning bosh qo‘mondoni.")
t.B("1298-yilda genuyaliklarga asir tushgan venetsiyalik sayyoh kim?", "Marko Polo", "Klavixo", "Vasko da Gama", "Kolumb", "Marko Polo.")
t.B("1378-yilda italiyalik kardinallar kimni papa qilib saylagan?", "Urban VI ni", "Kliment VII ni", "Aleksandr V ni", "Martin V ni", "Urban VI – Rimda; Kliment VII – Avinyonda.")
t.B("«Buyuk bo‘linish»ga qachon barham berilgan?", "1418-yilda", "1409-yilda", "1378-yilda", "1377-yilda", "1418-yilda Martin V saylangach.")
t.NAT("1377-yilda papa Grigoriy XI Rimga qaytib, 1378-yilda vafot etdi.", "italiyalik va fransuz kardinallari ikki papa sayladi", "papalik tugatildi", "papa qarorgohi Parijga ko‘chdi", "Venetsiya papani sayladi", "Katolik cherkovida ikki papa hukmronligi boshlandi.")
t.NAT("1409-yilda Pizadagi yig‘inda Aleksandr V papa qilib saylandi, ikki papa voz kechmadi.", "katolik cherkovida rasman uchta papa bo‘ldi – «Buyuk bo‘linish»", "bitta papa qoldi", "cherkov pravoslav cherkoviga qo‘shildi", "papalar Avinyonga ko‘chdi", "Uch papa hukmronlik qildi.")
t.NAT("1380-yilda Venetsiya Genuya flotini mag‘lub etdi.", "Genuyaning O‘rta dengiz sharqidagi hukmronligi barham topdi, Venetsiya Qora dengizga chiqdi", "Genuya Venetsiyani bosib oldi", "Venetsiya Genuyaga qo‘shildi", "savdo to‘xtadi", "Venetsiya floti Qora dengizga kirish huquqini oldi.")
t.NAT("Sitsiliyadagi fransuz amaldorlari arab mamlakatlari bilan savdoga ziyon yetkazdi.", "1282-yilda «Sitsiliya oqshomi» qo‘zg‘oloni bo‘ldi", "Sitsiliya Fransiyaga to‘liq qo‘shildi", "arablar Sitsiliyani egalladi", "savdo gullab-yashnadi", "Sitsiliyaliklar ajnabiylarni qirib tashladi.")
t.TF("Rim papalari o‘z boyliklarini Florensiya banklarida saqlagan.", True, "To‘g‘ri.")
t.TF("Italiyaning markazidagi Papa davlatida savdo va hunarmandchilik eng rivojlangan edi.", False, "Noto‘g‘ri: Papa davlati qoloq hudud edi.")
t.TF4([("Genuya respublikasi 1797-yilgacha mavjud bo‘lgan.", True), ("Korsika Genuya respublikasi tarkibida bo‘lgan.", True),
       ("XIV asrda Florensiyada 200 dan ortiq movut korxonasi bo‘lgan.", True), ("Italiya dehqonlarining ozod bo‘lishi boshqa Yevropa mamlakatlariga nisbatan sekin kechgan.", False)],
      "4-noto‘g‘ri: Italiyada qaramlikning bekor bo‘lishi tezroq va osonroq kechgan.")
t.MUL([("XV asrdan Kipr oroli Venetsiya tarkibiga kirgan.", True),
       ("1330-yilda Florensiyada 90 ming aholi yashagan.", True),
       ("Marko Polo kitobini Venetsiyada doj bo‘lganida yozgan.", False)],
      "III noto‘g‘ri: u Genuya asirligida sayohati tarixini aytib bergan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Florensiya oltin tanga zarb qildi", "«Sitsiliya oqshomi»", "Genuyaliklar Venetsiya flotini yengdi", "Ikki papa saylandi", "Venetsiya Genuya flotini yengdi", "Pizada yig‘in", "«Buyuk bo‘linish» tugadi"],
      "1252 → 1282 → 1298 → 1378 → 1380 → 1409 → 1418.")
t.VENN("Venetsiya", "Florensiya",
       [("«Adriatika malikasi»", 1), ("doj boshqargan", 1),
        ("«Italiya Afinasi»", 2), ("sinyoriya boshqargan", 2),
        ("Italiya shahar-respublikasi", 3)],
       "Venetsiya – Adriatika malikasi, doj; Florensiya – Italiya Afinasi, sinyoriya; ikkalasi shahar-respublika.")
t.MAPMATCH('italy', ['Venetsiya', 'Genuya', 'Florensiya', 'Palermo'],
           ["«Adriatika malikasi» – doj boshqargan respublika", "shimoli-g‘arbdagi, Korsikani egallagan dengiz respublikasi", "Arno bo‘yidagi «Italiya Afinasi»", "1282-yilda «Sitsiliya oqshomi» bo‘lgan orol shahri"],
           "1 – Venetsiya; 2 – Genuya; 3 – Florensiya; 4 – Palermo.")

# 8 Ispaniya va Portugaliya
t = Topic('y8j8', 8008); TOPICS['y8j8'] = t
t.B("Arab xalifaligi Pireney yarimorolidagi Vestgot qirolligini qachon bo‘ysundirgan?", "711–714-yillarda", "756-yilda", "1238-yilda", "905-yilda", "711–714-yillarda.")
t.B("XII asrda Pireney yarimorolida qaysi davlatlar yuzaga kelgan?", "Kastiliya, Navarra, Aragon, Portugaliya", "Granada va Qurdoba", "Leon va Sitsiliya", "Andorra va Gibraltar", "Kastiliya, Navarra, Aragon va Portugaliya.")
t.B("Granada amirligi qachon tashkil topgan?", "1238-yilda", "1492-yilda", "756-yilda", "1137-yilda", "1238-yildan.")
t.B("Granada amirligining qulashi bilan qaysi jarayon yakunlangan?", "rekonkista", "salib yurishlari", "Buyuk bo‘linish", "Yuz yillik urush", "Rekonkista.")
t.B("Navarra davlatining poytaxti qaysi shahar bo‘lgan?", "Pamplona", "Toledo", "Lissabon", "Granada", "Pamplona.")
t.B("Navarrani 1512-yilda kim bosib olgan?", "aragonlik Ferdinand", "Izabella", "Alfonso X", "Pedro I", "Aragonlik Ferdinand.")
t.B("Yevropadagi toifa vakillarining ilk yig‘ini qanday atalgan?", "kortes", "parlament", "General shtatlar", "sinyoriya", "Kastiliyadagi kortes.")
t.B("Kortesning birinchi yig‘ilishi qachon chaqirilgan?", "1137-yilda", "1188-yilda", "1302-yilda", "1265-yilda", "1137-yilda Kastiliyada.")
t.B("«Huquqning yetti bo‘limi» qonunlar to‘plamini kim yaratgan?", "Alfonso X", "Pedro I", "Ferdinand", "Sancho I", "Qirol Alfonso X.")
t.B("Alfonso X davrida qaysi maktab Yevropa tarjimashunosligining beshigiga aylangan?", "Toledo maktabi", "Salamanka maktabi", "Koimbra maktabi", "Kordova maktabi", "Toledo maktabi.")
t.B("Yuz yillik urushda Angliyaning ittifoqchisi bo‘lgan Kastiliya qiroli kim?", "Pedro I", "Alfonso X", "Genrix III", "Ferdinand", "Pedro I.")
t.B("Ferdinand va Izabella qachon turmush qurgan?", "1469-yilda", "1492-yilda", "1512-yilda", "1403-yilda", "1469-yilda.")
t.B("Portugaliya mustaqilligini kim e’lon qilgan?", "Afonso Enrikesh", "Vimara Peresh", "Dinish", "Xuan I", "1139-yilda qirol Afonso Enrikesh.")
t.B("Lissabon qachondan Portugaliya poytaxti bo‘lgan?", "1225-yildan", "1139-yildan", "868-yildan", "1279-yildan", "1225-yildan.")
t.B("Koimbra universitetiga qaysi qirol asos solgan?", "Dinish", "Sancho I", "Afonso II", "Xuan I", "Qirol Dinish.")
t.B("1498-yilda Hindistonni kashf etgan portugal dengizchisi kim?", "Vasko da Gama", "Pedro Kabral", "Kolumb", "Klavixo", "Vasko da Gama; 1500-yilda Kabral Braziliyani.")
t.B("Amir Temur huzuriga 1403-yilda yuborilgan Kastiliya elchisi kim?", "Rui Gonsales de Klavixo", "Payo Sotomayor", "Ernan Sanches", "Muhammadqozi", "Rui Gonsales de Klavixo.")
t.B("Klavixo Samarqandga qachon yetib borgan?", "1404-yil avgustda", "1403-yil mayda", "1406-yil martda", "1402-yilda", "1404-yil avgustda.")
t.NAT("1469-yilda Ferdinand va Izabella turmush qurdi.", "Kastiliya va Aragon yagona qirollikka aylanib, yagona Ispaniyaga asos solindi", "Kastiliya Portugaliyaga qo‘shildi", "Aragon mustaqil qoldi", "Granada kengaydi", "Yagona Ispaniya vujudga keldi.")
t.NAT("1492-yilda Granada amirligi quladi.", "uning hududi Kastiliya tojining bir qismiga aylandi, rekonkista yakunlandi", "arablar butun Ispaniyani egalladi", "Portugaliya Granadani oldi", "Navarra mustaqil bo‘ldi", "Rekonkista yakunlandi.")
t.NAT("Kastiliyada dehqonlar arablarga qarshi kurashda jonbozlik ko‘rsatdi.", "zamindorlar yon berib, dehqonlar nisbatan ertaroq qaramlikdan qutuldi", "dehqonlar qaramligi kuchaydi", "dehqonlar yerdan mahrum bo‘ldi", "kortes tarqatildi", "Dehqonlar ertaroq ozod bo‘ldi.")
t.NAT("Klavixo 1406-yilda hisobotini qirolga topshirdi.", "hisobot «Buyuk Temur tarixi» kabi nomlar bilan Ispaniya va Yevropada nashr etildi", "hisobot yo‘qolib ketdi", "Kastiliya Temur davlatiga qo‘shildi", "elchilik aloqalari uzildi", "«Esdaliklar» ko‘p tillarga tarjima qilindi.")
t.TF("Granada Yevropadagi so‘nggi arab davlati bo‘lgan.", True, "To‘g‘ri.")
t.TF("Aragonda qirol hokimiyati juda kuchli bo‘lgan.", False, "Noto‘g‘ri: Aragonda qirol hokimiyati juda zaif, parokandalik hukm surgan.")
t.TF4([("Kortesda 1188-yildan shaharliklar va dehqonlar vakillari ham qatnashgan.", True), ("Alfonso X Salamanka universitetida rasadxona qurdirgan.", True),
       ("Klavixo «Esdaliklar»i birinchi marta 1582-yilda Sevilyada chop etilgan.", True), ("Navarra XIII–XV asrlarda Pireneyning eng qudratli davlati bo‘lgan.", False)],
      "4-noto‘g‘ri: Navarra iqtisodiy qoloq bo‘lib, katta ta’sirga ega bo‘lmagan.")
t.MUL([("Sitsiliya, Sardiniya va Neapol Aragon tarkibiga kirgan.", True),
       ("Portugaliya grafligi 868-yilda Vimara Peresh boshchiligida tuzilgan.", True),
       ("Amir Temur Kastiliya elchilarini qabul qilishdan bosh tortgan.", False)],
      "III noto‘g‘ri: Sohibqiron ularni yaxshi qabul qilib, o‘z elchisini maktub va sovg‘alar bilan yuborgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Kortesning birinchi yig‘ilishi", "Portugaliya mustaqilligi e’lon qilindi", "Granada amirligi tuzildi", "Klavixo Samarqandga yetib bordi", "Ferdinand va Izabella turmush qurdi", "Granada qo‘shib olindi", "Navarra qo‘shib olindi"],
      "1137 → 1139 → 1238 → 1404 → 1469 → 1492 → 1512.")
t.MATCH("Shaxslarni ularga oid ma’lumot bilan moslashtiring.", ["Alfonso X", "Afonso Enrikesh", "Vasko da Gama", "Rui Gonsales de Klavixo"],
        ["«Huquqning yetti bo‘limi» muallifi", "Portugaliyaning birinchi qiroli", "1498-yilda Hindistonni kashf etgan", "Amir Temur huzuriga borgan elchi", "Braziliyani kashf etgan"], 'abcd',
        "Alfonso X – qonunlar; Afonso Enrikesh – birinchi qirol; Vasko da Gama – Hindiston; Klavixo – elchi.")
t.VENN("Kastiliya", "Portugaliya",
       [("Alfonso X ning «Huquqning yetti bo‘limi»", 1), ("Izabella vatani", 1),
        ("poytaxti 1225-yildan Lissabon", 2), ("Vasko da Gama Hindistonga yetgan", 2),
        ("kortes faoliyat yuritgan Pireney davlati", 3)],
       "Kastiliya – Alfonso X, Izabella; Portugaliya – Lissabon, Vasko da Gama; ikkalasida kortes.")
t.MAPMATCH('iberia', ['Granada', 'Toledo', 'Pamplona', 'Lissabon'],
           ["1492-yilgacha Yevropadagi so‘nggi arab davlati markazi", "Alfonso X davrida tarjimashunoslik maktabi markazi", "Navarra davlatining poytaxti", "1225-yildan Portugaliya poytaxti"],
           "1 – Granada; 2 – Toledo; 3 – Pamplona; 4 – Lissabon.")
