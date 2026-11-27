from qlib import Topic
TOPICS = {}
CA = 'ca'; FV = 'fargona'; XR = 'xorazm'

# 20 Milliy-ozodlik harakatlarining ahamiyati
t = Topic('e9u20', 9020); TOPICS['e9u20'] = t
t.B("Mustamlakachilik davrida Turkiston o‘lkasi nimaga aylandi?", "arzon xomashyo bazasi va tayyor bozorga", "sanoat markaziga", "mustaqil davlatga", "harbiy flot bazasiga", "O‘lka arzon xomashyo bazasi, tayyor bozor, aholisi arzon ishchi kuchiga aylandi.")
t.B("Milliy-ozodlik harakatlarining asosiy sabablaridan biri nima edi?", "soliq va majburiyatlarning og‘irligi", "temiryo‘llarning yo‘qligi", "madrasalarning ko‘pligi", "xonliklarning birlashuvi", "Soliq va majburiyatlarning og‘irligi.")
t.B("Ko‘chirib keltirilgan aholiga nima bo‘lib berilgani norozilikka sabab bo‘lgan?", "yangi ekin maydonlari", "harbiy lavozimlar", "madrasalar", "savdo do‘konlari", "Yangi ekin maydonlari bo‘lib berilgan.")
t.B("XIX asr ikkinchi yarmidagi milliy-ozodlik harakatlariga kimlar boshchilik qilgan?", "Po‘latxon, Qurbonjon dodxoh, Yetimxon, Darvishxon, Muhammad Ali eshon", "Kaufman, Skobelev, Chernyayev", "Munis, Ogahiy, Ahmad Donish", "Jo‘rabek, Abdumalik to‘ra, Nasriddinbek", "Po‘latxon, Qurbonjon dodxoh, Yetimxon, Darvishxon, Muhammad Ali eshon.")
t.B("Qo‘zg‘olonlar xarakteriga ko‘ra qanday ko‘rinishda yuz bergan?", "milliy-ozodlik", "saroy to‘ntarishi", "diniy urush", "fuqarolar urushi", "Asosiy kuchi keng xalq ommasi bo‘lgani uchun milliy-ozodlik ko‘rinishida.")
t.B("Qo‘zg‘olonlar bostirilgach, ishtirokchilar nima qilgan?", "o‘lkaning turli hududlariga qochib borib, harakatlarini davom ettirgan", "Rossiyaga ketgan", "mustamlakachilarga xizmat qilgan", "kurashni butunlay to‘xtatgan", "Ular turli hududlarga qochib, kurashni davom ettirgan.")
t.B("Mustamlakachi hukumat qo‘zg‘olonlardan keyin qanday siyosat olib borish kerakligini angladi?", "ehtiyotkor va vazmin siyosat", "o‘lkadan chiqib ketish", "barcha soliqlarni bekor qilish", "o‘lkani mustaqil qilish", "O‘lkani qo‘ldan chiqarmaslik uchun ehtiyotkor va vazmin siyosat.")
t.B("Mustamlakachilik davrida o‘lka aholisi nimaga aylandi?", "arzon ishchi kuchiga", "imtiyozli tabaqaga", "harbiy qo‘shinga", "savdogarlar jamoasiga", "Aholi arzon ishchi kuchiga aylandi.")
t.B("Yangi ishlab chiqarish va texnologiyalar kimning manfaatlariga xizmat qilgan?", "faqat imperiya manfaatlariga", "mahalliy dehqonlarga", "hunarmandlarga", "Buxoro amiriga", "Ular faqat imperiya manfaatlariga xizmat qilgan.")
t.NAT("Har bir qo‘zg‘olonning aks sadosi butun o‘lka bo‘ylab tarqaldi.", "boshqa joylarda ham norozilik chiqishlari ko‘tarildi", "qo‘zg‘olonlar to‘xtadi", "mustamlaka tugadi", "aholi Rossiyaga ko‘chdi", "Qo‘zg‘olonlar boshqa joylar aholisiga ruhan ta’sir ko‘rsatdi.")
t.NAT("Qo‘zg‘olonlarda har qanday jabr-zulm va qattiq jazolar xalqni ezgu niyatlaridan chekintirmadi.", "podsho hukumati tub aholining ozodlik yo‘lidan qaytmasligini tushunib yetdi", "hukumat o‘lkani tark etdi", "qo‘zg‘olonchilar taslim bo‘ldi", "soliqlar oshirildi", "Hukumat buni tushunib yetdi.")
t.TF("Qo‘zg‘olonlarda dehqonlar, hunarmandlar, ulamolar, oqsoqollar, mingboshilar, qozilar va savdogarlar ishtirok etgan.", True, "To‘g‘ri.")
t.TF("Milliy-ozodlik harakatlarida faqat bitta xalq vakillari ishtirok etgan.", False, "Noto‘g‘ri: o‘lka xalqlarining deyarli barchasidan vakillar ishtirok etgan.")
t.TF("Mahalliy aholi uchun tibbiy xizmatning yo‘qligi ham norozilik sabablaridan biri bo‘lgan.", True, "To‘g‘ri.")
t.MUL([("Qo‘zg‘olonlarda siyosiy, ijtimoiy, iqtisodiy va milliy-ozodlik kurashlari birlashgan holda sodir bo‘lgan.", True),
       ("Milliy-ozodlik harakatlari Turkistonning istilo yo‘li bilan bosib olinganini yana bir karra isbotlagan.", True),
       ("Milliy-ozodlik harakatlari faqat XX asrda boshlangan.", False)],
      "III noto‘g‘ri: ular XIX asr o‘rtalaridan boshlangan.")
