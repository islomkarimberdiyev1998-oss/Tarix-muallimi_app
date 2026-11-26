from qlib import Topic
TOPICS = {}
W = 'globe'; EU = 'europe'

# 5 Angliya
t = Topic('e8j5', 805); TOPICS['e8j5'] = t
t.B("Qirolning cheklanmagan hokimiyati qanday atalgan?", "absolutizm (mutlaq monarxiya)", "konstitutsion monarxiya", "respublika", "protektorat", "Bunday hokimiyat mutlaq monarxiya yoki absolutizm deb ataldi.")
t.B("Angliyada absolutizm qachon shakllangan?", "XVI asrda", "XIV asrda", "XVIII asrda", "XIII asrda", "Absolutizm Angliyada XVI asrda shakllandi.")
t.B("Cherkov va parlamentni o‘ziga bo‘ysundirgan Tyudor qirol kim?", "Genrix VIII", "Yakov I", "Karl I", "Georg I", "Genrix VIII Tyudor cherkov va parlamentni bo‘ysundirdi.")
t.B("Yelizaveta I qachon hokimiyatga kelgan?", "1558-yilda", "1603-yilda", "1640-yilda", "1485-yilda", "1558-yili hokimiyatga kelgan Yelizaveta I 45 yil hukmronlik qildi.")
t.B("Yelizaveta I davrida Angliya qanday nom olgan?", "«dengizlar malikasi»", "«ustaxona»", "«Yevropa jandarmi»", "«oltin davlat»", "Angliya kuchli dengiz davlati – «dengizlar malikasi»ga aylandi.")
t.B("1603-yildan Angliya taxtini qaysi sulola egallagan?", "styuartlar", "tyudorlar", "gannoverlar", "oranyelar", "Yakov I bilan styuartlar sulolasi taxtga keldi.")
t.B("Amerikadagi birinchi ingliz mustamlakasi qaysi?", "Virjiniya", "Massachusets", "Kanada", "Yamayka", "Birinchi mustamlaka – Virjiniyaga asos solindi.")
t.B("Angliyada kalvinistlar qanday atalgan?", "puritanlar", "lyuteranlar", "iyezuitlar", "gugenotlar", "Kalvinistlar Angliyada puritanlar deb atalgan.")
t.B("Angliya burjua inqilobi qachon boshlangan?", "1640-yilda", "1603-yilda", "1649-yilda", "1688-yilda", "Inqilob 1640-yili boshlandi.")
t.B("1640-yilda yig‘ilgan parlament qanday nom bilan tarixga kirgan?", "«Uzoq muddatli parlament»", "«Qisqa parlament»", "«Sharafli parlament»", "«Lordlar palatasi»", "U «Uzoq muddatli parlament» nomini oldi.")
t.B("Parlament g‘alabasida qaysi qo‘mondon otliqlari asosiy rol o‘ynagan?", "Oliver Kromvel", "Karl I", "Villem van Oranye", "Jon Lilbern", "Oliver Kromvel qo‘mondonligidagi otliqlar.")
t.B("Angliya qachon respublika deb e’lon qilingan?", "1649-yil 19-mayda", "1640-yilda", "1660-yilda", "1688-yilda", "1649-yil 19-may kuni respublika e’lon qilindi.")
t.B("«Protektor» so‘zi qanday ma’noni bildiradi?", "homiy, himoyachi", "qirol", "sudya", "lord", "Protektor – homiy, himoyachi.")
t.B("1688-yilda Angliya taxtiga kim taklif etilgan?", "Villem van Oranye", "Karl II", "Georg I", "Yakov II", "Gollandiya shahzodasi Villem van Oranye.")
t.B("1688-yilgi o‘zgarish tarixda qanday nom olgan?", "«Sharafli inqilob»", "«Uzoq parlament»", "«Restavratsiya»", "«Protektorat»", "Bu «Sharafli inqilob» nomini oldi.")
t.B("Mamlakat qachondan Buyuk Britaniya deb atala boshlagan?", "1707-yildan", "1688-yildan", "1714-yildan", "1649-yildan", "1707-yili Angliya–Shotlandiya uniyasi qonuniylashtirildi.")
t.B("1714-yildan Angliya taxtiga qaysi sulola vakili taklif qilingan?", "gannoverlik Georg I", "Villem van Oranye", "Yakov II", "Karl II", "Gannoverlik Georg I taklif qilindi.")
t.NAT("1688-yilgi «Sharafli inqilob» yuz berdi.", "qirol hokimiyati cheklanib, konstitutsion monarxiya o‘rnatildi", "absolutizm kuchaydi", "respublika e’lon qilindi", "katoliklik tiklandi",
      "Eng muhim masalalarni parlament hal qiladigan bo‘ldi.")
