from qlib import Topic, PLACES, REG
TOPICS = {}

# 12 Hindiston
t = Topic('y7j12', 7012); TOPICS['y7j12'] = t
t.B("Guptalar sulolasiga kim asos solgan?", "Chandragupta", "Xarsha", "Mahmud G‘aznaviy", "Syuan Szyan", "Hind rojasi Chandragupta (320–340).")
t.B("Guptalar imperiyasi IV–V asrlarda qaysi dengizgacha bo‘lgan hududlarni birlashtirgan?", "Arabiston dengizigacha", "O‘rta Yer dengizigacha", "Qora dengizgacha", "Sariq dengizgacha", "Arabiston dengizigacha.")
t.B("Hindistonda qishloq jamoasi a’zosining mavqei nima bilan belgilangan?", "qaysi kastaga mansubligi bilan", "mulkining ko‘pligi bilan", "yoshi bilan", "bilimi bilan", "Shaxsning qaysi kasta toifasiga mansubligi bilan.")
t.B("Hindistonda ilk tabaqalanish tartiblari qachondan boshlangan?", "qadimgi oriylar istilosidan so‘ng", "Guptalar davridan", "eftaliylar bosqinidan so‘ng", "Mahmud G‘aznaviy yurishlaridan so‘ng", "Oriylar istilosidan so‘ng rojaliklar tashkil topgan davrdan.")
t.B("VI asrda Guptalar imperiyasi kimlarning hujumlari natijasida parchalangan?", "eftaliylar", "arablar", "mo‘g‘ullar", "xunnlar", "Shimoli-g‘arbdan kelgan eftaliylar.")
t.B("Xarsha imperiyasiga kim asos solgan?", "Kanudja rojasi Xarsha", "Chandragupta", "Mahmud", "Kanishka", "Kanudja rojasi Xarsha (606–647).")
t.B("Xarsha ajdodlari hinduiy bo‘lsa-da, u qaysi dinni qabul qilgan?", "buddaviylik", "islom", "xristianlik", "zardushtiylik", "Buddaviylikni.")
t.B("Xarsha imperiyasida vassal rojalar soni qancha bo‘lgan?", "qirqqa yaqin", "yetmishga yaqin", "yigirmaga yaqin", "o‘nga yaqin", "Qirqqa yaqin.")
t.B("«Rajput» so‘zi qanday ma’noni anglatadi?", "«podsholar o‘g‘illari»", "«ritsarlar»", "«kohinlar»", "«dehqonlar»", "«Podsholar o‘g‘illari».")
t.B("Rajputlar asosan qayerda yashagan?", "Rajputanda (hozirgi Rojaston)", "Bengaliyada", "Panjobda", "Dekanda", "Rajputanda (Rojaston).")
t.B("VII asrda Hindistonda bo‘lgan xitoylik tarixchi kim?", "Syuan Szyan", "Konfutsiy", "Lao-szi", "Xubilay", "Syuan Szyan.")
t.B("Syuan Szyan yozishicha Hindistonda qancha katta-kichik knyazlik bo‘lgan?", "70 ga yaqin", "20 dan ortiq", "40 ga yaqin", "17 ta", "70 ga yaqin.")
t.B("Doimiy harbiy xizmat sharti bilan in’om etilgan yer qanday atalgan?", "grass", "patta", "benefitsiy", "iqto", "Grass («qultum», «bo‘lak»).")
t.B("Ma’lum xizmat muddatiga beriladigan yer qanday atalgan?", "patta", "grass", "feod", "domen", "Patta («yorliqqa olingan yer»).")
t.B("Rajput davlatlarida hukmron din qaysi bo‘lgan?", "hinduiylik", "buddaviylik", "islom", "jaynizm", "Hinduiylik.")
t.B("Mahmud G‘aznaviy Hindistonning shimoliga necha marta yurish qilgan?", "17 marta", "7 marta", "40 marta", "70 marta", "XI asr boshlarida 17 marta.")
t.NAT("Gupta hukmdorlari amaldor va harbiylarga yer-mulklar in’om etdi.", "yirik yer egalari toifasi paydo bo‘lib, feodal tuzum shakllandi", "qulchilik kuchaydi", "kastalar bekor qilindi", "Guptalar imperiyasi kengaydi", "Yirik yer egalari soliq va dehqonlar mehnatidan foydalanish huquqini oldi.")
t.NAT("Xarsha imperiyasida vassal rojalarning ayirmachilik harakati kuchaydi.", "imperiya zaiflashib, rojalar amalda mustaqil bo‘lib oldi", "imperiya markazlashdi", "Xarsha butun Hindistonni birlashtirdi", "buddaviylik taqiqlandi", "Imperiya uzoq yashamadi.")
t.NAT("Istilochi eftaliylar mahalliy yuqori toifalar bilan aralashdi.", "rajputlar kastasiga asos solindi", "eftaliylar Hindistonni tark etdi", "Dehli sultonligi tuzildi", "kasta tizimi yo‘qoldi", "Rajputlar kastasi vujudga keldi.")
t.NAT("Mahmud G‘aznaviy Hindiston shimoliga yurishlar qildi, musulmonlar o‘rnashdi.", "XIII asr boshlarida Dehli sultonligi tuzildi", "Guptalar imperiyasi tiklandi", "Hindiston Xitoyga qo‘shildi", "rajputlar butun Hindistonni birlashtirdi", "Dehli sultonligi tashkil topdi.")
t.TF("Hindistonda bir kastadan boshqasiga o‘tish va turli kastalar orasidagi nikoh qoralangan.", True, "To‘g‘ri.")
t.TF("Rajputlar o‘tochar qurollarni eng yaxshi qurol deb hisoblagan.", False, "Noto‘g‘ri: o‘tochar qurollarni qo‘rqoqlar quroli deb hisoblagan.")
t.TF4([("Rajputlar yevropalik ritsarlardan farqli ravishda faqat yengil sovut kiygan.", True), ("Rojalardan biri ibodatxonalarga 1400 ta qishloq in’om etgan.", True),
       ("Pattaga berilgan yerlar hech qachon merosiy mulkka aylanmagan.", False), ("O‘rta asrlar boshida Hindistonda qulchilik saqlanib qolgan.", True)],
      "3-noto‘g‘ri: pattaga berilgan yerlar ham merosiy mulkka aylana boshlagan.")
