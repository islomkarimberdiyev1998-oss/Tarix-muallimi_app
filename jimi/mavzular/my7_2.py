from qlib import Topic, PLACES, REG
TOPICS = {}
EU = 'europe'

# 4 Britaniyadan – Angliyaga
t = Topic('y7j4', 7004); TOPICS['y7j4'] = t
t.B("Mil. avv. I ming yillikda Britaniyada qaysi kelt qabilalari yashagan?", "brittlar", "angllar", "sakslar", "yutlar", "Kelt qabilalari – brittlar.")
t.B("Rimliklar Britaniya orollarining katta qismini qachondan bosib olgan?", "milodiy 43-yildan", "407-yildan", "milodiy 1-yildan", "mil. avv. 55-yildan", "Milodiy 43-yildan; deyarli 400 yillik hukmronlik.")
t.B("London qaysi daryo sohilida barpo etilgan?", "Temza", "Reyn", "Sena", "Elba", "Temza daryosi sohilida.")
t.B("Rim legioni Britaniyadan qachon Italiyaga qaytgan?", "407-yilda", "43-yilda", "476-yilda", "829-yilda", "407-yilda.")
t.B("Brittlar pikt va skottlardan himoyalanish uchun kimlardan yordam so‘ragan?", "anglosakslardan", "rimliklardan", "franklardan", "daniyaliklardan", "Angl, saks, yut va friz qabilalaridan.")
t.B("Anglosakslarga qarshi brittlarni birlashtirgan so‘nggi rimlik kim?", "Amvrosiy Avrelian", "Ekbert", "Alfred", "Kanut", "Amvrosiy Avrelian; dostonlarda Artur deb atalgan.")
t.B("Istilodan qochgan brittlar Armorika viloyatiga qanday nom bergan?", "Bretan", "Normandiya", "Uels", "Akvitaniya", "Bretan nomini berishgan.")
t.B("Anglosaks qirolliklarida qonunlarni tasdiqlagan oliy organ qanday atalgan?", "«Donolar kengashi»", "Davra stoli", "xalq majlisi", "senat", "Zodagonlardan iborat «Donolar kengashi».")
t.B("Grafliklarni qirol vakili sifatida kimlar idora qilgan?", "sheriflar", "lordlar", "konunglar", "markgraflar", "Sheriflar.")
t.B("829-yilda anglosaks qirolliklarini birlashtirgan Uesseks hukmdori kim?", "Ekbert", "Alfred", "Eduard", "Vilgelm", "Ekbert.")
t.B("Normannlarni Rusda qanday atashgan?", "varyaglar", "vikinglar", "vengerlar", "pikt", "Rusda – varyaglar.")
t.B("Normannlar Londonni qachon bosib olib, yondirgan?", "842-yilda", "838-yilda", "879-yilda", "1013-yilda", "842-yilda.")
t.B("Normannlar hujumini qaytargan qirol kim?", "Buyuk Alfred", "Ekbert", "Kanut", "Genrix I", "Buyuk Alfred (871–900).")
t.B("Alfred joriy qilgan doimiy soliq qanday atalgan?", "«daniyaliklar puli»", "«qalqon puli»", "ushr", "jizya", "«Daniyaliklar puli».")
t.B("Alfred davrida muhim voqealar yilma-yil qayd etilgan asar qaysi?", "«Anglosakson solnomasi»", "«Alfred haqiqati»", "«Sali haqiqati»", "«Germaniya»", "250 yil davomida bitilgan «Anglosakson solnomasi».")
t.B("Daniya qiroli Kanut Angliyani qachon zabt etgan?", "1013-yilda", "1066-yilda", "842-yilda", "879-yilda", "1013-yili.")
t.B("1066-yilda Angliyaga qo‘shin tushirgan Normandiya gersogi kim?", "Vilgelm I", "Kanut", "Genrix II", "Eduard", "Vilgelm I; Gastings jangi.")
t.B("Baronlarga harbiy xizmat o‘rniga to‘lanadigan soliq qanday atalgan?", "«qalqon puli»", "«daniyaliklar puli»", "benefitsiy", "desyatina", "Genrix II davridagi «qalqon puli».")
t.NAT("Anglosakslar V–VI asrlarda mahalliy brittlarni bo‘ysundirdi.", "angllar tili ustunlikka erishib, mamlakat Angliya nomini oldi", "kelt tili davlat tili bo‘ldi", "Britaniya Rimga qaytdi", "brittlar butun orolni qaytarib oldi", "Istilochilar tili ingliz, mamlakat Angliya nomini oldi.")
t.NAT("Qirol Alfred 879-yilda normannlarni shartnoma tuzishga majbur etdi.", "ingliz yerlarida tinchlik qaror topib, ilm-fan rivojlandi", "normannlar Londonni egalladi", "Angliya Daniyaga qo‘shildi", "anglosaks qirolliklari parchalandi", "Tinchlik va madaniy yuksalish boshlandi.")
t.NAT("Kanut vafot etdi.", "u tuzgan yirik davlat parchalanib, ingliz taxtiga Eduard keldi", "Daniya Angliyani to‘liq egalladi", "Vilgelm I qirol bo‘ldi", "Alfred hokimiyatga qaytdi", "Davlat parchalandi, Eduard anglosaks hukmronligini tikladi.")
t.NAT("Genrix II baronlarga «qalqon puli» to‘lashga ruxsat berdi.", "qirol muntazam yollanma qo‘shin tuzish imkoniga ega bo‘ldi", "baronlar kuchaydi", "qirol hokimiyati zaiflashdi", "Angliya Fransiyaga qo‘shildi", "Qirol hokimiyati kuchaydi.")
t.TF("Vikinglar Daniya, Norvegiya hududlarida yashagan skandinaviyaliklar bo‘lgan.", True, "To‘g‘ri.")
t.TF("Vilgelm I ingliz tilida so‘zlashgan, inglizlar uni xursandchilik bilan qarshi olgan.", False, "Noto‘g‘ri: u eski fransuz tilida gapirgan, inglizlar qo‘zg‘olon ko‘targan.")
t.TF4([("Davra stoli afsonasiga ko‘ra ritsarlar aksariyat manbalarda 24 ta bo‘lgan.", True), ("Alfred lotin asarlarini anglosaks tiliga tarjima qildirgan.", True),
       ("Kanut davlatiga Fransiya va Ispaniya kirgan.", False), ("Genrix I davrida qirollik moliya boshqarmasi tashkil topgan.", True)],
      "3-noto‘g‘ri: Kanut davlati Angliya, Shotlandiya, Norvegiya va Shvetsiyani o‘z ichiga olgan.")
