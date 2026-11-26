from qlib import Topic
TOPICS = {}
W = 'globe'; EU = 'europe'; EA = 'eastasia'

# 15–16 Ikkinchi jahon urushi
t = Topic('e10j15-16', 1015); TOPICS['e10j15-16'] = t
t.B("Chexoslovakiyaning kapitulatsiyasi Myunxenda qachon rasmiylashtirilgan?", "1938-yil 29-sentabrda", "1939-yil 1-sentabrda", "1938-yil martda", "1939-yil 23-avgustda", "1938-yil 29-sentabr kuni.")
t.B("Sovet-German pakti necha yil muddatga imzolangan?", "10 yil", "5 yil", "25 yil", "muddatsiz", "10 yil muddatga.")
t.B("Ikkinchi jahon urushi qachon boshlangan?", "1939-yil 1-sentabrda", "1939-yil 3-sentabrda", "1941-yil 22-iyunda", "1938-yil 29-sentabrda", "1939-yil 1-sentabr kuni Germaniya Polshaga bostirib kirdi.")
t.B("Ikkinchi jahon urushi qachon tugagan?", "1945-yil 2-sentabrda", "1945-yil 9-mayda", "1945-yil 8-mayda", "1946-yilda", "1945-yil 2-sentabrda.")
t.B("Sovet qo‘shinlari Polshaga qachon kiritilgan?", "1939-yil 17-sentabrda", "1939-yil 1-sentabrda", "1941-yil 22-iyunda", "1940-yilda", "1939-yil 17-sentabr kuni.")
t.B("Sovet-fin urushi natijasida SSSRga qaysi hudud qo‘shib olingan?", "Viborg bilan Kareliya", "Finlandiya to‘liq", "Estoniya", "Polshaning g‘arbi", "Kareliya Viborg shahri bilan birga.")
t.B("Uchlar pakti qachon imzolangan?", "1940-yil sentabrda", "1936-yil noyabrda", "1941-yil iyunda", "1939-yil avgustda", "1940-yil sentabrda.")
t.B("Gitlerning SSSRni tor-mor qilish rejasi qanday atalgan?", "«Barbarossa»", "«Daues»", "«Marshall»", "«Overlord»", "«Barbarossa» rejasi.")
t.B("Germaniya SSSRga qachon bostirib kirgan?", "1941-yil 22-iyunda", "1939-yil 1-sentabrda", "1942-yil noyabrda", "1940-yil sentabrda", "1941-yil 22-iyunda.")
t.B("1941-yil avgustda AQSH va Britaniya qanday hujjat imzolagan?", "Atlantik xartiya", "Uchlar pakti", "Myunxen kelishuvi", "BMT Ustavi", "Atlantik xartiya.")
t.B("Nemis qo‘shinlari dastlabki jiddiy mag‘lubiyatga qayerda uchragan?", "Moskva ostonalarida (1941-yil dekabr)", "Stalingradda", "Berlinda", "Kurskda", "1941-yil dekabrda Moskva ostonalarida.")
t.B("Stalingradda qurshovdagi nemis qo‘shinlari qachon taslim bo‘lgan?", "1943-yil fevralda", "1942-yil noyabrda", "1944-yilda", "1945-yil mayda", "1943-yil fevralda.")
t.B("Italyan-German qo‘shinlari Afrikadan qachon to‘liq quvib chiqarilgan?", "1943-yil mayda", "1942-yil noyabrda", "1944-yilda", "1941-yilda", "1943-yil may oyida.")
t.B("«Ozod Fransiya» Qarshilik harakatiga kim boshchilik qilgan?", "general de Goll", "I.B. Tito", "Cherchill", "Daladye", "General de Goll.")
t.B("Berlin operatsiyasi qaysi sanalarda bo‘lgan?", "1945-yil 16-apreldan 2-maygacha", "1945-yil 8–9-may", "1944-yil iyunda", "1943-yil fevralda", "1945-yil 16-apreldan 2-maygacha.")
t.B("Germaniyaning so‘zsiz taslim bo‘lish aktini SSSR nomidan kim imzolagan?", "G.K. Jukov", "I. Stalin", "Molotov", "Kutuzov", "Oliy bosh qo‘mondon o‘rinbosari G.K. Jukov.")
t.B("Urush yillari O‘zbekistonga qancha kishi evakuatsiya qilingan?", "1 mln.dan oshiq", "100 ming", "10 mln.", "500 ming", "1 mln.dan oshiq; shundan 200 mingdan oshig‘i bolalar.")
t.B("AQSH Xirosimaga atom bombasini qachon tashlagan?", "1945-yil 6-avgustda", "1945-yil 9-avgustda", "1945-yil 2-sentabrda", "1945-yil 8-mayda", "1945-yil 6-avgustda.")
t.B("Ikkinchi jahon urushida qancha kishi halok bo‘lgan?", "60–65 mln.", "110 mln.", "10 mln.", "20 mln.", "60–65 mln. kishi halok bo‘ldi.")
t.B("Nyurnberg sud jarayoni qachon bo‘lgan?", "1945-yil noyabr – 1946-yil oktabr", "1946-yil may – 1948-yil noyabr", "1945-yil mayda", "1949-yilda", "1945-yil noyabrdan 1946-yil oktabrgacha.")
t.NAT("Germaniya hujumi SSSR uchun kutilmaganda yuz berdi.", "sovet aviatsiyasining katta qismi aerodromlarda yo‘q qilindi", "SSSR Berlinni oldi", "Germaniya darhol taslim bo‘ldi", "Yaponiya SSSRga hujum qildi",
      "Qo‘shinni boshqarish va ta’minlash tizimi izdan chiqdi.")
