from qlib import Topic
TOPICS = {}
W = 'globe'; EU = 'europe'; EA = 'eastasia'; IN = 'india'; OA = 'oldasia'; AF = 'africa'

# 11 Yaponiya 1918–1939
t = Topic('e10j11', 1011); TOPICS['e10j11'] = t
t.B("XX asr boshida Osiyoda yetakchi davlatlarga qaram bo‘lmagan yagona davlat qaysi?", "Yaponiya", "Xitoy", "Hindiston", "Turkiya", "Yaponiya – Osiyo mintaqasidagi yagona shunday davlat.")
t.B("Yaponiyada sanoat to‘ntarishi qachon yuz bergan?", "1920-yillar o‘rtalarida", "1930-yillar oxirida", "1918-yilda", "1940-yillarda", "1920-yillar o‘rtalarida.")
t.B("Og‘ir sanoatda qaysi konsernlar mustahkamlangan?", "«Mitsubisi» va «Sumitomo»", "«Toyota» va «Honda»", "«Sony» va «Panasonic»", "«Krupp» va «Simens»", "«Mitsubisi» va «Sumitomo».")
t.B("Yaponiya inqirozdan chiqish yo‘li sifatida nimani tanlagan?", "iqtisodni militarizatsiyalash va tajovuzkorlikni", "«Yangi kurs»ni", "NEPni", "neytralitetni", "Militarizatsiya va tajovuzkorlik.")
t.B("Sovet-yapon munosabatlari qachondan yo‘lga qo‘yilgan?", "1925-yildan", "1918-yildan", "1933-yildan", "1941-yildan", "1925-yildan.")
t.B("«Yosh ofitserlar» tarafidagi hukumat boshlig‘i kim?", "general Giiti Tanaka", "Fumimaro Konoe", "Mutsuxito", "Xiroxito", "General Giiti Tanaka.")
t.B("«Yosh ofitserlar» isyoni qachon bo‘lgan?", "1932-yil mayda", "1931-yilda", "1936-yilda", "1925-yilda", "1932-yil mayda.")
t.B("Yaponiya Manchjuriyani qachon bosib olgan?", "1931-yilda", "1937-yilda", "1933-yilda", "1925-yilda", "1931-yili; Manchjou-Go tuzildi.")
t.B("Yaponiya va Germaniya antikomintern paktini qachon imzolagan?", "1936-yil noyabrda", "1937-yilda", "1933-yilda", "1940-yilda", "1936-yil noyabrda.")
t.B("Antikomintern paktiga 1937-yilda qaysi davlat qo‘shilgan?", "Italiya", "Ispaniya", "SSSR", "Turkiya", "Italiya qo‘shildi.")
t.B("Tajovuzkor davlatlar ittifoqi qanday nom olgan?", "«Berlin – Rim – Tokio» uchburchagi", "Antanta", "Muqaddas ittifoq", "Millatlar Ligasi", "«Berlin – Rim – Tokio» uchburchagi.")
t.B("1938-yilda Sharqiy Osiyoda yangi tartib o‘rnatishni e’lon qilgan hukumat boshlig‘i kim?", "Fumimaro Konoe", "Giiti Tanaka", "Tojo", "Meydzi", "General Fumimaro Konoe hukumati.")
t.B("Hasan ko‘li atrofidagi sovet-yapon mojarosi qachon bo‘lgan?", "1938-yil iyul–avgustda", "1939-yil mayda", "1941-yilda", "1931-yilda", "1938-yil iyul–avgustda.")
t.B("Yaponiya SSSR bilan neytralitet paktini qachon imzolagan?", "1941-yil 5-aprelda", "1939-yil sentabrda", "1936-yilda", "1945-yilda", "1941-yil 5-aprelda.")
t.NAT("Millatlar Ligasi Manchjuriya bosqiniga qarshi chiqdi.", "Yaponiya 1933-yilda Ligadan chiqdi", "Yaponiya Manchjuriyani qaytardi", "Liga Yaponiyaga urush ochdi", "Xitoy Yaponiyani bosib oldi",
      "Yaponiya 1933-yili Ligadan chiqdi.")
