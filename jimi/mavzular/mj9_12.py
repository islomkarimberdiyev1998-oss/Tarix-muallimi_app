from qlib import Topic
TOPICS = {}
EU = 'europe'; W = 'globe2'

# 38 Moddiy ishlab chiqarishda texnika va fan taraqqiyoti
t = Topic('e9j38', 9138); TOPICS['e9j38'] = t
t.B("Britaniya va AQSHning yirik shaharlarida tramvay qachondan ishlatila boshlangan?", "1895-yildan", "1876-yildan", "1903-yildan", "1889-yildan", "1895-yildan.")
t.B("1876-yilda «elektr shami» deb atalgan lampani kim ixtiro qilgan?", "P. N. Yablochkov", "T. Edison", "A. Popov", "A. Bell", "Rus olimi P. N. Yablochkov.")
t.B("Ko‘mir tolali cho‘g‘lanish lampasini kim yaratgan?", "T. Edison", "Yablochkov", "Tomson", "Daymler", "Amerikalik T. Edison.")
t.B("Temir-betonni kim ixtiro etgan deb hisoblanadi?", "fransuz bog‘boni Monye", "Eyfel", "Edison", "Kirxgof", "Fransuz bog‘boni Monye.")
t.B("1889-yilda Parijdagi Jahon ko‘rgazmasi uchun 300 metrlik minorani kim qurgan?", "Eyfel", "Monye", "Rodin", "Bell", "Fransuz muhandisi Eyfel.")
t.B("1880-yilda Alp tog‘laridagi qaysi dovon ostida 15 km lik tunnel qurilgan?", "Sen-Gotard", "Simplon", "Brenner", "Monblan", "Sen-Gotard dovoni ostida.")
t.B("Metallurgiyada avtomatlashtirishni kim yaratgan?", "R. Kirxgof", "I. A. Time", "L. Bakeland", "R. Dizel", "Nemis olimi R. Kirxgof.")
t.B("Aluminiy elektrolit yo‘li bilan qachon ajratib olingan?", "1886-yilda", "1897-yilda", "1876-yilda", "1903-yilda", "1886-yilda.")
t.B("Plastmassa olish yo‘lini kim topgan?", "L. Bakeland", "R. Kirxgof", "A. Nobel", "G. Daymler", "L. Bakeland (Belgiya).")
t.B("Avtomobil, motorli qayiq va mototsikl dvigatellarini yaratgan nemis olimi kim?", "G. Daymler", "R. Dizel", "Tomson", "Gers", "G. Daymler.")
t.B("1897-yilda o‘z-o‘zidan alangalanuvchi yangi dvigatelni kim yaratgan?", "R. Dizel", "G. Daymler", "Edison", "Mojayskiy", "R. Dizel.")
t.B("1903-yilda samolyotda uchgan aka-ukalar kimlar?", "Uilber va Orvill Raytlar", "Lyumyerlar", "Kyurilar", "Mongolfyelar", "Uilber va Orvill Raytlar.")
t.B("Elektromagnit to‘lqinlar tarqalishini birinchi bo‘lib tajribada isbotlagan nemis olimi kim?", "G. Gers", "A. Popov", "G. Markoni", "A. Bell", "G. Gers.")
t.B("Simsiz telegrafni Britaniyada kim ixtiro qilgan?", "G. Markoni", "A. Popov", "A. Bell", "Edison", "G. Markoni.")
t.B("Telefon apparatiga birinchi bo‘lib imtiyoznoma olgan kim?", "A. Bell", "Edison", "Markoni", "Popov", "Shotlandiyada tug‘ilgan A. Bell.")
t.B("Ovoz yozib olish va eshittirish apparati — fonografni kim yaratgan?", "T. Edison", "A. Bell", "Markoni", "Popov", "T. Edison.")
t.B("1884-yilda piroksilinli tutunsiz poroxni tayyorlagan fransuz olimi kim?", "Vyelye", "Nobel", "Mendeleyev", "Paster", "Vyelye.")
t.B("1888-yilda dinamitni kim yaratgan?", "A. Nobel", "Vyelye", "Mendeleyev", "Bakeland", "Shvetsiyalik muhandis A. Nobel.")
t.B("XX asr boshidagi samolyotlar soatiga qanchagacha tezlik bilan uchgan?", "220 km gacha", "50 km gacha", "1000 km gacha", "100 km gacha", "220 km gacha.")
t.NAT("Magazinli miltiqdan tez otishda tutun tarqalmay, nishon ko‘rinmay qolardi.", "harbiy amaliyot tutunsiz porox kashf etish vazifasini qo‘ydi", "miltiqlar taqiqlandi", "to‘plar bekor qilindi", "qilichlarga qaytildi", "Tutunsiz porox yaratildi.")
t.TF("Nyu-Yorkda Edison qurgan birinchi issiqlik elektr stansiyasi yuzlarcha iste’molchilarni energiya bilan ta’minlagan.", True, "To‘g‘ri.")
t.TF("Rossiyada tutunsiz poroxning sirini Nobel topgan.", False, "Noto‘g‘ri: uni Rossiyada D. I. Mendeleyev mustaqil ravishda topgan.")
t.MUL([("Metall kesish jarayonini ilmiy tekshirishga rus olimi I. A. Time asos solgan.", True),
       ("Raketaplanni N. I. Kibalchich yaratgan.", True),
       ("Tank jang sharoitida birinchi marta nemislar tomonidan ishlatilgan.", False)],
      "III noto‘g‘ri: tankni birinchi marta inglizlar ishlatgan.")
