from qlib import Topic
TOPICS = {}

# 21 Ziyolilar qatag'oni va shaxsga sig'inishning fosh qilinishi
t = Topic('e10u21', 10021); TOPICS['e10u21'] = t
t.B("XX asr 40-yillari oxiri – 50-yillari boshidagi qatag‘onlar asosan kimlarga qarshi qaratilgan?", "madaniyat va fan arboblariga", "harbiylarga", "dehqonlarga", "ruhoniylarga", "Madaniyat va fan arboblariga.")
t.B("«O‘zSSR Fanlar akademiyasining ishi to‘g‘risida»gi masala qachon ko‘rilgan?", "1950-yil 1-sentyabrda", "1952-yil fevralda", "1953-yil 5-martda", "1956-yil 25-fevralda", "1950-yil 1-sentyabrda.")
t.B("1950-yilda qoralangan sharqshunos va tarixchi olim kim?", "Abdusamad Boboxo‘jayev", "Vohid Zohidov", "Olim Aminov", "Olim Usmonov", "Abdusamad Boboxo‘jayev.")
t.B("Mafkuraviy masalalarga bag‘ishlangan X plenum qachon bo‘lib o‘tgan?", "1952-yil fevralda", "1950-yil sentyabrda", "1951-yilda", "1956-yil fevralda", "1952-yil fevralda.")
t.B("X plenumda «Respublikada mafkuraviy ishning ahvoli...» to‘g‘risida kim ma’ruza qilgan?", "Amin Niyozov", "Usmon Yusupov", "Nuriddin Muhitdinov", "Sobir Kamolov", "Birinchi sekretar Amin Niyozov.")
t.B("X plenumdan keyin qaysi dostonni o‘qish taqiqlangan?", "«Alpomish»", "«Go‘ro‘g‘li»", "«Farhod va Shirin»", "«Layli va Majnun»", "«Alpomish» dostoni.")
t.B("1951-yilda qamoqqa olingan 12 ijodkor necha yilga ozodlikdan mahrum etilgan?", "25 yilga", "10 yilga", "15 yilga", "5 yilga", "25 yilga.")
t.B("Said Ahmad, Shukrullo, Shayxzoda va boshqalar qachon oqlanib, ozod qilingan?", "1955-yili", "1953-yili", "1956-yili", "1951-yili", "1955-yili.")
t.B("Stalin qachon vafot etgan?", "1953-yil 5-martda", "1956-yil 25-fevralda", "1952-yil fevralda", "1954-yilda", "1953-yil 5-martda.")
t.B("Stalindan keyin SSSR Ministrlar Soveti raisi etib kim tayinlangan?", "Georgiy Malenkov", "Nikita Xrushchev", "M. Suslov", "V. Molotov", "Georgiy Malenkov.")
t.B("Shaxsga sig‘inish to‘g‘risidagi ma’ruza qayerda o‘qilgan?", "KPSS XX syezdining yopiq majlisida", "O‘zbekiston Kompartiyasi X plenumida", "SSSR Oliy Sovetida", "BMT Bosh Assambleyasida", "1956-yil 25-fevralda KPSS XX syezdida.")
t.B("Shaxsga sig‘inish to‘g‘risida kim ma’ruza qilgan?", "Nikita Xrushchev", "Georgiy Malenkov", "Amin Niyozov", "M. Suslov", "Nikita Xrushchev.")
t.B("O‘zbekiston bo‘yicha qatag‘on qilinganlardan qancha kishi oqlangan?", "40 000 nafarga yaqin", "4000 nafar", "400 000 nafar", "12 nafar", "40 000 nafarga yaqin.")
t.B("1950-yil aprelda Usmon Yusupov qaysi lavozimga tayinlangan?", "SSSR Paxtachilik ministri", "O‘zSSR Ministrlar Soveti raisi", "KPSS MK sekretari", "sovxoz direktori", "Moskvaga SSSR Paxtachilik ministri.")
t.B("Xrushchev 1954-yilda Usmon Yusupovni qayerga jo‘natgan?", "Mirzacho‘ldagi «4-Boyovut» sovxoziga direktor qilib", "Moskvaga ministr qilib", "Sibirga surgunga", "Farg‘onaga viloyat rahbari qilib", "Mirzacho‘ldagi «4-Boyovut» sovxoziga direktor qilib.")
t.B("1955–1957-yillarda O‘zbekiston Kompartiyasi MK birinchi sekretari kim bo‘lgan?", "Nuriddin Muhitdinov", "Amin Niyozov", "Sobir Kamolov", "Usmon Yusupov", "Nuriddin Muhitdinov.")
t.B("Amin Niyozov qayerda tug‘ilgan?", "Marg‘ilonda", "Toshkentda", "Samarqandda", "Buxoroda", "Marg‘ilonda.")
t.B("Sobir Kamolov respublika partiya tashkilotini qancha muddat boshqargan?", "atigi 15 oy", "5 yil", "2 yil", "10 oy", "Atigi 15 oy (1957-yil dekabr – 1959-yil mart).")
t.NAT("Sobir Kamolov davrida kadrlarni mahalliylashtirish ommaviy boshlanib, islom diniga erkinliklar berildi.", "bu Markazga yoqmay, u lavozimidan olib tashlandi", "u KPSS MK Bosh sekretari bo‘ldi", "u Qahramon unvoniga sazovor bo‘ldi", "Markaz bu siyosatni qo‘llab-quvvatladi", "Xrushchev, Suslovga yoqmay, u olib tashlandi.")
t.TF("Nuriddin Muhitdinov o‘zbek ziyolilarining oqlanishida tashabbuskorlik ko‘rsatgan.", True, "To‘g‘ri.")
t.TF("Stalin o‘limidan keyin boshqacha fikrlovchilarni ta’qib qilish butunlay to‘xtatilgan.", False, "Noto‘g‘ri: 1953-yildan keyin ham ta’qiblar davom etgan.")
t.MUL([("Amin Niyozov 1947–1950-yillarda O‘zSSR Oliy Soveti Prezidiumi raisi bo‘lgan.", True),
       ("Muhitdinov paxta xarid narxini oshirishni Markaz oldiga qo‘yib, buni uddalagan.", True),
       ("Sobir Kamolov marg‘ilonlik bo‘lgan.", False)],
      "III noto‘g‘ri: Sobir Kamolov toshkentlik bo‘lgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["U. Yusupov SSSR Paxtachilik ministri bo‘ldi", "12 ijodkor qamoqqa olindi", "X plenum", "Stalin vafot etdi", "Qatag‘on qilingan ijodkorlar ozod qilindi", "KPSS XX syezdi"],
      "1950 → 1951 → 1952 → 1953 → 1955 → 1956.")
