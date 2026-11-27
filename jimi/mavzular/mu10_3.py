from qlib import Topic, PLACES, REG
TOPICS = {}
CA = 'ca'
TK = 'Petro-Aleksandrovsk (To‘rtko‘l)'

# 7-§. Xiva xonligi, XXSR
t = Topic('e10u7', 10107); TOPICS['e10u7'] = t
t.B("Xiva xoni Asfandiyorxon Yosh xivaliklarning islohot to‘g‘risidagi manifestiga qachon imzo chekdi?", "1917-yil 5-aprelda", "1917-yil 8-aprelda", "1917-yil 7-aprelda", "1918-yil 30-oktyabrda", "1917-yil 5-aprelda.")
t.B("Yosh xivaliklar partiyasi qachon tashkil topgan?", "1914-yilda", "1917-yilda", "1910-yilda", "1905-yilda", "Partiya 1914-yilda tashkil topgan.")
t.B("Islohotlar ijrosini nazorat qilish uchun tuzilgan 30 kishilik organ qanday atalgan?", "Idorai mashruta", "Nozirlar Sho‘rosi", "Majlis", "Revkom", "30 kishidan iborat Idorai mashruta.")
t.B("1917-yil aprelda Xivada tuzilgan Majlisga kim boshchilik qildi?", "qozikalon Bobooxun Salimov", "Husaynbek Matmurodov", "Polvonniyoz Yusupov", "Is’hoqxo‘ja Xo‘jayev", "Majlis – Bobooxun Salimov, Nozirlar Sho‘rosi – Husaynbek Matmurodov.")
t.B("Yosh xivaliklar partiyasi rahbari kim bo‘lgan?", "Polvonniyoz Yusupov", "Bobooxun Salimov", "Junaidxon", "Qo‘shmamedxon Sapiyev", "Partiya rahbari – Polvonniyoz Yusupov.")
t.B("Asfandiyorxon Majlisni tarqatib yuborishda kimning harbiy kuchlariga tayandi?", "general Mirbadalov", "general Kuropatkin", "F.Kolesov", "M.V.Frunze", "Muvaqqat hukumatning Xivadagi vakili general Mirbadalov.")
t.B("Majlisning nechta sobiq a’zosi qamoqqa olinib, keyinchalik qatl etildi?", "17 nafar", "30 nafar", "10 nafar", "8 nafar", "Husaynbek Matmurodov boshchiligidagi 17 nafar sobiq a’zo.")
t.B("Junaidxonning asl ismi nima bo‘lgan?", "Qurbon Mamed Sardor", "Said Abdullaxon", "Davlatmurod mahram", "G‘ulomalixon Bahodir", "Asl ismi – Qurbon Mamed Sardor, yovmut urug‘idan.")
t.B("Amudaryo bo‘limining markazi qaysi shahar bo‘lgan?", "Petro-Aleksandrovsk (To‘rtko‘l)", "Xiva", "Urganch", "Chimboy", "Markazi – Petro-Aleksandrovsk (hozirgi To‘rtko‘l).")
t.B("Asfandiyorxon qachon o‘ldirildi?", "1918-yil 30-oktyabrda", "1917-yil noyabrda", "1919-yil 9-aprelda", "1920-yil 1-fevralda", "1918-yil 30-oktyabrdagi saroy fitnasi oqibatida.")
t.B("Asfandiyorxondan keyin taxtga kim o‘tirdi?", "Said Abdullaxon", "Junaidxon", "Davlatmurod mahram", "Polvonniyoz Yusupov", "Marhum xonning katta akasi Said Abdullaxon (1918 – 1920).")
t.B("Taxta shartnomasi qachon imzolandi?", "1919-yil 9-aprelda", "1919-yil 4-noyabrda", "1920-yil 2-fevralda", "1918-yil 30-oktyabrda", "1919-yil 9-aprelda Taxta qishlog‘ida.")
t.B("Xiva xonligi poytaxti Xiva qachon bosib olindi?", "1920-yil 1-fevralda", "1920-yil 2-fevralda", "1919-yil 4-noyabrda", "1920-yil 26-aprelda", "1920-yil 1-fevralda.")
t.B("XXSR tuzilganligi qaysi qurultoyda e’lon qilindi?", "Butunxorazm xalq vakillarining I qurultoyida (1920-yil 26 – 30-aprel)", "Butunxorazm IV qurultoyida", "Butunbuxoro I qurultoyida", "Butunxorazm V qurultoyida", "1920-yil 26 – 30-aprelda Xivada I qurultoyda.")
t.B("XXSR Nozirlar Sho‘rosi raisi qilib kim saylandi?", "Polvonniyoz Yusupov", "Bobooxun Salimov", "Fayzulla Xo‘jayev", "Qalandar Odinayev", "Polvonniyoz Yusupov.")
t.B("1921-yil 24-noyabrda Afg‘onistonga jo‘natilgan elchilik hay’atiga kim boshchilik qildi?", "qozikalon Bobooxun Salimov", "Polvonniyoz Yusupov", "Junaidxon", "Husaynbek Matmurodov", "Qozikalon Bobooxun Salimov.")
t.B("XXSRda qishloq xo‘jaligida yagona soliq tizimi qachon joriy qilindi?", "1922-yil dekabrda", "1923-yil iyunda", "1921-yil martda", "1920-yil bahorida", "1922-yil dekabrda.")
t.B("Xivada xalq dorilfununi qachon ochildi?", "1921-yil sentyabrda", "1920-yil bahorida", "1922-yil dekabrda", "1923-yil oktyabrda", "1921-yil sentyabrda.")
t.B("XXSR qaysi qurultoyda Xorazm SSRga aylantirildi?", "IV qurultoyda (1923-yil 17 – 20-oktyabr)", "I qurultoyda", "V qurultoyda", "II qurultoyda", "1923-yil 17 – 20-oktyabrdagi IV qurultoyda.")
t.NAT("1919-yil 9-aprelda Taxta shartnomasi imzolandi.", "Xiva xonligi mustaqilligi sovet hokimiyati tomonidan tan olindi", "Xiva xonligi tugatildi", "XXSR tuzildi", "Junaidxon Afg‘onistonga ketdi", "Bitimda Xiva xonligi mustaqilligi tan olindi.")
t.NAT("1921-yil 6-martda Xorazmda qizil askarlar harbiy davlat to‘ntarishini uyushtirdi.", "P.Yusupov hukumati ag‘darib tashlandi", "XXSR Konstitutsiyasi qabul qilindi", "Junaidxon taslim bo‘ldi", "Xiva xoni taxtga qaytdi", "P.Yusupov hukumati ag‘darildi, ko‘plab nozirlar otib tashlandi.")
t.TF("1917-yil aprelda Xiva xonligida qisqa muddatga konstitutsion monarxiya o‘rnatildi.", True, "To‘g‘ri: Majlis va Nozirlar Sho‘rosi tuzilishi bilan.")
t.TF("XXSR mavjud bo‘lgan 5 yil davomida MIK raislari va hukumat boshliqlari bir martadan ham o‘zgartirilmagan.", False, "Noto‘g‘ri: ularning har biri 10 martadan o‘zgartirilgan.")
t.MUL([("Manifestda temiryo‘l, pochta, telegraf barpo etish zarurligi ta’kidlangan.", True),
       ("Xiva olingach Said Abdullaxon taxtdan voz kechdi, Junaidxon Qoraqumga chekindi.", True),
       ("XSSR Konstitutsiyasiga ko‘ra vaqf mulklari qozixonalar ixtiyoriga berildi.", False)],
      "III noto‘g‘ri: vaqf mulklari maorif nozirligiga berildi, qozixonalar taqiqlandi.")
