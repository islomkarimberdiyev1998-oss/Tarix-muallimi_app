from qlib import Topic
TOPICS = {}
W = 'globe'; EU = 'europe'

# 1 Buyuk geografik kashfiyotlar
t = Topic('e8j1', 801); TOPICS['e8j1'] = t
t.B("Atlantika okeanidan xavfsiz suzib o‘ta oladigan ilk yelkanli kema qanday atalgan?", "karavella", "galera", "drakkar", "fregat", "XV asr oxirida karavella yaratildi.")
t.B("Osiyoga O‘rtayer dengizi orqali savdo yo‘llarini kim yopib qo‘ygan?", "Usmonlilar davlati", "Venetsiya", "Ispaniya", "Portugaliya", "Vizantiya qulagach, yo‘llar Usmonlilar tomonidan yopildi.")
t.B("Portugaliyaliklarning kashfiyotlari qaysi shahzoda nomi bilan bog‘liq?", "Genrix Dengizchi", "Vasko da Gama", "Bartolomeu Diash", "Magellan", "Muvaffaqiyatlar shahzoda Genrix Dengizchi nomi bilan bog‘liq.")
t.B("Afrika janubidagi burunni birinchi aylanib o‘tgan ekspeditsiya rahbari kim?", "Bartolomeu Diash", "Vasko da Gama", "Kolumb", "Torres", "XV asr oxirida B. Diash ekspeditsiyasi burunni aylanib o‘tdi.")
t.B("Kolumb ekspeditsiyasi Bagama orollariga qachon yetib kelgan?", "1492-yil 12-oktabrda", "1498-yilda", "1519-yilda", "1606-yilda", "1492-yil 12-oktabrda yetib keldi.")
t.B("Kolumb birinchi yetib kelgan orolni qanday atagan?", "San-Salvador", "Kuba", "Tasmaniya", "Madeyra", "«San-Salvador» («Muqaddas xaloskor») deb atadi.")
t.B("Yangi yerlar Hindiston emas, yangi materik ekanini kim isbotlagan?", "Amerigo Vespuchchi", "Kolumb", "Magellan", "Vasko da Gama", "Amerigo Vespuchchi isbotladi, materik uning sharafiga Amerika deb atala boshlandi.")
t.B("Vasko da Gamaga Hindistonga yetishda kim yordam bergan?", "arab dengizchisi Ahmad ibn Majid", "Kolumb", "Diash", "Genrix Dengizchi", "Arab dengizchisi Ahmad ibn Majid yordamida yetib keldi.")
t.B("Vasko da Gama Hindistonga qachon yetib kelgan?", "1498-yilda", "1492-yilda", "1497-yilda", "1522-yilda", "1498-yili Hindistonga yetib keldi.")
t.B("Magellan ekspeditsiyasi qachon yo‘lga chiqqan?", "1519-yilda", "1492-yilda", "1522-yilda", "1497-yilda", "1519-yili Magellan ekspeditsiyasi yo‘lga chiqdi.")
t.B("Magellan ekspeditsiyasi a’zolari Ispaniyaga qachon qaytib kelgan?", "1522-yilda", "1519-yilda", "1499-yilda", "1606-yilda", "1522-yili Ispaniya qirg‘oqlariga yetib keldi.")
t.B("Tinch okeaniga nomni kim bergan?", "Fernando Magellan", "Kolumb", "Abel Tasman", "Vespuchchi", "Sokin okeanni Magellan Tinch okeani deb atadi.")
t.B("1606-yilda Avstraliya qirg‘oqlariga kelib, uni Gollandiya mulki deb e’lon qilgan kim?", "Villem Yanszon", "Luis Torres", "Abel Tasman", "Magellan", "Gollandiyalik Villem Yanszon.")
t.B("Tasmaniya orolini kim kashf etgan?", "Abel Tasman", "Villem Yanszon", "Luis Torres", "Diash", "Abel Tasman Avstraliyani janubdan aylanib o‘tib, orolni kashf etdi.")
t.NAT("Magellan ekspeditsiyasi Yer sharini aylanib chiqdi.", "Yerning dumaloqligi amalda isbotlandi", "yangi savdo yo‘li faol ishlatildi", "Avstraliya kashf etildi", "Hindistonga yo‘l ochildi",
      "Yo‘l amaliy ahamiyatga ega bo‘lmasa-da, Yerning dumaloqligini isbotladi.")