t.NAT("Qirol armiyasi tor-mor qilindi.", "zodagonlar feodal soliqlardan ozod qilinib, yer ularning xususiy mulkiga aylandi", "qirol yerlari ko‘paydi", "cherkov kuchaydi", "savdo cheklandi",
      "Parlament islohoti zodagonlarni feodal soliqlardan ozod qildi.")
t.TF("Angliya burjua inqilobi dehqonlarni yerning to‘liq egalariga aylantirgan.", False, "Noto‘g‘ri: inqilob tugallanmay qoldi, dehqonlarni yer egasiga aylantirmadi.")
t.TF("Kromvel armiyasi Irlandiya va Shotlandiyaga bostirib kirgan.", True, "To‘g‘ri.")
t.MUL([("XVIII asrda parlament lordlar va jamoa palatalaridan iborat bo‘lgan.", True), ("1643-yil oxiriga kelib mamlakatning 3/4 qismi qirol qo‘lida edi.", True), ("Styuartlar fransuz sulolasi bo‘lgan.", False)],
      "III noto‘g‘ri: styuartlar shotlandiyalik edi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Yelizaveta I hokimiyatga keldi", "Styuartlar taxtga chiqdi", "Uzoq muddatli parlament yig‘ildi", "Respublika e’lon qilindi", "«Sharafli inqilob»", "Buyuk Britaniya tuzildi"],
      "1558 → 1603 → 1640 → 1649 → 1688 → 1707.")
t.MAPMATCH(EU, ['Angliya', 'Shotlandiya', 'Irlandiya', 'Gollandiya'],
           ["burjua inqilobi bo‘lgan mamlakat", "styuartlar vatani, 1707-yilda uniyaga kirgan", "Kromvel armiyasi bosib olgan orol", "Villem van Oranye vatani"],
           "1 – Angliya; 2 – Shotlandiya; 3 – Irlandiya; 4 – Gollandiya.")
t.VENN("Absolutizm", "Konstitutsion monarxiya",
       [("monarx hokimiyati cheklanmagan", 1), ("Genrix VIII davrida kuchaygan", 1),
        ("qirol hokimiyatini parlament cheklagan", 2), ("1688-yildan Angliyada o‘rnatilgan", 2),
        ("monarxiya shakli", 3)],
       "Absolutizm – cheksiz; konstitutsion – parlament cheklaydi. Ikkalasi monarxiya.")

