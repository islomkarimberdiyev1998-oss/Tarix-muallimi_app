from qlib import Topic
TOPICS = {}
W = 'globe'; EU = 'europe'; EA = 'eastasia'

# 5 AQSH 1918–1939
t = Topic('e10j5', 1005); TOPICS['e10j5'] = t
t.B("Urushdan keyin AQSH Yevropaga nisbatan qanday holatga kelgan?", "kreditorga aylangan", "qarzdorga aylangan", "mustamlakaga aylangan", "betaraf qolgan", "Urushdan oldin qarzdor bo‘lgan AQSH Yevropaning kreditoriga aylandi.")
t.B("AQSH qaysi yillarda jadal rivojlanib, dunyoning eng rivojlangan mamlakatiga aylangan?", "1924–1929", "1918–1920", "1929–1933", "1933–1939", "1924–1929-yillarda.")
t.B("1920-yillar oxirida har necha amerikalikning bittasida radiopriyomnik bo‘lgan?", "har ikki amerikalikning bittasida", "har o‘n amerikalikning bittasida", "har yuztadan bittasida", "har bir oilada uchtadan", "Har ikki amerikalikning bittasida.")
t.B("1929-yil yanvarda AQSH prezidenti etib kim saylangan?", "Gerbert Guver", "Franklin Ruzvelt", "Vudro Vilson", "Garri Trumen", "Respublikachi Gerbert Guver.")
t.B("Jahon iqtisodiy inqirozi qachon va qayerda boshlangan?", "1929-yil 24-oktabrda Nyu-York fond birjasida", "1930-yilda Parijda", "1933-yilda Berlinda", "1926-yilda Londonda", "1929-yil 24-oktabrda Nyu-York fond birjasida.")
t.B("1929–1932-yillarda AQShda sanoat ishlab chiqarishi qanchaga qisqargan?", "50 % ga", "10 % ga", "25 % ga", "90 % ga", "50 % ga qisqardi.")
t.B("Inqiroz yillarida AQShda qancha kishi ishsiz qolgan?", "13 mln.ga yaqin", "1 mln.", "50 mln.", "3 mln.", "13 mln.ga yaqin kishi ish joyidan mahrum bo‘ldi.")
t.B("AQSH prezidentligiga to‘rt marta saylangan yagona shaxs kim?", "Franklin Ruzvelt", "Gerbert Guver", "Jorj Vashington", "Avraam Linkoln", "Franklin Ruzvelt (1932, 1936, 1940, 1944).")
t.B("Ruzvelt siyosatining nomi nima?", "«Yangi kurs»", "«Daues rejasi»", "«Yopiq eshiklar»", "«Katta tayoq»", "«Yangi kurs».")
t.B("AQSH SSSR bilan diplomatik munosabatlarni qachon o‘rnatgan?", "1933-yilda", "1929-yilda", "1941-yilda", "1922-yilda", "1933-yili.")
t.B("Xalqaro muammolarni hal etishda ishtirok etishdan bosh tortish siyosati qanday ataladi?", "izolatsionizm", "neytralitet", "liberalizm", "individualizm", "Izolatsionizm.")
t.B("AQSH Ikkinchi jahon urushiga qachon qo‘shilgan?", "1941-yil 7-dekabrda Pyorl-Xarbor hujumidan so‘ng", "1939-yil 1-sentabrda", "1940-yilda", "1945-yilda", "1941-yil 7-dekabrdagi Pyorl-Xarbor hujumidan so‘ng.")
t.NAT("Guver hech qanday ijtimoiy choralar ko‘rishga rozi bo‘lmadi.", "1932-yil saylovlarida demokrat Ruzvelt nomzodi qo‘yilib, g‘alaba qozondi", "inqiroz o‘z-o‘zidan tugadi", "Guver qayta saylandi", "AQSH sotsialistik davlat bo‘ldi",
      "Guverga qarshi Franklin Ruzvelt saylovda g‘alaba qozondi.")
t.NAT("«Yangi kurs» siyosati amalga oshirildi.", "1930-yillar ikkinchi yarmida AQSH inqirozdan chiqib oldi", "inqiroz chuqurlashdi", "AQSH Yevropaga qarzdor bo‘ldi", "AQSH urushga kirdi",
      "«Yangi kurs» Amerika kapitalizmi xarakterini o‘zgartirib, inqirozdan chiqardi.")
