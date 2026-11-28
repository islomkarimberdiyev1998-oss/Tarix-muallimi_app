from qlib import Topic, PLACES, REG
TOPICS = {}

# 14-mavzu. Ma’naviy va tarixiy merosga munosabat
t = Topic('y11u14', 11014); TOPICS['y11u14'] = t
t.B("Respublika Ma’naviyat va ma’rifat jamoatchilik markazi qachon tashkil etilgan?", "1994-yilda", "2006-yilda", "2017-yilda", "1991-yilda", "1994-yilda.")
t.B("Respublika Ma’naviyat va ma’rifat markazi muassisligida qaysi jurnallar chop etiladi?", "«Tafakkur» va «Ma’naviy hayot»", "«Yagona oilada» va «Ziyo»", "«Jadid» va «Vaqf»", "«Kamolot» va «Kamalak»", "«Tafakkur», «Ma’naviy hayot».")
t.B("Markaz qaysi g‘oya asosida faoliyat yuritmoqda?", "«Milliy tiklanishdan milliy yuksalish sari»", "«Jaholatga qarshi – ma’rifat»", "«Biz – buyuk yurt farzandlarimiz»", "«Inson qadri uchun»", "«Milliy tiklanishdan milliy yuksalish sari».")
t.B("«Ma’rifat markazi» qachon bunyod etilgan?", "2011-yilda", "1994-yilda", "2017-yilda", "2021-yilda", "2011-yil, Toshkent.")
t.B("«Ma’rifat karvoni» tadbirlari doirasida yoshlarga nechtadan ortiq kitob yetkazilgan?", "3 milliondan", "300 mingdan", "30 milliondan", "3 mingdan", "3 milliondan ortiq.")
t.B("1991-yilda Alisher Navoiy tavalludining necha yilligi nishonlangan?", "550 yilligi", "600 yilligi", "660 yilligi", "500 yilligi", "550 yilligi.")
t.B("«Mirzo Ulug‘bek yili» qachon e’lon qilingan?", "1994-yilda", "1996-yilda", "1991-yilda", "1999-yilda", "1994-yil, 600 yillik.")
t.B("1996-yilda Amir Temur tavalludining necha yilligi nishonlangan?", "660 yilligi", "600 yilligi", "550 yilligi", "675 yilligi", "660 yilligi.")
t.B("Toshkentda Amir Temur haykali qachon o‘rnatilgan?", "1993-yilda", "1996-yilda", "1991-yilda", "2014-yilda", "1993-yilda.")
t.B("2014-yilda qaysi shahar «Amir Temur» ordeni bilan mukofotlangan?", "Termiz", "Samarqand", "Shahrisabz", "Buxoro", "Termiz (1996 – Samarqand va Shahrisabz).")
t.B("Qatag‘on qurbonlarini yod etish kuni qaysi sana?", "31-avgust", "9-may", "2-sentyabr", "1-sentyabr", "31-avgust.")
t.B("Abdulla Qodiriy va Abdulhamid Cho‘lpon qaysi orden bilan taqdirlangan?", "«Mustaqillik»", "«Buyuk xizmatlari uchun»", "«Amir Temur»", "«Do‘stlik»", "«Mustaqillik» ordeni.")
t.B("2020-yilda «Buyuk xizmatlari uchun» ordeni bilan taqdirlanmagan jadid kim?", "Abdulla Qodiriy", "Abdulla Avloniy", "Mahmudxo‘ja Behbudiy", "Munavvar qori Abdurashidxonov", "Qodiriy «Mustaqillik» ordeni bilan taqdirlangan.")
t.B("2025-yilda Mahmudxo‘ja Behbudiy tavalludining necha yilligi nishonlangan?", "150 yilligi", "100 yilligi", "175 yilligi", "200 yilligi", "150 yilligi.")
t.B("Islom Karimov xotirasi kuni qaysi sana?", "2-sentyabr", "31-avgust", "30-iyun", "9-may", "2-sentyabr.")
t.B("2017-yilda qaysi davlat arbobining 100 yilligi nishonlangan?", "Sharof Rashidov", "Islom Karimov", "Abdulla Oripov", "Usmon Nosir", "Sharof Rashidov.")
t.B("«Yangi O‘zbekiston» bog‘i qachon barpo etilgan?", "2021-yilda", "2020-yilda", "2011-yilda", "2017-yilda", "2021-yil, Toshkent.")
t.NAT("1991-yilda Alisher Navoiy tavalludining 550 yilligi nishonlandi.", "Navoiy nomidagi davlat mukofoti ta’sis etildi, Milliy bog‘ uning nomi bilan ataldi", "Navoiy asarlari taqiqlandi", "haykallar olib tashlandi", "universitet nomi o‘zgartirildi", "Mukofot ta’sis etildi.")
t.NAT("Mustaqillik yillarida jadidlarning nomi va merosi qayta tiklandi.", "Toshkentda «Shahidlar xotirasi» majmuasi va «Qatag‘on qurbonlari xotirasi» muzeyi tashkil qilindi", "jadidlar asarlari yo‘q qilindi", "qatag‘on davom ettirildi", "jadidlar unutildi", "Xotira majmuasi.")
t.NAT("2020-yil 9-mayda Xotira va qadrlash kuni nishonlandi.", "Toshkentda «G‘alaba bog‘i» majmuasi va «Shon-sharaf» muzeyi ochildi", "9-may bayrami bekor qilindi", "Xotira maydonlari yopildi", "«Yangi O‘zbekiston» bog‘i ochildi", "G‘alaba bog‘i.")
t.NAT("Birinchi Prezident xotirasini abadiylashtirish tashabbusi ilgari surildi.", "Toshkent xalqaro aeroporti va TDTUga Islom Karimov nomi berildi", "aeroport yopildi", "Karimov nomi olib tashlandi", "faqat chet elda haykal o‘rnatildi", "Nom berildi.")
t.TF("2006-yildan Milliy g‘oya va mafkura ilmiy-amaliy markazi alohida tashkilot sifatida ish boshlagan.", True, "To‘g‘ri.")
t.TF("Islom Karimov haykallari faqat O‘zbekistonda o‘rnatilgan.", False, "Noto‘g‘ri: Moskva va Turkmanobodda ham ochilgan.")
t.TF4([("«Temur tuzuklari» bir necha tilda chop etildi.", True), ("Xotira maydonlari Toshkent, Nukus va viloyat markazlarida barpo etildi.", True),
       ("2024-yildan «Jadid» gazetasi nashr etilmoqda.", True), ("Ulug‘bekning 600 yilligi faqat O‘zbekistonda nishonlangan.", False)],
      "4-noto‘g‘ri: YUNESKO qarorgohida ham nishonlangan.")