# 6 Xalqaro munosabatlar XVI–XVIII
t = Topic('e8j6', 806); TOPICS['e8j6'] = t
t.B("Avstriyadagi hukmron sulola qaysi?", "gabsburglar", "styuartlar", "burbonlar", "romanovlar", "Avstriyada gabsburglar sulolasi hukmron edi.")
t.B("Italiya urushlari natijasida Italiya kimga bo‘ysundirilgan?", "ispan qiroliga", "fransuz qiroliga", "turk sultoniga", "ingliz qiroliga", "Italiya ispan qiroliga bo‘ysundirildi.")
t.B("Gabsburglarga qarshi Fransiya va Angliya kim bilan yaxshi munosabat o‘rnatgan?", "Usmoniylar imperiyasi", "Rossiya", "Ispaniya", "Shvetsiya", "Ular Usmoniylar bilan yaxshi munosabat o‘rnatdi.")
t.B("O‘ttiz yillik urush qaysi yillarda bo‘lgan?", "1618–1648", "1700–1721", "1756–1763", "1768–1774", "O‘ttiz yillik urush 1618–1648-yillarda bo‘ldi.")
t.B("O‘ttiz yillik urush qanday sulh bilan yakunlangan?", "Vestfal sulhi", "Kuchukqaynarji", "Utrext", "Parij sulhi", "1648-yili Vestfal sulhi bilan yakunlandi.")
t.B("Vestfal sulhiga ko‘ra qaysi mamlakatning Ispaniyadan mustaqilligi tan olingan?", "Gollandiya", "Portugaliya", "Italiya", "Shveysariya", "Gollandiyaning mustaqilligi tan olindi.")
t.B("Ispaniya qiroli Karl II qachon vafot etgan?", "1700-yilda", "1714-yilda", "1648-yilda", "1756-yilda", "1700-yili Karl II vafot etdi.")
t.B("Karl II vasiyatiga ko‘ra Ispaniya taxtiga kim o‘tirgan?", "Filipp Anjuy", "Lyudovik XIV", "Karl Gabsburg", "Villem van Oranye", "Fransiya qirolining nabirasi Filipp Anjuy.")
t.B("Rossiya va Shvetsiya o‘rtasidagi Shimoliy urush qaysi yillarda bo‘lgan?", "1700–1721", "1618–1648", "1756–1763", "1768–1774", "Shimoliy urush 1700–1721-yillarda bo‘ldi.")
t.B("Yetti yillik urush qaysi yillarda bo‘lgan?", "1756–1763", "1700–1721", "1618–1648", "1768–1774", "Yetti yillik urush 1756–1763-yillarda.")
t.B("Yetti yillik urushdan eng katta foydani kim olgan?", "Angliya", "Fransiya", "Ispaniya", "Avstriya", "Hindiston va Shimoliy Amerikadagi fransuz mustamlakalari Angliyaga o‘tdi.")
t.B("1768-yilda Rossiyaga qarshi urush boshlagan Usmoniy sultoni kim?", "Mustafo III", "Sulaymon I", "Salim III", "Mahmud II", "Sulton Mustafo III 1768-yili urush boshladi.")
t.B("1768–1774-yillardagi urush qanday shartnoma bilan yakunlangan?", "Kuchukqaynarji", "Vestfal", "Utrext", "Nishtadt", "1774-yili Kuchukqaynarji shartnomasi imzolandi.")
t.NAT("Vestfal sulhi imzolandi (1648).", "katolik va protestant cherkovlarining tengligi tan olindi", "Germaniya birlashdi", "protestantlik taqiqlandi", "Fransiya zaiflashdi",
      "Sulh katolik va protestantlar dushmanligiga barham berdi.")
t.NAT("Ispaniya taxti uchun urushda fransuzlar ham, gabsburglar ham kuchsizlandi.", "Angliya kuchaydi", "Ispaniya kuchaydi", "Usmoniylar Venani oldi", "Gollandiya qulab tushdi",
      "Bu Angliyaning kuchayishiga olib keldi.")
t.NAT("Kuchukqaynarji shartnomasi imzolandi (1774).", "Qrim xonligi Rossiyaga qaram bo‘lib, Rossiya Qora dengizda flotga ega bo‘ldi", "Usmoniylar Qrimni qo‘shib oldi", "Rossiya Qora dengizdan voz kechdi", "Avstriya Qrimni oldi",
      "Rossiya Qora dengizda harbiy flot huquqini oldi.")
t.TF("O‘ttiz yillik urush asosan Germaniya hududida olib borilgan.", True, "To‘g‘ri.")
t.TF("Yetti yillik urush natijasida Yevropa chegaralari tubdan o‘zgargan.", False, "Noto‘g‘ri: Yevropadagi chegaralar o‘zgarmadi.")
t.MUL([("1714-yilgi sulhga ko‘ra Filipp Anjuy Fransiya taxtiga huquqidan voz kechgan.", True), ("Shimoliy urushda Rossiya g‘alaba qozongan.", True), ("Vestfal sulhidan keyin Germaniya yagona markazlashgan davlatga aylangan.", False)],
      "III noto‘g‘ri: Germaniya tarqoq knyazliklardan iborat bo‘lib qolaverdi.")
