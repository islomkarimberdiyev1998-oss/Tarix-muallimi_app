from qlib import Topic
TOPICS = {}
BK = 'balkan'; EA = 'eastasia'; FE = 'fareast'

# 25 Bolqon davlatlari
t = Topic('e9j25', 9125); TOPICS['e9j25'] = t
t.B("XIX asrning 70-yillarida janubiy slavyanlarning qaysi yerlarining bir qismigina mustaqil edi?", "Chernogoriya va Serbiya", "Bolgariya va Makedoniya", "Bosniya va Gersegovina", "Xorvatiya va Sloveniya", "Faqat Chernogoriya va Serbiya yerlarining bir qismi.")
t.B("Mustaqil demokratik Bolgariya Respublikasi rejasini ilgari surgan inqilobchi kim?", "Vasil Levskiy", "Xristo Botev", "Aleksandr Battenberg", "Ferdinand Koburg", "Vasil Levskiy; 1872-yilda qatl etilgan.")
t.B("1876-yilgi Bolgariya qo‘zg‘olonchilari bayrog‘ida qanday shior yozilgan?", "«Ozodlik yoki o‘lim»", "«Yer va ozodlik»", "«Biz o‘zimiz»", "«Non va tinchlik»", "«Ozodlik yoki o‘lim».")
t.B("Ozodlik harakatiga yo‘lboshchilik qilgan shoir va publitsist kim?", "Xristo Botev", "Vasil Levskiy", "Battenberg", "Koburg", "Xristo Botev; 1876-yil 1-iyunda halok bo‘ldi.")
t.B("Xristo Botev halok bo‘lgan kun Bolgariyada qanday nishonlanadi?", "Xotira kuni sifatida", "Mustaqillik kuni sifatida", "Konstitutsiya kuni sifatida", "Mehnat kuni sifatida", "Xotira kuni.")
t.B("Bolgariya konstitutsiyasi qachon qabul qilingan?", "1878-yilda", "1876-yilda", "1886-yilda", "1908-yilda", "1878-yilda; Bolgariya konstitutsiyaviy monarxiya.")
t.B("Aleksandr II qaysi qarindoshini Bolgariya davlati boshlig‘i etib saylashni taklif etgan?", "Aleksandr Battenbergni", "Ferdinand Koburgni", "Frans Ferdinandni", "Xristo Botevni", "Qaynisi Aleksandr Battenbergni.")
t.B("Aleksandr Battenberg qachon taxtdan voz kechishga majbur qilingan?", "1886-yilda", "1878-yilda", "1908-yilda", "1913-yilda", "1886-yilda.")
t.B("Battenbergdan keyin Bolgariya taxtiga kim o‘tqazilgan?", "Ferdinand Koburg", "Vasil Levskiy", "Frans Ferdinand", "Pedru II", "Avstriya-Vengriya nomzodi Ferdinand Koburg.")
t.B("Bolgariya qachon o‘zini Usmonli davlatidan to‘la mustaqil deb e’lon qilgan?", "1908-yilda", "1878-yilda", "1912-yilda", "1886-yilda", "1908-yilda.")
t.B("Ikkinchi Bolqon urushidan keyin Bolgariyada qanday hukumat hokimiyatga kelgan?", "germanparast hukumat", "rusparast hukumat", "respublikachilar", "sotsialistlar", "Germanparast hukumat.")
t.B("Albaniyada qo‘zg‘olon qaysi yillarda ko‘tarilgan?", "1909–1911-yillarda", "1876-yilda", "1912–1913-yillarda", "1885-yilda", "1909–1911-yillarda.")
t.B("Albaniya qachon mustaqillikka erishgan?", "1912-yil 28-noyabrda", "1878-yilda", "1908-yilda", "1913-yilda", "1912-yil 28-noyabrda.")
t.NAT("Battenberg armiyadagi rus zobitlarini nemis zobitlari bilan almashtirishga urindi.", "Rossiya unga dushman sifatida qaray boshlab, Bolgariyadan zobitlarini chaqirib oldi", "Rossiya Bolgariya bilan ittifoq tuzdi", "Battenberg imperator bo‘ldi", "Germaniya Bolgariyani bosib oldi", "Bu Rossiya bilan munosabatlarni buzdi.")
t.NAT("Birinchi Bolqon urushida Usmonli davlati yengildi.", "Albaniya mustaqillikka erishib, turklarning besh asrlik hukmronligi tugadi", "Albaniya Gretsiyaga qo‘shildi", "Usmonli davlati Albaniyani mustahkamladi", "Albaniya Italiyaga qo‘shildi", "1912-yil 28-noyabrda Albaniya mustaqil bo‘ldi.")
t.TF("Berlin kongressi Serbiyaning Usmonli davlatidan mustaqilligini tasdiqlagan.", True, "To‘g‘ri.")
t.TF("Polyaklar faqat Rossiya zulmi ostida bo‘lgan.", False, "Noto‘g‘ri: polyaklar Gabsburglar, Germaniya va Rossiya o‘rtasida bo‘lingan.")
t.MUL([("Serbiya Rossiyaning Usmonli davlatiga qarshi urushlarida faol qatnashgan.", True),
       ("Berlin kongressi Bolgariya hududlarini qisqartirish haqida qaror qabul qilgan.", True),
       ("Ikkinchi Bolqon urushidan keyin Bolgariya Antanta tarafida turishini e’lon qilgan.", False)],
      "III noto‘g‘ri: u «Uchlar ittifoqi» tarafida turishini bildirgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Vasil Levskiy qatl etildi", "Xristo Botev halok bo‘ldi", "Bolgariya konstitutsiyasi", "Battenberg taxtdan voz kechdi", "Bolgariya to‘la mustaqillikni e’lon qildi", "Albaniya mustaqil bo‘ldi"],
      "1872 → 1876 → 1878 → 1886 → 1908 → 1912.")
