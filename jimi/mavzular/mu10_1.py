from qlib import Topic, PLACES, REG
TOPICS = {}
CA = 'ca'
PLACES.update({'Skobelev (Farg‘ona)': (71.78, 40.38), 'Petrograd': (30.3, 59.93), 'Qizilo‘rda (Oqmachit)': (65.5, 44.85)})

# 1-§. Turkiston o‘lkasi 1917-yil fevral – oktyabr oralig‘ida
t = Topic('e10u1', 10101); TOPICS['e10u1'] = t
t.B("O‘zbekiston tarixida sovet davri qaysi yillarni o‘z ichiga oladi?", "1917 – 1991-yillar", "1917 – 1924-yillar", "1925 – 1991-yillar", "1918 – 1990-yillar", "1917 – 1991-yillar sovet davrini tashkil qiladi.")
t.B("Sovet davrining ikkinchi bosqichi qaysi voqea bilan boshlanadi?", "1925-yil fevralda O‘zbekiston SSRning tuzilishi", "Oktyabr to‘ntarishi", "Turkiston Muxtoriyatining tuzilishi", "BXSRning tashkil topishi", "Ikkinchi bosqich 1925-yil fevralda O‘zSSR tuzilishi bilan boshlanadi.")
t.B("“Haq olinur, berilmas!” shiorini kim o‘rtaga tashlagan?", "Mahmudxo‘ja Behbudiy", "Abdurauf Fitrat", "Munavvarqori Abdurashidxonov", "Mustafo Cho‘qay", "Shior Mahmudxo‘ja Behbudiy tomonidan o‘rtaga tashlangan.")
t.B("Bolshevizmni “Rusiyada bosh ko‘targan yangi bir balo – bolshevik balosi” deb atagan jadid kim?", "Abdurauf Fitrat", "Mahmudxo‘ja Behbudiy", "Ubaydulla Xo‘jayev", "Sherali Lapin", "Jadidchilikning yirik nazariyotchisi Abdurauf Fitrat shunday yozgan.")
t.B("Rossiyada Fevral inqilobi qachon bo‘lgan?", "1917-yil 27-fevralda (yangi hisob bilan 12-martda)", "1917-yil 25-oktyabrda", "1917-yil 2-martda", "1918-yil 14-fevralda", "1917-yil 27-fevral (yangi hisob – 12-mart).")
t.B("Rossiya imperatori Nikolay II qachon taxtdan voz kechdi?", "1917-yil 2-martda", "1917-yil 27-fevralda", "1917-yil 31-martda", "1917-yil 7-aprelda", "Nikolay II 2-mart kuni o‘z ixtiyori bilan taxtdan voz kechdi.")
t.B("Rossiya Muvaqqat hukumatiga 1917-yil iyul – oktyabrda kim boshchilik qilgan?", "Aleksandr Kerenskiy", "Georgiy Lvov", "Nikolay Shchepkin", "A.N.Kuropatkin", "Mart – iyulda G.Lvov, iyul – oktyabrda A.Kerenskiy.")
t.B("Toshkentda ishchi deputatlari Soveti (Toshkent Soveti) qachon tuzilgan?", "1917-yil 2-martda", "1917-yil 14-martda", "1917-yil 7-aprelda", "1917-yil 31-martda", "Toshkent Soveti 1917-yil 2-mart kuni tuzilgan.")
t.B("Turkiston general-gubernatori A.N.Kuropatkin qachon uy qamog‘iga olindi?", "1917-yil 31-martda", "1917-yil 2-martda", "1917-yil 7-aprelda", "1917-yil 14-martda", "Kuropatkin 31-martda uy qamog‘iga tashlangan.")
t.B("Muvaqqat hukumat tomonidan tuzilgan Turkiston komiteti necha kishidan iborat bo‘lgan?", "9 kishidan", "7 kishidan", "15 kishidan", "12 kishidan", "1917-yil 7-aprelda 9 kishidan iborat Turkiston komiteti tuzildi.")
t.B("Turkiston komitetiga raislik qilgan kadetlar partiyasi vakili kim?", "Nikolay Shchepkin", "Vladimir Nakivkin", "Sadri Maqsudiy", "Aleksandr Kerenskiy", "Kadet N.Shchepkin va eser V.Nakivkin raislik qilishgan.")
t.B("“Sho‘roi Islomiya” tashkiloti qachon tuzilgan?", "1917-yil 14-martda", "1917-yil iyunda", "1917-yil 16-aprelda", "1917-yil sentyabrda", "1917-yil 14-martda Toshkentda tuzildi.")
t.B("“Sho‘roi Islomiya”ga dastlab kim rais qilib saylangan?", "Abdulvohidqori Abduraufqori o‘g‘li", "Ubaydulla Xo‘jayev", "Mustafo Cho‘qay", "Sherali Lapin", "Dastlab Abdulvohidqori, keyinchalik Ubaydulla Xo‘jayev rais bo‘lgan.")
t.B("Butunturkiston musulmonlarining I qurultoyi qachon bo‘lib o‘tdi?", "1917-yil 16 – 23-aprelda", "1917-yil 14-martda", "1917-yil sentyabrda", "1917-yil 26 – 29-noyabrda", "1917-yil 16 – 23-aprelda Toshkentda.")
t.B("Turkiston o‘lka musulmonlar kengashi (Kraymussovet)ga kim rais bo‘lgan?", "Mustafo Cho‘qay", "Munavvarqori Abdurashidxonov", "Ahmad Zaki Validiy", "Ubaydulla Xo‘jayev", "Mustafo Cho‘qay rais, Munavvarqori va A.Z.Validiy kotiblar.")
t.B("“Sho‘roi Ulamo” jamiyati qachon tuzildi?", "1917-yil iyunda", "1917-yil martda", "1917-yil aprelda", "1918-yil mayda", "1917-yil iyunda ulamolar ajralib chiqib tuzgan.")
t.B("“Sho‘roi Ulamo”ning Toshkent shu’basiga kim rahbarlik qilgan?", "Sherali Lapin", "Mulla Muhiddinxon", "Islom Sulton Shoahmedov", "Abdulvohidqori", "Toshkent shu’basiga Sherali Lapin rahbarlik qilgan.")
t.B("“Sho‘roi Ulamo” qaysi jurnallarni nashr qilgan?", "“al-Izoh” va “al-Isloh”", "“Sho‘roi islom” va “Najot”", "“Kengash” va “Hurriyat”", "“Oyna” va “Tarjimon”", "“al-Izoh” va “al-Isloh” jurnallari.")
t.B("1917-yil sentyabrda ulamochilar va sho‘roi islomchilar birlashib qaysi partiyani tuzdilar?", "“Ittifoqi muslimin”", "“Ozod Turkiston”", "“Yosh buxoroliklar”", "“Turk adami markaziyat”", "Turkiston va Qozog‘iston musulmonlari qurultoyida tuzildi.")
t.B("“Kadetlar” atamasi nimani anglatadi?", "konstitutsion demokratlar", "sotsial revolyutsionerlar", "konstitutsion monarxistlar", "kommunistlar", "Kadet – “konstitutsion demokratlar” birikmasining bosh harflari.")
t.NAT("Muvaqqat hukumat Turkiston general-gubernatorligini Turkiston komitetiga almashtirdi.", "mustamlakachilik boshqaruvi mohiyatan avvalgicha qoldi, faqat nomi o‘zgardi", "Turkistonga muxtoriyat berildi", "boshqaruv to‘liq mahalliy xalq qo‘liga o‘tdi", "general-gubernatorlik qayta tiklandi", "Mustamlakachilik boshqaruvi mohiyatan saqlanib, faqat nomi o‘zgardi.")
t.NAT("Jadidlar bilan qadimchi ulamolar o‘rtasida kelishmovchiliklar kuchaydi.", "“Sho‘roi Islomiya”da bo‘linish yuz berib, “Sho‘roi Ulamo” tuzildi", "“Ittifoqi muslimin” tarqatildi", "Kraymussovet tugatildi", "Turkiston komiteti tuzildi", "1917-yil iyunda bir guruh ulamolar ajralib “Sho‘roi Ulamo”ni tuzdi.")
t.TF("Turkiston komiteti tarkibiga o‘zbek xalqining bitta ham vakili kiritilmagan.", True, "To‘g‘ri, darslikda shunday ta’kidlangan.")
t.TF("Turkistonda ham Rossiyadagi kabi ikki hokimiyatchilik vujudga keldi.", False, "Noto‘g‘ri: Turkistonda uch hokimiyatchilik paydo bo‘ldi.")
t.MUL([("Rossiyada grigorian kalendari 1918-yil 26-yanvardagi dekret bilan joriy qilindi.", True),
       ("1918-yil 31-yanvardan keyin 1-fevralga emas, 14-fevralga o‘tildi.", True),
       ("Kraymussovetga Ahmad Zaki Validiy rais etib saylandi.", False)],
      "III noto‘g‘ri: rais – Mustafo Cho‘qay, A.Z.Validiy kotib bo‘lgan.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["Toshkent Sovetining tuzilishi", "“Sho‘roi Islomiya”ning tuzilishi", "Kuropatkinning uy qamog‘iga olinishi",
       "Turkiston komitetining tuzilishi", "Butunturkiston musulmonlarining I qurultoyi"],
      "1917-yil: 2-mart → 14-mart → 31-mart → 7-aprel → 16 – 23-aprel.")
