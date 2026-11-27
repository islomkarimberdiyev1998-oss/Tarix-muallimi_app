from qlib import Topic
TOPICS = {}
EU = 'europe'; BK = 'balkan'; IT = 'italy'; AF = 'africa'

# 22 Avstriya-Vengriya imperiyasi
t = Topic('e9j22', 9122); TOPICS['e9j22'] = t
t.B("Avstriya-Vengriya imperiyasi qachon vujudga kelgan?", "1867-yilda", "1871-yilda", "1848-yilda", "1878-yilda", "1867-yilda Avstriya va Vengriya hukmron tabaqalari bitimi asosida.")
t.B("Avstriya qirolligi tarkibiga qaysi hududlar kirgan?", "Chexiya, Moraviya, Galitsiya, Bukovina", "Slovakiya, Xorvatiya, Transilvaniya", "Bosniya, Serbiya", "Bavariya, Saksoniya", "Chexiya, Moraviya, Galitsiya va Bukovina.")
t.B("Vengriya tarkibiga qaysi hududlar kirgan?", "Slovakiya, Xorvatiya, Transilvaniya", "Chexiya, Moraviya, Galitsiya", "Bosniya va Gersegovina", "Bolgariya va Ruminiya", "Slovakiya, Xorvatiya va Transilvaniya.")
t.B("Avstriya imperatori qaysi sulola vakili edi?", "Gabsburglar", "Gogensollernlar", "Romanovlar", "Burbonlar", "Gabsburglar sulolasi (1867–1918).")
t.B("Vengriyada qirol hokimiyatini qaysi organ cheklagan?", "Seym", "Reyxstag", "Duma", "Senat", "Seym.")
t.B("Imperiyada nechta umumimperiya vazirligi tashkil etilgan?", "3 ta", "5 ta", "10 ta", "2 ta", "Tashqi ishlar, harbiy va dengiz, moliya.")
t.B("Shahar aholisi imperiya aholisining qancha qismini tashkil qilgan?", "uchdan birini", "yarmini", "to‘rtdan uchini", "o‘ndan birini", "Faqat uchdan birini.")
t.B("Vengriyaning asosiy sanoat tarmog‘i qaysi edi?", "oziq-ovqat sanoati", "metallurgiya", "to‘qimachilik", "kimyo", "Oziq-ovqat sanoati.")
t.B("Avstriya hukumati ishchilar harakatiga qarshi «Favqulodda qonun»ni qachon joriy etgan?", "1884-yilda", "1878-yilda", "1889-yilda", "1907-yilda", "1884-yilda.")
t.B("Avstriya sotsial-demokratik partiyasi qachon tuzilgan?", "1889-yilda", "1884-yilda", "1907-yilda", "1867-yilda", "1889-yilda.")
t.B("Saylov tizimi islohoti haqidagi qonun qachon qabul qilingan?", "1907-yilda", "1889-yilda", "1912-yilda", "1884-yilda", "1907-yilda.")
t.B("Chexiyada sud va ma’muriy ishlar uchun nechta til joriy qilingan?", "ikkita", "bitta", "uchta", "to‘rtta", "Ikki til — nemis va chex.")
t.B("Avstriya-Vengriyada og‘ir iqtisodiy inqiroz qachon yuz bergan?", "1912-yilda", "1907-yilda", "1884-yilda", "1900-yilda", "1912-yilda.")
t.B("Imperiyani Avstriya, Vengriya va slavyan yerlaridan iborat federatsiyaga aylantirish g‘oyasi qanday atalgan?", "trializm", "irredentizm", "antisemitizm", "panslavizm", "Trializm (uchlik).")
t.B("Yahudiylarga qarshi dushmanlikni avj oldirish siyosati nima deyiladi?", "antisemitizm", "shovinizm", "irredentizm", "anarxizm", "Antisemitizm.")
t.NAT("Federatsiyaning slavyan qismi kuchayib ketishidan hukmron doiralar cho‘chidi.", "trializm g‘oyasi rad etilib, ichki ziddiyatlar keskinligicha qoldi", "federatsiya tuzildi", "slavyanlar mustaqil bo‘ldi", "imperiya tarqatildi", "Trializm rad etildi.")
t.NAT("Urushga tayyorgarlik va milliy zulmga qarshi Budapeshtda ko‘p ming kishilik namoyish bo‘ldi.", "Budapesht barrikadalarga to‘lib, kuchlar teng bo‘lmagani uchun namoyish to‘xtatildi", "hukumat iste’fo berdi", "urush tayyorgarligi to‘xtadi", "Vengriya mustaqil bo‘ldi", "Namoyishchilar politsiya kuchlariga duch keldi.")
t.TF("Avstriya-Vengriya konstitutsiyaviy monarxiya edi.", True, "To‘g‘ri.")
t.TF("Imperiya sanoati chet el kapitaliga qaram bo‘lmagan.", False, "Noto‘g‘ri: Fransiya, Belgiya, Germaniya kapitaliga qaramlik kuchaygan.")
t.MUL([("Imperiya aholisining aksariyatini bo‘ysundirilgan slavyan xalqlari tashkil etgan.", True),
       ("Praga universitetida o‘qitish nemis va chex tillarida olib boriladigan bo‘ldi.", True),
       ("Vengriya qirolligi o‘z parlamentiga ega bo‘lmagan.", False)],
      "III noto‘g‘ri: Vengriya o‘z parlamenti, ijroiya hokimiyati va muxtoriyatiga ega edi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Avstriya-Vengriya imperiyasi vujudga keldi", "«Favqulodda qonun»", "ASDP tuzildi", "Saylov tizimi islohoti", "Og‘ir iqtisodiy inqiroz"],
      "1867 → 1884 → 1889 → 1907 → 1912.")
