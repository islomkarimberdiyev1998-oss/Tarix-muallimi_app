from qlib import Topic
TOPICS = {}
W = 'globe'; EU = 'europe'; RU = 'rus'

# 21 Fransiya 1800–1870
t = Topic('e8j21', 821); TOPICS['e8j21'] = t
t.B("Senat Napoleonni qachon «Fransuzlar imperatori» deb e’lon qilgan?", "1804-yilda", "1799-yilda", "1805-yilda", "1812-yilda", "1804-yili Senat uni Napoleon I deb e’lon qildi.")
t.B("1805-yilda Napoleon Rossiya va Avstriya qo‘shinini qaysi jangda yenggan?", "Austerlis", "Borodino", "Leypsig", "Vaterloo", "1805-yili Austerlis jangida.")
t.B("Napoleon Buyuk Britaniyaga qarshi qanday choraga murojaat qilgan?", "«qit’a qamali»", "dengiz desanti", "savdo shartnomasi", "Muqaddas ittifoq", "U Buyuk Britaniyaga «qit’a qamali» e’lon qildi.")
t.B("Rossiya Napoleon bilan Tilzit shartnomasini qachon imzolagan?", "1807-yilda", "1805-yilda", "1812-yilda", "1814-yilda", "1807-yili Tilzit shartnomasi imzolandi.")
t.B("1812-yilgi urush Rossiya tarixiga qanday nom bilan kirgan?", "«Vatan urushi»", "«Shimoliy urush»", "«Qrim urushi»", "«Xalqlar jangi»", "U Rossiya tarixiga «Vatan urushi» nomi bilan kirdi.")
t.B("Borodino jangi qachon bo‘lgan?", "1812-yil 7-sentabrda", "1813-yilda", "1805-yilda", "1815-yilda", "1812-yil 7-sentabrda.")
t.B("Chekinayotgan fransuzlarni ta’qib qilgan rus armiyasiga kim boshchilik qilgan?", "M.I. Kutuzov", "Aleksandr I", "Suvorov", "Pojarskiy", "M.I. Kutuzov boshchiligidagi armiya.")
t.B("«Xalqlar jangi» qayerda bo‘lgan?", "Leypsig ostonasida", "Vaterlooda", "Borodinoda", "Austerlisda", "1813-yili Leypsig ostonasida.")
t.B("1814-yilda Napoleon qayerga surgun qilingan?", "Elba oroliga", "Muqaddas Yelena oroliga", "Korsikaga", "Sitsiliyaga", "Ittifoqchilar uni Elba oroliga surgun qildi.")
t.B("Napoleon qaytib kelib necha kun hokimiyatni boshqargan?", "100 kun", "30 kun", "1 yil", "10 kun", "Napoleon atigi 100 kun boshqardi.")
t.B("Vaterloo jangi qachon bo‘lgan?", "1815-yilda", "1813-yilda", "1814-yilda", "1821-yilda", "1815-yili Vaterloo qishlog‘ida.")
t.B("Napoleon qayerda vafot etgan?", "Muqaddas Yelena orolida", "Elba orolida", "Parijda", "Korsikada", "U Muqaddas Yelena orolida 1821-yili vafot etdi.")
t.B("Vena kongressi qaysi yillarda bo‘lgan?", "1814–1815", "1813–1814", "1815–1821", "1830–1831", "Vena kongressi 1814–1815-yillarda bo‘ldi.")
t.B("«Muqaddas ittifoq»ni qaysi davlatlar tuzgan?", "Rossiya, Avstriya, Prussiya", "Angliya, Fransiya, Ispaniya", "Rossiya, Angliya, Fransiya", "Avstriya, Italiya, Ispaniya", "1815-yili uch monarx ittifoq tuzdi.")
t.B("1830-yilda Fransiyada qanday monarxiya o‘rnatilgan?", "Iyul monarxiyasi", "Ikkinchi imperiya", "Birinchi imperiya", "Burbonlar restavratsiyasi", "Lui Filipp taxtga chiqdi – Iyul monarxiyasi.")
t.B("Fransiya ikkinchi marta qachon respublika deb e’lon qilingan?", "1848-yil 25-fevralda", "1830-yil iyulda", "1852-yil 2-dekabrda", "1792-yilda", "1848-yil 25-fevral.")
t.B("Napoleon III qachon o‘zini imperator deb e’lon qilgan?", "1852-yil 2-dekabrda", "1848-yil dekabrda", "1804-yilda", "1870-yilda", "1852-yil 2-dekabrda Ikkinchi imperiya o‘rnatildi.")
t.NAT("Napoleon Moskvani egalladi, lekin armiyada tartib yo‘qoldi.", "Napoleon Moskvani tashlab chiqishga majbur bo‘ldi", "Rossiya taslim bo‘ldi", "Napoleon Moskvada qishladi", "Kutuzov asir olindi",
      "Jangovar ruh yo‘qolib, Napoleon Moskvani tashlab chiqdi.")
