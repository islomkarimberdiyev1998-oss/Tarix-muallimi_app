from qlib import Topic
TOPICS = {}
W = 'globe'; EU = 'europe'; ME = 'mideast'; OA = 'oldasia'

# 17 Usmoniylar
t = Topic('e8j17', 817); TOPICS['e8j17'] = t
t.B("XVI asr boshida Usmoniylar imperiyasida viloyatlar nimalarga bo‘lingan?", "sanjoq (tuman)larga", "beklik", "amlok", "uyezd", "Viloyatlar sanjoqlarga bo‘lingan.")
t.B("Viloyatni kim boshqargan?", "vali", "sanjoqbey", "sipohiy", "vazir", "Viloyatlarni vali, sanjoqlarni sanjoqbey boshqargan.")
t.B("Harbiy majburiyat evaziga yer olgan otliq askarlar qanday atalgan?", "sipohiylar", "yanicharlar", "samuraylar", "daymyolar", "Sulton yerlarni sipohiylarga taqsimlab bergan.")
t.B("Usmoniylarning muntazam piyoda qo‘shini qanday atalgan?", "yanicharlar", "sipohiylar", "mamluklar", "navkarlar", "Yanicharlar – «yangi qo‘shin».")
t.B("Sulton Salim I Ismoil Safaviy qo‘shinini qachon tor-mor etgan?", "1514-yilda", "1517-yilda", "1502-yilda", "1684-yilda", "1514-yili Salim I Eron qo‘shinini tor-mor etdi.")
t.B("Usmoniylar Qohirani qachon egallagan?", "1517-yilda", "1514-yilda", "1453-yilda", "1529-yilda", "1517-yili Misr poytaxti Qohira egallandi.")
t.B("Osiyoda Usmoniylarning eng yirik raqibi kim edi?", "Eron", "Hindiston", "Xitoy", "Buxoro", "Eron imperiyaning Osiyodagi eng yirik raqibi edi.")
t.B("Yevropa davlatlari Turkiyaga qarshi «Muqaddas liga»ni qachon tuzgan?", "1684-yilda", "1683-yilda", "1700-yilda", "1774-yilda", "1684-yili «Muqaddas liga» tuzildi.")
t.B("Fransiya savdogarlari uchun qancha bojxona to‘lovi joriy etilgan?", "3 foiz", "10 foiz", "25 foiz", "1 foiz", "Fransiya savdogarlari uchun atigi 3 foiz boj joriy etildi.")
t.B("XVIII asrda Turkiya qaysi davlat bilan bir necha bor urushib, yengilgan?", "Rossiya", "Fransiya", "Angliya", "Eron", "Turkiya Rossiya bilan urushlarda yengildi.")
t.B("«Sayohatnoma» asarining muallifi kim?", "Avliyo Chalabiy", "Koshib Chalabiy", "Sinon", "Xizr Xalifa", "Avliyo Chalabiyning «Sayohatnoma»si.")
t.B("XVI asrning buyuk turk me’mori kim?", "Sinon", "Avliyo Chalabiy", "Behzod", "Mustafo Koshipzoda", "Buyuk me’mor Sinon.")
t.B("Bag‘dod va Ravon ko‘shklari qaysi saroyda joylashgan?", "To‘pqopi", "Ali Kapa", "Chexel Sotun", "Versal", "Sultonning To‘pqopi saroyida.")
t.NAT("Salim I Eron shohini yengdi (1514).", "Misr sultonligiga qarshi yurishga yo‘l ochildi", "Eron Turkiyani bosib oldi", "Turkiya Yevropadan chekindi", "Misr Turkiyaga hujum qildi",
      "Bu g‘alaba Eron ittifoqchisi Misrga yurishga yo‘l ochdi; 1517-yilda Qohira olindi.")
t.NAT("Dehqonlar xonavayron bo‘lib, ko‘plab qochib ketdi.", "XVI asr o‘rtalaridan qishloq xo‘jaligi inqirozi va harbiy qudrat zaiflashuvi boshlandi", "Turkiya boyidi", "shaharlar bo‘shab qoldi", "yanicharlar kuchaydi",
      "Qishloq xo‘jaligi inqirozi Turkiya harbiy qudratining zaiflashishiga olib keldi.")
