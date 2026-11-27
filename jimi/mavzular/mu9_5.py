from qlib import Topic
TOPICS = {}
CA = 'ca'; ZR = 'zarafshon'; XR = 'xorazm'

# 10 Buxoro amirligi ustidan protektorat
t = Topic('e9u10', 9010); TOPICS['e9u10'] = t
t.B("Kaufman Samarqandni bosib olishga qachon kirishgan?", "1868-yil aprelda", "1866-yil mayda", "1873-yil fevralda", "1867-yil avgustda", "1868-yil aprelda, 4 mingdan ziyod qo‘shin bilan.")
t.B("1868-yil 1-mayda qaysi tepalikda jang bo‘lgan?", "Cho‘ponota tepaligida", "Zirabuloq tepaligida", "Afrosiyob tepaligida", "Niyozbek tepaligida", "Cho‘ponota tepaligida.")
t.B("Cho‘ponotadan keyingi ikkinchi jang qayerda bo‘lgan?", "Zirabuloq tepaligida", "Erjar yaqinida", "Urgutda", "Kattaqo‘rg‘onda", "Zirabuloq tepaligida.")
t.B("Urgutga qo‘shin bilan qaysi general yuborilgan?", "Abramov", "Romanovskiy", "Veryovkin", "Krijanovskiy", "General Abramov.")
t.B("Samarqanddagi kurashga qaysi hokimlar boshchilik qilgan?", "Kitob hokimi Jo‘rabek va Shahrisabz hokimi Bobobek", "Solihbek dodxoh va Hakim xo‘ja", "Aliquli va Abdurahmon", "Po‘latxon va Iso avliyo", "Jo‘rabek va Bobobek.")
t.B("Jo‘rabek va Bobobek qachon Samarqand qal’asiga hujum qilgan?", "1868-yil 2-iyunda", "1868-yil 1-mayda", "1868-yil 23-iyunda", "1873-yil 12-avgustda", "1868-yil 2-iyunda.")
t.B("Samarqand va Kattaqo‘rg‘on bo‘limlaridan iborat qanday okrug tuzilgan?", "Zarafshon okrugi", "Amudaryo bo‘limi", "Sirdaryo viloyati", "Farg‘ona viloyati", "Zarafshon okrugi, boshlig‘i general Abramov.")
t.B("Buxoro amirligini protektoratga aylantirgan shartnoma qachon imzolangan?", "1868-yil 23-iyunda", "1873-yil 12-avgustda", "1868-yil 2-iyunda", "1866-yil 18-oktabrda", "1868-yil 23-iyunda Samarqandda.")
t.B("1868-yilgi shartnomaga ko‘ra amir harbiy xarajatlar uchun qancha to‘lashi kerak edi?", "500 ming rubl", "100 ming rubl", "2 mln 200 ming rubl", "1 mln rubl", "500 ming rubl.")
t.B("Rossiya tovarlaridan olinadigan boj qancha foizdan oshmasligi belgilangan?", "2,5 foiz", "10 foiz", "5 foiz", "1 foiz", "Umumiy qiymatning 2,5 foizidan oshmasligi.")
t.B("Siyosiy qaramligi uchun Buxoro hukmdori tarixchilar tomonidan qanday ataladi?", "vassal", "to‘ra", "valiahd", "protektor", "Vassal.")
t.B("Xalq Amir Muzaffar o‘rniga kimni amir deb e’lon qilgan?", "Abdumalik to‘rani", "Jo‘rabekni", "Bobobekni", "Sayid Olimxonni", "Amirning katta o‘g‘li Abdumalik to‘rani.")
t.B("Abdumalik to‘ra qayerda vafot etgan?", "Peshovarda", "Kobulda", "Xivada", "Samarqandda", "Peshovarda, 1909-yilda.")
t.B("Rossiyaning Buxorodagi birinchi vakili kim bo‘lgan?", "P. Lessar", "I. Abramov", "F. Romanovskiy", "K. Kaufman", "P. Lessar.")
t.B("Rossiya vakili qaysi shaharni qarorgoh qilgan?", "Kogon", "Buxoro", "Samarqand", "Qarshi", "Buxorodan 15 km uzoqdagi Kogon.")
t.NAT("Rossiya bilan 1873-yilda amirlikka vakil tayinlash huquqini beruvchi shartnoma imzolandi.", "vakilning roziligisiz amirlik biror ichki yoki tashqi masalani hal qila olmaydigan bo‘ldi", "amirlik to‘liq mustaqil bo‘ldi", "amirlik tugatildi", "Buxoro Angliya protektoratiga o‘tdi", "Vakil amaldagi norasmiy gubernatorga aylandi.")
t.NAT("Afg‘on amiri Sheralixon Angliya bilan urushda Rossiyaga tayanishni rejalashtirdi.", "u Abdumalik to‘raga yordam bermadi", "u Buxoroni bosib oldi", "u Abdumalikni amir qilib tayinladi", "u Rossiyaga urush e’lon qildi", "Shu sababli Abdumalikka yordam bermadi.")
t.TF("Zirabuloq jangidan keyin Amir Muzaffar mag‘lubiyatini tan olib, Kaufmanning yangi chegaralar haqidagi taklifini qabul qildi.", True, "To‘g‘ri.")
t.TF("Kaufmanning amir qo‘shinlarini Samarqandga to‘plagan, degan taxmini to‘liq tasdiqlangan.", False, "Noto‘g‘ri: bu taxmin o‘z tasdig‘ini topmagan.")
t.MUL([("1868-yilgi shartnomaga ko‘ra Xo‘jand, O‘ratepa, Panjikent, Jizzax, Samarqand, Kattaqo‘rg‘on Rossiya ixtiyoriga o‘tdi.", True),
       ("Abdumalik to‘ra boshchiligidagi xalq qo‘shini Shahrisabz, Qarshi va Karmanani egallagan.", True),
       ("1873-yilgi shartnomaga ko‘ra amir har kuni Rossiya vakili bilan shaxsan uchrashgan.", False)],
      "III noto‘g‘ri: qo‘shbegi har kuni vakildan ko‘rsatma olib, amirga yetkazgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Cho‘ponota tepaligidagi jang", "Jo‘rabek va Bobobekning Samarqand qal’asiga hujumi", "Buxoro protektorat shartnomasi", "Buxoroga Rossiya vakilini tayinlash shartnomasi", "Eron bilan chegara maxfiy shartnomada belgilandi"],
      "1868-yil 1-may → 2-iyun → 23-iyun → 1873 → 1881.")
