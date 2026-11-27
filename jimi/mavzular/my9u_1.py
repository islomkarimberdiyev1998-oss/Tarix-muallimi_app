from qlib import Topic, PLACES, REG
TOPICS = {}

# 1–2-§ Qipchoq dashti va Movarounnahrdagi siyosiy vaziyat
t = Topic('y9u1-2', 9001); TOPICS['y9u1-2'] = t
t.B("Abulxayrxon Sharqiy Qipchoq dashtini kimlarning qo‘llab-quvvatlashi natijasida birlashtirgan?", "200 dan ortiq sarkardalarning", "temuriylarning", "safaviylarning", "Mo‘g‘uliston xonining", "Turk-mo‘g‘ul qabilalarining 200 dan ortiq sarkardasi.")
t.B("Shayboniylar sulolasining nomi kimning ismi bilan bog‘liq?", "Jo‘jixonning beshinchi o‘g‘li Shayban", "Muhammad Shayboniy", "Po‘lat Sulton", "Shohbudog‘ Sulton", "Jo‘jixonning beshinchi o‘g‘li Shaybon.")
t.B("Abulxayrxon 1428-yilda qaysi shaharni bosib olib, poytaxtga aylantirgan?", "Tura", "Sig‘noq", "Saroy", "Urganch", "Sibir g‘arbidagi Tura shahri.")
t.B("Abulxayrxon «Ulug‘ xon» unvonini qachon qabul qilgan?", "1430-yilda Xorazmni ishg‘ol qilgach", "1428-yilda", "1446-yilda", "1465-yilda", "1430-yilda.")
t.B("1446-yilda Abulxayrxon poytaxtini qayerga ko‘chirgan?", "Sig‘noqqa", "Turaga", "Samarqandga", "Buxoroga", "Turadan Sig‘noqqa.")
t.B("Abulxayrxondan qochgan Girayxon va Jonibekxon kimning huzuriga borgan?", "Mo‘g‘uliston xoni Isobug‘axon", "Abu Said", "Ulug‘bek", "Husayn Boyqaro", "Isobug‘axon (Eson Buqo).")
t.B("Qozoq xonligiga qachon asos solingan?", "1465–1466-yillarda", "1428-yilda", "1500-yilda", "1446-yilda", "1465–1466-yillarda.")
t.B("Abulxayrxon kimning qiziga uylangan?", "Ulug‘bekning", "Abu Saidning", "Husayn Boyqaroning", "Umarshayx Mirzoning", "Ulug‘bekning qizi Robiya Sulton begimga.")
t.B("Abulxayrxon va Robiya Sulton begimning farzandi kim?", "Ko‘chkunchixo‘ja", "Muhammad Shayboniy", "Shohbudog‘", "Ubaydulla", "Ko‘chkunchixo‘ja – Buxoro xonligini 20 yil boshqargan.")
t.B("Abu Said kimning yordamida Samarqand taxtini egallagan?", "Abulxayrxonning", "Boburning", "Isobug‘axonning", "Husayn Boyqaroning", "Abulxayrxon yordamida.")
t.B("1469-yilda Hirot taxtini kim egallagan?", "Husayn Boyqaro", "Abu Said", "Abulqosim Bobur", "Sulton Ahmad Mirzo", "Husayn Boyqaro.")
t.B("Bobur qachon va qayerda tug‘ilgan?", "1483-yil 14-fevral, Andijon", "1494-yil, Samarqand", "1483-yil, Hirot", "1501-yil, Kobul", "1483-yil 14-fevralda Andijonda.")
t.B("Boburning onasi Qutlug‘ Nigorxonim kimning qizi edi?", "Toshkent hokimi Yunusxonning", "Abulxayrxonning", "Ulug‘bekning", "Sulton Ahmad Mirzoning", "Yunusxonning.")
t.B("Bobur necha yoshida taxtga o‘tqazilgan?", "12 yoshida", "16 yoshida", "20 yoshida", "39 yoshida", "1494-yilda 12 yoshida.")
t.B("Bobur Samarqandni 1497-yilda necha oylik qamaldan keyin egallagan?", "7 oylik", "4 oylik", "2 oylik", "12 oylik", "7 oylik qamaldan so‘ng.")
t.B("Bobur Samarqand uchun kurashayotganda Andijonni kim egallab olgan?", "Ahmad Tanbal", "Shayboniyxon", "Sulton Mahmudxon", "Sulton Ali Mirzo", "Ahmad Tanbal.")
t.B("Bobur Panipatda kimning qo‘shinini tor-mor qilgan?", "Dehli sultoni Ibrohim Lo‘diy", "Ismoil Safaviy", "Shayboniyxon", "Sulton Ahmad Mirzo", "Ibrohim Lo‘diy.")
t.B("Bobur valiahdlariga dasturulamal sifatida qaysi asarni yaratgan?", "«Mubayyin»", "«Boburnoma»", "«Abdullanoma»", "«Haft iqlim»", "1521-yilda «Mubayyin».")
t.B("Ham gorizontal, ham vertikal o‘qiladigan she’r janri qanday ataladi?", "masnu’", "tuyuq", "fard", "ruboiy", "Masnu’.")
t.NAT("Abulxayrxon 1446-yilda Sig‘noq, Oqqo‘rg‘on, Arquq, O‘zgan shaharlarini bosib oldi.", "u Temuriylar davlatining qo‘shnisiga aylanib, uning siyosiy hayotiga aralasha boshladi", "Temuriylar Qipchoq dashtini egalladi", "Abulxayrxon taxtdan voz kechdi", "Qozoq xonligi tugatildi", "Temuriylar qo‘shnisiga aylandi.")
t.NAT("1469-yilda Husayn Boyqaro Hirot taxtini egalladi.", "Temuriylar davlati ikki mustaqil qismga bo‘linib ketdi", "Temuriylar davlati birlashdi", "Shayboniylar Hirotni oldi", "Abu Said Movarounnahrni yo‘qotdi", "Davlat ikkiga bo‘lindi.")
t.NAT("Temuriylarning to‘xtovsiz janglari va og‘ir soliqlaridan xalq toliqdi.", "xalq Boburni qo‘llamay, u 1504-yilda Movarounnahrni tark etdi", "Bobur Farg‘onani qaytarib oldi", "Shayboniyxon yengildi", "Bobur Samarqandda qoldi", "Bobur Afg‘onistonga ketdi.")
t.NAT("1526-yil aprelda Panipat jangida Bobur g‘alaba qozondi.", "Dehlini egallab, Hindistonda boburiylar sulolasiga asos soldi", "Bobur Kobulni yo‘qotdi", "Ibrohim Lo‘diy Kobulni egalladi", "Bobur Movarounnahrga qaytdi", "Dehli egallandi.")
t.TF("Panipat jangida Boburning 12 ming kishilik qo‘shini 100 ming kishilik qo‘shinni tor-mor etgan.", True, "To‘g‘ri.")
t.TF("Bobur «Boburnoma»ni 1526-yilda Dehlini egallagach yoza boshlagan.", False, "Noto‘g‘ri: 1518–1519-yillarda yoza boshlagan.")
t.TF4([("Abulxayrxon Jaloliddin Rumiy asarlarini tarjima qilishni buyurgan.", True), ("Abulxayrxon 1412-yilda tug‘ilgan.", True),
       ("1501-yil aprelda Saripul jangida Bobur g‘alaba qozongan.", False), ("Bobur 200–300 navkari bilan Hisor tog‘lari orqali Afg‘onistonga o‘tgan.", True)],
      "3-noto‘g‘ri: Saripulda Bobur Shayboniyxondan yengilgan.")
