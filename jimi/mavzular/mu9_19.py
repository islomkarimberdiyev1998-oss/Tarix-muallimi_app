from qlib import Topic
TOPICS = {}
UZ = 'uzb'; CA = 'ca'

# 38 Ta’lim tizimi. Matbuot
t = Topic('e9u38', 9038); TOPICS['e9u38'] = t
t.B("Mahalliy aholini ruslashtirish maqsadida qanday maktablar ochilgan?", "rus-tuzem maktablari", "jadid maktablari", "qorixonalar", "madrasalar", "Rus-tuzem maktablari.")
t.B("An’anaviy maktabda boshlang‘ich ta’lim necha yil davom etgan?", "5–6 yil", "10 yil", "1–2 yil", "3 oy", "5–6 yil.")
t.B("Qur’oni Karimning yettidan biri bo‘lgan kitob qanday atalgan?", "«Haftiyak»", "«Chor kitob»", "«Risolai aziza»", "«Sabot ul-ojizin»", "«Haftiyak».")
t.B("«Risolai aziza» va «Sabot ul-ojizin» kitoblari muallifi kim?", "So‘fi Olloyor", "Hofiz", "Alisher Navoiy", "Ahmad Donish", "So‘fi Olloyor.")
t.B("Qur’oni Karim yod olinadigan muassasa qanday atalgan?", "qorixona", "madrasa", "gimnaziya", "rus-tuzem maktabi", "Qorixona.")
t.B("Ayollarga kimlar ta’lim bergan?", "otinlar", "mudarrislar", "qorilar", "mullalar", "Otinlar.")
t.B("Rus-tuzem maktablari tarmog‘i loyihasini ishlab chiqqan general-gubernator kim?", "G. Rozenbax", "K. Kaufman", "S. Duxovskoy", "A. Vrevskiy", "G. Rozenbax (1884–1889).")
t.B("Birinchi rus-tuzem maktabi qachon va kimning uyida ochilgan?", "1884-yilda Toshkentda Saidg‘ani Saidazimboy uyida", "1896-yilda Samarqandda", "1870-yilda Qo‘qonda", "1906-yilda Buxoroda", "1884-yilda Toshkentda Saidg‘ani Saidazimboy uyida.")
t.B("1911-yilda rus-tuzem maktablari soni nechtaga yetgan?", "89 taga", "63 taga", "50 taga", "24 taga", "89 taga.")
t.B("Toshkentda birinchi gimnaziya qachon ochilgan?", "1896-yilda", "1884-yilda", "1870-yilda", "1906-yilda", "1896-yilda.")
t.B("1911-yilda nechtaga yaqin jadid maktablari yopib qo‘yilgan?", "50 ga yaqin", "89 ta", "100 ta", "10 ta", "50 ga yaqin.")
t.B("Buxoro amirligida barcha jadid maktablari qachon yopilgan?", "1913-yilga kelib", "1911-yilda", "1906-yilda", "1917-yilda", "1913-yilga kelib.")
t.B("«Turkiston viloyatining gazeti» muharriri kim bo‘lgan?", "N. Ostroumov", "Ismoil Obidov", "Munavvarqori", "Abdulla Avloniy", "Mustamlakachilik targ‘ibotchisi N. Ostroumov.")
t.B("Ilk o‘zbek milliy gazetasi qaysi?", "«Taraqqiy»", "«Xurshid»", "«Shuhrat»", "«Osiyo»", "1906-yilda Ismoil Obidov muharrirligida «Taraqqiy».")
t.B("Matbuot va OAV xodimlari kuni qaysi sanada nishonlanadi?", "27-iyunda", "6-oktabrda", "8-aprelda", "19-yanvarda", "«Taraqqiy»ning birinchi soni chiqqan 27-iyunda.")
t.B("1906-yilda Munavvarqori muharrirligida qaysi gazeta chop etilgan?", "«Xurshid»", "«Taraqqiy»", "«Shuhrat»", "«Osiyo»", "«Xurshid».")
t.B("Ahmadjon Bektemirov muharrirligida qaysi gazeta chiqqan?", "«Osiyo»", "«Shuhrat»", "«Xurshid»", "«Turon»", "«Osiyo».")
t.NAT("Mustamlakachi ma’muriyat jadidlar ta’limini mustamlakachilikka qarshi kuch deb angladi.", "jadidlar qattiq ta’qibga olindi, o‘quv nashrlariga senzura joriy qilindi", "jadid maktablari ko‘paytirildi", "ma’muriyat jadidlarni moliyalashtirdi", "rus-tuzem maktablari yopildi", "Jadid maktablariga qarshi kurash boshlandi.")
t.TF("Rus-tuzem maktablarida o‘quv kunining bir qismini rus, ikkinchisini mahalliy o‘qituvchi olib borgan.", True, "To‘g‘ri.")
t.TF("Mustamlaka davrida eski maktablarga hukumat katta mablag‘ ajratgan.", False, "Noto‘g‘ri: ularga hech qanday mablag‘ ajratilmagan.")
t.MUL([("Jadid maktablarida turkiy xalqlar tarixi bo‘yicha ham ta’lim berilgan.", True),
       ("Jadid maktablaridan G‘afur G‘ulom, Uyg‘un, Oybek kabi arboblar yetishib chiqqan.", True),
       ("Rus-tuzem maktablarida o‘qitish darajasi Rossiya maktablaridan yuqori bo‘lgan.", False)],
      "III noto‘g‘ri: ular Rossiyadagi maktablarga nisbatan ancha sayoz bo‘lgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["«Turkestanskiye vedomosti» chiqa boshladi", "Birinchi rus-tuzem maktabi ochildi", "Toshkentda birinchi gimnaziya ochildi", "«Taraqqiy» gazetasi nashr etildi", "50 ga yaqin jadid maktabi yopildi"],
      "1870 → 1884 → 1896 → 1906 → 1911.")
