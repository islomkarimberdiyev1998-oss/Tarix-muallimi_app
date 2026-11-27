from qlib import Topic, PLACES, REG
TOPICS = {}

# 32-§ Qo‘qon adabiy muhiti
t = Topic('y9u32', 9032); TOPICS['y9u32'] = t
t.B("Umarxon qanday taxallus bilan she’rlar bitgan?", "Amiriy", "Maxmur", "Gulxaniy", "Komila", "Amiriy.")
t.B("Umarxon davrida qaysi shaharga asos solingan?", "Yangi Shahrixon", "Namangan", "Marg‘ilon", "Chust", "Yangi Shahrixon.")
t.B("Umarxon atrofida nechtadan ortiq shoir yig‘ilgan?", "70 dan", "7 dan", "700 dan", "26 dan", "70 dan ortiq.")
t.B("Umarxon devoni Istanbulda qachon chop etilgan?", "1882-yilda", "1905-yilda", "1821-yilda", "1842-yilda", "1882-yilda (Toshkentda 1905-yilda).")
t.B("1821-yilda «Majmuayi shoiron» to‘plamini kim tuzgan?", "Fazliy Namangoniy", "Maxmur", "Gulxaniy", "Uvaysiy", "Fazliy Namangoniy.")
t.B("«Majmuayi shoiron» necha shoirning she’rlarini o‘z ichiga olgan?", "63", "70", "26", "17", "63 shoirning.")
t.B("Hozirda Umarxonning nechta qo‘lyozma devoni mavjud?", "26 ta", "17 ta", "3 ta", "63 ta", "26 ta.")
t.B("Maxmurning asl ismi nima?", "Mahmud", "Muhammad Sharif", "Jahon", "Mohlaroyim", "Mahmud.")
t.B("Maxmurning qaysi she’rida qishloq xalqining ayanchli hayoti aks etgan?", "«Hapalak»", "«Zarbulmasal»", "«Karimquli Mehtarning sifatlari»", "«Yapaloqqush»", "«Hapalak».")
t.B("Gulxaniyning asl ismi nima?", "Muhammad Sharif", "Mahmud", "Jahon", "Fazliy", "Muhammad Sharif.")
t.B("Gulxaniy taxallusi nimadan kelib chiqqan?", "hammomda go‘lax (o‘t yoquvchi) bo‘lib ishlaganidan", "gulxan yoqqanidan", "gul sotganidan", "ustozi berganidan", "Go‘laxlik qilganidan.")
t.B("Gulxaniyning mashhur nasriy asari qaysi?", "«Zarbulmasal»", "«Hapalak»", "«Majmuayi shoiron»", "«Devon»", "«Zarbulmasal».")
t.B("«Zarbulmasal»da nechtaga yaqin xalq maqoli ishlatilgan?", "400 ga yaqin", "40 ga yaqin", "4000 ga yaqin", "69", "400 ga yaqin.")
t.B("Uvaysiyning asl ismi nima?", "Jahon", "Mohlaroyim", "Komila", "Maknuna", "Jahon.")
t.B("Uvaysiy 1842-yildan so‘ng qayerda yashagan?", "Marg‘ilonda", "Qo‘qonda", "Toshkentda", "Xo‘jandda", "Marg‘ilonda.")
t.B("Nodira qaysi taxalluslar bilan ham she’r yozgan?", "Komila va Maknuna", "Amiriy va Maxmur", "Uvaysiy", "Gulxaniy", "Komila va Maknuna.")
t.B("Nodira Umarxonga qachon turmushga chiqqan?", "1807-yilda", "1822-yilda", "1792-yilda", "1842-yilda", "1807-yilda.")
t.B("Umarxon vafotidan so‘ng necha yoshli Muhammad Alixon taxtga o‘tirgan?", "14 yoshli", "12 yoshli", "20 yoshli", "7 yoshli", "14 yoshli.")
t.B("Nodira yaxshi ishlagan kotiblarni qanday mansabga ko‘targan?", "«Zarrin qalam»", "«Mingboshi»", "«Beklarbegi»", "«Malik ush-shuaro»", "«Zarrin qalam».")
t.B("Nodira qurdirgan madrasalar qaysilar?", "Madrasayi Chalpak va Mohlaroyim madrasasi", "Norbo‘tabiy va Jome", "Mir Arab va Kukeldosh", "Muslihiddin", "Chalpak va Mohlaroyim madrasalari.")
t.NAT("Umarxon adabiyotga homiylik qildi.", "Buxoro, Sharqiy Turkiston, Afg‘onistondan ham olim va shoirlar Qo‘qonga kelib ijod qildi", "shoirlar Qo‘qondan ketdi", "adabiyot taqiqlandi", "faqat fors tilida yozildi", "Qo‘qon adabiy markazga aylandi.")
t.NAT("Umarxon davrida shakllangan adabiy oqim rivojlandi.", "Muqimiy, Furqat kabi demokrat shoirlarning paydo bo‘lishiga imkon yaratildi", "adabiyot so‘ndi", "shoirlar saroydan quvildi", "faqat diniy adabiyot qoldi", "Keyingi avlod shoirlari yetishdi.")
t.NAT("1822-yilda Umarxon vafot etib, 14 yoshli Muhammad Alixon taxtga o‘tirdi.", "davlatni asosan Nodira idora qildi", "Buxoro Qo‘qonni egalladi", "taxtni Uvaysiy egalladi", "xonlik tarqaldi", "Nodira davlatni boshqardi.")
t.NAT("1842-yilda amir Nasrulla Qo‘qonga bostirib kirdi.", "Madalixon, Nodira va boshqalar fojiali qatl etildi", "Nodira Buxoroga ketdi", "Qo‘qon mustaqil qoldi", "Uvaysiy saroyda qoldi", "Fojiali qatl.")
t.TF("Maxmur ijtimoiy hajviyani milliy adabiyotda yuksak pog‘onaga ko‘targan.", True, "To‘g‘ri.")
t.TF("Gulxaniy faqat fors tilida ijod qilgan.", False, "Noto‘g‘ri: o‘zbek va tojik tillarida ijod etgan.")
t.TF4([("Maxmur devonida 69 asar (3717 misra) jamlangan.", True), ("Uvaysiy saroyda Nodiraga she’riyatdan dars bergan.", True),
       ("Uvaysiy devonining nusxalari Andijon universiteti kutubxonasida ham saqlanadi.", True), ("Gulxaniy 1770-yilda Qo‘qonda tug‘ilgan.", False)],
      "4-noto‘g‘ri: Gulxaniy hozirgi Tojikistonning Tavildara tumanida tug‘ilgan.")