t.MUL([("Jizzax tumaniga Sharof Rashidov nomi berildi.", True),
       ("2018-yilda Islom Karimovning 80 yillik tavallud sanasi nishonlandi.", True),
       ("Ma’rifat markazi tarkibiga Temuriylar tarixi davlat muzeyi kiradi.", False)],
      "III noto‘g‘ri: Xalqaro anjumanlar saroyi va Navoiy nomidagi Milliy kutubxona kiradi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Navoiyning 550 yilligi", "Toshkentda Amir Temur haykali", "«Mirzo Ulug‘bek yili»", "Amir Temurning 660 yilligi", "«Ma’rifat markazi» bunyod etildi", "Termiz «Amir Temur» ordeni bilan mukofotlandi"],
      "1991 → 1993 → 1994 → 1996 → 2011 → 2014.")
t.MATCH("Sanalarni voqealar bilan moslashtiring.", ["31-avgust", "2-sentyabr", "9-may", "30-iyun"],
        ["Qatag‘on qurbonlarini yod etish kuni", "Islom Karimov xotirasi kuni", "Xotira va qadrlash kuni", "Yoshlar kuni", "Navro‘z"], 'abcd',
        "31-avgust – qatag‘on; 2-sentyabr – I. Karimov; 9-may – xotira; 30-iyun – yoshlar.")
t.VENN("1991–2016-yillar", "2017-yildan keyin",
       [("Navoiyning 550 yilligi", 1), ("«Mirzo Ulug‘bek yili»", 1),
        ("jadidlarga «Buyuk xizmatlari uchun» ordeni", 2), ("«Yangi O‘zbekiston» bog‘i", 2),
        ("buyuk ajdodlar xotirasini tiklash", 3)],
       "Navoiy, Ulug‘bek – 1991, 1994; jadidlarga orden 2020, bog‘ 2021; ikkalasi – xotira tiklanishi.")
