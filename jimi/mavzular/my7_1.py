from qlib import Topic, PLACES, REG
TOPICS = {}
EU = 'europe'

# 1 German qabilalari va Rim imperiyasi
t = Topic('y7j1', 7001); TOPICS['y7j1'] = t
t.B("German qabilalarining ko‘chishlari qaysi asrlarda bo‘lgan?", "milodiy IV–VI asrlarda", "milodiy I–II asrlarda", "VIII–IX asrlarda", "X–XI asrlarda", "Milodiy IV–VI asrlarda.")
t.B("German qabilalari haqidagi ilk yozma ma’lumotlar qaysi asarlarda keltirilgan?", "Yuliy Sezar va Korneliy Tatsit asarlarida", "Boetsiy asarlarida", "«Sali haqiqati»da", "Gomer dostonlarida", "Sezarning «Galliya urushi haqida xotiralar» va Tatsitning «Germaniya» asarlarida.")
t.B("German qabilalari qaysi daryolar oralig‘ida yashagan?", "Reyndan Elbagacha", "Dunaydan Dneprgacha", "Sena va Luara oralig‘ida", "Nil va Furot oralig‘ida", "Reyndan Elba daryosigacha bo‘lgan hududlarda.")
t.B("Germanlar rimliklarga qaysi mahsulotni yetkazib bergan?", "qahrabo", "shisha idishlar", "qimmatbaho matolar", "bronza idishlar", "Qullar, chorva mollari, teri, qahrabo.")
t.B("Germanlarda xalq yig‘inida saylanadigan zodagon qabila boshliqlari qanday atalgan?", "konunglar", "graflar", "gersoglar", "markgraflar", "Konunglar – qabila boshliqlari.")
t.B("Germanlarda oliy hokimiyat organi nima hisoblangan?", "barcha qurollangan erkin erkaklar xalq majlisi", "qirol saroyi", "kohinlar kengashi", "senat", "Xalq majlisi oliy hokimiyat organi edi.")
t.B("Germanlardagi harbiy bo‘linmalar qanday atalgan?", "drujina", "legion", "marka", "falanga", "Harbiy bo‘linmalar – drujina.")
t.B("Rim imperiyasi qachon G‘arbiy va Sharqiy qismlarga bo‘lingan?", "395-yilda", "410-yilda", "476-yilda", "418-yilda", "395-yili.")
t.B("Rim inqirozining eng asosiy sababi nima edi?", "qullar mehnatining past darajasi", "germanlarning xristianlikni qabul qilishi", "savdoning to‘xtashi", "Vizantiya bosqini", "Qullar ishlab chiqarish o‘sishidan manfaatdor bo‘lmagan.")
t.B("Xalqlarning buyuk ko‘chishini qaysi ko‘chmanchi qabilalar tezlashtirgan?", "xunnlar", "franklar", "sakslar", "langobardlar", "Sharqdan yurish boshlagan xunn qabilalari.")
t.B("410-yilda Rimni egallagan vestgotlar sarkardasi kim?", "Alarix", "Odoakr", "Teodorix", "Xlodvig", "Alarix boshchiligida.")
t.B("Ilk varvar qirolligi – Vestgot qirolligi qachon tuzilgan?", "418-yilda", "410-yilda", "476-yilda", "395-yilda", "418-yili janubi-g‘arbiy Galliyada.")
t.B("G‘arbiy Rimning so‘nggi imperatori kim?", "Romul Avgustul", "Teodorix", "Odoakr", "Alarix", "476-yili Odoakr Romul Avgustulni taxtdan ag‘dardi.")
t.B("Ostgot qirolligining poytaxti qaysi shahar bo‘lgan?", "Ravenna", "Rim", "Konstantinopol", "Milan", "Ravenna.")
t.B("Ostgotlar qiroli Teodorixning bosh vaziri kim bo‘lgan?", "Boetsiy", "Alarix", "Tatsit", "Odoakr", "Rimlik faylasuf Boetsiy.")
t.NAT("Xunnlar ta’qibidan qochgan vestgotlar imperiya qo‘shinlarini tor-mor etdi.", "imperiya o‘zini o‘nglay olmadi va 410-yilda Rim egallandi", "imperiya kuchaydi", "vestgotlar xunnlarga bo‘ysundi", "Rim Vizantiyaga qo‘shildi", "Shu mag‘lubiyatdan so‘ng imperiya o‘zini o‘nglay olmadi.")
t.NAT("476-yili Odoakr so‘nggi imperatorni taxtdan ag‘dardi.", "Yevropada qulchilikdan feodal jamiyatga o‘tish boshlandi", "Rim imperiyasi tiklandi", "qulchilik kuchaydi", "Ostgotlar Rimdan haydaldi", "Bu sana feodal jamiyatga o‘tish boshlanishini anglatadi.")
t.NAT("Omochdan temir plugga o‘tildi, almashlab ekish usuli joriy etildi.", "mehnat unumdorligi va hosil ortdi", "dehqonchilik to‘xtadi", "germanlar chorvachilikdan voz kechdi", "qishloqlar yo‘qoldi", "Mehnat unumdorligi oshdi, hosil ortdi.")
t.NAT("Ostgotlar va rimliklar o‘rtasida kelishmovchilik, Vizantiya istilolari davom etdi.", "VI asr o‘rtalarida Ostgot qirolligi quladi", "Ostgot qirolligi kuchaydi", "Rim imperiyasi tiklandi", "Boetsiy qirol bo‘ldi", "VI asr o‘rtalarida qirollik quladi, keyin langobardlar kirib keldi.")
t.TF("Germanlar tabiat kuchlari – osmon, momaqaldiroq, shamol va yerni ilohiylashtirgan.", True, "To‘g‘ri.")
t.TF("Germanlarning mustahkam, bir-biriga yaqin qurilgan qishloqlari bo‘lgan.", False, "Noto‘g‘ri: har bir oila alohida xo‘jalikda yashagan.")
t.TF4([("Vestgotlar Rimni uch kun talagan.", True), ("Vandal va alanlar Shimoliy Afrikada joylashgan.", True),
       ("Anglosakslar Italiyada davlat tuzgan.", False), ("Langobardlar Shimoliy Italiyada qirollik tuzgan.", True)],
      "3-noto‘g‘ri: anglosakslar Britaniya orollarida joylashgan.")
