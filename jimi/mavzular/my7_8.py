from qlib import Topic, PLACES, REG
TOPICS = {}
EU = 'europe'

# 17 Xristian olamidagi o‘zgarishlar
t = Topic('y7j17', 7017); TOPICS['y7j17'] = t
t.B("Xristian dini german qabilalari orasida qachondan tarqala boshlagan?", "IV asrdan", "VII asrdan", "X asrdan", "I asrdan", "IV asrdan.")
t.B("Kiyev Rusi va Bolgariya qachon pravoslav mazhabini qabul qilgan?", "X asr oxirlarida", "V asr oxirida", "1054-yilda", "XII asrda", "X asr oxirlarida Vizantiyadan.")
t.B("Papa viloyati qachon tashkil topgan?", "756-yilda", "1054-yilda", "496-yilda", "1198-yilda", "756-yil Frank qiroli ko‘magida.")
t.B("Vizantiya cherkovini kim boshqargan?", "Konstantinopol patriarxi", "Rim papasi", "imperator", "arxiyepiskop", "Konstantinopol patriarxi.")
t.B("Cherkovning katolik va pravoslav cherkovlariga bo‘linishiga nima sabab bo‘lgan?", "bolgarlarni xristianlikka o‘tkazishdagi raqobat", "salib yurishlari", "inkvizitsiyaning tuzilishi", "Xlodvigning cho‘qinishi", "Sharqiy Yevropada bolgarlarni o‘tkazishdagi raqobat.")
t.B("Rim-katolik va yunon-pravoslav cherkovlari qachondan mustaqil faoliyat yuritadi?", "1054-yildan", "756-yildan", "988-yildan", "1198-yildan", "1054-yildan.")
t.B("«Katolik» so‘zi qanday ma’noni anglatadi?", "«jahon»", "«sof din»", "«afv»", "«qidiruv»", "Katolik – «jahon».")
t.B("«Pravoslav» so‘zi qanday ma’noni anglatadi?", "«sof din», «chin e’tiqod»", "«jahon»", "«dahriy»", "«qidiruv»", "Pravoslav – «sof din», «chin e’tiqod».")
t.B("Katolik cherkovida ruhoniylarning uylanishini taqiqlash qanday atalgan?", "selebat", "interdikt", "indulgensiya", "autodafe", "Selebat.")
t.B("Ekinzorlarning qancha qismi ibodatxona va monastirlar qo‘lida to‘plangan?", "uchdan bir qismi", "yarmi", "o‘ndan bir qismi", "to‘rtdan bir qismi", "Uchdan bir qismi.")
t.B("Cherkov aholidan undiradigan hosilning 1/10 qismi qanday soliq bo‘lgan?", "ushr", "jizya", "«qalqon puli»", "«daniyaliklar puli»", "Ushr.")
t.B("Gunohlarni kechish uchun pulga sotilgan yorliqlar qanday atalgan?", "indulgensiya", "interdikt", "selebat", "autodafe", "Indulgensiya (lotincha «afv»).")
t.B("Cherkov qo‘llagan eng og‘ir jazo – ibodatlarni vaqtincha taqiqlash qanday atalgan?", "interdikt", "inkvizitsiya", "indulgensiya", "selebat", "Interdikt.")
t.B("Qaysi papa davrida katolik cherkovi qudrat cho‘qqisiga chiqqan?", "Innokentiy III", "Grigoriy IX", "Urban II", "Lev III", "Innokentiy III (1198–1216).")
t.B("Cherkov ta’limotiga qarshi kishilar qanday atalgan?", "yeretiklar", "inkvizitorlar", "rohiblar", "salibchilar", "Yeretiklar (yunoncha – «dahriylar»).")
t.B("Inkvizitsiya qaysi papa davrida ayniqsa avj olgan?", "Grigoriy IX", "Innokentiy III", "Urban II", "Silvester II", "Grigoriy IX (1227–1241).")
t.B("«Inkvizitsiya» so‘zi lotinchada qanday ma’noni anglatadi?", "«qidiruv»", "«afv»", "«e’tiqod»", "«jahon»", "«Qidiruv».")
t.B("Mahkumlarni gulxanda yondirish qanday atalgan?", "autodafe", "interdikt", "indulgensiya", "selebat", "Autodafe (portugalcha – «din ishi»).")
t.NAT("Rim imperiyasi G‘arbiy va Sharqiy Rimga ajraldi.", "cherkov ham bo‘linib ketdi", "cherkov yagona bo‘lib mustahkamlandi", "xristianlik taqiqlandi", "Papa viloyati yo‘qoldi", "Imperiyaning bo‘linishi cherkovning bo‘linishiga olib keldi.")
t.NAT("Katolik cherkovi katta boyliklarni qo‘lga kiritdi.", "«sof xristianlar» – yeretiklar cherkov boyliklari va hashamatiga qarshi chiqdi", "aholi cherkovni yanada qo‘llab-quvvatladi", "papa boylikdan voz kechdi", "salib yurishlari to‘xtadi", "Yeretiklar sodda cherkov g‘oyasini ilgari surdi.")
t.NAT("Ko‘plab shaharliklar, dehqonlar va ritsarlar katolik cherkovini tark etdi.", "yeretiklarga qarshi kurash uchun cherkov sudi – inkvizitsiya tuzildi", "papa yeretiklarga yon berdi", "cherkov yer-mulkini dehqonlarga berdi", "selebat bekor qilindi", "Inkvizitsiya tuzildi.")
t.NAT("Papa Innokentiy III qirollarga interdikt qo‘lladi.", "german, fransuz va ingliz hukmdorlari tavba-tazarru qildi", "qirollar papani taxtdan tushirdi", "katolik cherkovi parchalandi", "interdikt bekor qilindi", "Papa hukmdorlarni tavba qildirdi.")
t.TF("Pravoslavlarda faqat rohiblar oila qurmagan.", True, "To‘g‘ri.")
t.TF("Sharqiy cherkovda va’zlar lotin tilida olib borilgan.", False, "Noto‘g‘ri: g‘arbda lotincha, sharqda yunon tilida.")
t.TF4([("Cherkov yerlari davlat soliqlaridan ozod etilgan.", True), ("Inkvizitsiya faoliyati Ispaniyada ayniqsa keng tus olgan.", True),
       ("Yeretiklar ruhoniylarsiz xudoga murojaat qilib bo‘lmaydi deb hisoblagan.", False), ("Cherkov daromadining ancha qismi papa xazinasiga yuborilgan.", True)],
      "3-noto‘g‘ri: yeretiklar ruhoniylar kerak emas, har kim xudoga o‘zi murojaat qilishi mumkin deb e’lon qilgan.")