t.NAT("Stalingraddagi mag‘lubiyat Uchlar ittifoqi uchun halokatli bo‘ldi.", "Germaniya yalpi safarbarlik e’lon qilib, zaxiralarni Sharqiy frontga jalb qildi", "Germaniya sulh so‘radi", "Italiya Germaniyaga qo‘shildi", "Yaponiya taslim bo‘ldi",
      "Natijada ittifoqchilar Afrikada g‘alaba qozondi.")
t.NAT("Nyurnberg va Tokio sud jarayonlari o‘tkazildi.", "davlat yoki armiya boshlig‘i maqomi jinoiy javobgarlikdan ozod qilmasligi tan olindi", "fashistlar oqlandi", "Germaniya qayta qurollandi", "BMT tarqatildi",
      "Sud qarorlari xalqaro huquqning muhim manbayiga aylandi.")
t.TF("SSSR sovet-fin urushidan so‘ng Millatlar Ligasidan chiqarilgan.", True, "To‘g‘ri: tajovuzkor davlat sifatida.")
t.TF("Atom bombalari portlashida asosan harbiylar halok bo‘lgan.", False, "Noto‘g‘ri: asosan tinch aholi halok bo‘lgan.")
t.MUL([("Uchlar paktiga Vengriya, Ruminiya, Slovakiya va Bolgariya qo‘shilgan.", True), ("Urush davomida Tehron, Yalta va Potsdamda uchrashuvlar bo‘lgan.", True), ("9-may SSSRda «Mustaqillik kuni» deb e’lon qilingan.", False)],
      "III noto‘g‘ri: 9-may «G‘alaba kuni» deb e’lon qilingan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Myunxen kelishuvi", "Ikkinchi jahon urushi boshlandi", "Uchlar pakti", "Germaniya SSSRga bostirib kirdi", "Stalingradda taslim bo‘lish", "Germaniya taslim bo‘ldi", "Yaponiya taslim bo‘ldi"],
      "1938 → 1939 → 1940 → 1941 → 1943 → 1945 may → 1945 sentabr.")
t.MAPMATCH(EU, ['Stalingrad', 'Yalta', 'Potsdam', 'Nyurnberg'],
           ["1942–1943-yillarda nemislar qurshovga olingan shahar", "1945-yil fevralda Qrim konferensiyasi o‘tgan joy", "1945-yil iyul–avgustda konferensiya o‘tgan shahar", "fashist rahbarlari ustidan sud bo‘lgan shahar"],
           "1 – Stalingrad; 2 – Yalta; 3 – Potsdam; 4 – Nyurnberg.")
t.MAPMATCH('fareast', ['Xirosima', 'Nagasaki', 'Tokio'],
           ["1945-yil 6-avgustda atom bombasi tashlangan shahar", "1945-yil 9-avgustda atom bombasi tashlangan shahar", "yapon harbiy jinoyatchilari sudi bo‘lgan poytaxt"], "1 – Xirosima; 2 – Nagasaki; 3 – Tokio.")
