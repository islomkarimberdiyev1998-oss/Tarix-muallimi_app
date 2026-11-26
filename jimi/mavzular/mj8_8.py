from qlib import Topic
TOPICS = {}
W = 'globe'; EU = 'europe'; ME = 'mideast'; OA = 'oldasia'; AF = 'africa'

# 30 Usmoniylar 1800–1870
t = Topic('e8j30', 830); TOPICS['e8j30'] = t
t.B("Usmoniylar imperiyasining davlat tuzumi qanday edi?", "mutlaq monarxiya", "konstitutsion monarxiya", "respublika", "federatsiya", "Imperiya mutlaq monarxiya bo‘lib qoldi.")
t.B("Ruhoniylardan boshqa barcha davlat xizmatchilari kim hisoblangan?", "sultonning quli", "erkin fuqaro", "zodagon", "sipohiy", "Barcha xizmatchilar sultonning quli hisoblangan.")
t.B("Yevropa davlatlarining Usmoniylarga qaram o‘lkalar uchun kurashi qanday nom olgan?", "«Sharq masalasi»", "«Qit’a qamali»", "«Yopiq eshiklar»", "«Muqaddas liga»", "Bu kurash «Sharq masalasi» deb ataldi.")
t.B("Rossiya qaysi bo‘g‘ozlarni qo‘lga kiritishga intilgan?", "Bosfor va Dardanell", "Gibraltar va Bosfor", "Magellan va Dardanell", "Bering va Bosfor", "Qora dengizning Bosfor va Dardanell bo‘g‘ozlari.")
t.B("Gretsiyaga muxtoriyat berish haqidagi bitim qachon va qayerda imzolangan?", "1827-yilda Londonda", "1830-yilda Parijda", "1856-yilda Parijda", "1840-yilda Istanbulda", "1827-yili Londonda.")
t.B("Fransiya Jazoirni qachon bosib olgan?", "1830-yilda", "1827-yilda", "1840-yilda", "1853-yilda", "1830-yili.")
t.B("Sultonga qarshi bosh ko‘targan Misr hukmdori kim?", "Muhammad Ali", "Mustafo III", "Salim I", "Xayriddin", "Misr hukmdori Muhammad Ali.")
t.B("Sultonni Muhammad Ali hujumidan kim saqlab qolgan?", "Rossiya", "Fransiya", "Buyuk Britaniya", "Avstriya", "Sultonni Rossiya saqlab qoldi.")
t.B("Muhammad Ali Misr va Sudanni meros qoldirish huquqini qachon olgan?", "1840-yilda", "1830-yilda", "1827-yilda", "1856-yilda", "1840-yili.")
t.B("Qrim urushidan oldin Rossiya sultondan nimani talab qilgan?", "pravoslav xalqlar homiysi deb tan olinishni", "Istanbulni berishni", "Misrni berishni", "boj to‘lashni", "Rossiyani pravoslav xalqlar homiysi deb tan olishni talab qildi.")
t.B("Qrim urushida qaysi ittifoq g‘alaba qozongan?", "Britaniya, Fransiya va Turkiya", "Rossiya va Avstriya", "Rossiya va Prussiya", "Fransiya va Rossiya", "Uchlik ittifoqi g‘alaba qozondi.")
t.B("Qrim urushidan keyin qanday shartnoma imzolangan?", "1856-yilgi Parij tinchlik shartnomasi", "Kuchukqaynarji", "London bitimi", "Vena kongressi", "1856-yilgi Parij shartnomasi.")
t.B("«Konsessiya» so‘zi nimani anglatadi?", "davlat mulkini muddatga chet el kapitaliga berish", "boj to‘lovi", "harbiy ittifoq", "muxtoriyat", "Konsessiya – chet el kapitaliga berish shartnomasi.")
t.NAT("Muhammad Ali sulton qo‘shinini tor-mor etdi.", "Istanbulga yo‘l ochildi, Rossiya sultonni himoyaga oldi", "Misr Turkiyani egalladi", "Fransiya Istanbulni oldi", "Muhammad Ali sulton bo‘ldi",
      "Rossiya kuchsiz sultonni kuchli Muhammad Alidan ma’qul ko‘rdi.")
