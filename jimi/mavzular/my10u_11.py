from qlib import Topic, PLACES, REG
TOPICS = {}

# 22-mavzu. Islohotlar, kollektivlashtirish, industrlashtirish
t = Topic('y10u22', 10022); TOPICS['y10u22'] = t
t.B("Yer-suv islohotining ikkinchi bosqichi qaysi yillarda o‘tkazilgan?", "1925–1929", "1921–1922", "1930–1932", "1918–1920", "1925–1929.")
t.B("Rasmiy hujjatlarda katta yer egalari qanday atalgan?", "«quloqlar» – «mushtumzo‘rlar»", "«tekinxo‘rlar»", "«bosmachilar»", "«batraklar»", "«Quloqlar» – «mushtumzo‘rlar».")
t.B("«Agrar inqilob»ning strategiya va taktikasi qachon tasdiqlangan?", "1925-yil noyabrda", "1930-yilda", "1924-yil oktyabrda", "1932-yilda", "1925-yil noyabr.")
t.B("Toshkent va Samarqand viloyatlarida necha desyatinadan ortiq yerlar davlat fondiga o‘tkazilgan?", "40–50 desyatina va undan ortiq", "7–10 desyatina", "100 desyatina", "5 desyatina", "40–50 desyatina va undan ortiq.")
t.B("1925–1929-yillarda nechtaga yaqin boy xo‘jalik tugatilgan?", "5 000 ga yaqin", "23 000", "500", "50 000", "5 000 ga yaqin.")
t.B("Boy xo‘jalikning o‘ziga qancha yer qoldirilishi mumkin edi?", "7–10 desyatinagacha", "40–50 desyatina", "1 desyatina", "100 desyatina", "7–10 desyatina.")
t.B("«Kollektivlashtirish va quloq xo‘jaliklarini tugatish to‘g‘risida»gi qaror qachon qabul qilingan?", "1930-yilda", "1925-yilda", "1932-yilda", "1939-yilda", "1930-yilda.")
t.B("Dehqon xo‘jaliklarining necha foizi kolxoz va sovxozlarga birlashdi?", "75 foizi", "50 foizi", "100 foizi", "25 foizi", "75 foizi.")
t.B("O‘zbekistonda kollektivlashtirish rasman qachon tugallangan?", "1932-yilda", "1930-yilda", "1939-yilda", "1929-yilda", "1932-yilda.")
t.B("O‘zbekistonda yakka dehqon xo‘jaliklariga qachon butkul barham berilgan?", "1939-yilga kelib", "1932-yilda", "1930-yilda", "1945-yilda", "1939-yilga kelib.")
t.B("1927-yilda O‘zSSR xalq xo‘jaligida qishloq xo‘jaligining salmog‘i qancha bo‘lgan?", "62,6 %", "37,4 %", "90 %", "50 %", "62,6 % (sanoat – 37,4 %).")
t.B("Birinchi besh yillik davrida O‘zbekistonda nechta yangi sanoat korxonasi qurilgan?", "289 ta", "28 ta", "2890 ta", "100 ta", "289 ta.")
t.B("O‘rta Osiyoda qishloq xo‘jaligi mashinasozligining to‘ng‘ichi qaysi zavod?", "Toshkent qishloq xo‘jaligi mashinasozligi zavodi", "Chirchiq elektr kimyo kombinati", "Toshkent to‘qimachilik kombinati", "Olmaliq kombinati", "Toshkent qishloq xo‘jaligi mashinasozligi zavodi.")
t.B("XX asr 30-yillarida qanday GESlar kaskadi barpo etilgan?", "Chirchiq–Bo‘zsuv", "Farhod", "Chorvoq", "Norin", "Chirchiq–Bo‘zsuv GESlar kaskadi.")
t.B("«Davlat apparatini mahalliylashtirish Markaziy komissiyasi»ga kim raislik qilgan?", "Bobon Mavlonbekov", "Fayzulla Xo‘jayev", "Akmal Ikromov", "Rahim Inog‘omov", "Bobon Mavlonbekov.")
t.B("Mahalliylashtirish komissiyasi qachon tuzilgan?", "1925-yil martda", "1927-yilda", "1931-yilda", "1925-yil noyabrda", "1925-yil mart.")
t.B("1927-yilda komissiya qanday nom oldi?", "«Davlat apparati va sanoatni O‘zbeklashtirish Markaziy komissiyasi»", "«Ruslashtirish komissiyasi»", "«Kadrlar komissiyasi»", "«Milliy markaz»", "O‘zbeklashtirish Markaziy komissiyasi.")
t.B("O‘zbeklashtirish komissiyasi faoliyati qachon to‘xtatilgan?", "1931-yilda", "1927-yilda", "1939-yilda", "1925-yilda", "1931-yil SSSR MIK qarori bilan.")
t.NAT("Kollektivlashtirish mutasaddilari kolxozga kirmaganlarni suvdan mahrum qilish, surgun bilan qo‘rqitdi.", "ko‘pchilik tumanlarda kollektivlashtirish bir necha hafta ichida amalga oshirildi", "dehqonlar kolxozdan chiqdi", "kollektivlashtirish to‘xtatildi", "yakka xo‘jaliklar ko‘paydi", "Majburiy kollektivlashtirish.")
t.NAT("Industrlashtirish qishloq hisobidan amalga oshirildi, xarid narxlari pasaytirildi.", "dehqonlar qashshoqlashib, oziq-ovqat muammosi keskinlashdi", "dehqonlar boyidi", "narxlar oshdi", "oziq-ovqat mo‘l bo‘ldi", "Qashshoqlik va oziq-ovqat muammosi.")
t.NAT("Yakka xo‘jaliklarga majburiy topshiriladigan mahsulot hajmi kolxozlarga nisbatan 50 foiz ko‘paytirildi.", "yakka xo‘jaliklarga iqtisodiy tazyiq kuchayib, 1939-yilga kelib ular tugatildi", "yakka xo‘jaliklar ko‘paydi", "kolxozlar tarqaldi", "soliqlar kamaydi", "Yakka xo‘jaliklar tugatildi.")
t.NAT("1931-yilda mahalliylashtirish «burjua millatchiligi» deb e’lon qilindi.", "o‘zbeklashtirish siyosatiga zarba berilib, ruslashtirish yangi bosqichga o‘tdi", "o‘zbek tili davlat tili bo‘ldi", "milliy kadrlar ko‘paydi", "ruslashtirish to‘xtadi", "Ruslashtirish kuchaydi.")
t.TF("Yer bilan birga ishchi hayvonlari va dehqonchilik asbob-uskunalari ham musodara qilingan.", True, "To‘g‘ri.")
t.TF("1927-yilda sanoat ishlab chiqarishining asosiy qismi mashinasozlikka asoslangan edi.", False, "Noto‘g‘ri: 90 foizi qishloq xo‘jaligi xomashyosini qayta ishlashga asoslangan edi.")
t.TF4([("Quloqlikka tortilganlarning qaytishi taxminan 1934–1956-yillarni qamrab olgan.", True), ("Sanoatga malakali ishchilar RSFSRdan olib kelingan.", True),
       ("1925-yil noyabrda Kompartiyaning II syezdi Samarqandda bo‘lgan.", True), ("Birinchi besh yillik 1925–1929-yillarni qamragan.", False)],
      "4-noto‘g‘ri: 1928-yil oktyabr – 1932-yil dekabr.")