t.MAPN(CA, ['Qo‘qon', 'Toshkent', 'Samarqand', 'Marv'], "“Sho‘roi Ulamo” jamiyatining eng yirik shu’basi joylashgan shahar qaysi raqam bilan belgilangan?",
       "Jamiyatning eng yirik shu’basi Qo‘qonda bo‘lib, unga Mulla Muhiddinxon va Mulla Ulug‘xon To‘rayev rais bo‘lishgan.")
t.VENN("“Sho‘roi Islomiya”", "“Sho‘roi Ulamo”",
       [("1917-yil 14-martda tuzilgan", 1), ("“Sho‘roi islom” gazetasini chiqargan", 1),
        ("1917-yil iyunda tuzilgan", 2), ("“al-Izoh” va “al-Isloh” jurnallarini nashr qilgan", 2),
        ("1918-yil mayda bolsheviklar tomonidan tugatilgan", 3), ("“Ittifoqi muslimin” partiyasini tuzishda qatnashgan", 3)],
       "Ikkala tashkilot 1918-yil mayda tugatilgan va sentyabrda birlashib “Ittifoqi muslimin”ni tuzgan.")

# 2-§. Turkistonda sovet hokimiyatining majburiy tarzda o‘rnatilishi hamda bolsheviklar diktaturasi
t = Topic('e10u2', 10102); TOPICS['e10u2'] = t
t.B("Petrogradda Qishki saroyga bostirib kirib, Muvaqqat hukumat a’zolarini qamoqqa olish qachon yuz berdi?", "1917-yil 24-oktyabrdan 25-oktyabrga o‘tar kechasi", "1917-yil 27-oktyabrda", "1917-yil 28-oktyabrda", "1917-yil 2-martda", "24-oktyabrdan 25-oktyabrga o‘tar kechasi.")
t.B("Butunrossiya Sovetlarining II syezdida bolsheviklar qaysi dekretlarni e’lon qildi?", "Tinchlik va yer to‘g‘risida", "Non va mehnat to‘g‘risida", "Muxtoriyat va erkinlik to‘g‘risida", "Sanoat va savdo to‘g‘risida", "Tinchlik va yer to‘g‘risidagi dekretlar.")
t.B("Rossiyada Lenin boshchiligida tuzilgan hukumat qanday nomlangan?", "Xalq Komissarlari Soveti (XKS)", "Muvaqqat hukumat", "Davlat dumasi", "Markaziy Ijroiya Komiteti", "V.I.Ulyanov (Lenin) boshchiligida XKS tuzildi.")
t.B("1917-yil kuzida Turkistonda asosiy siyosiy kuchlar kimlar edi?", "eserlar va milliy partiyalar", "bolsheviklar va maksimalistlar", "kadetlar va monarxistlar", "mensheviklar va anarxistlar", "Bu yerda asosiy siyosiy kuchlar eserlar va milliy partiyalar edi.")
t.B("Oktyabr to‘ntarishi haqidagi xabar Toshkentga qachon yetib keldi?", "27-oktyabrda", "25-oktyabrda", "28-oktyabrda", "1-noyabrda", "Xabar 27-oktyabrda Toshkentga yetib keldi.")
t.B("Muvaqqat hukumat Turkiston o‘lkasining bosh komissari qilib kimni tayinlagan edi?", "general P.Korovichenkoni", "general A.N.Kuropatkinni", "Fyodor Kolesovni", "Ye.Perfilevni", "Bosh komissar – general P.Korovichenko.")
t.B("Toshkentning yangi shahar qismida necha kunlik janglardan so‘ng sovet hokimiyati o‘rnatildi?", "to‘rt kunlik", "uch kunlik", "ikki kunlik", "bir haftalik", "To‘rt kunlik janglardan so‘ng.")
t.B("Turkiston o‘lka Xalq Komissarlari Soveti qaysi syezdda tuzildi?", "Turkiston Sovetlarining III o‘lka syezdida", "Butunrossiya Sovetlarining II syezdida", "Turkiston Sovetlarining V o‘lka syezdida", "Musulmonlarning IV qurultoyida", "1917-yil 15 – 22-noyabrdagi III o‘lka syezdida.")
t.B("Turkiston o‘lka XKSda so‘l eserlarga nechta o‘rin berildi?", "8 ta", "7 ta", "9 ta", "5 ta", "8 o‘rin so‘l eserlarga, 7 o‘rin bolsheviklar va maksimalistlarga.")
t.B("Turkiston o‘lka XKS raisi lavozimini kim egalladi?", "Fyodor Kolesov", "Ye.Perfilev", "Ivan Tobolin", "P.Korovichenko", "Kasbi chizmachi bo‘lgan bolshevik Fyodor Kolesov.")
t.B("Turkiston o‘lka XKSda harbiy komissar qilib kim tayinlandi?", "izvoshchi Ye.Perfilev", "chizmachi F.Kolesov", "general P.Korovichenko", "Pyotr Kobozev", "Harbiy komissar – izvoshchi Ye.Perfilev.")
t.B("“Sho‘roi Ulamo”ning qaysi yetakchisi bolsheviklarni qo‘llab-quvvatladi?", "Sherali Lapin", "Mustafo Cho‘qay", "Munavvarqori", "Ubaydulla Xo‘jayev", "Toshkent shu’basi yetakchisi Sherali Lapin.")
t.B("Milliy Markaz (Kraymussovet) 1917-yil noyabr boshida qaysi shaharga ko‘chib o‘tdi?", "Qo‘qon", "Samarqand", "Andijon", "Namangan", "Toshkentdan Qo‘qonga ko‘chib o‘tdi.")
t.B("“Turli musulmon guruhlarining birlashgan kengashi” qachon o‘tkazildi?", "1917-yil 12 – 15-noyabrda", "1917-yil 15 – 22-noyabrda", "1917-yil 26 – 28-noyabrda", "1917-yil 28-oktyabrda", "1917-yil 12 – 15-noyabrda Toshkentda.")
t.B("“Maksimalistlar” atamasi nimani anglatadi?", "radikal o‘zgarishlar va islohotlar talab etuvchi siyosiy oqim", "konstitutsion demokratlar partiyasi", "dehqonlar manfaatini himoya qiluvchi guruh", "arman millatchilari partiyasi", "Mavjud tuzumni tanqid qilib, radikal o‘zgarishlar talab etuvchi oqim.")
t.B("Koalitsion hukumat deganda nima tushuniladi?", "bir nechta partiya tomonidan hukumatni ittifoq bo‘lib boshqarish", "bir partiyaning yakka hokimligi", "harbiy diktatura", "monarxiya boshqaruvi", "Bir nechta partiya ittifoq bo‘lib boshqaradigan hukumat.")
t.NAT("Rossiyada Oktyabr to‘ntarishi amalga oshirildi.", "hokimiyat Muvaqqat hukumatdan Lenin boshchiligidagi bolsheviklar qo‘liga o‘tdi", "Turkistonga muxtoriyat berildi", "Davlat dumasi tiklandi", "Muvaqqat hukumat kuchaydi", "Hokimiyat bolsheviklar partiyasi qo‘liga o‘tdi.")
t.NAT("Kengashda Sherali Lapin boshchiligidagi ulamochilar koalitsion hukumat tuzishni taklif qildi.", "bolsheviklar bu fikrni qat’iy rad etdi", "koalitsion hukumat tuzildi", "hukumat o‘rinlarining yarmi musulmonlarga berildi", "Lapin XKS raisi bo‘ldi", "Bolsheviklar ulamochilar fikrini qat’iy rad etishdi.")
t.TF("Turkiston o‘lka XKS tarkibiga mahalliy xalqlar vakillaridan biror kishi ham kiritilmadi.", True, "To‘g‘ri, hukumat faqat yevropaliklardan iborat qilib tuzildi.")
t.TF("Toshkentdagi qurolli to‘qnashuvlarda mahalliy aholi faol ishtirok etdi.", False, "Noto‘g‘ri: qurolli to‘qnashuvda mahalliy aholi deyarli ishtirok etmadi.")
t.MUL([("1917-yil noyabrda Samarqand, Skobelev va boshqa shaharlarda ham sovet hokimiyati o‘rnatildi.", True),
       ("Milliy Markaz bolsheviklar bilan hamkorlik qilishni qo‘llab-quvvatladi.", False),
       ("Jadidlar Butunturkiston musulmonlari qurultoyini chaqirib, muxtoriyat maqomini berishni taklif qildi.", True)],
      "II noto‘g‘ri: Milliy Markaz bolsheviklar bilan hamkorlikka qarshi chiqdi.")
