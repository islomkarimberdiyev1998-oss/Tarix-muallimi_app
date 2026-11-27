from qlib import Topic, PLACES, REG
TOPICS = {}
EU = 'europe'

# 19 Yevropa shaharlari
t = Topic('y7j19', 7019); TOPICS['y7j19'] = t
t.B("Yevropada ishlab chiqarish qachon yuksalgan?", "X–XI asrlarda", "V–VI asrlarda", "XIV–XV asrlarda", "VIII asrda", "X–XI asrlarda.")
t.B("Dehqonchilikda yer haydashni tezlashtirgan kashfiyot qaysi?", "bo‘yinturuq va plugni otga qo‘shish", "tosh bolta", "suzuvchi dalalar", "sug‘orish kanallari", "Bo‘yinturuqning kashf etilishi, plugni otga qo‘shish.")
t.B("Qaysi shaharlar IX–X asrlardayoq yuksala boshlagan?", "Venetsiya, Genuya, Florensiya", "London, Bristol, Bazel", "Lyubek, Novgorod, Riga", "Parij, Kyoln, Praga", "Italiya va janubiy Fransiyaning dengiz yo‘lidagi shaharlari.")
t.B("Vengriya, Boltiqbo‘yi, Rus yerlarida yangi shaharlar qachon vujudga kelgan?", "XII–XIII asrlarda", "IX–X asrlarda", "X–XI asrlarda", "VII–VIII asrlarda", "XII–XIII asrlarda.")
t.B("Shaharlar ko‘pincha kimlarning yerida vujudga kelgan?", "feodallar yerida", "davlat yerlarida", "cherkov yerlarida", "dehqon jamoalari yerida", "Ko‘pincha feodallar yerida.")
t.B("Shahar kengashi binosi qanday atalgan?", "ratusha", "sobor", "ark", "rabod", "Ratusha.")
t.B("Ma’lum kasb ustalarining uyushmasi qanday atalgan?", "sex", "gildiya ittifoqi", "Ganza", "faktoriya", "Sex.")
t.B("Sexni kim boshqargan?", "saylangan oqsoqol", "feodal", "qirol", "yepiskop", "Saylangan sex oqsoqoli.")
t.B("Xalfalik muddati qancha bo‘lgan?", "2–7 yil", "10–12 yil", "1 yil", "20 yil", "Kasb murakkabligiga qarab 2–7 yil.")
t.B("Germaniyaning 70 dan ortiq shaharlari qaysi ittifoqqa kirgan?", "Ganza shaharlar ittifoqi", "Lombardiya ittifoqi", "Uchlar ittifoqi", "Antanta", "Ganza shaharlar ittifoqi.")
t.B("Ispaniya, Italiya va janubiy Fransiyani Vizantiya va Osiyo bilan bog‘lagan dengiz yo‘li qanday atalgan?", "Levant", "Shimoliy savdo yo‘li", "Buyuk Ipak yo‘li", "Ganza yo‘li", "Levant.")
t.B("Italiyalik savdogarlarning savdo manzilgohlari qanday atalgan?", "faktoriyalar", "rastalar", "ratushalar", "sexlar", "Faktoriyalar.")
t.B("Marko Polo sayohati necha yil davom etgan?", "25 yil", "17 yil", "10 yil", "40 yil", "25 yil; 17 yilini Xubilay saroyida o‘tkazgan.")
t.B("Marko Polo kimning saroyida xizmat qilgan?", "Xubilay", "Chingizxon", "Botuxon", "Xuloku", "Mo‘g‘ullar xoni Xubilay saroyida.")
t.B("Marko Polo kitobidan 200 yil o‘tib taassurot olgan genuyalik dengizchi kim?", "Xristofor Kolumb", "Vasko da Gama", "Magellan", "Amerigo Vespuchchi", "Xristofor Kolumb.")
t.B("Aholisi eng ko‘p yirik Yevropa shahri qaysi?", "Parij", "Lyubek", "Bristol", "Bazel", "Parij, Konstantinopol, Milan, Florensiya, Kordova, Seviliya.")
t.NAT("Qishloqda feodallar hunarmand erkinligini chekladi.", "hunarmandlar qishloqlardan qochib, buyum sotish imkoni bo‘lgan joylarga ketdi va shaharlar paydo bo‘ldi", "hunarmandchilik yo‘qoldi", "feodallar shaharlarni taqiqladi", "hunarmandlar dehqonchilikka qaytdi", "Shaharlar vujudga keldi.")
t.NAT("Shaharlar o‘sib boyidi, feodallar ulardan ko‘proq daromad olishga intildi.", "shaharliklar to‘lov yoki qo‘zg‘olon orqali senyor hukmidan ozodlikka intildi", "shaharlar feodallarga to‘liq bo‘ysundi", "savdo to‘xtadi", "shaharlar yopildi", "Shaharlar erkinlik uchun kurashdi.")
t.NAT("Shaharlarda aholi zich yashadi, ko‘chalar tor va tozalik talabga javob bermadi.", "yuqumli kasalliklar tez-tez takrorlanib, ko‘plab kishilar bevaqt o‘ldi", "aholi sog‘lom yashadi", "shaharlar kengaydi", "suv quvurlari qurildi", "Yuqumli kasalliklar ko‘paydi.")
t.NAT("Hunarmandlar xalfalarning ustalikka o‘tishiga to‘sqinlik qildi.", "xalfalar «birodarlik» jamiyatlarini tuzib, huquqlari uchun kurashdi", "xalfalar sexlarni boshqardi", "sexlar tugatildi", "ish vaqti qisqardi", "Birodarlik jamiyatlari tuzildi.")
t.TF("Sexlarning o‘z gerbi, bayrog‘i va ibodatxonasi bo‘lgan.", True, "To‘g‘ri.")
t.TF("O‘rta asr Yevropa shaharlarida ko‘chalar tunda yoritilgan, kanalizatsiya mavjud bo‘lgan.", False, "Noto‘g‘ri: ko‘chalar yoritilmagan, suv quvurlari va kanalizatsiya bo‘lmagan.")
t.TF4([("Sex nizomida ustaning dastgohlari va shogirdlari soni belgilangan.", True), ("Tayyor buyumlar narxini sex oqsoqoli belgilagan.", True),
       ("Venetsiya va Genuya o‘rtasida savdoda raqobat bo‘lmagan.", False), ("Fransiyada qirol farmoni bilan yo‘llarga tosh yotqizila boshlangan.", True)],
      "3-noto‘g‘ri: Venetsiya va Genuya raqobati ba’zida urushlarga aylangan.")
