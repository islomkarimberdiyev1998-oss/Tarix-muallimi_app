from qlib import Topic, PLACES, REG
TOPICS = {}
W = 'globe'; EU = 'europe'; EA = 'eastasia'

# 11 Totalitar va avtoritar diktaturalar
t = Topic('y10j11', 10011); TOPICS['y10j11'] = t
t.B("XX asrda qaysi ikki qarama-qarshi totalitar mafkura asosida totalitar davlatlar vujudga kelgan?", "fashizm va bolshevizm", "liberalizm va konservatizm", "sotsializm va anarxizm", "monarxizm va respublikachilik", "Fashizm va bolshevizm.")
t.B("Rossiyada sovet hokimiyati qachon o‘rnatilgan?", "1917-yil 7-noyabrda", "1917-yil fevralda", "1922-yil 30-dekabrda", "1918-yilda", "1917-yil 7-noyabrdagi davlat to‘ntarishi natijasida.")
t.B("V. Lenin boshchiligidagi bolsheviklar hukumati qanday atalgan?", "Xalq komissarlari soveti", "Davlat Dumasi", "Muvaqqat hukumat", "Ta’sis majlisi", "Xalq komissarlari soveti.")
t.B("Rossiyada fuqarolar urushi qachongacha davom etgan?", "1922-yilgacha", "1918-yilgacha", "1930-yilgacha", "1924-yilgacha", "1922-yilgacha; 1 milliongacha kishi halok bo‘ldi.")
t.B("Turkistonda sovetlarga qarshi qurolli kurash qachongacha davom etgan?", "1930-yillarning o‘rtalarigacha", "1922-yilgacha", "1918-yilgacha", "1941-yilgacha", "1930-yillarning o‘rtalarigacha.")
t.B("1918–1922-yillarda iqtisodni boshqarishning harbiy usuli qanday atalgan?", "«harbiy kommunizm»", "YIS", "kollektivlashtirish", "«yangi kurs»", "«Harbiy kommunizm» siyosati.")
t.B("SSSR qachon tashkil topgan?", "1922-yil 30-dekabrda", "1917-yil 7-noyabrda", "1924-yilda", "1921-yilda", "1922-yil 30-dekabr kuni.")
t.B("O‘rta Osiyoda milliy-hududiy chegaralanish qachon o‘tkazilgan?", "1924-yilda", "1922-yilda", "1928-yilda", "1917-yilda", "1924-yili.")
t.B("YISning mohiyati nima edi?", "bozor iqtisodiyotini qisman tiklash", "barcha resurslarni safarbar qilish", "qishloqni kollektivlashtirish", "xususiy mulkni taqiqlash", "Bozor iqtisodiyotini qisman tiklash, xo‘jalik hisobi asosida rivojlantirish.")
t.B("Birinchi besh yillik qaysi yillarga mo‘ljallangan?", "1928–1932-yillarga", "1933–1937-yillarga", "1921–1925-yillarga", "1918–1922-yillarga", "1928–1932-yillarga; 1500 ta yirik korxona qurildi.")
t.B("1933-yilgi ocharchilikda qancha kishi vafot etgan?", "7 mln dan ortiq", "1 mln", "13 mln", "500 ming", "Ukraina, Kuban, Volgabo‘yi, Qozog‘istonda 7 mln dan ortiq.")
t.B("SSSRda majburiy boshlang‘ich ta’lim qachon joriy qilingan?", "1930-yilda", "1924-yilda", "1917-yilda", "1937-yilda", "1930-yili.")
t.B("Italiyada fashistlar partiyasi kim boshchiligida tuzilgan?", "Benito Mussolini", "Viktor Emmanuel III", "Anton Dreksler", "Adolf Gitler", "1919-yili Benito Mussolini boshchiligida.")
t.B("Mussolinini hukumat boshlig‘i etib kim tayinlagan?", "qirol Viktor Emmanuel III", "Gindenburg", "Lenin", "papa", "1922-yil oktyabrda Rimga yurishdan so‘ng qirol Viktor Emmanuel III.")
t.B("Italiya Millatlar Ligasidan qachon chiqqan?", "1937-yilda", "1935-yilda", "1933-yilda", "1939-yilda", "1937-yili.")
t.B("Germaniyada Veymar konstitutsiyasi qachon qabul qilingan?", "1919-yil 31-iyulda", "1918-yil noyabrda", "1933-yil 30-yanvarda", "1923-yil noyabrda", "1919-yil 31-iyul kuni Veymar shahrida.")
t.B("Germaniya natsional-sotsialistik ishchi partiyasiga kim asos solgan?", "Anton Dreksler", "Adolf Gitler", "Paul fon Gindenburg", "Mussolini", "1919-yili Anton Dreksler; Gitler unga boshchilik qildi.")
t.B("«Pivo isyoni» qachon va qayerda ko‘tarilgan?", "1923-yil noyabrda Myunxenda", "1919-yilda Veymarda", "1933-yilda Berlinda", "1932-yilda Gamburgda", "1923-yil noyabrda Myunxen shahrida.")
t.B("Gitler qachon reyxskansler etib tayinlangan?", "1933-yil 30-yanvarda", "1932-yilda", "1934-yilda", "1935-yilda", "1933-yil 30-yanvarda.")
t.B("Germaniyada umumiy harbiy majburiyat to‘g‘risidagi qonun qachon kuchga kirgan?", "1935-yilda", "1933-yilda", "1936-yilda", "1939-yilda", "1935-yili.")
t.B("«Antikomintern pakti»ni dastlab qaysi davlatlar imzolagan?", "Yaponiya va Germaniya", "Germaniya va Italiya", "Italiya va Yaponiya", "SSSR va Germaniya", "1936-yili Yaponiya va Germaniya; 1937-yili Italiya qo‘shildi.")
t.B("Yaponiya og‘ir sanoatida qaysi konsernlar mavqeini mustahkamlagan?", "«Mitsubisi» va «Sumitomo»", "«Krupp» va «Simens»", "«Ford» va «Jeneral motors»", "«Fiat» va «Pirelli»", "«Mitsubisi» va «Sumitomo».")
t.NAT("1921-yili sovet davlati kuchli iqtisodiy va siyosiy inqirozni boshidan kechirdi.", "bolsheviklar «harbiy kommunizm»dan voz kechib, YISga o‘tdi", "SSSR tarqaldi", "kollektivlashtirish boshlandi", "monarxiya tiklandi", "Inqirozdan chiqish uchun YISga o‘tildi.")
t.NAT("1928–1933-yillarda kollektivlashtirish o‘tkazildi.", "o‘ziga to‘q dehqonlar mulkidan mahrum qilinib, «quloq» sifatida surgun va qatl qilindi", "dehqonlar boyib ketdi", "qishloq xo‘jaligi bozor asosida rivojlandi", "ocharchilik yo‘qoldi", "Ko‘pchiligi quloq sifatida qamaldi, surgun qilindi, qatl etildi.")
t.NAT("1934-yili prezident Gindenburg vafot etdi.", "Gitler Germaniyaning fyureri (dohiysi) bo‘lib oldi", "Veymar respublikasi tiklandi", "Gitler hokimiyatdan ketdi", "Germaniya monarxiyaga aylandi", "Gitler fyurerga aylandi.")
t.TF("Ikkinchi besh yillikda SSSR sanoat ishlab chiqarishi bo‘yicha AQSHdan keyin ikkinchi o‘ringa chiqqan.", True, "To‘g‘ri: 1933–1937-yillarda.")
t.TF("«Pivo isyoni» natsistlarning hokimiyatga kelishi bilan muvaffaqiyatli yakunlangan.", False, "Noto‘g‘ri: isyon muvaffaqiyatsiz tugagan, ammo partiyani yirik siyosiy kuchga aylantirgan.")
t.MUL([("1935–1936-yillarda Efiopiya Italiya mustamlakasiga aylantirilgan.", True),
       ("1936–1939-yillarda Germaniyada harbiy xarajatlar 10 barobar oshirilgan.", True),
       ("Dastlab SSSR tarkibiga O‘zbekiston, Ukraina va Belorussiya kirgan.", False)],
      "III noto‘g‘ri: dastlab Rossiya, Ukraina, Belorussiya va Kavkazorti respublikalari kirgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Sovet hokimiyati o‘rnatildi", "Veymar konstitutsiyasi qabul qilindi", "Rimga yurish", "SSSR tashkil topdi", "«Pivo isyoni»", "Gitler reyxskansler bo‘ldi"],
      "1917 → 1919 → 1922-yil oktyabr → 1922-yil dekabr → 1923 → 1933.")
