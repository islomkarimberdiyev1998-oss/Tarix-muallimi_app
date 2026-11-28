from qlib import Topic, PLACES, REG
TOPICS = {}

# 10-mavzu. Qoraqalpoqlar madaniyati
t = Topic('y10u10', 10010); TOPICS['y10u10'] = t
t.B("XIX asr oxiri – XX asr boshida qoraqalpoqlarning eng katta madrasalari qaysilar?", "Qoraqum eshon va Tosh madrasa", "Mir Arab va Ko‘kaldosh", "Sherg‘ozixon va Qutlug‘ Inoq", "Chalpak va Jome", "Qoraqum eshon va Tosh madrasalari.")
t.B("Tosh madrasani kim qurdirgan?", "Mang‘it hokimi Xo‘janiyoz", "Berdaq", "Ajiniyoz", "Muhammad Rahimxon II", "1841-yilda Mang‘it hokimi Xo‘janiyoz.")
t.B("Tosh madrasa qachon qurilgan?", "1841-yilda", "1873-yilda", "1900-yilda", "1799-yilda", "1841-yilda.")
t.B("Qoraqum eshon madrasasi dastlab qanday vazifani bajargan?", "masjid", "kutubxona", "karvonsaroy", "qal’a", "Dastlab masjid vazifasini bajargan.")
t.B("Madrasada birinchi bosqichda nima o‘rganilgan?", "arab tili grammatikasi", "diniy-huquqiy bilimlar", "astronomiya", "tibbiyot", "Arab tili grammatikasi.")
t.B("XIX asr boshlarida qoraqalpoqlarda nechta maktab bo‘lgan?", "318 ta", "31 ta", "3180 ta", "100 ta", "318 ta.")
t.B("Kunxo‘ja qaysi yillarda yashagan?", "1799–1880", "1824–1878", "1827–1900", "1788–1875", "1799–1880.")
t.B("Otash Olshinboy qaysi yillarda yashagan?", "1788–1875", "1799–1880", "1824–1878", "1827–1900", "1788–1875.")
t.B("Ajiniyoz qanday ilmiy darajaga birinchilardan bo‘lib erishgan?", "oxund", "mudarris", "qozi", "muftiy", "Oxund.")
t.B("Ajiniyoz qaysi tillarni yaxshi bilgan?", "o‘zbek, qozoq, turkman", "rus, nemis, fransuz", "arab, fors, hind", "xitoy, mo‘g‘ul", "O‘zbek, qozoq, turkman.")
t.B("Berdaq qayerda tug‘ilgan?", "Orolbo‘yida", "Xivada", "Mo‘ynoqda", "Nukusda", "Orolbo‘yida.")
t.B("Berdaq qaysi madrasada o‘qigan?", "Qoraqum eshon madrasasi", "Sherg‘ozixon madrasasi", "Tosh madrasa", "Mir Arab", "Qoraqum eshon madrasasida.")
t.B("Berdaqning she’rlaridan biri qanday nomlangan?", "«Xalq uchun»", "«Bo‘zatov»", "«Qirq qiz»", "«O‘roqchilar»", "«Xalq uchun».")
t.B("XX asr boshida qoraqalpoq adabiyotidagi demokratik an’analarni davom ettirganlar kimlar?", "Umar, Sariboy, Qulmurot, Sodiq", "Kunxo‘ja, Ajiniyoz", "Munis, Ogahiy", "Behbudiy, Fitrat", "Umar, Sariboy, Qulmurot, Sodiq.")
t.B("«Qirq qiz» dostonining bosh qahramoni kim?", "Guloyim", "Arslon", "Olloyor", "Mengesh", "Guloyim.")
t.B("«Qirq qiz»da Guloyimga yordam bergan xorazmlik bahodir kim?", "Arslon", "Olloyor", "Alpomish", "Edigey", "Arslon.")
t.B("Guloyimning otasi Olloyor qaysi yurt hukmdori edi?", "Sarkub", "Muyeli", "Xorazm", "Xiva", "Sarkub.")
t.NAT("Kunxo‘ja o‘z ijodida ovullarning oddiy ahlini kuyladi.", "u adolatsiz tartiblarni qattiq qoraladi", "u xonni madh etdi", "u ijodni to‘xtatdi", "u faqat ishqiy she’r yozdi", "Adolatsizlikni qoraladi.")
t.NAT("Dushmanlar Sarkub yerlariga hujum qilib, Guloyimning otasini o‘ldirdi.", "Guloyim va kanizaklari kurashib, qoraqalpoqlarni asirlikdan ozod qildi", "Guloyim asir tushdi", "Sarkub dushmanga qo‘shildi", "kanizaklar qochib ketdi", "Ona yurtga ozodlik qaytdi.")
t.NAT("O‘mirbek laqqi obrazi orqali salbiy illatlar hajv qilindi.", "razillik, zolimlik fosh etilib, mehnatsevarlik va ezgulik ulug‘landi", "zolimlik maqtaldi", "xalq og‘zaki ijodi yo‘qoldi", "hajv taqiqlandi", "Ezgulik ulug‘landi.")
t.TF("Ajiniyoz adabiy merosidan 100 ga yaqin she’r va dostonlar yetib kelgan.", True, "To‘g‘ri.")
t.TF("Qoraqalpoqlar to‘y-marakalarini qo‘shiq va dostonlarsiz o‘tkazgan.", False, "Noto‘g‘ri: qo‘shiqsiz, dostonsiz o‘tkazmaganlar.")
t.TF4([("Qoraqalpoqlar Buxoro va Xiva shaharlarida ham ta’lim olgan.", True), ("«Bo‘zatov»da qoraqalpoqlarning ko‘chib yurishi tasvirlangan.", True),
       ("«Qirq qiz» dostonining bosh g‘oyasi vatanparvarlik.", True), ("Berdaq 1799–1880-yillarda yashagan.", False)],
      "4-noto‘g‘ri: Berdaq 1827–1900-yillarda yashagan.")