t.MATCH("Qo‘zg‘olon rahbarlarini voqealar bilan moslashtiring.", ["Po‘latxon", "Yetimxon", "Darvishxon", "Muhammad Ali eshon"],
        ["1885-yil Andijondagi qo‘zg‘olon", "1898-yil Andijon qo‘zg‘oloni", "1875-yil Qo‘qon xonligidagi qo‘zg‘olon", "1878-yil Mingtepadagi qo‘zg‘olon"], "cdab",
        "Po‘latxon — 1875; Yetimxon — 1878; Darvishxon — 1885; Dukchi eshon — 1898.")
t.CHR("Qo‘zg‘olonlarni xronologik tartibda joylashtiring.", ["Po‘latxon qo‘zg‘oloni", "Yetimxon qo‘zg‘oloni", "Darvishxon qo‘zg‘oloni", "«Vabo isyoni»", "Andijon qo‘zg‘oloni"],
      "1875 → 1878 → 1885 → 1892 → 1898.")
t.MAPMATCH(CA, ['Toshkent', 'Andijon', 'Qo‘qon'],
           ["1892-yilgi «Vabo isyoni» bo‘lgan shahar", "1898-yilda Dukchi eshon qo‘zg‘oloni bo‘lgan shahar", "1875-yilda Po‘latxon qo‘zg‘oloni boshlangan xonlik poytaxti"],
           "1 – Toshkent; 2 – Andijon; 3 – Qo‘qon.")
t.VENN("Qo‘zg‘olonlarning sabablari", "Qo‘zg‘olonlarning ahamiyati",
       [("narx-navolarning oshib ketishi", 1), ("mahalliy boshqaruv vakillarining sotqinligi", 1),
        ("boshqa hududlar aholisini ruhlantirgan", 2), ("Vatan tarixida milliy mustaqillik kurashi sifatida o‘rin tutgan", 2),
        ("mustamlakachilik tartiblariga qarshi qaratilgan", 3)],
       "Sabablar — narxlar, sotqinlik; ahamiyati — ruhlantirgan, tarixda o‘rin; umumiy — mustamlakaga qarshi.")