t.NAT("Vasko da Gama ekspeditsiyasi muvaffaqiyatli qaytdi (1499).", "Hindistonga muntazam dengiz yo‘li ochildi", "Amerika kashf etildi", "Portugaliya qashshoqlashdi", "Usmonlilar yo‘lni ochdi",
      "Savdogarlar Sharqqa otlandi, Hindistonga muntazam dengiz yo‘li ochildi.")
t.NAT("Buyuk geografik kashfiyotlar amalga oshdi.", "asosiy savdo yo‘llari O‘rtayer dengizidan Atlantika okeaniga ko‘chdi", "O‘rtayer savdosi kuchaydi", "qul savdosi yo‘qoldi", "mustamlakalar tugatildi",
      "Savdo yo‘llari Atlantikaga ko‘chdi, jahon mustamlaka tizimi shakllandi.")
t.TF("Kolumb o‘zi kashf etgan yerlarni Hindiston deb hisoblagan.", True, "To‘g‘ri: shuning uchun aholini hindular deb atadi.")
t.TF("Magellan kashf etgan dengiz yo‘lidan keyin keng foydalanilgan.", False, "Noto‘g‘ri: undan uzoq vaqt hech kim foydalanmadi.")
t.MUL([("Portugaliyaliklar XV asrda Madeyra, Kanar va Azor orollarini kashf etgan.", True), ("Kashfiyotlarning eng salbiy oqibatlaridan biri qul savdosining rivojlanishi bo‘ldi.", True), ("Magellan ekspeditsiyadan sog‘-salomat qaytgan.", False)],
      "III noto‘g‘ri: Magellan halok bo‘lgan.")
t.MATCH("Sayyohlarni kashfiyotlari bilan moslashtiring.", ["Bartolomeu Diash", "Xristofor Kolumb", "Vasko da Gama", "Abel Tasman"],
        ["Yaxshi Umid burni", "Amerika", "Hindistonga dengiz yo‘li", "Tasmaniya", "Tinch okeani"], 'abcd', "Diash – Yaxshi Umid burni; Kolumb – Amerika; Gama – Hindiston; Tasman – Tasmaniya.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Kolumb Amerikani kashf etdi", "Vasko da Gama Hindistonga yetdi", "Magellan ekspeditsiyasi boshlandi", "Avstraliya kashf etildi"],
      "1492 → 1498 → 1519 → 1606.")
t.MAPMATCH(W, ['Bagama orollari', 'Yaxshi Umid burni', 'Kalkutta (Hindiston)', 'Avstraliya'],
           ["Kolumb 1492-yilda yetib kelgan orollar", "Diash aylanib o‘tgan burun", "Vasko da Gama yetib kelgan mamlakat", "1606-yilda kashf etilgan qit’a"],
           "1 – Bagama; 2 – Yaxshi Umid burni; 3 – Hindiston; 4 – Avstraliya.")
t.MAP1(EU, 'Portugaliya', "Atlantika bo‘ylab suzishni boshlab bergan, Genrix Dengizchi vatani bo‘lgan mamlakatni aniqlang.", "Portugaliya", ["Ispaniya", "Angliya", "Gollandiya"],
       "1 – Portugaliya.")
t.VENN("Kolumb", "Vasko da Gama",
       [("Ispaniya qiroli xizmatida suzgan", 1), ("Bagama orollariga yetib kelgan", 1),
        ("Afrikani janubdan aylanib o‘tgan", 2), ("Ahmad ibn Majid yordamida Hindistonga yetgan", 2),
        ("Hindistonga dengiz yo‘lini izlagan", 3)],
       "Kolumb: Ispaniya, Bagama. Gama: Afrika, Hindiston. Ikkalasi Hindistonga yo‘l izlagan.")