t.MATCH("Sanalarni voqealar bilan moslashtiring (1917-yil).", ["24 – 25-oktyabr", "28-oktyabr", "12 – 15-noyabr", "15 – 22-noyabr"],
        ["Turkiston Sovetlarining III o‘lka syezdi", "Toshkentning yangi shahrida qurolli to‘qnashuvlar boshlanishi", "Qishki saroyning egallanishi", "turli musulmon guruhlarining birlashgan kengashi"],
        "cbda", "24 – 25-oktyabr – Qishki saroy; 28-oktyabr – Toshkentda janglar; 12 – 15-noyabr – kengash; 15 – 22-noyabr – III syezd.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["Qishki saroyning egallanishi", "Oktyabr to‘ntarishi haqidagi xabarning Toshkentga yetib kelishi", "Toshkentda qurolli to‘qnashuvlarning boshlanishi",
       "Turli musulmon guruhlarining birlashgan kengashi", "Turkiston o‘lka XKSning tuzilishi"],
      "24 – 25-oktyabr → 27-oktyabr → 28-oktyabr → 12 – 15-noyabr → 15 – 22-noyabr.")
t.MAPN(CA, ['Toshkent', 'Qo‘qon', 'Samarqand', 'Skobelev (Farg‘ona)'], "Milliy Markaz va “Sho‘roi Islomiya” o‘z qarorgohlarini ko‘chirgan shahar qaysi raqam bilan belgilangan?",
       "Ular bolsheviklar bilan hamkorlikka qarshi chiqib, Toshkentdan Qo‘qonga ko‘chib o‘tdi.", ask_idx=1)
