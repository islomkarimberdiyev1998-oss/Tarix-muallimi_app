from qlib import Topic, PLACES, REG
TOPICS = {}

# 11-§ Ashtarxoniylar davrida davlat boshqaruvi va tashqi siyosat
t = Topic('y9u11', 9011); TOPICS['y9u11'] = t
t.B("Ashtarxoniylar davrida asosiy boshqaruv idorasi nima bo‘lgan?", "dargoh (oliy devon)", "qurultoy", "kengash", "Senat", "Dargoh (oliy devon).")
t.B("Ashtarxoniylar davrida ahamiyati ortgan, ov qushlari va tozi itlarga mas’ul lavozim qaysi?", "qushbegi", "naqib", "dodxoh", "miroxur", "Qushbegi.")
t.B("Qushbegi qanday imtiyozga ega bo‘lgan?", "xon yorlig‘isiz ham yozma ko‘rsatmalar bera olgan", "taxt vorisi hisoblangan", "soliqdan ozod bo‘lgan", "qo‘shinga qo‘mondon bo‘lgan", "Xon yorlig‘isiz yozma ko‘rsatma bera olgan.")
t.B("Ashtarxoniylar tashqi siyosatida qaysi hudud janubiy chegarasini himoya qilish muhim vazifa bo‘lgan?", "Balx mulki", "Xorazm", "Farg‘ona", "Toshkent", "Balx mulkining janubiy hududlari.")
t.B("Xuroson va Hirotga ega bo‘lgan safaviylar e’tiborini qayerga qaratgan?", "Xorazmga", "Farg‘onaga", "Toshkentga", "Badaxshonga", "Xorazmga.")
t.B("Imomqulixon davrida Hindistonga qaysi hukmdor huzuriga elchilar yuborilgan?", "Jahongir podshoh", "Akbarshoh", "Avrangzeb", "Bobur", "Akbarning o‘g‘li Jahongir.")
t.B("1657-yilda Abdulazizxon Hindistonga elchi sifatida kimni jo‘natgan?", "naqshbandiya tariqati vakilini", "Mulla Farruxni", "Mustafoni", "Yalangto‘shni", "Naqshbandiya tariqati vakilini.")
t.B("Hindistondan Buxoroga kelgan elchilik qaysi?", "Yakkatozxon elchiligi", "Mustafo elchiligi", "Beneveni elchiligi", "Pazuxinlar elchiligi", "Yakkatozxon elchiligi.")
t.B("1691-yilda Subhonqulixon saroyiga elchi Mustafoni kim yuborgan?", "usmonli Sulton Ahmad II", "Pyotr I", "Jahongir", "shoh Abbos", "Sulton Ahmad II.")
t.B("1671-yilda Buxorodan Moskvaga yuborilgan elchi kim?", "Mulla Farrux", "Rustambiy", "Muhammad Sharif", "Mustafo", "Mulla Farrux.")
t.B("Rossiyadan qaysi mahsulotni olib chiqish taqiqlangan?", "metall va undan yasalgan buyumlar", "mo‘yna", "non", "matolar", "Metall – harbiy sohada asosiy mahsulot.")
t.B("Florio Beneveni elchiligiga yo‘riqnomani kim bergan?", "Pyotr I", "Ivan Grozniy", "Yekaterina II", "Aleksey Mixaylovich", "Pyotr I.")
t.B("Ashtarxoniylar davrida Rossiyadan kelgan elchilardan biri kim?", "Ivan Xoxlov", "Antoni Jenkinson", "Mir Quraysh", "Hakim Humom", "Ivan Xoxlov, Pazuxinlar, Beneveni va boshqalar.")
t.NAT("Eronga shimol va g‘arbdan usmonlilar tahdidi kuchaydi.", "safaviylar Buxoro bilan «do‘stlik va yaxshi qo‘shnichilik» siyosatini ishga soldi", "safaviylar Buxoroni bosib oldi", "Eron usmonlilarga taslim bo‘ldi", "Buxoro Eronga qarshi urush ochdi", "Safaviylar elchilar yubordi.")
t.NAT("Metall harbiy sohada asosiy mahsulot edi.", "Rossiya metallni mamlakatdan olib chiqishni taqiqladi", "Rossiya metallni Buxoroga sotdi", "Buxoro metall ishlab chiqarishni to‘xtatdi", "metall narxi tushdi", "Metall eksporti taqiqlangan.")
t.NAT("Savdo-elchilik tariqasida kelgan ruslar xonlik haqida ma’lumotlar to‘pladi.", "Rossiya hududdagi davlatlar va Hindiston bilan munosabat o‘rnatishga harakat qildi", "Rossiya xonlikka qo‘shin yubordi", "savdo aloqalari uzildi", "ruslar Buxoroda qoldi", "Rossiya mintaqaga qiziqishini oshirdi.")
t.NAT("Ashtarxoniylar va boburiylar o‘rtasida elchiliklar almashindi.", "ikki tomon safaviylarga qarshi kurash rejalarini bir-biriga taklif qildi", "ikki davlat urushga kirdi", "boburiylar Buxoroni egalladi", "Hindiston bilan aloqa uzildi", "Safaviylarga qarshi rejalar.")
t.TF("Jahongir podshoh Imomqulixon elchisini ehtirom bilan qabul qilgan.", True, "To‘g‘ri.")
t.TF("Ashtarxoniylar davri davlat boshqaruvi shayboniylarnikidan butunlay farq qilgan.", False, "Noto‘g‘ri: deyarli farq qilmagan.")
t.TF4([("Ashtarxoniylar Xurosonni Buxoro xonligi hukmiga to‘liq o‘tkaza olmagan.", True), ("XVIII asr boshidan rus elchiliklari siyosiy vazifalar bilan ham yuborilgan.", True),
       ("Beneveni Buxoro oltini qayerdan olinishini aniqlashi kerak edi.", True), ("Rossiya buxorolik savdogarlarga hech qanday to‘siq qo‘ymagan.", False)],
      "4-noto‘g‘ri: rus hukumati bir qator to‘siqlar qo‘ygan.")
