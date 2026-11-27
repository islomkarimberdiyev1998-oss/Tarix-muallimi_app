from qlib import Topic
TOPICS = {}
XR = 'xorazm'

# 37 Xiva xonligining tugatilishi
t = Topic('e9u37', 9037); TOPICS['e9u37'] = t
t.B("XIX asrning 80-yillarida qaysi tumanlarda dehqon uyushmalari vujudga kelgan?", "Pitnak, Hazorasp, Yangi Urganch, Ko‘hna Urganch", "Chimboy, Nukus", "Xonqa, Bog‘ot", "Mang‘it, Xo‘jayli", "Pitnak, Hazorasp, Yangi Urganch, Ko‘hna Urganch.")
t.B("1902-yilgi qo‘zg‘olonga kim rahnamolik qilgan?", "Matyoqub pishiq", "Junaidxon", "Bobo Go‘klan", "Polvonniyoz hoji", "Matyoqub pishiq.")
t.B("1902-yilda qaysi tumanlar dehqonlari qo‘zg‘olon ko‘targan?", "Xonqa, Hazorasp, Bog‘ot", "Mang‘it, Xo‘jayli", "Pitnak, Ko‘hna Urganch", "Alieli, Toshhovuz", "Xonqa, Hazorasp, Bog‘ot.")
t.B("Xiva xonligida qaysi yillar qurg‘oqchilik va hosilsizlik yili bo‘lgan?", "1910–1911-yillar", "1902–1903-yillar", "1916–1917-yillar", "1885–1886-yillar", "1910–1911-yillar.")
t.B("Asfandiyorxon qo‘zg‘olonchilarga qarshi necha kishilik sara qo‘shinini tashlagan?", "1000 kishilik", "1,5 ming kishilik", "300 kishilik", "10 ming kishilik", "1000 kishilik qo‘shin.")
t.B("Xonning sara qo‘shini qayerda tor-mor etilgan?", "Alieli va Toshhovuz o‘rtasida", "Hazorasp yonida", "Xiva ostonasida", "Mang‘itda", "Alieli va Toshhovuz o‘rtasida.")
t.B("Yosh xivaliklar harakatining Yosh buxoroliklardan farqi nimada edi?", "unda aholining turli qatlamlari ishtirok etgan", "u faqat ziyolilardan iborat bo‘lgan", "u qurolli harakat bo‘lgan", "u Rossiyaga qarshi bo‘lmagan", "Dehqonlar, hunarmandlar, savdogarlar, ziyolilar ishtirok etgan.")
t.B("Xon «Islohotlar loyihasi»ni qachon qabul qilgan?", "1910-yilda", "1917-yilda", "1913-yilda", "1902-yilda", "1910-yilda.")
t.B("Muhammad Rahimxon II dan so‘ng taxtni kim egallagan?", "Asfandiyorxon", "Said Abdulla", "Junaidxon", "Islom xo‘ja", "O‘g‘li Asfandiyorxon (1910–1918).")
t.B("Asfandiyorxon 1913-yilda qaysi islohotchi bosh vazirni o‘ldirtirgan?", "Islom xo‘jani", "Bobooxun Salimovni", "Polvonniyoz hojini", "Matyoqub pishiqni", "Bosh vazir Islom xo‘jani.")
t.B("Yerlarni qayta o‘lchashga javoban qayerlarda qo‘zg‘olon ko‘tarilgan?", "Mang‘it va Xo‘jaylida", "Xonqa va Hazoraspda", "Pitnakda", "Alielida", "Mang‘it va Xo‘jaylida.")
t.B("Yosh xivaliklar qachon xondan islohotlar haqidagi manifestni imzolashni talab qilgan?", "1917-yil 5-aprelda", "1917-yil 26-aprelda", "1910-yilda", "1918-yil yanvarda", "1917-yil 5-aprelda.")
t.B("Manifest qanday boshqaruv shaklini nazarda tutgan?", "konstitutsiyaviy monarxiya", "respublika", "mutlaq monarxiya", "harbiy diktatura", "Majlis va Nozirlar kengashi bilan cheklangan konstitutsiyaviy monarxiya.")
t.B("1917-yil 26-apreldagi Majlis sessiyasida nechta xivalik deputat qatnashgan?", "30 nafar", "7 nafar", "150 nafar", "350 nafar", "30 xivalik va 7 turkman vakili.")
t.B("1918-yil yanvarda Xivani kim egallagan?", "Junaidxon", "Asfandiyorxon", "Said Abdulla", "bolsheviklar", "Turkman sardori Junaidxon 1,5 ming otliq bilan.")
t.B("Asfandiyorxon o‘ldirilgach, taxtga kim o‘tqazilgan?", "Said Abdulla", "Junaidxon", "Islom xo‘ja", "Polvonniyoz hoji", "Said Abdulla.")
t.B("«Xalq inqilobi» deb atalgan to‘ntarish qachon ro‘y bergan?", "1920-yil 2-fevralda", "1920-yil 27-aprelda", "1918-yil yanvarda", "1917-yil 5-aprelda", "1920-yil 2-fevralda.")
t.B("Xorazm Xalq Sovet Respublikasi qachon e’lon qilingan?", "1920-yil 27-aprelda", "1920-yil 2-fevralda", "1920-yil 6-oktabrda", "1918-yil oktabrda", "1920-yil 27-aprelda.")
t.NAT("Xon ixtiyorida dehqonlar harakatiga qarshi kuchlar yetarli emas edi.", "u Rossiya podshosi qo‘shinlarini yordamga chaqirdi", "xon taxtdan voz kechdi", "dehqonlarga yer berildi", "Xiva mustaqil bo‘ldi", "Podsho qo‘shinlari isyonlarni bostirdi.")
t.NAT("1917-yilgi fevral voqealaridan keyin Asfandiyorxon podsho hukumati tayanchidan mahrum bo‘ldi.", "u hokimiyatni saqlab qolish uchun islohotlar manifestiga imzo chekdi", "u Rossiyaga qochdi", "u Yosh xivaliklarni qatl etdi", "Xiva Buxoroga qo‘shildi", "Vaqtdan yutish uchun manifestni imzoladi.")
t.TF("1912-yilgi qo‘zg‘olonda qo‘zg‘olonchilar o‘qotar aslahalar bilan qurollanib, urush taktikasini o‘zlashtirgan edi.", True, "To‘g‘ri.")
t.TF("Majlis bir necha yil faoliyat ko‘rsatib, Xivani respublikaga aylantirgan.", False, "Noto‘g‘ri: ikki oy o‘tmay konservativ kuchlar Majlisni tarqatib yubordi.")
t.MUL([("Yosh xivaliklar rahbarlari Polvonniyoz hoji Yusupov, Bobooxun Salimov, Bekjon Rahmonov va boshqalar edi.", True),
       ("Yosh xivaliklar yangi usul maktablari, temiryo‘l va pochta-telegraf qurilishini talab qilgan.", True),
       ("Petro-Aleksandrovskda Yosh xivaliklar partiyasi tuzilgan.", False)],
      "III noto‘g‘ri: Petro-Aleksandrovskda bolsheviklar Kommunistik partiyani tuzgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Matyoqub pishiq qo‘zg‘oloni", "«Islohotlar loyihasi» qabul qilindi", "Islom xo‘ja o‘ldirildi", "Manifest imzolandi", "Junaidxon Xivani egalladi", "XXSR e’lon qilindi"],
      "1902 → 1910 → 1913 → 1917 → 1918 → 1920.")
t.MAPMATCH(XR, ['Xiva', 'Hazorasp', 'Mang‘it'],
           ["1918-yil yanvarda Junaidxon egallagan poytaxt", "1902 va 1912-yillarda qo‘zg‘olonlar bo‘lgan joy", "yerlarni qayta o‘lchashga qarshi Xo‘jayli bilan birga qo‘zg‘olon ko‘targan joy"],
           "1 – Xiva; 2 – Hazorasp; 3 – Mang‘it.")
t.VENN("Yosh buxoroliklar", "Yosh xivaliklar",
       [("«Buxoroi sharif» va «Turon» gazetalarini chiqargan", 1), ("Fayzulla Xo‘jayev rahbarlik qilgan", 1),
        ("tarkibida dehqonlar, hunarmandlar, savdogarlar bo‘lgan", 2), ("Polvonniyoz hoji Yusupov rahbarlik qilgan", 2),
        ("islohotlar o‘tkazishga intilgan jadidlar", 3)],
       "Buxoroliklar — gazetalar, Xo‘jayev; xivaliklar — keng tarkib, Polvonniyoz hoji; ikkalasi islohotchi jadidlar.")
