# Qiziqarli tarix: Tarixiy davlat, Tarixiy shaxs, Ha/Yo'q, Yozma, Fleshkard
# Faktlar 7–10-sinf yangi darsliklaridan olingan. Ishga tushirish: python3 jimi/qiziq/qz5.py
import json, random, os
R = random.Random(2026)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def mc(items, pool):
    """items: (ta'rif, javob, izoh) -> {q,a,c,e}; noto'g'ri variantlar pool'dan."""
    out = []
    for d, ans, e in items:
        wrong = [x for x in pool if x != ans]
        R.shuffle(wrong)
        out.append({"q": d, "a": [ans] + wrong[:3], "c": 0, "e": e})
    return out

# ---------- Tarixiy davlat ----------
DAV = ["Gana", "Mali", "Songay", "Monomotapa", "Mamluklar davlati", "Xiva xonligi", "Qo‘qon xonligi",
       "Buxoro amirligi", "Jung‘or xonligi", "Qozoq xonligi", "Sibir xonligi", "No‘g‘ay xonligi",
       "Atsteklar davlati", "Inklar imperiyasi", "Mayyalar", "Usmonli saltanati", "Safaviylar davlati",
       "Boburiylar davlati", "Qozon xonligi", "Ashtarxon xonligi", "Orol (Aran) davlati"]
