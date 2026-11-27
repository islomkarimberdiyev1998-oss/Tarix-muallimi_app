from qlib import Topic, PLACES, REG
TOPICS = {}

# 14 Koreya
t = Topic('y7j14', 7014); TOPICS['y7j14'] = t
t.B("Ilk koreys davlati qanday atalgan?", "Choson", "Koryo", "Silla", "Pekche", "Choson – ilk koreys davlati.")
t.B("«Choson» so‘zi koreyschada qanday ma’noni anglatadi?", "«Tonggi tarovat»", "«Kunchiqar mamlakat»", "«Osmonosti»", "«Baxtli o‘lka»", "«Tonggi tarovat».")
t.B("Choson davlatining afsonaviy asoschisi kim?", "Tangun", "Jumong", "Van Gon", "Van In", "Afsonaviy Tangun.")
t.B("Choson qirolligining poytaxti qaysi shahar bo‘lgan?", "Pxenyan", "Sonak", "Seul", "Kunneson", "Pxenyan (Pxenbin).")
t.B("Mil. avv. I asrda Choson qaysi uch qirollikka bo‘lingan?", "Pekche, Silla, Koguryo", "Koryo, Silla, Choson", "Tan, Suy, Xan", "Koguryo, Koryo, Pekche", "Pekche, Silla va Koguryo.")
t.B("«Uch qirollik davri» qancha davom etgan?", "qariyb yetti asr", "yuz yil", "uch asr", "ming yil", "Qariyb yetti asr.")
t.B("Koguryo qirolligining asoschisi kim?", "Jumong (Tonmyon)", "Tangun", "Van Gon", "Xvanun", "Jumong (Tonmyon).")
t.B("V asrda Koguryoning poytaxti qaysi shaharga ko‘chirilgan?", "Pxenyanga", "Sonakka", "Kunnesonga", "Seulga", "Kunneson qal’asidan Pxenyanga.")
t.B("Koguryo qachon Tan sulolasi tomonidan bosib olingan?", "668-yilda", "918-yilda", "1231-yilda", "IV asr boshida", "668-yilda.")
t.B("Pekche davlati qachon vujudga kelgan?", "III–IV asrlarda", "mil. avv. I asrda", "VII asrda", "X asrda", "Yarimorolning janubida III–IV asrlarda.")
t.B("Yaponiya taxt vorisi shahzodaga ustozlik qilgan pekchelik olim kim?", "Van In", "Van Gon", "Jumong", "Tangun", "Pekchelik olim Van In.")
t.B("Koreyaga iyerogliflar va buddizm qaysi sulola hukmdorlari orqali kirib kelgan?", "Pekche", "Silla", "Koguryo", "Koryo", "Pekche sulolasi hukmdorlari orqali.")
t.B("Silla qirolligi Koreya yarimorolini qachon birlashtirgan?", "668-yilda", "918-yilda", "1392-yilda", "VIII asr o‘rtalarida", "668-yilda Tan sulolasi bilan ittifoqda.")
t.B("Silla qirolligining oltin davri qachon boshlangan?", "VIII asr o‘rtalarida", "668-yilda", "X asrda", "IV asrda", "VIII asr o‘rtalarida.")
t.B("Koryo qirolligiga kim asos solgan?", "lashkarboshi Van Gon", "Jumong", "Tangun", "Van In", "Lashkarboshi Van Gon.")
t.B("Koryo sulolasi qaysi yillarda hukmronlik qilgan?", "918–1392-yillarda", "668–918-yillarda", "1231–1392-yillarda", "618–907-yillarda", "918–1392-yillar.")
t.B("Koryo qirolligining poytaxti qaysi shahar bo‘lgan?", "Sonak (hozirgi Keson)", "Pxenyan", "Kunneson", "Seul", "Sonak (hozirgi Keson).")
t.NAT("Koguryoda zodagonlar mavqei yuqori bo‘ldi.", "qirollar nufuzi past bo‘lib, mustaqillikka intilgan hukmdorni almashtirish oson bo‘ldi", "qirollar mutlaq hokimiyatga ega bo‘ldi", "zodagonlar yo‘q qilindi", "Koguryo Silla bilan birlashdi", "Qirollik besh-oltita nufuzli oila ishi bo‘lgan.")
t.NAT("Silla mamlakatni birlashtirdi, o‘zaro urushlarga chek qo‘yildi.", "yer egaligi munosabatlari uzil-kesil shakllanib, ishlab chiqarish rivojlandi", "Koreya Xitoyga qo‘shildi", "Koreya mo‘g‘ullarga bo‘ysundi", "Silla zaiflashdi", "Ishlab chiqarish rivojiga yo‘l ochildi.")
t.NAT("XIII asr boshlarida Koryo o‘zaro kurashlardan zaiflashdi.", "mo‘g‘ullar 1231-yilda Koryo qirolligini bosib oldi", "Koryo Xitoyni bosib oldi", "Silla qayta tiklandi", "Koryo Yaponiya bilan birlashdi", "1231-yilda mo‘g‘ullar bosib oldi.")
t.NAT("Pekchelik tabib, hunarmand va olimlar Yaponiyaga bordi.", "Yaponiyaning ijtimoiy va madaniy hayoti asoslari shakllanishiga katta ta’sir ko‘rsatildi", "Yaponiya Koreyani bosib oldi", "Pekche yo‘q bo‘lib ketdi", "Yaponiya buddizmni taqiqladi", "Ilk budda tasvirlari Yaponiyaga Pekche orqali yetdi.")
t.TF("IV asr boshlarida Koguryo xitoyliklarni o‘z hududidan batamom surib chiqargan.", True, "To‘g‘ri.")
t.TF("Dastlab Uch qirollik ichida Silla eng kuchli va rivojlangani bo‘lgan.", False, "Noto‘g‘ri: dastlab Silla eng zaif va kam taraqqiy etgani edi.")
t.TF4([("Uch qirollik davrida aholi erkinlar va qullarga bo‘lingan.", True), ("Qullar odatda sochlari kalta qilib olingan.", True),
       ("Silla birlashuvdan so‘ng Xitoyga boj-yasoq to‘lamagan.", False), ("Van Gon Koguryoning yo‘qotilgan hududlarini qaytarib ololmagan.", True)],
      "3-noto‘g‘ri: Koreya Xitoyga boj-yasoq to‘lab turgan.")