t.MAPMATCH('uzb', ['Jizzax', 'Shahrisabz', 'Termiz', 'Qarshi'],
           ["Sharof Rashidov haykali va muzeyi barpo etilgan shahar", "1996-yilda Amir Temur haykali o‘rnatilgan, Temur tug‘ilgan shahar", "2014-yilda «Amir Temur» ordeni bilan mukofotlangan shahar", "Islom Karimov haykali o‘rnatilgan, Qashqadaryo viloyati markazi"],
           "1 – Jizzax; 2 – Shahrisabz; 3 – Termiz; 4 – Qarshi.")

# 15-mavzu. Milliy va diniy qadriyatlarning qayta tiklanishi
t = Topic('y11u15', 11015); TOPICS['y11u15'] = t
t.B("«Navro‘z» so‘zi qanday ma’noni bildiradi?", "yangi kun", "bahor bayrami", "yangi yil", "uyg‘onish", "«Yangi kun».")
t.B("Manbalarga ko‘ra Navro‘z bayrami necha yildan ortiq tarixga ega?", "3 ming yildan", "1 ming yildan", "500 yildan", "10 ming yildan", "3 ming yildan ortiq.")
t.B("Navro‘zni dunyoda nechtadan ortiq inson nishonlaydi?", "300 milliondan", "30 milliondan", "3 milliarddan", "100 milliondan", "300 milliondan ortiq.")
t.B("Sovet davrida Navro‘z qanday tamg‘a bilan taqiqlangan?", "diniy bayram", "chet el bayrami", "burjua bayrami", "qishloq bayrami", "«Diniy bayram» tamg‘asi bilan.")
t.B("Navro‘z umumxalq bayrami deb qachon e’lon qilingan?", "1990-yilda", "1991-yilda", "2009-yilda", "2010-yilda", "1990-yilda, 21-mart dam olish kuni.")
t.B("YUNESKO Navro‘zni nomoddiy madaniy meros sifatida qachon e’tirof etgan?", "2009-yilda", "2010-yilda", "1990-yilda", "2007-yilda", "2009-yilda.")
t.B("BMT 21-martni Xalqaro Navro‘z kuni deb qachon e’lon qilgan?", "2010-yilda", "2009-yilda", "1990-yilda", "2020-yilda", "2010-yilda.")
t.B("Toshkent islom universiteti qachon ochilgan?", "1999-yilda", "1990-yilda", "2007-yilda", "2018-yilda", "1999-yilda.")
t.B("Hazrati Imom (Hastimom) majmuasi qachon qayta ta’mirlangan?", "2007-yilda", "1999-yilda", "2017-yilda", "2020-yilda", "2007-yilda.")
t.B("Hastimom majmuasida qaysi xalifa davriga oid noyob mus’haf saqlangan?", "xalifa Usmon", "xalifa Abu Bakr", "xalifa Umar", "xalifa Ali", "Usmon mus’hafi.")
t.B("Usmon mus’hafidan 2004-yilda nusxa ko‘chirgan xattot kim?", "Habibulloh Solih", "Abu Muin Nasafiy", "Burhoniddin Marg‘inoniy", "Is’hoqxon Ibrat", "Habibulloh Solih.")
t.B("ICESCO 2007-yilda qaysi shaharni Islom madaniyati poytaxti deb e’lon qilgan?", "Toshkent", "Buxoro", "Samarqand", "Xiva", "Toshkent (2020 – Buxoro).")
t.B("2024-yilda Xiva qanday maqomga ega bo‘ldi?", "«Islom dunyosining turizm poytaxti»", "«Islom madaniyati poytaxti»", "«Turkiy dunyo madaniy poytaxti»", "«MDH yoshlar poytaxti»", "ITT tomonidan turizm poytaxti.")
t.B("Islom sivilizatsiyasi markazi gumbazining balandligi necha metr?", "65 metr", "56 metr", "100 metr", "45 metr", "65 metr.")
t.B("Islom sivilizatsiyasi markaziga qachon poydevor qo‘yilgan?", "2018-yil Ramazon hayiti kuni", "2017-yil Navro‘z kuni", "2020-yil Qurbon hayiti kuni", "2016-yil Mustaqillik kuni", "2018-yil Ramazon hayiti.")
t.NAT("Sovet hokimiyati davrida Navro‘z taqiqlandi.", "xalq bayramni unutmadi, goh oshkor, goh yashirin nishonlayverdi", "bayram butunlay unutildi", "bayram boshqa sanaga ko‘chirildi", "faqat shaharlarda nishonlandi", "Yashirin nishonlandi.")
t.NAT("1990-yildan Saudiya Arabistoniga borish imkoniyati yaratildi.", "yurtdoshlarimiz haj amalini ado eta boshladi", "haj taqiqlandi", "faqat sanoqli kishilar bordi", "masjidlar yopildi", "Haj imkoniyati.")
t.NAT("2009–2010-yillarda Navro‘z xalqaro e’tirofga ega bo‘ldi.", "BMT bosh qarorgohida Navro‘zni nishonlash an’anaga aylandi", "Navro‘z taqiqlandi", "Navro‘z faqat O‘zbekistonda qoldi", "bayram bekor qilindi", "BMTda nishonlanadi.")
t.NAT("2024-yilda Xiva «Islom dunyosining turizm poytaxti» deb e’lon qilindi.", "shahardagi obidalar atrofida obodonlashtirish ishlari va madaniy tadbirlar o‘tkazildi", "shahar yopildi", "sayyohlar kamaydi", "obidalar buzildi", "Obodonlashtirish.")
t.TF("Toshkent islom universiteti hozir O‘zbekiston xalqaro islomshunoslik akademiyasi sifatida faoliyat yuritadi.", True, "To‘g‘ri.")
t.TF("Islom sivilizatsiyasi markazi zamonaviy shisha uslubida qurilgan.", False, "Noto‘g‘ri: qadimiy me’morchilik uslubida barpo etilgan.")
t.TF4([("Markazda «Ikkinchi Renessans davri» bo‘limi bor.", True), ("Markaz qurilishi 2017-yildagi qarorga binoan boshlangan.", True),
       ("Burhoniddin Marg‘inoniy, Abduxoliq G‘ijduvoniy, Moturidiy tavallud sanalari nishonlandi.", True), ("Sovet davrida xudosizlik taqiqlangan edi.", False)],
      "4-noto‘g‘ri: sovet davrida xudosizlik keng targ‘ib etilgan.")