t.MUL([("Xarsha shoir va dramaturg bo‘lgan.", True),
       ("Xarsha imperiyasi XIII asr boshlariga qadar so‘nggi yirik imperiya sifatida mavjud bo‘lgan.", True),
       ("Rajputlar dehqonchilik va savdo bilan faol shug‘ullangan.", False)],
      "III noto‘g‘ri: rajputlar faqat ov va harbiy ish bilan shug‘ullangan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Guptalar sulolasiga asos solindi", "Eftaliylar hujumida Guptalar imperiyasi parchalandi", "Xarsha imperiyasi tashkil topdi", "Mahmud G‘aznaviy yurishlari", "Dehli sultonligi tuzildi"],
      "IV asr (320) → VI asr → VII asr (606) → XI asr boshi → XIII asr boshi.")
t.VENN("Grass", "Patta",
       [("harbiy xizmatga doimo shay turish majburiyati", 1), ("rojaning yaqinlari va jangchilariga berilgan", 1),
        ("«yorliqqa olingan yer»", 2), ("xonadonga mansub bo‘lmagan amaldorlarga muddatli berilgan", 2),
        ("rojalar in’om etgan yer", 3)],
       "Grass – harbiy xizmat, yaqinlarga; patta – yorliqli, muddatli; ikkalasi rojalar in’omi.")
t.MAPMATCH('india', ['G‘azna', 'Dehli', 'Rajputana', 'Bengaliya'],
           ["17 marta Hindistonga yurish qilgan hukmdor davlati markazi", "XIII asr boshida tuzilgan sultonlik markazi", "rajputlar yashagan hudud (hozirgi Rojaston)", "Xarsha imperiyasi sharqda yetib borgan qo‘ltiq hududi"],
           "1 – G‘azna; 2 – Dehli; 3 – Rajputana; 4 – Bengaliya.")

