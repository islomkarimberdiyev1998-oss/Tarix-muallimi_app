from qlib import Topic, PLACES, REG
TOPICS = {}

# 13 Oltin O‘rda
t = Topic('y8j13', 8013); TOPICS['y8j13'] = t
t.B("Oltin O‘rda kimning ulusi hududida tashkil topgan?", "Jo‘ji", "Chig‘atoy", "O‘qtoy", "Tulu", "Chingizxonning to‘ng‘ich o‘g‘li Jo‘ji ulusi hududida.")
t.B("Oltin O‘rda davlatiga kim asos solgan?", "Botuxon", "Berkaxon", "O‘zbekxon", "Jo‘ji", "XIII asr 40-yillari boshida Botuxon.")
t.B("Sharq manbalarida Oltin O‘rda qanday atalgan?", "Jo‘ji ulusi", "Chig‘atoy ulusi", "Dashti Qipchoq", "Elxoniylar davlati", "Jo‘ji ulusi.")
t.B("«O‘rda» atamasi qanday ma’noni anglatadi?", "qarorgoh, chodir", "qo‘shin", "shahar", "davlat", "Qarorgoh, chodir.")
t.B("Oltin O‘rdada ijro hokimiyati boshlig‘i kim bo‘lgan?", "beklarbegi", "vazir", "dorug‘a", "ulusbegi", "Beklarbegi.")
t.B("Viloyat va shaharlarga hokim qilib kimlar yuborilgan?", "dorug‘alar", "ulusbegilar", "beklarbegilar", "no‘yonlar", "Dorug‘alar.")
t.B("Mo‘g‘ulcha «in’om, sovg‘a» ma’nosidagi meros yer-mulk qanday atalgan?", "suyurg‘ol", "iqto", "tumori", "xolisa", "Suyurg‘ol.")
t.B("O‘zbekxon davrida Oltin O‘rda qo‘shini qanchadan oshgan?", "300 ming jangchidan", "70 ming jangchidan", "1 mln jangchidan", "150 ming jangchidan", "300 ming jangchidan oshgan.")
t.B("Oltin O‘rdaning dastlabki poytaxti qaysi shahar bo‘lgan?", "Saroy Botu", "Saroy Berka", "Qozon", "Astraxan", "Saroy Botu – Volga quyi oqimida.")
t.B("Jonibek davrida Saroy Berka aholisi qanchaga yetgan?", "100 ming", "300 ming", "50 ming", "1 mln", "100 ming kishi.")
t.B("Ulug‘ xon ruxsatisiz hokimiyatga kelgan Jo‘ji ulusining birinchi hukmdori kim?", "Berkaxon", "Botuxon", "Mangu Temur", "O‘zbekxon", "Berkaxon (1255–1266).")
t.B("Oltin O‘rdani 1269-yilda Mo‘g‘ullar imperiyasidan mustaqil deb e’lon qilgan kim?", "Mangu Temur", "Berkaxon", "Botuxon", "Jonibek", "Botuning nabirasi Mangu Temur.")
t.B("O‘zbekxon imperiya hududini nechta tumanga bo‘lgan?", "70 ta", "10 ta", "20 ta", "25 ta", "70 ta tumanga, o‘nta yirik viloyatga.")
t.B("O‘zbekxon islomni qachon qabul qilgan?", "1314-yilda", "1312-yilda", "1342-yilda", "1357-yilda", "1314-yilda.")
t.B("XIV asr ikkinchi yarmida 25 yil ichida nechta xon almashgan?", "20 ta", "10 ta", "5 ta", "25 ta", "20 ta xon.")
t.B("1502-yilda Oltin O‘rda qo‘shinini uzil-kesil yenggan Qrim xoni kim?", "Mengli Garay", "To‘xtamishxon", "Jonibek", "Mamay", "Mengli Garay.")
t.NAT("Botuxon Qoraqurumdagi fitnalarga aralashib, Munkening ulug‘ xon bo‘lishiga yordam berdi.", "imperiyadagi eng nufuzli chingiziy hukmdorga aylandi", "Botuxon taxtdan ag‘darildi", "Oltin O‘rda tarqaldi", "Munke Oltin O‘rdani bosib oldi", "Botuxon mavqeini mustahkamladi.")
t.NAT("Mangu Temur o‘z nomidan tangalar zarb qila boshladi.", "Oltin O‘rda Mo‘g‘ullar imperiyasidan ajralib, rasman mustaqil bo‘ldi", "Oltin O‘rda Xubilayga to‘liq bo‘ysundi", "tangalar taqiqlandi", "Hulokuiylar Oltin O‘rdani egalladi", "Rasman mustaqil davlat bo‘ldi.")
t.NAT("O‘zbekxon ma’muriy-hududiy islohot o‘tkazib, ayirmachilikni bostirdi.", "davlat hokimiyati markazlashib, Oltin O‘rda yuksaldi", "Oltin O‘rda parchalanib ketdi", "rus knyazlari mustaqil bo‘ldi", "poytaxt Qoraqurumga ko‘chdi", "Oltin O‘rda yuksaldi.")
t.NAT("1395-yilda Amir Temur To‘xtamishxon ustidan g‘alaba qozondi.", "Oltin O‘rda inqirozi tezlashib, XV asrda qator xonliklarga bo‘linib ketdi", "Oltin O‘rda kuchaydi", "To‘xtamish Samarqandni egalladi", "rus knyazliklari Oltin O‘rdaga qo‘shildi", "Astraxan, Qozon, Qrim, Sibir xonliklari ajraldi.")
t.TF("Oltin O‘rda xonlari faqat chingiziylar va Jo‘ji avlodlaridan bo‘lishi shart edi.", True, "To‘g‘ri.")
t.TF("Rus knyazliklari Oltin O‘rda tarkibiga to‘g‘ridan-to‘g‘ri kiritilgan.", False, "Noto‘g‘ri: ular vassal hisoblanib, soliq to‘lagan, lekin tarkibga kiritilmagan.")
t.TF4([("Saylangan xon oq kigizda ko‘tarilib, taxtga o‘tqizilgan.", True), ("Ipak yo‘lining shimoliy tarmog‘i Oltin O‘rda hududidan o‘tgan.", True),
       ("Oltin O‘rda Hulokuiylarga qarshi Misr sultonlari bilan ittifoq tuzgan.", True), ("Oltin O‘rda Xitoydagi Yuan imperiyasini tan olgan.", False)],
      "4-noto‘g‘ri: Yuan imperiyasi tan olinmagan.")
