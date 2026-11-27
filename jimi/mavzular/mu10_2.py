from qlib import Topic, PLACES, REG
TOPICS = {}
CA = 'ca'
PLACES.update({'Jalolobod': (73.0, 40.93), 'Skobelev (Farg‘ona)': (71.78, 40.38)})

# 5-§. Turkiston ASSRda sovet hokimiyatiga qarshi qurolli harakatlar
t = Topic('e10u5', 10105); TOPICS['e10u5'] = t
t.B("Turkistonda sovet rejimiga qarshi istiqlolchilik harakati qachon va qayerda boshlandi?", "1918-yil fevralning so‘nggi o‘n kunligida Qo‘qon atroflarida", "1918-yil martda Samarqandda", "1919-yil kuzida Andijonda", "1920-yil avgustda Buxoroda", "1918-yil fevralning so‘nggi o‘n kunligida, dastlab Qo‘qon atroflarida.")
t.B("Kichik Ergash va Katta Ergash qaysi qishloqdan bo‘lgan?", "Bachqir", "Pastqishloq", "Ergashtom", "Fathobod", "Qo‘qon atrofidagi Bachqir qishlog‘idan.")
t.B("Kichik Ergash qachon shahid bo‘ldi?", "1918-yil 27-fevralda", "1918-yil 22-fevralda", "1919-yil 12-oktyabrda", "1920-yil mayda", "27-fevraldagi janglarning birida.")
t.B("Marg‘ilonda istiqlol kurashini kim boshladi?", "Madaminbek (Muhammad Aminbek Ahmadbek o‘g‘li)", "Shermuhammadbek", "Katta Ergash", "Islom Polvon", "Militsiyaning sobiq boshlig‘i Madaminbek.")
t.B("1918-yil o‘rtalarida Farg‘ona vodiysida taxminan nechta qo‘rboshi kurash olib borgan?", "100 ga yaqin", "30 dan ortiq", "200 dan ortiq", "50 ga yaqin", "Taxminan 100 ga yaqin qo‘rboshi.")
t.B("Sovet hujjatlarida istiqlolchilik harakati qanday noto‘g‘ri nom bilan atalgan?", "“bosmachilik”", "“jadidchilik”", "“qadimchilik”", "“muxtoriyatchilik”", "Harakat “bosmachilik”, qatnashchilari “bosmachilar” deb soxtalashtirildi.")
t.B("Istiqlolchilik harakatining asosiy maqsadi nima edi?", "Turkiston mustaqilligi uchun kurash", "amir hokimiyatini tiklash", "Rossiya tarkibida qolish", "sovet hokimiyatini mustahkamlash", "Asosiy maqsad Turkiston mustaqilligi uchun kurash bo‘lib qolaverdi.")
t.B("Farg‘ona muvaqqat muxtoriyat hukumati qachon tuzildi?", "1919-yil 12-oktyabrda", "1920-yil 3-mayda", "1920-yil 6-martda", "1921-yil 13-sentyabrda", "1919-yil 12-oktyabrda Ergashtom ovulida.")
t.B("Farg‘ona muvaqqat muxtoriyat hukumati qayerda tuzildi?", "Pomirning Ergashtom ovulida", "Qo‘qonda", "Skobelevda", "Bachqir qishlog‘ida", "Pomirning Ergashtom ovulidagi anjumanda.")
t.B("1919-yil kech kuzida Madaminbek qo‘l ostida qancha yigit bo‘lgan?", "30 000 ga yaqin", "20 000", "8000", "2000", "Madaminbekda 30 000, Shermuhammadbekda 20 000, Katta Ergashda 8000.")
t.B("Madaminbek bilan yarash bitimi qachon va qayerda imzolandi?", "1920-yil 6-martda Skobelevda", "1920-yil 3-mayda Andijonda", "1919-yil 12-oktyabrda Ergashtomda", "1918-yil 22-fevralda Qo‘qonda", "1920-yil 6-martda Skobelev shahrida N.Veryovkin-Roxalskiy bilan.")
t.B("Turkiston – turk mustaqil islom jumhuriyati qachon tashkil topdi?", "1920-yil 3-mayda", "1920-yil 6-martda", "1919-yil 12-oktyabrda", "1921-yil noyabrda", "1920-yil 3-mayda Shermuhammadbek boshchiligida.")
t.B("Farg‘ona vodiysida favqulodda holat qachon e’lon qilindi?", "1921-yil 13-sentyabrda", "1921-yil noyabrda", "1920-yil mayda", "1923-yil 10-mayda", "1921-yil 13-sentyabrda.")
t.B("1921-yil noyabrda Farg‘ona viloyatining harbiy diktatori qilib kim tayinlandi?", "P.Baranov", "M.V.Frunze", "N.Veryovkin-Roxalskiy", "Ye.Perfilev", "Turkfront harbiy inqilobiy kengashi a’zosi P.Baranov.")
t.B("Shermuhammadbek Afg‘onistonga o‘tib ketgach, 1923 – 1924-yillarda vodiy istiqlolchilariga kimlar rahbarlik qildi?", "Islom Polvon va Yormat Maxsum", "Bahrombek va Ochilbek", "Katta Ergash va Madaminbek", "Hamroqulbek va Shahriyor", "Islom Polvon va Yormat Maxsum.")
t.B("Samarqand viloyatida 1918 – 1923-yillarda istiqlolchilarga qaysi qo‘rboshilar rahbarlik qilgan?", "Bahrombek va Ochilbek", "Madaminbek va Shermuhammadbek", "Islom Polvon va Yormat Maxsum", "Kichik va Katta Ergash", "Bahrombek va Ochilbek.")
t.B("Ochilbek qachon va qayerda halok bo‘ldi?", "1923-yil 10-mayda Kitob atrofida", "1922-yil kuzida Samarqandda", "1920-yil mayda Farg‘onada", "1918-yil 27-fevralda Qo‘qonda", "1923-yil 10-mayda Kitob atrofida.")
t.B("Xalq orasida jasurligi uchun “Ochildov” nomi bilan mashhur bo‘lgan qo‘rboshi kim?", "Ochilbek", "Bahrombek", "Hamroqulbek", "Yormat Maxsum", "Ochilbek – “Ochildov”.")
t.B("Qo‘rboshilarning nechtadan ortiq qurultoylari bo‘lib o‘tgan?", "30 dan ortiq", "10 dan ortiq", "100 dan ortiq", "5 ta", "Farg‘ona, Buxoro va Xorazmda 30 dan ortiq qurultoy.")
t.NAT("1920-yil yanvar o‘rtalariga kelib Farg‘ona vodiysiga bolsheviklarning qo‘shimcha kuchlari kela boshladi.", "jangovar tashabbus qizil armiya qo‘liga o‘tdi", "Madaminbek Andijonni egalladi", "Farg‘ona muxtoriyati tuzildi", "istiqlolchilik harakati tugadi", "Tashabbus qizil armiya qo‘liga o‘tdi.")
t.NAT("Yetti yillik kurash, iqtisodiy inqiroz va ocharchilik xalqni charchatdi.", "1924-yil oxirida istiqlolchilik harakatining birinchi davri yakunlandi", "Turkiston mustaqil bo‘ldi", "Madaminbek hukumati tuzildi", "harbiy diktatura o‘rnatildi", "Qo‘rboshilarning ko‘pchiligi 1924-yilda qarshilikni to‘xtatdi.")
t.TF("Istiqlolchilik harakati saflarida ba’zi yevropaliklar, hatto ruslar ham bo‘lgan.", True, "To‘g‘ri.")
t.TF("Farg‘ona muvaqqat muxtoriyat hukumati tarkibiga faqat tub aholi vakillari kiritilgan.", False, "Noto‘g‘ri: tarkibda 16 nafar tub aholi va 8 nafar rus bo‘lgan.")
t.MUL([("Madaminbek lashkarlari 1919-yil sentyabrda Jalolobod va O‘sh shaharlarini egallashdi.", True),
       ("Bahrombek va ukasi Shahriyor 1922-yil kuzida Samarqandda otib tashlandi.", True),
       ("Madaminbek 1920-yil mayda Andijonni qamal qilish paytida jangda halok bo‘ldi.", False)],
      "III noto‘g‘ri: Madaminbek qo‘rboshilar o‘rdasiga yuborilib, noaniq vaziyatda o‘ldirilgan.")
