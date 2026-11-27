from qlib import Topic
TOPICS = {}
W = 'globe2'; EU = 'europe'

# 1 Kapitalizm taraqqiyotidagi tub o‘zgarishlar
t = Topic('e9j1', 9101); TOPICS['e9j1'] = t
t.B("XIX asr oxiri – XX asr boshlarida kapitalizm taraqqiyotida qanday bosqich qaror topdi?", "monopolistik kapitalizm", "erkin kapitalizm", "manufaktura bosqichi", "feodalizm", "Monopolistik kapitalizm bosqichi.")
t.B("Ishlab chiqarish yoki savdoning bir sohasida yakka hukmronlikni egallagan korxonalar birlashmasi nima?", "monopoliya", "oligarxiya", "anneksiya", "migratsiya", "Monopoliya.")
t.B("Germaniyada ko‘mirning asosiy qismini qaysi sindikat o‘z qo‘lida to‘plagan?", "Reyn-Vestfaliya ko‘mir sindikati", "Rokfeller tresti", "Krupp konserni", "Morgan tresti", "Reyn-Vestfaliya ko‘mir sindikati.")
t.B("XIX asr oxirida Germaniyada nechta monopoliya faoliyat ko‘rsatgan?", "250 ta", "185 ta", "100 ta", "60 ta", "Germaniyada 250 ta, AQSHda 185 ta.")
t.B("Moliya oligarxiyasi nimaning qo‘shilishi natijasida vujudga kelgan?", "sanoat va bank kapitalining", "yer va savdo kapitalining", "davlat va cherkovning", "ishchilar va dehqonlarning", "Sanoat va bank kapitalining qo‘shilishi.")
t.B("AQSHda iqtisodiy hayotni nazorat qilgan nechta oila bo‘lgan?", "60 ta", "200 ta", "3 ta", "100 ta", "60 ta oila.")
t.B("AQSHdagi «katta uchlik»ka kimlar kirgan?", "Rokfeller, Morgan, Karnegi", "Krupp, Rotshild, Morgan", "Ford, Edison, Bell", "Rotshild, Krupp, Karnegi", "Rokfeller (neft), Morgan (moliya), Karnegi (po‘lat).")
t.B("Morganning po‘lat tresti AQSH po‘latining qancha qismini bergan?", "66 foizini", "25 foizini", "90 foizini", "50 foizini", "66 foizini.")
t.B("Fransiyada moliyaviy qudrat timsoli nima bo‘lgan?", "«200 oila»", "«katta uchlik»", "«60 oila»", "«tojsiz qirollar»", "Fransuz bankining yirik omonatchilari — «200 oila».")
t.B("1900–1913-yillarda industrial davlatlar chetga chiqargan kapital hajmi qanchaga oshgan?", "ikki barobar", "o‘n barobar", "uch barobar", "o‘zgarmagan", "Ikki barobar oshgan.")
t.B("1910-yilda millatlararo korporatsiyalar soni nechtaga yetgan?", "100 taga", "250 taga", "60 taga", "1000 taga", "100 taga.")
t.B("Jahon kerosin bozorini qaysi moliya guruhlari bo‘lib olgan?", "Rokfeller va Rotshildlar", "Morgan va Krupp", "Karnegi va Rotshildlar", "Krupp va Rokfeller", "Rokfeller (AQSH) va Rotshildlar.")
t.B("Bir davlat hududini butunlay yoki qisman egallab olish nima deyiladi?", "anneksiya", "kartel", "konsern", "migratsiya", "Anneksiya.")
t.B("XIX asr oxirida AQSH qaysi orollarni anneksiya qilgan?", "Gavayi orollarini", "Britaniya orollarini", "Yapon orollarini", "Kanar orollarini", "Gavayi orollarini.")
t.B("AQSH monopoliyachilari qanday atalgan?", "«Amerikaning tojsiz qirollari»", "«po‘lat qirollari»", "«200 oila»", "«katta uchlik»", "«Amerikaning tojsiz qirollari».")
t.NAT("Monopoliyalar vujudga keldi.", "ishlab chiqarishga yangi texnika keng joriy etilib, mehnat unumdorligi keskin oshdi", "ishlab chiqarish to‘xtadi", "raqobat kuchaydi va mayda korxonalar ko‘paydi", "texnika taraqqiyoti sekinlashdi", "Monopoliyalarning birinchi oqibati — yangi texnika va unumdorlik o‘sishi.")
t.NAT("Dunyo bo‘lib olinib, mustamlakalarni qayta bo‘lish masalasi paydo bo‘ldi.", "qurollanish poygasi boshlanib, hayotni harbiylashtirish avj oldi", "davlatlar qurolsizlandi", "mustamlakalar ozod qilindi", "monopoliyalar tugatildi", "Ko‘plab davlatlar kuchga tayanishni lozim topdi.")
t.TF("AQSH ochiq qurolli hujumdan ko‘ra Lotin Amerikasi iqtisodiga kirib borishni afzal ko‘rgan.", True, "To‘g‘ri.")
t.TF("XIX asr oxirida Germaniya iqtisodiy ko‘rsatkichlar bo‘yicha dunyoda birinchi o‘rinda edi.", False, "Noto‘g‘ri: Yevropada birinchi, dunyoda AQSHdan keyin ikkinchi o‘rinda edi.")
t.MUL([("Chetga kapital chiqarish tovar chiqarishdan foydaliroq bo‘lib qoldi.", True),
       ("1907-yilda AQSH va Germaniya elektr monopoliyalari jahon elektr bozorini bo‘lish shartnomasini tuzgan.", True),
       ("«Imperializm» atamasi «erkin kapitalizm» atamasining sinonimi sifatida qo‘llangan.", False)],
      "III noto‘g‘ri: u «monopolistik kapitalizm»ning sinonimi bo‘ldi.")