t.TF("Keyinchalik Ruzvelt neytralitet qonuni va izolatsionizm xato bo‘lganini tan olgan.", True, "To‘g‘ri.")
t.TF("AQSH Ispaniya fuqarolar urushida respublikachilarga qurol yetkazib bergan.", False, "Noto‘g‘ri: AQSH neytralitetga qat’iy rioya qilgan.")
t.MUL([("1920-yillarda AQShda yo‘lovchi aviatsiyasi davri boshlangan.", True), ("Guver amerikacha individualizm va liberalizm tamoyillarini himoya qilgan.", True), ("AQSH Birinchi jahon urushida eng ko‘p qo‘shin yo‘qotgan.", False)],
      "III noto‘g‘ri: AQSH ancha kam qo‘shin yo‘qotgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Guver prezident bo‘ldi", "Nyu-York birjasida inqiroz boshlandi", "Ruzvelt birinchi marta saylandi", "SSSR bilan diplomatik munosabat", "Pyorl-Xarborga hujum"],
      "1929 yanvar → 1929 oktabr → 1932 → 1933 → 1941.")
t.MAPMATCH('globe2', ['Nyu-York', 'Moskva', 'Pyorl-Xarbor'],
           ["1929-yilda fond birjasida inqiroz boshlangan shahar", "1933-yilda AQSH diplomatik munosabat o‘rnatgan davlat poytaxti", "1941-yilda Yaponiya hujum qilgan AQSH floti bazasi"],
           "1 – Nyu-York; 2 – Moskva; 3 – Pyorl-Xarbor.")
t.VENN("Gerbert Guver", "Franklin Ruzvelt",
       [("respublikachilar partiyasidan", 1), ("ijtimoiy choralar ko‘rishga qarshi", 1),
        ("demokratik partiyadan", 2), ("«Yangi kurs» siyosati muallifi", 2),
        ("AQSH prezidenti bo‘lgan", 3)],
       "Guver – respublikachi, liberalizm. Ruzvelt – demokrat, Yangi kurs. Ikkalasi prezident.")

# 6 Germaniya 1918–1939
t = Topic('e10j6', 1006); TOPICS['e10j6'] = t
t.B("Germaniya inqilobi qayerdagi qo‘zg‘olondan boshlangan?", "Kil shahridagi harbiy dengizchilar qo‘zg‘olonidan", "Berlindagi ishchilar qo‘zg‘olonidan", "Myunxendagi pivo isyonidan", "Rurdagi ish tashlashdan", "Kil shahridagi dengizchilar qo‘zg‘olonidan.")
t.B("Noyabr inqilobidan keyin yangi hukumatni kim boshqargan?", "Fridrix Ebert", "Gindenburg", "Gitler", "Daues", "Fridrix Ebert boshchiligida.")
t.B("Veymar konstitutsiyasi qachon qabul qilingan?", "1919-yil 31-iyulda", "1918-yil noyabrda", "1923-yilda", "1933-yilda", "1919-yil 31-iyul kuni Veymarda.")
t.B("Fransuzlar Germaniyaning qaysi viloyatiga 1923-yilda bostirib kirgan?", "Rur", "Saar", "Bavariya", "Prussiya", "Rur viloyatiga.")
t.B("1924-yilda reparatsiya muammosi uchun qabul qilingan reja qanday atalgan?", "«Daues rejasi»", "«Marshall rejasi»", "«Yangi kurs»", "«Barbarossa rejasi»", "Amerikalik bankir Charlz Daues rejasi.")
t.B("Germaniya natsional-sotsialistik ishchi partiyasi qachon paydo bo‘lgan?", "1919-yilda", "1923-yilda", "1933-yilda", "1918-yilda", "1919-yili.")
t.B("«Pivo isyoni» qachon va qayerda bo‘lgan?", "1923-yil 8-noyabrda Myunxenda", "1919-yilda Berlinda", "1933-yilda Veymarda", "1918-yilda Kilda", "1923-yil 8-noyabrda Myunxenda.")
t.B("1932-yil aprelgi prezidentlik saylovlarida kim g‘olib chiqqan?", "Gindenburg", "Gitler", "Ebert", "Daues", "Gindenburg g‘olib chiqdi, Gitler sal ortda qoldi.")
t.B("Gitler reyxskansler etib qachon tayinlangan?", "1933-yil 30-yanvarda", "1934-yilda", "1932-yil aprelda", "1923-yil 8-noyabrda", "1933-yil 30-yanvarda.")
t.B("Gitler fyurer qachon bo‘lib olgan?", "1934-yilda Gindenburg vafotidan so‘ng", "1933-yilda", "1935-yilda", "1938-yilda", "1934-yili.")
t.B("Germaniyada umumiy harbiy majburiyat to‘g‘risidagi qonun qachon kuchga kirgan?", "1935-yilda", "1933-yilda", "1938-yilda", "1919-yilda", "1935-yili.")
t.B("1936–1939-yillarda Germaniyaning harbiy xarajatlari qanchaga oshirilgan?", "10 barobar", "2 barobar", "100 barobar", "5 foizga", "Harbiy xarajatlar 10 barobar oshirildi.")
t.B("Avstriya qachon anshlyus qilingan?", "1938-yilda", "1939-yilda", "1936-yilda", "1935-yilda", "1938-yili Avstriya anshlyus qilindi.")
t.B("«Anshlyus» so‘zi nimani anglatadi?", "qo‘shib olish, ittifoq", "bosqin", "inqilob", "isyon", "Anshlyus – qo‘shib olish, ittifoq.")
t.NAT("«Pivo isyoni» muvaffaqiyatsiz tugadi.", "shunga qaramay natsistik partiya umumgermaniya siyosiy kuchiga aylandi", "natsistlar partiyasi tugatildi", "Gitler hokimiyatga keldi", "Bavariya mustaqil bo‘ldi",
      "Aynan pivo isyoni natsistlarni umumgermaniya kuchiga aylantirdi.")
