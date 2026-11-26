from qlib import Topic
TOPICS = {}
W = 'globe'; EU = 'europe'; LA = 'latam'; AF = 'africa'

# 27 Lotin Amerikasi 1946–1991
t = Topic('e10j27', 1027); TOPICS['e10j27'] = t
t.B("Nikaraguada inqilob qachon bo‘lgan?", "1979-yilda", "1959-yilda", "1973-yilda", "1989-yilda", "1979-yili.")
t.B("Lotin Amerikasida modernizatsiyalashning nechta varianti ko‘zga tashlanadi?", "uchta", "ikkita", "to‘rtta", "beshta", "Inqilobiy, neokonservativ va islohotchilik – uchta variant.")
t.B("Kubada inqilob qachon g‘alaba qozongan?", "1959-yil 1-yanvarda", "1962-yilda", "1953-yilda", "1970-yilda", "1959-yil 1-yanvar kuni.")
t.B("Kubada inqilobga kim boshchilik qilgan?", "Fidel Kastro", "Salvador Alyende", "Augusto Pinochet", "Simon Bolivar", "Fidel Kastro.")
t.B("Kuba poytaxti qaysi shahar?", "Gavana", "Santyago", "Mexiko", "Karakas", "Gavana.")
t.B("Kuba qanday modernizatsiyalash variantini tanlagan?", "inqilobiy", "neokonservativ", "islohotchilik", "liberal", "Inqilobiy variant.")
t.B("Kuba–SSSR yaqinlashuvi qanday inqirozga olib kelgan?", "1962-yilgi Karib inqirozi", "Berlin inqirozi", "Suvaysh inqirozi", "neft inqirozi", "1962-yilgi Karib inqiroziga.")
t.B("1970-yilda Chili prezidenti etib kim saylangan?", "Salvador Alyende", "Augusto Pinochet", "P. Eylvin", "Fidel Kastro", "Xalq birligi bloki nomzodi Salvador Alyende.")
t.B("Chilida davlat to‘ntarishi qachon bo‘lgan?", "1973-yilda", "1970-yilda", "1979-yilda", "1989-yilda", "1973-yili.")
t.B("1973-yilda Chilida hokimiyatga kim keldi?", "general Augusto Pinochet boshchiligidagi harbiy xunta", "Fidel Kastro", "Alyende", "Eylvin", "General Augusto Pinochet.")
t.B("Pinochet qaysi modernizatsiyalash variantini tanlagan?", "neokonservativ", "inqilobiy", "islohotchilik", "sotsialistik", "Neokonservativ variant.")
t.B("1989-yilgi saylovlarda Chilida kim g‘olib chiqqan?", "P. Eylvin", "Pinochet", "Alyende", "Kastro", "Xristian-demokrat P. Eylvin.")
t.B("Meksika qachon sanoat hajmi bo‘yicha Lotin Amerikasida birinchi o‘ringa chiqqan?", "1958-yilda", "1946-yilda", "1970-yilda", "1980-yilda", "1958-yili.")
t.B("Meksika qanday modernizatsiyalash yo‘lini tanlagan?", "liberal-islohotchilik", "inqilobiy", "neokonservativ", "harbiy", "Liberal-islohotchilik yo‘li.")
t.B("Davlat to‘ntarishi orqali hokimiyatga kelgan harbiylar hokimiyati qanday ataladi?", "harbiy xunta", "koalitsiya", "parlament", "kortes", "Harbiy xunta.")
t.NAT("Pinochetning neokonservativ islohotlari amalga oshirildi.", "ish haqi kamayib, ishsizlik keskin oshdi", "ishsizlik yo‘qoldi", "demokratik erkinliklar kengaydi", "Chili sotsialistik bo‘ldi",
      "Bu katta ijtimoiy muammolarga olib keldi.")
t.NAT("SSSR parchalandi.", "bu Kuba uchun juda katta zarba bo‘ldi", "Kuba boyib ketdi", "Kastro rejimi darhol quladi", "Kuba AQShga qo‘shildi",
      "SSSRning parchalanishi Kubaga katta zarba bo‘ldi.")