t.MUL([("Umarxon davrida arab va fors tilidagi kitoblar o‘zbek tiliga tarjima qilingan.", True),
       ("Uvaysiy aruz va muammo san’atini mukammal egallagan.", True),
       ("Umarxonning 17 ta qo‘lyozma devoni Sankt-Peterburgda saqlanadi.", False)],
      "III noto‘g‘ri: 17 ta devon Sharqshunoslik instituti fondida (Toshkent).")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Nodira Umarxonga turmushga chiqdi", "«Majmuayi shoiron» tuzildi", "Umarxon vafot etdi", "Nodira qatl etildi", "Umarxon devoni Istanbulda chop etildi"],
      "1807 → 1821 → 1822 → 1842 → 1882.")
t.MATCH("Shoirlarni asl ismi bilan moslashtiring.", ["Maxmur", "Gulxaniy", "Uvaysiy", "Nodira"],
        ["Mahmud", "Muhammad Sharif", "Jahon", "Mohlaroyim", "Fazliy"], 'abcd',
        "Maxmur – Mahmud; Gulxaniy – Muhammad Sharif; Uvaysiy – Jahon; Nodira – Mohlaroyim.")
t.VENN("Uvaysiy", "Nodira",
       [("asli ismi Jahon", 1), ("umrining oxirini Marg‘ilonda o‘tkazgan", 1),
        ("Komila, Maknuna taxalluslari", 2), ("Chalpak madrasasini qurdirgan", 2),
        ("Qo‘qon adabiy muhitidagi shoira", 3)],
       "Uvaysiy – Jahon, Marg‘ilon; Nodira – Komila, Chalpak; ikkalasi shoira.")
t.MAPMATCH('fargona', ['Marg‘ilon', 'Namangan', 'Qo‘qon', 'Xo‘jand'],
           ["Uvaysiy umrining oxirigacha yashagan shahar", "Gulxaniy mardikorlik qilgan shahar", "Gulxaniy go‘laxlik qilgan, Umarxon saroyi joylashgan poytaxt", "Uvaysiy va Nodira safar qilgan Sirdaryo bo‘yidagi shahar"],
           "1 – Marg‘ilon; 2 – Namangan; 3 – Qo‘qon; 4 – Xo‘jand.")

