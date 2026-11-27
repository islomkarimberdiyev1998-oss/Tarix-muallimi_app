from qlib import Topic, PLACES, REG
TOPICS = {}

# 9-§ Shayboniylarning tashqi siyosati
t = Topic('y9u9', 9009); TOPICS['y9u9'] = t
t.B("XVI asrda shayboniylar, safaviylar va boburiylar manfaatlari to‘qnashgan asosiy nuqta qaysi?", "Xuroson", "Badaxshon", "Xorazm", "Sibir", "Xuroson.")
t.B("Xuroson uchun kurashda safaviylar uchun asosiy to‘siq qaysi davlat edi?", "Usmonli saltanati", "Boburiylar davlati", "Qozoq xonligi", "Rossiya", "Usmonli saltanati.")
t.B("Shahzoda Abdulmo‘min Eronga qarshi birga kurashish taklifi bilan kimga xat yuborgan?", "usmonli sultoni Murod III", "Akbarshoh", "Ivan Grozniy", "Kuchumxon", "Murod III ga.")
t.B("Murod III safaviylarga qarshi qachon urush ochgan?", "1576-yilda", "1556-yilda", "1586-yilda", "1509-yilda", "1576-yilda.")
t.B("Abdullaxon II Hindistonga kim boshchiligida elchilar jo‘natgan?", "Mir Quraysh", "Hakim Humom", "Sadr Jahon", "Mir Arab", "Mir Quraysh.")
t.B("1586-yilda Buxoroga Hakim Humom va Sadr Jahon boshchiligidagi elchilarni kim yuborgan?", "Akbarshoh", "Murod III", "shoh Abbos", "Kuchumxon", "Akbarshoh.")
t.B("1509-yilda Shayboniyxon kimlarga qattiq zarba bergan?", "qozoq sultonlariga", "safaviylarga", "boburiylarga", "qalmoqlarga", "Jonish Sulton, Burunduqxon, Qosim Sultonga.")
t.B("1509-yilgi g‘alabadan so‘ng Shayboniyxon qaysi maqbarani ta’mirlashga buyurgan?", "Xo‘ja Ahmad Yassaviy maqbarasi", "Go‘ri Amir", "Ismoil Somoniy", "Bahouddin Naqshband", "Turkistondagi Yassaviy maqbarasi.")
t.B("Kuchumxon kimning yordamida Sibir xonligida hokimiyatga kelgan?", "Abdullaxon II", "Ivan Grozniy", "Akbarshoh", "Murod III", "1563-yilda Abdullaxon II yordamida.")
t.B("Kuchumxon 1574-yilgi xatida Abdullaxon II dan nimani so‘ragan?", "sayyid va shayxlar yuborishni", "qo‘shin yuborishni", "oltin berishni", "qizini berishni", "Sayyid-u shayxlar yuborishni.")
t.B("Ivan Grozniy Qozon xonligini qachon bosib olgan?", "1552-yilda", "1556-yilda", "1563-yilda", "1581-yilda", "1552-yilda.")
t.B("Ashtarxon xonligi qachon Rossiya tomonidan bosib olingan?", "1556-yilda", "1552-yilda", "1574-yilda", "1601-yilda", "1556-yilda.")
t.B("1581–1583-yillarda Kuchumxonga qarshi kim boshliq kazaklar kurashgan?", "Yermak", "Ivan Grozniy", "Kuchum", "Stepan Razin", "Yermak.")
t.B("Shayboniylarning asosiy raqibi qaysi davlat edi?", "safaviylar", "boburiylar", "usmonlilar", "Xitoy", "Shialik safaviylar davlati.")
t.B("Shayboniylar Xitoy bilan qanday munosabatda bo‘lgan?", "iliq munosabatlarda", "doimiy urushda", "hech aloqa bo‘lmagan", "tobe bo‘lgan", "Iliq munosabatlarda.")
t.B("Shayboniyxon dastlab nechta o‘zbek urug‘iga tayangan?", "olti", "o‘n besh", "to‘rt", "yigirma", "Olti urug‘ga, keyinchalik 15 ga.")
t.NAT("1576-yilda Murod III safaviylarga qarshi urush ochdi.", "Abdullaxon II Xurosonga kirib, Mashhad va Nishopurni egalladi", "safaviylar Buxoroni oldi", "boburiylar Xurosonni egalladi", "Abdullaxon II usmonlilarga qarshi chiqdi", "Xurosonga yurish uchun qulay vaziyat yaratildi.")
t.NAT("Qozon va Ashtarxon xonliklari Rossiya tomonidan bosib olindi.", "ruslarning sharqqa yurishi, Sibir yerlarini bosib olish boshlandi", "Rossiya Buxoroni egalladi", "Sibir xonligi kuchaydi", "Kuchumxon Moskvani oldi", "Sibirga yurish boshlandi.")
t.NAT("Sibirdagi rus fuqarolari to‘kinlik so‘rab podshoga murojaat qildi.", "rus hukumati buxorolik savdogarlardan soliq va boj olmaslikni buyurdi", "Buxoro bilan savdo taqiqlandi", "savdogarlar Sibirdan haydaldi", "Rossiya Xivaga yurish qildi", "Savdogarlarga imtiyoz berildi.")
t.NAT("Shayboniylar Sibir xonligiga sayyid va shayxlar yubordi.", "Sibir xonligining g‘arbida islom dini tarqaldi, turonliklar soni ortdi", "Sibir xonligi tugadi", "Kuchumxon nasroniylikni qabul qildi", "elchilik aloqalari uzildi", "Islom tarqaldi.")
t.TF("Usmonli sultonligi Xuroson uchun kurashda shayboniylarni qo‘llab-quvvatlagan.", True, "To‘g‘ri.")
t.TF("Boburiylar shayboniylarning safaviylarga qarshi kurashiga faol aralashgan.", False, "Noto‘g‘ri: faol aralashish yo‘lini tutmagan.")
t.TF4([("1509-yilda Shayboniyxon Sig‘noq, Yassi, Savron shaharlarini qo‘lga kiritgan.", True), ("Yermak bilan kurashda Kuchumxonning qo‘li baland kelgan.", True),
       ("Abdullaxon II Badaxshonni egallashni Makka va Madinaga yo‘l ochish bilan asoslagan.", True), ("Shayboniylar Xiva xonligi bilan doimo ittifoqda bo‘lgan.", False)],
      "4-noto‘g‘ri: Xiva bilan munosabatlar turlicha kechgan.")