t.MUL([("Angliya va Irlandiya rohiblari Yevropaning chekka joylarida xristianlikni targ‘ib qilgan.", True),
       ("Cherkov sud vazifasini ham bajargan.", True),
       ("Ikkita guvoh yeretik deb e’tirof etgan kishi darhol oqlangan.", False)],
      "III noto‘g‘ri: u inkvizitsiya sudiga chaqirilib, zindonga tashlangan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Papa viloyati tashkil topdi", "Cherkovlar rasman bo‘lindi", "Innokentiy III papa bo‘ldi", "Grigoriy IX papa bo‘ldi"],
      "756 → 1054 → 1198 → 1227.")
t.MATCH("Atamalarni ma’nolari bilan moslashtiring.", ["indulgensiya", "interdikt", "inkvizitsiya", "autodafe"],
        ["gunohlarni kechish yorlig‘i", "ibodat va marosimlarni vaqtincha taqiqlash", "yeretiklarni qidiruvchi cherkov sudi", "mahkumni gulxanda yondirish", "ruhoniylarga uylanishni taqiqlash"], 'abcd',
        "Indulgensiya – afv; interdikt – taqiq; inkvizitsiya – sud; autodafe – yondirish.")
t.VENN("Katolik cherkovi", "Pravoslav cherkovi",
       [("Rim papasi boshqargan", 1), ("barcha ruhoniylarga selebat", 1),
        ("Konstantinopol patriarxi boshqargan", 2), ("va’zlar yunon tilida", 2),
        ("1054-yildan mustaqil xristian cherkovi", 3)],
       "Katolik – papa, selebat; pravoslav – patriarx, yunoncha; ikkalasi 1054-yildan mustaqil.")
t.MAPMATCH(EU, ['Rim', 'Konstantinopol', 'Ispaniya', 'Kiyev'],
           ["papalar davlati joylashgan shahar", "pravoslav cherkovi patriarxi qarorgohi", "inkvizitsiya faoliyati ayniqsa keng tus olgan mamlakat", "X asr oxirida Vizantiyadan pravoslavlikni qabul qilgan Rus markazi"],
           "1 – Rim; 2 – Konstantinopol; 3 – Ispaniya; 4 – Kiyev.")