t.MATCH("Shaxslarni ular bilan bog‘liq ma’lumotlar bilan moslashtiring.", ["Asfandiyorxon", "Junaidxon", "Said Abdullaxon", "Husaynbek Matmurodov"],
        ["Nozirlar Sho‘rosi raisi (1917)", "1918 – 1920-yillarda xon", "Yosh xivaliklar manifestini imzolagan xon", "1918-yilda xonlik qurolli kuchlari qo‘mondoni"],
        "cdba", "Asfandiyorxon – manifest; Junaidxon – qo‘mondon; Said Abdullaxon – 1918 – 1920 xon; Matmurodov – Nozirlar Sho‘rosi.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["Asfandiyorxonning manifestni imzolashi", "Asfandiyorxonning o‘ldirilishi", "Taxta shartnomasi", "Xivaning bosib olinishi", "XXSRning tuzilishi"],
      "1917-yil 5-aprel → 1918-yil 30-oktyabr → 1919-yil 9-aprel → 1920-yil 1-fevral → 1920-yil 26 – 30-aprel.")
t.MAPN('xorazm', ['Xiva', TK, 'Ko‘hna Urganch', 'Chimboy'], "Turkiston general-gubernatorligi tarkibidagi Amudaryo bo‘limining markazi qaysi raqam bilan belgilangan?",
       "Amudaryo bo‘limining markazi Petro-Aleksandrovsk (hozirgi To‘rtko‘l) edi.", ask_idx=1)
t.VENN("Xiva xonligi (1917 – 1920)", "XXSR (1920 – 1923)",
       [("Majlis va Nozirlar Sho‘rosi xon huzurida tuzilgan", 1), ("Taxta shartnomasi bilan mustaqilligi tan olingan", 1),
        ("muvaqqat Konstitutsiya va Bayroq qabul qilgan", 2), ("Xivada xalq dorilfununi ochilgan", 2),
        ("poytaxti Xiva shahri bo‘lgan", 3)],
       "Xonlik – Majlis, Taxta shartnomasi; XXSR – Konstitutsiya, dorilfunun; ikkalasining markazi Xiva.")

