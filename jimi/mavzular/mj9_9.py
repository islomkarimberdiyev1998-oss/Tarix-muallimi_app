from qlib import Topic
TOPICS = {}
IN = 'india'; IA = 'iranafg'; NE = 'nearest'; BK = 'balkan'

# 29 Hindiston
t = Topic('e9j29', 9129); TOPICS['e9j29'] = t
t.B("Britaniya Hindistonni kim boshchiligidagi amaldorlar orqali boshqargan?", "vitse-qirol", "gubernator", "sulton", "maharaja", "Vitse-qirol boshchiligidagi amaldorlar va politsiya.")
t.B("1886-yilda Hindiston to‘qimachilik sanoatida nechta fabrika bo‘lgan?", "95 ta", "1300 ta", "600 ta", "26 ta", "95 ta.")
t.B("Mustamlakachilar qurgan sug‘orish inshootlari yerlarning qancha qismini sug‘orishga yetgan?", "20 foizini", "50 foizini", "80 foizini", "5 foizini", "Bor-yo‘g‘i 20 foizini.")
t.B("Assam qaysi mahsulot yetishtirishga ixtisoslashgan?", "choy", "kanop", "paxta", "bug‘doy", "Assam — choy; Bengaliya — kanop; Panjob — bug‘doy.")
t.B("1896–1906-yillarda Hindistonda ochlikdan qancha odam o‘lgan?", "10 mln dan ortiq", "1 mln", "100 ming", "50 mln", "10 mln dan ortiq.")
t.B("«Hindiston milliy kongressi» qachon va qayerda tuzilgan?", "1885-yilda Bombeyda", "1905-yilda Kalkuttada", "1906-yilda Dehlida", "1890-yilda Punada", "1885-yilda Bombey shahrida.")
t.B("«Milliy Kongress inqilobdan arzonroq», degan vitse-qirol kim?", "lord Dafferin", "Tilak", "Reyter", "Dyurand", "Lord Dafferin.")
t.B("HMKdagi «so‘l» — radikal oqimga kim rahbarlik qilgan?", "Bal Gangadxara Tilak", "lord Dafferin", "Sun Yat Sen", "Muhammad Tarziy", "Bal Gangadxara Tilak (1856–1920).")
t.B("Tilak qaysi shaharda mustaqil o‘rta maktab tashkil qilgan?", "Puna", "Bombey", "Kalkutta", "Surat", "Puna shahrida.")
t.B("Tilak tashkil etgan gazeta qanday atalgan?", "«Kesari» (Sher)", "«Minbao»", "«Ibrat»", "«Siroj ul-axbor»", "«Kesari» (Sher).")
t.B("Britaniya 1905-yilda qaysi viloyatni ikki qismga bo‘lgan?", "Bengaliyani", "Panjobni", "Assamni", "Bombeyni", "Bengaliyani.")
t.B("«Svaraj» so‘zi nimani anglatadi?", "«o‘z hokimiyatimiz»", "«o‘z ishlab chiqarishimiz»", "«boykot»", "«ozodlik yoki o‘lim»", "«O‘z hokimiyatimiz»; «Svadeshi» — «o‘z ishlab chiqarishimiz».")
t.B("HMK qurultoyi qaysi shaharda chaqirilib, radikal oqim chiqarilgan?", "Surat", "Bombey", "Kalkutta", "Dehli", "Bombey viloyatining Surat shahrida.")
t.B("«Hindiston kengashlari haqida qonun»ga ko‘ra aholining qancha qismi saylov huquqini olgan?", "yarim foizi", "10 foizi", "50 foizi", "hammasi", "Faqat yarim foizi.")
t.B("1911-yilda Hindiston poytaxti qayerga ko‘chirilgan?", "Dehliga", "Bombeyga", "Kalkuttaga", "Punaga", "Dehliga.")
t.NAT("1905-yilda Bengaliya ikki qismga bo‘lindi.", "milliy ozodlik harakati yangidan kuchayib, Kalkuttada katta namoyish bo‘ldi", "harakat so‘ndi", "Bengaliya mustaqil bo‘ldi", "Tilak hokimiyatga keldi", "Tadbir aks ta’sir ko‘rsatdi.")
t.NAT("1911-yilda mehnatkashlar harakatidan cho‘chigan ma’murlar chora ko‘rdi.", "bo‘lib tashlangan Bengaliya qayta birlashtirildi", "Bengaliya yana bo‘lindi", "Hindiston mustaqil bo‘ldi", "HMK taqiqlandi", "Bengaliya birlashtirildi, poytaxt Dehliga ko‘chdi.")
t.TF("Saylovlar diniy jamoa asosida o‘tkazilib, hindlar va musulmonlar alohida ovoz bergan.", True, "To‘g‘ri: maqsad ular orasiga nifoq solish edi.")
t.TF("Tilak qurolli qo‘zg‘olon yo‘lini tanlagan.", False, "Noto‘g‘ri: u «kuch ishlatmaslik» yo‘lini tanlagan.")
t.MUL([("Universitetlarga kirish puli ikki baravar oshirilib, huquq fakultetlari yopilgan.", True),
       ("Mustamlaka ma’muriyati ish vaqtini 12 soat bilan cheklagan.", True),
       ("Tilak inglizlar tomonidan umrbod qamalgan.", False)],
      "III noto‘g‘ri: u bir yarim yilga qamalib, tez orada ozod qilingan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["HMK tuzildi", "Radikal oqim shakllandi", "Bengaliya bo‘lindi", "«Svaraj» va «Svadeshi» qarori", "Bengaliya birlashtirildi, poytaxt Dehliga ko‘chdi"],
      "1885 → 1890 → 1905 → 1906 → 1911.")