t.MUL([("IV–V asrlarda alemann, got, franklarning yirik qabila ittifoqlari shakllangan.", True),
       ("Germanlar kundalik hayotda nondan ko‘ra sut, pishloq va go‘shtni ko‘proq iste’mol qilgan.", True),
       ("Odoakr imperatorlik nishonlarini Ravennaga yuborishni buyurgan.", False)],
      "III noto‘g‘ri: nishonlar Konstantinopolga yuborildi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Rim imperiyasi ikkiga bo‘lindi", "Vestgotlar Rimni egalladi", "Vestgot qirolligi tuzildi", "Romul Avgustul taxtdan ag‘darildi"],
      "395 → 410 → 418 → 476.")
t.MATCH("Qabilalarni ular joylashgan hududlar bilan moslashtiring.", ["vestgotlar", "ostgotlar", "franklar", "anglosakslar"],
        ["janubi-g‘arbiy Galliya", "Italiya", "Galliya", "Britaniya orollari", "Kichik Osiyo"], 'abcd',
        "Vestgotlar – janubi-g‘arbiy Galliya; ostgotlar – Italiya; franklar – Galliya; anglosakslar – Britaniya.")
t.VENN("Vestgotlar", "Ostgotlar",
       [("410-yilda Rimni egallagan", 1), ("418-yilda ilk varvar qirolligini tuzgan", 1),
        ("poytaxti Ravenna bo‘lgan", 2), ("qiroli Teodorix", 2),
        ("german qabilasi", 3)],
       "Vestgotlar – 410, 418; ostgotlar – Ravenna, Teodorix; ikkalasi german qabilasi.")
t.MAPMATCH('medit', ['Rim', 'Ravenna', 'Konstantinopol', 'Shimoliy Afrika'],
           ["410-yilda vestgotlar uch kun talagan «boqiy shahar»", "Ostgot qirolligining poytaxti", "476-yilda imperatorlik nishonlari yuborilgan shahar", "vandal va alanlar davlat tuzgan hudud"],
           "1 – Rim; 2 – Ravenna; 3 – Konstantinopol; 4 – Shimoliy Afrika.")

