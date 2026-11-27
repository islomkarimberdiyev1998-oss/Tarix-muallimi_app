from qlib import Topic, PLACES, REG
TOPICS = {}
G2 = 'globe2'; EU = 'europe'

# 17 AQSH: yangi lider
t = Topic('y10j17', 10017); TOPICS['y10j17'] = t
t.B("Urush yillarida AQSH eksport hajmi necha barobar o‘sgan?", "besh barobar", "ikki barobar", "o‘n barobar", "uch barobar", "Ishlab chiqarish quvvatlari ikki, eksport besh, YaMM ikki barobar o‘sdi.")
t.B("1952-yilgi saylovlarda qaysi partiya g‘alaba qozongan?", "respublikachilar partiyasi", "demokratik partiya", "leyboristlar", "konservatorlar", "1932-yildan beri muxolifatda bo‘lgan respublikachilar.")
t.B("1952-yilda AQSH prezidenti etib kim saylangan?", "Duayt Eyzenhauer", "Jon Kennedi", "Lindon Jonson", "Richard Nikson", "General Duayt Eyzenhauer.")
t.B("Eyzenhauer urush yillarida qanday lavozimda bo‘lgan?", "AQSHning Yevropadagi qo‘shinlari qo‘mondoni", "davlat kotibi", "vitse-prezident", "senator", "AQSHning Yevropadagi qo‘shinlari qo‘mondoni.")
t.B("1960-yilgi prezidentlik saylovlarida kim g‘olib chiqqan?", "Jon Kennedi", "Richard Nikson", "Duayt Eyzenhauer", "Jimmi Karter", "Demokratik partiya nomzodi Jon Kennedi.")
t.B("J. Kennedining islohotchilik dasturi qanday atalgan?", "«Yangi marralar»", "«Yangi kurs»", "«Reyganomika»", "«Yangi erkinlik»", "«Yangi marralar» dasturi.")
t.B("J. Kennedi qachon o‘ldirilgan?", "1963-yil 22-noyabrda", "1968-yil 4-aprelda", "1964-yilda", "1960-yilda", "1963-yil 22-noyabrda.")
t.B("J. Kennedi qaysi shaharda o‘ldirilgan?", "Dallasda", "Memfisda", "Vashingtonda", "Nyu-Yorkda", "Texas shtatining Dallas shahrida.")
t.B("1964-yilgi saylovlarda kim g‘alaba qozongan?", "Lindon Jonson", "Jon Kennedi", "Richard Nikson", "Jorj Bush", "Lindon Jonson.")
t.B("1960-yillarda AQSHdagi ommaviy norozilik harakatining asosiy sababi nima edi?", "afroamerikaliklarning kamsitilishi", "Vyetnamdagi g‘alaba", "inflyatsiya", "soliqlar kamayishi", "Afroamerikaliklarning kamsitilishi.")
t.B("Martin Lyuter King qachon o‘ldirilgan?", "1968-yil 4-aprelda", "1963-yil 22-noyabrda", "1973-yilda", "1979-yilda", "1968-yil 4-aprel kuni Memfisda.")
t.B("Martin Lyuter King qaysi mukofot laureati bo‘lgan?", "tinchlik bo‘yicha Nobel mukofoti", "adabiyot bo‘yicha Nobel mukofoti", "Pulitser mukofoti", "Oskar mukofoti", "Tinchlik bo‘yicha Nobel mukofoti laureati.")
t.B("1968-yilgi saylovlarda AQSH prezidenti etib kim saylangan?", "Richard Nikson", "Jimmi Karter", "Lindon Jonson", "Ronald Reygan", "Respublikachi Richard Nikson.")
t.B("R. Nikson «yangi iqtisodiy siyosat»ni qachon e’lon qilgan?", "1971-yilda", "1968-yilda", "1976-yilda", "1980-yilda", "1971-yili.")
t.B("AQSH mustaqilligining 200 yilligini qachon nishonlagan?", "1976-yilda", "1973-yilda", "1980-yilda", "1988-yilda", "1976-yili.")
t.B("1976-yilgi saylovlarda kim g‘alaba qozongan?", "Jimmi Karter", "Ronald Reygan", "Richard Nikson", "Jorj Bush", "Demokrat Jimmi Karter.")
t.B("Karter davrida AQSH obro‘yiga berilgan katta zarbalardan biri nima bo‘lgan?", "1979-yilgi Eron inqilobi", "Kennedining o‘ldirilishi", "Vyetnamdagi g‘alaba", "Koreya urushi", "1979-yilgi Eron inqilobi.")
t.B("R. Reyganning ijtimoiy-iqtisodiy dasturi qanday nom bilan mashhur?", "«Reyganomika»", "«Yangi marralar»", "«Tetcherizm»", "«Yangi kurs»", "«Reyganomika».")
t.B("1988-yilgi prezidentlik saylovlarida kim g‘alaba qozongan?", "Jorj Bush", "Ronald Reygan", "Jimmi Karter", "Bill Klinton", "Respublikachi Jorj Bush.")
t.B("Vyetnamdagi urush qachon to‘xtatilgan?", "1973-yilda", "1968-yilda", "1976-yilda", "1963-yilda", "1973-yili; Vyetnam yagona davlatga birlashdi.")
t.NAT("1968-yil 4-aprelda Martin Lyuter King o‘ldirildi.", "dafn marosimi afroamerikaliklarga nisbatan zo‘ravonlikka qarshi namoyishga aylandi", "fuqarolar tengligi harakati to‘xtadi", "Nikson iste’foga chiqdi", "Vyetnam urushi tugadi", "Ko‘mish marosimi norozilik namoyishiga aylandi.")
t.NAT("Reygan iqtisodiy tushkunlikni yengdi, ishsizlikni qisqartirdi, daromad solig‘ini pasaytirdi.", "1984-yili ikkinchi muddatga prezident etib saylandi", "iste’foga chiqdi", "demokratlar Senatda ko‘pchilikni oldi", "inflyatsiya keskin oshdi", "Bu omillar uning qayta saylanishini ta’minladi.")
t.NAT("1980-yillar oxiri – 1990-yillar boshida sovuq urush tugadi, SSSR tarqaldi.", "AQSH dunyoning yagona tan olingan yetakchisiga aylandi", "AQSH izolyatsiyaga o‘tdi", "AQSH ta’siri pasaydi", "ikki qutbli dunyo kuchaydi", "Bir qutbli dunyo tartibi haqidagi fikr paydo bo‘ldi.")
t.TF("Eyzenhauer ma’muriyati ijtimoiy sohada demokratlar siyosatini biroz o‘zgarishlar bilan davom ettirgan.", True, "To‘g‘ri.")
t.TF("Jimmi Karter saylovoldi va’dalarining barchasini muvaffaqiyatli bajargan.", False, "Noto‘g‘ri: ko‘pchiligini bajarishga erisha olmadi.")
t.MUL([("Urush yillari AQSHning yalpi milliy mahsuloti ikki barobar o‘sgan.", True),
       ("1980-yilgi saylovlarda demokratlar Senat va Vakillar palatasida ko‘plab o‘rinlaridan ajralgan.", True),
       ("Vyetnam urushi AQSHning Janubi-sharqiy Osiyodagi g‘alabasi bilan tugagan.", False)],
      "III noto‘g‘ri: bu Amerika tajovuzining to‘liq mag‘lubiyatini anglatardi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Eyzenhauer saylandi", "Kennedi saylandi", "Kennedi o‘ldirildi", "Martin Lyuter King o‘ldirildi", "Vyetnam urushi to‘xtatildi", "Eron inqilobi"],
      "1952 → 1960 → 1963 → 1968 → 1973 → 1979.")