t.VENN("Rossiya XKS (1917)", "Turkiston o‘lka XKS (1917)",
       [("V.I.Lenin boshchiligida tuzilgan", 1), ("Petrogradda tuzilgan", 1),
        ("raisi – F.Kolesov", 2), ("8 o‘rin so‘l eserlarga berilgan", 2),
        ("bolsheviklar ishtirokida tuzilgan sovet hukumati", 3)],
       "Rossiya XKS – Lenin, Petrograd; Turkiston XKS – Kolesov, 8 o‘rin so‘l eserlarga; ikkalasi ham bolsheviklar ishtirokidagi sovet hukumati.")

# 3-§. Turkiston Muxtoriyati
t = Topic('e10u3', 10103); TOPICS['e10u3'] = t
t.B("Butunturkiston o‘lka musulmonlarining favqulodda IV qurultoyi qachon va qayerda bo‘lib o‘tdi?", "1917-yil 26 – 28-noyabrda Qo‘qonda", "1917-yil 16 – 23-aprelda Toshkentda", "1918-yil 19 – 26-yanvarda Toshkentda", "1917-yil 12 – 15-noyabrda Samarqandda", "1917-yil 26 – 28-noyabrda Qo‘qon shahrida.")
t.B("Turkistonni muxtor deb e’lon qilgan qaror qachon qabul qilindi?", "27-noyabr kuni kechqurun", "26-noyabr kuni ertalab", "28-noyabrda", "1-dekabrda", "Qaror 27-noyabr kuni kechqurun qabul qilingan.")
t.B("Qurultoy qaroriga ko‘ra Turkiston qaysi davlat tarkibida muxtor deb e’lon qilindi?", "Federativ Rossiya Respublikasi tarkibida", "Turkiya tarkibida", "Buxoro amirligi tarkibida", "mustaqil davlat sifatida", "Federativ Rossiya Respublikasi tarkibida hududiy jihatdan muxtor.")
t.B("Ta’sis Majlisi chaqirilgunga qadar hokimiyat qaysi organlar qo‘lida bo‘lishi belgilandi?", "Turkiston Muvaqqat Kengashi va Turkiston Xalq (Millat) Majlisi", "Toshkent Soveti va XKS", "Turkiston komiteti va Kraymussovet", "“Sho‘roi Ulamo” va “Sho‘roi Islomiya”", "Turkiston Muvaqqat Kengashi va Xalq (Millat) Majlisi.")
t.B("Turkiston Muxtoriyati hukumati necha kishidan iborat tarkibda tuzildi?", "8 nafar", "9 nafar", "7 nafar", "12 nafar", "Muvaqqat Kengash a’zolaridan 8 nafar kishidan iborat.")
t.B("Turkiston Muxtoriyati hukumatining birinchi Bosh vaziri kim bo‘lgan?", "Muhammadjon Tinishboyev", "Mustafo Cho‘qay", "Islom Sulton Shoahmedov", "Ubaydulla Xo‘jayev", "Bosh vazir va ichki ishlar vaziri – M.Tinishboyev.")
t.B("Turkiston Muxtoriyati hukumatida harbiy vazir kim edi?", "Ubaydulla Xo‘jayev", "Obidjon Mahmudov", "Solomon Gersfeld", "Mustafo Cho‘qay", "Harbiy vazir – Ubaydulla Xo‘jayev.")
t.B("Turkiston Muxtoriyati hukumatida moliya vaziri kim bo‘lgan?", "Solomon Gersfeld", "Hidoyatbek Yurg‘uli Agayev", "Abdurahmon O‘rozayev", "Obidjon Mahmudov", "Moliya vaziri – Solomon Gersfeld.")
t.B("Muhammadjon Tinishboyev kasbi bo‘yicha kim bo‘lgan?", "temiryo‘l muhandisi", "huquqshunos", "agronom", "tog‘-kon sanoati mutaxassisi", "Tinishboyev temiryo‘l muhandisi bo‘lgan.")
t.B("Hidoyatbek Yurg‘uli Agayev hukumatda qaysi lavozimni egallagan?", "yer va suv boyliklari vaziri", "oziq-ovqat vaziri", "tashqi ishlar vaziri", "moliya vaziri", "Agronom H.Agayev – yer va suv boyliklari vaziri.")
t.B("Muxtoriyat hukumatining Murojaatnomasi qachon e’lon qilindi?", "1-dekabrda", "27-noyabrda", "28-noyabrda", "15-dekabrda", "Qurultoy tugagach, 1-dekabrda.")
t.B("1918-yil boshidagi ko‘rikda Muxtoriyat milliy qo‘shinida necha askar bo‘lgan?", "2000 kishi", "10 000 kishi", "5000 kishi", "60 000 kishi", "Askarlar soni 2000 kishi bo‘lgan.")
t.B("Muxtoriyat hukumati qancha miqdorda ichki zayom chiqarishni yo‘lga qo‘ydi?", "30 million so‘m", "10 million so‘m", "50 million so‘m", "4,4 million so‘m", "30 million so‘m miqdorida ichki zayom.")
t.B("Fitrat muxtoriyat e’lon qilingan 27-noyabr tunini qanday atadi?", "“Milliy laylatulqadrimiz”", "“Milliy bayramimiz”", "“Ozodlik tuni”", "“Turkiston tongi”", "Fitrat uni “Milliy laylatulqadrimiz” deb atadi.")
t.B("1917-yil dekabrda Toshkentda Munavvarqori rahbarligida o‘tkazilgan mitingda necha kishi qatnashdi?", "60 000 kishi", "10 000 kishi", "20 000 kishi", "2000 kishi", "“Ulug‘ Turkiston” gazetasining yozishicha, 60 000 kishi.")
t.B("Turkiston Sovetlarining qaysi syezdida Muxtoriyatni kuch bilan tugatishga qaror qilindi?", "IV favqulodda syezdida (1918-yil 19 – 26-yanvar)", "III o‘lka syezdida", "V o‘lka syezdida", "Butunrossiya II syezdida", "1918-yil 19 – 26-yanvardagi IV syezdda.")
t.B("Qaysi kundan boshlab Kichik Ergash amalda muxtoriyat hukumatining rahbariga aylandi?", "18-fevraldan", "30-yanvardan", "22-fevraldan", "15-fevraldan", "Qo‘qon mirshablar boshlig‘i Kichik Ergash 18-fevraldan rahbarga aylandi.")
t.B("Qo‘qonda bolsheviklarning “tinchlik shartnomasi” qachon imzolandi?", "1918-yil 22-fevralda", "1918-yil 20-fevralda", "1918-yil 31-yanvarda", "1918-yil 15-fevralda", "1918-yil 22-fevralda Rus-Osiyo banki binosida.")
t.B("Turkiston Muxtoriyati hukumati necha kun mavjud bo‘lgan?", "72 kun", "100 kun", "60 kun", "90 kun", "Atigi 72 kun mavjud bo‘lgan.")
t.NAT("Bolsheviklar, qizil gvardiyachilar va dashnoqlar Qo‘qonga hujum qildi.", "Muxtoriyat ag‘darildi, faqat Qo‘qonning o‘zida 3 kunda 10 000 kishi o‘ldirildi", "Muxtoriyat hukumati Toshkentga ko‘chdi", "Turkiston ASSR tuzildi", "Qo‘qon himoyachilari g‘alaba qozondi", "Muxtoriyat ag‘darildi, Qo‘qonda ommaviy qirg‘in bo‘ldi.")
t.NAT("Turkiston Muxtoriyatining tor-mor qilinishi.", "1918-yil erta bahorida Farg‘ona vodiysida qurolli istiqlolchilik harakati boshlandi", "jadidlar sovet hokimiyatini tan oldi", "Buxoro amirligi ag‘darildi", "NEP joriy etildi", "1918-yil erta bahorida avval Farg‘ona vodiysida istiqlolchilik harakati boshlandi.")
t.TF("Muxtoriyat hukumati gazetalari o‘zbek, qozoq va rus tillarida nashr qilingan.", True, "To‘g‘ri: “El bayrog‘i”, “Birlik tug‘i” va boshqalar.")
t.TF("Samarqand viloyat Sovetlari syezdi Turkiston Muxtoriyatiga qarshi chiqdi.", False, "Noto‘g‘ri: syezd Muxtoriyatga qo‘shilishga qaror qilib, Millat Majlisiga 5 vakil sayladi.")
t.MUL([("Mustafo Cho‘qay hukumatda tashqi ishlar vaziri bo‘lgan, keyinchalik Bosh vazir vazifasini bajargan.", True),
       ("Obidjon Mahmudovning bosmaxonasi hukumat ixtiyoriga o‘tgan.", True),
       ("Toshkent Sovetiga Fyodor Kolesov rahbarlik qilgan.", False)],
      "III noto‘g‘ri: Toshkent Sovetining rahbari Ivan Tobolin bo‘lgan.")
