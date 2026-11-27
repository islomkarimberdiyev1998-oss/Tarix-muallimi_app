from qlib import Topic, PLACES, REG
TOPICS = {}

# 19-§ Qo‘ng‘irotlar davrida ijtimoiy-iqtisodiy hayot
t = Topic('y9u19', 9019); TOPICS['y9u19'] = t
t.B("Xiva xonligi qumli sahro tufayli qaysi ikki qismga bo‘lingan?", "Suvbo‘yi va Tog‘bo‘yi", "Shimol va Janub", "Ustyurt va Qoraqum", "Orol va Kaspiy", "Suvbo‘yi (daryo tomoni) va Tog‘bo‘yi (Kopetdog‘ oldi).")
t.B("XVI–XVII asrlarda Xorazm vohasiga qayerdan ko‘chmanchi urug‘lar kirib kelgan?", "Qipchoq dashtidan", "Erondan", "Hindistondan", "Sibirdan", "Qipchoq dashtidan.")
t.B("Qoraqalpoqlarning bir qismi Xiva xonligiga qachon ko‘chib o‘tgan?", "XVIII asrda", "XVI asrda", "XIX asr oxirida", "XIV asrda", "XVIII asrda Sirdaryo quyi oqimidan.")
t.B("Turkmanlarning katta qismi qayerda yashagan?", "Kaspiy dengizi bo‘ylarida", "Orol bo‘yida", "Farg‘onada", "Zarafshonda", "Kaspiy dengizi bo‘ylarida.")
t.B("Turkmanlar XVI asr o‘rtalarida nima sababdan sharqqa ko‘chgan?", "yaylovlarning siyraklashib qolishi", "urush", "zilzila", "Eron bosqini", "Yaylovlar siyraklashgan.")
t.B("O‘zlashtirilgan yerlarning necha foizi xonlikning janubiy qismiga to‘g‘ri kelgan?", "93 foizi", "50 foizi", "30 foizi", "75 foizi", "93 foizi.")
t.B("Xorazmda dala eniga va bo‘yiga necha martagacha haydalgan?", "20 martagacha", "2 marta", "50 marta", "bir marta", "5, 10, hatto 20 martalab.")
t.B("XVII asrda Balxda navlarni yaxshilash uchun Xorazm qovunining qaysi navidan foydalanilgan?", "ko‘ktarnay", "bo‘rikalla", "shakarpalak", "qizilurug‘", "Ko‘ktarnay navidan.")
t.B("Xorazm qovuni qoqisi qayerlargacha sotilgan?", "Hindiston va Xitoy shaharlarigacha", "faqat Xivada", "Yevropagacha", "Arabistongacha", "Hindiston va Xitoygacha.")
t.B("Xorazmda chavandozlikda qaysi ot zoti ishlatilgan?", "turkman oti", "qozoq oti", "arab oti", "qorabayir", "Turkman oti; qozoq oti – ishchi kuchi.")
t.B("Manbaga ko‘ra qaysi shaharning olmalari tahsinga loyiq?", "Hazorasp", "Xiva", "Urganch", "Shovot", "Hazoraspning olmalari.")
t.B("Vorisi bo‘lmagan shaxsdan meros sifatida davlatga o‘tgan yerlar qanday atalgan?", "zamini matruka", "zamini maita", "bo‘z yer", "vaqf yer", "Zamini matruka.")
t.B("Arab Muhammadxon qaysi qal’aning yuqorisidan ariq qazdirgan?", "Tuk qal’asi", "Vazir qal’asi", "Hazorasp qal’asi", "Ark", "Tuk qal’asining yuqorisidan.")
t.B("Xorazmda chig‘irning nechta asosiy qismi bo‘lgan?", "uchta", "ikkita", "beshta", "to‘rtta", "G‘ildirak, gorizontal o‘q va charxlar.")
t.B("Qorako‘l terisidan tikilgan maxsus telpak qanday ataladi?", "cho‘girma", "do‘ppi", "qalpoq", "salla", "Cho‘girma.")
t.B("Xorazmda bolalar maktabda necha yoshdan o‘qishni boshlagan?", "6 yoshdan (ba’zan 5 yoshdan)", "10 yoshdan", "3 yoshdan", "12 yoshdan", "6 yoshdan, ba’zan 5 yoshdan.")
t.B("Maktablar odatda kimning qaramog‘ida bo‘lgan?", "mahalla masjidlari", "xon saroyi", "qozilar", "savdogarlar", "Mahalla masjidlari.")
t.NAT("Tuproq hosildorligi past edi.", "dalaga ishlov berishning maxsus usullari – ko‘p martalab haydash qo‘llanildi", "dehqonchilik to‘xtadi", "aholi ko‘chib ketdi", "faqat chorvachilik qoldi", "Maxsus ishlov usullari.")
t.NAT("Xorazmda Amudaryo orqali savdo va kemalar qatnovi yaxshi yo‘lga qo‘yildi.", "kemachilik hunarmandchilikning rivojlangan turiga aylandi", "daryo yo‘li yopildi", "kemalar Rossiyadan olib kelindi", "savdo karvonlari to‘xtadi", "Kemasozlik rivojlandi.")
t.NAT("Qo‘ng‘irotlarga qarshi muxolif kuchlar bartaraf etilib, mulklari musodara qilindi.", "davlat yer jamg‘armasi kengaydi", "xususiy yerlar ko‘paydi", "vaqf yerlar tugatildi", "dehqonlar yer oldi", "Davlat yerlari ko‘paydi.")
t.NAT("Sun’iy sug‘orishga asoslangan xo‘jalik keng yoyildi.", "Xiva xonligida chig‘ir tayyorlash keng tarqaldi", "chig‘irlar taqiqlandi", "lalmikor dehqonchilik kengaydi", "ariqlar ko‘mildi", "Chig‘irsozlik rivojlandi.")
t.TF("Xiva xonligida barcha yerlar xon mulki hisoblansa-da, davlat, xususiy va vaqf yerlari mavjud bo‘lgan.", True, "To‘g‘ri.")
t.TF("Xorazm maktablarida qiz bolalar o‘qitilmagan.", False, "Noto‘g‘ri: qiz bolalar uchun maxsus sinflar ajratilgan.")
t.TF4([("Xonlik xo‘jaligida donli ekinlar asosiy o‘rinni egallagan.", True), ("Xorazmda ekinlarni almashlab ekish tajribasi qo‘llanilgan.", True),
       ("Madrasalar faqat Xivada bo‘lgan.", False), ("Xorazmda turkman gilamlari ham tayyorlangan.", True)],
      "3-noto‘g‘ri: Urganch, Shohobod, Shovot, Hazoraspda ham bo‘lgan.")
