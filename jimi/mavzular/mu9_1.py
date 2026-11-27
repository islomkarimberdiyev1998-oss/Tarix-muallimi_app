from qlib import Topic
TOPICS = {}
CA = 'ca'; UZ = 'uzb'

# 1 XIX asr o‘rtalarida O‘rta Osiyo davlatlarining hududi va aholisi
t = Topic('e9u1', 9001); TOPICS['e9u1'] = t
t.B("XIX asrda O‘rta Osiyoda nechta mustaqil davlat mavjud bo‘lgan?", "uchta", "ikkita", "to‘rtta", "beshta", "Buxoro amirligi, Xiva va Qo‘qon xonliklari.")
t.B("Buxoro amirligi poytaxti qanday nom bilan ham atalgan?", "«Buxoroi Sharif»", "«Qubbat ul-islom»", "«Ko‘hna shahar»", "«Oltin darvoza»", "«Buxoroi Sharif», ya’ni «Muqaddas Buxoro».")
t.B("Buxoro amirligining markaziy qismi qaysi vodiy hisoblangan?", "Zarafshon vodiysi", "Farg‘ona vodiysi", "Surxon vodiysi", "Vaxsh vodiysi", "Buxoro va Samarqand joylashgan Zarafshon vodiysi.")
t.B("Buxoro amirligida nechta beklik bo‘lgan?", "40 ta", "18 ta", "15 ta", "28 ta", "Amirlikda 40 ta beklik bo‘lgan.")
t.B("Xiva xonligi nechta beklik va noiblikka bo‘lingan?", "18 ta beklik, 2 ta noiblik", "40 ta beklik", "15 ta beklik", "20 ta beklik, 5 ta noiblik", "18 ta beklik, 2 ta noiblik.")
t.B("Qo‘qon xonligi nechta beklikka bo‘lingan?", "15 ta", "40 ta", "18 ta", "12 ta", "Xonlik 15 ta beklikka bo‘lingan.")
t.B("Xiva xonligining g‘arbiy chegarasi nima bilan tutashgan?", "Kaspiy dengizi", "Orol dengizi", "Eron", "Buxoro amirligi", "G‘arbda Kaspiy dengizi bilan chegaradosh bo‘lgan.")
t.B("Qo‘qon xonligi qachon tashkil topgan?", "XVIII asr boshlarida", "XVI asr oxirida", "XIX asr o‘rtalarida", "XVII asr boshlarida", "XVIII asr boshlarida Buxoro amirligidan ajrab tashkil topgan.")
t.B("Qo‘qon xonligi sharqda qaysi hudud bilan chegaradosh bo‘lgan?", "Sharqiy Turkiston", "Eron", "Afg‘oniston", "Kaspiy dengizi", "Sharqda Sharqiy Turkiston bilan.")
t.B("XIX asr o‘rtalarida Buxoro amirligi aholisi qancha bo‘lgan?", "2 million atrofida", "800 ming", "3 millionga yaqin", "5 million", "2 million atrofida.")
t.B("Xiva xonligida aholi soni qancha bo‘lgan?", "800 ming kishidan ortiq", "2 million", "3 million", "500 ming", "800 ming kishidan ortiq.")
t.B("Qo‘qon xonligida aholi soni qancha bo‘lgan?", "3 millionga yaqin", "2 million atrofida", "800 ming", "1 million", "3 millionga yaqin.")
t.B("Qaysi xonlik hududi sersuv daryolar, so‘lim vodiylar, serhosil yerlarga boy bo‘lgan?", "Qo‘qon xonligi", "Xiva xonligi", "Buxoro amirligi", "Qozoq xonligi", "Qo‘qon xonligi boshqalardan farqli o‘laroq.")
t.B("Qo‘qon xonligining janubiy chegarasidagi qaysi tog‘li o‘lkalar uchun Buxoro bilan to‘qnashuvlar bo‘lgan?", "Qorategin, Ko‘lob, Darvoz, Sho‘g‘non", "Xorazm, Mang‘ishloq", "Toshkent, Chimkent", "Marv, Chorjo‘y", "Qorategin, Ko‘lob, Darvoz, Sho‘g‘non.")
t.NAT("XVIII asr boshlarida Farg‘ona vodiysi va Sirdaryoning quyi qismigacha bo‘lgan hududlar Buxoro amirligidan ajraldi.", "mustaqil Qo‘qon xonligi tashkil topdi", "Xiva xonligi tuzildi", "Buxoro amirligi kuchaydi", "Turkiston general-gubernatorligi tuzildi", "Natijada mustaqil davlat — Qo‘qon xonligi tashkil topdi.")
t.TF("Xonliklarda o‘zbeklar o‘troq turmush kechirib, dehqonchilik, hunarmandchilik va savdo bilan shug‘ullangan.", True, "To‘g‘ri.")
t.TF("Qozoqlar, qoraqalpoqlar, turkmanlar va qirg‘izlar asosan o‘troq dehqonchilik bilan shug‘ullangan.", False, "Noto‘g‘ri: ular ko‘chmanchi bo‘lib, chorvachilik bilan shug‘ullangan.")
t.MUL([("Buxoro amirligida mang‘it, saroy, qo‘ng‘irot, kenagas kabi o‘zbek urug‘lari ko‘pchilikni tashkil qilgan.", True),
       ("Xiva xonligining ma’muriy markazi Urganch shahri bo‘lgan.", False),
       ("Xonliklar hududi bugungi Qirg‘iziston, Qozog‘iston, Tojikiston va Turkmaniston yerlarining bir qismini ham o‘z ichiga olgan.", True)],
      "II noto‘g‘ri: Xiva xonligining ma’muriy markazi Xiva shahri bo‘lgan.")