t.MUL([("Koguryo Xitoydagi Xan, Suy va Tan sulolalariga qarshi kurashgan.", True),
       ("Pekche IV asrda markazlashgan davlatga aylangan.", True),
       ("Koryo qirolligi 1392-yilda mo‘g‘ullar tomonidan tashkil etilgan.", False)],
      "III noto‘g‘ri: Koryoga 918-yilda Van Gon asos solgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Choson uch qirollikka bo‘lindi", "Koguryo poytaxti Pxenyanga ko‘chirildi", "Silla yarimorolni birlashtirdi", "Koryo qirolligi tuzildi", "Mo‘g‘ullar Koryoni bosib oldi"],
      "mil. avv. I asr → V asr → 668 → 918 → 1231.")
t.MATCH("Qirolliklarni ularga oid ma’lumot bilan moslashtiring.", ["Koguryo", "Pekche", "Silla", "Koryo"],
        ["asoschisi Jumong", "iyeroglif va buddizm orqali kirib kelgan qirollik", "668-yilda yarimorolni birlashtirgan", "Van Gon asos solgan, poytaxti Sonak", "asoschisi Tangun"], 'abcd',
        "Koguryo – Jumong; Pekche – buddizm; Silla – 668; Koryo – Van Gon.")
t.VENN("Koguryo", "Silla",
       [("asoschisi Jumong", 1), ("668-yilda Tan sulolasi bosib olgan", 1),
        ("yarimorolning janubi-sharqida joylashgan", 2), ("Tan bilan ittifoqda mamlakatni birlashtirgan", 2),
        ("Uch qirollikdan biri", 3)],
       "Koguryo – Jumong, Tan bosib olgan; Silla – janubi-sharq, birlashtirgan; ikkalasi Uch qirollikdan.")
