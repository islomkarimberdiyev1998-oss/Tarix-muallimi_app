from qlib import Topic, PLACES, REG
TOPICS = {}

# 22-§ Qoraqalpoqlarning qo‘shni xalqlar bilan munosabatlari
t = Topic('y9u22', 9022); TOPICS['y9u22'] = t
t.B("Qoraqalpoq tili qaysi tillar guruhiga kiradi?", "qipchoq tillari guruhining qipchoq-no‘g‘ay shoxobchasi", "o‘g‘uz guruhi", "qarluq guruhi", "fors tillari", "Qipchoq-no‘g‘ay shoxobchasi.")
t.B("Qoraqalpoqlar antropologik jihatdan kimlarga yaqin?", "qozoqlar, Xorazm mang‘itlari, quramalar", "forslar", "arablar", "ruslar", "Qozoqlar, Xorazm mang‘itlari va quramalarga.")
t.B("X–XI asrlarda qoraqalpoqlar yashagan hududlar qaysi davlatga bo‘ysungan?", "O‘g‘uz davlatiga", "Somoniylarga", "Oltin O‘rdaga", "Xiva xonligiga", "O‘g‘uz davlatiga, keyin Xorazmga.")
t.B("Eshmuhammadxon Rossiyaga qachon elchilar yuborgan?", "1721-yilda", "1723-yilda", "1731-yilda", "1743-yilda", "1721-yilda.")
t.B("Jung‘orlar qaysi xalq hisoblanadi?", "qalmiqlar – g‘arbiy mo‘g‘ullar", "qozoqlar", "boshqirdlar", "no‘g‘aylar", "Qalmiqlar – g‘arbiy mo‘g‘ullar.")
t.B("Jung‘or davlati qachon tashkil topgan?", "1635-yilda", "1723-yilda", "1758-yilda", "1556-yilda", "1635-yilda.")
t.B("Jung‘or davlati qachon va kim tomonidan tugatilgan?", "1758-yilda Chin imperiyasi", "1723-yilda Rossiya", "1811-yilda Xiva", "1731-yilda qozoqlar", "1758-yilda Chin imperiyasi.")
t.B("Quyi qoraqalpoqlarning asosiy qismi qayerda joylashgan?", "Quvondaryo atrofida", "Toshkentda", "Talas bo‘yida", "Farg‘onada", "Quvondaryo atrofida.")
t.B("1731-yilda Rossiya Abulxayrxon huzuriga kimni yuborgan?", "M. Tevkelevni", "Bekovichni", "Perovskiyni", "Mamanbiyni", "M. Tevkelevni.")
t.B("1743-yilda Peterburgga yuborilgan elchilikka kim boshchilik qilgan?", "Mamanbiy", "Oydo‘stbiy", "Eshimxon", "Tevkelev", "Atoqli botir Mamanbiy.")
t.B("Qozoq xoni Abulxayrxon qoraqalpoqlarning bir qismini qaysi daryo bo‘yiga ko‘chishga majburlagan?", "Talas", "Chirchiq", "Zarafshon", "Ili", "Talas daryosi bo‘yiga.")
t.B("Qoraqalpoqlarning asosiy qismi qaysi daryolar bo‘yiga ko‘chgan?", "Yangidaryo va Quvondaryo", "Talas va Chu", "Zarafshon va Qashqadaryo", "Murg‘ob va Tajan", "Yangidaryo va Quvondaryo.")
t.B("Muhammad Amin inoq qaysi yillarda hukmronlik qilgan?", "1770–1790", "1790–1804", "1806–1825", "1825–1842", "1770–1790.")
t.B("Qoraqalpoqlar qachon to‘la Xiva xonligiga bo‘ysundirilgan?", "1811-yilda", "1770-yilda", "1827-yilda", "1743-yilda", "1811-yilda.")
t.B("Muhammad Rahimxon I Oydo‘stbiyni qanday lavozimga tayinlagan?", "biylar biyi", "mehtar", "qushbegi", "mirob", "Biylar biyi.")
t.B("Oydo‘stbiy qo‘zg‘oloni qachon boshlangan?", "1827-yilda", "1811-yilda", "1842-yilda", "1790-yilda", "1827-yilda.")
t.B("Oydo‘stbiy qo‘zg‘olonini bostirgan Xiva xoni kim?", "Olloqulixon", "Muhammad Rahimxon I", "Eltuzarxon", "Muhammad Aminxon", "Olloqulixon.")
t.NAT("XVIII asrning 20-yillari boshida jung‘orlar hujumi xavfi kuchaydi.", "qoraqalpoq xoni Rossiya bilan yaqinlashish yo‘llarini qidirdi", "qoraqalpoqlar Jung‘orga qo‘shildi", "Rossiya qoraqalpoqlarga qarshi chiqdi", "qoraqalpoqlar Xivaga hujum qildi", "Rossiya bilan yaqinlashuv.")
t.NAT("1723-yilda jung‘orlarning hujumi boshlandi.", "qoraqalpoq xalqi uch guruhga bo‘linib ketdi", "qoraqalpoqlar jung‘orlarni yengdi", "Rossiya qoraqalpoqlarni himoya qildi", "qoraqalpoqlar birlashdi", "Xalq uch guruhga bo‘lindi.")
t.NAT("Rossiya saroyidagi nizolar tufayli qoraqalpoqlarga berilgan yorliq unutildi.", "Abulxayrxon qoraqalpoqlar yurtiga hujum qilib, ularni qayta bo‘ysundirdi", "qoraqalpoqlar mustaqil bo‘ldi", "Xiva qoraqalpoqlarni himoya qildi", "Mamanbiy xon bo‘ldi", "Kichik juzga qayta qaramlik.")
t.NAT("Olloqulixon Oydo‘stbiyga berilgan imtiyozlarni bekor qildi va soliqlar oshirildi.", "1827-yilda Oydo‘stbiy boshchiligida qo‘zg‘olon ko‘tarildi", "Oydo‘stbiy Rossiyaga ketdi", "qoraqalpoqlar soliqdan ozod bo‘ldi", "Oydo‘stbiy mehtar bo‘ldi", "Qo‘zg‘olon boshlandi.")
t.TF("Rossiyaning O‘rta Osiyoga savdo karvon yo‘li qoraqalpoqlar hududidan o‘tgan.", True, "To‘g‘ri.")
t.TF("1731-yilgi muzokaralarga ko‘ra qoraqalpoqlar o‘lponni to‘g‘ridan to‘g‘ri Rossiyaga to‘lay boshlagan.", False, "Noto‘g‘ri: Kichik juz xonligiga o‘lpon to‘lashi tan olingan; Rossiyaga to‘lash 1743-yilda Mamanbiy yorlig‘i bilan.")
t.TF4([("Qoraqalpoqlar shartli ravishda «quyi» va «yuqori» qoraqalpoqlarga bo‘lingan.", True), ("Orollik o‘zbeklar Xiva markaziy hokimiyatiga muxolif bo‘lgan.", True),
       ("Hal qiluvchi jangda Oydo‘stbiy g‘alaba qozongan.", False), ("Muhammad Amin inoq davrida qoraqalpoqlar ixtiyoriy Xiva fuqaroligiga o‘ta boshlagan.", True)],
      "3-noto‘g‘ri: qo‘zg‘olonchilar tor-mor etilib, Oydo‘stbiy va ikki o‘g‘li halok bo‘lgan.")