# 8-§. BXSR va XXSRda qizil armiyaga qarshi kurash
t = Topic('e10u8', 10108); TOPICS['e10u8'] = t
t.B("Sobiq amir Olimxon Sharqiy Buxoroga qachon keldi?", "1920-yil sentyabrda", "1921-yil martda", "1920-yil avgustda", "1921-yil oktyabrda", "1920-yil sentyabrda.")
t.B("G‘arbiy Buxoro hududida istiqlolchilarga kim rahbarlik qildi?", "Mulla Abdulqahhor", "Ibrohimbek", "Davlatmandbek", "Junaidxon", "G‘arbiy Buxoroda – Mulla Abdulqahhor.")
t.B("Sharqiy Buxoro hududida qaysi qo‘rboshilar harakatga rahbarlik qildi?", "Ibrohimbek va Davlatmandbek", "Mulla Abdulqahhor va Hamro Polvon", "Madaminbek va Shermuhammadbek", "Bahrombek va Ochilbek", "Ibrohimbek va Davlatmandbek.")
t.B("Olimxon qachon Afg‘oniston hududiga o‘tib ketishga majbur bo‘ldi?", "1921-yil martda", "1920-yil sentyabrda", "1922-yil avgustda", "1924-yil iyunda", "1921-yil martda.")
t.B("Mulla Abdulqahhor qo‘l ostida Buxoroning g‘arbiy qismida nechta qo‘rboshi birlashgan?", "20 nafar", "30 nafar", "100 nafar", "10 nafar", "20 nafar qo‘rboshi birlashgan.")
t.B("Mulla Abdulqahhor qachon va qayerda halok bo‘ldi?", "1924-yil oxirida Qizilqumda", "1922-yil avgustda Obidarada", "1923-yil 10-mayda Kitobda", "1921-yil martda Nurotada", "1924-yil oxirida Qizilqumdagi janglarning birida.")
t.B("Ibrohimbek Sharqiy Buxoroda qanday boshqaruv usulini joriy qildi?", "amirlik davridagi boshqaruv usulini", "sovet boshqaruvini", "g‘arbcha respublika boshqaruvini", "Turkiston Muxtoriyati tartibini", "Yangi Buxoro hukumati tugatilib, amirlik davridagi boshqaruv joriy qilindi.")
t.B("Buxorodagi istiqlolchilik harakatida Turkiyadan kelgan qaysi generallar ishtirok etgan?", "Anvar va Salim Posho", "Mustafo Kamol va Ismat Posho", "Jamol va Tal’at Posho", "Kozim va Fevzi Posho", "Anvar va Salim Posho.")
t.B("Anvar Posho Mulla Nafis qo‘rboshi bilan qayerda uchrashdi?", "Qarshi yaqinidagi Qiliko‘l atrofida", "Baljuvon atrofidagi Obidarada", "Buxoro shahrida", "Dushanbeda", "1921-yil 9-noyabrda Qarshi yaqinidagi Qiliko‘l atrofida.")
t.B("Anvar Posho qachon halok bo‘ldi?", "1922-yil avgustda", "1921-yil noyabrda", "1923-yil yanvarda", "1924-yil iyunda", "1922-yil avgustda Obidara qishlog‘ida.")
t.B("Cho‘lpon Anvar Posho xotirasiga qanday marsiya yozdi?", "“Baljuvon”", "“Buzilgan o‘lka”", "“Kishan”", "“Turkiston”", "“Baljuvon” marsiyasi.")
t.B("Qaysi BXSR rahbari lavozimini tark etib, qurolli harakat safiga o‘tib ketgan?", "MIK raisi Usmon Xo‘ja", "Fayzulla Xo‘jayev", "Porso Xo‘jayev", "Abdulqodir Muhitdinov", "Usmon Xo‘ja, Abdulhamid Oripov va boshqalar o‘tib ketgan.")
t.B("1922-yil ko‘klamida Junaidxon qo‘shinlari soni qancha bo‘lgan?", "15 000 nafar", "30 000 nafar", "20 000 nafar", "2000 nafar", "15 000 nafar yigit.")
t.B("1922-yil aprelda Junaidxon qo‘shinlari qaysi shaharni ozod qildi?", "Porsu", "Xiva", "To‘rtko‘l", "Chimboy", "Porsu shahri va uning atroflari.")
t.B("XXSR MIK II sessiyasida RSFSRdan “shoshilinch harbiy yordam” qachon so‘raldi?", "1923-yil 12-yanvarda", "1922-yil aprelda", "1924-yil 17-iyunda", "1921-yil 6-martda", "1923-yil 12-yanvarda.")
t.B("Junaidxonni “Rossiya hukmronligi oldida bo‘yin egishni xohlamagan davlat qahramoni” deb ta’riflagan kim?", "Ahmad Zaki Validiy", "M.Frunze", "Cho‘lpon", "Fitrat", "Ahmad Zaki Validiy “Xotiralar” kitobida.")
t.B("Istiqlolchilik harakatining ikkinchi davri qaysi yillarni o‘z ichiga oladi?", "1925 – 1935-yillar", "1918 – 1924-yillar", "1920 – 1930-yillar", "1924 – 1929-yillar", "Ikkinchi davr 1925 – 1935-yillar.")
t.B("Yagona qo‘mondonlikka bo‘ysunmagan qo‘rboshilar qatorida kim tilga olingan?", "Xolxo‘ja Eshon", "Mulla Abdulqahhor", "Anvar Posho", "Ibrohimbek", "Xolxo‘ja Eshon, G‘ulomalixon Bahodir va boshqalar.")
t.NAT("1921-yil martda Olimxon bir qator janglarda mag‘lubiyatga uchradi.", "u Afg‘onistonga o‘tib ketishga majbur bo‘ldi", "Buxoro amirligi tiklandi", "BXSR tugatildi", "Anvar Posho halok bo‘ldi", "Olimxon Afg‘onistonga o‘tib ketdi.")
t.NAT("1924-yil kuzida O‘rta Osiyoda milliy-hududiy chegaralanish o‘tkazildi.", "qurolli kurashning birinchi davri yakunlandi", "istiqlolchilar g‘alaba qozondi", "Junaidxon XXSR raisi bo‘ldi", "Anvar Posho Buxoroga keldi", "Qurolli kurashning birinchi davri yakunlandi.")
t.TF("Junaidxon qo‘shinlari safida turkman va o‘zbeklardan tashqari qozoq va qoraqalpoqlar ham ko‘p edi.", True, "To‘g‘ri.")
t.TF("Turkistondagi istiqlolchilik harakati 1924-yilda butunlay mag‘lubiyatga uchradi.", False, "Noto‘g‘ri: harakat 1935-yilga kelib mag‘lubiyatga uchradi.")
t.MUL([("Junaidxon 1924-yil 17-iyunda 20 nafar hamrohi bilan Hirotga yetib keldi.", True),
       ("Anvar Posho 1921-yil oktyabrda Kavkazdan Buxoroga kelgan.", True),
       ("Harakat mag‘lubiyatining sababi uning yagona markaz ostida to‘liq birlashganidir.", False)],
      "III noto‘g‘ri: eng zaif tomoni yagona markaz ostida to‘liq birlasha olmaganligi edi.")
