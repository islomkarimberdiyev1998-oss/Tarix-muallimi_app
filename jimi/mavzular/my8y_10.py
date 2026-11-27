from qlib import Topic, PLACES, REG
TOPICS = {}

# 25 Osiyo, Afrika va Amerika xalqlari madaniyati
t = Topic('y8j25', 8025); TOPICS['y8j25'] = t
t.B("Rivojlangan o‘rta asrlarda Osiyoda eng taraqqiy etgan fanlardan biri qaysi bo‘lgan?", "astronomiya", "alkimyo", "ilohiyot", "huquq", "Astronomiya.")
t.B("XIII–XV asrlarda qaysi shaharlarda rasadxonalar faoliyat yuritgan?", "Marog‘a, Samarqand, Istanbul", "Bag‘dod, Qohira, Dehli", "Pekin, Kioto, Seul", "Buxoro, Xiva, Termiz", "Marog‘a, Samarqand, Istanbul.")
t.B("Marog‘a astronomiya maktabiga kim boshchilik qilgan?", "Nosiriddin at-Tusiy", "Qutb Sheroziy", "Mirzo Ulug‘bek", "Ibn Battuta", "Nosiriddin at-Tusiy.")
t.B("Marog‘a maktabi vakillari kimning nazariyasini inkor etgan?", "Ptolemey", "Kopernik", "Arastu", "Aflotun", "Ptolemey nazariyasini.")
t.B("Marog‘a olimlari Yer aylanishini Kopernikdan necha yil oldin isbotlagan?", "300 yil", "100 yil", "50 yil", "500 yil", "300 yil oldin.")
t.B("Yerning o‘z o‘qi atrofida aylanishini isbotlagan kashfiyot fanda qanday nom oldi?", "«Marog‘a inqilobi»", "«Samarqand inqilobi»", "«Kopernik inqilobi»", "«Ptolemey tizimi»", "«Marog‘a inqilobi».")
t.B("XIV asrning birinchi yarmida Afrikadan Xitoygacha sayohat qilgan arab sayyohi kim?", "Ibn Battuta", "Marko Polo", "Chjan Xe", "Ibn Sino", "Ibn Battuta.")
t.B("Samarqandda rasadxona, madrasa va kutubxonali akademiyani kim tashkil etgan?", "Mirzo Ulug‘bek", "Amir Temur", "Nosiriddin at-Tusiy", "Sejong", "Mirzo Ulug‘bek.")
t.B("Koreya qirollik akademiyasi kimning hukmronligi davrida tashkil etilgan?", "Sejong", "Van Gon", "Asikaga Yoshimitsu", "Xubilay", "XV asrda Sejong davrida.")
t.B("Koreys fonetik alifbosi necha harfdan iborat bo‘lgan?", "yigirma sakkiz", "o‘ttiz uch", "yigirma olti", "o‘n to‘qqiz", "28 harf.")
t.B("Oltin pavilyonni kim qurgan?", "syogun Asikaga Yoshimitsu", "imperator Sejong", "Xubilayxon", "Minamoto Yoritomo", "1397-yilda Asikaga Yoshimitsu.")
t.B("Oltin pavilyonning uchinchi qavati nima uchun mo‘ljallangan?", "ibodat qilish uchun", "yashash uchun", "musiqa va she’riyat uchun", "qurol saqlash uchun", "Ibodat uchun.")
t.B("Qutb minor qaysi shaharda joylashgan?", "Dehli", "Samarqand", "Pekin", "Halab", "Dehlida, XIII asr.")
t.B("Xo‘ja Ahmad Yassaviy maqbarasi qayerda qurilgan?", "Turkistonda", "Samarqandda", "Buxoroda", "Istanbulda", "Turkistonda, XV asr.")
t.B("Buyuk Xitoy devorining bugungacha saqlangan qismlari asosan qaysi sulola davrida qurilgan?", "Min", "Yuan", "Tan", "Sun", "Min sulolasi (1368–1644).")
t.B("Tombuktudagi qaysi madrasa ayniqsa mashhur bo‘lgan?", "Sankore", "Al-Firdavs", "Ulug‘bek", "Jenne", "Sankore madrasasi.")
t.B("Qaysi shahar madrasasi tibbiyot ilmining markazi bo‘lgan?", "Jenne", "Gao", "Niara", "Kumbi Sale", "Jenne madrasasi.")
t.B("Madrasa bitiruvchilari nima bilan taqdirlangan?", "salla bilan", "qilich bilan", "oltin bilan", "uzuk bilan", "Bilimdonlik ramzi – salla.")
t.B("Songay hukmdori Buyuk Askiya qaysi yo‘ldan borgan?", "islom dinini mustahkamlash", "xristianlikni yoyish", "Quyosh xudosiga sig‘inish", "madrasalarni yopish", "Islomni mustahkamlagan.")
t.B("G‘arbiy Afrikada san’atning eng rivojlangan sohasi qaysi bo‘lgan?", "haykaltaroshlik", "rangtasvir", "teatr", "me’morchilik", "Haykaltaroshlik.")
t.B("Inklar qaysi xudoga sig‘ingan?", "Quyosh xudosi", "yomg‘ir xudosi", "urush xudosi", "Oy xudosi", "Quyosh xudosiga.")
t.B("Inklar yozuv o‘rnida nimadan foydalangan?", "kipu – tugunli xatlar", "ierogliflar", "mixxat", "lotin alifbosi", "Kipu.")
t.B("Atsteklar tabobatda nechtadan ortiq o‘simlikni dori sifatida ishlatgan?", "100 dan", "10 dan", "1000 dan", "50 dan", "100 dan ortiq.")
t.NAT("Islom olamida xalqlar umumiy tillarga ega edi.", "olimlar bir-birini tushunib, fanlarni birgalikda rivojlantirdi", "olimlar o‘zaro aloqani uzdi", "fanlar tanazzulga uchradi", "faqat ilohiyot o‘qitildi", "Ilmiy hamkorlik rivojlandi.")
t.NAT("Islom mamlakatlarida astronomiya rivojlandi.", "geografiya fani taraqqiy etib, aniq xaritalar tuzildi", "sayohatlar to‘xtadi", "rasadxonalar yopildi", "geografiya taqiqlandi", "Geografiya rivojlandi.")
t.NAT("Koreya akademiyasida aholining savodxonligini oshirish vazifasi qo‘yildi.", "28 harfdan iborat koreys fonetik alifbosi yaratildi", "xitoy yozuvi taqiqlandi", "akademiya yopildi", "lotin alifbosi qabul qilindi", "Koreys alifbosi yaratildi.")
t.NAT("Inklar tosh bo‘laklarini juda aniq kesib terdi.", "ularni bog‘lash uchun qorishma shart bo‘lmagan, toshlar orasiga pichoq ham sig‘magan", "binolar tez qulagan", "g‘isht qo‘llanila boshlandi", "devorlar yog‘ochdan qurildi", "Inklar me’morchiligi mukammal bo‘lgan.")
t.TF("Jenne madrasasida bezgakka qarshi muolajalar ishlab chiqilgan.", True, "To‘g‘ri.")
t.TF("Inklar bosib olingan xalqlarga mahalliy xudolarga sig‘inishni taqiqlagan.", False, "Noto‘g‘ri: taqiqlamagan, ammo Quyosh dinini rasmiy qabul qilish shart bo‘lgan.")
t.TF4([("Oq pagoda Pekinda XIII asrda qurilgan.", True), ("To‘pqopi saroyi Istanbulda XV asrda qurilgan.", True),
       ("Kumush pavilyon Dehlida joylashgan.", False), ("Sulton Xon karvonsaroyi Ko‘nyoda joylashgan.", True)],
      "3-noto‘g‘ri: Kumush pavilyon Kiotoda, XV asr oxiri.")
