from qlib import Topic, PLACES, REG
TOPICS = {}

# 10 Saljuqiylar davlati
t = Topic('y7j10', 7010); TOPICS['y7j10'] = t
t.B("Saljuqiylar qaysi turkiy qavm tarkibida bo‘lgan?", "o‘g‘uz", "qipchoq", "qarluq", "uyg‘ur", "Turkiy o‘g‘uz qavmi tarkibida.")
t.B("Saljuqiylar dastlab qayerda yashagan?", "Janubiy Qozog‘iston va Sirdaryoning o‘rta oqimida", "Kichik Osiyoda", "Xurosonda", "Mo‘g‘ulistonda", "Hozirgi Janubiy Qozog‘iston va Sirdaryoning o‘rta oqimida.")
t.B("O‘g‘uzlar kim boshchiligida islom dinini qabul qilgan?", "Saljuqbek", "To‘g‘rulbek", "Alp Arslon", "Malikshoh", "Saljuqbek boshchiligida.")
t.B("Saljuqiylar qachon Xuroson yerlariga ko‘chib o‘tgan?", "1025-yilda", "1038-yilda", "1055-yilda", "1071-yilda", "1025-yilda Mahmud G‘aznaviy roziligi bilan.")
t.B("Saljuqiylar davlatiga kim asos solgan?", "sulton To‘g‘rulbek", "Saljuqbek", "Chag‘ribek", "Nizomulmulk", "1038-yilda Saljuqning nabirasi To‘g‘rulbek.")
t.B("Saljuqiylar sulolasi qaysi yillarda hukmronlik qilgan?", "1038–1308-yillarda", "1025–1092-yillarda", "1055–1258-yillarda", "1071–1243-yillarda", "1038–1308-yillar.")
t.B("Bag‘dodda To‘g‘rulbek nomiga qachon xutba o‘qilgan?", "1055-yilda", "1038-yilda", "1071-yilda", "1074-yilda", "1055-yilda.")
t.B("Xalifa Al-Qoim To‘g‘rulbekni qanday deb tan olgan?", "sulton hamda «Sharq va G‘arb podshohi»", "xalifa", "amir ul-umaro", "beylarbeyi", "Sulton hamda «Sharq va G‘arb podshohi».")
t.B("Saljuqiylarning eng yuksalgan davri qaysi sulton hukmronligiga to‘g‘ri keladi?", "Malikshoh", "Alp Arslon", "To‘g‘rulbek", "Kaykubod", "Malikshoh (1072–1092).")
t.B("Malikshoh Buxoro va Samarqandni qachon egallagan?", "1074-yilda", "1055-yilda", "1072-yilda", "1092-yilda", "1074-yili.")
t.B("Mansikert jangi qachon bo‘lgan?", "1071-yilda", "1055-yilda", "1243-yilda", "1308-yilda", "1071-yilda saljuqiylar Vizantiyani yengdi.")
t.B("Anatoliyada o‘g‘uzlar qanday sultonlik tuzgan?", "Ko‘niya sultonligi", "Usmon beyligi", "Xulokuylar davlati", "Qurdoba amirligi", "Ko‘niya sultonligi.")
t.B("Ko‘niya sultonligining dastlabki markazi qaysi shahar bo‘lgan?", "Nikeya", "Ko‘niya", "Sivas", "Bursa", "Dastlab Nikeya, keyin Ko‘niya.")
t.B("Ko‘niya sultonligi qaysi sulton davrida yuqori cho‘qqiga chiqqan?", "Alouddin Kaykubod", "Malikshoh", "Alp Arslon", "Kayxusrav II", "Sulton Alouddin Kaykubod.")
t.B("Saljuqiylarning bosh vaziri qanday atalgan?", "«rais ur-ruaso»", "«vasilevs»", "«voliy»", "«no‘yon»", "Bosh vazir «rais ur-ruaso» deb atalgan.")
t.B("«Siyosatnoma» asarini kim yozgan?", "Nizomulmulk", "Malikshoh", "Alp Arslon", "To‘g‘rulbek", "Mashhur bosh vazir Nizomulmulk.")
t.NAT("1071-yilda Mansikert jangida saljuqiylar Vizantiyani yengdi.", "o‘g‘uz turklarining katta qismi Kichik Osiyoga ko‘chib kelib, o‘troqlasha boshladi", "Vizantiya Kichik Osiyoni qaytarib oldi", "saljuqiylar Xurosondan haydaldi", "turklar xristianlikni qabul qildi", "Kichik Osiyoda turk millati shakllana boshladi.")
t.NAT("Malikshoh vafot etdi.", "taxt uchun kurash kuchayib, davlat XII asr boshida ikkiga bo‘linib ketdi", "davlat yanada kengaydi", "Bag‘dod mustaqil bo‘ldi", "Nizomulmulk sulton bo‘ldi", "Davlat sharqiy va g‘arbiy qismlarga bo‘lindi.")
t.NAT("1243-yilda mo‘g‘ullar sharqdan bostirib keldi.", "Ko‘niya sultonligi zaiflashib, 1308-yilda beyliklarga bo‘linib ketdi", "sultonlik kuchaydi", "mo‘g‘ullar mag‘lub bo‘ldi", "Vizantiya Anatoliyani egalladi", "1308-yilda davlat beyliklarga bo‘lindi.")
t.NAT("Qoraxoniylar va g‘aznaviylar o‘rtasida kurash kechdi.", "saljuqiylar bundan foydalanib Xurosonni egallab, davlat barpo etdi", "saljuqiylar Sirdaryoga qaytdi", "g‘aznaviylar saljuqiylarni yo‘q qildi", "Xuroson Vizantiyaga qo‘shildi", "Saljuqiylar davlati tashkil topdi.")
t.TF("Usmon beyligi keyinchalik Usmonli turk imperiyasining paydo bo‘lishida asosiy rol o‘ynagan.", True, "To‘g‘ri.")
t.TF("Saljuqiylar davlat boshqaruvi va soliq tizimini Vizantiyadan qabul qilgan.", False, "Noto‘g‘ri: ularni sharqdagi musulmon davlatlardan qabul qilganlar.")
t.TF4([("To‘g‘rulbek ukasi Chag‘ribekni Xurosonda qoldirgan.", True), ("Alp Arslon davrida Kichik Osiyoga yurishlar uyushtirilgan.", True),
       ("Saljuqiylar davlat boshqaruvi dargoh va devonga bo‘lingan.", True), ("Beylar Saljuqiylar hukmronligini rasman ham tan olmagan.", False)],
      "4-noto‘g‘ri: beylar rasman tan olgan, amalda mustaqil boshqargan.")
