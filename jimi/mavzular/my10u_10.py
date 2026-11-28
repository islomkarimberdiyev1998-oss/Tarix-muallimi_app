from qlib import Topic, PLACES, REG
TOPICS = {}

# 20-mavzu. Hududiy chegaralanish
t = Topic('y10u20', 10020); TOPICS['y10u20'] = t
t.B("O‘rta Osiyoni hududiy chegaralash qachon amalga oshirila boshlandi?", "1924-yil boshlaridan", "1920-yildan", "1918-yildan", "1929-yildan", "1924-yil boshlaridan.")
t.B("Turkiy xalqlar yagona, Turkistonni bo‘lib bo‘lmaydi degan g‘oyani kim boshchiligidagi guruh ilgari surgan?", "Turor Risqulov", "Akmal Ikromov", "Y. Rudzutak", "Q. Odinayev", "Turor Risqulov.")
t.B("Markaz kommunistlari Risqulov g‘oyasini qanday deb atagan?", "«panturkizm», «panislomizm»", "«internatsionalizm»", "«leninizm»", "«demokratiya»", "«Panturkizm», «panislomizm», «burjua millatchiligi».")
t.B("1924-yil fevralda Buxoro Kompartiyasi kim yozgan tezislarni qabul qildi?", "Fayzulla Xo‘jayev", "Turor Risqulov", "Sultonbek Xo‘janov", "Qalandar Odinayev", "Fayzulla Xo‘jayev.")
t.B("1920-yil 10-martda O‘rta Osiyo federatsiyasini tuzish taklifi bilan chiqqanlardan biri kim?", "Sultonbek Xo‘janov", "Stalin", "Rudzutak", "Kalugin", "S. Xo‘janov, S. Asfandiyorov, N. Paskutskiy.")
t.B("1923-yil dekabrda Farg‘ona vodiysi vakillari nima taklif qilgan?", "RSFSR tarkibida Farg‘ona muxtor viloyati", "Farg‘ona mustaqilligi", "Farg‘onani Qirg‘izistonga berish", "Farg‘onani Buxoroga qo‘shish", "Farg‘ona muxtor viloyati.")
t.B("Xorazmni chegaralanishga qo‘shmaslikni qo‘llab-quvvatlagan va lavozimidan olingan kim?", "Qalandar Odinayev", "Polvonniyoz Yusupov", "Fayzulla Xo‘jayev", "Akmal Ikromov", "Q. Odinayev, 1924-yil iyul.")
t.B("RKP(b) MK O‘rta Osiyo byurosi milliy respublikalar muvaqqat byurosini qachon tuzgan?", "1924-yil 15-iyulda", "1924-yil 27-oktyabrda", "1924-yil 8-mayda", "1925-yil fevralda", "1924-yil 15-iyul.")
t.B("RKP(b) MK O‘rta Osiyo byurosi raisi kim bo‘lgan?", "Y. Rudzutak", "I. Stalin", "P. Kobozev", "V. Ivanov", "Y. Rudzutak.")
t.B("SSSR MIK III sessiyasi O‘rta Osiyoda milliy respublikalar tuzish haqida qachon qaror qabul qilgan?", "1924-yil 27-oktyabrda", "1924-yil 15-iyulda", "1925-yil 13-fevralda", "1929-yil 16-oktyabrda", "1924-yil 27-oktyabr, Moskva.")
t.B("Chegaralanish natijasida nechta milliy davlat birlashmasi tuzilgan?", "oltita", "uchta", "beshta", "o‘nta", "Oltita.")
t.B("Tojikiston ASSR 1929-yilgacha qaysi respublika tarkibida bo‘lgan?", "O‘zbekiston SSR", "RSFSR", "Turkmaniston SSR", "Qozog‘iston ASSR", "O‘zbekiston SSR.")
t.B("Qoraqalpoq muxtor viloyati dastlab qaysi respublika tarkibida tuzilgan?", "Qozog‘iston ASSR", "O‘zbekiston SSR", "Turkmaniston SSR", "Qirg‘iziston", "Qozog‘iston ASSR tarkibida.")
t.B("Qoraqirg‘iz (Qirg‘iziston) muxtor viloyati qaysi respublika tarkibida tuzilgan?", "RSFSR", "O‘zbekiston SSR", "Qozog‘iston ASSR", "Turkmaniston SSR", "RSFSR tarkibida.")
t.NAT("Markaz milliy masalani sun’iy ravishda bo‘rttirib yubordi.", "bu respublikalar hududini tubdan qayta belgilash uchun asosiy dalil sifatida ilgari surildi", "yagona Turkiston saqlab qolindi", "chegaralanish bekor qilindi", "milliy ixtiloflar yo‘qoldi", "Chegaralanish asoslandi.")
t.NAT("1924-yil 8-mayda Xorazm rahbarlari Xorazmni chegaralanishga qo‘shmaslikni so‘radi.", "Odinayev lavozimidan olinib, XXSR chegaralanishga tortildi", "Xorazm mustaqil qoldi", "iltimos qondirildi", "Xorazm Buxoroga qo‘shildi", "Iltimos rad etildi.")
t.NAT("1924-yil sentyabr–oktyabrda milliy-hududiy chegaralanish o‘tkazildi.", "Turkiston ASSR, Buxoro va Xorazm o‘rnida oltita milliy davlat birlashmasi tuzildi", "Turkiston yagona respublika bo‘ldi", "xonliklar tiklandi", "BXSR kengaydi", "Oltita birlashma.")
t.NAT("Markaz kommunistlari Risqulov g‘oyasini inkor etdi.", "yagona Turkistonni saqlash g‘oyasi «panturkizm» deb qoralandi", "Risqulov g‘oyasi qabul qilindi", "Turkiston federatsiyasi tuzildi", "chegaralanish to‘xtatildi", "G‘oya qoralandi.")
t.TF("Chegaralanish siyosatiga dastavval Turkiston ASSR, BXSR va XXSR rahbarlari qarshi bo‘lgan.", True, "To‘g‘ri.")
t.TF("Qoraqalpog‘iston ASSR 1924-yildan O‘zSSR tarkibida bo‘lgan.", False, "Noto‘g‘ri: 1936-yildan O‘zSSR tarkibiga kirgan.")
t.TF4([("O‘zbeklar byurosi tarkibiga Fayzulla Xo‘jayev va Akmal Ikromov kiritilgan.", True), ("Turkiston va Buxoro Kompartiyalari huzurida maxsus komissiyalar tuzilgan.", True),
       ("S. Xo‘janov Turkiston yaxlitligini buzish maqsadga muvofiq emas deb ta’kidlagan.", True), ("Chegaralanish natijasida Turkmaniston ASSR RSFSR tarkibida tuzilgan.", False)],
      "4-noto‘g‘ri: Turkmaniston SSR tuzilgan.")
