from qlib import Topic
TOPICS = {}
UZ = 'uzb'; FV = 'fargona'

# 3 Turkiston Muxtoriyati
t = Topic('e10u3', 10003); TOPICS['e10u3'] = t
t.B("Butunturkiston musulmonlarining favqulodda IV qurultoyi qachon va qayerda bo‘lgan?", "1917-yil 26–28-noyabrda Qo‘qonda", "1917-yil 16–23-aprelda Toshkentda", "1918-yil 19–26-yanvarda Toshkentda", "1917-yil sentyabrda Samarqandda", "1917-yil 26–28-noyabrda Qo‘qonda.")
t.B("Muxtoriyat to‘g‘risidagi qaror qaysi kuni qabul qilingan?", "27-noyabr kechqurun", "26-noyabr ertalab", "28-noyabr", "1-dekabr", "27-noyabr kechqurun.")
t.B("Turkiston qaysi davlat tarkibida hududiy muxtor deb e’lon qilingan?", "Federativ Rossiya Respublikasi", "Buxoro amirligi", "Usmonli davlati", "Afg‘oniston", "Federativ Rossiya Respublikasi tarkibida.")
t.B("Hukumat nomi qachon «Turkiston Muxtoriyati» deb belgilangan?", "28-noyabrda", "27-noyabrda", "1-dekabrda", "26-noyabrda", "28-noyabrda.")
t.B("Turkiston Muxtoriyati hukumati necha kishidan iborat edi?", "8 kishi", "9 kishi", "15 kishi", "5 kishi", "8 kishi.")
t.B("Muxtoriyat hukumatining birinchi Bosh vaziri kim?", "Muhammadjon Tinishboyev", "Mustafo Cho‘qay", "Ubaydulla Xo‘jayev", "Islom Sulton Shoahmedov", "Muhammadjon Tinishboyev.")
t.B("Muxtoriyat hukumatida harbiy vazir kim edi?", "Ubaydulla Xo‘jayev", "Mustafo Cho‘qay", "Obidjon Mahmudov", "Solomon Gersfeld", "Ubaydulla Xo‘jayev.")
t.B("Muxtoriyat hukumatida tashqi ishlar vaziri kim edi?", "Mustafo Cho‘qay", "Tinishboyev", "Agayev", "O‘rozayev", "Mustafo Cho‘qay; keyinchalik Bosh vazir.")
t.B("Muhammadjon Tinishboyev qanday mutaxassis edi?", "temiryo‘l muhandisi", "huquqshunos", "agronom", "tog‘-kon mutaxassisi", "Temiryo‘l muhandisi.")
t.B("Kimning bosmaxonasi hukumat ixtiyoriga o‘tgan?", "O. Mahmudovning", "Behbudiyning", "Munavvarqorining", "Fitratning", "Obidjon Mahmudovning.")
t.B("1918-yil boshidagi paradda milliy qo‘shin askarlari soni qancha bo‘lgan?", "2000 kishi", "10 000 kishi", "500 kishi", "60 000 kishi", "2000 kishi.")
t.B("Muxtoriyat hukumati qancha ichki zayom chiqarishni yo‘lga qo‘ygan?", "30 million so‘m", "4,4 mln pud", "100 mln so‘m", "1 mln so‘m", "30 million so‘m.")
t.B("Fitrat 27-noyabr tunini qanday atagan?", "«Milliy laylatulqadrimiz»", "«Ozodlik tuni»", "«Qonli tun»", "«Buyuk tun»", "«Milliy laylatulqadrimiz».")
t.B("1917-yil dekabrda Toshkentda Munavvarqori rahbarligidagi mitingda qancha kishi qatnashgan?", "60 000 kishi", "10 000 kishi", "2000 kishi", "5000 kishi", "60 000 kishi.")
t.B("Toshkent Sovetining rahbari kim edi?", "Ivan Tobolin", "F. Kolesov", "Ye. Perfilev", "P. Kobozev", "Ivan Tobolin.")
t.B("Muxtoriyatni kuch bilan tugatish qaysi syezdda qaror qilingan?", "1918-yil 19–26-yanvardagi IV o‘lka syezdida", "III o‘lka syezdida", "V o‘lka syezdida", "IV qurultoyda", "Sovetlarning favqulodda IV syezdida.")
t.B("Turkiston o‘lka XKS harbiy harakatlarni qachon boshlagan?", "1918-yil 30-yanvarda", "1918-yil 22-fevralda", "1918-yil 15-fevralda", "1917-yil 1-dekabrda", "1918-yil 30-yanvarda.")
t.B("Bolsheviklar armanlarning qaysi partiyasi a’zolaridan foydalangan?", "«Dashnoqsutyun»", "«Ittifoqi muslimin»", "kadetlar", "eserlar", "«Dashnoqsutyun».")
t.B("18-fevraldan Muxtoriyat hukumatining amaldagi rahbari kim bo‘lgan?", "Kichik Ergash qo‘rboshi", "Mustafo Cho‘qay", "Tinishboyev", "Ubaydulla Xo‘jayev", "Qo‘qon mirshablar boshlig‘i Kichik Ergash.")
t.B("Qo‘qonning o‘zida 3 kun davomida qancha kishi o‘ldirilgan?", "10 000 kishi", "2000 kishi", "60 000 kishi", "1 mln kishi", "10 000 kishi.")
t.B("«Tinchlik shartnomasi» qachon imzolangan?", "1918-yil 22-fevralda", "1918-yil 20-fevralda", "1918-yil 30-yanvarda", "1918-yil 18-fevralda", "1918-yil 22-fevralda Rus-Osiyo banki binosida.")
t.B("Turkiston Muxtoriyati necha kun mavjud bo‘lgan?", "72 kun", "100 kun", "30 kun", "365 kun", "Atigi 72 kun.")
t.NAT("Qurolsiz qo‘qonliklar sovet harbiy kuchlari hujumini uch kun qaytardi.", "Perfilev boshchiligida 11 eshelon yuborilib, shahar yondiruvchi snaryadlar bilan o‘qqa tutildi", "bolsheviklar chekindi", "Muxtoriyat g‘alaba qozondi", "sulh tezda tuzildi", "Shahar vayron qilindi, Muxtoriyat ag‘darildi.")
t.NAT("Samarqanddagi viloyat Sovetlari syezdi Turkiston Muxtoriyatiga qo‘shilishga qaror qildi.", "Millat Majlisi tarkibiga 5 vakil saylandi", "Samarqand mustaqil bo‘ldi", "syezd tarqatildi", "bolsheviklar Samarqandni tark etdi", "5 vakil saylandi.")
t.TF("Muxtoriyat hukumati vazirlarining aksariyati oliy ma’lumotli huquqshunoslar bo‘lgan.", True, "To‘g‘ri.")
t.TF("Muxtoriyatning ma’muriy markazi Toshkent shahri deb belgilangan.", False, "Noto‘g‘ri: markaz Qo‘qon shahri deb belgilangan.")
t.MUL([("Hukumat gazetalari o‘zbek, qozoq va rus tillarida nashr qilingan.", True),
       ("Muxtoriyat hukumati Kavkazdan Orenburg orqali g‘alla keltirish muammosini hal qilishga uringan.", True),
       ("1918-yil 22-fevraldagi shartnomada aholi Muxtoriyat hukumatini tan oladi, deb yozilgan.", False)],
      "III noto‘g‘ri: aholi o‘lka XKS hokimiyatini tan oladi, deb yozilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Muxtoriyat e’lon qilindi", "Murojaatnoma e’lon qilindi", "IV o‘lka syezdi Muxtoriyatni tugatishga qaror qildi", "Harbiy harakatlar boshlandi", "«Xo‘qand tarixining eng dahshatli kuni»", "«Tinchlik shartnomasi» imzolandi"],
      "1917-yil 27-noyabr → 1-dekabr → 1918-yil 19–26-yanvar → 30-yanvar → 20-fevral → 22-fevral.")