t.MUL([("Aholining asosiy qismini qipchoq, bijanak, xazar va bulg‘orlar tashkil etgan.", True),
       ("Ibn Battuta ma’lumotiga ko‘ra O‘zbekxon taxti oltin bilan qoplangan.", True),
       ("To‘xtamishxon Amir Temurga qarshi kurashda doim ittifoqchi bo‘lgan.", False)],
      "III noto‘g‘ri: To‘xtamish Temur yordamida hokimiyatga kelgan, keyin unga qarshi chiqqan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Botuxonning g‘arbiy yurishlari boshlandi", "Mangu Temur mustaqillik e’lon qildi", "O‘zbekxon islomni qabul qildi", "To‘xtamishxon taxtga keldi", "Amir Temurning To‘xtamish ustidan g‘alabasi", "Ruslar boj to‘lashdan bosh tortdi", "Mengli Garay Oltin O‘rdani yengdi"],
      "1237 → 1269 → 1314 → 1380 → 1395 → 1480 → 1502.")
t.MATCH("Xonlarni ularga oid ma’lumot bilan moslashtiring.", ["Botuxon", "Berkaxon", "O‘zbekxon", "To‘xtamishxon"],
        ["Oltin O‘rdaga asos solgan", "poytaxtni Yangi Saroyga ko‘chirgan", "islomni davlat dini deb e’lon qilgan", "Amir Temur yordamida hokimiyatga kelgan", "1502-yilda Oltin O‘rdani yenggan"], 'abcd',
        "Botu – asos; Berka – Saroy Berka; O‘zbekxon – islom; To‘xtamish – Temur yordami.")
t.VENN("Saroy Botu", "Saroy Berka",
       [("Oltin O‘rdaning dastlabki poytaxti", 1), ("hozirgi Astraxan yaqinida", 1),
        ("Berkaxon davrida poytaxt qilingan", 2), ("Jonibek davrida aholisi 100 ming", 2),
        ("dunyoning eng katta shaharlaridan biri", 3)],
       "Saroy Botu – dastlabki poytaxt; Saroy Berka – Berkaxon davri, 100 ming; ikkalasi yirik shahar.")
t.MAPMATCH('goldh', ['Saroy Botu', 'Saroy Berka', 'Qrim', 'Qozon'],
           ["Volga quyi oqimidagi dastlabki poytaxt", "Berkaxon davrida ko‘chirilgan yangi poytaxt", "xoni 1502-yilda Oltin O‘rdani yenggan xonlik", "Oltin O‘rda parchalanishidan vujudga kelgan Volga bo‘yidagi xonlik"],
           "1 – Saroy Botu; 2 – Saroy Berka; 3 – Qrim; 4 – Qozon.")