t.MUL([("Navro‘zda ko‘chatlar o‘tqaziladi, xayriya hasharlari o‘tkaziladi.", True),
       ("Islom sivilizatsiyasi markazida muzey, kutubxona va ilmiy markaz bor.", True),
       ("2020-yilda ICESCO Samarqandni Islom madaniyati poytaxti deb e’lon qilgan.", False)],
      "III noto‘g‘ri: 2020-yilda Buxoro.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Navro‘z umumxalq bayrami deb e’lon qilindi", "Toshkent islom universiteti ochildi", "Hastimom majmuasi ta’mirlandi", "YUNESKO Navro‘zni nomoddiy meros deb tan oldi", "BMT Xalqaro Navro‘z kunini e’lon qildi", "Islom sivilizatsiyasi markaziga poydevor qo‘yildi"],
      "1990 → 1999 → 2007 → 2009 → 2010 → 2018.")
t.MATCH("Shaharlarni maqomlari bilan moslashtiring.", ["Toshkent (2007)", "Buxoro (2020)", "Xiva (2024)", "Buxoro (2022)"],
        ["ICESCO Islom madaniyati poytaxti", "ICESCO Islom madaniyati poytaxti (ikkinchi)", "Islom dunyosining turizm poytaxti", "Turkiy dunyo yoshlar tashabbuslari poytaxti", "MDH yoshlar poytaxti"], 'abcd',
        "Toshkent 2007 va Buxoro 2020 – Islom madaniyati poytaxti; Xiva – turizm; Buxoro 2022 – yoshlar poytaxti.")
t.VENN("Milliy qadriyatlar", "Diniy qadriyatlar",
       [("Navro‘z bayrami", 1), ("hashar va to‘y marosimlari", 1),
        ("haj amalini ado etish", 2), ("Usmon mus’hafi", 2),
        ("sovet davrida taqiqlangan, mustaqillikda tiklangan", 3)],
       "Navro‘z, hashar – milliy; haj, mus’haf – diniy; ikkalasi sovet davrida cheklangan.")
t.MAPMATCH('uzb', ['Toshkent', 'Buxoro', 'Xiva', 'Marg‘ilon'],
           ["2007-yilda Islom madaniyati poytaxti, Hastimom majmuasi joylashgan", "2020-yilda Islom madaniyati poytaxti deb e’lon qilingan", "2024-yilda «Islom dunyosining turizm poytaxti»", "Burhoniddin Marg‘inoniy nisbasi bog‘liq shahar"],
           "1 – Toshkent; 2 – Buxoro; 3 – Xiva; 4 – Marg‘ilon.")