t.MATCH("Davlatlarni ularning aholisi soni bilan moslashtiring.", ["Buxoro amirligi", "Xiva xonligi", "Qo‘qon xonligi"],
        ["800 ming kishidan ortiq", "3 millionga yaqin", "2 million atrofida"], "cab",
        "Buxoro — 2 mln; Xiva — 800 mingdan ortiq; Qo‘qon — 3 mlnga yaqin.")
t.MAPMATCH(CA, ['Buxoro', 'Xiva', 'Qo‘qon'],
           ["Buxoro amirligi poytaxti — «Buxoroi Sharif»", "Xiva xonligining ma’muriy markazi", "Qo‘qon xonligining markazi"],
           "1 – Buxoro; 2 – Xiva; 3 – Qo‘qon.")
t.VENN("Buxoro amirligi", "Qo‘qon xonligi",
       [("40 ta beklikka bo‘lingan", 1), ("Zarafshon vodiysi markaziy qismi bo‘lgan", 1),
        ("15 ta beklikka bo‘lingan", 2), ("Sharqiy Turkiston bilan chegaradosh", 2),
        ("aholisining asosiy qismi o‘zbeklar", 3)],
       "Buxoro — 40 beklik, Zarafshon. Qo‘qon — 15 beklik, Sharqiy Turkiston. Ikkalasida aholining asosiy qismi o‘zbeklar.")