t.NAT("Yevropa savdogarlariga imtiyozlar berildi.", "Turkiya bozorlari Yevropa tovarlariga to‘lib, mahalliy hunarmandchilikka zarba berildi", "turk hunarmandlari boyidi", "Turkiya eksportni ko‘paytirdi", "Yevropa savdosi to‘xtadi",
      "Bu mahalliy hunarmandchilikka qattiq zarba berdi.")
t.TF("Sulton qochgan dehqonlarni majburan qaytarish huquqini yer egalariga bergan.", True, "To‘g‘ri.")
t.TF("XVII asrdan Turkiyada dunyoviy fanlar asosan Bag‘dodda rivojlangan.", False, "Noto‘g‘ri: asosan poytaxt Istanbulda.")
t.MUL([("Usmoniylar Afrikada ham mustamlakalarga ega bo‘lgan.", True), ("Turkiya Rossiyaga qarshi Angliya va Fransiyaga yaqinlashgan.", True), ("Yevropa madaniyati ta’sirida turk madaniyati milliyligini butunlay yo‘qotgan.", False)],
      "III noto‘g‘ri: turk madaniyati asosan milliylikni saqlab qoldi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Salim I Eron qo‘shinini yengdi", "Qohira egallandi", "Vena ostonasida mag‘lubiyat", "«Muqaddas liga» tuzildi"],
      "1514 → 1517 → 1683 → 1684.")
t.MAPMATCH(OA, ['Istanbul', 'Qohira', 'Suriya', 'Tabriz'],
           ["Usmoniylar poytaxti", "1517-yilda egallangan Misr poytaxti", "Salim I Misrdan oldin bosib olgan hudud", "Ismoil Safaviy poytaxti"],
           "1 – Istanbul; 2 – Qohira; 3 – Suriya; 4 – Tabriz.")
t.VENN("Sipohiylar", "Yanicharlar",
       [("otliq askarlar", 1), ("harbiy majburiyat evaziga yer olgan", 1),
        ("muntazam piyoda qo‘shin", 2), ("«yangi qo‘shin» deb atalgan", 2),
        ("Usmoniylar harbiy kuchi", 3)],
       "Sipohiylar – otliq, yer egasi; yanicharlar – piyoda. Ikkalasi Usmoniylar qo‘shini.")

