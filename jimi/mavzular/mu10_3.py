from qlib import Topic
TOPICS = {}
UZ = 'uzb'; FV = 'fargona'; ZR = 'zarafshon'

# 5 Sovet hokimiyatiga qarshi qurolli harakatlar
t = Topic('e10u5', 10005); TOPICS['e10u5'] = t
t.B("Istiqlolchilik harakati qachon va qayerda boshlangan?", "1918-yil fevral oxirida Qo‘qon atroflarida", "1919-yil kuzida Andijonda", "1920-yil mayda Samarqandda", "1917-yil noyabrda Toshkentda", "1918-yil fevralining so‘nggi o‘n kunligida Qo‘qon atroflarida.")
t.B("Dastlabki guruhlar qaysi qishloqdan bo‘lgan qo‘rboshilar nomlari bilan bog‘liq?", "Bachqir", "Ergashtom", "Pastqishloq", "Fathobod", "Qo‘qon atrofidagi Bachqir.")
t.B("Kichik Ergash qachon shahid bo‘lgan?", "1918-yil 27-fevralda", "1918-yil 18-fevralda", "1920-yil mayda", "1921-yil", "27-fevralda.")
t.B("Marg‘ilonda kurash boshlagan militsiyaning sobiq boshlig‘i kim?", "Madaminbek", "Katta Ergash", "Shermuhammadbek", "Bahrombek", "Madaminbek — Muhammad Aminbek Ahmadbek o‘g‘li.")
t.B("1918-yil o‘rtalarida Farg‘ona vodiysida nechtaga yaqin qo‘rboshi kurashgan?", "100 ga yaqin", "10 ga yaqin", "1000 ga yaqin", "200 dan ortiq", "Taxminan 100 ga yaqin.")
t.B("Sovet hujjatlarida istiqlolchilik harakati qanday noto‘g‘ri nom bilan atalgan?", "«bosmachilik»", "«jadidchilik»", "«muxtoriyat»", "«qo‘rboshilik»", "«Bosmachilik».")
t.B("Istiqlolchilik harakatining bosh sababi nima edi?", "sovet hokimiyatining mustamlakachilik va shovinistik siyosati", "ocharchilik", "diniy nizolar", "chet el aralashuvi", "Mustamlakachilik va shovinistik siyosat.")
t.B("«Bosmachilikka qarshi kurash tamomila yangi... dushman bilan kurash» deb yozgan kim?", "M. Frunze", "T. Risqulov", "Lenin", "P. Baranov", "Turkfront qo‘mondoni M. Frunze.")
t.B("Farg‘ona muvaqqat muxtoriyat hukumati qachon tuzilgan?", "1919-yil 12-oktyabrda", "1920-yil 3-mayda", "1918-yil 27-fevralda", "1920-yil 6-martda", "1919-yil 12-oktyabrda.")
t.B("Farg‘ona muvaqqat hukumati qayerda tuzilgan?", "Pomirning Ergashtom ovulida", "Qo‘qonda", "Andijonda", "Skobelevda", "Ergashtom ovulidagi anjumanda.")
t.B("1919-yil kech kuzida Madaminbek qo‘l ostida qancha yigit bo‘lgan?", "30 000 ga yaqin", "20 000", "8000", "2000", "30 000 ga yaqin.")
t.B("Madaminbek va Veryovkin-Roxalskiy o‘rtasida yarash bitimi qachon imzolangan?", "1920-yil 6-martda", "1920-yil 3-mayda", "1919-yil 12-oktyabrda", "1921-yil 13-sentyabrda", "1920-yil 6-martda Skobelevda.")
t.B("Turkiston – turk mustaqil islom jumhuriyati kim boshchiligida tashkil topgan?", "Shermuhammadbek", "Madaminbek", "Katta Ergash", "Islom Polvon", "1920-yil 3-mayda Shermuhammadbek boshchiligida.")
t.B("Farg‘ona viloyatining harbiy diktatori qilib kim tayinlangan?", "P. Baranov", "M. Frunze", "N. Veryovkin-Roxalskiy", "Ye. Perfilev", "P. Baranov, 1921-yil noyabr.")
t.B("1923–1924-yillarda Farg‘ona istiqlolchilariga kimlar rahbarlik qilgan?", "Islom Polvon va Yormat Maxsum", "Madaminbek va Katta Ergash", "Bahrombek va Ochilbek", "Shermuhammadbek va Hamroqulbek", "Islom Polvon va Yormat Maxsum.")
t.B("Samarqand viloyatidagi istiqlolchilarga kimlar rahbarlik qilgan?", "Bahrombek va Ochilbek", "Madaminbek va Shermuhammadbek", "Islom Polvon", "Katta Ergash", "Bahrombek va Ochilbek.")
t.B("Ochilbek qachon va qayerda halok bo‘lgan?", "1923-yil 10-mayda Kitob atrofida", "1922-yil kuzida Samarqandda", "1920-yil mayda Andijonda", "1918-yil fevralda Qo‘qonda", "1923-yil 10-mayda Kitob atrofida.")
t.B("Buxorodagi ayol qo‘rboshi kim bo‘lgan?", "Nodira qiz", "Shakarxon", "Rizvonbibi", "Anbar otin", "Nodira qiz.")
t.B("Qo‘rboshilarning nechtadan ortiq qurultoylari bo‘lib o‘tgan?", "30 dan ortiq", "5 ta", "100 dan ortiq", "10 ta", "30 dan ortiq.")
t.NAT("Farg‘ona vodiysiga bolsheviklar qo‘shimcha kuchlar tashladi.", "1920-yil yanvar o‘rtalarida jangovar tashabbus qizil armiyaga o‘tdi", "istiqlolchilar g‘alaba qozondi", "Madaminbek Toshkentni egalladi", "bolsheviklar chekindi", "Tashabbus qizil armiyaga o‘tdi.")
t.NAT("Yetti yillik kurashdan qo‘rboshilar ham, xalq ham charchadi.", "1924-yil oxirida istiqlolchilik harakatining birinchi davri yakunlandi", "harakat kuchaydi", "Turkiston mustaqil bo‘ldi", "qo‘rboshilar hokimiyatni oldi", "Ko‘pchilik qarshilikni to‘xtatdi.")
t.TF("Istiqlolchilik harakatining asosiy kuchi dehqonlar, chorikorlar, mardikorlar, hunarmandlar va ziyolilar edi.", True, "To‘g‘ri.")
t.TF("Istiqlolchilar safida biror yevropalik bo‘lmagan.", False, "Noto‘g‘ri: ba’zi yevropaliklar, hatto ruslar ham bo‘lgan.")
t.MUL([("Madaminbek hukumatiga 16 nafar tub aholi va 8 nafar rus kiritilgan.", True),
       ("Bahrombek va ukasi Shahriyor 1922-yil kuzida Samarqandda otib tashlangan.", True),
       ("Madaminbek 1925-yilda qizil armiya bilan jangda halok bo‘lgan.", False)],
      "III noto‘g‘ri: Madaminbek 1920-yil mayda noaniq vaziyatda o‘ldirilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Kichik Ergash shahid bo‘ldi", "Farg‘ona muvaqqat muxtoriyat hukumati tuzildi", "Skobelevda yarash bitimi", "Shermuhammadbekning islom jumhuriyati", "Farg‘ona vodiysida favqulodda holat", "Ochilbek halok bo‘ldi"],
      "1918-yil 27-fevral → 1919-yil 12-oktyabr → 1920-yil 6-mart → 3-may → 1921-yil 13-sentyabr → 1923-yil 10-may.")