t.MUL([("Abulxayrxon o‘z davlatini Oltin O‘rdadan mustaqil deb e’lon qilgan.", True),
       ("Bobur Afg‘onistonda G‘azna va Kobulni egallagan.", True),
       ("Boburning siyosiy maqsadi Oltin O‘rdani tiklash edi.", False)],
      "III noto‘g‘ri: maqsadi Amir Temur saltanatini qayta tiklash edi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Abulxayrxon Turani egalladi", "Poytaxt Sig‘noqqa ko‘chirildi", "Husayn Boyqaro Hirot taxtini egalladi", "Bobur taxtga o‘tirdi", "Saripul jangi", "Panipat jangi"],
      "1428 → 1446 → 1469 → 1494 → 1501 → 1526.")
t.MATCH("Shaxslarni ular haqidagi ma’lumot bilan moslashtiring.", ["Abulxayrxon", "Husayn Boyqaro", "Ahmad Tanbal", "Ibrohim Lo‘diy"],
        ["1446-yilda poytaxtni Sig‘noqqa ko‘chirgan", "1469-yilda Hirot taxtini egallagan", "Bobur yo‘qligida Andijonni egallagan", "Panipatda yengilgan Dehli sultoni", "Qozoq xonligiga asos solgan"], 'abcd',
        "Abulxayrxon – Sig‘noq; Husayn Boyqaro – Hirot; Ahmad Tanbal – Andijon; Ibrohim Lo‘diy – Panipat.")