t.MUL([("Navro‘z Ahmadxon usmonli sultonlari bilan yaqinlashishga harakat qilgan.", True),
       ("Akbarshoh shayboniylar bilan munosabatni keskinlashtirmaslikka qaror qilgan.", True),
       ("Kuchumxon Ivan Grozniy yordamida taxtga chiqqan.", False)],
      "III noto‘g‘ri: Abdullaxon II yordamida.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Shayboniyxon qozoq sultonlarini yengdi", "Qozon xonligi bosib olindi", "Kuchumxon hokimiyatga keldi", "Murod III safaviylarga qarshi urush ochdi", "Yermak Kuchumxonga qarshi kurash boshladi", "Akbarshoh elchilari Buxoroga keldi"],
      "1509 → 1552 → 1563 → 1576 → 1581 → 1586.")
t.MATCH("Hukmdorlarni davlati bilan moslashtiring.", ["Murod III", "Akbarshoh", "Kuchumxon", "Ivan Grozniy"],
        ["Usmonli saltanati", "Boburiylar davlati", "Sibir xonligi", "Rossiya", "Safaviylar davlati"], 'abcd',
        "Murod III – Usmonli; Akbarshoh – boburiylar; Kuchumxon – Sibir; Ivan Grozniy – Rossiya.")
t.VENN("Usmonli saltanati", "Safaviylar davlati",
       [("shayboniylarning ittifoqchisi", 1), ("1576-yilda Eronga urush ochgan", 1),
        ("shialikka e’tiqod qilgan", 2), ("shayboniylarning asosiy raqibi", 2),
        ("Xuroson masalasiga aralashgan davlat", 3)],
       "Usmonli – ittifoqchi, 1576; safaviylar – shia, raqib; ikkalasi Xuroson masalasiga aralashgan.")
t.MAPMATCH('ca', ['Mashhad', 'Badaxshon', 'Turkiston', 'Buxoro'],
           ["1576-yildan keyin Abdullaxon II egallagan Xuroson shahri", "egallanishi boburiylarga elchilar orqali izohlangan viloyat", "Yassaviy maqbarasi joylashgan shahar", "1586-yilda Akbarshoh elchilari kelgan poytaxt"],
           "1 – Mashhad; 2 – Badaxshon; 3 – Turkiston; 4 – Buxoro.")

