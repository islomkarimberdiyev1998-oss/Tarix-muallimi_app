from qlib import Topic, PLACES, REG
TOPICS = {}
EU = 'europe'

# 21 Yevropa madaniyati
t = Topic('y7j21', 7021); TOPICS['y7j21'] = t
t.B("Buyuk Karl davridagi madaniy yuksalish qanday atalgan?", "«Karolinglar uyg‘onishi»", "«Otton uyg‘onishi»", "«Oltin asr»", "«Yetti erkin san’at»", "«Karolinglar uyg‘onishi».")
t.B("Karl «xalq maktablari»ni kimga topshirgan?", "anglosaks olimi, rohib Alkuinga", "Eyngardga", "Boetsiyga", "Prokopiyga", "Rohib Alkuinga.")
t.B("Zamondoshlari «mehnatsevar chumoli» deb atagan tarixchi kim?", "Eyngard", "Alkuin", "Lev Diakon", "Kesariyalik Prokopiy", "Tarixchi Eyngard.")
t.B("Karl qurdirgan binolardan qaysi biri saqlanib qolgan?", "Axendagi saroy kopellasi", "Rimdagi Avliyo Pyotr ibodatxonasi", "Parijdagi sobor", "Ravennadagi San-Vitale", "Faqat Axendagi saroy kopellasi.")
t.B("Konstantinopolda IX asrda qaysi oliy maktab ochilgan?", "Magnavr oliy maktabi", "Bayt ul-hikma", "Boloniya universiteti", "Al-Azhar", "Magnavr oliy maktabi.")
t.B("Vizantiyada VII asrda ixtiro qilingan, dengiz janglarida ustunlik bergan qurol qaysi?", "«yunon olovi»", "arbalet", "porox", "palaxmon", "«Yunon olovi».")
t.B("Nam suvoq ustiga tushirilgan rangli tasvir qanday ataladi?", "freska", "mozaika", "ikona", "miniatyura", "Freska.")
t.B("Ayo Sofiya ibodatxonasi qaysi yillarda qurilgan?", "532–537-yillarda", "527–565-yillarda", "IX asrda", "X asrda", "532–537-yillarda.")
t.B("Ayo Sofiya gumbazining diametri qancha?", "31,5 metr", "70 metr", "15 metr", "40 metr", "31,5 metr; 40 ta deraza bilan qurshalgan.")
t.B("«Yetti erkin san’at»da qaysi fan «barcha fanlarning onasi» hisoblangan?", "grammatika", "ritorika", "arifmetika", "astronomiya", "Grammatika.")
t.B("G‘arbiy Yevropa maktablarida o‘rta asrlar oxirigacha o‘qitish qaysi tilda olib borilgan?", "lotin tilida", "yunon tilida", "fransuz tilida", "nemis tilida", "Lotin tilida.")
t.B("Milliy tilda o‘qitiladigan maktablar qachon ochila boshlagan?", "XIV asrga kelib", "IX asrda", "XI asrda", "XII asrda", "XIV asrga kelib.")
t.B("Yevropada birinchi universitetlar qachon paydo bo‘lgan?", "XI–XII asrlarda", "IX asrda", "XIV asrda", "VII asrda", "XI–XII asrlarda.")
t.B("Universitetlar kimga bo‘ysungan?", "faqat Rim papasiga", "qirolga", "mahalliy yepiskopga", "shahar kengashiga", "Faqat Rim papasiga.")
t.B("Yevropadagi dastlabki universitetlar qaysilar?", "Boloniya va Parij", "Oksford va Kembrij", "Sevilya va Valensiya", "Tuluza va Neapol", "Boloniya va Parij universitetlari.")
t.B("Universitet fakultetini kim boshqargan?", "dekan", "rektor", "kansler", "professor", "Har bir fakultetni dekan boshqargan.")
t.B("Talabalar yashagan yotoqxonalar qanday atalgan?", "kollegiyalar", "monastirlar", "ratushalar", "faktoriyalar", "Kollegiyalar; keyinchalik kollejlarga asos bo‘ldi.")
t.NAT("Vizantiya o‘z daxlsizligini saqlab qoldi.", "uning madaniyati G‘arbiy Yevropa singari inqirozni boshdan kechirmadi", "Vizantiya madaniyati yo‘q bo‘ldi", "Vizantiya lotin tiliga o‘tdi", "Vizantiyada maktablar yopildi", "Vizantiya Yevropaning eng ilg‘or mamlakati bo‘lib qoldi.")
t.NAT("Knyaz Vladimir elchilari Ayo Sofiyaning go‘zalligini ko‘rdi.", "Kiyev knyazining xristianlikni Vizantiyadan qabul qilishida bu hal qiluvchi o‘rin tutgan bo‘lishi ehtimol", "Rus islomni qabul qildi", "Vladimir Ayo Sofiyani vayron qildi", "Rus katoliklikni qabul qildi", "Elchilar taassuroti tanlovga ta’sir qilgan.")
t.NAT("Markazlashgan davlatlarga malakali amaldor va huquqshunoslar zarur bo‘ldi.", "universitetlar ochila boshladi", "maktablar yopildi", "cherkov maktablari kengaydi", "lotin tili taqiqlandi", "Universitetlar paydo bo‘ldi.")
t.NAT("Xristian dini ta’siri Vizantiya madaniyatida kuchaydi.", "antik falsafa majusiylik deb qoralanib, o‘rnini ilohiyot egalladi", "antik falsafa gullab-yashnadi", "ilohiyot taqiqlandi", "Vizantiya islomni qabul qildi", "Ilohiyot antik falsafa o‘rnini egalladi.")
t.TF("Buyuk Karl lotin va yunon tillarini bilgan, ammo yozishni o‘zlashtira olmagan.", True, "To‘g‘ri.")
t.TF("O‘rta asr maktablarida o‘quvchilar yoshi bo‘yicha sinflarga bo‘lingan.", False, "Noto‘g‘ri: yosh bolalar ham, kattalar ham bir sinfda o‘qigan.")
t.TF4([("Konstantinopolda XI asr o‘rtalarida universitet ochilgan.", True), ("Kesariyalik Prokopiy VI asr tarixchisi bo‘lgan.", True),
       ("Xori monastiri hozirgi Istanbuldagi Qahriya masjididir.", True), ("Universitetlarda darslar milliy tillarda olib borilgan.", False)],
      "4-noto‘g‘ri: universitetlarda darslar lotin tilida olib borilgan.")
