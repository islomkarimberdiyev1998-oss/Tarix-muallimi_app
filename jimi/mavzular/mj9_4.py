from qlib import Topic
TOPICS = {}
AF = 'africa'; NA = 'namerica'; W = 'globe'

# 11 Buyuk Britaniyaning siyosiy va iqtisodiy ahvoli
t = Topic('e9j11', 9111); TOPICS['e9j11'] = t
t.B("Buyuk Britaniyada davlatning ichki va tashqi siyosatini kim boshqargan?", "parlament tuzadigan hukumat", "qirol", "Lordlar palatasi", "anglikan cherkovi", "Parlament tuzadigan hukumat.")
t.B("Buyuk Britaniyadagi ikki kuchli partiya qaysilar edi?", "Konservatorlar va Liberallar", "Demokratlar va Respublikachilar", "Leyboristlar va Liberallar", "Torilar va Sotsialistlar", "Konservatorlar va Liberallar.")
t.B("Konservatorlar partiyasining asosiy tayanchi kimlar edi?", "yirik zamindorlar va anglikan cherkovi", "o‘rta sinf", "ishchilar", "fermerlar", "Yirik zamindorlar va anglikan cherkovi.")
t.B("1867-yilgi parlament islohotidan keyin erkak aholining qancha qismi saylov huquqiga ega bo‘ldi?", "50 foizi", "10 foizi", "100 foizi", "25 foizi", "50 foizi.")
t.B("Liberal U. Gladston bosh vazirligi davrida qanday islohot o‘tkazilgan?", "yashirin ovoz berish joriy etilgan", "54 soatlik ish haftasi belgilangan", "Lordlar palatasi vetosi cheklangan", "pensiya joriy etilgan", "Yashirin ovoz berish, tred-yunionlarga huquqlar, maktab islohoti.")
t.B("Dizraeli davrida 1875-yilda haftada necha soatlik ish vaqti belgilangan?", "54 soat", "48 soat", "60 soat", "40 soat", "54 soat.")
t.B("Dizraeli davrida necha yoshdan kichik bolalarni ishga olish taqiqlangan?", "10 yoshdan", "13 yoshdan", "16 yoshdan", "8 yoshdan", "10 yoshdan kichik.")
t.B("Buyuk Britaniya qanday nom bilan mashhur bo‘lgan?", "«Jahon ustaxonasi»", "«Dengizlar bekasi»", "«Yevropa non ombori»", "«Sharq darvozasi»", "«Jahon ustaxonasi».")
t.B("Sanoat ishlab chiqarish hajmi bo‘yicha Britaniya qaysi o‘ringa tushib ketgan?", "3-o‘ringa", "2-o‘ringa", "4-o‘ringa", "1-o‘rinda qolgan", "3-o‘ringa.")
t.B("Chetga kapital chiqarish foydasi tashqi savdo foydasidan necha marta ko‘p bo‘lgan?", "5 marta", "2 marta", "10 marta", "teng bo‘lgan", "5 marta.")
t.B("Germaniyaning Britaniyaga eksporti 20 yil ichida qanchaga ko‘paygan?", "41 foizga", "2 marta", "5 marta", "10 foizga", "41 foiz; AQSHdan eksport ikki martadan ziyod.")
t.B("Jahon savdosida hisob-kitob qaysi pul birligida amalga oshirilgan?", "funt sterling", "dollar", "frank", "marka", "Funt sterling.")
t.NAT("Ingliz sarmoyadorlari kapitalni mustamlakalarga chiqarishni afzal ko‘rdi.", "Britaniyadagi korxonalar zamonaviy texnika bilan qayta jihozlanmay, mahsulot raqobatbardoshligi pasaydi", "Britaniya sanoati birinchi o‘ringa chiqdi", "mustamlakalar mustaqil bo‘ldi", "eksport ko‘paydi", "Raqobatbardoshlik pasaydi.")
t.NAT("Yosh rivojlanayotgan davlatlar ingliz tovarlariga katta boj joriy etdi, Britaniya esa bojsiz savdoga sodiq qoldi.", "Britaniya iqtisodiy jihatdan orqada qola boshladi", "Britaniya eksporti ikki baravar oshdi", "boshqa davlatlar bojni bekor qildi", "Britaniya mustamlakalarini sotdi", "Bu Britaniyaning orqada qolishiga ta’sir qildi.")
t.TF("Britaniya qirollari davlatni amalda boshqarmagan.", True, "To‘g‘ri: ular davlat boshlig‘i edi, xolos.")
t.TF("London jahon moliya markazi maqomini yo‘qotgan.", False, "Noto‘g‘ri: London jahon moliya markazi hisoblangan.")
t.MUL([("Liberallar partiyasining tayanchi o‘rta sinf vakillari edi.", True),
       ("Britaniya vositachilik savdosi, sug‘urta, bank, kemasozlikdagi monopol hukmronligini saqlab qoldi.", True),
       ("Gladston Konservatorlar partiyasidan edi.", False)],
      "III noto‘g‘ri: Gladston Liberallar partiyasidan edi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Gladston bosh vazir bo‘ldi", "Parlament islohoti: saylovchilar 50% ga yetdi", "54 soatlik ish haftasi", "Yana bir parlament islohoti"],
      "1864 → 1867 → 1875 → 1911.")
