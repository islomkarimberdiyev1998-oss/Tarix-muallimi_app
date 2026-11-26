from qlib import Topic
TOPICS = {}
W = 'globe'; EU = 'europe'; EA = 'eastasia'

# 1 Xalqaro munosabatlar 1918–1939
t = Topic('e10j1', 1001); TOPICS['e10j1'] = t
t.B("Parij tinchlik konferensiyasi qayerda o‘tgan?", "Versal saroyida", "Vashingtonda", "Lozannada", "Londonda", "Parij yaqinidagi Versal saroyida.")
t.B("Parij tinchlik konferensiyasida nechta davlat vakillari qatnashgan?", "27 ta", "9 ta", "4 ta", "50 ta", "27 davlat vakillari ishtirok etdi.")
t.B("«Katta uchlik»ka kimlar kirgan?", "Lloyd Jorj, Klemanso, Vilson", "Cherchill, Ruzvelt, Stalin", "Gitler, Mussolini, Xiroxito", "Bismark, Kavur, Napoleon III", "Lloyd Jorj, Klemanso va Vudro Vilson.")
t.B("Germaniya Versal tinchlik shartnomasini qachon imzolagan?", "1919-yil 28-iyunda", "1919-yil 18-yanvarda", "1920-yil 21-yanvarda", "1918-yil 11-noyabrda", "1919-yil 28-iyunda.")
t.B("Germaniya qancha reparatsiya to‘lashi lozim edi?", "132 mlrd. marka", "13 mlrd. marka", "1 mlrd. dollar", "500 mln. marka", "132 mlrd. marka reparatsiya.")
t.B("Millatlar Ligasi kimning tashabbusi bilan tashkil qilingan?", "Vudro Vilson", "Lloyd Jorj", "Klemanso", "Lenin", "AQSH prezidenti Vudro Vilson tashabbusi bilan.")
t.B("Ma’lum hududni boshqarish vakolati qanday atalgan?", "mandat", "reparatsiya", "konsessiya", "protektorat", "Mandat – hududni boshqarish vakolati.")
t.B("Vashington konferensiyasi qaysi davrda o‘tgan?", "1921-yil noyabr – 1922-yil fevral", "1919–1920", "1923", "1925", "1921-yil 12-noyabr – 1922-yil 6-fevral.")
t.B("Vashington konferensiyasida nechta davlat qatnashgan?", "to‘qqizta", "27 ta", "to‘rtta", "uchta", "To‘qqiz davlat vakillari ishtirok etdi.")
t.B("Turkiyaning chegaralarini belgilagan shartnoma qaysi?", "1923-yilgi Lozanna shartnomasi", "Versal shartnomasi", "Vashington shartnomasi", "Sevr shartnomasi", "1923-yili Lozanna tinchlik shartnomasi.")
t.B("1919–1923-yillardagi xalqaro munosabatlar tizimi qanday nom olgan?", "Versal-Vashington tizimi", "Vena tizimi", "Yalta-Potsdam tizimi", "Vestfal tizimi", "Versal-Vashington tizimi.")
t.B("Italiyada paydo bo‘lgan o‘ng radikal siyosiy oqim qanday atalgan?", "fashizm", "liberalizm", "kommunizm", "anarxizm", "Fashizm (birlashma).")
t.B("Yaponiya Manchjuriyani qachon bosib olgan?", "1931–1932-yillarda", "1937-yilda", "1933-yilda", "1921-yilda", "1931–1932-yillarda; Manchjou-Go tuzildi.")
t.B("Yaponiya Millatlar Ligasidan qachon chiqqan?", "1933-yilda", "1931-yilda", "1937-yilda", "1939-yilda", "1933-yili.")
t.B("Yaponiya Xitoyga qarshi keng miqyosli urushni qachon boshlagan?", "1937-yil iyulda", "1931-yilda", "1933-yilda", "1941-yilda", "1937-yil iyulda.")
t.NAT("Versal shartnomasi Germaniyani urush uchun yagona javobgar deb e’lon qildi.", "g‘olib va mag‘lublar o‘rtasida o‘ch olish intilishi kuchayib, yangi urushga yo‘l ochildi", "Germaniya tinchliksevar bo‘ldi", "reparatsiya bekor qilindi", "Millatlar Ligasi kuchaydi",
      "Ziddiyatlar tizimi yangi urushga olib keldi.")