t.MUL([("Universitetlar san’at, tibbiyot, huquqshunoslik va ilohiyot fakultetlaridan iborat bo‘lgan.", True),
       ("Axendagi saroyda yunoncha «Akademiya» tashkil etilgan.", True),
       ("Universitetlar davlat va mahalliy cherkovga to‘liq bo‘ysungan.", False)],
      "III noto‘g‘ri: ular davlatga ham, mahalliy cherkovga ham bo‘ysunmagan, faqat papaga bo‘ysungan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Ayo Sofiya qurila boshladi", "«Yunon olovi» ixtiro qilindi", "Magnavr oliy maktabi ochildi", "Yevropada ilk universitetlar paydo bo‘ldi", "Milliy tildagi maktablar ochila boshladi"],
      "532 → VII asr → IX asr → XI–XII asr → XIV asr.")
t.MATCH("Atamalarni ma’nolari bilan moslashtiring.", ["mozaika", "freska", "ikona", "ritorika"],
        ["tosh, marmar, rangli shishadan ishlangan naqsh", "nam suvoq ustidagi rangli tasvir", "yog‘ochga ishlangan avliyolar tasviri", "notiqlik san’ati", "mantiq"], 'abcd',
        "Mozaika – naqsh; freska – suvoq ustida; ikona – yog‘ochda; ritorika – notiqlik.")
t.VENN("«Karolinglar uyg‘onishi»", "Vizantiya madaniyati",
       [("rohib Alkuin xalq maktablari", 1), ("Axen saroy akademiyasi", 1),
        ("Magnavr oliy maktabi", 2), ("«yunon olovi»", 2),
        ("o‘rta asrlar Yevropa madaniyati", 3)],
       "Karolinglar – Alkuin, Axen; Vizantiya – Magnavr, yunon olovi; ikkalasi o‘rta asr Yevropa madaniyati.")
t.MAPMATCH(EU, ['Axen', 'Bolonya', 'Oksford', 'Konstantinopol'],
           ["Karlning saroy «Akademiya»si joylashgan shahar", "Italiyadagi dastlabki universitet shahri", "Kembrij bilan birga Angliyada universitet ochilgan shahar", "Ayo Sofiya va Magnavr oliy maktabi joylashgan shahar"],
           "1 – Axen; 2 – Boloniya; 3 – Oksford; 4 – Konstantinopol.")