t.MUL([("Yangidaryodagi sug‘orish inshootlari qoraqalpoq ajdodlari mehnatining xotirasidir.", True),
       ("1726-yilgi Abulxayrxon elchilari tarkibida qoraqalpoqlar vakili ham bo‘lgan.", True),
       ("Qoraqalpoqlar XVII asrda Rossiya tarkibiga kiritilgan.", False)],
      "III noto‘g‘ri: XIX asrning ikkinchi yarmida Rossiya tarkibiga kiritilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Eshmuhammadxon Rossiyaga elchi yubordi", "Jung‘orlar hujumi boshlandi", "Tevkelev Abulxayrxon huzuriga yuborildi", "Mamanbiy Peterburgga bordi", "Qoraqalpoqlar to‘la Xivaga bo‘ysundirildi", "Oydo‘stbiy qo‘zg‘oloni"],
      "1721 → 1723 → 1731 → 1743 → 1811 → 1827.")
t.MATCH("Shaxslarni ular haqidagi ma’lumot bilan moslashtiring.", ["Eshmuhammadxon", "Mamanbiy", "M. Tevkelev", "Oydo‘stbiy"],
        ["1721-yilda Rossiyaga elchi yuborgan xon", "1743-yilda Peterburgdan yorliq olgan botir", "1731-yilda Abulxayrxonga yuborilgan rus elchisi", "1827-yilgi qo‘zg‘olon rahbari", "Jung‘or xoni"], 'abcd',
        "Eshmuhammadxon – 1721; Mamanbiy – 1743; Tevkelev – 1731; Oydo‘stbiy – 1827.")
t.VENN("Qoraqalpoq–Rossiya munosabatlari", "Qoraqalpoq–Xiva munosabatlari",
       [("1743-yilgi Mamanbiy yorlig‘i", 1), ("savdo yo‘llari xavfsizligi", 1),
        ("1811-yilda to‘la bo‘ysundirish", 2), ("Oydo‘stbiy qo‘zg‘oloni", 2),
        ("XVIII–XIX asrlardagi qoraqalpoqlar tashqi aloqalari", 3)],
       "Rossiya – yorliq, savdo yo‘llari; Xiva – 1811, Oydo‘stbiy; ikkalasi qoraqalpoqlar munosabatlari.")
