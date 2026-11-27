"""Qiziqarli tarix: juftliklar (chap – o'ng) asosida o'rganish kartalari va testlar.

Foydalanish (repo ildizidan):  python3 jimi/qiziq.py
questions.json dagi sections.qz_yil / qz_obida / qz_shaxs / qz_atama ni qayta yozadi.
Manba: yangi darslik 7- va 10-sinf Jahon tarixi matnlari.
"""
import json, os, random
HERE = os.path.dirname(os.path.abspath(__file__))

YIL = [
 ("395-yil", "Rim imperiyasining G‘arbiy va Sharqiy qismlarga bo‘linishi"),
 ("410-yil", "Vestgotlar Alarix boshchiligida Rimni egallashi"),
 ("476-yil", "Odoakr so‘nggi imperator Romul Avgustulni taxtdan ag‘darishi"),
 ("496-yil", "Franklar qiroli Xlodvigning xristianlikni qabul qilishi"),
 ("570-yil", "Muhammad (s.a.v.)ning Makkada tavallud topishi"),
 ("622-yil", "Hijrat – Makkadan Yasribga (Madinaga) ko‘chish"),
 ("732-yil", "Puate jangi – Karl Martell arablarni to‘xtatishi"),
 ("751-yil", "Pipin Pakananing franklar qiroli deb e’lon qilinishi"),
 ("800-yil", "Buyuk Karlga Rimda imperatorlik tojining kiygizilishi"),
 ("843-yil", "Verden shartnomasi – Karl imperiyasining uchga bo‘linishi"),
 ("863-yil", "Kirill va Mefodiyning Moraviyaga kelishi"),
 ("882-yil", "Olegning Kiyevni egallab, Kiyev Rusiga asos solishi"),
 ("962-yil", "Otton I ning imperator deb e’lon qilinishi"),
 ("988-yil", "Rusda xristianlikning qabul qilinishi"),
 ("1054-yil", "Xristian cherkovining katolik va pravoslavga bo‘linishi"),
 ("1066-yil", "Gastings jangi – Vilgelm I ning Angliyani egallashi"),
 ("1071-yil", "Mansikert jangi – saljuqiylarning Vizantiya ustidan g‘alabasi"),
 ("1095-yil", "Papa Urban II ning Klermonda salib yurishiga chaqirishi"),
 ("1187-yil", "Salohiddin Ayyubiyning Quddusni qaytarib olishi"),
 ("1206-yil", "Temuchinning Onon bo‘yidagi qurultoyda ulug‘ xon deb e’lon qilinishi"),
 ("1258-yil", "Xulokuning Bag‘dodni egallashi – Arab xalifaligining barham topishi"),
 ("1260-yil", "Ayn-Jalut jangi – Sayfiddin Qutuzning mo‘g‘ullar ustidan g‘alabasi"),
 ("1871-yil", "Vilgelm I ning Versalda Germaniya imperatori deb e’lon qilinishi"),
 ("1885-yil", "Hindiston milliy kongressining tashkil topishi"),
 ("1914-yil 28-iyun", "Sarayevoda Frans Ferdinandning o‘ldirilishi"),
 ("1918-yil 11-noyabr", "Birinchi jahon urushining yakunlanishi"),
 ("1919-yil 28-iyun", "Germaniyaning Versal tinchlik shartnomasini imzolashi"),
 ("1922-yil 30-dekabr", "SSSRning tashkil topishi"),
 ("1923-yil 29-oktyabr", "Turkiyaning respublika deb e’lon qilinishi"),
 ("1929-yil 24-oktyabr", "Nyu-York fond birjasida jahon iqtisodiy inqirozining boshlanishi"),
 ("1939-yil 1-sentabr", "Ikkinchi jahon urushining boshlanishi"),
 ("1941-yil 22-iyun", "Germaniyaning SSSRga hujum qilishi"),
 ("1945-yil 24-oktyabr", "BMT Ustavining kuchga kirishi"),
 ("1947-yil 15-avgust", "Hindiston va Pokistonning mustaqil davlat sifatida tashkil topishi"),
 ("1949-yil 1-oktyabr", "Xitoy Xalq Respublikasining e’lon qilinishi"),
 ("1957-yil 4-oktyabr", "Yerning birinchi sun’iy yo‘ldoshining uchirilishi"),
 ("1960-yil", "«Afrika yili» – 17 ta Afrika davlatining mustaqillikka erishishi"),
 ("1961-yil 12-aprel", "Yuriy Gagarinning koinotga parvozi"),
 ("1966-yil yanvar", "«Toshkent deklaratsiyasi»ning imzolanishi"),
 ("1990-yil 3-oktyabr", "Yagona Germaniya davlatining tashkil topishi"),
]