t.NAT("1925-yildan sovet-yapon munosabatlari yo‘lga qo‘yildi.", "yapon qo‘shinlari Shimoliy Saxalindan olib chiqildi", "Yaponiya Saxalinni bosib oldi", "SSSR Yaponiyaga urush ochdi", "Hasan ko‘li mojarosi bo‘ldi",
      "Hamkorlik va Shimoliy Saxalindan qo‘shinlar olib chiqilishida aks etdi.")
t.TF("Yaponiyadagi totalitar tizim avtoritar-monarxistik shaklga ega bo‘lgan.", True, "To‘g‘ri.")
t.TF("Xalxin-Gol urushi Hasan ko‘li janglaridan kichikroq bo‘lgan.", False, "Noto‘g‘ri: miqyosi bo‘yicha ancha yirik edi.")
t.MUL([("Yapon mahsulotlari sifati past bo‘lgani uchun tashqi bozorda raqobatbardosh emasdi.", True), ("«Yosh ofitserlar» diktatura o‘rnatishni talab qilgan.", True), ("1932-yilgi «Yosh ofitserlar» isyoni g‘alaba qozongan.", False)],
      "III noto‘g‘ri: isyon muvaffaqiyat qozonmagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Sovet-yapon munosabatlari yo‘lga qo‘yildi", "Manchjuriya bosib olindi", "«Yosh ofitserlar» isyoni", "Antikomintern pakti", "Hasan ko‘li mojarosi", "Neytralitet pakti"],
      "1925 → 1931 → 1932 → 1936 → 1938 → 1941.")
t.MAPMATCH('fareast', ['Manchjuriya', 'Saxalin', 'Tokio'],
           ["1931-yilda Yaponiya bosib olgan Xitoy provinsiyasi", "1925-yildan yapon qo‘shinlari olib chiqilgan orol (shimoliy qismi)", "Yaponiya poytaxti, «Berlin – Rim – ...» uchburchagi uchi"], "1 – Manchjuriya; 2 – Saxalin; 3 – Tokio.")
t.VENN("Hasan ko‘li janglari", "Xalxin-Gol janglari",
       [("1938-yil iyul–avgustda bo‘lgan", 1), ("SSSR hududida bo‘lgan", 1),
        ("1939-yil mayda boshlangan", 2), ("Mo‘g‘uliston hududida bo‘lgan", 2),
        ("yaponlar mag‘lubiyati bilan tugagan", 3)],
       "Hasan – 1938, SSSR. Xalxin-Gol – 1939, Mo‘g‘uliston. Ikkalasida yaponlar yengilgan.")

