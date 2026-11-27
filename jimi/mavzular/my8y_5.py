from qlib import Topic, PLACES, REG
TOPICS = {}

# 17 O‘rta asrlarda Afrika
t = Topic('y8j17', 8017); TOPICS['y8j17'] = t
t.B("Afrika kattaligi va aholi soni bo‘yicha dunyoda nechanchi o‘rinda turadi?", "ikkinchi", "birinchi", "uchinchi", "to‘rtinchi", "Ikkinchi o‘rinda.")
t.B("Qit’aning shimoli-sharqida yashagan, chorvachilik ustun bo‘lgan qabilalar qaysilar?", "Nilot qabilalari", "bantu", "bushmenlar", "barbarlar", "Nilot qabilalari.")
t.B("Markaziy va Janubiy Afrikada dehqonchilik bilan shug‘ullangan qabilalar qaysilar?", "bantu", "barbarlar", "bushmenlar", "nilotlar", "Bantu qabilalari.")
t.B("Hayoti tosh davri odamlaridan deyarli farq qilmagan ovchi-terimchi qabila qaysi?", "bushmenlar", "bantu", "nilotlar", "songaylar", "Janubiy afrikalik bushmenlar.")
t.B("Mamluklar Ayyubiylar sulolasini qachon ag‘darib tashlagan?", "1250-yilda", "1260-yilda", "1187-yilda", "1076-yilda", "1250-yilda.")
t.B("Arab tilida «Sudan» qanday ma’noni anglatadi?", "«qora tanlilar mamlakati»", "«oltin yurti»", "«cho‘l»", "«qora qit’a»", "«Qora tanlilar mamlakati».")
t.B("G‘arbiy Sudandagi eng qudratli davlat – Gana qachon vujudga kelgan?", "VIII asrda", "XI asrda", "XIII asrda", "XV asrda", "VIII asrda.")
t.B("Gana hukmdorini qanday ta’riflashgan?", "«oltinlarning egasi»", "«Quyosh o‘g‘li»", "«Osmon o‘g‘li»", "«arslon yurak»", "«Oltinlarning egasi».")
t.B("Ganani 1076-yilda kim bosib olgan?", "Marokash sultoni Abu Bakr", "Sundiata Keyta", "Mansa Muso", "Sunni Ali", "Marokash sultoni Abu Bakr.")
t.B("Mali davlatining poytaxti qaysi shahar bo‘lgan?", "Niara", "Gao", "Tombuktu", "Jenne", "Niara.")
t.B("Mali qaysi hukmdor davrida yuksala boshlagan?", "Sundiata Keyta", "Mansa Muso", "Sunni Ali", "Muhammad I", "XIII asrda Sundiata Keyta davrida.")
t.B("Mali imperiyasi qaysi hukmdor davrida qudrat cho‘qqisiga chiqqan?", "Mansa Muso", "Sundiata Keyta", "Abu Bakr", "Sunni Ali", "Mansa Muso (1312–1337).")
t.B("Mansa Muso nechta o‘lka va viloyat ustidan nazorat o‘rnatgan?", "yigirma to‘rtta", "o‘nta", "yetmishta", "to‘rtta", "Yigirma to‘rtta.")
t.B("XV asrda Malini qaysi davlat bosib olgan?", "Songay", "Gana", "Marokash", "Monomotapa", "Songay davlati.")
t.B("Songay qaysi hukmdorlar davrida har tomonlama rivojlangan?", "Sunni Ali va Muhammad I", "Sundiata va Mansa Muso", "Abu Bakr va Salohiddin", "Qutuz va Baybars", "Sunni Ali va Muhammad I.")
t.B("Monomotapa davlatining poytaxti qaysi shahar bo‘lgan?", "Buyuk Zimbabve", "Niara", "Gao", "Tombuktu", "Buyuk Zimbabve; 15 ming aholi.")
t.B("XVII asr oxirida Monomotapani kimlar bosib olgan?", "shona qabilalari", "Marokash sultoni", "mamluklar", "songaylar", "Shona qabilalari.")
t.NAT("G‘arbiy Sudan qabila boshliqlari arablar bilan savdodan katta foyda oldi.", "ular hukmdorga aylanib, Gana, Mali, Songay davlatlari vujudga keldi", "savdo to‘xtadi", "arablar bu hududni bosib oldi", "Sudan aholisi kamaydi", "G‘arbiy Sudanda davlatlar paydo bo‘ldi.")
t.NAT("Gana Marokash bilan uzoq kurashdi, oltin zaxiralari tugadi.", "Gana tanazzulga yuz tutib, parchalanib ketdi", "Gana Marokashni bosib oldi", "Gana kuchaydi", "Gana Mali bilan birlashdi", "Gana parchalandi.")
t.NAT("Sundiata Keyta Bambukning oltinga boy hududlarini egalladi.", "davlatning moliyaviy farovonligi uchun mustahkam poydevor yaratildi", "Mali qashshoqlashdi", "Mali Songayga bo‘ysundi", "oltin savdosi taqiqlandi", "Mali boyidi.")
t.NAT("Afrika boshqa qit’alardan geografik jihatdan ajralib qoldi.", "porox, qog‘oz, chinni kabi yangiliklardan chetda qolib, taraqqiyotda orqada qoldi", "Afrika eng rivojlangan qit’aga aylandi", "Afrika Yevropani bosib oldi", "neolit inqilobi erta yuz berdi", "Taraqqiyotdan orqada qolish sabablaridan biri.")
t.TF("Mamluklar 1260-yilda Sayfiddin Qutuz boshchiligida mo‘g‘ullar bosqinini to‘xtatgan.", True, "To‘g‘ri.")
t.TF("Afrikada neolit inqilobi Yevropa va Osiyoga qaraganda ancha oldin sodir bo‘lgan.", False, "Noto‘g‘ri: ancha kechroq sodir bo‘lgan.")
t.TF4([("Arab savdogarlari tuzni oltinga ayirboshlagan.", True), ("Mali Niger daryosining yuqori oqimida vujudga kelgan.", True),
       ("XVI asr oxirida Songayni Mali bosib olgan.", False), ("Monomotapa hukmdori oliy ruhoniy ham hisoblangan.", True)],
      "3-noto‘g‘ri: Songayni XVI asr oxirida Marokash sultonligi bosib olgan.")
