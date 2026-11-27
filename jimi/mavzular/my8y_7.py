from qlib import Topic, PLACES, REG
TOPICS = {}

# 21 Osiyo, Afrika va Amerika xalqlari iqtisodiy hayoti
t = Topic('y8j21', 8021); TOPICS['y8j21'] = t
t.B("XIII asrda Osiyoda ulkan iqtisodiy inqirozni nima yuzaga keltirdi?", "mo‘g‘ullarning harbiy yurishlari", "qora o‘lat", "salib yurishlari", "zilzilalar", "Mo‘g‘ul bosqinlari.")
t.B("Mo‘g‘ullar savdo ishida kimlardan unumli foydalangan?", "turkistonlik savdogarlardan", "venetsiyalik savdogarlardan", "arab dengizchilaridan", "yapon savdogarlaridan", "Turkistonlik savdogarlardan.")
t.B("Yaponiya Xitoydan nimalarni olib kelgan?", "harbiy qurollar, ipak, paxta, mis", "oltin va tuz", "kartoshka va kakao", "lama juni", "Qurollar, ipak mato, paxta, mis.")
t.B("XIII–XIV asrlarda Yaponiyada qaysi shaharlarda yirik portlar paydo bo‘lgan?", "Suruga, Xakata, Osaka", "Kioto, Kamakura, Nara", "Pekin, Nankin, Guanchjou", "Kusko, Tenochtitlan", "Suruga, Xakata va Osaka.")
t.B("1307-yilda savdo kemalarini Fors ko‘rfaziga kim boshlab borgan?", "Suy Yangchyuy", "Van Dayuan", "Chjan Xe", "Marko Polo", "Suy Yangchyuy.")
t.B("1334-yilda Arabiston yarimoroliga savdo kemalari kim rahbarligida yuborilgan?", "Van Dayuan", "Suy Yangchyuy", "Chjan Xe", "Xubilay", "Van Dayuan.")
t.B("Min sulolasi davrida yetti marta dengiz safariga chiqqan kim?", "Chjan Xe", "Van Dayuan", "Suy Yangchyuy", "Marko Polo", "Chjan Xe.")
t.B("Min sulolasi davrida qaysi yirik hunarmandchilik tarmog‘i yuzaga kelgan?", "chinni ishlab chiqarish", "temir eritish", "gilam to‘qish", "kemasozlik", "Chinni ishlab chiqarish.")
t.B("Gana imperiyasi qaysi daryolar o‘rtasida joylashgan?", "Niger va Senegal", "Nil va Kongo", "Zambezi va Limpopo", "Niger va Nil", "Niger va Senegal daryolari o‘rtasida.")
t.B("Ganaga tuz qayerdan kelgan?", "shimoldagi Sahrodan", "Gvineya ko‘rfazidan", "Nil bo‘yidan", "Arabistondan", "Shimoldagi Sahrodan.")
t.B("Gananing poytaxti qaysi shahar?", "Kumbi Sale", "Niara", "Gao", "Tombuktu", "Kumbi Sale.")
t.B("Mansa Muso qachon haj ziyoratiga borgan?", "1324-yilda", "1312-yilda", "1337-yilda", "1076-yilda", "1324-yilda.")
t.B("Mansa Muso hajga ketayotib qancha oltinni hadya qilgan?", "300 pud", "30 pud", "3000 pud", "100 pud", "300 pud oltin.")
t.B("Atsteklarning «suzuvchi dalalari» qanday atalgan?", "chinampa", "mita", "akveduk", "tlatoani", "Chinampa.")
t.B("Tenochtitlanni qirg‘oq bilan nechta keng yo‘l bog‘lagan?", "uchta", "bitta", "to‘rtta", "yettita", "Uchta.")
t.B("Inklarda fuqarolarning soliq o‘rniga mehnat majburiyati qanday atalgan?", "mita", "chinampa", "veksel", "o‘lpon", "Mita tizimi.")
t.B("Inklar eng baland tog‘larda go‘sht va jun olish uchun qaysi hayvonni boqqan?", "lama", "qo‘y", "ot", "tuya", "Lamalarni.")
t.NAT("Mo‘g‘ullar Buyuk ipak yo‘li savdosining ahamiyatini tushunib, savdo yo‘llari xavfsizligini ta’minladi.", "ichki va tashqi savdo rivojlanib, davlat daromadi oshdi", "savdo butunlay to‘xtadi", "Buxoro vayron bo‘ldi", "dengiz savdosi taqiqlandi", "Savdo jonlandi.")
t.NAT("Gana shimol va janub savdo yo‘llarini nazorat qildi.", "mamlakat haddan tashqari boyib ketdi", "Gana qashshoqlashdi", "savdo yo‘llari yopildi", "Gana Malini bosib oldi", "Gana boyidi.")
t.NAT("Mansa Muso hajga ketayotib 300 pud oltin hadya qildi.", "Mali butun Afrika, Osiyo va Yevropada mashhur bo‘ldi", "Mali xazinasi bo‘shab, davlat parchalandi", "oltin savdosi to‘xtadi", "Muso taxtdan ag‘darildi", "Mali shuhrat qozondi.")
t.NAT("Tenochtitlan orolda joylashgani uchun dehqonchilik yerlari juda kam edi.", "atsteklar chinampa – «suzuvchi dalalar»ni ixtiro qildi", "atsteklar dehqonchilikdan voz kechdi", "poytaxt ko‘chirildi", "inklar yerini bosib oldi", "Chinampalar yaratildi.")
t.TF("Ganada oltin va tuz «so‘zsiz» ayirboshlangan.", True, "To‘g‘ri: oltin konlari joyini sir saqlash uchun.")
t.TF("Inklar davlatida yirik bozorlar bo‘lgan.", False, "Noto‘g‘ri: inklarda bozorlar bo‘lmagan.")
t.TF4([("Tenochtitlanni o‘rab turgan ko‘l suvi iste’molga yaroqsiz bo‘lgan.", True), ("Chinampalardan yil davomida hosil olingan.", True),
       ("Mansa Muso davrida Tombuktu, Gao, Jenne yuksalgan.", True), ("Kulolchilik buyumlari asosan tashqi bozor uchun ishlab chiqarilgan.", False)],
      "4-noto‘g‘ri: ular asosan ichki bozor uchun ishlab chiqarilgan.")