t.MATCH("Prezidentlarni ularga oid ma’lumot bilan moslashtiring.", ["Jon Kennedi", "Richard Nikson", "Jimmi Karter", "Ronald Reygan"],
        ["«Yangi marralar» dasturi", "1971-yilda «yangi iqtisodiy siyosat»", "1976-yilda saylangan demokrat", "«Reyganomika»", "«Yangi erkinlik» dasturi"], 'abcd',
        "Kennedi – «Yangi marralar»; Nikson – 1971; Karter – 1976; Reygan – «Reyganomika».")
t.VENN("Eyzenhauer", "Kennedi",
       [("respublikachi", 1), ("urush yillari Yevropadagi qo‘shinlar qo‘mondoni", 1),
        ("demokrat", 2), ("Dallasda o‘ldirilgan", 2),
        ("AQSH prezidenti", 3)],
       "Eyzenhauer – respublikachi, qo‘mondon; Kennedi – demokrat, Dallas; ikkalasi prezident.")
t.MAPMATCH(G2, ['Dallas', 'Vyetnam', 'Eron', 'Koreya'],
           ["1963-yilda Kennedi o‘ldirilgan shahar", "1973-yilda urush to‘xtatilib, yagona davlatga birlashgan mamlakat", "1979-yildagi inqilobi AQSH obro‘siga zarba bo‘lgan mamlakat", "Vyetnamdan tashqari AQSH urush olib borgan Osiyo hududi"],
           "1 – Dallas; 2 – Vyetnam; 3 – Eron; 4 – Koreya.")