# 12 Xitoy va Hindiston 1918–1939
t = Topic('e10j12', 1012); TOPICS['e10j12'] = t
t.B("Birinchi jahon urushi yillarida Xitoy amalda kimga qaram bo‘lib qolgan?", "Yaponiyaga", "Rossiyaga", "Britaniyaga", "AQShga", "Xitoy amalda Yaponiyaga to‘liq qaram bo‘lib qoldi.")
t.B("Xitoylik talabalar Pekinda qachon namoyish boshlagan?", "1919-yil 4-mayda", "1925-yil 30-mayda", "1920-yil iyulda", "1931-yil sentabrda", "1919-yil 4-may kuni.")
t.B("1920-yil iyulda Pekinda hokimiyatga kim kelgan?", "U Peyfu", "Sun Yatsen", "Chan Kayshi", "Mao Szedun", "Britaniya va AQSH qo‘llagan U Peyfu.")
t.B("Vashington konferensiyasidan so‘ng Yaponiya qaysi viloyatni Xitoyga qaytargan?", "Shandun", "Manchjuriya", "Tayvan", "Koreya", "Shandun viloyatini qaytarishga majbur bo‘ldi.")
t.B("Sun Yatsen Xitoy Respublikasi prezidenti etib qachon saylangan?", "1921-yilda", "1919-yilda", "1925-yilda", "1931-yilda", "1921-yili.")
t.B("Sun Yatsen qachon vafot etgan?", "1925-yil martda", "1921-yilda", "1931-yilda", "1926-yilda", "1925-yil martda.")
t.B("1925-yil bahorida inglizlarga qarshi harakat qanday nom olgan?", "«30-may harakati»", "«4-may harakati»", "«Ixetuan»", "«Taypin»", "«30-may harakati».")
t.B("«Buyuk milliy inqilob»ga qaysi partiya rahbarlik qilgan?", "Gomindan (Milliy partiya)", "Kommunistik partiya", "Liberal partiya", "Leyboristlar", "Gomindan partiyasi.")
t.B("Shimolga yurishni boshlagan Gomindan hukumati boshlig‘i kim?", "Chan Kayshi", "Sun Yatsen", "Mao Szedun", "U Peyfu", "1926-yili general Chan Kayshi.")
t.B("Xitoy Sovet Respublikasi qachon e’lon qilingan?", "1931-yilda", "1926-yilda", "1925-yilda", "1949-yilda", "1931-yili; raisi Mao Szedun.")
t.B("Manchjou-Go davlati qachon e’lon qilingan?", "1932-yil 1-martda", "1931-yil sentabrda", "1937-yilda", "1933-yilda", "1932-yil 1-martda.")
t.B("Hindistonda zo‘ravonliklarsiz ommaviy chiqishlarni tashkil qilgan yetakchi kim?", "Maxatma Gandi", "Javoharlal Neru", "Sun Yatsen", "Muhammad Ali Jinna", "Maxatma Gandi.")
t.B("Gandi qaysi partiyaning g‘oyaviy rahbari bo‘lgan?", "Hindiston Milliy kongressi", "Musulmonlar Ligasi", "Gomindan", "Kommunistik partiya", "Hindiston Milliy kongressi (HMK).")
t.B("Zo‘ravonliklarsiz qarshilik ko‘rsatish usuli qanday nom olgan?", "«Gandizm»", "«Sotsializm»", "«Konservatizm»", "«Gomindan»", "«Gandizm».")
t.B("Jahon urushlari oralig‘ida Hindiston milliy ozodlik harakatining asosiy kuchi kim edi?", "hind dehqonlari", "ishchilar", "zodagonlar", "harbiylar", "Asosiy kuchni hind dehqonlari tashkil qildi.")
t.NAT("1919-yilda G‘arb davlatlari Xitoy talablarini rad etdi.", "xitoylik talabalar Pekinda namoyish boshlab, harakat butun Xitoyni larzaga soldi", "Xitoy Yaponiyaga qo‘shildi", "Xitoy Ligaga kirmadi", "Sun Yatsen vafot etdi",
      "Talabalar harakati katta ijobiy natijalarga olib keldi.")
t.NAT("Gomindanchilar va kommunistlar o‘rtasida ajralish yuz berdi.", "yigirma yil davom etgan fuqarolar urushi boshlandi", "Xitoy birlashdi", "Yaponiya Xitoydan chiqdi", "Sun Yatsen prezident bo‘ldi",
      "Kurash yigirma yillik fuqarolar urushiga aylandi.")
t.NAT("1939-yilda Britaniya Germaniyaga urush e’lon qildi.", "Hindiston vitse-qiroli mamlakatni urush holatida deb e’lon qildi", "Hindiston mustaqil bo‘ldi", "Gandi urushga chaqirdi", "Hindiston betaraf qoldi",
      "Vitse-qirol Hindistonni urush holatida deb e’lon qildi.")