# 2 Industrial jamiyatning shakllanishi
t = Topic('e8j2', 802); TOPICS['e8j2'] = t
t.B("Narxlarning shiddat bilan o‘sishi jarayoni qanday atalgan?", "«narx-navo inqilobi»", "«sanoat inqilobi»", "«yer islohoti»", "«savdo urushi»", "Bu jarayon «narx-navo inqilobi» deb ataldi.")
t.B("Narxlar o‘sishiga asosiy sabab nima bo‘lgan?", "Amerikadan ko‘plab oltin-kumush keltirilishi", "urushlar", "hosilsizlik", "vabo", "Ko‘p oltin-kumush keltirilib, tangalar ko‘paydi.")
t.B("Mahsulotlarni e’lon qilib, shartnoma tuziladigan maxsus joy qanday atalgan?", "birja", "yarmarka", "gildiya", "manufaktura", "Yirik shaharlardagi bunday joy birja deb atalgan.")
t.B("Zamonaviy ko‘rinishdagi ilk bank qaysi?", "Genuyadagi Avliyo Georgiy banki", "London banki", "Antverpen banki", "Parij banki", "XV asrda Genuyadagi Avliyo Georgiy banki paydo bo‘ldi.")
t.B("O‘rta asrlarda banklar rolini nima bajargan?", "sarroflik do‘konlari", "gildiyalar", "monastirlar", "birjalar", "Banklar rolini pul maydalaydigan sarroflik do‘konlari bajargan.")
t.B("Kompaniya foydasidan ulush olish huquqini beruvchi qimmatbaho qog‘oz nima?", "aksiya", "veksel", "patent", "yorliq", "Bu qimmatbaho qog‘oz aksiya deb ataladi.")
t.B("Mashinalar qo‘llanilmagan, qo‘l mehnatiga asoslangan katta korxona nima deb ataladi?", "manufaktura", "fabrika", "sex", "birja", "Manufaktura – qo‘l mehnatiga asoslangan ishlab chiqarish.")
t.B("Dehqonlar uch dalali ekishdan qanday tizimga o‘tgan?", "ko‘p dalali ekishga", "ikki dalali ekishga", "lalmikorlikka", "ko‘chmanchilikka", "Dehqonlar ko‘p dalali ekishga o‘tdi.")
t.B("Unvon sotib olgan boy burjuaziya vakillari qanday atalgan?", "yangi zodagonlar", "gildiyachilar", "proletariat", "ritsarlar", "Bu qatlam yangi zodagonlar deb ataldi.")
t.B("Yollanma ishchilar qaysi sinfga birlashgan?", "proletariat", "burjuaziya", "zodagonlar", "dehqonlar", "Ular yollanma ishchilar – proletariat sinfiga birlashdi.")
t.B("XVI asr ikkinchi yarmidan Niderlanddagi asosiy savdo markazi qaysi shahar bo‘lgan?", "Antverpen", "London", "Genuya", "Lissabon", "Asosiy savdo markazi Antverpen bo‘lib qoldi.")
t.B("London qaysi daryo bo‘yida joylashgan?", "Temza", "Sena", "Reyn", "Tibr", "Temza daryosi bo‘yida joylashgan London tez rivojlandi.")
t.B("Savdogarlar va hunarmandlar uyushmasi nima deb ataladi?", "gildiya", "birja", "aksiya", "bank", "Gildiya – a’zolar manfaatini himoya qiluvchi uyushma.")
t.NAT("Yangi savdo yo‘llari ochildi.", "Lissabon va Sevilya jadal rivojlandi, Italiya shaharlari ahamiyatini yo‘qotdi", "Italiya shaharlari gullab-yashnadi", "Parij yopildi", "London qashshoqlashdi",
      "Lissabon va Sevilya rivojlandi, chetda qolgan Italiya shaharlari mavqeini yo‘qotdi.")
