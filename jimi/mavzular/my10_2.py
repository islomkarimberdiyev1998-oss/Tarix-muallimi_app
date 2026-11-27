from qlib import Topic, PLACES, REG
TOPICS = {}
W = 'globe'; EA = 'eastasia'; LA = 'latam'

# 5 Ikki xil Amerika
t = Topic('y10j5', 10005); TOPICS['y10j5'] = t
t.B("AQSHda fuqarolar urushi qaysi yillarda bo‘lgan?", "1861–1865-yillarda", "1775–1783-yillarda", "1898-yilda", "1910–1917-yillarda", "1861–1865-yillarda.")
t.B("AQSHdagi fuqarolar urushi o‘z mohiyatiga ko‘ra qanday inqilob edi?", "burjua-demokratik inqilob", "sotsialistik inqilob", "milliy-ozodlik inqilobi", "diniy inqilob", "Burjua-demokratik inqilob edi.")
t.B("Fuqarolar urushidan so‘ng AQSH qishloq xo‘jaligida qanday yo‘l qaror topgan?", "erkin fermerlikka asoslangan «amerikacha» yo‘l", "plantatsiya qulchiligi", "feodal yer egaligi", "jamoa xo‘jaligi", "Erkin fermerlikka asoslangan «amerikacha» yo‘l.")
t.B("AQSH sanoat mahsulotlari hajmi bo‘yicha qachon dunyoda birinchi o‘ringa chiqqan?", "1894-yilda", "1865-yilda", "1901-yilda", "1913-yilda", "1894-yili barcha rivojlangan mamlakatlarni quvib o‘tdi.")
t.B("1901-yili AQSH prezidentligini kim egallagan?", "Teodor Ruzvelt", "Vudro Vilson", "Avraam Linkoln", "Uilyam Makkinli", "1901-yili Teodor Ruzvelt.")
t.B("1912-yilgi saylovlarda kim g‘olib chiqqan?", "Vudro Vilson", "Teodor Ruzvelt", "Madero", "Uerta", "Demokratlar vakili, tarixchi Vudro Vilson.")
t.B("Vudro Vilsonning siyosiy dasturi qanday atalgan?", "«yangi erkinlik»", "«yangi kurs»", "«progressiv era»", "«ochiq eshiklar»", "«Yangi erkinlik» dasturi.")
t.B("AQSH Alyaskani kimdan sotib olgan?", "Rossiyadan", "Ispaniyadan", "Angliyadan", "Kanadadan", "Rossiyadan sotib olingan Alyaska yarimoroli.")
t.B("I Panamerika konferensiyasi qachon va qayerda chaqirilgan?", "1889-yilda Vashingtonda", "1898-yilda Gavanada", "1910-yilda Mexikoda", "1912-yilda Nyu-Yorkda", "1889-yili Vashingtonda.")
t.B("1898-yilgi urushda AQSH kimni yengib, Puerto-Riko va Guamni qo‘shib olgan?", "Ispaniyani", "Meksikani", "Angliyani", "Yaponiyani", "1898-yili Ispaniya bilan urushda g‘olib chiqdi.")
t.B("AQSH madaniyatining asosini qaysi aholi belgilagan?", "inglizzabon aholi", "ispanzabon aholi", "Amerika hindulari", "nemis immigrantlari", "Asosni inglizzabon aholi belgiladi.")
t.B("XIX asr 60–90-yillarida AQSH adabiyotida kimlar ijod qilgan?", "Uolt Uitmen va Mark Tven", "Sezar Valyexo va Gabrila Mistral", "Diyego Rivera va Orosko", "Uinslou Homer va Jeyms Uistler", "Adabiyotda Uolt Uitmen va Mark Tven.")
t.B("Braziliyada qulchilik qachon bekor qilingan?", "1888-yilda", "1891-yilda", "1865-yilda", "1910-yilda", "1888-yili bekor qilindi, 1891-yili respublika e’lon qilindi.")
t.B("Meksika inqilobi qaysi yillarda bo‘lgan?", "1910–1917-yillarda", "1861–1865-yillarda", "1888–1891-yillarda", "1898-yilda", "1910–1917-yillarda.")
t.B("1911-yili Meksikada kimning diktatorlik hokimiyati ag‘darilgan?", "Dias", "Madero", "Uerta", "Rivera", "Diktator Dias hokimiyati ag‘darildi.")
t.B("1913-yil fevraldagi qo‘zg‘olon natijasida hokimiyatga kim kelgan?", "general Uerta", "Madero", "Dias", "Sikeyros", "General Uerta; Madero otib tashlandi.")
t.B("Bir davlatning boshqa davlat ichki ishlariga zo‘rlik bilan aralashuvi nima deb ataladi?", "intervensiya", "anneksiya", "avtoritar rejim", "immigratsiya", "Intervensiya.")
t.B("XX asr boshlarida Lotin Amerikasi tasviriy san’atida kim ijod qilgan?", "Diyego Rivera", "Mark Tven", "Uolt Uitmen", "Tomas Ikins", "Diyego Rivera, Xose Orosko, David Sikeyros.")
t.NAT("1916-yili AQSH Meksikaga qo‘shin kiritdi.", "barcha inqilobiy kuchlar birlashdi; 1917-yil fevralda AQSH qo‘shinlari olib chiqildi, inqilob g‘alaba qozondi", "Meksika AQSH mustamlakasiga aylandi", "Madero hokimiyatga qaytdi", "Dias diktaturasi tiklandi", "Interventlar bilan kurash qariyb bir yil davom etdi.")
t.NAT("1889-yilgi I Panamerika konferensiyasi o‘tkazildi.", "Amerika respublikalari xalqaro assotsiatsiyasi tuzildi, panamerika siyosati shakllandi", "AQSH Alyaskani sotdi", "Lotin Amerikasi AQSHdan mustaqil bo‘ldi", "Braziliyada qulchilik bekor qilindi", "Panamerika siyosati shakllandi.")
t.TF("AQSH mustamlakalarni egallashga Yevropa davlatlaridan keyinroq kirishgan.", True, "To‘g‘ri: AQSH ichki imkoniyatlari va Alyaskani o‘zlashtirish bilan band edi.")
t.TF("XIX asr oxirida Lotin Amerikasiga chet el kapitali kiritishda Yaponiya yetakchilik qilgan.", False, "Noto‘g‘ri: XIX asrda Angliya, asr oxiriga kelib Germaniya va ayniqsa AQSH.")
t.MUL([("1898-yildan keyin Filippin AQSH mustamlakasiga aylangan.", True),
       ("Lotin Amerikasidagi ko‘plab davlatlarda armiyaga tayangan avtoritar rejimlar o‘rnatilgan.", True),
       ("Madero hukumati AQSHning qo‘llab-quvvatlashi tufayli mustahkamlangan.", False)],
      "III noto‘g‘ri: AQSH Maderoga qarshi kuchlarni qo‘llab-quvvatlagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["AQSHda fuqarolar urushi boshlandi", "Braziliyada qulchilik bekor qilindi", "I Panamerika konferensiyasi", "AQSH–Ispaniya urushi", "Meksikada Dias hokimiyati ag‘darildi", "AQSH qo‘shinlari Meksikadan olib chiqildi"],
      "1861 → 1888 → 1889 → 1898 → 1911 → 1917.")