# 13 Xitoy
t = Topic('y7j13', 7013); TOPICS['y7j13'] = t
t.B("Mil. avv. V asrda Xitoyda kimlarning ta’limotlari qaror topgan?", "Konfutsiy va Lao-szi", "Budda va Syuan Szyan", "Xubilay va Chingizxon", "Sun Yatsen va Mao", "Konfutsiy va Lao-szi.")
t.B("Konfutsiylikka ko‘ra inson uchun eng muhimi nima?", "insoniylikni saqlab qolish", "boylik to‘plash", "harbiy shon-shuhrat", "dunyodan voz kechish", "Insoniylikni saqlab qolish.")
t.B("III asrda Xan imperiyasi nechta podsholikka parchalangan?", "uchta", "ikkita", "to‘rtta", "beshta", "Uchta podsholikka.")
t.B("Vey podsholigining poytaxti qaysi shahar bo‘lgan?", "Loyan", "Chanan", "Pekin", "Nankin", "Loyan.")
t.B("Vey sulolasi davrida qanday yer tizimi shakllangan?", "davlat chek yer tizimi", "feod tizimi", "patta tizimi", "benefitsiy tizimi", "Davlat chek yer tizimi.")
t.B("Xitoyliklarga umid beruvchi so‘zlar qaysi ta’limot rohiblaridan chiqqan?", "buddaviylik", "konfutsiylik", "daosiylik", "xristianlik", "Hindistondan kelgan buddaviylik rohiblaridan.")
t.B("Uzoq Sharq sivilizatsiyasining asosi qaysi ta’limotlar birlashmasidan paydo bo‘lgan?", "konfutsiylik, daosiylik, buddaviylik", "islom, xristianlik, buddaviylik", "hinduiylik, jaynizm, buddaviylik", "shomonlik, sintoizm, konfutsiylik", "Uch buyuk ta’limot birlashmasidan.")
t.B("VI asr oxirida Xitoydagi podsholiklar qaysi xavf ostida birlashgan?", "Turk xoqonligi bosqini", "mo‘g‘ullar bosqini", "arablar bosqini", "Yaponiya bosqini", "Turk xoqonligi bosqini xavfi ostida.")
t.B("Tan sulolasi qaysi yillarda hukmronlik qilgan?", "618–907-yillarda", "589–618-yillarda", "960–1279-yillarda", "907–960-yillarda", "618–907-yillar.")
t.B("Sun sulolasi qaysi yillarda hukmronlik qilgan?", "960–1279-yillarda", "618–907-yillarda", "589–618-yillarda", "907–960-yillarda", "960–1279-yillar.")
t.B("Xitoy imperatori qanday atalgan?", "Osmon o‘g‘li", "vasilevs", "xalifa", "raja", "Osmon o‘g‘li – «xudoning farzandi».")
t.B("Imperator har bir erkin dehqonga qancha ekin maydoni bergan?", "80 mu", "10 mu", "100 mu", "6 sotix", "80 mudan ekin maydoni.")
t.B("1 mu taxminan qanchaga teng?", "6 sotixga", "1 gektarga", "100 sotixga", "1 sotixga", "1 mu ≈ 6 sotix.")
t.B("Xuanxe va Yanszi daryolarini qanday inshoot birlashtirgan?", "Buyuk kanal", "Buyuk Xitoy devori", "Ipak yo‘li", "Grand to‘g‘on", "Buyuk kanal.")
t.B("Xitoyda amaldorlar qanday tanlab olingan?", "davlat imtihonlari orqali", "meros yo‘li bilan", "qur’a tashlash bilan", "imperator saylovi bilan", "Davlat imtihonlari orqali.")
t.B("Xitoyni 1279-yilda butunlay bosib olgan mo‘g‘ul hukmdori kim?", "Xubilay", "Chingizxon", "Botuxon", "Xuloku", "Xubilay.")
t.NAT("Shimoliy dashtlarning ko‘chmanchi qabilalari IV–V asrlarda Xitoyga siljidi.", "mamlakatda siyosiy tarqoqlik hukm surib, imperiya ko‘plab podsholiklarga bo‘lindi", "Xitoy kuchaydi", "ko‘chmanchilar konfutsiylikni taqiqladi", "Xan imperiyasi tiklandi", "Imperiya raqobatdagi podsholiklarga bo‘lindi.")
t.NAT("Xitoyni o‘rab turgan Koreya, Yaponiya, Vyetnam, Tibet Xitoydan iyeroglif, qonun va uch ta’limotni o‘zlashtirdi.", "Uzoq Sharqda o‘ziga xos Xitoy (Uzoq Sharq) sivilizatsiyasi shakllandi", "bu mamlakatlar Xitoyga qo‘shildi", "buddaviylik yo‘qoldi", "Xitoy izolyatsiyaga o‘tdi", "Uzoq Sharq sivilizatsiyasi shakllandi.")
t.NAT("X–XII asrlarda amaldorlar suiiste’molliklari va yer tanqisligi kuchaydi.", "dehqonlar qo‘zg‘olonlari boshlanib, mamlakat zaiflashdi", "Xitoy boyib ketdi", "imtihon tizimi bekor qilindi", "Sun sulolasi mo‘g‘ullarni yengdi", "Zaiflashgan mamlakatni 1279-yilda mo‘g‘ullar bosib oldi.")
t.NAT("Imperator dehqonlarga 80 mudan yer berib, tartib va intizom o‘rnatdi.", "qishloq aholisi tez o‘sib, yirik shaharlar yanada yuksaldi", "dehqonlar yerni sotib boyib ketdi", "shaharlar qisqardi", "Buyuk kanal buzildi", "Aholi tez o‘sdi, shaharlar yuksaldi.")
t.TF("Xitoyliklar chinni yasash, kitob bosish va poroxni kashf qilgan.", True, "To‘g‘ri.")
t.TF("Xitoyda imtihonlarni faqat zodagon oilalarning farzandlari topshirishi mumkin edi.", False, "Noto‘g‘ri: imtihonlarni har bir kishi topshirishi mumkin edi.")
t.TF4([("Dehqon imperatordan olgan yerni sotishi mumkin bo‘lmagan.", True), ("Dehqonlar Buyuk Xitoy devorini ta’mirlashda ishtirok etgan.", True),
       ("Suy sulolasi Tan sulolasidan keyin hukmronlik qilgan.", False), ("Xitoyliklar kompasni takomillashtirgan.", True)],
      "3-noto‘g‘ri: Suy (589–618) Tan (618–907)dan oldin hukmronlik qilgan.")