# 18 Eron
t = Topic('e8j18', 818); TOPICS['e8j18'] = t
t.B("Eronni yagona davlatga birlashtirgan Ardabil hokimi kim?", "Ismoil Safaviy", "Abbos I", "Nodirshoh", "Og‘a Muhammad", "Ardabil hokimi Ismoil Safaviy.")
t.B("Ismoil I o‘zini qachon shahanshoh deb e’lon qilgan?", "1502-yilda", "1514-yilda", "1587-yilda", "1736-yilda", "1502-yili Tabrizni olib, shahanshoh deb e’lon qildi.")
t.B("Safaviylar davlatining dastlabki poytaxti qaysi shahar?", "Tabriz", "Isfahon", "Tehron", "Sheroz", "Poytaxt etib Tabriz belgilandi.")
t.B("Ismoil I suyurg‘ol o‘rniga qanday yer egaligini joriy etgan?", "tiyul", "iqto", "tanho", "vaqf", "Suyurg‘ol o‘rniga tiyul joriy etildi.")
t.B("Abbos I qaysi yillarda hukmronlik qilgan?", "1587–1629", "1502–1524", "1736–1747", "1722–1736", "Abbos I davri – 1587–1629.")
t.B("Abbos I poytaxtni qayerga ko‘chirgan?", "Isfahonga", "Tehronga", "Tabrizga", "Sherozga", "Poytaxt Tabrizdan Isfahonga ko‘chirildi.")
t.B("1710-yilda dehqonlarning yerni tashlab ketishini taqiqlagan shoh kim?", "Sulton Husayn", "Abbos I", "Taxmasp II", "Ismoil I", "Shoh Sulton Husayn farmon chiqardi.")
t.B("Afg‘onlar Eronga qachon hujum qilgan?", "1722-yilda", "1710-yilda", "1736-yilda", "1747-yilda", "1722-yili afg‘onlar Mir Mahmud boshchiligida hujum qildi.")
t.B("Afg‘onlar yetakchisi kim edi?", "Mir Mahmud", "Nodir Quli", "Taxmasp II", "Og‘a Muhammad", "Afg‘onlar yetakchisi Mir Mahmud.")
t.B("Nodir Quli o‘zini Eron shohi deb qachon e’lon qilgan?", "1736-yilda", "1722-yilda", "1747-yilda", "1758-yilda", "1736-yili qurultoyda Nodirshoh deb e’lon qilindi.")
t.B("Nodirshoh qachon o‘ldirilgan?", "1747-yilda", "1736-yilda", "1758-yilda", "1796-yilda", "1747-yili ichki nizolar natijasida o‘ldirildi.")
t.B("Zend qabilasi qachon g‘alaba qozongan?", "1758-yilda", "1747-yilda", "1796-yilda", "1736-yilda", "1758-yili zendlar g‘alaba qozondi.")
t.B("Qojarlar hokimiyatni qachon egallagan?", "1796-yilda", "1758-yilda", "1747-yilda", "1925-yilda", "1796-yili hokimiyatni qojarlar egalladi.")
t.B("Qojarlar davrida poytaxt qaysi shaharga ko‘chirilgan?", "Tehron", "Isfahon", "Tabriz", "Mashhad", "Poytaxt Tehron shahriga ko‘chirildi.")
t.B("Qojarlar sulolasi qachongacha hukmronlik qilgan?", "1925-yilgacha", "1796-yilgacha", "1911-yilgacha", "1979-yilgacha", "Qojarlar 1925-yilgacha hukmronlik qildi.")
t.B("Ismoil I Safaviy qaysi taxallus bilan she’r yozgan?", "Xatoiy", "Soib", "Nodir", "Hasaniy", "Shoir Xatoiy – Ismoil I Safaviy.")
t.B("Eron miniatura san’atining markazi qaysi shahar edi?", "Isfahon", "Tabriz", "Tehron", "Hirot", "Isfahon miniatura san’atining markaziga aylandi.")
t.NAT("Tiyul yerlar ko‘paydi.", "davlat yerlari va xazina daromadi kamaydi", "xazina boyidi", "dehqonlar yer egasiga aylandi", "suyurg‘ol tiklandi",
      "Bu iqtisodiy inqirozga olib keldi.")
t.NAT("Abbos I yirik yer egalarining mustaqilligini tugatdi.", "Safaviylar davlati qudratining cho‘qqisiga erishdi", "davlat parchalandi", "afg‘onlar Eronni egalladi", "Turkiya Eronni bosib oldi",
      "Abbos I davrida davlat cho‘qqiga erishdi.")
t.NAT("Nodirshoh 1747-yilda o‘ldirildi.", "imperiya bir necha qismga bo‘linib, taxt uchun kurash avj oldi", "imperiya kuchaydi", "safaviylar qaytdi", "afg‘onlar hokimiyatni oldi",
      "Zend va qojar qabilalari o‘rtasida kurash boshlandi.")
t.TF("Tiyul yerlarni meros qoldirish mumkin bo‘lmagan.", True, "To‘g‘ri.")
t.TF("Abbos I soliqlarni oshirgan va savdoni cheklagan.", False, "Noto‘g‘ri: soliqlarni kamaytirgan, savdo va hunarmandchilikni rivojlantirgan.")
t.MUL([("Isfahondagi Shoh masjidi va Chexel Sotun saroyi mashhur.", True), ("Miniatura rivojiga Hirotdagi Behzod maktabi ta’sir ko‘rsatgan.", True), ("Taxmasp II xalqni bosqinchilarga qarshi muvaffaqiyatli kurashga chorlagan.", False)],
      "III noto‘g‘ri: Taxmasp II amalda hokimiyatga ega emasdi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Ismoil I shahanshoh bo‘ldi", "Abbos I taxtga chiqdi", "Afg‘onlar hujumi", "Nodirshoh shoh bo‘ldi", "Zendlar g‘alabasi", "Qojarlar hokimiyatni oldi"],
      "1502 → 1587 → 1722 → 1736 → 1758 → 1796.")