# 18 Buyuk Britaniya va Fransiya
t = Topic('y10j18', 10018); TOPICS['y10j18'] = t
t.B("Britaniyada sanoat ishlab chiqarishi qachon urushdan oldingi darajaga yetgan?", "1947-yil oxirida", "1945-yilda", "1950-yilda", "1960-yilda", "1947-yil oxiriga kelib.")
t.B("Britaniya iqtisodiyoti o‘sishiga qaysi hukumat siyosati ta’sir ko‘rsatgan?", "leyboristlar hukumati davlat sektorini kengaytirgani", "konservatorlarning xususiylashtirishi", "Tetcherning inflyatsiyaga qarshi kursi", "Cherchillning harbiy islohoti", "Leyboristlar davlat sektorini ancha kengaytirdi.")
t.B("1960-yillar o‘rtalarida Britaniyani ikkinchi o‘rindan qaysi davlat surib chiqargan?", "GFR", "Yaponiya", "Fransiya", "Italiya", "GFR ikkinchi, 1970-yillar boshida Yaponiya uchinchi o‘rindan surdi.")
t.B("Britaniya tarixida birinchi marta hukumatni ayol kishi qachon boshqargan?", "1979-yilda", "1990-yilda", "1982-yilda", "1970-yilda", "1979-yili Margaret Tetcher.")
t.B("Konservatorlar kursi asoslari aks etgan dasturiy hujjat qanday atalgan?", "«To‘g‘ri yondashuv»", "«Yangi marralar»", "«Yangi kurs»", "«Umumiy farovonlik»", "«To‘g‘ri yondashuv».")
t.B("«Tetcherizm» o‘zining asosiy maqsadi qilib nimaga qarshi kurashni tanlagan?", "inflyatsiyaga", "ishsizlikka", "kasaba uyushmalariga", "AQSHga", "Ishsizlikka emas, inflyatsiyaga qarshi kurash.")
t.B("Folklend orollari voqealari qachon yuz bergan?", "1982-yilda", "1979-yilda", "1990-yilda", "1968-yilda", "1982-yili.")
t.B("Folklend orollari ustidan suverenitet o‘rnatishga qaysi davlat uringan?", "Argentina", "Braziliya", "Chili", "Ispaniya", "Argentina.")
t.B("1990-yilgi saylovlarda Britaniya bosh vaziri etib kim saylangan?", "Jon Meyjor", "Margaret Tetcher", "Tony Bler", "Harold Vilson", "Jon Meyjor; «tetcherizm» davri tugadi.")
t.B("Ikkinchi jahon urushida Fransiya qancha kishisidan ayrilgan?", "3 mln", "1 mln", "600 ming", "13 mln", "Urush, ocharchilik va kasalliklar tufayli 3 mln.")
t.B("1945-yilda Fransiyada koalitsion hukumatni kim boshqargan?", "general Sharl de Goll", "Jorj Pompidu", "Fransua Mitteran", "Jak Shirak", "General Sharl de Goll.")
t.B("To‘rtinchi respublika konstitutsiyasiga ko‘ra prezident necha yil muddatga saylangan?", "7 yil", "5 yil", "4 yil", "umrbod", "Parlament 5 yilga, prezident 7 yilga saylanardi.")
t.B("To‘rtinchi respublika qaysi yillarda mavjud bo‘lgan?", "1946–1958-yillarda", "1870–1940-yillarda", "1958–1969-yillarda", "1945–1950-yillarda", "O‘n ikki yil (1946–1958).")
t.B("1958-yil sentabrdagi referendumdan so‘ng Fransiya qanday respublikaga aylangan?", "prezidentlik respublikasiga", "parlament respublikasiga", "sovet respublikasiga", "konstitutsion monarxiyaga", "Prezidentlik respublikasiga (Beshinchi respublika).")
t.B("Jazoirga qachon mustaqillik berilgan?", "1962-yilda", "1958-yilda", "1960-yilda", "1968-yilda", "1962-yili; fransuz mustamlaka imperiyasi to‘liq barham topdi.")
t.B("1969-yil oxirida Fransiya prezidenti etib kim saylangan?", "Jorj Pompidu", "Fransua Mitteran", "Sharl de Goll", "Jak Shirak", "Jorj Pompidu.")
t.B("Fransiyada birinchi marta sotsialist prezident qachon saylangan?", "1981-yilda", "1969-yilda", "1986-yilda", "1988-yilda", "1981-yili Fransua Mitteran.")
t.B("1986-yilgi parlament saylovlaridan so‘ng bosh vazir lavozimini kim egallagan?", "Jak Shirak", "Jorj Pompidu", "Fransua Mitteran", "Jon Meyjor", "O‘ng kuchlar vakili Jak Shirak.")
t.B("Xususiy mulkni davlat mulkiga aylantirish nima deb ataladi?", "natsionalizatsiya", "privatizatsiya", "inflyatsiya", "integratsiya", "Natsionalizatsiya.")
t.NAT("1982-yili Argentina Folklend orollari ustidan suverenitet o‘rnatishga urindi.", "Britaniya harbiy eskadra jo‘natdi va iyunda Argentina qo‘shinlari taslim bo‘ldi", "orollar Argentinaga o‘tdi", "BMT orollarni bo‘lib berdi", "Britaniya Argentinaga urush e’lon qilmay orollardan voz kechdi", "Iyunda Argentina qo‘shinlari taslim bo‘ldi.")
t.NAT("1968-yil mayda Parij talabalari namoyishi shafqatsiz bostirildi.", "mehnatkashlar ish tashlashlariga ulanib, De Goll iste’foga chiqdi", "De Goll umrbod prezident bo‘ldi", "Beshinchi respublika tugadi", "Mitteran prezident bo‘ldi", "De Goll iste’foga chiqishga majbur bo‘ldi.")
t.TF("1958–1960-yillarda Fransiyaning Afrikadagi mustamlakalari mustaqilligini e’lon qilgan.", True, "To‘g‘ri.")
t.TF("1981-yildan keyin sotsialistlar Fransiyada inflyatsiyani to‘liq to‘xtatgan.", False, "Noto‘g‘ri: inflyatsiyani to‘xtatishning iloji bo‘lmadi.")
t.MUL([("1950-yillarda Britaniya kapitalistik dunyoda AQSHdan keyin ikkinchi o‘rinda turgan.", True),
       ("1981-yildan so‘ng Fransiyada banklar va sanoatning ko‘plab sohalari natsionalizatsiya qilingan.", True),
       ("1988-yilgi prezidentlik saylovlarida Jak Shirak g‘alaba qozongan.", False)],
      "III noto‘g‘ri: 1988-yilda yana F. Mitteran g‘alaba qozondi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["To‘rtinchi respublika boshlandi", "Beshinchi respublika konstitutsiyasi ma’qullandi", "Jazoirga mustaqillik berildi", "Tetcher hukumat boshlig‘i bo‘ldi", "Folklend voqealari", "Jon Meyjor bosh vazir bo‘ldi"],
      "1946 → 1958 → 1962 → 1979 → 1982 → 1990.")