# 21 Qoraqalpoqlarning hududiy joylashuvi va ijtimoiy hayoti
t = Topic('e9u21', 9021); TOPICS['e9u21'] = t
t.B("Qoraqalpoqlar XIX asr boshlarida qayerda muqim hayot tarziga o‘ta boshlagan?", "quyi Amudaryo havzasi, Orolning janub va janubi g‘arbida", "Farg‘ona vodiysida", "Zarafshon vodiysida", "Yettisuvda", "Quyi Amudaryo havzasi, Orolning janubi va janubi g‘arbida.")
t.B("Qoraqalpoqlar kimlarning hujumlari oqibatida Xiva xonligi fuqaroligiga o‘tgan?", "qozoqlar va turkmanlar", "ruslar va inglizlar", "afg‘onlar", "qirg‘izlar", "Qozoqlar va turkmanlar hujumlari oqibatida.")
t.B("XIX asr o‘rtalarida qoraqalpoqlar soni qancha bo‘lgan?", "100 ming nafardan oshmagan", "1 million", "800 ming", "2 million", "Taxminan 100 ming nafardan oshmagan.")
t.B("Qoraqalpoqlarda yerdan foydalanish qanday tariqada kechgan?", "jamoa tariqasida", "xususiy tarzda", "vaqf tarzida", "ijara asosida", "Jamoa tariqasida.")
t.B("Qoraqalpoqlarda sug‘orish kanallari qazilishi uchun kim mas’ul bo‘lgan?", "urug‘lar", "xon", "beklarbegi", "qozilar", "Urug‘lar mas’ul bo‘lgan.")
t.B("«Qoraqalpoq ulusi»ni kim shakllantirgan?", "Muhammad Rahimxon I", "Muhammad Rahimxon II", "Eltuzar", "Ollohqulixon", "Muhammad Rahimxon I.")
t.B("Qoraqalpoq urug‘larini boshqarish uchun qaysi oliy amaldorlar tayinlangan?", "otaliq va beklarbegi", "qo‘shbegi va devonbegi", "mirob va mutavalli", "parvonachi va dodxoh", "Otaliq va beklarbegi.")
t.B("Qoraqalpoqlarda sudlarning qanday turlari bo‘lgan?", "qozilar sudi va biylar sudi", "okrug va mirovoy sudlari", "harbiy sudlar", "faqat qozi sudi", "Qozilar sudi va biylar sudi.")
t.B("Xitoy-qipchoq, mang‘it va kenagas qabilalari urug‘lari qanday birlashmani tashkil qilgan?", "«o‘n to‘rt urug‘»", "aris-qo‘ng‘irot", "Qoraqalpoq ulusi", "Kichik juz", "«O‘n to‘rt urug‘» aris birlashmasi.")
t.B("Harbiy kuch borasida ikkinchi o‘rinda qaysi aris turgan?", "aris-qo‘ng‘irotlar", "o‘n to‘rt urug‘", "mang‘itlar", "kenagaslar", "Shulluk va joungurni birlashtirgan aris-qo‘ng‘irotlar.")
t.B("Urug‘ biylarini kim tayinlagan?", "Xiva xonlari", "Buxoro amiri", "Turkiston general-gubernatori", "urug‘ oqsoqollari", "Xiva xonlari tayinlab, yorliq bergan.")
t.B("Qoraqalpoq urug‘larini boshqarish, soliq undirish va harbiy xizmatni tartibga solish uchun qanday lavozim tayin etilgan?", "beklarbegi", "otaliq", "mirob", "qozi", "Beklarbegi lavozimi.")
t.B("Qoraqalpoqlar va boshqa turkiy xalqlarning ma’naviy mulki bo‘lgan doston qaysi?", "«Qirqqiz»", "«Alpomish»", "«Go‘ro‘g‘li»", "«Shirin va Shakar»", "«Qirqqiz» dostoni.")
t.NAT("Qaroqchi guruhlar qoraqalpoq o‘tovlariga to‘satdan hujum qilar edi.", "yurt oqsoqollari Xiva xonidan himoya so‘rab chopar yo‘llardi", "qoraqalpoqlar Rossiyaga ko‘chdi", "chorvachilik to‘xtadi", "qoraqalpoqlar mustaqil bo‘ldi", "Oqsoqollar Xiva xonidan himoya so‘ragan.")
t.NAT("Urug‘ oqsoqollari, ruhoniylar va biylarning yer-suv va chorvadagi ulushi katta bo‘ldi.", "tabaqalanish jarayoni tezlashdi", "urug‘lar tarqalib ketdi", "tenglik o‘rnatildi", "dehqonchilik to‘xtadi", "Bu XIX asr ikkinchi yarmida tabaqalanishni tezlashtirdi.")
t.TF("Qoraqalpoqlarda chorva xususiy mulk bo‘lgani uchun unga urug‘ tamg‘asi urilgan.", True, "To‘g‘ri.")
t.TF("Qoraqalpoqlarning barcha urug‘lari uchun yagona umumiy qabriston bo‘lgan.", False, "Noto‘g‘ri: har bir urug‘ning qabristoni alohida edi.")
t.MUL([("Qoraqalpoqlar hayotida baliqchilik va ovchilik muhim o‘rin egallagan.", True),
       ("Ular yog‘och va suyakka ishlov berishda qo‘li gul usta bo‘lgan.", True),
       ("O‘troq hayotga o‘tgach, qoraqalpoqlar chorvachilikni butunlay tashlagan.", False)],
      "III noto‘g‘ri: chorvachilik yetakchi sohalardan biri bo‘lib qolaverdi.")
t.MAPN(XR, ['Xiva', 'Hazorasp', 'Orol bo‘yi', 'Qo‘ng‘irot'], "Qoraqalpoqlar Orol dengiziga quyiladigan yerlarda yashagan. Qaysi raqam bilan Orol bo‘yidagi hudud belgilangan?",
       "3 – Orol bo‘yi; qoraqalpoqlar quyi Amudaryo va Orol bo‘yida yashagan.", ask_idx=2)
t.VENN("Qoraqalpoqlarning xo‘jaligi", "Qoraqalpoqlarning hunarmandchiligi",
       [("dehqonchilik va chorvachilik", 1), ("baliqchilik va ovchilik", 1),
        ("tuya junidan guldor namat to‘qish", 2), ("o‘ymakor eshiklar yasash", 2),
        ("ro‘zg‘or ehtiyojlarini ta’minlagan", 3)],
       "Xo‘jalik — dehqonchilik, baliqchilik; hunarmandchilik — namat, o‘ymakorlik.")