# 16-mavzu. Madaniyat va san’at taraqqiyoti
t = Topic('y11u16', 11016); TOPICS['y11u16'] = t
t.B("Mustaqillikdan so‘ng qaysi viloyatlarda davlat qo‘g‘irchoq teatrlari tashkil etilgan?", "Farg‘ona va Xorazmda", "Qashqadaryo va Namanganda", "Buxoro va Samarqandda", "Surxondaryo va Jizzaxda", "Farg‘ona va Xorazmda.")
t.B("Alisher Navoiy nomidagi katta teatr binosi qachon qayta ta’mirlangan?", "2015-yilda", "2001-yilda", "1993-yilda", "2018-yilda", "2015-yilda.")
t.B("«Turkiston» san’at saroyi qachon ish boshlagan?", "1993-yilda", "1997-yilda", "2014-yilda", "2001-yilda", "1993-yil, Toshkent.")
t.B("«Teatr: Sharq – G‘arb» xalqaro festivali qachon bo‘lib o‘tgan?", "1997-yilda", "1993-yilda", "2001-yilda", "2018-yilda", "1997-yilda.")
t.B("2001-yilda qaysi teatrga «Milliy teatr» maqomi berilgan?", "Hamza nomidagi o‘zbek davlat akademik drama teatriga", "Alisher Navoiy nomidagi katta teatrga", "«Ilhom» teatriga", "«Turon» teatr studiyasiga", "Hamza nomidagi teatr.")
t.B("O‘zbekistonda ilk harbiy teatr studiyasi qanday nomlangan?", "«Turon»", "«Ilhom»", "«Yoshlar»", "«Eski masjid»", "2018-yil, «Turon».")
t.B("Jadidlarning «Turon» teatr truppasi kimning badiiy rahbarligida tashkil etilgan?", "Abdulla Avloniy", "Mahmudxo‘ja Behbudiy", "Abdulla Qodiriy", "Munavvar qori", "Abdulla Avloniy.")
t.B("2021-yildan qayta tiklangan Toshkent xalqaro kinofestivali qanday nomlanadi?", "«Ipak yo‘li durdonasi»", "«Oltin humo»", "«Tirik tarix»", "«Sharq taronalari»", "«Ipak yo‘li durdonasi».")
t.B("Kinoijodkorlarni rag‘batlantirish uchun qaysi mukofot ta’sis etilgan?", "«Oltin humo»", "«Nihol»", "«Ipak yo‘li durdonasi»", "«Xalq ustasi»", "«Oltin humo».")
t.B("«O‘zbekiston – Vatanim manim» ko‘rik-tanlovi qachondan o‘tkazila boshlagan?", "1996-yildan", "1991-yildan", "2002-yildan", "2017-yildan", "1996-yildan.")
t.B("Toshkent davlat konservatoriyasi O‘zbekiston davlat konservatoriyasiga qachon aylantirilgan?", "2002-yilda", "1997-yilda", "2020-yilda", "1996-yilda", "2002-yilda.")
t.B("O‘zbekiston davlat xoreografiya akademiyasi qachon tashkil etilgan?", "2020-yilda", "2002-yilda", "2017-yilda", "1997-yilda", "2020-yilda.")
t.B("O‘zbekiston Badiiy akademiyasi qachon tashkil etilgan?", "1997-yilda", "1993-yilda", "2002-yilda", "2020-yilda", "1997-yilda.")
t.B("Adiblar xiyoboni qachon barpo etilgan?", "2020-yilda", "2017-yilda", "2021-yilda", "2015-yilda", "2020-yil, Toshkent.")
t.B("Muzey sohasiga oid qaysi jurnal faoliyati yo‘lga qo‘yilgan?", "«Moziydan sado»", "«Tafakkur»", "«Ma’naviy hayot»", "«Yagona oilada»", "«Moziydan sado».")
t.B("Xalqaro muzeylar kuni qaysi sana?", "18-may", "21-mart", "11-fevral", "16-noyabr", "18-may.")
t.B("O‘zbekiston Milliy muzeyi qurilishiga qachon tamal toshi qo‘yilgan?", "2025-yilda", "2020-yilda", "2017-yilda", "1996-yilda", "2025-yilda.")
t.NAT("Farg‘ona, Xorazmda qo‘g‘irchoq teatrlari, Qashqadaryo, Namangan, Surxondaryoda yangi teatr guruhlari ish boshladi.", "viloyatlardagi bolalar va kattalar teatr tomoshalaridan bahramand bo‘la boshladi", "teatrlar faqat Toshkentda qoldi", "tomoshabinlar kamaydi", "teatrlar yopildi", "Viloyatlarda tomoshalar.")
t.NAT("1996-yildan «O‘zbekiston – Vatanim manim» ko‘rik-tanlovi o‘tkazila boshlandi.", "mustaqillikni tarannum etuvchi yuzlab qo‘shiqlar yaratildi", "qo‘shiqlar taqiqlandi", "estrada yopildi", "musiqa maktablari tugatildi", "Yuzlab qo‘shiqlar.")
t.NAT("«Tirik tarix» loyihasi yo‘lga qo‘yildi.", "qadimgi davrdan yaqin tarixgacha bo‘lgan turkum filmlar yaratila boshlandi", "kinostudiyalar yopildi", "tarixiy filmlar taqiqlandi", "faqat xorijiy filmlar ko‘rsatildi", "Tarixiy turkum filmlar.")
t.NAT("Yozuvchilarni qo‘llab-quvvatlash uchun «Ijod» fondi tashkil etildi.", "yosh ijodkorlarning kitoblari chop etila boshladi", "kitob nashri to‘xtadi", "adabiyot taqiqlandi", "yozuvchilar uyushmasi tugatildi", "Yosh ijodkorlar kitoblari.")
t.TF("2014-yilda Farg‘ona viloyati teatr-konsert saroyi ochilgan.", True, "To‘g‘ri.")
t.TF("«Turon» harbiy teatr studiyasi faqat harbiylarga xizmat ko‘rsatadi.", False, "Noto‘g‘ri: keng aholi vakillariga ham xizmat ko‘rsatadi.")
t.TF4([("1996-yili Toshkentda Temuriylar tarixi davlat muzeyi va Olimpiya shon-shuhrati muzeyi tashkil etildi.", True), ("Termizda Arxeologiya muzeyi tashkil etildi.", True),
       ("2020-yilda «Shon-sharaf» muzeyi va Toshkent muzeyi ish boshladi.", True), ("Qatag‘on qurbonlari xotirasi muzeyi 2020-yilda tashkil etildi.", False)],
      "4-noto‘g‘ri: 2002-yilda tashkil etilgan.")