t.NAT("Gindenburg vafot etdi (1934).", "prezident lavozimi bekor qilinib, Veymar respublikasi amalda tugadi", "Ebert prezident bo‘ldi", "Veymar konstitutsiyasi kuchaydi", "natsistlar hokimiyatdan ketdi",
      "Gitler fyurer bo‘lib, Veymar respublikasi yakunlandi.")
t.TF("Charlz Dauesga Nobel mukofoti berilgan.", True, "To‘g‘ri.")
t.TF("Germaniyada italyan tipidagi fashizm shakllangan.", False, "Noto‘g‘ri: Germaniyada fashizm emas, natsizm shakllangan.")
t.MUL([("1923-yil oxirida Yevropadagi eng qadrsiz pul Germaniyada edi.", True), ("Germaniyadagi totalitar rejimga Italiya va Yaponiya ittifoqchi bo‘lgan.", True), ("Pivo isyonidan so‘ng Gitler darhol reyxskansler bo‘lgan.", False)],
      "III noto‘g‘ri: Gitler qamoqqa tashlangan; reyxskansler 1933-yilda bo‘lgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Noyabr inqilobi", "Veymar konstitutsiyasi", "Rur inqirozi va pivo isyoni", "«Daues rejasi»", "Gitler reyxskansler bo‘ldi", "Avstriya anshlyusi"],
      "1918 → 1919 → 1923 → 1924 → 1933 → 1938.")
t.MAPMATCH(EU, ['Kil', 'Veymar', 'Myunxen', 'Rur'],
           ["1918-yilda dengizchilar qo‘zg‘oloni boshlangan shahar", "1919-yilda konstitutsiya qabul qilingan shahar", "1923-yilda «pivo isyoni» bo‘lgan shahar", "1923-yilda fransuzlar bostirib kirgan viloyat"],
           "1 – Kil; 2 – Veymar; 3 – Myunxen; 4 – Rur.")
t.VENN("Veymar respublikasi", "Gitler totalitar rejimi",
       [("1919-yilgi demokratik konstitutsiya", 1), ("Ebert hukumati", 1),
        ("fyurer hokimiyati", 2), ("iqtisod urush maqsadlariga bo‘ysundirilgan", 2),
        ("1918–1939-yillardagi Germaniya davlati", 3)],
       "Veymar – demokratik konstitutsiya; Gitler – totalitarizm. Ikkalasi Germaniya davlati.")