t.MUL([("Mo‘g‘ul bosqiniga uchragan hududlar yarim asrdan ortiq tanazzulga yuz tutgan.", True),
       ("Inklar iliq vodiylarda makkajo‘xori, salqin tog‘larda kartoshka yetishtirgan.", True),
       ("Atsteklar poytaxtga suvni ko‘ldan to‘g‘ridan to‘g‘ri ichish uchun olgan.", False)],
      "III noto‘g‘ri: ko‘l suvi yaroqsiz, suvo‘tkazgich va kanallar qurilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Suy Yangchyuy kemalari Fors ko‘rfaziga bordi", "Mansa Muso hajga bordi", "Van Dayuan kemalari Arabistonga yuborildi", "Chjan Xe dengiz safarlari"],
      "1307 → 1324 → 1334 → Min sulolasi davri.")
t.MATCH("Atamalarni izohi bilan moslashtiring.", ["chinampa", "mita", "«so‘zsiz» ayirboshlash", "Kumbi Sale"],
        ["atsteklarning suzuvchi dalalari", "inklarning mehnat majburiyati", "oltin va tuzni bevosita aloqasiz almashish", "Gana poytaxti", "Mali poytaxti"], 'abcd',
        "Chinampa – atsteklar; mita – inklar; so‘zsiz savdo – Gana; Kumbi Sale – Gana poytaxti.")
t.VENN("Atsteklar", "Inklar",
       [("chinampa – suzuvchi dalalar", 1), ("poytaxtda ulkan bozor bo‘lgan", 1),
        ("mita tizimi, bozorlar bo‘lmagan", 2), ("lamalarni boqqan", 2),
        ("bosib olingan hududlar yutuqlarini o‘zlashtirgan", 3)],
       "Atsteklar – chinampa, bozor; inklar – mita, lama; umumiy – o‘zlashtirish.")
t.MAPMATCH('africa', ['Kumbi Sale', 'Gao', 'Misr (Afrika)', 'Buyuk Zimbabve'],
           ["Gana poytaxti", "Mansa Muso davrida yuksalgan savdo shahri", "Mansa Muso haj yo‘lida o‘tgan, Mamluklar mamlakati", "Monomotapa poytaxti"],
           "1 – Kumbi Sale; 2 – Gao; 3 – Misr; 4 – Buyuk Zimbabve.")