t.NAT("Millatlar Ligasi Britaniya va Fransiyaga mandat berdi (1919).", "g‘oliblarning dunyoni bo‘lib olishiga qonuniy tus berildi", "mustamlakalar ozod bo‘ldi", "Germaniya mustamlakalarini qaytardi", "Turkiya kuchaydi",
      "Liga g‘oliblarning dunyoni bo‘lib olishini qonunlashtirdi.")
t.TF("Dastlab mag‘lub davlatlar va Sovet Rossiyasi Millatlar Ligasiga qabul qilinmagan.", True, "To‘g‘ri.")
t.TF("1930-yillar oxirida Yevropa davlatlari Versal-Vashington tizimiga qat’iy amal qilgan.", False, "Noto‘g‘ri: hech bir davlat unga amal qilmay qo‘ydi.")
t.MUL([("1921-yil dekabrda AQSH, Britaniya, Fransiya va Yaponiya to‘rt davlat shartnomasini imzolagan.", True), ("Vashington konferensiyasida asosiy rolni AQSH, Britaniya va Yaponiya o‘ynagan.", True), ("SSSR va AQSH 1930-yillarda Germaniya bilan harbiy ittifoq tuzgan.", False)],
      "III noto‘g‘ri: ular kutib turishni ma’qul ko‘rgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Parij konferensiyasi ochildi", "Versal shartnomasi imzolandi", "Vashington konferensiyasi boshlandi", "Lozanna shartnomasi", "Yaponiya Ligadan chiqdi", "Yaponiya–Xitoy urushi boshlandi"],
      "1919 yanvar → 1919 iyun → 1921 → 1923 → 1933 → 1937.")
t.MAPMATCH(W, ['Versal', 'Vashington', 'Manchjuriya'],
           ["1919–1920-yillardagi tinchlik konferensiyasi joyi", "1921–1922-yillardagi konferensiya joyi", "1931–1932-yillarda Yaponiya bosib olgan hudud"],
           "1 – Versal; 2 – Vashington; 3 – Manchjuriya.")
t.VENN("Parij konferensiyasi", "Vashington konferensiyasi",
       [("Versal saroyida o‘tgan", 1), ("Millatlar Ligasi tuzilgan", 1),
        ("Uzoq Sharq va Tinch okeani muammolari", 2), ("dengiz qurollarini cheklash", 2),
        ("Versal-Vashington tizimini shakllantirgan", 3)],
       "Parij – Versal, Liga. Vashington – Tinch okeani. Ikkalasi Versal-Vashington tizimini shakllantirgan.")

# 2 Ilmiy-texnik taraqqiyot
t = Topic('e10j2', 1002); TOPICS['e10j2'] = t
t.B("Nemis olimlari uran yadrolari parchalanishining zanjirli reaksiyasini qachon kashf etgan?", "1938-yilda", "1942-yilda", "1945-yilda", "1928-yilda", "1938-yili.")
t.B("Ilk atom reaktorini kim yaratgan?", "Enriko Fermi", "Frederik Jolio-Kyuri", "Aleksandr Fleming", "Boris Grabovskiy", "1942-yili Chikagoda Enriko Fermi yaratdi.")
t.B("Ilk atom reaktori qayerda yaratilgan?", "Chikagoda", "Nyu-Yorkda", "Londonda", "Berlinda", "Chikagoda.")
t.B("Birinchi atom bombasi qachon va qayerda portlatilgan?", "1945-yilda Nyu-Meksiko poligonida", "1942-yilda Chikagoda", "1938-yilda Germaniyada", "1949-yilda SSSRda", "1945-yili Nyu-Meksiko shtatidagi poligonda.")
t.B("Harakatlanuvchi tasvirni elektron-nurli trubka yordamida birinchi bo‘lib qayerda uzatishgan?", "Toshkentda", "Nyu-Yorkda", "Londonda", "Moskvada", "1928-yili Toshkentda.")
t.B("1928-yilgi televideniye tajribasini kimlar o‘tkazgan?", "Boris Grabovskiy va Ivan Belyanskiy", "Makleod va Banting", "Fermi va Jolio-Kyuri", "Fleming va Banting", "Ixtirochilar Grabovskiy va Belyanskiy.")
t.B("Birinchi ovozli kino deb qaysi film tan olingan?", "«Jaz kuychisi»", "«Zamonaviy davr»", "«Buyuk diktator»", "«Shelkunchik»", "1927-yili Nyu-Yorkda namoyish qilingan «Jaz kuychisi».")
t.B("Insulinni kimlar olishga muvaffaq bo‘lgan?", "Jon Makleod va Frederik Banting", "Fleming va Fermi", "Grabovskiy va Belyanskiy", "Jolio-Kyuri va Fermi", "1922-yili Makleod va Banting.")
t.B("Insulinning kashf etilishi qaysi kasallikni davolash imkonini bergan?", "qandli diabet", "vabo", "sil", "bezgak", "Qandli diabet endi bedavo dard bo‘lmay qoldi.")
t.B("Penitsillinni kim kashf qilgan?", "Aleksandr Fleming", "Frederik Banting", "Enriko Fermi", "Jon Makleod", "1928-yili britaniyalik Aleksandr Fleming.")
t.B("Fleming Nobel mukofotiga qachon sazovor bo‘lgan?", "1945-yilda", "1928-yilda", "1922-yilda", "1938-yilda", "1945-yili.")
t.B("Bi-bi-si radiokorporatsiyasi qachon tashkil qilingan?", "1927-yilda", "1922-yilda", "1938-yilda", "1945-yilda", "1927-yili Buyuk Britaniyada.")
t.B("AQSH va Germaniyada qanday sun’iy tolalar olingan?", "kapron, perlon, neylon", "paxta, jun, ipak", "zig‘ir, kanop", "shisha, po‘lat", "Kapron, perlon, neylon, sintetik qatron.")
t.NAT("Penitsillin va boshqa antibiotiklar kashf etildi.", "yuqumli kasalliklarni davolashda haqiqiy inqilob bo‘ldi", "kasalliklar ko‘paydi", "tibbiyot rivoji to‘xtadi", "vitaminlar kashf etilmadi",
      "Antibiotiklar yuqumli kasalliklar davolashini tubdan o‘zgartirdi.")