# 7–8 SSSR 1918–1939
t = Topic('e10j7-8', 1007); TOPICS['e10j7-8'] = t
t.B("1917-yil noyabrda tuzilgan bolsheviklar hukumati qanday atalgan?", "Xalq komissarlari soveti", "Muvaqqat hukumat", "Davlat dumasi", "Zemstvo sobori", "Lenin boshchiligida Xalq komissarlari soveti tuzildi.")
t.B("Germaniya bilan Brest-Litovsk sulhi qachon tuzilgan?", "1918-yil martida", "1917-yil noyabrda", "1922-yilda", "1939-yilda", "1918-yil martida.")
t.B("Brest-Litovsk sulhiga ko‘ra Rossiya nimadan ayrilgan?", "5 mln. kishi yashaydigan hudud va Qora dengiz flotidan", "Sibirdan", "Moskvadan", "Uzoq Sharqdan", "5 mln. aholili hudud va Qora dengiz flotidan.")
t.B("Fuqarolar urushi qachon asosan yakunlangan?", "1922-yil kuzda", "1918-yilda", "1920-yilda", "1924-yilda", "1922-yil kuzda Uzoq Sharqda.")
t.B("Antanta davlatlarining Rossiyaga qarshi bosqinchilik harakatlari qanday nom olgan?", "chet el intervensiyasi", "harbiy kommunizm", "kollektivlashtirish", "NEP", "Chet el intervensiyasi.")
t.B("1918–1922-yillardagi iqtisodni boshqarishning harbiy usuli qanday atalgan?", "«harbiy kommunizm»", "NEP", "«Yangi kurs»", "industrlashtirish", "«Harbiy kommunizm» siyosati.")
t.B("Dehqonlardan oshiqcha oziq-ovqatni majburiy tortib olish qanday atalgan?", "oziq-ovqat razvyorstkasi", "kollektivlashtirish", "natsionalizatsiya", "kontributsiya", "Oziq-ovqat razvyorstkasi.")
t.B("Qizil armiya Vladivostokni qachon olgan?", "1922-yil noyabrda", "1920-yilda", "1918-yilda", "1924-yilda", "1922-yil noyabrda.")
t.B("SSSR qachon tashkil qilingan?", "1922-yil 30-dekabrda", "1917-yil noyabrda", "1924-yilda", "1918-yil martida", "1922-yil 30-dekabrda.")
t.B("SSSRning birinchi konstitutsiyasi qachon qabul qilingan?", "1924-yilda", "1922-yilda", "1936-yilda", "1918-yilda", "1924-yili.")
t.B("1921-yilgi ochlarga yordam tashkil qilgan norveg sayyohi kim?", "Fritof Nansen", "Charlz Daues", "Amundsen", "Ruzvelt", "Fritof Nansen.")
t.B("«Harbiy kommunizm» o‘rniga qanday siyosat joriy etilgan?", "yangi iqtisodiy siyosat (NEP)", "kollektivlashtirish", "Yangi kurs", "industrlashtirish", "NEP – yangi iqtisodiy siyosat.")
t.B("Lenin qachon vafot etgan?", "1924-yilda", "1922-yilda", "1927-yilda", "1929-yilda", "1924-yili.")
t.B("Birinchi besh yillik qaysi yillarga mo‘ljallangan?", "1928–1932", "1933–1937", "1921–1925", "1938–1942", "1928–1932-yillar.")
t.B("Birinchi besh yillikda nechta yirik sanoat korxonasi qurilgan?", "1500 ta", "150 ta", "15 000 ta", "500 ta", "1500 ta yirik korxona qurildi.")
t.B("Kollektivlashtirish oqibatida qancha dehqon surgun qilingan?", "15 mln. ga yaqin", "1 mln.", "50 mln.", "500 ming", "15 mln.ga yaqin dehqon surgun qilindi.")
t.B("1933-yilgi ocharchilikda qancha kishi halok bo‘lgan?", "7 mln. dan ortiq", "1 mln.", "15 mln.", "500 ming", "7 mln.dan ortiq kishi ochlikdan vafot etdi.")
t.B("SSSRda majburiy boshlang‘ich ta’lim qachon joriy qilingan?", "1930-yilda", "1924-yilda", "1922-yilda", "1936-yilda", "1930-yili.")
t.B("SSSR Millatlar Ligasiga qachon a’zo bo‘lgan?", "1934-yilda", "1922-yilda", "1933-yilda", "1939-yilda", "1934-yili.")
t.B("Molotov – Ribbentrop pakti qachon imzolangan?", "1939-yil 23-avgustda", "1939-yil 1-sentabrda", "1922-yilda", "1941-yilda", "1939-yil 23-avgustda Moskvada.")
t.NAT("NEP joriy etildi.", "xususiy tadbirkorlik rag‘batlanib, xalq xo‘jaligi tiklandi", "xususiy mulk bekor qilindi", "ocharchilik kuchaydi", "SSSR tarqaldi",
      "NEP iqtisodning o‘sishiga ko‘maklashdi.")