t.VENN("Nyurnberg jarayoni", "Tokio jarayoni",
       [("Germaniya rahbarlari sud qilingan", 1), ("gestapo, SS jinoyatchi tashkilot deb topilgan", 1),
        ("yapon harbiy jinoyatchilari sud qilingan", 2), ("1946–1948-yillarda bo‘lgan", 2),
        ("bosh harbiy jinoyatchilar ustidan xalqaro sud", 3)],
       "Nyurnberg – Germaniya; Tokio – Yaponiya. Ikkalasi xalqaro harbiy tribunal.")

# 17 Sovuq urush
t = Topic('e10j17', 1017); TOPICS['e10j17'] = t
t.B("Cherchill «temir parda» iborasini qo‘llagan nutqini qachon va qayerda so‘zlagan?", "1946-yil martda Fulton shahrida", "1945-yilda Yaltada", "1947-yilda Londonda", "1949-yilda Vashingtonda", "1946-yil martda AQSHning Fulton shahrida.")
t.B("Yevropaga yordam ko‘rsatish g‘oyasini qachon J. Marshall ilgari surgan?", "1947-yil iyunda", "1946-yil martda", "1949-yil aprelda", "1955-yilda", "1947-yil iyunda.")
t.B("«Marshall rejasi»ni kim rad etgan?", "sovet diplomatiyasi", "Fransiya", "Britaniya", "Italiya", "Sovet diplomatiyasi rad etdi.")
t.B("O‘zaro Iqtisodiy Yordam Kengashi (O‘IYK) qachon tuzilgan?", "1949-yil yanvarda", "1949-yil aprelda", "1955-yilda", "1947-yilda", "1949-yil yanvarda.")
t.B("NATO qachon tuzilgan?", "1949-yil aprelda", "1949-yil yanvarda", "1955-yilda", "1946-yilda", "1949-yil aprelda.")
t.B("Varshava Shartnomasi Tashkiloti qachon tuzilgan?", "1955-yilda", "1949-yilda", "1961-yilda", "1947-yilda", "1955-yili NATOga javob tariqasida.")
t.B("Mustamlakachilikdan ozod bo‘lgan yangi davlatlar qanday nom olgan?", "«uchinchi dunyo mamlakatlari»", "«sotsialistik lager»", "«oq mustamlakalar»", "«dominionlar»", "«Uchinchi dunyo mamlakatlari».")
t.B("Qo‘shilmaslik harakati qachon tashkil qilingan?", "1961-yilda", "1955-yilda", "1949-yilda", "1975-yilda", "1961-yili.")
t.B("Qo‘shilmaslik harakati tashabbuskorlari kimlar?", "Tito, Neru, Nosir", "Gandi, Sun Yatsen, Otaturk", "Cherchill, Ruzvelt, Stalin", "Marshall, Trumen, Eyzenxauer", "Iosif Broz Tito, Javoharlal Neru, Jamol Abdul Nosir.")
t.B("SSSR va AQSH o‘rtasida SQCH-1 shartnomasi qachon imzolangan?", "1972-yilda", "1975-yilda", "1979-yilda", "1985-yilda", "1972-yili.")
t.B("Yevropada Xavfsizlik va hamkorlik kengashining Yakunlovchi akti qachon imzolangan?", "1975-yilda", "1972-yilda", "1979-yilda", "1961-yilda", "1975-yili.")
t.B("SQCH-2 shartnomasi qachon imzolangan?", "1979-yilda", "1972-yilda", "1975-yilda", "1987-yilda", "1979-yili.")
t.B("Sovet qo‘shinlari Afg‘onistonga qachon kiritilgan?", "1979-yil dekabrda", "1975-yilda", "1985-yilda", "1972-yilda", "1979-yil dekabrda.")
t.B("1980-yillarda Jeneva va Reykyavikda qaysi liderlar uchrashgan?", "M.S. Gorbachev va R. Reygan", "Stalin va Trumen", "Xrushchev va Kennedi", "Brejnev va Nikson", "Gorbachev va Reygan.")
t.NAT("AQSH «Marshall rejasi»ni ilgari surdi, SSSR uni rad etdi.", "Yevropa ikki guruhga bo‘linib, uzoq qarama-qarshilik boshlandi", "Yevropa birlashdi", "SSSR NATOga kirdi", "AQSH Yevropadan chiqib ketdi",
      "Qarama-qarshi harbiy-siyosiy ittifoqlar tizimi shakllandi.")