t.NAT("1830-yilda Karl X parlamentni tarqatib, saylov huquqini cheklamoqchi bo‘ldi.", "Parijda inqilob boshlanib, Karl X chet elga qochdi", "parlament rozi bo‘ldi", "Napoleon qaytdi", "respublika o‘rnatildi",
      "Inqilob boshlandi, hokimiyat yirik burjuaziyaga o‘tdi.")
t.NAT("1846-yilgi sovuq qishda g‘alla va tut daraxtlari nobud bo‘ldi.", "narx oshdi, ishsizlik ko‘paydi va 1848-yilgi inqilobga sharoit yaratildi", "hosildorlik oshdi", "Iyul monarxiyasi mustahkamlandi", "Fransiya urush boshladi",
      "Iqtisodiy inqiroz fevral inqilobiga olib keldi.")
t.TF("Vena kongressi qora tanli qullar savdosini taqiqlovchi deklaratsiya qabul qilgan.", True, "To‘g‘ri.")
t.TF("Lui Napoleon Bonapart Napoleon I ning o‘g‘li edi.", False, "Noto‘g‘ri: u Napoleon Bonapartning jiyani edi.")
t.MUL([("Vena kongressi Fransiya hududini 1789-yilgi chegaragacha qisqartirdi.", True), ("1848-yilda 21 yoshga to‘lgan barcha erkaklarga saylov huquqi berildi.", True), ("Napoleon Elbadan qaytganda Lyudovik XVIII qo‘shini unga qarshi jang qilgan.", False)],
      "III noto‘g‘ri: 30 ming kishilik qo‘shin Napoleon tomoniga o‘tib ketdi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Austerlis jangi", "Tilzit shartnomasi", "Borodino jangi", "«Xalqlar jangi»", "Vaterloo jangi", "Ikkinchi imperiya o‘rnatildi"],
      "1805 → 1807 → 1812 → 1813 → 1815 → 1852.")
t.MAPMATCH(EU, ['Austerlis', 'Leypsig', 'Vaterloo', 'Elba oroli'],
           ["1805-yilgi g‘alaba joyi", "1813-yilgi «Xalqlar jangi» joyi", "1815-yilgi hal qiluvchi jang joyi", "Napoleon birinchi surgun qilingan orol"],
           "1 – Austerlis; 2 – Leypsig; 3 – Vaterloo; 4 – Elba.")