t.MUL([("Janubiy Xorazm dehqonchiligi mutlaqo sun’iy sug‘orishga asoslangan.", True),
       ("To‘qimachilik rivojiga ko‘chmanchi dasht aholisining ehtiyoji ham sabab bo‘lgan.", True),
       ("Xorazmda bog‘dorchilik iqtisodiyotda yetakchi o‘rin tutgan.", False)],
      "III noto‘g‘ri: bog‘dorchilikning o‘rni yuqori bo‘lmagan.")
t.CHR("Jarayonlarni xronologik ketma-ketlikda joylashtiring.", ["turkmanlar yaylov siyraklashuvi sabab sharqqa ko‘cha boshladi", "turkmanlarning Xorazm hayotidagi ishtiroki sezilarli oshdi", "qoraqalpoqlarning bir qismi Sirdaryodan ko‘chib o‘tdi", "turkmanlarning xonlikka joylashuvi yakunlandi"],
      "XVI asr o‘rtasi → XVII asr boshi → XVIII asr → XIX asr birinchi yarmi.")
t.MATCH("Atamalarni izohi bilan moslashtiring.", ["zamini matruka", "zamini maita", "chig‘ir", "cho‘girma"],
        ["meros huquqi asosida davlatga o‘tgan yer", "qo‘riq (bekor) yer shakli", "suv chiqaruvchi g‘ildirakli moslama", "qorako‘l teridan telpak", "vaqf yer"], 'abcd',
        "Matruka – meros yer; maita – qo‘riq yer; chig‘ir – suv moslamasi; cho‘girma – telpak.")