# 14 O‘rta asrlarda Hindiston
t = Topic('y8j14', 8014); TOPICS['y8j14'] = t
t.B("Dehli sultonligiga kim asos solgan?", "Qutbiddin Oyboq", "Shamsiddin Eltutmish", "Jaloliddin Feruzshoh", "Bahlul Lo‘diy", "1206-yilda Qutbiddin Oyboq.")
t.B("Dehli sultonligi qaysi yillarda mavjud bo‘lgan?", "1206–1526-yillarda", "1206–1398-yillarda", "1290–1526-yillarda", "1451–1526-yillarda", "1206–1526-yillar.")
t.B("Shamsiddin Eltutmishni Bag‘dod xalifasi qachon mustaqil hukmdor deb e’tirof etgan?", "1229-yilda", "1206-yilda", "1236-yilda", "1240-yilda", "1229-yilda.")
t.B("Janubiy Osiyoning birinchi musulmon ayol hukmdori kim?", "Roziya", "Nurjahon", "Mumtoz", "Hamida", "Eltutmishning qizi Roziya.")
t.B("Roziya qachon taxtga o‘tirgan?", "1236-yilda", "1240-yilda", "1229-yilda", "1290-yilda", "1236-yilda.")
t.B("Xiljiylar sulolasiga kim asos solgan?", "Jaloliddin Feruzshoh", "Alouddin Xiljiy", "Muhammad Tug‘luq", "Xizr Xon", "1290-yilda Jaloliddin Feruzshoh.")
t.B("Bozordagi narxlarni belgilagan, «sinov xaridlari» o‘tkazdirgan sulton kim?", "Alouddin Xiljiy", "Feruzshoh Tug‘luq", "Iskandar Lo‘diy", "Eltutmish", "Alouddin Xiljiy.")
t.B("Musulmon bo‘lmaganlardan olinadigan jon solig‘i qanday atalgan?", "jizya", "xiroj", "ushr", "zakot", "Jizya.")
t.B("Vaqtincha yoki umrbod foydalanish uchun beriladigan yer qanday atalgan?", "iqto", "xolisa", "suyurg‘ol", "patta", "Iqto.")
t.B("Davlat ixtiyoridagi yerlar qanday atalgan?", "xolisa", "iqto", "vaqf", "grass", "Xolisa.")
t.B("O‘zini «Iskandar Zulqarnaynning davomchisi» deb atagan sulton kim?", "Muhammad Tug‘luq", "Feruzshoh Tug‘luq", "Alouddin Xiljiy", "Ibrohim Lo‘diy", "Muhammad Tug‘luq (1325–1351).")
t.B("«Xalq homiysi» deb nom olgan sulton kim?", "Feruzshoh Tug‘luq", "Muhammad Tug‘luq", "Qutbiddin Oyboq", "Bahlul Lo‘diy", "Feruzshoh Tug‘luq.")
t.B("Amir Temur Dehlini qachon zabt etgan?", "1398-yilda", "1402-yilda", "1451-yilda", "1526-yilda", "1398-yilda.")
t.B("Amir Temur Dehliga noib qilib kimni tayinlagan?", "Xizr Xonni", "Bahlul Lo‘diyni", "Mahmudxonni", "Roziyani", "Sayyidlardan Xizr Xonni.")
t.B("1451-yilda Dehlini egallab, o‘zini sulton deb e’lon qilgan kim?", "Bahlul Lo‘diy", "Ibrohim Lo‘diy", "Xizr Xon", "Iskandar Lo‘diy", "Afg‘on urug‘i boshlig‘i Bahlul Lo‘diy.")
t.B("Poytaxtni Dehlidan Agraga kim ko‘chirgan?", "Iskandar Lo‘diy", "Bahlul Lo‘diy", "Ibrohim Lo‘diy", "Feruzshoh", "Iskandar (1489–1517).")
t.B("Bobur Ibrohim Lo‘diy qo‘shinini qachon tor-mor etgan?", "1526-yil 21-aprelda", "1398-yilda", "1451-yilda", "1517-yilda", "1526-yil 21-aprelda.")
t.NAT("Roziyaning turk zodagonlari bilan munosabatlari keskinlashdi.", "1240-yil apreldagi isyondan so‘ng u taxtdan ag‘darildi", "Roziya umrbod hukmronlik qildi", "turk zodagonlari quvildi", "Dehli sultonligi tugadi", "Roziya taxtdan ag‘darildi.")
t.NAT("Dehli sultonligi kuchli va intizomli qo‘shinga ega bo‘ldi.", "shimoldan mo‘g‘ullar hujumlari qaytarildi", "mo‘g‘ullar Hindistonni egalladi", "sultonlik parchalandi", "rajputlar hokimiyatga keldi", "Mo‘g‘ul hujumlari qaytarildi.")
t.NAT("Feruzshoh Tug‘luq soliqlarni kamaytirib, davlat yerlarini dehqonlarga ijaraga berdi.", "qishloq xo‘jaligi va hunarmandchilik yuksaldi, sulton «xalq homiysi» nomini oldi", "dehqonlar qo‘zg‘olon ko‘tardi", "xazina bo‘shab qoldi", "sultonlik parchalandi", "Sulton obro‘si oshdi.")
t.NAT("Zodagonlar Ibrohim Lo‘diyga qarshi chiqib, Bobur Mirzodan yordam so‘radi.", "1526-yilda Bobur Ibrohim Lo‘diyni yengib, Dehli sultonligi parchalandi", "Ibrohim Lo‘diy Kobulni egalladi", "Bobur yordam bermadi", "Dehli sultonligi kuchaydi", "Bobur Hindistonni egalladi.")
t.TF("Dehli sultonligi boshqaruvi islom huquqiga asoslangan.", True, "To‘g‘ri.")
t.TF("Sayyidlar davrida Dehli sultonligi eng qudratli davrini boshdan kechirgan.", False, "Noto‘g‘ri: XV asr birinchi yarmida sultonlik qudratini yo‘qotib, oddiy davlatga aylandi.")
t.TF4([("Eltutmish sultonlikka Panjob, Sind va Bengaliyani qo‘shib olgan.", True), ("Iqto egalari soliqlarning 10–20% ini o‘ziga qoldirgan.", True),
       ("Alouddin Xiljiy Dekan, Gujarot va Rajastonni egallagan.", True), ("Amir Temur Hindistondan hech qanday hunarmand olib ketmagan.", False)],
      "4-noto‘g‘ri: Sohibqiron ko‘plab hind hunarmandlari va me’morlarini Samarqandga olib qaytgan.")