t.NAT("1980-yillardagi jahon iqtisodiy inqirozi Meksikaga ta’sir qildi.", "ishsizlik va tashqi qarz oshib, AQShga qaramlik ortdi", "Meksika eng boy davlatga aylandi", "Meksika inqilobni tanladi", "tashqi qarz yo‘qoldi",
      "Inqiroz yengilgan bo‘lsa-da, AQShga qaramlik ortdi.")
t.TF("1990-yillarda ko‘pchilik bashorat qilganiga qaramay, Kastro rejimi saqlanib qolgan.", True, "To‘g‘ri.")
t.TF("Pinochet davrida Chilida konstitutsiya va demokratik erkinliklar kengaytirilgan.", False, "Noto‘g‘ri: ular bekor qilingan.")
t.MUL([("Meksikaning iqtisodiy rivojlanishida davlat sektori asosiy rol o‘ynagan.", True), ("Ekvador, Peru, Boliviya, Argentina, Braziliya va Urugvayda harbiy rejimlar fuqarolik hukumatlari bilan almashtirilgan.", True), ("Meksika Kuba variantini to‘liq qabul qilgan.", False)],
      "III noto‘g‘ri: Meksika Kuba variantini qabul qilmagan.")
t.MATCH("Mamlakatlarni modernizatsiya varianti bilan moslashtiring.", ["Kuba", "Chili (Pinochet)", "Meksika"], ["inqilobiy", "neokonservativ", "islohotchilik", "monarxistik"], 'abc',
        "Kuba – inqilobiy; Chili – neokonservativ; Meksika – islohotchilik.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Meksika sanoatda birinchi o‘ringa chiqdi", "Kuba inqilobi g‘alabasi", "Karib inqirozi", "Alyende prezident bo‘ldi", "Pinochet to‘ntarishi", "Nikaragua inqilobi", "Eylvin saylandi"],
      "1958 → 1959 → 1962 → 1970 → 1973 → 1979 → 1989.")
t.MAPMATCH(LA, ['Kuba', 'Chili', 'Meksika', 'Nikaragua'],
           ["1959-yilda Kastro inqilobi g‘alaba qozongan davlat", "1973-yilda Pinochet to‘ntarishi bo‘lgan davlat", "islohotchilik variantini tanlagan davlat", "1979-yilda inqilob bo‘lgan Markaziy Amerika davlati"],
           "1 – Kuba; 2 – Chili; 3 – Meksika; 4 – Nikaragua.")
t.VENN("Salvador Alyende", "Augusto Pinochet",
       [("1970-yilda Xalq birligi bloki nomzodi sifatida saylangan", 1), ("chuqur islohotlar boshlagan", 1),
        ("1973-yilda to‘ntarish bilan hokimiyatga kelgan", 2), ("demokratik erkinliklarni bekor qilgan", 2),
        ("Chili rahbari bo‘lgan", 3)],
       "Alyende – saylangan, islohotchi. Pinochet – to‘ntarish, diktatura. Ikkalasi Chili rahbari.")