t.VENN("Abulxayrxon", "Bobur",
       [("poytaxti Tura, so‘ng Sig‘noq", 1), ("Rumiy asarlarini tarjima qildirgan", 1),
        ("«Boburnoma» muallifi", 2), ("Panipatda g‘alaba qozongan", 2),
        ("Movarounnahr siyosiy hayotiga ta’sir ko‘rsatgan hukmdor", 3)],
       "Abulxayrxon – Tura, Sig‘noq; Bobur – «Boburnoma», Panipat; ikkalasi Movarounnahr siyosatiga ta’sir etgan.")
t.MAPMATCH('tsent', ['Tura', 'Sig‘noq', 'Andijon', 'Panipat'],
           ["1428-yilda Abulxayrxon poytaxtga aylantirgan shahar", "1446-yildan Abulxayrxon poytaxti", "Bobur tug‘ilgan shahar", "1526-yilda Bobur Ibrohim Lo‘diyni yenggan joy"],
           "1 – Tura; 2 – Sig‘noq; 3 – Andijon; 4 – Panipat.")

# 3-§ Movarounnahrda Shayboniy hukmronligining o‘rnatilishi
t = Topic('y9u3', 9003); TOPICS['y9u3'] = t
t.B("Muhammad Shayboniyning otasi kim edi?", "Shohbudog‘ Sulton", "Abulxayrxon", "Boyshayx", "Ko‘chkunchixon", "Shohbudog‘ Sulton.")
t.B("Muhammad Shayboniyning taxallusi qanday bo‘lgan?", "Shohbaxt", "Xon", "Bobur", "Nisoriy", "«Shohbaxt».")
t.B("Abulxayrxon tuzgan O‘zbek ulusi davlati qachon qulagan?", "1468-yilda", "1480-yilda", "1500-yilda", "1446-yilda", "1468-yilda.")
t.B("Shayboniyxon bobosining davlatini qachon qayta tiklagan?", "1480-yilda", "1468-yilda", "1499-yilda", "1510-yilda", "1480-yilda.")
t.B("1500-yilda Samarqandni Shayboniyxonga jangsiz kim topshirgan?", "Sulton Ali Mirzo", "Bobur", "Abdulloh Mirzo", "Sulton Mahmud Mirzo", "Sulton Ali Mirzo.")
t.B("1503-yilda Shayboniyxon qayerda Mahmudxon, Bobur va qalmoqlarning birlashgan qo‘shinini yengdi?", "Sirdaryo bo‘yida", "Marv yaqinida", "G‘ijduvonda", "Saripulda", "Sirdaryo bo‘yida.")
t.B("Shayboniyxon 1510-yilda kimdan yengilib halok bo‘lgan?", "Ismoil Safaviy", "Bobur", "Husayn Boyqaro", "Najmi Soniy", "Marv yaqinida Ismoil Safaviydan.")
t.B("1511-yilda Bobur kim bilan harbiy-siyosiy ittifoq tuzgan?", "shoh Ismoil", "Ubaydulla Sulton", "Mahmudxon", "Ibrohim Lo‘diy", "Shoh Ismoil Safaviy bilan.")
t.B("1512-yil 28-aprelda Bobur qaysi jangda yengildi?", "Ko‘li Malik", "G‘ijduvon", "Saripul", "Panipat", "Ko‘li Malik jangida.")
t.B("Bobur Movarounnahrni egallash umidini qaysi jangdan so‘ng butunlay uzdi?", "G‘ijduvon jangi", "Ko‘li Malik jangi", "Saripul jangi", "Marv jangi", "1512-yil noyabrdagi G‘ijduvon jangi.")
t.B("Shoh Ismoil Boburga yuborgan lashkarboshining laqabi nima?", "Najmi Soniy", "Ahmad Tanbal", "Mahdiy Xoja", "Shohbaxt", "Najmi Soniy.")
t.B("Ubaydullaxon poytaxtni qachon Buxoroga ko‘chirgan?", "1533-yilda", "1512-yilda", "1557-yilda", "1598-yilda", "1533-yilda.")
t.B("Poytaxt Buxoroga ko‘chirilgach, shayboniylar davlati qanday atalgan?", "Buxoro xonligi", "O‘zbek ulusi", "Movarounnahr davlati", "Turon", "Buxoro xonligi.")
t.B("Abdullaxon II siyosiy yuksalishini qaysi voqeadan boshlagan?", "1557-yilda Buxoroni qo‘lga kiritishdan", "1533-yilda", "1510-yilda", "1598-yilda", "1557-yilda Buxoroni egallashdan.")
t.B("Abdullaxon II qachon vafot etgan?", "1598-yilda", "1557-yilda", "1533-yilda", "1601-yilda", "1598-yilda.")
t.B("Shayboniylar sulolasining so‘nggi vakili kim?", "Pir Muhammadxon II", "Abdulmo‘minxon", "Abdullaxon II", "Abdulazizxon", "Pir Muhammadxon II.")
t.B("Abdullaxon II qanday taxallus bilan she’rlar yozgan?", "Xon", "Shohbaxt", "Nisoriy", "Mutribiy", "«Xon».")
t.B("Hofiz Tanish Buxoriyning asari qaysi?", "«Abdullanoma»", "«Haft iqlim»", "«Tazkirati shuaro»", "«Muzakkiri ahbob»", "«Abdullanoma» («Sharafnomayi shohiy»).")
t.B("Dunyo xaritasi ilova qilingan «Tazkirati shuaro» muallifi kim?", "Mutribiy", "Amin Ahmad Roziy", "Hasanxo‘ja Nisoriy", "Hofiz Tanish", "Mutribiy.")
t.NAT("Shayboniyxon 1505–1509-yillarda Urganch, Balx, Hirot va Xuroson hududlarini egalladi.", "Sirdaryodan Qandahorgacha bo‘lgan hududlar yagona davlatga birlashdi", "Temuriylar davlati tiklandi", "Shayboniyxon Eronga bo‘ysundi", "Bobur Samarqandni oldi", "Yagona davlat tuzildi.")
t.NAT("Bobur shia mazhabidagi eroniylar bilan ish tutdi.", "mahalliy aholida norozilik uyg‘ondi", "aholi uni qo‘llab-quvvatladi", "shayboniylar unga bo‘ysundi", "Eron uni tark etdi", "Norozilik kuchaydi.")
t.NAT("Ubaydullaxonning o‘limidan so‘ng siyosiy parokandalik boshlandi.", "qo‘shhokimiyatchilik vujudga keldi", "markaziy hokimiyat kuchaydi", "Abdullaxon II taxtga chiqdi", "Bobur qaytib keldi", "Buxoro va Samarqandda alohida hukmdorlar.")
t.NAT("Abdullaxon II Balx, Samarqand, Toshkent, Farg‘ona, Xorazm ustidan hukmronlik o‘rnatdi.", "mamlakat birlashib, markazlashgan boshqaruv tiklandi", "davlat parchalandi", "qo‘shhokimiyatchilik kuchaydi", "Eron Buxoroni egalladi", "Markazlashgan davlat tiklandi.")
t.TF("Shayboniyxon 1499-yilda Jizzax va Samarqand orqali Qarshi va Shahrisabzgacha bosib borgan.", True, "To‘g‘ri.")
t.TF("Abdulmo‘minxon taxtda 20 yil hukmronlik qilgan.", False, "Noto‘g‘ri: olti oy hukmronlik qilgan.")
t.TF4([("Muhammad Shayboniy ukasi bilan Boyshayx otalig‘ida voyaga yetgan.", True), ("1500-yilda Buxoro ham Shayboniyxon tomonidan zabt etilgan.", True),
       ("Ubaydullaxon Hirotni eronliklardan ikki marta tortib olgan.", True), ("«Haft iqlim» asarini Hofiz Tanish yozgan.", False)],
      "4-noto‘g‘ri: «Haft iqlim» – Amin Ahmad Roziy asari.")