t.NAT("1979-yilda sovet qo‘shinlari Afg‘onistonga kiritildi.", "xalqaro munosabatlarda yana keskinlik boshlandi", "keskinlik yumshadi", "SQCH-2 imzolandi", "NATO tarqatildi",
      "Bu yana keskinlikka olib keldi.")
t.TF("Jeneva va Reykyavik uchrashuvlari biron-bir shartnoma imzolanishi bilan yakunlanmagan.", True, "To‘g‘ri, lekin yadro urushi xavfidan xalos bo‘lish intilishini ko‘rsatdi.")
t.TF("Yevropada Xavfsizlik va hamkorlik kengashining Yakunlovchi akti majburiy shartnoma edi.", False, "Noto‘g‘ri: u shartnoma emasdi, lekin katta axloqiy-siyosiy ahamiyatga ega edi.")
t.MUL([("Urushdan so‘ng AQSH birinchi marta SSSRga yadro quroli bilan tahdid qilgan.", True), ("Ikki qarama-qarshi ittifoq markazlari AQSH va SSSR edi.", True), ("Qo‘shilmaslik harakati a’zolari SSSR bilan qattiq bog‘lanishni tanlagan.", False)],
      "III noto‘g‘ri: ular na SSSR, na AQSH bilan qattiq bog‘lanishni istamagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Fulton nutqi", "«Marshall rejasi»", "O‘IYK tuzildi", "NATO tuzildi", "Varshava Shartnomasi Tashkiloti", "Qo‘shilmaslik harakati"],
      "1946 → 1947 → 1949 yanvar → 1949 aprel → 1955 → 1961.")
t.MAPMATCH('globe2', ['Fulton', 'Varshava', 'Afg‘oniston'],
           ["Cherchill «temir parda» nutqini so‘zlagan AQSH shahri", "1955-yilgi harbiy-siyosiy ittifoq nomini bergan shahar", "1979-yilda sovet qo‘shinlari kiritilgan davlat"], "1 – Fulton; 2 – Varshava; 3 – Afg‘oniston.")
t.VENN("NATO", "Varshava Shartnomasi Tashkiloti",
       [("1949-yil aprelda tuzilgan", 1), ("G‘arb davlatlarining ittifoqi", 1),
        ("1955-yilda tuzilgan", 2), ("SSSR va Sharqiy Yevropa davlatlari ittifoqi", 2),
        ("harbiy-siyosiy ittifoq", 3)],
       "NATO – 1949, G‘arb. VShT – 1955, SSSR. Ikkalasi harbiy-siyosiy ittifoq.")