t.TF("Vashington konferensiyasida ishtirokchi davlatlar Xitoyning suvereniteti va hududiy yaxlitligini kafolatlagan.", True, "To‘g‘ri.")
t.TF("Manchjuriya bosqinidan so‘ng xalqaro hamjamiyat Yaponiyaga qarshi qat’iy choralar ko‘rgan.", False, "Noto‘g‘ri: birorta yirik davlat Yaponiya bilan janjallashishni istamadi.")
t.MUL([("Shimolga yurishda Uxan, Nankin, Shanxay gomindanchilar qo‘liga o‘tgan.", True), ("Gandizm qurolli kurashsiz mustamlakachilarning ketishini talab qilgan.", True), ("Britaniya urushdan keyin Hindistonga o‘zini o‘zi boshqarish huquqini bergan.", False)],
      "III noto‘g‘ri: Hindiston maqomi o‘zgarmadi, va’da bajarilmadi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["4-may harakati", "Sun Yatsen prezident bo‘ldi", "«30-may harakati»", "Shimolga yurish boshlandi", "Xitoy Sovet Respublikasi e’lon qilindi", "Manchjou-Go e’lon qilindi"],
      "1919 → 1921 → 1925 → 1926 → 1931 → 1932.")
t.MAPMATCH(EA, ['Pekin', 'Shanxay', 'Shandun', 'Manchjuriya'],
           ["1919-yil 4-may namoyishi boshlangan poytaxt", "1925-yilda «30-may harakati» boshlangan shahar", "Vashington konferensiyasidan so‘ng Yaponiya qaytargan viloyat", "1931-yil sentabrda yaponlar bostirib kirgan hudud"],
           "1 – Pekin; 2 – Shanxay; 3 – Shandun; 4 – Manchjuriya.")
t.VENN("Sun Yatsen", "Chan Kayshi",
       [("1921-yilda Xitoy Respublikasi prezidenti", 1), ("1925-yilda vafot etgan", 1),
        ("1926-yilda Shimolga yurishni boshlagan", 2), ("Manchjuriya bosqini haqida Ligaga murojaat qilgan", 2),
        ("Xitoy milliy inqilobi yetakchisi", 3)],
       "Sun Yatsen – 1921 prezident; Chan Kayshi – 1926 yurish. Ikkalasi milliy inqilob yetakchisi.")

