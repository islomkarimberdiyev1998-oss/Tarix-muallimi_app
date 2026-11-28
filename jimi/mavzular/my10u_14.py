from qlib import Topic, PLACES, REG
TOPICS = {}

# 26-mavzu. Frontdagi jasorat
t = Topic('y10u26', 10026); TOPICS['y10u26'] = t
t.B("Brest qal’asi mudofaasida halok bo‘lgan o‘zbekistonlik kim?", "Avazmat Niyozmatov", "Qo‘chqor Turdiyev", "Kamol Turg‘unov", "Botir Boboyev", "Avazmat Niyozmatov.")
t.B("1941-yil yozida Samarqandda tuzilgan diviziya qayerda jangga kirgan?", "Yelnya yaqinida", "Stalingrad ostonasida", "Kursk yoyida", "Brestda", "Yelnya yaqinida.")
t.B("O‘zbekistonda nechta alohida o‘qchilar brigadasi tashkil etilgan?", "9 ta", "5 ta", "90 ta", "14 ta", "9 ta brigada va 5 ta kavaleriya diviziyasi.")
t.B("Zebo G‘aniyeva nechta fashistni yo‘q qilgan?", "129 nafar", "300 nafar", "11 nafar", "1000 nafar", "129 nafar.")
t.B("«Moskva mudofaasi uchun» medali bilan nechta o‘zbekistonlik taqdirlangan?", "1 753", "2 738", "301", "200 ming", "1 753 kishi.")
t.B("O‘zbeklardan birinchi bo‘lib Sovet Ittifoqi Qahramoni unvonini olgan kim?", "Qo‘chqor Turdiyev", "Sobir Rahimov", "Zebo G‘aniyeva", "Samig‘ Abdullayev", "Qo‘chqor Turdiyev, 1942-yil 27-mart.")
t.B("«Sharqlik o‘n bir qahramon tepaligi»da nechta dushman yo‘q qilingan?", "300 nafar", "129 nafar", "1000 nafar", "11 nafar", "300 nafar.")
t.B("Sobir Rahimovga general-mayor unvoni qachon berilgan?", "1943-yil 19-martda", "1945-yil 26-martda", "1965-yilda", "1942-yil 27-martda", "1943-yil 19-mart.")
t.B("Stalingraddagi «Pavlov uyi»ni himoya qilgan o‘zbekistonlik kim?", "Kamol Turg‘unov", "Sobirjon Oxunjonov", "Abdulla Ayupov", "Samig‘ Abdullayev", "Kamol Turg‘unov.")
t.B("«Stalingrad mudofaasi uchun» medali bilan nechta o‘zbekistonlik taqdirlangan?", "2 738", "1 753", "301", "70", "2 738 nafar.")
t.B("Kavkaz janglarida 3 mingga yaqin minani zararsizlantirgan qahramon kim?", "Samig‘ Abdullayev", "Bois Ergashev", "Qudrat Suyunov", "Abdulla Qurbonov", "Samig‘ Abdullayev.")
t.B("Sobir Rahimov qayerda og‘ir yarador bo‘lgan?", "Polshaning Dansig (Gdansk) shahri uchun jangda", "Stalingradda", "Berlinda", "Kurskda", "1945-yil 25-mart, Dansig.")
t.B("Sobir Rahimovga Sovet Ittifoqi Qahramoni unvoni qachon berilgan?", "1965-yilda", "1945-yilda", "1943-yilda", "1999-yilda", "1965-yilda.")
t.B("Oder daryosini birinchilardan bo‘lib kechib o‘tgan o‘zbekistonlik kim?", "Botir Boboyev", "Tojiali Boboyev", "Plis Nurpeysov", "Abdusamat Taymetov", "Botir Boboyev.")
t.B("Kapitulyatsiya Akti va G‘alaba bayrog‘ini Moskvaga olib kelgan uchuvchilar safida qaysi o‘zbek bo‘lgan?", "Abdusamat Taymetov", "Abdusattor Eshonqulov", "Plis Nurpeysov", "Botir Boboyev", "Abdusamat Taymetov.")
t.B("Florens Naytingeyl medaliga sazovor bo‘lgan hamshira kim?", "Rixsixon Mo‘minova", "Zebo G‘aniyeva", "Muqaddam Ashrapova", "Fotima Qosimova", "Rixsixon Mo‘minova.")
t.B("Urush yillarida nechta o‘zbekistonlik Sovet Ittifoqi Qahramoni bo‘lgan?", "301", "70", "1 753", "2 738", "301 nafar.")
t.B("Toshkentda Xotira maydoni qachon bunyod etilgan?", "1999-yilda", "1995-yilda", "2020-yilda", "1945-yilda", "1999-yilda.")
t.B("«G‘alaba bog‘i» yodgorlik majmuasi qachon barpo etilgan?", "2020-yilda", "1999-yilda", "1995-yilda", "2000-yilda", "2020-yilda.")
t.B("Amersfort konslageridagi nechta o‘zbek asiri xotirasiga installyatsiya o‘rnatilgan?", "101 nafar", "301 nafar", "11 nafar", "1000 nafar", "101 nafar.")
t.NAT("Urush boshida askarlar keskin ko‘paydi, kiyim va qurol yetishmadi.", "ular tayyorgarliksiz jangga yuborilib, katta insoniy yo‘qotishlar bo‘ldi", "urush tez tugadi", "yo‘qotishlar bo‘lmadi", "askarlar uyga qaytarildi", "Katta yo‘qotishlar.")
t.NAT("Stalingrad jangi Ikkinchi jahon urushida tub burilish yasadi.", "antigitler koalitsiyasi mustahkamlanib, Britaniya va AQSh ikkinchi frontni ochishga qaror qildi", "Germaniya g‘alaba qildi", "urush to‘xtadi", "SSSR taslim bo‘ldi", "Tub burilish.")
t.NAT("1945-yil 8-mayda Germaniyaning so‘zsiz taslim bo‘lishi haqidagi Akt imzolandi.", "9-may SSSRda «G‘alaba bayrami» deb e’lon qilindi", "urush davom etdi", "Germaniya g‘alaba qildi", "Berlin operatsiyasi boshlandi", "G‘alaba bayrami.")
t.NAT("1999-yildan G‘alaba bayrami boshqacha nishonlana boshlandi.", "u «Xotira va qadrlash kuni» sifatida nishonlanmoqda", "bayram bekor qilindi", "faqat harbiy parad o‘tkaziladi", "u 22-iyunga ko‘chirildi", "Xotira va qadrlash kuni.")
t.TF("Moskva mudofaasidagi 316-o‘qchi diviziya tarkibida Toshkent piyoda askarlar bilim yurti kursantlari bo‘lgan.", True, "To‘g‘ri.")
t.TF("Brigada va diviziyalar 50 yoshdan katta kishilardan tuzilgan.", False, "Noto‘g‘ri: 40 yoshdan katta bo‘lmagan sog‘lom kishilar bilan to‘ldirilgan.")
t.TF4([("90 va 94-alohida o‘qchi brigadalari Moskva va Stalingrad janglarida qatnashgan.", True), ("Mamadali Topivoldiyev razvedkachi partizan bo‘lib, Qahramon unvonini olgan.", True),
       ("Ikkinchi front 1944-yil 6-iyunda ochilgan.", True), ("Sobir Rahimov Berlin osmonida halok bo‘lgan uchuvchi.", False)],
      "4-noto‘g‘ri: Berlin osmonida Plis Nurpeysov halok bo‘lgan; Rahimov Dansigda yarador bo‘lib vafot etgan.")
