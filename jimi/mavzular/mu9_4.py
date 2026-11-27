from qlib import Topic
TOPICS = {}
CA = 'ca'; UZ = 'uzb'

# 8 Turkiston general-gubernatorligining tashkil etilishi
t = Topic('e9u8', 9008); TOPICS['e9u8'] = t
t.B("Turkiston general-gubernatorligi qachon tashkil qilingan?", "1867-yilda", "1865-yilda", "1868-yilda", "1876-yilda", "1867-yilda; shu bilan birga Turkiston harbiy okrugi tuzildi.")
t.B("Turkiston harbiy okrugidagi harbiylar soni qancha bo‘lgan?", "40 ming kishi", "6 ming kishi", "100 ming kishi", "3 ming kishi", "40 ming kishidan iborat bo‘lgan.")
t.B("Turkiston general-gubernatorligining markazi qaysi shahar edi?", "Toshkent", "Samarqand", "Verniy", "Orenburg", "Toshkent shahri.")
t.B("Turkiston general-gubernatorligiga 1867-yilda kim tayinlangan?", "K. P. fon Kaufman", "M. Chernyayev", "F. Romanovskiy", "N. Krijanovskiy", "Konstantin Petrovich fon Kaufman (1867–1881).")
t.B("Kaufman xalq orasida qanday nom olgan?", "«yarim podsho»", "«oq podsho»", "«temir general»", "«Turkiston xoni»", "Katta vakolatlari uchun «yarim podsho».")
t.B("Dastlab Turkiston general-gubernatorligi nechta viloyatga bo‘lingan?", "ikkita", "beshta", "uchta", "to‘rtta", "Sirdaryo va Yettisuv viloyatlari.")
t.B("Yettisuv viloyatining markazi qaysi shahar bo‘lgan?", "Verniy", "Toshkent", "Samarqand", "Ashxobod", "Yettisuv — markazi Verniy.")
t.B("1868-yilda Buxoro amirligiga qarashli yerlarda qanday ma’muriy birlik tashkil qilingan?", "Zarafshon okrugi", "Amudaryo bo‘limi", "Farg‘ona viloyati", "Kaspiyorti viloyati", "Zarafshon okrugi (markazi Samarqand).")
t.B("Amudaryo bo‘limining markazi qaysi shahar bo‘lgan?", "Petro-Aleksandrovsk (To‘rtko‘l)", "Xiva", "Nukus", "Ashxobod", "1873-yil; markazi Petro-Aleksandrovsk (To‘rtko‘l).")
t.B("Farg‘ona viloyati qachon tashkil qilingan?", "1876-yilda", "1868-yilda", "1873-yilda", "1881-yilda", "1876-yilda.")
t.B("Farg‘ona viloyatining markazi qanday atalgan?", "Yangi Marg‘ilon, keyinchalik Skobelev", "Qo‘qon", "Andijon", "Namangan", "Yangi Marg‘ilon, keyinchalik Skobelev — hozirgi Farg‘ona.")
t.B("Kaspiyorti viloyati qachon tashkil qilingan?", "1881-yilda", "1876-yilda", "1873-yilda", "1867-yilda", "1881-yilda, markazi Ashxobod.")
t.B("1 verst necha kilometrga teng?", "1,066 km", "1,5 km", "0,5 km", "2 km", "1 verst — 1,066 km.")
t.B("Sirdaryo viloyatining hududi qaysi gubernadan katta bo‘lgan?", "Moskva gubernasidan", "Saratov gubernasidan", "Orenburg gubernasidan", "Kiyev gubernasidan", "Sirdaryo viloyati Moskva gubernasidan katta.")
t.NAT("O‘rta Osiyo Orenburg general-gubernatorligidan uzoqda joylashgan edi.", "alohida Turkiston general-gubernatorligi tashkil etildi", "Turkiston viloyati tugatildi", "Orenburg poytaxtga aylandi", "hudud Buxoroga qaytarildi", "Uzoqlik alohida general-gubernatorlik tuzish sabablaridan biri bo‘ldi.")
t.NAT("Kaufmanga boshqa guberna boshliqlaridan farqli ravishda katta vakolatlar berildi.", "u xalq orasida «yarim podsho» nomini oldi", "u ishdan olindi", "Turkiston mustaqil bo‘ldi", "general-gubernatorlik tugatildi", "«Yarim podsho» nomini oldi.")
t.TF("Turkiston general-gubernatori bir vaqtda qo‘shinlar qo‘mondoni va bosh sudya hisoblangan.", True, "To‘g‘ri.")
t.TF("Samarqand viloyati o‘lkadagi viloyatlarning hududiy jihatdan eng kattasi bo‘lgan.", False, "Noto‘g‘ri: Samarqand viloyati eng kichigi bo‘lgan.")
t.MUL([("1847-yildan istilochilik yurishlarida qatnashgan barcha harbiy qismlar Turkiston harbiy okrugiga kiritildi.", True),
       ("Kaufman bir paytning o‘zida Turkiston harbiy okrugining qo‘mondoni ham edi.", True),
       ("Sirdaryo viloyatining markazi Verniy shahri bo‘lgan.", False)],
      "III noto‘g‘ri: Sirdaryo viloyatining markazi Toshkent bo‘lgan.")