t.MATCH("Atamalarni ta’riflari bilan moslashtiring.", ["kartel", "sindikat", "trest", "konsern"],
        ["markaziy boshqaruv qarori asosida ishlovchi birlashma", "manfaatlar umumiyligi asosidagi yirik birlashma", "narx, bozor va ulushlar haqidagi bitim asosidagi tuzilma", "bir turdagi mahsulot ishlab chiqaruvchi korxonalar birlashmasi"], "cdab",
        "Kartel — bitim; sindikat — bir turdagi mahsulot; trest — markaziy boshqaruv; konsern — manfaatlar umumiyligi.")
t.MAPMATCH(W, ['Gavayi orollari', 'Filippin', 'Puerto-Riko'],
           ["AQSH anneksiya qilgan orollar", "AQSH bosib olgan mamlakat", "AQSH yarimmustamlakasiga aylantirgan orol"],
           "1 – Gavayi; 2 – Filippin; 3 – Puerto-Riko.")
t.VENN("Erkin kapitalizm", "Monopolistik kapitalizm",
       [("monopoliyalar hali hukmron emas", 1), ("asosan tovar chiqarilgan", 1),
        ("moliya oligarxiyasi shakllangan", 2), ("chetga kapital chiqarish ustun", 2),
        ("kapitalizm bosqichi", 3)],
       "Monopolistik bosqich — monopoliyalar, oligarxiya, kapital eksporti bilan ajralib turadi.")