t.MATCH("Urushlarni yakunlagan hujjat yoki natija bilan moslashtiring.", ["O‘ttiz yillik urush", "Ispaniya taxti uchun urush", "Rus-turk urushi (1768–1774)"],
        ["Vestfal sulhi (1648)", "1714-yilgi sulh", "Kuchukqaynarji shartnomasi", "Parij sulhi (1763)"], 'abc', "1648 Vestfal; 1714 sulh; 1774 Kuchukqaynarji.")
t.CHR("Urushlarni xronologik ketma-ketlikda joylashtiring.", ["O‘ttiz yillik urush", "Shimoliy urush", "Yetti yillik urush", "Rus-turk urushi (Mustafo III)"],
      "1618 → 1700 → 1756 → 1768.")
t.MAPMATCH(EU, ['Vestfaliya (Myunster)', 'Shvetsiya', 'Kuchukqaynarji', 'Ispaniya'],
           ["1648-yilgi sulh nomini bergan hudud", "Shimoliy urushda Rossiyaga qarshi kurashgan davlat", "1774-yilgi shartnoma imzolangan joy", "1700-yildan taxti uchun urush boshlangan davlat"],
           "1 – Vestfaliya; 2 – Shvetsiya; 3 – Kuchukqaynarji; 4 – Ispaniya.")
t.VENN("O‘ttiz yillik urush", "Yetti yillik urush",
       [("diniy mojaro sifatida boshlangan", 1), ("Vestfal sulhi bilan tugagan", 1),
        ("Angliya Hindiston va Amerikadagi fransuz mustamlakalarini olgan", 2), ("Yevropa chegaralari o‘zgarmagan", 2),
        ("ko‘plab Yevropa davlatlari qatnashgan", 3)],
       "30 yillik: diniy, Vestfal. 7 yillik: mustamlakalar Angliyaga. Ikkalasida ko‘p davlat qatnashgan.")