t.MUL([("70 nafar o‘zbekistonlik uchala darajadagi «Slava» ordeniga sazovor bo‘lgan.", True),
       ("Ahmadjon Mamajonov Italiyadagi Qarshilik harakati qatnashchisi bo‘lgan.", True),
       ("Yaponiyaga qarshi urush 1944-yilda boshlangan.", False)],
      "III noto‘g‘ri: 1945-yil 9-avgustga o‘tar kechasi boshlangan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Qo‘chqor Turdiyevning Trudolyubovkadagi jasorati", "Turdiyevga Qahramon unvoni", "Rahimovga general-mayor unvoni", "ikkinchi front ochildi", "Rahimov Dansigda yarador bo‘ldi", "Berlin operatsiyasi boshlandi"],
      "1941-10-15 → 1942-03-27 → 1943-03-19 → 1944-06-06 → 1945-03-25 → 1945-04-16.")
t.MATCH("Qahramonlarni jasorati bilan moslashtiring.", ["Zebo G‘aniyeva", "Kamol Turg‘unov", "Samig‘ Abdullayev", "Botir Boboyev"],
        ["snayper, 129 fashistni yo‘q qilgan", "«Pavlov uyi» himoyachisi", "3 mingga yaqin minani zararsizlantirgan", "Oderni birinchilardan kechib o‘tgan", "Florens Naytingeyl medali"], 'abcd',
        "G‘aniyeva – snayper; Turg‘unov – Pavlov uyi; Abdullayev – minalar; Boboyev – Oder.")