# 18 AQSH 1946–1991
t = Topic('e10j18', 1018); TOPICS['e10j18'] = t
t.B("Urushdan keyin AQSH qanday mavqega ega bo‘lgan?", "G‘arb dunyosining siyosiy, iqtisodiy va harbiy yetakchisi", "Sharq bloki yetakchisi", "betaraf davlat", "qarzdor davlat", "AQSH G‘arb dunyosi yetakchisiga aylandi.")
t.B("Harbiy sanoat korxonalarini iste’mol tovarlari ishlab chiqarishga o‘tkazish nima deb ataladi?", "konversiya", "retsessiya", "inflatsiya", "militarizatsiya", "Konversiya.")
t.B("1960-yillarda iqtisodiy o‘sishni jadallashtirgan prezidentlar kimlar?", "Jon Kennedi va Lindon Jonson", "Eyzenxauer va Trumen", "Nikson va Ford", "Reygan va Bush", "J. Kennedi va L. Jonson.")
t.B("Reygan ma’muriyatining iqtisodiy tadbirlari qanday nom olgan?", "«Reyganomika»", "«Yangi kurs»", "«Marshall rejasi»", "«Makkartizm»", "«Reyganomika».")
t.B("Reygan prezidentlik saylovida qachon g‘alaba qozongan?", "1980-yilda", "1976-yilda", "1984-yilda", "1972-yilda", "1980-yilgi saylovlarda.")
t.B("1952-yilgi saylovlarda kim g‘olib chiqqan?", "Duayt Eyzenxauer", "Jon Kennedi", "Garri Trumen", "Richard Nikson", "Respublikachi Duayt Eyzenxauer.")
t.B("Davlat organlarida josuslar va kommunistlarni aniqlash tekshiruvlarini kim olib borgan?", "senator Jozef Makkarti", "Martin Lyuter King", "Richard Nikson", "Jorj Marshall", "Senator Jozef Makkarti – makkartizm.")
t.B("Jon Kennedi qachon o‘ldirilgan?", "1963-yilda", "1968-yilda", "1960-yilda", "1974-yilda", "1963-yili.")
t.B("Martin Lyuter King qachon va qayerda o‘ldirilgan?", "1968-yilda Memfisda", "1963-yilda Dallasda", "1965-yilda Vashingtonda", "1970-yilda Nyu-Yorkda", "1968-yil Memfisda.")
t.B("Prezident Niksonning iste’fosiga qaysi janjal sabab bo‘lgan?", "«Uotergeyt ishi»", "«Makkartizm»", "«Reyganomika»", "Vyetnam urushi", "«Uotergeyt ishi».")
t.B("AQSH Vyetnamda faol urush harakatlarini qaysi yillarda olib borgan?", "1965–1973", "1950–1953", "1979–1989", "1990–1991", "1965–1973-yillarda.")
t.B("Qog‘oz pulning qadrsizlanishi nima deb ataladi?", "inflatsiya", "retsessiya", "konversiya", "devalvatsiya", "Inflatsiya.")
t.B("1990-yillar boshida AQSH iqtisodiyotida nima kuzatilgan?", "qisqa muddatli retsessiya", "keskin o‘sish", "giperinflatsiya", "konversiya", "Qisqa muddatli retsessiya.")
t.NAT("«Reyganomika» siyosati amalga oshirildi.", "inflatsiya pasayib, ishsizlik kamaydi, chet el kapitali kirib keldi", "inflatsiya oshdi", "ishsizlik ko‘paydi", "AQSH inqirozga uchradi",
      "Reyganomika yaxshi natijalarga olib keldi.")
t.NAT("Gorbachev boshchiligida SSSRda yangi rahbariyat keldi.", "sovet-Amerika munosabatlarida jiddiy ijobiy o‘zgarishlar boshlandi", "yangi urush boshlandi", "NATO tarqatildi", "AQSH SSSRni bosib oldi",
      "Strategik hujum qurollarini cheklash shartnomasi muhim ahamiyatga ega bo‘ldi.")
t.TF("Martin Lyuter King Nobel tinchlik mukofoti sovrindori bo‘lgan.", True, "To‘g‘ri.")
t.TF("1970-yillar inqirozi AQShda boshqa rivojlangan davlatlarga nisbatan yengil kechgan.", False, "Noto‘g‘ri: AQShda ancha og‘ir kechgan.")
t.MUL([("1960-yillarda fuqarolar tengligi uchun harakat eng yuqori nuqtasiga yetgan.", True), ("1980–1990-yillar boshi neokonservatizm tantanasi davri bo‘lgan.", True), ("Urushdan keyin AQSH yangi bozorlardan voz kechgan.", False)],
      "III noto‘g‘ri: AQSH yangi bozorlarni egallab olgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Eyzenxauer saylandi", "Kennedi o‘ldirildi", "Vyetnam urushi boshlandi", "Martin Lyuter King o‘ldirildi", "Reygan saylandi"],
      "1952 → 1963 → 1965 → 1968 → 1980.")
t.MAPN('usa_e', ['Vashington', 'Memfis (AQSH)', 'Nyu-York', 'Chikago'], "1968-yilda Martin Lyuter King o‘ldirilgan shahar qaysi raqam bilan belgilangan?", "Memfis – 2.", ask_idx=1)
t.VENN("Makkartizm davri", "1960-yillar",
       [("josuslar va kommunistlarni qidirish", 1), ("siyosiy reaksiya kuchaygan", 1),
        ("fuqarolar tengligi harakati cho‘qqiga chiqqan", 2), ("Vyetnam urushiga qarshi namoyishlar", 2),
        ("AQSH ichki siyosiy hayotidagi davr", 3)],
       "Makkartizm – reaksiya; 1960-yillar – fuqarolik harakati. Ikkalasi AQSH tarixi davri.")