t.MAPMATCH('korea', ['Pxenyan', 'Sonak (Keson)', 'Kyondju'],
           ["Choson va V asrdan Koguryo poytaxti", "918–1392-yillardagi Koryo poytaxti", "yarimorolning janubi-sharqidagi Silla qirolligi markazi"],
           "1 – Pxenyan; 2 – Sonak; 3 – Kyondju.")

# 15 Yaponiya
t = Topic('y7j15', 7015); TOPICS['y7j15'] = t
t.B("Yaponiya nechta yirik oroldan iborat?", "to‘rtta", "ikkita", "oltita", "o‘nta", "Minglab orollardan to‘rttasi yirik.")
t.B("Gullardan guldastalar tayyorlash san’ati qanday ataladi?", "ikebana", "busido", "kipu", "mikado", "Ikebana.")
t.B("Shimoldagi Xokkaydo orolida yashagan mahalliy qabilalar kimlar?", "aynlar", "samuraylar", "mayyalar", "koryoliklar", "Aynlar.")
t.B("Yaponlar xitoyliklardan nimani o‘zlashtirgan?", "choy, sholi, iyerogliflar", "makkajo‘xori va kartoshka", "kirill yozuvi", "temir plug", "Choy, sholi, tibbiyot, harbiy ishlar, iyerogliflar.")
t.B("Mamlakat VII asrdan qanday atala boshlagan?", "Nippon", "Choson", "Koryo", "Mikado", "Nippon (yapon tilida «kunchiqar mamlakat»).")
t.B("«Nippon» so‘zi qanday ma’noni anglatadi?", "«kunchiqar mamlakat»", "«tonggi tarovat»", "«Osmonosti»", "«orollar yurti»", "«Kunchiqar mamlakat».")
t.B("Yaponiyada qabilalar ittifoqi qachon shakllangan?", "IV asrda", "VII asrda", "XII asrda", "I asrda", "IV asrda.")
t.B("Yaponiya imperatori qanday unvonga ega bo‘lgan?", "mikado", "syogun", "vasilevs", "raja", "Mikado.")
t.B("XII asrdan oliy harbiy hukmdorlar qanday unvonga ega bo‘lgan?", "syogun", "mikado", "samuray", "daymyo", "Syogun.")
t.B("Knyazlar xizmatidagi jangchilar qanday atalgan?", "samuraylar", "rajputlar", "ritsarlar", "keshiklar", "Samuraylar.")
t.B("Samuraylar hayotini belgilagan yozilmagan qonun qanday atalgan?", "busido", "ikebana", "sinto", "kipu", "Busido.")
t.B("Mo‘g‘ullar Yaponiyani qachon bosib olishga urinishgan?", "XIII asr oxirida", "XII asrda", "VII asrda", "IV asrda", "XIII asr oxirida.")
t.B("Tomi yupqa oltin plastinalar bilan yopilgan mashhur pavilion qanday atalgan?", "«Oltin pavilion»", "«Kumush pavilion»", "«Quyosh saroyi»", "«Osmon ibodatxonasi»", "«Oltin pavilion».")
t.B("Yaponiyada ko‘pchilik bog‘bonlar kimlar bo‘lgan?", "buddaviylik rohiblari", "samuraylar", "imperatorlar", "aynlar", "Buddaviylik rohiblari.")
t.NAT("Yaponiya orollarda joylashgan.", "ko‘chmanchilar bosqinlaridan ishonchli himoyalangan", "ko‘chmanchilar uni tez-tez bosib olgan", "Xitoy ta’siridan butunlay chetda qolgan", "dehqonchilik umuman bo‘lmagan", "Orollar ko‘chmanchilardan himoya vositasi bo‘lgan.")
t.NAT("Yaponlar asrlar davomida sunami, zilzila va vulqonlarga qarshi kurashdi.", "ularda mehnatsevarlik va intizomlilik ko‘nikmalari shakllandi", "aholi orollarni tashlab ketdi", "dehqonchilik to‘xtadi", "imperator hokimiyati kuchaydi", "Mehnatsevarlik va intizom shakllandi.")
t.NAT("Mo‘g‘ullar Xitoy floti ko‘magida Yaponiyaga hujum qildi.", "to‘fon va samuraylarning qat’iyati tufayli bosib olish rejasi amalga oshmadi", "Yaponiya mo‘g‘ullarga bo‘ysundi", "syogunlik tugatildi", "Yaponiya Xitoyga qo‘shildi", "Reja amalga oshmadi.")
t.NAT("Markaziy hokimiyat vaqti-vaqti bilan zaiflashdi.", "mamlakatda Yevropanikiga o‘xshash siyosiy tarqoqlik hukm surdi", "imperator mutlaq hukmdorga aylandi", "samuraylar yo‘q qilindi", "Yaponiya Koreyaga qo‘shildi", "Siyosiy tarqoqlik hukm surgan.")
t.TF("Yapon imperatorlari iloh hisoblangan, ammo real hokimiyatga ega bo‘lmagan.", True, "To‘g‘ri.")
t.TF("Yaponiyadagi boshqaruv tizimi Xitoynikidan deyarli farq qilmagan.", False, "Noto‘g‘ri: keskin farq qilgan – imperator zaif, zodagonlar kuchli edi.")
t.TF4([("Samuraylar dastlab xizmatlari uchun yer-mulk olgan.", True), ("Samuraylar o‘z burchlarini hayotlaridan yuqori hisoblagan.", True),
       ("Xitoydan o‘tgan buddaviylik yaponlarning an’anaviy dinlarini butunlay siqib chiqargan.", False), ("Orollarning aksariyati tog‘lardan iborat bo‘lgan.", True)],
      "3-noto‘g‘ri: buddaviylik an’anaviy dinlar bilan aralashib ketgan.")