# 2 Industrial sivilizatsiya
t = Topic('e9j2', 9102); TOPICS['e9j2'] = t
t.B("Industrial sivilizatsiyaning asosiy qadriyati nima bo‘lgan?", "texnika taraqqiyoti", "yer mulki", "diniy an’analar", "qishloq xo‘jaligi", "Asosiy qadriyati — texnika taraqqiyoti.")
t.B("G‘arbiy Yevropa va AQSHda sanoat to‘ntarishi qachon nihoyasiga yetgan?", "XIX asrning 50–60-yillarida", "XVIII asr oxirida", "XX asr boshida", "XIX asr boshida", "XIX asrning 50–60-yillarida.")
t.B("Industrial sivilizatsiyaning belgilaridan biri nima bo‘lgan?", "shaharlarning juda tez o‘sishi", "shaharlarning qisqarishi", "aholining qishloqqa ko‘chishi", "sanoatning pasayishi", "Shaharlarning juda tez o‘sishi.")
t.B("XIX asr o‘rtalariga kelib industrial davlatlarda aholining qancha qismi shaharlarda to‘plangan?", "qariyb yarmi", "o‘ndan biri", "to‘rtdan uchi", "deyarli hammasi", "Qariyb yarmi.")
t.B("Parij aholisi 1880-yilda qancha bo‘lgan?", "ikki million", "bir million", "besh million", "500 ming", "1850-yilda 1 mln, 1880-yilda 2 mln.")
t.B("Parij qachondan boshlab 20 yil davomida qurilish maydoniga aylangan?", "1853-yildan", "1871-yildan", "1880-yildan", "1830-yildan", "1853-yildan.")
t.B("Jamiyat hayotida shaharlar roli va shahar aholisi salmog‘ining ortishi nima deyiladi?", "urbanizatsiya", "migratsiya", "industriya", "immigratsiya", "Urbanizatsiya.")
t.B("XIX asr o‘rtalarida Britaniya jamoalar palatasining 652 a’zosidan nechtasi yer mulkdorlari edi?", "489 tasi", "300 tasi", "100 tasi", "652 tasi", "489 tasi.")
t.B("Britaniya aristokrat yoshlari qaysi universitetlarda o‘qigan?", "Oksford yoki Kembrij", "Sorbonna", "Geydelberg", "Garvard", "Oksford yoki Kembrij.")
t.B("Muhandislar, shifokorlar, o‘qituvchilar, huquqshunoslar jamiyatning qaysi qatlamini tashkil etgan?", "o‘rta qatlam", "aristokratiya", "ishchilar sinfi", "burjuaziya", "O‘rta qatlam («erkin kasb» egalari).")
t.B("XIX asr ikkinchi yarmida o‘rta qatlam orasida qaysi toifa ajralib turgan?", "huquqshunoslar", "harbiylar", "ruhoniylar", "dehqonlar", "Huquqshunoslar.")
t.B("XX asr boshida sanoat ishchilari soni bo‘yicha qaysi davlat birinchi o‘rinda edi?", "AQSH", "Germaniya", "Buyuk Britaniya", "Fransiya", "AQSH — 10,4 mln sanoat ishchisi.")
t.B("1907-yilda Germaniyada sanoat ishchilari soni qancha bo‘lgan?", "8,6 mln", "10,4 mln", "20 mln", "40 mln", "8,6 mln.")
t.B("Britaniyada «ishchi aristokratiyasi» ishchilarning qancha qismini tashkil qilgan?", "uchdan birini", "yarmini", "o‘ndan birini", "to‘rtdan uchini", "Uchdan birini.")
t.B("XIX asrning 70-yillarigacha industrial davlatlarda ish kuni qancha bo‘lgan?", "10–16 soat", "8 soat", "6 soat", "20 soat", "10–16 soat.")
t.B("II Internatsional qachon tashkil topgan?", "1889-yilda", "1871-yilda", "1864-yilda", "1907-yilda", "1889-yilda.")
t.NAT("Qishloq xo‘jaligida texnika qo‘llanilib, bir qism qishloq aholisi ishsiz qoldi.", "ular ish izlab shaharlarga keta boshladi, migratsiya kuchaydi", "shaharlar qisqardi", "qishloqlar kengaydi", "sanoat to‘xtadi", "Qishloqdan ketish migratsiyani keltirib chiqardi.")
t.NAT("Mulkidan ayrilgan eski aristokratlar yangi boylar bilan qarindosh tutindi.", "aristokratiya burjuaziya bilan qo‘shilib ketdi", "aristokratiya kuchaydi", "burjuaziya yo‘qoldi", "yer mulklari ko‘paydi", "Aristokratiya burjuaziya bilan qo‘shilib ketdi.")
t.TF("O‘rta qatlam odatda inqiloblardan islohotlarni afzal ko‘radi.", True, "To‘g‘ri: u jamiyatga barqarorlik baxsh etadi.")
t.TF("Ayollar va bolalar mehnatiga erkaklarnikidan ko‘p haq to‘langan.", False, "Noto‘g‘ri: ularga kam to‘langan.")
t.MUL([("10–12 yoshli bolalar tamaki fabrikalari va toshko‘mir shaxtalarida ishlagan.", True),
       ("AQSHda sanoat ishchilarining 2/3 qismi malakali ishchilar edi.", True),
       ("II Internatsional ishchi partiyalarini to‘liq birlashtirishga erishgan.", False)],
      "III noto‘g‘ri: kelishmovchiliklar natijasida II Internatsional halokatga uchragan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Parij aholisi 1 million", "Parijni qayta qurish boshlandi", "Parij aholisi 2 million", "II Internatsional tashkil topdi", "Germaniyada 8,6 mln sanoat ishchisi"],
      "1850 → 1853 → 1880 → 1889 → 1907.")
t.MAPMATCH(EU, ['Parij', 'London', 'Berlin'],
           ["1853-yildan 20 yil zamonaviy qilib qayta qurilgan poytaxt", "jamoalar palatasining 489 a’zosi yer mulkdori bo‘lgan parlament joylashgan shahar", "sanoat ishchilari 1907-yilda 8,6 mln ga yetgan davlat poytaxti"],
           "1 – Parij; 2 – London; 3 – Berlin.")
t.VENN("Aristokratiya", "Burjuaziya",
       [("asosiy boyligi yer mulklari", 1), ("hayoti ko‘proq qishloq bilan bog‘liq", 1),
        ("yirik sanoat korxonalari va banklar egalari", 2), ("XIX asrda roli tobora ortgan", 2),
        ("o‘zaro qarindoshlik orqali qo‘shilib ketgan", 3)],
       "Aristokratiya — yer, qishloq; burjuaziya — sanoat, banklar; ular qo‘shilib ketgan.")