t.MATCH("Gazetalarni muharrirlari bilan moslashtiring.", ["«Taraqqiy»", "«Xurshid»", "«Shuhrat»", "«Osiyo»"],
        ["Abdulla Avloniy", "Ahmadjon Bektemirov", "Ismoil Obidov", "Munavvarqori"], "cdab",
        "«Taraqqiy» — Obidov; «Xurshid» — Munavvarqori; «Shuhrat» — Avloniy; «Osiyo» — Bektemirov.")
t.VENN("Rus-tuzem maktablari", "Jadid maktablari",
       [("G. Rozenbax loyihasi asosida ochilgan", 1), ("rus madaniyatini yoyishga xizmat qilgan", 1),
        ("vatanga muhabbat, milliy davlatchilik g‘oyalarini singdirgan", 2), ("1911-yilda 50 ga yaqini yopilgan", 2),
        ("Toshkentda ochilgan maktablar", 3)],
       "Rus-tuzem — Rozenbax, ruslashtirish; jadid — milliy g‘oyalar, yopilgan.")

# 39 Ilm-fan taraqqiyoti
t = Topic('e9u39', 9039); TOPICS['e9u39'] = t
t.B("«Tarixi Turkiston» asarini kim yozgan?", "Mulla Olim Maxdum hoji", "Muhammad Solih", "Bayoniy", "Behbudiy", "Tarixchi va jurnalist Mulla Olim Maxdum hoji.")
t.B("O‘zbek tilidagi ilk tarixiy asar sifatida shuhrat qozongan kitob qaysi?", "«Tarixi Turkiston»", "«Tarixi jadidai Toshkent»", "«Xorazm tarixi»", "«Shajarai Xorazmshohiy»", "«Tarixi Turkiston».")
t.B("«Tarixi jadidai Toshkent» asari muallifi kim?", "Muhammad Solih", "Mulla Olim Maxdum hoji", "Bayoniy", "Vyatkin", "Muhammad Solih, 25 yillik izlanishdan keyin.")
t.B("«Xorazm tarixi» va «Shajarai Xorazmshohiy» asarlari muallifi kim?", "Muhammad Yusuf Bayoniy", "Ogahiy", "Munis", "Muhammad Solih", "Xorazmlik Muhammad Yusuf Bayoniy.")
t.B("Ulug‘bek rasadxonasi qoldiqlarini kim topgan?", "V. Vyatkin", "N. Seversev", "A. Fedchenko", "Semyonov-Tyanshanskiy", "V. Vyatkin 1908-yilda.")
t.B("Vyatkin rasadxona qoldiqlarini qachon topgan?", "1908-yilda", "1895-yilda", "1876-yilda", "1867-yilda", "1908-yilda.")
t.B("Arxeologiya havaskorlari to‘garagi qachon tashkil etilgan?", "1895-yilda", "1908-yilda", "1871-yilda", "1876-yilda", "1895-yilda.")
t.B("Mintaqaning bosh xaritasi qachon tuzib chiqilgan?", "1867-yilda", "1876-yilda", "1870-yilda", "1895-yilda", "1867-yilda.")
t.B("Pomir tog‘ tizimini kim o‘rganib chiqqan?", "N. A. Seversev", "Semyonov-Tyanshanskiy", "A. P. Fedchenko", "V. Vyatkin", "Zoolog va sayyoh N. A. Seversev.")
t.B("Tyanshan tog‘ tizimini kim o‘rgangan?", "P. P. Semyonov-Tyanshanskiy", "N. Seversev", "A. Fedchenko", "N. Ostroumov", "P. P. Semyonov-Tyanshanskiy.")
t.B("Farg‘ona vodiysi, Oloy, Zarafshon vodiysi va Qizilqumni kim tekshirgan?", "A. P. Fedchenko", "N. Seversev", "Vyatkin", "Semyonov-Tyanshanskiy", "A. P. Fedchenko.")
t.B("O‘rta Osiyo Olimlar jamiyati qachon tashkil etilgan?", "1871-yilda", "1893-yilda", "1876-yilda", "1895-yilda", "1871-yilda; 1893-yilda mablag‘ yo‘qligidan to‘xtagan.")
t.B("Turkiston muzeyi qachon tashkil etilgan?", "1876-yilda", "1870-yilda", "1871-yilda", "1895-yilda", "1876-yilda (hozirgi O‘zbekiston tarixi davlat muzeyi).")
t.B("Turkiston xalq kutubxonasi qachon tashkil etilgan?", "1870-yilda", "1876-yilda", "1906-yilda", "1867-yilda", "1870-yilda Toshkentda.")
t.B("Erk va ozodlikni tarannum etgan she’rlari uchun zindonga tashlangan shoir kim?", "Zavqiy", "Muqimiy", "Furqat", "Avaz O‘tar o‘g‘li", "Ubaydulla Solih o‘g‘li Zavqiy.")
t.B("«Qo‘qondan Farg‘onagacha» sayohatnomasi muallifi kim?", "Muqimiy", "Zavqiy", "Furqat", "Anbar otin", "Muhammad Aminxo‘ja Muqimiy.")
t.B("Ayollar huquqi uchun kurashga da’vat etgani uchun kaltaklangan shoira kim?", "Anbar otin", "Nodira", "Uvaysiy", "Zebunniso", "Qo‘qonlik Anbar otin.")
t.B("Abdulla Qodiriy ilk nasriy asarlarini qachon e’lon qilgan?", "1910-yilda", "1906-yilda", "1913-yilda", "1917-yilda", "1910-yilda.")
t.B("1911–1917-yillarda jadid teatrlarida nechta pyesa namoyish etilgan?", "25 ta", "10 ta", "63 ta", "100 ta", "25 ta pyesa.")
t.B("«Padarkush» pyesasi muallifi kim?", "Mahmudxo‘ja Behbudiy", "Nusratilla Qudratilla", "Abdulla Qodiriy", "Abdulla Avloniy", "Mahmudxo‘ja Behbudiy.")
t.B("«To‘y» pyesasi kimning qalamiga mansub?", "Nusratilla Qudratilla", "Behbudiy", "Abdulla Qodiriy", "Hamza", "Nusratilla Qudratilla.")
t.NAT("O‘rta Osiyo Olimlar jamiyatida mablag‘ yo‘q edi.", "jamiyat 1893-yilda faoliyatini to‘xtatdi", "jamiyat kengaydi", "jamiyat Turkiston muzeyiga aylandi", "jamiyat Rossiyaga ko‘chirildi", "Mablag‘ yo‘qligi sababli 1893-yilda to‘xtadi.")
t.TF("Abdulla Qodiriyning asarlari qatorida «Juvonboz» hikoyasi va «Baxtsiz kuyov» pyesasi bor.", True, "To‘g‘ri.")
t.TF("Jadidlar tarixni faqat xonlar va amirlar almashinuvi sifatida tasvirlagan.", False, "Noto‘g‘ri: ular xalqni tarixning haqiqiy bunyodkori sifatida ko‘rsatgan.")
t.MUL([("Vyatkin «Shohizinda», «Cho‘ponota», «Afrosiyob qo‘rg‘oni» asarlarini yozgan.", True),
       ("Turkiston qishloq xo‘jaligi jamiyati «Turkistonning qishloq xo‘jaligi» jurnalini nashr ettirgan.", True),
       ("«Padarkush»da serchiqim sunnat to‘yi tanqid qilingan.", False)],
      "III noto‘g‘ri: serchiqim to‘y «To‘y» pyesasida tanqid qilingan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Mintaqaning bosh xaritasi tuzildi", "Turkiston xalq kutubxonasi tashkil etildi", "O‘rta Osiyo Olimlar jamiyati tuzildi", "Turkiston muzeyi tashkil etildi", "Arxeologiya havaskorlari to‘garagi tuzildi", "Ulug‘bek rasadxonasi qoldiqlari topildi"],
      "1867 → 1870 → 1871 → 1876 → 1895 → 1908.")
t.MATCH("Olimlarni ular o‘rgangan hududlar bilan moslashtiring.", ["N. A. Seversev", "P. P. Semyonov-Tyanshanskiy", "A. P. Fedchenko", "V. Vyatkin"],
        ["Samarqand (Ulug‘bek rasadxonasi)", "Tyanshan tog‘ tizimi", "Pomir tog‘ tizimi", "Farg‘ona vodiysi va Oloy"], "cbda",
        "Seversev — Pomir; Semyonov — Tyanshan; Fedchenko — Farg‘ona, Oloy; Vyatkin — Samarqand.")
t.VENN("Muqimiy", "Zavqiy",
       [("Qo‘qonda tug‘ilgan, «Tanobchilar» muallifi", 1), ("«Qo‘qondan Isfaragacha» sayohatnomasi", 1),
        ("erk haqidagi she’rlari uchun zindonga tashlangan", 2), ("Ubaydulla Solih o‘g‘li", 2),
        ("satirik she’rlar yozgan xalq shoiri", 3)],
       "Muqimiy — «Tanobchilar», sayohatnomalar; Zavqiy — zindonga tashlangan; ikkalasi satirik shoirlar.")
