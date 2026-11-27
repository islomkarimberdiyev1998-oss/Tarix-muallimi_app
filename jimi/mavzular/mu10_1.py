from qlib import Topic
TOPICS = {}
UZ = 'uzb'; CA = 'ca'; EU = 'europe'

# 1 Turkiston o‘lkasi 1917-yil fevral – oktyabr oralig‘ida
t = Topic('e10u1', 10001); TOPICS['e10u1'] = t
t.B("«Haq olinur, berilmas!» shiorini kim o‘rtaga tashlagan?", "Mahmudxo‘ja Behbudiy", "Abdurauf Fitrat", "Munavvarqori", "Mustafo Cho‘qay", "Mahmudxo‘ja Behbudiy.")
t.B("«Rusiyada bosh ko‘targan yangi bir balo – bolshevik balosi» deb yozgan jadid nazariyotchisi kim?", "Abdurauf Fitrat", "Behbudiy", "Ubaydulla Xo‘jayev", "Validiy", "Abdurauf Fitrat.")
t.B("Rossiyada Fevral inqilobi qachon bo‘lgan?", "1917-yil 27-fevralda (yangi hisob — 12-mart)", "1917-yil 25-oktyabrda", "1917-yil 2-martda", "1918-yil 14-fevralda", "1917-yil 27-fevralda.")
t.B("Nikolay II qachon taxtdan voz kechgan?", "1917-yil 2-martda", "1917-yil 27-fevralda", "1917-yil 7-aprelda", "1917-yil 31-martda", "2-mart kuni.")
t.B("Rossiya Muvaqqat hukumatiga 1917-yil iyul – oktyabrda kim boshchilik qilgan?", "Aleksandr Kerenskiy", "Georgiy Lvov", "Lenin", "Kuropatkin", "Aleksandr Kerenskiy; mart – iyulda Georgiy Lvov.")
t.B("Grigorian kalendari Rossiyada qaysi dekret bilan joriy qilingan?", "1918-yil 26-yanvardagi XKS dekreti", "1917-yil fevral dekreti", "Tinchlik dekreti", "Yer dekreti", "1918-yil 26-yanvar dekreti; 31-yanvardan keyin 14-fevralga o‘tildi.")
t.B("Toshkentda ishchi deputatlari Soveti qachon tuzilgan?", "1917-yil 2-martda", "1917-yil 14-martda", "1917-yil 7-aprelda", "1917-yil 16-aprelda", "1917-yil 2-martda.")
t.B("Uy qamog‘iga olingan Turkiston general-gubernatori kim?", "A. N. Kuropatkin", "P. Korovichenko", "N. Shchepkin", "F. Kolesov", "General A. N. Kuropatkin, 31-martda.")
t.B("Turkiston komiteti qachon tuzilgan?", "1917-yil 7-aprelda", "1917-yil 2-martda", "1917-yil 14-martda", "1917-yil iyunda", "1917-yil 7-aprelda, 9 kishidan iborat.")
t.B("Turkiston komitetiga kimlar raislik qilgan?", "Nikolay Shchepkin va Vladimir Nakivkin", "Kerenskiy va Lvov", "Kolesov va Perfilev", "Tinishboyev va Bukeyxonov", "Kadet Shchepkin va eser Nakivkin.")
t.B("«Sho‘roi Islomiya» qachon tuzilgan?", "1917-yil 14-martda", "1917-yil iyunda", "1917-yil 16-aprelda", "1917-yil sentyabrda", "1917-yil 14-martda Toshkentda.")
t.B("«Sho‘roi Islomiya»ga keyinchalik kim rais qilib saylangan?", "Ubaydulla Xo‘jayev", "Mustafo Cho‘qay", "Sherali Lapin", "Mulla Muhiddinxon", "Ubaydullaxo‘ja Asadullaxo‘jayev.")
t.B("Butunturkiston musulmonlarining I qurultoyi qachon bo‘lib o‘tgan?", "1917-yil 16–23-aprelda", "1917-yil 14-martda", "1917-yil sentyabrda", "1917-yil noyabrda", "1917-yil 16–23-aprelda.")
t.B("Turkiston o‘lka musulmonlar kengashiga (Kraymussovet) kim rais bo‘lgan?", "Mustafo Cho‘qay", "Munavvarqori", "Ahmad Zaki Validiy", "Behbudiy", "Mustafo Cho‘qay.")
t.B("«Sho‘roi Ulamo» qachon tuzilgan?", "1917-yil iyunda", "1917-yil martda", "1917-yil sentyabrda", "1918-yil mayda", "1917-yil iyunda.")
t.B("«Sho‘roi Ulamo»ning Toshkent shu’basiga kim rahbarlik qilgan?", "Sherali Lapin", "Mulla Muhiddinxon", "Ubaydulla Xo‘jayev", "Mustafo Cho‘qay", "Sherali Lapin.")
t.B("«Sho‘roi Ulamo» qaysi jurnallarni nashr qilgan?", "«al-Izoh» va «al-Isloh»", "«Sho‘roi islom»", "«Turon» va «Oyina»", "«Taraqqiy» va «Xurshid»", "«al-Izoh» va «al-Isloh».")
t.B("1917-yil sentyabrdagi qurultoyda qaysi partiya tuzilgan?", "«Ittifoqi muslimin»", "«Sho‘roi Ulamo»", "«Turon»", "bolsheviklar", "«Ittifoqi muslimin».")
t.B("«Kadet» atamasi nimaning qisqartmasi?", "«konstitutsion demokratlar»", "«kazak deputatlari»", "«kadrlar komiteti»", "«kapital egalari»", "Konstitutsion demokratlar.")
t.NAT("Muvaqqat hukumat general-gubernatorlikni Turkiston komitetiga almashtirdi, xolos.", "mustamlakachilik boshqaruvi mohiyatan saqlanib, qarama-qarshiliklar vujudga keldi", "Turkiston mustaqil bo‘ldi", "jadidlar hokimiyatga keldi", "Sovetlar tugatildi", "Faqat nom o‘zgardi, boshqaruv avvalgicha qoldi.")
t.NAT("Jadidlar va eskilik tarafdori ulamolar o‘rtasida kelishmovchilik kuchaydi.", "1917-yil iyunda ulamolar ajralib chiqib, «Sho‘roi Ulamo»ni tuzdi", "tashkilotlar birlashdi", "bolsheviklar zaiflashdi", "Turkiston komiteti kuchaydi", "Bu bo‘linish bolsheviklarga qo‘l keldi.")
t.TF("Turkiston komiteti tarkibiga o‘zbek xalqining bitta ham vakili kiritilmagan.", True, "To‘g‘ri.")
t.TF("Turkistonda Rossiyadagi kabi faqat ikki hokimiyatchilik vujudga kelgan.", False, "Noto‘g‘ri: uch hokimiyatchilik paydo bo‘lgan.")
t.MUL([("Kraymussovet kotiblari Munavvarqori va Ahmad Zaki Validiy bo‘lgan.", True),
       ("1918-yil mayda bolsheviklar «Sho‘roi Islomiya» va «Sho‘roi Ulamo»ni tugatgan.", True),
       ("«Sho‘roi Ulamo» madrasalarni iqtisodiy qo‘llab-quvvatlashga qarshi chiqqan.", False)],
      "III noto‘g‘ri: uning dasturida madrasalarni qo‘llab-quvvatlash aytilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Toshkent Soveti tuzildi", "«Sho‘roi Islomiya» tuzildi", "Turkiston komiteti tuzildi", "Butunturkiston musulmonlarining I qurultoyi", "«Sho‘roi Ulamo» tuzildi", "«Ittifoqi muslimin» tuzildi"],
      "2-mart → 14-mart → 7-aprel → 16–23-aprel → iyun → sentyabr.")