t.NAT("Vitaminlar, gormonlar kashf etildi, virusologiya rivojlandi.", "mikrobiologiya sanoati paydo bo‘lishiga asos yaratildi", "kimyo rivoji to‘xtadi", "kino san’ati tug‘ildi", "atom bombasi yaratildi",
      "Bu kashfiyotlar mikrobiologiya sanoatiga asos bo‘ldi.")
t.TF("Zamonaviy televideniye Toshkentdagi tramvay tresti bazasida o‘tkazilgan tajribadan boshlangan deb hisoblanadi.", True, "To‘g‘ri.")
t.TF("Atom bombasini yaratishda Germaniya AQShdan oldinlab ketgan.", False, "Noto‘g‘ri: AQSH raqiblaridan ancha oldinlab ketgan.")
t.MUL([("1930-yillar oxirida rivojlangan mamlakatlar sanoatining katta qismi elektrlashtirilgan.", True), ("Makleod va Banting Nobel mukofotiga sazovor bo‘lgan.", True), ("Sun’iy tolalarni ommaviy ishlab chiqarish Birinchi jahon urushidan oldin boshlangan.", False)],
      "III noto‘g‘ri: ommaviy ishlab chiqarish Ikkinchi jahon urushidan keyin boshlandi.")
t.MATCH("Kashfiyotlarni mualliflari bilan moslashtiring.", ["Ilk atom reaktori", "Insulin", "Penitsillin", "Elektron televideniye tajribasi"],
        ["Enriko Fermi", "Makleod va Banting", "Aleksandr Fleming", "Grabovskiy va Belyanskiy", "Jolio-Kyuri"], 'abcd',
        "Reaktor – Fermi; insulin – Makleod va Banting; penitsillin – Fleming; TV – Grabovskiy va Belyanskiy.")
t.CHR("Kashfiyotlarni xronologik ketma-ketlikda joylashtiring.", ["Insulin olindi", "«Jaz kuychisi» namoyish qilindi", "Toshkentda TV tajribasi", "Zanjirli reaksiya kashf etildi", "Ilk atom reaktori", "Birinchi atom bombasi"],
      "1922 → 1927 → 1928 → 1938 → 1942 → 1945.")
t.MAPMATCH(W, ['Chikago', 'Nyu-Meksiko', 'Toshkent (1928)', 'London'],
           ["1942-yilda ilk atom reaktori yaratilgan shahar", "1945-yilda birinchi atom bombasi portlatilgan shtat", "1928-yilda elektron televideniye tajribasi o‘tkazilgan shahar", "Bi-bi-si joylashgan mamlakat poytaxti"],
           "1 – Chikago; 2 – Nyu-Meksiko; 3 – Toshkent; 4 – London.")
