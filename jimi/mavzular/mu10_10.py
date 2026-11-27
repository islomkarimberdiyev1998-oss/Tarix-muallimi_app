from qlib import Topic
TOPICS = {}

# 19 Fan va madaniyat g'alaba uchun xizmatda
t = Topic('e10u19', 10019); TOPICS['e10u19'] = t
t.B("Urush yillarida O‘zbekiston san’at ustalari nechta konsert brigadasiga bo‘lingan?", "30 ta", "35 ta", "26 ta", "7 ta", "30 ta konsert brigadasiga.")
t.B("San’atkorlar frontdagi jangchilarga qancha konsert ko‘rsatgan?", "35 000 ta", "26 000 ta", "30 000 ta", "3500 ta", "Frontda 35 000, gospitallarda 26 000 ta.")
t.B("San’atkorlar gospitallarda qancha konsert ko‘rsatgan?", "26 000 ta", "35 000 ta", "375 ta", "2600 ta", "26 000 ta.")
t.B("«Muqanna» dramasining muallifi kim?", "Hamid Olimjon", "Oybek", "Maqsud Shayxzoda", "Uyg‘un", "Hamid Olimjon.")
t.B("«Mahmud Torobiy» asarining muallifi kim?", "Oybek", "Hamid Olimjon", "Abdulla Qahhor", "G‘afur G‘ulom", "Oybek.")
t.B("«Jaloliddin Manguberdi» dramasini kim yozgan?", "Maqsud Shayxzoda", "Oybek", "Uyg‘un", "Izzat Sulton", "Maqsud Shayxzoda.")
t.B("«Alisher Navoiy» dramasining mualliflari kimlar?", "Uyg‘un va Izzat Sulton", "Hamid Olimjon va Oybek", "G‘afur G‘ulom va Shayxzoda", "Sobir Abdulla va Uyg‘un", "Uyg‘un va Izzat Sulton.")
t.B("O‘zbekiston SSR Fanlar akademiyasi qachon tashkil topgan?", "1943-yil 4-noyabrda", "1940-yil 9-yanvarda", "1943-yil sentyabrda", "1945-yil 9-mayda", "1943-yil 4-noyabrda Toshkentda.")
t.B("O‘zSSR FAning birinchi prezidenti kim bo‘lgan?", "Toshmuhammad Qori-Niyoziy", "Otajon Hoshimov", "Usmon Yusupov", "Oybek", "Matematik olim T.N. Qori-Niyoziy.")
t.B("Til, adabiyot va tarix instituti qaysi institutlarga ajratilgan?", "O‘zbek tili va adabiyoti hamda Tarix va arxeologiya institutlariga", "Matematika va Fizika institutlariga", "Sharqshunoslik va Falsafa institutlariga", "Pedagogika va Psixologiya institutlariga", "O‘zbek tili va adabiyoti hamda Tarix va arxeologiya institutlariga.")
t.B("Toshkentga mamlakatning nechta taniqli ilmiy xodimi kelgan?", "375 nafar", "200 nafar", "31 nafar", "1000 nafar", "375 nafar.")
t.B("O‘zbekistonga nechta oliy o‘quv yurti evakuatsiya qilingan?", "31 ta", "7 ta", "375 ta", "100 ta", "31 ta oliy o‘quv yurti va 7 ta harbiy akademiya.")
t.B("O‘zbekistonga nechta harbiy akademiya evakuatsiya qilingan?", "7 ta", "31 ta", "3 ta", "12 ta", "7 ta.")
t.B("Fashistlar bosib olgan hududlardan qancha yozuvchi va shoir O‘zbekistonga kelgan?", "200 nafardan ortiq", "375 nafar", "31 nafar", "1000 nafardan ortiq", "200 nafardan ortiq.")
t.B("O‘zbek va ko‘chib kelgan shoirlar hamkorlikda yaratgan almanax qanday nomlangan?", "«Biz g‘alaba qozonamiz»", "«O‘zbekiston qilichi»", "«Xotira»", "«Motamsaro ona»", "«Biz g‘alaba qozonamiz».")
t.NAT("SSSR XKS raisi Stalinning 1943-yil sentyabrdagi qarori chiqdi.", "O‘zFAN negizida O‘zSSR Fanlar akademiyasi tashkil topdi", "O‘zFAN yopildi", "olimlar Moskvaga qaytarildi", "universitet yopildi", "1943-yil 4-noyabrda O‘zSSR FA tuzildi.")
t.NAT("31 ta oliy o‘quv yurti va ko‘plab ilmiy institutlar O‘zbekistonga ko‘chirildi.", "O‘zbekiston oliy o‘quv yurtlari faoliyati Markaz darajasiga yaqinlashdi", "mahalliy oliy o‘quv yurtlari yopildi", "ilmiy ishlar to‘xtadi", "talabalar soni kamaydi", "Markaz darajasiga yaqinlashish imkoni tug‘ildi.")
t.TF("Urush yillarida teatrlar repertuarida harbiy va tarixiy asarlar ustun bo‘lgan.", True, "To‘g‘ri.")
t.TF("O‘zSSR Fanlar akademiyasi urush tugagach, 1946-yilda tashkil topgan.", False, "Noto‘g‘ri: 1943-yil 4-noyabrda, urushning qizg‘in pallasida.")
t.MUL([("Anna Axmatova va Aleksey Tolstoy urush yillarida O‘zbekistonda bo‘lgan.", True),
       ("Yakub Kolas va Yanka Kupala ham O‘zbekistonga kelgan.", True),
       ("«O‘zbekiston shoirlari frontga» antologiyasi urushdan keyin Moskvada yaratilgan.", False)],
      "III noto‘g‘ri: u urush yillarida o‘zbek va ko‘chib kelgan shoirlar hamkorligida yaratilgan.")