t.MUL([("Gana hukmdorlari arab savdogarlariga homiylik qilib, islomning yoyilishiga imkon bergan.", True),
       ("Monomotapaning eng rivojlangan davri XV asrga to‘g‘ri keladi.", True),
       ("Sahroyi Kabir Afrikani boshqa qit’alar bilan bog‘laydigan qulay yo‘l bo‘lgan.", False)],
      "III noto‘g‘ri: Sahroyi Kabir quruqlik orqali borishni imkonsiz qilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Gana davlati vujudga keldi", "Abu Bakr Ganani bosib oldi", "Mamluklar Ayyubiylarni ag‘dardi", "Ayn-Jalutda mo‘g‘ullar to‘xtatildi", "Mansa Muso hukmronligi boshlandi"],
      "VIII asr → 1076 → 1250 → 1260 → 1312.")
t.MATCH("Hukmdorlarni davlati bilan moslashtiring.", ["Sundiata Keyta", "Mansa Muso", "Sunni Ali", "Abu Bakr"],
        ["Malini yuksaltira boshlagan", "Mali qudrati cho‘qqisidagi hukmdor", "Songay hukmdori", "Ganani bosib olgan Marokash sultoni", "Monomotapa hukmdori"], 'abcd',
        "Sundiata – Mali yuksalishi; Mansa Muso – cho‘qqi; Sunni Ali – Songay; Abu Bakr – Marokash.")
t.VENN("Gana", "Mali",
       [("VIII asrda vujudga kelgan, «oltinlar egasi»", 1), ("1076-yilda Marokash bosib olgan", 1),
        ("poytaxti Niara", 2), ("Mansa Muso davrida cho‘qqiga chiqqan", 2),
        ("G‘arbiy Sudandagi oltin savdosi davlati", 3)],
       "Gana – VIII asr, Marokash; Mali – Niara, Mansa Muso; ikkalasi oltin savdosi davlati.")
t.MAPMATCH('africa', ['Misr (Afrika)', 'Gana', 'Gao', 'Buyuk Zimbabve'],
           ["1250-yilda Mamluklar davlati tuzilgan mamlakat", "VIII asrda vujudga kelgan «oltinlar egasi» davlati", "Songay qabilalari yashagan savdo markazi", "Monomotapa davlati poytaxti"],
           "1 – Misr; 2 – Gana; 3 – Gao; 4 – Buyuk Zimbabve.")