t.NAT("Bozorlarda raqobat kuchaydi.", "texnika va texnologiya jadal rivojlanib, mahsulot arzonlashdi", "narxlar keskin oshdi", "ixtirolar to‘xtadi", "savdo taqiqlandi",
      "Raqobat ixtirolarni ko‘paytirdi, mahsulot arzonlashdi.")
t.TF("Kishilar kapital va daromadiga qarab farqlanadigan jamiyat sinfiy jamiyat deb ataladi.", True, "To‘g‘ri.")
t.TF("XVI asrdagi diniy urushlar va vabo Parijning rivojlanishini tezlashtirgan.", False, "Noto‘g‘ri: rivojlanishni sekinlashtirgan.")
t.MUL([("Tadbirkor yollanma mehnatdan foydalanib, kapital yig‘gan.", True), ("Manufakturada mahsulot uning egasiga tegishli bo‘lgan.", True), ("Kapitalistik munosabatlar feodal munosabatlarni kuchaytirgan.", False)],
      "III noto‘g‘ri: ular feodal munosabatlarni siqib chiqardi.")
t.MATCH("Atamalarni izohi bilan moslashtiring.", ["Birja", "Aksiya", "Manufaktura", "Proletariat"],
        ["ulgurji savdo bitimlari joyi", "foydadan ulush beruvchi qog‘oz", "qo‘l mehnatiga asoslangan korxona", "yollanma ishchilar sinfi", "hunarmandlar uyushmasi"], 'abcd',
        "Birja – savdo; aksiya – qog‘oz; manufaktura – korxona; proletariat – ishchilar.")
t.MAPMATCH(EU, ['Lissabon', 'Genuya', 'Antverpen', 'London'],
           ["Hindiston tovarlari keltirilgan Portugaliya poytaxti", "ilk zamonaviy bank paydo bo‘lgan shahar", "XVI asr 2-yarmida Niderland savdo markazi", "keyinchalik Yevropaning asosiy savdo markazi"],
           "1 – Lissabon; 2 – Genuya; 3 – Antverpen; 4 – London.")
t.VENN("Burjuaziya", "Proletariat",
       [("ishlab chiqarish vositalariga ega", 1), ("yollanma mehnatdan foydalangan", 1),
        ("mulkdan mahrum, ish haqi olgan", 2), ("manufakturalarga yollangan", 2),
        ("yangi sinfiy jamiyat sinflari", 3)],
       "Burjuaziya – mulkdor; proletariat – yollanma ishchi. Ikkalasi yangi jamiyat sinflari.")