t.MUL([("Yaponiya Xitoy va Koreyadan sharqda joylashgan.", True),
       ("Yaponiyada ishlov beradigan yer maydonlari ko‘p bo‘lgan.", False),
       ("Harbiy ish samuraylar uchun merosiy mashg‘ulotga aylangan.", True)],
      "II noto‘g‘ri: orollar tog‘li bo‘lgani uchun ishlov beradigan yer kam edi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Qabilalar ittifoqi shakllandi", "Mamlakat Nippon deb atala boshladi", "Oliy harbiy hukmdorlar syogun unvonini oldi", "Mo‘g‘ullar Yaponiyaga hujum qildi"],
      "IV asr → VII asr → XII asr → XIII asr oxiri.")
t.VENN("Samuraylar", "Yevropa ritsarlari",
       [("busido qoidalariga amal qilgan", 1), ("Yaponiya knyazlari xizmatida", 1),
        ("G‘arbiy Yevropa feodallari", 2), ("og‘ir zirhlarda jang qilgan", 2),
        ("harbiy ishni merosiy kasb qilgan jangchilar", 3)],
       "Samuraylar – busido, Yaponiya; ritsarlar – Yevropa; ikkalasi merosiy jangchilar.")
t.MAPN('eastasia', ['Xokkaydo', 'Kioto', 'Koreya', 'Xitoy'], "Qaysi raqam bilan aynlar yashagan shimoliy orol belgilangan?",
       "1 – Xokkaydo (aynlar); 2 – Kioto (Yaponiya); 3 – Koreya; 4 – Xitoy.")