t.MUL([("Dehli sultonligini G‘ulomlar, Xiljiylar, Tug‘luqlar, Sayyidlar va Lo‘diylar boshqargan.", True),
       ("Sultonlikda maxfiy bo‘lim tuzilgan.", True),
       ("Islom avvalo dehqonlar tomonidan qabul qilingan.", False)],
      "III noto‘g‘ri: avvalo savdogarlar, hunarmandlar va shahar aholisi qabul qilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Dehli sultonligi tuzildi", "Eltutmish mustaqil hukmdor deb e’tirof etildi", "Roziya taxtga o‘tirdi", "Xiljiylar sulolasi boshlandi", "Amir Temur Dehlini egalladi", "Bahlul Lo‘diy sulton bo‘ldi", "Bobur Ibrohim Lo‘diyni yengdi"],
      "1206 → 1229 → 1236 → 1290 → 1398 → 1451 → 1526.")
t.MATCH("Sultonlarni ularga oid ma’lumot bilan moslashtiring.", ["Qutbiddin Oyboq", "Alouddin Xiljiy", "Feruzshoh Tug‘luq", "Iskandar Lo‘diy"],
        ["Dehli sultonligi asoschisi", "bozor narxlarini belgilagan", "«xalq homiysi»", "poytaxtni Agraga ko‘chirgan", "Sayyidlar sulolasi asoschisi"], 'abcd',
        "Oyboq – asoschi; Xiljiy – narxlar; Feruzshoh – xalq homiysi; Iskandar – Agra.")
t.VENN("Iqto", "Xolisa",
       [("feodallarga vaqtincha yoki umrbod berilgan", 1), ("egasi soliqning 10–20% ini olgan", 1),
        ("davlat ixtiyoridagi yerlar", 2), ("soliqlari xazinaga tushgan", 2),
        ("Dehli sultonligidagi yer egaligi turi", 3)],
       "Iqto – feodalga, 10–20%; xolisa – davlatga, xazina; ikkalasi yer egaligi turi.")
t.MAPMATCH('india', ['Dehli', 'Rajputana', 'Kobul', 'Bengaliya'],
           ["1206-yilda tuzilgan sultonlik poytaxti", "Alouddin Xiljiy Dekan va Gujarot bilan birga egallagan Rajaston", "Bobur Mirzo hukmronlik qilgan shahar", "Eltutmish Panjob va Sind bilan birga qo‘shib olgan hudud"],
           "1 – Dehli; 2 – Rajaston; 3 – Kobul; 4 – Bengaliya.")