# 3 Reformatsiya
t = Topic('e8j3', 803); TOPICS['e8j3'] = t
t.B("Gunohlarni afv etganlik haqidagi Rim papasining yorlig‘i qanday atalgan?", "indulgensiya", "bulla", "tezis", "inkvizitsiya", "Indulgensiya – gunohlarni afv etish yorlig‘i.")
t.B("Cherkov marosimlari qaysi tilda o‘tkazilgan?", "lotin tilida", "nemis tilida", "yunon tilida", "fransuz tilida", "Marosimlar oddiy odamlar tushunmaydigan lotin tilida o‘tkazilgan.")
t.B("«Reforma» so‘zi qanday ma’noni bildiradi?", "islohot", "norozilik", "qayta tug‘ilish", "insoniy", "Reforma – islohot.")
t.B("Reformatsiya qachon boshlangan?", "1517-yilda", "1524-yilda", "1540-yilda", "1492-yilda", "Reformatsiya 1517-yilda boshlandi.")
t.B("«95 tezis»ning muallifi kim?", "Martin Lyuter", "Jan Kalvin", "Tomas Myunser", "Ignatiy Loyola", "Vittenberg universiteti professori Martin Lyuter.")
t.B("Papa Lyuterni qaysi shahar sudiga chaqirgan?", "Vorms", "Vittenberg", "Rim", "Jeneva", "Papa Lyuterni Vorms shahar sudiga chaqirdi.")
t.B("Germaniyadagi dehqonlar qo‘zg‘oloni qachon boshlangan?", "1524-yil yozida", "1517-yilda", "1526-yilda", "1540-yilda", "Qo‘zg‘olon 1524-yil yozida boshlandi.")
t.B("Xalq Reformatsiyasi deb atalgan qo‘zg‘olonga kim boshchilik qilgan?", "Tomas Myunser", "Martin Lyuter", "Jan Kalvin", "Tomas Mor", "Ruhoniy Tomas Myunser boshchilik qildi.")
t.B("Dehqonlar qo‘zg‘oloni qachon mag‘lubiyatga uchragan?", "1526-yil boshida", "1524-yil oxirida", "1530-yilda", "1517-yilda", "Qo‘zg‘olon 1526-yil boshida mag‘lub bo‘ldi.")
t.B("«Protest» so‘zi qanday ma’noni bildiradi?", "norozilik", "islohot", "insoniy", "qayta tiklanish", "Protest – norozilik.")
t.B("Jeneva shahrida protestantlikning yangi oqimiga kim asos solgan?", "Jan Kalvin", "Martin Lyuter", "Ignatiy Loyola", "Tomas Myunser", "Fransuz Jan Kalvin Jenevada asos soldi.")
t.B("Kalvin ta’limotining asosiy shiori qanday?", "«Duo o‘qi va ishla!»", "«Hamma uchun tenglik!»", "«Iso jamiyati»", "«Xudo bilan!»", "«Duo o‘qi va ishla!» shiori.")
t.B("«Iso jamiyati» (iyezuitlar ordeni) qachon ta’sis etilgan?", "1540-yilda", "1517-yilda", "1526-yilda", "1600-yilda", "Rim papasi 1540-yilda iyezuitlar ordenini ta’sis etdi.")
t.B("Iyezuitlar ordenining asoschisi kim?", "Ignatiy Loyola", "Jan Kalvin", "Lyuter", "Tomas Mor", "Ispan zodagoni Ignatiy Loyola.")
t.B("Katolik cherkovining protestantlarga qarshi tadbirlari qanday nom olgan?", "kontrreformatsiya", "renessans", "gumanizm", "inkvizitsiya", "Ular tarixda kontrreformatsiya nomini oldi.")
t.NAT("Katolik reyxstag Reformatsiya yutuqlarini bekor qilmoqchi bo‘ldi.", "Lyuter tarafdorlari norozilik bildirib, protestantlar deb atala boshladi", "lyuteranlar katoliklikka qaytdi", "Lyuter qatl etildi", "Germaniya birlashdi",
      "Norozilik bildirganlar protestantlar deb atala boshlandi.")
t.NAT("Protestantlikda Injilni mustaqil o‘qish talab qilindi.", "kishilar savodli bo‘lishga undaldi, savodxonlik oshdi", "savodxonlik pasaydi", "Injil taqiqlandi", "lotin tili kuchaydi",
      "Injilni mustaqil o‘qish ehtiyoji savodxonlikni oshirdi.")
t.TF("Lyuter Vorms sudida o‘z g‘oyalaridan voz kechgan.", False, "Noto‘g‘ri: u papaga bo‘ysunishdan bosh tortib, yorqin nutq so‘zladi.")
t.TF("Reformatsiya natijasida ko‘p mamlakatlarda milliy cherkovlar tashkil qilingan.", True, "To‘g‘ri.")
t.MUL([("Lyuter tarafdorlari lyuteranlar deb atalgan.", True), ("Papa dindan qaytganlarni jazolashni inkvizitsiya sudiga topshirgan.", True), ("Kalvin ta’limoti burjuaziyaga yoqmagan.", False)],
      "III noto‘g‘ri: boylik orttirishni maqsad qilgan burjuaziyaga ma’qul kelgan.")