t.MUL([("«O‘zbekiston Respublikasi xalq ustasi» faxriy unvoni ta’sis etildi.", True),
       ("Odil Yoqubov, Pirimqul Qodirov tarixiy shaxslarga bag‘ishlangan asarlar yaratdi.", True),
       ("«Muzeylar haftaligi» har yili mart oyida o‘tkaziladi.", False)],
      "III noto‘g‘ri: sentyabr oyida o‘tkaziladi.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["«Turkiston» san’at saroyi", "«Teatr: Sharq – G‘arb» festivali", "Hamza teatriga «Milliy teatr» maqomi", "Farg‘ona teatr-konsert saroyi", "«Turon» harbiy teatr studiyasi", "«Ipak yo‘li durdonasi» kinofestivali"],
      "1993 → 1997 → 2001 → 2014 → 2018 → 2021.")
t.MATCH("Ijodkorlarni sohasi bilan moslashtiring.", ["Akmal Nur", "Ilhom Jabborov", "O‘tkir Hoshimov", "Rauf Parfi"],
        ["rassom (tasviriy san’at)", "haykaltarosh", "nasr (yozuvchi)", "she’riyat (shoir)", "kinorejissyor"], 'abcd',
        "Akmal Nur – rassom; Ilhom Jabborov – haykaltarosh (rassom va haykaltaroshlar qatorida); Hoshimov – nasr; Rauf Parfi – she’riyat.")
t.VENN("Teatr san’ati", "Musiqa san’ati",
       [("«Turon» harbiy teatr studiyasi", 1), ("«Teatr: Sharq – G‘arb» festivali", 1),
        ("«Sharq taronalari» festivali", 2), ("maqom va baxshichilik", 2),
        ("mustaqillik yillarida qo‘llab-quvvatlandi", 3)],
       "Teatr – Turon, Sharq–G‘arb; musiqa – Sharq taronalari, maqom; ikkalasi qo‘llab-quvvatlandi.")
t.MAPMATCH('uzb', ['Farg‘ona', 'Termiz', 'Qarshi', 'Toshkent'],
           ["2014-yilda viloyat teatr-konsert saroyi ochilgan shahar", "Arxeologiya muzeyi tashkil etilgan shahar", "«Eski masjid» teatr studiyasi faoliyat yuritgan viloyat markazi", "2020-yilda Adiblar xiyoboni barpo etilgan shahar"],
           "1 – Farg‘ona; 2 – Termiz; 3 – Qarshi (Qashqadaryo); 4 – Toshkent.")

