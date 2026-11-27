from qlib import Topic, PLACES, REG
TOPICS = {}

# 31 Ilm-fan va madaniyat
t = Topic('y10j31', 10031); TOPICS['y10j31'] = t
t.B("Ilmiy-texnik inqilob jahon iqtisodiyotini kapitalizmning qaysi davriga olib chiqqan?", "postindustrial davriga", "industrial davriga", "agrar davriga", "feodal davriga", "Postindustrial davriga.")
t.B("Ilmiy-texnik inqilobning salbiy oqibatlaridan biri qaysi?", "ish o‘rinlari kamayib, ishsizlik avj olgan", "sanoat robotlari yaratilgan", "konveyer liniyalari paydo bo‘lgan", "sintetik materiallar ishlab chiqarilgan", "Avtomatlashtirish natijasida ishsizlik avj oldi, tabiatga zarar ortdi.")
t.B("Mexanikaga asoslangan dunyoqarash kimdan boshlangan?", "Isaak Nyutondan", "Albert Eynshteyndan", "Maks Plankdan", "Jon Keynsdan", "Isaak Nyutondan.")
t.B("Fizikadan boshlangan ilmiy-texnik inqilob kimlarning nomi bilan bog‘liq?", "Maks Plank va Albert Eynshteyn", "Basov va Proxorov", "Kilbi va Noys", "Korolyov va Gagarin", "Maks Plank va Albert Eynshteyn.")
t.B("Kimyoviy bog‘lanishlarning tabiatini qaysi nazariya tushuntirib bergan?", "kvant nazariyasi", "nisbiylik nazariyasi", "xromosoma nazariyasi", "keynschilik", "Kvant nazariyasi.")
t.B("Lazer qachon yaratilgan?", "1960-yilda", "1957-yilda", "1969-yilda", "1959-yilda", "1960-yili.")
t.B("Lazerni yaratgan amerikalik olim kim?", "Ch. Tauns", "D. Kilbi", "R. Noys", "Jon Keyns", "Sovet fiziklari Basov, Proxorov va amerikalik Ch. Tauns.")
t.B("«Kompyuter» so‘zi ingliz tilida qanday ma’noni anglatadi?", "«hisoblagich»", "«yorug‘lik kuchaytirgich»", "«uzatgich»", "«xotira»", "Computer – «hisoblagich».")
t.B("Yarimo‘tkazgichli integral mikrosxemalarni kimlar yaratgan?", "D. Kilbi va R. Noys", "Basov va Proxorov", "Plank va Eynshteyn", "Nyuton va Keyns", "1959-yili amerikalik muhandislar D. Kilbi va R. Noys.")
t.B("Integral mikrosxemalar qachon yaratilgan?", "1959-yilda", "1960-yilda", "1969-yilda", "1957-yilda", "1959-yili.")
t.B("Uyali telefonlarni yaratish ustida 1940-yillar oxiridayoq ish boshlagan kompaniya qaysi?", "Shvetsiyaning «Televerket» kompaniyasi", "«Mitsubisi»", "«Aramko»", "«Sumitomo»", "Shvetsiyaning «Televerket» kompaniyasi.")
t.B("Internetning o‘tmishdoshi qanday atalgan?", "ARPANET", "MTA", "EHM", "Ericsson", "1969-yili yaratilgan ARPANET.")
t.B("Yerning birinchi sun’iy yo‘ldoshi qachon uchirilgan?", "1957-yil 4-oktyabrda", "1961-yil 12-aprelda", "1969-yilda", "1960-yilda", "1957-yil 4-oktyabr kuni Sovet Ittifoqida.")
t.B("Oyga kosmik kema uchirish tadqiqotlariga kim boshchilik qilgan?", "akademik S. P. Korolyov", "Y. A. Gagarin", "N. G. Basov", "A. M. Proxorov", "Akademik S. P. Korolyov.")
t.B("Y. A. Gagarin qaysi kosmik kemada koinotga parvoz qilgan?", "«Vostok»", "«Apollon-11»", "«Sputnik»", "«Soyuz»", "«Vostok» kosmik kemasida.")
t.B("Makroiqtisodiyotni yaratgan ingliz iqtisodchisi kim?", "Jon Keyns", "Daniel Bell", "Maks Plank", "Isaak Nyuton", "Jon Keyns; nazariyasi keynschilik nomini oldi.")
t.B("Urushdan keyin keynschilik asosida yaratilgan nazariya qanday nom olgan?", "neokeynschilik", "neokonservatizm", "postmodernizm", "monetarizm", "Neokeynschilik.")
t.B("Fotografiyaning rivojlanishiga javob tarzida paydo bo‘lgan san’at yo‘nalishi qaysi?", "abstraksionizm", "pop art", "realizm", "klassitsizm", "Abstraksionizm (mavhumlik).")
t.B("Abstraksionizmga qarama-qarshi ravishda paydo bo‘lgan yo‘nalish qaysi?", "pop art (ommaviy san’at)", "postmodernizm", "realizm", "romantizm", "Pop art (ommaviy san’at).")
t.B("G‘arb va Sharq san’ati, folklor va ommaviy madaniyat elementlarini jamlagan uslub qanday atalgan?", "postmodernizm", "abstraksionizm", "pop art", "modernizm", "Postmodernizm.")
t.B("Mashinani butlab yig‘ish uchun uzluksiz ishlaydigan lentasimon qurilma nima deb ataladi?", "konveyer", "robot", "lazer", "mikrosxema", "Konveyer.")
t.NAT("1959-yili integral mikrosxemalar yaratildi.", "kompyuter va boshqa asboblar hajmi keskin qisqarib, faoliyat sohasi kengaydi", "kompyuterlar kattalashdi", "lazer kashf etildi", "uyali telefonlar taqiqlandi", "Olimlar uni so‘nggi 50 yildagi eng mashhur ixtiro deb hisobladi.")
t.NAT("Elektron va radioaktivlik kashf etildi.", "Nyuton mexanikasiga asoslangan dunyoqarash inqirozga uchrab, ilmiy-texnik inqilob yuz berdi", "mexanika yanada mustahkamlandi", "fizika rivojlanishi to‘xtadi", "genetika taqiqlandi", "Bu yangi davr fani inqiroziga va ilmiy-texnik inqilobga turtki bo‘ldi.")
t.TF("Lazerni yaratgan uchala olimga fizika bo‘yicha Nobel mukofoti berilgan.", True, "To‘g‘ri.")
t.TF("Ommaviy adabiyot voqealar rivojining oldindan noma’lumligi bilan XX asr birinchi yarmi adabiyotidan farq qilgan.", False, "Noto‘g‘ri: u voqealar rivojining oldindan ma’lumligi bilan farq qiladi.")
t.MUL([("1970–1980-yillarda Ericsson va Philips kompaniyalari uyali telefonlarning yangi turlarini yaratgan.", True),
       ("Massachusets texnologiya instituti xodimlari kompyuter orqali masofaviy aloqa mumkinligini asoslagan.", True),
       ("Jon Keyns o‘z nazariyasini XX asrning ikkinchi yarmida yaratgan.", False)],
      "III noto‘g‘ri: Keyns XX asrning birinchi yarmida yangi yo‘nalishni yaratgan.")