t.MATCH("Muxtoriyat hukumati a’zolarini lavozimlari bilan moslashtiring.", ["Islom Sulton Shoahmedov", "Obidjon Mahmudov", "Abdurahmon O‘rozayev", "Mustafo Cho‘qay"],
        ["oziq-ovqat vaziri", "tashqi ishlar vaziri", "Bosh vazir o‘rinbosari", "ichki ishlar vazirining o‘rinbosari"],
        "cadb", "Shoahmedov – Bosh vazir o‘rinbosari; Mahmudov – oziq-ovqat; O‘rozayev – ichki ishlar vaziri o‘rinbosari; Cho‘qay – tashqi ishlar.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["Turkiston Muxtoriyatining e’lon qilinishi", "Muxtoriyat hukumati Murojaatnomasining e’lon qilinishi", "Sovetlar IV syezdining Muxtoriyatni tugatish qarori",
       "Qo‘qonga qarshi harbiy harakatlarning boshlanishi", "“Tinchlik shartnomasi”ning imzolanishi"],
      "27-noyabr 1917 → 1-dekabr 1917 → 19 – 26-yanvar 1918 → 30-yanvar 1918 → 22-fevral 1918.")
t.MAPMATCH(CA, ['Qo‘qon', 'Toshkent', 'Samarqand'],
           ["Muxtoriyatning markazi", "60 000 kishilik miting o‘tkazilgan shahar", "viloyat Sovetlari syezdi Muxtoriyatga qo‘shilishga qaror qilgan shahar"],
           "1 – Qo‘qon (markaz); 2 – Toshkent (60 000 kishilik miting); 3 – Samarqand (viloyat syezdi).")