# 17-mavzu. Tashqi siyosatning shakllanishi va ustuvor yo‘nalishlari
t = Topic('y11u17', 11017); TOPICS['y11u17'] = t
t.B("Sharq va G‘arbni savdo-iqtisodiy va madaniy jihatdan tutashtirgan qaysi yo‘l O‘zbekiston hududidan o‘tgan?", "Buyuk ipak yo‘li", "Shoh yo‘li", "Qahrabo yo‘li", "Choy yo‘li", "Buyuk ipak yo‘li.")
t.B("O‘zbekiston geosiyosiy joylashuvining asosiy noqulayligi nima?", "xalqaro dengiz portlariga to‘g‘ridan to‘g‘ri chiqish imkoni yo‘qligi", "tabiiy resurslarning yo‘qligi", "iqlimning noqulayligi", "aholining kamligi", "Dengizga chiqish yo‘q.")
t.B("O‘zbekiston tashqi siyosatini amalga oshiruvchi davlat organi qaysi?", "Tashqi ishlar vazirligi", "Mudofaa vazirligi", "Iqtisodiyot vazirligi", "Adliya vazirligi", "Tashqi ishlar vazirligi.")
t.B("Jahon iqtisodiyoti va diplomatiya universiteti qachon tashkil etilgan?", "1992-yilda", "1991-yilda", "2017-yilda", "1995-yilda", "1992-yilda.")
t.B("Konstitutsiyaning qaysi bobi «Tashqi siyosat» deb nomlanadi?", "4-bob", "2-bob", "6-bob", "17-bob", "4-bob.")
t.B("Konstitutsiyaning qaysi moddalari tashqi faoliyatni huquqiy asoslaydi?", "17–18-moddalar", "4–5-moddalar", "20–21-moddalar", "1–2-moddalar", "17–18-moddalar.")
t.B("2025-yil holatiga ko‘ra O‘zbekiston nechta davlat bilan aloqa o‘rnatgan?", "163 ta", "130 ta", "193 ta", "100 ta", "163 ta.")
t.B("O‘zbekiston nechtaga yaqin «Markaziy Osiyo+» platformalarida ishtirok etmoqda?", "10 ga yaqin", "5 ga yaqin", "20 ga yaqin", "163 ga yaqin", "10 ga yaqin.")
t.B("O‘zbekiston qaysi bloklarga qo‘shilmaydi?", "harbiy-siyosiy bloklarga", "savdo uyushmalariga", "madaniy tashkilotlarga", "xalqaro tashkilotlarga", "Harbiy-siyosiy bloklarga.")
t.B("O‘zbekiston nizolarni qanday hal qilish tarafdori?", "faqat tinch siyosiy yo‘l bilan", "kuch ishlatib", "harbiy ittifoqlar orqali", "iqtisodiy bosim bilan", "Tinch siyosiy yo‘l bilan.")
t.B("Ikki davlat o‘rtasidagi siyosiy, iqtisodiy, madaniy aloqa va hamkorlik nima deyiladi?", "ikki tomonlama munosabatlar", "ko‘p tomonlama munosabatlar", "mintaqaviy integratsiya", "harbiy ittifoq", "Ikki tomonlama munosabatlar.")
t.B("2017-yildan O‘zbekiston tashabbusi bilan anjumanlar o‘tkazilgan shaharlar qaysi?", "Toshkent, Samarqand, Xiva, Buxoro", "Nukus, Termiz, Qarshi, Navoiy", "Andijon, Namangan, Farg‘ona, Qo‘qon", "Jizzax, Guliston, Urganch, Nukus", "Toshkent, Samarqand, Xiva, Buxoro.")
t.NAT("Mustaqil tashqi siyosat olib borish zarurati yuzaga keldi.", "Tashqi ishlar vazirligi faoliyati yo‘lga qo‘yildi", "tashqi aloqalar to‘xtatildi", "faqat bir davlat bilan aloqa qilindi", "elchixonalar yopildi", "TIV faoliyati.")
t.NAT("Diplomatiya sohasida milliy kadrlarga ehtiyoj tug‘ildi.", "1992-yilda Jahon iqtisodiyoti va diplomatiya universiteti tashkil etildi", "chet ellik diplomatlar yollandi", "kadrlar tayyorlash to‘xtatildi", "diplomatiya bekor qilindi", "JIDU.")
t.NAT("2017-yildan ochiq va faol tashqi siyosat yuritila boshlandi.", "xalqaro hamjamiyat tomonidan yuqori baholanib, Markaziy Osiyoda yangi hamkorlik imkoniyatlari ochildi", "O‘zbekiston yakkalanib qoldi", "qo‘shnilar bilan munosabatlar uzildi", "xalqaro tashkilotlardan chiqildi", "Yuqori baholandi.")
t.NAT("Markaziy Osiyoga yaqin hududlarda beqarorlik, terrorizm va ekstremizm mavjud.", "bu omillar mintaqa tashqi siyosati uchun noqulay omil hisoblanadi", "bu omillar foydali hisoblanadi", "O‘zbekiston harbiy blokka kirdi", "chegaralar ochib yuborildi", "Noqulay omil.")
t.TF("O‘zbekiston xalq manfaatidan kelib chiqib ittifoqlar tuzishi, hamdo‘stliklarga kirishi va ulardan chiqishi mumkin.", True, "To‘g‘ri.")
t.TF("O‘zbekiston boshqa davlatlarning ichki ishlariga aralashish tamoyiliga amal qiladi.", False, "Noto‘g‘ri: aralashmaslik tamoyiliga amal qiladi.")
t.TF4([("Davlatlarning suveren tengligini hurmat qilish – asosiy tamoyil.", True), ("Chegaralarning daxlsizligi – asosiy tamoyil.", True),
       ("Ochiqlik va pragmatizm – asosiy tamoyil.", True), ("Kuch ishlatish orqali nizolarni hal qilish – asosiy tamoyil.", False)],
      "4-noto‘g‘ri: kuch ishlatmaslik yoki kuch bilan tahdid qilmaslik tamoyili.")
