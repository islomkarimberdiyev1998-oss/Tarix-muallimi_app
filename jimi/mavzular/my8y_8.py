from qlib import Topic, PLACES, REG
TOPICS = {}

# 23 Yevropada me’morchilik va san’at
t = Topic('y8j23', 8023); TOPICS['y8j23'] = t
t.B("X–XIII asrlardagi cherkovlar qaysi uslubda qurilgan?", "roman", "gotika", "barokko", "klassitsizm", "Roman uslubida.")
t.B("Roman uslubidagi inshootlar tuzilishining asosini nima tashkil etgan?", "arkali gumbaz va minoralar", "vitrajli oynalar", "uchli yoylar", "yupqa devorlar", "Arkali gumbaz va minoralar.")
t.B("Roman uslubidagi cherkov xonalari nima uchun qorong‘i bo‘lgan?", "derazalar uchun kam joy qoldirilgani uchun", "vitrajlar qora bo‘lgani uchun", "yer ostida qurilgani uchun", "chiroq taqiqlangani uchun", "Derazalarga kam joy qoldirilgan.")
t.B("Gotika uslubi qachon paydo bo‘lgan?", "XII asrda", "X asrda", "XIII asrda", "XV asrda", "XII asrda paydo bo‘lib, XIII asrda mukammallikka erishgan.")
t.B("Gotika cherkovlarining uchli minoralari balandligi qanchagacha bo‘lgan?", "150 m gacha", "50 m gacha", "300 m gacha", "20 m gacha", "150 m gacha.")
t.B("Gotika cherkovlarining yupqa devorlari nima bilan to‘ldirilgan?", "vitrajli oynalar", "mozaika", "gilamlar", "freskalar", "Vitrajli oynalar bilan.")
t.B("Birinchi g‘ishtli gotika ibodatxonasi qayerda bo‘lgan?", "Lyubekda", "Parijda", "Milanda", "Londonda", "XIII asrda Lyubekdagi cherkov.")
t.B("Germaniyada gotika inshootlari nima uchun g‘ishtdan qurila boshlangan?", "tosh yetishmasligi tufayli", "g‘isht arzon bo‘lgani uchun", "papa buyrug‘i bilan", "zilzila xavfi tufayli", "Tosh yetishmagan.")
t.B("Italiyadagi mashhur gotika inshooti qaysi?", "Milan sobori", "Reyms sobori", "Linkoln sobori", "Vestminster abbatligi", "Milan sobori.")
t.B("Qal’aning kirish darvozasini himoya qiladigan qo‘shimcha istehkom nima deb atalgan?", "barbakan", "mashikuli", "vitraj", "manor", "Barbakan.")
t.B("Dushmanga o‘q, tosh otish, qaynoq suv quyish joylari nima deb atalgan?", "mashikuli", "barbakan", "akveduk", "freska", "Mashikulilar.")
t.B("Dastlabki tosh qal’alar qayerda bunyod etilgan?", "Italiya va Fransiyaning janubida", "Angliyada", "Germaniya shimolida", "Ispaniyada", "Italiya va Fransiya janubida.")
t.B("Kusi qal’asi markaziy minorasining balandligi qancha bo‘lgan?", "64 m", "31 m", "7 m", "150 m", "64 m (kengligi 31 m, devori 7 m).")
t.B("O‘rta asrlarda «tasvir savodsizlar uchun ...» deb ta’kidlangan. Davomini toping.", "adabiyotdir", "ibodatdir", "o‘yindir", "maktabdir", "«Tasvir savodsizlar uchun adabiyotdir».")
t.B("Ko‘ngilochar tomosha qo‘yuvchilar Germaniyada qanday atalgan?", "shpilman", "jonglyor", "menestrel", "akrobat", "Shpilman.")
t.B("Ko‘ngilochar tomosha qo‘yuvchilar Angliyada qanday atalgan?", "menestrel", "shpilman", "jonglyor", "dorboz", "Menestrel.")
t.B("Jonglyor va shpilmanlar faoliyatining gullagan davri qachon?", "XIII–XV asrlar", "X–XI asrlar", "XVI–XVII asrlar", "IX asr", "XIII–XV asrlar.")
t.B("Qo‘g‘irchoq teatri san’ati qachon paydo bo‘lgan?", "XIV–XV asrlarda", "X asrda", "XII asrda", "XVII asrda", "XIV–XV asrlarda.")
t.NAT("Gotika cherkovlari tashqarisiga yarim arka shaklidagi tayanch ustunlar o‘rnatildi.", "tom og‘irligi taqsimlanib, qalin devorlarga zarurat yo‘qoldi", "cherkovlar pastlashdi", "derazalar yopildi", "cherkovlar qorong‘i bo‘ldi", "Inshoot yengil va ko‘kka cho‘zilgan bo‘ldi.")
t.NAT("Shaharlar o‘rtasida cherkovni katta va baland qurish bo‘yicha raqobat yuzaga keldi.", "cherkov balandligi shaharning kuchi va boyligidan dalolat bergan", "cherkov qurilishi to‘xtadi", "shaharlar birlashdi", "faqat qal’alar qurildi", "Cherkov – shahar boyligi ramzi.")
t.NAT("Rim papasining farmoni bilan ruhoniylarning sahnaga chiqishi taqiqlandi.", "oddiy shahar aholisi aktyorlik vazifalarini bajara boshladi", "teatr butunlay yo‘qoldi", "ruhoniylar bozorga chiqdi", "jonglyorlar taqiqlandi", "Aktyorlar oddiy shaharliklar bo‘ldi.")
t.NAT("Aksariyat odamlar savodsiz edi.", "xristianlik haqida ma’lumot berishning eng yaxshi usuli rasm, tasvir va haykallar bo‘ldi", "kitoblar ko‘p chop etildi", "cherkovlar bezaksiz qurildi", "maktablar yopildi", "Tasvir – savodsizlar adabiyoti.")
t.TF("Vitrajlarda diniy manzaralar bilan birga kundalik hayot manzaralari ham tasvirlangan.", True, "To‘g‘ri.")
t.TF("Feodal qal’alari dastlab toshdan, keyinchalik yog‘ochdan qurilgan.", False, "Noto‘g‘ri: dastlab yog‘ochdan, keyin toshdan.")
t.TF4([("Gotika inshootlari bir necha avlod tomonidan, ba’zan bir asr qurilgan.", True), ("Roman cherkovlari qalin devorlari tufayli qal’alarga o‘xshagan.", True),
       ("Cherkov jonglyorlar chiqishlarini butunlay yo‘q qilgan.", False), ("Sayyor truppalarda akrobat va dorbozlar ham bo‘lgan.", True)],
      "3-noto‘g‘ri: cherkov jonglyorlar chiqishlarini yo‘q qila olmagan.")