t.MATCH("Istiqlolchilar rahbarlarini faoliyat hududlari bilan moslashtiring.", ["Mulla Abdulqahhor", "Ibrohimbek", "Junaidxon"],
        ["Xorazm", "G‘arbiy Buxoro", "Sharqiy Buxoro"], "bca",
        "Mulla Abdulqahhor – G‘arbiy Buxoro; Ibrohimbek – Sharqiy Buxoro; Junaidxon – Xorazm.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["Olimxonning Sharqiy Buxoroga kelishi", "Olimxonning Afg‘onistonga o‘tib ketishi", "Anvar Poshoning Mulla Nafis bilan uchrashuvi", "Anvar Poshoning halok bo‘lishi", "Junaidxonning Hirotga yetib kelishi"],
      "1920-yil sentyabr → 1921-yil mart → 1921-yil 9-noyabr → 1922-yil avgust → 1924-yil 17-iyun.")
t.MAPMATCH('buxamir', ['G‘ijduvon', 'Qarshi', 'Baljuvon'],
           ["Mulla Abdulqahhor qo‘rboshilari faoliyat ko‘rsatgan tumanlardan biri", "Anvar Posho Mulla Nafis bilan uchrashgan Qiliko‘l shu shahar yaqinida", "Anvar Posho halok bo‘lgan Obidara qishlog‘i shu joy atrofida"],
           "1 – G‘ijduvon; 2 – Qarshi; 3 – Baljuvon.")
t.MAP1(CA, 'Hirot', "Junaidxon 1924-yil 17-iyunda 20 nafar hamrohi bilan yetib kelgan bu shahar qaysi?", "Hirot", ["Kobul", "Mashhad", "Balx"],
       "Junaidxon Afg‘onistondagi Hirot shahriga yetib kelgan.")
t.VENN("Mulla Abdulqahhor", "Anvar Posho",
       [("G‘arbiy Buxoroda 20 qo‘rboshini birlashtirgan", 1), ("Qizilqumdagi jangda halok bo‘lgan", 1),
        ("Turkiyadan kelgan general", 2), ("Obidara qishlog‘ida halok bo‘lgan", 2),
        ("Buxorodagi istiqlolchilik harakati rahbari", 3)],
       "Abdulqahhor – G‘arbiy Buxoro, Qizilqum; Anvar Posho – turk generali, Obidara; ikkalasi Buxoro istiqlolchilari rahbari.")