# 10-§ Ashtarxoniylarning hukmronlik davri
t = Topic('y9u10', 9010); TOPICS['y9u10'] = t
t.B("Shayboniylarning so‘nggi hukmdori Pir Muhammadxon II qanday halok bo‘lgan?", "ashtarxoniylar bilan jangda", "safaviylar bilan jangda", "qozoqlar bilan jangda", "kasallikdan", "Ashtarxoniylar urug‘i bilan jangda.")
t.B("Hokimiyat qachon ashtarxoniylar qo‘liga o‘tgan?", "1601-yilda", "1598-yilda", "1611-yilda", "1556-yilda", "1601-yilda.")
t.B("Ashtarxon xonligi bosib olingach, Buxoroga kim kelgan?", "Yor Muhammadxon", "Boqi Muhammad", "Imomquli", "Kuchumxon", "Yor Muhammadxon.")
t.B("Iskandarxon qizi Zuhrabonuni kimga turmushga bergan?", "Joni Muhammad sultonga", "Boqi Muhammadga", "Yalangto‘shga", "Vali Muhammadga", "Joni Muhammad sultonga.")
t.B("Taxtni shayboniylardan tortib olgan ashtarxoniy kim?", "Boqi Muhammad", "Vali Muhammad", "Imomqulixon", "Joni Muhammad", "1601-yilda Boqi Muhammad.")
t.B("Vali Muhammadxon necha yil hukmronlik qilgan?", "olti yil", "o‘ttiz yil", "bir yil", "o‘n yil", "Olti yil.")
t.B("Vali Muhammadxonga «yaxshi qo‘shnichilik» taklifi bilan elchilar yuborgan safaviy shoh kim?", "shoh Abbos", "shoh Ismoil", "Nodirshoh", "shoh Tahmasp", "Shoh Abbos.")
t.B("1611-yilda zodagonlar kimni oliy taxtga o‘tqazdi?", "Samarqand hokimi Imomquli sultonni", "Nadr Muhammadni", "Yalangto‘shni", "Abdulazizni", "Imomquli sultonni.")
t.B("Imomqulixon mamlakatni qancha muddat boshqargan?", "o‘ttiz yildan ortiq", "olti yil", "uch yil", "o‘n yil", "O‘ttiz yildan ortiq.")
t.B("Yalangto‘sh Bahodir qachon va qayerda tug‘ilgan?", "1578-yilda Nurota hokimi oilasida", "1601-yilda Buxoroda", "1611-yilda Samarqandda", "1556-yilda Balxda", "1578-yilda Nurotada.")
t.B("Yalangto‘sh Samarqandni qachondan amalda mustaqil idora eta boshlagan?", "1626-yildan", "1611-yildan", "1640-yildan", "1648-yildan", "1626-yildan.")
t.B("Nadr Muhammadxon o‘zbek davlatini qaysi yillarda boshqargan?", "1642–1645-yillarda", "1611–1642-yillarda", "1645–1681-yillarda", "1601–1605-yillarda", "1642–1645-yillarda.")
t.B("1645-yilda qozoqlar qaysi shahargacha bostirib kelgan?", "Xo‘jandgacha", "Samarqandgacha", "Buxorogacha", "Toshkentgacha", "Xo‘jandgacha.")
t.B("Nadr Muhammadxon qanday vafot etgan?", "Makkaga hajga ketayotib yo‘lda", "jangda", "zindonda", "Buxoroda kasallikdan", "Haj yo‘lida.")
t.B("1648-yilda Abdulazizxon Balxni kimlardan qaytarib olgan?", "boburiylardan", "safaviylardan", "qozoqlardan", "Xivadan", "Boburiylardan.")
t.B("Abdulazizxon Balxga necha kishilik qo‘shin bilan yurish qilgan?", "200 ming", "10 ming", "12 ming", "50 ming", "200 ming kishilik.")
t.B("Nodirshoh qo‘shinlarining Buxoroga yurishi qachon boshlangan?", "1740-yilda", "1711-yilda", "1747-yilda", "1702-yilda", "1740-yilda.")
t.B("Taslim bo‘lish shartnomasini imzolash uchun Abulfayzxon qayerga borgan?", "Chorbakr qo‘rig‘iga", "Mashhadga", "Samarqandga", "Balxga", "Zarafshon bo‘yidagi Chorbakrga.")
t.B("Nodirshohga yuborilgan 10 ming kishilik qo‘shinga kim qo‘mondon etib tayinlangan?", "Muhammad Rahim", "Muhammad Hakimbiy", "Abulfayzxon", "Yalangto‘sh", "Muhammad Hakimbiyning o‘g‘li Muhammad Rahim.")
t.NAT("Vali Muhammadxon safaviylar bilan murosaga bordi.", "bir guruh buxorolik amaldorlar norozi bo‘lib, Imomqulini taxtga o‘tqazdi", "safaviylar Buxoroni bosib oldi", "Vali Muhammadning mavqei mustahkamlandi", "Yalangto‘sh Eronga ketdi", "1611-yilda taxt almashdi.")
t.NAT("Nadr Muhammadxon nufuzli zodagonlar mulkini tortib olib, viloyatlarni qarindoshlariga bo‘lib berdi.", "norozi amirlar fitna uyushtirib, Abdulazizni xon deb e’lon qildi", "zodagonlar unga sodiq qoldi", "davlat markazlashdi", "qozoqlar bilan sulh tuzildi", "Nadr Muhammad hokimiyatdan ayrildi.")
t.NAT("Toshkent, Xo‘jand, Balx, Hisor kabi viloyatlar deyarli mustaqil mulklarga aylandi.", "davlat xorijiy bosqinchilar uchun yengil o‘ljaga aylandi", "davlat kuchaydi", "Nodirshoh mag‘lub bo‘ldi", "markaziy hokimiyat mustahkamlandi", "Nodirshoh bostirib keldi.")
t.NAT("Buxoro Nodirshohga jangsiz taslim bo‘ldi.", "Abulfayzxon nomigagina oliy hukmdor etib qoldirildi", "Abulfayzxon qatl etildi", "Buxoro Eronga qo‘shib olindi", "mang‘itlar Eronni bosib oldi", "Abulfayzxon nomigagina xon.")
t.TF("Boqi Muhammadxon Xorazm, Balx, Marv kabi shaharlarni o‘z izmiga solgan.", True, "To‘g‘ri.")
t.TF("Shartnomaga ko‘ra Buxoro Nodirshoh qo‘shini uchun 2 yilga yetadigan don to‘plab bergan.", False, "Noto‘g‘ri: 8 yilga yetadigan 200 ming xarbor bug‘doy va arpa.")
t.TF4([("Yalangto‘sh 1611-yilda Imomqulixonni taxtga o‘tqazishda qatnashgan.", True), ("Yalangto‘sh Balx va Samarqand viloyatlari hokimi bo‘lgan.", True),
       ("Abulfayzxon 1645–1681-yillarda hukmronlik qilgan.", False), ("Joni Muhammad va Zuhrabonudan Boqi Muhammad tug‘ilgan.", True)],
      "3-noto‘g‘ri: 1645–1681 – Abdulazizxon; Abulfayzxon 1711–1747.")