t.MATCH("Qo‘rboshilarni ular bilan bog‘liq ma’lumotlar bilan moslashtiring.", ["Madaminbek", "Shermuhammadbek", "Bahrombek", "Ochilbek"],
        ["“Turkiston milliy birligi” ko‘rsatmalari asosida faoliyat ko‘rsatgan", "Farg‘ona muvaqqat muxtoriyat hukumati boshlig‘i", "Turkiston – turk mustaqil islom jumhuriyati boshlig‘i", "1918-yildan 2000 yigit bilan Samarqandda kurashgan"],
        "bcda", "Madaminbek – Farg‘ona hukumati; Shermuhammadbek – Turk jumhuriyati; Bahrombek – Samarqand, 2000 yigit; Ochilbek – “Turkiston milliy birligi”.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["Kichik Ergashning shahid bo‘lishi", "Farg‘ona muvaqqat muxtoriyat hukumatining tuzilishi", "Skobelevda yarash bitimining imzolanishi",
       "Turkiston – turk mustaqil islom jumhuriyatining tashkil topishi", "Farg‘ona vodiysida favqulodda holat e’lon qilinishi"],
      "1918-yil 27-fevral → 1919-yil 12-oktyabr → 1920-yil 6-mart → 1920-yil 3-may → 1921-yil 13-sentyabr.")
