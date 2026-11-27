from qlib import Topic, PLACES, REG
TOPICS = {}
EU = 'europe'

# 6 Vizantiya
t = Topic('y7j6', 7006); TOPICS['y7j6'] = t
t.B("Vizantiya taxminan qancha vaqt Yevropaning eng qudratli davlati bo‘lib qolgan?", "deyarli ming yil", "yuz yil", "ikki asr", "besh yuz yil", "Deyarli ming yil davomida.")
t.B("395-yilda Rim imperiyasini bo‘lib olganlar kimning o‘g‘illari edi?", "imperator Feodosiyning", "Yustinianning", "Konstantinning", "Irakliyning", "Imperator Feodosiyning o‘g‘illari.")
t.B("Sharqiy Rim imperiyasining poytaxti qaysi shahar bo‘lgan?", "Konstantinopol", "Rim", "Aleksandriya", "Antioxiya", "Konstantinopol.")
t.B("Imperiyaning boy hududlari Feodosiyning qaysi o‘g‘liga tekkan?", "Arkadiyga", "Yustinga", "Gonoriyga", "Irakliyga", "Katta o‘g‘il Arkadiyga.")
t.B("Vizantiyaliklar o‘zlarini qanday atagan?", "romeylar – rimliklar", "yunonlar", "vizantlar", "elinlar", "O‘zlarini romeylar – rimliklar deb nomlagan.")
t.B("Vizantiyada vaqt o‘tib lotin tili o‘rnini qaysi til egallagan?", "yunon tili", "arab tili", "slavyan tili", "arman tili", "Yunon tili.")
t.B("Konstantinopolni ramziy ma’noda qanday atashgan?", "«oltin ko‘prik»", "«boqiy shahar»", "«dunyo mo‘jizasi»", "«Osmonosti shahri»", "Osiyo va Yevropani bog‘lovchi «oltin ko‘prik».")
t.B("Asrlar davomida ishonchli xalqaro pul hisoblangan Vizantiya oltin tangasi qanday atalgan?", "numisma", "dinor", "dirham", "solid", "Numisma.")
t.B("Vizantiya imperatori qanday unvon bilan atalgan?", "vasilevs", "konung", "xalifa", "syogun", "Vasilevs (yunoncha – «podsho»).")
t.B("Vizantiya o‘z qudrati cho‘qqisiga qaysi imperator davrida erishgan?", "Yustinian I", "Feodosiy", "Irakliy I", "Arkadiy", "Yustinian I (527–565).")
t.B("Yustinian I davrida Konstantinopolda qaysi ibodatxona qurilgan?", "Ayo Sofiya", "San-Vitale", "Avliyo Pyotr", "Notr-Dam", "Ayo Sofiya (Avliyo Sofiya).")
t.B("Ravennada Yustinian davrida qurilgan ibodatxona qaysi?", "San-Vitale", "Ayo Sofiya", "Avliyo Sofiya (Kiyev)", "Avliyo Pyotr", "San-Vitale.")
t.B("Yustinianning orzusi nima edi?", "Rim imperiyasining 395-yildan oldingi chegaralarini tiklash", "Eronni bosib olish", "xristianlikni taqiqlash", "poytaxtni Rimga ko‘chirish", "395-yilgacha bo‘lgan chegaralarni tiklash.")
t.B("Irakliy I qaysi Eron hukmdori qo‘shinini mag‘lub etgan?", "Xusrav II", "Shopur I", "Doro I", "Kir II", "Xusrav II qo‘shinini.")
t.B("Vizantiya saroyida qaysi rangni faqat imperator qo‘llashi mumkin bo‘lgan?", "to‘q qizil", "oltin", "oq", "yashil", "To‘q qizil rangni.")
t.NAT("Yustinian g‘arbga yurishlar qildi, sharqda Eron bilan urushdi.", "xazina bo‘shab, aholi xonavayron bo‘ldi, qo‘shin holdan toydi", "imperiya boyib ketdi", "Eron Vizantiyaga qo‘shildi", "qullik butunlay yo‘qoldi", "Xazina bo‘shab qoldi.")
t.NAT("Irakliy I va Eron o‘rtasidagi urush har ikki tomonni zaiflashtirdi.", "arablar Misr, Suriya, Falastinni bosib oldi", "Vizantiya Eronni egalladi", "Bulg‘oriya parchalandi", "Vizantiya kuchaydi", "Bu Bulg‘oriya podsholigi vujudga kelishiga ham imkon berdi.")
t.NAT("Imperiyaning ahvoli og‘irlashgani sari «diplomatiya san’ati» muhim bo‘ldi.", "zamonaviy diplomatiya asoslariga Vizantiya qoidalari kirdi", "Vizantiya urushlardan butunlay voz kechdi", "diplomatiya taqiqlandi", "imperator unvoni bekor qilindi", "Vizantiya diplomatiyasi qoidalari zamonaviy diplomatiyaga kirdi.")
t.NAT("Yustinian bosib olingan o‘lkalarda qullikni tiklashga intildi.", "mahalliy aholi uni qo‘llab-quvvatlamadi", "aholi uni xursand kutib oldi", "qullik butun Yevropaga yoyildi", "Italiya mustaqil bo‘ldi", "Mahalliy aholi qo‘llab-quvvatlamadi.")
t.TF("Vizantiya aholisining katta qismini soliq to‘laydigan erkin dehqonlar tashkil etgan.", True, "To‘g‘ri.")
t.TF("Vizantiyada imperator unvonining merosiyligi to‘liq kafolatlangan bo‘lgan.", False, "Noto‘g‘ri: merosiylik to‘liq kafolatlanmagan, imperatorlar ag‘darilgan va qatl etilgan.")
t.TF4([("Yustinian kambag‘al dehqon oilasida tug‘ilgan.", True), ("Yustinianning amakisi Yustin imperatorlik taxtini egallagan.", True),
       ("Yustinian buyrug‘i bilan qadimgi Rim qonunlari majmui yaratilgan.", True), ("Yustinian vafotidan so‘ng Vizantiya hududlari kengayib borgan.", False)],
      "4-noto‘g‘ri: hududlar sekin-asta qisqarib borgan.")