# 15 O‘rta asrlarda Xitoy
t = Topic('y8j15', 8015); TOPICS['y8j15'] = t
t.B("Xubilay qachon ulug‘ xoqon deb e’lon qilingan?", "1260-yilda", "1279-yilda", "1368-yilda", "1206-yilda", "1260-yilda.")
t.B("Yuan sulolasining asoschisi kim?", "Xubilay", "Chju Yuan Chjan", "Yongle", "Chingizxon", "Xubilay.")
t.B("Yuan sulolasi qaysi yillarda hukmronlik qilgan?", "1279–1368-yillarda", "1368–1644-yillarda", "1260–1279-yillarda", "1206–1368-yillarda", "1279–1368-yillar.")
t.B("Xubilay qaysi shaharni poytaxt etib belgilagan?", "Xonbaliq", "Nankin", "Loyan", "Chanan", "Xonbaliq (Xon shahri).")
t.B("Xubilay imperiyani nechta viloyatga bo‘lgan?", "o‘n ikkita", "yigirmata", "oltita", "o‘nta", "O‘n ikki viloyatga.")
t.B("Xubilay saroyida yuqori lavozimda xizmat qilgan venetsiyalik kim?", "Marko Polo", "Klavixo", "Kolumb", "Ibn Battuta", "Marko Polo.")
t.B("XIV asr 40-yillarida qaysi daryoda toshqin yuz bergan?", "Xuanxe (Sariq daryo)", "Yanszi", "Amudaryo", "Gang", "Xuanxe – Shandun suv ostida qoldi.")
t.B("1351-yildagi qo‘zg‘olon qanday nom bilan mashhur?", "«Qizil peshonabog‘lilar»", "«Oq nilufar»", "«Sariq sallalilar»", "«Boshini dorga tikkanlar»", "«Oq nilufar» ittifoqi tayyorlagan «Qizil peshonabog‘lilar».")
t.B("Min sulolasiga kim asos solgan?", "rohib Chju Yuan Chjan", "Xubilay", "Yongle", "Cheng Xua", "1368-yilda rohib Chju Yuan Chjan.")
t.B("«Min» so‘zi qanday ma’noni anglatadi?", "yorug‘lik imperiyasi", "osmon imperiyasi", "o‘rta davlat", "buyuk sulola", "Min – yorug‘lik imperiyasi.")
t.B("Chju Yuan Chjan 1368-yilda qaysi shaharni egallagan?", "Nankin", "Pekin", "Xonbaliq", "Shanxay", "Nankinni.")
t.B("Imperator Yongle qaysi yillarda hukmronlik qilgan?", "1402–1424-yillarda", "1368–1398-yillarda", "1279–1294-yillarda", "1424–1450-yillarda", "1402–1424-yillar.")
t.B("«Yongle ensiklopediyasi» qachon yozilgan?", "1408-yilda", "1421-yilda", "1368-yilda", "1405-yilda", "1408-yilda.")
t.B("Beypin qachon Min imperiyasi poytaxti bo‘lib, Pekin deb atala boshlagan?", "1421-yilda", "1368-yilda", "1408-yilda", "1260-yilda", "1421-yilda.")
t.B("Buyuk Xitoy devorini tiklashni buyurgan imperator kim?", "Cheng Xua", "Yongle", "Xubilay", "Chju Yuan Chjan", "Cheng Xua; 200 ming askar 600 km qismini qurdi.")
t.B("Admiral Chjan Xening asl ismi nima edi?", "Mahmud", "Umar", "Kamoliddin", "Muhammad", "Mahmud; ajdodlari buxorolik.")
t.B("Chjan Xe ekspeditsiyalari qaysi yillarda bo‘lgan?", "1405–1433-yillarda", "1368–1388-yillarda", "1402–1424-yillarda", "1279–1300-yillarda", "1405–1433-yillar.")
t.B("Chjan Xe flotida taxminan nechta ulkan kema bo‘lgan?", "250 ga yaqin", "70 ta", "30 ta", "1000 ta", "250 ga yaqin kema.")
t.NAT("Xuanxe toshqini Buyuk kanalni vayron qildi.", "shimoliy viloyatlarda ocharchilik boshlanib, moliyaviy inqiroz yuz berdi", "hosil ko‘paydi", "mo‘g‘ullar kuchaydi", "Nankin poytaxt bo‘ldi", "Dehqonlar janubga qocha boshladi.")
t.NAT("Min sulolasi dastlab mehnatkashlar manfaatini birinchi o‘ringa qo‘ydi.", "soliqlar kamaytirildi, qullarni ozod qilish haqida qonun qabul qilindi", "soliqlar oshirildi", "qullik kuchaydi", "mo‘g‘ul zodagonlari yerlari saqlab qolindi", "Yersiz dehqonlarga yer bo‘lib berildi.")
t.NAT("Yongle Buyuk kanalni qayta qurdirdi.", "yagona suv yo‘li barpo etilib, ekin maydonlari ko‘paydi – «oltin davr» boshlandi", "kanal yopildi", "savdo to‘xtadi", "ocharchilik boshlandi", "Min imperiyasining «oltin davri».")
t.NAT("1404-yil oxirida Amir Temur Xitoyga yurish boshladi.", "Temur yo‘lda vafot etib, yurish amalga oshmay qoldi", "Temur Xitoyni egalladi", "Min sulolasi quladi", "Xitoy Temurga bo‘ysundi", "Yongle temuriylar bilan munosabat o‘rnatdi.")
t.TF("Yuan davrida mo‘g‘ullar xitoyliklarning kuchli ta’siriga tushib, xitoy tilida so‘zlasha boshlagan.", True, "To‘g‘ri.")
t.TF("Min sulolasi davrida imtihon tizimi butunlay bekor qilingan.", False, "Noto‘g‘ri: uch bosqichli imtihon tizimi qayta tiklangan.")
t.TF4([("Xubilay Birma, Kambodja va Koreyani bo‘ysundirgan.", True), ("1387–1388-yillarda Yuan davlati butunlay tugatilgan.", True),
       ("Ryukyu orollari yaqinida yapon floti tor-mor etilgan.", True), ("Chjan Xe kemalari Amerikaga yetib borgan.", False)],
      "4-noto‘g‘ri: kemalar Janubi-Sharqiy Osiyo, Seylon, Hindiston, Fors ko‘rfazi, Arabiston va Afrikaga yetgan.")
