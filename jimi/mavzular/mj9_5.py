from qlib import Topic
TOPICS = {}
LA = 'latam'; W = 'globe2'; UE = 'usa_e'

# 15 AQSHning ichki siyosati
t = Topic('e9j15', 9115); TOPICS['e9j15'] = t
t.B("AQSH ishchilar harakatining asosiy maqsadi nima edi?", "ish kunini qisqartirish", "monarxiyani tiklash", "mustamlakalar olish", "qullikni tiklash", "Ish kunini qisqartirishga erishish.")
t.B("1886-yil 1-maydagi umumiy ish tashlashda qancha ishchi qatnashgan?", "350 mingdan ortiq", "200 ming", "6 ming", "1 million", "350 mingdan ortiq; 200 mingga yaqini 8 soatlik ish kuniga erishdi.")
t.B("8 soatlik ish kuni uchun harakat qaysi shaharda juda keskin tus olgan?", "Chikagoda", "Nyu-Yorkda", "Vashingtonda", "Bostonda", "Chikagoda.")
t.B("Chikagoda ommaviy harakat rahbarlaridan necha kishi dorga osilgan?", "4 kishi", "6 kishi", "10 kishi", "2 kishi", "4 kishi.")
t.B("«Shunday zamon keladiki, bizning sukunatimiz nutqlarimizdan ham o‘tkirroq bo‘ladi», degan kim?", "Shpis", "Ruzvelt", "Vilson", "Taft", "Osib o‘ldirishga mahkum Shpis.")
t.B("1886-yilda «Tred-yunionlar federatsiyasi» qanday nom olgan?", "Amerika Mehnat Federatsiyasi", "II Internatsional", "Leyboristlar partiyasi", "Panamerika ittifoqi", "Amerika Mehnat Federatsiyasi (AMF).")
t.B("Hukumat qachondan sentabrning birinchi dushanbasini «Mehnat kuni» deb e’lon qilgan?", "1894-yildan", "1886-yildan", "1913-yildan", "1901-yildan", "1894-yilda.")
t.B("1913-yilgi konchilar ish tashlashida qaysi shtatda harbiy holat e’lon qilingan?", "Kolorado", "Illinoys", "Texas", "Kaliforniya", "Butun Kolorado shtatida.")
t.B("Aholini majburan irqiy guruhlarga bo‘lish qanday ataladi?", "segregatsiya", "rezervatsiya", "immigratsiya", "assimilyatsiya", "Segregatsiya.")
t.B("Hindular qaysi yilgi oxirgi jangda yengilgan?", "1880-yilgi", "1886-yilgi", "1870-yilgi", "1898-yilgi", "1880-yilgi oxirgi jangda.")
t.B("Tub joy aholisi zo‘rlab joylashtirilgan hudud qanday ataladi?", "rezervatsiya", "segregatsiya", "latifundiya", "protektorat", "Rezervatsiya.")
t.B("1900–1914-yillar AQSH tarixiga qanday nom bilan kirgan?", "«taraqqiyparvar davr»", "«oltin asr»", "«yangi kurs»", "«qayta qurish davri»", "«Taraqqiyparvar davr».")
t.B("Teodor Ruzvelt qachon prezident bo‘lgan?", "1901-yilda", "1912-yilda", "1894-yilda", "1898-yilda", "1901-yilda.")
t.B("T. Ruzveltning monopoliyalarga qarshi siyosati qanday nom olgan?", "«Adolatli yo‘l»", "«Yo‘g‘on kaltak»", "«Dollar diplomatiyasi»", "«Ochiq eshiklar»", "«Adolatli yo‘l».")
t.B("1912-yilgi prezident saylovida kim g‘alaba qozongan?", "demokrat Vudro Vilson", "Teodor Ruzvelt", "Taft", "Linkoln", "Demokrat Vudro Vilson.")
t.B("Vilson davrida bojxona tarif stavkasi qanchaga kamaytirilgan?", "10 foizga", "50 foizga", "2 foizga", "25 foizga", "10 foizga.")
t.NAT("Sud qaroriga ko‘ra Morgan nazorat qiladigan temiryo‘l kompaniyasi ikkiga bo‘lindi.", "bu Ruzvelt hukumatining trestlarga qarshi kurashi natijasi edi", "Morgan prezident bo‘ldi", "temiryo‘llar yopildi", "trestlar kuchaydi", "Hukumat trestlarga qarshi ko‘plab sud jarayonlari tashkil etdi.")
t.NAT("1914-yilda Kongress trestlarga qarshi qonun qabul qildi.", "ish tashlash zararini kasaba uyushmalaridan undirish tartibi bekor qilindi", "ish tashlash taqiqlandi", "trestlar ko‘paydi", "kasaba uyushmalari yopildi", "Zararni kasaba uyushmalaridan undirish bekor qilindi.")
t.TF("Vilson davrida senatorlar xalqning ovoz berishi bilan saylanadigan bo‘ldi.", True, "To‘g‘ri.")
t.TF("Hindular uchun ajratilgan rezervatsiyalar unumdor yerlar edi.", False, "Noto‘g‘ri: ular unumsiz, tashlandiq yerlar edi.")
t.MUL([("Qora tanlilar oq tanlilar maktabi, cherkovi va transportidan foydalana olmagan.", True),
       ("Qora tanlilarning ziyoli guruhlari kurashning tinch yo‘lini tanlagan.", True),
       ("Hindularga fermerlik huquqini beruvchi qonun to‘liq amalga oshgan.", False)],
      "III noto‘g‘ri: qonun amalga oshmay qolgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Hindularning oxirgi jangi", "1-maydagi umumiy ish tashlash", "«Mehnat kuni» bayrami e’lon qilindi", "T. Ruzvelt prezident bo‘ldi", "V. Vilson saylovda g‘alaba qozondi", "Kolorado konchilari ish tashladi"],
      "1880 → 1886 → 1894 → 1901 → 1912 → 1913.")