t.MUL([("VI asrda Aleksandriya, Antioxiya, Edessa yirik savdo markazlari bo‘lgan.", True),
       ("Vizantiyada qulchilik butunlay yo‘q qilingan.", False),
       ("Konstantinopol Yevropaning eng yirik shahriga aylangan.", True)],
      "II noto‘g‘ri: Vizantiyada qulchilik saqlanib qolgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Rim imperiyasi ikkiga bo‘lindi", "Yustinian I taxtga o‘tirdi", "Yustinian I vafot etdi"], "395 → 527 → 565.")
t.MATCH("Shaharlarni ularga oid ma’lumot bilan moslashtiring.", ["Konstantinopol", "Ravenna", "Aleksandriya", "Rim"],
        ["Ayo Sofiya ibodatxonasi", "San-Vitale ibodatxonasi", "muhtasham binolar va favvoralar bilan bezangan Misr shahri", "G‘arbiy Rim imperiyasi poytaxti", "Vizantiya oltin tangasi zarb etilgan Eron shahri"], 'abcd',
        "Konstantinopol – Ayo Sofiya; Ravenna – San-Vitale; Aleksandriya – Misr shahri; Rim – G‘arbiy Rim poytaxti.")
t.VENN("G‘arbiy Rim imperiyasi", "Sharqiy Rim imperiyasi",
       [("poytaxti Rim", 1), ("476-yilda so‘nggi imperatori ag‘darilgan", 1),
        ("poytaxti Konstantinopol", 2), ("Yustinian davrida qudrat cho‘qqisiga chiqqan", 2),
        ("395-yildagi bo‘linish natijasida vujudga kelgan", 3)],
       "G‘arbiy – Rim, 476; Sharqiy – Konstantinopol, Yustinian; ikkalasi 395-yilda vujudga kelgan.")
t.MAPMATCH('medit', ['Konstantinopol', 'Ravenna', 'Aleksandriya (Misr)', 'Antioxiya'],
           ["«oltin ko‘prik» deb atalgan Vizantiya poytaxti", "San-Vitale ibodatxonasi qurilgan Italiya shahri", "muhtasham binolari bilan mashhur Misrdagi markaz", "Edessa bilan birga gullab-yashnagan Old Osiyo markazi"],
           "1 – Konstantinopol; 2 – Ravenna; 3 – Aleksandriya; 4 – Antioxiya.")