# 13 Turkiya va Eron 1918–1939
t = Topic('e10j13', 1013); TOPICS['e10j13'] = t
t.B("Turkiya hududini Yevropa davlatlari o‘rtasida bo‘lib olishni ko‘zda tutgan shartnoma qaysi?", "1920-yilgi Sevr shartnomasi", "Lozanna shartnomasi", "Versal shartnomasi", "Parij shartnomasi", "1920-yilgi Sevr shartnomasi.")
t.B("Turkiyadagi qarshilik harakatiga kim rahbarlik qilgan?", "general Mustafo Kamol posho", "sulton Mexmed VI", "Rizoxon", "Enver posho", "General Mustafo Kamol posho.")
t.B("Turkiya-Gretsiya urushida Turkiya hududi qachon to‘liq ozod qilingan?", "1922-yil oktabrga kelib", "1920-yilda", "1923-yil 29-oktabrda", "1919-yilda", "1922-yil oktabrga kelib.")
t.B("Buyuk Millat majlisi sulton hokimiyatini qachon bekor qilgan?", "1922-yil 1-noyabrda", "1923-yil 29-oktabrda", "1920-yilda", "1924-yilda", "1922-yil 1-noyabr kuni.")
t.B("Taxtdan ag‘darilgan oxirgi usmonli sulton kim?", "Mexmed VI", "Abdulhamid II", "Mahmud II", "Mustafo III", "Sulton Mexmed VI.")
t.B("Turkiya qachon respublika deb e’lon qilingan?", "1923-yil 29-oktabrda", "1922-yil 1-noyabrda", "1920-yilda", "1932-yilda", "1923-yil 29-oktabrda.")
t.B("Mustafo Kamolga qanday nasab berilgan?", "«Otaturk» (turklar otasi)", "«Posho»", "«G‘ozi»", "«Pahlaviy»", "«Otaturk» – turklar otasi.")
t.B("Otaturk islohotlarining birinchi tamoyili nima edi?", "dunyoviylik – dinni davlatdan ajratish", "sanoatlashtirish", "kollektivlashtirish", "militarizatsiya", "Dunyoviylik.")
t.B("Turkiyada qanday alifbo joriy qilingan?", "lotin alifbosi", "arab alifbosi", "kirill alifbosi", "yunon alifbosi", "Arab alifbosidan voz kechib, lotin alifbosi joriy qilindi.")
t.B("Turkiya Millatlar Ligasiga qachon a’zo bo‘lgan?", "1932-yilda", "1923-yilda", "1934-yilda", "1920-yilda", "1932-yili.")
t.B("1919-yilgi Angliya–Eron shartnomasiga ko‘ra Eron amalda nimaga aylangan?", "Britaniya protektoratiga", "mustaqil respublikaga", "SSSR tarkibiga", "Turkiya qaramog‘iga", "Eron amalda Britaniya protektoratiga aylantirildi.")
t.B("1921-yil fevralda hukumatni ag‘dargan kazaklar polki sardori kim?", "polkovnik Rizoxon", "Muhammad Rizo", "Mustafo Kamol", "Nodirshoh", "Polkovnik Rizoxon.")
t.B("Rizoxon qaysi sulolaning shohi deb e’lon qilingan?", "Pahlaviylar", "Qojarlar", "Safaviylar", "Afshorlar", "1925-yil dekabrda Pahlaviylar sulolasi shohi.")
t.B("Fors nomi o‘rniga «Eron» nomi qachondan qo‘llangan?", "1935-yildan", "1925-yildan", "1928-yildan", "1941-yildan", "1935-yildan.")
t.B("Sovet va ingliz qo‘shinlari Eronga qachon kiritilgan?", "1941-yil avgustda", "1939-yilda", "1942-yilda", "1918-yilda", "1941-yil avgustda.")
t.NAT("Sevr shartnomasi Turkiyani bo‘lib olishni ko‘zda tutdi.", "turk xalqining g‘azabi oshib, Mustafo Kamol boshchiligida qarshilik harakati boshlandi", "Turkiya rozi bo‘ldi", "sulton kuchaydi", "Gretsiya Turkiyani butunlay egalladi",
      "Turk xalqi qarshilik harakatini boshladi.")
t.NAT("1923-yilgi Lozanna shartnomasi imzolandi.", "Turkiya suvereniteti va hududiy yaxlitligini saqlab qoldi", "Turkiya bo‘lib olindi", "Turkiya Britaniya mandatiga o‘tdi", "sultonlik tiklandi",
      "Turkiya suvereniteti va yaxlitligini saqlab qoldi.")
t.NAT("Rizo shoh Germaniya bilan hamkorlikni kuchaytirdi.", "Eronga ko‘plab nemis mutaxassislari va texnikasi kirib keldi", "Eron Germaniyaga urush ochdi", "Britaniya ta’siri kuchaydi", "Eron SSSRga qo‘shildi",
      "Maqsad – inglizlar ta’sirini kamaytirish edi.")
t.TF("Eronda 1935-yilda chodra o‘rab yurishni bekor qilish to‘g‘risida qonun qabul qilingan.", True, "To‘g‘ri.")
t.TF("Rizo shoh agrar sohada keskin islohot o‘tkazib, dehqonlar ahvolini yaxshilagan.", False, "Noto‘g‘ri: keskin o‘zgarish qilmagan, dehqonlar ahvoli o‘zgarmagan.")
t.MUL([("Turkiya 1941-yilda Germaniya bilan do‘stlik shartnomasini imzolagan.", True), ("Eronda Tehron universiteti ochilgan.", True), ("Turkiya Ikkinchi jahon urushida Germaniya tomonida rasman urushgan.", False)],
      "III noto‘g‘ri: Turkiya rasman betaraf qolgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Angliya–Eron shartnomasi", "Sevr shartnomasi", "Rizoxon to‘ntarishi", "Sultonlik bekor qilindi", "Turkiya respublika bo‘ldi", "Rizoxon shoh deb e’lon qilindi"],
      "1919 → 1920 → 1921 → 1922 → 1923 → 1925.")