# 22 Arab xalifaligi madaniyati
t = Topic('y7j22', 7022); TOPICS['y7j22'] = t
t.B("Qaysi antik mutafakkirlar asarlari arab tiliga tarjima qilingan?", "Aristotel, Gippokrat, Yevklid", "Konfutsiy, Lao-szi", "Kalidasa, Budda", "Tatsit, Sezar", "Aristotel, Gippokrat va Yevklid.")
t.B("Algebraga kim asos solgan?", "Muhammad al-Xorazmiy", "Ahmad al-Farg‘oniy", "Abu Rayhon Beruniy", "Ibn Sino", "Muhammad al-Xorazmiy (783–850).")
t.B("Damashqdagi rasadxonada yangicha zij yaratish ishlariga kim rahbarlik qilgan?", "Ahmad al-Farg‘oniy", "Al-Xorazmiy", "Beruniy", "Ibn Batuta", "Ahmad al-Farg‘oniy (797–865).")
t.B("Astronomik jadval qanday ataladi?", "zij", "madrasa", "rasta", "devon", "Zij.")
t.B("Yerning dumaloqligini aniqlab, Quyosh markazdaligi haqida faraz ilgari surgan olim kim?", "Abu Rayhon Beruniy", "Al-Xorazmiy", "Al-Farg‘oniy", "Ibn Sino", "Beruniy (973–1048).")
t.B("Yevropada Avitsenna deb atalgan olim kim?", "Abu Ali ibn Sino", "Beruniy", "Al-Xorazmiy", "Al-Ma’sudiy", "Ibn Sino (980–1037).")
t.B("Ibn Sinoning tibbiyotga oid shoh asari qaysi?", "«Al-qonun fit-tib»", "«Ming bir kecha»", "«Siyosatnoma»", "«Yulduzlar jadvali»", "«Al-qonun fit-tib».")
t.B("Qaysi biri dunyoni kezgan arab sayyohi?", "ibn Batuta", "Marko Polo", "Syuan Szyan", "Eyngard", "Al-Ma’sudiy, ibn Dast, ibn Fadlan, ibn Batuta.")
t.B("«Bayt ul-hikma» kutubxonasida qancha qo‘lyozma saqlangan?", "400 ming jild", "40 ming jild", "1 mln jild", "11 ming jild", "400 ming jild.")
t.B("«Bayt ul-hikma» qayerda tashkil etilgan?", "Bag‘dodda", "Qohirada", "Tunisda", "Fesda", "IX asrda Bag‘dodda.")
t.B("Qohiradagi «Al-Azhar» qachon tashkil etilgan?", "X asrda", "VIII asrda", "IX asrda", "XII asrda", "X asrda.")
t.B("Tunisdagi ilm dargohi qanday atalgan?", "«Zaytuna»", "«Qaroviyun»", "«Al-Azhar»", "«Bayt ul-hikma»", "VIII asrda Tunisda «Zaytuna».")
t.B("Arablar choy yetishtirish va qog‘oz tayyorlashni kimdan o‘rgangan?", "xitoyliklardan", "hindlardan", "vizantiyaliklardan", "forslardan", "Xitoydan.")
t.B("Arablar hindlardan nimani o‘rgangan?", "raqamlarni va shakarqamishdan shakar olishni", "porox va kompasni", "qog‘oz tayyorlashni", "choy yetishtirishni", "Raqamlar, shakar olish, apelsin va limon yetishtirish.")
t.B("Ko‘plab xalqlar og‘zaki ijodini qamrab olgan arab adabiyoti durdonasi qaysi?", "«Ming bir kecha»", "«Gitanjali»", "«Anglosakson solnomasi»", "«Al-qonun fit-tib»", "«Ming bir kecha».")
t.B("Granadadagi mashhur saroy qaysi?", "Al-Hamro", "Al-Qasar", "Hasan masjidi", "Ismoil Somoniy maqbarasi", "Al-Hamro saroyi.")
t.B("X asrda Qurdoba xalifasi kutubxonasida qancha qo‘lyozma saqlangan?", "400 ming", "40 ming", "11 ming", "1 mln", "400 ming qo‘lyozma.")
t.NAT("Arab tili zabt etilgan mamlakatlar tillarini chetga surdi.", "arab tili maorif, fan va madaniyat tiliga aylandi", "arab tili yo‘qoldi", "lotin tili ilm tiliga aylandi", "tarjima taqiqlandi", "Arab tili fan va madaniyat tiliga aylandi.")
t.NAT("VIII asrda arablar qog‘oz yasashni o‘zlashtirdi.", "kitoblar arzon va hammabop bo‘la boshladi", "kitoblar qimmatlashdi", "kutubxonalar yopildi", "pergament keng tarqaldi", "Kitoblar arzonlashdi.")
t.NAT("Islom inson va jonivorlar suratini chizishni taqiqladi.", "masjid-madrasalar devorlari Qur’on oyatlari bitilgan chiroyli harflar bilan bezatildi", "me’morchilik to‘xtadi", "masjidlarda haykallar o‘rnatildi", "freska san’ati rivojlandi", "Arab yozuvi bezak vazifasini bajardi.")
t.NAT("X asrga kelib musulmon adabiyoti fors tiliga tarjima qilindi.", "adabiyot fors tilida ham yozila boshladi", "arab adabiyoti yo‘qoldi", "she’riyat taqiqlandi", "lotin tilida yozila boshladi", "Fors tilidagi adabiyot vujudga keldi.")
t.TF("Qadim yunon mualliflarining ko‘plab asarlari bizgacha faqat arabcha tarjimada yetib kelgan.", True, "To‘g‘ri.")
t.TF("Xalifalikda san’atning barcha sohalariga qaraganda tasviriy san’at eng yuksak taraqqiy etgan.", False, "Noto‘g‘ri: me’morchilik eng yuksak taraqqiy etgan.")
t.TF4([("Beruniy bir gradus meridian yoyi uzunligini hisoblagan.", True), ("Al-Xorazmiy arab raqamlarini soddalashtirib, keng tarqalishiga hissa qo‘shgan.", True),
       ("«Bayt ul-hikma» Damashqda tashkil etilgan.", False), ("Fesda (Marokash) «Qaroviyun» ilm dargohi bo‘lgan.", True)],
      "3-noto‘g‘ri: «Bayt ul-hikma» Bag‘dodda tashkil etilgan.")
