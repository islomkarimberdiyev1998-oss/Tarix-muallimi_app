from qlib import Topic
TOPICS = {}
AF = 'africa'; EU = 'europe'; NE = 'nearest'

# 7 Fransiyaning tashqi siyosati
t = Topic('e9j7', 9107); TOPICS['e9j7'] = t
t.B("Germaniya va Avstriya-Vengriya o‘rtasida ittifoqchilik shartnomasi qachon tuzilgan?", "1879-yilda", "1882-yilda", "1891-yilda", "1904-yilda", "1879-yilda.")
t.B("Fransiyaning yangi mustamlakalar bosib olish yo‘lidagi dastlabki qadami qaysi?", "1881-yilda Tunisning bosib olinishi", "1884-yilda Vyetnamning egallanishi", "1912-yilda Marokash protektorati", "Madagaskarning bosib olinishi", "1881-yilda Tunis bosib olindi.")
t.B("Germaniya Fransiyaning Tunisni bosib olishiga nima uchun qarshilik ko‘rsatmagan?", "Fransiya va Italiya munosabatlarini keskinlashtirish uchun", "Fransiya bilan ittifoq tuzish uchun", "Tunisga qiziqmagani uchun", "Britaniyani zaiflashtirish uchun", "Italiya ham Tunisga da’vogar edi.")
t.B("Italiya qachon Germaniya va Avstriya-Vengriya ittifoqiga qo‘shilgan?", "1882-yilda", "1879-yilda", "1891-yilda", "1907-yilda", "1882-yilda — «Uchlar ittifoqi».")
t.B("Fransiya Marokash ustidan qachon protektorat o‘rnatgan?", "1912-yilda", "1904-yilda", "1881-yilda", "1896-yilda", "1912-yilda.")
t.B("Fransiya Vyetnamni qachon egallagan?", "1884-yilda", "1881-yilda", "1894-yilda", "1912-yilda", "1884-yilda; o‘n yildan keyin Laos protektorat bo‘ldi.")
t.B("Fransiya mustamlakachilik imperiyasida qancha aholi yashagan?", "20 mln", "5 mln", "100 mln", "2 mln", "20 mln aholi.")
t.B("Britaniya–Fransiya bitimi qachon imzolangan?", "1904-yilda", "1907-yilda", "1891-yilda", "1882-yilda", "1904-yilda.")
t.B("1904-yilgi bitimga ko‘ra Fransiya qaysi davlatni Britaniya ta’sir doirasida deb tan olgan?", "Misrni", "Marokashni", "Tunisni", "Jazoirni", "Misrni.")
t.B("Marokashning Gibraltar bo‘g‘oziga tutash qismi qaysi davlatga berilishi belgilangan?", "Ispaniyaga", "Fransiyaga", "Britaniyaga", "Italiyaga", "Ispaniyaga.")
t.B("Fransiya va Rossiya o‘rtasida ittifoq bitimi qachon tuzilgan?", "1891-yilda", "1904-yilda", "1907-yilda", "1879-yilda", "1891-yilda.")
t.B("Rossiya Britaniya–Fransiya ittifoqiga qachon qo‘shilgan?", "1907-yilda", "1904-yilda", "1891-yilda", "1912-yilda", "1907-yilda — Antanta vujudga keldi.")
t.B("Britaniya, Fransiya va Rossiya ittifoqi qanday nomlangan?", "Antanta", "Uchlar ittifoqi", "Muqaddas ittifoq", "German ittifoqi", "Antanta.")
t.NAT("1882-yilda «Uchlar ittifoqi» tashkil etildi.", "Fransiya bilan Rossiya yaqinlashishga majbur bo‘ldi", "Fransiya Germaniyaga qo‘shildi", "Rossiya Uchlar ittifoqiga kirdi", "Italiya Fransiya bilan ittifoq tuzdi", "Bu Fransiya va Rossiyani yaqinlashtirdi; 1891-yilda bitim tuzildi.")
t.NAT("Germaniya «quyosh hammaga birdek nur sochishi lozim», deb mustamlakalarni qayta bo‘lishga da’vo qildi.", "Fransiya va Britaniya yaqinlashib, 1904-yilda bitim tuzdi", "Fransiya Germaniya bilan ittifoq tuzdi", "Britaniya mustamlakalarini berdi", "Rossiya Germaniyaga qo‘shildi", "Umumiy raqib Fransiya va Britaniyani yaqinlashtirdi.")
t.TF("1891-yilgi bitimga ko‘ra ikki davlatdan biriga hujum bo‘lsa, har ikkalasi bir vaqtda safarbarlik e’lon qilishi kerak edi.", True, "To‘g‘ri.")
t.TF("Prussiya bilan urushdan keyin Fransiyaning xalqaro mavqeyi kuchaygan.", False, "Noto‘g‘ri: mavqeyi yo‘qqa chiqib, Germaniya hujumidan xavfsirab yashaydigan davlatga aylandi.")
t.MUL([("1891–1896-yillarda Fransiya Gvineya, Senegal, Madagaskar va Mavritaniyani bosib olgan.", True),
       ("Rossiya va Avstriya-Vengriya manfaatlari Bolqon yarimorolida to‘qnash kelgan.", True),
       ("1904-yilgi bitimda Britaniya Fransiyaning Misrdagi manfaatlarini tan olgan.", False)],
      "III noto‘g‘ri: Britaniya Fransiyaning Marokashdagi manfaatlarini tan olgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Germaniya va Avstriya-Vengriya ittifoqi", "Tunisning bosib olinishi", "«Uchlar ittifoqi»", "Fransiya–Rossiya bitimi", "Britaniya–Fransiya bitimi", "Antantaning vujudga kelishi"],
      "1879 → 1881 → 1882 → 1891 → 1904 → 1907.")