t.MAPMATCH('fargona', ['Andijon', 'Skobelev (Farg‘ona)', 'Jalolobod', 'Qo‘qon'],
           ["Madaminbek lashkarlari qamal qilgan vodiydagi eng yirik strategik shahar", "1920-yil 6-martda yarash bitimi imzolangan shahar",
            "1919-yil sentyabrda Madaminbek egallagan shaharlardan biri (O‘sh bilan birga)", "istiqlolchilik harakati dastlab atroflarida boshlangan shahar"],
           "1 – Andijon; 2 – Skobelev; 3 – Jalolobod; 4 – Qo‘qon.")
t.VENN("Madaminbek", "Shermuhammadbek",
       [("Farg‘ona muvaqqat muxtoriyat hukumati boshlig‘i", 1), ("1920-yil 6-martda yarash bitimi imzolagan", 1),
        ("Turkiston – turk mustaqil islom jumhuriyatini boshqargan", 2), ("Afg‘onistonga o‘tib ketgan", 2),
        ("Farg‘ona vodiysidagi qo‘rboshi", 3), ("1919-yil kuzida vodiydagi uch lashkarboshidan biri", 3)],
       "Madaminbek – hukumat boshlig‘i, yarash bitimi; Shermuhammadbek – Turk jumhuriyati, Afg‘onistonga o‘tgan; ikkalasi vodiy qo‘rboshilari.")