t.VENN("Insulin", "Penitsillin",
       [("Makleod va Banting olgan", 1), ("qandli diabetni davolash imkonini bergan", 1),
        ("Fleming mog‘ordan kashf etgan", 2), ("antibiotiklar davrini boshlagan", 2),
        ("kashfiyotchilari Nobel mukofotini olgan", 3)],
       "Insulin – diabet; penitsillin – antibiotik. Ikkalasi Nobel mukofotiga sazovor bo‘lgan.")

# 3 Buyuk Britaniya 1918–1939
t = Topic('e10j3', 1003); TOPICS['e10j3'] = t
t.B("Urushdan keyin Buyuk Britaniya kimdan qarzdor bo‘lib qolgan?", "AQSH va o‘z dominionlaridan", "Fransiyadan", "Germaniyadan", "Rossiyadan", "Kreditor bo‘lgan Britaniya AQSH va dominionlardan qarzdor bo‘ldi.")
t.B("Britaniya tarixidagi eng katta umumiy ish tashlash qachon bo‘lgan?", "1926-yil mayda", "1919-yilda", "1931-yilda", "1934-yilda", "1926-yil mayda.")
t.B("Britaniya qachondan inqirozdan chiqa boshlagan?", "1934-yildan", "1929-yildan", "1937-yildan", "1940-yildan", "1934-yildan boshlab.")
t.B("1937-yilda Britaniya nimaga erishgan?", "inqirozdan oldingi ko‘rsatkichlarga yetib oldi", "eng katta ish tashlash bo‘ldi", "leyboristlar g‘alaba qozondi", "Hindiston mustaqil bo‘ldi", "Sanoat inqirozdan oldingi ko‘rsatkichlarga yetdi.")
t.B("Uzoq yillar Britaniyani boshqargan ikki partiya qaysilar?", "konservatorlar va liberallar", "leyboristlar va kommunistlar", "respublikachilar va demokratlar", "vig va tori", "Konservatorlar va liberallar.")
t.B("Leyboristlar birinchi marta qachon hukumatni boshqargan?", "1924-yil yanvarda", "1918-yilda", "1931-yilda", "1940-yilda", "1924-yil yanvarda.")
t.B("1937–1940-yillarda hukumatni kim boshqargan?", "Nevill Chemberlen", "Uinston Cherchill", "Lloyd Jorj", "Stenli Bolduin", "Konservatorlar yetakchisi Nevill Chemberlen.")
t.B("Hindistonning qaysi shahrida 1919-yilda ingliz qo‘shinlari namoyishchilarni o‘qqa tutgan?", "Amritsar", "Dehli", "Kalkutta", "Bombey", "Amritsar shahrida.")
t.B("Britaniya Misr mustaqilligini qachon tan olgan?", "1922-yilda", "1919-yilda", "1931-yilda", "1936-yilda", "1922-yili.")
t.B("«Ozod Irlandiya davlati» qachon tan olingan?", "1921-yil dekabrda", "1922-yilda", "1919-yilda", "1931-yilda", "1921-yil dekabrda dominion huquqli davlat sifatida.")
t.B("Dominionlar bilan munosabatlarni qaysi hujjat belgilagan?", "Vestminster statuti (1931)", "Versal shartnomasi", "Myunxen kelishuvi", "Lozanna shartnomasi", "1931-yilgi Vestminster statuti.")
t.B("Dominionlar va metropoliya qanday ittifoqni tashkil qilgan?", "Britaniya Millatlar Hamdo‘stligi", "Millatlar Ligasi", "Antanta", "Muqaddas ittifoq", "Britaniya Millatlar Hamdo‘stligi.")
t.B("Britaniyaning fashistlarga faol qarshilik ko‘rsatmaslik siyosati qanday nom olgan?", "«tajovuzkorga yon berish»", "«yopiq eshiklar»", "«yangi kurs»", "«qit’a qamali»", "«Tajovuzkorga yon berish» siyosati.")
t.B("Myunxen kelishuvi qachon imzolangan?", "1938-yilda", "1939-yilda", "1936-yilda", "1940-yilda", "1938-yili.")
t.B("Myunxen kelishuviga ko‘ra Germaniyaga qaysi hudud berilgan?", "Sudet viloyati", "Elzas", "Saar", "Polsha", "Chexoslovakiyaning Sudet viloyati.")
t.B("Britaniya Germaniyaga qachon urush e’lon qilgan?", "1939-yil 3-sentabrda", "1939-yil 1-sentabrda", "1940-yilda", "1938-yilda", "1939-yil 3-sentabrda.")
t.NAT("1938-yilda Myunxen kelishuvi imzolandi.", "Chemberlen 1940-yilda iste’foga chiqdi, hukumatni Cherchill boshqardi", "Germaniya tinchlandi", "Chexoslovakiya kuchaydi", "SSSR Germaniyaga urush ochdi",
      "Myunxen kelishuvi oqibatida Chemberlen iste’foga chiqdi.")