# 9-§. Milliy-hududiy chegaralanish
t = Topic('e10u9', 10109); TOPICS['e10u9'] = t
t.B("1918 – 1924-yillarda Turkiston mintaqasida qaysi davlatlar mavjud bo‘lgan?", "Turkiston ASSR, BXSR, XXSR", "O‘zSSR, Turkmaniston SSR, Tojikiston ASSR", "Buxoro amirligi, Xiva va Qo‘qon xonliklari", "Qozog‘iston ASSR va Qirg‘iziston SSR", "Turkiston ASSR, BXSR va XXSR.")
t.B("1920-yildayoq yagona Turkistonni alohida qismlarga ajratib bo‘lmaydi degan g‘oyani ilgari surgan milliy kommunistlar guruhiga kim boshchilik qilgan?", "Turor Risqulov", "Ya.Rudzutak", "Akmal Ikromov", "Qalandar Odinayev", "T.Risqulov boshchiligidagi milliy kommunistlar.")
t.B("Markaz kommunistlari yagona Turkiston g‘oyasini qanday baholagan?", "“panturkizm”, “panislomizm”, “burjua millatchiligi”", "“internatsionalizm”", "“leninizm”", "“sotsializm”", "Noto‘g‘ri ravishda panturkizm, panislomizm deb baholangan.")
t.B("1924-yil fevralda Buxoro Kompartiyasi chegaralanish yuzasidan kimning tezislarini qabul qildi?", "Fayzulla Xo‘jayev", "Akmal Ikromov", "Sultonbek Xo‘janov", "Turor Risqulov", "F.Xo‘jayev yozgan tezislar.")
t.B("O‘rta Osiyo federatsiyasini tuzish taklifi bilan chiqqanlardan biri kim?", "Sultonbek Xo‘janov", "Ya.Rudzutak", "Qalandar Odinayev", "I.V.Stalin", "S.Xo‘janov, S.Asfandiyorov, N.Paskutskiy.")
t.B("1923-yil dekabrda Farg‘ona vodiysi vakillari qanday taklif bilan chiqdi?", "RSFSR tarkibida Farg‘ona muxtor viloyatini tashkil etish", "Farg‘onani Qirg‘izistonga qo‘shish", "Farg‘ona mustaqil respublikasini tuzish", "Farg‘onani BXSRga qo‘shish", "RSFSR tarkibida Farg‘ona muxtor viloyati.")
t.B("Xorazmni chegaralanishga qo‘shmaslikni yoqlagani uchun lavozimidan olingan Xorazm Kompartiyasi MK mas’ul kotibi kim?", "Qalandar Odinayev", "Polvonniyoz Yusupov", "Abdulla Rahimboyev", "Sultonbek Xo‘janov", "Qalandar Odinayev 1924-yil iyulda olib tashlandi.")
t.B("Xorazm Kompartiyasining yangi rahbarlari chegaralanishga qachon rozilik bildirdi?", "1924-yil 26-iyulda", "1924-yil 8-mayda", "1924-yil 12-iyunda", "1924-yil 29-oktyabrda", "1924-yil 26-iyulda.")
t.B("RKP(b) MK Siyosiy byurosining chegaralash to‘g‘risidagi qarori kimning taklifi bilan qabul qilingan?", "I.V.Stalin", "V.I.Lenin", "Ya.Rudzutak", "M.I.Kalinin", "1924-yil 12-iyunda Stalinning taklifi bilan.")
t.B("RKP(b) MK O‘rta Osiyo byurosi raisi kim bo‘lgan?", "Ya.Rudzutak", "I.V.Stalin", "I.Vareykis", "V.Ivanov", "O‘rta Osiyo byurosi raisi – Y.Rudzutak.")
t.B("Turkiston ASSR MIK favqulodda sessiyasi chegaralanish to‘g‘risida qachon qaror qabul qildi?", "1924-yil 16-sentyabrda", "1924-yil 20-sentyabrda", "1924-yil 29-oktyabrda", "1924-yil 14-oktyabrda", "1924-yil 16-sentyabrda.")
t.B("Butunxorazm xalq vakillarining V qurultoyi chegaralanish to‘g‘risida qachon qaror qabul qildi?", "1924-yil 29-oktyabrda", "1924-yil 20-sentyabrda", "1924-yil 16-sentyabrda", "1924-yil 27-oktyabrda", "29-oktyabrda.")
t.B("SSSR MIQ III sessiyasi O‘rta Osiyoda milliy respublikalar tuzish to‘g‘risida qachon qaror qabul qildi?", "1924-yil 27-oktyabrda", "1924-yil 14-oktyabrda", "1924-yil 31-oktyabrda", "1924-yil 18-noyabrda", "1924-yil 27-oktyabrda Moskvada.")
t.B("Chegaralanish natijasida Turkiston ASSR, Buxoro va Xorazm o‘rnida nechta milliy davlat birlashmasi tashkil etildi?", "oltita", "beshta", "uchta", "to‘rtta", "Oltita milliy davlat birlashmasi.")
t.B("Tojikiston ASSR dastlab qaysi respublika tarkibida tuzilgan?", "O‘zbekiston SSR", "RSFSR", "Qozog‘iston ASSR", "Turkmaniston SSR", "O‘zSSR tarkibida (1929-yilgacha).")
t.B("Qoraqalpoq muxtor viloyati dastlab qaysi respublika tarkibida bo‘lgan?", "Qozog‘iston ASSR", "O‘zbekiston SSR", "Turkmaniston SSR", "Tojikiston ASSR", "Qozog‘iston ASSR tarkibida.")
t.B("O‘zbekiston SSR Muvaqqat inqilobiy komiteti qachon tashkil topdi?", "1924-yil 31-oktyabrda", "1924-yil 18-noyabrda", "1924-yil 27-oktyabrda", "1925-yil 13-fevralda", "1924-yil 31-oktyabrda F.Xo‘jayev raisligida.")
t.B("O‘zbekiston SSR Muvaqqat inqilobiy komitetiga kim raislik qildi?", "Fayzulla Xo‘jayev", "Akmal Ikromov", "Porso Xo‘jayev", "Yo‘ldosh Oxunboboyev", "F.Xo‘jayev raisligida.")
t.NAT("1924-yil 18-noyabrda Turkiston ASSR, Buxoro SSR va Xorazm SSR MIKlari qo‘shma qaror qabul qildi.", "o‘z vakolatlarini O‘zSSR Muvaqqat inqilobiy komitetiga topshirdi", "mustaqil federatsiya tuzdi", "chegaralanishni rad etdi", "RSFSR tarkibiga kirdi", "Vakolatlar O‘zSSR Muvaqqat inqilobiy komitetiga topshirildi.")
t.NAT("Milliy-hududiy chegaralanishda ko‘plab siyosiy xatolarga yo‘l qo‘yildi.", "o‘zbeklar azaldan yashagan hududlarning katta qismi qo‘shni respublikalarga berildi", "barcha o‘zbek yerlari O‘zSSRga kirdi", "Turkiston yaxlitligi saqlandi", "Xorazm chegaralanishdan chetda qoldi", "O‘zbek xalqi manfaatlariga jiddiy zarar yetkazildi.")
t.TF("Chegaralash tarafdorlari xo‘jalikka oid iqtisodiy omillar va umumiy sug‘orish tizimlarini kamroq hisobga oldilar.", True, "To‘g‘ri: ular til va milliy tafovutlarga ko‘proq e’tibor qaratdi.")
t.TF("Sovet hokimiyatining chegaralanish siyosatini dastavval Turkiston ASSR, BXSR va XXSR rahbarlari qo‘llab-quvvatlagan.", False, "Noto‘g‘ri: ular dastavval bu siyosatga qarshi bo‘lgan.")
t.MUL([("1924-yil 15-iyulda tuzilgan O‘zbeklar byurosiga Fayzulla Xo‘jayev va Akmal Ikromov kiritildi.", True),
       ("1924-yil 8-mayda Xorazm rahbarlari Xorazmni chegaralanishga qo‘shmaslikni so‘rab maktub yubordi.", True),
       ("RSFSR MIK II sessiyasi 1924-yil 27-oktyabrda bo‘lib o‘tdi.", False)],
      "III noto‘g‘ri: RSFSR MIK II sessiyasi 14-oktyabrda, SSSR MIQ III sessiyasi 27-oktyabrda bo‘lgan.")