# 16 Amerika
t = Topic('y7j16', 7016); TOPICS['y7j16'] = t
t.B("Amerikaga dastlabki odamlar qayerdan o‘tgan?", "Shimoliy Osiyodan Bering bo‘g‘ozi orqali", "Afrikadan Atlantika orqali", "Yevropadan Grenlandiya orqali", "Avstraliyadan", "Shimoliy Osiyodan hozirgi Bering bo‘g‘ozi orqali.")
t.B("Odamlar Amerikaga taxminan qachon o‘ta boshlagan?", "40 ming yil avval", "4 ming yil avval", "400 ming yil avval", "milodiy I asrda", "Buyuk muzlik davrida, 40 ming yil avval.")
t.B("Qaysi ekin yevropaliklarga ma’lum bo‘lmagan, Amerikada yetishtirilgan?", "makkajo‘xori", "bug‘doy", "sholi", "arpa", "Makkajo‘xori, kartoshka, kungaboqar, pomidor, kakao, tamaki.")
t.B("Janubiy Amerikada qaysi uy hayvoni boqilgan?", "lama", "ot", "sigir", "qo‘y", "Tuyasimonlar oilasiga mansub lama.")
t.B("Mayya xalqlari qayerda yashagan?", "Yukatan yarimorolida", "And tog‘larida", "Bering bo‘g‘ozida", "Urubamba vodiysida", "Yukatan yarimorolida (hozirgi Meksika).")
t.B("Mayyalar poytaxti qaysi shahar bo‘lgan?", "Chichen-Itsa", "Tenochtitlan", "Kusko", "Machu-Pikchu", "Chichen-Itsa; u yerda rasadxona qurilgan.")
t.B("Matematikaga «nol» belgisini hindlardan avval kim kiritgan?", "mayyalar", "asteklar", "inklar", "olmeklar", "Mayyalar.")
t.B("Asteklar Tenochtitlan shahriga qachon asos solgan?", "XII asrda", "milodiy I asrda", "XV asrda", "VII asrda", "XII asrda.")
t.B("Asteklar ko‘l tagidan loy ko‘tarib, sollarda nima yaratgan?", "«suzuvchi dalalar»", "terrasalar", "to‘g‘onlar", "kanallar", "«Suzuvchi dalalar».")
t.B("Asteklarda oliy hukmdor va bosh kohin vazifasini bajargan lashkarboshi qanday atalgan?", "tlatoani", "Oliy Inka", "kipu", "mikado", "Tlatoani.")
t.B("Asteklar xo‘jaligining asosi nima bo‘lgan?", "sug‘orma dehqonchilik", "chorvachilik", "ovchilik", "baliqchilik", "Sug‘orma dehqonchilik.")
t.B("Asteklarda qanday yozuv shakllangan?", "piktografik", "kirill", "lotin", "tugunli", "Piktografik yozuv.")
t.B("Inklar Kusko shahriga qaysi daryo havzasida asos solgan?", "Urubamba", "Amazonka", "Missisipi", "Parana", "XII–XIII asrlarda Urubamba daryosi havzasida.")
t.B("Inklar davlatini kim boshqargan?", "Oliy Inka – «Quyoshning o‘g‘li»", "tlatoani", "«buyuk kishi»", "Osmon o‘g‘li", "Oliy Inka.")
t.B("Inklarda jamoalar hosilning qancha qismini davlat va ibodatxonalarga topshirgan?", "2/3 qismini", "1/3 qismini", "yarmini", "1/10 qismini", "2/3 qismini.")
t.B("Inklarning «tugunli xati» qanday atalgan?", "kipu", "busido", "tlatoani", "ikebana", "Kipu.")
t.B("Inklar taqvimi necha oyga bo‘lingan?", "12 oyga", "10 oyga", "13 oyga", "18 oyga", "12 oyga.")
t.NAT("Mayyalarda iqtisodiy-madaniy taraqqiyot yuksaldi.", "yozuv yaratilib, kohinlar iyerogliflar bitdi", "mayyalar temirni kashf qildi", "mayyalar Yevropaga ko‘chdi", "mayyalarda g‘ildirak paydo bo‘ldi", "Yozuv yaratish imkoni tug‘ildi.")
t.NAT("Asteklarda yer taqchil bo‘ldi.", "ko‘l ustida «suzuvchi dalalar» yaratilib, yiliga bir necha marta hosil olindi", "asteklar ko‘chmanchilikka o‘tdi", "asteklar dehqonchilikdan voz kechdi", "asteklar mayyalarni bosib oldi", "Suzuvchi dalalar yaratildi.")
t.NAT("Inklar tog‘li hududda tik qoyalar yonbag‘rini o‘yib, tosh devorli ekinzorlar qildi.", "ekinzor tuprog‘ini yomg‘ir yuvib ketmadi, kartoshka va makkajo‘xori yetishtirildi", "tog‘larda dehqonchilik to‘xtadi", "inklar ovchilikka o‘tdi", "yerlar sho‘rlandi", "Terrasali ekinzorlar yaratildi.")
t.NAT("Inklar boshqa qabilalar yerlarini bosib olib, o‘z tartib va madaniyatini o‘tkazdi.", "«ink» atamasi hukmron toifa – zodagonlarning umumiy nomiga aylandi", "inklar boshqa qabilalarga qo‘shilib yo‘qoldi", "qulchilik rasman joriy etildi", "inklar yozuv yaratdi", "Qabila nomi zodagonlar nomiga aylandi.")
t.TF("Amerikalik hindular temir, omoch, g‘ildirak va o‘tochar qurollarni bilmagan.", True, "To‘g‘ri.")
t.TF("Inklar ko‘plab kitoblar yozib qoldirgan.", False, "Noto‘g‘ri: inklarda yozuv bo‘lmagan, bolalar ma’lumotlarni yodlagan.")
t.TF4([("Mayyalar saroy va ibodatxonalarida derazalar bo‘lmagan.", True), ("Asteklar temir ma’danini bilmagan, bolta va pichoqni toshdan yasagan.", True),
       ("Inklar tabiblari bosh suyagida jarrohlik muolajalarini bilgan.", True), ("Tenochtitlanda zodagon va oddiy xalq bolalari bir maktabda o‘qigan.", False)],
      "4-noto‘g‘ri: ular uchun alohida-alohida maktablar bo‘lgan.")