# 2 Xonliklarning ma’muriy boshqaruv tizimi
t = Topic('e9u2', 9002); TOPICS['e9u2'] = t
t.B("Buxoro amirligini qaysi sulola boshqargan?", "mang‘itlar", "qo‘ng‘irotlar", "minglar", "ashtarxoniylar", "Mang‘itlar sulolasi.")
t.B("Xiva xonligini qaysi sulola boshqargan?", "qo‘ng‘irotlar", "mang‘itlar", "minglar", "shayboniylar", "Qo‘ng‘irotlar sulolasi.")
t.B("Qo‘qon xonligini qaysi sulola boshqargan?", "minglar", "mang‘itlar", "qo‘ng‘irotlar", "temuriylar", "Minglar sulolasi.")
t.B("Buxoro amirligida ijro hokimiyati kimning qo‘lida bo‘lgan?", "qo‘shbegi (bosh vazir)", "devonbegi", "otaliq", "parvonachi", "Bosh vazir — qo‘shbegi qo‘lida.")
t.B("Buxoro amirligida moliya, xazina, soliqlar va tashqi aloqalarni kim idora qilgan?", "devonbegi", "qo‘shbegi", "mushrif", "dodxoh", "Devonbegi.")
t.B("Buxoro amirligida amirlik hujjatlarini yuritishga kim mas’ul bo‘lgan?", "mirzaboshi", "mushrif", "sadr", "muftiy", "Devonbegiga bo‘ysungan mirzaboshi.")
t.B("Buxoro amirligida soliqlarni o‘z vaqtida yig‘ish va hisobga olishga kim javobgar bo‘lgan?", "mushrif", "mirzaboshi", "dodxoh", "parvonachi", "Mushrif.")
t.B("Buxoro amirligida xalqning shikoyatlari bilan kim shug‘ullangan?", "dodxoh", "mushrif", "ko‘kaldosh", "otaliq", "Dodxoh lavozimidagi shaxs.")
t.B("Buxoro amirligida oliy hukmdor farmonlarini kim e’lon qilgan?", "parvonachi", "mirzaboshi", "sadr", "topchiboshi", "Parvonachi.")
t.B("Buxoro amirligida vaqf ishlari va mulklari bilan kim shug‘ullangan?", "sadr", "muftiy", "qozikalon", "mushrif", "Sadr.")
t.B("Buxoro amirligida valiahd tarbiyasi bilan kim mashg‘ul bo‘lgan?", "otaliq", "ko‘kaldosh", "parvonachi", "mirshabboshi", "Otaliq.")
t.B("Buxoro amir qo‘shinlarining bosh qo‘mondoni kim bo‘lgan?", "topchiboshi", "yasovulboshi", "amirlashkar", "mirshabboshi", "Topchiboshi.")
t.B("Buxoro amirligida mamlakat xavfsizligi, amirning do‘st va dushmanlari haqida ma’lumot to‘plagan amaldor kim?", "ko‘kaldosh", "dodxoh", "otaliq", "mushrif", "Ko‘kaldosh.")
t.B("Xiva shahridagi ichki qal’a qanday atalgan?", "Ichan qal’a", "Dishan qal’a", "Ark", "Ko‘hna ark", "Ichki — Ichan qal’a, tashqi — Dishan qal’a.")
t.B("Xiva xonligida oliy amaldor kim hisoblangan?", "devonbegi", "qo‘shbegi", "mehtar", "otaliq", "Xivada oliy amaldor devonbegi edi.")
t.B("Xiva xonligida sug‘orish inshootlari va suv taqsimotiga kim mas’ul bo‘lgan?", "mirobboshi", "yasovulboshi", "mirshabboshi", "lashkarboshi", "Mirobboshi.")
t.B("Xiva xon qo‘shinlarining bosh qo‘mondoni kim bo‘lgan?", "yasovulboshi", "topchiboshi", "amirlashkar", "mingboshi", "Yasovulboshi.")
t.B("Qo‘qon xonligida eng yuqori harbiy lavozim qaysi edi?", "amirlashkar", "topchiboshi", "yasovulboshi", "lashkarboshi", "Amirlashkar — harbiy vazir.")
t.B("Qo‘qon xonligida xazina ishlari va xarajatlarini kim nazorat qilgan?", "mehtar", "mingboshi", "muhtasib", "qozikalon", "Mehtar.")
t.TF("Xiva xonligida askarlik xizmatida bo‘lganlar soliqlardan ozod qilingan.", True, "To‘g‘ri.")
t.TF("Qo‘qon xonligida mingboshilar keyinchalik moliya vaziri vazifasini bajargan.", False, "Noto‘g‘ri: ular keyinchalik bosh vazir vazifasini bajargan.")
t.MUL([("Buxoro amirligida sud boshlig‘i qozikalon, raiskalon hisoblangan.", True),
       ("Buxoro amirligida shayxulislom shariat qoidalari, qonunlar ijrosi va sud ishlarini nazorat qilgan.", True),
       ("Buxoro amirligida shaharlarda tinchlik va tartibni yasovulboshi saqlagan.", False)],
      "III noto‘g‘ri: buni amir soqchilari boshlig‘i — mirshabboshi bajargan.")
t.MATCH("Xonliklarni sulolalar bilan moslashtiring.", ["Buxoro amirligi", "Xiva xonligi", "Qo‘qon xonligi"],
        ["minglar", "mang‘itlar", "qo‘ng‘irotlar"], "bca", "Buxoro — mang‘itlar; Xiva — qo‘ng‘irotlar; Qo‘qon — minglar.")
t.VENN("Buxoro amirligi", "Xiva xonligi",
       [("bosh vazir — qo‘shbegi", 1), ("qo‘shin qo‘mondoni — topchiboshi", 1),
        ("oliy amaldor — devonbegi", 2), ("suv taqsimoti — mirobboshi", 2),
        ("diniy ishlar — shayxulislom", 3)],
       "Buxoroda qo‘shbegi, topchiboshi; Xivada devonbegi oliy amaldor, mirobboshi; ikkalasida shayxulislom.")