t.MUL([("Angllar yashagan Mersiya shevasi tobora keng qo‘llanila boshlagan.", True),
       ("Anglosaks qirolliklarida qirol hokimiyati juda kuchli bo‘lgan.", False),
       ("838-yilda Ekbert normannlar hujumlaridan birini qaytargan.", True)],
      "II noto‘g‘ri: qirol hokimiyati zaif, «Donolar kengashi»ga qaram edi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Rimliklar Britaniyani bosib oldi", "Rim legioni Italiyaga qaytdi", "Ekbert qirolliklarni birlashtirdi", "Normannlar Londonni yondirdi", "Alfred normannlar bilan shartnoma tuzdi", "Kanut Angliyani zabt etdi", "Gastings jangi"],
      "43 → 407 → 829 → 842 → 879 → 1013 → 1066.")
t.MATCH("Hukmdorlarni ularga oid ma’lumotlar bilan moslashtiring.", ["Ekbert", "Buyuk Alfred", "Kanut", "Genrix II"],
        ["829-yilda qirolliklarni birlashtirgan", "«daniyaliklar puli»ni joriy qilgan", "Angliya, Norvegiya va Shvetsiyani birlashtirgan", "«qalqon puli»ni joriy qilgan", "Gastings jangi g‘olibi"], 'abcd',
        "Ekbert – 829; Alfred – daniyaliklar puli; Kanut – yirik davlat; Genrix II – qalqon puli.")
t.VENN("Buyuk Alfred", "Vilgelm I",
       [("«Anglosakson solnomasi»", 1), ("normannlarni to‘xtatgan", 1),
        ("Normandiya gersogi bo‘lgan", 2), ("Gastings jangida g‘alaba qozongan", 2),
        ("Angliya qiroli", 3)],
       "Alfred – solnoma, normannlarga qarshi; Vilgelm – Normandiya, Gastings; ikkalasi Angliya qiroli.")
t.MAPMATCH('britain', ['London', 'Normandiya', 'Daniya', 'Shotlandiya'],
           ["842-yilda normannlar yondirgan shahar", "1066-yilda Angliyaga qo‘shin tortgan gersoglik", "qiroli Kanut 1013-yilda Angliyani zabt etgan mamlakat", "Rim davrida skott va pikt qabilalari yashagan shimoliy hudud"],
           "1 – London; 2 – Normandiya; 3 – Daniya; 4 – Shotlandiya.")