t.MUL([("«Otalar so‘zi» maqol, hikmat, nasihat qo‘shiqlarida ifodalangan.", True),
       ("Ajiniyoz Mo‘ynoqdagi maktabda o‘qigan.", True),
       ("Tosh madrasada faqat matematika o‘qitilgan.", False)],
      "III noto‘g‘ri: arab grammatikasi va diniy-huquqiy bilimlar o‘qitilgan.")
t.CHR("Ijodkorlarni tug‘ilgan yili bo‘yicha tartiblang.", ["Otash Olshinboy", "Kunxo‘ja", "Ajiniyoz", "Berdaq"],
      "1788 → 1799 → 1824 → 1827.")
t.MATCH("Ijodkorlarni asar yoki ma’lumot bilan moslashtiring.", ["Ajiniyoz", "Berdaq", "Kunxo‘ja", "O‘mirbek laqqi"],
        ["«Bo‘zatov» dostoni", "«Xalq uchun» she’ri", "ovul ahlining mehnatini kuylagan", "xalq og‘zaki ijodidagi kulgi qahramoni", "«Shajarayi turk»"], 'abcd',
        "Ajiniyoz – Bo‘zatov; Berdaq – Xalq uchun; Kunxo‘ja – ovul ahli; O‘mirbek – kulgi qahramoni.")
t.VENN("Ajiniyoz", "Berdaq",
       [("Zevar taxallusi", 1), ("Sherg‘ozixon madrasasida o‘qigan", 1),
        ("Orolbo‘yida tug‘ilgan", 2), ("Qoraqum eshon madrasasida o‘qigan", 2),
        ("qoraqalpoq shoiri", 3)],
       "Ajiniyoz – Zevar, Sherg‘ozixon; Berdaq – Orolbo‘yi, Qoraqum eshon; ikkalasi shoir.")
t.MAPMATCH('xorazm2', ['Mo‘ynoq', 'Xiva', 'Mang‘it'],
           ["Ajiniyoz boshlang‘ich ta’lim olgan joy", "Ajiniyoz Sherg‘ozixon madrasasida o‘qigan shahar", "hokimi Xo‘janiyoz Tosh madrasani qurdirgan joy"],
           "1 – Mo‘ynoq; 2 – Xiva; 3 – Mang‘it.")