t.MAPMATCH(BK, ['Bolgariya', 'Serbiya', 'Albaniya', 'Chernogoriya'],
           ["1876-yilda «Ozodlik yoki o‘lim» shiori ostida qo‘zg‘olon bo‘lgan davlat", "mustaqilligi Berlin kongressida tasdiqlangan, Rossiya tarafdorlari ta’sirli bo‘lgan davlat", "1912-yil 28-noyabrda mustaqillikka erishgan davlat", "Serbiya bilan birga 70-yillarda mustaqil bo‘lgan kichik davlat"],
           "1 – Bolgariya; 2 – Serbiya; 3 – Albaniya; 4 – Chernogoriya.")
t.VENN("Vasil Levskiy", "Xristo Botev",
       [("mustaqil Bolgariya Respublikasi rejasini ilgari surgan", 1), ("1872-yilda qatl etilgan", 1),
        ("shoir va publitsist", 2), ("1876-yil 1-iyunda jangda halok bo‘lgan", 2),
        ("bolgar xalqining ozodlik kurashi rahnamosi", 3)],
       "Levskiy — respublika rejasi, 1872; Botev — shoir, 1876.")

# 26 Yaponiya
t = Topic('e9j26', 9126); TOPICS['e9j26'] = t
t.B("Yaponiyada bozor munosabatlariga yo‘l ochgan islohot qanday atalgan?", "Meydzi islohoti", "Stolipin islohoti", "Sinxay islohoti", "Taysey islohoti", "1867–1868-yillardagi Meydzi islohoti.")
t.B("Islohotlarni amalga oshirgan Yaponiya imperatori kim?", "Mutsixito", "Xirotito", "Taysyo", "Meydzi Tokugava", "Imperator Mutsixito.")
t.B("Yaponiyada qanday yagona pul birligi joriy etilgan?", "iyena", "yuan", "von", "dollar", "Iyena.")
t.B("To‘rt tabaqa haqidagi qonun qachon bekor qilingan?", "1869-yilda", "1871-yilda", "1889-yilda", "1867-yilda", "1869-yilda.")
t.B("1890-yilda to‘qimachilik sanoati barcha tarmoqlarning qancha qismini tashkil etgan?", "45 foizini", "10 foizini", "75 foizini", "25 foizini", "45 foizini.")
t.B("Chorak asr davomida Yaponiyada nechta sanoat korxonasi qurilgan?", "1300 ta", "175 ta", "600 ta", "81 ta", "1300 ta.")
t.B("Yaponiyada sanoat ishlab chiqarishi Rossiyadan necha barobar tezroq rivojlangan?", "o‘n barobar", "ikki barobar", "besh barobar", "teng", "O‘n barobar.")
t.B("1900–1913-yillarda Yaponiya sanoat hajmi bo‘yicha qaysi davlatdan o‘zib ketgan?", "Italiyadan", "Fransiyadan", "Germaniyadan", "Britaniyadan", "Italiyadan o‘zib, Fransiyaga yaqinlashdi.")
t.B("Yaponiya konstitutsiyasi qachon qabul qilingan?", "1889-yilda", "1869-yilda", "1871-yilda", "1895-yilda", "1889-yilda.")
t.B("Yaponiya konstitutsiyasi qaysi davlat konstitutsiyasi namunasida tuzilgan?", "Prussiya", "Fransiya", "AQSH", "Britaniya", "Prussiya konstitutsiyasi namunasida.")
t.B("Yaponiyada saylov yoshi necha yosh qilib belgilangan?", "25 yosh", "21 yosh", "18 yosh", "30 yosh", "25 yosh.")
t.B("Yaponiya qachon Ryukyu orolini bosib olgan?", "1879-yilda", "1875-yilda", "1895-yilda", "1910-yilda", "1879-yilda.")
t.B("Xitoy qo‘shinlari 1894-yilda qayerda mag‘lubiyatga uchragan?", "Pxenyan yonida", "Seulda", "Port-Arturda", "Pekinda", "Pxenyan yonida.")
t.B("Yaponiya–Xitoy urushidan keyin 1895-yilda qanday sulh tuzilgan?", "Simonoseki sulhi", "Portsmut sulhi", "Pekin sulhi", "San-Stefano sulhi", "Simonoseki sulhi.")
t.B("Yaponiya Koreyani qachon harbiy kuch bilan o‘ziga qo‘shib olgan?", "1910-yilda", "1895-yilda", "1876-yilda", "1905-yilda", "1910-yilda.")
t.NAT("1894-yilda Yaponiya Seulda saroy to‘ntarishi uyushtirib, yaponparast hukumat tuzdi.", "Yapon–Xitoy urushi boshlandi", "Koreya mustaqil bo‘ldi", "Xitoy Yaponiya bilan ittifoq tuzdi", "Rossiya Koreyani egalladi", "Bu Yapon–Xitoy urushiga olib keldi.")
t.NAT("Aholining kambag‘alligi sanoat mahsulotlarini sotishni qiyinlashtirdi.", "hukmron doiralar qo‘shni davlatlar hududlarini bosib olishga intildi", "sanoat yopildi", "ish haqi oshirildi", "Yaponiya qurolsizlandi", "Yaponiya zo‘r berib qurollanib, bosqinchilik urushlarini boshladi.")
t.TF("Simonoseki sulhiga ko‘ra Xitoy Tayvan va Penxu orollarini Yaponiyaga bergan.", True, "To‘g‘ri; Lyaodun ham berildi.")
t.TF("Yaponiya konstitutsiyasi imperator huquqlarini sezilarli cheklagan.", False, "Noto‘g‘ri: imperator huquqlari saqlanib, yanada kengaytirilgan.")
t.MUL([("Samuray, dehqon, hunarmand va savdogar tabaqalari rasman teng huquqli deb e’lon qilingan.", True),
       ("Hosildan hissa ko‘rinishidagi soliq pul solig‘i bilan almashtirilgan.", True),
       ("Yaponiyada hokimiyat faqat burjuaziya qo‘lida bo‘lgan.", False)],
      "III noto‘g‘ri: hokimiyat zamindor-burjuaziya tabaqalari ittifoqi qo‘lida edi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Meydzi islohoti", "To‘rt tabaqa qonuni bekor qilindi", "Ryukyu bosib olindi", "Konstitutsiya qabul qilindi", "Simonoseki sulhi", "Koreya anneksiya qilindi"],
      "1867–1868 → 1869 → 1879 → 1889 → 1895 → 1910.")