# 2–3 Franklar davlati
t = Topic('y7j2-3', 7002); TOPICS['y7j2-3'] = t
t.B("Frank qabilalari dastlab qayerda yashagan?", "Reyn daryosining quyi qismida", "Elba bo‘yida", "Pireney yarimorolida", "Italiyada", "Reyn daryosining quyi qismida.")
t.B("Xlodvig qo‘shini 486-yili qaysi shahar yaqinida Rim qo‘shinini yengan?", "Suasson", "Puate", "Verden", "Axen", "486-yili Suasson yaqinida.")
t.B("Xlodvig qaysi sulolaga asos solgan?", "Merovinglar", "Karolinglar", "Kapetinglar", "Robertinlar", "Merovinglar sulolasiga.")
t.B("Xlodvigning buyrug‘i bilan bitilgan qonunlar to‘plami qanday atalgan?", "«Sali haqiqati»", "«Germaniya»", "«Galliya urushi haqida xotiralar»", "Verden shartnomasi", "Lotin tilida bitilgan «Sali haqiqati».")
t.B("Xlodvig xristian dinini qachon qabul qilgan?", "496-yilda", "486-yilda", "732-yilda", "751-yilda", "496-yili Rim cherkovi tartiblari bo‘yicha.")
t.B("Karl Martell arablarni qaysi jangda to‘xtatgan?", "732-yilgi Puate jangida", "486-yilgi Suasson jangida", "843-yilgi Verden jangida", "Rim jangida", "Yetti kun davom etgan 732-yilgi Puate jangida.")
t.B("«Martell» laqabi qanday ma’noni anglatadi?", "«Bolg‘a»", "«Pakana»", "«Buyuk»", "«Sher»", "«Martell» – «Bolg‘a».")
t.B("Harbiy xizmat sharti bilan muddatga beriladigan yer qanday atalgan?", "benefitsiy", "feod", "marka", "domen", "Benefitsiy («ehson», «yaxshilik»).")
t.B("X asrga kelib benefitsiy nimaga aylangan?", "feodga – merosiy yer-mulkka", "jamoa yeriga", "qirol domeniga", "cherkov yeriga", "Merosiy yer-mulk – feodga aylandi.")
t.B("Pipin Pakana qachon franklar qiroli deb e’lon qilingan?", "751-yilda", "732-yilda", "768-yilda", "800-yilda", "751-yili Suassondagi yig‘ilishda.")
t.B("Papaning dunyoviy davlati (hozirgi Vatikan) qachon vujudga kelgan?", "756-yilda", "751-yilda", "800-yilda", "843-yilda", "756-yili.")
t.B("Buyuk Karl franklar davlatini necha yil boshqargan?", "46 yil", "53 yil", "30 yil", "64 yil", "768–814-yillar – 46 yil.")
t.B("Buyuk Karl hukmronligida nechta harbiy yurish olib borilgan?", "53 ta", "46 ta", "12 ta", "100 ta", "53 ta harbiy yurish.")
t.B("Franklarning eng uzoq va og‘ir urushlari kimlarga qarshi olib borilgan?", "sakslarga", "langobardlarga", "arablarga", "vestgotlarga", "772–804-yillarda sakslarga qarshi.")
t.B("Buyuk Karlga imperatorlik tojini qachon kiygizilgan?", "800-yil dekabrda", "768-yilda", "814-yilda", "751-yilda", "800-yil dekabrida Rimda.")
t.B("«Yangi Rim imperiyasi»ning markazi qaysi shahar bo‘lgan?", "Axen", "Parij", "Rim", "Suasson", "Axen shahri.")
t.B("Chegara viloyatlari qanday atalgan?", "markalar", "grafliklar", "domenlar", "benefitsiylar", "Markalar; ularni markgraflar boshqargan.")
t.B("Verden shartnomasi qachon tuzilgan?", "843-yilda", "814-yilda", "987-yilda", "800-yilda", "843-yili.")
t.B("987-yilda Fransiya qiroli deb kim e’lon qilingan?", "Gugo Kapet", "Lyudovik V", "Filipp II", "Lyudovik VI", "Robertinlardan graf Gugo Kapet; Kapetinglar sulolasi boshlandi.")
t.NAT("Xlodvig 496-yili xristian dinini qabul qildi.", "qirol hokimiyati va Rim papasi boshchiligidagi g‘arbiy cherkov ittifoqi ta’minlandi", "franklar majusiylikka qaytdi", "Franklar davlati parchalandi", "rim-gallar franklardan ajralib ketdi", "Franklar va rim-gallar yagona xalqqa aylana bordi.")
t.NAT("Xlodvig mamlakat hududlarini o‘g‘illariga taqsimlab berdi.", "keyinchalik davlat parchalanib ketdi", "davlat mustahkamlandi", "imperiya tashkil topdi", "Karolinglar hokimiyatga keldi", "Bu keyinchalik davlatning parchalanishiga sabab bo‘ldi.")
t.NAT("843-yilda Verden shartnomasi tuzildi.", "imperiya uchga bo‘linib, Fransiya, Germaniya va Italiya tashkil topdi", "imperiya kengaydi", "Karl imperator bo‘ldi", "Kapetinglar ag‘darildi", "Imperiya uchga bo‘lindi.")
t.NAT("Karl Martell otliq jangchilarga benefitsiy taqsimladi.", "feodallar toifasi shakllanib, ritsarlik asoslari yaratildi", "piyoda lashkar asosiy kuchga aylandi", "cherkov yerlari ko‘paydi", "arablar g‘alaba qozondi", "Benefitsiy islohoti feodallar toifasini shakllantirdi.")
t.TF("Franklar tuzgan davlat X asrda Il-de-Frans nomidan Fransiya deb atala boshlagan.", True, "To‘g‘ri.")
t.TF("Pipin Pakana otasining cherkov yerlarini musodara qilish siyosatini kuchaytirgan.", False, "Noto‘g‘ri: u bu siyosatdan voz kechib, cherkov bilan yaqinlashdi.")
t.TF4([("Karl Arab xalifaligi hukmronligidagi Ispaniyada Ispan markasini tuzgan.", True), ("Horun ar-Rashid Karlga qimmatbaho tuhfalar yuborgan.", True),
       ("Karolinglar sulolasi 486–751-yillarda hukmronlik qilgan.", False), ("Kapetinglar dastlab faqat Il-de-Frans gersogligida hukmronlik qilgan.", True)],
      "3-noto‘g‘ri: 486–751 – Merovinglar; Karolinglar 751–987-yillarda.")