t.MUL([("Yuan davrida ish yuritish mo‘g‘ul va xitoy tillarida baravar olib borilgan.", True),
       ("1370-yilda soliqlarni aniqlash uchun aholi ro‘yxatga olingan.", True),
       ("Yongle davrida poytaxt Pekindan Nankinga ko‘chirilgan.", False)],
      "III noto‘g‘ri: poytaxt Nankindan Pekinga ko‘chirilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Xubilay ulug‘ xoqon bo‘ldi", "Xitoy to‘liq egallandi", "«Qizil peshonabog‘lilar» qo‘zg‘oloni", "Min sulolasi tuzildi", "Chjan Xe ekspeditsiyalari boshlandi", "«Yongle ensiklopediyasi» yozildi", "Pekin Min poytaxti bo‘ldi"],
      "1260 → 1279 → 1351 → 1368 → 1405 → 1408 → 1421.")
t.MATCH("Shaxslarni ularga oid ma’lumot bilan moslashtiring.", ["Xubilay", "Chju Yuan Chjan", "Yongle", "Chjan Xe"],
        ["Yuan sulolasi asoschisi", "Min sulolasi asoschisi", "«Yongle ensiklopediyasi» davri imperatori", "dengiz ekspeditsiyalari admirali", "Buyuk devorni tiklagan imperator"], 'abcd',
        "Xubilay – Yuan; Chju – Min; Yongle – ensiklopediya; Chjan Xe – admiral.")
t.VENN("Yuan sulolasi", "Min sulolasi",
       [("asoschisi Xubilay", 1), ("poytaxti Xonbaliq", 1),
        ("asoschisi Chju Yuan Chjan", 2), ("«Yongle ensiklopediyasi»", 2),
        ("Xitoyni boshqargan sulola", 3)],
       "Yuan – Xubilay, Xonbaliq; Min – Chju Yuan Chjan, ensiklopediya; ikkalasi Xitoy sulolasi.")
t.MAPMATCH('eastasia', ['Pekin', 'Nankin', 'Ryukyu orollari', 'Koreya'],
           ["Xubilay Xonbaliq deb atagan, 1421-yildan Min poytaxti", "1368-yilda Chju Yuan Chjan egallagan shahar", "yaqinida yapon floti tor-mor etilgan orollar", "Xubilay Birma va Kambodja bilan birga bo‘ysundirgan mamlakat"],
           "1 – Pekin; 2 – Nankin; 3 – Ryukyu; 4 – Koreya.")