t.NAT("Kollektivlashtirish amalga oshirildi.", "SSSR tarixining oxirigacha o‘zini o‘zi oziq-ovqat bilan ta’minlay olmadi", "qishloq xo‘jaligi gullab-yashnadi", "dehqonlar boyidi", "eksport ko‘paydi",
      "Kollektivlashtirishning dahshatli oqibati shu bo‘ldi.")
t.NAT("1939-yilda yaponlar Mo‘g‘ulistonga bostirib kirdi.", "SSSR qo‘shin kiritib, Xalxin-Gol yonida yaponlar mag‘lub bo‘ldi", "Mo‘g‘uliston Yaponiyaga qo‘shildi", "SSSR betaraf qoldi", "Xitoy urush ochdi",
      "Xalxin-Gol jangida yaponlar mag‘lubiyatga uchradi.")
t.TF("Ikkinchi besh yillikda SSSR sanoat ko‘rsatkichlari bo‘yicha dunyoda AQShdan keyin ikkinchi o‘ringa chiqqan.", True, "To‘g‘ri.")
t.TF("SSSRni 1933-yilda tan olgan oxirgi yirik davlat Fransiya bo‘lgan.", False, "Noto‘g‘ri: oxirgi yirik davlat AQSH bo‘lgan.")
t.MUL([("Molotov–Ribbentrop pakti maxfiy protokolida Boltiq bo‘yi davlatlari SSSR manfaatlari zonasi deb belgilangan.", True), ("1922-yilda Rapallo shartnomasi imzolangan.", True), ("SSSR tarkibiga dastlab O‘rta Osiyo respublikalari kirgan.", False)],
      "III noto‘g‘ri: dastlab Rossiya, Ukraina, Belorusiya va Kavkazorti respublikalari kirgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Brest-Litovsk sulhi", "NEPga o‘tish", "SSSR tashkil topdi", "Birinchi besh yillik boshlandi", "SSSR Millatlar Ligasiga kirdi", "Molotov–Ribbentrop pakti"],
      "1918 → 1921 → 1922 → 1928 → 1934 → 1939.")
t.MAPMATCH('eurasia2', ['Brest-Litovsk', 'Moskva', 'Vladivostok', 'Xalxin-Gol'],
           ["1918-yilda Germaniya bilan sulh tuzilgan shahar", "1939-yilda Molotov–Ribbentrop pakti imzolangan shahar", "1922-yilda Qizil armiya olgan Tinch okeani shahri", "1939-yilda yaponlar mag‘lub bo‘lgan daryo"],
           "1 – Brest-Litovsk; 2 – Moskva; 3 – Vladivostok; 4 – Xalxin-Gol.")
t.VENN("«Harbiy kommunizm»", "NEP",
       [("xususiy mulkchilik bekor qilingan", 1), ("oziq-ovqat razvyorstkasi", 1),
        ("bozor iqtisodiyoti qisman tiklangan", 2), ("xususiy tadbirkorlik rag‘batlangan", 2),
        ("bolsheviklar iqtisodiy siyosati", 3)],
       "Harbiy kommunizm – razvyorstka; NEP – bozor. Ikkalasi bolsheviklar siyosati.")