t.MATCH("Asarlarni mualliflari bilan moslashtiring.", ["«Muqanna»", "«Mahmud Torobiy»", "«Jaloliddin Manguberdi»", "«Alisher Navoiy»"],
        ["Hamid Olimjon", "Oybek", "Maqsud Shayxzoda", "Uyg‘un va Izzat Sulton", "Abdulla Qahhor"], 'abcd',
        "«Muqanna» – Hamid Olimjon; «Mahmud Torobiy» – Oybek; «Jaloliddin Manguberdi» – Shayxzoda; «Alisher Navoiy» – Uyg‘un va Izzat Sulton.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["O‘zSSR Fanlar komiteti tuzildi", "O‘zFAN tashkil topdi", "Stalinning Fanlar akademiyasi to‘g‘risidagi qarori", "O‘zSSR Fanlar akademiyasi tashkil topdi"],
      "1932 → 1940-yil yanvar → 1943-yil sentyabr → 1943-yil 4-noyabr.")
t.MAPN('europe', ['Leningrad', 'Moskva', 'Kiyev', 'Minsk'],
       "Urush yillarida O‘zbekistonga oliy o‘quv yurtlari evakuatsiya qilingan Belorusiya poytaxti qaysi raqam bilan belgilangan?",
       "Minsk – Belorusiya poytaxti.", 3)
t.VENN("O‘zbek yozuvchilari", "Ko‘chib kelgan yozuvchilar",
       [("Hamid Olimjon", 1), ("Maqsud Shayxzoda", 1),
        ("Anna Axmatova", 2), ("Yakub Kolas", 2),
        ("«Biz g‘alaba qozonamiz» almanaxini yaratishda qatnashgan", 3)],
       "O‘zbek — Hamid Olimjon, Shayxzoda; ko‘chib kelgan — Axmatova, Kolas.")