# 18 O‘rta asrlarda Amerika xalqlari
t = Topic('y8j18', 8018); TOPICS['y8j18'] = t
t.B("Shimoliy Amerika hindulari qaysi irqqa mansub?", "mongoloid", "yevropoid", "negroid", "avstraloid", "Osiyodan borgani uchun mongoloid irqiga.")
t.B("«Qizil tanli» iborasi qanday kelib chiqqan?", "jangchilarning badanini qizil bo‘yoq bilan bo‘yashidan", "quyoshda qorayishidan", "qizil kiyim kiyishidan", "qizil tuproqdan", "Badanni qizil bo‘yoq bilan bo‘yash odatidan.")
t.B("Kichik Kolorado va Rio Grande havzalarida qaysi qabilalar madaniyati shakllangan?", "Pueblo va Pima", "irokezlar", "krik va chiroki", "aleutlar", "Pueblo va Pima.")
t.B("Buyuk ko‘llar yaqinida qaysi qabilalar madaniyati joylashgan?", "irokezlar", "Pueblo", "natchez", "eskimoslar", "Irokez qabilalari.")
t.B("Irokezlarning uzun uylari nechtagacha oilani sig‘dira olgan?", "20 tagacha", "5 tagacha", "100 tagacha", "2 tagacha", "20 tagacha oilani.")
t.B("Irokezlarning Besh qabila ittifoqi qanday atalgan?", "«Irokezlar ligasi»", "«Pueblo ittifoqi»", "«Uchlar ittifoqi»", "«Buyuk ko‘llar ittifoqi»", "«Irokezlar ligasi».")
t.B("Grenlandiya va Alyaskadagi tub aholi kimlar?", "eskimoslar", "aleutlar", "irokezlar", "Pueblo", "Eskimoslar.")
t.B("Mayyalarni nima uchun «Yangi dunyo yunonlari» deb atashgan?", "har bir shahar-davlati mustaqil boshqaruvga ega bo‘lgani uchun", "yunon tilida gapirgani uchun", "Olimpiya o‘yinlarini o‘tkazgani uchun", "dengizchi bo‘lgani uchun", "Shahar-davlatlari mustaqil bo‘lgan.")
t.B("1263-yilda asos solinib, Yukatanning asosiy markaziga aylangan shahar qaysi?", "Mayyapan", "Chichen-Itsa", "Tikal", "Kopan", "Mayyapan.")
t.B("Mayyalarda pul vazifasini nima bajargan?", "loviya va kakao urug‘i", "oltin tangalar", "chig‘anoqlar", "tuz", "Loviya va kakao urug‘i.")
t.B("Mayyalar davlati qachon to‘liq bo‘ysundirilgan?", "1697-yilda", "1528-yilda", "1521-yilda", "1572-yilda", "1697-yilda.")
t.B("Atsteklar Tenochtitlanga qachon asos solgan?", "1325-yilda", "1376-yilda", "1429-yilda", "1521-yilda", "1325-yilda Teskoko ko‘lidagi orollarda.")
t.B("Atsteklar qaysi qabilaga tobe bo‘lib, soliq to‘lagan?", "tepanek", "tenochka", "tlakopan", "teskoko", "Tepanek qabilasiga.")
t.B("Atsteklar mustaqillikka qachon erishgan?", "1429-yilda", "1325-yilda", "1376-yilda", "1521-yilda", "1429-yilda.")
t.B("Atsteklar davlatini tugatgan ispan konkistadori kim?", "Ernan Kortes", "Kolumb", "Pisarro", "Magellan", "1521-yilda Ernan Kortes.")
t.B("Inklar imperiyasi kimning davrida vujudga kelgan?", "Inka Pachakutek", "Montezuma I", "Montezuma II", "Oliy Inka Atahualpa", "Inka Pachakutek.")
t.B("Inklar imperiyasi nechta viloyatga bo‘lingan?", "to‘rtta", "o‘n ikkita", "uchta", "yigirmata", "To‘rt viloyatga.")
t.B("Inklar dalalarni sug‘orish uchun qanday inshoot qurgan?", "akveduklar (osma quvurlar)", "zinapoyali ehromlar", "to‘g‘onlar", "suzuvchi dalalar", "Akveduklar.")
t.B("Inklar davlati qachon butunlay tugatilgan?", "1572-yilda", "1532-yilda", "1521-yilda", "1697-yilda", "1572-yilda.")
t.NAT("Atsteklar Teskoko va Tlakopan bilan ittifoq tuzib, tepaneklarga qarshi qo‘zg‘olon ko‘tardi.", "1429-yilda mustaqillikka erishib, Tenochtitlan eng qudratli shaharga aylandi", "atsteklar tepaneklarga to‘liq bo‘ysundi", "Tenochtitlan vayron bo‘ldi", "ittifoq tarqaldi", "Atsteklar mustaqil bo‘ldi.")
t.NAT("Tenochtitlan, Teskoko va Tlakopan ittifoqi buzildi.", "atsteklar davlati zaiflashib, 1521-yilda Kortes uni tugatdi", "atsteklar kuchaydi", "mayyalar atsteklarni bosib oldi", "inklar Meksikani egalladi", "Konkistadorlar Tenochtitlanni egalladi.")
t.NAT("XVI asr boshida inklar imperiyasida taxt vorislari o‘rtasida kurash boshlandi.", "imperiya ikkiga bo‘linib, 1532-yilda konkistadorlar inklarni tor-mor etdi", "imperiya kengaydi", "inklar Ispaniyani bosib oldi", "Kusko poytaxtlikdan mahrum bo‘ldi", "Oliy Inka asir olindi.")
t.NAT("Inklar bosib olingan qabilalarni kechua tilini o‘rganishga majbur qildi.", "ular orasida inklarning urf-odat va qonunlari joriy etildi", "kechua tili yo‘qoldi", "qabilalar mustaqil bo‘ldi", "inklar boshqa tilga o‘tdi", "Inklar madaniyati yoyildi.")
t.TF("Kartoshkaning ko‘plab turlari Yevropaga inklar yurtidan olib borilgan.", True, "To‘g‘ri.")
t.TF("Shimoliy Amerika hindulari yirik shaharlar va katta imperiyalar barpo etgan.", False, "Noto‘g‘ri: ular yirik shaharlar va katta imperiyalarga asos solmagan.")
t.TF4([("Kaliforniya hindulari dehqonchilikni bilmagan.", True), ("Mayyalar kakao daraxtini birinchilardan bo‘lib o‘stirgan.", True),
       ("Atsteklarda tlatoani bo‘lish uchun kamida o‘n yetti dushmanni asir olish kerak bo‘lgan.", True), ("Inklar imperiyasining markazi Tenochtitlan bo‘lgan.", False)],
      "4-noto‘g‘ri: inklar markazi Quyosh shahri – Kusko.")