t.NAT("1856-yilgi Parij shartnomasi imzolandi.", "chet elliklarga Turkiyada yer sotib olish ruxsat berilib, yarimmustamlakaga yo‘l ochildi", "Turkiya mustaqilligi mustahkamlandi", "Rossiya Bosforni oldi", "konsessiyalar bekor qilindi",
      "Shartnoma G‘arb davlatlari «homiyligi»ni o‘rnatdi.")
t.TF("Qrim urushidagi g‘alaba Turkiyaning Britaniya va Fransiyaga qaramligini kuchaytirgan.", True, "To‘g‘ri.")
t.TF("Usmoniylar imperiyasidagi islohotlar mutaassib din arboblari qo‘llab-quvvatlagani uchun muvaffaqiyatli bo‘lgan.", False, "Noto‘g‘ri: islohotlar mutaassiblar va chet davlatlar qarshiligi tufayli amalga oshmadi.")
t.MUL([("Yevropa davlatlari imperiya xalqlarining ozodlik kurashidan aralashuv quroli sifatida foydalangan.", True), ("XIX asr 60-yillariga kelib mustamlakachilar Turkiya siyosatini belgilay boshlagan.", True), ("Qrim urushida Rossiya g‘alaba qozongan.", False)],
      "III noto‘g‘ri: Rossiya mag‘lub bo‘lgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["London bitimi (Gretsiya)", "Fransiya Jazoirni bosib oldi", "Muhammad Ali meros huquqini oldi", "Qrim urushi boshlandi", "Parij tinchlik shartnomasi"],
      "1827 → 1830 → 1840 → 1853 → 1856.")
t.MAPMATCH('crusade', ['Istanbul', 'Gretsiya', 'Qohira', 'Falastin'],
           ["Rossiya egallashga intilgan imperiya poytaxti", "1827-yilda muxtoriyat berilishi kelishilgan o‘lka", "Muhammad Ali hukmronlik qilgan Misr poytaxti", "xristianlik muqaddas qadamjolari joylashgan hudud"],
           "1 – Istanbul; 2 – Gretsiya; 3 – Qohira; 4 – Falastin.")
t.VENN("Rossiya maqsadlari", "Britaniya va Fransiya maqsadlari",
       [("Bosfor, Dardanell va Istanbulni egallash", 1), ("pravoslav xalqlar homiysi bo‘lish", 1),
        ("imperiyani o‘z ta’sirida tutish", 2), ("Muhammad Alini qo‘llab-quvvatlash", 2),
        ("Usmoniylar o‘lkalaridan o‘lja olish", 3)],
       "Rossiya – bo‘g‘ozlar; Britaniya va Fransiya – ta’sir. Hammasi «Sharq masalasi» ishtirokchisi.")