t.MUL([("Ilk o‘rta asrlardagi natural xo‘jalik o‘rnini tovar xo‘jaligi egalladi.", True),
       ("Yevropada hunarmandchilik va savdoning yuksalishi bozor, bank, birjalarni vujudga keltirdi.", True),
       ("Yevropa shaharlaridagi uylarning aksariyati marmar va pishiq g‘ishtdan qurilgan.", False)],
      "III noto‘g‘ri: uylarning aksariyati yog‘ochdan qurilgan.")
t.CHR("Jarayonlarni xronologik ketma-ketlikda joylashtiring.", ["Italiya va janubiy Fransiya shaharlari yuksala boshladi", "Fransiya shimoli, Angliya, Germaniyada shaharlar vujudga keldi", "Vengriya, Boltiqbo‘yi, Rus yerlarida shaharlar vujudga keldi", "Pololar oilasi mo‘g‘ullar qarorgohiga yetib bordi"],
      "IX–X → X–XI → XII–XIII → XIII asr.")
t.VENN("Levant yo‘li", "Shimoliy savdo yo‘li",
       [("Venetsiya va Genuya shaharlari", 1), ("Vizantiya va Osiyo bilan bog‘lagan", 1),
        ("Boltiq dengizi orqali o‘tgan", 2), ("Ganza shaharlar ittifoqi", 2),
        ("Yevropaning dengiz savdo yo‘li", 3)],
       "Levant – Venetsiya, Genuya; Shimoliy – Boltiq, Ganza; ikkalasi dengiz savdo yo‘li.")
t.MAPMATCH(EU, ['Venetsiya', 'Marsel', 'Lyubek', 'Novgorod'],
           ["Pololar oilasi chiqqan dengiz respublikasi", "IX–X asrlarda yuksalgan janubiy Fransiya port shahri", "Ganza ittifoqiga kirgan, Shimoliy yo‘ldagi German shahri", "Shimoliy savdo yo‘li orqali Londonga bog‘langan Rus shahri"],
           "1 – Venetsiya; 2 – Marsel; 3 – Lyubek; 4 – Novgorod.")