t.MUL([("Afrika niqoblarida sirtlon, sher, maymun qiyofalari tasvirlangan.", True),
       ("Inklarda zodagonlarning o‘g‘illari Kuskodagi maktablarda o‘qigan.", True),
       ("Afrika diniy haykallarini oddiy kishilar bemalol ko‘ra olgan.", False)],
      "III noto‘g‘ri: oddiy kishilarga ko‘rish man etilgan.")
t.CHR("Inshootlarni qurilish davri bo‘yicha ketma-ket joylashtiring.", ["Qutb minor (Dehli)", "Oltin pavilyon (Kioto)", "Go‘ri Amir maqbarasi (Samarqand)", "Kumush pavilyon (Kioto)"],
      "XIII asr → 1397 → XV asr → XV asr oxiri.")
t.MATCH("Inshootlarni joylashgan shahri bilan moslashtiring.", ["Al-Firdavs madrasasi", "Oltin pavilyon", "Go‘ri Amir maqbarasi", "Qutb minor"],
        ["Halab", "Kioto", "Samarqand", "Dehli", "Istanbul"], 'abcd',
        "Al-Firdavs – Halab; Oltin pavilyon – Kioto; Go‘ri Amir – Samarqand; Qutb minor – Dehli.")
t.VENN("Atsteklar", "Inklar",
       [("urush va yomg‘ir ma’budlariga ehtirom", 1), ("Mayya taqvimiga o‘xshash taqvim", 1),
        ("kipu – tugunli xatlar", 2), ("Quyosh xudosiga sig‘inish", 2),
        ("zodagon farzandlari maxsus maktablarda o‘qigan", 3)],
       "Atsteklar – yomg‘ir xudosi, taqvim; inklar – kipu, Quyosh; umumiy – zodagonlar maktabi.")
t.MAPMATCH('eurasia2', ['Marog‘a', 'Samarqand', 'Dehli', 'Kioto'],
           ["Nosiriddin at-Tusiy rasadxonasi", "Mirzo Ulug‘bek akademiyasi", "Qutb minor joylashgan shahar", "Oltin va Kumush pavilyonlar shahri"],
           "1 – Marog‘a; 2 – Samarqand; 3 – Dehli; 4 – Kioto.")