# 33-§ Qo‘qon xonligining tashqi siyosati
t = Topic('y9u33', 9033); TOPICS['y9u33'] = t
t.B("Abdukarimxon jung‘orlarga qarshi qo‘shinni kim boshchiligida yuborgan?", "ukasi Bobobek", "Erdona", "Norbo‘ta", "Abdurahim", "Ukasi Bobobek.")
t.B("Norbo‘taxon davrida tashqi siyosatga ta’sir etgan yangi omil nima edi?", "Xitoy bilan Sharqiy Turkiston xo‘jalari masalasi", "Rossiya bosqini", "Eron hujumi", "Xiva bilan urush", "Xitoy va xo‘jalar masalasi.")
t.B("1782–1783-yillarda Pekinga elchilikni kim boshqargan?", "Abdulqosim", "Mirza Muhammad Rahim", "Bobojon", "Xoja Mir Qurbon", "Abdulqosim.")
t.B("1796–1797-yillarda Pekinga elchilikka kim boshchilik qilgan?", "Bobojon", "Abdulqosim", "Mirza Muhammad Rahim", "Bobobek", "Bobojon.")
t.B("Sharqiy Turkistonda Qo‘qon savdogarlarini nazorat qilgan rasmiy vakil qanday atalgan?", "xudoydod", "beklarbegi", "mingboshi", "dodxoh", "Xudoydod (konsul).")
t.B("Xitoy Sharqiy Turkistonda qachon hukmronligini o‘rnatgan?", "1757–1759-yillarda", "1831-yilda", "1745-yilda", "1810-yilda", "1757–1759-yillarda.")
t.B("Erdonaxon Xitoyga qarshi harbiy ittifoqqa kimni da’vat etgan?", "Ahmadshoh Durroniyni", "Nodirshohni", "Changlingni", "Mahmud II ni", "Afg‘on hukmdori Ahmadshoh Durroniyni.")
t.B("1831-yilgi Qo‘qon–Pekin shartnomasi Qo‘qonga qanday imkoniyat bergan?", "Koshg‘ardagi xalqaro savdoni to‘liq nazorat qilish", "Pekinda elchixona ochish", "Xitoyga qo‘shin kiritish", "Sharqiy Turkistonni bosib olish", "Koshg‘ar savdosini to‘liq nazorat.")
t.B("Shartnomaga ko‘ra Qo‘qon qanday majburiyat olgan?", "Jahongirxo‘ja avlodlarini Sharqiy Turkistonga o‘tkazmaslik", "Xitoyga soliq to‘lash", "qo‘shin berish", "Toshkentni berish", "Jahongirxo‘ja avlodlarini o‘tkazmaslik.")
t.B("Qo‘qon xonligining Rossiya bilan elchilik munosabatlari qachon boshlangan?", "1810-yildan", "1831-yildan", "1745-yildan", "1853-yildan", "1810-yildan.")
t.B("Umarxon Istanbulga elchi sifatida kimni yuborgan?", "Xoja Mir Qurbon", "Bobojon", "Abdulqosim", "Mirza Muhammad Rahim", "Xoja Mir Qurbon.")
t.B("Muhammad Alixon Usmonli poytaxtiga qaysi yillarda elchilik yuborgan?", "1833 va 1837", "1810 va 1819", "1782 va 1792", "1842 va 1853", "1833 va 1837-yillarda.")
t.B("Qo‘qon–Hindiston dastlabki elchiligi qachon yuborilgan?", "1837-yilda", "1810-yilda", "1831-yilda", "1850-yilda", "1837-yilda.")
t.B("Hindiston orqali qaysi davlat bilan aloqa o‘rnatilgan?", "Buyuk Britaniya", "Fransiya", "Rossiya", "Eron", "Buyuk Britaniya.")
t.B("Buxoro amiri Haydar Qo‘qon va Xiva ustidan kimga arz qilgan?", "usmonli sultoni Mahmud II ga", "Rossiya imperatoriga", "Xitoy imperatoriga", "Ahmadshoh Durroniyga", "Mahmud II ga.")
t.B("Toshkentning mustaqil beklik maqomi qachon tugatilgan?", "1810-yilda", "1831-yilda", "1842-yilda", "1853-yilda", "1810-yilda.")
t.NAT("Norbo‘taxon Pekinga bir necha elchilik yubordi.", "Sharqiy Turkistonda Qo‘qon xudoydodi mansabi joriy etildi", "Xitoy Qo‘qonni bosib oldi", "savdo to‘xtadi", "xo‘jalar hokimiyatni oldi", "Xudoydod mansabi joriy etildi.")
t.NAT("Xitoy Sharqiy Turkistonni bosib oldi.", "bu Qo‘qonga ham xavf tug‘dirib, Erdonaxon faol tashqi siyosat yurita boshladi", "Qo‘qon Xitoyga qo‘shildi", "Qo‘qon savdoni to‘xtatdi", "Erdonaxon taxtdan voz kechdi", "Faol tashqi siyosat boshlandi.")
t.NAT("Qo‘qon hukmdorlari maktublar dushman qo‘liga tushishidan ehtiyot bo‘ldi.", "barcha masalalar muxtor elchi tomonidan og‘zaki aytilgan", "maktublar shifrlangan", "elchilik to‘xtatildi", "maktublar ochiq e’lon qilindi", "Og‘zaki bayon qilingan.")
t.NAT("Rossiya Qo‘qonning Usmonli va Britaniya bilan harbiy hamkorlik intilishidan xabardor edi.", "1850-yillardan Qo‘qon bu aloqalarni sir tutishga harakat qildi", "Qo‘qon Rossiya bilan ittifoq tuzdi", "Britaniya Qo‘qonni himoya qildi", "aloqalar to‘xtatildi", "Aloqalar maxfiy olib borildi.")
t.TF("Minglar Xitoy hukmdori Changlingga Qo‘qonliklar olib kirgan tovarlardan boj olmaslikni talab qilgan.", True, "To‘g‘ri.")
t.TF("1745-yilda Bobobek qo‘shini jung‘orlarni tor-mor etgan.", False, "Noto‘g‘ri: qo‘shin mag‘lubiyatga uchragan.")
t.TF4([("Koshg‘arda Qo‘qon xudoydodligi (konsulligi) ochilgan.", True), ("Xiva va Qo‘qon munosabatlarida o‘zaro yordamga intilish yetakchi bo‘lgan.", True),
       ("Buxoro o‘zini uchta o‘zbek davlati orasida yetakchi deb hisoblagan.", True), ("Qo‘qon–Hindiston aloqalari XVIII asr boshida boshlangan.", False)],
      "4-noto‘g‘ri: XIX asrning birinchi yarmidan, 1837-yildan boshlangan.")