t.MUL([("Ko‘niya, Qaysari, Sivas hunarmandchilik va savdo markazlari bo‘lgan.", True),
       ("Saljuqiylar davlati salibchilar hujumlarini qaytarishda katta xizmat qilgan.", True),
       ("Saljuqiylarda taxt saylov yo‘li bilan o‘tgan.", False)],
      "III noto‘g‘ri: taxt otadan bolaga meros bo‘lib o‘tgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Saljuqiylar Xurosonga ko‘chdi", "Saljuqiylar davlati tuzildi", "Bag‘dodda To‘g‘rulbek nomiga xutba o‘qildi", "Mansikert jangi", "Buxoro va Samarqand egallandi", "Mo‘g‘ullar bostirib keldi", "Davlat beyliklarga bo‘lindi"],
      "1025 → 1038 → 1055 → 1071 → 1074 → 1243 → 1308.")
t.MATCH("Shaxslarni ularga oid ma’lumot bilan moslashtiring.", ["Saljuqbek", "To‘g‘rulbek", "Malikshoh", "Nizomulmulk"],
        ["o‘g‘uzlarni islomga kiritgan yo‘lboshchi", "1038-yilda davlatga asos solgan", "Buxoro va Samarqandni egallagan", "«Siyosatnoma» muallifi", "Ko‘niya sultonligini cho‘qqiga olib chiqqan"], 'abcd',
        "Saljuqbek – islom; To‘g‘rulbek – 1038; Malikshoh – Buxoro, Samarqand; Nizomulmulk – «Siyosatnoma».")
t.VENN("Buyuk Saljuqiylar", "Ko‘niya sultonligi",
       [("To‘g‘rulbek asos solgan", 1), ("1055-yilda Bag‘dodni tobe qilgan", 1),
        ("markazi Nikeya, keyin Ko‘niya", 2), ("Alouddin Kaykubod davrida cho‘qqiga chiqqan", 2),
        ("o‘g‘uz turklari davlati", 3)],
       "Buyuk Saljuqiylar – To‘g‘rulbek, Bag‘dod; Ko‘niya – Nikeya, Kaykubod; ikkalasi o‘g‘uz turklari davlati.")
t.MAPMATCH('mideast', ['Bag‘dod', 'Mansikert', 'Ko‘niya', 'Samarqand'],
           ["1055-yilda To‘g‘rulbek nomiga xutba o‘qilgan shahar", "1071-yilda Vizantiya yengilgan joy", "Anatoliyadagi sultonlik markazi", "1074-yilda Buxoro bilan birga Malikshoh egallagan shahar"],
           "1 – Bag‘dod; 2 – Mansikert; 3 – Ko‘niya; 4 – Samarqand.")