# 20 Osiyo shaharlari
t = Topic('y7j20', 7020); TOPICS['y7j20'] = t
t.B("O‘rta asr Osiyo shaharlari dastlab qanday tashkil topgan?", "ma’muriy markaz yoki harbiy qal’alar sifatida", "feodallar yerida", "monastirlar atrofida", "savdo faktoriyalari sifatida", "Ma’muriy markaz yoki harbiy qal’alar sifatida.")
t.B("Osiyo shaharlari nima uchun yirik zamindorlarga qarshi kurash olib bormagan?", "davlat yerlarida vujudga kelgani uchun", "feodallar bo‘lmagani uchun", "aholisi kam bo‘lgani uchun", "qirollar taqiqlagani uchun", "Davlat yerlarida vujudga kelgan.")
t.B("Xitoyda o‘rta asrlar shaharlarining rivojlanishi qaysi asrlarga to‘g‘ri keladi?", "IX–XIII asrlarga", "V–VII asrlarga", "XIV–XV asrlarga", "I–III asrlarga", "IX–XIII asrlarga.")
t.B("Yaponiyaning Xeyyan shahri qachon yong‘in natijasida vayron bo‘lgan?", "1177-yilda", "1231-yilda", "918-yilda", "1279-yilda", "1177-yilda.")
t.B("Xeyyan qayta tiklangach qanday nom olgan?", "Kioto", "Nara", "Kamakura", "Osaka", "Kioto; mamlakat poytaxti.")
t.B("Xitoyda yog‘och tanqis bo‘lganidan qurilishda nimalardan keng foydalanilgan?", "g‘isht, sopol va tosh", "faqat yog‘och", "loy va qamish", "temir", "G‘isht, sopol va toshdan.")
t.B("Xitoy shaharlarida aholi toza suv bilan qanday ta’minlangan?", "sopol quvurlar orqali", "quduqlar orqali", "suv tashuvchilar orqali", "yomg‘ir suvi bilan", "Sopol quvurlar orqali.")
t.B("O‘rta Osiyo shaharlarining markazidagi shahar hokimi qal’asi qanday atalgan?", "ark", "rabod", "shahriston", "ratusha", "Ark.")
t.B("O‘rta Osiyo shaharlarida asosiy aholi yashagan qism qanday atalgan?", "shahriston", "ark", "rabod", "rasta", "Shahriston.")
t.B("Hunarmandlar guzar va mahallalari joylashgan shahar atrofi qanday atalgan?", "rabod", "ark", "shahriston", "faktoriya", "Rabod.")
t.B("Xitoyliklar qurgan 600–700 kishi sig‘adigan yirik kemalar qanday atalgan?", "jonkalar", "drakkarlar", "galeralar", "karavellalar", "Jonkalar.")
t.B("Chet ellik savdogarlar qaysi shahar qog‘ozini yuqori baholagan?", "Samarqand", "Buxoro", "Marv", "Bag‘dod", "Samarqand qog‘ozi.")
t.B("Qaysi shahar kulolchilik buyumlari bilan mashhur bo‘lgan?", "G‘ijduvon", "Marv", "Samarqand", "Kioto", "G‘ijduvon kulolchiligi.")
t.B("O‘rta Osiyo va Erondagi yirik bozorlar nimalarga bo‘lingan?", "rastalarga", "sexlarga", "faktoriyalarga", "dahalarga", "Rastalarga.")
t.B("Ilk o‘rta asrlarda qaysi shaharlarda mardikorlar bozori bo‘lgan?", "Bag‘dod, Ishbiliya, G‘arnota", "Buxoro, Samarqand, Marv", "Kioto, Nara, Osaka", "Chanan, Loyan, Xanchjou", "Bag‘dod, Ishbiliya va G‘arnota.")
t.B("Yaponiyaning qaysi shahri qal’a yaqinida qurilgan?", "Nagoya", "Nara", "Otsu", "Xyogo", "Nagoya.")
t.NAT("Hindiston shaharlari ko‘p marotaba chet el bosqinchilari hujumiga uchradi.", "shaharlarning taraqqiyotiga to‘sqinlik qilindi", "shaharlar tez rivojlandi", "Hindiston shaharlari yo‘qoldi", "bosqinchilar shaharlarni tikladi", "Istilochilik urushlari taraqqiyotga to‘sqinlik qilgan.")
t.NAT("Arab xalifaligi, Tan imperiyasi kabi markazlashgan davlatlar paydo bo‘ldi.", "savdo yuqori daromad manbaiga aylandi", "savdo to‘xtab qoldi", "karvon yo‘llari yopildi", "shaharlar qisqardi", "Savdo yuqori daromad manbayiga aylandi.")
t.NAT("Afrika iqtisodiy qoloq bo‘lib, unda tinimsiz urushlar bo‘ldi.", "qit’a xomashyo, oltin, fil suyagi va qullar manbaiga aylandi", "Afrika savdo markaziga aylandi", "Afrika Osiyoni bosib oldi", "Afrikada yirik shaharlar ko‘paydi", "Xomashyo va qullar manbayiga aylandi.")
t.NAT("Buxoro islom, madaniyat, savdo va hunarmandchilik markazi sifatida shuhrat qozondi.", "O‘rta Osiyo sulolalari uni ma’muriy markaz sifatida tanladi", "Buxoro tashlab ketildi", "Buxoro Xitoyga qo‘shildi", "Buxoroda savdo taqiqlandi", "Sulolalar Buxoro va Samarqandni markaz qildi.")
t.TF("Xitoyda barcha ustalar sex a’zosi bo‘lishlari majburiy etib qo‘yilgan.", True, "To‘g‘ri.")
t.TF("Osiyo shaharlari aholisi Yevropanikiga nisbatan kamroq bo‘lgan.", False, "Noto‘g‘ri: Osiyo shaharlari aholisi ko‘proq bo‘lgan.")
t.TF4([("Arab xalifaligi, Yaponiya, Xitoyda soliqlarni sex oqsoqollari yig‘ib bergan.", True), ("Kioto ko‘p asrlar Yaponiyaning iqtisodiy, madaniy va diniy markazi bo‘lgan.", True),
       ("Kambag‘allar uylarini pishiq g‘isht va marmardan qurgan.", False), ("Fors ko‘rfazi va Qizil dengizda arab, hind, xitoy kemalari suzgan.", True)],
      "3-noto‘g‘ri: kambag‘allar uylarini paxsa va guvaladan qurgan.")