t.MAPMATCH(IN, ['Bombey', 'Kalkutta', 'Dehli', 'Assam'],
           ["1885-yilda HMK tuzilgan shahar", "Bengaliya bo‘linishiga qarshi katta namoyish bo‘lgan shahar", "1911-yilda poytaxt ko‘chirilgan shahar", "choy yetishtirishga ixtisoslashgan hudud"],
           "1 – Bombey; 2 – Kalkutta; 3 – Dehli; 4 – Assam.")
t.VENN("HMKdagi mo‘tadil oqim", "HMKdagi radikal oqim",
       [("ingliz imperiyasi tarkibida qolishni ma’qullagan", 1), ("Surat qurultoyida g‘olib chiqqan", 1),
        ("Tilak rahbarlik qilgan", 2), ("ingliz boshqaruvidan ham voz kechishga chaqirgan", 2),
        ("Hindiston milliy kongressi tarkibida shakllangan", 3)],
       "Mo‘tadillar — imperiya tarkibida; radikallar — Tilak, to‘liq voz kechish.")

# 30 Eron
t = Topic('e9j30', 9130); TOPICS['e9j30'] = t
t.B("XIX asr oxiri – XX asr boshida Eron qanday holatga tushgan?", "yarimmustamlakaga aylangan", "mustaqil industrial davlat bo‘lgan", "respublika bo‘lgan", "Rossiyaga qo‘shilgan", "Sarmoyador davlatlarning yarimmustamlakasi.")
t.B("Eronga kapital chiqarish bo‘yicha qaysi davlat birinchi o‘rinda edi?", "Buyuk Britaniya", "Rossiya", "Germaniya", "Fransiya", "Buyuk Britaniya.")
t.B("1889-yilda «Shahanshohbank»ni kim ochgan?", "ingliz monopolisti Reyter", "Rokfeller", "Simens", "Morgan", "Ingliz monopolisti Reyter.")
t.B("Eron Britaniyadan qancha qarz bo‘lib qolgan?", "9,6 mln funt sterling", "164 mln rubl", "33 mln dollar", "5,5 mlrd frank", "9,6 mln funt sterling.")
t.B("Birinchi jahon urushi arafasida Eronning Rossiyadan qarzi qancha edi?", "164 mln rubl", "9,6 mln funt", "33 mln dollar", "100 mln rubl", "164 mln rubl.")
t.B("Eronda inqilobiy harakat qachon boshlangan?", "1905-yilda", "1906-yilda", "1907-yilda", "1911-yilda", "1905-yilda.")
t.B("Masjid va qabristonlarda tinch o‘tirib sust qarshilik ko‘rsatish qanday ataladi?", "best", "boykot", "svadeshi", "konsessiya", "Best.")
t.B("Shoh konstitutsiya qabul qilish haqida farmonni qachon chiqargan?", "1906-yil avgustida", "1905-yilda", "1907-yilda", "1909-yilda", "1906-yil avgustida.")
t.B("Majlisga saylovda nechta ijtimoiy qatlam saylov huquqiga ega bo‘lgan?", "6 ta", "3 ta", "10 ta", "2 ta", "Jami 6 ijtimoiy qatlam.")
t.B("Konstitutsiyaning birinchi qismini qaysi shoh tasdiqlagan?", "Muzaffariddin", "Muhammad Alishoh", "Ahmad shoh", "Nosiriddin", "Shoh Muzaffariddin.")
t.B("1907-yilda taxtga o‘tirgan mustabid tuzum tarafdori kim?", "Muhammad Alishoh", "Muzaffariddin", "Ahmad shoh", "Habibullo", "Muhammad Alishoh.")
t.B("Qonunlarning shariatga muvofiqligini nazorat qilish uchun nechta ulamo tayinlangan?", "besh", "uch", "o‘n", "yetti", "Besh ulug‘ ulamo.")
t.B("1907-yilgi Britaniya–Rossiya bitimiga ko‘ra Eron necha qismga bo‘lingan?", "uch qismga", "ikki qismga", "to‘rt qismga", "bo‘linmagan", "Shimoli — Rossiya, janubi — Britaniya, o‘rtasi — betaraf.")
t.B("Majlis halokatidan keyin inqilobiy harakat markazi qayerga ko‘chgan?", "Tabrizga", "Tehronga", "Mashhadga", "Isfahonga", "Tabrizga.")
t.B("Muhammad Alishoh taxtdan tushirilgach, kim shoh deb e’lon qilingan?", "uning o‘g‘li Ahmad", "Muzaffariddin", "Reyter", "Habibullo", "1909-yilda o‘g‘li Ahmad.")
t.NAT("Shoh xalq harakatiga qarshi qo‘shindan foydalanmoqchi bo‘ldi, ammo qo‘shin xalqqa o‘q uzishdan bosh tortdi.", "shoh 1906-yil avgustida konstitutsiya haqida farmon chiqarishga majbur bo‘ldi", "inqilob bostirildi", "shoh qochib ketdi", "Eron Rossiyaga qo‘shildi", "Shoh farmon chiqardi.")
t.NAT("Rossiya qo‘shini 1911-yilda aksilinqilobiy to‘ntarishda qatnashdi.", "Eron inqilobi bostirildi", "Eron respublika bo‘ldi", "Majlis kuchaydi", "Rossiya Erondan chiqdi", "Shu tariqa Eron inqilobi bostirildi.")
t.TF("Chet elliklar bilan iqtisodiy bitimlarga Majlisning roziligi olinishi belgilangan.", True, "To‘g‘ri.")
t.TF("1908-yilda Rossiya kazak qo‘shinlari Majlisni himoya qilgan.", False, "Noto‘g‘ri: ular Majlis binosini to‘pga tutgan.")
t.MUL([("1872-yilda Eron neft konlaridan foydalanish konsessiyalari olingan.", True),
       ("Mujohidlar 8 soatlik ish vaqti, bepul va majburiy ta’lim talabi bilan chiqqan.", True),
       ("1905–1911-yillardagi inqilob Eronni respublikaga aylantirgan.", False)],
      "III noto‘g‘ri: u feodal-monarxiyadan konstitutsiyaviy monarxiyaga o‘tish bosqichi bo‘ldi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["«Shahanshohbank» ochildi", "Inqilobiy harakat boshlandi", "Konstitutsiya haqida farmon", "Britaniya–Rossiya bitimi", "Majlis to‘pga tutildi", "Muhammad Alishoh taxtdan tushirildi", "Inqilob bostirildi"],
      "1889 → 1905 → 1906 → 1907 → 1908 → 1909 → 1911.")