# 28 Afrika 1946–1991
t = Topic('e10j28', 1028); TOPICS['e10j28'] = t
t.B("V Panafrika kongressi qachon va qayerda bo‘lgan?", "1945-yilda Manchesterda", "1960-yilda Londonda", "1919-yilda Parijda", "1975-yilda Lissabonda", "1945-yili Manchester shahrida.")
t.B("Mustamlakachilikdan ozod bo‘lish jarayonining eng yuqori nuqtasi qaysi yil?", "1960-yil («Afrika yili»)", "1945-yil", "1975-yil", "1990-yil", "1960-yil – «Afrika yili».")
t.B("1960-yilda nechta yangi Afrika davlati paydo bo‘lgan?", "17 ta", "40 ta", "5 ta", "50 ta", "17 ta yangi davlat.")
t.B("1960-yilda mustaqillik e’lon qilgan Afrikaning eng katta davlatlari qaysilar?", "Nigeriya va Kongo", "Misr va Liviya", "Efiopiya va Liberiya", "Angola va Mozambik", "Nigeriya va Kongo.")
t.B("Mustamlakachilik davrida ikkiga bo‘linib, 1960-yilda birlashgan davlat qaysi?", "Somali", "Kongo", "Nigeriya", "Sudan", "Somali Demokratik Respublikasi.")
t.B("Portugaliya mustamlakalari qachon mustaqil bo‘lgan?", "1975-yilda Portugaliyadagi inqilobdan so‘ng", "1960-yilda", "1945-yilda", "1990-yilda", "1975-yili.")
t.B("1990-yillarga kelib Sahroyi Kabirdan janubda nechtadan oshiq mustaqil davlat tashkil topgan?", "40 dan", "17 dan", "100 dan", "10 dan", "40 dan oshiq.")
t.B("SSSRga ergashgan Afrika davlatlari qanday yo‘lni tanlagan?", "«nokapitalistik taraqqiyot yo‘li»", "«yangi kurs»", "«qayta qurish»", "«oq inqilob»", "«Nokapitalistik taraqqiyot yo‘li».")
t.B("Afrikadagi oxirgi mustamlaka rejimi qaysi mamlakatdagi aparteid tuzumi edi?", "Janubiy Afrika Respublikasi", "Nigeriya", "Kongo", "Angola", "Janubiy Afrika Respublikasidagi aparteid.")
t.B("«Aparteid» so‘zi qanday ma’noni bildiradi?", "alohida-alohida yashash (irqiy kamsitish)", "birgalikda yashash", "mustaqillik", "inqilob", "Aparteid – irqiy kamsitishning eng ashaddiy ko‘rinishi.")
t.B("Etnik, diniy belgilar asosida xalqlarni qirg‘in qilish qanday ataladi?", "genotsid", "aparteid", "sanksiya", "intervensiya", "Genotsid.")
t.NAT("Mustamlaka davridan qolgan chegaralar etnik mansublikni hisobga olmagan.", "doimiy etnik mojarolar va millionlab qochoqlar paydo bo‘ldi", "etnik tinchlik o‘rnatildi", "Afrika birlashdi", "chegaralar o‘zgarmadi",
      "Sun’iy chegaralar etnik mojarolarga olib keldi.")
t.NAT("Tajribasiz va korrupsiyaga botgan byurokratik apparat vujudga keldi.", "yagona tartibli kuch bo‘lgan armiya to‘xtovsiz harbiy to‘ntarishlar uyushtirdi", "demokratiya mustahkamlandi", "iqtisod gullab-yashnadi", "armiya tarqatildi",
      "Natijada to‘xtovsiz harbiy to‘ntarishlar yuz berdi.")
t.NAT("Qashshoqlik, urush va ishsizlik davom etdi.", "millionlab afrikaliklar qit’ani tashlab, Yevropaga ko‘chdi", "Afrika aholisi boyidi", "Yevropaliklar Afrikaga qaytdi", "migratsiya to‘xtadi",
      "Millionlab afrikaliklar Britaniya, Fransiyada istiqomat qilmoqda.")
t.TF("Barcha afrikaliklar aparteid tuzumini qoralashda yakdil bo‘lgan.", True, "To‘g‘ri.")
t.TF("Mustaqillikdan so‘ng Afrika davlatlari darhol dunyoning eng boy davlatlariga aylangan.", False, "Noto‘g‘ri: ko‘plari eng kambag‘al davlatlardan bo‘lib qolaverdi.")
t.MUL([("V Panafrika kongressida mustamlakachilikka qarshi ruh ustuvor bo‘lgan.", True), ("«Afrika yili»da mustaqil bo‘lganlarning ko‘pchiligi fransuz va ingliz mustamlakalari edi.", True), ("Kapitalistik yo‘lni tanlagan davlatlarda hech qanday muammo bo‘lmagan.", False)],
      "III noto‘g‘ri: ularda ham deyarli bir xil muammolar paydo bo‘ldi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["V Panafrika kongressi", "«Afrika yili»", "Portugaliya mustamlakalari mustaqil bo‘ldi", "Sahroyi Kabirdan janubda 40 dan ortiq davlat"],
      "1945 → 1960 → 1975 → 1990-yillar.")