t.MAPN(RU, ['Borodino', 'Tilzit', 'Peterburg', 'Kiyev'], "1812-yil 7-sentabrda Napoleon va rus qo‘shini o‘rtasidagi hal qiluvchi jang bo‘lgan joy qaysi raqam bilan belgilangan?", "Borodino – 1.", ask_idx=0)
t.VENN("Birinchi imperiya", "Ikkinchi imperiya",
       [("1804-yilda o‘rnatilgan", 1), ("Napoleon I boshchiligida", 1),
        ("1852-yilda o‘rnatilgan", 2), ("Napoleon III boshchiligida", 2),
        ("urushdagi mag‘lubiyat bilan qulagan", 3)],
       "I imperiya – 1804, Napoleon I. II imperiya – 1852, Napoleon III. Ikkalasi urushda yengilib qulagan.")

# 22 Germaniya va Italiya
t = Topic('e8j22', 822); TOPICS['e8j22'] = t
t.B("Germaniya inqilobining asosiy sababi nima edi?", "feodal tartiblarning kapitalistik taraqqiyotga to‘siqligi", "Fransiya bosqini", "dehqonlar urushi", "diniy nizolar", "Asosiy sabab – feodal tartiblarning to‘siq bo‘lishi.")
t.B("Germaniya inqilobiga kim rahbarlik qilgan?", "burjuaziyaning mo‘tadil qismi", "ishchilar", "dehqonlar", "qirol", "Konstitutsiyaviy monarxiya tarafdori bo‘lgan mo‘tadil burjuaziya.")
t.B("Germaniyadagi iqtisodiy inqiroz qachon yuz bergan?", "1847-yilda", "1848-yilda", "1866-yilda", "1861-yilda", "1847-yili iqtisodiy inqiroz yuz berdi.")
t.B("Berlinda qo‘zg‘olon qaysi voqea ta’sirida boshlangan?", "Fransiyadagi 1848-yil fevral inqilobi", "Vena kongressi", "Vaterloo jangi", "Italiya birlashuvi", "Fransiyadagi fevral inqilobi ta’sirida.")
t.B("Prussiya qirolligida konstitutsiya qachon joriy etilgan?", "1848-yilda", "1866-yilda", "1871-yilda", "1919-yilda", "1848-yili konstitutsiya joriy etildi.")
t.B("Birlashgan Italiya qirolligi qachon tashkil etilgan?", "1861-yilda", "1860-yilda", "1866-yilda", "1870-yilda", "1861-yili tashkil etildi.")
t.B("Italiya bosh vaziri kim bo‘lgan?", "Kamillo Kavur", "Juzeppe Garibaldi", "Juzeppe Madzini", "Bismark", "Bosh vazir Kamillo Kavur.")
t.B("Garibaldi Sitsiliyaga qachon kelib tushgan?", "1860-yilda", "1861-yilda", "1848-yilda", "1866-yilda", "1860-yili Sitsiliyaga kelib tushdi.")
t.B("«Yosh Italiya» jamiyatiga kim rahnamolik qilgan?", "Juzeppe Madzini", "Kavur", "Garibaldi", "Viktor Emmanuil", "Juzeppe Madzini.")
t.B("Venetsiya Italiya qirolligiga qachon qo‘shilgan?", "1866-yilda", "1861-yilda", "1870-yilda", "1860-yilda", "1866-yili Venetsiya qo‘shib olindi.")
t.B("Rim shahri Italiyaga qachon qo‘shilgan?", "1870-yilda", "1866-yilda", "1861-yilda", "1848-yilda", "1870-yili Rim qo‘shildi.")
t.B("Italiya parlamenti qaysi palatalardan iborat bo‘lgan?", "Senat va Deputatlar palatasi", "Lordlar va jamoa palatasi", "Reyxstag va Bundesrat", "Konvent va Direktoriya", "Senat va Deputatlar palatasi.")
t.B("Germaniyani birlashtirishga rahbarlik qilgan kansler kim?", "Otto fon Bismark", "Kavur", "Fridrix II", "Vilgelm I", "Otto fon Bismark.")
t.B("Prussiya Avstriya ustidan qachon g‘alaba qozongan?", "1866-yilda", "1848-yilda", "1870-yilda", "1861-yilda", "1866-yili tarixiy g‘alaba qozonildi.")
t.B("Shimoliy Germaniya ittifoqi konstitutsiyasi qachongacha amal qilgan?", "1919-yilgacha", "1871-yilgacha", "1945-yilgacha", "1890-yilgacha", "1919-yil Veymar konstitutsiyasi qabul qilinguncha.")
t.NAT("Garibaldi qo‘shini Neapolga yurish qildi.", "Neapol qirolligi tugatildi", "Garibaldi asir olindi", "Avstriya Italiyani egalladi", "Rim papasi Italiyani birlashtirdi",
      "Neapol qo‘shini tor-mor etilib, qirollik tugatildi.")