# 11 Mo‘g‘ullar davlati
t = Topic('y7j11', 7011); TOPICS['y7j11'] = t
t.B("Mo‘g‘ul qabilalari qayerlarda yashagan?", "Janubiy Sibir, Manchjuriya va Mo‘g‘ulistonda", "Kichik Osiyoda", "Yettisuvda", "Hindistonda", "Janubiy Sibir, Manchjuriya va Mo‘g‘uliston hududlarida.")
t.B("Mo‘g‘ullarning diniy tasavvurlarida qanday e’tiqod saqlanib qolgan?", "shomonlik", "buddaviylik", "zardushtiylik", "xristianlik", "Ajdodlar ruhiga sig‘inish, shomonlik.")
t.B("Mo‘g‘ullarda alohida ko‘chmanchi xo‘jaliklar qanday atalgan?", "ayllar", "uluslar", "keshiklar", "qurultoylar", "Ayllar.")
t.B("Mo‘g‘ul urug‘ boshliqlari qanday atalgan?", "no‘yonlar", "konunglar", "beylar", "voliylar", "No‘yonlar.")
t.B("Qabila ittifoqlarining yig‘inlari qanday atalgan?", "qurultoy", "xalq majlisi", "«Donolar kengashi»", "devon", "Qurultoy.")
t.B("Temuchin qachon ulug‘ xon deb e’lon qilingan?", "1206-yilda", "1155-yilda", "1211-yilda", "1227-yilda", "1206-yilda.")
t.B("Temuchin qayerdagi qurultoyda ulug‘ xon deb e’lon qilingan?", "Onon daryosi bo‘yida", "Qoraqurumda", "Kalka daryosi bo‘yida", "Samarqandda", "Onon daryosi bo‘yidagi qurultoyda.")
t.B("«Chingiz» so‘zi qanday ma’noni anglatadi?", "«kuchli», «qudratli», «toza»", "«davlat», «xalq»", "«ulug‘ xon»", "«g‘olib»", "«Kuchli», «qudratli», «toza».")
t.B("Chingizxon davlatining poytaxti qaysi qal’a bo‘lgan?", "Qoraqurum", "Saroy", "Bag‘dod", "Pekin", "Qoraqurum qal’asi.")
t.B("Chingizxonning maxsus gvardiyasi qanday atalgan?", "keshik", "drujina", "mamluk", "tuman", "Keshik.")
t.B("Mo‘g‘ullarning sevimli quroli nima edi?", "kamon", "qilich", "nayza", "palaxmon", "Kamon.")
t.B("Chingizxon Shimoliy Xitoyga qarshi urushni qachon boshlagan?", "1211-yilda", "1206-yilda", "1218-yilda", "1219-yilda", "1211-yilda.")
t.B("Xorazmshohlar davlatiga bosqinlar qaysi yillarda bo‘lgan?", "1219–1221-yillarda", "1211–1215-yillarda", "1237–1242-yillarda", "1256–1258-yillarda", "1219–1221-yillarda.")
t.B("Mo‘g‘ullar qipchoqlarga yordamga kelgan rus qo‘shinini qaysi daryo bo‘yida yengan?", "Kalka", "Onon", "Dajla", "Volga", "Kalka daryosi bo‘yida.")
t.B("Chingizxon zabt etilgan hududlarni qachon uluslarga bo‘lgan?", "1224-yilda", "1206-yilda", "1227-yilda", "1237-yilda", "1224-yilda.")
t.B("Chingizxon kimni taxt vorisi etib tayinlagan?", "O‘qtoyni", "Jo‘jini", "Chig‘atoyni", "Tuluni", "O‘qtoyni.")
t.B("«Ulus» so‘zi mo‘g‘ulchada qanday ma’noni anglatadi?", "«davlat», «xalq», «odamlar»", "«kuchli»", "«qurultoy»", "«gvardiya»", "«Davlat», «xalq», «odamlar».")
t.B("Sharqiy Yevropaga 1237–1242-yillarda kim yurish qilgan?", "Botuxon", "Xuloku", "O‘qtoy", "Jo‘ji", "Chingizxonning nabirasi Botuxon.")
t.B("Xuloku Eronni qachon bosib olgan?", "1256-yilda", "1258-yilda", "1260-yilda", "1224-yilda", "1256-yilda; Xulokuylar davlati.")
t.B("1260-yilda mo‘g‘ullarni yenggan Misr sultoni kim?", "Sayfiddin Qutuz", "Al-Mansur Ali", "As-Solih II", "Jaloliddin Manguberdi", "Sulton Sayfiddin Qutuz.")
t.NAT("Botuxon Rus knyazliklari, Polsha, qisman Serbiya va Bolgariyani istilo qildi.", "istilo qilingan hududlarda Oltin O‘rda davlatiga asos solindi", "Botuxon Qoraqurumga qaytdi", "Rus knyazliklari mo‘g‘ullarni yengdi", "Xulokuylar davlati tuzildi", "Oltin O‘rda davlati tashkil topdi.")
t.NAT("1258-yilda Xuloku Bag‘dodni egalladi.", "shahar talandi, kutubxona yondirilib, kitoblar Dajlaga tashlandi", "Bag‘dod mo‘g‘ullar poytaxti bo‘ldi", "xalifalik kuchaydi", "Bag‘dod jangsiz taslim bo‘ldi", "Madaniyat va san’at asarlari yo‘q qilindi.")
t.NAT("Bag‘dod va Halab vayron qilindi.", "Damashq jangsiz taslim bo‘lib, islom dunyosining markazi Qohiraga ko‘chdi", "Damashq mo‘g‘ullarni yengdi", "Misr mo‘g‘ullarga taslim bo‘ldi", "islom dunyosining markazi Makkaga ko‘chdi", "Markaz Qohiraga ko‘chdi.")
t.NAT("1260-yilda Ayn-Jalutda Qutuz mo‘g‘ullarni tor-mor etdi.", "mo‘g‘ullarning Yaqin Sharq va Afrikaga yurishlari to‘xtadi", "mo‘g‘ullar Misrni egalladi", "Xuloku xalifa bo‘ldi", "Qutuz mo‘g‘ullarga bo‘ysundi", "Qutuz «Mo‘g‘ullar g‘olibi» nomini oldi.")
t.TF("Sayfiddin Qutuz Jaloliddin Manguberdining jiyani bo‘lgan.", True, "To‘g‘ri: Jaloliddinning opasining o‘g‘li.")
t.TF("Mo‘g‘ullar qo‘shini odatda beshta qismga bo‘lingan.", False, "Noto‘g‘ri: uchta qismga – markaz va ikki qanot.")
t.TF4([("Mo‘g‘ul qo‘shinini yuzboshi, mingboshi, tumanboshilar boshqargan.", True), ("Mo‘g‘ullar devor teshadigan palaxmondan foydalangan.", True),
       ("Chingizxon dastlab Xorazmshohlarni, keyin naymanlarni bo‘ysundirgan.", False), ("Qutuz Damashqning qul bozorida sotilgan.", True)],
      "3-noto‘g‘ri: avval naymanlar, uyg‘ur, yoqut, qirg‘iz, buryatlar, keyin Xitoy va Xorazmshohlar.")