t.MUL([("Konfutsiylik ibodatxonalarida Lao-szi va Budda haykalchalari ham turgan.", True),
       ("Barcha xitoyliklar qishloq, hunarmandchilik, savdo jamoalariga birlashtirilgan.", True),
       ("Konfutsiylik yovuzlikka yovuzlik bilan javob berishga undagan.", False)],
      "III noto‘g‘ri: yovuzlikka adolat bilan javob berishga undagan.")
t.CHR("Sulolalarni xronologik ketma-ketlikda joylashtiring.", ["Suy", "Tan", "U Day", "Sun"], "589 → 618 → 907 → 960.")
t.VENN("Konfutsiylik", "Buddaviylik",
       [("Xitoyda mil. avv. V asrda qaror topgan", 1), ("ajdodlar marosimlariga qat’iy amal qilish", 1),
        ("Hindistondan kelgan", 2), ("azob-uqubatlar xohish-istaklardan kelib chiqadi deb o‘rgatgan", 2),
        ("Uzoq Sharq sivilizatsiyasi asoslaridan biri", 3)],
       "Konfutsiylik – Xitoy, marosimlar; buddaviylik – Hindiston, istaklarni jilovlash; ikkalasi Uzoq Sharq sivilizatsiyasi asosi.")
t.MAPN('eastasia', ['Loyan', 'Koreya', 'Yaponiya', 'Vyetnam'], "Qaysi raqam bilan Vey podsholigining poytaxti belgilangan?",
       "1 – Loyan (Vey poytaxti); 2 – Koreya; 3 – Yaponiya; 4 – Vyetnam (Xitoydan ta’limotlarni o‘zlashtirgan qo‘shnilar).")