# 5 Muqaddas Rim imperiyasi
t = Topic('y7j5', 7005); TOPICS['y7j5'] = t
t.B("Sharqiy Frank qirolligida Karolinglar boshqaruvi qachon yakun topgan?", "911-yilda", "919-yilda", "843-yilda", "962-yilda", "911-yilda.")
t.B("Germaniya qirolligi paydo bo‘lgan yil qaysi?", "919-yil", "911-yil", "962-yil", "955-yil", "919-yili Saksoniya gersogi Genrix hukmdor etib saylandi.")
t.B("Genrix I vengerlar bilan necha yilga sulh imzolagan?", "9 yilga", "5 yilga", "20 yilga", "1 yilga", "9 yilga tinchlik sulhi.")
t.B("Genrix I buyrug‘i bilan qishloqlardagi nechta xo‘jalikdan bittadan kishi burglarga ko‘chirilgan?", "har 9 xo‘jalikdan", "har 10 xo‘jalikdan", "har 5 xo‘jalikdan", "har 100 xo‘jalikdan", "Har 9 xo‘jalikdan bittadan.")
t.B("Otton I vengerlarni qaysi jangda yenggan?", "955-yilgi Lex daryosi jangida", "1176-yilgi Lenyano jangida", "732-yilgi Puate jangida", "962-yilgi Rim jangida", "955-yili Lex daryosi sohilida.")
t.B("Otton I qachon imperator deb e’lon qilingan?", "962-yilda", "955-yilda", "919-yilda", "996-yilda", "962-yili papa Ioann XII tomonidan.")
t.B("Muqaddas Rim imperiyasi qachongacha hukm surgan?", "1806-yilgacha", "1453-yilgacha", "1176-yilgacha", "1918-yilgacha", "962–1806-yillar.")
t.B("Imperiyaga «muqaddas» nomi nima uchun berilgan?", "xristian katolik cherkovi homiyligida bo‘lgani uchun", "poytaxti Rim bo‘lgani uchun", "Vizantiyaga qarshi kurashgani uchun", "papa imperator bo‘lgani uchun", "Katolik cherkovi homiyligida bo‘lgani uchun.")
t.B("Zamondoshlari kimni «dunyo mo‘jizasi» deb atagan?", "Otton III", "Otton I", "Genrix II", "Fridrix I", "Otton III.")
t.B("Rimliklar qarshi chiqqach, Otton III qaysi shaharga ko‘chib o‘tgan?", "Ravennaga", "Axenga", "Milanga", "Parijga", "Ravennaga.")
t.B("Otton I davridagi madaniy yuksalish qanday atalgan?", "«Otton Uyg‘onish davri»", "«Karoling uyg‘onishi»", "«Iliqlik davri»", "«Oltin asr»", "«Otton Uyg‘onish davri».")
t.B("Otton III ning ustozi rohib Gerbert papalikka qanday nom bilan saylangan?", "Silvester II", "Lev III", "Ioann XII", "Grigoriy VII", "Silvester II.")
t.B("Gerbert qaysi shaharlarda tahsil olgan?", "Qurdoba va Ishbiliyada", "Parij va Oksfordda", "Rim va Ravennada", "Bag‘dod va Damashqda", "Arablar Ispaniyasidagi Qurdoba va Ishbiliyada.")
t.B("Saksoniyaliklar sulolasining oxirgi imperatori kim?", "Genrix II", "Otton III", "Fridrix I", "Konrad II", "Genrix II (1014–1024).")
t.B("Shtaufenlar sulolasining eng taniqli vakili kim?", "Fridrix I Barbarossa", "Otton I", "Genrix I", "Silvester II", "Fridrix I Barbarossa (1152–1190).")
t.B("Fridrix I qachon Rimda toj kiygan?", "1155-yilda", "1158-yilda", "1176-yilda", "962-yilda", "1155-yilda.")
t.B("Lombardiya shaharlari qo‘zg‘oloniga qaysi shahar boshchilik qilgan?", "Milan", "Rim", "Ravenna", "Venetsiya", "Milan shahri boshchiligida.")
t.B("Fridrix I qo‘shini qaysi jangda italiyaliklardan mag‘lub bo‘lgan?", "1176-yilgi Lenyano jangida", "955-yilgi Lex jangida", "1155-yilgi Rim jangida", "1066-yilgi Gastings jangida", "1176-yilgi Lenyano jangida.")
t.NAT("955-yilda Otton I vengerlarni Lex daryosi bo‘yida yengdi.", "vengerlar o‘troq hayotga o‘tib, xristianlikni qabul qildi", "vengerlar Germaniyani bosib oldi", "Otton I taxtdan tushirildi", "vengerlar Vizantiyaga ko‘chib ketdi", "Vengerlar hujumlarini to‘xtatdi.")
t.NAT("Imperatorlar cherkovni davlat apparatining bir qismiga aylantirishga urindi.", "papalar noroziligi ortib, XI asrdan imperatorlarga qarshi kurash boshlandi", "papalar imperatorga bo‘ysundi", "imperiya kuchaydi", "cherkov yer-mulkidan mahrum bo‘ldi", "Bu kurash imperiyani zaiflashtirdi.")
t.NAT("1176-yilgi Lenyano jangida Fridrix I mag‘lub bo‘ldi.", "Shimoliy Italiya shaharlarining erkinligi va mustaqilligi tan olindi", "Milan vayron qilindi", "Italiya imperiyaga to‘liq bo‘ysundi", "Fridrix I papa bo‘ldi", "Fridrix I mustaqillikni tan olishga majbur bo‘ldi.")
t.NAT("Imperatorlar uzoq vaqt Germaniyani tark etib, Rimda toj kiyish uchun yurishlar qildi.", "yirik feodallarning mustaqillikka intilishi va sulolaviy nizolar kuchaydi", "Germaniya markazlashdi", "gersoglar zaiflashdi", "Italiya Germaniyaga to‘liq qo‘shildi", "Feodallar mustaqillikka intildi.")
t.TF("Muqaddas Rim imperiyasida hukumat o‘tiradigan doimiy bitta poytaxt bo‘lmagan.", True, "To‘g‘ri.")
t.TF("Otton I asosiy e’tiborini sharqqa – slavyan yerlariga qaratgan.", False, "Noto‘g‘ri: u e’tiborini Italiyaning janubiga qaratgan.")
t.TF4([("Otton II Vizantiya malikasiga uylangan.", True), ("Otton III davrida toj, oltin shar va saltanat hassasi yaratilgan.", True),
       ("Fridrix I Italiyaga faqat bir marta yurish qilgan.", False), ("Fridrix I o‘g‘li Genrixni Sitsiliya malikasi Konstansiyaga uylantirgan.", True)],
      "3-noto‘g‘ri: Fridrix I Italiyaga besh marotaba yurish qilgan.")