t.MUL([("XII asr ikkinchi yarmidan mo‘g‘ullarda mulkiy tabaqalanish kuchaygan.", True),
       ("Xuloku Tuluning o‘g‘li bo‘lgan.", True),
       ("Misr sultoni Xulokuning taslim bo‘lish shartiga rozi bo‘lgan.", False)],
      "III noto‘g‘ri: Misr sultoni rozi bo‘lmagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Temuchin tug‘ildi", "Temuchin ulug‘ xon deb e’lon qilindi", "Shimoliy Xitoyga urush boshlandi", "Xorazmshohlar davlatiga bosqin boshlandi", "Hududlar uluslarga bo‘lindi", "Xuloku Eronni bosib oldi", "Ayn-Jalut jangi"],
      "1155 → 1206 → 1211 → 1219 → 1224 → 1256 → 1260.")
t.MATCH("Mo‘g‘ul hukmdorlarini ularga oid ma’lumot bilan moslashtiring.", ["Chingizxon", "O‘qtoy", "Botuxon", "Xuloku"],
        ["Qoraqurumni poytaxtga aylantirgan", "Chingizxonning taxt vorisi", "Oltin O‘rdaga asos solgan", "Bag‘dodni egallagan", "Ayn-Jalutda g‘alaba qozongan"], 'abcd',
        "Chingizxon – Qoraqurum; O‘qtoy – voris; Botuxon – Oltin O‘rda; Xuloku – Bag‘dod.")
t.VENN("Botuxon yurishlari", "Xuloku yurishlari",
       [("Rus knyazliklari istilo qilingan", 1), ("Oltin O‘rda tuzilgan", 1),
        ("Bag‘dod egallangan", 2), ("Xulokuylar davlati tuzilgan", 2),
        ("Chingizxon avlodlari boshchiligida", 3)],
       "Botuxon – Rus, Oltin O‘rda; Xuloku – Bag‘dod, Xulokuylar; ikkalasi Chingizxon avlodlari.")
t.MAPMATCH('eurasia2', ['Onon daryosi', 'Kalka daryosi', 'Bag‘dod', 'Ayn-Jalut'],
           ["1206-yilda qurultoy bo‘lgan joy", "rus qo‘shini mag‘lub etilgan daryo", "1258-yilda Xuloku egallagan shahar", "1260-yilda Qutuz mo‘g‘ullarni yenggan joy"],
           "1 – Onon; 2 – Kalka; 3 – Bag‘dod; 4 – Ayn-Jalut.")