t.MAPMATCH(OA, ['Ardabil', 'Isfahon', 'Tehron'],
           ["Ismoil Safaviy hokim bo‘lgan shahar", "Abbos I ko‘chirgan poytaxt", "qojarlar poytaxti"], "1 – Ardabil; 2 – Isfahon; 3 – Tehron.")
t.VENN("Ismoil I Safaviy", "Abbos I",
       [("1502-yilda shahanshoh deb e’lon qilgan", 1), ("Xatoiy taxallusi bilan she’r yozgan", 1),
        ("poytaxtni Isfahonga ko‘chirgan", 2), ("muntazam qo‘shin barpo etgan", 2),
        ("Safaviylar sulolasi hukmdori", 3)],
       "Ismoil I: 1502, Xatoiy. Abbos I: Isfahon, qo‘shin. Ikkalasi safaviy.")

AF = 'africa'
# 19 Afrika
t = Topic('e8j19', 819); TOPICS['e8j19'] = t
t.B("Shimoliy Afrika arab mamlakatlari qachondan islom ta’sirida rivojlangan?", "VII asrdan", "XVI asrdan", "X asrdan", "I asrdan", "Ular VII asrdan islom dini va madaniyati ta’sirida rivojlandi.")
t.B("Misrda turklar bosqinidan oldin kimlar hukmron edi?", "mamluklar", "fotimiylar", "ayyubiylar", "ispanlar", "Misr mamluklar hukmronligi ostida edi.")
t.B("Salim I armiyasi Qohirani qachon egallagan?", "1517-yil boshida", "1514-yilda", "1551-yilda", "1574-yilda", "1517-yilning boshida Qohira egallandi.")
t.B("XVIII asr oxirida Qohirada chet el bilan savdo qiluvchi nechta savdogar bo‘lgan?", "5 mingta", "500 ta", "50 mingta", "1 mingta", "5 mingta savdogar faoliyat yuritgan.")
t.B("Misrda turk va mamluk zulmiga qarshi harakatga qaysi masjid shayxlari boshchilik qilgan?", "al-Azhar", "Shoh masjidi", "Sulaymoniya", "Umaviylar", "Qohiradagi al-Azhar masjidi shayxlari.")
t.B("Napoleon qo‘shinlari Misrga qachon bostirib kirgan?", "1798-yilda", "1795-yilda", "1800-yilda", "1517-yilda", "1798-yili fransuz qo‘shinlari bostirib kirdi.")
t.B("Fransuzlar Misrni qachon tark etgan?", "1800-yilda", "1798-yilda", "1805-yilda", "1795-yilda", "1800-yili fransuzlar Misrni tark etdi.")
t.B("Jazoirda ispanlarga qarshi harakatga boshchilik qilgan sarkarda kim?", "Xayriddin", "Salim I", "Mir Mahmud", "Nodir", "Sarkarda Xayriddin Turkiyadan yordam so‘radi.")
t.B("Salim I Xayriddinga qanday unvon bergan?", "beklarbegi (beylerbeyi)", "sanjoqbey", "vali", "posho", "Xayriddinga beklarbegi unvoni berildi.")
t.B("Tripoli ispanlar tomonidan qachon zabt etilgan?", "1510-yilda", "1551-yilda", "1574-yilda", "1517-yilda", "1510-yili Tripoli ispanlar tomonidan zabt etildi.")
t.B("Turklar butun Liviyani qachon imperiyaga qo‘shib olgan?", "1551-yilda", "1510-yilda", "1574-yilda", "1517-yilda", "1551-yili Liviya qo‘shib olindi.")
t.B("Turk qo‘shini Tunisda ispanlar hukmronligiga qachon xotima bergan?", "1574-yilda", "1551-yilda", "1510-yilda", "1600-yilda", "1574-yili 40 ming kishilik turk qo‘shini kelib tushdi.")
t.B("Qaysi Shimoliy Afrika davlatlari mustaqilligini saqlab qolgan?", "Sudan va Marokash", "Misr va Liviya", "Jazoir va Tunis", "Misr va Sudan", "Sudan va Marokash mustaqilligini saqlab qoldi.")
t.B("XVI asr oxirigacha qul savdosi bilan faqat kimlar shug‘ullangan?", "portugallar", "gollandlar", "inglizlar", "fransuzlar", "XVI asr oxirigacha faqat portugallar shug‘ullangan.")
t.B("XVII asrdan qul savdosida kim yetakchilik qilgan?", "gollandlar", "portugallar", "ispanlar", "arablar", "XVII asrdan gollandlar yetakchilik qildi.")
t.B("Volta va Niger daryolari oralig‘idagi qirg‘oq qanday atalgan?", "Qul qirg‘og‘i", "Oltin qirg‘oq", "Fil Suyagi qirg‘og‘i", "Qalampir qirg‘og‘i", "Volta va Niger oralig‘i Qul qirg‘og‘i deb atalgan.")
t.B("XVI–XVIII asrlarda yevropaliklar Amerikaga qancha qul olib kelgan?", "15–16 million", "1–2 million", "60–70 million", "100 million", "15–16 million qul olib kelindi.")
t.B("Atlantika orqali qul savdosida qancha afrikalik halok bo‘lgan?", "60–70 million", "15–16 million", "5 million", "1 million", "60–70 million afrikalik halok bo‘ldi.")
t.NAT("Amerikada plantatsiya xo‘jaliklari kengaydi, mahalliy hindular qirilib ketdi.", "G‘arbiy Afrika katta qul bozoriga aylantirildi", "qul savdosi to‘xtadi", "Afrika boyidi", "Amerikaga yevropalik dehqonlar ko‘chdi",
      "Ishchi kuchiga ehtiyoj G‘arbiy Afrikani qul bozoriga aylantirdi.")