# 16 Yaponiya va Koreya
t = Topic('y8j16', 8016); TOPICS['y8j16'] = t
t.B("Yaponlar e’tiqodiga ko‘ra imperator kimning o‘g‘li hisoblangan?", "quyosh xudosi Amaterasuning", "Budda", "Osmon o‘g‘li", "dengiz xudosining", "Quyosh xudosi Amaterasuning.")
t.B("1156-yilda qaysi xonadonlar o‘zaro urush boshlagan?", "Tayra va Minamoto", "Asikaga va Minamoto", "Fudzivara va Tayra", "Li va Koryo", "Tayra va Minamoto.")
t.B("Minamoto Yoritomo qachon syogun unvonini olgan?", "1192-yilda", "1185-yilda", "1156-yilda", "1333-yilda", "1192-yilda.")
t.B("Kamakura syogunligi qaysi yillarda mavjud bo‘lgan?", "1192–1333-yillarda", "1338–1573-yillarda", "1156–1192-yillarda", "1274–1281-yillarda", "1192–1333-yillar.")
t.B("Xubilay Yaponiyaga birinchi marta qachon qo‘shin yuborgan?", "1274-yilda", "1281-yilda", "1260-yilda", "1333-yilda", "1274-yilda.")
t.B("1281-yilda mo‘g‘ullar qaysi ko‘rfazga kirib kelgan?", "Xakata ko‘rfazi", "Tokio ko‘rfazi", "Fors ko‘rfazi", "Bengal ko‘rfazi", "Xakata ko‘rfaziga.")
t.B("Yaponlar mo‘g‘ul flotini cho‘ktirgan tayfunni qanday atagan?", "kamikadze – «ilohiy shamol»", "busido", "syogun", "daymyo", "Kamikadze – «ilohiy shamol».")
t.B("1281-yilda mo‘g‘ullar qancha kema va askar yo‘qotgan?", "to‘rt ming kema va yuz ming askar", "yuz kema va o‘n ming askar", "ming kema va 30 ming askar", "250 kema va 70 ming askar", "To‘rt ming kema va yuz ming askar.")
t.B("Kamakura syogunligi qachon ag‘darilgan?", "1333-yilda", "1338-yilda", "1281-yilda", "1467-yilda", "1333-yilda.")
t.B("Kioto syogunligiga kim asos solgan?", "Asikaga", "Minamoto", "Tayra", "Li Son Ge", "1338-yilda Asikaga.")
t.B("Viloyatlardagi eng yirik mulkdorlar qanday atalgan?", "daymyolar", "samuraylar", "syogunlar", "mikadolar", "Daymyolar.")
t.B("«Onin urushi» qaysi yillarda bo‘lgan?", "1467–1477-yillarda", "1338–1348-yillarda", "1274–1281-yillarda", "1156–1185-yillarda", "1467–1477-yillarda; Kioto vayron bo‘ldi.")
t.B("1231-yilda Koryo qo‘shinlari qaysi qal’a jangida yengilgan?", "Anbuk", "Kanxva", "Kegyon", "Xanson", "Anbuk qal’asida.")
t.B("Mo‘g‘ullardan himoyalanish uchun Koryo poytaxti qayerga ko‘chirilgan?", "Kanxva oroliga", "Xansonga", "Pxenyanga", "Kiotoga", "Kanxva oroliga.")
t.B("Li sulolasiga kim asos solgan?", "Li Son Ge", "Konmin", "Sejong", "Taejong", "1392-yilda Li Son Ge.")
t.B("Li Son Ge qaysi nom bilan taxtga o‘tirgan?", "Taejo", "Taejong", "Sejong", "Seongjong", "Qirol Taejo.")
t.B("Choson qirolligining poytaxti qaysi shahar bo‘lgan?", "Xanson (hozirgi Seul)", "Kegyon", "Pxenyan", "Kanxva", "Xanson (hozirgi Seul).")
t.B("«Buyuk» unvonini olgan Koreya qiroli kim?", "Sejong", "Taejo", "Taejong", "Seongjong", "Buyuk Sejong (1418–1450).")
t.NAT("Syogun Xubilay elchilarini qatl ettirdi.", "1274-yilda Xubilay Yaponiyaga katta dengiz floti qo‘shinini yubordi", "Yaponiya Xubilayga bo‘ysundi", "Koreya Yaponiyani bosib oldi", "Xubilay Yaponiya bilan ittifoq tuzdi", "Mo‘g‘ullar bostirib keldi.")
t.NAT("1281-yilda kuchli tayfun mo‘g‘ul flotini halokatga uchratdi.", "Xubilay Yaponiyani bosib olishdan voz kechdi", "mo‘g‘ullar Kiotoni egalladi", "Yaponiya Xitoyga qo‘shildi", "syogunlik tugatildi", "Yaponlar o‘zlarini yengilmas deb bildi.")
t.NAT("Zodagonlar syogun urushdagi ishtirokini yetarli baholamaganidan norozi bo‘ldi.", "1333-yilda Asikaga xonadoni bilan birlashib, Kamakura syogunligini ag‘dardi", "syogun kuchaydi", "imperator hokimiyati to‘liq tiklandi", "mo‘g‘ullar qaytib keldi", "Kioto syogunligi boshlandi.")
t.NAT("Yuan imperiyasi tanazzulga yuz tutdi, 1368-yilda Xitoyda mo‘g‘ullar hukmronligi tugadi.", "Koryo Yuan imperiyasiga qaramlikdan xalos bo‘ldi", "Koryo mo‘g‘ullarga to‘liq qo‘shildi", "Koreya Yaponiyaga bo‘ysundi", "Koryo qiroli taxtdan voz kechdi", "Koryo mustaqillikka erishdi.")
t.TF("Taejong davrida har bir voyaga yetgan fuqaro ismi yozilgan «taxta bo‘lagi»ni olib yurishi shart bo‘lgan.", True, "To‘g‘ri: 1413-yilgi qonun.")
t.TF("O‘rta asrlarda Yaponiya imperatori davlat ishlarini shaxsan va doimiy boshqargan.", False, "Noto‘g‘ri: imperator amalda davlat ishlariga kamdan kam aralashgan.")
t.TF4([("Minamoto Yoritomo 1185-yilda barcha raqiblarini mag‘lub etgan.", True), ("Koryo hukmdori Konmin 1356-yilda mo‘g‘ul tarafdorlarini lavozimdan chetlatgan.", True),
       ("1402-yilda shikoyatlar uchun saroy tashqarisiga «katta do‘mbira» o‘rnatilgan.", True), ("Taejo Chosonni Xitoydan butunlay mustaqil deb tan oldirgan.", False)],
      "4-noto‘g‘ri: Taejo Koreyani Xitoyning vassali sifatida tan olishga majbur bo‘lgan.")