t.NAT("Prussiya Avstriyani yengdi (1866).", "Shimoliy Germaniya Ittifoqi tuzildi, Bismark Bundeskansler bo‘ldi", "Avstriya Germaniyani birlashtirdi", "Prussiya tarqatildi", "Fransiya Germaniyani egalladi",
      "G‘alabadan so‘ng Shimoliy Germaniya Ittifoqi tuzildi.")
t.NAT("Italiyada ichki bozor sust rivojlangan edi.", "hukmron doiralar mustamlaka imperiyasini tuzishga intildi", "Italiya respublika bo‘ldi", "sanoat tez rivojlandi", "Italiya qayta parchalandi",
      "Sust ichki bozor bosqinchilikka chorladi.")
t.TF("Germaniyani birlashtirish yo‘lidagi asosiy tashqi to‘siq Fransiya edi.", True, "To‘g‘ri.")
t.TF("Kavur Avstriyaga qarshi Angliya bilan shartnoma tuzgan.", False, "Noto‘g‘ri: u Fransiya bilan shartnoma tuzgan.")
t.MUL([("Italiyani birlashtiruvchilar «Vatanning aql-zakovati, joni va shamshiri»ga qiyoslanadi.", True), ("Garibaldi Lotin Amerikasidagi urushlarda nom qozongan.", True), ("1848-yilgi Germaniya inqilobi siyosiy tarqoqlikni darhol tugatgan.", False)],
      "III noto‘g‘ri: inqilob bostirildi, birlashuv keyinroq Bismark davrida bo‘ldi.")
t.MATCH("Shaxslarni faoliyati bilan moslashtiring.", ["Kamillo Kavur", "Juzeppe Garibaldi", "Juzeppe Madzini", "Otto fon Bismark"],
        ["Italiya bosh vaziri", "Sitsiliya va Neapolni ozod qilgan xalq qahramoni", "«Yosh Italiya» rahnamosi", "Shimoliy Germaniya Ittifoqi kansleri", "Prussiya qiroli"], 'abcd',
        "Kavur – bosh vazir; Garibaldi – Sitsiliya; Madzini – Yosh Italiya; Bismark – kansler.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Berlinda qo‘zg‘olon", "Garibaldi Sitsiliyaga tushdi", "Italiya qirolligi tuzildi", "Venetsiya qo‘shildi", "Rim qo‘shildi"],
      "1848 → 1860 → 1861 → 1866 → 1870.")
t.MAPMATCH('italy', ['Palermo', 'Neapol', 'Venetsiya', 'Rim'],
           ["Garibaldi 1860-yilda egallagan Sitsiliya shahri", "tugatilgan qirollik poytaxti", "1866-yilda Avstriyadan qo‘shib olingan viloyat", "1870-yilda qo‘shib olingan shahar"],
           "1 – Palermo; 2 – Neapol; 3 – Venetsiya; 4 – Rim.")
t.VENN("Germaniya birlashuvi", "Italiya birlashuvi",
       [("Prussiya yetakchiligida", 1), ("Bismark rahbarlik qilgan", 1),
        ("Kavur, Garibaldi, Madzini xizmati", 2), ("1861-yilda qirollik tuzilgan", 2),
        ("Avstriya bilan kurash orqali amalga oshgan", 3)],
       "Germaniya: Prussiya, Bismark. Italiya: Kavur, Garibaldi. Ikkalasida Avstriyaga qarshi kurash.")