t.MATCH("Shaxslarni ular bilan bog‘liq ma’lumotlar bilan moslashtiring.", ["Ya.Rudzutak", "Qalandar Odinayev", "Sultonbek Xo‘janov", "Turor Risqulov"],
        ["yagona Turkistonni bo‘lib bo‘lmaydi degan milliy kommunistlar yetakchisi", "RKP(b) MK O‘rta Osiyo byurosi raisi", "O‘rta Osiyo federatsiyasini taklif qilgan", "Xorazm Kompartiyasi MK mas’ul kotibi"],
        "bdca", "Rudzutak – O‘rta Osiyo byurosi; Odinayev – Xorazm KP kotibi; Xo‘janov – federatsiya; Risqulov – yagona Turkiston.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["RKP(b) MK Siyosiy byurosining chegaralash to‘g‘risidagi qarori", "Turkiston ASSR MIK favqulodda sessiyasi qarori", "RSFSR MIK II sessiyasi", "SSSR MIQ III sessiyasi", "O‘zSSR Muvaqqat inqilobiy komitetining tuzilishi"],
      "12-iyun → 16-sentyabr → 14-oktyabr → 27-oktyabr → 31-oktyabr (1924).")
t.VENN("O‘zbekiston SSR (1924)", "Qozog‘iston ASSR (1924)",
       [("tarkibida Tojikiston ASSR tuzilgan", 1), ("Muvaqqat inqilobiy komitetiga F.Xo‘jayev raislik qilgan", 1),
        ("RSFSR tarkibida bo‘lgan", 2), ("tarkibida Qoraqalpoq muxtor viloyati bo‘lgan", 2),
        ("milliy-hududiy chegaralanish natijasida vujudga kelgan", 3)],
       "O‘zSSR – Tojikiston ASSR, F.Xo‘jayev revkomi; Qozog‘iston ASSR – RSFSR tarkibida, Qoraqalpoq viloyati; ikkalasi chegaralanish natijasi.")