t.VENN("Turkman oti", "Qozoq oti",
       [("asosan chavandozlikda", 1), ("Kaspiy bo‘yi xalqi nomidagi zot", 1),
        ("ishchi kuchi sifatida", 2), ("dasht xalqi nomidagi zot", 2),
        ("Xorazm dehqonchiligida otlar asosiy ish kuchi", 3)],
       "Turkman oti – chavandozlik; qozoq oti – ishchi kuch; ikkalasi Xorazmda mashhur.")
t.MAPMATCH('xorazm2', ['Hazorasp', 'Ko‘hna Urganch', 'Orol dengizi'],
           ["olmalari tahsinga loyiq deb yozilgan shahar", "madrasalar bo‘lgan shimoliy shahar", "xonlik shimoli-sharqida qoraqalpoqlar yashagan hudud yonidagi dengiz"],
           "1 – Hazorasp; 2 – Ko‘hna Urganch; 3 – Orol dengizi.")

# 20-§ Qo‘ng‘irotlar davrida Xiva me’morchiligi
t = Topic('y9u20', 9020); TOPICS['y9u20'] = t
t.B("Eron qo‘shinlari Xorazmga qachon kirib kelgan?", "1740-yilda", "1768-yilda", "1623-yilda", "1855-yilda", "1740-yilda.")
t.B("Butun Xiva xonligi bo‘ylab o‘lat qachon tarqalgan?", "1768-yilda", "1740-yilda", "1842-yilda", "1806-yilda", "1768-yilda.")
t.B("«Firdavs ul-iqbol» asari muallifi kim?", "Munis Xorazmiy", "Abulg‘ozixon", "Ogahiy", "Bayoniy", "Munis; asarni Ogahiy yakunlagan.")
t.B("«Firdavs ul-iqbol»da Xorazm tarixi qaysi yilgacha bayon etilgan?", "1825-yilgacha", "1740-yilgacha", "1855-yilgacha", "1770-yilgacha", "1825-yilgacha.")
t.B("Munis qanday lavozimda ishlagan?", "bosh mirob", "mehtar", "qushbegi", "qozikalon", "Xonlikning bosh mirobi.")
t.B("Munisning sug‘orish inshootlariga oid risolasi qanday ataladi?", "«Arnalar»", "«Firdavs ul-iqbol»", "«Shajarayi turk»", "«Riyoz ud-davla»", "«Arnalar».")
t.B("Ogahiyning to‘liq ismi nima?", "Muhammadrizo Erniyozbek o‘g‘li", "Sherniyoz Avazbiy o‘g‘li", "Muhammad Amin", "Bobojon Tarroh", "Muhammadrizo Erniyozbek o‘g‘li.")
t.B("1842-yilda Xiva atrofida qurilgan yangi qal’a devorining uzunligi qancha?", "6 km", "26 km", "2 km", "10 km", "6 km, 6 ta darvozasi bilan.")
t.B("Xivaning katta halqa ichidagi tashqi qismi qanday ataladi?", "Dishan qal’a", "Ichan qal’a", "Ko‘hna ark", "Toshhovli", "Dishan qal’a.")
t.B("Ichan qal’a Xivaning necha gektarini egallagan?", "26 gektar", "6 gektar", "62 gektar", "100 gektar", "26 gektar.")
t.B("Ichan qal’a qachon YUNESKO jahon merosi ro‘yxatiga kiritilgan?", "1990-yilda", "1995-yilda", "2001-yilda", "1997-yilda", "1990-yildan.")
t.B("Arab Muhammadxon poytaxtni qayerdan Xivaga ko‘chirgan?", "Urganchdan", "Vazirdan", "Hazoraspdan", "Kotdan", "Urganchdan.")
t.B("Arab Muhammadxon qachon vafot etgan?", "1623-yilda", "1603-yilda", "1657-yilda", "1686-yilda", "1623-yilda Qum qal’ada.")
t.B("Sherg‘ozixon madrasasi qaysi yillarda qurilgan?", "1719–1726-yillarda", "1616-yilda", "1852–1855-yillarda", "1657–1664-yillarda", "1719–1726-yillarda.")
t.B("Sherg‘ozixon madrasasida nechta hujra bo‘lgan?", "55 ta", "39 ta", "114 ta", "26 ta", "55 ta.")
t.B("Kaltaminor qurilishi qachon boshlangan?", "1852-yilda", "1855-yilda", "1842-yilda", "1806-yilda", "1852-yilda.")
t.B("Kaltaminor qurilishi to‘xtaganda balandligi qancha bo‘lgan?", "29 m", "73 m", "110 m", "14,2 m", "29 metr.")
t.B("Muhammad Aminxon qayerda halok bo‘lgan?", "Saraxs yaqinida", "Marvda", "Buxoroda", "Mashhadda", "1855-yilda Saraxs yaqinida.")
t.B("Kaltaminor yana qanday nomlar bilan atalgan?", "«Ko‘k minor», «Ulli minor»", "«Minorayi kalon»", "«Islomxo‘ja minorasi»", "«Qutb minor»", "«Ko‘k minor», «Ulli minor».")
t.B("Anushaxon hammomi taxminan qachon qurilgan?", "1657–1664-yillarda", "1719–1726-yillarda", "1616-yilda", "1835-yilda", "1657–1664-yillarda.")
t.B("Anushaxon kimning o‘g‘li?", "Abulg‘ozi Bahodirxonning", "Arab Muhammadxonning", "Sherg‘ozixonning", "Elbarsxonning", "Abulg‘ozi Bahodirxonning.")
t.B("Polvon darvozani 1806-yilda kim pishiq g‘ishtdan qayta qurgan?", "Eltuzarxon", "Olloqulixon", "Muhammad Aminxon", "Anushaxon", "Eltuzarxon.")
t.B("Polvon darvoza chiroyli koshinlari uchun qanday nom olgan?", "«Gul darvoza»", "«Ota darvoza»", "«Ko‘k darvoza»", "«Tosh darvoza»", "«Gul darvoza».")
t.NAT("Amudaryo o‘zani o‘zgarib, qurib bordi.", "Arab Muhammadxon poytaxtni Urganchdan Xivaga ko‘chirishga majbur bo‘ldi", "Xiva tashlab ketildi", "yangi kanal qazildi va Urganch saqlandi", "xonlik Buxoroga qo‘shildi", "Poytaxt Xivaga ko‘chdi.")
t.NAT("Muhammad Aminxon 1855-yilda Saraxs yaqinidagi jangda halok bo‘ldi.", "Kaltaminor qurilishi to‘xtab, minora tugallanmay qoldi", "minora 110 metrga yetkazildi", "minora buzib tashlandi", "minora Buxoroda qurildi", "Kaltaminor bitmadi.")
t.NAT("1657-yilda Anushaxon Abdulazizxonga qarshi jangda qahramonlik ko‘rsatib, otasini saqlab qoldi.", "otasi unga tug‘, lashkar va Hazoraspni in’om etib, nomiga hammom qurdirdi", "Anushaxon surgun qilindi", "Xiva Buxoroga bo‘ysundi", "Anushaxon jangda halok bo‘ldi", "Anushaxon taqdirlandi.")
t.NAT("Sovetlar davrida Kaltaminordagi yozuvlar yulib tashlangan edi.", "mustaqillikdan keyin Ogahiy qo‘lyozmasi asosida qayta tiklandi", "yozuvlar butunlay yo‘qoldi", "minora buzildi", "minora boshqa joyga ko‘chirildi", "Yozuvlar tiklandi.")
t.TF("Kaltaminor butunlay sirlangan koshinlar bilan qoplangan yagona minora hisoblanadi.", True, "To‘g‘ri.")
t.TF("Anushaxon hammomi xonalari yer ustida baland qilib qurilgan.", False, "Noto‘g‘ri: issiqni saqlash uchun yer ostida joylashtirilgan.")
t.TF4([("Ichan qal’a devorlari balandligi 8–10 metr bo‘lgan.", True), ("Kaltaminor poydevori diametri 14,2 metr.", True),
       ("Anushaxon hammomida tish olib tashlash ham bajarilgan.", True), ("Sherg‘ozixon Pahlavon Mahmud maqbarasidan uzoqda madrasa qurdirgan.", False)],
      "4-noto‘g‘ri: madrasa Pahlavon Mahmud maqbarasiga yaqin qurilgan.")