t.MAPMATCH(AF, ['Tunis', 'Marokash', 'Madagaskar', 'Misr'],
           ["1881-yilda Fransiya bosib olgan, Italiya ham da’vo qilgan hudud", "1912-yilda Fransiya protektorat o‘rnatgan davlat", "1891–1896-yillarda Fransiya bosib olgan orol", "1904-yilda Britaniya ta’sir doirasida deb tan olingan davlat"],
           "1 – Tunis; 2 – Marokash; 3 – Madagaskar; 4 – Misr.")
t.VENN("Uchlar ittifoqi", "Antanta",
       [("Germaniya, Avstriya-Vengriya, Italiya", 1), ("1882-yilda tuzilgan", 1),
        ("Britaniya, Fransiya, Rossiya", 2), ("1907-yilda yakunlangan", 2),
        ("Yevropa mustamlakachi davlatlarining harbiy-siyosiy ittifoqi", 3)],
       "Uchlar ittifoqi — 1882; Antanta — 1907; ikkalasi harbiy-siyosiy bloklar.")

# 8 Germaniya imperiyasining tashkil topishi
t = Topic('e9j8', 9108); TOPICS['e9j8'] = t
t.B("Vilgelm I qachon va qayerda Germaniya imperatori deb e’lon qilingan?", "1871-yil 18-yanvarda Versalda", "1870-yil 2-sentabrda Sedanda", "1871-yil 10-mayda Frankfurtda", "1888-yilda Berlinda", "1871-yil 18-yanvarda Versalda.")
t.B("Prussiya Germaniya hududining qancha qismini egallagan?", "2/3 qismini", "1/3 qismini", "yarmini", "to‘rtdan birini", "2/3 qismi, aholining 60% i.")
t.B("Elzas-Lotaringiya imperiyaga qanday maqomda kirgan?", "«maxsus imperiya viloyati»", "mustaqil davlat", "protektorat", "Prussiya provinsiyasi", "Shtatgalter boshqaradigan «maxsus imperiya viloyati».")
t.B("Germaniya parlamentining yuqori palatasi qanday atalgan?", "Bundesrat", "Reyxstag", "Landtag", "Senat", "Bundesrat (Ittifoq Kengashi).")
t.B("Germaniya parlamentining quyi palatasi qanday atalgan?", "Reyxstag", "Bundesrat", "Landtag", "Duma", "Reyxstag.")
t.B("Germaniyaning birinchi imperiya kansleri kim bo‘lgan?", "Otto fon Bismark", "Vilgelm I", "Vilgelm II", "Kaprivi", "Otto fon Bismark (1871–1890).")
t.B("Bismark qanday laqab bilan tarixda qolgan?", "«Temir kansler»", "«Qonli kansler»", "«Oq kansler»", "«Buyuk kansler»", "«Temir kansler».")
t.B("Reyxstag necha yil muddatga saylangan?", "besh yil", "to‘rt yil", "yetti yil", "uch yil", "Besh yil.")
t.B("Germaniyada necha yoshga to‘lgan erkaklar saylov huquqidan foydalangan?", "25 yoshga", "21 yoshga", "18 yoshga", "30 yoshga", "25 yoshga to‘lgan erkaklar.")
t.B("Germaniya iqtisodi gurkirab rivojlanishining bosh omili nima edi?", "Germaniyaning birlashtirilganligi", "mustamlakalar", "Fransiya bilan ittifoq", "qishloq xo‘jaligi", "Birlashuv yagona ichki bozorni vujudga keltirdi.")
t.B("Fosfor olish jarayonini soddalashtirgan kim?", "Tomson", "Krupp", "Simens", "Bismark", "Tomson.")
t.B("Germaniya qaysi sanoatda jahonda birinchi o‘ringa chiqqan?", "kimyo", "to‘qimachilik", "kemasozlik", "neft", "Kimyo sanoatida.")
t.B("1912-yilda Germaniyada qancha cho‘yan ishlab chiqarilgan?", "17,6 mln tonna", "8,6 mln tonna", "5 mln tonna", "40 mln tonna", "17,6 mln tonna.")
t.B("1914-yilga kelib Germaniya ishlab chiqarishi 1871-yilga nisbatan necha marta ko‘paygan?", "7 marta", "2 marta", "20 marta", "3 marta", "7 marta.")
t.NAT("Fransiya 3 yilda 5 mlrd. frank tovon to‘ladi, Lotaringiya va Saar Germaniyaga o‘tdi.", "Germaniya og‘ir sanoati rivojiga muhim turtki berildi", "Germaniya iqtisodi inqirozga uchradi", "Fransiya kuchaydi", "Germaniya qishloq xo‘jaligiga o‘tdi", "Bu Germaniya iqtisodi gurkirashining ikkinchi omili.")
t.TF("1871-yil konstitutsiyasiga ko‘ra imperator bir vaqtning o‘zida Prussiya qiroli ham bo‘lgan.", True, "To‘g‘ri.")
t.TF("Germaniyada harbiy xizmatchilar ham saylov huquqidan foydalangan.", False, "Noto‘g‘ri: harbiy xizmatchilar saylov huquqidan mahrum edi.")
t.MUL([("Imperator urush e’lon qilar, sulh tuzar va qurolli kuchlarning bosh qo‘mondoni edi.", True),
       ("Ko‘mir, cho‘yan va po‘lat ishlab chiqarish asosan 4 ta monopoliya qo‘lida to‘plangan.", True),
       ("Temir va po‘lat ishlab chiqarishda Germaniya dunyoda birinchi o‘rinda edi.", False)],
      "III noto‘g‘ri: bu sohada AQSHdan keyin ikkinchi o‘rinda edi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Vilgelm I imperator deb e’lon qilindi", "Germaniya konstitutsiyasi qabul qilindi", "Bismark iste’fo berdi", "Cho‘yan ishlab chiqarish 17,6 mln tonnaga yetdi"],
      "1871-yil yanvar → 1871 → 1890 → 1912.")