# 11-mavzu. Turkistonda jadidchilik harakati
t = Topic('y10u11', 10011); TOPICS['y10u11'] = t
t.B("Jadidchilik harakati qachon yuzaga kelgan?", "XIX asr oxirlarida", "XVIII asrda", "1917-yilda", "1924-yilda", "XIX asr oxirlarida.")
t.B("Jadidlar qanday maktablar tashkil qilgan?", "yangi usul maktablari", "rus-tuzem maktablari", "harbiy maktablar", "madrasalar", "Yangi usul maktablari.")
t.B("Ziyolilar ilg‘or g‘oyalarni tarqatishda nimani asosiy vosita deb bilgan?", "maorif tizimini", "qurolli kurashni", "savdoni", "diniy marosimlarni", "Maorifni.")
t.B("Buxoro amirligida birinchi yangi usul maktabi qachon ochilgan?", "1893-yilda", "1898-yilda", "1899-yilda", "1910-yilda", "1893-yilda.")
t.B("Jadidlar qaysi hudud ziyolilari tajribasini o‘rgangan?", "Qrim", "Kavkaz", "Sibir", "Polsha", "Qrim ziyolilari.")
t.B("O‘rta Osiyo jadidchiligi hududiy jihatdan qanday bo‘linadi?", "Turkiston, Buxoro va Xiva jadidlari", "shimoliy va janubiy", "o‘ng va so‘l", "shahar va qishloq", "Turkiston, Buxoro, Xiva jadidlari.")
t.B("Buxoro jadidlarining asosiy tarkibi kimlardan iborat edi?", "mayda do‘kondorlar, o‘qituvchilar, hunarmandlar, savdogarlar", "zodagonlar va beklar", "harbiylar", "ruhoniylar", "Do‘kondor, o‘qituvchi, hunarmand, savdogarlar.")
t.B("Buxoroda jadidchilik qachondan siyosiy tashkilot sifatida shakllana boshlagan?", "1910-yildan", "1893-yildan", "1917-yildan", "1905-yildan", "1910-yildan.")
t.B("Xiva jadidlarining o‘ng oqimiga kim boshchilik qilgan?", "Bosh vazir Islomxo‘ja", "Bobooxun Salimov", "Polvonniyoz Yusupov", "Asfandiyorxon", "Islomxo‘ja.")
t.B("Xiva jadidlarining so‘l oqimiga kim rahbarlik qilgan?", "qozikalon Bobooxun Salimov", "Islomxo‘ja", "Muhammad Rahimxon II", "Mannon qori", "Bobooxun Salimov.")
t.B("1898-yilda Qo‘qonda ikkinchi jadid maktabini kim ochgan?", "Salohiddin domla", "Shamsiddin domla", "Mannon qori", "Munavvar qori", "Salohiddin domla.")
t.B("1899-yilda Andijonda jadid maktabini kim ochgan?", "Shamsiddin domla", "Salohiddin domla", "Mannon qori", "Behbudiy", "Shamsiddin domla.")
t.B("1899-yilda Toshkentda jadid maktabini kim ochgan?", "Mannon qori", "Munavvar qori", "Shamsiddin domla", "Salohiddin domla", "Mannon qori.")
t.NAT("XX asr boshida ko‘plab jadid adabiyotlari, gazeta va jurnallar ommaviy nashr etildi.", "bu aholining ularga ehtiyoji va savodxonligidan dalolat berdi", "aholi o‘qimay qo‘ydi", "nashrlar taqiqlandi", "jadidlar yo‘qoldi", "Savodxonlik va ehtiyoj.")
t.NAT("Buxoroda jadidchilik og‘ir ijtimoiy-siyosiy sharoitda yuzaga keldi.", "u mutaassib mullalar va yangilikni xush ko‘rmaydiganlar qarshiligiga uchradi", "amir jadidlarni qo‘llab-quvvatladi", "jadidlar tezda hokimiyatni oldi", "harakat Turkistondan oldin kuchaydi", "Mutaassiblar qarshiligi.")
t.NAT("Xiva jadidlarining o‘ng oqimi xon hokimiyatini saqlab qolishni istadi.", "u islohotlarni xon hokimiyati doirasida o‘tkazishni maqsad qildi", "u xonni ag‘darishni maqsad qildi", "u Rossiyaga qo‘shilishni istadi", "u maktablarni yopdi", "Islohot xon hokimiyati doirasida.")
t.NAT("Mustamlakachilar va mutaassiblar jadidlarga qarshilik ko‘rsatdi.", "jadidlar ma’rifatparvarlikni matbuot, noshirlik va teatr sohalarida davom ettirdi", "jadidlar faoliyatni to‘xtatdi", "jadidlar xorijga ketdi", "jadidlar qurolli kurash boshladi", "Matbuot, noshirlik, teatr.")
t.TF("Jadidlar ta’limni rivojlantirish orqali mustaqillikka erishish mumkin deb hisoblagan.", True, "To‘g‘ri.")
t.TF("Turkiston jadidchiligining asosiy tarkibini harbiy zobitlar tashkil etgan.", False, "Noto‘g‘ri: asosiy tarkibni ziyolilar tashkil etgan.")
t.TF4([("Xiva jadidchiligi ikki oqimdan iborat bo‘lgan.", True), ("So‘l oqim yangi usul maktablari orqali xalq faolligiga erishmoqchi bo‘lgan.", True),
       ("Buxorodagi birinchi yangi usul maktabi 1910-yilda ochilgan.", False), ("Turkiston jadidlari mustamlakachilikka qarshi kurash safida turgan.", True)],
      "3-noto‘g‘ri: 1893-yilda ochilgan.")