t.VENN("Moskva mudofaasi", "Stalingrad jangi",
       [("1 753 o‘zbekistonlik medal olgan", 1), ("316-o‘qchi diviziya", 1),
        ("2 738 o‘zbekistonlik medal olgan", 2), ("«Pavlov uyi» himoyasi", 2),
        ("90 va 94-alohida o‘qchi brigadalari qatnashgan", 3)],
       "Moskva – 1 753, 316-diviziya; Stalingrad – 2 738, Pavlov uyi; ikkalasida 90 va 94-brigadalar.")
t.MAPMATCH('ww2', ['Brest', 'Stalingrad', 'Gdansk', 'Berlin'],
           ["Avazmat Niyozmatov mudofaasida halok bo‘lgan qal’a", "Kamol Turg‘unov «Pavlov uyi»ni himoya qilgan shahar", "S. Rahimov og‘ir yarador bo‘lgan Dansig shahri", "Plis Nurpeysov osmonida halok bo‘lgan poytaxt"],
           "1 – Brest; 2 – Stalingrad; 3 – Dansig (Gdansk); 4 – Berlin.")

# 27-mavzu. Sobir Rahimovning dafn qilinishi
t = Topic('y10u27', 10027); TOPICS['y10u27'] = t
t.B("Birinchi o‘zbek generali kim?", "Sobir Rahimov", "Qo‘chqor Turdiyev", "Usmon Yusupov", "Abdusattor Eshonqulov", "Sobir Rahimov.")
t.B("Sobir Rahimovning xoki solingan idish qayerga qo‘yilgan?", "O‘zbekiston Oliy Sovetining zaliga", "Moskvaga", "Gdanskka", "Samarqandga", "Oliy Sovet zaliga.")
t.B("General xoki yonida necha kun davomida o‘n minglab mehnatkashlar bo‘ldi?", "ikki kun", "bir hafta", "bir kun", "o‘n kun", "Ikki kun.")
t.B("Motam mitingida so‘zga chiqqan O‘zbekiston XKS raisi kim?", "Abdurahmonov", "Yusupov", "Lipatov", "Islamov", "Abdurahmonov.")
t.B("Motam mitingida so‘zga chiqqan O‘rta Osiyo harbiy okrugi qo‘mondoni kim?", "general-mayor Lipatov", "Abdurahmonov", "Rahimov", "Yusupov", "General-mayor Lipatov.")
t.B("Mitingda so‘zga chiqqan respublikaning xizmat ko‘rsatgan o‘qituvchisi kim?", "Hasan ota Islamov", "Yo‘ldosh Oxunboboyev", "Abdurahmonov", "Lipatov", "Hasan ota Islamov.")
t.B("O‘zbekiston KP(b) MK sekretari kim edi?", "U. Yusupov", "Abdurahmonov", "Lipatov", "Islamov", "U. Yusupov.")
t.B("Generalning xoki solingan idish nimaning ichiga qo‘yilgan?", "chor qirrali yaxlit marmar tosh", "bronza haykal", "yog‘och sanduq", "shisha idish", "Chor qirrali yaxlit marmar tosh.")
t.B("Ushbu xabar qaysi gazetada chop etilgan?", "«Qizil askar haqiqati»", "«Pravda Vostoka»", "«Qizil O‘zbekiston»", "«Shuhrat»", "«Qizil askar haqiqati».")
t.B("Gazeta xabari qachon chop etilgan?", "1945-yil 30-mayda", "1945-yil 27-mayda", "1945-yil 9-mayda", "1945-yil 26-martda", "1945-yil 30-may, 35-son.")
t.B("Gazeta Sobir Rahimovga qayerda haykal qo‘yilishini xabar qilgan?", "Toshkentda", "Moskvada", "Gdanskda", "Samarqandda", "Toshkentda.")
t.B("Toshkent mehnatkashlari general bilan qachon vidolashgan (xabar sanasi)?", "27-may", "9-may", "26-mart", "19-mart", "Toshkent, 27-may.")
t.NAT("Sobir Rahimov vatan ozodligi uchun kurashda qahramonlarcha halok bo‘ldi.", "Toshkent mehnatkashlari u bilan so‘nggi marta vidolashdi", "uning nomi unutildi", "u Moskvada dafn qilindi", "unga hech qanday hurmat ko‘rsatilmadi", "Toshkentda vidolashuv.")
t.NAT("U. Yusupov so‘zga chiqib bo‘ldi.", "generalning xoki solingan idish marmar tosh ichiga qo‘yildi", "miting bekor qilindi", "xok Moskvaga jo‘natildi", "haykal ochildi", "Xok marmar toshga qo‘yildi.")
t.NAT("O‘zbekiston mehnatkashlari sodiq o‘g‘lining xotirasini abadiy saqlashga ahd qildi.", "Toshkentda generalga haykal qo‘yilishi e’lon qilindi", "uning nomi o‘chirildi", "xotira kuni bekor qilindi", "uning ishi yopildi", "Haykal qo‘yilishi.")
t.TF("Sobir Rahimov gvardiyachi general-mayor bo‘lgan.", True, "To‘g‘ri.")
t.TF("Sobir Rahimovning xoki Gdanskda dafn etilgan.", False, "Noto‘g‘ri: Toshkentga keltirilib, vidolashuv o‘tkazilgan.")
t.TF4([("Generalning xoki yonida o‘n minglab mehnatkashlar bo‘lgan.", True), ("Mitingda Hasan ota Islamov so‘zga chiqqan.", True),
       ("Xabar «Qizil askar haqiqati» gazetasining 35-sonida chiqqan.", True), ("Rahimov birinchi qozoq generali bo‘lgan.", False)],
      "4-noto‘g‘ri: u birinchi o‘zbek generali.")