# 7 Fransuz inqilobi
t = Topic('e8j7', 807); TOPICS['e8j7'] = t
t.B("General shtatlar majlisi qachon ochilgan?", "1789-yil 5-mayda", "1789-yil 14-iyulda", "1791-yil sentabrda", "1792-yil 22-sentabrda", "1789-yil 5-may kuni Lyudovik XVI General shtatlar majlisini ochdi.")
t.B("General shtatlarni ochgan qirol kim?", "Lyudovik XVI", "Lyudovik XIV", "Karl X", "Filipp Anjuy", "Qirol Lyudovik XVI.")
t.B("Uchinchi tabaqa deputatlari o‘z yig‘ilishini qanday deb e’lon qilgan?", "Milliy kengash", "Konvent", "Direktoriya", "Kommuna", "Ular yig‘ilishni Milliy kengash deb e’lon qildi.")
t.B("Uchinchi tabaqa qarashlarining ifodachisi kim bo‘lgan?", "Gabriel de Mirabo", "Robespyer", "Marat", "Danton", "Gabriel de Mirabo uchinchi tabaqani birlikka chaqirdi.")
t.B("Birinchi tabaqani kimlar tashkil etgan?", "ruhoniylar", "dvoryanlar", "dehqonlar", "burjuaziya", "Birinchi tabaqa – ruhoniylar, ikkinchi – dvoryanlar.")
t.B("Bastiliya qal’asi qachon egallangan?", "1789-yil 14-iyulda", "1789-yil 5-mayda", "1792-yil 22-sentabrda", "1793-yil yanvarda", "1789-yil 14-iyulda Bastiliya egallandi.")
t.B("Poytaxtda hokimiyat qaysi organ qo‘liga o‘tgan?", "Parij Kommunasi", "Konvent", "Direktoriya", "General shtatlar", "Hokimiyat shahar kengashi – Parij Kommunasi qo‘liga o‘tdi.")
t.B("«Inson va fuqaro huquqlari deklaratsiyasi» mohiyati qaysi shiorda ifodalangan?", "«Ozodlik, Tenglik, Birodarlik!»", "«Vatan xavf ostida!»", "«Xalq, uyg‘on!»", "«Kuchli hokimiyat!»", "Mohiyat «Ozodlik, Tenglik, Birodarlik!» so‘zlarida.")
t.B("Fransiyaning ilk konstitutsiyasi qachon qabul qilingan?", "1791-yil sentabrda", "1789-yilda", "1795-yilda", "1792-yilda", "1791-yil sentabrda Ta’sis majlisi ilk konstitutsiyani qabul qildi.")
t.B("Qirol tarafdorlari bo‘lgan deputatlar qanday atalgan?", "royalistlar", "jirondachilar", "yakobinchilar", "termidorchilar", "O‘nglar yoki royalistlar (royal – qirol).")
t.B("Ko‘pchiligi Jironda viloyatidan saylangan so‘l deputatlar qanday atalgan?", "jirondachilar", "yakobinchilar", "royalistlar", "termidorchilar", "Ular jirondachilar degan nom oldi.")
t.B("Yakobinchilar nomi nimadan kelib chiqqan?", "Avliyo Yakob monastiri kutubxonasida yig‘ilganidan", "Yakob ismli rahbaridan", "Yakob shahridan", "qirol Yakovdan", "Ular Avliyo Yakob monastiri kutubxonasida yig‘ilgan.")
t.B("Fransuz qo‘shinlari pruss hujumini qaysi qishloq yaqinida qaytargan?", "Valmi", "Versal", "Vorms", "Vaterloo", "Valmi qishlog‘i yaqinidagi jangda.")
t.B("Fransiyada respublika qachon e’lon qilingan?", "1792-yil 22-sentabrda", "1789-yil 14-iyulda", "1793-yil yanvarda", "1794-yil 27-iyulda", "1792-yil 22-sentabrda Konvent respublika dekretini qabul qildi.")
t.B("Lyudovik XVI qachon qatl qilingan?", "1793-yil yanvarda", "1792-yilda", "1794-yilda", "1789-yilda", "1793-yil yanvarda qirol qatl qilindi.")
t.B("Robespyer qachon qamoqqa olingan?", "1794-yil 27-iyulda", "1793-yil yanvarda", "1795-yil aprelda", "1792-yilda", "1794-yil 27-iyulda Robespyer qamoqqa olindi.")
t.NAT("Qonun chiqaruvchi majlis «Vatan xavf ostida!» deb xalqqa murojaat qildi.", "fransuz qo‘shinlari Valmida prusslarni qaytarib, ozodlik boshlandi", "Fransiya taslim bo‘ldi", "qirol hokimiyati kuchaydi", "Angliya ittifoqchi bo‘ldi",
      "Valmi jangi mamlakatni ozod qilishning boshlanishi bo‘ldi.")
t.NAT("Lyudovik XVI qatl qilindi.", "Angliya va Ispaniya Fransiyaga qarshi urushga kirdi", "urushlar to‘xtadi", "monarxiya tiklandi", "Avstriya sulh tuzdi",
      "Qirolning qatli Angliya va Ispaniyani urushga chorladi.")
t.TF("Yakobinchilar shafqatsiz terror boshqaruvini o‘rnatgan.", True, "To‘g‘ri.")
t.TF("1791-yilgi konstitutsiya bilan qirol hokimiyati butunlay bekor qilingan.", False, "Noto‘g‘ri: qirol hokimiyati cheklandi; monarxiya 1792-yilda ag‘darildi.")
t.MUL([("Inqilob arafasida Fransiya aholi soni bo‘yicha Yevropaning eng katta davlati edi.", True), ("Respublika davrida 25 yoshga to‘lgan barcha erkaklarga saylov huquqi berilgan.", True), ("Bastiliya olingach, qirol Ta’sis majlisini tan olmagan.", False)],
      "III noto‘g‘ri: qirol yon berib, Ta’sis majlisini tan oldi.")