# 6-§. Buxoro amirligi, amir hokimiyatining ag‘darilishi, BXSR
t = Topic('e10u6', 10106); TOPICS['e10u6'] = t
t.B("Amir Sayid Olimxon e’tirof etishicha, qaysi hukumat Buxoro davlatining mustaqilligini tan olgan?", "Rossiya Muvaqqat hukumati", "Turkiston o‘lka XKS", "Turkiston Muxtoriyati", "Afg‘oniston hukumati", "Muvaqqat hukumat Buxoro mustaqilligini tan olgan.")
t.B("Yosh buxoroliklar partiyasi dastlab qanday boshqaruv o‘rnatish tarafdori bo‘lgan?", "konstitutsiyaviy monarxiya", "sovet respublikasi", "mutlaq monarxiya", "harbiy diktatura", "Konstitutsiyaviy monarxiya orqali amir hokimiyatini cheklash.")
t.B("Yosh buxoroliklar ichida faol harakatlarni qo‘llovchi yosh jadidlarga kimlar yetakchilik qildi?", "Abdurauf Fitrat va Fayzulla Xo‘jayev", "Abdulvohid Munzim va Sadriddin Ayniy", "Usmon Xo‘ja va Porso Xo‘jayev", "Mirza Salimbek va Abdulqodir Muhitdinov", "Yosh jadidlar – Fitrat va Fayzulla Xo‘jayev.")
t.B("Amir Sayid Olimxon islohotlar to‘g‘risidagi farmonni qachon imzoladi?", "1917-yil 7-aprelda", "1917-yil 8-aprelda", "1917-yil 14-aprelda", "1917-yil 2-dekabrda", "1917-yil 7-aprelda; 14-aprelda bekor qilindi.")
t.B("Buxoroda amirlik tuzumini ag‘darish to‘g‘risidagi qaror qayerda qabul qilindi?", "Yangi Buxoro (Kogon)da rus manzilgohlari Sovetlarining II syezdida", "Toshkentda Sovetlar III syezdida", "Samarqandda viloyat syezdida", "Qo‘qonda IV qurultoyda", "1917-yil 2-dekabrda Yangi Buxoroda.")
t.B("F.Kolesov boshchiligidagi qo‘shin necha kishidan iborat bo‘lgan?", "3500 kishi", "7000 kishi", "15 000 kishi", "2000 kishi", "3500 kishidan iborat harbiy kuchlar.")
t.B("Kolesov qo‘shini Yangi Buxoroga qachon yetib keldi?", "1918-yil 1-martda", "1918-yil 2-martda", "1918-yil 5-martda", "1918-yil 17-martda", "1918-yil 1-martda.")
t.B("Buxoroliklar temiryo‘l izlarini qaysi oraliqda buzib tashladi?", "Karmanadan Qorako‘lgacha (170 km)", "Samarqanddan Kattaqo‘rg‘ongacha", "Kogondan Chorjo‘ygacha", "Toshkentdan Samarqandgacha", "Karmanadan Qorako‘lgacha 170 km masofada.")
t.B("Sovet Turkistoni bilan Buxoro amirligi o‘rtasida qanday bitim imzolandi?", "Qiziltepa bitimi (1918-yil 25-mart)", "Skobelev bitimi", "Qo‘qon “tinchlik shartnomasi”", "Kogon bitimi", "1918-yil 25-martda Qiziltepa bitimi.")
t.B("Qiziltepa bitimini amir nomidan kim imzoladi?", "bosh zakotchi Mirza Salimbek", "qo‘shbegi", "Sayid Olimxon", "Abdulvohid Munzim", "Bosh zakotchi Mirza Salimbek.")
t.B("Mirza Salimbek qaysi tarixiy asar muallifi?", "“Tarixi Salimiy”", "“Tarixi nafoe”", "“Turkiston qayg‘usi”", "“Tarixi Muqimxoniy”", "Kolesov voqealari “Tarixi Salimiy”da aks etgan.")
t.B("M.V.Frunze Samarqand-Buxoro guruhini tuzish haqida qachon buyruq berdi?", "1920-yil 12-avgustda", "1920-yil 29-avgustda", "1920-yil 2-sentyabrda", "1920-yil 6-oktyabrda", "1920-yil 12-avgustda.")
t.B("Frunze qo‘shinlarining qaysi zarbdor guruhiga asosiy vazifa yuklandi?", "Kogon guruhi", "Samarqand guruhi", "Kattaqo‘rg‘on guruhi", "Chorjo‘y guruhi", "Kogon guruhi poytaxtni egallashi kerak edi.")
t.B("Buxoro shahri qizil armiya tomonidan qachon egallandi?", "1920-yil 2-sentyabrda", "1920-yil 29-avgustda", "1920-yil 12-avgustda", "1920-yil 8-oktyabrda", "1920-yil 2-sentyabrda.")
t.B("Buxoroning vayron bo‘lishini “Tarixi nafoe” asarida yozib qoldirgan tarixchi kim?", "Muhammad Ali Baljuvoniy", "Mirza Salimbek", "Sadriddin Ayniy", "Abdurauf Fitrat", "Muhammad Ali Baljuvoniy.")
t.B("BXSR tuzilganligi qayerda e’lon qilindi?", "Sitorai Mohi Xosada, Butunbuxoro xalq vakillarining I qurultoyida", "Yangi Buxoroda, Sovetlar II syezdida", "Buxoro Arkida", "Samarqandda", "1920-yil 6 – 8-oktyabrda amirning yozgi saroyi Sitorai Mohi Xosada.")
t.B("BXSR Nozirlar Sho‘rosining raisi kim bo‘ldi?", "Fayzulla Xo‘jayev", "Abdulqodir Muhitdinov", "Usmon Xo‘ja", "Porso Xo‘jayev", "Fayzulla Xo‘jayev rais va tashqi ishlar noziri.")
t.B("Butunbuxoro Markaziy Inqilobiy Qo‘mitasi raisi kim bo‘ldi?", "Abdulqodir Muhitdinov", "Fayzulla Xo‘jayev", "Muinjon Aminov", "Qori Yo‘ldosh Po‘latov", "Markaziy revkom raisi – Abdulqodir Muhitdinov.")
t.B("BXSR Konstitutsiyasi qachon qabul qilindi?", "1921-yil 18 – 23-sentyabrda", "1920-yil 6 – 8-oktyabrda", "1924-yil 18 – 20-sentyabrda", "1922-yil yanvarda", "Butunbuxoro xalq vakillarining II qurultoyida.")
t.B("BXSR qachon Buxoro Sovet Sotsialistik Respublikasi (BSSR)ga aylantirildi?", "1924-yil 18 – 20-sentyabrda", "1923-yil kuzida", "1921-yil sentyabrda", "1925-yil fevralda", "Butunbuxoro xalq vakillarining V qurultoyida.")
t.B("Fayzulla Xo‘jayev 1922-yilda qaysi shaharga nemis banklari bilan mustaqil shartnoma tuzish uchun bordi?", "Berlin", "Moskva", "Kobul", "Istanbul", "1922-yili Berlinga bordi.")
t.NAT("Kolesovning Buxoroga hujumi barbod bo‘ldi va Qiziltepa bitimi imzolandi.", "Buxoro amirligi harbiy harakatlar uchun javobgar deb topilib, katta tovon to‘lashi belgilandi", "amir hokimiyati ag‘darildi", "Yosh buxoroliklar hokimiyatga keldi", "BXSR tuzildi", "Amirlik aybdor hisoblanib, katta tovon to‘lashga majbur bo‘ldi.")
t.NAT("1923-yil yozi va kuzida tashqi kuchlar tazyiqi kuchaydi.", "Fitrat, Otaulla Xo‘jayev va boshqa nozirlar hukumatdan chiqarilib, surgun qilindi", "BXSR mustaqilligi kuchaydi", "amir hokimiyati tiklandi", "Fayzulla Xo‘jayev iste’foga chiqdi", "F.Xo‘jayevning safdoshlari hukumatdan chiqarildi va surgun qilindi.")
t.TF("Amir Olimxon ixtiyorida 15 000 sarboz, 55 ta eski to‘p va 12 ta pulemyot bo‘lgan.", True, "To‘g‘ri.")
t.TF("Butunbuxoro MIQ raisligini 1922 – 1924-yillarda Usmon Xo‘ja egallagan.", False, "Noto‘g‘ri: Usmon Xo‘ja xorijga ketgach, 1922 – 1924-yillarda bu lavozimni Porso Xo‘jayev egalladi.")
t.MUL([("1920-yil 1 – 2-sentyabrda Buxoroga 12 000 snaryad tashlangan.", True),
       ("Amir Olimxon poytaxtni tashlab, Sharqiy Buxoroga chekingan.", True),
       ("Amirlik xazinasi ortilgan eshelonlar Kogon orqali Afg‘onistonga jo‘natilgan.", False)],
      "III noto‘g‘ri: 2 ta eshelon Samarqand va Toshkent orqali Moskvaga yo‘l olgan.")