# 19–20 SSSR 1946–1991
t = Topic('e10j19-20', 1019); TOPICS['e10j19-20'] = t
t.B("Ikkinchi jahon urushida qancha sovet fuqarosi halok bo‘lgan?", "27 mln.", "12,5 mln.", "60 mln.", "7 mln.", "27 mln. sovet fuqarosi halok bo‘ldi.")
t.B("SSSR iqtisodiyotni nima hisobiga tiklagan?", "to‘liq ichki resurslar hisobiga", "«Marshall rejasi» bo‘yicha", "Britaniya kreditlari hisobiga", "Germaniya tovonlari hisobiga", "SSSR iqtisodiyotni o‘z kuchi bilan tikladi.")
t.B("Qachon SSSRda sanoat ishlab chiqarishi urushdan oldingi darajadan oshgan?", "1950-yilda", "1946-yilda", "1955-yilda", "1960-yilda", "1950-yili.")
t.B("Stalin qachon vafot etgan?", "1953-yil 5-martda", "1956-yil fevralda", "1964-yil oktabrda", "1952-yilda", "1953-yil 5-mart kuni.")
t.B("Xrushchyov hokimiyatda turgan yillar qanday nom olgan?", "«iliqlik» davri", "«turg‘unlik» davri", "«qayta qurish»", "«harbiy kommunizm»", "«Iliqlik» davri (1953–1964).")
t.B("«Shaxsga sig‘inish va uning oqibatlari to‘g‘risida» nutqi qachon so‘zlangan?", "1956-yil fevralda KPSS XX syezdida", "1953-yilda", "1964-yilda", "1958-yilda", "1956-yil fevralda.")
t.B("Xrushchyov lavozimlaridan qachon ozod qilingan?", "1964-yil oktabrda", "1958-yil martda", "1962-yilda", "1956-yilda", "1964-yil oktabrdagi Plenumda.")
t.B("Xrushchyovdan keyin KPSS MK Birinchi kotibi kim bo‘lgan?", "Leonid Brejnev", "Aleksey Kosigin", "Yuriy Andropov", "Konstantin Chernenko", "Leonid Brejnev.")
t.B("1970-yillar ikkinchi yarmidagi inqiroz davri qanday nom olgan?", "«turg‘unlik» davri", "«iliqlik» davri", "«qayta qurish»", "«oshkoralik»", "«Turg‘unlik» davri.")
t.B("Brejnev qachon vafot etgan?", "1982-yil 10-noyabrda", "1985-yil martda", "1964-yilda", "1979-yilda", "1982-yil 10-noyabrda.")
t.B("Mixail Gorbachyov qachon Bosh kotib etib saylangan?", "1985-yil martda", "1982-yilda", "1987-yilda", "1991-yilda", "1985-yil martda.")
t.B("Gorbachyov «qayta qurish» va «oshkoralik» siyosatini qachon e’lon qilgan?", "1987-yilda", "1985-yilda", "1991-yilda", "1989-yilda", "1987-yili.")
t.B("Kubada F. Kastro qachon hokimiyatga kelgan?", "1959-yilda", "1962-yilda", "1953-yilda", "1965-yilda", "1959-yili.")
t.B("SSSR va AQSH o‘rtasidagi yadro urushi xavfi qanday nom olgan?", "«Karib inqirozi»", "«Berlin inqirozi»", "«Suvaysh inqirozi»", "«Avgust inqirozi»", "«Karib inqirozi».")
t.B("Favqulodda holat davlat komiteti (GKCHP) qachon tuzilgan?", "1991-yil 19-avgustga o‘tar kechasi", "1991-yil 8-dekabrda", "1985-yilda", "1990-yilda", "1991-yil 19-avgustga o‘tar kechasi.")
t.B("MDH qachon va qayerda tuzilgan?", "1991-yil 8-dekabrda Minskda", "1991-yil 19-avgustda Moskvada", "1922-yilda", "1992-yilda Kiyevda", "1991-yil 8-dekabrda Minskda.")
t.NAT("Xrushchyov XX syezdda Stalin shaxsiga sig‘inishni fosh etdi.", "qatag‘on qilinganlarni oqlash jarayoni ommaviy tus oldi", "qatag‘onlar kuchaydi", "Stalin rejimi tiklandi", "SSSR tarqaldi",
      "Bu nutq qatag‘on qurbonlarini oqlashga yo‘l ochdi.")