OBIDA = [
 ("Ayo Sofiya", "532–537-yillarda Konstantinopolda qurilgan, gumbazi diametri 31,5 m bo‘lgan ibodatxona"),
 ("San-Vitale", "Yustinian davrida Ravennada (Italiya) bunyod etilgan ibodatxona"),
 ("Axen saroy kopellasi", "Buyuk Karl qurdirgan binolardan saqlanib qolgan yagona ibodatxona"),
 ("Kiyevdagi Avliyo Sofiya ibodatxonasi", "Yaroslav Donishmand bunyod ettirgan, hozirgacha saqlangan ibodatxona"),
 ("Ka’ba", "Makkadagi barcha musulmonlar uchun asosiy ziyoratgoh"),
 ("Al-Hamro saroyi", "Ispaniyaning Granada shahridagi xalifalik davri me’morchilik durdonasi"),
 ("Ismoil Somoniy maqbarasi", "Buxorodagi Arab xalifaligi davri me’morchilik durdonasi"),
 ("Hasan masjidi", "Misrning Qohira shahridagi mashhur masjid"),
 ("Qutb Minor", "Dehlidagi masjidning 70 metrlik minorasi"),
 ("Ajanta ibodatxonasi", "Qoyaga o‘yib ishlangan, 29 xonadan iborat buddaviylik ibodatxonasi"),
 ("Oltin pavilion", "Tomi yupqa oltin plastinalar bilan yopilgan mashhur yapon pavilioni"),
 ("Buyuk Xitoy devori", "Xitoycha «Changcheng» – «uzun devor», sayyoramizdagi eng uzun devor"),
 ("Machu-Pikchu", "Perudagi baland tog‘da joylashgan inklarning yo‘qolgan shahri"),
 ("Chichen-Itsa", "Mayyalar poytaxti, unda rasadxona qurilgan"),
 ("Tenochtitlan", "Asteklar XII asrda ko‘l o‘rtasidagi orollarda barpo etgan shahar"),
 ("Kusko", "Inklar Urubamba daryosi havzasida asos solgan poytaxt"),
 ("Xori monastiri", "Mozaika va freskalari bilan mashhur, hozirgi Istanbuldagi Qahriya masjidi"),
 ("Buyuk kanal", "Xitoyda Xuanxe va Yanszi daryolarini birlashtirgan inshoot"),
 ("Bayt ul-hikma", "Bag‘doddagi «Donishmandlik uyi», 400 ming jildli kutubxonaga ega ilm dargohi"),
 ("Al-Azhar", "X asrda Qohirada tashkil etilgan ilm dargohi"),
 ("Zaytuna", "VIII asrda Tunisda tashkil etilgan ilm dargohi"),
 ("Qaroviyun", "Fes (Marokash) shahridagi ilm dargohi"),
 ("Magnavr oliy maktabi", "IX asrda Konstantinopolda ochilgan oliy maktab"),
 ("Boloniya universiteti", "Italiyadagi Yevropaning dastlabki universitetlaridan biri"),
 ("Versal saroyi", "1871-yilda Vilgelm I imperator deb e’lon qilingan va 1919-yilgi tinchlik konferensiyasi o‘tgan saroy"),
 ("Berlin devori", "Balandligi 3,6 m, uzunligi 106 km bo‘lgan, sovuq urush ramzi"),
 ("Reyxstag", "1945-yilda ustiga sovetlarning qizil bayrog‘i o‘rnatilgan Germaniya parlamenti binosi"),
 ("Kamelot qal’asi", "Afsonaga ko‘ra, qirol Arturning davra stoli joylashgan qal’a"),
 ("Qoraqurum", "Chingizxon davlatining poytaxti bo‘lgan qal’a"),
 ("Kordova masjidi", "Ispaniyadagi Arab xalifaligi davri me’morchilik durdonasi"),
]