t.MUL([("Ichan qal’a qurilishida «qo‘sh» uslubidan foydalanilgan.", True),
       ("Anushaxon Pahlavon Mahmud maqbarasiga dafn etilgan.", True),
       ("Arab Muhammadxon madrasasi Olloqulixon davrida buzib tashlangan.", False)],
      "III noto‘g‘ri: Olloqulixon davrida qayta qurilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Arab Muhammadxon vafot etdi", "Anushaxon Abdulazizxonga qarshi jangda qahramonlik ko‘rsatdi", "Sherg‘ozixon madrasasi qurildi", "O‘lat tarqaldi", "Polvon darvoza qayta qurildi", "Kaltaminor qurilishi to‘xtadi"],
      "1623 → 1657 → 1720 → 1768 → 1806 → 1855.")
t.MATCH("Inshootlarni u bilan bog‘liq shaxs bilan moslashtiring.", ["Kaltaminor", "Polvon darvoza (1806)", "Arab Muhammadxon madrasasini qayta qurish", "hammom (1657–1664)"],
        ["Muhammad Aminxon", "Eltuzarxon", "Olloqulixon", "Anushaxon", "Sherg‘ozixon"], 'abcd',
        "Kaltaminor – Muhammad Aminxon; Polvon darvoza – Eltuzarxon; qayta qurish – Olloqulixon; hammom – Anushaxon.")