# 22 Yevropada ilm-fan
t = Topic('y8j22', 8022); TOPICS['y8j22'] = t
t.B("O‘rta asrlarda eng muhim fan qaysi bo‘lgan?", "ilohiyot (teologiya)", "alkimyo", "astronomiya", "tibbiyot", "Ilohiyot.")
t.B("Cherkov talqiniga ko‘ra olamning markazida nima joylashgan?", "Yer", "Quyosh", "Oy", "Rim", "Yer.")
t.B("Yer qanday shaklda deb taxmin qilingan?", "okean bilan o‘ralgan g‘ildirak", "shar", "kub", "tuxum", "Okean bilan o‘ralgan g‘ildirak.")
t.B("Marko Polo qaysi shahardan bo‘lgan savdogar?", "Venetsiya", "Genuya", "Florensiya", "Rim", "Venetsiyalik.")
t.B("Xitoyda Marko Poloni kim iliq kutib olgan?", "Xubilayxon", "Chingizxon", "Chjan Xe", "Temur", "Xubilayxon.")
t.B("Marko Polo Osiyoda necha yildan ortiq sayohat qilgan?", "20 yildan ortiq", "5 yil", "50 yil", "2 yil", "20 yildan ortiq.")
t.B("«Yetti erkin san’at»ning birinchi bosqichi qanday atalgan?", "trivium", "kvadrivium", "fakultet", "magistratura", "Trivium.")
t.B("Kvadriviumda qaysi fanlar o‘qitilgan?", "arifmetika, geometriya, astronomiya, musiqa", "grammatika, ritorika, dialektika", "ilohiyot va huquq", "tibbiyot va alkimyo", "Arifmetika, geometriya, astronomiya, musiqa.")
t.B("Yevropadagi eng katta oliy ta’lim muassasasi qaysi bo‘lgan?", "Sorbonna", "Oksford", "Bolonya", "Salerno", "Sorbonna universiteti.")
t.B("Sorbonnada nechta fakultet bo‘lgan?", "to‘rtta", "yettita", "ikkita", "o‘nta", "San’at, huquqshunoslik, tibbiyot, ilohiyot.")
t.B("Ilohiyotni o‘rganish kamida necha yil davom etgan?", "8 yil", "4 yil", "5–6 yil", "12 yil", "Kamida 8 yil.")
t.B("XV asrga kelib Yevropada nechta universitet bo‘lgan?", "80 ta", "20 ta", "200 ta", "8 ta", "80 ta.")
t.B("Qaysi universitetda huquqdan eng yaxshi dars berilgan?", "Bolonya", "Oksford", "Salerno", "Sorbonna", "Bolonyada.")
t.B("Universitetda o‘qitish qaysi tilda olib borilgan?", "lotin", "fransuz", "yunon", "ingliz", "Lotin tilida.")
t.B("XIII asr o‘rtalarida Arastu falsafasi va xristianlikni tadqiq qilgan kim?", "Foma Akvinskiy", "Rojer Bekon", "Luka Pacholi", "Buyuk Albert", "Foma Akvinskiy.")
t.B("Birinchi optik linzalarni yaratish tajribasini kim o‘tkazgan?", "Rojer Bekon", "Foma Akvinskiy", "Gutenberg", "Luka Pacholi", "Rojer Bekon.")
t.B("«Ilohiy nisbat to‘g‘risida» asari muallifi kim?", "Luka Pacholi", "Rojer Bekon", "Buyuk Albert", "Marko Polo", "Luka Pacholi.")
t.B("«Nibelunglar qo‘shig‘i» qaysi mamlakatda yaratilgan?", "Germaniya", "Ispaniya", "Angliya", "Fransiya", "Germaniyada, XII asr.")
t.B("Germaniyada paydo bo‘lgan satirik adabiy janr qaysi?", "shvank", "fablio", "ballada", "epos", "Shvank (Fransiyada – fablio).")
t.B("Bosma mashinani kim va qachon ixtiro qilgan?", "Iogann Gutenberg, 1445-yil", "Rojer Bekon, 1250-yil", "Luka Pacholi, 1494-yil", "Marko Polo, 1295-yil", "1445-yilda Gutenberg.")
t.NAT("Marko Poloning sayohat kitobi chiqdi.", "yevropaliklarning Osiyoga qiziqishi ortdi, olam haqidagi tasavvurlari boyidi", "Yevropa Osiyo bilan aloqani uzdi", "cherkov ta’siri kuchaydi", "Venetsiya savdosi to‘xtadi", "Tasavvurlar kengaydi.")
t.NAT("Iqtisodiyot taraqqiy etdi, davlat boshqaruvi ehtiyojlari oshdi.", "yirik cherkov maktablari universitetlarga aylandi", "maktablar yopildi", "lotin tili taqiqlandi", "ilohiyot fani yo‘qoldi", "Universitetlar tashkil etildi.")
t.NAT("Alkimyogarlar oddiy metallni oltinga aylantiradigan moddani izladi.", "alkimyo zamonaviy kimyoning asosiga aylandi", "Yevropada oltin ko‘paydi", "alkimyo taqiqlandi", "fizika paydo bo‘ldi", "Kimyo asoslari yaratildi.")
t.NAT("1445-yilda bosma mashina ixtiro qilindi.", "ilm-fan rivojiga katta hissa qo‘shildi", "kitoblar qimmatlashdi", "qo‘lyozmalar ko‘paydi", "universitetlar yopildi", "Madaniy rivojlanish tezlashdi.")
t.TF("Universitet rektori o‘qituvchi va talabalarning umumiy yig‘ilishida saylangan.", True, "To‘g‘ri.")
t.TF("Ritorika diniy bayramlarni hisoblash uchun zarur fan hisoblangan.", False, "Noto‘g‘ri: bayramlarni astronomiya hisoblagan, ritorika – va’zlar uchun.")
t.TF4([("Oksfordda matematika va astronomiyadan eng yaxshi dars berilgan.", True), ("«Robin Gud haqida ballada» Angliyada XIV asrda paydo bo‘lgan.", True),
       ("«Sid haqida qo‘shiq» Germaniyada yaratilgan.", False), ("Kitoblar qimmat bo‘lgani uchun ijaraga olinib, qo‘lda ko‘chirilgan.", True)],
      "3-noto‘g‘ri: «Sid haqida qo‘shiq» – Ispaniya.")