t.MAPMATCH('uzb', ['Marg‘ilon', 'Guliston', 'Toshkent'],
           ["Amin Niyozov va Yo‘ldosh Oxunboboyev tug‘ilgan shahar", "atrofidagi Mirzacho‘l sovxoziga U. Yusupov direktor qilib jo‘natilgan shahar", "Sobir Kamolov tug‘ilgan shahar"],
           "1 – Marg‘ilon; 2 – Guliston (Mirzacho‘l); 3 – Toshkent.")
t.VENN("Amin Niyozov", "Nuriddin Muhitdinov",
       [("davrida ziyolilarga qatag‘onchilik siyosati olib borilgan", 1), ("X plenumda ma’ruza qilgan", 1),
        ("ziyolilar oqlanishida tashabbus ko‘rsatgan", 2), ("KPSS MK Prezidiumi a’zosi bo‘lgan", 2),
        ("O‘zbekiston Kompartiyasi MK birinchi sekretari bo‘lgan", 3)],
       "Niyozov — qatag‘on, X plenum; Muhitdinov — oqlash, KPSS MK Prezidiumi.")

# 22 Sanoatning bir tomonlama rivojlanishi
t = Topic('e10u22', 10022); TOPICS['e10u22'] = t
t.B("To‘rtinchi besh yillik qaysi yillarni o‘z ichiga olgan?", "1946–1950-yillar", "1951–1955-yillar", "1928–1932-yillar", "1959–1965-yillar", "1946–1950-yillar.")
t.B("Urushdan keyingi besh yilliklarda kapital mablag‘larning aksariyati qaysi sohaga sarflangan?", "og‘ir sanoatga", "yengil sanoatga", "maorifga", "sog‘liqni saqlashga", "Og‘ir sanoatga.")
t.B("O‘zbekistonda og‘ir sanoat asosan nimaga xizmat qilgan?", "paxtachilikni rivojlantirishga", "aholi farovonligiga", "eksportga", "harbiy sanoatga", "Paxtachilikni rivojlantirishga, Markaz manfaatlariga.")
t.B("Aholi qalin joylarda qurilib, atrof-muhitni ifloslantirgan korxonalardan biri qaysi?", "Chirchiq elektrkimyo kombinati", "Toshkent traktor zavodi", "Farg‘ona to‘qimachilik kombinati", "Toshkent aviatsiya zavodi", "Chirchiq elektrkimyo, Navoiy kimyo kombinati va b.")
t.B("1947-yilda qurilgan Chorjo‘y – Qo‘ng‘irot temir yo‘lining uzunligi qancha?", "600 km", "1000 km", "300 km", "1500 km", "600 km.")
t.B("Toshkentda ilk marta trolleybuslar qachon qatnay boshlagan?", "1947-yilda", "1959-yilda", "1966-yilda", "1955-yilda", "1947-yilda.")
t.B("Qoraqalpog‘istonni Qozog‘iston bilan bog‘lagan temir yo‘l qaysi?", "Qo‘ng‘irot – Beynov", "Chorjo‘y – Qo‘ng‘irot", "Toshkent – Orenburg", "Krasnovodsk – Toshkent", "Qo‘ng‘irot – Beynov.")
t.B("Toshkent katta halqa avtomobil yo‘li qachon loyihalashtirilib qurilgan?", "1959–1968-yillarda", "1947–1950-yillarda", "1970–1980-yillarda", "1951–1955-yillarda", "1959–1968-yillarda.")
t.B("50-yillar o‘rtalaridan qaysi rusumli yo‘lovchi samolyotlar paydo bo‘lgan?", "TU-104", "IL-62", "AN-2", "YAK-40", "TU-104.")
t.B("1959-yilda respublika aholisi tarkibida o‘zbeklarning salmog‘i qancha bo‘lgan?", "62 foizdan ortiq", "43 foiz", "75 foiz", "50 foiz", "62 foizdan ortiq.")
t.B("1959-yilda respublika ishchilarining necha foizini o‘zbeklar tashkil etgan?", "43 foizini", "62 foizini", "75 foizini", "25 foizini", "Atigi 43 foizini.")
t.B("Ittifoqqa bo‘ysunadigan korxonalarda ish haqi mahalliy korxonalardagidan necha marta ko‘p bo‘lgan?", "2–3 marta va undan ko‘p", "1,5 marta", "10 marta", "bir xil bo‘lgan", "2–3 marta va undan ham ko‘proq.")
t.B("Respublikadagi rahbar lavozimlarga nomzodlarni kim tavsiya qilgan?", "Kreml", "O‘zbekiston Oliy Soveti", "xalq", "viloyat kengashlari", "Kreml.")
t.B("Ikkinchi sekretarlar va muhim ministrliklar rahbarlari asosan kimlardan iborat bo‘lgan?", "Moskvadan yuborilgan vakillardan", "mahalliy millat vakillaridan", "saylangan deputatlardan", "harbiylardan", "Moskvadan yuborilgan (asosan slavyan va arman) vakillardan.")
t.NAT("Temir va avtomobil yo‘llari boshqa respublikalar hududidan o‘tkazildi.", "ular iqtisodiy jihatdan Markazga qaram qilib qo‘yildi", "O‘zbekiston mustaqil transport tizimiga ega bo‘ldi", "yo‘llar qisqardi", "transport arzonlashdi", "Bu SSSR parchalangach ayniqsa sezildi.")
t.NAT("Kadrlar siyosatida mahalliy aholi manfaatlari kamsitildi, ruslashtirish olib borildi.", "ijtimoiy vaziyat keskinlashib, millatlararo munosabatlar murakkablashdi", "millatlararo do‘stlik mustahkamlandi", "o‘zbek ishchilari ko‘paydi", "ish haqi tenglashdi", "Ijtimoiy vaziyat keskinlashdi.")
t.TF("Yengil sanoatda aholini iste’mol mollari bilan ta’minlash darajasi Ittifoqqa nisbatan bir necha marta kam bo‘lgan.", True, "To‘g‘ri.")
t.TF("Temir yo‘llarni elektrlashtirish ishlari jadal sur’atlarda olib borilgan.", False, "Noto‘g‘ri: sekinlik bilan olib borilgan.")
t.MUL([("Beshinchi besh yillik 1951–1955-yillarni o‘z ichiga olgan.", True),
       ("Qo‘ng‘irot – Beynov yo‘li O‘rta Osiyodan Markazga olib boradigan ikkinchi poyezd yo‘lini vujudga keltirgan.", True),
       ("Yetakchi sanoat sohalari uchun mutaxassislar faqat mahalliy aholidan tayyorlangan.", False)],
      "III noto‘g‘ri: mutaxassislar Markazdan taklif qilingan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["To‘rtinchi besh yillik boshlandi", "Chorjo‘y – Qo‘ng‘irot temir yo‘li qurildi", "Beshinchi besh yillik boshlandi", "TU-104 samolyotlari paydo bo‘ldi", "Toshkent katta halqa yo‘li qurilishi tugadi"],
      "1946 → 1947 → 1951 → 50-yillar o‘rtasi → 1968.")