# 23 Rossiya 1800–1870
t = Topic('e8j23', 823); TOPICS['e8j23'] = t
t.B("Rossiyada hukmdorning cheklanmagan hokimiyati qanday atalgan?", "samoderjaviye", "absolutizm", "protektorat", "konsullik", "Samoderjaviye – hukmdorning cheklanmagan hokimiyati.")
t.B("Samoderjaviye va krepostnoylikka qarshi zodagon farzandlari harakati qanday atalgan?", "dekabristlar harakati", "chartistlar harakati", "narodniklar", "yakobinchilar", "Bu kurash «Dekabristlar harakati» nomini oldi.")
t.B("«Janubiy jamiyat»ning ko‘zga ko‘ringan arbobi kim?", "Pavel Pestel", "Nikita Muravyov", "Aleksandr II", "Pushkin", "Vatan urushi qatnashchisi Pavel Pestel.")
t.B("Pestel tuzgan konstitutsiya loyihasi qanday atalgan?", "«Rus haqiqati»", "«Xalq vechesi»", "«Sudebnik»", "«Manifest»", "Loyiha «Rus haqiqati» deb ataldi.")
t.B("«Shimoliy jamiyat» konstitutsiya loyihasini kim tayyorlagan?", "Nikita Muravyov", "Pavel Pestel", "Nikolay I", "Tolstoy", "Nikita Muravyov.")
t.B("Muravyov loyihasi Rossiyani qanday davlat deb e’lon qilishni ko‘zda tutgan?", "konstitutsiyaviy monarxiya", "respublika", "mutlaq monarxiya", "federativ respublika", "Konstitutsiyaviy monarxiya.")
t.B("Dekabristlar qo‘zg‘oloni qachon bo‘lgan?", "1825-yil 14-dekabrda", "1812-yilda", "1861-yil 19-fevralda", "1853-yilda", "1825-yil 14-dekabr kuni.")
t.B("Qo‘zg‘olon qaysi imperatorning taxtga o‘tqazilishi kuniga belgilangan?", "Nikolay I", "Aleksandr I", "Aleksandr II", "Pyotr I", "Aleksandr I o‘rniga Nikolay I ning taxtga chiqish kuniga.")
t.B("Qrim urushi qaysi yillarda bo‘lgan?", "1853–1856", "1812–1814", "1861–1864", "1877–1878", "1853–1856-yillarda; Rossiya mag‘lub bo‘ldi.")
t.B("Krepostnoy huquqni bekor qilish to‘g‘risidagi qonun qachon imzolangan?", "1861-yil 19-fevralda", "1825-yil 14-dekabrda", "1856-yilda", "1864-yilda", "1861-yil 19-fevralda Aleksandr II imzoladi.")
t.B("Qonunni imzolagan imperator kim?", "Aleksandr II", "Nikolay I", "Aleksandr I", "Aleksandr III", "Imperator Aleksandr II.")
t.B("Pomeshikka o‘tkazilgan ortiqcha dehqon yerlari qanday atalgan?", "«otrezok»", "«vikup»", "«chek yer»", "«nadel»", "Bunday yerlar «otrezok» deb atalgan.")
t.B("Dehqonning yerni haq to‘lab sotib olishi qanday atalgan?", "vikup", "otrezok", "obrok", "barshchina", "Vikup – yerni haq to‘lab sotib olish.")
t.B("Dehqonlar vikup qarzini necha yil davomida to‘lashi kerak edi?", "49 yil", "10 yil", "25 yil", "100 yil", "49 yil davomida foizi bilan.")
t.B("Butun Kavkaz qachon Rossiya tarkibiga kiritilgan?", "1864-yilga kelib", "1825-yilda", "1812-yilda", "1867-yilda", "1864-yilga kelib.")
t.B("Turkiston general-gubernatorligi qachon tashkil etilgan?", "1867-yilda", "1864-yilda", "1861-yilda", "1876-yilda", "1867-yilda tashkil etildi.")
t.B("Rossiya Alyaskani qachon AQShga sotgan?", "1867-yilda", "1861-yilda", "1853-yilda", "1876-yilda", "1867-yilda Alyaska AQShga sotildi.")
t.B("Zamonaviy rus adabiy tiliga kim asos solgan?", "A.S. Pushkin", "L.N. Tolstoy", "Dostoyevskiy", "Gogol", "A.S. Pushkin.")
t.B("«Urush va tinchlik» romanining muallifi kim?", "L.N. Tolstoy", "Dostoyevskiy", "Pushkin", "Turgenev", "L.N. Tolstoy.")
t.B("Rus mumtoz musiqasiga kim asos solgan?", "M.I. Glinka", "P.I. Chaykovskiy", "Repin", "Bryullov", "M.I. Glinka.")
t.NAT("Rossiya Qrim urushida mag‘lub bo‘ldi.", "krepostnoylikni bekor qilish zarurati ayon bo‘ldi", "Rossiya Qrimni bosib oldi", "dekabristlar g‘alaba qozondi", "krepostnoylik kuchaytirildi",
      "Mag‘lubiyat iqtisodiy qoloqlik oqibati ekanini ko‘rsatdi.")