t.VENN("Margaret Tetcher", "Fransua Mitteran",
       [("konservator", 1), ("Folklend urushi davridagi hukumat boshlig‘i", 1),
        ("sotsialist", 2), ("banklarni natsionalizatsiya qilgan", 2),
        ("1980-yillarda o‘z mamlakatiga rahbarlik qilgan", 3)],
       "Tetcher – konservator, Folklend; Mitteran – sotsialist, natsionalizatsiya; ikkalasi 1980-yillar rahbari.")
t.MAPMATCH(G2, ['Folklend orollari', 'Argentina', 'Jazoir'],
           ["1982-yilda Britaniya va Argentina o‘rtasida voqealar bo‘lgan orollar", "bahsli orollar ustidan suverenitet o‘rnatishga uringan davlat", "1962-yilda Fransiya mustaqillik bergan mamlakat"],
           "1 – Folklend; 2 – Argentina; 3 – Jazoir.")

# 19 Germaniya va Italiya
t = Topic('y10j19', 10019); TOPICS['y10j19'] = t
t.B("Germaniya urushda qancha aholisidan ayrilgan?", "6,5 mln", "3 mln", "330 ming", "13 mln", "6,5 mln aholisidan ayrildi.")
t.B("G‘olib davlatlar Germaniya hududini nechta okkupatsiya zonasiga bo‘lgan?", "to‘rtta", "ikkita", "uchta", "beshta", "To‘rtta zonaga; Berlin ham to‘rtta sektorga bo‘lindi.")
t.B("Kommunistlar va sotsial-demokratlar birlashib qanday partiya tuzgan?", "Germaniya birlashgan sotsialistik partiyasi (GBSP)", "Xristian-demokratik ittifoqi", "Natsional-sotsialistik partiya", "Yashillar partiyasi", "GBSP.")
t.B("GFR qachon tashkil etilgan?", "1949-yil 7-sentabrda", "1949-yil 7-oktyabrda", "1955-yilda", "1990-yil 3-oktyabrda", "1949-yil 7-sentabrda.")
t.B("GFRning poytaxti qaysi shahar bo‘lgan?", "Bonn", "Berlin", "Myunxen", "Gamburg", "Bonn shahri.")
t.B("GFRning birinchi kansleri kim bo‘lgan?", "Konrad Adenauer", "Lyudvig Erhard", "Gelmut Kol", "Villi Brandt", "Konrad Adenauer.")
t.B("GDR qachon tashkil qilingan?", "1949-yil 7-oktyabrda", "1949-yil 7-sentabrda", "1945-yilda", "1955-yilda", "1949-yil 7-oktyabrda SSSR zonasida.")
t.B("GDRning poytaxti qaysi shahar deb e’lon qilingan?", "Sharqiy Berlin", "Bonn", "Drezden", "Leypsig", "Sharqiy Berlin.")
t.B("Germaniyaning ikki davlatga bo‘lingan davri qancha davom etgan?", "40 yil", "20 yil", "10 yil", "50 yil", "40 yil davom etdi.")
t.B("GFR qachon NATOga a’zo bo‘lgan?", "1955-yilda", "1949-yilda", "1957-yilda", "1963-yilda", "1955-yili.")
t.B("Adenauer qayerda repatriatsion to‘lovlar haqidagi shartnomani imzolagan?", "Lyuksemburgda", "Parijda", "Rimda", "Londonda", "Lyuksemburgda; yosh Isroil davlatiga yordam ko‘zda tutilgan.")
t.B("«Nemis iqtisodiy mo‘jizasining tan olingan otasi» kim?", "Lyudvig Erhard", "Konrad Adenauer", "Gelmut Kol", "Alchide de Gasperi", "Lyudvig Erhard.")
t.B("K. Adenauer qachon iste’foga chiqqan?", "1963-yilda", "1955-yilda", "1949-yilda", "1982-yilda", "1963-yili.")
t.B("1982-yili GFR kansleri etib kim saylangan?", "Gelmut Kol", "Lyudvig Erhard", "Konrad Adenauer", "Alchide de Gasperi", "Xristian-demokrat Gelmut Kol.")
t.B("Yagona Germaniya davlati qachon tashkil topgan?", "1990-yil 3-oktyabrda", "1989-yilda", "1949-yil 7-sentabrda", "1991-yilda", "1990-yil 3-oktyabr kuni.")
t.B("Ikkinchi jahon urushida Italiyada qancha kishi halok bo‘lgan yoki bedarak yo‘qolgan?", "330 mingga yaqin", "6,5 mln", "3 mln", "1 mln", "330 mingga yaqin kishi.")
t.B("1947-yilda Italiyada kommunistlar kimning aralashuvi bilan hukumatdan chiqarilgan?", "AQSH", "SSSR", "Britaniya", "Vatikan", "AQSH aralashuvi bilan.")
t.B("Italiya NATOga qachon a’zo bo‘lgan?", "1949-yilda", "1955-yilda", "1957-yilda", "1947-yilda", "1949-yili.")
t.B("Yevropa iqtisodiy hamjamiyatini tuzish to‘g‘risidagi shartnoma qanday atalgan?", "Rim shartnomasi", "Parij ahdnomasi", "Bonn shartnomasi", "Versal shartnomasi", "1957-yilgi Rim shartnomasi.")
t.B("Italiyada chuqur iqtisodiy inqiroz qachon boshlangan?", "1974-yilda", "1957-yilda", "1980-yilda", "1947-yilda", "1974-yili.")
t.B("XX asrning 80–90-yillari Italiyada nimaga qarshi kurash davri bo‘lgan?", "mafiyaga", "fashizmga", "kommunizmga", "monarxiyaga", "Mafiyaga qarshi kurash davri.")
t.NAT("1989-yili GDRda inqilob boshlandi.", "Berlin devori buzib tashlandi va 1990-yilda yagona Germaniya tashkil topdi", "GDR SSSR tarkibiga kirdi", "GFR tarqatildi", "Berlin devori mustahkamlandi", "Demokratiya tiklandi, Germaniya birlashdi.")
t.NAT("Parij ahdnomasi kuchga kirdi, GFR NATOga a’zo bo‘ldi (1955).", "GFR uchun okkupatsiya davri tugadi", "GFR GDR bilan birlashdi", "Adenauer iste’foga chiqdi", "Germaniya to‘rt zonaga bo‘lindi", "Okkupatsiya davri tugadi.")
t.TF("«Italiya iqtisodiy mo‘jizasi» natijalaridan asosan mamlakatning sanoati rivojlangan shimoliy qismi foyda ko‘rgan.", True, "To‘g‘ri: janub kambag‘allik manbai bo‘lib qoldi.")
t.TF("L. Erhard mamlakatdagi iqtisodiy va siyosiy holatni muvaffaqiyatli barqarorlashtirgan.", False, "Noto‘g‘ri: u buning uddasidan chiqolmadi.")
t.MUL([("Adenauer 1955-yilgacha bir paytning o‘zida tashqi ishlar vaziri vazifasini ham bajargan.", True),
       ("Urushdan keyin Italiyada pomeshchiklarning foydalanilmayotgan yerlari dehqonlarga berilgan.", True),
       ("1990-yildagi navbatdan tashqari saylovlarda G. Kol koalitsiyasi mag‘lub bo‘lgan.", False)],
      "III noto‘g‘ri: yana G. Kol boshchiligidagi koalitsiya g‘alaba qozondi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["GFR tashkil etildi", "GFR NATOga a’zo bo‘ldi", "Rim shartnomasi imzolandi", "Adenauer iste’foga chiqdi", "Italiyada chuqur iqtisodiy inqiroz", "Gelmut Kol kansler bo‘ldi", "Yagona Germaniya tashkil topdi"],
      "1949 → 1955 → 1957 → 1963 → 1974 → 1982 → 1990.")