LA = 'latam'
# 9 Italiya va Ispaniya
t = Topic('e10j9', 1009); TOPICS['e10j9'] = t
t.B("Italiyada fashistlar partiyasi qachon tuzilgan?", "1919-yil martida", "1921-yilda", "1922-yil oktabrda", "1933-yilda", "1919-yil martida Benito Mussolini boshchiligida.")
t.B("Fashistlar 1921-yilgi saylovlarda nechta o‘ringa ega bo‘lgan?", "36 ta", "300 ta", "12 ta", "100 ta", "36 ta o‘ringa ega bo‘ldi.")
t.B("Fashistlarning «Rimga yurishi» qachon bo‘lgan?", "1922-yil oktabrda", "1919-yilda", "1921-yilda", "1925-yilda", "1922-yil oktabrda.")
t.B("Mussolinini hukumat boshlig‘i etib kim tayinlagan?", "qirol Viktor Emmanuil III", "Rim papasi", "parlament", "Gitler", "Qirol Viktor Emmanuil III.")
t.B("Mussolini irqiy qonunlarni qachon chiqargan?", "1938-yilda", "1922-yilda", "1935-yilda", "1940-yilda", "1938-yili.")
t.B("1939-yilda Deputatlar palatasi o‘rniga nima tuzilgan?", "Katta fashistik kengash", "Senat", "Kortes", "Konvent", "Katta fashistik kengash.")
t.B("Albaniya Italiya protektoratiga qachon aylantirilgan?", "1927-yilda", "1935-yilda", "1922-yilda", "1939-yilda", "1927-yili.")
t.B("Italiya–Efiopiya urushi qaysi yillarda bo‘lgan?", "1935–1936", "1927–1928", "1937–1938", "1940–1941", "1935–1936-yillarda.")
t.B("Italiya Millatlar Ligasidan qachon chiqqan?", "1937-yil dekabrda", "1933-yilda", "1935-yilda", "1939-yilda", "1937-yil dekabrda.")
t.B("Italiya Ikkinchi jahon urushiga qachon kirgan?", "1940-yil 10-iyunda", "1939-yil 1-sentabrda", "1941-yilda", "1938-yilda", "1940-yil 10-iyunda Fransiyaga urush e’lon qildi.")
t.B("Ispaniyada 1923-yilda davlat to‘ntarishini kim uyushtirgan?", "general Migel Primo de Rivera", "Fransisko Franko", "Mussolini", "Viktor Emmanuil", "General Primo de Rivera.")
t.B("Primo de Rivera qachon iste’foga chiqqan?", "1930-yilda", "1923-yilda", "1936-yilda", "1939-yilda", "1930-yili.")
t.B("Ispan falangasi qachon tashkil qilingan?", "1933-yilda", "1923-yilda", "1936-yilda", "1930-yilda", "1933-yili.")
t.B("Ispaniya va Portugaliyada parlament qanday ataladi?", "kortes", "reyxstag", "duma", "seym", "Kortes.")
t.B("Ispaniyada fuqarolar urushi qachon boshlangan?", "1936-yil 18-iyulda", "1933-yilda", "1939-yil 1-aprelda", "1934-yilda", "1936-yil 18-iyulda.")
t.B("Ispaniya fuqarolar urushida qancha ispan halok bo‘lgan?", "deyarli 1 mln.", "100 ming", "10 mln.", "50 ming", "Deyarli 1 mln. ispan halok bo‘ldi.")
t.B("Franko diktaturasi qachon batamom o‘rnatilgan?", "1939-yil 1-aprelda", "1936-yil 18-iyulda", "1933-yilda", "1940-yilda", "1939-yil 1-aprelda.")
t.NAT("1936-yilda Xalq fronti kortes saylovlarida g‘olib chiqdi.", "siyosiy mahbuslar ozod qilinib, demokratik yutuqlar tiklandi", "falanga hokimiyatga keldi", "Ispaniya monarxiyaga aylandi", "fuqarolar urushi tugadi",
      "Xalq fronti barcha mahbuslarni ozod qildi.")
t.NAT("Kataloniyada ish tashlashlar boshlandi.", "hukumat 8 soatlik ish kuni, ijtimoiy sug‘urta qonunlarini qabul qildi", "ish tashlashlar bostirilib, hech narsa o‘zgarmadi", "Kataloniya mustaqil bo‘ldi", "Franko hokimiyatga keldi",
      "Ish tashlashlar hukumatni islohotlarga majbur qildi.")