t.MAPMATCH(EU, ['Versal', 'Berlin', 'Elzas', 'Saar'],
           ["1871-yil 18-yanvarda Vilgelm I imperator deb e’lon qilingan joy", "Germaniya imperiyasi poytaxti", "Lotaringiya bilan birga «maxsus imperiya viloyati» bo‘lgan hudud", "toshko‘mir koni Germaniya og‘ir sanoatiga muhim bo‘lgan hudud"],
           "1 – Versal; 2 – Berlin; 3 – Elzas; 4 – Saar.")
t.VENN("Bundesrat", "Reyxstag",
       [("Ittifoq Kengashi", 1), ("parlamentning yuqori palatasi", 1),
        ("besh yil muddatga saylangan", 2), ("parlamentning quyi palatasi", 2),
        ("imperiyaning oliy vakolatli muassasasi", 3)],
       "Bundesrat — yuqori palata; Reyxstag — quyi palata, 5 yilga saylangan.")

# 9 Imperiyaning ichki siyosati
t = Topic('e9j9', 9109); TOPICS['e9j9'] = t
t.B("Germaniya hukumati ichki siyosatda qaysi masalaga alohida e’tibor bergan?", "mamlakatni prusslashtirishga", "Fransiya bilan yaqinlashishga", "katoliklikni kuchaytirishga", "federatsiyani kengaytirishga", "Prusslashtirish masalasiga.")
t.B("1906-yilda qancha polyak bolasi maktabga borishdan bosh tortgan?", "100 mingdan ortiq", "10 ming", "1 million", "500", "100 mingdan ortiq.")
t.B("Bismarkning katolik cherkovi ta’siriga qarshi tadbirlari qanday nom olgan?", "«Kulturkampf»", "«Drang nach Osten»", "«Realpolitik»", "«Temir va qon»", "«Kulturkampf» (Madaniyat uchun kurash).")
t.B("Germaniya sotsial-demokratik partiyasi (GSDP) qachon tashkil etilgan?", "1875-yilda", "1878-yilda", "1889-yilda", "1890-yilda", "1875-yilda.")
t.B("Sotsialistlarga qarshi favqulodda qonun qachon qabul qilingan?", "1878-yilda", "1875-yilda", "1890-yilda", "1871-yilda", "1878-yilda.")
t.B("Favqulodda qonun qabul qilinishiga nima bahona bo‘lgan?", "Vilgelm I ga ikki bor uyushtirilgan suiqasd", "ishchilar qo‘zg‘oloni", "Fransiya bilan urush", "Bismarkka suiqasd", "Vilgelm I ga ikki bor suiqasd.")
t.B("Favqulodda qonun necha yil amal qilgan?", "12 yil", "2,5 yil", "5 yil", "20 yil", "2,5 yilga qabul qilinsa-da, 12 yil amal qildi.")
t.B("Vilgelm I qachon vafot etgan?", "1888-yilda", "1890-yilda", "1871-yilda", "1878-yilda", "1888-yilda.")
t.B("Vilgelm II necha yoshida taxtga chiqqan?", "28 yoshida", "18 yoshida", "40 yoshida", "25 yoshida", "28 yoshli Vilgelm II (1888–1918).")
t.B("Bismark qachon iste’fo bergan?", "1890-yilda", "1888-yilda", "1889-yilda", "1871-yilda", "1890-yilda.")
t.B("1891-yildan qaysi kun dam olish kuni deb belgilangan?", "yakshanba", "shanba", "juma", "dushanba", "Yakshanba.")
t.B("Germaniyada katta yer egalari qanday atalgan?", "yunkerlar", "lendlordlar", "boyarlar", "fermerlar", "Yunkerlar.")
t.B("1912-yilgi saylovda GSDP necha foiz ovoz olgan?", "34,8%", "11%", "50%", "25%", "34,8%.")
t.NAT("1889-yilda Reyxstag sotsialistlarga qarshi qonunga doimiy tus berishni rad etdi, imperator ham Bismarkni qo‘llamadi.", "Bismark iste’fo berdi va favqulodda qonun bekor qilindi", "Bismark Reyxstagni tarqatdi", "GSDP taqiqlandi", "Vilgelm II taxtdan tushdi", "Bismark 1890-yilda iste’fo berdi.")
t.NAT("Qishloq xo‘jaligida texnika keng qo‘llanildi.", "ortiqcha ishchi kuchi shaharga ko‘chib, sanoatni ishchi kuchi bilan ta’minladi", "qishloq aholisi ko‘paydi", "sanoat pasaydi", "yunkerlar yerni sotdi", "Bu Germaniyaning industrial davlatga aylanishiga yordam berdi.")
t.TF("Bismark ishchilar kasal bo‘lganda, shikastlanganda va qariganda sug‘urta haqidagi qonunlarni qabul qildirgan.", True, "To‘g‘ri.")
t.TF("Germaniya ishchilari AQSH va Britaniya ishchilaridan ko‘proq ish haqi olgan.", False, "Noto‘g‘ri: ular kamroq haq olgan.")
t.MUL([("13 yoshdan kichik bolalar mehnati taqiqlangan.", True),
       ("Xotin-qizlar uchun 11 soatlik ish kuni joriy qilingan.", True),
       ("GSDP kurashning qurolli qo‘zg‘olon yo‘lini tanlagan.", False)],
      "III noto‘g‘ri: GSDP tinch, parlament yo‘lini tanlagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["GSDP tashkil etildi", "Sotsialistlarga qarshi favqulodda qonun", "Vilgelm II taxtga chiqdi", "Bismark iste’fo berdi", "Polyak bolalari maktabdan bosh tortdi", "GSDP 34,8% ovoz oldi"],
      "1875 → 1878 → 1888 → 1890 → 1906 → 1912.")