t.MAPMATCH(OA, ['Anqara', 'Istanbul', 'Tehron'],
           ["respublika Turkiyasining poytaxti (Buyuk Millat majlisi joyi)", "usmonli sultonlarining avvalgi poytaxti", "Rizo shoh davrida universitet ochilgan poytaxt"], "1 – Anqara; 2 – Istanbul; 3 – Tehron.")
t.VENN("Otaturk islohotlari", "Rizo shoh islohotlari",
       [("lotin alifbosi joriy qilingan", 1), ("sultonlik bekor qilinib respublika e’lon qilingan", 1),
        ("chodra o‘rab yurish bekor qilingan", 2), ("mamlakat nomi Fors o‘rniga Eron bo‘lgan", 2),
        ("nasab (familiya) joriy qilingan", 3)],
       "Turkiya – lotin alifbosi, respublika. Eron – chodra, nom. Ikkalasida nasab joriy qilingan.")

# 14 Afrika 1918–1939
t = Topic('e10j14', 1014); TOPICS['e10j14'] = t
t.B("Britaniya Misr ustidan protektoratini bekor qilib, uning mustaqilligini qachon tan olgan?", "1922-yilda", "1923-yilda", "1931-yilda", "1941-yilda", "1922-yili.")
t.B("1923-yilgi konstitutsiyaga ko‘ra Misr qanday davlat deb e’lon qilingan?", "monarxiya", "respublika", "protektorat", "mandat hudud", "Misr monarxiya deb e’lon qilindi.")
t.B("Misr hududiga Germaniya va Italiya qo‘shinlari qachon kiritilgan?", "1941-yilda", "1939-yilda", "1940-yilda", "1922-yilda", "1941-yili.")
t.B("Jazoirdagi milliy-ozodlik harakati rahbari kim?", "Farhod Abbos", "Habib Burg‘iba", "Abdul Karim", "Markus Garvi", "Jazoirda – Farhod Abbos.")
t.B("Tunisdagi milliy-ozodlik harakati rahbari kim?", "Habib Burg‘iba", "Farhod Abbos", "Abdul Karim", "Uilyam Dyubua", "Tunisda – Habib Burg‘iba.")
t.B("Marokashdagi milliy-ozodlik harakati rahbari kim?", "Abdul Karim", "Habib Burg‘iba", "Farhod Abbos", "Mustafo Kamol", "Marokashda – Abdul Karim.")
t.B("Liviyadagi qarshilik harakati qachon bostirilgan?", "1931-yilda", "1922-yilda", "1940-yilda", "1926-yilda", "1931-yili bostirilib, rahbarlari qatl qilindi.")
t.B("Liviya qaysi davlatning mustamlakasiga aylantirilgan?", "Italiya", "Fransiya", "Britaniya", "Ispaniya", "Italiyaning.")
t.B("Millatlar Ligasi «Qullik haqida» konvensiyani qachon qabul qilgan?", "1926-yilda", "1920-yilda", "1931-yilda", "1919-yilda", "1926-yili.")
t.B("Afrikadagi birinchi siyosiy partiya qaysi?", "Afrika Milliy kongressi (AMK)", "Panafrika kongressi", "Vafd", "Neo-Destur", "1920-yili Afrika Milliy kongressi tashkil topdi.")
t.B("Panafrikanizmning «ota»lari kimlar?", "Uilyam Dyubua va Markus Garvi", "Gandi va Neru", "Burg‘iba va Abbos", "Sun Yatsen va Chan Kayshi", "Uilyam Dyubua va Markus Garvi.")
t.B("Afrikaning janubiy va markaziy qismidagi hududlar asosan qaysi davlatga qarashli edi?", "Buyuk Britaniya", "Fransiya", "Belgiya", "Italiya", "Buyuk Britaniyaga.")
t.B("Fransiya mustamlakalarining asosiy qismi qayerda joylashgan?", "G‘arbiy va Ekvatorial Afrikada", "Janubiy Afrikada", "Sharqiy Afrikada", "Madagaskarda", "G‘arbiy va Ekvatorial Afrikada.")
t.NAT("1940-yilda Fransiya mag‘lub bo‘ldi.", "Jazoir va Tunis Germaniya va Italiyaning xomashyo bazasiga aylantirildi", "Jazoir mustaqil bo‘ldi", "Tunis Britaniyaga o‘tdi", "Marokash Fransiyani ozod qildi",
      "Fransiya mag‘lubiyatidan so‘ng ular xomashyo bazasiga aylandi.")