t.MUL([("O‘zbekiston qulay iqlim, boy tabiiy resurslar va intellektual salohiyatga ega.", True),
       ("Xalqaro majburiyatlarni bajarish – tashqi siyosat tamoyillaridan biri.", True),
       ("O‘zbekiston dengiz portlariga to‘g‘ridan to‘g‘ri chiqa oladi.", False)],
      "III noto‘g‘ri: dengiz portlariga to‘g‘ridan to‘g‘ri chiqish imkoni yo‘q.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["O‘zbekiston mustaqilligi e’lon qilindi", "JIDU tashkil etildi", "ochiq va faol tashqi siyosat bosqichi boshlandi", "163 ta davlat bilan aloqa o‘rnatildi"],
      "1991 → 1992 → 2017 → 2025.")
t.MATCH("Tushunchalarni izohi bilan moslashtiring.", ["Konstitutsiya 4-bobi", "JIDU", "Markaziy Osiyo+", "Buyuk ipak yo‘li"],
        ["«Tashqi siyosat» bobi", "diplomat kadrlar tayyorlovchi universitet", "O‘zbekiston ishtirok etayotgan hamkorlik platformalari", "Sharq va G‘arbni tutashtirgan tarixiy yo‘l", "harbiy-siyosiy blok"], 'abcd',
        "4-bob – Tashqi siyosat; JIDU – kadrlar; MO+ – platformalar; Ipak yo‘li – Sharq–G‘arb.")
t.VENN("Geosiyosiy imkoniyatlar", "Geosiyosiy noqulayliklar",
       [("boy tabiiy resurslar", 1), ("Buyuk ipak yo‘li hududida joylashgan", 1),
        ("dengiz portlariga chiqish yo‘qligi", 2), ("yaqin hududlardagi beqarorlik", 2),
        ("Markaziy Osiyodagi joylashuv", 3)],
       "Resurslar, ipak yo‘li – imkoniyat; dengizga chiqish yo‘qligi, beqarorlik – noqulaylik; joylashuv ikkalasiga ham ta’sir qiladi.")
t.MAPMATCH('uzb', ['Toshkent', 'Samarqand', 'Xiva', 'Buxoro'],
           ["O‘zbekiston poytaxti", "Samarqand viloyati markazi", "Xorazm viloyatidagi qadimiy shahar", "Buxoro viloyati markazi"],
           "2017-yildan nufuzli anjumanlar o‘tkazilgan shaharlar: 1 – Toshkent; 2 – Samarqand; 3 – Xiva; 4 – Buxoro.")
