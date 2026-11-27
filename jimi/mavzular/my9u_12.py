from qlib import Topic, PLACES, REG
TOPICS = {}

# 24-§ Qoraqalpoqlarning madaniy hayoti
t = Topic('y9u24', 9024); TOPICS['y9u24'] = t
t.B("Qoraqalpoqlarning O‘zbeklar Afandisiga o‘xshash qiziqchisi kim?", "O‘mirbek laqqi", "Jiyen jirov", "Berdaq", "Kunxo‘ja", "O‘mirbek laqqi.")
t.B("Qaysi dostonda Amir Temur va To‘xtamish faoliyati bilan bog‘liq voqealar bayon etilgan?", "«Edigey»", "«Qirqqiz»", "«Alpomish»", "«Qublon»", "«Edigey».")
t.B("«Qirqqiz» dostonida qaysi kurash badiiy ifodasini topgan?", "Xorazm xalqining Nodirshohga qarshi kurashi", "Temurning To‘xtamishga qarshi kurashi", "ruslarga qarshi kurash", "jung‘orlarga qarshi kurash", "Qoraqalpoqlar ozodlik kurashi va Nodirshohga qarshi kurash.")
t.B("Qoraqalpoq gilam va kashtalaridagi to‘lqinsimon naqshlar nimaning ramzi?", "suv", "olov", "osmon", "tog‘", "Suv ramzi – daryo va ko‘l bo‘yida yashaganlari uchun.")
t.B("Qoraqalpoq yog‘och o‘ymakorligining o‘ziga xosligi nimada?", "qadama naqshlarda", "girih naqshlarda", "islimiy naqshlarda", "koshinlarda", "Qadama naqshli yog‘och o‘ymakorligi.")
t.B("Doston ijrochilari qanday uch guruhga bo‘lingan?", "jirovlar, baxshilar, qissaxonlar", "hofiz, maqomchi, baxshi", "chechan, laqqi, jirov", "shoir, xattot, musavvir", "Jirovlar, baxshilar, qissaxonlar.")
t.B("Jirovlar qahramonlik dostonlarini qaysi cholg‘u jo‘rligida ijro etgan?", "qo‘biz", "dutor", "g‘ijjak", "surnay", "Qo‘biz jo‘rligida.")
t.B("Baxshilar qaysi cholg‘ular jo‘rligida ijro etgan?", "dutor va g‘ijjak", "qo‘biz", "nog‘ora", "surnay", "Dutor va g‘ijjak.")
t.B("Qo‘bizning torlari nimadan yasaladi?", "otning chiyratilmagan qilidan", "ipakdan", "metalldan", "ichakdan", "Ot qilidan, 2 ta tor.")
t.B("Qirg‘izlarda qo‘bizga o‘xshash cholg‘u qanday nom bilan saqlangan?", "qo‘muz", "xomis", "do‘mbira", "rubob", "Qo‘muz.")
t.B("Jiyen jirov qaysi yillarda yashagan?", "1730–1784", "1799–1880", "1824–1878", "1827–1900", "1730–1784.")
t.B("«O‘roqchilar», «Cho‘ponlar» she’rlari muallifi kim?", "Kunxo‘ja Ibrohim", "Berdaq", "Ajiniyoz", "Jiyen jirov", "Kunxo‘ja Ibrohim.")
t.B("Ajiniyozning taxallusi nima?", "Zevar", "Berdaq", "Nishoniy", "Munis", "Zevar.")
t.B("Ajiniyoz boshlang‘ich ta’limni qayerda olgan?", "Mo‘ynoqdagi eski maktabda", "Xivada", "Chimboyda", "Buxoroda", "Mo‘ynoqda.")
t.B("Ajiniyoz Xivadagi qaysi madrasada o‘qigan?", "Sherg‘ozixon madrasasi", "Muhammad Aminxon madrasasi", "Arab Muhammadxon madrasasi", "Olloqulixon madrasasi", "Sherg‘ozixon madrasasida.")
t.B("Ajiniyozning qaysi dostonida qoraqalpoqlarning majburan ko‘chishi tasvirlangan?", "«Bo‘zatov»", "«Qirqqiz»", "«Edigey»", "«Omongeldi»", "«Bo‘zatov».")
t.B("Ajiniyoz tavalludining 200 yilligi qachon nishonlandi?", "2024-yilda", "2014-yilda", "2000-yilda", "2020-yilda", "2024-yilda.")
t.B("Berdaqning asl ismi nima?", "Berdimurod Qarg‘aboy o‘g‘li", "Ajiniyoz Qo‘siboy o‘g‘li", "Kunxo‘ja Ibrohim", "Muhammadrizo Erniyozbek o‘g‘li", "Berdimurod Qarg‘aboy o‘g‘li.")
t.B("Berdaq necha yoshida iste’dodli shoir sifatida tanilgan?", "25 yoshida", "18 yoshida", "40 yoshida", "12 yoshida", "25 yoshida.")
t.B("Berdaqning yoshlarni ma’rifatga chaqiruvchi she’ri qaysi?", "«O‘g‘limga»", "«Bo‘lgan emas»", "«Umrim»", "«Oydo‘stbiy»", "«O‘g‘limga», «Ahmoq bo‘lma».")
t.NAT("O‘mirbek laqqi adolatsiz amaldorlar va qozilar kirdikorlarini fosh qildi.", "u jamiyat kamchiliklari ustidan kuluvchi xalq qahramoni sifatida gavdalandi", "u xon tomonidan mukofotlandi", "latifalari taqiqlandi", "u qozi bo‘ldi", "Xalq qahramoniga aylandi.")
t.NAT("Qoraqalpoqlar qadimdan daryo va ko‘l bo‘ylarida yashab kelgan.", "gilam va kashta naqshlarida suv ramzi – to‘lqin ko‘rinishi aks etgan", "naqshlarda tog‘lar tasvirlangan", "naqshlar ishlatilmagan", "kashtachilik yo‘qolgan", "To‘lqinsimon naqshlar.")
t.NAT("Berdaq Navoiy, Fuzuliy, Maxtumquli asarlarini chuqur mutolaa qildi.", "tarix va xalq og‘zaki ijodini mukammal bilgan shoir bo‘lib yetishdi", "shoirlikdan voz kechdi", "faqat tarjima bilan shug‘ullandi", "Xivaga ko‘chib ketdi", "Yetuk shoir bo‘ldi.")
t.NAT("Berdaq tarixiy mavzularda asarlar yozdi.", "«Oydo‘stbiy», «Ernazarbiy» asarlarida xalq qahramonlari jasorati kuylandi", "u xonlarni maqtadi", "tarixiy asarlar taqiqlandi", "u tarixchi bo‘ldi", "Qahramonlar kuylandi.")
t.TF("Qoraqalpoq xalq qo‘shiqlarida Maman botir, Oydo‘stbiy, Ernazarbiy ulug‘lanadi.", True, "To‘g‘ri.")
t.TF("Qissaxonlar dostonlarni qo‘biz jo‘rligida kuylagan.", False, "Noto‘g‘ri: qissaxonlar qo‘lyozmalarni o‘qib yoki yoddan aytib bergan.")
t.TF4([("Ajiniyozdan yuzdan ortiq she’r va dostonlar meros qolgan.", True), ("«Qiz Mengesh bilan aytishuv» 1878-yilda yaratilgan.", True),
       ("Berdaq ijodi 40 yoshida boshlangan.", False), ("Ibroyim Yusupov «Ajiniyoz» asarini yaratgan.", True)],
      "3-noto‘g‘ri: ijodi 18–19 yoshida do‘mbira chertib she’r aytishdan boshlangan.")