t.MUL([("23 000 dan ortiq o‘ziga to‘q xo‘jaliklarning «ortiqcha» yerlari tortib olingan.", True),
       ("Davlat va xo‘jalik organlarida ish yuritish rus tilida bo‘lgan.", True),
       ("Industrlashtirish natijasida O‘zbekiston sanoati har tomonlama rivojlangan.", False)],
      "III noto‘g‘ri: sanoat bir tomonlama, xomashyo yo‘nalishida ixtisoslashgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["mahalliylashtirish komissiyasi tuzildi", "«Agrar inqilob» strategiyasi tasdiqlandi", "komissiya o‘zbeklashtirish komissiyasi deb ataldi", "birinchi besh yillik boshlandi", "kollektivlashtirish qarori", "o‘zbeklashtirish komissiyasi to‘xtatildi"],
      "1925-03 → 1925-11 → 1927 → 1928-10 → 1930 → 1931.")
t.MATCH("Atamalarni izohi bilan moslashtiring.", ["kolxoz", "sovxoz", "quloq", "mahalliylashtirish"],
        ["jamoa xo‘jaligi", "davlat xo‘jaligi", "katta yer egasi – «mushtumzo‘r»", "boshqaruvga mahalliy kadrlarni jalb etish", "yakka dehqon"], 'abcd',
        "Kolxoz – jamoa; sovxoz – davlat; quloq – mushtumzo‘r; mahalliylashtirish – milliy kadrlar.")
t.VENN("Kollektivlashtirish", "Industrlashtirish",
       [("1932-yilda rasman tugallangan", 1), ("kolxoz va sovxozlar tuzildi", 1),
        ("289 ta yangi korxona qurildi", 2), ("Chirchiq elektr kimyo kombinati", 2),
        ("sovet hokimiyatining majburiy siyosati", 3)],
       "Kollektivlashtirish – kolxoz, 1932; industrlashtirish – 289 korxona; ikkalasi sovet siyosati.")
t.MAPN('uzb', ['Samarqand', 'Toshkent', 'Buxoro', 'Xiva'], "1925-yil noyabrda «mahalliy aholini jalb qilish» masalasi ko‘rilgan Kompartiya II syezdi bo‘lgan shahar xaritada qaysi raqamda?",
       "Samarqand.")