t.VENN("Ichan qal’a", "Dishan qal’a",
       [("26 gektar ichki shahar", 1), ("Kaltaminor, Toshhovli joylashgan", 1),
        ("1842-yilda qurilgan 6 km devor bilan o‘ralgan", 2), ("Rafoniq, Nurillaboy bog‘lari kiritilgan", 2),
        ("Xiva shahrining qismi", 3)],
       "Ichan qal’a – ichki shahar, yodgorliklar; Dishan qal’a – 1842 devor, bog‘lar; ikkalasi Xiva qismi.")
t.MAPMATCH('xorsar', ['Xiva', 'Ko‘hna Urganch', 'Saraxs', 'Qarshi'],
           ["Ichan qal’a joylashgan poytaxt", "Arab Muhammadxon poytaxtni ko‘chirishdan oldingi shahar", "1855-yilda Muhammad Aminxon halok bo‘lgan joy", "Anushaxon Buxoroga yurishida egallagan shahar"],
           "1 – Xiva; 2 – Ko‘hna Urganch; 3 – Saraxs; 4 – Qarshi.")

# 21-§ XVI–XIX asrning birinchi yarmida qoraqalpoqlar
t = Topic('y9u21', 9021); TOPICS['y9u21'] = t
t.B("Qoraqalpoqlarning eng qadimgi ajdodlari kimlar?", "massaget qabilalari", "sak qabilalari", "xunnlar", "eftaliylar", "Orol janubidagi massagetlar.")
t.B("Qoraqalpoqlar qaysi qabila negizida xalq sifatida shakllangan?", "bijanak", "qipchoq", "o‘g‘uz", "nayman", "Turkiy bijanak qabilasi negizida.")
t.B("Qoraqalpoqlarning xalq sifatida shakllanishi qachon nihoyasiga yetgan?", "XI asrda", "XVI asrda", "VIII asrda", "XIV asrda", "XI asrda.")
t.B("XV asr ikkinchi yarmidan XVI asr ikkinchi yarmigacha qoraqalpoqlar qaysi xonlik tarkibida bo‘lgan?", "No‘g‘ay xonligi", "Xiva xonligi", "Buxoro xonligi", "Qozoq xonligi", "No‘g‘ay xonligi.")
t.B("No‘g‘ay xonligida qaysi yillarda ekin bitmay ocharchilik bo‘lgan?", "1557–1558", "1714–1715", "1723–1724", "1598–1599", "1557–1558-yillarda.")
t.B("No‘g‘ay xonligini tark etgan qoraqalpoqlar qayerga joylashgan?", "Sirdaryo sohillariga", "Amudaryo bo‘ylariga", "Farg‘onaga", "Volga bo‘yiga", "Sirdaryo sohillariga.")
t.B("Amudaryo qachon eski o‘zaniga qaytib, Orolga quyila boshlagan?", "XVII asr boshida", "XVI asr boshida", "XVIII asr oxirida", "XIX asrda", "XVII asr boshlarida.")
t.B("XVII asrda qoraqalpoqlar o‘zbeklar bilan qanday davlat barpo etgan?", "Orol (Aran) davlati", "No‘g‘ay xonligi", "Kichik juz", "Jung‘or xonligi", "Orol (Aran) davlati.")
t.B("XII asr rus manbalarida qoraqalpoqlar qanday nom bilan uchraydi?", "«chyorniye klobuki»", "«polovtsi»", "«pechenegi»", "«tatari»", "«Chyorniye klobuki».")
t.B("Qoraqalpoqlarga nisbatan yana qaysi atama ishlatilgan?", "«qora bo‘rkli»", "«qora tanli»", "«oq qalpoq»", "«ko‘k bo‘rk»", "«Qora bo‘rkli».")
t.B("Olimlar fikricha «qoraqalpoq» so‘zi qaysi tilga mansub?", "qipchoq tiliga", "fors tiliga", "arab tiliga", "mo‘g‘ul tiliga", "Qipchoq tiliga.")
t.B("Qoraqalpoq xalqi nomi ilk bor qaysi hujjatda to‘liq keltirilgan?", "1598-yilda Abdullaxon II yorliqnomasida", "«Boburnoma»da", "Ivan Grozniy farmonida", "«Shajarayi turk»da", "Abdullaxon II ning 1598-yilgi yorliqnomasida.")
t.B("Abdullaxon II yorliqnomasi qaysi maqbaraga berilgan?", "Sig‘noqdagi Ziyovuddin maqbarasiga", "Yassaviy maqbarasiga", "Pahlavon Mahmud maqbarasiga", "Sulton Uvays bobo maqbarasiga", "Sig‘noqdagi Ziyovuddin maqbarasiga.")
t.B("1723-yilda qoraqalpoqlarni uch guruhga bo‘lingan holda ko‘chishga majbur qilgan hujum kimniki?", "Jung‘or xonligi", "Rossiya", "Buxoro", "Xiva", "Jung‘or xonligining Turkistonga hujumi.")
t.B("1714-yilda Sirdaryo bo‘yi qoraqalpoqlari kim boshchiligida birlashgan?", "Eshmuhammad (Eshimxon)", "Abulg‘ozixon", "Elbarsxon", "To‘lepbergen", "Eshmuhammad (Eshimxon).")
t.B("Eshimxon davlati iqtisodiy va siyosiy jihatdan qaysi xonlikka qaram bo‘lgan?", "Kichik juz qozoq xonligiga", "Xiva xonligiga", "Buxoro xonligiga", "Jung‘or xonligiga", "Kichik juzga.")
t.NAT("1556-yilda Rossiya Ashtarxon xonligini bosib oldi.", "No‘g‘ay qabila sardorlari o‘rtasida nifoq va janjallar boshlandi", "No‘g‘ay xonligi kuchaydi", "qoraqalpoqlar Rossiyaga qo‘shildi", "Xiva No‘g‘ayni egalladi", "No‘g‘ayda nizolar boshlandi.")
t.NAT("XVII asr boshida Amudaryo eski o‘zaniga qaytdi.", "qoraqalpoqlar Amudaryo bo‘yidagi qadimiy joylariga qaytib, yerlarni qayta o‘zlashtirdi", "qoraqalpoqlar Volgaga ketdi", "Orol qurib qoldi", "Xiva poytaxti ko‘chirildi", "Qoraqalpoqlar qaytdi.")
t.NAT("XIX asr boshida qozoqlar siquvi va xonlar zulmi kuchaydi.", "Sirdaryo quyi oqimidagi qoraqalpoqlar Amudaryo quyi qismiga ko‘chdi", "qoraqalpoqlar Farg‘onaga ko‘chdi", "qoraqalpoqlar mustaqil davlat tuzdi", "qozoqlar Amudaryoga ketdi", "Amudaryoga ko‘chish.")
t.NAT("Eshimxon davlati Kichik juzga qaram bo‘lib qoldi.", "qoraqalpoqlar o‘lpon (yasoq) to‘lash va jangchi berishga majbur bo‘ldi", "qoraqalpoqlar soliqdan ozod bo‘ldi", "Kichik juz qoraqalpoqlarga bo‘ysundi", "davlat kengaydi", "O‘lpon to‘lashga majbur bo‘lgan.")
t.TF("XIV asr boshida No‘g‘ay ulusidagi qoraqalpoqlar Volga sohillariga ko‘chib o‘tgan.", True, "To‘g‘ri.")
t.TF("XVIII asrda qoraqalpoqlarning bir qismi Xitoyga emas, faqat Farg‘onaga ko‘chgan.", False, "Noto‘g‘ri: 1723-yildan keyin bir guruh Xitoy, Afg‘on yerlariga ham ko‘chgan.")
t.TF4([("«Qoraqalpoq» nomi qalpoqning shakli va rangiga qarab berilgan.", True), ("Eshimxon davlati Boshqird ulusi bilan chegaradosh bo‘lgan.", True),
       ("Qoraqalpoqlar Oltin O‘rda hukmronligida bo‘lmagan.", False), ("Qipchoq dashti qabilalari qoraqalpoq tiliga ta’sir o‘tkazgan.", True)],
      "3-noto‘g‘ri: G‘arbiy Xorazm, Ustyurt va Volgadagi qoraqalpoqlar Oltin O‘rda ostida bo‘lgan.")