t.MAPMATCH('ca2', ['Chorjo‘y', 'Qo‘ng‘irot', 'Beynov', 'Navoiy'],
           ["1947-yilgi 600 km temir yo‘lning janubiy boshlang‘ich nuqtasi", "Chorjo‘y yo‘li yetib borgan va Beynovga yo‘l boshlangan Qoraqalpog‘istondagi shahar", "Qoraqalpog‘istonni Qozog‘iston bilan bog‘lagan yo‘lning so‘nggi nuqtasi", "atrof-muhitni ifloslantirgan kimyo kombinati joylashgan shahar"],
           "1 – Chorjo‘y; 2 – Qo‘ng‘irot; 3 – Beynov; 4 – Navoiy.")
t.VENN("Og‘ir sanoat", "Yengil sanoat",
       [("katta kapital mablag‘larning aksariyati sarflangan", 1), ("kimyo korxonalari ekologiyaga zarar keltirgan", 1),
        ("ishlab chiqarish rejalari bajarilmagan", 2), ("iste’mol mollari bilan ta’minlash past bo‘lgan", 2),
        ("Markazda ishlab chiqilgan siyosat asosida rivojlangan", 3)],
       "Og‘ir — mablag‘lar, kimyo; yengil — rejalar bajarilmagan, ta’minot past.")