t.MAPMATCH(EA, ['Seul', 'Simonoseki', 'Tayvan', 'Ryukyu orollari'],
           ["1894-yilda Yaponiya saroy to‘ntarishi uyushtirgan Koreya poytaxti", "1895-yilda Yaponiya va Xitoy sulh tuzgan joy", "Simonoseki sulhiga ko‘ra Yaponiyaga berilgan orol", "1879-yilda Yaponiya bosib olgan orollar"],
           "1 – Seul; 2 – Simonoseki; 3 – Tayvan; 4 – Ryukyu.")
t.VENN("Meydzi islohotlari", "1889-yilgi konstitutsiya",
       [("yagona pul birligi — iyena joriy etilgan", 1), ("yalpi harbiy xizmat qonuni", 1),
        ("ikki palatali parlament joriy etilgan", 2), ("saylov yoshi 25 yosh", 2),
        ("Yaponiyani modernizatsiyalash", 3)],
       "Meydzi — iyena, harbiy xizmat; konstitutsiya — parlament, saylov.")

# 27 XIX asr oxirida Xitoy
t = Topic('e9j27', 9127); TOPICS['e9j27'] = t
t.B("XIX asr oxirida Xitoy qanday davlat edi?", "qoloq, yarimfeodal davlat", "industrial davlat", "respublika", "mustamlakachi davlat", "Qoloq, yarimfeodal davlat.")
t.B("Chet el firmalarining yollangan vakillari bo‘lgan Xitoy burjuaziyasi qanday atalgan?", "kompradorlar", "samuraylar", "mandarinlar", "ixetuanlar", "Kompradorlar.")
t.B("70-yillarda ajnabiylar Xitoyning nechta bandargohiga bemalol kirgan?", "26 ta", "10 ta", "100 ta", "5 ta", "26 ta bandargohga.")
t.B("1897–1898-yillarda Germaniya qaysi bandargohni bosib olgan?", "Szyaochjouvan (Sindao)", "Port-Artur", "Veyxayvey", "Guanchjouvan", "Szyaochjouvan (Sindao).")
t.B("Rossiya Xitoyning qaysi bandargohini ijaraga olgan?", "Port-Artur (Lyuyshun)", "Veyxayvey", "Sindao", "Gonkong", "Port-Artur.")
t.B("Eng boy hudud — Yanszi havzasi kimning ta’sir doirasiga tushgan?", "Buyuk Britaniya", "Fransiya", "Germaniya", "Yaponiya", "Buyuk Britaniya.")
t.B("Shimoliy Xitoyda birinchi temiryo‘l qachon ishga tushirilgan?", "1881-yilda", "1897-yilda", "1900-yilda", "1876-yilda", "1881-yilda.")
t.B("1884-yilda Fransiyaning qaysi davlatni bosib olishi Fransiya–Xitoy munosabatlarini yomonlashtirgan?", "Vyetnamni", "Koreyani", "Tayvanni", "Laosni", "Vyetnamni.")
t.B("«Xitoy uyg‘onish jamiyati»ni kim boshqargan?", "Sun Yat Sen", "Yuan Shikay", "Mutsixito", "Xey", "Sun Yat Sen.")
t.B("«Ixetuan» nimani anglatadi?", "«Tinchlik va adolat uchun ko‘tarilgan musht»", "«Xitoy uyg‘onishi»", "«Xalq gazetasi»", "«Milliy partiya»", "«Tinchlik va adolat uchun ko‘tarilgan musht».")
t.B("«Ixetuan» harakati qachon qo‘zg‘olon tusini olgan?", "1899-yilda", "1900-yilda", "1884-yilda", "1911-yilda", "1899-yilda.")
t.B("Xitoyga intervensiyada nechta davlat qatnashgan?", "sakkiz", "uch", "besh", "o‘n ikki", "Sakkiz davlat.")
t.B("Chet el interventlari Pekinni qachon egallagan?", "1900-yil iyulda", "1899-yil sentabrda", "1911-yilda", "1895-yilda", "1900-yil iyulda.")
t.B("Xitoy interventlarga qancha tovon to‘lashga majbur etilgan?", "33 mln. dollar", "5 mlrd. frank", "1,5 mlrd. dollar", "10 mln. dollar", "33 mln. dollar.")
t.B("O‘zga davlat ichki ishlariga zo‘rlik bilan aralashish nima deyiladi?", "intervensiya", "konvensiya", "anneksiya", "komprador", "Intervensiya.")
t.NAT("Xitoy Yaponiya bilan 1894–1895-yillardagi urushda mag‘lub bo‘ldi.", "chet ellik monopolistlar Xitoyni yanada ko‘proq talab, asoratga sola boshladi", "Xitoy kuchaydi", "Xitoy Yaponiyani bosib oldi", "Xitoy respublika bo‘ldi", "Mag‘lubiyat Xitoyni yarimmustamlakaga aylantirdi.")
t.NAT("Ixetuanlar Pekinga yurish qilib, u yerda o‘z hokimiyatini o‘rnatdi.", "bu chet elliklar intervensiyasiga bahona bo‘ldi", "Sin sulolasi qulab tushdi", "Xitoy mustaqil bo‘ldi", "chet elliklar Xitoyni tark etdi", "Sakkiz davlat intervensiyasi boshlandi.")
t.TF("Ixetuan qo‘zg‘oloni mustamlakachilarni ehtiyotkorlik bilan harakat qilishga majbur etgan.", True, "To‘g‘ri.")
t.TF("Intervensiyadan keyin Xitoyga qurol-aslaha kiritish erkin qilib qo‘yilgan.", False, "Noto‘g‘ri: qurol-aslaha kiritish taqiqlangan.")
t.MUL([("1897-yilda Xitoyda 600 ga yaqin chet el firmalari bo‘lgan.", True),
       ("Xitoy–Britaniya konvensiyasi Britaniyaga 10 dan ortiq bandargohga erkin kirish huquqini bergan.", True),
       ("XIX asr oxirida Xitoyda eksport importdan ancha ko‘p edi.", False)],
      "III noto‘g‘ri: import eksportdan ancha ko‘p edi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Birinchi temiryo‘l ishga tushirildi", "Fransiya Vyetnamni bosib oldi", "Yapon–Xitoy urushi", "Germaniya Sindaoni bosib oldi", "Ixetuan qo‘zg‘oloni", "Interventlar Pekinni egalladi"],
      "1881 → 1884 → 1894–1895 → 1897–1898 → 1899 → 1900.")