t.MUL([("Missisipi aholisi temir tishli chopqilar bilan yerga ishlov bergan.", True),
       ("Montezuma I davrida Tenochtitlanda katta qurilish ishlari olib borilgan.", True),
       ("Aleutlar Buyuk ko‘llar yaqinida yashagan.", False)],
      "III noto‘g‘ri: aleutlar Aleut orollari va Alyaska yarimoroli g‘arbiy qirg‘oqlarida yashagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Mayyapan shahriga asos solindi", "Tenochtitlanga asos solindi", "Birinchi tlatoani saylandi", "Atsteklar mustaqillikka erishdi", "Kortes Tenochtitlanni egalladi", "Konkistadorlar inklarni tor-mor etdi", "Inklar davlati tugatildi"],
      "1263 → 1325 → 1376 → 1429 → 1521 → 1532 → 1572.")
t.MATCH("Xalqlarni ular yashagan joy bilan moslashtiring.", ["irokezlar", "Pueblo", "eskimoslar", "inklar"],
        ["Buyuk ko‘llar yaqini", "Kichik Kolorado va Rio Grande havzasi", "Grenlandiya va Alyaska", "And tog‘lari, markazi Kusko", "Teskoko ko‘li orollari"], 'abcd',
        "Irokezlar – Buyuk ko‘llar; Pueblo – Rio Grande; eskimoslar – Grenlandiya; inklar – Kusko.")
t.VENN("Atsteklar", "Inklar",
       [("poytaxti Tenochtitlan", 1), ("1521-yilda Kortes tugatgan", 1),
        ("markazi Kusko", 2), ("akveduklar qurgan", 2),
        ("ispan konkistadorlari tomonidan tugatilgan davlat", 3)],
       "Atsteklar – Tenochtitlan, Kortes; inklar – Kusko, akveduklar; ikkalasini konkistadorlar tugatgan.")
t.MAPMATCH('amer', ['Buyuk ko‘llar', 'Tenochtitlan', 'Mayyapan', 'Kusko'],
           ["irokezlar madaniyati joylashgan hudud", "1325-yilda atsteklar asos solgan shahar", "1263-yilda asos solingan Yukatanning asosiy markazi", "inklarning «Quyosh shahri»"],
           "1 – Buyuk ko‘llar; 2 – Tenochtitlan; 3 – Mayyapan; 4 – Kusko.")