t.CHR("Kashfiyotlarni xronologik ketma-ketlikda joylashtiring.", ["Birinchi sun’iy yo‘ldosh uchirildi", "Integral mikrosxemalar yaratildi", "Lazer yaratildi", "Gagarin koinotga parvoz qildi", "ARPANET yaratildi"],
      "1957 → 1959 → 1960 → 1961 → 1969.")
t.MATCH("Olimlarni kashfiyotlari bilan moslashtiring.", ["Basov, Proxorov, Tauns", "Kilbi va Noys", "S. P. Korolyov", "Jon Keyns"],
        ["lazer", "integral mikrosxemalar", "kosmik kemalar tadqiqoti", "makroiqtisodiyot", "nisbiylik nazariyasi"], 'abcd',
        "Lazer – Basov, Proxorov, Tauns; mikrosxemalar – Kilbi, Noys; kosmos – Korolyov; makroiqtisodiyot – Keyns.")
t.VENN("Abstraksionizm", "Pop art",
       [("fotografiyaga javob tarzida paydo bo‘lgan", 1), ("tasvirda harakat va hissiyotni ifodalash", 1),
        ("har qanday buyum badiiy sifat kasb etishi mumkin", 2), ("ommaviy san’at", 2),
        ("XX asr san’at yo‘nalishi", 3)],
       "Abstraksionizm – fotografiyaga javob, hissiyot; pop art – buyum, ommaviy; ikkalasi XX asr yo‘nalishi.")
t.MAPMATCH('globe2', ['Shvetsiya', 'Boston', 'Angliya'],
           ["«Televerket» kompaniyasi uyali telefon ustida ish boshlagan mamlakat", "Massachusets texnologiya instituti joylashgan hudud", "makroiqtisodiyot asoschisi Jon Keyns vatani"],
           "1 – Shvetsiya; 2 – Massachusets (Boston); 3 – Angliya.")