SHAXS = [
 ("Xlodvig", "Franklar qirolligiga va Merovinglar sulolasiga asos solgan"),
 ("Karl Martell", "732-yilgi Puate jangida arablarni to‘xtatgan, benefitsiy islohotini o‘tkazgan"),
 ("Buyuk Karl", "800-yilda imperator bo‘lgan, «Yangi Rim imperiyasi»ga asos solgan"),
 ("Buyuk Alfred", "Normannlar hujumini qaytargan, «Anglosakson solnomasi»ni tuzdirgan ingliz qiroli"),
 ("Vilgelm I (Normandiya gersogi)", "1066-yilda Gastings jangida g‘alaba qozonib, Angliya qiroli bo‘lgan"),
 ("Otton I", "955-yilda vengerlarni yengib, 962-yilda imperator deb e’lon qilingan"),
 ("Fridrix I Barbarossa", "Shtaufenlar sulolasining mashhur vakili, 1176-yilda Lenyanoda mag‘lub bo‘lgan"),
 ("Yustinian I", "Vizantiyani qudrat cho‘qqisiga olib chiqqan, Ayo Sofiyani qurdirgan imperator"),
 ("Kirill va Mefodiy", "Slavyan alifbosini yaratib, Injilni slavyan tiliga tarjima qilgan"),
 ("Yaroslav Donishmand", "«Rus haqiqati» qonunlarini tuzdirgan, Yaroslavl shahriga asos solgan"),
 ("To‘g‘rulbek", "1038-yilda Saljuqiylar davlatiga asos solgan"),
 ("Nizomulmulk", "Saljuqiylarning mashhur bosh vaziri, «Siyosatnoma» muallifi"),
 ("Chingizxon", "1206-yilda ulug‘ xon deb e’lon qilingan, Qoraqurumni poytaxt qilgan"),
 ("Sayfiddin Qutuz", "1260-yilda Ayn-Jalutda mo‘g‘ullarni yenggan «Mo‘g‘ullar g‘olibi»"),
 ("Salohiddin Ayyubiy", "Ayyubiylar davlatini tuzgan, 1187-yilda Quddusni qaytarib olgan"),
 ("Muhammad al-Xorazmiy", "Algebra faniga asos solgan vatandoshimiz"),
 ("Ahmad al-Farg‘oniy", "Damashq rasadxonasida yangicha zij yaratishga rahbarlik qilgan"),
 ("Abu Rayhon Beruniy", "Yerning meridian aylanasi uzunligini hisoblab chiqqan"),
 ("Abu Ali ibn Sino", "«Al-qonun fit-tib» asari muallifi, Yevropada Avitsenna deb atalgan"),
 ("Marko Polo", "17 yilini Xubilay saroyida o‘tkazib, Sharq o‘lkalarini kitobida tasvirlagan venetsiyalik"),
 ("Xarsha", "Buddaviylikni qabul qilgan, shoir va dramaturg bo‘lgan hind imperatori"),
 ("Kalidasa", "Pyesalari ko‘plab tillarga o‘girilgan buyuk hind dramaturgi"),
 ("Bismark", "Germaniyani birlashtirishni uddalagan davlat arbobi"),
 ("Vudro Vilson", "Millatlar Ligasi tashabbuskori, «yangi erkinlik» dasturi muallifi"),
 ("Mustafo Kamol Otaturk", "Turkiya Respublikasining birinchi prezidenti, xalifalikni tugatgan"),
 ("Sun Yatsen", "Sinxay inqilobiga boshchilik qilgan, Gomindan partiyasiga asos solgan"),
 ("Mahatma Gandi", "Zo‘ravonliksiz qarshilik taktikasini ishlab chiqqan Hindiston milliy harakati yetakchisi"),
 ("Franklin Ruzvelt", "AQSHda «yangi kurs»ni amalga oshirgan prezident"),
 ("Konrad Adenauer", "GFRning birinchi kansleri"),
 ("Lyudvig Erhard", "«Nemis iqtisodiy mo‘jizasining tan olingan otasi»"),
 ("Margaret Tetcher", "Buyuk Britaniya tarixida hukumatni boshqargan birinchi ayol"),
 ("Martin Lyuter King", "Fuqarolar tengligi uchun harakat rahbari, tinchlik bo‘yicha Nobel mukofoti laureati"),
 ("Nelson Mandela", "JAR tarixidagi birinchi qora tanli prezident"),
 ("Yuriy Gagarin", "1961-yilda «Vostok» kemasida dunyoda birinchi bo‘lib koinotga parvoz qilgan"),
 ("Rabindranath Thakur", "«Gitanjali» turkumi uchun 1913-yilda Nobel mukofotini olgan hind adibi"),
 ("Jon Keyns", "Makroiqtisodiyot asoschisi bo‘lgan ingliz iqtisodchisi"),
]