dav1 = [
 ("VIII asrda G‘arbiy Sudanda vujudga kelgan, hukmdori «oltinlarning egasi» deb ta’riflangan davlat.", "Gana", "Gana; 1076-yilda Marokash sultoni Abu Bakr bosib olgan."),
 ("Poytaxti Niara bo‘lgan, Mansa Muso davrida qudrat cho‘qqisiga chiqqan davlat.", "Mali", "Mali; Mansa Muso 1312–1337-yillarda hukmronlik qilgan."),
 ("Sunni Ali va Muhammad I davrida rivojlangan, XVI asr oxirida Marokash bosib olgan davlat.", "Songay", "Songay davlati."),
 ("Poytaxti Buyuk Zimbabve bo‘lgan, hukmdori oliy ruhoniy ham hisoblangan davlat.", "Monomotapa", "Monomotapa; XVII asr oxirida shona qabilalari bosib olgan."),
 ("1250-yilda Ayyubiylarni ag‘darib Misrda tuzilgan, 1260-yilda mo‘g‘ullarni to‘xtatgan davlat.", "Mamluklar davlati", "Mamluklar; Sayfiddin Qutuz boshchiligida mo‘g‘ullar to‘xtatilgan."),
 ("Poytaxti Tenochtitlan bo‘lgan, 1521-yilda Ernan Kortes tugatgan davlat.", "Atsteklar davlati", "Atsteklar; Tenochtitlanga 1325-yilda asos solingan."),
 ("Markazi Kusko bo‘lgan, to‘rt viloyatga bo‘lingan va 1572-yilda butunlay tugatilgan davlat.", "Inklar imperiyasi", "Inklar imperiyasi; Inka Pachakutek davrida vujudga kelgan."),
 ("Shahar-davlatlari mustaqil bo‘lgani uchun «Yangi dunyo yunonlari» deb atalgan xalq.", "Mayyalar", "Mayyalar; Mayyapan 1263-yilda asos solingan."),
 ("Ivan Grozniy 1552-yilda bosib olgan Volgabo‘yi xonligi.", "Qozon xonligi", "Qozon xonligi – 1552-yil."),
 ("1556-yilda Rossiya bosib olgach, hukmdori Yor Muhammadxon Buxoroga ketgan xonlik.", "Ashtarxon xonligi", "Ashtarxon xonligi."),
 ("Kuchumxon 1563-yilda Abdullaxon II yordamida taxtga chiqqan xonlik.", "Sibir xonligi", "Sibir xonligi; Yermak 1581–1583-yillarda unga qarshi kurashgan."),
 ("1465–1466-yillarda Abulxayrxondan qochgan Girayxon va Jonibekxon asos solgan xonlik.", "Qozoq xonligi", "Qozoq xonligi."),
 ("1635-yilda tashkil topib, 1758-yilda Chin imperiyasi tugatgan qalmiqlar davlati.", "Jung‘or xonligi", "Jung‘or xonligi."),
 ("XVII asrda qoraqalpoqlar o‘zbeklar bilan birga Xiva xonligi shimolida barpo etgan davlat.", "Orol (Aran) davlati", "Orol (Aran) davlati."),
 ("XV asr ikkinchi yarmidan XVI asr ikkinchi yarmigacha qoraqalpoqlar tarkibida bo‘lgan xonlik.", "No‘g‘ay xonligi", "No‘g‘ay xonligi."),
]
dav2 = [
 ("1511-yilda arabshohiylar sulolasi asos solgan, O‘rta Osiyodagi ikkinchi o‘zbek davlati.", "Xiva xonligi", "Xiva xonligi; birinchi xoni Elbarsxon."),
 ("1709-yilda ming urug‘idan Shohruxbiy Farg‘onada tuzgan davlat.", "Qo‘qon xonligi", "Qo‘qon xonligi."),
 ("1756-yildan mang‘itlar boshqargan, hukmdori xon emas, amir deb atalgan davlat.", "Buxoro amirligi", "Buxoro amirligi; mang‘itlar chingiziy bo‘lmagan."),
 ("Shayboniylar bilan Xuroson uchun kurashgan shialik davlat.", "Safaviylar davlati", "Safaviylar – shayboniylarning asosiy raqibi."),
 ("Xuroson uchun kurashda shayboniylarni qo‘llab-quvvatlagan, sultoni xalifa deb e’tirof etilgan davlat.", "Usmonli saltanati", "Usmonli saltanati."),
 ("1526-yilda Panipat jangidan so‘ng Hindistonda tuzilgan sulola davlati.", "Boburiylar davlati", "Boburiylar; asoschisi Zahiriddin Muhammad Bobur."),
 ("Mansa Muso 1324-yilda hajga borib 300 pud oltin hadya qilgan davlat.", "Mali", "Mali."),
 ("Poytaxti Kumbi Sale bo‘lgan, oltin va tuz «so‘zsiz» ayirboshlangan davlat.", "Gana", "Gana."),
 ("Mita – soliq o‘rniga mehnat majburiyati tizimi bo‘lgan, bozorlari bo‘lmagan davlat.", "Inklar imperiyasi", "Inklar."),
 ("«Suzuvchi dalalar» – chinampalarni ixtiro qilgan xalq davlati.", "Atsteklar davlati", "Atsteklar."),
 ("Mo‘g‘ul bosqinini Ayn-Jalutda to‘xtatgan Misr davlati.", "Mamluklar davlati", "Mamluklar, 1260-yil."),
 ("Toshkent hokimiga 1831-yilda beklarbegi unvoni berilgan davlat.", "Qo‘qon xonligi", "Qo‘qon xonligi; Muhammad Alixon davri."),
 ("Bosh vaziri mehtar deb atalgan, Ichan qal’a joylashgan poytaxtli davlat.", "Xiva xonligi", "Xiva xonligi."),
 ("Bosh vaziri qushbegi bo‘lib, poytaxt hokimi ham sanalgan davlat.", "Buxoro amirligi", "Buxoro amirligi (mang‘itlar)."),
 ("1723-yilda Turkistonga hujum qilib, qoraqalpoqlarni uch guruhga bo‘lib yuborgan davlat.", "Jung‘or xonligi", "Jung‘orlar."),
]

# ---------- Tarixiy shaxs ----------
SHX = ["Abulxayrxon", "Muhammad Shayboniyxon", "Zahiriddin Muhammad Bobur", "Abdullaxon II", "Ubaydullaxon",
       "Yalangto‘sh Bahodir", "Subhonqulixon", "Muhammad Rahimbiy", "Amir Shohmurod", "Amir Nasrulla",
       "Elbarsxon", "Abulg‘ozi Bahodirxon", "Sherg‘ozixon", "Muhammad Aminxon", "Shohruxbiy", "Erdonaxon",
       "Umarxon", "Nodira", "Uvaysiy", "Gulxaniy", "Berdaq", "Ajiniyoz", "Mansa Muso", "Ernan Kortes",
       "Yan van Eyk", "Iogann Gutenberg", "Filippo Brunelleski", "Marko Polo", "Jon Viklif", "Lyudovik XI"]