t.NAT("Al-Azhar shayxlari da’vati bilan 1795-yil Qohira hunarmandlari do‘konlarini yopdi.", "mamluk hukmdorlari zo‘ravonlikni to‘xtatishga va’da berdi", "turklar Misrni tark etdi", "Napoleon Misrga keldi", "shayxlar qatl etildi",
      "Mamluk hukmdorlari muzokaraga majbur bo‘ldi.")
t.NAT("Qul savdosi keng rivojlandi.", "irqchilik mafkurasi shakllanib, inson hayoti qadrsizlandi", "Afrika jamiyati tenglashdi", "qabilaviy tuzum mustahkamlandi", "Afrika aholisi ko‘paydi",
      "Qul savdosining og‘ir oqibatlaridan biri irqchilik mafkurasi bo‘ldi.")
t.TF("Turklar istilosi Misrdagi ijtimoiy-iqtisodiy munosabatlarni tubdan o‘zgartirgan.", False, "Noto‘g‘ri: katta o‘zgarish kiritmadi, faqat mamluklar siyosiy hokimiyati ag‘darildi.")
t.TF("Bristol, Liverpul, Nant kabi shaharlarning gullashi qul savdosi foydasi bilan bog‘liq bo‘lgan.", True, "To‘g‘ri.")
t.MUL([("1434–1482-yillarda Yashil burundan Kongo daryosigacha qirg‘oqlar o‘rganilgan.", True), ("Portugallar dastlab G‘arbiy Afrikadan oltin olib ketgan.", True), ("Jazoir Istanbulga to‘liq bo‘ysunib, mustaqil siyosat yuritmagan.", False)],
      "III noto‘g‘ri: Jazoir podshosi deyarli mustaqil siyosat olib bordi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Ispanlar Tripolini egalladi", "Turklar Qohirani egalladi", "Liviya imperiyaga qo‘shildi", "Turklar Tunisga keldi", "Napoleon Misrga bostirib kirdi"],
      "1510 → 1517 → 1551 → 1574 → 1798.")