t.MUL([("Kimyoga oid birinchi asarlarni Rojer Bekon va Buyuk Albert yozgan.", True),
       ("«Tulki haqida roman»da Renar ritsar bo‘ri Izengrim ustidan g‘alaba qozonadi.", True),
       ("Salamanka va Monpelyeda ilohiyot eng yaxshi o‘qitilgan.", False)],
      "III noto‘g‘ri: Salamanka, Monpelye, Salernoda tibbiyot o‘rgatilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["«Sid haqida qo‘shiq» paydo bo‘ldi", "Foma Akvinskiy ilohiyot asoslarini mustahkamladi", "«Robin Gud haqida ballada» paydo bo‘ldi", "Gutenberg bosma mashinani ixtiro qildi"],
      "XII asr → XIII asr o‘rtasi → XIV asr → 1445.")
t.MATCH("Asarlarni yaratilgan mamlakati bilan moslashtiring.", ["«Sid haqida qo‘shiq»", "«Nibelunglar qo‘shig‘i»", "«Robin Gud haqida ballada»", "«Atirgul haqida roman»"],
        ["Ispaniya", "Germaniya", "Angliya", "Fransiya", "Italiya"], 'abcd',
        "Sid – Ispaniya; Nibelunglar – Germaniya; Robin Gud – Angliya; Atirgul – Fransiya.")
t.VENN("Trivium", "Kvadrivium",
       [("grammatika", 1), ("ritorika", 1), ("arifmetika", 2), ("astronomiya", 2),
        ("«Yetti erkin san’at» bosqichi", 3)],
       "Trivium – grammatika, ritorika, dialektika; kvadrivium – arifmetika, geometriya, astronomiya, musiqa.")
t.MAPMATCH('europe', ['Bolonya', 'Parij', 'Oksford', 'Salamanka'],
           ["huquqdan eng yaxshi dars bergan Italiya universiteti", "ilohiyotchilarni tayyorlagan Sorbonna shahri", "matematika va astronomiya o‘qitilgan Angliya universiteti", "tibbiyot o‘rgatilgan Ispaniya universiteti"],
           "1 – Bolonya; 2 – Parij; 3 – Oksford; 4 – Salamanka.")