t.NAT("Dekabristlar qo‘zg‘oloni bostirildi.", "mamlakatda reaksiya kuchaydi, erkin fikr ta’qib qilindi", "konstitutsiya qabul qilindi", "krepostnoylik bekor qilindi", "respublika o‘rnatildi",
      "Reaksiya kuchayib, ilg‘or yozuvchilar quvg‘inga olindi.")
t.TF("1861-yilgi qonunga ko‘ra dehqonlarni sotish va hadya qilish taqiqlangan.", True, "To‘g‘ri.")
t.TF("1861-yilgi islohot krepostnoylik asoratlarini darhol butunlay yo‘q qilgan.", False, "Noto‘g‘ri: krepostnoylik asorati uzoq davom etdi.")
t.MUL([("Pestel va Muravyov dorga osilgan.", True), ("Pomeshik o‘z yerining 1/3, cho‘l hududlarda 1/2 qismini saqlab qolgan.", True), ("Chaykovskiyning eng mashhur asari «Ruslan va Lyudmila» operasi.", False)],
      "III noto‘g‘ri: «Ruslan va Lyudmila» – Glinka operasi.")
t.MATCH("Asarlarni mualliflari bilan moslashtiring.", ["«Yevgeniy Onegin» (roman)", "«Jinoyat va jazo»", "«Ruslan va Lyudmila» (opera)", "«Shelkunchik»"],
        ["Pushkin", "Dostoyevskiy", "Glinka", "Chaykovskiy", "Repin"], 'abcd', "Onegin – Pushkin; Jinoyat va jazo – Dostoyevskiy; Ruslan – Glinka; Shelkunchik – Chaykovskiy.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Vatan urushi", "Dekabristlar qo‘zg‘oloni", "Qrim urushi boshlandi", "Krepostnoylik bekor qilindi", "Kavkaz qo‘shib olindi", "Alyaska sotildi"],
      "1812 → 1825 → 1853 → 1861 → 1864 → 1867.")
t.MAPMATCH('eurasia', ['Kavkaz', 'Turkiston o‘lkasi', 'Sibir'],
           ["1864-yilga kelib Rossiyaga qo‘shilgan hudud", "1867-yilda general-gubernatorlik tuzilgan o‘lka", "dekabristlar surgun qilingan hudud"],
           "1 – Kavkaz; 2 – Turkiston; 3 – Sibir.")