t.VENN("GFR", "GDR",
       [("poytaxti Bonn", 1), ("1955-yilda NATOga a’zo bo‘lgan", 1),
        ("poytaxti Sharqiy Berlin", 2), ("SSSR okkupatsiya zonasida tuzilgan", 2),
        ("1949-yilda tashkil topgan", 3)],
       "GFR – Bonn, NATO; GDR – Sharqiy Berlin, SSSR zonasi; ikkalasi 1949-yilda tuzilgan.")
t.MAPMATCH(EU, ['Bonn', 'Berlin', 'Rim', 'Parij'],
           ["1949-yilda GFR poytaxti bo‘lgan shahar", "1989-yilda devori buzilgan, to‘rt sektorga bo‘lingan shahar", "1957-yilda YIH haqidagi shartnoma imzolangan shahar", "ahdnomasi kuchga kirgach GFR uchun okkupatsiya tugagan shahar"],
           "1 – Bonn; 2 – Berlin; 3 – Rim; 4 – Parij.")

# 20 G‘arbiy Yevropada integratsiya
t = Topic('y10j20', 10020); TOPICS['y10j20'] = t
t.B("Urushdan keyin Yevropa mamlakatlari tashqi savdo aylanmasining o‘sish sur’atlari iqtisodiy o‘sish sur’atlaridan qanday bo‘lgan?", "ikki barobar yuqori", "ikki barobar past", "teng", "o‘n barobar yuqori", "Ikki barobar yuqori bo‘ldi.")
t.B("Tariflar va savdo bo‘yicha bosh kelishuv (TSBK) qachon imzolangan?", "1947-yilda", "1948-yilda", "1951-yilda", "1957-yilda", "1947-yili.")
t.B("Keyinchalik TSBK qaysi tashkilotga aylantirilgan?", "Jahon savdo tashkiloti (JST)", "Yevropa Ittifoqi", "IHTT", "NATO", "Jahon savdo tashkilotiga (JST).")
t.B("Yevropa iqtisodiy hamkorlik tashkiloti (YIHT) qachon tuzilgan?", "1948-yilda", "1947-yilda", "1949-yilda", "1960-yilda", "1948-yili.")
t.B("YIHTning dastlabki vazifasi nima edi?", "«Marshall rejasi» yordamini taqsimlash", "ko‘mir va po‘lat bozorini yaratish", "atom energiyasini rivojlantirish", "harbiy ittifoq tuzish", "AQSHning «Marshall rejasi» bo‘yicha yordamini taqsimlash.")
t.B("1960-yili YIHT qanday qayta nomlangan?", "Iqtisodiy hamkorlik va taraqqiyot tashkiloti (IHTT)", "Yevropa Ittifoqi", "YESA", "YKPB", "IHTT; unga Yaponiya ham qo‘shildi.")
t.B("Yevropa Kengashi (YK) qachon tuzilgan?", "1949-yilda", "1951-yilda", "1957-yilda", "1948-yilda", "1949-yili 10 ta davlat ta’sis etdi.")
t.B("Germaniya va Fransiyaning iqtisodiy imkoniyatlarini birlashtirish tashabbusi bilan kim chiqqan?", "Robert Shuman", "Konrad Adenauer", "Sharl de Goll", "Alchide de Gasperi", "Fransiya tashqi ishlar vaziri Robert Shuman.")
t.B("Yevropa ko‘mir va po‘lat birlashmasi (YKPB) qachon tuzilgan?", "1951-yilda", "1949-yilda", "1957-yilda", "1948-yilda", "1951-yili olti davlat ishtirokida.")
t.B("Qaysi davlat YKPB a’zosi bo‘lgan?", "Lyuksemburg", "Buyuk Britaniya", "Shvetsiya", "Norvegiya", "GFR, Fransiya, Italiya, Belgiya, Niderlandlar, Lyuksemburg.")
t.B("1957-yili YKPB a’zolari qaysi ikki hujjatni imzolagan?", "YIH haqida Rim shartnomasi va YEVROATOM shartnomasi", "NATO va Varshava shartnomalari", "TSBK va JST", "Yagona Yevropa akti va Parij ahdnomasi", "YIH va YEVROATOM haqidagi shartnomalar.")
t.B("YIHda qonunchilik organi sifatida qaysi tashkilot tuzilgan?", "Yevropa Kengashi", "Yevropa hamjamiyati komissiyasi", "Maxsus sud", "Yevropa parlamenti", "Qonunchilik – Yevropa Kengashi, ijro – komissiya, Maxsus sud.")
t.B("Shimoliy Yevropa mamlakatlari integratsiyaning qanday muqobil modelini yaratgan?", "Yevropa erkin savdo assotsiatsiyasi (YESA)", "Yevropa ko‘mir va po‘lat birlashmasi", "Yevropa Ittifoqi", "O‘IYK", "YESA.")
t.B("Qaysi davlat YESA a’zosi bo‘lgan?", "Shveytsariya", "Fransiya", "Italiya", "Belgiya", "Britaniya, Avstriya, Daniya, Irlandiya, Norvegiya, Shvetsiya, Shveytsariya, Portugaliya.")
t.B("YESAning maqsadi nima qilib belgilangan?", "faqat sanoat mahsulotlariga boj to‘lovlarini kamaytirish", "millatlararo organ tuzish", "qonunchilikni bir xillashtirish", "yagona valyuta joriy qilish", "Faqat sanoat mahsulotlariga bojni bosqichma-bosqich kamaytirish.")
t.B("Yagona Yevropa aktiga binoan YIH qanday qayta tashkil qilingan?", "Yevropa Ittifoqi (YI) sifatida", "YESA sifatida", "IHTT sifatida", "NATO sifatida", "Yevropa Ittifoqi sifatida – «ichki chegaralarsiz makon».")
t.B("Ommaviy yig‘in, majlis, yirik anjuman nima deb ataladi?", "forum", "korporatsiya", "kvota", "koalitsiya", "Forum.")
t.NAT("1980-yillarda Fransiyada davlat nazorati va yuqori soliqlar kuchaydi.", "transmilliy korporatsiyalar kapitalini chiqarib keta boshladi, o‘sish sur’atlari pasaydi", "investitsiyalar keskin oshdi", "Fransiya YIHdan chiqdi", "ishsizlik yo‘qoldi", "Shundan so‘ng Fransiya qisman xususiylashtirish va soliqlarni pasaytirishga o‘tdi.")
t.NAT("1980-yillar oxirida Yevropada sotsialistik tizim inqirozga uchradi, SSSR tarqaldi.", "integratsiya imkoniyatlari kengaydi, sobiq sotsialistik mamlakatlar YIga intila boshladi", "Yevropa Ittifoqi tarqaldi", "YESA kuchaydi", "NATO tarqatildi", "Kechagi sotsialistik mamlakatlar ham YIga intildi.")
t.TF("Millatlararo tashkilotlar qabul qilgan integratsiya qarorlari milliy parlamentlar tasdig‘isiz to‘g‘ridan-to‘g‘ri kuchga kirgan.", True, "To‘g‘ri.")
t.TF("YESA millatlararo organ tashkil qilish va qonunchilikni bir xillashtirishni nazarda tutgan.", False, "Noto‘g‘ri: bu nazarda tutilmagan.")
t.MUL([("Ko‘plab G‘arbiy Yevropa mamlakatlarida iste’molning 50 foizdan ortig‘ini boshqa hududlarda ishlab chiqarilgan mahsulotlar tashkil qilgan.", True),
       ("Rim shartnomasi bo‘yicha tovarlar, kapital va ishchi kuchining erkin harakati tamoyili qo‘llangan.", True),
       ("Buyuk Britaniya YKPBning ta’sischi a’zolaridan biri bo‘lgan.", False)],
      "III noto‘g‘ri: YKPBni GFR, Fransiya, Italiya, Belgiya, Niderlandlar va Lyuksemburg tuzgan.")