t.MAPMATCH('steppe', ['Toshkent', 'Talas', 'Xiva', 'Orol dengizi'],
           ["yuqori qoraqalpoqlarning bir qismi siljigan shahar", "Abulxayrxon qoraqalpoqlarni majburan ko‘chirgan daryo bo‘yi", "1811-yilda qoraqalpoqlar to‘la bo‘ysungan xonlik poytaxti", "quyi qoraqalpoqlar siljigan dengiz"],
           "1 – Toshkent; 2 – Talas; 3 – Xiva; 4 – Orol dengizi.")

# 23-§ Qoraqalpoqlarning turmush tarzi
t = Topic('y9u23', 9023); TOPICS['y9u23'] = t
t.B("Qoraqalpoqlarda har bir urug‘ yoki qabilaga kim boshchilik qilgan?", "biylar", "botirlar", "oqsoqollar", "xo‘jalar", "Biylar.")
t.B("Qoraqalpoqlarda harbiy qismlarni kim boshqargan?", "botirlar", "biylar", "qozilar", "shayxlar", "Botirlar.")
t.B("Qoraqalpoqlarda boshlang‘ich ma’muriy bo‘g‘in nima edi?", "ovul", "beklik", "tuman", "mahalla", "Ovul.")
t.B("Ovul hayotiga qaysi kengash rahbarlik qilgan?", "Oqsoqollar kengashi", "Oliy Kengash", "Biylar kengashi", "Kichik Kengash", "Oqsoqollar kengashi.")
t.B("Xivaga bo‘ysundirilgach, biylar biyi kim tomonidan tayinlangan?", "xon tomonidan", "urug‘ yig‘inida", "Rossiya tomonidan", "qozilar tomonidan", "Xon tomonidan.")
t.B("Amudaryoning so‘l sohilidagi qoraqalpoqlar ma’muriy markazi qaysi?", "Qo‘ng‘irot", "Chimboy", "Xiva", "Nukus", "Qo‘ng‘irot.")
t.B("Amudaryoning o‘ng sohilidagi qoraqalpoqlar ma’muriy markazi qaysi?", "Chimboy", "Qo‘ng‘irot", "Xo‘jayli", "Urganch", "Chimboy.")
t.B("Qaysi dostonda qoraqalpoqlarning yer o‘zlashtirishi haqida ma’lumot bor?", "«Qirqqiz»", "«Alpomish»", "«Go‘ro‘g‘li»", "«Manas»", "«Qirqqiz».")
t.B("XVIII asr oxirida Amudaryo quyi tarmoqlarida qaysi dehqonchilik vohalari vujudga kelgan?", "Qalliko‘l, Kegayli", "Chimboy, Qo‘ng‘irot", "Xiva, Hazorasp", "Quvondaryo, Yangidaryo", "Qalliko‘l va Kegayli.")
t.B("Chorva mollari uchun to‘yimli ozuqa bo‘lib xizmat qilgan o‘simlik qaysi?", "mayda qamish", "beda", "makkajo‘xori", "yantoq", "Mayda qamish.")
t.B("Qoraqalpoq egarchilari egar yasaydigan qolip nima deb atalgan?", "otorqa", "o‘rmak", "urchuq", "chig‘ir", "Otorqa.")
t.B("Egar necha bo‘lakdan yig‘ilgan?", "sakkiz", "to‘rt", "o‘n ikki", "ikki", "Sakkiz bo‘lakdan.")
t.B("Gilam va sholcha to‘qish uchun ishlatilgan moslama qanday atalgan?", "o‘rmak", "urchuq", "otorqa", "mola", "O‘rmak.")
t.B("Qaysi urug‘ ayollari nihoyatda mohir to‘quvchi bo‘lgan?", "kenagas va mang‘it", "qo‘ng‘irot va xitoy", "nayman va qipchoq", "do‘rmon va burgut", "Kenagas va mang‘it ayollari.")
t.B("Qoraqalpoqlar o‘tovni qanday atagan?", "«qora uy»", "«qoqra»", "«oq uy»", "«yerto‘la»", "«Qora uy».")
t.B("Loysuvoq uylar qanday nom bilan ma’lum bo‘lgan?", "qoqra", "qora uy", "o‘tov", "hovli", "Qoqra.")
t.B("Qoraqalpoq dehqonlaridan olingan yer solig‘i qanday atalgan?", "salg‘ut", "zakot", "ushur", "qozon", "Salg‘ut.")
t.B("Harbiy xavf yuz berganda qanday soliq undirilgan?", "qozon (xo‘jalik) solig‘i", "salg‘ut", "ushur", "tanob puli", "Qozon solig‘i.")
t.NAT("Yerga jamoa bo‘lib egalik qilish barham topib, katta yer egaligi vujudga keldi.", "yersiz va chorvasiz kambag‘allar soni ko‘paydi", "barcha aholi boyidi", "yer solig‘i bekor qilindi", "urug‘chilik kuchaydi", "Mulkiy tabaqalanish kuchaydi.")
t.NAT("Orol bo‘ylari va daryo havzalari baliqqa boy edi.", "baliqchilik aholi uchun qo‘shimcha tirikchilik manbayi bo‘ldi", "baliq ovlash taqiqlandi", "dehqonchilik to‘xtadi", "aholi ko‘chib ketdi", "Baliqchilik rivojlandi.")
t.NAT("Yangidaryo va Quvondaryo havzalarida kanal va sug‘orish inshootlari barpo etildi.", "bu dehqonchilikning xo‘jalikda yetakchi o‘rinda bo‘lganidan guvohlik beradi", "chorvachilik yo‘qoldi", "qoraqalpoqlar ko‘chmanchi bo‘lib qoldi", "inshootlar tezda buzildi", "Dehqonchilik yetakchi bo‘lgan.")
t.NAT("Biy va amaldorlar o‘z xarajatlarini qoplash uchun qo‘shimcha soliqlar undirdi.", "xalqning soliq yuki og‘irlashdi", "aholi boyidi", "soliqlar kamaydi", "xon soliqlarni bekor qildi", "Soliq yuki oshdi.")
t.TF("Qoraqalpoqlar orasida chig‘ir, qayiq va o‘tov yasaydigan ustalar ko‘p bo‘lgan.", True, "To‘g‘ri.")
t.TF("Yer solig‘i har bir xo‘jalikka alohida-alohida solingan.", False, "Noto‘g‘ri: butun qabila yoki urug‘ga biryo‘la solingan.")
t.TF4([("XIX asr o‘rtalarida Chimboy va Qo‘ng‘irot dehqonchilik vohalari vujudga kelgan.", True), ("Ip yigirish uchun urchuq ishlatilgan.", True),
       ("Chorvadorlardan salg‘ut solig‘i olingan.", False), ("Yigitlar majburiy harbiy xizmatga chaqirilgan.", True)],
      "3-noto‘g‘ri: chorvadorlardan zakot, dehqonlardan salg‘ut olingan.")