t.VENN("Konservatorlar partiyasi", "Liberallar partiyasi",
       [("an’analarga sodiq", 1), ("tayanchi zamindorlar va anglikan cherkovi", 1),
        ("islohotlar tashabbuskori", 2), ("tayanchi o‘rta sinf", 2),
        ("Britaniyaning yetakchi mavqeyini saqlashga intilgan", 3)],
       "Konservatorlar — an’ana; liberallar — islohot; umumiy manfaat — imperiya.")

# 12 Buyuk Britaniyaning ichki siyosati
t = Topic('e9j12', 9112); TOPICS['e9j12'] = t
t.B("Britaniya ichki siyosatidagi keskin muammolardan biri qaysi edi?", "Irlandiya muammosi", "Shotlandiya muammosi", "Hindiston muammosi", "Uels muammosi", "Irlandiya muammosi.")
t.B("Irlandiya yerlarini kimlar o‘zlariniki qilib olgan?", "Britaniya lendlordlari", "irland dehqonlari", "katolik cherkovi", "AQSH fermerlari", "Britaniya lendlordlari.")
t.B("1875-yilda Irlandiyaga muxtoriyat (gomrul) talab qilgan deputat kim?", "Parnell", "Griffit", "Gladston", "Lloyd-Jorj", "Olsterlik protestant Parnell.")
t.B("«Gomrul» nimani anglatadi?", "Irlandiyada o‘z-o‘zini idora qilish", "yer islohoti", "ish tashlash huquqi", "Lordlar palatasining vetosi", "O‘z-o‘zini idora qilish.")
t.B("Irland dehqonlarining ommaviy tashkiloti qanday atalgan?", "«Yer-suv ligasi»", "«Shinfeyn»", "«Oq o‘g‘lonlar»", "tred-yunion", "«Yer-suv ligasi».")
t.B("Hukumat 1881-yilda gomrul o‘rniga nimani taklif qilgan?", "«Yer-suv akti»ni", "mustaqillikni", "parlament islohotini", "pensiyani", "«Yer-suv akti» — 15 yillik ijara komissiyasi.")
t.B("1882-yilda Dublinda kimlar o‘ldirilgan?", "Irlandiya ishlari stats-sekretari va lord-hokimi", "Parnell va Griffit", "Gladston", "qirolicha Viktoriya", "Stats-sekretar va lord-hokim.")
t.B("1905-yilda A. Griffit qaysi partiyani tuzgan?", "«Shinfeyn»", "Leyboristlar", "Liberallar", "«Yer-suv ligasi»", "«Shinfeyn» («Biz o‘zimiz»).")
t.B("1911-yilgi parlament islohoti qaysi palataning veto huquqini cheklagan?", "Lordlar palatasining", "Jamoa palatasining", "Senatning", "Reyxstagning", "Lordlar palatasining.")
t.B("1911-yildan parlamentning vakolat muddati necha yil etib belgilangan?", "5 yil", "7 yil", "4 yil", "3 yil", "5 yil; deputatlarga maosh joriy etildi.")
t.B("Tred-yunionlar tuzgan partiya qachondan Leyboristlar partiyasi deb atala boshlagan?", "1906-yildan", "1900-yildan", "1911-yildan", "1875-yildan", "1900-yilda tuzilib, 1906-yildan Leyboristlar partiyasi.")
t.B("Leyboristlar birinchi saylovda nechta deputatlik o‘rnini egallagan?", "29 ta", "5 ta", "100 ta", "50 ta", "29 ta.")
t.B("«Leyboristlar partiyasining tuzilishi Liberallar hukumatining xatosi» degan kim?", "D. Lloyd-Jorj", "Gladston", "Dizraeli", "Parnell", "D. Lloyd-Jorj.")
t.B("1911-yilgi konchilar ish tashlashi qancha davom etgan?", "6 hafta", "6 kun", "6 oy", "1 yil", "6 hafta.")
t.B("Britaniyada necha yoshga to‘lganlarga pensiya tayinlangan?", "70 yosh", "65 yosh", "60 yosh", "55 yosh", "70 yosh.")
t.NAT("Parnell kelishuvchilik yo‘lini tutdi.", "mayda terrorchi guruhlar faollashdi", "Irlandiya mustaqil bo‘ldi", "boykot to‘xtadi va tinchlik o‘rnatildi", "gomrul darhol qabul qilindi", "Kelishuv terrorchi guruhlarni faollashtirdi.")
t.NAT("1911-yildagi konchilar ish tashlashi hukumatni chora ko‘rishga majbur etdi.", "«Ish haqi minimumi to‘g‘risida»gi qonun qabul qilindi", "tred-yunionlar taqiqlandi", "ish kuni uzaytirildi", "konlar yopildi", "Ish tashlash zararini tred-yunionlardan undirish taqiqlandi.")
t.NAT("Jahon urushi boshlandi, ichki barqarorlik zarur bo‘ldi.", "parlament gomrul haqidagi qonunni tasdiqladi", "Irlandiya Germaniyaga qo‘shildi", "Shinfeyn hukumat tuzdi", "gomrul butunlay rad etildi", "Urush gomrulni tasdiqlashga majbur etdi.")
t.TF("Jamoa palatasi qonunni 3 marta ma’qullasa, Lordlar tasdiqlamasa ham qonun kuchiga ega bo‘ladigan bo‘ldi.", True, "To‘g‘ri.")
t.TF("1886-yilda parlament gomrulni tasdiqlagan.", False, "Noto‘g‘ri: hukumat qaror qilgan bo‘lsa-da, parlament uni rad etgan.")
t.MUL([("«Yer-suv ligasi» taqiqlangach, «Xotin-qizlar yer ligasi» tuzilgan.", True),
       ("Konchilar uchun 8 soatlik ish kuni belgilangan.", True),
       ("Leyboristlar partiyasi qurolli qo‘zg‘olon yo‘lini tanlagan.", False)],
      "III noto‘g‘ri: ular parlament yo‘lini tanlagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Parnell gomrulni talab qildi", "«Yer-suv akti» taklif qilindi", "Dublinda stats-sekretar o‘ldirildi", "Parlament gomrulni rad etdi", "«Shinfeyn» tuzildi", "Parlament islohoti"],
      "1875 → 1881 → 1882 → 1886 → 1905 → 1911.")