t.VENN("Italiya fashizmi", "Germaniya natsizmi",
       [("Rimga yurish", 1), ("Viktor Emmanuel III Mussolinini tayinlagan", 1),
        ("«Pivo isyoni»", 2), ("Veymar konstitutsiyasi bekor qilingan", 2),
        ("«Berlin – Rim – Tokio uchburchagi» a’zosi", 3)],
       "Italiya – Rimga yurish; Germaniya – Pivo isyoni, Veymar; ikkalasi «uchburchak» a’zosi.")
t.MAPMATCH(W, ['Berlin', 'Rim', 'Tokio', 'Efiopiya'],
           ["«uchburchak»ning Germaniya poytaxti", "1922-yilda fashistlar yurish qilgan shahar", "«uchburchak»ning Osiyodagi poytaxti", "1935–1936-yillarda Italiya mustamlakasiga aylantirilgan davlat"],
           "1 – Berlin; 2 – Rim; 3 – Tokio; 4 – Efiopiya.")

# 12 Osiyo mamlakatlarida mustaqillik
t = Topic('y10j12', 10012); TOPICS['y10j12'] = t
t.B("Turkiyadagi qarshilik harakatiga kim rahbarlik qilgan?", "general Mustafo Kamol posho", "Anvar posho", "sulton Mehmed VI", "Midhat posho", "General Mustafo Kamol posho.")
t.B("M. Kamol qo‘shinlari butun Turkiya hududini qachon ozod qilgan?", "1922-yil oktyabrda", "1923-yil 29-oktyabrda", "1920-yilda", "1924-yilda", "1922-yil oktyabrda.")
t.B("Turkiya Buyuk Millat majlisi monarxiyani qachon bekor qilgan?", "1922-yil 1-noyabrda", "1923-yil 29-oktyabrda", "1924-yilda", "1919-yilda", "1922-yil 1-noyabr kuni.")
t.B("Taxtdan ag‘darilgan oxirgi usmoniy sulton kim?", "Mehmed VI Vahideddin", "Abdulhamid II", "Abdulaziz", "Mehmed V", "Sulton Mehmed VI taxtdan ag‘darildi.")
t.B("Qaysi shartnomaga ko‘ra Turkiya suvereniteti va hududiy yaxlitligini saqlab qolgan?", "1923-yilgi Lozanna shartnomasi", "Versal shartnomasi", "San-Stefano sulhi", "Sevr shartnomasi", "1923-yili Lozannada imzolangan shartnoma.")
t.B("Turkiya qachon respublika deb e’lon qilingan?", "1923-yil 29-oktyabrda", "1922-yil 1-noyabrda", "1924-yilda", "1932-yilda", "1923-yil 29-oktyabrda.")
t.B("M. Kamol islohotlarni qaysi sohadan boshlagan?", "dindan", "harbiydan", "iqtisoddan", "tashqi siyosatdan", "U islohotlarni dindan boshladi.")
t.B("Xalifalikni tugatish to‘g‘risida qaror qachon qabul qilingan?", "1924-yilda", "1922-yilda", "1923-yilda", "1932-yilda", "1924-yili.")
t.B("Turkiyada arab alifbosi o‘rniga qaysi alifbo joriy qilingan?", "lotin alifbosi", "kirill alifbosi", "fors alifbosi", "yunon alifbosi", "Lotin alifbosi joriy qilindi.")
t.B("Buyuk millat majlisi M. Kamolga qanday nasab bergan?", "«Otaturk»", "«Fyurer»", "«Mahatma»", "«Posho»", "«Otaturk» nasabi.")
t.B("Turkiya Millatlar Ligasiga qachon a’zo bo‘lgan?", "1932-yilda", "1923-yilda", "1919-yilda", "1941-yilda", "1932-yili.")
t.B("Turkiya tashqi savdosining yarmidan ko‘prog‘i qaysi davlat hissasiga to‘g‘ri kelgan?", "Germaniya", "Buyuk Britaniya", "Fransiya", "SSSR", "Germaniya; 1941-yili do‘stlik shartnomasi imzolandi.")
t.B("Xitoylik talabalar Pekinda qachon namoyish boshlagan?", "1919-yil 4-mayda", "1925-yil 30-mayda", "1920-yil iyulda", "1931-yilda", "1919-yil 4-may kuni.")
t.B("1920-yil iyulda Pekinda kim hokimiyatga kelgan?", "U Peyfu", "Sun Yatsen", "Mao Szedun", "Chan Kayshi", "Britaniya va AQSH qo‘llab-quvvatlagan U Peyfu.")
t.B("Sun Yatsen qachon Xitoy Respublikasi prezidenti etib saylangan?", "1921-yilda", "1912-yilda", "1925-yilda", "1928-yilda", "1921-yili.")
t.B("Shanxaydagi inglizlarga qarshi vatanparvarlik harakati qanday nom olgan?", "«30-may harakati»", "«4-may harakati»", "«Yosh Xitoy»", "«Sinxay»", "1925-yil bahordagi «30-may harakati».")
t.B("Xitoy Sovet respublikasi raisi etib kim saylangan?", "Mao Szedun", "Sun Yatsen", "U Peyfu", "Gandi", "1931-yili Mao Szedun.")
t.B("Hind Milliy kongressining g‘oyaviy rahbari, xalq harakati yetakchisi kim bo‘lgan?", "Mahatma Gandi", "Rabindranath Thakur", "Vivekananda", "Sun Yatsen", "Mahatma Gandi.")
t.B("Urush olib borayotgan tomonning boshqa davlat yerlarini vaqtincha egallab turishi nima deb ataladi?", "okkupatsiya", "anneksiya", "aqidaparastlik", "mandat", "Okkupatsiya.")
t.NAT("1919-yil Parij konferensiyasida G‘arb davlatlari Xitoy talablarini rad etdi.", "Pekinda talabalar namoyishi boshlanib, butun Xitoyni larzaga soldi", "Xitoy Yaponiyaga qo‘shildi", "Xitoy Ligaga a’zo bo‘ldi", "Sun Yatsen iste’foga chiqdi", "1919-yil 4-may namoyishi.")
t.NAT("1924-yili Turkiyada xalifalik tugatildi.", "darveshxonalar tarqatildi, shariat sudlari bekor qilindi, madrasalar yopildi", "sulton hokimiyati tiklandi", "Turkiya monarxiyaga aylandi", "arab alifbosi saqlab qolindi", "Diniy muassasalar tugatildi, maktablar Maorif vazirligiga o‘tdi.")
t.TF("1928-yil oxirida butun Xitoy rasman Pekindagi Gomindan hukumati boshchiligida birlashgan.", True, "To‘g‘ri.")
t.TF("Ikkinchi jahon urushida Turkiya rasman Germaniya tomonida urushga kirgan.", False, "Noto‘g‘ri: Turkiya rasman betaraf qolgan.")
t.MUL([("1921–1922-yillarda Vashington konferensiyasida Xitoyning suvereniteti kafolatlangan.", True),
       ("Gandi ishlab chiqqan zo‘ravonliksiz qarshilik taktikasi millionlab kishilarni o‘limdan saqlab qolgan.", True),
       ("Gomindan bilan kommunistlar o‘rtasidagi kurash besh yil davom etgan.", False)],
      "III noto‘g‘ri: kurash yigirma yil davom etgan fuqarolar urushiga aylandi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Pekinda talabalar namoyishi", "Sun Yatsen prezident etib saylandi", "Turkiyada monarxiya bekor qilindi", "Turkiya respublika deb e’lon qilindi", "Xalifalik tugatildi", "Xitoy Sovet respublikasi e’lon qilindi"],
      "1919 → 1921 → 1922 → 1923 → 1924 → 1931.")