shx1 = [
 ("1428-yilda Turani egallab poytaxt qilgan, 1446-yilda poytaxtni Sig‘noqqa ko‘chirgan hukmdor.", "Abulxayrxon", "Abulxayrxon."),
 ("1510-yilda Marv yaqinida Ismoil Safaviy bilan jangda halok bo‘lgan hukmdor.", "Muhammad Shayboniyxon", "Muhammad Shayboniyxon."),
 ("1483-yilda Andijonda tug‘ilgan, 1526-yilda Panipatda g‘alaba qozongan hukmdor.", "Zahiriddin Muhammad Bobur", "Bobur."),
 ("1533-yilda poytaxtni Samarqanddan Buxoroga ko‘chirgan shayboniy.", "Ubaydullaxon", "Ubaydullaxon."),
 ("1557-yilda Buxoroni egallab, mamlakatni birlashtirgan, «Xon» taxallusi bilan she’r yozgan hukmdor.", "Abdullaxon II", "Abdullaxon II."),
 ("Samarqandda Sherdor va Tillakori madrasalarini qurdirgan ashtarxoniylar davri arbobi.", "Yalangto‘sh Bahodir", "Yalangto‘sh Bahodir (1578–1656)."),
 ("«Nishoniy» taxallusli, «Ihyo at-tibbi Subhoniy» asarini yozgan va 1682-yilda kasalxona qurdirgan xon.", "Subhonqulixon", "Subhonqulixon."),
 ("Chingiziy bo‘lmagani uchun o‘zini amir deb e’lon qilgan birinchi mang‘it hukmdori.", "Muhammad Rahimbiy", "Muhammad Rahimbiy, 1756-yil."),
 ("Darveshona hayot kechirib «Amiri Jannatmakon» deb atalgan, Samarqandda 24 mavze qurdirgan amir.", "Amir Shohmurod", "Amir Shohmurod (1785–1800)."),
 ("1842-yilda Qo‘qonni egallab, Nodirani qatl ettirgan Buxoro amiri.", "Amir Nasrulla", "Amir Nasrulla."),
 ("1511-yilda Xorazm taxtiga taklif qilingan, Xiva xonligining birinchi xoni.", "Elbarsxon", "Elbarsxon."),
 ("«Shajarayi turk» asarini yozgan Xiva xoni.", "Abulg‘ozi Bahodirxon", "Abulg‘ozi Bahodirxon."),
 ("Pyotr I yuborgan Bekovich-Cherkasskiy qo‘shinini harbiy hiyla bilan tor-mor etgan Xiva xoni.", "Sherg‘ozixon", "Sherg‘ozixon (1714–1726)."),
 ("Kaltaminor qurilishini boshlagan, 1855-yilda Saraxs yaqinida halok bo‘lgan Xiva xoni.", "Muhammad Aminxon", "Muhammad Aminxon."),
 ("1709-yilda Farg‘onada mustaqil hokimiyat o‘rnatgan ming urug‘i boshlig‘i.", "Shohruxbiy", "Shohruxbiy."),
]
shx2 = [
 ("Minglar orasida birinchi bo‘lib xon unvonini olgan, 1758-yilda Xo‘jand va O‘ratepani egallagan hukmdor.", "Erdonaxon", "Erdonaxon."),
 ("«Amiriy» taxallusi bilan she’rlar yozgan, atrofida 70 dan ortiq shoir yig‘ilgan Qo‘qon xoni.", "Umarxon", "Umarxon."),
 ("«Komila» va «Maknuna» taxalluslari bilan ham ijod qilgan shoira va davlat arbobi.", "Nodira", "Nodira – Mohlaroyim (1792–1842)."),
 ("Asl ismi Jahon bo‘lgan, Nodiraga she’riyatdan dars bergan shoira.", "Uvaysiy", "Uvaysiy (1779–1845)."),
 ("«Zarbulmasal» asari muallifi, hammomda go‘lax bo‘lib ishlagan shoir.", "Gulxaniy", "Gulxaniy – Muhammad Sharif."),
 ("Qoraqalpoq xalq adabiyotining asoschisi, asl ismi Berdimurod Qarg‘aboy o‘g‘li.", "Berdaq", "Berdaq."),
 ("«Zevar» taxallusli, «Bo‘zatov» dostoni muallifi qoraqalpoq shoiri.", "Ajiniyoz", "Ajiniyoz (1824–1878)."),
 ("1324-yilda hajga borib, yo‘l-yo‘lakay 300 pud oltin hadya qilgan Mali hukmdori.", "Mansa Muso", "Mansa Muso."),
 ("1521-yilda atsteklar davlatini tugatgan ispan konkistadori.", "Ernan Kortes", "Ernan Kortes."),
 ("Moybo‘yoqning yangi turlarini ishlab chiqqan, «Jovanni Arnolfini» portreti muallifi.", "Yan van Eyk", "Yan van Eyk – Shimoliy Renessans."),
 ("1445-yilda bosma mashina va harf quyish dastgohini ixtiro qilgan olim.", "Iogann Gutenberg", "Gutenberg."),
 ("Santa Mariya sobori gumbazini yaratgan, Uyg‘onish davri arxitekturasining asoschisi.", "Filippo Brunelleski", "Brunelleski (1377–1446)."),
 ("Xubilayxon saroyida xizmat qilib, sayohat kitobi bilan yevropaliklarning tasavvurini boyitgan venetsiyalik.", "Marko Polo", "Marko Polo."),
 ("Angliyaning papaga soliq to‘lashiga qarshi chiqqan Oksford professori.", "Jon Viklif", "Jon Viklif."),
 ("«Men hamma maslahatchilarni otimning egarida olib yuraman» degan fransuz qiroli.", "Lyudovik XI", "Lyudovik XI."),
]