t.MAPMATCH(EU, ['Vena', 'Budapesht', 'Praga', 'Galitsiya'],
           ["imperiya poytaxti, yirik banklar to‘plangan shahar", "Vengriyaning asosiy shahri, barrikada janglari bo‘lgan", "o‘qitish ikki tilda olib borilgan universitet shahri", "ukrain va polyak aholisi milliy zulm ostida bo‘lgan hudud"],
           "1 – Vena; 2 – Budapesht; 3 – Praga; 4 – Galitsiya.")
t.VENN("Avstriya", "Vengriya",
       [("imperator hokimiyatini Reyxstag cheklagan", 1), ("tarkibida Chexiya va Galitsiya", 1),
        ("qirol hokimiyatini Seym cheklagan", 2), ("asosiy sanoati oziq-ovqat", 2),
        ("1867-yilgi bitim asosida birlashgan", 3)],
       "Avstriya — Reyxstag, Chexiya; Vengriya — Seym, oziq-ovqat sanoati.")

# 23 Avstriya-Vengriyaning tashqi siyosati
t = Topic('e9j23', 9123); TOPICS['e9j23'] = t
t.B("Avstriya-Vengriya tashqi siyosatining markazida qaysi hudud turgan?", "Bolqon yarimoroli", "Shimoliy Afrika", "Uzoq Sharq", "O‘rta Osiyo", "Bolqon yarimoroli.")
t.B("Avstriya-Vengriya Bolqondagi maqsadlari uchun qaysi davlat bilan yaqinlashgan?", "Germaniya", "Rossiya", "Fransiya", "Britaniya", "Germaniya bilan.")
t.B("Slavyan xalqlari milliy ozodlik kurashida qaysi davlatga tayangan?", "Rossiyaga", "Germaniyaga", "Avstriya-Vengriyaga", "Italiyaga", "Rossiyaga.")
t.B("Avstriya-Vengriya Bosniya va Gersegovinani qachon egallagan?", "1908-yilda", "1878-yilda", "1912-yilda", "1914-yilda", "1908-yilda.")
t.B("Bolqon ittifoqiga qaysi davlatlar kirgan?", "Bolgariya, Serbiya, Chernogoriya, Gretsiya", "Ruminiya, Bolgariya, Turkiya", "Avstriya, Vengriya, Serbiya", "Rossiya, Serbiya, Bosniya", "Bolgariya, Serbiya, Chernogoriya va Gretsiya.")
t.B("Birinchi Bolqon urushi qachon boshlangan?", "1912-yilda", "1913-yilda", "1908-yilda", "1914-yilda", "1912-yilda Usmonli davlatiga qarshi.")
t.B("1913-yilda Bolgariya qaysi davlatlarga hujum qilgan?", "Serbiya va Gretsiyaga", "Usmonli davlatiga", "Ruminiyaga", "Avstriya-Vengriyaga", "Serbiya va Gretsiyaga — Ikkinchi Bolqon urushi.")
t.B("Ikkinchi Bolqon urushida kim yengilgan?", "Bolgariya", "Serbiya", "Gretsiya", "Chernogoriya", "Bolgariya.")
t.B("Urush natijasida qaysi davlat Bolqonning yetakchi davlatiga aylangan?", "Serbiya", "Bolgariya", "Gretsiya", "Ruminiya", "Serbiya.")
t.B("Avstriya-Vengriya taxti vorisi kim edi?", "Frans Ferdinand", "Frans Iosif", "Vilgelm II", "Ferdinand Koburg", "Frans Ferdinand.")
t.B("Frans Ferdinandni kimlar o‘ldirgan?", "serb millatchilari", "rus inqilobchilari", "italyan anarxistlari", "turk askarlari", "Serb millatchilari.")
t.B("Avstriya-Vengriya parlamenti qachon tarqatib yuborilgan?", "1914-yilda", "1912-yilda", "1908-yilda", "1907-yilda", "1914-yilda.")
t.B("Harbiylarning cheklanmagan hokimiyati nima deyiladi?", "harbiy diktatura", "trializm", "federatsiya", "protektorat", "Harbiy diktatura.")
t.NAT("Avstriya-Vengriya 1908-yilda Bosniya va Gersegovinani egalladi, Rossiya bunga to‘sqinlik qila olmadi.", "slavyan xalqlari orasida Rossiya obro‘siga putur yetdi", "Rossiya Bosniyani egalladi", "Serbiya Avstriyaga qo‘shildi", "Germaniya Rossiyani qo‘llab-quvvatladi", "Rossiya obro‘si tushdi.")
t.NAT("Usmonli davlati va Italiya o‘rtasidagi urushda Usmonli davlati yengildi.", "janubiy slavyanlarning ozodlik kurashi kuchayib, Bolqon ittifoqi tuzildi", "Usmonli davlati kuchaydi", "Italiya Bolqonni egalladi", "slavyanlar Usmonliga bo‘ysundi", "Bu Bolqon ittifoqiga qulay sharoit yaratdi.")
t.NAT("Ittifoqchilar Usmonli davlatidan ozod etilgan hududlarni bo‘lishda kelisha olmadi.", "Ikkinchi Bolqon urushi boshlandi", "Bolqon ittifoqi mustahkamlandi", "Usmonli davlati hududlarni qaytarib oldi", "Rossiya hududlarni egalladi", "1913-yilda Bolgariya Serbiya va Gretsiyaga hujum qildi.")
t.TF("Frans Ferdinandning o‘ldirilishi urushni boshlash uchun bahona bo‘lgan.", True, "To‘g‘ri.")
t.TF("Ikkinchi Bolqon urushida Usmonli davlati Bolgariya tarafida jang qilgan.", False, "Noto‘g‘ri: Usmonli davlati ham Bolgariyaga qarshi urushgan.")
t.MUL([("Bolgariyaning da’volarini Avstriya-Vengriya qo‘llab-quvvatlagan.", True),
       ("Ikkinchi Bolqon urushida Chernogoriya va Ruminiya Serbiya va Gretsiyaga yordam bergan.", True),
       ("Birinchi Bolqon urushi Usmonli davlati g‘alabasi bilan tugagan.", False)],
      "III noto‘g‘ri: urush slavyanlar va greklarning ozod bo‘lishi bilan tugagan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Berlin kongressi", "Bosniya va Gersegovinaning egallanishi", "Birinchi Bolqon urushi", "Ikkinchi Bolqon urushi", "Frans Ferdinandning o‘ldirilishi"],
      "1878 → 1908 → 1912 → 1913 → 1914.")