t.MAPN(FV, ['Namangan', 'Qo‘qon', 'Farg‘ona', 'Andijon'], "Qaysi raqam bilan Turkiston Muxtoriyatining markazi belgilangan?",
       "2 – Qo‘qon; 3 – Skobelev (Farg‘ona): bu yerdan otryadlar Qo‘qonga yetib kelgan.", ask_idx=1)
t.VENN("Turkiston Muxtoriyati hukumati", "Turkiston o‘lka XKS",
       [("vazirlarining aksariyati oliy ma’lumotli", 1), ("markazi Qo‘qon", 1),
        ("faqat yevropaliklardan tuzilgan", 2), ("dashnoqlardan foydalangan", 2),
        ("1917-yil oxirida tuzilgan hukumat", 3)],
       "Muxtoriyat — bilimli vazirlar, Qo‘qon; XKS — yevropaliklar, dashnoqlar.")

# 4 Sovet boshqaruv tizimi va iqtisodiyotdagi o‘zgarishlar
t = Topic('e10u4', 10004); TOPICS['e10u4'] = t
t.B("Lenin buyrug‘i bilan O‘rta Osiyoning favqulodda komissari qilib kim jo‘natilgan?", "Pyotr Kobozev", "Ivan Tobolin", "M. V. Frunze", "F. Kolesov", "Bolshevik Pyotr Kobozev.")
t.B("Turkiston ASSR tuzilganligi qaysi syezdda e’lon qilingan?", "1918-yil 20-aprel – 1-maydagi V o‘lka syezdida", "IV o‘lka syezdida", "III o‘lka syezdida", "TKP tashkiliy syezdida", "V o‘lka syezdida.")
t.B("«Turkiston Sovet Respublikasi haqidagi Nizom» qachon qabul qilingan?", "1918-yil 30-aprelda", "1918-yil 1-mayda", "1918-yil 17-iyunda", "1918-yil 20-aprelda", "30-aprelda.")
t.B("Turkiston Kommunistik partiyasi qachon rasmiylashtirilgan?", "1918-yil 17–25-iyunda", "1918-yil 30-aprelda", "1919-yil martda", "1921-yil avgustda", "1918-yil 17–25-iyunda.")
t.B("TKP Markaziy Komiteti kim raisligida saylangan?", "Ivan Tobolin", "T. Risqulov", "N. Xo‘jayev", "P. Kobozev", "Ivan Tobolin, 7 kishilik.")
t.B("TKP MK tarkibiga mahalliy kommunistlardan kim kiritilgan?", "Nizomiddin Xo‘jayev", "Turor Risqulov", "Munavvarqori", "Fitrat", "Nizomiddin Xo‘jayev.")
t.B("Musulmonlar byurosi (Musbyuro) qachon tashkil qilingan?", "1919-yil martda", "1918-yil iyunda", "1920-yil yanvarda", "1921-yil martda", "1919-yil martda, TKP II konferensiyasida.")
t.B("Musulmonlar byurosiga kim rais bo‘lgan?", "T. Risqulov", "N. Xo‘jayev", "A. Muhitdinov", "Munavvarqori", "Turor Risqulov.")
t.B("1920-yil yanvarda T. Risqulov respublikani qanday atashni taklif qilgan?", "Turk Respublikasi", "O‘zbek Respublikasi", "Turon Respublikasi", "Turkiston Muxtoriyati", "Turk Respublikasi.")
t.B("Risqulovning takliflariga kim qarshi chiqqan?", "M. V. Frunze va V. I. Lenin", "Tobolin va Kobozev", "Kolesov va Perfilev", "Munavvarqori va Avloniy", "Turkfront qo‘mondoni Frunze va Lenin.")
t.B("Ocharchilikka qarshi kurash Markaziy komissiyasi qachon tuzilgan?", "1918-yil 20-noyabrda", "1917-yil qishida", "1921-yil mart", "1919-yil mart", "1918-yil 20-noyabrda, Risqulov raisligida.")
t.B("1917–1923-yillarda Farg‘ona vodiysida ocharchilikdan qancha kishi o‘lgan?", "1 mln kishi", "200 000 kishi", "10 000 kishi", "4,4 mln kishi", "1 mln kishi; Samarqandda 200 ming.")
t.B("1921–1922-yillarda Turkistondan Rossiyaga qancha g‘alla jo‘natilgan?", "4,4 mln pud", "1 mln pud", "30 mln pud", "600 ming pud", "4,4 mln pud.")
t.B("1918–1920-yillardagi bolsheviklar siyosati qanday nomlangan?", "«harbiy kommunizm»", "yangi iqtisodiy siyosat", "kollektivlashtirish", "industrlashtirish", "«Harbiy kommunizm».")
t.B("Oziq-ovqat razvyorstkasini soliq bilan almashtirish qaysi syezdda qaror qilingan?", "RKP(b) X syezdida (1921-yil mart)", "TKP VI syezdida", "V o‘lka syezdida", "II konferensiyada", "RKP(b) X syezdi, 1921-yil mart.")
t.B("1 pud necha kilogrammga teng?", "16,38 kg", "1,09 kg", "10 kg", "100 kg", "16,38 kg.")
t.B("Yer-suv islohotining birinchi bosqichi qaysi yillarda o‘tkazilgan?", "1921–1922-yillarda", "1918–1920-yillarda", "1925–1929-yillarda", "1917–1918-yillarda", "1921–1922-yillarda.")
t.B("Islohotning birinchi bosqichida mahalliy aholiga qancha yer ajratilgan?", "600 000 desyatina", "1 722 626 desyatina", "4,4 mln desyatina", "100 000 desyatina", "Faqat 600 000 desyatina.")
t.NAT("RKP(b) X syezdi razvyorstkani oziq-ovqat solig‘i bilan almashtirishga qaror qildi.", "yangi iqtisodiy siyosat (NEP) boshlandi", "harbiy kommunizm kuchaydi", "bozor taqiqlandi", "barcha korxonalar xususiylashtirildi", "NEP — dehqonlarga bir qadar erkinlik berish.")
t.NAT("Risqulovning Turkistonni mustaqillik tomon olib boruvchi takliflari rad etildi.", "1920-yil yozida u vazifasidan ozod qilinib, Moskvaga chaqirib olindi", "u Turkiston rahbari bo‘ldi", "Turk Respublikasi tuzildi", "Turkfront tugatildi", "Risqulov Moskvaga chaqirildi.")
t.TF("Musulmonlar byurosi faoliyatida Munavvarqori va Abdulla Avloniy ham ishtirok etgan.", True, "To‘g‘ri.")
t.TF("«Harbiy kommunizm» davrida bozor munosabatlari rag‘batlantirilgan.", False, "Noto‘g‘ri: bozor yo‘qotilib, pul natura bilan almashtirilgan.")
t.MUL([("Markaz Turkkomissiya, Turkbyuro, O‘rta Osiyo byurosi orqali Turkiston ASSRni boshqarishga harakat qilgan.", True),
       ("Yer-suv islohoti boy-quloq xo‘jaliklarini tugatishga qaratilgan edi.", True),
       ("Ocharchilik komissiyasiga sovet hukumati yetarli mablag‘ ajratgan.", False)],
      "III noto‘g‘ri: komissiyaga tegishli mablag‘ ajratilmagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Turkiston ASSR haqidagi Nizom", "TKP tashkiliy syezdi", "Ocharchilikka qarshi komissiya", "Musulmonlar byurosi tuzildi", "Risqulovning «Turk Respublikasi» taklifi", "RKP(b) X syezdi"],
      "1918-yil aprel → iyun → noyabr → 1919-yil mart → 1920-yil yanvar → 1921-yil mart.")
t.VENN("«Harbiy kommunizm»", "Yangi iqtisodiy siyosat (NEP)",
       [("oziq-ovqat razvyorstkasi", 1), ("mehnat militarizatsiyasi", 1),
        ("oziq-ovqat solig‘i", 2), ("dehqonlarga bir qadar erkinlik", 2),
        ("sovet hokimiyatining iqtisodiy siyosati", 3)],
       "Harbiy kommunizm — razvyorstka, majburiy mehnat; NEP — soliq, erkinlik.")
