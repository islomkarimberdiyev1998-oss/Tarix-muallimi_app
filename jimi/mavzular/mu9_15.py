from qlib import Topic
TOPICS = {}
UZ = 'uzb'; FV = 'fargona'

# 30 1916-yilgi qo‘zg‘olonning boshlanishi
t = Topic('e9u30', 9030); TOPICS['e9u30'] = t
t.B("Sirdaryo viloyatidan necha kishini mardikorlikka yuborish belgilangan?", "87 ming", "38 ming", "50 ming", "11 ming", "Sirdaryo — 87 ming, Samarqand — 38 ming, Farg‘ona — 50 ming.")
t.B("Samarqand viloyatidan necha kishini mardikorlikka yuborish belgilangan?", "38 ming", "87 ming", "50 ming", "25 ming", "38 ming.")
t.B("Farg‘ona viloyatidan necha kishini mardikorlikka yuborish belgilangan?", "50 ming", "87 ming", "38 ming", "11 ming", "50 ming.")
t.B("Farg‘ona viloyatida mardikorlarni to‘plash uchun nechta xonadondan bir kishi olinishi kerak edi?", "har beshtasidan", "har o‘ntasidan", "har ikkitasidan", "har yigirmatasidan", "Har beshtasidan bir kishi.")
t.B("Norozilik xavfi haqida ma’lumot bergani uchun lavozimidan ozod etilgan Farg‘ona gubernatori kim?", "A. Gippius", "polkovnik Ivanov", "Afanasyev", "Kuropatkin", "A. Gippius.")
t.B("1916-yil 4-iyulda qaysi shaharda aholi mardikorlikdan bosh tortib yig‘ilgan?", "Xo‘jandda", "Toshkentda", "Andijonda", "Jizzaxda", "4-iyulda Xo‘jandda.")
t.B("5-iyulda Samarqanddagi qaysi qishloqda norozilik bo‘lgan?", "Urgut", "Dahbed", "Zomin", "Sangzor", "5-iyulda Urgutda.")
t.B("Toshkentda 11-iyulda aholi qayerdagi politsiya mahkamasi oldiga to‘plangan?", "Beshyog‘ochdagi", "Ko‘kchadagi", "Sebzordagi", "Shayxontohurdagi", "Beshyog‘ochdagi politsiya mahkamasi.")
t.B("«Bizni o‘ldirsanglar ham o‘g‘illarimizni sizlarga bermaymiz» deb xitob qilgan ayol kim?", "Rizvonbibi Ahmadjonova", "Guloyim", "Nodira", "Hokim Oyim", "Rizvonbibi Ahmadjonova.")
t.B("Toshkentdagi namoyishda necha kishi otib o‘ldirilgan?", "11 kishi", "63 kishi", "3 kishi", "16 kishi", "11 kishi o‘ldirildi, 15 kishi yarador.")
t.B("9-iyulda qaysi shaharda podsho farmoni o‘qilgach qo‘zg‘olon boshlangan?", "Andijonda", "Namanganda", "Marg‘ilonda", "Xo‘jandda", "Andijonda; 3 kishi o‘ldirildi.")
t.B("10-iyulda Eski Marg‘ilonda taxminan necha kishi yig‘ilgan?", "25 ming kishi", "1500 kishi", "400 kishi", "100 ming kishi", "Taxminan 25 ming kishi.")
t.B("Eski Marg‘ilonda harbiylar necha qo‘zg‘olonchini otib o‘ldirgan?", "63 kishi", "11 kishi", "16 kishi", "3 kishi", "63 kishi.")
t.B("Namanganda qo‘zg‘olonchilar qaysi dahada yig‘ilgan?", "Labbaytog‘a dahasida", "Beshyog‘och dahasida", "Ko‘kcha dahasida", "Xadra dahasida", "Labbaytog‘a dahasida 1500 dan ortiq kishi.")
t.NAT("Mardikorlar ro‘yxatini tuzishda badavlat xonadonlar pora berib yozilmadi, kambag‘allar esa kiritildi.", "keng xalq ommasining noroziligi kuchaydi", "ro‘yxat bekor qilindi", "boylar jazolandi", "mardikorlik to‘xtatildi", "Nohaqliklar norozilikni kuchaytirdi.")
t.NAT("Markaziy hokimiyat Gippiusning ogohlantirishini «farmonni bajarmaslik» deb baholadi.", "Gippius gubernator lavozimidan ozod qilindi", "farmon bekor qilindi", "Gippius mukofotlandi", "mardikorlar soni kamaytirildi", "U lavozimidan ozod qilindi.")
t.NAT("Toshkentda politsiya namoyishchilarga qarata o‘q uzdi.", "xaloyiq mahkamaga bostirib kirdi", "namoyishchilar tarqab ketdi", "mardikorlik bekor qilindi", "politsiya chekindi", "O‘q uzilgach xaloyiq mahkamaga bostirib kirdi.")
t.TF("Norozilik harakatlarida dehqonlar, hunarmandlar, mayda savdogarlar va ishchilar ishtirok etgan.", True, "To‘g‘ri.")
t.TF("Mardikorlikka qarshi harakatlar faqat Toshkentda bo‘lib, boshqa joylarga tarqalmagan.", False, "Noto‘g‘ri: bir necha kun ichida butun o‘lkaga yoyildi.")
t.MUL([("Qo‘zg‘olon iyul o‘rtalarida Qo‘qon, Rishton, Marg‘ilon, Andijon, Namangan uyezdlarida keskin tus oldi.", True),
       ("Shahrixonda qo‘zg‘olonchilardan 16 kishi o‘ldirilgan.", True),
       ("Qurbonlar orasida ayollar va bolalar bo‘lmagan.", False)],
      "III noto‘g‘ri: ular orasida ayollar va bolalar ham bo‘lgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Xo‘jandda norozilik yig‘ini", "Urgutda norozilik", "Andijonda farmon o‘qilgach qo‘zg‘olon", "Eski Marg‘ilonda 25 ming kishi yig‘ildi", "Toshkentda Beshyog‘och mahkamasi oldidagi namoyish"],
      "4-iyul → 5-iyul → 9-iyul → 10-iyul → 11-iyul.")