t.MUL([("Qoraqalpoq qo‘shiqlari xalq, tarixiy va marosim qo‘shiqlariga bo‘lingan.", True),
       ("Berdaq qoraqalpoq xalq adabiyotining asoschisi hisoblanadi.", True),
       ("Kunxo‘ja Ibrohim XVIII asr boshida yashagan.", False)],
      "III noto‘g‘ri: Kunxo‘ja 1799–1880-yillarda yashagan.")
t.CHR("Ijodkorlarni tug‘ilgan yili bo‘yicha tartiblang.", ["Jiyen jirov", "Kunxo‘ja Ibrohim", "Ajiniyoz"],
      "1730 → 1799 → 1824.")
t.MATCH("Asarlarni mualliflari bilan moslashtiring.", ["«Bo‘zatov»", "«O‘roqchilar»", "«Ernazarbiy»", "«Ajiniyoz» asari"],
        ["Ajiniyoz", "Kunxo‘ja Ibrohim", "Berdaq", "Ibroyim Yusupov", "Jiyen jirov"], 'abcd',
        "Bo‘zatov – Ajiniyoz; O‘roqchilar – Kunxo‘ja; Ernazarbiy – Berdaq; «Ajiniyoz» – I. Yusupov.")
t.VENN("Jirovlar", "Baxshilar",
       [("qo‘biz jo‘rligida ijro", 1), ("qahramonlik dostonlari", 1),
        ("dutor va g‘ijjak jo‘rligida ijro", 2), ("ijro uslubi va kuyi boshqacha", 2),
        ("doston ijrochilari", 3)],
       "Jirovlar – qo‘biz; baxshilar – dutor, g‘ijjak; ikkalasi doston ijrochisi.")