t.MAPN(IA, ['Tehron', 'Hirot', 'Tabriz', 'Kobul'], "Qaysi raqam bilan Majlis tarqatilgach inqilobiy harakat markaziga aylangan, qamal qilingan shahar belgilangan?",
       "3 – Tabriz; 1 – Tehron: 1909-yilda Muhammad Alishoh shu yerda taxtdan tushirilgan.", ask_idx=2)
t.VENN("Inqilobning birinchi bosqichi (1905–1907)", "Inqilobning ikkinchi bosqichi (1907–1911)",
       [("konstitutsiya haqida farmon", 1), ("Majlisga birinchi saylov", 1),
        ("harakat asosan mustamlakachilarga qarshi qaratilgan", 2), ("mujohidlar tashkiloti katta ta’sirga ega bo‘lgan", 2),
        ("Eron inqilobi bosqichi", 3)],
       "Birinchi — konstitutsiya, Majlis; ikkinchi — mustamlakachilarga qarshi, mujohidlar.")

# 31 Afg‘oniston
t = Topic('e9j31', 9131); TOPICS['e9j31'] = t
t.B("Rossiyadan yordam so‘rab elchi yuborgan Afg‘on amiri kim?", "Sheralixon", "Abdurahmon", "Yoqubxon", "Habibullo", "Amir Sheralixon.")
t.B("Kobulga Rossiya elchilik missiyasi kim boshchiligida yuborilgan?", "general Stoletov", "Kaufman", "Dyurand", "Skobelev", "General Stoletov.")
t.B("Sheralixon ingliz missiyasini qachon Kobulga kiritmagan?", "1878-yilda", "1879-yilda", "1880-yilda", "1887-yilda", "1878-yilda.")
t.B("Gandamak bitimini kim imzolagan?", "Yoqubxon", "Sheralixon", "Abdurahmon", "Ayubxon", "1879-yilda Yoqubxon.")
t.B("Gandamak bitimiga ko‘ra Kobulda nima ochilgan?", "ingliz rezidensiyasi", "rus konsulligi", "bank", "universitet", "Ingliz rezidensiyasi.")
t.B("1880-yil boshida Shimoliy Afg‘onistonda kim hokimiyat o‘rnatgan?", "Abdurahmon", "Ayubxon", "Yoqubxon", "Habibullo", "Abdurahmon.")
t.B("Sheralixonning o‘g‘li Ayubxon qaysi shaharga yurish boshlagan?", "Qandahorga", "Kobulga", "Hirotga", "Peshovarga", "Qandahorga.")
t.B("Ikkinchi ingliz–afg‘on urushi qanday tugagan?", "Britaniyaning mag‘lubiyati bilan", "Afg‘onistonning taslim bo‘lishi bilan", "Rossiyaning g‘alabasi bilan", "Afg‘onistonning bo‘linishi bilan", "Britaniyaning mag‘lubiyati bilan.")
t.B("Amir Abdurahmon qaysi yillarda hukmronlik qilgan?", "1880–1901-yillarda", "1901–1919-yillarda", "1863–1879-yillarda", "1879–1880-yillarda", "1880–1901-yillarda.")
t.B("Afg‘on–rus chegarasi qachon qat’iy belgilangan?", "1887-yilda", "1880-yilda", "1907-yilda", "1901-yilda", "1887-yilda.")
t.B("Afg‘oniston janubidagi chegara chizig‘i kimning nomi bilan atalgan?", "Dyurand", "Stoletov", "Reyter", "Abdurahmon", "Dyurand chizig‘i.")
t.B("1901-yilda amirlik taxtini kim egallagan?", "Habibullo", "Omonulloxon", "Ayubxon", "Yoqubxon", "Abdurahmonning o‘g‘li Habibullo.")
t.B("1907-yilgi bitimda Afg‘oniston kimning manfaatlari mintaqasi deb e’lon qilingan?", "Buyuk Britaniya", "Rossiya", "Eron", "Germaniya", "Buyuk Britaniya.")
t.B("«Yosh afg‘onlar» harakatiga kim rahbarlik qilgan?", "Muhammad Tarziy", "Omonulloxon", "Habibullo", "Tilak", "«Siroj ul-axbori afg‘oniya» muharriri Muhammad Tarziy.")
t.B("Islohotchilarning butun umidi kimga qaratilgan?", "Omonulloxonga", "Habibulloga", "Ayubxonga", "Abdurahmonga", "Habibulloxonning uchinchi o‘g‘li Omonulloxonga.")
t.NAT("Amir Yoqubxon taslimchilik siyosatini yuritdi.", "Kobulda unga qarshi qo‘zg‘olon ko‘tarilib, ingliz rezidensiyasi egallandi", "Afg‘oniston Britaniyaga qo‘shildi", "Yoqubxon mukofotlandi", "Rossiya Kobulni oldi", "Shaharliklar rezidensiyaga bostirib kirdi.")
t.NAT("Abdurahmon Hind daryosi bo‘yidagi afg‘on qabilalarini inglizlarga qarshi kurashga chorladi.", "Britaniya bilan urush xavfi tug‘ilib, Abdurahmon bitim tuzishga majbur bo‘ldi", "qabilalar Afg‘onistonga qo‘shildi", "Britaniya Hindistondan chiqdi", "Rossiya urush e’lon qildi", "Dyurand chizig‘i bo‘yicha bitim tuzildi.")
t.TF("Amir Abdurahmon mamlakatda yopiq siyosat olib borib, yevropaliklarning kirishini taqiqlagan.", True, "To‘g‘ri.")
t.TF("XX asr boshida Afg‘onistonda rivojlangan ishlab chiqarish sanoati bo‘lgan.", False, "Noto‘g‘ri: Afg‘oniston sanoatsiz, qoloq davlat bo‘lib qoldi.")
t.MUL([("Abdurahmon diniy ulamolarga maosh belgilagan.", True),
       ("Abdurahmon davrida yagona pul birligi va o‘lchovlar joriy qilingan.", True),
       ("Habibullo Rossiya bilan savdo aloqalarini butunlay to‘xtatgan.", False)],
      "III noto‘g‘ri: u Rossiya bilan savdo aloqalarini o‘rnatishga uringan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Sheralixon ingliz missiyasini kiritmadi", "Gandamak bitimi", "Abdurahmon hokimiyati o‘rnatildi", "Afg‘on–rus chegarasi belgilandi", "Habibullo taxtga chiqdi", "Britaniya bilan bitim imzolandi"],
      "1878 → 1879 → 1880 → 1887 → 1901 → 1907.")