t.MUL([("Inklar Kuskoni viloyatlar bilan bog‘lovchi 15 ming km tosh yo‘llar qurgan.", True),
       ("Asteklar quyosh taqvimini mayyalar ixtirosi asosida yaratgan.", True),
       ("Ot, sigir va qo‘ylar Amerikada qadimdan xonakilashtirilgan.", False)],
      "III noto‘g‘ri: ular keyinchalik Yevropadan olib kelingan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Odamlar Bering bo‘g‘ozi orqali o‘ta boshladi", "Mayyalarda shahar-davlatlar vujudga keldi", "Asteklar Tenochtitlanga asos soldi"],
      "40 ming yil avval → milodiy I ming yillik → XII asr.")
t.MATCH("Xalqlarni ularga oid ma’lumot bilan moslashtiring.", ["mayyalar", "asteklar", "inklar"],
        ["poytaxti Chichen-Itsa, «nol» belgisi", "Tenochtitlan, «suzuvchi dalalar»", "Kusko, kipu", "Bering bo‘g‘ozi orqali Osiyoga qaytgan"], 'abc',
        "Mayyalar – Chichen-Itsa; asteklar – Tenochtitlan; inklar – Kusko.")
t.VENN("Asteklar", "Inklar",
       [("poytaxti Tenochtitlan", 1), ("piktografik yozuv", 1),
        ("poytaxti Kusko", 2), ("yozuv o‘rniga kipu – tugunli xat", 2),
        ("makkajo‘xori asosiy ekin bo‘lgan", 3)],
       "Asteklar – Tenochtitlan, piktografiya; inklar – Kusko, kipu; ikkalasida makkajo‘xori asosiy ekin.")
t.MAPMATCH('latam', ['Yukatan yarimoroli', 'Tenochtitlan', 'Kusko'],
           ["mayyalar yashagan yarimorol", "XII asrda asteklar ko‘l ichida barpo etgan shahar", "inklar Urubamba havzasida asos solgan poytaxt"],
           "1 – Yukatan; 2 – Tenochtitlan; 3 – Kusko.")