t.CHR("Kashfiyotlarni xronologik tartibda joylashtiring.", ["«Elektr shami»", "Sen-Gotard tunneli", "Tutunsiz porox", "Aluminiy olish", "Dinamit", "Eyfel minorasi", "Dizel dvigateli", "Raytlar parvozi"],
      "1876 → 1880 → 1884 → 1886 → 1888 → 1889 → 1897 → 1903.")
t.MATCH("Ixtirochilarni ixtirolari bilan moslashtiring.", ["A. Bell", "G. Markoni", "R. Dizel", "A. Nobel"],
        ["dinamit", "simsiz telegraf", "telefon", "o‘z-o‘zidan alangalanuvchi dvigatel"], "cbda",
        "Bell — telefon; Markoni — simsiz telegraf; Dizel — dvigatel; Nobel — dinamit.")
t.MAPMATCH(W, ['Parij', 'Nyu-York', 'Panama kanali'],
           ["1889-yilgi Jahon ko‘rgazmasi uchun 300 metrlik minora qurilgan shahar", "Edison birinchi issiqlik elektr stansiyasini qurgan shahar", "Atlantika va Tinch okeanlarini tutashtiruvchi kanal"],
           "1 – Parij; 2 – Nyu-York; 3 – Panama kanali.")
t.VENN("T. Edison ixtirolari", "A. Popov ixtirolari",
       [("ko‘mir tolali cho‘g‘lanish lampasi", 1), ("fonograf", 1),
        ("simsiz aloqa uchun uzatgich va qabul qilgich", 2), ("radioga asos solgan", 2),
        ("XIX asr oxiridagi texnik kashfiyot", 3)],
       "Edison — lampa, fonograf; Popov — radio.")