t.CHR("Tashkilotlarni tuzilish ketma-ketligida joylashtiring.", ["TSBK", "YIHT", "Yevropa Kengashi", "YKPB", "YIH va YEVROATOM", "IHTT"],
      "1947 → 1948 → 1949 → 1951 → 1957 → 1960.")
t.VENN("YIH", "YESA",
       [("Rim shartnomasi asosida tuzilgan", 1), ("millatlararo organlarga ega", 1),
        ("Shimoliy Yevropa mamlakatlari tuzgan muqobil model", 2), ("faqat sanoat mahsulotlariga bojni kamaytirgan", 2),
        ("G‘arbiy Yevropa integratsiya tashkiloti", 3)],
       "YIH – Rim, millatlararo organlar; YESA – Shimoliy Yevropa, faqat sanoat; ikkalasi integratsiya tashkiloti.")
t.MAPMATCH('europeN', ['Rim', 'Fransiya', 'Shvetsiya'],
           ["1957-yilda YIH haqidagi shartnoma imzolangan shahar", "tashqi ishlar vaziri Robert Shuman tashabbus bilan chiqqan davlat", "Yevropa Kengashi ta’sischisi va YESA a’zosi bo‘lgan shimoliy davlat"],
           "1 – Rim; 2 – Fransiya; 3 – Shvetsiya.")