# 18 Salib yurishlari
t = Topic('y7j18', 7018); TOPICS['y7j18'] = t
t.B("Salib yurishlari qaysi yillar oralig‘ida bo‘lgan?", "1096–1270-yillarda", "1054–1204-yillarda", "1189–1192-yillarda", "1000–1100-yillarda", "1096–1270-yillar.")
t.B("XI asr oxirida Kichik Osiyo kimlar qo‘lida edi?", "saljuqiy turklar", "arablar", "mo‘g‘ullar", "vizantiyaliklar", "Saljuqiy turklar qo‘lida.")
t.B("Papa Urban II salib yurishiga qaysi shaharda chaqirgan?", "Klermon", "Rim", "Venetsiya", "Parij", "1095-yilda Klermon shahrida.")
t.B("Urban II qachon nutq so‘zlagan?", "1095-yilda", "1096-yilda", "1099-yilda", "1187-yilda", "1095-yilda.")
t.B("Meros faqat katta o‘g‘ilga qoldirilish tizimi qanday atalgan?", "mayorat", "benefitsiy", "selebat", "patta", "Mayorat tizimi.")
t.B("Konstantinopolda salibchilardan vassallik qasamyodini qabul qilgan imperator kim?", "Aleksey I", "Isaak II Angel", "Yustinian I", "Irakliy I", "Imperator Aleksey I.")
t.B("Birinchi salib yurishi natijasida tuzilgan asosiy salibchilar davlati qaysi?", "Quddus qirolligi", "Lotin imperiyasi", "Edessa grafligi", "Antioxiya knyazligi", "Quddus qirolligi.")
t.B("Dastlabki diniy-ritsarlik ordeni qaysi?", "gospitalyerlar", "tampliyerlar", "tevtonlar", "dominikanlar", "Gospitalyerlar (ioanniylar) ordeni.")
t.B("Ko‘pchilik ritsarlari Germaniyadan bo‘lgan orden qanday atalgan?", "Tevton (Nemis) ordeni", "tampliyerlar", "gospitalyerlar", "ioanniylar", "Tevton ordeni.")
t.B("Nuriddin Zangiy qachon taxtga o‘tirgan?", "1146-yilda", "1155-yilda", "1169-yilda", "1187-yilda", "1146-yilda.")
t.B("Ikkinchi salib yurishi qaysi yillarda bo‘lgan?", "1147–1149-yillarda", "1096–1099-yillarda", "1189–1192-yillarda", "1269–1270-yillarda", "1147–1149-yillarda.")
t.B("Nuriddin Zangiy qo‘shini Damashqni qachon egallagan?", "1155-yilda", "1146-yilda", "1169-yilda", "1187-yilda", "1155-yilda.")
t.B("Salohiddin Misrda qaysi davlatni tuzgan?", "Ayyubiylar davlatini", "Zangiylar davlatini", "Saljuqiylar davlatini", "Mamluklar davlatini", "Ayyubiylar davlatini.")
t.B("Salohiddin Ayyubiy Quddusni qachon salibchilardan tortib olgan?", "1187-yilda", "1169-yilda", "1099-yilda", "1192-yilda", "1187-yilda.")
t.B("Uchinchi salib yurishi qaysi yillarda bo‘lgan?", "1189–1192-yillarda", "1147–1149-yillarda", "1096–1099-yillarda", "1202–1204-yillarda", "1189–1192-yillarda.")
t.B("To‘rtinchi salib yurishida salibchilar Venetsiyaga qancha to‘lashni zimmasiga olgan?", "85 ming kumush marka", "10 ming oltin", "1 mln marka", "100 ming dinor", "85 ming kumush marka.")
t.B("Vizantiya xarobalarida salibchilar qanday davlat tuzgan?", "Lotin imperiyasi", "Quddus qirolligi", "Muqaddas Rim imperiyasi", "Ayyubiylar davlati", "Lotin imperiyasi.")
t.B("So‘nggi – sakkizinchi salib yurishini kim boshlagan?", "Fransiya qiroli Lyudovik IX", "papa Urban II", "Aleksey I", "Innokentiy III", "1269–1270-yillarda Lyudovik IX.")
t.NAT("Salohiddin Ayyubiy 1187-yilda Quddusni tortib oldi.", "Yevropada uchinchi salib yurishi tashkil qilindi", "salibchilar Quddusni darhol qaytardi", "salib yurishlari tugadi", "Ayyubiylar davlati quladi", "1189–1192-yillardagi uchinchi salib yurishi boshlandi.")
t.NAT("Salibchilar Venetsiyaga kelishilgan pulning 1/3 qismini to‘lay olmadi.", "Venetsiyaning raqibi – Vizantiyaga qarshi urush boshlandi, Konstantinopol talandi", "yurish bekor qilindi", "Venetsiya salibchilarni qarzdan ozod qildi", "salibchilar Misrni egalladi", "To‘rtinchi yurishda Konstantinopol dushman o‘ljasiga aylandi.")
t.NAT("Salibchilar Yaqin Sharqda hosilning 1/3 qismini soliqqa oldi.", "mahalliy aholida nafrat kuchayib, qo‘zg‘olonlar bo‘lib turdi", "aholi salibchilarni qo‘llab-quvvatladi", "dehqonlar boyib ketdi", "musulmon amirliklari tarqaldi", "Mahalliy aholining nafrati kuchaydi.")
t.NAT("Salibchilar Sharq madaniyati bilan tanishdi.", "Yevropaga limon, o‘rik, sholi, shakarqamish va shamol tegirmonlari kirib keldi", "Yevropa Sharqdan butunlay uzildi", "Yevropada hammomlar yo‘qoldi", "arbalet unutildi", "Yevropaliklar turmush tarzi o‘zgardi.")
t.TF("Salib yurishlari Sharqda kuchli xristian davlatini yaratish maqsadiga erisha olmagan.", True, "To‘g‘ri.")
t.TF("Ikkinchi salib yurishi to‘liq g‘alaba bilan yakunlangan.", False, "Noto‘g‘ri: muvaffaqiyatsizlikka uchradi, Damashq egallanmadi.")
t.TF4([("Tampliyerlarda oq matoda qizil but tasvirlangan.", True), ("Gospitalyerlar ordeni keyinchalik Rodos, so‘ng Maltaga ko‘chgan.", True),
       ("Uchinchi salib yurishi to‘liq muvaffaqiyat bilan tugagan.", False), ("Tampliyerlar sudxo‘rlik bilan ham shug‘ullangan.", True)],
      "3-noto‘g‘ri: uchinchi salib yurishi ham muvaffaqiyatsiz tugagan.")