t.MUL([("Xoja Mir Qurbon Istanbul va Sankt-Peterburgga elchi bo‘lib borgan.", True),
       ("Elchilik hindlarning ingliz harbiy usulida Qo‘qon askarlarini o‘qitishini maqsad qilgan.", True),
       ("Qo‘qon–Buxoro munosabatlarida doimo do‘stlik ustun bo‘lgan.", False)],
      "III noto‘g‘ri: dushmanlik kayfiyati ustunlik qilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Bobobek qo‘shini jung‘orlardan yengildi", "Xitoy Sharqiy Turkistonni egalladi", "Abdulqosim elchiligi Pekinga bordi", "Toshkent Qo‘qonga qo‘shib olindi", "Qo‘qon–Pekin shartnomasi tuzildi", "Hindistonga dastlabki elchilik yuborildi"],
      "1745 → 1757–1759 → 1782 → 1810 → 1831 → 1837.")
t.MATCH("Elchilarni yo‘nalishi bilan moslashtiring.", ["Abdulqosim", "Xoja Mir Qurbon", "Bobojon", "Mirza Muhammad Rahim"],
        ["1782–1783-yillarda Pekinga", "Istanbulga (Umarxon davrida)", "1796–1797-yillarda Pekinga", "1792–1793-yillarda Pekinga", "Kobulga"], 'abcd',
        "Abdulqosim – 1782; Mir Qurbon – Istanbul; Bobojon – 1796; Mirza Muhammad Rahim – 1792.")
t.VENN("Qo‘qon–Xitoy munosabatlari", "Qo‘qon–Usmonli munosabatlari",
       [("xudoydod mansabi", 1), ("1831-yilgi shartnoma", 1),
        ("Xoja Mir Qurbon elchiligi", 2), ("harbiy yordam so‘ralgan", 2),
        ("Qo‘qon xonligining tashqi aloqasi", 3)],
       "Xitoy – xudoydod, 1831; Usmonli – Mir Qurbon, harbiy yordam; ikkalasi tashqi aloqa.")
t.MAPMATCH('eurasia2', ['Istanbul', 'Peterburg', 'Pekin', 'Kobul'],
           ["Xoja Mir Qurbon yuborilgan Usmonli poytaxti", "Xoja Mir Qurbon elchi bo‘lgan Rossiya poytaxti", "Norbo‘taxon elchilari yuborilgan Xitoy poytaxti", "Erdonaxon ittifoqqa chaqirgan afg‘on hukmdorlari yurti shahri"],
           "1 – Istanbul; 2 – Peterburg; 3 – Pekin; 4 – Kobul.")