t.MAPMATCH(FV, ['Xo‘jand', 'Andijon', 'Marg‘ilon', 'Namangan'],
           ["4-iyulda mardikorlikdan bosh tortib aholi yig‘ilgan shahar", "9-iyulda farmon o‘qilgach qo‘zg‘olon boshlangan shahar", "10-iyulda 25 ming kishi yig‘ilib, 63 kishi o‘ldirilgan shahar", "11-iyulda Labbaytog‘a dahasida 1500 kishi to‘plangan shahar"],
           "1 – Xo‘jand; 2 – Andijon; 3 – Marg‘ilon; 4 – Namangan.")
t.VENN("Toshkentdagi chiqish (11-iyul)", "Eski Marg‘ilondagi chiqish (10-iyul)",
       [("Beshyog‘och politsiya mahkamasi oldida", 1), ("Rizvonbibi Ahmadjonova og‘ir yaralangan", 1),
        ("taxminan 25 ming kishi qatnashgan", 2), ("63 kishi otib o‘ldirilgan", 2),
        ("mardikorlikka qarshi chiqish", 3)],
       "Toshkent — Beshyog‘och, Rizvonbibi; Marg‘ilon — 25 ming kishi, 63 qurbon.")

# 31 Jizzax qo‘zg‘oloni
t = Topic('e9u31', 9031); TOPICS['e9u31'] = t
t.B("Jizzax aholisi asosan nima bilan shug‘ullangan?", "don mahsulotlari yetishtirish", "paxtachilik", "baliqchilik", "ipakchilik", "Asosan don mahsulotlari yetishtirish.")
t.B("Jizzax uyezdidan necha kishini mardikorlikka olish belgilangan?", "11 ming kishi", "38 ming kishi", "87 ming kishi", "3 ming kishi", "11 ming kishi.")
t.B("Jizzaxda farmon qachon e’lon qilingan?", "1916-yil 3-iyulda", "1916-yil 13-iyulda", "1916-yil 25-iyunda", "1916-yil 18-iyulda", "3-iyulda.")
t.B("Jizzax qo‘zg‘oloniga kimlar rahbarlik qilgan?", "Nazirxo‘ja eshon va Abdurahmon jevachi", "Rizvonbibi va Damin kulol", "Dukchi eshon va Ziyovuddin", "Ernazarbiy va Zarliq", "Nazirxo‘ja eshon va Abdurahmon jevachi.")
t.B("13-iyulda hunarmandlarga kim boshchilik qilgan?", "Damin kulol", "Nazirxo‘ja eshon", "Mirzayor Xudoyorov", "Qosim hoji eshon", "Damin kulol.")
t.B("Ro‘yxatni bermay, odamlarni haqorat qilgan qishloq oqsoqoli kim?", "Mirzayor Xudoyorov", "Abdurahmon jevachi", "To‘raqul To‘rabekov", "Ivanov", "Mirzayor Xudoyorov.")
t.B("Qo‘zg‘olonchilarning umumiy rahbari kim bo‘lgan?", "Nazirxo‘ja eshon", "Damin kulol", "Abdurahmon jevachi", "Eshonqul To‘rabekov", "Nazirxo‘ja eshon.")
t.B("Qo‘zg‘olonchilar Jizzaxdan 12 chaqirim uzoqdagi qaysi joyda to‘planishga kelishgan?", "Kuyaboshi", "Zomin", "Sangzor", "Dahbed", "Kuyaboshi degan joyda.")
t.B("Turkistonda harbiy holat qachon e’lon qilingan?", "1916-yil 18-iyulda", "1916-yil 13-iyulda", "1916-yil 3-iyulda", "1916-yil 26-iyulda", "18-iyulda.")
t.B("Jizzaxga yuborilgan harbiy kuchlarga kim boshchilik qilgan?", "polkovnik Ivanov", "A. Gippius", "N. Korolkov", "Kuropatkin", "Polkovnik Ivanov.")
t.B("Jizzaxga yuborilgan harbiy kuchlar jami qancha bo‘lgan?", "ikki yarim ming kishi", "11 ming kishi", "600 kishi", "40 ming kishi", "13 rota, 2 artilleriya qismi, kazaklar — jami 2,5 ming.")
t.B("Abdurahmon jevachi 600 kishi bilan kimga qarshi jang qilgan?", "polkovnik Afanasyevga", "polkovnik Ivanovga", "Gippiusga", "Mirzayor Xudoyorovga", "20–21-iyulda Afanasyev kuchlariga qarshi.")
t.B("Qo‘zg‘olonchilardan necha kishi hibsga olingan?", "3 ming kishi", "11 ming kishi", "600 kishi", "2000 kishi", "3 ming kishi.")
t.B("«Jevachi» so‘zi nimani anglatadi?", "qurol-aslahaxona boshlig‘i", "qozi", "soliqchi", "mirob", "Jevachi — qurol-aslahaxona boshlig‘i.")
t.B("O‘qni tez otadigan avtomatik qurol qanday ataladi?", "pulemyot", "to‘p", "miltiq", "artilleriya", "Pulemyot.")
t.NAT("Mirzayor Xudoyorovning ro‘yxati asosan kambag‘al oila vakillaridan tuzilgan bo‘lib chiqdi va u ro‘yxatni bermadi.", "aholining keskin noroziligi qo‘zg‘olonga aylandi", "ro‘yxat qayta tuzildi", "mardikorlik bekor qilindi", "aholi tarqab ketdi", "Qo‘zg‘olonchilar Jizzaxning yangi shahar qismiga yo‘l oldi.")
t.NAT("Polkovnik Ivanov boshchiligidagi kuchlar Afanasyevga yordamga keldi.", "qo‘zg‘olonchilar yengilib, chekinishga majbur bo‘ldi", "qo‘zg‘olonchilar g‘alaba qozondi", "harbiylar chekindi", "sulh tuzildi", "Qo‘zg‘olonchilar mag‘lubiyatga uchradi.")
t.TF("Jizzax aholisi boshqa shaharlarga, jumladan, Toshkent va Samarqandga vakillar yuborgan.", True, "To‘g‘ri.")
t.TF("Qo‘zg‘olon bostirilgach, qo‘zg‘olonchilarning oila a’zolari jazodan chetda qoldi.", False, "Noto‘g‘ri: qariyalar, ayollar, hatto bolalar ham jazolandi.")
t.MUL([("13-iyulda qo‘zg‘olonchilar temiryo‘l stansiyalari va aloqa simlarini uzib tashlagan.", True),
       ("Mustamlakachilar avval Jizzaxni, keyin Zominni egallab, Sangzorga yurgan.", True),
       ("Qo‘zg‘olon rahbarlari afv etilgan.", False)],
      "III noto‘g‘ri: rahbarlar o‘lim jazosiga hukm etilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Jizzaxda farmon e’lon qilindi", "Dastlabki g‘alayonlar boshlandi", "Damin kulol oqsoqoldan ro‘yxatni talab qildi", "Turkistonda harbiy holat e’lon qilindi", "Abdurahmon jevachining Afanasyevga qarshi jangi"],
      "3-iyul → 5-iyul → 13-iyul → 18-iyul → 20–21-iyul.")
t.MAPMATCH(UZ, ['Jizzax', 'Zomin', 'Samarqand', 'Toshkent'],
           ["1916-yilda Nazirxo‘ja eshon qo‘zg‘oloni bo‘lgan shahar", "Jizzaxdan keyin jazo qo‘shini egallagan joy", "Jizzax uyezdi qarashli bo‘lgan viloyat markazi", "Jizzax aholisi vakil yuborgan, 11-iyulda Beshyog‘ochda chiqish bo‘lgan shahar"],
           "1 – Jizzax; 2 – Zomin; 3 – Samarqand; 4 – Toshkent.")
t.VENN("Nazirxo‘ja eshon", "Abdurahmon jevachi",
       [("qo‘zg‘olonchilarning umumiy rahbari", 1), ("eshon unvoniga ega", 1),
        ("o‘z uyida vakillar bilan yig‘ilish o‘tkazgan", 2), ("600 kishi bilan Afanasyevga qarshi jang qilgan", 2),
        ("o‘lim jazosiga hukm etilgan", 3)],
       "Nazirxo‘ja — umumiy rahbar; Abdurahmon jevachi — yig‘ilish, Afanasyevga qarshi jang; ikkalasi o‘limga hukm etilgan.")