t.MUL([("Seongjong davrida «Davlat boshqaruvi to‘g‘risida»gi Katta kodeks hayotga tatbiq etilgan.", True),
       ("Kyonbokkun saroyi Xansonda qurilgan.", True),
       ("Kioto syogunligi Minamoto sulolasi davrida bo‘lgan.", False)],
      "III noto‘g‘ri: Kioto syogunligi Asikaga sulolasi davri (1338–1573).")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Tayra va Minamoto urushi boshlandi", "Minamoto syogun bo‘ldi", "Anbuk jangi", "Mo‘g‘ullarning birinchi hujumi", "Kamakura syogunligi ag‘darildi", "Li sulolasi tuzildi", "«Onin urushi» boshlandi"],
      "1156 → 1192 → 1231 → 1274 → 1333 → 1392 → 1467.")
t.MATCH("Shaxslarni ularga oid ma’lumot bilan moslashtiring.", ["Minamoto Yoritomo", "Asikaga", "Li Son Ge", "Sejong"],
        ["Kamakura syogunligi asoschisi", "Kioto syogunligi asoschisi", "Li sulolasi asoschisi", "«Buyuk» unvonini olgan qirol", "Koryo hukmdori Konmin"], 'abcd',
        "Minamoto – Kamakura; Asikaga – Kioto; Li Son Ge – Li sulolasi; Sejong – Buyuk.")
t.VENN("Kamakura syogunligi", "Kioto syogunligi",
       [("Minamoto va Fudzivara sulolasi", 1), ("mo‘g‘ul hujumlarini qaytargan", 1),
        ("Asikaga sulolasi", 2), ("«Onin urushi» davrida zaiflashgan", 2),
        ("samuraylar qo‘shiniga tayangan syogun hokimiyati", 3)],
       "Kamakura – Minamoto, mo‘g‘ullar; Kioto – Asikaga, Onin; ikkalasi syogun hokimiyati.")
t.MAPMATCH('japko', ['Kamakura', 'Kioto', 'Xakata', 'Xanson (Seul)'],
           ["1192–1333-yillardagi syogunlik markazi", "1338-yildan syogunlik markazi, «Onin urushi»da vayron bo‘lgan poytaxt", "1281-yilda mo‘g‘ullar kirib kelgan ko‘rfaz", "Choson qirolligi poytaxti"],
           "1 – Kamakura; 2 – Kioto; 3 – Xakata; 4 – Xanson.")