t.MUL([("Motam mitingida harbiy okrug qo‘mondoni ham qatnashgan.", True),
       ("Gazeta Rahimovni «o‘zbek xalqining sodiq o‘g‘li» deb atagan.", True),
       ("Mitingda Yo‘ldosh Oxunboboyev nutq so‘zlagan.", False)],
      "III noto‘g‘ri: Abdurahmonov, Lipatov, Islamov va Yusupov so‘zga chiqqan.")
t.CHR("Dafn marosimi bosqichlarini tartiblang.", ["xok solingan idish Oliy Sovet zaliga qo‘yildi", "ikki kun davomida xalq vidolashdi", "motam mitingi – nutqlar", "xok marmar tosh ichiga qo‘yildi"],
      "Zal → vidolashuv → miting → marmar tosh.")
t.MATCH("Shaxslarni lavozimi bilan moslashtiring.", ["Abdurahmonov", "Lipatov", "U. Yusupov", "Hasan ota Islamov"],
        ["O‘zbekiston XKS raisi", "O‘rta Osiyo harbiy okrugi qo‘mondoni", "O‘zbekiston KP(b) MK sekretari", "xizmat ko‘rsatgan o‘qituvchi", "Oliy sud raisi"], 'abcd',
        "Abdurahmonov – XKS; Lipatov – okrug; Yusupov – MK; Islamov – o‘qituvchi.")
t.VENN("Qo‘chqor Turdiyev", "Sobir Rahimov",
       [("o‘zbeklardan birinchi Sovet Ittifoqi Qahramoni", 1), ("Trudolyubovka jangi", 1),
        ("birinchi o‘zbek generali", 2), ("Dansig jangida halok bo‘lgan", 2),
        ("Ikkinchi jahon urushi qahramoni", 3)],
       "Turdiyev – birinchi Qahramon; Rahimov – birinchi general; ikkalasi urush qahramoni.")
t.MAPN('uzb', ['Toshkent', 'Samarqand', 'Buxoro', 'Xiva'], "1945-yil mayda general Sobir Rahimov bilan vidolashuv bo‘lgan va haykal qo‘yilishi e’lon qilingan shahar xaritada qaysi raqamda?",
       "Toshkent.")