# 31 Eron va Afg'oniston
t = Topic('e8j31', 831); TOPICS['e8j31'] = t
t.B("XIX asrda Eron qanday davlat edi?", "mutlaq monarxiya", "respublika", "konstitutsion monarxiya", "federatsiya", "Eron mutlaq monarxiya bo‘lib, shoh cheklanmagan huquqqa ega edi.")
t.B("Eronda bosh vazir qanday atalgan?", "sadri a’zam", "amin ad-davla", "hakimboshi", "beklarbegi", "Sadri a’zam – bosh vazir.")
t.B("Moliya va ichki ishlar vaziri qanday atalgan?", "amin ad-davla", "sadri a’zam", "hakimboshi", "shayxulislom", "Amin ad-davla.")
t.B("Taxt vorisining qarorgohi qaysi shahar edi?", "Tabriz", "Tehron", "Isfahon", "Mashhad", "Taxt vorisiga Ozarbayjon berilgan, qarorgohi Tabrizda.")
t.B("Eron Rossiya bilan urushlarda qachon mag‘lub bo‘lgan?", "1826–1828-yillarda", "1853–1856-yillarda", "1838–1842-yillarda", "1856–1857-yillarda", "1826–1828-yillarda Eron mag‘lub bo‘ldi.")
t.B("Bobiylar qo‘zg‘oloni qachon boshlangan?", "1848-yilda", "1850-yilda", "1856-yilda", "1826-yilda", "1848-yili boshlandi.")
t.B("Bobiylik ta’limotining asoschisi kim?", "sayyid Ali Muhammad", "Do‘st Muhammadxon", "Mir Vaysxon", "Ahmadshoh", "Asoschisi sayyid Ali Muhammad (Bob).")
t.B("«Bob» taxallusi qanday ma’noni anglatadi?", "«Haqiqat va adolat yo‘liga olib chiquvchi eshik»", "«javohirlar javohiri»", "«ma’rifatli boshqaruv»", "«kengash»", "Bob – haqiqat va adolat yo‘liga eshik.")
t.B("Eron Hirotni qachon bosib olgan?", "1856-yilda", "1857-yilda", "1848-yilda", "1838-yilda", "1856-yili Eron Hirotni bosib oldi.")
t.B("Eron Hirotdan voz kechgan Parij shartnomasi qachon imzolangan?", "1857-yilda", "1856-yilda", "1855-yilda", "1863-yilda", "1857-yili Parij tinchlik shartnomasi imzolandi.")
t.B("1709-yilda Qandahordagi qo‘zg‘olonga kim rahbarlik qilgan?", "Mir Vaysxon", "Mir Mahmud", "Ahmadxon", "Fathxon", "Gilzoiy qabilasi xoni Mir Vaysxon.")
t.B("Afg‘oniston shohi deb qachon Ahmadxon e’lon qilingan?", "1747-yilda", "1736-yilda", "1722-yilda", "1826-yilda", "1747-yili jirg‘a Ahmadxonni shoh deb e’lon qildi.")
t.B("Ahmadshoh qanday unvonni qabul qilgan?", "«Durri durron»", "«Sohibqiron»", "«Amir al-muslimin»", "«Shahanshoh»", "«Durri durron» – javohirlar javohiri.")
t.B("Afg‘on qabila xonlarining kengashi qanday atalgan?", "jirg‘a", "qurultoy", "divan", "senat", "Jirg‘a – kengash.")
t.B("Do‘st Muhammadxon Afg‘oniston taxtini qachon egallagan?", "1826-yilda", "1747-yilda", "1842-yilda", "1863-yilda", "1826-yili taxtni egallab, o‘zini amir deb e’lon qildi.")
t.B("Birinchi ingliz–afg‘on urushi qaysi yillarda bo‘lgan?", "1838–1842", "1826–1828", "1856–1857", "1878–1880", "1838–1842-yillarda.")
t.B("Inglizlar Kobul taxtiga kimni o‘tqazgan?", "Shuju", "Akbarshoh", "Fathxon", "Mir Mahmud", "Durroniylar vakili Shuju.")
t.NAT("Britaniya Eronni teng bo‘lmagan savdo shartnomasini imzolashga majbur etdi.", "Eron bozorlari ingliz mahsulotlariga to‘lib, mahalliy hunarmandlar xonavayron bo‘ldi", "Eron sanoati rivojlandi", "Eron Britaniyaga qarshi urushda g‘alaba qozondi", "savdo to‘xtadi",
      "Eron Britaniya sanoat mahsulotlari bozoriga aylandi.")
t.NAT("Kobul aholisi qo‘zg‘olon ko‘tardi (Akbarshoh katta rol o‘ynadi).", "1842-yilda ingliz qo‘shini Afg‘onistondan chiqib ketdi", "Britaniya Kobulni mustahkam egalladi", "Shuju kuchaydi", "Rossiya Afg‘onistonni egalladi",
      "Birinchi ingliz–afg‘on urushi Britaniya mag‘lubiyati bilan tugadi.")
t.NAT("1857-yilda Britaniya bilan Afg‘oniston o‘rtasida harbiy shartnoma tuzildi.", "bu Afg‘onistonni vassal davlatga aylantirish yo‘lidagi birinchi qadam bo‘ldi", "Afg‘oniston Britaniyaga qo‘shildi", "Rossiya Afg‘onistonni egalladi", "urush boshlandi",
      "Shartnoma Afg‘onistonni vassalga aylantirish yo‘lidagi birinchi qadam bo‘ldi.")
t.TF("Bobiylar qo‘zg‘oloni bostirilib, Ali Muhammad qatl etilgan.", True, "To‘g‘ri.")
t.TF("Afg‘oniston XIX asrda Britaniya mustamlakasiga aylangan.", False, "Noto‘g‘ri: Afg‘oniston mustaqilligini saqlab qoldi.")
t.MUL([("Do‘st Muhammadxon 1855-yilda ingliz–afg‘on do‘stlik shartnomasini imzolagan.", True), ("Fathxon barakzaylar yetakchisi bo‘lib, bosh vazir lavozimini egallagan.", True), ("XIX asr oxirida Afg‘oniston eng taraqqiy etgan mamlakatlardan biri edi.", False)],
      "III noto‘g‘ri: Afg‘oniston taraqqiyotning eng ortida qolib ketdi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Mir Vays qo‘zg‘oloni", "Ahmadxon shoh deb e’lon qilindi", "Do‘st Muhammadxon amir bo‘ldi", "Birinchi ingliz–afg‘on urushi tugadi", "Bobiylar qo‘zg‘oloni", "Parij tinchlik shartnomasi"],
      "1709 → 1747 → 1826 → 1842 → 1848 → 1857.")