t.MUL([("Salib yurishlarida ayollar va bolalar ham qatnashgan.", True),
       ("Salibchilar Quddusni egallashda jome masjidda 10 ming musulmonni qirgan.", True),
       ("Nuriddin Zangiy 1169-yilda Misrni egallash uchun Lyudovik IX ni yuborgan.", False)],
      "III noto‘g‘ri: Shirkuh va uning jiyani Salohiddinni yuborgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Klermondagi nutq", "Birinchi salib yurishi yakunlandi", "Ikkinchi salib yurishi boshlandi", "Nuriddin Damashqni egalladi", "Misr egallandi", "Salohiddin Quddusni qaytarib oldi", "Sakkizinchi salib yurishi"],
      "1095 → 1099 → 1147 → 1155 → 1169 → 1187 → 1269.")
t.MATCH("Shaxslarni ularga oid ma’lumot bilan moslashtiring.", ["Urban II", "Aleksey I", "Salohiddin Ayyubiy", "Lyudovik IX"],
        ["Klermonda salib yurishiga chaqirgan", "salibchilardan vassallik qasamyodini olgan", "1187-yilda Quddusni qaytargan", "sakkizinchi salib yurishini boshlagan", "Lotin imperiyasini tuzgan"], 'abcd',
        "Urban II – Klermon; Aleksey I – qasamyod; Salohiddin – Quddus; Lyudovik IX – so‘nggi yurish.")
t.VENN("Tampliyerlar", "Gospitalyerlar",
       [("oq matoda qizil but", 1), ("sudxo‘rlik bilan ham shug‘ullangan", 1),
        ("qizil matoda oq but", 2), ("Rodosga, so‘ng Maltaga ko‘chgan", 2),
        ("Falastinda tuzilgan diniy-ritsarlik ordeni", 3)],
       "Tampliyerlar – oq/qizil, sudxo‘rlik; gospitalyerlar – qizil/oq, Malta; ikkalasi diniy-ritsarlik ordeni.")
t.MAPMATCH('crusade', ['Klermon', 'Venetsiya', 'Konstantinopol', 'Quddus'],
           ["1095-yilda Urban II nutq so‘zlagan shahar", "salibchilar kemalar uchun 85 ming kumush marka to‘lashga kelishgan shahar", "to‘rtinchi yurishda ilk bor dushman o‘ljasiga aylangan poytaxt", "1187-yilda Salohiddin qaytarib olgan shahar"],
           "1 – Klermon; 2 – Venetsiya; 3 – Konstantinopol; 4 – Quddus.")