t.MUL([("Buxorodagi Ismoil Somoniy maqbarasi xalifalik davri me’morchiligi durdonasi.", True),
       ("Masjid va madrasalardagi ikki minora Allohga e’tiqodda ko‘tarilgan qo‘llar ramzi.", True),
       ("Islomgacha arablarda she’riyat mavjud bo‘lmagan.", False)],
      "III noto‘g‘ri: islomgacha ham arablarda boy she’riyat bo‘lgan.")
t.CHR("Olimlarni tug‘ilgan yillari bo‘yicha ketma-ket joylashtiring.", ["Muhammad al-Xorazmiy", "Ahmad al-Farg‘oniy", "Abu Rayhon Beruniy", "Abu Ali ibn Sino"],
      "783 → 797 → 973 → 980.")
t.MATCH("Olimlarni sohasi bilan moslashtiring.", ["al-Xorazmiy", "al-Farg‘oniy", "Beruniy", "Ibn Sino"],
        ["algebra asoschisi", "Damashq rasadxonasida zij yaratgan", "Yer meridiani uzunligini hisoblagan", "«Al-qonun fit-tib» muallifi", "«Ming bir kecha» muallifi"], 'abcd',
        "Xorazmiy – algebra; Farg‘oniy – zij; Beruniy – meridian; Ibn Sino – tibbiyot.")
t.VENN("Bayt ul-hikma", "Al-Azhar",
       [("IX asrda Bag‘dodda tashkil etilgan", 1), ("400 ming jildli kutubxona", 1),
        ("X asrda tashkil etilgan", 2), ("Qohirada joylashgan", 2),
        ("Arab xalifaligi davridagi ilm dargohi", 3)],
       "Bayt ul-hikma – Bag‘dod, 400 ming jild; Al-Azhar – X asr, Qohira; ikkalasi xalifalik ilm dargohi.")
t.MAPMATCH('mideast', ['Bag‘dod', 'Qohira', 'Tunis', 'Granada'],
           ["«Bayt ul-hikma» joylashgan shahar", "X asrda «Al-Azhar» ochilgan shahar", "VIII asrda «Zaytuna» ochilgan shahar", "Al-Hamro saroyi joylashgan shahar"],
           "1 – Bag‘dod; 2 – Qohira; 3 – Tunis; 4 – Granada.")