t.MAPMATCH('namerica', ['Chikago', 'Kolorado', 'Vashington'],
           ["1886-yilda politsiya miting qatnashchilariga o‘q uzgan shahar", "1913-yilda harbiy holat e’lon qilingan shtat", "AQSH poytaxti"],
           "1 – Chikago; 2 – Kolorado; 3 – Vashington.")
t.VENN("Teodor Ruzvelt", "Vudro Vilson",
       [("«Adolatli yo‘l» siyosati", 1), ("Amerika-Ispaniya urushida qatnashgan", 1),
        ("1912-yilda saylangan demokrat", 2), ("bojxona tarifini 10% ga kamaytirgan", 2),
        ("monopoliyalarga qarshi kurashgan prezident", 3)],
       "Ruzvelt — «Adolatli yo‘l»; Vilson — demokrat, tarif islohoti; ikkalasi trestlarga qarshi.")

# 16 AQSHning tashqi siyosati
t = Topic('e9j16', 9116); TOPICS['e9j16'] = t
t.B("AQSH Rossiyadan qaysi hududni sotib olgan?", "Alyaskani", "Kaliforniyani", "Gavayini", "Floridani", "Alyaskani.")
t.B("Birinchi Panamerika konferensiyasi qachon va qayerda chaqirilgan?", "1889-yilda Vashingtonda", "1910-yilda Buenos-Ayresda", "1898-yilda Parijda", "1823-yilda Nyu-Yorkda", "1889-yilda Vashingtonda.")
t.B("AQSHning G‘arbiy yarimshar ustidan tanho hukmronlikka qaratilgan siyosati qanday nomlangan?", "Panamerikanizm", "«Ochiq eshiklar»", "izolyatsionizm", "«Adolatli yo‘l»", "Panamerikanizm.")
t.B("Gavayi orollari qachon bosib olingan?", "1898-yilda", "1889-yilda", "1903-yilda", "1914-yilda", "1898-yilda.")
t.B("Amerika–Ispaniya urushi necha oy davom etgan?", "3 oy", "3 yil", "1 oy", "1 yil", "3 oy.")
t.B("AQSH–Ispaniya tinchlik shartnomasi qachon va qayerda imzolangan?", "1898-yil 10-dekabrda Parijda", "1903-yilda Vashingtonda", "1899-yilda Madridda", "1898-yilda Gavanada", "1898-yil 10-dekabrda Parijda.")
t.B("AQSH Kubaga majburan shartnomani qachon qabul qildirgan?", "1903-yilda", "1898-yilda", "1910-yilda", "1889-yilda", "1903-yilda.")
t.B("1911-yil oxirida AQSHning Meksikaga kiritgan kapitali qancha bo‘lgan?", "1,5 mlrd. dollar", "10 mln. dollar", "3 mlrd. dollar", "20 mlrd. dollar", "1,5 mlrd. dollar.")
t.B("Panama kanali qaysi davlat hududida bo‘lgan?", "Kolumbiya", "Meksika", "Nikaragua", "Kosta-Rika", "Kolumbiya hududida.")
t.B("AQSH Panamada Kolumbiyaga qarshi isyonni qachon tashkil etgan?", "1903-yilda", "1898-yilda", "1914-yilda", "1889-yilda", "1903-yilda.")
t.B("Panama kanal shartnomasi evaziga qancha olgan?", "10 mln. dollar", "1,5 mlrd. dollar", "20 mln. dollar", "1 mln. dollar", "10 mln. dollar va har yili renta.")
t.B("Panama kanali qurilishi qachon tugallangan?", "1914-yilda", "1903-yilda", "1910-yilda", "1898-yilda", "1914-yilda.")
t.B("IV Panamerika konferensiyasi qayerda o‘tkazilgan?", "Buenos-Ayresda", "Vashingtonda", "Mexikoda", "Gavanada", "1910-yilda Buenos-Ayresda.")
t.B("«Dollar diplomatiyasi» siyosatini qaysi prezident e’lon qilgan?", "Taft", "T. Ruzvelt", "Vilson", "Monro", "Prezident Taft.")
t.B("«Monro doktrinasi» qachon qabul qilingan?", "1823-yilda", "1889-yilda", "1899-yilda", "1910-yilda", "1823-yilda — «Amerika amerikaliklar uchun».")
t.B("AQSHni «G‘arbiy yarimshar politsiyasi»ga aylantirgan siyosat qanday nomlangan?", "«Yo‘g‘on kaltak»", "«Dollar diplomatiyasi»", "«Ochiq eshiklar»", "Panamerikanizm", "«Yo‘g‘on kaltak».")
t.B("«Ochiq eshiklar va teng imkoniyatlar» doktrinasi qaysi davlatga nisbatan e’lon qilingan?", "Xitoyga", "Kubaga", "Meksikaga", "Yaponiyaga", "1899-yilda davlat kotibi Xey — Xitoyga nisbatan.")
t.NAT("1898-yilda AQSH harbiy kemasi Gavana reydida portlab ketdi.", "Kongress Ispaniyaga qarshi urush boshlash haqida qaror qabul qildi", "AQSH Kubadan voz kechdi", "Ispaniya AQSHga urush e’lon qildi", "Kuba AQSHga qo‘shildi", "AQSH Ispaniyani aybladi va urush boshlandi.")
t.NAT("Kolumbiya Senati kanal huquqlarini AQSHga berishga qarshilik qildi.", "AQSH Panamada isyon tashkil etib, uni mustaqil respublika deb e’lon qildirdi", "AQSH kanaldan voz kechdi", "Kolumbiya kanalni qurdi", "Fransiya kanalni tugatdi", "1903-yilda Panama «mustaqil» bo‘ldi.")
t.TF("Amerika–Ispaniya urushi dunyoni qayta bo‘lib olish yo‘lidagi birinchi urush edi.", True, "To‘g‘ri.")
t.TF("Parij shartnomasidan keyin Kuba haqiqatan to‘liq mustaqil davlat bo‘ldi.", False, "Noto‘g‘ri: Kuba nomiga mustaqil bo‘lib, amalda AQSHga qaram qoldi.")
t.MUL([("Parij shartnomasiga ko‘ra AQSH Puerto-Riko, Guam va Filippinni oldi.", True),
       ("AQSH Panama kanalini qurayotgan fransuz jamiyatining aksiyalarini arzon sotib olgan.", True),
       ("Vilson AQSH dunyoni boshqarishga intilmasligini e’lon qilgan.", False)],
      "III noto‘g‘ri: Vilson «amerikaliklar dunyoni boshqarishimiz kerak» degan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["«Monro doktrinasi»", "Birinchi Panamerika konferensiyasi", "Gavayi orollari bosib olindi", "«Ochiq eshiklar» doktrinasi", "Panama «mustaqil» bo‘ldi", "IV Panamerika konferensiyasi", "Panama kanali tugallandi"],
      "1823 → 1889 → 1898 → 1899 → 1903 → 1910 → 1914.")