# 39 Aniq va tabiiy fanlar rivoji
t = Topic('e9j39', 9139); TOPICS['e9j39'] = t
t.B("Fizika bilan kimyo chegarasida qanday mustaqil fan paydo bo‘lgan?", "fizika-kimyo", "biokimyo", "geofizika", "astrofizika", "Fizika-kimyo.")
t.B("1904-yilda qanotning ko‘tarish kuchi formulasini kashf qilgan rus olimi kim?", "N. Y. Jukovskiy", "N. I. Lobachevskiy", "P. N. Lebedev", "A. S. Popov", "N. Y. Jukovskiy.")
t.B("Yorug‘likning elektromagnit nazariyasini isbotlagan olim kim?", "P. N. Lebedev", "Jukovskiy", "Kurks", "Tomson", "P. N. Lebedev.")
t.B("1870-yilda katod nurlarini kashf etgan ingliz olimi kim?", "U. Kurks", "J. Tomson", "E. Rezerford", "N. Bor", "U. Kurks.")
t.B("1897-yilda katod nurlari elektronlar oqimi ekanini aniqlagan olim kim?", "J. Tomson", "U. Kurks", "Bekkerel", "Rentgen", "Ingliz olimi J. Tomson.")
t.B("Kimyoviy elementlarning davriy sistemasini kim yaratgan?", "D. I. Mendeleyev", "Bekkerel", "Kyuri", "Arrenius", "D. I. Mendeleyev, 1869-yilda.")
t.B("Uran atomlari nur chiqarishini aniqlagan fransuz fizigi kim?", "A. Bekkerel", "P. Kyuri", "Rentgen", "Tomson", "A. Bekkerel.")
t.B("Muayyan atomlarning bu xususiyatini radioaktivlik deb atagan olim kim?", "M. Sklodovskaya-Kyuri", "A. Bekkerel", "E. Rezerford", "N. Bor", "M. Sklodovskaya-Kyuri.")
t.B("Kyurilar ajratgan elementlardan biri M. Sklodovskaya-Kyurining vatani sharafiga qanday atalgan?", "poloniy", "radiy", "uran", "kyuriy", "Poloniy (Polsha sharafiga).")
t.B("Atomning planetar modelini kim yaratgan?", "E. Rezerford", "N. Bor", "J. Tomson", "A. Eynshteyn", "Ingliz fizigi E. Rezerford.")
t.B("Nisbiylik nazariyasining asosiy g‘oyalarini 1905-yilda kim e’lon qilgan?", "A. Eynshteyn", "N. Bor", "Rezerford", "Plank", "Nemis olimi A. Eynshteyn.")
t.B("Genetika rivojlanishiga kimning irsiyat qonunlari asos solgan?", "G. Mendel", "Ch. Darvin", "I. Pavlov", "L. Paster", "G. Mendel.")
t.B("Organizmlarning hujayrali tuzilishi haqidagi kashfiyot kimga tegishli?", "T. Shvan", "Ch. Darvin", "Paster", "Virxov", "Nemis olimi T. Shvan.")
t.B("«Turlarning kelib chiqishi» asari muallifi kim?", "Charlz Darvin", "G. Mendel", "T. Shvan", "R. Kox", "Charlz Darvin.")
t.B("Hozirgi zamon mikrobiologiya va immunologiyasining asoschisi kim?", "Lui Paster", "Robert Kox", "Mechnikov", "Virxov", "Lui Paster.")
t.B("1895-yilda «X nurlar»ni kashf etgan nemis fizigi kim?", "Vilgelm Konrad Rentgen", "A. Bekkerel", "J. Tomson", "Maksvell", "V. K. Rentgen; fiziklar orasida birinchi Nobel mukofoti.")
t.B("Sil kasalligi batsillasini kashf qilgan nemis olimi kim?", "Robert Kox", "Lui Paster", "F. Lyofler", "K. Eber", "Robert Kox (1843–1910).")
t.B("Suyuqlikni 60–80 °C gacha qizdirib tezda sovitish usuli qanday ataladi?", "pasterlash", "sterilizatsiya", "gidratlanish", "dissotsiatsiya", "Pasterlash.")
t.NAT("Rentgen ko‘rinmas nurlarni kashf etib, uning nomi bilan apparat yaratildi.", "shifokorlar ichki jarohatlar va suyak sinishlarini ko‘ra oladigan bo‘ldi", "tibbiyot rivoji to‘xtadi", "radioaktivlik kashf etildi", "elektron kashf etildi", "Rentgen apparati tibbiyotda keng qo‘llanildi.")
t.TF("Daniyalik fizik N. Bor modelida elektronlar bir orbitadan ikkinchisiga sakrab, energiya kvantini chiqaradi.", True, "To‘g‘ri.")
t.TF("Eynshteyn nazariyasiga ko‘ra tezlik yorug‘lik tezligiga yaqinlashganda vaqt tezlashadi.", False, "Noto‘g‘ri: vaqtning kechishi sekinlashadi.")
t.MUL([("I. P. Pavlov inson xatti-harakati negizida bosh miya qobig‘idagi fiziologik jarayonlar yotishini isbotlagan.", True),
       ("1887-yilda shved olimi S. Arrenius elektrolitik dissotsiatsiya nazariyasini yaratgan.", True),
       ("Paster mikroblarning achish jarayonidagi rolini rad etgan.", False)],
      "III noto‘g‘ri: Paster achish mikroblar keltirib chiqaradigan biologik jarayon ekanini isbotlagan.")
t.CHR("Kashfiyotlarni xronologik tartibda joylashtiring.", ["Mendeleyev davriy sistemasi", "Kurks katod nurlarini kashf etdi", "Rentgen «X nurlar»ni kashf etdi", "Tomson elektronlarni aniqladi", "Eynshteyn nisbiylik nazariyasi"],
      "1869 → 1870 → 1895 → 1897 → 1905.")