# ---------- Ha / Yo'q ----------
def hy(items):
    return [{"q": "Ha yoki Yo‘q?\n" + s, "a": ["Ha", "Yo‘q"], "c": 0 if ok else 1, "fx": 1, "e": e} for s, ok, e in items]
hy1 = hy([
 ("Shayboniylar Markaziy Osiyoda taxminan 100 yil hukmronlik qilgan.", True, "Ha: 1500–1601."),
 ("Bobur Panipat jangida 100 ming kishilik qo‘shin bilan 12 ming kishilik qo‘shinni yenggan.", False, "Yo‘q: aksincha, 12 ming kishi bilan 100 ming kishilik qo‘shinni yenggan."),
 ("Mir Arab madrasasi Buxorodagi Minorayi kalon qarshisida joylashgan.", True, "Ha."),
 ("Kaltaminor qurib bitkazilgan va 110 metr balandlikka yetgan.", False, "Yo‘q: 29 metrda qurilish to‘xtagan."),
 ("Ichan qal’a 1990-yildan YUNESKO jahon merosi ro‘yxatida.", True, "Ha."),
 ("Abdullaxon II butun Xorazmni 1593-yilda bo‘ysundirgan.", True, "Ha."),
 ("Mang‘itlar chingiziylar avlodi bo‘lgan.", False, "Yo‘q: shuning uchun hukmdor amir deb atalgan."),
 ("Qo‘qonda bosh vazir lavozimi Umarxon davrida mingboshi deb o‘zgartirilgan.", True, "Ha."),
 ("Qora o‘lat 1347–1351-yillarda Yevropa aholisining uchdan bir qismini qirib yuborgan.", True, "Ha."),
 ("Ilk birja 1406-yilda Venetsiyada tashkil etilgan.", False, "Yo‘q: Bryuggeda (hozirgi Belgiya)."),
 ("Gotika uslubi XII asrda paydo bo‘lgan.", True, "Ha."),
 ("Inklar davlatida yirik bozorlar bo‘lgan.", False, "Yo‘q: inklarda bozorlar bo‘lmagan."),
 ("Kartoshkaning ko‘plab turlari Yevropaga inklar yurtidan olib borilgan.", True, "Ha."),
 ("Marog‘a olimlari Yerning o‘z o‘qi atrofida aylanishini Kopernikdan 300 yil oldin isbotlagan.", True, "Ha – «Marog‘a inqilobi»."),
 ("Koreys fonetik alifbosi 33 harfdan iborat bo‘lgan.", False, "Yo‘q: 28 harfdan."),
 ("Subhonqulixon yozda non yuziga kunjut sepishni buyurgan.", True, "Ha."),
 ("Chor Minor 1807-yilda Samarqandda qurilgan.", False, "Yo‘q: Buxoroda."),
 ("Sherg‘ozixon madrasasida Ajiniyoz o‘qigan.", True, "Ha."),
 ("Qozoq xonligiga 1465–1466-yillarda asos solingan.", True, "Ha."),
 ("Qoraqalpoqlar 1811-yilda to‘la Buxoro amirligiga bo‘ysundirilgan.", False, "Yo‘q: Xiva xonligiga."),
])
hy2 = hy([
 ("Mansa Muso 1324-yilda haj ziyoratiga borgan.", True, "Ha."),
 ("Tenochtitlanga atsteklar 1521-yilda asos solgan.", False, "Yo‘q: 1325-yilda; 1521-yilda Kortes egallagan."),
 ("Salerno tibbiyot maktabi 1213-yilda universitet maqomini olgan.", True, "Ha."),
 ("«Karantin» so‘zi italyan tilida «o‘n kun» degani.", False, "Yo‘q: «qirq kun»."),
 ("Sorbonnada to‘rtta fakultet bo‘lgan.", True, "Ha: san’at, huquqshunoslik, tibbiyot, ilohiyot."),
 ("Lyubekda birinchi g‘ishtli gotika ibodatxonasi qurilgan.", True, "Ha, XIII asrda."),
 ("Renessans Fransiyada boshlangan.", False, "Yo‘q: Italiyada."),
 ("Ubaydullaxon 1708-yilda pul islohoti o‘tkazgan.", True, "Ha."),
 ("Nodirshoh qo‘shinlarining Buxoroga yurishi 1740-yilda boshlangan.", True, "Ha."),
 ("Toqi Zargaronda 36 ta zargarlik ustaxonasi bo‘lgan.", True, "Ha."),
 ("Xiva xonligi Buxoro xonligidan katta bo‘lgan.", False, "Yo‘q: Qo‘qon xonligi Xivadan besh baravar katta bo‘lgan."),
 ("Anushaxon hammomi xonalari yer ostida joylashtirilgan.", True, "Ha: issiqni saqlash uchun."),
 ("Arab Muhammadxon poytaxtni Xivadan Urganchga ko‘chirgan.", False, "Yo‘q: Urganchdan Xivaga."),
 ("1831-yilgi Qo‘qon–Pekin shartnomasi Koshg‘ar savdosini Qo‘qon nazoratiga bergan.", True, "Ha."),
 ("Oqmasjidni 1853-yilda Perovskiy bosib olgan.", True, "Ha."),
 ("Jiyen jirov XIX asr oxirida tug‘ilgan.", False, "Yo‘q: 1730–1784-yillarda yashagan."),
 ("Dunyoda ilk temiryo‘l 1825-yilda qurilgan.", True, "Ha."),
 ("Amir Temur qurdirgan minora qarshisida Abdullaxon II 1582-yilda masjid qurdirgan.", True, "Ha."),
 ("Samarqanddagi Chorsu olti yo‘lakli bo‘lib, bu shahar darvozalari soniga ishora.", True, "Ha."),
 ("Kuloh – kigizdan konus shaklida tikilgan bosh kiyim.", True, "Ha."),
])