t.MUL([("Stalin va Rudzutak O‘rta Osiyoda milliy mojarolar borligini ta’kidlagan.", True),
       ("Xorazm rahbarlari respublikaning olisligi va iqtisodiy alohidaligini dalil qilgan.", True),
       ("Chegaralanish masalasi 1930-yilda boshlangan.", False)],
      "III noto‘g‘ri: 1924-yil boshlaridan amalga oshirila boshlangan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Turkiston MIK kengashida federatsiya taklifi", "Farg‘ona muxtor viloyati taklifi", "Xorazm rahbarlarining maktubi", "muvaqqat byuro tuzildi", "SSSR MIK III sessiyasi qarori"],
      "1920-03-10 → 1923-12 → 1924-05-08 → 1924-07-15 → 1924-10-27.")
t.MATCH("Yangi birlashmalarni tarkibi bilan moslashtiring.", ["O‘zbekiston SSR", "Tojikiston ASSR", "Qozog‘iston ASSR", "Qoraqalpoq muxtor viloyati"],
        ["mustaqil ittifoqdosh respublika", "1929-yilgacha O‘zSSR tarkibida", "RSFSR tarkibida", "Qozog‘iston ASSR tarkibida", "Turkmaniston tarkibida"], 'abcd',
        "O‘zSSR – ittifoqdosh; Tojik ASSR – O‘zSSR; Qozoq ASSR – RSFSR; Qoraqalpoq – Qozog‘iston ASSR.")
t.VENN("Chegaralanish tarafdorlari", "Chegaralanish muxoliflari",
       [("Stalin va Rudzutak", 1), ("milliy mojarolar bor deb ta’kidlagan", 1),
        ("Turor Risqulov guruhi", 2), ("yagona Turkiston g‘oyasi", 2),
        ("1920-yillarda milliy masala bo‘yicha fikr bildirgan", 3)],
       "Tarafdorlar – Stalin, Rudzutak; muxoliflar – Risqulov, yagona Turkiston; ikkalasi munozara ishtirokchisi.")
t.MAPMATCH('uzb', ['Buxoro', 'Xiva', 'Toshkent', 'Farg‘ona vodiysi'],
           ["1924-yil fevralda Kompartiyasi Xo‘jayev tezislarini qabul qilgan respublika markazi", "chegaralanishga qo‘shilmaslikni so‘ragan respublika markazi", "Turkiston ASSR poytaxti", "1923-yilda muxtor viloyat tuzish taklif qilingan hudud"],
           "1 – Buxoro; 2 – Xiva; 3 – Toshkent; 4 – Farg‘ona vodiysi.")