t.MAPMATCH(FV, ['Jalolobod', 'Marg‘ilon', 'Andijon', 'Qo‘qon'],
           ["1919-yil sentyabrda O‘sh bilan birga Madaminbek egallagan shahar", "Madaminbek militsiya boshlig‘i bo‘lgan, keyin ozod qilingan shahar", "vodiydagi eng yirik strategik shahar, qamal qilingan", "atrofida 1918-yil fevralda istiqlolchilik harakati boshlangan shahar"],
           "1 – Jalolobod; 2 – Marg‘ilon; 3 – Andijon; 4 – Qo‘qon.")
t.VENN("Madaminbek", "Shermuhammadbek",
       [("Farg‘ona muvaqqat muxtoriyat hukumati boshlig‘i", 1), ("1920-yil mayda o‘ldirilgan", 1),
        ("Turkiston – turk mustaqil islom jumhuriyati rahbari", 2), ("Afg‘onistonga o‘tib ketgan", 2),
        ("Farg‘ona vodiysidagi qo‘rboshi", 3)],
       "Madaminbek — muvaqqat hukumat, o‘ldirilgan; Shermuhammadbek — islom jumhuriyati, Afg‘onistonga ketgan.")

# 6 Buxoro amirligi va BXSR
t = Topic('e10u6', 10006); TOPICS['e10u6'] = t
t.B("Buxoroning so‘nggi amiri kim?", "Sayid Olimxon", "Amir Muzaffar", "Abdulahad", "Nasrullo", "Amir Sayid Olimxon (1881–1944).")
t.B("Yosh buxoroliklar dastlab qanday boshqaruv tarafdori bo‘lgan?", "konstitutsiyaviy monarxiya", "sovet respublikasi", "mutlaq monarxiya", "anarxiya", "Amirlik doirasida konstitutsiyaviy monarxiya.")
t.B("Yosh jadidlarga kimlar yetakchilik qilgan?", "Abdurauf Fitrat va Fayzulla Xo‘jayev", "Munzim va Ayniy", "Kolesov va Frunze", "Usmon Xo‘ja va Porso Xo‘jayev", "Fitrat va Fayzulla Xo‘jayev; eski jadidlarga Munzim va Ayniy.")
t.B("Amir islohotlar farmonini qachon imzolagan?", "1917-yil 7-aprelda", "1917-yil 8-aprelda", "1917-yil 14-aprelda", "1918-yil 1-martda", "7-aprelda; 14-aprelda bekor qilingan.")
t.B("Kolesov boshchiligidagi qancha harbiy kuch Yangi Buxoroga yetib kelgan?", "3500 kishi", "7000 kishi", "15 000 kishi", "1000 kishi", "1918-yil 1-martda 3500 kishi.")
t.B("Kolesov otryadi bilan buxoroliklar o‘rtasidagi dastlabki to‘qnashuv qayerda bo‘lgan?", "Fathobodda", "Kogonda", "Qorako‘lda", "Karmanada", "Buxoro yaqinidagi Fathobodda.")
t.B("Amir sarbozlari qancha masofadagi temiryo‘l izlarini buzgan?", "170 km", "17 km", "500 km", "70 km", "Karmanadan Qorako‘lgacha 170 km.")
t.B("Sovet Turkistoni va Buxoro o‘rtasidagi bitim qachon imzolangan?", "1918-yil 25-martda", "1918-yil 17-martda", "1920-yil 2-sentyabrda", "1918-yil 5-martda", "1918-yil 25-martda — Qiziltepa bitimi.")
t.B("Qiziltepa bitimini amir nomidan kim imzolagan?", "bosh zakotchi Mirza Salimbek", "Sayid Olimxon", "Usmon Xo‘ja", "Fayzulla Xo‘jayev", "Mirza Salimbek.")
t.B("«Tarixi Salimiy» asari muallifi kim?", "Mirza Salimbek", "Muhammad Ali Baljuvoniy", "Sadriddin Ayniy", "Fitrat", "Mirza Salimbek.")
t.B("Frunze Samarqand-Buxoro guruhini tuzish haqida qachon buyruq bergan?", "1920-yil 12-avgustda", "1920-yil 29-avgustda", "1920-yil 2-sentyabrda", "1918-yil 1-martda", "1920-yil 12-avgustda.")
t.B("Amir Olimxon ixtiyorida qancha sarboz bo‘lgan?", "15 000", "7000", "2500", "3500", "15 000 sarboz, 55 eski to‘p, 12 pulemyot.")
t.B("Buxoro shahri qizil armiya tomonidan qachon egallangan?", "1920-yil 2-sentyabrda", "1920-yil 29-avgustda", "1920-yil 6-oktyabrda", "1918-yil 2-martda", "1920-yil 2-sentyabrda.")
t.B("«Tarixi nafoe» asari muallifi kim?", "Muhammad Ali Baljuvoniy", "Mirza Salimbek", "Fitrat", "Ayniy", "Muhammad Ali Baljuvoniy.")
t.B("BXSR tuzilganligi qayerda e’lon qilingan?", "Sitorai Mohi Xosada", "Arkda", "Kogonda", "Samarqandda", "1920-yil 6–8-oktyabrda Sitorai Mohi Xosada.")
t.B("BXSR Nozirlar Sho‘rosining raisi kim bo‘lgan?", "Fayzulla Xo‘jayev", "Abdulqodir Muhitdinov", "Usmon Xo‘ja", "Porso Xo‘jayev", "Fayzulla Xo‘jayev.")
t.B("Butunbuxoro Markaziy Ijroiya Qo‘mitasiga avval kim rais bo‘lgan?", "Usmon Xo‘ja", "Porso Xo‘jayev", "Muhitdinov", "Fitrat", "Usmon Xo‘ja; 1922–1924-yillarda Porso Xo‘jayev.")
t.B("BXSR Konstitutsiyasi qaysi qurultoyda qabul qilingan?", "1921-yil 18–23-sentyabrdagi II qurultoyda", "I qurultoyda", "V qurultoyda", "1920-yil oktyabrda", "II qurultoyda.")
t.B("BXSR qachon BSSRga aylantirilgan?", "1924-yil 18–20-sentyabrda", "1921-yilda", "1923-yil kuzida", "1920-yil oktyabrda", "V qurultoyda, 1924-yil 18–20-sentyabr.")
t.NAT("Buxoroliklar Kolesov otryadini qurshab, temiryo‘llarni buzdi.", "Kolesov 5-mart kuni Toshkent tomonga chekinishga buyruq berdi", "Buxoro egallandi", "amir taxtdan voz kechdi", "Yosh buxoroliklar hokimiyatga keldi", "Kolesov chekinib, 17-martda Samarqandga yetdi.")
t.NAT("Buxoro havodan va yerdan qattiq bombardimon qilindi.", "Amir Olimxon obidalar va aholini saqlash uchun Sharqiy Buxoroga chekindi", "Buxoro mustaqil qoldi", "Frunze chekindi", "Yosh buxoroliklar amirni himoya qildi", "Amir Sharqiy Buxoroga chekindi.")
t.TF("1922-yilda Fayzulla Xo‘jayev nemis banklari bilan shartnoma tuzish uchun Berlinga borgan.", True, "To‘g‘ri.")
t.TF("Qiziltepa bitimiga ko‘ra Turkiston Buxoroga tovon to‘lashi belgilangan.", False, "Noto‘g‘ri: Buxoro amirligi tovon to‘lashi belgilangan.")
t.MUL([("Frunze qo‘shinlarini Samarqand, Kattaqo‘rg‘on, Chorjo‘y va Kogon guruhlariga bo‘lgan.", True),
       ("1923-yilda Fitrat, Otaulla Xo‘jayev va boshqa nozirlar hukumatdan chiqarilgan.", True),
       ("BXSR davlat tuzumi jihatidan mutlaq monarxiya edi.", False)],
      "III noto‘g‘ri: BXSR xalq demokratik hokimiyati edi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Amir islohot farmonini imzoladi", "Yangi Buxoroda Sovetlar syezdi", "Qiziltepa bitimi", "Buxoro egallandi", "BXSR e’lon qilindi", "BXSR Konstitutsiyasi qabul qilindi"],
      "1917-yil aprel → 1917-yil dekabr → 1918-yil mart → 1920-yil sentyabr → 1920-yil oktyabr → 1921-yil sentyabr.")
t.MAPMATCH('buxamir', ['Buxoro', 'Karmana', 'Qorako‘l', 'Samarqand'],
           ["Arkdagi amir xazinasi joylashgan, 1920-yil 2-sentyabrda egallangan shahar", "Kolesov otryadi talon-toroj qilgan, temiryo‘l buzilgan uchastka boshlanadigan joy", "buzilgan temiryo‘l uchastkasining ikkinchi chekkasi", "Kolesov chekinib, 17-martda yetib kelgan shahar"],
           "1 – Buxoro; 2 – Karmana; 3 – Qorako‘l; 4 – Samarqand.")
t.VENN("Eski jadidlar", "Yosh jadidlar",
       [("Abdulvohid Burhonov-Munzim", 1), ("Sadriddin Ayniy", 1),
        ("Abdurauf Fitrat", 2), ("Fayzulla Xo‘jayev", 2),
        ("Yosh buxoroliklar harakati a’zolari", 3)],
       "Eski — Munzim, Ayniy (asta-sekin islohot); yosh — Fitrat, Xo‘jayev (faol harakat).")