t.VENN("Mustafo Kamol", "Sun Yatsen",
       [("«Otaturk» nasabini olgan", 1), ("xalifalikni tugatgan", 1),
        ("1925-yilda vafot etgan", 2), ("Gomindan asoschisi", 2),
        ("respublika prezidenti bo‘lgan", 3)],
       "Kamol – Otaturk, xalifalik; Sun Yatsen – 1925, Gomindan; ikkalasi prezident.")
t.MAPMATCH(EA, ['Pekin', 'Shanxay', 'Yaponiya'],
           ["1919-yil 4-mayda talabalar namoyishi boshlangan shahar", "1925-yilda «30-may harakati» boshlangan shahar", "qo‘shinlari Xitoy hududini bosib olayotgan davlat"],
           "1 – Pekin; 2 – Shanxay; 3 – Yaponiya.")

# 13 Afrikada milliy uyg‘onish
t = Topic('y10j13', 10013); TOPICS['y10j13'] = t
t.B("Afrika qit’asini keng ma’noda qaysi ikki mintaqaga bo‘lish mumkin?", "Shimoliy va Tropik Afrika", "G‘arbiy va Sharqiy Afrika", "Ekvatorial va Janubiy Afrika", "Sahroyi Kabir va Sahel", "Shimoliy va Tropik Afrika.")
t.B("Afrikaning shimoliy qismi qaysi sivilizatsiyaning bo‘lagiga aylangan?", "arab-islom sivilizatsiyasining", "Yevropa sivilizatsiyasining", "hind sivilizatsiyasining", "Lotin Amerikasi sivilizatsiyasining", "Arab-islom sivilizatsiyasining bir bo‘lagi.")
t.B("Buyuk Britaniya Misrning to‘liq mustaqilligini qachon tan olgan?", "1922-yil fevralda", "1923-yilda", "1931-yilda", "1941-yilda", "1922-yil fevralda protektoratni bekor qildi.")
t.B("1923-yilgi konstitutsiyaga ko‘ra Misr qanday davlat deb e’lon qilingan?", "monarxiya", "respublika", "protektorat", "dominion", "Misr monarxiya deb e’lon qilindi.")
t.B("1941-yili Misr hududiga qaysi davlatlar qo‘shini kiritilgan?", "Germaniya va Italiya", "Britaniya va Fransiya", "AQSH va SSSR", "Ispaniya va Portugaliya", "Germaniya va Italiya qo‘shinlari.")
t.B("Jazoir, Tunis va Marokash qaysi davlatning mustamlakalari bo‘lgan?", "Fransiya", "Buyuk Britaniya", "Italiya", "Ispaniya", "Fransiya mustamlakalari.")
t.B("Jazoirda milliy-ozodlik harakatiga kim boshchilik qilgan?", "Farhod Abbos", "Habib Burg‘iba", "Abdul Karim", "Samori", "Jazoirda Farhod Abbos.")
t.B("Tunisdagi milliy-ozodlik harakati rahbari kim?", "Habib Burg‘iba", "Farhod Abbos", "Abdul Karim", "Behanzin", "Tunisda Habib Burg‘iba.")
t.B("Marokashda milliy-ozodlik harakatiga kim boshchilik qilgan?", "Abdul Karim", "Habib Burg‘iba", "Farhod Abbos", "Raboh", "Marokashda Abdul Karim.")
t.B("Liviya qarshilik harakati qachon bostirilgan?", "1931-yilda", "1922-yilda", "1941-yilda", "1919-yilda", "1931-yili bostirilib, Liviya Italiya mustamlakasiga aylandi.")
t.B("Millatlar Ligasi Qullik haqida konvensiyani qachon qabul qilgan?", "1926-yilda", "1919-yilda", "1890-yilda", "1931-yilda", "1926-yili.")
t.B("Afrikaning eng katta hududini qaysi davlat egallagan?", "Fransiya", "Buyuk Britaniya", "Belgiya", "Portugaliya", "Eng katta hududni Fransiya egallagan.")
t.B("Birinchi Panafrika konferensiyasi qachon va qayerda bo‘lgan?", "1900-yilda Londonda", "1919-yilda Parijda", "1920-yilda Keyptaunda", "1926-yilda Jenevada", "1900-yili Londonda.")
t.B("Panafrikanizm harakati qachon rasmiylashtirilgan?", "1919-yili I Ta’sis kongressida", "1900-yilda", "1920-yilda", "1926-yilda", "1919-yili I Ta’sis kongressida.")
t.B("Afrikadagi birinchi siyosiy partiya qaysi?", "Afrika milliy kongressi (AMK)", "Hindiston milliy kongressi", "Gomindan", "Vafd", "1920-yili tuzilgan Afrika milliy kongressi.")
t.B("Janubiy Afrika Ittifoqi qachon tuzilgan?", "1910-yilda", "1920-yilda", "1902-yilda", "1931-yilda", "1910-yili Britaniya dominioni sifatida.")
t.B("Dunyodagi eng irqchi konstitutsiya sifatida tarixda qolgan hujjat qaysi?", "Janubiy Afrika to‘g‘risidagi akt", "Midhat konstitutsiyasi", "Veymar konstitutsiyasi", "Qullik haqida konvensiya", "Janubiy Afrika to‘g‘risidagi akt 50 yil amal qildi.")
t.NAT("1940-yili Fransiya mag‘lubiyatga uchradi.", "Jazoir va Tunis Germaniya va Italiyaning xomashyo bazasiga aylantirildi", "Jazoir mustaqil bo‘ldi", "Tunis Britaniyaga o‘tdi", "Marokash Ispaniyaga qo‘shildi", "Jazoir va Tunis xomashyo bazasiga aylandi.")
t.NAT("Birinchi jahon urushidan keyin Italiya Liviyaga ko‘p ming kishilik qo‘shin kiritdi.", "qarshilik harakati 1931-yilda bostirilib, Liviya Italiya mustamlakasiga aylandi", "Liviya mustaqil bo‘ldi", "Italiya Liviyadan chiqib ketdi", "Liviya Misrga qo‘shildi", "Rahbarlar qatl qilindi, Liviya mustamlaka bo‘ldi.")
t.TF("Ikkinchi jahon urushida yuz minglab afrikaliklar urush harakatlarida qatnashgan.", True, "To‘g‘ri.")
t.TF("Shimoliy Afrikadagi milliy-ozodlik harakatlari jahon urushlari oralig‘ida g‘alaba qozongan.", False, "Noto‘g‘ri: g‘alaba qozonmagan, ammo milliy ongning o‘sishida katta rol o‘ynagan.")
t.MUL([("Britaniya mustamlakalarida Afrika aholisining yarmidan ko‘pi yashagan.", True),
       ("Missionerlik faoliyati orqali Afrikada xristian dini tarqalgan.", True),
       ("Tropik Afrikada qabila boshliqlari va kohinlarning roli butunlay yo‘qolgan.", False)],
      "III noto‘g‘ri: yangi siyosiy institutlarda ham qabila boshliqlari va kohinlar asosiy rol o‘ynagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Birinchi Panafrika konferensiyasi", "Janubiy Afrika Ittifoqi tuzildi", "Afrika milliy kongressi tuzildi", "Misr mustaqilligi tan olindi", "Qullik haqida konvensiya", "Liviya qarshiligi bostirildi"],
      "1900 → 1910 → 1920 → 1922 → 1926 → 1931.")