t.MAPMATCH(W, ['Gavayi orollari', 'Alyaska', 'Panama kanali', 'Filippin'],
           ["1898-yilda bosib olingan Tinch okeani markazidagi orollar", "AQSH Rossiyadan sotib olgan hudud", "1914-yilda qurilishi tugallangan kanal", "Ispaniyaga mablag‘ to‘lab olingan Osiyodagi orollar"],
           "1 – Gavayi; 2 – Alyaska; 3 – Panama kanali; 4 – Filippin.")
t.VENN("«Monro doktrinasi»", "«Ochiq eshiklar» doktrinasi",
       [("1823-yilda qabul qilingan", 1), ("«Amerika amerikaliklar uchun»", 1),
        ("1899-yilda Xey e’lon qilgan", 2), ("Xitoyda savdo erkinligini talab qilgan", 2),
        ("AQSH tashqi siyosati doktrinasi", 3)],
       "Monro — 1823, Amerika; Ochiq eshiklar — 1899, Xitoy.")

# 17 Lotin Amerikasi davlatlari
t = Topic('e9j17', 9117); TOPICS['e9j17'] = t
t.B("Nima uchun materik Lotin Amerikasi deb atalgan?", "ispan va portugallar tili lotin tilidan kelib chiqqani uchun", "lotinlar yashagani uchun", "Rim imperiyasi bosib olgani uchun", "lotin alifbosi uchun", "Ispan va portugal tillari lotin tilidan kelib chiqqan.")
t.B("Lotin Amerikasining orqada qolishining asosiy sababi nima edi?", "o‘rta asr feodal tartiblarining saqlanib qolgani", "tabiiy boyliklarning yo‘qligi", "aholining kamligi", "urushlarda mag‘lubiyat", "Feodal tartiblarning saqlanishi.")
t.B("Lotin Amerikasida mustaqil davlatlar tashkil topishi qachonga kelib deyarli tugallangan?", "1870-yilga", "1823-yilga", "1910-yilga", "1898-yilga", "1870-yilga kelib.")
t.B("Lotin Amerikasiga eng ko‘p kapital kiritgan davlat qaysi edi?", "Buyuk Britaniya", "AQSH", "Germaniya", "Fransiya", "Buyuk Britaniya.")
t.B("Ispaniya Kubani qachon bosib olgan?", "1510-yilda", "1868-yilda", "1898-yilda", "1492-yilda", "1510-yilda.")
t.B("1868–1878-yillardagi kurash natijasida Kubada nimaga erishildi?", "qulchilik bekor qilindi", "mustaqillik olindi", "AQSHga qo‘shildi", "monarxiya tiklandi", "Qulchilikning bekor qilinishiga erishildi.")
t.B("1895-yilgi Kuba qo‘zg‘oloniga kimlar boshchilik qilgan?", "Xose Marti va Maksimo Gomes", "Sapata va Vilya", "Madero va Dias", "Bolivar va San-Martin", "Xose Marti va Maksimo Gomes.")
t.B("Meksika qachon mustaqillikni qo‘lga kiritgan?", "1821-yilda", "1876-yilda", "1910-yilda", "1898-yilda", "1821-yilda.")
t.B("Porfirio Dias qachon prezident deb e’lon qilingan?", "1876-yilda", "1911-yilda", "1910-yilda", "1821-yilda", "1876-yilda; 1911-yilgacha hukmronlik qildi.")
t.B("1909-yilda Meksikada dehqonlar harakatiga kim rahbarlik qilgan?", "Emiliano Sapata", "Madero", "Uerta", "Dias", "Emiliano Sapata.")
t.B("Sapata harakatining shiori qanday edi?", "«Yer va ozodlik»", "«Amerika amerikaliklar uchun»", "«Non va tinchlik»", "«Mustaqillik yoki o‘lim»", "«Yer va ozodlik».")
t.B("1910-yilgi saylovda muxolifat kim atrofida birlashgan?", "Madero", "Uerta", "Sapata", "Vilya", "Madero atrofida.")
t.B("1913-yilda davlat to‘ntarishi o‘tkazgan general kim?", "Uerta", "Dias", "Vilya", "Madero", "General Uerta; Madero otib tashlandi.")
t.B("Meksikadagi 1910–1917-yillardagi inqilob tarixga qanday nom bilan kirgan?", "«Burjua inqilobi»", "«Agrar inqilob»", "«Sotsialistik inqilob»", "«Mustaqillik inqilobi»", "«Burjua inqilobi».")
t.B("Mamlakat shimolidagi dehqonlar harakati rahbari kim edi?", "Fransisko Vilya", "Emiliano Sapata", "Madero", "Uerta", "Fransisko Vilya.")
t.B("Sapata va Vilya qo‘shinlari Mexiko shahrini qachon egallagan?", "1914-yilda", "1911-yilda", "1917-yilda", "1910-yilda", "1914-yilda.")
t.NAT("Madero xalqni qo‘zg‘olonga chaqirdi.", "Dias Meksikadan qochishga majbur bo‘ldi, Madero prezident bo‘ldi", "Madero qatl etildi", "Dias kuchaydi", "AQSH Meksikani bosib oldi", "Dias qochdi, Madero poytaxtga kirdi.")
t.NAT("Dehqonlar qo‘zg‘oloni yengildi.", "hukumat agrar masalani qisman hal etib, 1917-yilda demokratik konstitutsiya qabul qildi", "barcha yerlar latifundistlarga qaytdi", "Meksika AQSHga qo‘shildi", "Dias qaytib keldi", "Qo‘zg‘olon izsiz ketmadi.")
t.TF("Madero ish kunini 10 soatgacha cheklab, jarima tizimini bekor qilgan.", True, "To‘g‘ri.")
t.TF("Dias diktaturasi davrida Meksika chet el monopoliyalaridan to‘liq mustaqil bo‘lgan.", False, "Noto‘g‘ri: Meksika ularning yarimmustamlakasiga aylandi.")
t.MUL([("Sapataning agrar dasturi hindulardan tortib olingan yerlarni qaytarishni talab qilgan.", True),
       ("XIX asr oxirida Lotin Amerikasi amalda Britaniya va AQSHning yarimmustamlakalariga aylangan.", True),
       ("Uerta diktaturasini faqat oddiy xalq qo‘llab-quvvatlagan.", False)],
      "III noto‘g‘ri: oddiy xalq ham, milliy burjuaziya ham Uertaga qarshi chiqqan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Meksika mustaqillikka erishdi", "Porfirio Dias prezident bo‘ldi", "Kubada Xose Marti qo‘zg‘oloni", "Meksikada prezidentlik saylovi", "Uerta to‘ntarishi", "Demokratik konstitutsiya qabul qilindi"],
      "1821 → 1876 → 1895 → 1910 → 1913 → 1917.")
t.MAPMATCH(LA, ['Mexiko', 'Kuba', 'Kolumbiya'],
           ["1914-yilda Sapata va Vilya qo‘shinlari egallagan poytaxt", "1895-yilda Xose Marti qo‘zg‘oloni bo‘lgan orol", "Ispaniya zulmiga qarshi uzoq kurashgan, keyinchalik Panama ajralib chiqqan davlat"],
           "1 – Mexiko; 2 – Kuba; 3 – Kolumbiya.")
t.VENN("Emiliano Sapata", "Fransisko Vilya",
       [("mamlakat janubidagi dehqonlar rahbari", 1), ("1911-yilda agrar dasturini e’lon qilgan", 1),
        ("mamlakat shimolidagi dehqonlar rahbari", 2), ("bayrog‘ida «Yer va ozodlik» shiori", 2),
        ("1914-yilda Mexikoni egallagan", 3)],
       "Sapata — janub, agrar dastur; Vilya — shimol, bayroq; ikkalasi 1914-yilda Mexikoni egalladi.")