t.MATCH("Olimlarni kashfiyotlari bilan moslashtiring.", ["D. I. Mendeleyev", "E. Rezerford", "G. Mendel", "Lui Paster"],
        ["irsiyat qonunlari", "emlash va pasterlash usullari", "davriy sistema", "atomning planetar modeli"], "cdab",
        "Mendeleyev — davriy sistema; Rezerford — planetar model; Mendel — irsiyat; Paster — emlash.")
t.VENN("Mariya Sklodovskaya-Kyuri", "Pyer Kyuri",
       [("«radioaktivlik» atamasini kiritgan", 1), ("Polshadan bo‘lgan", 1),
        ("atoqli fransuz fizigi", 2), ("Mariyaning eri", 2),
        ("poloniy va radiyni ajratgan", 3)],
       "Mariya — radioaktivlik, Polsha; Pyer — fransuz fizigi; birga poloniy va radiyni ajratgan.")

# 40 Xalq ta’limi. Gumanitar fanlar. San’at
t = Topic('e9j40', 9140); TOPICS['e9j40'] = t
t.B("Rivojlangan mamlakatlarda necha yoshgacha bo‘lgan bolalar uchun majburiy va bepul ta’lim joriy qilingan?", "12–13 yoshgacha", "16 yoshgacha", "10 yoshgacha", "18 yoshgacha", "12–13 yoshgacha.")
t.B("AQSH maorif tizimi qanday ruhda edi?", "irqchilik ruhida", "tenglik ruhida", "diniy ruhda", "militarizm ruhida", "Qora tanlilar uchun alohida maktablar bo‘lgan.")
t.B("Irqchilikka qarshi kurash qaysi asarda yaqqol ifodasini topgan?", "«Tom tog‘aning kulbasi»", "«Temir tovon»", "«Mutafakkir»", "«Salomeya»", "G. Bicher-Stouning «Tom tog‘aning kulbasi».")
t.B("«Zardusht tavallosi» asarini yozgan faylasuf kim?", "Fridrix Nitsshe", "O. Shpengler", "Z. Freyd", "Dekart", "Fridrix Nitsshe.")
t.B("«Yevropa quyoshining botishi» asari muallifi kim?", "O. Shpengler", "F. Nitsshe", "Z. Freyd", "R. Kipling", "O. Shpengler.")
t.B("Barcha madaniyatlarni yevropalashtirish g‘oyasi qanday ataladi?", "yevrosentrizm", "psixoanaliz", "impressionizm", "dekadentlik", "Yevrosentrizm.")
t.B("Psixoanaliz nazariyasining asoschisi kim?", "Z. Freyd", "F. Nitsshe", "O. Shpengler", "I. Pavlov", "Avstriyalik Z. Freyd.")
t.B("«Oq tanli kishining burch anduhi» kitobi muallifi kim?", "R. Kipling", "B. Shou", "J. London", "M. Tven", "Ingliz yozuvchisi R. Kipling.")
t.B("«Salomeya», «Elektra» asarlari muallifi bo‘lgan bastakor kim?", "Rixard Shtraus", "Gustav Maler", "Skryabin", "Raxmaninov", "Rixard Shtraus.")
t.B("«Qazo qilgan bolalar haqida qo‘shiq» asarini yozgan avstriyalik simfonist kim?", "Gustav Maler", "R. Shtraus", "Skryabin", "Raxmaninov", "Gustav Maler.")
t.B("Taassurotni sof holda aks ettiruvchi rassomchilik oqimi qanday atalgan?", "impressionizm", "naturalizm", "dekadentlik", "realizm", "Impressionizm.")
t.B("Impressionizmning iste’dodli namoyandalari kimlar?", "Mane, Mone, Renuar, Pissaro", "Sezann, Gogen, Van Gog", "Roden, Eyfel", "Shtraus, Maler", "Eduard Mane, Klod Mone, Ogyust Renuar, Kamil Pissaro.")
t.B("Ipak matoga rasm solishning qulay usulini yaratgan xitoylik rassom kim?", "Jen Bonyan", "Lu Sin", "Sun Yat Sen", "Roka Tokutomi", "Jen Bonyan.")
t.B("«Mutafakkir» haykali muallifi kim?", "O. Roden", "Eyfel", "Mone", "Sezann", "Fransuz haykaltaroshi O. Roden.")
t.B("Inson huquqi va manfaatlariga oid tushuncha qanday ataladi?", "gumanitar", "yevrosentrizm", "individ", "psixoanaliz", "Gumanitar.")
t.NAT("Texnika taraqqiyoti yuqori saviyali mutaxassislarga ehtiyojni kuchaytirdi.", "12–13 yoshgacha bepul majburiy ta’lim joriy qilinib, savodxonlik oshdi", "maktablar yopildi", "ta’lim pullik qilindi", "faqat zodagonlar o‘qidi", "Aholi savodxonligi oshdi.")
t.TF("Freyd ta’limotiga ko‘ra insonning psixik hayoti tug‘ma, ongsiz mayllarga bog‘liq.", True, "To‘g‘ri.")
t.TF("Impressionistlar asosiy maqsad sifatida insonning ichki dunyosini va ijtimoiy o‘rnini ko‘rsatishni qo‘ygan.", False, "Noto‘g‘ri: ular buni o‘z oldilariga maqsad qilib qo‘ymagan.")
t.MUL([("Pol Sezann, Pol Gogen va Vinsent van Gog mehnat ahlini alohida tasvirlagan.", True),
       ("R. Shtraus motsartcha operani qaytadan tiklagan.", True),
       ("Shpengler yevrosentrizmni to‘liq qo‘llab-quvvatlagan.", False)],
      "III noto‘g‘ri: u yevrosentrizmga qarshi chiqqan.")