t.VENN("«Janubiy jamiyat»", "«Shimoliy jamiyat»",
       [("Pestel boshchiligida", 1), ("respublika o‘rnatish tarafdori", 1),
        ("Muravyov loyihasi", 2), ("konstitutsiyaviy monarxiya tarafdori", 2),
        ("dekabristlarning maxfiy jamiyati", 3)],
       "Janubiy – Pestel, respublika. Shimoliy – Muravyov, konstitutsiyaviy monarxiya.")

# 24 AQSH 1800–1870
t = Topic('e8j24', 824); TOPICS['e8j24'] = t
t.B("AQShda sanoat inqilobi qachon boshlangan?", "XIX asrning 30-yillarida", "XVIII asr oxirida", "1865-yilda", "XIX asr oxirida", "XIX asrning 30-yillarida sanoat inqilobi boshlandi.")
t.B("AQSH shimolida qishloq xo‘jaligining asosini nima tashkil etgan?", "fermer xo‘jaligi", "plantatsiya", "krepostnoylik", "jamoa xo‘jaligi", "Shimolda fermer xo‘jaligi asosiy edi.")
t.B("Janubiy shtatlarda qanday xo‘jalik hukmron edi?", "qulchilikka asoslangan plantatsiya", "fermer xo‘jaligi", "manufaktura", "jamoa xo‘jaligi", "Janubda plantatsiya xo‘jaligi hukmron edi.")
t.B("Qulchilikni bekor qilish tarafdorlari qanday atalgan?", "abolitsionistlar", "konfederatlar", "plantatorlar", "chartistlar", "Abolitsionistlar harakati vujudga keldi.")
t.B("Virjiniyada qullar qo‘zg‘olonini ko‘tarishga uringan oq tanli fermer kim?", "Jon Braun", "Avraam Linkoln", "Mark Tven", "Jorj Vashington", "Atoqli abolitsionist Jon Braun.")
t.B("Jon Braun guruhi necha kishidan iborat bo‘lgan?", "22 kishidan", "5 kishidan", "100 kishidan", "500 kishidan", "Guruh 22 kishidan iborat, 5 nafari qora tanli.")
t.B("Avraam Linkoln qaysi partiya vakili edi?", "Respublikachilar partiyasi", "Demokratlar partiyasi", "Federalistlar", "Konfederatlar", "Respublikachilar partiyasining eng obro‘li arbobi.")
t.B("Linkolnning saylov shiori qanday edi?", "«O‘zingizga yer olish uchun ovoz bering!»", "«Ozodlik, Tenglik, Birodarlik!»", "«Vatan xavf ostida!»", "«Fan va taraqqiyot»", "«O‘zingizga yer olish uchun ovoz bering!»")
t.B("Linkoln prezident etib qachon saylangan?", "1860-yilda", "1861-yilda", "1865-yilda", "1856-yilda", "1860-yilgi saylovlarda g‘alaba qozondi.")
t.B("Janub plantatorlari qaysi partiyaning tayanchi edi?", "Demokratlar partiyasi", "Respublikachilar partiyasi", "Federalistlar", "Vig partiyasi", "Ular Demokratlar partiyasining asosiy tayanchi edi.")
t.B("AQShda fuqarolar urushi qaysi yillarda bo‘lgan?", "1861–1865", "1775–1783", "1812–1815", "1846–1848", "Fuqarolar urushi 1861–1865-yillarda.")
t.B("AQShda qullik qachon bekor qilingan?", "1865-yil dekabrda", "1861-yil aprelda", "1866-yilda", "1863-yilda", "1865-yilning dekabrida qullik bekor qilindi.")
t.B("Qora tanlilar huquqini tenglashtiruvchi konstitutsiyaviy tuzatish qachon kiritilgan?", "1866-yilda", "1865-yilda", "1870-yilda", "1861-yilda", "1866-yili Kongress tuzatish kiritdi.")
t.B("G‘arbdagi bo‘sh yerlarni bepul berish to‘g‘risidagi qonun qanday atalgan?", "«Gomstedlar to‘g‘risida»gi Qonun", "«Sudebnik»", "«Xartiya»", "«Konstitutsiya»", "«Gomstedlar to‘g‘risida»gi Qonun qabul qilindi.")
t.B("«Mobi Dik» asarining muallifi kim?", "German Melvill", "Fenimor Kuper", "Mark Tven", "Uolt Uitmen", "German Melvill.")
t.B("«Pionerlar» asarining muallifi kim?", "Fenimor Kuper", "Melvill", "Longfello", "Dikkens", "Fenimor Kuper.")
t.NAT("Britaniya fabrikalari AQShdan ko‘proq paxta xarid qila boshladi.", "Janubda qullarni ekspluatatsiya qilish kuchaydi", "qullik bekor qilindi", "paxta ekish qisqardi", "Janub sanoatlashdi",
      "Paxtaga talab oshgani sari qullar ekspluatatsiyasi kuchaydi.")