t.MAPMATCH(AF, ['Nigeriya', 'Kongo', 'Somali', 'Janubiy Afrika Respublikasi'],
           ["1960-yilda mustaqil bo‘lgan Afrikaning eng katta davlatlaridan biri (G‘arbiy Afrika)", "1960-yilda mustaqil bo‘lgan eng katta davlatlardan biri (Markaziy Afrika)", "ikki qismi birlashib, Demokratik Respublika bo‘lgan davlat", "aparteid tuzumi hukm surgan davlat"],
           "1 – Nigeriya; 2 – Kongo; 3 – Somali; 4 – JAR.")
t.VENN("Mustaqillikdan oldin", "Mustaqillikdan keyin",
       [("Yevropa metropoliyalari hukmronligi", 1), ("mustamlaka boshqaruv tuzumi", 1),
        ("afrikaliklar davlat apparati, armiyani o‘zlari shakllantirgan", 2), ("BMTda teng huquqli ishtirok", 2),
        ("qashshoqlik va etnik muammolar", 3)],
       "Oldin – metropoliya; keyin – o‘z davlati, BMT. Ikkala davrda qashshoqlik va etnik muammolar.")

# 29 Fan va madaniyat
t = Topic('e10j29', 1029); TOPICS['e10j29'] = t
t.B("Ilmiy-texnik inqilob jahon iqtisodiyotini qaysi davrga olib chiqqan?", "kapitalizmning postindustrial davriga", "feodalizmga", "manufaktura davriga", "agrar davrga", "Postindustrial davrga.")
t.B("Dunyoda birinchi Yerning sun’iy yo‘ldoshi qachon uchirilgan?", "1957-yil 4-oktabrda", "1961-yil 12-aprelda", "1969-yilda", "1960-yilda", "1957-yil 4-oktabr kuni SSSRda.")
t.B("Oyga kosmik kema uchirish tadqiqotlariga kim boshchilik qilgan?", "akademik S.P. Korolyov", "Yuriy Gagarin", "N.G. Basov", "D. Kilbi", "Akademik S.P. Korolyov.")
t.B("Yuriy Gagarin qachon koinotga parvoz qilgan?", "1961-yil 12-aprelda", "1957-yil 4-oktabrda", "1969-yilda", "1965-yilda", "1961-yil 12-aprel kuni.")
t.B("Gagarin qaysi kosmik kemada parvoz qilgan?", "«Vostok»", "«Soyuz»", "«Apollon»", "«Sputnik»", "«Vostok» kosmik kemasida.")
t.B("Lazer qachon yaratilgan?", "1960-yilda", "1957-yilda", "1969-yilda", "1972-yilda", "1960-yili.")
t.B("Lazerni yaratgan olimlar kimlar?", "Basov, Proxorov va Tauns", "Kilbi va Noys", "Korolyov va Gagarin", "Fermi va Fleming", "N.G. Basov, A.M. Proxorov va Ch. Tauns.")
t.B("Yarimo‘tkazgichli integral mikrosxemalarni kim yaratgan?", "D. Kilbi va R. Noys", "Basov va Proxorov", "Ericsson va Philips", "Korolyov", "1959-yili amerikalik injenerlar D. Kilbi va R. Noys.")
t.B("Kompyuter dastlab qanday nomlangan?", "elektron hisoblash mashinasi (EHM)", "ARPANET", "MTS", "lazer", "Elektron hisoblash mashinasi – EHM.")
t.B("Uyali telefonlar ustida 1940-yillar oxiridayoq ish boshlagan kompaniya qaysi?", "Shvetsiyaning Televerket kompaniyasi", "Philips", "IBM", "Ericsson", "Televerket kompaniyasi.")
t.B("Internetning o‘tmishdoshi ARPANET qachon yaratilgan?", "1969-yilda", "1972-yilda", "1959-yilda", "1980-yilda", "1969-yili.")
t.B("Elektron pochta (E-mail) qachon paydo bo‘lgan?", "1972-yilda", "1969-yilda", "1980-yilda", "1991-yilda", "1972-yili.")
t.B("Fotografiyaga javob tarzida paydo bo‘lgan mavhum san’at yo‘nalishi qanday ataladi?", "abstraksionizm", "pop-art", "realizm", "postmodernizm", "Abstraksionizm.")
t.B("Abstraksionizmga qarama-qarshi paydo bo‘lgan ommaviy san’at qanday ataladi?", "pop-art", "postmodernizm", "patsifizm", "realizm", "Pop-art.")
t.B("Tinchlik uchun, urushga qarshi harakat mafkurasi qanday ataladi?", "patsifizm", "abstraksionizm", "fundamentalizm", "militarizm", "Patsifizm.")
t.NAT("«Sovuq urush»dagi qurollanish poygasi kosmos sohasiga ko‘chdi.", "1957-yilda birinchi sun’iy yo‘ldosh, 1961-yilda birinchi inson koinotga uchdi", "kosmik tadqiqotlar to‘xtadi", "AQSH va SSSR ittifoq tuzdi", "Oy bosib olindi",
      "Kosmonavtika davri boshlandi.")