t.NAT("Germaniya 1939-yil 1-sentabrda Polshaga bostirib kirdi.", "Britaniya Germaniyaga urush e’lon qilib, Ikkinchi jahon urushiga qo‘shildi", "Britaniya betaraf qoldi", "Polsha Germaniyani yengdi", "Myunxen kelishuvi yangilandi",
      "3-sentabr kuni Britaniya urushga qo‘shildi.")
t.TF("Jahon iqtisodiy inqirozi Britaniya iqtisodiyotiga juda katta ta’sir qilmagan.", True, "To‘g‘ri.")
t.TF("Leyboristlar 1924-yilda Jamoa palatasida mutlaq ko‘pchilikka ega bo‘lgan.", False, "Noto‘g‘ri: ko‘pchilikka ega bo‘lmagan va bir yildan kam hokimiyatda turgan.")
t.MUL([("Sanoat o‘sishi avtomobil, samolyotsozlik, radioapparatura hisobiga bo‘lgan.", True), ("Britaniya Afg‘oniston va Eron siyosatini nazorat qilishdan voz kechgan.", True), ("Britaniya fashistlarga qarshi 1930-yillarda faol kurashgan.", False)],
      "III noto‘g‘ri: «tajovuzkorga yon berish» siyosatini yuritgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Amritsar fojiasi", "Ozod Irlandiya tan olindi", "Misr mustaqilligi tan olindi", "Leyboristlar hukumati", "Umumiy ish tashlash", "Vestminster statuti", "Myunxen kelishuvi"],
      "1919 → 1921 → 1922 → 1924 → 1926 → 1931 → 1938.")
t.MAPMATCH(EU, ['Irlandiya', 'Myunxen', 'Sudet viloyati', 'Polsha'],
           ["1921-yilda dominion huquqini olgan davlat", "1938-yilgi kelishuv imzolangan shahar", "Myunxen kelishuvi bilan Germaniyaga berilgan hudud", "1939-yil 1-sentabrda Germaniya bostirib kirgan davlat"],
           "1 – Irlandiya; 2 – Myunxen; 3 – Sudet; 4 – Polsha.")
t.VENN("Chemberlen", "Cherchill",
       [("«tajovuzkorga yon berish» siyosati", 1), ("Myunxen kelishuvini imzolagan", 1),
        ("1940-yildan hukumat boshlig‘i", 2), ("XX asr Britaniya tarixida juda katta rol o‘ynagan", 2),
        ("Britaniya bosh vaziri", 3)],
       "Chemberlen – Myunxen; Cherchill – 1940-yildan. Ikkalasi bosh vazir.")