t.MUL([("Qoraqalpoqlar Xorazm va Volga o‘rtasidagi kengliklarda yaxlit xalq sifatida shakllangan.", True),
       ("XVIII asrda qoraqalpoqlarning bir qismi Farg‘ona vodiysiga ko‘chib o‘tgan.", True),
       ("1714-yilgi davlat Xiva xonligining tarkibiy qismi edi.", False)],
      "III noto‘g‘ri: u Kichik juz qozoq xonligiga qaram bo‘lgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Rossiya Ashtarxonni bosib oldi", "No‘g‘ayda ocharchilik", "Abdullaxon II yorliqnomasi", "Eshimxon davlati tuzildi", "Jung‘orlarning Turkistonga hujumi"],
      "1556 → 1557–1558 → 1598 → 1714 → 1723.")
t.MATCH("Atamalarni ma’nosi bilan moslashtiring.", ["«chyorniye klobuki»", "«qora bo‘rkli»", "Orol (Aran)", "bijanak"],
        ["XII asr rus manbalaridagi nom", "qoraqalpoqlarga nisbatan qo‘llangan atama", "XVII asrda o‘zbeklar bilan tuzilgan davlat", "qoraqalpoqlar shakllangan turkiy qabila", "No‘g‘ay xonligi poytaxti"], 'abcd',
        "Chyorniye klobuki – rus manbasi; qora bo‘rkli – atama; Orol – davlat; bijanak – qabila.")
t.VENN("No‘g‘ay xonligi davri", "Eshimxon davlati",
       [("XV–XVI asrlar", 1), ("1557–1558-yilgi ocharchilik", 1),
        ("1714-yilda tuzilgan", 2), ("Kichik juzga o‘lpon to‘lagan", 2),
        ("qoraqalpoqlar tarixidagi bosqich", 3)],
       "No‘g‘ay – XV–XVI asr, ocharchilik; Eshimxon – 1714, o‘lpon; ikkalasi qoraqalpoqlar tarixi.")
t.MAPMATCH('steppe', ['Orol dengizi', 'Sig‘noq', 'Ashtarxon', 'Farg‘ona vodiysi'],
           ["qadimgi ajdodlar – massagetlar yashagan dengiz bo‘yi", "1598-yilgi yorliq berilgan Ziyovuddin maqbarasi shahri", "1556-yilda Rossiya bosib olgan xonlik markazi", "XVIII asrda qoraqalpoqlarning bir qismi ko‘chgan vodiy"],
           "1 – Orol; 2 – Sig‘noq; 3 – Ashtarxon; 4 – Farg‘ona vodiysi.")