t.MATCH("Asarlarni mualliflari bilan moslashtiring.", ["«Zardusht tavallosi»", "«Yevropa quyoshining botishi»", "«Oq tanli kishining burch anduhi»", "«Mutafakkir»"],
        ["R. Kipling", "O. Roden", "F. Nitsshe", "O. Shpengler"], "cdab",
        "Nitsshe — «Zardusht tavallosi»; Shpengler — «Yevropa quyoshining botishi»; Kipling — «Oq tanli...»; Roden — «Mutafakkir».")
t.VENN("Impressionistlar", "Real hayotni aks ettirgan rassomlar",
       [("Mane, Mone, Renuar, Pissaro", 1), ("quyosh yog‘dusini aks ettirishning yangi vositalarini topgan", 1),
        ("Sezann, Gogen, Van Gog", 2), ("mehnat ahlini alohida tasvirlagan", 2),
        ("XIX asr oxiri – XX asr boshi rassomchiligi", 3)],
       "Impressionistlar — taassurot; realistlar — mehnat ahli.")

# 41 Adabiyot
t = Topic('e9j41', 9141); TOPICS['e9j41'] = t
t.B("XIX asr oxiri – XX asr boshida Yevropa madaniy hayotida qaysi oqimlar o‘rtasida kurash avj olgan?", "realistik va dekadentlik", "romantizm va klassitsizm", "impressionizm va kubizm", "sentimentalizm va barokko", "Realistik oqim va dekadentlik.")
t.B("Bu davr adabiyoti qanday nom olgan?", "«tanqidiy realizm»", "«romantizm»", "«klassitsizm»", "«futurizm»", "«Tanqidiy realizm».")
t.B("«Hayot», «Azizim», «Mont-Oriol» asarlari muallifi kim?", "Gi de Mopassan", "Emil Zolya", "A. Frans", "V. Gyugo", "Gi de Mopassan.")
t.B("«Temir tovon» va «Marten Iden» romanlari muallifi kim?", "J. London", "M. Tven", "B. Shou", "S. Kreyn", "Amerikalik J. London.")
t.B("«Sodiq fuqaro» romani muallifi bo‘lgan nemis yozuvchisi kim?", "G. Mann", "A. Frans", "Nitsshe", "Kipling", "G. Mann.")
t.B("«Silvester Bonnarning jinoyati» asari muallifi kim?", "A. Frans", "Gi de Mopassan", "E. Zolya", "V. Gyugo", "A. Frans.")
t.B("«Olomon qiluvchi Qo‘shma Shtatlar» maqolasi muallifi bo‘lgan satirik kim?", "M. Tven", "J. London", "S. Kreyn", "F. Norris", "M. Tven.")
t.B("«Halokat» romani mashhur bo‘lgan hind yozuvchisi kim?", "R. Tagor", "Lu Sin", "Tilak", "Roka Tokutomi", "R. Tagor.")
t.B("«Qurol va inson», «Shayton shogirdi» asarlari muallifi kim?", "Bernard Shou", "R. Kipling", "J. London", "A. Chexov", "Ingliz dramaturgi Bernard Shou.")
t.B("«Dahshatli yil», «To‘qson uchinchi yil» asarlari muallifi kim?", "Viktor Gyugo", "Jyul Vern", "Emil Zolya", "A. Frans", "Viktor Gyugo.")
t.B("Ilmiy-fantastik romanchilikning yirik vakili kim?", "Jyul Vern", "V. Gyugo", "Mopassan", "B. Shou", "Jyul Vern.")
t.B("«Uch opa-singil», «Olchazor bog‘i» pyesalari muallifi kim?", "A. P. Chexov", "L. N. Tolstoy", "F. M. Dostoyevskiy", "Gorkiy", "A. P. Chexov.")
t.B("«Kurosivo» romani muallifi bo‘lgan yapon yozuvchisi kim?", "Roka Tokutomi", "Naoe Kinosita", "Lu Sin", "Tagor", "Roka Tokutomi.")
t.B("20 jildli «Rugon-Makkarlar» asarini yozgan naturalist kim?", "Emil Zolya", "Gi de Mopassan", "A. Frans", "V. Gyugo", "Emil Zolya.")
t.B("«Jasoratning qonli belgisi» asari muallifi bo‘lgan amerikalik naturalist kim?", "Stiven Kreyn", "Frenk Norris", "J. London", "M. Tven", "Stiven Kreyn.")
t.B("Dekadentlik oqimi vakillari kimlar edi?", "P. Verlen, A. Rembo, S. Mallarme", "E. Zolya, Mopassan", "Tolstoy, Chexov", "Shou, Kipling", "Verlen, Rembo, Mallarme.")
t.B("Tanazzul va umidsizlik kayfiyatini aks ettiruvchi oqim qanday atalgan?", "dekadentlik", "naturalizm", "tanqidiy realizm", "demokratik adabiyot", "Dekadentlik.")
t.NAT("Xalq dekadentlik ruhidagi asarlarni qabul qilmadi.", "turmushni aniq ifodalaydigan realistik asarlarga ehtiyoj ortdi", "dekadentlik kuchaydi", "adabiyot rivojlanishdan to‘xtadi", "naturalizm yo‘qoldi", "Bu davr «tanqidiy realizm» nomini oldi.")
t.TF("R. Tagorning butun ijodi milliy mustaqillikka otashin chaqiriqdan iborat edi.", True, "To‘g‘ri.")
t.TF("«Tom tog‘aning kulbasi» romanida Fransiya inqilobi tasvirlangan.", False, "Noto‘g‘ri: unda XIX asr Amerika qullari va quldorlari hayoti yoritilgan.")
t.MUL([("Xitoylik Lu Sin ijodi kambag‘allarga chuqur hamdardlik ruhi bilan sug‘orilgan.", True),
       ("Italiyada naturalizm namoyandalari Luiji Kapuana va Jovanni Verga edi.", True),
       ("Emil Zolyaning «Jerminal» romani dekadentlik namunasi hisoblanadi.", False)],
      "III noto‘g‘ri: «Jerminal» naturalist Zolya ijodining cho‘qqisi.")
t.MATCH("Yozuvchilarni oqimlar bilan moslashtiring.", ["Emil Zolya", "P. Verlen", "Gi de Mopassan", "G. Bicher-Stou"],
        ["demokratik adabiyot", "naturalizm", "dekadentlik", "tanqidiy realizm"], "bcda",
        "Zolya — naturalizm; Verlen — dekadentlik; Mopassan — tanqidiy realizm; Bicher-Stou — demokratik adabiyot.")
t.VENN("Jek London", "Mark Tven",
       [("«Temir tovon» romani", 1), ("«Dengiz bo‘risi» asari", 1),
        ("«Olomon qiluvchi Qo‘shma Shtatlar» maqolasi", 2), ("achchiq va darg‘azab satira ustasi", 2),
        ("amerikalik yozuvchi", 3)],
       "London — «Temir tovon»; Tven — satira; ikkalasi amerikalik.")