t.MATCH("BXSR nozirlarini lavozimlari bilan moslashtiring.", ["Qori Yo‘ldosh Po‘latov", "Muxtorjon Saidjonov", "Usmon Xo‘ja", "Mukammal Burhonov"],
        ["adliya noziri", "moliya noziri", "maorif noziri", "ichki ishlar noziri"],
        "cdba", "Po‘latov – maorif; Saidjonov – ichki ishlar; Usmon Xo‘ja – moliya; Burhonov – adliya.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["Amirning islohotlar to‘g‘risidagi farmoni", "Yangi Buxoroda Sovetlar II syezdi", "Qiziltepa bitimi", "Buxoro shahrining qizil armiya tomonidan egallanishi", "BXSR Konstitutsiyasining qabul qilinishi"],
      "1917-yil 7-aprel → 1917-yil 2-dekabr → 1918-yil 25-mart → 1920-yil 2-sentyabr → 1921-yil sentyabr.")
t.MAPMATCH('buxamir', ['Buxoro', 'Samarqand', 'Karmana'],
           ["1920-yil 2-sentyabrda qizil armiya egallagan amirlik poytaxti", "Kolesov otryadi 1918-yil 17-martda chekinib yetib kelgan shahar", "Kolesov otryadi talagan, temiryo‘l izi shu yerdan Qorako‘lgacha buzilgan shahar"],
           "1 – Buxoro; 2 – Samarqand; 3 – Karmana.")
t.VENN("Kolesov bosqini (1918)", "Frunze bosqini (1920)",
       [("Qiziltepa bitimi bilan yakunlangan", 1), ("3500 kishilik qo‘shin bilan amalga oshirilgan", 1),
        ("amir hokimiyati ag‘darilgan", 2), ("qo‘shinlar 4 ta zarbdor guruhga bo‘lingan", 2),
        ("Buxoro amirligiga qarshi qaratilgan", 3)],
       "Kolesov – 3500 kishi, Qiziltepa bitimi; Frunze – 4 zarbdor guruh, amir ag‘darildi; ikkalasi Buxoro amirligiga qarshi.")