t.NAT("Ikkinchi jahon urushida yuz minglab afrikaliklar janglarda qatnashdi.", "afrikaliklardan tuzilgan milliy harbiy qismlar keyinchalik mustaqillik kurashida muhim rol o‘ynadi", "Afrika urushdan chetda qoldi", "qul savdosi tiklandi", "mustamlakalar ko‘paydi",
      "Milliy harbiy qismlar mustaqillik uchun kurashda muhim rol o‘ynadi.")
t.TF("Panafrika harakati irqiy kamsitish, tan jazosi va majburiy mehnatni bekor qilishni talab qilgan.", True, "To‘g‘ri.")
t.TF("Jahon urushlari oralig‘ida Jazoir, Tunis va Marokashdagi harakatlar g‘alaba qozonib, mustaqillikka erishgan.", False, "Noto‘g‘ri: harakatlar g‘alaba qozonmagan, lekin ongning o‘sishida katta rol o‘ynagan.")
t.MUL([("Missionerlik faoliyati orqali Afrikada xristian dini tarqaldi.", True), ("Afrika jamiyatida mahalliy tabib va kohinlarning obro‘si yuqori bo‘lib qolgan.", True), ("Afrikada qishloq xo‘jaligi zamonaviy mashinalar bilan olib borilgan.", False)],
      "III noto‘g‘ri: qishloq xo‘jaligi ibtidoiy usulda olib borilgan.")
t.MATCH("Milliy harakat rahbarlarini mamlakatlari bilan moslashtiring.", ["Farhod Abbos", "Habib Burg‘iba", "Abdul Karim"], ["Jazoir", "Tunis", "Marokash", "Liviya"], 'abc',
        "Abbos – Jazoir; Burg‘iba – Tunis; Abdul Karim – Marokash.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Afrika Milliy kongressi tashkil topdi", "Misr mustaqilligi tan olindi", "«Qullik haqida» konvensiya", "Liviyadagi qarshilik bostirildi", "Fransiya mag‘lub bo‘ldi", "Misrga nemis-italyan qo‘shini kirdi"],
      "1920 → 1922 → 1926 → 1931 → 1940 → 1941.")
t.MAPMATCH(AF, ['Misr', 'Jazoir', 'Marokash'],
           ["1922-yilda mustaqilligi tan olingan monarxiya", "Farhod Abbos harakati bo‘lgan Fransiya mustamlakasi", "Abdul Karim harakati bo‘lgan mamlakat"],
           "1 – Misr; 2 – Jazoir; 3 – Marokash.")
t.VENN("Shimoliy Afrika", "Tropik Afrika",
       [("arab-islom sivilizatsiyasining bir qismi", 1), ("Misr, Jazoir, Tunis, Marokash, Liviya", 1),
        ("asosan Britaniya va Fransiya o‘rtasida bo‘lingan, qabila tuzumi saqlangan", 2), ("1920-yilda AMK tashkil topgan", 2),
        ("Yevropa mustamlakachiligiga uchragan", 3)],
       "Shimoliy – arab-islom; Tropik – qabila tuzumi, AMK. Ikkalasi mustamlaka bo‘lgan.")