t.MUL([("Xitoy shaharlarida axlatni tozalash va o‘t o‘chirish ishlari yo‘lga qo‘yilgan.", True),
       ("Osiyo bozorlari ko‘pincha shahar darvozalari yaqinida joylashgan.", True),
       ("Sharqda shahar aholisi hech qachon soliqdan ozod qilinmagan.", False)],
      "III noto‘g‘ri: dastlab shahar aholisi soliqlardan ozod qilingan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Xitoyda o‘rta asr shaharlari rivojlana boshladi", "Xitoyda shaharsozlik yuksak darajaga ko‘tarildi", "Xeyyan yong‘inda vayron bo‘ldi"],
      "IX asr → XI asr → 1177.")
t.VENN("Yevropa shaharlari", "Osiyo shaharlari",
       [("feodallar yerida vujudga kelgan", 1), ("senyorlarga qarshi erkinlik uchun kurashgan", 1),
        ("davlat yerlarida vujudga kelgan", 2), ("Xitoyda sopol quvurli suv ta’minoti", 2),
        ("hunarmandchilik sexlari mavjud bo‘lgan", 3)],
       "Yevropa – feodal yeri, erkinlik kurashi; Osiyo – davlat yeri, sopol quvur; ikkalasida sexlar.")
t.MAPMATCH('eurasia2', ['Kioto', 'Xanchjou', 'Buxoro', 'Bag‘dod'],
           ["1177-yilgi yong‘indan so‘ng tiklanib, Yaponiya poytaxti bo‘lgan shahar", "Chanan va Loyan bilan birga Xitoyning yirik shahri", "Sharqda islom va madaniyat markazi sifatida shuhrat qozongan shahar", "Ishbiliya va G‘arnota kabi mardikorlar bozori bo‘lgan xalifalik shahri"],
           "1 – Kioto; 2 – Xanchjou; 3 – Buxoro; 4 – Bag‘dod.")