t.NAT("Qo‘riq va bo‘z yerlar o‘zlashtirildi, qishloq xo‘jaligi soliqlari pasaytirildi.", "1950-yillar ikkinchi yarmida kolxozlarning pul daromadi 3 martadan ko‘proq oshdi", "ocharchilik boshlandi", "g‘alla importi to‘xtadi", "kolxozlar tarqatildi",
      "Qishloq xo‘jaligi mahsulotlari keskin o‘sdi.")
t.NAT("Kennedi va Xrushchyov o‘rtasida kelishuvga erishildi.", "dunyo yadro urushi halokatidan asrab qolindi", "yadro urushi boshlandi", "Kuba AQShga qo‘shildi", "SSSR tarqaldi",
      "Kelishuv Karib inqirozini hal qildi.")
t.NAT("GKCHP a’zolari 1991-yil 22-avgustda qamoqqa olindi.", "KPSS faoliyati to‘xtatilib, respublikalar mustaqilligini e’lon qildi", "SSSR mustahkamlandi", "Gorbachyov iste’foga chiqmadi", "GKCHP hokimiyatni oldi",
      "Avgust voqealaridan keyin barcha respublikalar mustaqilligini e’lon qildi.")
t.TF("Oshkoralik sovet xalqlarining milliy mustaqillikka intilishini jadallashtirgan.", True, "To‘g‘ri.")
t.TF("MDHga Gruziya, Latviya, Litva va Estoniya ham a’zo bo‘lgan.", False, "Noto‘g‘ri: bu respublikalardan boshqa barcha sobiq sovet respublikalari a’zo bo‘ldi.")
t.MUL([("1958-yilda Xrushchyov Ministrlar Soveti Raisi lavozimini ham egallagan.", True), ("Brejnevdan keyin Andropov va Chernenko hokimiyatga kelgan.", True), ("SSSR «Marshall rejasi» bo‘yicha AQShdan yordam olgan.", False)],
      "III noto‘g‘ri: SSSR iqtisodiyotni o‘z ichki resurslari hisobiga tikladi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Stalin vafot etdi", "XX syezd", "Xrushchyov lavozimidan ozod qilindi", "Gorbachyov Bosh kotib bo‘ldi", "GKCHP tuzildi", "MDH tuzildi"],
      "1953 → 1956 → 1964 → 1985 → 1991 avgust → 1991 dekabr.")
t.MATCH("Rahbarlarni davr nomlari bilan moslashtiring.", ["Nikita Xrushchyov", "Leonid Brejnev", "Mixail Gorbachyov"], ["«iliqlik» davri", "«turg‘unlik» davri", "«qayta qurish»", "«harbiy kommunizm»"], 'abc',
        "Xrushchyov – iliqlik; Brejnev – turg‘unlik; Gorbachyov – qayta qurish.")
t.MAPMATCH('eurasia2', ['Moskva', 'Minsk', 'Afg‘oniston'],
           ["1991-yil avgustda GKCHP qo‘shin kiritgan poytaxt", "1991-yil 8-dekabrda MDH tuzilgan shahar", "1979-yilda sovet qo‘shinlari kiritilgan davlat"], "1 – Moskva; 2 – Minsk; 3 – Afg‘oniston.")
t.VENN("«Iliqlik» davri", "«Qayta qurish» davri",
       [("Stalin shaxsiga sig‘inish fosh etilgan", 1), ("qo‘riq yerlar o‘zlashtirilgan", 1),
        ("«oshkoralik» siyosati", 2), ("«yangicha siyosiy tafakkur»", 2),
        ("sovet tuzumini isloh qilishga urinish", 3)],
       "Iliqlik – XX syezd, qo‘riq. Qayta qurish – oshkoralik. Ikkalasi tuzumni isloh qilishga urinish.")