t.MUL([("Franklarda yozish uchun faqat lotin tili qo‘llanilgan.", True),
       ("Yirik qabilalarni gersoglar, kichik hududlarni graflar boshqargan.", True),
       ("Lyudovik VII Burgundiya merosxo‘riga uylanib domenini kengaytirgan.", False)],
      "III noto‘g‘ri: u Akvitaniya merosxo‘ri Eleonoraga uylangan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Suasson yaqinidagi g‘alaba", "Xlodvig xristianlikni qabul qildi", "Puate jangi", "Pipin qirol deb e’lon qilindi", "Karlga imperatorlik toji kiygizildi", "Verden shartnomasi", "Gugo Kapet qirol bo‘ldi"],
      "486 → 496 → 732 → 751 → 800 → 843 → 987.")
t.MATCH("Hukmdorlarni ularga oid ma’lumot bilan moslashtiring.", ["Xlodvig", "Karl Martell", "Pipin Pakana", "Buyuk Karl"],
        ["Merovinglar sulolasi asoschisi", "Puate jangi g‘olibi", "papa davlatining vujudga kelishiga yordam bergan", "«Yangi Rim imperiyasi» asoschisi", "Kapetinglar sulolasi asoschisi"], 'abcd',
        "Xlodvig – Merovinglar; Martell – Puate; Pipin – papa davlati; Buyuk Karl – imperiya.")
t.VENN("Merovinglar", "Karolinglar",
       [("asoschisi Xlodvig", 1), ("«Sali haqiqati»", 1),
        ("Puate jangi va benefitsiy islohoti avlodi", 2), ("800-yilda imperiya tuzilgan", 2),
        ("franklar sulolasi", 3)],
       "Merovinglar – Xlodvig, Sali haqiqati; Karolinglar – Pipin, Karl; ikkalasi franklar sulolasi.")
t.MAPMATCH('france', ['Suasson', 'Puate', 'Verden', 'Axen'],
           ["486-yilda Xlodvig Rim qo‘shinini yenggan shahar", "732-yilda arablar to‘xtatilgan jang joyi", "843-yilda imperiyani bo‘lgan shartnoma tuzilgan shahar", "«Yangi Rim imperiyasi» markazi"],
           "1 – Suasson; 2 – Puate; 3 – Verden; 4 – Axen.")