t.VENN("Shimoliy Afrika", "Tropik Afrika",
       [("arab-islom sivilizatsiyasi bo‘lagi", 1), ("Farhod Abbos va Burg‘iba harakatlari", 1),
        ("kohin va tabiblarning obro‘si yuqori", 2), ("missionerlar xristianlikni tarqatgan", 2),
        ("Yevropa metropoliyalari hukmronligi", 3)],
       "Shimol – arab-islom, Abbos, Burg‘iba; Tropik – kohinlar, missionerlar; ikkalasida metropoliyalar hukmron.")
t.MAPMATCH('africa', ['Misr (Afrika)', 'Liviya (Afrika)', 'Jazoir', 'Marokash'],
           ["1922-yilda Britaniya to‘liq mustaqilligini tan olgan davlat", "1931-yilda Italiya mustamlakasiga aylantirilgan hudud", "Farhod Abbos boshchiligida harakat bo‘lgan mamlakat", "Abdul Karim boshchiligida harakat bo‘lgan mamlakat"],
           "1 – Misr; 2 – Liviya; 3 – Jazoir; 4 – Marokash.")

# 14 Ikkinchi jahon urushi
t = Topic('y10j14', 10014); TOPICS['y10j14'] = t
t.B("Germaniyada Gitler boshchiligidagi partiya qachon hokimiyatga kelgan?", "1933-yil yanvarda", "1932-yilda", "1938-yilda", "1923-yilda", "1933-yil yanvarda.")
t.B("Chexoslovakiyaning qaysi viloyati Germaniyaga berilishi talab qilingan?", "Sudet viloyati", "Elzas", "Saar", "Kareliya", "Aholisining ko‘pchiligi nemis bo‘lgan Sudet viloyati.")
t.B("Myunxen kelishuvi qachon rasmiylashtirilgan?", "1938-yil 29-sentabrda", "1939-yil 23-avgustda", "1939-yil 1-sentabrda", "1940-yil sentabrda", "1938-yil 29-sentabr kuni.")
t.B("Molotov-Ribbentrop pakti qachon imzolangan?", "1939-yil 23-avgustda", "1938-yil 29-sentabrda", "1941-yil 22-iyunda", "1940-yil martda", "1939-yil 23-avgustda 10 yil muddatga.")
t.B("Ikkinchi jahon urushi qachon boshlangan?", "1939-yil 1-sentabrda", "1939-yil 3-sentabrda", "1941-yil 22-iyunda", "1938-yil 29-sentabrda", "Germaniyaning Polshaga bostirib kirishi bilan.")
t.B("Polshaga sovet qo‘shinlari qachon kiritilgan?", "1939-yil 17-sentabrda", "1939-yil 1-sentabrda", "1940-yil martda", "1941-yil 22-iyunda", "1939-yil 17-sentabr kuni.")
t.B("Sovet-fin urushi natijasida SSSR qaysi hududni qo‘shib olgan?", "Kareliya", "Sudet", "Elzas", "Saar", "Kareliya SSSR tarkibiga qo‘shildi.")
t.B("Uchlar pakti qachon imzolangan?", "1940-yil sentabrda", "1936-yilda", "1939-yil avgustda", "1941-yil avgustda", "1940-yil sentabrda Germaniya, Yaponiya, Italiya o‘rtasida.")
t.B("SSSRni shiddat bilan tor-mor qilishni ko‘zda tutgan reja qanday atalgan?", "«Barbarossa»", "«Overlord»", "«Tayfun»", "«Atlantik»", "«Barbarossa» rejasi.")
t.B("Germaniya SSSRga qachon hujum boshlagan?", "1941-yil 22-iyunda", "1939-yil 1-sentabrda", "1941-yil dekabrda", "1942-yil noyabrda", "1941-yil 22-iyunda.")
t.B("Atlantik xartiyani qaysi davlatlar imzolagan?", "AQSH va Buyuk Britaniya", "SSSR va AQSH", "Germaniya va Italiya", "Fransiya va Britaniya", "1941-yil avgustda AQSH va Buyuk Britaniya.")
t.B("Nemis qo‘shinlari urushdagi dastlabki jiddiy mag‘lubiyatga qayerda uchragan?", "Moskva ostonalarida", "Stalingradda", "Berlinda", "Kurskda", "1941-yil dekabrda Moskva ostonalarida.")
t.B("Stalingrad ostonalarida qurshovdagi nemis qo‘shinlari qachon taslim bo‘lgan?", "1943-yil fevralda", "1942-yil noyabrda", "1944-yilda", "1941-yil dekabrda", "1943-yil fevralda.")
t.B("«Ozod Fransiya» qarshilik harakatiga kim boshchilik qilgan?", "general Sharl de Goll", "I. B. Tito", "G. K. Jukov", "U. Cherchill", "General Sharl de Goll.")
t.B("Germaniyaning so‘zsiz taslim bo‘lganligi to‘g‘risidagi aktni SSSR nomidan kim imzolagan?", "G. K. Jukov", "I. B. Tito", "F. D. Ruzvelt", "Sharl de Goll", "1945-yil 8-may kuni G. K. Jukov.")
t.B("AQSH Xirosimaga atom bombasini qachon tashlagan?", "1945-yil 6-avgustda", "1945-yil 9-avgustda", "1945-yil 2-sentabrda", "1945-yil 8-mayda", "6-avgust – Xirosima, 9-avgust – Nagasaki.")
t.B("Ikkinchi jahon urushida qancha kishi halok bo‘lgan?", "65–70 mln", "110 mln", "13 mln", "7 mln", "110 mln safarbar qilindi, 65–70 mln halok bo‘ldi.")
t.B("BMT Ustavi qaysi shaharda tasdiqlangan?", "San-Fransiskoda", "Nyu-Yorkda", "Jenevada", "Londonda", "1945-yil San-Fransiskoda tasdiqlandi.")
t.B("O‘zbekiston Respublikasi BMTga qachon a’zo bo‘lgan?", "1992-yilda", "1991-yilda", "1995-yilda", "1945-yilda", "1992-yili.")
t.B("Nyurnberg sud jarayoni qachon bo‘lib o‘tgan?", "1945-yil noyabr – 1946-yil oktyabr", "1946-yil may – 1948-yil noyabr", "1945-yil iyul – avgust", "1943-yil", "1945-yil noyabrdan 1946-yil oktyabrgacha.")
t.NAT("Sovet-fin urushida SSSR tajovuzkor sifatida harakat qildi.", "SSSR Millatlar Ligasi tarkibidan chiqarildi", "SSSR Ligaga qabul qilindi", "Finlandiya SSSRga qo‘shildi", "Germaniya SSSRga urush ochdi", "Tajovuzkor davlat sifatida Ligadan chiqarildi.")
t.NAT("Germaniya 1939-yil 1-sentabrda Polshaga bostirib kirdi.", "3-sentabrda Buyuk Britaniya va Fransiya Germaniyaga urush e’lon qildi", "Britaniya betaraf qoldi", "Polsha Germaniyani yengdi", "SSSR Germaniyaga urush e’lon qildi", "Polshaga yordam va’da qilgan davlatlar urush e’lon qildi.")
t.TF("BMT Ustavi 1945-yil 24-oktyabrda kuchga kirgan.", True, "To‘g‘ri: bu sana BMT kuni sifatida nishonlanadi.")
t.TF("BMTni tuzish g‘oyasi dastlab Germaniya, Italiya va Yaponiya deklaratsiyasida aks etgan.", False, "Noto‘g‘ri: 1942-yilda AQSH, Britaniya, SSSR va Xitoy imzolagan deklaratsiyada.")
t.MUL([("Uchlar paktiga Vengriya, Ruminiya, Slovakiya va Bolgariya ham qo‘shilgan.", True),
       ("Tinch okeanda Yaponiya boshlagan harakatlar AQSHning urushga qo‘shilishini tezlashtirgan.", True),
       ("Antigitler koalitsiyasi liderlari urush davomida faqat bir marta – Potsdamda uchrashgan.", False)],
      "III noto‘g‘ri: uch marta – Tehron (1943), Yalta (1945-yil fevral), Potsdam (1945-yil iyul–avgust).")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Myunxen kelishuvi", "Molotov-Ribbentrop pakti", "Uchlar pakti", "Germaniya SSSRga hujum qildi", "Stalingradda nemislar taslim bo‘ldi", "Yaponiya taslim bo‘ldi"],
      "1938 → 1939 → 1940 → 1941 → 1943 → 1945.")
t.VENN("Nyurnberg jarayoni", "Tokio jarayoni",
       [("gestapo jinoyatchi tashkilot deb topilgan", 1), ("1945–1946-yillarda o‘tgan", 1),
        ("1946–1948-yillarda o‘tgan", 2), ("yapon harbiy jinoyatchilari hukm qilingan", 2),
        ("urush jinoyatchilari ustidan xalqaro sud", 3)],
       "Nyurnberg – gestapo, 1945–1946; Tokio – 1946–1948, yaponlar; ikkalasi urush jinoyatchilari sudi.")
t.MAPMATCH('eurasia', ['Myunxen', 'Stalingrad', 'Tehron (1943)', 'Yalta'],
           ["1938-yilda Chexoslovakiya kapitulyatsiyasi rasmiylashtirilgan shahar", "1942–1943-yillarda nemislar qurshovga olingan shahar", "1943-yilda uch lider uchrashgan shahar", "1945-yil fevralda Qrimda uch lider uchrashgan shahar"],
           "1 – Myunxen; 2 – Stalingrad; 3 – Tehron; 4 – Yalta.")