t.VENN("Bismark siyosati", "Bismarkdan keyingi hukumat siyosati",
       [("«Kulturkampf»", 1), ("sotsialistlarga qarshi favqulodda qonun", 1),
        ("favqulodda qonunning bekor qilinishi", 2), ("yakshanba dam olish kuni deb belgilanishi", 2),
        ("ishchilar uchun qonunlar qabul qilinishi", 3)],
       "Bismark — Kulturkampf, favqulodda qonun; keyin — qonun bekor, yakshanba dam olish.")

# 10 Imperiyaning tashqi siyosati
t = Topic('e9j10', 9110); TOPICS['e9j10'] = t
t.B("Germaniya hukmron doiralari qanday talab bilan chiqqan?", "«quyoshning hammaning yelkasiga birday nur sochishi»", "«Germaniyaning kelajagi quruqlikda»", "«Bo‘lib tashla, hukmronlik qil»", "«Yevropa yevropaliklar uchun»", "Mustamlakalarni qayta bo‘lish talabi.")
t.B("Bismark ittifoqdosh sifatida qaysi davlatni topgan?", "Avstriya-Vengriyani", "Rossiyani", "Britaniyani", "Fransiyani", "1879-yilda Avstriya-Vengriya bilan ittifoq tuzildi.")
t.B("Bismark o‘z rejalari yo‘lidagi asosiy g‘ov deb qaysi davlatni bilgan?", "Rossiyani", "Italiyani", "Usmonli davlatini", "AQSHni", "Rossiyani.")
t.B("Shovinistik «German ittifoqi» qachon tuzilgan?", "1891-yilda", "1882-yilda", "1879-yilda", "1905-yilda", "1891-yilda.")
t.B("1882-yilda Bremen savdogarlari Afrikaning qaysi qismiga kelgan?", "janubi-g‘arbiy sohilidagi Angra-Peken buxtasiga", "Misrga", "Marokashga", "Madagaskarga", "Janubi-g‘arbiy sohildagi Angra-Peken buxtasiga.")
t.B("Afrikaning sharqidagi Germaniya hududlari qanday nom olgan?", "«Germaniya Sharqiy Afrikasi»", "«Germaniya Kongosi»", "«Yangi Germaniya»", "«Zanzibar protektorati»", "«Germaniya Sharqiy Afrikasi».")
t.B("90-yillar oxirida Germaniya Xitoyning qaysi provinsiyasining bir qismini bosib olgan?", "Shandun", "Manchjuriya", "Guandun", "Tibet", "Shandun provinsiyasi.")
t.B("Shimoliy dengizni Boltiq dengizi bilan tutashtirgan kanal qaysi?", "Kil kanali", "Suvaysh kanali", "Panama kanali", "Bosfor", "Kil kanali.")
t.B("Berlinni Fors qo‘ltig‘i bilan bog‘lovchi temiryo‘l kimning tashabbusi bilan rejalashtirilgan?", "nemis bankiri Simens", "Bismark", "Krupp", "Tomson", "Nemis bankiri Simens.")
t.B("Vilgelm II Falastinga qachon borgan?", "1889-yilda", "1882-yilda", "1891-yilda", "1905-yilda", "1889-yilda.")
t.B("Temiryo‘l qaysi nom bilan tarixga kirgan?", "«Bag‘dod temiryo‘li»", "«Sharq ekspressi»", "«Kil yo‘li»", "«Berlin–Istanbul yo‘li»", "«Bag‘dod temiryo‘li».")
t.B("Britaniya Bag‘dod temiryo‘lining Fors qo‘ltig‘iga chiqishiga yo‘l qo‘ymaslik uchun qayerda protektorat o‘rnatgan?", "Quvaytda", "Misrda", "Iroqda", "Arabistonda", "Quvaytda.")
t.B("Vilgelm II qanday shiorni e’lon qilgan?", "«Germaniyaning kelajagi dengizda»", "«Temir va qon»", "«Quyosh hammaga»", "«Sharqqa hujum»", "«Germaniyaning kelajagi dengizda».")
t.B("Germaniya Bosh shtabi ikki frontda urush rejasini qachon ishlab chiqqan?", "1905-yilda", "1891-yilda", "1907-yilda", "1914-yilda", "1905-yilda.")
t.B("Germaniyaning Bolqon va Sharqqa suqilib kirishi tarixga qanday nom bilan kirgan?", "«Sharqqa hujum»", "«Kulturkampf»", "«Dengizga yurish»", "«Yangi tartib»", "«Sharqqa hujum» (Drang nach Osten).")
t.NAT("Germaniya Usmonli davlatini moliyaviy va harbiy jihatdan qo‘llab-quvvatladi.", "Usmonli davlati Germaniyaning deyarli vassaliga aylanib, urushda uning tarafida turishga majbur bo‘ldi", "Usmonli davlati Antantaga qo‘shildi", "Germaniya Istanbulni bosib oldi", "Usmonli davlati kuchaydi", "Usmonli davlati deyarli vassalga aylandi.")
t.NAT("Germaniya harbiy flot qurishning ulkan dasturini qabul qildi.", "Buyuk Britaniya bilan munosabatlar yanada keskinlashdi", "Britaniya bilan ittifoq tuzildi", "Germaniya flot qurishdan voz kechdi", "Fransiya Germaniyaga qo‘shildi", "Bu Britaniya bilan munosabatlarni keskinlashtirdi.")
t.TF("Usmonli davlati ko‘z o‘ngida Germaniya uning hududlariga da’vo qilmayotgan yagona davlat edi.", True, "To‘g‘ri.")
t.TF("XIX asr 90-yillarida Germaniya mustamlakalari hududi o‘zining hududidan kichik edi.", False, "Noto‘g‘ri: u o‘z hududidan deyarli besh baravar ortiq edi.")
t.MUL([("Germaniya Togo va Kamerun hududlarini ishg‘ol qilgan.", True),
       ("Germaniya harbiy dengiz floti qudrat jihatidan ikkinchi o‘ringa chiqqan.", True),
       ("Germaniya Rossiyaning Bolqondagi manfaatlarini qo‘llab-quvvatlagan.", False)],
      "III noto‘g‘ri: u Avstriya-Vengriyaning Bolqon siyosatini qo‘llab-quvvatlagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Germaniya va Avstriya-Vengriya ittifoqi", "Bremen savdogarlari Angra-Peken buxtasiga keldi", "Vilgelm II Falastinga bordi", "«German ittifoqi» tuzildi", "Ikki frontda urush rejasi ishlab chiqildi"],
      "1879 → 1882 → 1889 → 1891 → 1905.")
t.MAPMATCH(NE, ['Istanbul', 'Bag‘dod', 'Quvayt', 'Falastin'],
           ["Bosfor bo‘yidagi Usmonli poytaxti — temiryo‘l boshlanadigan joy", "temiryo‘l nomi berilgan shahar", "Britaniya protektorat o‘rnatgan joy", "Vilgelm II 1889-yilda ziyorat qilgan hudud"],
           "1 – Istanbul; 2 – Bag‘dod; 3 – Quvayt; 4 – Falastin.")
t.VENN("Germaniyaning Afrikadagi mustamlakalari", "Germaniyaning Osiyo va Tinch okeanidagi mulklari",
       [("Togo va Kamerun", 1), ("«Germaniya Sharqiy Afrikasi»", 1),
        ("Shandun provinsiyasining bir qismi", 2), ("Karolina, Mariana, Marshall orollari", 2),
        ("Germaniya ekspansiyasi natijasi", 3)],
       "Afrika — Togo, Kamerun, Sharqiy Afrika; Osiyo — Shandun, orollar.")