t.MUL([("Otton I o‘ziga ma’qul kelmagan papani sud qilib, lavozimidan chetlatgan.", True),
       ("Otton III 996-yilda Rimda toj kiygan.", True),
       ("Genrix II Italiyada umrbod qolib, Germaniyani yepiskoplar orqali boshqargan.", False)],
      "III noto‘g‘ri: Genrix II Germaniyada yashagan, Italiya shaharlarini nemis yepiskoplari boshqargan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Karolinglar boshqaruvi tugadi", "Genrix hukmdor etib saylandi", "Lex daryosi jangi", "Otton I imperator bo‘ldi", "Otton III Rimda toj kiydi", "Fridrix I Rimda toj kiydi", "Lenyano jangi"],
      "911 → 919 → 955 → 962 → 996 → 1155 → 1176.")
t.VENN("Otton I", "Fridrix I Barbarossa",
       [("Lex daryosida vengerlarni yenggan", 1), ("962-yilda imperator deb e’lon qilingan", 1),
        ("Milanni vayron qilgan", 2), ("Lenyano jangida mag‘lub bo‘lgan", 2),
        ("Muqaddas Rim imperatori", 3)],
       "Otton I – Lex, 962; Fridrix I – Milan, Lenyano; ikkalasi imperator.")
t.MAPMATCH(EU, ['Lex daryosi', 'Lenyano', 'Rim', 'Sitsiliya'],
           ["955-yilda vengerlar mag‘lub etilgan joy", "1176-yilda imperator qo‘shini yengilgan joy", "imperatorlar toj kiyish uchun yurish qilgan shahar", "malikasi Konstansiya Fridrix I o‘g‘liga uylangan orol"],
           "1 – Lex daryosi; 2 – Lenyano; 3 – Rim; 4 – Sitsiliya.")