t.MAPMATCH(BK, ['Bosniya va Gersegovina', 'Serbiya', 'Bolgariya', 'Gretsiya'],
           ["1908-yilda Avstriya-Vengriya egallagan hudud", "Ikkinchi Bolqon urushidan keyin Bolqonning yetakchi davlati", "1913-yilda qo‘shnilariga hujum qilib yengilgan davlat", "Bolqon ittifoqiga qo‘shilgan grek davlati"],
           "1 – Bosniya va Gersegovina; 2 – Serbiya; 3 – Bolgariya; 4 – Gretsiya.")
t.VENN("Birinchi Bolqon urushi", "Ikkinchi Bolqon urushi",
       [("1912-yilda boshlangan", 1), ("Bolqon ittifoqi Usmonli davlatiga qarshi", 1),
        ("1913-yilda Bolgariya hujumi bilan boshlangan", 2), ("Bolgariya yengilgan", 2),
        ("Bolqon yarimorolidagi urush", 3)],
       "Birinchi — 1912, Usmonliga qarshi; Ikkinchi — 1913, Bolgariya yengildi.")

# 24 Italiya
t = Topic('e9j24', 9124); TOPICS['e9j24'] = t
t.B("Rim shahri qachon Italiya qirolligi poytaxtiga aylantirilgan?", "1870-yil 3-oktabrda", "1871-yilda", "1861-yilda", "1896-yilda", "1870-yil 3-oktabrda.")
t.B("Rim shahrining Italiyaga qo‘shilishiga qarshilik qilgan papa kim?", "Piy IX", "Lev XIII", "Piy X", "Ioann XXIII", "Papa Piy IX.")
t.B("Italiyada qonun chiqaruvchi hokimiyatni parlament bilan bo‘lgan qirol kim?", "Viktor Emmanuil II", "Umberto I", "Garibaldi", "Kavur", "Qirol Viktor Emmanuil II.")
t.B("Italiya senatorlari qanday tayinlangan?", "qirol tomonidan umrbod", "xalq tomonidan 5 yilga", "papa tomonidan", "parlament tomonidan 4 yilga", "Qirol tomonidan umrbod.")
t.B("1871-yilgi qonunga ko‘ra papa qarorgohi joylashgan shahar-davlat qaysi?", "Vatikan", "Rim", "Milan", "Venetsiya", "Vatikan.")
t.B("Zamindorlar yerni dehqonlarga hosilning qancha qismini to‘lash sharti bilan berardi?", "3/4 qismini", "1/3 qismini", "yarmini", "1/10 qismini", "3/4 qismini.")
t.B("Italiya savdo floti dunyoda qaysi o‘ringa chiqqan?", "uchinchi", "birinchi", "ikkinchi", "beshinchi", "Uchinchi o‘ringa.")
t.B("«Fiat» aksiyadorlik jamiyati qachon tashkil topgan?", "1906-yilda", "1898-yilda", "1911-yilda", "1870-yilda", "1906-yilda.")
t.B("1898-yilda qaysi shahardagi umumiy ish tashlash 5 kunlik barrikada janglariga aylangan?", "Milan", "Rim", "Neapol", "Turin", "Milanda.")
t.B("1903–1914-yillarda Italiya hukumatini kim boshqargan?", "J. Jolitti", "Kavur", "Mussolini", "Garibaldi", "J. Jolitti.")
t.B("«Sanoat taraqqiyoti tepasida ish haqi yuqori bo‘lgan mamlakatlar turadi», degan kim?", "J. Jolitti", "Bismark", "Vilson", "Gladston", "J. Jolitti.")
t.B("Italyanlar yashaydigan qo‘shni hududlarni qo‘shib olishni targ‘ib qiluvchi harakat qanday atalgan?", "irredentizm", "trializm", "antisemitizm", "shovinizm", "Irredentizm.")
t.B("1896-yil 1-avgustda Italiya qo‘shinlari qayerda tor-mor etilgan?", "Adua yonida", "Tripolida", "Somalida", "Tunisda", "Adua yonida; 5 ming askar halok bo‘ldi.")
t.B("Italiya va Fransiya o‘rtasida betaraflik bitimi qachon imzolangan?", "1902-yilda", "1909-yilda", "1896-yilda", "1911-yilda", "1902-yilda.")
t.B("Italiya Liviyaga qachon hujum qilgan?", "1911-yilda", "1912-yilda", "1896-yilda", "1909-yilda", "1911-yilda; 1912-yildan Liviya mustamlakaga aylandi.")
t.NAT("Italiya da’vo qilgan Shimoliy Afrika hududlarini Fransiya egalladi.", "Italiya Germaniya bilan yaqinlashib, Uchlar ittifoqiga qo‘shildi", "Italiya Fransiya bilan ittifoq tuzdi", "Italiya Afrikadan voz kechdi", "Italiya Rossiyaga qo‘shildi", "Bu Italiyani Germaniyaga yaqinlashtirdi.")
t.NAT("Adua yonida 5 ming italyan askari halok bo‘ldi.", "bu voqea Italiyada milliy sharmandalik sifatida qabul qilindi", "Italiya Efiopiyani bosib oldi", "Italiya Uchlar ittifoqidan chiqdi", "Jolitti hokimiyatga keldi", "Milliy sharmandalik deb baholandi.")
t.TF("Jolitti davrida tungi smenada bolalar va ayollar mehnatidan foydalanmaslik haqida qonun qabul qilingan.", True, "To‘g‘ri.")
t.TF("Italiya aholi jon boshiga daromad bo‘yicha G‘arbiy Yevropada birinchi o‘rinda edi.", False, "Noto‘g‘ri: oxirgi o‘rinda edi.")
t.MUL([("Hukumat Italiyani Fransiya va Shveytsariya bilan bog‘laydigan ikkita tunnel qurdi.", True),
       ("1909-yilda Italiya Rossiya bilan Bolqondagi manfaatlarini quvvatlovchi bitim tuzgan.", True),
       ("Italiya Birinchi jahon urushigacha industrial davlatga aylangan.", False)],
      "III noto‘g‘ri: Italiya agrar mamlakatligicha qolgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Rim poytaxt bo‘ldi", "Cherkov va davlat haqidagi qonun", "Adua yonidagi mag‘lubiyat", "Milandagi barrikada janglari", "Fransiya bilan bitim", "«Fiat» tashkil topdi", "Liviyaga hujum"],
      "1870 → 1871 → 1896 → 1898 → 1902 → 1906 → 1911.")
t.MAPN(AF, ['Liviya', 'Marokash', 'Efiopiya', 'Madagaskar'], "Qaysi raqam bilan 1896-yilda Adua yonida italyan qo‘shinlari tor-mor etilgan davlat belgilangan?",
       "3 – Efiopiya; 1 – Liviya 1912-yildan Italiya mustamlakasi bo‘ldi.", ask_idx=2)
t.VENN("Jolitti davridagi ichki siyosat", "Italiyaning tashqi siyosati",
       [("kasaba uyushmalari va ish tashlashga ruxsat", 1), ("saylovchilarning mulk va savodxonlik senzi bekor qilingan", 1),
        ("1902-yilda Fransiya bilan betaraflik bitimi", 2), ("1911-yilda Liviyaga hujum", 2),
        ("XX asr boshida amalga oshirilgan", 3)],
       "Ichki — kasaba uyushmalari, senz bekor; tashqi — Fransiya bilan bitim, Liviya.")