# ---------- Yozma ----------
def wz(items):
    return [{"q": q, "w": w, "e": e} for q, w, e in items]
yz1 = wz([
 ("Bobur qaysi shaharda tug‘ilgan?", ["Andijon"], "Andijon, 1483-yil 14-fevral."),
 ("Shayboniylar davlati 1533-yildan qanday nom bilan atalgan? (… xonligi)", ["Buxoro xonligi", "Buxoro"], "Buxoro xonligi."),
 ("Boburning mashhur memuar asari qanday ataladi?", ["Boburnoma"], "«Boburnoma»."),
 ("Xiva xonligiga 1511-yilda kim asos solgan?", ["Elbarsxon", "Elbars"], "Elbarsxon."),
 ("Qo‘qon xonligida bosh vazir lavozimi qanday atalgan (Umarxondan keyin)?", ["mingboshi"], "Mingboshi."),
 ("Xivadagi tugallanmagan, butunlay koshin bilan qoplangan minora nomi?", ["Kaltaminor", "Kalta minor"], "Kaltaminor."),
 ("Gulxaniyning mashhur nasriy asari qanday ataladi?", ["Zarbulmasal"], "«Zarbulmasal»."),
 ("Atsteklarning «suzuvchi dalalari» qanday atalgan?", ["chinampa"], "Chinampa."),
 ("Inklar yozuv o‘rnida foydalangan tugunli xatlar nomi?", ["kipu"], "Kipu."),
 ("Bosma mashinani 1445-yilda kim ixtiro qilgan? (familiyasi)", ["Gutenberg", "Iogann Gutenberg"], "Iogann Gutenberg."),
 ("Mali davlatining poytaxti qaysi shahar?", ["Niara"], "Niara."),
 ("Hunarmand yoki savdogarlar uyushmasi qanday atalgan?", ["gildiya"], "Gildiya."),
 ("Zodagonlarning qasrlari jamlangan hudud qanday atalgan?", ["manor"], "Manor."),
 ("«Renessans» so‘zi qanday tarjima qilinadi? (bir so‘z)", ["uyg‘onish", "uygonish", "qayta tiklanish"], "Uyg‘onish."),
 ("Samarqanddagi olti qirrali Chorsu o‘sha davrda qanday atalgan?", ["Toqi musaddas"], "Toqi musaddas."),
])
yz2 = wz([
 ("Mang‘itlar sulolasi Buxoroda qaysi yilda hokimiyatga kelgan?", ["1756"], "1756-yilda."),
 ("Qo‘qon xonligi qaysi yilda tashkil topgan?", ["1709"], "1709-yilda."),
 ("Panipat jangi qaysi yilda bo‘lgan?", ["1526"], "1526-yil aprel."),
 ("Ichan qal’a qaysi shaharda joylashgan?", ["Xiva"], "Xiva."),
 ("Qoraqalpoq xalq adabiyotining asoschisi kim? (taxallusi)", ["Berdaq"], "Berdaq."),
 ("Umarxonning she’riy taxallusi qanday?", ["Amiriy"], "Amiriy."),
 ("Abulg‘ozi Bahodirxonning turkiy qabilalar shajarasi haqidagi asari?", ["Shajarayi turk", "Shajarai turk"], "«Shajarayi turk»."),
 ("Xiva xonligida bosh vazir qanday atalgan?", ["mehtar"], "Mehtar."),
 ("Buxoro amirligida bosh vazir qanday atalgan?", ["qushbegi"], "Qushbegi."),
 ("Qora o‘lat (bubon vabosi) nimadan tarqalgan? (bir so‘z)", ["kalamush", "kalamushlar", "qora kalamushlar"], "Qora kalamushlardan."),
 ("1250-yilda Ayyubiylarni ag‘dargan sulola nomi?", ["Mamluklar", "mamluk"], "Mamluklar."),
 ("Yevropada eng muhim o‘rta asr fani qaysi edi?", ["ilohiyot", "teologiya"], "Ilohiyot (teologiya)."),
 ("Atsteklarni 1521-yilda tor-mor etgan konkistador kim? (familiyasi)", ["Kortes", "Ernan Kortes"], "Ernan Kortes."),
 ("Toshkent hokimiga 1831-yilda berilgan unvon?", ["beklarbegi"], "Beklarbegi."),
 ("Ajiniyozning taxallusi?", ["Zevar"], "Zevar."),
])