# 23 Xitoy, Koreya, Yaponiya, Hindiston madaniyati
t = Topic('y7j23', 7023); TOPICS['y7j23'] = t
t.B("Xitoyliklar choy o‘simligini qachon bilgan?", "III–IV asrlarda", "IX asrda", "XIV asrda", "mil. avv. V asrda", "III–IV asrlarda.")
t.B("Xitoyning eng katta bayrami qaysi?", "Yangi yil", "fonuslar bayrami", "hosil bayrami", "Qurbon hayiti", "Yangi yil.")
t.B("Xitoyda zamonaviy futbolning uzoq ajdodi qanday o‘yin bo‘lgan?", "o‘n kishilik jamoalarning koptok o‘yini", "chovgon", "shaxmat", "oshiq", "O‘n kishidan iborat jamoalarning koptok o‘yini.")
t.B("Xitoyda oddiy xalq qaysi ta’limotni yoqlagan?", "daosizm", "buddaviylik", "konfutsiylik", "islom", "Tenglikka chaqiruvchi daosizmni.")
t.B("Ayrim Xitoy monastirlarida qanday jang san’ati o‘rgatilgan?", "u-shu", "busido", "kendo", "dzyudo", "«U-shu».")
t.B("Xitoyda ilk bo‘rtma iyeroglifli kitob qachon bosilgan?", "IX asrda", "III asrda", "XIV asrda", "VI asrda", "IX asrdayoq.")
t.B("Xitoyliklar qaysi asbobni ixtiro qilgan?", "seysmograf", "teleskop", "arbalet", "shamol tegirmoni", "Porox, kompas va seysmograf.")
t.B("Koreyada buddizm qachon tarqala boshlagan?", "IV asr oxirlarida", "VI asrda", "III asrda", "X asrda", "IV asr oxirlarida.")
t.B("Konfutsiylikka e’tiqod Koreyada birinchi bo‘lib qaysi qirollikda kuzatilgan?", "Koguryoda (III asr)", "Pekcheda (IV asr)", "Sillada (VI asr)", "Koryoda", "III asrda Koguryoda.")
t.B("Silla qirolligida qirol maslahatchisi lavozimiga kim tayinlangan?", "bosh buddaviy rohib", "konfutsiy olimi", "arab savdogari", "xitoy amaldori", "Bosh buddaviy rohib.")
t.B("Islom Koreya zaminiga qachon kirib kelgan?", "VII–X asrlarda", "XIII asrda", "IV asrda", "XV asrda", "VII–X asrlarda arab savdogarlari orqali.")
t.B("Arablar Koreyaga olib kelgan eng noyob yutuq nima bo‘lgan?", "quyosh va oy tutilishini aniqlaydigan musulmon taqvimi", "qog‘oz", "porox", "kompas", "Musulmon taqvimi.")
t.B("Yapon alifbosi qachon kashf qilingan?", "IX asr o‘rtalarida", "VIII asrda", "XII asrda", "IV asrda", "IX asr o‘rtalarida.")
t.B("Hindistonning qadimgi va o‘rta asrlar adabiy tili qaysi?", "sanskrit", "pali", "fors", "urdu", "Sanskrit.")
t.B("Hindlar qanday hisob tizimini yaratgan?", "o‘nlik tizimni", "o‘n ikkilik tizimni", "rim raqamlarini", "ikkilik tizimni", "Hozirgi arab raqamlari deb ataluvchi o‘nlik tizimni.")
t.B("Asarlari ko‘plab tillarga o‘girilgan buyuk hind dramaturgi kim?", "Kalidasa", "Xarsha", "Syuan Szyan", "Thakur", "Kalidasa.")
t.B("Ajanta ibodatxonasi necha xonadan iborat?", "29 ta", "40 ta", "70 ta", "9 ta", "Qoyalarga o‘yib ishlangan 29 ta xona.")
t.B("Dehlidagi masjidning minorasi qanday atalgan?", "Qutb Minor", "Al-Hamro", "Ajanta", "Chichen-Itsa", "70 metrlik Qutb Minor.")
t.B("Hind ayollarining o‘rama kiyimi qanday atalgan?", "sari", "kimono", "chopon", "toga", "Sari.")
t.NAT("Mo‘g‘ul istilolari boshlanib, saroydagilar mag‘lubiyat sababini buddaviylikdan ko‘rdi.", "rohiblar shaharlardan tog‘larga ketib, ibodatxonalar borish mushkul joylarda qurildi", "buddaviylik davlat dini bo‘lib qoldi", "rohiblar soliqdan ozod qilindi", "Koreya islomni qabul qildi", "XIII asrdan keyin ibodatxonalar tog‘larda qurildi.")
t.NAT("Davlatga ta’lim olgan amaldorlar zarur bo‘ldi.", "Xitoyda davlat ta’lim haqida g‘amxo‘rlik qildi", "Xitoyda maktablar yopildi", "amaldorlar meros bo‘yicha tayinlandi", "ta’lim faqat monastirlarda qoldi", "Davlat ta’limga e’tibor berdi.")
t.NAT("Hindistonda hokimiyatga musulmonlar keldi.", "shimoliy Hindistonda masjid, madrasa, maqbara va minoralar qad ko‘tardi", "hind qishloq jamoalari kastalarni bekor qildi", "sanskrit adabiyoti taqiqlandi", "hind quruvchilari ishdan chetlatildi", "Yangi musulmon me’morchiligi paydo bo‘ldi.")
t.NAT("Buddaviylik O‘rta Osiyodan Xitoyga, undan Koreyaga o‘tdi.", "turli e’tiqodlarga moslashib, Koreyada nisbatan tez tarqaldi", "Koreyada taqiqlandi", "Xitoyda yo‘qoldi", "Yaponiyaga yetib bormadi", "Budda ta’limoti Koreyada tez tarqaldi.")
t.TF("Xitoyda 11000 tomlik ulkan ensiklopediyalar tuzilgan.", True, "To‘g‘ri.")
t.TF("Hindlar mol go‘shti va spirtli ichimliklarni ko‘p iste’mol qilgan.", False, "Noto‘g‘ri: din taqiqlagani sababli deyarli iste’mol qilmagan.")
t.TF4([("Hindlar shaxmatni kashf etgan.", True), ("Ajanta ibodatxonasi to‘qqiz asr davomida qurilgan.", True),
       ("Yaponiyada VIII asrdan zodagonlar bolalari uchun maktablar ochilgan.", True), ("XIV asrgacha xitoyliklar choyni faqat quruq holda chaynagan.", False)],
      "4-noto‘g‘ri: XIV asrgacha choyni suyuq taom singari pishirishgan.")