t.MAPMATCH(EA, ['Pekin', 'Sindao', 'Tayvan', 'Vyetnam'],
           ["1900-yilda interventlar egallagan Xitoy poytaxti", "Germaniya bosib olgan bandargoh", "ixetuanlar Xitoyga birlashtirishni talab qilgan orol", "1884-yilda Fransiya bosib olgan davlat"],
           "1 – Pekin; 2 – Sindao; 3 – Tayvan; 4 – Vyetnam.")
t.VENN("«Xitoy uyg‘onish jamiyati»", "«Ixetuan» harakati",
       [("Sun Yat Sen boshqargan", 1), ("demokratik milliy davlat tuzishni maqsad qilgan", 1),
        ("«Manjur sinlarini haydab chiqaramiz» shiori", 2), ("1899-yilda qo‘zg‘olon ko‘targan", 2),
        ("manjurlarning Sin sulolasiga qarshi", 3)],
       "Jamiyat — Sun Yat Sen, demokratiya; Ixetuan — qo‘zg‘olon, chet elliklarga qarshi.")

# 28 XX asr boshlarida Xitoy
t = Topic('e9j28', 9128); TOPICS['e9j28'] = t
t.B("XX asr boshida Xitoyda har yili nechtadan ortiq korxona ishga tushirilgan?", "50 tadan", "5 tadan", "500 tadan", "1300 tadan", "50 tadan ko‘proq; eksport 2 baravar o‘sdi.")
t.B("Tovar ayirboshlashda qaysi davlat birinchi o‘rinda turgan?", "Buyuk Britaniya", "Yaponiya", "AQSH", "Rossiya", "Buyuk Britaniya.")
t.B("Sun Yat Sen qaysi yillarda yashagan?", "1866–1925", "1851–1914", "1875–1919", "1866–1911", "1866–1925.")
t.B("Sun Yat Sen qayerda tug‘ilgan?", "Guanchjou (Kanton) yaqinida", "Pekinda", "Nankinda", "Shanxayda", "Guanchjou yaqinida dehqon oilasida.")
t.B("Sun Yat Sen qayerda tibbiyot institutini tamomlagan?", "Gonkongda", "Tokioda", "Londonda", "Pekinda", "Gonkongda.")
t.B("1905-yilda Sun Yat Sen qanday tashkilot tuzgan?", "«Xitoy uyushmalari ittifoqi» (Tunminxay)", "Gomindan", "«Ixetuan»", "«Xitoy uyg‘onish jamiyati»", "Tunminxay.")
t.B("«Minbao» gazetasining ma’nosi nima?", "«Xalq gazetasi»", "«Yangi Xitoy»", "«Ozodlik»", "«Tong»", "«Xalq gazetasi».")
t.B("Inqilobchilar Uxanni qachon to‘la qo‘lga kiritgan?", "1911-yil 11-oktabrda", "1912-yil 12-fevralda", "1911-yil 29-dekabrda", "1913-yilda", "11-oktabrda.")
t.B("1911-yilgi inqilob qanday nom olgan?", "Sinxay inqilobi", "Ixetuan inqilobi", "Meydzi inqilobi", "Ikkinchi inqilob", "Sinxay inqilobi.")
t.B("Millat Majlisi qayerda to‘plangan?", "Nankinda", "Pekinda", "Uxanda", "Guanchjouda", "29-dekabrda Nankinda.")
t.B("Pekindagi imperator hukumatining boshlig‘i kim edi?", "Yuan Shikay", "Sun Yat Sen", "Mutsixito", "Xey", "Yuan Shikay.")
t.B("Sin sulolasi qachon taxtdan voz kechgan?", "1912-yil 12-fevralda", "1911-yil 11-oktabrda", "1913-yilda", "1914-yilda", "1912-yil 12-fevralda.")
t.B("1912-yilda demokratik kuchlar qanday partiya tuzgan?", "Gomindan", "Tunminxay", "Ixetuan", "Minbao", "Gomindan (Milliy partiya).")
t.B("1913-yilda Xitoy janubidagi qo‘zg‘olon qanday nomlangan?", "«Ikkinchi inqilob»", "«Sinxay inqilobi»", "«Ixetuan qo‘zg‘oloni»", "«Uxan qo‘zg‘oloni»", "«Ikkinchi inqilob».")
t.B("Sin sulolasi qaysi yillarda hukmronlik qilgan?", "1644–1911-yillarda", "1628–1644-yillarda", "1368–1644-yillarda", "1912–1949-yillarda", "1644–1911-yillarda.")
t.NAT("Intervensiya xavfi ostida qoldi.", "Sun Yat Sen prezidentlikni Yuan Shikayga topshirdi", "Sun Yat Sen urush e’lon qildi", "Xitoy monarxiyaga qaytdi", "Gomindan tarqatildi", "Sun Yat Sen prezidentlikdan voz kechdi.")
t.NAT("1914-yilda Konstitutsiyaviy Kengashda «Yangi Xitoy Konstitutsiyasi» qabul qilindi.", "Yuan Shikay cheklanmagan hokimiyatga ega bo‘lib, harbiy diktatura o‘rnatildi", "Xitoyda demokratiya qaror topdi", "Sun Yat Sen prezident bo‘ldi", "respublika muassasalari kengaydi", "Respublika muassasalari tugatildi.")
t.TF("«Sinxay» so‘zi o‘zbek tilida «yil» degan ma’noni anglatadi.", True, "To‘g‘ri.")
t.TF("Nankindagi konstitutsiyada «yerga egalik qilishda teng huquqli bo‘lish» shiori o‘z aksini topgan.", False, "Noto‘g‘ri: bu shior aks etmagan.")
t.MUL([("Tunminxay dasturida Sin monarxiyasini ag‘darish va Respublika ta’sis etish ko‘zda tutilgan.", True),
       ("Yuan Shikay Millat Majlisini o‘zini besh yilga prezident etib saylashga majbur qilgan.", True),
       ("«Ikkinchi inqilob» g‘alaba bilan tugagan.", False)],
      "III noto‘g‘ri: u hukumat qo‘shinlari tomonidan tor-mor etilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Tunminxay tuzildi", "Uxan inqilobchilar qo‘liga o‘tdi", "Millat Majlisi Nankinda to‘plandi", "Sin sulolasi taxtdan voz kechdi", "«Ikkinchi inqilob»", "«Yangi Xitoy Konstitutsiyasi»"],
      "1905 → 1911-yil 11-oktabr → 29-dekabr → 1912-yil 12-fevral → 1913 → 1914.")
t.MAPMATCH(EA, ['Uxan', 'Nankin', 'Pekin', 'Gonkong'],
           ["1911-yil 11-oktabrda inqilobchilar qo‘lga kiritgan shahar", "Millat Majlisi to‘planib, Sun Yat Sen prezident etib saylangan shahar", "Yuan Shikay boshliq imperator hukumati joylashgan shahar", "Sun Yat Sen tibbiyot institutini tamomlagan shahar"],
           "1 – Uxan; 2 – Nankin; 3 – Pekin; 4 – Gonkong.")
t.VENN("Sun Yat Sen", "Yuan Shikay",
       [("Tunminxay va Gomindanga rahbarlik qilgan", 1), ("Nankinda vaqtincha prezident etib saylangan", 1),
        ("Pekindagi imperator hukumati boshlig‘i", 2), ("harbiy diktatura o‘rnatgan", 2),
        ("Xitoy Respublikasi prezidenti bo‘lgan", 3)],
       "Sun Yat Sen — inqilobchi demokrat; Yuan Shikay — diktator; ikkalasi prezident bo‘lgan.")