# ---------- Fleshkard ----------
FL = [
 ("«Men hamma maslahatchilarni otimning egarida olib yuraman»", "Lyudovik XI (Fransiya qiroli)"),
 ("«Qirol davlatni papa nomidan emas, balki Xudoning nomi bilan boshqaradi»", "Jon Viklif (Oksford professori)"),
 ("«Biz jaklar qiroliga shunday tarzda toj kiydiramiz»", "Fransuz zodagonlari – Gilyom Kalni mazax qilib"),
 ("«Mo‘g‘ullarni biz o‘zimizga singdirib yuboramiz»", "Xitoylik – Marko Polo ma’lumotiga ko‘ra"),
 ("«Samarqandning yana bir matosi qirmizi baxmaldirki, uni atrof va yiroq-yaqinlarga eltadilar»", "Zahiriddin Muhammad Bobur"),
 ("«Samarqand shahri ajoyib orasta bir shahardir… har hunarmandning alohida bozori bor»", "Zahiriddin Muhammad Bobur («Boburnoma»)"),
 ("«O‘zbakning urushda bir ulug‘ hunari ushbu to‘lg‘amadir»", "Zahiriddin Muhammad Bobur («Boburnoma»)"),
 ("«Ayniqsa, hammomlar shunday ko‘rkam qurilganki, bunaqasi dunyoning hech qayerida yo‘q»", "Antoni Jenkinson (ingliz sayyohi, 1558)"),
 ("«Shaharda har yili Hindiston, Eron, Balx, Rossiya… savdogarlarning yig‘ilishi bo‘ladi»", "Antoni Jenkinson (Buxoro haqida)"),
 ("«Madrasalar toliblari orasida Erondan tashqari hamma mamlakatlar kishilarini uchratish mumkin»", "Aleksandr Byorns (ingliz elchisi)"),
 ("«Buxoroning ko‘ylak bozori serhasham kiyim bilan Xitoy Tatariyasiga qadar barcha musulmonlarni ta’minlaydi»", "Arminiy Vamberi (vengriyalik sayyoh, 1863)"),
 ("«Xivada bor-yo‘g‘i 40 oiladan iborat aholi tirik qoldi…»", "Munis Xorazmiy"),
 ("«Ko‘p tosh to‘plasinlar» (1582-yil, yodgorlik masjidi uchun)", "Abdullaxon II – Hofiz Tanish Buxoriy yozib qoldirgan"),
 ("«Bobur podshoh Samarqand qamali paytida opasi Xonzodabegimni… Shayboniyxonga berib, o‘zi chiqib ketgan edi»", "Mirzo Muhammad Haydar («Tarixi Rashidiy»)"),
 ("«Endilikda biz tomonlarga hech qayerdan to‘kinlik bo‘lsin»", "Sibirdagi Rossiya fuqarolari – podshoga murojaat"),
 ("«Tasvir savodsizlar uchun adabiyotdir»", "O‘rta asrlar Yevropasi iborasi"),
]
AUTH = sorted(set(b for a, b in FL))
fl_test = mc([("Kim aytgan yoki yozgan?\n" + a, b, b) for a, b in FL], AUTH)