# 4 Fransiya 1918–1939
t = Topic('e10j4', 1004); TOPICS['e10j4'] = t
t.B("Urush natijasida Fransiya hududining qancha qismida korxonalar vayron bo‘lgan?", "uchdan bir qismida", "yarmida", "to‘rtdan bir qismida", "hammasida", "Hududining uchdan bir qismidagi korxonalar vayron qilindi.")
t.B("Versal shartnomasiga ko‘ra Fransiya qaysi hududlarni qaytarib olgan?", "Elzas va Lotaringiya", "Saar va Rur", "Sudet va Bogemiya", "Korsika va Sardiniya", "Elzas va Lotaringiya.")
t.B("Fransiya Saar ko‘mir havzasini necha yilga egallagan?", "15 yilga", "5 yilga", "50 yilga", "abadiy", "15 yilga.")
t.B("Jahon iqtisodiy inqirozi Fransiyada qachon boshlangan?", "1930-yilda", "1929-yilda", "1933-yilda", "1926-yilda", "1930-yili.")
t.B("1919-yil noyabrdagi saylovda tuzilgan burjua partiyalari guruhi qanday atalgan?", "Milliy blok", "Xalq fronti", "Leyboristlar", "Milliy front", "Milliy blok.")
t.B("Milliy blok saylovda qancha ovoz olgan?", "2/3 qismdan ko‘proq", "yarmi", "1/3 qismi", "10 foiz", "2/3 qismdan ko‘proq ovoz oldi.")
t.B("Qaysi yillarda hukumat pul qadrsizlanishini to‘xtatgan?", "1926–1929", "1919–1924", "1930–1934", "1936–1938", "1926–1929-yillarda.")
t.B("Fashistlarga qarshi faol harakat qilgan kuch qaysi?", "Xalq fronti", "Milliy blok", "o‘nglar", "royalistlar", "Faqat Xalq fronti faol harakat qildi.")
t.B("«Xalq frontidan ko‘ra Gitler ma’qul» degan o‘nglar yetakchisi kim?", "Pyer Laval", "Eduard Daladye", "Klemanso", "de Goll", "Pyer Laval.")
t.B("Myunxen kelishuvini ma’qullagan fransuz hukumati boshlig‘i kim?", "Eduard Daladye", "Pyer Laval", "Klemanso", "Puankare", "Eduard Daladye hukumati.")
t.B("Nemis qo‘shinlari Parijga qachon kirib kelgan?", "1940-yil 14-iyunda", "1939-yil 3-sentabrda", "1938-yilda", "1944-yilda", "1940-yil 14-iyunda.")
t.B("Bir irqning boshqalardan ustunligini da’vo qiluvchi ashaddiy millatchilik qanday ataladi?", "shovinizm", "liberalizm", "gumanizm", "pasifizm", "Shovinizm.")
t.NAT("Germaniya ustidan g‘alaba qozonildi.", "mamlakatda shovinistik kayfiyat keng tarqaldi", "Fransiya qashshoqlashmadi", "sotsialistlar hokimiyatga keldi", "qishloq xo‘jaligi gullab-yashnadi",
      "G‘alabadan so‘ng shovinistik kayfiyat tarqaldi.")
t.NAT("Fransiya Myunxen kelishuvini ma’qulladi.", "yangi jahon urushiga yo‘l ochildi, Fransiya uning birinchi qurbonlaridan biri bo‘ldi", "Germaniya tinchlandi", "Chexoslovakiya kuchaydi", "Fransiya SSSR bilan ittifoq tuzdi",
      "Uchinchi respublika nemis qo‘shinlari oyog‘i ostida barbod bo‘ldi.")
t.TF("1926–1929-yillarda keksalik, kasallik va nogironlik uchun pensiyalar joriy qilingan.", True, "To‘g‘ri.")
t.TF("Fransiyada sanoat ishlab chiqarishi 1930-yillar oxirida inqirozdan oldingi darajadan oshib ketgan.", False, "Noto‘g‘ri: inqirozdan oldingi darajaga ham yetmadi.")
t.MUL([("1920-yillarda avtomobil, samolyotsozlik, kimyo sanoati paydo bo‘lgan.", True), ("1929–1932-yillarda bir nechta hukumat almashgan.", True), ("Urushdan keyin qishloq xo‘jaligi tez o‘sgan.", False)],
      "III noto‘g‘ri: qishloq xo‘jaligi turg‘unlikda edi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Milliy blok saylovda g‘alaba qozondi", "Pul qadrsizlanishi to‘xtatildi", "Inqiroz Fransiyada boshlandi", "O‘nglar yana hokimiyatga keldi", "Myunxen kelishuvi", "Nemislar Parijga kirdi"],
      "1919 → 1926–1929 → 1930 → 1934 → 1938 → 1940.")
t.MAPMATCH(EU, ['Elzas', 'Saar', 'Parij'],
           ["Versal shartnomasi bilan qaytarilgan hudud (Lotaringiya bilan)", "15 yilga egallangan ko‘mir havzasi", "1940-yil 14-iyunda nemislar kirgan poytaxt"], "1 – Elzas; 2 – Saar; 3 – Parij.")
t.VENN("Milliy blok", "Xalq fronti",
       [("burjua partiyalari guruhi", 1), ("1919-yilda saylovda g‘alaba qozongan", 1),
        ("fashistlarga qarshi faol harakat qilgan", 2), ("o‘nglar uni «sovetlashtirish»da ayblagan", 2),
        ("Fransiya siyosiy kuchi", 3)],
       "Milliy blok – burjua, 1919. Xalq fronti – antifashist. Ikkalasi siyosiy kuch.")