# 7 Slavyan davlatlari
t = Topic('y7j7', 7007); TOPICS['y7j7'] = t
t.B("Slavyan davlatlari qaysi asrlarda tashkil topgan?", "VII–X asrlarda", "IV–VI asrlarda", "XI–XIII asrlarda", "II–III asrlarda", "VII–X asrlarda.")
t.B("«Slavyan (sloven)» so‘zi qanday ma’noni anglatadi?", "«tushunarli bir xil tilda so‘zlashuvchilar»", "«o‘rmon odamlari»", "«dehqonlar»", "«shimolliklar»", "«Tushunarli bir xil tilda so‘zlashuvchilar».")
t.B("Qaysi xalq g‘arbiy slavyanlarga kiradi?", "chexlar", "serblar", "bolgarlar", "xorvatlar", "Polyaklar, chexlar, slovaklar.")
t.B("Qaysi xalq janubiy slavyanlarga kiradi?", "serblar", "polyaklar", "slovaklar", "chexlar", "Bolgarlar, serblar, xorvatlar va boshqalar.")
t.B("Buyuk Moraviya davlati qachon paydo bo‘lgan?", "IX asr boshlarida", "VII asrda", "X asr o‘rtalarida", "XI asrda", "IX asr boshlarida hozirgi Chexiya o‘rnida.")
t.B("Kirill va Mefodiy Moraviyaga qachon kelgan?", "863-yilda", "681-yilda", "988-yilda", "966-yilda", "863-yili.")
t.B("Yunon yozuvi asosidagi slavyan yozuvi qanday nom olgan?", "kirill yozuvi", "lotin yozuvi", "glagol yozuvi", "runa yozuvi", "«Kirill yozuvi».")
t.B("Ilk slavyan davlati – Bulg‘or podsholigiga kim asos solgan?", "podsho Asparux", "podsho Simeon", "Meshko I", "Oleg", "681-yili podsho Asparux.")
t.B("Bolgariya eng kuchaygan davrdagi podsho kim?", "Simeon", "Asparux", "Boleslav I", "Svyatoslav", "Podsho Simeon (893–927).")
t.B("Polsha knyazi Meshko I xristianlikni qachon qabul qilgan?", "966-yilda", "988-yilda", "863-yilda", "1000-yilda", "966-yili nemis yepiskoplaridan.")
t.B("Polshada qirollik tojiga qaysi hukmdor davrida erishilgan?", "Boleslav I Jasur", "Meshko I", "Simeon", "Yaroslav", "Boleslav I Jasur.")
t.B("Qaysi mamlakatda kirill alifbosi yetakchilik qilgan?", "Serbiya", "Polsha", "Chexiya", "Xorvatiya", "Bolgariya, Serbiya va Kiyev Rusida.")
t.B("Oleg Kiyevni qachon egallab, Kiyev Rusiga asos solgan?", "882-yilda", "862-yilda", "988-yilda", "1019-yilda", "882-yili.")
t.B("Rusda xristianlik qachon qabul qilingan?", "988-yilda", "882-yilda", "966-yilda", "1054-yilda", "988-yili knyaz Vladimir davrida.")
t.B("Yaroslav Donishmand Volga bo‘yida qaysi shaharga asos solgan?", "Yaroslavl", "Novgorod", "Kiyev", "Polosk", "Yaroslavl.")
t.B("Yaroslav davrida tuzilgan qonunlar qanday atalgan?", "«Rus haqiqati»", "«Sali haqiqati»", "«Alfred haqiqati»", "«Anglosakson solnomasi»", "«Rus haqiqati».")
t.B("Ruslar qipchoqlarni qanday atashgan?", "poloveslar", "pecheneglar", "xazarlar", "varyaglar", "Poloveslar.")
t.B("Qipchoqlarga qarshi urush harakatlarini ularning yerlariga ko‘chirgan knyaz kim?", "Vladimir Monomax", "Yaroslav", "Oleg", "Igor", "Vladimir Monomax (1113–1125).")
t.NAT("Kirill va Mefodiy slavyan alifbosini yaratib, Injilni tarjima qildi.", "slavyan madaniyati yuksaldi, kirill yozuvi Bolgariya, Serbiya va Rusga yoyildi", "slavyanlar lotin yozuviga o‘tdi", "Moraviya Vizantiyaga qo‘shildi", "Injil taqiqlandi", "Slavyan madaniyatining yuksalishiga ulkan hissa qo‘shildi.")
t.NAT("Bulg‘orlar son jihatdan kam bo‘lib, slavyanlar orasida yashadi.", "ular sekin-asta slavyanlar bilan aralashib ketdi", "slavyanlar turkiy tilga o‘tdi", "Bulg‘oriya Volga bo‘yiga qaytdi", "bulg‘orlar islomni qabul qildi", "Bulg‘orlar slavyanlashdi.")
t.NAT("Genrix IV papaga qarshi kurashdagi yordami uchun chex knyaziga qirollik tojini in’om etdi.", "Chexiyada qirol hokimiyati kuchayib, XIII asrda u Yevropaning kuchli davlatlaridan biriga aylandi", "Chexiya parchalandi", "Chexiya Polshaga qo‘shildi", "Chexiya kirill yozuviga o‘tdi", "Qirol hokimiyati kuchaydi.")
t.NAT("Vladimir Monomax vafot etdi.", "qarama-qarshiliklar qayta boshlanib, knyazlik siyosiy tarqoqlikka yuz tutdi", "Kiyev Rusi markazlashdi", "qipchoqlar butunlay yo‘qoldi", "Rus Vizantiyaga qo‘shildi", "Knyazlik siyosiy tarqoqlikka yuz tutdi.")
t.TF("Polsha cherkovi 1000-yilda arxiyepiskoplik rutbasini olib, nemis cherkovidan mustaqil bo‘lgan.", True, "To‘g‘ri.")
t.TF("Polsha, Chexiya va Xorvatiyada kirill alifbosi qaror topgan.", False, "Noto‘g‘ri: ularda Rim ta’siri va lotin yozuvi qaror topgan.")
t.TF4([("Ryuriklar dastlab Novgorod, Beloozero va Izborskda knyazlik qilgan.", True), ("Yaroslav pecheneglarni uzil-kesil mag‘lub etgan.", True),
       ("Yaroslav Kiyevda Ayo Sofiya ibodatxonasini qurdirgan va u saqlanmagan.", False), ("Novgorod va Kiyevda yilnomalar tuzila boshlangan.", True)],
      "3-noto‘g‘ri: Kiyevdagi Avliyo Sofiya ibodatxonasi hozirga qadar yaxshi saqlangan.")