t.TF("Ispaniya fuqarolar urushida Germaniya va Italiya falangachilarga yordam ko‘rsatgan.", True, "To‘g‘ri; SSSR esa respublikachilarga yordam bergan.")
t.TF("Franko 1939-yil sentabrda Ikkinchi jahon urushiga darhol qo‘shilgan.", False, "Noto‘g‘ri: u neytralitet haqidagi dekretni imzoladi.")
t.MUL([("Ispaniya Birinchi jahon urushida neytral bo‘lgan.", True), ("Italyan fashizmi millatchilik poydevoriga qurilgan.", True), ("Mussolini hokimiyatga kelishi bilan barcha partiyalarni taqiqlagan.", False)],
      "III noto‘g‘ri: dastlab partiyalar va kasaba uyushmalarini taqiqlamagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Fashistlar partiyasi tuzildi", "Rimga yurish", "Primo de Rivera to‘ntarishi", "Albaniya protektoratga aylandi", "Italiya–Efiopiya urushi", "Franko diktaturasi o‘rnatildi"],
      "1919 → 1922 → 1923 → 1927 → 1935 → 1939.")
t.MAPMATCH('mideast', ['Rim', 'Albaniya', 'Efiopiya', 'Kataloniya'],
           ["1922-yilda fashistlar yurish qilgan poytaxt", "1927-yilda Italiya protektoratiga aylangan davlat", "1935–1936-yillarda Italiya bosib olgan davlat", "Ispaniyada ish tashlashlar boshlangan viloyat"],
           "1 – Rim; 2 – Albaniya; 3 – Efiopiya; 4 – Kataloniya.")
t.VENN("Mussolini rejimi", "Franko rejimi",
       [("1922-yilda Rimga yurishdan so‘ng hokimiyatga kelgan", 1), ("Efiopiyani bosib olgan", 1),
        ("fuqarolar urushidan so‘ng 1939-yilda o‘rnatilgan", 2), ("Ikkinchi jahon urushida neytralitet e’lon qilgan", 2),
        ("fashistik diktatura", 3)],
       "Mussolini – Rimga yurish, Efiopiya. Franko – 1939, neytralitet. Ikkalasi fashistik diktatura.")

# 10 Lotin Amerikasi 1918–1939
t = Topic('e10j10', 1010); TOPICS['e10j10'] = t
t.B("Birinchi jahon urushi yillarida Kuba shakarining narxi necha marta oshgan?", "11 marta", "2 marta", "50 marta", "5 marta", "Kuba shakari narxi 11 marta oshdi.")
t.B("1920-yillarda Lotin Amerikasi mamlakatlari siyosiy jihatdan qanday edi?", "faqat nomigagina respublika", "mutlaq monarxiya", "konstitutsion monarxiya", "sotsialistik", "Ular faqat nomigagina respublika edi.")
t.B("Argentinadagi liberal-islohotchi hukumat rahbari kim?", "Ipolito Irigoyen", "Simon Bolivar", "Primo de Rivera", "Franko", "Ipolito Irigoyen.")
t.B("Irigoyen qanday qonun qabul qilinishiga erishgan?", "8 soatlik ish kuni to‘g‘risidagi qonun", "irqiy qonunlar", "neytralitet qonuni", "harbiy majburiyat qonuni", "8 soatlik ish kuni to‘g‘risida.")
t.B("Argentinada Irigoyenning ikkinchi hukumati qachon ag‘darilgan?", "1930-yilda", "1929-yilda", "1933-yilda", "1936-yilda", "1930-yilgi harbiy to‘ntarishda.")
t.B("Braziliyada hukmronlik qilgan oligarxiya qanday atalgan?", "«qahva oligarxiyasi»", "«shakar oligarxiyasi»", "«neft oligarxiyasi»", "«kauchuk oligarxiyasi»", "«Qahva oligarxiyasi».")
t.B("Braziliyada oligarxiya rejimi qachon ag‘darilgan?", "1930-yilgi burjua inqilobida", "1922-yilda", "1933-yilda", "1918-yilda", "1930-yilgi burjua inqilobi.")
t.B("Ruzvelt Lotin Amerikasiga nisbatan qanday siyosatni e’lon qilgan?", "«yaxshi qo‘shnichilik»", "«katta tayoq»", "«yopiq eshiklar»", "«yangi kurs»", "1933-yili «yaxshi qo‘shnichilik» siyosati.")
t.B("«Yaxshi qo‘shnichilik» siyosati qachon e’lon qilingan?", "1933-yilda", "1929-yilda", "1930-yilda", "1941-yilda", "1933-yili.")
t.B("Bir davlatning o‘zga hudud va bozorlarni egallashga qaratilgan siyosati qanday ataladi?", "ekspansiya", "diktatura", "plantatsiya", "neytralitet", "Ekspansiya.")
t.NAT("Inqiroz yillarida an’anaviy mahsulotlarga talab kamaydi.", "millionlab tonna qahva va g‘alla yo‘q qilinib, minglab korxonalar to‘xtadi", "narxlar oshdi", "eksport ko‘paydi", "ishsizlik kamaydi",
      "Ko‘plab ishlab chiqaruvchilar xonavayron bo‘ldi.")
