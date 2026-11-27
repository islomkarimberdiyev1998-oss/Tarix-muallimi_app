from qlib import Topic
TOPICS = {}
CA = 'ca'

# 14 Yer-suv siyosati
t = Topic('e9u14', 9014); TOPICS['e9u14'] = t
t.B("1886-yilgi «Nizom»ning qaysi bo‘limida an’anaviy yer egaligi munosabatlari o‘zgartirildi?", "«Turkiston o‘lkasining yer tuzilishi»", "«Shahar nizomi»", "«Harbiy-xalq boshqaruvi»", "«Sud tuzilishi»", "«Turkiston o‘lkasining yer tuzilishi» bo‘limida.")
t.B("1886-yilgi Nizomga ko‘ra Turkiston yerlari, o‘rmonlari va yerosti boyliklari kimning mulki deb e’lon qilindi?", "davlat mulki", "xususiy mulk", "vaqf mulki", "jamoa mulki", "Davlat (Rossiya imperiyasi) mulki.")
t.B("Nizom bo‘yicha o‘lkada qanday yer egaligi tugatildi?", "yirik yer egaligi", "vaqf yer egaligi", "dehqon yer egaligi", "jamoa yer egaligi", "Yirik yer egaligi tugatildi.")
t.B("Yangi vaqf hujjatlari kimning roziligi bilan tasdiqlangan?", "general-gubernator", "qozikalon", "shayxulislom", "amir", "Faqat general-gubernator roziligi bilan.")
t.B("Vaqf hujjatlarini taftish qilish huquqi kimga o‘tkazildi?", "viloyat ma’muriyatiga", "masjid imomlariga", "qozilarga", "shahar dumasiga", "Viloyat ma’muriyati ixtiyoriga.")
t.B("Ko‘chib kelganlar necha yil soliqlardan to‘liq ozod etilgan?", "5 yil", "10 yil", "1 yil", "15 yil", "5 yil ozod, keyingi 5 yil soliqning yarmini to‘lagan.")
t.B("Rossiyadan kelgan dehqonlarning birinchi manzilgohi qachon va qayerda paydo bo‘lgan?", "1875-yilda Avliyootada", "1867-yilda Toshkentda", "1886-yilda Samarqandda", "1892-yilda Andijonda", "1875-yilda Avliyootada.")
t.B("1875–1890-yillarda Turkistonga necha oila ko‘chib kelgan?", "1300 oila", "19 oila", "25 ming oila", "400 ming oila", "1300 oila; 19 ta rus qishlog‘i tashkil topdi.")
t.B("1891–1892-yillarda ko‘chib kelganlarning nechta manzilgohi paydo bo‘lgan?", "25 ta", "19 ta", "100 ta", "5 ta", "25 ta manzilgoh.")
t.B("Toshkentni ikki qismga ajratgan chegara nima bo‘lgan?", "Bo‘zsuv anhori", "Chirchiq daryosi", "Kaykovus arig‘i", "Ankhor ko‘prigi", "Bo‘zsuv anhori.")
t.B("O‘lkadagi yirik shaharlarning yangi qismida kimlar yashagan?", "ma’muriyat, harbiy qismlar va ko‘chirib keltirilganlar", "mahalliy aholi", "hunarmandlar", "ulamolar", "Yangi qismda ma’muriyat, harbiylar va ko‘chirilganlar.")
t.B("Turkistonda qaysi hududlardagidek mustamlakachilik siyosati olib borilgan?", "Sibir va Kavkaz", "Hindiston va Misr", "Polsha va Finlyandiya", "Alyaska", "Sibir va Kavkaz hududlaridagidek.")
t.NAT("Vaqf mulklarini nazorat qilish mustamlakachi hukumat vakillari qo‘liga o‘tdi.", "masjid va maktablarning moddiy ahvoli yomonlashdi", "madrasalar ko‘paydi", "vaqf daromadlari oshdi", "ulamolar imtiyoz oldi", "Bu bilan din peshvolari va diniy muassasalarga zarba berildi.")
t.NAT("1892-yildan o‘zboshimchalik bilan ko‘chib kelganlarga ham imtiyozlardan foydalanish huquqi berildi.", "o‘lkaga ko‘chib keluvchilar soni yanada ko‘paydi", "ko‘chish to‘xtadi", "ko‘chib kelganlar qaytib ketdi", "mahalliy aholiga yer berildi", "Ko‘chib keluvchilar soni yanada oshdi.")
t.NAT("Ko‘chirib keltirilganlarga unumdor yerlar berildi.", "mahalliy aholining jiddiy noroziligi yuzaga keldi", "mahalliy aholi boyidi", "yer solig‘i bekor qilindi", "vaqf yerlari ko‘paydi", "Bu mahalliy aholining noroziligiga sabab bo‘ldi.")
t.TF("Masjid tasarrufidan tashqaridagi xususiy shaxs ixtiyoridagi yerlar ham davlat solig‘iga tortiladigan bo‘ldi.", True, "To‘g‘ri.")
t.TF("Ko‘chib kelganlar asosan shahar aholisi bo‘lgan.", False, "Noto‘g‘ri: ular asosan qishloq aholisi bo‘lgan.")
t.MUL([("Ko‘chib kelganlar mablag‘, turar joy, yer va kreditlar bilan ta’minlangan.", True),
       ("O‘lka ma’muriyati ko‘chib kelganlar uchun maktab va cherkovlar qurishga mablag‘ ajratgan.", True),
       ("Harbiy xizmatchilarga Turkistonda yashab qolish taqiqlangan.", False)],
      "III noto‘g‘ri: ular yashab qolishlari va tomorqa yer olishlari mumkin bo‘lgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Avliyootada birinchi rus manzilgohi", "1886-yilgi Nizom: yerlar davlat mulki", "25 ta yangi manzilgoh paydo bo‘ldi", "o‘zboshimcha ko‘chib kelganlarga imtiyoz e’lon qilindi"],
      "1875 → 1886 → 1891–1892 → 1892-yildan.")