t.NAT("Linkoln prezident etib saylandi (1860).", "janubiy shtatlar AQShdan chiqib, konfederatsiya tuzdi", "Janub qullikni bekor qildi", "Demokratlar g‘alaba qozondi", "AQSH Britaniyaga qo‘shildi",
      "Plantatorlar alohida davlat tuzib, urush muqarrar bo‘ldi.")
t.NAT("Fuqarolar urushi Shimol g‘alabasi bilan tugadi.", "mamlakat yaxlitligi saqlanib, qullik bekor qilindi", "AQSH ikkiga bo‘lindi", "qullik kengaydi", "Janub mustaqil bo‘ldi",
      "G‘alaba yaxlitlikni saqladi, qullik bekor qilindi.")
t.TF("Shimoliy shtatlarda qulchilik XIX asr boshlaridayoq bekor qilingan.", True, "To‘g‘ri.")
t.TF("Urush boshida kuchlar nisbati jihatidan Janub ustun bo‘lgan.", False, "Noto‘g‘ri: kuchlar nisbati jihatidan Shimol ustun edi.")
t.MUL([("Linkoln reaksion kuchlar yollagan qotil tomonidan o‘ldirilgan.", True), ("Robinzon Kruzo obrazi Amerika milliy adabiyoti yo‘nalishiga ta’sir qilgan.", True), ("Jon Braun umumiy qo‘zg‘olon ko‘tarishga muvaffaq bo‘lgan.", False)],
      "III noto‘g‘ri: Braun guruhi tor-mor etilib, o‘zi osib o‘ldirildi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["AQShda sanoat inqilobi boshlandi", "Linkoln prezident bo‘ldi", "Fuqarolar urushi boshlandi", "Qullik bekor qilindi", "Qora tanlilar huquqi tenglashtirildi"],
      "1830-yillar → 1860 → 1861 → 1865 → 1866.")
t.MAPN('usa_e', ['Janubiy shtatlar', 'Shimoliy shtatlar', 'Virjiniya', 'Filadelfiya'], "Qulchilikka asoslangan plantatsiya xo‘jaligi hukmron bo‘lgan, konfederatsiya tuzgan hudud qaysi raqam bilan belgilangan?", "Janubiy shtatlar – 1.", ask_idx=0)
t.VENN("Shimol", "Janub",
       [("fermer xo‘jaligi rivojlangan", 1), ("qullik XIX asr boshida bekor qilingan", 1),
        ("plantatsiya va qulchilik", 2), ("konfederatsiya tuzib, ajralib chiqqan", 2),
        ("1861–1865-yillardagi fuqarolar urushi ishtirokchisi", 3)],
       "Shimol – fermerlar; Janub – plantatsiya, konfederatsiya. Ikkalasi urush tomoni.")