# 10-§. O‘zbekiston SSRning tashkil topishi
t = Topic('e10u10', 10110); TOPICS['e10u10'] = t
t.B("Butuno‘zbek Sovetlarining I ta’sis qurultoyi qachon va qayerda ochildi?", "1925-yil 13-fevralda Buxoroda", "1925-yil 17-fevralda Samarqandda", "1924-yil 31-oktyabrda Toshkentda", "1925-yil 13-mayda Moskvada", "1925-yil 13-fevralda Buxorodagi Xalq uyida.")
t.B("O‘zSSRni tashkil etish to‘g‘risidagi Deklaratsiya qachon qabul qilindi?", "1925-yil 17-fevralda", "1925-yil 13-fevralda", "1925-yil 13-mayda", "1927-yil 30-martda", "1925-yil 17-fevralda.")
t.B("Ta’sis qurultoyida qatnashib nutq so‘zlagan SSSR MIQ raisi kim?", "Mixail Kalinin", "I.V.Stalin", "Ya.Rudzutak", "V.Ivanov", "Mixail Kalinin.")
t.B("O‘zSSR Xalq Komissarlari Soveti raisi kim bo‘ldi?", "Fayzulla Xo‘jayev", "Yo‘ldosh Oxunboboyev", "Akmal Ikromov", "Vladimir Ivanov", "XKS raisi – Fayzulla Xo‘jayev.")
t.B("O‘zSSR Markaziy Ijroiya Qo‘mitasi raisi kim bo‘ldi?", "Yo‘ldosh Oxunboboyev", "Fayzulla Xo‘jayev", "Porso Xo‘jayev", "Rustam Islomov", "“Qo‘shchi” uyushmasi faoli Yo‘ldosh Oxunboboyev.")
t.B("Tashkil topgan paytda O‘zSSR aholisi qancha bo‘lgan?", "3 963 285 kishi", "8 131 062 kishi", "739 503 kishi", "312 394 kishi", "3 963 285 kishi (Tojikiston ASSR va Qoraqalpoq viloyatisiz).")
t.B("1925-yil apreldan 1930-yil sentyabrgacha O‘zSSR poytaxti qaysi shahar edi?", "Samarqand", "Buxoro", "Toshkent", "Qo‘qon", "Samarqand.")
t.B("O‘zbekiston poytaxti Toshkentga qachon ko‘chirildi?", "1930-yil 20-sentyabrda", "1925-yil aprelda", "1929-yil 16-oktyabrda", "1936-yil 5-dekabrda", "1930-yil 20-sentyabrda.")
t.B("O‘zSSRda ilk ma’muriy-hududiy bo‘linish qachon o‘tkazildi?", "1925-yil 29-yanvarda", "1926-yil 29-sentyabrda", "1925-yil 17-fevralda", "1927-yil 30-martda", "1925-yil 29-yanvarda – 7 viloyat va Konimex tumani.")
t.B("1926-yil 29-sentyabrdagi rayonlashtirishga ko‘ra nechta okrug tuzildi?", "10 ta", "7 ta", "23 ta", "87 ta", "10 ta okrug, 87 tuman, 1720 qishloq sho‘rosi.")
t.B("O‘zbekiston Kommunistik partiyasining I ta’sis syezdi qachon bo‘lib o‘tdi?", "1925-yil 6 – 12-fevralda", "1925-yil 13 – 17-fevralda", "1925-yil 21-martda", "1925-yil aprelda", "1925-yil 6 – 12-fevralda eski Buxoroda.")
t.B("O‘zbekiston Kompartiyasi MK mas’ul sekretarlari qilib kimlar saylandi?", "Vladimir Ivanov va Akmal Ikromov", "Fayzulla Xo‘jayev va Yo‘ldosh Oxunboboyev", "Porso Xo‘jayev va Rustam Islomov", "M.Kalinin va Ya.Rudzutak", "V.Ivanov va A.Ikromov.")
t.B("O‘zSSR SSSR tarkibiga qachon qabul qilindi?", "1925-yil 13-mayda", "1925-yil 17-fevralda", "1922-yil 30-dekabrda", "1927-yil 30-martda", "Butunittifoq Sovetlarining III syezdida 1925-yil 13-mayda.")
t.B("SSSR qachon tashkil topgan?", "1922-yil 30-dekabrda", "1917-yil 25-oktyabrda", "1924-yil 27-oktyabrda", "1925-yil 13-mayda", "1922-yil 30-dekabrda 4 ta respublika asosida.")
t.B("O‘zSSRning birinchi Konstitutsiyasi qachon qabul qilindi?", "1927-yil 30-martda", "1925-yil 17-fevralda", "1926-yil 29-sentyabrda", "1936-yil 5-dekabrda", "1927-yil 30-martda O‘zSSR Sovetlarining II syezdida.")
t.B("O‘zbekiston kasaba uyushmalari I ta’sis syezdi qachon bo‘ldi?", "1925-yil 21-martda", "1925-yil aprelda", "1925-yil 6-fevralda", "1926-yil dekabrda", "1925-yil 21-martda.")
t.B("“Qo‘shchi” ittifoqi qaysi yillarda faoliyat ko‘rsatgan?", "1920 – 1933-yillarda", "1925 – 1936-yillarda", "1917 – 1924-yillarda", "1930 – 1941-yillarda", "1920 – 1933-yillarda; 1925-yilda 200 000 kishini birlashtirgan.")
t.B("Tojikiston ASSR qachon Tojikiston SSRga aylantirilib, O‘zSSR tarkibidan chiqdi?", "1929-yil 16-oktyabrda", "1926-yil 1 – 12-dekabrda", "1936-yil 5-dekabrda", "1930-yil 20-sentyabrda", "1929-yil 16-oktyabrda.")
t.B("Qoraqalpog‘iston ASSR qachon O‘zSSR tarkibiga kiritildi?", "1936-yil 5-dekabrda", "1925-yil 19-fevralda", "1932-yilda", "1929-yil 16-oktyabrda", "1936-yil 5-dekabrda.")
t.NAT("1929-yilda Tojikiston SSR tashkil topdi.", "O‘zSSRning Xo‘jand okrugi Tojikiston SSRga berildi", "Tojikiston O‘zSSR tarkibiga qaytdi", "Qoraqalpog‘iston O‘zSSRga kirdi", "O‘zSSR poytaxti Toshkentga ko‘chdi", "Markaz buyrug‘i bilan Xo‘jand okrugi Tojikistonga berildi.")
t.NAT("Mahalliy hokimiyat organlari mustahkamlanib, markaziy hukumat bilan aloqalari kuchaydi.", "poytaxt Samarqanddan Toshkentga ko‘chirildi", "poytaxt Buxoroga qaytarildi", "O‘zSSR SSSRdan chiqdi", "okruglar tugatildi", "1930-yil 20-sentyabrda poytaxt Toshkentga ko‘chirildi.")
t.TF("O‘zbekiston komsomoliga 1925-yil aprelda Samarqandda asos solindi.", True, "To‘g‘ri.")
t.TF("Qoraqalpog‘iston 1925 – 1936-yillarda doimo O‘zSSR tarkibida bo‘lgan.", False, "Noto‘g‘ri: 1925 – 1932-yillarda Qozog‘iston, 1932 – 1936-yillarda RSFSR tarkibida bo‘lgan.")
t.MUL([("Qoraqalpoq avtonom viloyati Sovetlarining I ta’sis syezdi To‘rtko‘lda bo‘lgan.", True),
       ("Tojikiston ASSR Sovetlarining I ta’sis syezdi Dushanbeda bo‘lgan.", True),
       ("1924-yil oxirida O‘rta Osiyo aholisining uchdan bir qismi O‘zbekistonda yashagan.", False)],
      "III noto‘g‘ri: aholining qariyb yarmisi O‘zbekistonda istiqomat qilgan.")