t.NAT("Birinchi jahon urushi yillarida Yevropa davlatlarining e’tibori susaydi.", "AQSH kapitali Markaziy va Janubiy Amerikaga kirib keldi", "Yevropa Lotin Amerikasini bosib oldi", "Lotin Amerikasi sanoati yo‘qoldi", "Braziliya monarxiya bo‘ldi",
      "AQSH kapitali mintaqaga kirib keldi.")
t.NAT("1930-yillarda Argentina, Meksika, Braziliya kabi davlatlarda davlatning iqtisodiy roli oshdi.", "mahalliy ishlab chiqarish o‘sib, milliy kapital kuchaydi", "milliy kapital yo‘qoldi", "AQSH kapitali chiqib ketdi", "iqtisod inqirozga uchradi",
      "Bu mahalliy ishlab chiqarish va milliy kapitalni kuchaytirdi.")
t.TF("1930-yilda Kolumbiyada konservativ oligarxiya o‘rniga liberal-islohotchilar kelgan.", True, "To‘g‘ri.")
t.TF("«Yaxshi qo‘shnichilik» siyosati AQSH ning Lotin Amerikasiga intervensiyalarini kuchaytirgan.", False, "Noto‘g‘ri: AQSH intervensiya uyushtirmaslikni e’lon qildi.")
t.MUL([("1920-yillar oxiriga kelib ekstensiv rivojlanish imkoniyatlari tugagan.", True), ("Chili va Kubada diktatorlik rejimlari ag‘darilgan.", True), ("Irigoyen milliy suverenitetni AQSHga topshirgan.", False)],
      "III noto‘g‘ri: Irigoyen milliy suverenitetni qat’iy himoya qilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Birinchi jahon urushi (shakar narxi oshdi)", "Jahon iqtisodiy inqirozi boshlandi", "Argentina va Braziliyada to‘ntarishlar", "«Yaxshi qo‘shnichilik» e’lon qilindi"],
      "1914–1918 → 1929 → 1930 → 1933.")
t.MAPMATCH(LA, ['Kuba', 'Kolumbiya', 'Braziliya', 'Argentina'],
           ["shakar narxi 11 marta oshgan orol davlat", "1930-yilda liberal-islohotchilar hokimiyatga kelgan davlat", "«qahva oligarxiyasi» ag‘darilgan davlat", "Irigoyen hukumati faoliyat yuritgan davlat"],
           "1 – Kuba; 2 – Kolumbiya; 3 – Braziliya; 4 – Argentina.")
t.VENN("Argentina (1930)", "Braziliya (1930)",
       [("harbiy to‘ntarish bilan Irigoyen ag‘darilgan", 1), ("konservatorlar hokimiyatga qaytgan", 1),
        ("burjua inqilobi «qahva oligarxiyasi»ni ag‘dargan", 2), ("muxolif burjua-millatchilar g‘alaba qozongan", 2),
        ("jahon iqtisodiy inqirozi ta’sirida siyosiy o‘zgarish bo‘lgan", 3)],
       "Argentina – konservatorlar qaytgan; Braziliya – oligarxiya ag‘darilgan. Ikkalasi inqiroz ta’sirida.")