t.MATCH("Siyosiy oqimlarni izohi bilan moslashtiring.", ["Royalistlar", "Jirondachilar", "Yakobinchilar"],
        ["qirol tarafdorlari", "Jironda viloyatidan saylangan so‘llar", "Robespyer boshchiligidagi o‘ta so‘llar", "termidorchilar"], 'abc', "Royalistlar – qirol; jirondachilar – Jironda; yakobinchilar – o‘ta so‘l.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["General shtatlar ochildi", "Bastiliya olindi", "Ilk konstitutsiya qabul qilindi", "Respublika e’lon qilindi", "Qirol qatl qilindi", "Robespyer qamoqqa olindi"],
      "1789 may → 1789 iyul → 1791 → 1792 → 1793 → 1794.")
t.VENN("Jirondachilar", "Yakobinchilar",
       [("ko‘pchiligi Jironda viloyatidan", 1), ("deputatlari qatl qilingan", 1),
        ("Robespyer, Marat, Danton boshchiligida", 2), ("terror boshqaruvini o‘rnatgan", 2),
        ("fransuz inqilobidagi siyosiy oqim", 3)],
       "Jirondachilar: Jironda, qatl etilgan. Yakobinchilar: Robespyer, terror. Ikkalasi inqilob oqimi.")
t.MAPMATCH(EU, ['Parij', 'Valmi', 'Belgiya', 'Avstriya'],
           ["Bastiliya joylashgan poytaxt", "1792-yilda prusslar to‘xtatilgan joy", "fransuzlar qo‘shin kiritgan hudud", "1792-yilda Fransiya urush e’lon qilgan davlat"],
           "1 – Parij; 2 – Valmi; 3 – Belgiya; 4 – Avstriya.")

# 8 Inqilobning yakunlanishi
t = Topic('e8j8', 808); TOPICS['e8j8'] = t
t.B("Termidorchilar qanday respublika tarafdori bo‘lgan?", "mulk va erkin tadbirkorlikni himoya qiluvchi", "yakobinchilar diktaturasi", "monarxiya", "teokratik", "Termidorchilar mulk va erkin tadbirkorlik himoyachisi edi.")
t.B("Termidor nima?", "fransuz inqilobiy taqvimidagi oy nomi", "qal’a nomi", "partiya nomi", "shahar nomi", "Termidor – yangi taqvimdagi oy nomi.")
t.B("1795-yilgi xalq qo‘zg‘oloni qachon boshlangan?", "1795-yil aprelda", "1795-yil avgustda", "1794-yil iyulda", "1799-yil noyabrda", "1795-yil aprelda qo‘zg‘olon boshlandi.")
t.B("1795-yilgi Konstitutsiya qachon qabul qilingan?", "1795-yil avgustda", "1795-yil aprelda", "1791-yil sentabrda", "1799-yilda", "1795-yilning avgustida qabul qilindi.")
t.B("1795-yilgi Konstitutsiyaga ko‘ra ijro hokimiyati nimaga topshirilgan?", "besh kishilik Direktoriyaga", "Konventga", "uch konsulga", "qirolga", "Ijro hokimiyati besh kishidan iborat Direktoriyaga berildi.")
t.B("1795-yilgi qonunchilik palatasi qaysi kengashlardan iborat bo‘lgan?", "Besh yuzlar kengashi va Oqsoqollar kengashi", "Lordlar va jamoa palatasi", "Konvent va Kommuna", "Senat va Duma", "Ikki palata – Beshyuzlar va Oqsoqollar kengashlari.")
t.B("Monarxiya tarafdorlari isyonini artilleriya bilan bostirgan general kim?", "Napoleon Bonapart", "Robespyer", "Danton", "Mirabo", "General Napoleon Bonapart Konvent xaloskoriga aylandi.")
t.B("Direktoriya davrida Fransiyaga qo‘shib olingan hududlar qaysi?", "Reynning so‘l qirg‘og‘i va Belgiya", "Italiya va Ispaniya", "Gollandiya va Angliya", "Misr va Suriya", "Reynning so‘l qirg‘og‘i va Belgiya qo‘shib olindi.")
t.B("Napoleonning Misrga yurishi qachon bo‘lgan?", "1798-yilda", "1795-yilda", "1799-yilda", "1804-yilda", "1798-yilda Misrga yurish qilindi.")
t.B("Davlat to‘ntarishi qachon yuz bergan?", "1799-yil 9-noyabrda", "1795-yil avgustda", "1798-yilda", "1794-yil 27-iyulda", "1799-yil 9-noyabr davlat to‘ntarishi.")
t.B("1799-yilgi to‘ntarishdan so‘ng qanday boshqaruv o‘rnatilgan?", "Konsullik (uch konsul)", "Direktoriya", "Konvent", "Imperiya", "Uch kishilik Konsullik tasdiqlandi.")
t.NAT("Termidorchilar savdodagi cheklashlarni bekor qildi.", "narxlar ko‘tarilib, pul keskin qadrsizlandi", "narxlar tushdi", "xalq boyidi", "savdo to‘xtadi",
      "Savdo erkinligi boshlanib, narxlar oshdi, pul qadrsizlandi.")