t.MATCH("Shaxslarni faoliyati bilan moslashtiring.", ["Martin Lyuter", "Tomas Myunser", "Jan Kalvin", "Ignatiy Loyola"],
        ["«95 tezis» muallifi", "dehqonlar qo‘zg‘oloni rahbari", "Jenevadagi protestant oqimi asoschisi", "iyezuitlar ordeni asoschisi", "«Utopiya» muallifi"], 'abcd',
        "Lyuter – tezislar; Myunser – qo‘zg‘olon; Kalvin – Jeneva; Loyola – iyezuitlar.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["«95 tezis» e’lon qilindi", "Dehqonlar qo‘zg‘oloni boshlandi", "Qo‘zg‘olon mag‘lub bo‘ldi", "Iyezuitlar ordeni ta’sis etildi"],
      "1517 → 1524 → 1526 → 1540.")
t.MAPMATCH(EU, ['Vittenberg', 'Vorms', 'Jeneva', 'Rim'],
           ["Lyuter professor bo‘lgan universitet shahri", "Lyuter sudga chaqirilgan shahar", "Kalvin ta’limoti vujudga kelgan shahar", "Rim papasi qarorgohi"],
           "1 – Vittenberg; 2 – Vorms; 3 – Jeneva; 4 – Rim.")
t.VENN("Lyuteranlik", "Kalvinizm",
       [("Vittenberg professori asos solgan", 1), ("Germaniyada boshlangan", 1),
        ("Jenevada vujudga kelgan", 2), ("«Duo o‘qi va ishla!» shiori", 2),
        ("protestantlik oqimi", 3)],
       "Lyuteranlik – Germaniya; kalvinizm – Jeneva. Ikkalasi protestantlik.")

# 4 Yangi davr madaniyati
t = Topic('e8j4', 804); TOPICS['e8j4'] = t
t.B("Antik madaniyatning qayta tiklanish jarayoni qanday nom olgan?", "Renessans (Uyg‘onish)", "Reformatsiya", "Ma’rifat", "Gumanizm", "Bu jarayon Renessans – Uyg‘onish nomini oldi.")
t.B("Gumanizm dastlab qayerda paydo bo‘lgan?", "Italiyada (XIV asr o‘rtalari)", "Angliyada", "Germaniyada", "Fransiyada", "Gumanizm XIV asr o‘rtalarida Italiyada paydo bo‘ldi.")
t.B("«Utopiya» asarining muallifi kim?", "Tomas Mor", "Shekspir", "Servantes", "Jon Lokk", "Angliya qirolining birinchi vaziri Tomas Mor.")
t.B("«Utopiya» so‘zi qanday ma’noni bildiradi?", "«mavjud bo‘lmagan yer»", "«ideal shahar»", "«insoniy»", "«qayta tug‘ilish»", "Utopiya – «mavjud bo‘lmagan yer».")
t.B("«Hamlet», «Otello» asarlarining muallifi kim?", "Uilyam Shekspir", "Migel de Servantes", "Tomas Mor", "Rafael", "Shekspir mashhur tragediyalar muallifi.")
t.B("«Don Kixot» asarining muallifi kim?", "Migel de Servantes", "Shekspir", "Leonardo da Vinchi", "Jordano Bruno", "Ispan yozuvchisi Servantes.")
t.B("«Mona Liza» («Jokonda») asarining muallifi kim?", "Leonardo da Vinchi", "Rafael Santi", "Mikelanjelo", "Rembrandt", "«Mona Liza» – Leonardo da Vinchi asari.")
t.B("«Sikstin madonnasi» asarining muallifi kim?", "Rafael Santi", "Leonardo da Vinchi", "Rembrandt", "Mikelanjelo", "Rafael Santining eng mashhur asari.")
t.B("«Adashgan o‘g‘ilning qaytishi» rasmini kim chizgan?", "Rembrandt", "Rafael", "Leonardo", "Mikelanjelo", "Rembrandtning eng mashhur asari.")
t.B("«David» haykalining muallifi kim?", "Mikelanjelo Buonarroti", "Leonardo da Vinchi", "Rafael", "Rembrandt", "Mikelanjelo yaratgan «David» haykali.")
t.B("Yer Quyosh atrofida aylanadi, degan xulosaga kelgan polyak astronomi kim?", "Nikolay Kopernik", "Galileo Galiley", "Jordano Bruno", "Nyuton", "Kopernik 30 yil kuzatib shu xulosaga keldi.")
t.B("Olamning cheksizligi g‘oyasi uchun gulxanda yoqishga hukm qilingan olim kim?", "Jordano Bruno", "Galiley", "Kopernik", "Lyuter", "Jordano Bruno cherkov tomonidan gulxanda yoqishga hukm qilindi.")
t.B("Yevropada osmon jismlarini birinchi bo‘lib teleskopda kuzatgan olim kim?", "Galileo Galiley", "Kopernik", "Nyuton", "Bruno", "Galiley birinchi bo‘lib teleskop bilan kuzatdi.")
t.B("Butun olam tortishish qonunini kim ishlab chiqqan?", "Isaak Nyuton", "Galiley", "Jon Lokk", "Kopernik", "Nyuton butun olam tortishish qonunini yaratdi.")
t.B("Insonning tabiiy huquqlari haqidagi ta’limotni kim yaratgan?", "Jon Lokk", "Nyuton", "Tomas Mor", "Shekspir", "Jon Lokk yashash, erkinlik va mulk huquqlari ta’limotini yaratdi.")
t.NAT("Uyg‘onish davrida fan va san’at diniy taqiqdan chiqdi.", "bilim va erkin fikr rivojlandi, olamga dunyoviy qarash kuchaydi", "cherkov ta’siri kuchaydi", "lotin tili yagona tilga aylandi", "san’at taqiqlandi",
      "Gumanizm olamga insoniy qarashni kuchaytirdi.")