t.MUL([("Koreya haqidagi arab yozma ma’lumotlari yevropaliklarnikidan 4–5 asr oldin bitilgan.", True),
       ("Dehli sultonligi saroyida braxman-tabiblar kasallarni davolagan.", True),
       ("Yapon alifbosi lotin yozuviga asoslangan.", False)],
      "III noto‘g‘ri: yapon alifbosi xitoy yozuviga asoslangan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Xitoyliklar choyni bildi", "Koreyada buddizm tarqala boshladi", "Yaponiyada zodagonlar maktablari ochildi", "Yapon alifbosi kashf qilindi", "Xitoyda choy pishirish usuli o‘zgardi"],
      "III–IV asr → IV asr oxiri → VIII asr → IX asr o‘rtasi → XIV asr.")
t.MATCH("Mamlakatlarni ularning madaniy yutug‘i bilan moslashtiring.", ["Xitoy", "Koreya", "Yaponiya", "Hindiston"],
        ["seysmograf va ilk gazeta", "arablardan musulmon taqvimini olgan", "IX asrda o‘z alifbosini kashf qilgan", "o‘nlik hisob tizimi va shaxmat", "«Ming bir kecha»"], 'abcd',
        "Xitoy – seysmograf; Koreya – musulmon taqvimi; Yaponiya – alifbo; Hindiston – o‘nlik tizim.")
t.VENN("Xitoy madaniyati", "Hindiston madaniyati",
       [("porox, kompas, seysmograf", 1), ("u-shu jang san’ati", 1),
        ("o‘nlik hisob tizimi", 2), ("Ajanta ibodatxonasi", 2),
        ("buddaviylik tarqalgan", 3)],
       "Xitoy – porox, u-shu; Hindiston – o‘nlik tizim, Ajanta; ikkalasida buddaviylik.")
t.MAPMATCH('asiaE', ['Ajanta', 'Dehli', 'Xitoy', 'Koreya'],
           ["qoyaga o‘yilgan 29 xonali buddaviylik ibodatxonasi joyi", "70 metrlik Qutb Minor minorasi joylashgan poytaxt", "IX asrda ilk bosma kitob chiqarilgan mamlakat", "arablar «oltinga boy Silla» deb yozgan mamlakat"],
           "1 – Ajanta; 2 – Dehli; 3 – Xitoy; 4 – Koreya.")