t.MAPN('xorazm', ['Mo‘ynoq', 'Xiva', 'Ko‘hna Urganch', 'Hazorasp'], "Ajiniyoz boshlang‘ich ta’limni olgan joy xaritada qaysi raqam bilan belgilangan?",
       "Mo‘ynoq; keyin Xivadagi Sherg‘ozixon madrasasida o‘qigan.")

# 25-§ Qoraqalpoqlarning milliy kiyimlari
t = Topic('y9u25', 9025); TOPICS['y9u25'] = t
t.B("Bo‘z to‘n tikish uchun to‘qilgan yo‘l-yo‘l mato qanday atalgan?", "alasha", "shatirash", "movut", "olacha", "Alasha.")
t.B("Ayollar ko‘ylagi uchun ishlatilgan katak-katak mato qanday atalgan?", "shatirash", "alasha", "movut", "chit", "Shatirash.")
t.B("Ingichka tuya junidan tayyorlangan mato qaysi?", "movut (shol)", "alasha", "shatirash", "baxmal", "Movut (shol).")
t.B("Qoraqalpoq erkaklarining an’anaviy kiyimlari kimlarnikiga o‘xshaydi?", "xorazmliklarnikiga", "buxoroliklarnikiga", "qozoqlarnikiga", "ruslarnikiga", "Xorazmliklarnikiga.")
t.B("Keyinchalik erkaklar orasida qanday ko‘ylak urfga aylangan?", "no‘g‘ay yoqali ko‘ylak", "rus ko‘ylagi", "halqali ko‘ylak", "yengsiz ko‘ylak", "No‘g‘ay yoqali ko‘ylak.")
t.B("Jun, gazlama va movutdan tikilgan chakmon qoraqalpoqcha qanday ataladi?", "shekpen", "jegde", "kimishek", "jengse", "Shekpen.")
t.B("Bayram choponi ustidan bog‘lanadigan kamar qanday atalgan?", "kayis", "belbog‘", "jegde", "savkali", "Kayis.")
t.B("Qalpoqni yana qanday atashgan?", "takiya", "kimishek", "do‘ppi", "salla", "Takiya.")
t.B("Qoraqalpoq erkaklaridan kimlar salla o‘ragan?", "faqat din peshvolari", "barcha erkaklar", "yoshlar", "biylar", "Faqat din peshvolari.")
t.B("Ayollar boshiga yopib yurgan chopon qanday atalgan?", "jegde", "shekpen", "kayis", "jengse", "Jegde.")
t.B("Ayollar bayram ko‘ylaklari qayerdan keltirilgan shoyidan tikilgan?", "Buxorodan", "Xivadan", "Rossiyadan", "Xitoydan", "Buxorodan olib kelingan ola shoyidan.")
t.B("Yoqadan beligacha chillak shaklida kashta tikilgan ko‘ylak qanday atalgan?", "halqali ko‘ylak", "no‘g‘ay ko‘ylak", "kimishek", "jegde", "Halqali ko‘ylak.")
t.B("Azador ayollar qanday ko‘ylak kiygan?", "gulsiz ko‘k ko‘ylak", "qizil ko‘ylak", "oq ko‘ylak", "halqali ko‘ylak", "Gulsiz ko‘k ko‘ylak.")
t.B("Qoraqalpoq ayollarining mashhur bosh kiyimlari qaysilar?", "kimishek va savkali", "do‘ppi va salla", "telpak va qalpoq", "paranji va chachvon", "Kimishek va savkali.")
t.B("Kimishekni kim tikkan?", "qizning o‘zi", "kuyov", "ona", "usta tikuvchi", "Qizning o‘zi.")
t.B("Kimishekning old tarafi nimadan va qanday shaklda tikilgan?", "qizil movutdan uchburchak", "ko‘k shoyidan doira", "oq chitdan kvadrat", "baxmaldan to‘rtburchak", "Qizil movutdan uchburchak.")
t.B("Qizil guldor matodan alohida tayyorlanib, to‘nga tikiladigan yeng qanday ataladi?", "jengse", "jegde", "kayis", "shekpen", "Jengse.")
t.NAT("Qiz to‘yi kuni kimishek kiyadigan bo‘ldi.", "kimishek qiz yashaydigan har bir xonadonda albatta tikilgan", "kimishek faqat bozordan sotib olingan", "kimishek kiyish taqiqlangan", "kimishekni kuyov tikkan", "Har xonadonda tikilgan.")
t.NAT("Sovuq kunlar keldi.", "yupqa shalvar ustidan qalin chit yoki jun gazlamali issiq shim kiyilgan", "faqat ko‘ylak kiyilgan", "salla o‘ralgan", "kayis bog‘langan", "Issiq shim kiyilgan.")
t.NAT("Kimishekda boshga kiyish uchun maxsus teshik bo‘lgan.", "uni kuyov ovulidan kelgan ayol qizning bo‘yniga solib qo‘ygan", "uni qo‘lga taqishgan", "uni belga bog‘lashgan", "uni faqat erkaklar kiygan", "Bo‘yinga solingan.")
t.NAT("To‘quvchi ustalar kiyim uchun zarur gazlamalarni yetkazib berdi.", "alasha, shatirash, movut kabi matolar tayyorlandi", "matolar faqat chetdan keltirildi", "kiyim tikish to‘xtadi", "faqat teri kiyimlar kiyildi", "Mahalliy matolar to‘qildi.")
t.TF("Yoshlar bilan katta yoshdagi erkaklarning kiyimlari deyarli farq qilmagan.", True, "To‘g‘ri; kattalarniki sal keng va uzunroq.")
t.TF("Qoraqalpoq erkaklari shalvar poychalarini etik ustidan qo‘yib kiygan.", False, "Noto‘g‘ri: poychalar etik ichiga tiqib kiyilgan.")
t.TF4([("Qoraqalpoqlar qishda po‘stin va qalpoq kiygan.", True), ("Kimishekning orqasidan uzun guldor «kokil» osilib turgan.", True),
       ("Qoraqalpoqlarda chopon kam tarqalgan.", False), ("Qishda jun paypoq kiyilgan.", True)],
      "3-noto‘g‘ri: chopon keng tarqalgan.")