t.MAPMATCH(AF, ['Qohira', 'Jazoir', 'Tripoli', 'Marokash'],
           ["1517-yilda Salim I egallagan shahar", "Xayriddin ispanlardan ozod qilgan mamlakat", "1510-yilda ispanlar zabt etgan Liviya shahri", "mustaqilligini saqlab, savdodan foyda olgan davlat"],
           "1 – Qohira; 2 – Jazoir; 3 – Tripoli; 4 – Marokash.")
t.VENN("Shimoliy Afrika (XVI–XVIII)", "G‘arbiy Afrika (XVI–XVIII)",
       [("ko‘p qismi Usmoniylarga qo‘shilgan", 1), ("islom sivilizatsiyasi doirasida rivojlangan", 1),
        ("ulkan qul bozoriga aylantirilgan", 2), ("Qul, Oltin, Fil Suyagi qirg‘oqlari", 2),
        ("yevropaliklar kirib kelgan hudud", 3)],
       "Shimoliy: Usmoniylar, islom. G‘arbiy: qul savdosi. Ikkalasiga yevropaliklar kirib kelgan.")

# 20 Buyuk Britaniya 1800–1870
t = Topic('e8j20', 820); TOPICS['e8j20'] = t
t.B("1816-yilda Buyuk Britaniyada mashinalar necha kishining qo‘l mehnatiga teng ish bajargan?", "150 million", "12 million", "300 million", "50 million", "Mashinalar 150 million odam mehnatiga teng ishni bajarardi.")
t.B("O‘sha davrda Buyuk Britaniya aholisi qancha bo‘lgan?", "12 million", "150 million", "30 million", "300 million", "Aholi 12 million kishi edi.")
t.B("Dunyodagi ilk temiryo‘l qachon qurilgan?", "1825-yilda", "1816-yilda", "1832-yilda", "1867-yilda", "1825-yili Buyuk Britaniyada qurildi.")
t.B("Sanoat to‘ntarishining tugallanishi nimani anglatadi?", "bir mashina yordamida boshqa mashina yaratilishini", "temiryo‘l qurilishini", "manufaktura paydo bo‘lishini", "qishloq xo‘jaligi yetakchiligini", "Bir mashina bilan boshqa mashina yaratila boshlanishi.")
t.B("Buyuk Britaniyada sanoat to‘ntarishi qachon tugallangan?", "XIX asrning 40-yillarida", "XVIII asr oxirida", "1825-yilda", "XIX asr oxirida", "XIX asrning 40-yillarida.")
t.B("Yoqilg‘ining eng muhim turi nimaga aylangan?", "toshko‘mir", "neft", "o‘tin", "gaz", "Toshko‘mir eng muhim yoqilg‘iga aylandi.")
t.B("Ish tashlashni taqiqlovchi qonun qachon qabul qilingan?", "1825-yilda", "1832-yilda", "1836-yilda", "1867-yilda", "1825-yili parlament bunday qonun qabul qildi.")
t.B("Birinchi parlament islohoti qachon o‘tkazilgan?", "1832-yilda", "1825-yilda", "1867-yilda", "1836-yilda", "1832-yili parlament islohoti o‘tkazildi.")
t.B("1832-yilgi islohotga ko‘ra sanoat markazlariga parlamentdan nechta o‘rin berilgan?", "144 ta", "12 ta", "300 ta", "50 ta", "Yirik sanoat markazlariga 144 o‘rin ajratildi.")
t.B("Yangi parlament 13 yoshgacha bolalar uchun qancha ish vaqti belgilagan?", "8 soat", "12 soat", "6 soat", "10 soat", "13 yoshgacha bolalarga 8 soatlik ish vaqti belgilandi.")
t.B("Necha yoshgacha bo‘lgan bolalar mehnati taqiqlangan?", "9 yoshgacha", "13 yoshgacha", "7 yoshgacha", "16 yoshgacha", "9 yoshgacha bolalar mehnati taqiqlandi.")
t.B("«Umumiy saylov huquqi uchun kurash ishchi assotsiatsiyasi» qachon tuzilgan?", "1836-yilda", "1832-yilda", "1848-yilda", "1867-yilda", "1836-yili Londonda tuzildi.")
t.B("Umumiy saylov huquqi uchun harakat qanday nom bilan tarixga kirgan?", "chartistlar harakati", "luddistlar harakati", "trade-yunionlar", "puritanlar", "Bu harakat «chartistlar harakati» nomi bilan kirdi.")
t.B("Ikkinchi parlament islohoti qachon o‘tkazilgan?", "1867-yilda", "1832-yilda", "1848-yilda", "1884-yilda", "1867-yili ikkinchi islohot o‘tkazildi.")
t.B("Buyuk Britaniyaning eng yirik mustamlakasi qaysi?", "Hindiston", "Kanada", "Avstraliya", "Misr", "Hindistonda 300 million aholi yashardi.")
t.B("Kanadaga dominion maqomi qachon berilgan?", "1867-yilda", "1832-yilda", "1825-yilda", "1876-yilda", "1867-yili Kanadaga dominion maqomi berildi.")
t.B("«Dominion» so‘zi nimani anglatadi?", "o‘zini o‘zi boshqaradigan qaram o‘lka", "harbiy baza", "mustaqil davlat", "qirollik yerlari", "Dominion – o‘zini o‘zi boshqaradigan qaram yer.")
t.NAT("Temiryo‘l qurilishi boshlandi.", "cho‘yan, temir, po‘latga ehtiyoj oshib, parovozsozlik paydo bo‘ldi", "metallurgiya to‘xtadi", "dengiz savdosi yo‘qoldi", "ichki bozor torydi",
      "Temiryo‘l yangi tarmoq – parovozsozlikni vujudga keltirdi.")