t.MAPN('europe', ['London', 'Dublin', 'Parij', 'Berlin'], "Qaysi raqam bilan 1882-yilda Irlandiya lord-hokimi o‘ldirilgan shahar belgilangan?",
       "2 – Dublin.", ask_idx=1)
t.VENN("«Yer-suv ligasi»", "«Shinfeyn»",
       [("irland dehqonlarining ommaviy tashkiloti", 1), ("taqiqlab qo‘yilgan", 1),
        ("1905-yilda A. Griffit tuzgan", 2), ("mustaqil parlament tuzish tashviqoti", 2),
        ("Britaniya tovarlarini boykot qilgan", 3)],
       "Liga — dehqonlar, taqiqlangan; Shinfeyn — Griffit, mustaqil parlament.")

# 13 Buyuk Britaniyaning tashqi siyosati
t = Topic('e9j13', 9113); TOPICS['e9j13'] = t
t.B("XIX asr oxirida Britaniya mustamlakalari maydoni qancha bo‘lgan?", "33 mln kv. km", "10 mln kv. km", "100 mln kv. km", "5 mln kv. km", "33 mln kv. km, qariyb 370 mln aholi.")
t.B("«Britaniyani boquvchi enaga» deb qaysi mustamlaka atalgan?", "Hindiston", "Misr", "Kanada", "Avstraliya", "Hindiston; Misr esa «boshiga kiydirilgan toj».")
t.B("Britaniya madhiyasida qanday satr bo‘lgan?", "«Britaniya, dengizlarni boshqar, hukmronlik qil!»", "«Xudo qirolichani asrasin»", "«Quyosh botmaydi»", "«Hukmronlik qil, Britaniya»", "«Britaniya, dengizlarni boshqar, hukmronlik qil!»")
t.B("1875-yilda Britaniya Suvaysh kanali aksiyalarining qancha qismini sotib olgan?", "45%", "100%", "25%", "60%", "45%.")
t.B("Qirolicha Viktoriya qachon Hindiston imperatori deb e’lon qilingan?", "1876-yilda", "1875-yilda", "1882-yilda", "1901-yilda", "1876-yilda — Buyuk Britaniya imperiyasi tashkil etildi.")
t.B("Britaniya va Rossiya manfaatlari tig‘ini qaytaruvchi hudud vazifasini qaysi davlat o‘tashi kerak edi?", "Afg‘oniston", "Eron", "Turkiya", "Xitoy", "Afg‘oniston.")
t.B("Rossiya–Usmonli urushi qachon boshlangan?", "1877-yilda", "1882-yilda", "1899-yilda", "1856-yilda", "1877-yilda.")
t.B("San-Stefano shartnomasi qayerda qayta ko‘rib chiqilgan?", "Berlin kongressida", "Parij konferensiyasida", "Vena kongressida", "London konferensiyasida", "Berlin kongressida.")
t.B("Usmonli davlati Britaniya foydasiga qaysi oroldan voz kechgan?", "Kipr", "Krit", "Rodos", "Malta", "Kipr orolidan.")
t.B("Britaniya Misrni qachon egallagan?", "1882-yilda", "1875-yilda", "1899-yilda", "1904-yilda", "1882-yilda.")
t.B("Bur respublikalariga qarshi urush qachon boshlangan?", "1899-yilda", "1882-yilda", "1902-yilda", "1876-yilda", "1899-yilda; 1902-yilda burlar taslim bo‘ldi.")
t.B("Taslim bo‘lgan Bur respublikalari qaysilar edi?", "Transvaal va Oranj", "Natal va Kap", "Keniya va Uganda", "Nigeriya va Somali", "Transvaal va Oranj.")
t.B("1901-yilda Britaniya Panama kanali qurish huquqini qaysi davlatga bergan?", "AQSHga", "Fransiyaga", "Germaniyaga", "Yaponiyaga", "AQSHga.")
t.B("Kanada dominionlik huquqini qachon olgan?", "1867-yilda", "1901-yilda", "1907-yilda", "1876-yilda", "1867-yilda.")
t.NAT("Britaniya Suvaysh kanalining aksiyalarini to‘liq qo‘lga kiritdi.", "Hindistonga chiqadigan dengiz yo‘llari nazorati to‘la Britaniya qo‘liga o‘tdi", "Misr mustaqil bo‘ldi", "kanal yopildi", "Fransiya kanalni egalladi", "Dengiz yo‘llari nazorati Britaniyaga o‘tdi.")
t.NAT("Germaniya harbiy qudrati o‘sib, Britaniya mustamlakalariga ham da’vo qila boshladi.", "Britaniya va Rossiya umumiy dushmanga qarshi yaqinlasha boshladi", "Britaniya Germaniya bilan ittifoq tuzdi", "Rossiya mustamlakalarini berdi", "Britaniya flotni qisqartirdi", "Umumiy xavf Britaniya va Rossiyani yaqinlashtirdi.")
t.TF("Rossiya Hindistonga xavf solishdan, Britaniya esa O‘rta Osiyoni egallashdan voz kechgan.", True, "To‘g‘ri.")
t.TF("Britaniya Erondagi 1905–1911-yillardagi inqilobni qo‘llab-quvvatlagan.", False, "Noto‘g‘ri: Britaniya bu inqilobni bostirgan.")
t.MUL([("Britaniya Afrikada Nigeriya, Somali, Keniya, Ugandani zabt etgan.", True),
       ("Avstraliya, Yangi Zelandiya va Janubiy Afrika Ittifoqi dominionlik huquqini olgan.", True),
       ("Britaniya Xitoydagi 1911-yilgi inqilobni qo‘llab-quvvatlagan.", False)],
      "III noto‘g‘ri: u inqilobga qarshi kuchlarni qo‘llab-quvvatlagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Kanada dominion bo‘ldi", "Suvaysh kanali aksiyalari sotib olindi", "Viktoriya Hindiston imperatori bo‘ldi", "Rossiya–Usmonli urushi", "Misrning egallanishi", "Bur respublikalari taslim bo‘ldi"],
      "1867 → 1875 → 1876 → 1877 → 1882 → 1902.")