S = {
 "qz_davlat": {"topics": [{"id": "qz_davlat1", "title": "1-to‘plam", "questions": mc(dav1, DAV)},
                          {"id": "qz_davlat2", "title": "2-to‘plam", "questions": mc(dav2, DAV)}]},
 "qz_tshaxs": {"topics": [{"id": "qz_tshaxs1", "title": "1-to‘plam", "questions": mc(shx1, SHX)},
                          {"id": "qz_tshaxs2", "title": "2-to‘plam", "questions": mc(shx2, SHX)}]},
 "qz_hayoq": {"topics": [{"id": "qz_hayoq1", "title": "1-to‘plam", "questions": hy1},
                         {"id": "qz_hayoq2", "title": "2-to‘plam", "questions": hy2}]},
 "qz_yozma": {"topics": [{"id": "qz_yozma1", "title": "1-to‘plam", "questions": yz1},
                         {"id": "qz_yozma2", "title": "2-to‘plam", "questions": yz2}]},
 "qz_flesh": {"cards": [[a, b] for a, b in FL],
              "topics": [{"id": "qz_flesh1", "title": "Kim aytgan? – test", "questions": fl_test}]},
}
p = os.path.join(ROOT, "questions.json")
d = json.load(open(p, encoding="utf-8"))
d["sections"].update(S)
open(p, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, separators=(",", ":")))
for k, v in S.items():
    print(k, sum(len(t["questions"]) for t in v["topics"]), len(v.get("cards", [])))