t.NAT("1825-yilda ish tashlashni taqiqlovchi qonun qabul qilindi.", "ishchilar noroziligi kuchayib, parlament islohoti zaruratga aylandi", "ishchilar rozi bo‘ldi", "chartistlar g‘alaba qozondi", "parlament tarqatildi",
      "Norozilik 1832-yilgi islohotga olib keldi.")
t.TF("Jahon tarixida birinchi marta Buyuk Britaniyada iqtisodda yetakchilik qishloq xo‘jaligidan sanoatga o‘tgan.", True, "To‘g‘ri.")
t.TF("Chartistlar harakati g‘alaba bilan yakunlangan.", False, "Noto‘g‘ri: harakat yengilgan, lekin keyingi islohotlarga ta’sir qilgan.")
t.MUL([("Quyi palata hukumatga ishonchsizlik bildirsa, hukumat iste’foga chiqishi shart bo‘lgan.", True), ("Kanada, Avstraliya, Yangi Zelandiya «oq mustamlakalar» edi.", True), ("1867-yilgi islohot ayollarga ham saylov huquqini bergan.", False)],
      "III noto‘g‘ri: islohot o‘z uyiga ega erkaklarga saylov huquqi bergan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Ilk temiryo‘l qurildi", "Birinchi parlament islohoti", "Chartistlar assotsiatsiyasi tuzildi", "Ikkinchi parlament islohoti"],
      "1825 → 1832 → 1836 → 1867.")
t.MAPMATCH(W, ['Kanada', 'Hindiston', 'Avstraliya', 'Yangi Zelandiya'],
           ["1867-yilda dominion maqomini olgan «oq mustamlaka»", "300 million aholili eng yirik mustamlaka", "Okeaniyadagi «oq mustamlaka» – qit’a", "Avstraliya yonidagi orol «oq mustamlaka»"],
           "1 – Kanada; 2 – Hindiston; 3 – Avstraliya; 4 – Yangi Zelandiya.")
t.VENN("1832-yilgi islohot", "1867-yilgi islohot",
       [("sanoat markazlariga 144 o‘rin berilgan", 1), ("quyi palata roli oshgan", 1),
        ("shaharlarda uyi bor erkaklarga saylov huquqi", 2), ("chartistlar harakatidan keyin o‘tkazilgan", 2),
        ("Buyuk Britaniya parlament islohoti", 3)],
       "1832: 144 o‘rin. 1867: uy egalari saylov huquqi. Ikkalasi parlament islohoti.")