t.TF("Leonardo da Vinchi rasm chizishni «san’atlar malikasi» deb atagan.", True, "To‘g‘ri.")
t.TF("Rafael Santi uzoq umr ko‘rib, 80 yoshdan oshgan.", False, "Noto‘g‘ri: u atigi 37 yil umr ko‘rgan.")
t.MUL([("Jon Lokk «hokimiyatni bo‘lish» ta’limotini ishlab chiqqan.", True), ("Nyuton ko‘zguli teleskopni kashf qilgan.", True), ("Galiley geliotsentrik nazariyani rad etgan.", False)],
      "III noto‘g‘ri: Galiley Kopernik ta’limotini davom ettirib, geliotsentrik nazariyaga asos solgan.")
t.MATCH("Asarlarni mualliflari bilan moslashtiring.", ["«Hamlet»", "«Don Kixot»", "«Mona Liza»", "«David»"],
        ["Shekspir", "Servantes", "Leonardo da Vinchi", "Mikelanjelo", "Rafael"], 'abcd', "Hamlet – Shekspir; Don Kixot – Servantes; Mona Liza – Leonardo; David – Mikelanjelo.")
t.MATCH("Olimlarni mamlakatlari bilan moslashtiring.", ["Kopernik", "Galiley", "Nyuton"], ["Polsha", "Italiya", "Angliya", "Ispaniya"], 'abc',
        "Kopernik – polyak; Galiley – italiyalik; Nyuton – ingliz.")
t.MAPMATCH(EU, ['Italiya', 'Angliya', 'Ispaniya', 'Polsha'],
           ["Leonardo, Rafael va Mikelanjelo vatani", "Shekspir va Nyuton vatani", "Servantes vatani", "Kopernik vatani"],
           "1 – Italiya; 2 – Angliya; 3 – Ispaniya; 4 – Polsha.")
t.CHR("Olimlarni tug‘ilgan yili bo‘yicha joylashtiring.", ["Nikolay Kopernik", "Jordano Bruno", "Galileo Galiley", "Isaak Nyuton"], "1473 → 1548 → 1564 → 1643.")
t.VENN("Kopernik", "Galiley",
       [("polyak astronomi", 1), ("30 yil osmon jismlarini kuzatgan", 1),
        ("teleskop bilan birinchi kuzatgan", 2), ("italiyalik olim", 2),
        ("Yer Quyosh atrofida aylanishini asoslagan", 3)],
       "Kopernik: polyak, 30 yil. Galiley: teleskop, italiyalik. Ikkalasi geliotsentrik qarash tarafdori.")