t.MATCH("Sanalarni voqealar bilan moslashtiring.", ["1925-yil 17-fevral", "1925-yil 13-may", "1927-yil 30-mart", "1930-yil 20-sentyabr"],
        ["poytaxtning Toshkentga ko‘chirilishi", "O‘zSSRning birinchi Konstitutsiyasi", "O‘zSSRning SSSR tarkibiga qabul qilinishi", "O‘zSSRni tashkil etish to‘g‘risidagi Deklaratsiya"],
        "dcba", "17-fevral – Deklaratsiya; 13-may – SSSRga qabul; 30-mart – Konstitutsiya; 20-sentyabr – poytaxt Toshkentga.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["O‘zSSRda ilk ma’muriy-hududiy bo‘linish", "O‘zbekiston Kompartiyasining I ta’sis syezdi", "Butuno‘zbek Sovetlarining I ta’sis qurultoyi ochilishi", "O‘zSSRning SSSR tarkibiga qabul qilinishi", "Rayonlashtirish to‘g‘risidagi qaror"],
      "1925-yil 29-yanvar → 6 – 12-fevral → 13-fevral → 13-may → 1926-yil 29-sentyabr.")
t.MAPMATCH(CA, ['Buxoro', 'Samarqand', 'Toshkent', 'Dushanbe'],
           ["1925-yil fevral – aprelda O‘zSSR poytaxti", "1925 – 1930-yillarda O‘zSSR poytaxti", "1930-yil 20-sentyabrdan O‘zSSR poytaxti", "Tojikiston ASSR Sovetlarining I ta’sis syezdi o‘tkazilgan shahar"],
           "1 – Buxoro; 2 – Samarqand; 3 – Toshkent; 4 – Dushanbe.")
t.VENN("Tojikiston ASSR", "Qoraqalpoq avtonom viloyati",
       [("1926-yil dekabrda Dushanbeda tuzilgan", 1), ("1929-yilda ittifoqdosh respublikaga aylangan", 1),
        ("ta’sis syezdi To‘rtko‘lda bo‘lgan", 2), ("dastlab Qozog‘iston ASSR tarkibida bo‘lgan", 2),
        ("milliy-hududiy chegaralanish natijasida tuzilgan", 3)],
       "Tojikiston ASSR – Dushanbe, 1929-yil SSR; Qoraqalpoq viloyati – To‘rtko‘l, Qozog‘iston ASSR tarkibida; ikkalasi chegaralanish natijasi.")