t.MUL([("Rustambiy va Muhammad Sharif Hindistonga elchi bo‘lib borgan.", True),
       ("Sulton Ahmad II Eronga qarshi birgalikda kurashishni taklif qilgan.", True),
       ("Beneveni Buxoroni Eron bilan ittifoqqa chaqirishi kerak edi.", False)],
      "III noto‘g‘ri: Rossiya bilan harbiy ittifoqqa chaqirishi kerak edi.")
t.CHR("Elchiliklarni xronologik ketma-ketlikda joylashtiring.", ["Abdulazizxon naqshbandiya vakilini Hindistonga yubordi", "Mulla Farrux Moskvaga yuborildi", "Mustafo Subhonqulixon saroyiga keldi", "Florio Beneveni elchiligi"],
      "1657 → 1671 → 1691 → XVIII asr boshi (Pyotr I davri).")
t.MATCH("Elchilarni yuborgan tomoni bilan moslashtiring.", ["Mulla Farrux", "Mustafo", "Yakkatozxon", "Florio Beneveni"],
        ["Buxorodan Moskvaga", "Usmonli sultonidan Buxoroga", "Hindistondan Buxoroga", "Rossiyadan Buxoroga", "Erondan Buxoroga"], 'abcd',
        "Farrux – Moskvaga; Mustafo – usmonlilardan; Yakkatozxon – Hindistondan; Beneveni – Rossiyadan.")
t.VENN("Shayboniylar boshqaruvi", "Ashtarxoniylar boshqaruvi",
       [("Abdullaxon II davrida markazlashgan", 1), ("devoni sarkorixossa", 1),
        ("qushbegi imtiyozlari kengaygan", 2), ("chuhraboshi, inoq lavozimlari tilga olingan", 2),
        ("dargoh asosiy boshqaruv idorasi", 3)],
       "Shayboniylar – markazlashuv, sarkorixossa; ashtarxoniylar – qushbegi imtiyozlari; ikkalasida dargoh.")
t.MAPMATCH('wasia', ['Moskva', 'Istanbul', 'Buxoro', 'Agra'],
           ["1671-yilda Mulla Farrux yuborilgan poytaxt", "Eronga qarshi ittifoq taklif qilgan usmonli sultoni poytaxti", "ashtarxoniylar poytaxti", "Jahongir podshoh hukmronlik qilgan boburiylar shahri"],
           "1 – Moskva; 2 – Istanbul; 3 – Buxoro; 4 – Agra.")