t.VENN("Turkiston Muxtoriyati hukumati", "Turkiston o‘lka XKS",
       [("vazirlarining aksariyati oliy ma’lumotli huquqshunoslar", 1), ("markazi – Qo‘qon", 1),
        ("faqat yevropaliklardan iborat bo‘lgan", 2), ("raisi – F.Kolesov", 2),
        ("1917-yil noyabrda tuzilgan", 3)],
       "Ikkala hukumat ham 1917-yil noyabrda tuzilgan (XKS 15 – 22-noyabr, Muxtoriyat 27 – 28-noyabr).")

# 4-§. Turkiston o‘lkasida sovet boshqaruv tizimi va iqtisodiyot
t = Topic('e10u4', 10104); TOPICS['e10u4'] = t
t.B("Lenin buyrug‘i bilan O‘rta Osiyoning favqulodda komissari qilib kim jo‘natildi?", "Pyotr Kobozev", "M.V.Frunze", "Ivan Tobolin", "Fyodor Kolesov", "Bolshevik Pyotr Kobozev.")
t.B("Turkiston Sovetlarining V o‘lka syezdi qachon bo‘lib o‘tdi?", "1918-yil 20-aprel – 1-mayda", "1918-yil 17 – 25-iyunda", "1918-yil 19 – 26-yanvarda", "1917-yil 15 – 22-noyabrda", "1918-yil 20-aprel – 1-may, Toshkentda.")
t.B("Turkiston ASSR tuzilganligini e’lon qilgan Nizom qachon qabul qilindi?", "1918-yil 30-aprelda", "1918-yil 1-mayda", "1918-yil 22-fevralda", "1918-yil 25-iyunda", "30-aprelda “Turkiston Sovet Respublikasi haqidagi Nizom” qabul qilindi.")
t.B("Turkiston ASSR qaysi davlat tarkibida tuzildi?", "RSFSR", "SSSR", "BXSR", "XXSR", "RSFSR tarkibida avtonom respublika sifatida.")
t.B("Turkiston Kommunistik partiyasi (TKP) qachon tashkiliy jihatdan rasmiylashtirildi?", "1918-yil 17 – 25-iyunda", "1918-yil 30-aprelda", "1919-yil martda", "1921-yil avgustda", "1918-yil 17 – 25-iyundagi tashkiliy o‘lka syezdida.")
t.B("TKP Markaziy Komiteti raisi kim bo‘ldi?", "Ivan Tobolin", "Turor Risqulov", "Nizomiddin Xo‘jayev", "Pyotr Kobozev", "Ivan Tobolin raisligida 7 kishilik MK saylandi.")
t.B("TKP MK tarkibiga mahalliy kommunistlardan kim kiritildi?", "Nizomiddin Xo‘jayev", "Turor Risqulov", "Yu.Aliyev", "A.Muhitdinov", "Mahalliy kommunistlardan Nizomiddin Xo‘jayev.")
t.B("RKP (b) o‘lka Musulmonlar byurosi (Musbyuro) qachon tashkil qilindi?", "1919-yil martda", "1918-yil iyunda", "1920-yil yanvarda", "1921-yil martda", "1919-yil martda TKP II konferensiyasida.")
t.B("Musulmonlar byurosining raisi kim bo‘lgan?", "Turor Risqulov", "Nizomiddin Xo‘jayev", "Munavvarqori", "Abdulla Avloniy", "Musbyuro raisi – T.Risqulov.")
t.B("T.Risqulov 1920-yil yanvarda Turkiston Sovet Respublikasini qanday nomlashni taklif qildi?", "Turk Respublikasi", "Turon Respublikasi", "O‘zbekiston Respublikasi", "Turkiston Muxtoriyati", "Turk Respublikasi deb atash va Turk partiyasini tuzishni taklif qildi.")
t.B("T.Risqulovning g‘oyalariga qaysi shaxslar keskin qarshi chiqdi?", "M.V.Frunze va V.I.Lenin", "I.Tobolin va F.Kolesov", "P.Kobozev va Ye.Perfilev", "I.Stalin va A.Kerenskiy", "Turkfront qo‘mondoni M.V.Frunze va V.I.Lenin.")
t.B("Ocharchilikka qarshi kurash Markaziy komissiyasi qachon tuzildi?", "1918-yil 20-noyabrda", "1917-yil qishida", "1921-yil martda", "1919-yil martda", "1918-yil 20-noyabrda T.Risqulov raisligida.")
t.B("1917 – 1923-yillarda Farg‘ona vodiysida ocharchilik natijasida qancha kishi o‘lib ketgan?", "1 mln kishi", "200 000 kishi", "500 000 kishi", "10 000 kishi", "Farg‘onada 1 mln, Samarqand viloyatida 200 000 kishi.")
t.B("1921 – 1922-yillarda Turkistondan Rossiyaga qancha g‘alla jo‘natilgan?", "4,4 mln pud", "1 mln pud", "30 mln pud", "600 ming pud", "4,4 mln pud g‘alla jo‘natilgan.")
t.B("Bolsheviklar 1918 – 1920-yillarda yuritgan siyosat qanday nomlangan?", "“harbiy kommunizm”", "yangi iqtisodiy siyosat", "kollektivlashtirish", "industrlashtirish", "Dastlabki davr siyosati “harbiy kommunizm” deb nomlangan.")
t.B("Qaysi syezd oziq-ovqat razvyorstkasini oziq-ovqat solig‘i bilan almashtirishga qaror qildi?", "RKP (b) X syezdi (1921-yil mart)", "TKP VI syezdi", "Turkiston ASSR Sovetlari X syezdi", "TKP II konferensiyasi", "RKP (b) X syezdi (1921-yil mart).")
t.B("Turkiston ASSRda NEPga o‘tish qaysi syezdda siyosiy jihatdan asoslab berildi?", "Turkiston Kompartiyasi VI syezdida (1921-yil avgust)", "RKP (b) X syezdida", "TKP tashkiliy syezdida", "Turkiston Sovetlarining V syezdida", "TKP VI syezdi (1921-yil avgust).")
t.B("Yer-suv islohotining birinchi bosqichi qaysi yillarda amalga oshirildi?", "1921 – 1922-yillarda", "1918 – 1920-yillarda", "1925 – 1929-yillarda", "1917 – 1923-yillarda", "1921 – 1922-yillarda TASSR va Qozog‘iston ASSRda.")
t.B("Desyatina qancha yer maydoniga teng?", "1,09 gektar", "16,38 gektar", "10 gektar", "0,5 gektar", "Desyatina – 1,09 gektarga teng.")
t.NAT("RKP (b) X syezdi oziq-ovqat razvyorstkasini oziq-ovqat solig‘i bilan almashtirdi.", "yangi iqtisodiy siyosat (NEP) boshlandi", "“harbiy kommunizm” joriy etildi", "kollektivlashtirish boshlandi", "Turkiston ASSR tuzildi", "Bu qaror bilan NEP boshlanib ketdi.")
t.NAT("T.Risqulovning Turkistonni mustaqillik tomon olib boruvchi takliflari Frunze va Lenin tomonidan rad etildi.", "1920-yil yozida Risqulov vazifasidan ozod qilinib, Moskvaga chaqirib olindi", "Turk Respublikasi tuzildi", "Turkkomissiya tugatildi", "Risqulov TKP MK raisi bo‘ldi", "Risqulov 1920-yil yozida Moskvaga ishga chaqirib olindi.")
t.TF("Yer-suv islohotining birinchi bosqichida yer jamg‘armasiga qo‘shilgan 1722626 desyatina yerning barchasi mahalliy aholiga berildi.", False, "Noto‘g‘ri: mahalliy aholiga faqat 600000 desyatina ajratildi.")
t.TF("“Harbiy kommunizm” davrida bozor yo‘qotilib, pul muomalasi natura bilan almashtirildi.", True, "To‘g‘ri.")
t.MUL([("Musulmonlar byurosi faoliyatida Munavvarqori va Abdulla Avloniy ham ishtirok etgan.", True),
       ("Yer-suv islohoti dastlab Yettisuv, Sirdaryo, Farg‘ona, Samarqand viloyatlarida o‘tkazildi.", True),
       ("NEP dehqonlar erkinligini to‘liq cheklashga qaratilgan edi.", False)],
      "III noto‘g‘ri: NEP ishlab chiqaruvchiga, avvalo dehqonlarga bir qadar erkinlik berishdan iborat edi.")