t.MUL([("Vorms va Mayns soborlari roman me’morchiligining mashhur yodgorliklari.", True),
       ("Bryusseldagi shahar meriyasi gotikaning dunyoviy yodgorligi.", True),
       ("Kusi qal’asi Germaniyaning janubida qurilgan.", False)],
      "III noto‘g‘ri: Kusi qal’asi Fransiyaning shimolida, XIII asr boshida qurilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Roman uslubidagi cherkovlar qurilishi boshlandi", "Gotika uslubi paydo bo‘ldi", "Lyubekda birinchi g‘ishtli gotika ibodatxonasi qurildi", "Qo‘g‘irchoq teatri paydo bo‘ldi"],
      "X asr → XII asr → XIII asr → XIV–XV asrlar.")
t.MATCH("Yodgorliklarni mamlakati bilan moslashtiring.", ["Reyms sobori", "Linkoln sobori", "Milan sobori", "Vorms sobori"],
        ["Fransiya", "Angliya", "Italiya", "Germaniya", "Ispaniya"], 'abcd',
        "Reyms – Fransiya; Linkoln – Angliya; Milan – Italiya; Vorms – Germaniya.")
t.VENN("Roman uslubi", "Gotika uslubi",
       [("qalin devor va baland ustunlar", 1), ("qorong‘i xonalar", 1),
        ("vitrajli ulkan derazalar", 2), ("150 m gacha uchli minoralar", 2),
        ("cherkov qurilishida qo‘llanilgan", 3)],
       "Roman – qalin devor, qorong‘i; gotika – vitraj, uchli minora; ikkalasi – cherkov uslubi.")
t.MAPMATCH('europe', ['Lyubek', 'Milan', 'London', 'Tuluza'],
           ["birinchi g‘ishtli gotika ibodatxonasi qurilgan shahar", "Italiyadagi mashhur gotika sobori shahri", "Vestminster abbatligi joylashgan shahar", "roman uslubidagi mashhur Fransiya sobori shahri"],
           "1 – Lyubek; 2 – Milan; 3 – London; 4 – Tuluza.")