t.NAT("1795-yil may qo‘zg‘oloni bostirildi.", "so‘nggi yakobinchilar gilotinada qatl qilindi", "yakobinchilar hokimiyatga qaytdi", "qirollik tiklandi", "Konvent tarqatildi",
      "Yo‘lboshchilar – so‘nggi yakobinchilar qatl etildi.")
t.NAT("Direktoriya xalq orasida obro‘ga ega emasdi.", "fitnachilar Napoleondan foydalanib, Konsullik o‘rnatdi", "Direktoriya kuchaydi", "monarxiya tiklandi", "yakobinchilar qaytdi",
      "1799-yil 9-noyabr to‘ntarishi Konsullikni o‘rnatdi.")
t.TF("1795-yilgi Konstitutsiya umumiy saylov huquqini bekor qilgan.", True, "To‘g‘ri.")
t.TF("Direktoriya davridagi urushlar faqat mudofaa xarakterida bo‘lgan.", False, "Noto‘g‘ri: ular bosqinchilik xarakteriga ega bo‘ldi.")
t.MUL([("Gollandiya qaram respublikaga aylantirilgan.", True), ("Napoleon bosib olingan yerlarda feodal qaramlikni yo‘q qilgan.", True), ("1795-yilgi qo‘zg‘olonchilar g‘alaba qozonib, hokimiyatni olgan.", False)],
      "III noto‘g‘ri: qo‘zg‘olonchilar tor-mor qilindi.")
t.MATCH("Atamalarni izohi bilan moslashtiring.", ["Konvent", "Direktoriya", "Konsul", "Terror"],
        ["alohida vakolatli vakillik organi", "kollegial ijroiya hokimiyati", "uchta ijroiya rahbaridan biri", "raqiblarni yo‘qotish, qo‘rqitish", "mahalliy o‘zini o‘zi boshqarish organi"], 'abcd',
        "Konvent – vakillik; Direktoriya – ijroiya; konsul – rahbar; terror – qo‘rqitish.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Robespyer hokimiyatdan ag‘darildi", "1795-yil aprel qo‘zg‘oloni", "1795-yilgi Konstitutsiya", "Misrga yurish", "9-noyabr davlat to‘ntarishi"],
      "1794 → 1795 aprel → 1795 avgust → 1798 → 1799.")
t.MAPMATCH('mideast', ['Fransiya', 'Italiya', 'Misr'],
           ["inqilob bo‘lgan mamlakat", "Napoleon yurishi uni mashhur qilgan mamlakat", "1798-yilda Napoleon yurish qilgan mamlakat"], "1 – Fransiya; 2 – Italiya; 3 – Misr.")
t.VENN("Direktoriya", "Konsullik",
       [("besh kishidan iborat", 1), ("1795-yilgi Konstitutsiya asosida", 1),
        ("uch kishidan iborat", 2), ("1799-yil 9-noyabr to‘ntarishidan keyin", 2),
        ("Fransiyadagi ijroiya hokimiyati", 3)],
       "Direktoriya – 5 kishi, 1795. Konsullik – 3 kishi, 1799. Ikkalasi ijroiya hokimiyati.")