t.VENN("AQSH", "Lotin Amerikasi",
       [("1894-yilda sanoatda dunyoda birinchi", 1), ("Uolt Uitmen va Mark Tven ijodi", 1),
        ("Braziliyada qulchilik 1888-yilda bekor qilingan", 2), ("Diyego Rivera va Orosko ijodi", 2),
        ("Amerika qit’asidagi mamlakatlar", 3)],
       "AQSH – 1894, Uitmen, Tven; Lotin Amerikasi – Braziliya, Rivera; ikkalasi Amerika qit’asida.")
t.MAPMATCH('amerpac', ['Alyaska', 'Gavayi orollari', 'Filippin', 'Meksika'],
           ["AQSH Rossiyadan sotib olgan yarimorol", "Tinch okeanida Osiyoga eltuvchi yo‘llar chorrahasidagi orollar", "1898-yildan AQSH mustamlakasiga aylangan", "1910–1917-yillarda inqilob bo‘lgan davlat"],
           "1 – Alyaska; 2 – Gavayi; 3 – Filippin; 4 – Meksika.")

# 6 Yaponiya, Xitoy va Hindiston
t = Topic('y10j6', 10006); TOPICS['y10j6'] = t
t.B("XIX asr oxiri – XX asr boshlari qanday davr deb atalgan?", "«Osiyo uyg‘onishi» davri", "«Pax Britanica» davri", "«progressiv era»", "«ajoyib davr»", "«Osiyo uyg‘onishi» davri.")
t.B("Yevropa-amerikacha boshqaruv, ta’lim, kiyinish modeliga taqlid qilish qanday atalgan?", "«g‘arblashish»", "«o‘z-o‘zini kuchaytirish»", "«yopiq mamlakat»", "«Meydzi»", "«G‘arblashish» – mustamlakalashtirish oqibati.")
t.B("Yaponiya necha asr davomida G‘arb uchun «yopiq» bo‘lgan?", "ikki asr", "bir asr", "uch asr", "besh asr", "Ikki asr davomida «yopiq» bo‘lib qolgan.")
t.B("Tokugava syogunligi qachon ag‘darilgan?", "1868-yilda", "1869-yilda", "1871-yilda", "1889-yilda", "1868-yili ag‘darildi, 1869-yili butunlay tugatildi.")
t.B("«Meydzi» so‘zi qanday ma’noni anglatadi?", "ma’rifatli boshqaruv", "quyosh chiqar mamlakat", "o‘z-o‘zini kuchaytirish", "milliy partiya", "Meydzi – ma’rifatli boshqaruv.")
t.B("Meydzi davri qaysi yillarni o‘z ichiga oladi?", "1868–1912-yillar", "1856–1860-yillar", "1904–1905-yillar", "1871–1889-yillar", "1868–1912-yillar.")
t.B("Meydzi davrida hukmronlik qilgan imperator kim?", "Mutsuxito", "Tokugava", "Sun Yatsen", "Xirohito", "Imperator Mutsuxito.")
t.B("1871-yilda Yaponiyada feodal yer mulklari o‘rniga nimalar joriy qilingan?", "prefekturalar", "syogunliklar", "knyazliklar", "shtatlar", "Markaziy hukumatga bo‘ysunuvchi prefekturalar.")
t.B("Yaponiya konstitutsiyasi qachon qabul qilingan?", "1889-yil boshlarida", "1868-yilda", "1871-yilda", "1912-yilda", "1889-yil boshlarida; mamlakat konstitutsion monarxiyaga aylandi.")
t.B("Koreya qachondan rasman Yaponiya mustamlakasi bo‘lgan?", "1910-yildan", "1905-yildan", "1895-yildan", "1889-yildan", "1910-yildan rasman mustamlaka.")
t.B("Ikkinchi «afyun urushi» qaysi yillarda bo‘lgan?", "1856–1860-yillarda", "1840–1842-yillarda", "1894–1895-yillarda", "1911–1912-yillarda", "1856–1860-yillarda.")
t.B("Xitoyda «szi syan» nomini olgan yo‘l nimani anglatadi?", "«o‘z-o‘zini kuchaytirish»", "«g‘arblashish»", "«milliy partiya»", "«ma’rifatli boshqaruv»", "«O‘z-o‘zini kuchaytirish» yo‘li.")
t.B("XX asr boshlarida Xitoy aholisining qancha qismi savodsiz edi?", "90% i", "50% i", "30% i", "10% i", "400 mln aholining 90% i savodsiz edi.")
t.B("Sinxay inqilobiga kim boshchilik qilgan?", "Sun Yatsen", "Mutsuxito", "Vivekananda", "Tokugava", "Sun Yatsen boshchiligida.")
t.B("Gomindan partiyasi nomi qanday ma’noni anglatadi?", "«Milliy partiya»", "«Xalq fronti»", "«Musulmon ligasi»", "«Kongress»", "Gomindan – «Milliy partiya», 1912-yilda tuzilgan.")
t.B("Aholining keng qatlamlariga tushunarli bo‘lgan Xitoy adabiy tili qaysi?", "bayxua", "venyan", "sanskrit", "xangul", "Bayxua venyanni siqib chiqardi.")
t.B("Hindistonda birinchi yirik ingliz sarmoyasi kiritilgan soha qaysi?", "temiryo‘l qurilishi", "plantatsiya xo‘jaligi", "to‘qimachilik", "kemasozlik", "Birinchi sarmoya temiryo‘l qurilishiga kiritildi.")
t.B("Hindiston milliy kongressi qachon va qayerda tashkil qilingan?", "1885-yil dekabrda Bombeyda", "1906-yilda Dehlida", "1913-yilda Kalkuttada", "1889-yilda Madrasda", "1885-yil dekabrda Bombeyda.")
t.B("Musulmon ligasi qachon tashkil qilingan?", "1906–1907-yillarda", "1885-yilda", "1913-yilda", "1871-yilda", "1906–1907-yillari.")
t.B("«Gitanjali» turkum she’rlari uchun Nobel mukofotini kim olgan?", "Rabindranath Thakur", "Svami Vivekananda", "Ramakrishna Paramahamsa", "Sun Yatsen", "1913-yili Rabindranath Thakur.")
t.NAT("1904–1905-yillardagi rus-yapon urushi.", "Yaponiya Janubiy Manchjuriya va Koreya ustidan hukmronlik o‘rnatdi", "Yaponiya Koreyadan voz kechdi", "Rossiya Yaponiyani bosib oldi", "Xitoy respublika bo‘ldi", "Yaponiya Koreyaning tashqi siyosatini belgilay boshladi.")
t.NAT("1911–1912-yillardagi Sinxay inqilobi.", "manchjurlar sulolasi ag‘darildi, Xitoy respublika deb e’lon qilindi", "syogunlik tugatildi", "Xitoy Yaponiya mustamlakasiga aylandi", "afyun urushi boshlandi", "Respublika e’lon qilindi, lekin mamlakat siyosiy tarqoq bo‘ldi.")
t.TF("Vivekananda hozirgi zamon Hindiston milliy harakatining asoschilaridan biri edi.", True, "To‘g‘ri.")
t.TF("XX asr boshlarida Musulmon ligasi va HMK o‘rtasida parlament islohotlari masalasida keskin kelishmovchilik bo‘lgan.", False, "Noto‘g‘ri: jiddiy kelishmovchilik mavjud emasdi.")
t.MUL([("1871-yilda Yaponiyada tabaqalar soni uchtagacha qisqartirilgan.", True),
       ("«O‘z-o‘zini kuchaytirish» yo‘li 1895-yilgacha amalga oshirilgan.", True),
       ("Sinxay inqilobi nomini birinchi bo‘lib Sun Yatsen tug‘ilgan shahar nomidan olgan.", False)],
      "III noto‘g‘ri: xitoy taqvimi bo‘yicha «sinxay» yilida boshlangani uchun shunday nomlangan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Ikkinchi afyun urushi boshlandi", "Tokugava syogunligi ag‘darildi", "Hindiston milliy kongressi tuzildi", "Yaponiya konstitutsiyasi qabul qilindi", "Koreya Yaponiya mustamlakasiga aylandi", "Thakur Nobel mukofotini oldi"],
      "1856 → 1868 → 1885 → 1889 → 1910 → 1913.")
t.MATCH("Shaxslarni mamlakati bilan moslashtiring.", ["Mutsuxito", "Sun Yatsen", "Vivekananda", "Rabindranath Thakur"],
        ["Yaponiya imperatori", "Gomindan asoschisi (Xitoy)", "hind milliy harakati asoschilaridan biri", "«Gitanjali» muallifi", "Koreya qiroli"], 'abcd',
        "Mutsuxito – Yaponiya; Sun Yatsen – Xitoy; Vivekananda va Thakur – Hindiston.")
t.MAPMATCH(EA, ['Yaponiya', 'Koreya', 'Janubiy Manchjuriya', 'Xitoy'],
           ["1868-yilda Meydzi inqilobi bo‘lgan mamlakat", "1910-yildan Yaponiya mustamlakasi", "rus-yapon urushidan so‘ng janubiy qismi Yaponiya hukmronligiga o‘tgan hudud", "1911–1912-yillarda Sinxay inqilobi bo‘lgan mamlakat"],
           "1 – Yaponiya; 2 – Koreya; 3 – Manchjuriya; 4 – Xitoy.")