t.MUL([("Qoraqalpoqlarda yuzboshi, mirobboshi, qozi, rais mansablari bo‘lgan.", True),
       ("Yirik boylarning paxsadan qurilgan katta hovlilari bo‘lgan.", True),
       ("Ruhoniylar uchun salg‘ut solig‘i olingan.", False)],
      "III noto‘g‘ri: ruhoniylar uchun ushur solig‘i olingan.")
t.CHR("Dehqonchilik vohalarining paydo bo‘lishini tartiblang.", ["Yangidaryo va Quvondaryo sug‘orish inshootlari (XVIII asr o‘rtasi)", "Qalliko‘l va Kegayli vohalari (XVIII asr oxiri)", "Chimboy va Qo‘ng‘irot vohalari (XIX asr o‘rtasi)"],
      "XVIII asr o‘rtasi → XVIII asr oxiri → XIX asr o‘rtasi.")
t.MATCH("Soliqlarni kimdan olinishi bilan moslashtiring.", ["salg‘ut", "zakot", "ushur", "qozon"],
        ["dehqonlardan yer solig‘i", "chorvadorlardan", "ruhoniylar uchun aholidan", "harbiy xavfda xo‘jalikdan", "savdogarlardan boj"], 'abcd',
        "Salg‘ut – dehqon; zakot – chorvador; ushur – ruhoniylar uchun; qozon – harbiy xavfda.")
t.VENN("O‘tov («qora uy»)", "Qoqra",
       [("har qanday sharoitga mos ko‘chma uy", 1), ("ustalar yasagan yog‘och karkasli uy", 1),
        ("loysuvoq uy", 2), ("doimiy joyda qurilgan", 2),
        ("qoraqalpoqlar turarjoyi", 3)],
       "O‘tov – ko‘chma; qoqra – loysuvoq; ikkalasi qoraqalpoq uyi.")
t.MAPMATCH('xorazm2', ['Qo‘ng‘irot', 'Chimboy', 'Xiva', 'Orol dengizi'],
           ["Amudaryo so‘l sohilidagi qoraqalpoqlar markazi", "Amudaryo o‘ng sohilidagi qoraqalpoqlar markazi", "biylar biyini tayinlagan xon poytaxti", "baliqchilik rivojlangan dengiz"],
           "1 – Qo‘ng‘irot; 2 – Chimboy; 3 – Xiva; 4 – Orol dengizi.")