ATAMA = [
 ("Konung", "German qabilasi boshlig‘i, zodagonlarning oliy vakili"),
 ("Drujina", "Germanlar va slavyanlardagi harbiy bo‘linma"),
 ("Benefitsiy", "Harbiy xizmat sharti bilan muddatga berilgan yer"),
 ("Feod", "Harbiy xizmat sharti bilan berilgan merosiy yer-mulk"),
 ("Marka", "Chegara viloyati"),
 ("Vasilevs", "Vizantiya imperatori unvoni («podsho»)"),
 ("Numisma", "Ishonchli xalqaro pul bo‘lgan Vizantiya oltin tangasi"),
 ("Hijrat", "«Ko‘chib o‘tish» – musulmon yil hisobining boshlanishi"),
 ("Xalifa", "«O‘rinbosar» – Arab xalifaligi rahbari"),
 ("Mazhab", "«Yo‘nalish», «oqim» – diniy masalada ulamo fikriga ergashish"),
 ("Ulus", "Chingizxon farzandlariga bo‘lib berilgan hudud («davlat», «xalq»)"),
 ("Keshik", "Chingizxonning maxsus gvardiyasi"),
 ("Grass", "Hindistonda doimiy harbiy xizmat sharti bilan in’om etilgan yer"),
 ("Patta", "Hindistonda ma’lum xizmat muddatiga berilgan «yorliqqa olingan yer»"),
 ("Busido", "Samuraylar hayotini belgilagan yozilmagan qonun"),
 ("Kipu", "Inklarning «tugunli xati»"),
 ("Indulgensiya", "Gunohlarni kechish uchun sotilgan yorliq («afv»)"),
 ("Interdikt", "Ibodat va marosimlarni vaqtincha taqiqlash – cherkovning eng og‘ir jazosi"),
 ("Inkvizitsiya", "Yeretiklarni qidiruvchi cherkov sudi («qidiruv»)"),
 ("Selebat", "Katolik ruhoniylarining uylanishini taqiqlash"),
 ("Sex", "Bir xil kasb egalarini birlashtirgan hunarmandlar uyushmasi"),
 ("Ratusha", "O‘rta asr Yevropa shahrida shahar kengashi binosi"),
 ("Mayorat", "Meros faqat katta o‘g‘ilga qoldirilish tizimi"),
 ("Dominion", "Ingliz qirolini davlat boshlig‘i deb tan oladigan imperiya tarkibidagi davlat"),
 ("Anneksiya", "Boshqa davlat hududini egallab olish yoki qo‘shib olish siyosati"),
 ("Samoderjaviye", "Rossiyada podshoning cheklanmagan mustabid hokimiyati"),
 ("Sekulyarlik", "Hukumat dinning har qanday turidan alohida bo‘lishi kerakligi haqidagi tushuncha"),
 ("Mandat", "Ma’lum hududni boshqarish vakolatini tasdiqlovchi hujjat"),
 ("Intervensiya", "Bir davlatning boshqa davlat ichki ishlariga zo‘rlik bilan aralashuvi"),
 ("Izolyatsionizm", "Boshqa davlatlar ishlariga aralashmaslikka asoslangan tashqi siyosat"),
 ("Okkupatsiya", "Boshqa davlat yerlarini qurolli kuchlar bilan vaqtincha egallab turish"),
 ("Referendum", "Muhim masalalar bo‘yicha fuqarolarning bevosita ovoz berishi"),
 ("Natsionalizatsiya", "Xususiy mulkni davlat mulkiga aylantirish"),
 ("Avtarkiya", "Boshqa mamlakatlar bilan aloqadan uzilgan, o‘zini o‘zi ta’minlovchi xo‘jalik"),
 ("Aparteid", "Irqiy kamsitishning eng ashaddiy ko‘rinishi"),
 ("Genotsid", "Aholi guruhlarini irqi, millati yoki diniga ko‘ra qirib yuborish jinoyati"),
 ("Sanksiya", "Xalqaro huquqni buzgan davlatga qo‘llanadigan jazo yoki ta’sir chorasi"),
 ("Harbiy xunta", "Davlat to‘ntarishi orqali hokimiyatga kelgan harbiylar hokimiyati"),
]