t.MUL([("Slavyanlarning asosiy mashg‘uloti dehqonchilik bo‘lgan.", True),
       ("XI asr boshlarida Bolgariyani Vizantiya istilo qilgan.", True),
       ("Chexiya XI asrda Vizantiya tarkibiga kiritilgan.", False)],
      "III noto‘g‘ri: Chexiya Muqaddas Rim imperiyasi tarkibiga kiritilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Bulg‘or podsholigi tuzildi", "Kirill va Mefodiy Moraviyaga keldi", "Oleg Kiyevni egalladi", "Meshko I xristianlikni qabul qildi", "Rusda xristianlik qabul qilindi", "Yaroslav hukmronligi boshlandi"],
      "681 → 863 → 882 → 966 → 988 → 1019.")
t.VENN("Polsha", "Kiyev Rusi",
       [("Meshko I davrida xristianlik qabul qilingan", 1), ("lotin yozuvi ustun", 1),
        ("Oleg asos solgan", 2), ("kirill alifbosi yetakchilik qilgan", 2),
        ("slavyan davlati", 3)],
       "Polsha – Meshko, lotin; Rus – Oleg, kirill; ikkalasi slavyan davlati.")
t.MAPMATCH(EU, ['Kiyev', 'Novgorod', 'Moraviya', 'Bolgariya'],
           ["882-yilda Oleg egallagan va davlatga nom bergan shahar", "Ryuriklar dastlab knyazlik qilgan shaharlardan biri", "863-yilda Kirill va Mefodiy kelgan davlat", "681-yilda Asparux asos solgan ilk slavyan davlati hududi"],
           "1 – Kiyev; 2 – Novgorod; 3 – Moraviya; 4 – Bolgariya.")