# 20 Urushdan keyingi xalq xo'jaligi
t = Topic('e10u20', 10020); TOPICS['e10u20'] = t
t.B("Markazning rejalarida O‘zbekistonga qanday qaralgan?", "xomashyo yetkazib beruvchi chekka o‘lka", "sanoat markazi", "harbiy baza", "savdo markazi", "Faqat xomashyo yetkazib beruvchi chekka o‘lka.")
t.B("1945-yil oxirida mashinasozlik sanoati nimaga o‘tkazildi?", "qishloq xo‘jaligi va irrigatsiya uchun mashina ishlab chiqarishga", "tank ishlab chiqarishga", "samolyot ishlab chiqarishga", "avtomobil ishlab chiqarishga", "Qishloq xo‘jaligi va irrigatsiya ehtiyojlari uchun.")
t.B("O‘zbekiston metallurgiya zavodida yangi prokat sexi qachon ishga tushirilgan?", "1946-yili", "1944-yili", "1948-yili", "1956-yili", "1946-yili.")
t.B("Urushdan keyingi yillarda qaysi neft konlari ochilgan?", "Polvontosh va Janubiy Olamushuk", "Muborak va Sho‘rtan", "Gazli va Qorovulbozor", "Ko‘kdumaloq va Shimoliy So‘x", "Polvontosh va Janubiy Olamushuk.")
t.B("Neftni qayta ishlash zavodi qaysi shaharda foydalanishga topshirilgan?", "Farg‘onada", "Toshkentda", "Buxoroda", "Bekobodda", "Farg‘onada.")
t.B("Paxtachilikni tiklash rejasi to‘g‘risidagi SSSR hukumati qarori qachon qabul qilingan?", "1946-yil 5-fevralda", "1956-yil 6-avgustda", "1947-yil dekabrda", "1948-yilda", "1946-yil 5-fevralda.")
t.B("1946-yili O‘zSSR uchun paxta ekin maydoni qancha qilib belgilangan?", "779 000 gektar", "218 000 gektar", "200 000 gektar", "160 000 gektar", "779 000 gektar.")
t.B("1946-yili qancha sug‘oriladigan maydon faqat paxta ekish uchun bo‘shatilgan?", "218 000 gektar", "779 000 gektar", "100 000 gektar", "160 000 gektar", "218 000 gektar.")
t.B("Paxta terish mashinalarining dastlabki partiyasini qaysi zavod ishlab chiqargan?", "«Tashselmash»", "«Tashavtomash»", "TTZ", "Chirchiq kombinati", "1948-yili «Tashselmash».")
t.B("«Tashavtomash» zavodi bazasida 1969-yili qaysi zavod barpo etilgan?", "Toshkent traktor zavodi (TTZ)", "«Tashselmash»", "Toshkent aviatsiya zavodi", "Farg‘ona neft zavodi", "Toshkent traktor zavodi (TTZ).")
t.B("Kartochka tizimi qachon bekor qilingan?", "1947-yil dekabrda", "1945-yil mayda", "1946-yil fevralda", "1950-yilda", "1947-yil dekabrda.")
t.B("1945-yili O‘zbekistonda qancha paxta yetishtirilgan?", "850 000 tonna", "2 222 000 tonna", "1,6 mln tonna", "4 mln tonna", "850 000 tonna; 1950-yili 2 222 000 tonna.")
t.B("Mirzacho‘lning qo‘riq yerlarini sug‘orish to‘g‘risidagi qaror qachon qabul qilingan?", "1956-yil 6-avgustda", "1946-yil 5-fevralda", "1961-yilda", "1955-yilda", "1956-yil 6-avgustda.")
t.B("Mirzacho‘lni o‘zlashtirishga rahbarlik qilgan maxsus tashkilot qanday nomlangan?", "«Glavgolodnostepstroy»", "«Tashselmash»", "MTS", "«Qo‘shchi»", "«Glavgolodnostepstroy».")
t.B("1955–1959-yillarda O‘zbekistonda qancha yangi yer o‘zlashtirilgan?", "160 000 gektardan ziyod", "779 000 gektar", "218 000 gektar", "1 mln gektar", "160 000 gektardan ziyod.")
t.B("Mirzacho‘l shaharchasi qachon Guliston shahriga aylantirilgan?", "1961-yil", "1956-yil", "1969-yil", "1959-yil", "1961-yil.")
t.B("1956-yili MTSlarga to‘lanadigan natura haqi stavkalari necha foizga kamaytirilgan?", "40 %", "20 %", "50 %", "10 %", "40 %.")
t.NAT("Sovet hukumati ko‘rsatmasi bilan oziq-ovqat ekinlari maydonlari chigit ekish uchun ajratildi.", "oziq-ovqat muammosi o‘tkirlashdi, ekologiya buzildi", "oziq-ovqat mo‘l bo‘ldi", "paxta ekish kamaydi", "aholi salomatligi yaxshilandi", "Oziq-ovqat muammosi o‘tkirlashdi.")
t.NAT("Sovet hokimiyati hunarmandlarning erkin faoliyatini chekladi.", "yakka tartibda hunarmandchilik bilan shug‘ullanish man etildi", "hunarmandchilik gullab-yashnadi", "artellar tarqatildi", "hunarmandlar soliqdan ozod bo‘ldi", "Yakka hunarmandchilik man etildi.")
t.TF("Mirzacho‘l qarorida O‘zbekistonda paxta maydonlarini 200 000 gektar kengaytirish rejalashtirilgan.", True, "To‘g‘ri; Qozog‘istonda 100 000 gektar.")
t.TF("1946-yildagi qarordan keyin paxtaning xarid narxi keskin oshirilgan.", False, "Noto‘g‘ri: xarid narxi oshirilmagan.")
t.MUL([("1956-yili suv uchun to‘lanadigan haq bekor qilingan.", True),
       ("1956-yili mineral o‘g‘itlar narxi pasaytirilgan.", True),
       ("Barcha texnikaning MTS qo‘lida to‘planishi ijobiy natija bergan.", False)],
      "III noto‘g‘ri: bu salbiy oqibatlarga olib kelgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Paxtachilikni tiklash rejasi to‘g‘risida qaror", "Kartochka tizimi bekor qilindi", "«Tashselmash» paxta terish mashinalarini chiqardi", "Mirzacho‘lni sug‘orish to‘g‘risida qaror", "Guliston shahri tashkil topdi", "TTZ barpo etildi"],
      "1946 → 1947 → 1948 → 1956 → 1961 → 1969.")
t.MAPMATCH('uzb', ['Farg‘ona', 'Bekobod', 'Guliston', 'Toshkent'],
           ["urushdan keyin neftni qayta ishlash zavodi foydalanishga topshirilgan shahar", "1946-yili metallurgiya zavodida prokat sexi ishga tushgan shahar", "1961-yilda Mirzacho‘l shaharchasidan shaharga aylantirilgan", "«Tashselmash» va TTZ joylashgan shahar"],
           "1 – Farg‘ona; 2 – Bekobod; 3 – Guliston; 4 – Toshkent.")
t.VENN("1946-yilgi paxta qarori", "1956-yilgi Mirzacho‘l qarori",
       [("paxta ekin maydoni 779 000 gektar qilib belgilangan", 1), ("paxta xarid narxi oshirilmagan", 1),
        ("qo‘riq yerlarni sug‘orish ko‘zda tutilgan", 2), ("Qozog‘iston SSR yerlari ham kiritilgan", 2),
        ("paxta yetishtirishni ko‘paytirishga qaratilgan", 3)],
       "1946 — 779 000 ga, narx oshirilmagan; 1956 — qo‘riq yerlar, Qozog‘iston ham.")