t.MUL([("Bobur 1512-yil kuzida Huzar (G‘uzor) qal’asini egallagan.", True),
       ("«Muzakkiri ahbob» asari Abdullaxon II ga bag‘ishlangan.", True),
       ("Muhammad Shayboniyxon Marv jangida Ismoil Safaviyni yenggan.", False)],
      "III noto‘g‘ri: Marv yaqinida Shayboniyxon yengilib, halok bo‘lgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["O‘zbek ulusi davlati quladi", "Shayboniyxon davlatni qayta tikladi", "Samarqand jangsiz topshirildi", "Marv jangi", "G‘ijduvon jangi", "Poytaxt Buxoroga ko‘chirildi"],
      "1468 → 1480 → 1500 → 1510 → 1512 → 1533.")
t.MATCH("Asarlarni mualliflari bilan moslashtiring.", ["«Abdullanoma»", "«Haft iqlim»", "«Tazkirati shuaro»", "«Muzakkiri ahbob»"],
        ["Hofiz Tanish Buxoriy", "Amin Ahmad Roziy", "Mutribiy", "Hasanxo‘ja Nisoriy", "Zahiriddin Bobur"], 'abcd',
        "Abdullanoma – Hofiz Tanish; Haft iqlim – Roziy; Tazkirati shuaro – Mutribiy; Muzakkiri ahbob – Nisoriy.")
t.VENN("Muhammad Shayboniyxon", "Abdullaxon II",
       [("1510-yilda Marv yaqinida halok bo‘lgan", 1), ("taxallusi «Shohbaxt»", 1),
        ("1557-yilda Buxoroni egallagan", 2), ("«Xon» taxallusi bilan she’r yozgan", 2),
        ("shayboniylar sulolasi vakili", 3)],
       "Shayboniyxon – Marv, «Shohbaxt»; Abdullaxon II – 1557, «Xon»; ikkalasi shayboniy.")
t.MAPMATCH('ca', ['Marv', 'G‘ijduvon', 'Hirot', 'Jizzax'],
           ["1510-yilda Shayboniyxon halok bo‘lgan jang joyi", "1512-yil noyabrida Bobur yengilgan joy", "Shayboniyxon 1505–1507-yillarda egallagan Xuroson poytaxti", "1499-yilgi yurishda Samarqanddan avval o‘tilgan shahar"],
           "1 – Marv; 2 – G‘ijduvon; 3 – Hirot; 4 – Jizzax.")