t.MUL([("Jadidlar boshqa mamlakatlar taraqqiyparvarlarining g‘oyalaridan ham foydalangan.", True),
       ("Xiva o‘ng oqimi savdo-sanoat egalari va yirik boylarni birlashtirgan.", True),
       ("Buxoro jadidlari mutaassib mullalar tomonidan to‘liq qo‘llab-quvvatlangan.", False)],
      "III noto‘g‘ri: mutaassib mullalar qarshilik ko‘rsatgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Buxoroda birinchi yangi usul maktabi", "Qo‘qonda Salohiddin domla maktabi", "Andijon va Toshkentda jadid maktablari", "Buxoroda jadidchilik siyosiy tashkilot sifatida shakllana boshladi"],
      "1893 → 1898 → 1899 → 1910.")
t.MATCH("Jadid maktablari ochgan shaxslarni shahar bilan moslashtiring.", ["Salohiddin domla", "Shamsiddin domla", "Mannon qori", "Bobooxun Salimov"],
        ["Qo‘qon", "Andijon", "Toshkent", "Xiva (so‘l oqim rahbari)", "Samarqand"], 'abcd',
        "Salohiddin – Qo‘qon; Shamsiddin – Andijon; Mannon qori – Toshkent; Bobooxun – Xiva.")
t.VENN("Xiva jadidlari o‘ng oqimi", "Xiva jadidlari so‘l oqimi",
       [("Islomxo‘ja boshchiligida", 1), ("xon hokimiyatini saqlab islohot", 1),
        ("Bobooxun Salimov rahbarligida", 2), ("yangi usul maktablari orqali faollik", 2),
        ("Xiva xonligidagi jadidchilik oqimi", 3)],
       "O‘ng – Islomxo‘ja; so‘l – Bobooxun Salimov; ikkalasi Xiva jadidchiligi.")
t.MAPMATCH('uzb', ['Buxoro', 'Qo‘qon', 'Andijon', 'Toshkent'],
           ["1893-yilda birinchi yangi usul maktabi ochilgan joy", "1898-yilda Salohiddin domla maktab ochgan shahar", "1899-yilda Shamsiddin domla maktab ochgan shahar", "1899-yilda Mannon qori maktab ochgan shahar"],
           "1 – Buxoro; 2 – Qo‘qon; 3 – Andijon; 4 – Toshkent.")