# 21-mavzu. O‘zbekiston SSRning tashkil topishi
t = Topic('y10u21', 10021); TOPICS['y10u21'] = t
t.B("Butuno‘zbek Sovetlarining I ta’sis qurultoyi qachon bo‘lgan?", "1925-yil 13–17-fevralda", "1924-yil 27-oktyabrda", "1925-yil 6–12-fevralda", "1927-yil 30-martda", "1925-yil 13–17-fevral.")
t.B("I ta’sis qurultoyi qayerda bo‘lgan?", "Buxoroda", "Toshkentda", "Samarqandda", "Moskvada", "Buxoroda.")
t.B("O‘zbekiston SSR Xalq Komissarlari Soveti raisi kim bo‘lgan?", "Fayzulla Xo‘jayev", "Yo‘ldosh Oxunboboyev", "Akmal Ikromov", "Vladimir Ivanov", "Fayzulla Xo‘jayev.")
t.B("O‘zbekiston SSR Markaziy Ijroiya Qo‘mitasi raisi kim bo‘lgan?", "Yo‘ldosh Oxunboboyev", "Fayzulla Xo‘jayev", "Akmal Ikromov", "Turor Risqulov", "Yo‘ldosh Oxunboboyev.")
t.B("Dastlab O‘zbekiston SSR poytaxti qaysi shahar bo‘lgan?", "Samarqand", "Toshkent", "Buxoro", "Qo‘qon", "Samarqand.")
t.B("Poytaxt Toshkentga qachon ko‘chirilgan?", "1930-yil 20-sentyabrda", "1925-yil 17-fevralda", "1936-yil 5-dekabrda", "1929-yil 16-oktyabrda", "1930-yil 20-sentyabr.")
t.B("1925-yil 29-yanvardagi ma’muriy bo‘linishda nechta viloyat tuzilgan?", "7 ta", "10 ta", "12 ta", "5 ta", "7 viloyat va Konimex tumani.")
t.B("1926-yil 29-sentyabrda nechta okrug tuzilgan?", "10 ta", "7 ta", "14 ta", "6 ta", "10 ta okrug.")
t.B("O‘zbekiston Kompartiyasining I ta’sis syezdi qachon bo‘lgan?", "1925-yil 6–12-fevralda", "1925-yil 13–17-fevralda", "1924-yil iyulda", "1927-yil martda", "1925-yil 6–12-fevral, eski Buxoro.")
t.B("O‘zbekiston Kompartiyasi MK mas’ul sekretarlari kimlar?", "Vladimir Ivanov va Akmal Ikromov", "Xo‘jayev va Oxunboboyev", "Risqulov va Xo‘janov", "Rudzutak va Stalin", "V. Ivanov va A. Ikromov.")
t.B("O‘zSSRning birinchi Konstitutsiyasi qachon qabul qilingan?", "1927-yil 30-martda", "1925-yil 17-fevralda", "1936-yilda", "1930-yilda", "1927-yil 30-mart.")
t.B("O‘zbekiston kasaba uyushmalariga qachon asos solingan?", "1925-yil 21-martda", "1927-yil 30-martda", "1920-yilda", "1933-yilda", "1925-yil 21-mart.")
t.B("«Qo‘shchi» ittifoqi qaysi yillarda faoliyat ko‘rsatgan?", "1920–1933", "1925–1941", "1918–1924", "1930–1950", "1920–1933.")
t.B("1925-yilda «Qo‘shchi» ittifoqi necha kishini birlashtirgan?", "200 000", "20 000", "2 million", "50 000", "200 000 kishi.")
t.B("Tojikiston SSR qachon tashkil topib, O‘zSSR tarkibidan chiqdi?", "1929-yil 16-oktyabrda", "1924-yil oktyabrda", "1936-yil 5-dekabrda", "1930-yilda", "1929-yil 16-oktyabr.")
t.B("Qoraqalpog‘iston ASSR qachon O‘zbekiston SSR tarkibiga kiritilgan?", "1936-yil 5-dekabrda", "1932-yilda", "1925-yilda", "1929-yilda", "1936-yil 5-dekabr.")
t.NAT("Samarqand respublikaning markazida joylashgan edi.", "bu O‘zSSR hududining barcha qismlarida sovet tashkilotlari ishini jonlantirishga yordam berdi", "poytaxt darhol ko‘chirildi", "boshqaruv qiyinlashdi", "viloyatlar ajralib chiqdi", "Sovet tashkilotlari ishi jonlandi.")
t.NAT("Mahalliy hokimiyat organlari mustahkamlanib, markaz bilan aloqalar kuchaydi.", "poytaxt 1930-yilda eng muhim markaz – Toshkentga ko‘chirildi", "poytaxt Buxoroga ko‘chirildi", "Samarqand poytaxt bo‘lib qoldi", "respublika tarqatildi", "Poytaxt Toshkentga ko‘chdi.")
t.NAT("O‘zbekiston partiya tashkiloti Moskvada ishlab chiqilgan qarorlarni bajardi.", "respublika va o‘zbek xalqi manfaatlari hisobga olinmadi", "xalq manfaatlari to‘liq himoya qilindi", "respublika mustaqil siyosat yuritdi", "partiya tarqatildi", "Manfaatlar e’tiborsiz qoldi.")
t.NAT("Kasaba uyushmalari partiya komitetlariga to‘la qaram bo‘lib qoldi.", "Uzsovprof Butunittifoq kasaba uyushmalari markaziy soveti rahbarligida ishladi", "kasaba uyushmalari mustaqil bo‘ldi", "kasaba uyushmalari tarqatildi", "ular xorijga bo‘ysundi", "VSSPS rahbarligi.")
t.TF("1925-yilda O‘zbekiston leninchi kommunistik yoshlar ittifoqi (O‘zLKSM) tashkil etilgan.", True, "To‘g‘ri.")
t.TF("Qoraqalpog‘iston 1925–1932-yillarda O‘zSSR tarkibida bo‘lgan.", False, "Noto‘g‘ri: Qozog‘iston tarkibida, 1932–1936-yillarda RSFSR tarkibida bo‘lgan.")
t.TF4([("Deklaratsiyada O‘zSSR tarkibiga Tojikiston ASSR kirganligi ta’kidlangan.", True), ("1925-yilgi bo‘linishda alohida Konimex tumani tashkil etilgan.", True),
       ("O‘zSSR Kompartiyasi respublika siyosiy hayotida asosiy rol o‘ynagan.", True), ("Ta’sis qurultoyida «Qo‘shchi» uyushmasi tarqatilgan.", False)],
      "4-noto‘g‘ri: «Qo‘shchi» faoli Oxunboboyev MIK raisi bo‘ldi, ittifoq 1933-yilgacha ishladi.")