t.CHR("Ma’muriy birliklarning tashkil topishini xronologik tartibda joylashtiring.", ["Turkiston general-gubernatorligi", "Zarafshon okrugi", "Amudaryo bo‘limi", "Farg‘ona viloyati", "Kaspiyorti viloyati"],
      "1867 → 1868 → 1873 → 1876 → 1881.")
t.MATCH("Ma’muriy birliklarni markazlari bilan moslashtiring.", ["Zarafshon okrugi", "Amudaryo bo‘limi", "Kaspiyorti viloyati", "Yettisuv viloyati"],
        ["Verniy", "Petro-Aleksandrovsk", "Samarqand", "Ashxobod"], "cbda",
        "Zarafshon — Samarqand; Amudaryo — Petro-Aleksandrovsk; Kaspiyorti — Ashxobod; Yettisuv — Verniy.")
t.MAPMATCH('ca2', ['Samarqand', 'Petro-Aleksandrovsk (To‘rtko‘l)', 'Ashxobod', 'Verniy (Almati)'],
           ["Zarafshon okrugi markazi (1868)", "Amudaryo bo‘limi markazi (1873)", "Kaspiyorti viloyati markazi (1881)", "Yettisuv viloyati markazi"],
           "1 – Samarqand; 2 – Petro-Aleksandrovsk; 3 – Ashxobod; 4 – Verniy.")
t.VENN("Sirdaryo viloyati", "Yettisuv viloyati",
       [("markazi Toshkent", 1), ("hududi Moskva gubernasidan katta", 1),
        ("markazi Verniy", 2), ("Sergiopol, Kopal, Olatavsk okruglari yerlarini o‘z ichiga olgan", 2),
        ("dastlabki ikki viloyatdan biri", 3)],
       "Sirdaryo — Toshkent; Yettisuv — Verniy; ikkalasi general-gubernatorlikning dastlabki viloyatlari.")