# 12-§ Ashtarxoniylar davrida ijtimoiy-iqtisodiy hayot
t = Topic('y9u12', 9012); TOPICS['y9u12'] = t
t.B("Ashtarxoniylar davrida bug‘doyning nechtadan ortiq navi mavjud bo‘lgan?", "yigirmadan", "beshdan", "yuzdan", "o‘ndan", "Yigirmadan ortiq.")
t.B("Yog‘ olishda keng qo‘llanilgan ekin qaysi?", "kunjut", "kanop", "tamaki", "ro‘yon", "Kunjut (va zig‘ir).")
t.B("Bo‘yoq olish uchun ekilgan o‘simliklar qaysilar?", "ro‘yon, buzg‘unch, qirmiz", "kunjut, zig‘ir", "tariq, arpa", "sholg‘om, turp", "Ro‘yon, buzg‘unch, qirmiz.")
t.B("Nadr Muhammadning nechta qorako‘l teri beruvchi qo‘yi bo‘lgan?", "80000 ta", "8000 ta", "600 ta", "800 ta", "80000 ta.")
t.B("Nadr Muhammadning nechta oti bo‘lgan?", "8000 ta", "80000 ta", "600 ta", "200 ta", "8000 ta.")
t.B("Davlat yerlari amaldorlarga qanday shakllarda tortiq etilgan?", "suyurg‘ol, tiul, iqto, tanho", "vaqf va mulk", "xiroj va ushr", "tanob va alaf", "Suyurg‘ol, tiul, iqto, tanho.")
t.B("XVII asrning ikkinchi yarmida tangalardagi kumush ulushi har safar qanchaga kamaytirilgan?", "5–10 foizga", "50 foizga", "1 foizga", "25 foizga", "5–10 foizga.")
t.B("Ubaydullaxon pul islohotini qachon o‘tkazgan?", "1708-yilda", "1702-yilda", "1711-yilda", "1740-yilda", "1708-yilda.")
t.B("Ubaydullaxon islohotidagi yangi tangada necha foiz kumush bo‘lgan?", "9 foiz", "35 foiz", "25 foiz", "50 foiz", "9 foiz.")
t.B("Yangi tanga qiymati tarkibida necha foiz kumush bo‘lgan oldingi tangaga teng deb e’lon qilingan?", "35 foiz", "9 foiz", "50 foiz", "100 foiz", "35 foizli tangaga.")
t.B("XVIII asrda bir oltin tanga (ashrafiy) nechta kumush tangaga tenglashtirilgan?", "50–80 ta", "20–21 ta", "10 ta", "200 ta", "50–80 kumush tangaga.")
t.B("Ashtarxoniylar davrida nikoh-oila va jinoyat-jazo masalalari nima bilan belgilangan?", "shariat qoidalari", "Yasa qonunlari", "xon farmonlari", "Rossiya qonunlari", "Shariat qoidalari bilan.")
t.B("Bu davr yer huquqiga oid muhim manba qaysi?", "«Buxoro yer hujjatlari»", "«Abdullanoma»", "«Boburnoma»", "«Temur tuzuklari»", "«Buxoro yer hujjatlari» to‘plami.")
t.B("Manbaga ko‘ra Imomqulixon kechasi nima qilgan?", "oddiy kiyimda bozor va mahallalarni aylangan", "ovga chiqqan", "ziyofat bergan", "kitob yozgan", "Xalq ahvolidan boxabar bo‘lgan.")
t.NAT("Siyosiy beqarorlik davrida davlat xazinasi bo‘shab bordi.", "Ubaydullaxon 1708-yilda pul islohotini o‘tkazdi", "soliqlar bekor qilindi", "oltin tangalar zarbi to‘xtadi", "xazina boyidi", "Pul islohoti.")
t.NAT("Kumushi 9 foizli yangi tanga 35 foizli eski tangaga teng deb e’lon qilindi.", "savdogarlar va aholi norozi bo‘lib, qo‘zg‘olon ko‘tardi", "savdo rivojlandi", "narxlar tushdi", "aholi islohotni qo‘llab-quvvatladi", "Qo‘zg‘olon shafqatsiz bostirildi.")
t.NAT("Imomqulixon arz bilan kelganlarni qaytarmadi va xalq ahvolidan boxabar bo‘ldi.", "uning hukmronligi yillarida birorta ham isyon ko‘tarilmadi", "ko‘plab isyonlar bo‘ldi", "u taxtdan ag‘darildi", "soliqlar ikki barobar oshdi", "Isyonlar bo‘lmagan.")
t.NAT("Davlat Yevropa bilan aloqalar o‘rnatmadi, jahon siyosiy davrasiga kirmadi.", "ajdodlarimiz gidravlika, mashina, zamonaviy qurollardan bexabar qoldi", "Buxoro Yevropadan oldinga o‘tdi", "texnika tez rivojlandi", "Yevropa Buxoroga qaram bo‘ldi", "Texnik taraqqiyotdan orqada qolish.")
t.TF("O‘z yeriga ega bo‘lmagan aholi ko‘p hollarda yerni ijaraga olgan.", True, "To‘g‘ri.")
t.TF("Ashtarxoniylar siyosiy beqarorlik tufayli ilm-fan va san’atga homiylik qilmagan.", False, "Noto‘g‘ri: siyosiy vaziyatdan qat’i nazar homiylik qilgan.")
t.TF4([("Ashtarxoniylar davrida ham aholi xiroj, ushr, zakot to‘lagan.", True), ("Nadr Muhammadning 600 qator tuyasi bo‘lgan.", True),
       ("Ubaydullaxon islohotiga qarshi qo‘zg‘olon muvaffaqiyatli tugagan.", False), ("«Buxoro yer hujjatlari»da vaqf mulkini almashtirish tartibga solingan.", True)],
      "3-noto‘g‘ri: qo‘zg‘olon shafqatsizlarcha bostirilgan.")