t.MAPMATCH('iranafg', ['Qandahor', 'Kobul', 'Hirot', 'Tehron'],
           ["1709-yilda Mir Vays qo‘zg‘oloni bo‘lgan viloyat", "inglizlar egallagan, keyin qo‘zg‘olon ko‘targan shahar", "1856-yilda Eron bosib olgan shahar", "Eron poytaxti"],
           "1 – Qandahor; 2 – Kobul; 3 – Hirot; 4 – Tehron.")
t.VENN("Eron (XIX asr)", "Afg‘oniston (XIX asr)",
       [("bobiylar qo‘zg‘oloni bo‘lgan", 1), ("kuchli davlatlar yarimmustamlakasiga aylangan", 1),
        ("mustaqilligini saqlab qolgan", 2), ("durroniylar, keyin barakzaylar sulolasi", 2),
        ("Britaniya bilan urushgan", 3)],
       "Eron – bobiylar, yarimmustamlaka. Afg‘oniston – mustaqil, barakzaylar. Ikkalasi Britaniya bilan urushgan.")

# 32 Afrika 1800–1870
t = Topic('e8j32', 832); TOPICS['e8j32'] = t
t.B("G‘arbiy Afrikadagi eng qadimgi davlatlar qaysilar?", "Gana va Mali", "Efiopiya va Misr", "Liberiya va Gvineya", "Angola va Kongo", "Gana va Mali eng qadimgi davlatlar.")
t.B("Qaysi Portugaliya mustamlakalari eng muhim qul savdosi bazalari edi?", "Angola va Mozambik", "Liberiya va Gana", "Misr va Sudan", "Jazoir va Tunis", "Angola va Mozambik.")
t.B("XIX asr oxiriga kelib qit’a hududining qancha qismi mustamlakachilar qo‘liga o‘tgan?", "90 foizi", "50 foizi", "25 foizi", "10 foizi", "90 foizi mustamlakachilar qo‘liga o‘tdi.")
t.B("Afrikada mustaqilligini saqlab qolgan ikki davlat qaysilar?", "Liberiya va Efiopiya", "Misr va Sudan", "Marokash va Tunis", "Gana va Mali", "Liberiya va Efiopiya.")
t.B("AQShda ozod qora tanlilarni Afrikaga joylashtirish harakati qachon boshlangan?", "1816-yilda", "1821-yilda", "1847-yilda", "1830-yilda", "1816-yili boshlandi.")
t.B("1821-yilda Gvineya qirg‘og‘ida tashkil etilgan manzilgoh qanday atalgan?", "Monroviya", "Liberiya", "Akkra", "Lagos", "AQSH prezidenti Monro nomidan Monroviya.")
t.B("Liberiya ozod davlati qachon e’lon qilingan?", "1847-yilda", "1821-yilda", "1855-yilda", "1867-yilda", "1847-yili.")
t.B("Efiopiyani birlashtirib, 1855-yilda imperator bo‘lgan kim?", "Kassa", "Abdulqodir", "Muhammad Ali", "Menelik", "Kichik yer egasining o‘g‘li Kassa.")
t.B("Kassa hokimiyati qachon ag‘darilgan?", "1867-yilda", "1855-yilda", "1847-yilda", "1870-yilda", "Britaniya aralashuvi bilan 1867-yili ag‘darildi.")
t.B("Britaniya Janubiy Afrikada qaysi koloniyani bosib olgan?", "Kap koloniyasi", "Transvaal", "Oranj", "Natal", "XIX asr boshida Kap koloniyasi.")
t.B("Kap koloniyasining fransuz, nemis va golland avlodlari qanday atalgan?", "burlar", "kreollar", "mamluklar", "metislar", "Burlar (bur – dehqon).")
t.B("Burlar tuzgan ikki davlat qaysilar?", "Oranj Respublikasi va Transvaal", "Liberiya va Efiopiya", "Kap va Natal", "Angola va Mozambik", "Ozod Oranj Respublikasi va Transvaal.")
t.B("Jazoirliklarning fransuzlarga qarshi kurashida kim alohida rol o‘ynagan?", "Abdulqodir", "Xayriddin", "Kassa", "Muhammad Ali", "Yo‘lboshchi Abdulqodir.")
t.B("Abdulqodir qo‘shini qachon tor-mor etilgan?", "1847-yilda", "1830-yilda", "1855-yilda", "1867-yilda", "1847-yili qurshab olinib tor-mor etildi.")
t.B("Fransiya Hind okeanida qaysi orolni bosib olishga urinib, muvaffaqiyatsiz bo‘lgan?", "Madagaskar", "Shri Lanka", "Mavrikiy", "Zanzibar", "Madagaskarni bosib olishga urinishlar muvaffaqiyatsiz bo‘ldi.")
t.NAT("Liberiya Buyuk Britaniya va Fransiya raqobatidan ustalik bilan foydalandi.", "o‘z mustaqilligini saqlab qoldi", "mustamlakaga aylandi", "AQShga qo‘shildi", "Efiopiya bilan birlashdi",
      "Raqobatdan foydalanib mustaqilligini saqlab qoldi.")