t.MAPMATCH(ZR, ['Urgut', 'Samarqand', 'Kattaqo‘rg‘on', 'Shahrisabz'],
           ["mahalliy aholi Abramov qo‘shiniga qarshi kurashgan shahar", "1868-yil 23-iyunda protektorat shartnomasi imzolangan shahar", "Zarafshon okrugidagi ikkinchi bo‘lim markazi", "hokimi Bobobek bo‘lgan shahar"],
           "1 – Urgut; 2 – Samarqand; 3 – Kattaqo‘rg‘on; 4 – Shahrisabz.")
t.VENN("1868-yilgi shartnoma", "1873-yilgi shartnoma",
       [("500 ming rubl harbiy xarajat to‘lash", 1), ("Toshkentdan Samarqandgacha hudud Rossiyaga o‘tgan", 1),
        ("amirlikka Rossiya vakili tayinlangan", 2), ("14-moddada Rossiya ruxsatisiz kimsalarni qabul qilmaslik", 2),
        ("Buxoro amirligini Rossiyaga qaram qilgan", 3)],
       "1868 — tovon, hududlar; 1873 — vakil, 14-modda; ikkalasi qaramlikni mustahkamlagan.")

# 11 Xiva xonligi ustidan protektorat
t = Topic('e9u11', 9011); TOPICS['e9u11'] = t
t.B("Rossiya Xivaga qarshi yurishga necha yil tayyorgarlik ko‘rgan?", "besh yil", "bir yil", "o‘n yil", "yigirma yil", "Besh yil tayyorgarlik ko‘rdi.")
t.B("Bekovich-Cherkasskiy boshchiligidagi qo‘shin qachon mag‘lubiyatga uchragan?", "1717-yilda", "1839-yilda", "1873-yilda", "1718-yilda", "1717-yilda.")
t.B("1839-yilda kim boshchiligidagi qo‘shin Xivaga yetib borolmay qaytgan?", "V. Perovskiy", "K. Kaufman", "N. Veryovkin", "M. Chernyayev", "V. Perovskiy.")
t.B("Xiva xonligining istilosi qaysi bosqichda amalga oshirilgan?", "uchinchi (1873–1879)", "birinchi (1847–1865)", "ikkinchi (1865–1868)", "to‘rtinchi (1880–1885)", "Uchinchi bosqichda.")
t.B("Xivaga hujum nechta harbiy okrugdan olib borilgan?", "to‘rtta", "ikkita", "bitta", "oltita", "Mang‘ishloq, Orenburg, Turkiston, Krasnovodsk.")
t.B("Xiva yurishida qancha askar qatnashgan?", "12 mingdan ortiq", "4 ming", "40 ming", "7,5 ming", "12 mingdan ortiq askar, 4600 ot, 20 ming tuya.")
t.B("Xivaga qancha askar yetib borgan?", "7,5 ming kishi", "12 ming kishi", "3 ming kishi", "20 ming kishi", "Xivaga 7,5 ming kishigina yetib bordi.")
t.B("Qaysi yo‘nalishlardan chiqqan qo‘shinlar yo‘lning yarmidan qaytgan?", "Krasnovodsk va Mang‘ishloq", "Toshkent va Orenburg", "Toshkent va Krasnovodsk", "Orenburg va Mang‘ishloq", "Krasnovodsk va Mang‘ishloqdan chiqqanlar qaytgan.")
t.B("Xivaga birinchi hujumga boshchilik qilib yarador bo‘lgan general kim?", "Veryovkin", "Kaufman", "Abramov", "Perovskiy", "General Veryovkin.")
t.B("Qaysi darvozaning ochib berilishi Xivaning egallanishiga olib kelgan?", "Hazorasp darvozasi", "Kamolon darvozasi", "Ko‘kcha darvozasi", "Ota darvoza", "29-mayda Hazorasp darvozasi ochib berildi.")
t.B("Xiva qachon egallangan?", "1873-yil 29-mayda", "1873-yil 12-avgustda", "1868-yil 23-iyunda", "1873-yil fevralda", "1873-yil 29-mayda.")
t.B("Xiva bilan sulh shartnomasi qaysi qishloqda imzolangan?", "Gandimiyon", "Hazorasp", "Xo‘jayli", "Kogon", "Gandimiyon qishlog‘ida.")
t.B("Gandimiyon shartnomasini qaysi xon imzolagan?", "Muhammad Rahimxon II", "Eltuzar", "Ollohqulixon", "Asfandiyorxon", "Muhammad Rahimxon II, 1873-yil 12-avgustda.")
t.B("Gandimiyon shartnomasiga ko‘ra Xiva qancha tovon to‘lashi kerak edi?", "2 million 200 ming rubl", "500 ming rubl", "100 ming rubl", "1 million rubl", "20 yil davomida 2 mln 200 ming rubl.")
t.B("Mag‘lub davlatning g‘olib davlat foydasiga pul to‘lovi qanday ataladi?", "kontributsiya", "pristan", "protektorat", "vassal", "Kontributsiya.")
t.B("Daryo sohilidagi kema to‘xtaydigan jihozlangan joy qanday ataladi?", "pristan", "kontributsiya", "forti", "istehkom", "Pristan — bandargoh.")
t.NAT("Xiva xonligi xazinasida tovon uchun yetarli pul bo‘lmadi.", "tovon aholidan yig‘ib olinadigan bo‘ldi", "tovon bekor qilindi", "Rossiya qarz berdi", "xonlik mustaqil bo‘ldi", "Tovon va yangi soliqlar xalq zimmasiga tushdi.")
t.NAT("Gandimiyon shartnomasi bilan Amudaryoning o‘ng sohili xon tasarrufidan chiqdi.", "xonlik hududi uch baravar qisqardi", "xonlik hududi kengaydi", "Xiva Buxoroga qo‘shildi", "xon Rossiya imperatori bo‘ldi", "Hudud uch baravar qisqardi, xonlik protektoratga aylandi.")
t.TF("Xivaga yurish yo‘lida qo‘shin 25 daraja sovuq va 40 darajadan yuqori issiqqa duch kelgan.", True, "To‘g‘ri.")
t.TF("Gandimiyon shartnomasiga ko‘ra Xiva xoni qo‘shni hukmdorlar bilan erkin shartnoma tuza olardi.", False, "Noto‘g‘ri: u bunday munosabatlardan voz kechgan.")
t.MUL([("Kaufman Xiva xazinasi, qo‘lyozmalar, xonning taxti va tojini Sankt-Peterburgga jo‘natgan.", True),
       ("Rossiya kemalariga Amudaryo bo‘ylab erkin harakatlanish huquqi berilgan.", True),
       ("Rossiyalik savdogarlar Xivada 2,5 foiz boj to‘lab savdo qilgan.", False)],
      "III noto‘g‘ri: ular boj to‘lovlarisiz savdo qilish huquqini olgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Bekovich-Cherkasskiy qo‘shinining mag‘lubiyati", "Perovskiy qo‘shinining Xivaga yetolmay qaytishi", "Qo‘shinlarning Toshkent, Orenburg, Mang‘ishloq, Krasnovodskdan yo‘lga chiqishi", "Xivaning egallanishi", "Gandimiyon shartnomasining imzolanishi"],
      "1717 → 1839 → 1873-yil fevral → 29-may → 12-avgust.")
t.MAPN(XR, ['Hazorasp', 'Xiva', 'Qo‘ng‘irot', 'Xo‘jayli'], "Qaysi raqam bilan 1873-yil 29-mayda Hazorasp darvozasi ochib berilishi natijasida egallangan xonlik poytaxti belgilangan?",
       "2 – Xiva; 1 – Hazorasp qal’asi, 3 – Qo‘ng‘irot, 4 – Xo‘jayli (may janglari bo‘lgan joylar).", ask_idx=1)
t.VENN("Buxoro bilan 1868-yilgi shartnoma", "Gandimiyon shartnomasi",
       [("500 ming rubl to‘lash", 1), ("Samarqand Rossiyaga o‘tgan", 1),
        ("2 mln 200 ming rubl tovon", 2), ("Amudaryoning o‘ng sohili xon tasarrufidan chiqqan", 2),
        ("xonlikni Rossiya protektoratiga aylantirgan", 3)],
       "Buxoro — 500 ming, Samarqand; Xiva — 2,2 mln, o‘ng sohil; ikkalasi protektorat o‘rnatgan.")