t.MUL([("Qoraqalpoq ayollarining kiyimi ko‘ylak, lozim, kamzul va yengsiz chopondan iborat.", True),
       ("Po‘stin, qalpoq va poyabzalbop teriga mahorat bilan ishlov berilgan.", True),
       ("Qalpoq kichik va tor qilib tikilgan.", False)],
      "III noto‘g‘ri: qalpoq katta va keng qilib tikilgan.")
t.CHR("Kimishek bilan bog‘liq jarayonni tartiblang.", ["qiz kimishekni o‘zi tikadi", "to‘y kuni kuyov ovulidan ayollar keladi", "ayol kimishekni qizning bo‘yniga soladi", "qiz kimishekni kiyib ovulga boradi"],
      "Tikish → ayollar kelishi → bo‘yinga solish → kiyib borish.")
t.MATCH("Kiyim nomlarini izohi bilan moslashtiring.", ["shekpen", "jegde", "kimishek", "jengse"],
        ["jun yoki movutdan chakmon", "ayollar boshga yopadigan chopon", "qiz to‘yda kiyadigan bosh kiyim", "qizil guldor matodan alohida yeng", "erkaklar etigi"], 'abcd',
        "Shekpen – chakmon; jegde – bosh choponi; kimishek – to‘y bosh kiyimi; jengse – yeng.")
t.VENN("Erkaklar kiyimi", "Ayollar kiyimi",
       [("shalvar va dambal", 1), ("takiya (qalpoq)", 1),
        ("kimishek va savkali", 2), ("halqali ko‘ylak", 2),
        ("chopon", 3)],
       "Erkaklar – shalvar, takiya; ayollar – kimishek, halqali ko‘ylak; umumiy – chopon.")
t.MAPN('uzb', ['Buxoro', 'Xiva', 'Samarqand', 'Toshkent'], "Qoraqalpoq ayollarining bayram ko‘ylaklari uchun ola shoyi va kimishek orqasi uchun shoyi olib kelingan shahar xaritada qaysi raqamda?",
       "Buxoro.")