t.MUL([("Fayzulla Xo‘jayev poytaxtni bir kechada Samarqanddan Toshkentga ko‘chirgan.", True),
       ("1926-yilda 10 ta okrug va Konimex tumani tuzilgan.", True),
       ("O‘zSSR birinchi Konstitutsiyasi 1936-yilda qabul qilingan.", False)],
      "III noto‘g‘ri: 1927-yil 30-martda qabul qilingan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["ilk ma’muriy-hududiy bo‘linish (7 viloyat)", "Kompartiya I ta’sis syezdi", "Sovetlar I ta’sis qurultoyi", "birinchi Konstitutsiya", "Tojikiston SSR tuzildi", "poytaxt Toshkentga ko‘chdi"],
      "1925-01-29 → 1925-02-06 → 1925-02-13 → 1927-03-30 → 1929-10-16 → 1930-09-20.")
t.MATCH("Shaxslarni lavozimi bilan moslashtiring.", ["Fayzulla Xo‘jayev", "Yo‘ldosh Oxunboboyev", "Akmal Ikromov", "Vladimir Ivanov"],
        ["Xalq Komissarlari Soveti raisi", "Markaziy Ijroiya Qo‘mitasi raisi", "Kompartiya MK mas’ul sekretari (o‘zbek)", "Kompartiya MK mas’ul sekretari (Ivanov)", "Turkiston byurosi raisi"], 'abcd',
        "Xo‘jayev – XKS; Oxunboboyev – MIK; Ikromov – MK; Ivanov – MK.")
t.VENN("Samarqand", "Toshkent",
       [("1925–1930-yillarda poytaxt", 1), ("respublikaning markazida joylashgan", 1),
        ("1930-yil 20-sentyabrdan poytaxt", 2), ("eng muhim iqtisodiy-madaniy markaz", 2),
        ("O‘zSSR poytaxti bo‘lgan shahar", 3)],
       "Samarqand – 1925–1930; Toshkent – 1930-yildan; ikkalasi poytaxt bo‘lgan.")
t.MAPMATCH('uzb', ['Buxoro', 'Samarqand', 'Toshkent', 'Nukus'],
           ["1925-yil fevralda ta’sis qurultoyi va partiya syezdi o‘tgan shahar", "O‘zSSRning dastlabki poytaxti", "1930-yildan O‘zSSR poytaxti", "1936-yilda O‘zSSR tarkibiga kirgan Qoraqalpog‘iston markazi"],
           "1 – Buxoro; 2 – Samarqand; 3 – Toshkent; 4 – Nukus.")