CATS = [
 ('qz_yil', YIL, "{l} yilda qanday voqea sodir bo‘lgan?", "«{r}» qachon sodir bo‘lgan?"),
 ('qz_obida', OBIDA, "«{l}» haqida qaysi ma’lumot to‘g‘ri?", "Ta’rifga mos tarixiy obidani toping:\n{r}"),
 ('qz_shaxs', SHAXS, "{l} qanday ish qilgan?", "Ta’rifga mos tarixiy shaxsni toping:\n{r}"),
 ('qz_atama', ATAMA, "«{l}» atamasining izohi qaysi?", "Izohga mos atamani toping:\n{r}"),
]

def build():
    out = {}
    for key, pairs, ql, qr in CATS:
        R = random.Random(key)
        assert len({l for l, _ in pairs}) == len(pairs) and len({r for _, r in pairs}) == len(pairs), key
        order = list(range(len(pairs))); R.shuffle(order)
        nt = -(-len(pairs) // 20); per = -(-len(pairs) // nt)
        topics = []
        for ti in range(0, len(order), per):
            chunk = order[ti:ti + per]
            qs = []
            for n, i in enumerate(chunk):
                l, r = pairs[i]
                others = [j for j in range(len(pairs)) if j != i]
                w = R.sample(others, 3)
                if n % 2 == 0:
                    q = {'q': ql.format(l=l), 'a': [r] + [pairs[j][1] for j in w], 'c': 0, 'e': f'{l} — {r}.'}
                else:
                    q = {'q': qr.format(r=r), 'a': [l] + [pairs[j][0] for j in w], 'c': 0, 'e': f'{l} — {r}.'}
                qs.append(q)
            topics.append({'id': f'{key}{ti // per + 1}', 'title': f'{ti // per + 1}-to‘plam', 'questions': qs})
        out[key] = {'cards': [[l, r] for l, r in pairs], 'topics': topics}
    return out

if __name__ == '__main__':
    f = os.path.join(os.path.dirname(HERE), 'questions.json')
    d = json.load(open(f, encoding='utf-8'))
    for k in ['qz_davlat', 'qz_hayoq', 'qz_yozma', 'qz_flesh']:
        d['sections'].pop(k, None)
    d['sections'].update(build())
    open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, separators=(',', ':')) + '\n')
    print({k: (len(v['cards']), [len(t['questions']) for t in v['topics']]) for k, v in build().items()})