t.MAPMATCH(AF, ['Misr', 'Nigeriya', 'Somali', 'Kap koloniyasi'],
           ["1882-yilda egallangan, «imperiya boshidagi toj» deb atalgan davlat", "Britaniya zabt etgan G‘arbiy Afrika hududi", "Britaniya zabt etgan Sharqiy Afrika hududi", "Janubiy Afrika Ittifoqiga birlashtirilgan hududlardan biri"],
           "1 – Misr; 2 – Nigeriya; 3 – Somali; 4 – Janubiy Afrika.")
t.VENN("Hindiston", "Misr",
       [("«Britaniyani boquvchi enaga»", 1), ("Viktoriya uning imperatori deb e’lon qilingan", 1),
        ("«imperiya boshiga kiydirilgan toj»", 2), ("1882-yilda egallangan", 2),
        ("Britaniya mustamlakasi", 3)],
       "Hindiston — enaga, Viktoriya imperator; Misr — toj, 1882.")

# 14 Amerika Qo‘shma Shtatlari
t = Topic('e9j14', 9114); TOPICS['e9j14'] = t
t.B("AQSHga qo‘shni qaysi davlatlar kuchsiz edi?", "Kanada va Meksika", "Kuba va Panama", "Braziliya va Argentina", "Britaniya va Fransiya", "Kanada va Meksika — bu AQSHni harbiy xarajatlardan xalos etdi.")
t.B("1870–1914-yillarda AQSHga qancha kishi ko‘chib kelgan?", "25 mln", "5 mln", "100 mln", "1 mln", "25 mln kishi.")
t.B("AQSH sanoat mahsuloti hajmi bo‘yicha qachon dunyoda birinchi o‘ringa chiqqan?", "1894-yilda", "1860-yilda", "1914-yilda", "1870-yilda", "1894-yilda (1860-yilda 4-o‘rinda edi).")
t.B("Ekin maydonlarini kengaytirish hisobiga mahsulotni ko‘paytirish qanday nomlangan?", "«amerikacha yo‘l»", "«prussiyacha yo‘l»", "«inglizcha yo‘l»", "«yangi kurs»", "Qishloq xo‘jaligining «amerikacha yo‘li».")
t.B("1890-yilda Yevropa davlatlarining AQSHga qo‘ygan kapitali qancha edi?", "3 mlrd. dollar", "20 mlrd. dollar", "1 mlrd. dollar", "60 mlrd. dollar", "3 mlrd. dollar.")
t.B("1909-yilda AQSH sanoat mahsuloti qiymati qanchadan oshgan?", "20 mlrd. dollardan", "3 mlrd. dollardan", "100 mlrd. dollardan", "1 mlrd. dollardan", "20 mlrd. dollardan.")
t.B("Kim «avtomobil qiroli»ga aylangan?", "Ford", "Morgan", "Rokfeller", "Karnegi", "Ford.")
t.B("1901-yilda Morgan tashkil etgan 1 mlrd. dollarlik trest qaysi?", "«Po‘lat korporatsiyasi»", "«Standart oyl»", "«Umumiy elektr kompaniyasi»", "«Ford motor»", "«Po‘lat korporatsiyasi».")
t.B("Rokfellerning «Standart oyl» tresti neft mahsulotining qancha qismini nazorat qilgan?", "90 foizini", "66 foizini", "50 foizini", "100 foizini", "90 foizini.")
t.B("1914-yilga kelib aholining 2 foizi milliy boylikning qancha qismiga egalik qilgan?", "60 foiziga", "90 foiziga", "20 foiziga", "50 foiziga", "60 foiziga.")
t.B("1860–1910-yillarda AQSHda fermerlar soni necha marta ko‘paygan?", "3 marta", "10 marta", "2 marta", "o‘zgarmagan", "3 marta.")
t.B("Turkistondan AQSHga qaysi o‘simlik keltirilgan?", "beda", "paxta", "bug‘doy", "makkajo‘xori", "Beda.")
t.B("1870-yilgi konstitutsiya tuzatishi nimani bekor qilgan?", "irqi va teri rangiga ko‘ra saylov cheklovlarini", "prezidentlik lavozimini", "Kongressni", "shtatlar huquqlarini", "Irq, teri rangi, ilgarigi qullik bahonasidagi cheklovlar bekor qilindi.")
t.B("Kongress Janubdagi sobiq isyonchilarga qachon umumiy afv bergan?", "1872-yilda", "1870-yilda", "1865-yilda", "1877-yilda", "1872-yilda.")
t.B("Janubda qaysi irqiy-terrorchi tashkilot bosh ko‘targan?", "«Ku-kluks-klan»", "«Shinfeyn»", "«Oq o‘g‘lonlar»", "«German ittifoqi»", "«Ku-kluks-klan».")
t.B("Qora tanlilarni sudsiz jazolash qanday atalgan?", "«Linch sudi»", "«Dala sudi»", "«Xalq sudi»", "«Kulturkampf»", "«Linch sudi».")
t.NAT("Ishchi kuchiga doimiy muhtojlik bor edi.", "yangi texnika va texnologiyalar ishlab chiqarishga keng joriy etildi", "sanoat pasaydi", "immigratsiya taqiqlandi", "qullik tiklandi", "Bu AQSHning gurkirab rivojlanishiga olib keldi.")
t.NAT("Isyon boshliqlaridan 500 ga yaqin kishining davlat vazifalarida ishlashi taqiqlandi.", "plantatorlar eski tartiblarni tiklash uchun kurashga bahona topdi", "Janubda tinchlik o‘rnatildi", "plantatorlar shimolga ko‘chdi", "qullik qayta joriy etildi", "Bu kurashga bahona bo‘ldi; Ku-kluks-klan bosh ko‘tardi.")
t.TF("AQSHda qirol xonadoni ham, yirik cherkov yer egaligi ham yo‘q edi.", True, "To‘g‘ri.")
t.TF("Chetga kapital chiqarish bo‘yicha AQSH Britaniya, Fransiya va Germaniyadan oldinda edi.", False, "Noto‘g‘ri: AQSH ulardan orqada edi.")
t.MUL([("Respublikachilar partiyasi yirik sanoatchilar va moliyachilar partiyasiga aylangan.", True),
       ("Ikki partiyaviy tizim uchinchi partiya tuzilishiga jiddiy to‘siq bo‘lgan.", True),
       ("Prezident saylovi oldidan barcha janubiy shtatlar respublikachilar tarafida qolgan.", False)],
      "III noto‘g‘ri: faqat Janubiy Karolina va Luiziana respublikachilar tarafida qolgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["AQSH sanoatda dunyoda 4-o‘rinda", "Konstitutsiyaga tuzatish kiritildi", "Sobiq isyonchilarga umumiy afv", "AQSH sanoatda birinchi o‘ringa chiqdi", "«Po‘lat korporatsiyasi» tashkil etildi"],
      "1860 → 1870 → 1872 → 1894 → 1901.")
t.MAPN(NA, ['Kanada', 'Kuba', 'Meksika', 'Nyu-York'], "AQSHning qo‘shnilari Kanada va Meksika kuchsiz edi. Qaysi raqam bilan Meksika belgilangan?",
       "3 – Meksika; 1 – Kanada.", ask_idx=2)
t.VENN("Demokratik partiya", "Respublikachilar partiyasi",
       [("yirik yer egalari va Janub burjuaziyasi manfaatini himoya qilgan", 1), ("fuqarolar urushida muvaffaqiyatsizlikka uchragan", 1),
        ("yirik sanoatchilar va moliyachilar partiyasiga aylangan", 2), ("ikki janubiy shtat uning tarafida qolgan", 2),
        ("ikki partiyaviy tizimning bir qismi", 3)],
       "Demokratlar — Janub, yer egalari; respublikachilar — sanoatchilar, moliyachilar.")