t.CHR("Voqealarni xronologik tartibda joylashtiring.",
      ["Turkiston ASSR tuzilganligining e’lon qilinishi", "Turkiston Kommunistik partiyasining rasmiylashtirilishi", "Ocharchilikka qarshi kurash Markaziy komissiyasining tuzilishi",
       "Musulmonlar byurosining tashkil qilinishi", "RKP (b) X syezdi"],
      "1918-yil 30-aprel → 1918-yil iyun → 1918-yil 20-noyabr → 1919-yil mart → 1921-yil mart.")
t.MAPN(CA, ['Samarqand', 'Farg‘ona vodiysi', 'Toshkent', 'Xiva'], "1917 – 1923-yillarda ocharchilik natijasida 1 mln kishi o‘lib ketgan hudud qaysi raqam bilan belgilangan?",
       "Farg‘ona vodiysida 1 mln, Samarqand viloyatida 200 000 kishi o‘lgan.", ask_idx=1)
t.VENN("“Harbiy kommunizm”", "Yangi iqtisodiy siyosat (NEP)",
       [("oziq-ovqat razvyorstkasi", 1), ("mehnat militarizatsiyasi", 1),
        ("oziq-ovqat solig‘i", 2), ("dehqonlarga bir qadar erkinlik berish", 2),
        ("bolsheviklar tomonidan joriy qilingan iqtisodiy siyosat", 3)],
       "Harbiy kommunizm – razvyorstka, majburiy mehnat; NEP – oziq-ovqat solig‘i, erkinlik; ikkalasi bolsheviklar siyosati.")