t.MAPMATCH(IA, ['Kobul', 'Qandahor', 'Hirot'],
           ["ingliz rezidensiyasi ochilgan Afg‘oniston poytaxti", "Ayubxon yurish qilgan, Britaniya ta’sir doirasida qolgan shahar", "Ayubxon chekinishga majbur bo‘lgan shahar"],
           "1 – Kobul; 2 – Qandahor; 3 – Hirot.")
t.VENN("Amir Abdurahmon", "Amir Habibullo",
       [("1880–1901-yillarda hukmronlik qilgan", 1), ("Dyurand chizig‘i bo‘yicha bitim tuzgan", 1),
        ("1901-yilda taxtni egallagan", 2), ("1907-yilda Britaniya bilan bitim imzolagan", 2),
        ("afg‘on qabilalarini birlashtirish siyosatini olib borgan", 3)],
       "Abdurahmon — 1880–1901, Dyurand; Habibullo — 1901-dan, 1907-bitim.")

# 32 Usmonli davlati
t = Topic('e9j32', 9132); TOPICS['e9j32'] = t
t.B("Usmonli davlatining tashqi qarzi qanchaga yetgan?", "5,5 mlrd frank", "9,6 mln funt", "164 mln rubl", "33 mln dollar", "5,5 mlrd frank.")
t.B("Hukumat Turkiyani qachon moliyaviy bankrot deb e’lon qilgan?", "1876-yilda", "1889-yilda", "1908-yilda", "1903-yilda", "1876-yilda.")
t.B("Usmonli davlati qaysi davlat bilan yaqinlashgan?", "Germaniya", "Rossiya", "Britaniya", "Fransiya", "Germaniya — imperiyadan ulush olmagan yagona davlat.")
t.B("Bag‘dod temiryo‘lining qaysi qismini qurish nemislarga tegdi?", "Izmir–Anqara qismi", "Istanbul–Sofiya qismi", "Bag‘dod–Basra qismi", "Anqara–Tehron qismi", "Izmir–Anqara qismi.")
t.B("«Yangi usmonlilar harakati»ning gazetasi qanday atalgan?", "«Ibrat»", "«Kesari»", "«Minbao»", "«Siroj ul-axbor»", "«Ibrat».")
t.B("1876-yilgi xalq qo‘zg‘olonidan keyin qaysi sulton taxtdan tushirilgan?", "Abdulaziz", "Abdulhamid II", "Mahmud II", "Mehmed V", "Abdulaziz, Shayx ul-Islom fatvosi bilan.")
t.B("Usmonli davlatida konstitutsiya qachon e’lon qilingan?", "1876-yil 23-dekabrda", "1908-yil 24-iyulda", "1889-yilda", "1909-yilda", "1876-yil 23-dekabrda.")
t.B("Konstitutsiyaga ko‘ra parlamentning yuqori palatasi qanday atalgan?", "Senat", "Majlis", "Duma", "Seym", "Senat; quyi palata — Deputatlar palatasi.")
t.B("Abdulhamid II davri qanday nom olgan?", "«Zulm davri»", "«Lola davri»", "«Tanzimat»", "«Oltin asr»", "«Zulm davri».")
t.B("«Birlik va taraqqiyot» tashkilotini kimlar tuzgan?", "Istanbul harbiy-tibbiy bilim yurti kursantlari", "ruhoniylar", "savdogarlar", "chet elliklar", "1889-yilda kursantlar.")
t.B("«Birlik va taraqqiyot» a’zolari umumiy nom bilan qanday atalgan?", "«Yosh turklar»", "«Yangi usmonlilar»", "«Yosh afg‘onlar»", "«Ixetuanlar»", "«Yosh turklar».")
t.B("1908-yil 20-iyulda qaysi shaharda konstitutsiya tiklanganligi e’lon qilingan?", "Monastirda", "Istanbulda", "Salonikida", "Anqarada", "Monastir shahrida.")
t.B("Abdulhamid konstitutsiyani qachon tiklashga majbur bo‘lgan?", "1908-yil 24-iyulda", "1908-yil 3-iyulda", "1909-yil 13-aprelda", "1912-yil 5-avgustda", "1908-yil 24-iyulda.")
t.B("«Yosh turklar»ni xudosizlikda ayblagan ruhoniylar partiyasi qaysi?", "«Ittihodi Muhammadi»", "«Hurriyat va birdamlik»", "«Birlik va taraqqiyot»", "«Yangi usmonlilar»", "«Ittihodi Muhammadi».")
t.B("1913-yil yanvaridagi isyonga «Yosh turklar» rahbarlaridan kim boshchilik qilgan?", "Anvarbey", "Tal’at", "Jamol", "Abdulhamid", "Anvarbey.")
t.B("Hokimiyatni olgan «Uchlik»ka kimlar kirgan?", "Anvar, Tal’at va Jamol", "Abdulhamid, Abdulaziz, Mehmed", "Tilak, Tarziy, Sun Yat Sen", "Kaufman, Skobelev, Chernyayev", "Anvar, Tal’at va Jamol.")
t.B("Germaniya va Usmonli davlati o‘rtasida maxfiy ittifoq shartnomasi qachon tuzilgan?", "1914-yil 2-avgustda", "1908-yilda", "1903-yilda", "1913-yilda", "1914-yil 2-avgustda.")
t.NAT("«Yosh turklar» o‘zlariga sodiq harbiy qismlar bilan 26-aprelda isyonchilar hukumatini ag‘dardi.", "sulton Abdulhamid taxtdan ag‘darildi", "Abdulhamid kuchaydi", "konstitutsiya bekor qilindi", "Usmonli davlati Antantaga qo‘shildi", "1909-yilda Abdulhamid taxtdan ag‘darildi.")
t.NAT("Usmonli davlati Germaniya bilan ittifoq shartnomasini imzoladi.", "hukmron doiralar imperiyani halokatga mahkum etdi", "imperiya kuchaydi", "Bolqon qaytarib olindi", "Usmonli davlati betaraf qoldi", "Bu imperiyani halokatga mahkum etdi.")
t.TF("Bolqon urushlarida Usmonli davlati Bolqondagi ta’siridan deyarli to‘la ajralgan.", True, "To‘g‘ri.")
t.TF("Konstitutsiyaga ko‘ra fuqarolarning ko‘pchiligi saylov huquqiga ega bo‘lgan.", False, "Noto‘g‘ri: juda oz qismigina saylov huquqiga ega bo‘lgan.")
t.MUL([("«Yosh turklar» birinchi qurultoyini Parijda o‘tkazgan.", True),
       ("1912-yil 5-avgustda «Hurriyat va birdamlik» partiyasi davlat to‘ntarishi o‘tkazgan.", True),
       ("Abdulhamid II «Birlik va taraqqiyot» tashkilotini qo‘llab-quvvatlagan.", False)],
      "III noto‘g‘ri: u tashkilot ustidan sud uyushtirib, 13 kishini o‘limga hukm qilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Konstitutsiya e’lon qilindi", "«Birlik va taraqqiyot» tuzildi", "Konstitutsiya tiklandi", "Abdulhamid taxtdan ag‘darildi", "«Hurriyat va birdamlik» to‘ntarishi", "Anvarbey isyoni", "Germaniya bilan maxfiy ittifoq"],
      "1876 → 1889 → 1908 → 1909 → 1912 → 1913 → 1914.")
t.MAPMATCH(BK, ['Istanbul', 'Monastir', 'Saloniki', 'Izmir'],
           ["«Birlik va taraqqiyot» tashkiloti tuzilgan poytaxt", "1908-yil 20-iyulda konstitutsiya tiklanganligi e’lon qilingan shahar", "«Yosh turklar» qochgan, harbiy qismlari ularga sodiq shahar", "Bag‘dod temiryo‘lining Anqaragacha qismi boshlanadigan shahar"],
           "1 – Istanbul; 2 – Monastir; 3 – Saloniki; 4 – Izmir.")
t.VENN("«Birlik va taraqqiyot»", "«Ittihodi Muhammadi»",
       [("«Yosh turklar» partiyasi", 1), ("konstitutsiyani tiklashga erishgan", 1),
        ("ruhoniylar partiyasi", 2), ("shariat va sulton hokimiyatini tiklashni talab qilgan", 2),
        ("Usmonli davlatidagi siyosiy kuch", 3)],
       "Birlik va taraqqiyot — konstitutsiya; Ittihodi Muhammadi — ruhoniylar, sulton hokimiyati.")