t.NAT("Yarimo‘tkazgichli integral mikrosxemalar yaratildi.", "kompyuter va boshqa asboblar hajmi keskin qisqarib, faoliyat sohasi kengaydi", "kompyuterlar kattalashdi", "lazer kashf etildi", "telefonlar yo‘qoldi",
      "Bu XX asr so‘nggi 50 yilidagi eng mashhur ixtiro deb ataldi.")
t.TF("Lazer kashfiyotchilariga fizika sohasida Nobel mukofoti berilgan.", True, "To‘g‘ri.")
t.TF("Ommaviy adabiyot asarlari yuksak badiiy qiymati bilan ajralib turadi.", False, "Noto‘g‘ri: ular badiiy jihatdan unchalik yuksak emas, tijoriy xarakterga ega.")
t.MUL([("Massachuset texnologiya instituti xodimlari masofadan kompyuter aloqasi mumkinligini asoslagan.", True), ("Postmodernizm G‘arb va Sharq, o‘tmish va zamonaviy uslublarni jamlagan.", True), ("Birinchi sun’iy yo‘ldosh AQShda uchirilgan.", False)],
      "III noto‘g‘ri: birinchi sun’iy yo‘ldosh Sovet Ittifoqida uchirilgan.")
t.MATCH("Kashfiyotlarni mualliflari bilan moslashtiring.", ["Lazer", "Integral mikrosxema", "Kosmik kema tadqiqotlari"], ["Basov, Proxorov, Tauns", "Kilbi va Noys", "S.P. Korolyov", "Fleming"], 'abc',
        "Lazer – Basov, Proxorov, Tauns; mikrosxema – Kilbi va Noys; kosmos – Korolyov.")
t.CHR("Kashfiyotlarni xronologik ketma-ketlikda joylashtiring.", ["Sun’iy yo‘ldosh uchirildi", "Integral mikrosxema yaratildi", "Lazer yaratildi", "Gagarin parvozi", "ARPANET yaratildi", "E-mail paydo bo‘ldi"],
      "1957 → 1959 → 1960 → 1961 → 1969 → 1972.")
t.VENN("Abstraksionizm", "Pop-art",
       [("tasvirda harakat va hissiyotni ifodalashga intilgan", 1), ("fotografiyaga javob tarzida paydo bo‘lgan", 1),
        ("har qanday buyum badiiy sifat kasb etishi mumkin, deb hisoblagan", 2), ("ommaviy san’at deb atalgan", 2),
        ("XX asrning ikkinchi yarmidagi san’at yo‘nalishi", 3)],
       "Abstraksionizm – hissiyot; pop-art – buyum estetikasi. Ikkalasi XX asr 2-yarmi san’ati.")