t.MAPN(CA, ['Buxoro', 'Avliyoota', 'Samarqand', 'Xiva'], "Qaysi raqam bilan 1875-yilda Rossiyadan kelgan dehqonlarning birinchi manzilgohi paydo bo‘lgan shahar belgilangan?",
       "2 – Avliyoota.", ask_idx=1)
t.VENN("Shaharning yangi qismi", "Shaharning eski qismi",
       [("ma’muriyat va harbiy qismlar joylashgan", 1), ("ko‘chirib keltirilganlar yashagan", 1),
        ("mahalliy aholi vakillari yashagan", 2), ("Toshkentda duma a’zolarining 1/3 qismi shu qismdan saylangan", 2),
        ("Toshkentda Bo‘zsuv anhori bilan ajralgan", 3)],
       "Yangi qism — ma’muriyat va ko‘chirilganlar; eski qism — mahalliy aholi; Toshkentda ular Bo‘zsuv bilan ajralgan.")

# 15 Sud tizimi va harbiy politsiya tartiboti
t = Topic('e9u15', 9015); TOPICS['e9u15'] = t
t.B("Xonlik davrida qozi qaroridan norozi bo‘lganlar kimga murojaat qilgan?", "qozikalonga", "general-gubernatorga", "biyga", "mirshabboshiga", "Qozikalonga.")
t.B("Podsho hukumati dastlab sud tizimidagi qaysi lavozimni tugatgan?", "qozikalon", "qozi", "biy", "mirob", "Qozikalon lavozimi tugatilib, qozilar huquqi tenglashtirildi.")
t.B("Ko‘chmanchi aholining urf-odatlariga asoslangan sud qanday atalgan?", "biy sudi", "qozi sudi", "mirovoy sud", "okrug sudi", "Biy sudi — qabila urf-odatlariga tayangan.")
t.B("Qozi va biylar necha yil muddatga saylangan?", "uch yil", "bir yil", "besh yil", "umrbod", "Uch yil muddatga.")
t.B("Toshkentda mahkama qachon joriy qilingan?", "1866-yilda", "1867-yilda", "1886-yilda", "1898-yilda", "1866-yilda; tarkibida qozi va 7 nafar a’lam.")
t.B("Qozi sudlari da’vo hajmi qanchadan oshmaydigan ishlarni ko‘rgan?", "100 rubl", "1000 rubl", "10 rubl", "500 rubl", "100 rubldan oshmaydigan ishlar.")
t.B("Xalq sudyalari qurultoyi da’vo hajmi qanchagacha bo‘lgan ishlarni hal qilgan?", "1000 rubl", "100 rubl", "10 000 rubl", "50 rubl", "1000 rubldan oshmaydigan ishlar — ikkinchi bosqich.")
t.B("Toshkent shahrida nechta qozi bo‘lgan?", "to‘rtta", "ikkita", "bitta", "yettita", "To‘rt dahaning har birida bittadan.")
t.B("O‘lkaning bosh prokurori va oliy sudyasi vazifasini kim bajargan?", "general-gubernator", "qozikalon", "harbiy vazir", "hukumat senati", "General-gubernator.")
t.B("1886-yilgi Nizomga ko‘ra uyezd sudlari o‘rniga qanday sudlar tuzildi?", "uchastka mirovoy sudlari", "okrug sudlari", "qozi sudlari", "biy sudlari", "Uchastka mirovoy sudyalari.")
t.B("1898-yilda viloyat sudlari o‘rniga nimalar tuzildi?", "okrug sudlari va Toshkent sud palatasi", "mirovoy sudlar", "qozi sudlari", "harbiy-sud komissiyalari", "Okrug sudlari va Toshkent sud palatasi.")
t.B("Toshkent sud palatasi faqat kimga bo‘ysungan?", "hukumat senatiga", "general-gubernatorga", "harbiy vazirga", "viloyat sudiga", "Imperiyaning oliy sudi — hukumat senatiga.")
t.B("«Davlat tartiboti va jamoat osoyishtaligini qo‘riqlash» Nizomi qachon e’lon qilingan?", "1881-yilda", "1886-yilda", "1892-yilda", "1898-yilda", "1881-yilda.")
t.B("Turkiston qaysi yillarda «kuchaytirilgan» va «favqulodda qo‘riqlov» holatida bo‘lgan?", "1892–1916-yillarda", "1865–1886-yillarda", "1881–1892-yillarda", "1898–1905-yillarda", "1892-yildan 1916-yilga qadar.")
t.B("Uyezd boshliqlari har qanday odamni necha kunga qamoqqa olishi mumkin edi?", "yetti kunga", "bir kunga", "o‘ttiz kunga", "uch kunga", "Yetti kunga.")
t.B("Uyezd politsiyasi boshlig‘i qanday atalgan?", "ispravnik", "pristav", "komendant", "zemstvo", "Ispravnik.")
t.B("1882–1884-yillarda o‘lkani tekshirgan imperatorning maxfiy maslahatchisi kim?", "F. Girs", "K. Palen", "S. Duxovskoy", "M. Skobelev", "F. Girs.")
t.NAT("Qozi va biy saylovlarida nayranglar, poraxo‘rliklar avj oldi.", "qozilik va biylik serdaromad mansabga aylandi", "sudlar adolatli bo‘ldi", "saylovlar bekor qilindi", "qozilar soni kamaydi", "Saylangan qozilar xarajatlarini poralar hisobiga qaytarishga harakat qilgan.")
t.NAT("Podsho hukumati mahalliy aholi zamonaviy qurollardan unga qarshi foydalanishidan cho‘chidi.", "mahalliy aholi armiyada xizmat qilishdan mahrum etildi", "barcha erkaklar armiyaga chaqirildi", "mahalliy aholiga qurol tarqatildi", "Turkiston harbiy okrugi tugatildi", "F. Girs ham aholini armiyaga chaqirmaslikni yoqlagan.")
t.TF("Podsho hukumati qozi va biy sudlarini dastlab butunlay tugatmasdan saqlab qoldi.", True, "To‘g‘ri.")
t.TF("Qozi sudlari shariat qoidalari asosida emas, imperiya qonunlari asosida ish ko‘rgan.", False, "Noto‘g‘ri: qozi sudlari shariat qoidalari asosida ish ko‘rgan.")
t.MUL([("Qozilar tomonlardan pul, sovg‘a va xizmatlar qabul qilmasligi lozim edi.", True),
       ("Qozi sud majlisidan oldin tomonlarga kelishib olishni taklif qilgan.", True),
       ("Har bir qozi qat’iy belgilangan uchastkaga ega bo‘lgan.", False)],
      "III noto‘g‘ri: qozilar qat’iy uchastkaga ega bo‘lmagan, da’vogar o‘zi ishongan qoziga borgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Toshkentda mahkama joriy qilindi", "1867-yilgi «Nizom» loyihasi", "Qo‘riqlash chora-tadbirlari to‘g‘risidagi Nizom", "Uchastka mirovoy sudlari tuzildi", "Okrug sudlari va Toshkent sud palatasi tuzildi"],
      "1866 → 1867 → 1881 → 1886 → 1898.")
t.VENN("Qozi sudi", "Biy sudi",
       [("shariat qoidalari asosida ish ko‘rgan", 1), ("o‘troq aholi uchun", 1),
        ("qabila urf-odatlariga tayangan", 2), ("ko‘chmanchi aholi uchun", 2),
        ("uch yil muddatga saylangan", 3)],
       "Qozi — shariat, o‘troqlar; biy — urf-odat, ko‘chmanchilar; ikkalasi 3 yilga saylangan.")