t.MUL([("Ashtarxoniylar davrida davlat yerlarining hajmi ortgan.", True),
       ("Tashqi aloqalar asosan Xuroson va shimoldagi ko‘chmanchilar bilan cheklanib qolgan.", True),
       ("Ubaydullaxon islohotida tanga tarkibidagi kumush ko‘paytirilgan.", False)],
      "III noto‘g‘ri: kumush 4 marta kamaygan.")
t.CHR("Pul muomalasidagi o‘zgarishlarni tartiblang.", ["Abdullaxon II pul islohoti", "XVII asr ikkinchi yarmida kumush ulushining kamaytirilishi", "Ubaydullaxonning pul islohoti", "XVIII asrda muntazam oltin tanga zarbi"],
      "XVI asr → XVII asr 2-yarmi → 1708 → XVIII asr.")
t.MATCH("Atamalarni izohi bilan moslashtiring.", ["ashrafiy", "suyurg‘ol", "«Buxoro yer hujjatlari»", "qirmiz"],
        ["oltin tanga", "amaldorlarga tortiq etilgan davlat yeri", "yer huquqiga oid manba", "bo‘yoq beruvchi o‘simlik", "mis tanga"], 'abcd',
        "Ashrafiy – oltin tanga; suyurg‘ol – tortiq yer; yer hujjatlari – manba; qirmiz – bo‘yoq.")
t.VENN("Shayboniylar davri", "Ashtarxoniylar davri",
       [("Abdullaxon II pul islohoti", 1), ("Abdullaxon bandi qurilgan", 1),
        ("Ubaydullaxonning 1708-yilgi islohoti", 2), ("«Buxoro yer hujjatlari»", 2),
        ("xiroj, zakot, tanob puli undirilgan", 3)],
       "Shayboniylar – Abdullaxon II islohoti, band; ashtarxoniylar – 1708 islohot, yer hujjatlari; umumiy soliqlar.")
t.MAPN('uzb', ['Buxoro', 'Samarqand', 'Toshkent', 'Xiva'], "1708-yilda Ubaydullaxon pul islohotini o‘tkazgan ashtarxoniylar poytaxti xaritada qaysi raqam bilan belgilangan?",
       "Buxoro.")