t.NAT("Kassaning islohotlari yirik feodallar va cherkov qarshiligiga uchradi.", "Britaniya aralashuvi bilan 1867-yilda uning hokimiyati ag‘darildi", "Kassa Afrikani birlashtirdi", "cherkov uni qo‘llab-quvvatladi", "Efiopiya mustamlakaga aylandi",
      "Biroq Britaniya Efiopiyada mustahkam o‘rnasha olmadi.")
t.NAT("Mustamlakachilar Afrikaning qoloqligi va qabilalar ziddiyatidan foydalandi.", "XIX asr oxirida Afrikani bosib olish asosan yakunlandi", "Afrika birlashdi", "mustamlakachilar chekindi", "qul savdosi kuchaydi",
      "Asr oxirida qit’a deyarli to‘liq bo‘lib olindi.")
t.TF("Liberiyada G‘arbiy Yevropa va Shimoliy Amerika tartib-qoidalari joriy etilgan.", True, "To‘g‘ri.")
t.TF("Kassa yirik feodallarga o‘z qo‘shiniga ega bo‘lishga ruxsat bergan.", False, "Noto‘g‘ri: u feodallarni o‘z qo‘shiniga ega bo‘lish huquqidan mahrum etgan.")
t.MUL([("Fransiya Jazoirni 1830-yilda bosib olgan.", True), ("Marokash aholisi mustamlakachilarga muvaffaqiyatli qarshilik ko‘rsatgan.", True), ("XIX asr 70-yillarida Afrikaning ichki hududlari yevropaliklarga to‘liq ma’lum edi.", False)],
      "III noto‘g‘ri: ichki hududlar hali deyarli noma’lum edi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Qora tanlilarni joylashtirish harakati boshlandi", "Monroviya tashkil etildi", "Fransiya Jazoirni bosib oldi", "Liberiya ozod davlati e’lon qilindi", "Kassa imperator bo‘ldi", "Kassa hokimiyati ag‘darildi"],
      "1816 → 1821 → 1830 → 1847 → 1855 → 1867.")
t.MAPMATCH(AF, ['Liberiya', 'Efiopiya', 'Kap koloniyasi', 'Madagaskar'],
           ["1847-yilda ozod davlat deb e’lon qilingan mamlakat", "Kassa imperator bo‘lgan mamlakat", "Britaniya bosib olgan Janubiy Afrika koloniyasi", "Fransiya bosib ololmagan orol"],
           "1 – Liberiya; 2 – Efiopiya; 3 – Kap; 4 – Madagaskar.")
t.VENN("Liberiya", "Efiopiya",
       [("AQShdan kelgan ozod qora tanlilar tuzgan", 1), ("1847-yilda ozod davlat e’lon qilingan", 1),
        ("Kassa 1855-yilda birlashtirgan", 2), ("feodal monarxiya qaror topgan", 2),
        ("XIX asr oxirida mustaqilligini saqlab qolgan", 3)],
       "Liberiya – ozod qullar, 1847. Efiopiya – Kassa, monarxiya. Ikkalasi mustaqil qolgan.")