t.MUL([("1640-yilda Imomqulixon Moskvaga qalmiqlarga qarshi qo‘shin yuborishga tayyorligini bildirgan.", True),
       ("Yalangto‘shning shaxsiy qo‘shini bo‘lgan.", True),
       ("Ashtarxoniylar sulolasi uch asr hukmronlik qilgan.", False)],
      "III noto‘g‘ri: bir yarim asrlik hukmronlik.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Ashtarxoniylar hokimiyatni egalladi", "Imomqulixon taxtga o‘tqazildi", "Yalangto‘sh Samarqandni mustaqil idora eta boshladi", "Qozoqlar Xo‘jandgacha keldi", "Abdulazizxon Balxni qaytarib oldi", "Nodirshoh Buxoroga yurish boshladi"],
      "1601 → 1611 → 1626 → 1645 → 1648 → 1740.")
t.MATCH("Ashtarxoniy xonlarni hukmronlik yillari bilan moslashtiring.", ["Abdulazizxon", "Subhonqulixon", "Ubaydullaxon", "Abulfayzxon"],
        ["1645–1681", "1681–1702", "1702–1711", "1711–1747", "1642–1645"], 'abcd',
        "Abdulaziz 1645–1681; Subhonquli 1681–1702; Ubaydulla 1702–1711; Abulfayz 1711–1747.")
t.VENN("Imomqulixon", "Nadr Muhammadxon",
       [("o‘ttiz yildan ortiq hukmronlik qilgan", 1), ("1611-yilda taxtga o‘tqazilgan", 1),
        ("zodagonlar mulkini tortib olgan", 2), ("haj yo‘lida vafot etgan", 2),
        ("ashtarxoniylar sulolasi vakili", 3)],
       "Imomquli – 30 yil, 1611; Nadr Muhammad – mulk musodarasi, haj; ikkalasi ashtarxoniy.")
t.MAPMATCH('uzb', ['Nurota', 'Samarqand', 'Balx', 'Xo‘jand'],
           ["Yalangto‘sh Bahodir tug‘ilgan joy", "1626-yildan Yalangto‘sh mustaqil idora etgan shahar", "1648-yilda boburiylardan qaytarib olingan viloyat", "1645-yilda qozoqlar yetib kelgan shahar"],
           "1 – Nurota; 2 – Samarqand; 3 – Balx; 4 – Xo‘jand.")