t.MAPN(UZ, ['Samarqand', 'Toshkent', 'Andijon', 'Qo‘qon'], "Qaysi raqam bilan 1917-yil 14-martda «Sho‘roi Islomiya» tuzilgan va I qurultoy o‘tgan shahar belgilangan?",
       "2 – Toshkent; 4 – Qo‘qon: «Sho‘roi Ulamo»ning eng yirik shu’basi.", ask_idx=1)
t.VENN("«Sho‘roi Islomiya»", "«Sho‘roi Ulamo»",
       [("taraqqiyparvarlar (jadidlar) tashkiloti", 1), ("1917-yil 14-martda tuzilgan", 1),
        ("eskilik tarafdori ulamolar tashkiloti", 2), ("«al-Izoh» va «al-Isloh» jurnallari", 2),
        ("1918-yil mayda bolsheviklar tugatgan", 3)],
       "Sho‘roi Islomiya — jadidlar; Sho‘roi Ulamo — ulamolar; ikkalasi 1918-yilda tugatilgan.")

# 2 Sovet hokimiyatining majburiy o‘rnatilishi
t = Topic('e10u2', 10002); TOPICS['e10u2'] = t
t.B("Bolsheviklar Qishki saroyga qachon bostirib kirgan?", "24-oktyabrdan 25-oktyabrga o‘tar kechasi", "27-oktyabrda", "28-oktyabrda", "2-martda", "1917-yil 24–25-oktyabr kechasi.")
t.B("Butunrossiya Sovetlarining II syezdida qaysi dekretlar e’lon qilingan?", "Tinchlik va yer to‘g‘risidagi dekretlar", "kalendar dekreti", "muxtoriyat dekreti", "konstitutsiya", "Tinchlik va yer to‘g‘risida.")
t.B("Lenin boshchiligidagi hukumat qanday atalgan?", "Xalq Komissarlari Soveti (XKS)", "Muvaqqat hukumat", "Davlat dumasi", "Turkiston komiteti", "XKS.")
t.B("Oktyabr to‘ntarishi haqidagi xabar Toshkentga qachon yetib kelgan?", "27-oktyabrda", "25-oktyabrda", "28-oktyabrda", "15-noyabrda", "27-oktyabrda.")
t.B("Turkiston o‘lkasining bosh komissari qilib tayinlangan general kim?", "P. Korovichenko", "A. Kuropatkin", "F. Kolesov", "Ye. Perfilev", "General P. Korovichenko.")
t.B("Toshkentning yangi shaharida qurolli to‘qnashuvlar qachondan avj olgan?", "28-oktyabrdan", "27-oktyabrdan", "15-noyabrdan", "25-oktyabrdan", "28-oktyabrdan; to‘rt kunlik janglar.")
t.B("Turkiston ishchi va soldat deputatlari Sovetlarining III o‘lka syezdi qachon bo‘lgan?", "1917-yil 15–22-noyabrda", "1917-yil 12–15-noyabrda", "1917-yil 27-oktyabrda", "1917-yil 16–23-aprelda", "15–22-noyabrda.")
t.B("Turkiston o‘lka XKS da so‘l eserlarga nechta o‘rin berilgan?", "8 ta", "7 ta", "9 ta", "15 ta", "8 o‘rin; 7 o‘rin bolsheviklar va maksimalistlarga.")
t.B("Turkiston o‘lkasi XKS raisi kim bo‘lgan?", "Fyodor Kolesov", "Ye. Perfilev", "Sherali Lapin", "Lenin", "Kasbi chizmachi bolshevik Fyodor Kolesov.")
t.B("Turkiston XKS harbiy komissari kim bo‘lgan?", "Ye. Perfilev", "F. Kolesov", "P. Korovichenko", "Kerenskiy", "Izvoshchi Ye. Perfilev.")
t.B("1917-yil 12–15-noyabrda «turli musulmon guruhlarining birlashgan kengashi» kimning tashabbusi bilan o‘tkazilgan?", "«Sho‘roi Ulamo»", "«Sho‘roi Islomiya»", "bolsheviklar", "Milliy Markaz", "«Sho‘roi Ulamo» tashabbusi bilan.")
t.B("Bolsheviklarni qo‘llab-quvvatlagan «Sho‘roi Ulamo» Toshkent shu’basi yetakchisi kim?", "Sherali Lapin", "Mustafo Cho‘qay", "Ubaydulla Xo‘jayev", "Munavvarqori", "Sherali Lapin.")
t.B("Milliy Markaz noyabr boshlarida qayerga ko‘chib o‘tgan?", "Qo‘qonga", "Samarqandga", "Buxoroga", "Andijonga", "Toshkentdan Qo‘qonga.")
t.B("Mavjud tuzumni tanqid qilib radikal o‘zgarishlar talab etuvchi oqim qanday atalgan?", "maksimalistlar", "kadetlar", "mensheviklar", "monarxistlar", "Maksimalistlar.")
t.NAT("Turkiston o‘lka XKS faqat yevropaliklardan iborat qilib tuzildi.", "hukumatga mahalliy xalqlar vakillaridan biror kishi ham kiritilmadi", "jadidlar hukumatni boshqardi", "muxtoriyat e’lon qilindi", "koalitsion hukumat tuzildi", "Bu tasodifiy hol emas edi.")
t.NAT("Turkistondagi milliy siyosiy kuchlar bolsheviklar kuchini yetarli baholamadi va birlasha olmadi.", "bolsheviklar zo‘ravonlik bilan sovet hokimiyatini o‘rnatdi", "bolsheviklar Turkistondan chiqib ketdi", "Muvaqqat hukumat kuchaydi", "milliy kuchlar g‘alaba qozondi", "Bolsheviklar diktaturasi o‘rnatildi.")
t.TF("Toshkentdagi qurolli to‘qnashuvda mahalliy aholi deyarli ishtirok etmagan.", True, "To‘g‘ri.")
t.TF("Bolsheviklar ulamochilar taklif qilgan koalitsion hukumatni qo‘llab-quvvatlagan.", False, "Noto‘g‘ri: ular bu taklifni qat’iy rad etgan.")
t.MUL([("1917-yil noyabrda Samarqand, Skobelev va boshqa shaharlarda ham sovet hokimiyati o‘rnatilgan.", True),
       ("Jadidlar Butunturkiston qurultoyini chaqirib, muxtoriyat berish taklifi bilan chiqqan.", True),
       ("1917-yil kuzida Turkistonda bolsheviklarning omma orasida ta’siri juda katta edi.", False)],
      "III noto‘g‘ri: ularning ta’siri oz bo‘lgan, asosiy kuchlar eserlar va milliy partiyalar edi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Qishki saroy egallandi", "Xabar Toshkentga yetib keldi", "Toshkentda qurolli to‘qnashuvlar boshlandi", "Musulmon guruhlarining birlashgan kengashi", "III o‘lka syezdi"],
      "24–25-oktyabr → 27-oktyabr → 28-oktyabr → 12–15-noyabr → 15–22-noyabr.")
t.MAPMATCH(UZ, ['Toshkent', 'Qo‘qon', 'Samarqand'],
           ["to‘rt kunlik janglardan so‘ng yangi shahar qismida sovet hokimiyati o‘rnatilgan shahar", "Milliy Markaz va «Sho‘roi Islomiya» ko‘chib o‘tgan shahar", "1917-yil noyabrda Skobelev bilan birga sovet hokimiyati o‘rnatilgan shahar"],
           "1 – Toshkent; 2 – Qo‘qon; 3 – Samarqand.")
t.VENN("Rossiya XKS", "Turkiston o‘lka XKS",
       [("Lenin boshchiligida", 1), ("Petrogradda tuzilgan", 1),
        ("F. Kolesov raisligida", 2), ("faqat yevropaliklardan iborat", 2),
        ("bolsheviklar ishtirokidagi sovet hukumati", 3)],
       "Rossiya XKS — Lenin; Turkiston XKS — Kolesov, yevropaliklar.")