# 9 Buxoro amirligiga qarshi harbiy harakatlarning boshlanishi
t = Topic('e9u9', 9009); TOPICS['e9u9'] = t
t.B("Mustamlakachilar xonliklarga nisbatan qaysi shiorga amal qilgan?", "«Bo‘lib tashla, hukmronlik qil»", "«Birlikda kuch»", "«Tinchlik va savdo»", "«Kuch adolatda»", "«Bo‘lib tashla, hukmronlik qil».")
t.B("Chernyayev o‘rniga Turkiston viloyatining gubernatori qilib kim tayinlangan?", "F. Romanovskiy", "K. Kaufman", "N. Krijanovskiy", "N. Veryovkin", "F. Romanovskiy.")
t.B("Romanovskiy qanday bahona bilan Buxoroga qarshi yurish boshlashga ruxsat so‘ragan?", "Buxoro Rossiyaga qarshi urushga tayyorlanayotgani", "Buxoroda qo‘zg‘olon bo‘lgani", "Buxoro soliq to‘lamagani", "Angliyaning iltimosi", "Buxoro urushga tayyorlanmoqda, degan bahona bilan.")
t.B("Buxoro qo‘shini bilan birinchi jang qachon va qayerda bo‘lgan?", "1866-yil 8-mayda Erjar yaqinida", "1866-yil 18-oktabrda Jizzaxda", "1866-yil 24-mayda Xo‘jandda", "1865-yil iyunda Toshkentda", "1866-yil 8-mayda Erjar qishlog‘i yaqinida.")
t.B("Xo‘jand qal’asi necha to‘pdan o‘qqa tutilgan?", "20 ta", "100 ta", "6 ta", "12 ta", "20 ta to‘pdan o‘qqa tutildi.")
t.B("Mustamlakachilar Xo‘jand mudofaasini qachon yorib o‘tgan?", "1866-yil 24-mayda", "1866-yil 8-mayda", "1866-yil 12-oktabrda", "1866-yil 18-oktabrda", "24-mayda tunga borib.")
t.B("Orenburg general-gubernatori kim edi?", "N. Krijanovskiy", "F. Romanovskiy", "K. Kaufman", "M. Chernyayev", "N. Krijanovskiy.")
t.B("Krijanovskiy Buxoro amiridan 10 kun ichida qancha tovon talab qilgan?", "100 ming rubl", "1 million rubl", "500 ming rubl", "10 ming rubl", "100 ming rubl.")
t.B("O‘ratepa qamalida shahar necha kun to‘plardan o‘qqa tutilgan?", "uch kun", "bir kun", "o‘n kun", "yigirma kun", "Uch kun.")
t.B("O‘ratepa uchun jangda qancha aholi halok bo‘lgan?", "2 ming nafardan ko‘proq", "200 nafar", "6 mingdan ko‘proq", "20 ming", "2 ming nafardan ko‘proq.")
t.B("Jizzax qachon bosib olingan?", "1866-yil 18-oktabrda", "1866-yil 12-oktabrda", "1866-yil 24-mayda", "1868-yil 2-mayda", "1866-yil 18-oktabrda.")
t.B("Jizzax uchun jangda har ikki tomondan qancha kishi halok bo‘lgan?", "6 mingdan ko‘proq", "2 mingdan ko‘proq", "300", "20 ming", "6 mingdan ko‘proq kishi.")
t.B("1864–1866-yillarda bosib olingan hududlarda qaysi viloyat tashkil qilingan?", "Sirdaryo viloyati", "Farg‘ona viloyati", "Zarafshon okrugi", "Yettisuv viloyati", "Sirdaryo viloyati.")
t.B("Rus davlatida qochoq krepostnoy dehqonlardan tuzilgan qo‘shin qanday atalgan?", "kazak", "sarboz", "yasovul", "navkar", "Kazak.")
t.NAT("Erjar yaqinidagi jangda kuchlar harbiy jihatdan teng bo‘lmadi.", "amir qo‘shinlari mag‘lubiyatga uchradi", "Romanovskiy chekindi", "Buxoro g‘alaba qozondi", "sulh tuzildi", "Amir qo‘shinlari mag‘lub bo‘ldi.")
t.NAT("Jizzax himoyasiga Buxorodan yordamga chiqqan kuchlar kechikib keldi.", "ular hech qanday yordam bera olmay orqaga qaytdi", "shahar saqlab qolindi", "Romanovskiy asirga olindi", "Jizzax ozod qilindi", "Yordam bera olmay qaytdilar.")
t.TF("Xo‘jand Toshkent, Qo‘qon, Balx va Buxoro bilan bog‘lovchi muhim shahar bo‘lgan.", True, "To‘g‘ri.")
t.TF("Jizzax bosib olingach, u yerda hech qanday harbiy kuch qoldirilmagan.", False, "Noto‘g‘ri: 3 ming askar, 300 kazak va 12 to‘p qoldirilgan.")
t.MUL([("1866-yil kuzida O‘ratepaga 6 ming piyoda, 500 kazak va 28 to‘pdan iborat qo‘shin yo‘lga chiqdi.", True),
       ("Barcha harbiy harakatlar Toshkent shahridan turib boshqarilgan.", True),
       ("Krijanovskiy Qo‘qonga qarshi yurishni ham shaxsan boshqargan va Qo‘qonni 1866-yilda egallagan.", False)],
      "III noto‘g‘ri: u Qo‘qonga qarshi yurishga kelgan bo‘lsa-da, kuchlar Buxoroga qarshi burildi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Erjar yaqinidagi jang", "Xo‘jandning egallanishi", "O‘ratepaning egallanishi", "Jizzaxning bosib olinishi"],
      "1866-yil 8-may → 24-may → oktabr boshi → 18-oktabr.")
t.MAPMATCH(UZ, ['Erjar', 'Xo‘jand', 'O‘ratepa', 'Jizzax'],
           ["1866-yil 8-mayda birinchi jang bo‘lgan joy", "24-mayda mudofaasi yorib o‘tilgan qal’a", "uch kun o‘qqa tutilib, 2 mingdan ortiq aholi halok bo‘lgan shahar", "1866-yil 18-oktabrda bosib olingan shahar"],
           "1 – Erjar; 2 – Xo‘jand; 3 – O‘ratepa; 4 – Jizzax.")
t.VENN("O‘ratepa uchun jang", "Jizzax uchun jang",
       [("shahar uch kun to‘plardan o‘qqa tutilgan", 1), ("2 mingdan ko‘proq aholi halok bo‘lgan", 1),
        ("1866-yil 18-oktabrda yakunlangan", 2), ("Buxorodan yordam kechikib kelgan", 2),
        ("1866-yil kuzida podsho qo‘shinlari egallagan", 3)],
       "O‘ratepa — 3 kunlik o‘q, 2 ming qurbon; Jizzax — 18-oktabr, yordam kechikdi; ikkalasi 1866-yil kuzida egallangan.")
