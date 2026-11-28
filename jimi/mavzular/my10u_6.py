from qlib import Topic, PLACES, REG
TOPICS = {}

# 12-mavzu. Jadidchilik namoyandalari
t = Topic('y10u12', 10012); TOPICS['y10u12'] = t
t.B("O‘rta Osiyo jadidchilik harakatining asoschisi va yo‘lboshchisi kim?", "Mahmudxo‘ja Behbudiy", "Abdulla Avloniy", "Munavvarqori", "Ubaydullaxo‘ja", "Mahmudxo‘ja Behbudiy.")
t.B("Behbudiy tashabbusi bilan otasi sharafiga qanday kutubxona tashkil qilingan?", "«Behbudiya kutubxonasi»", "«Turon kutubxonasi»", "«Navoiy kutubxonasi»", "«Ma’rifat kutubxonasi»", "«Behbudiya kutubxonasi».")
t.B("Abdulla Avloniy qachon va qayerda tug‘ilgan?", "1878-yilda Toshkentda", "1875-yilda Samarqandda", "1878-yilda Buxoroda", "1886-yilda Qo‘qonda", "1878-yil, Toshkent.")
t.B("Avloniy 1907-yilda qaysi gazetaga asos solgan?", "«Shuhrat»", "«Taraqqiy»", "«Oyina»", "«Sadoi Turkiston»", "«Shuhrat».")
t.B("«Birinchi muallim», «Turkiy guliston yoxud axloq» darsliklari muallifi kim?", "Abdulla Avloniy", "Munavvarqori", "Behbudiy", "Fitrat", "Abdulla Avloniy.")
t.B("Munavvarqori Abdurashidxonov qaysi yillarda yashagan?", "1878–1931", "1875–1919", "1878–1934", "1886–1938", "1878–1931.")
t.B("«Adibi avval», «Adibi soniy», «Yer yuzi» darsliklari muallifi kim?", "Munavvarqori", "Avloniy", "Behbudiy", "Ubaydullaxo‘ja", "Munavvarqori Abdurashidxonov.")
t.B("Yoshlarni chet elga o‘qishga yuborishga katta mablag‘ ajratgan andijonlik kim?", "Mirkomil Mirmo‘minboyev", "Abduvohid Burhonov", "Hamidxo‘ja Meqriy", "Ahmadjon Abdusaidov", "Mirkomil Mirmo‘minboyev.")
t.B("1908-yilda Buxoroda qanday jamiyat tashkil qilingan?", "«Tarbiyai atfol»", "«Fuqaho jamiyati»", "«Sho‘royi islomiya»", "«Ittifoq»", "«Tarbiyai atfol» («Bolalar tarbiyasi»).")
t.B("«Tarbiyai atfol» 1912-yilda Turkiyaga nechta talaba yuborgan?", "30 nafar", "15 nafar", "100 nafar", "5 nafar", "30 nafar (1911-yilda 15 nafar).")
t.B("«Fuqaho jamiyati» qachon va qayerda tashkil topgan?", "1917-yil 10-avgustda Toshkentda", "1908-yilda Buxoroda", "1910-yilda Samarqandda", "1905-yilda Qo‘qonda", "1917-yil 10-avgust, Toshkent.")
t.B("«Fuqaho jamiyati»ning nashri qaysi jurnal edi?", "«Izhor ul-Haq»", "«Oyina»", "«Al-Isloh»", "«Shuhrat»", "«Izhor ul-Haq».")
t.B("Birinchi oliy ma’lumotli o‘zbek advokati kim bo‘lgan?", "Ubaydullaxo‘ja Asadullaxo‘ja o‘g‘li", "Munavvarqori", "Behbudiy", "Mirkomil Mirmo‘minboyev", "Ubaydullaxo‘ja.")
t.B("Ubaydullaxo‘ja qaysi rus yozuvchisi bilan yozishmalar olib borgan?", "Lev Tolstoy", "Aleksandr Pushkin", "Fyodor Dostoyevskiy", "Anton Chexov", "Lev Tolstoy.")
t.B("1917-yilda tuzilgan milliy-siyosiy tashkilotlardan biri qaysi?", "«Sho‘royi islomiya»", "«Tarbiyai atfol»", "«Fuqaho jamiyati»", "«Behbudiya»", "«Sho‘royi islomiya», «Ittifoq».")
t.NAT("Jadidlar yangi usul maktablarida yoshlarni tarbiyaladi.", "ular orqali mustaqil davlat barpo etish uchun milliy davlatchilik g‘oyalari ilgari surildi", "maktablar yopildi", "yoshlar Rossiyaga ko‘chdi", "jadidlar hukumatga qo‘shildi", "Milliy davlatchilik g‘oyalari.")
t.NAT("Mustamlaka davrida hanafiylik mazhabini sofligicha avlodga yetkazish dolzarb bo‘ldi.", "1917-yilda Toshkentda «Fuqaho jamiyati» tashkil topdi", "madrasalar yopildi", "jadidlar tarqatildi", "«Tarbiyai atfol» tuzildi", "Fuqaho jamiyati tuzildi.")
t.NAT("Taraqqiyparvarlar xalqning tinchliksevarligi, bosiqligidan kelib chiqdi.", "barcha muammolarni tinch yo‘l bilan hal etishga intildi", "qurolli kurash boshladi", "Rossiyaga qochdi", "siyosatdan voz kechdi", "Tinch yo‘l bilan.")
t.NAT("Jadidlar tub aholining barcha qatlamlarini o‘z ortidan ergashtirdi.", "jadidchilik mustamlakachilikka qarshi asosiy ma’naviy kuch sifatida namoyon bo‘ldi", "jadidchilik so‘ndi", "aholi jadidlarga qarshi chiqdi", "imperiya kuchaydi", "Asosiy ma’naviy kuch.")
t.TF("1917-yilga kelib Turkiston jadidchiligi siyosiy harakatga aylandi.", True, "To‘g‘ri.")
t.TF("«Fuqaho jamiyati» faqat jadid o‘qituvchilaridan iborat bo‘lgan.", False, "Noto‘g‘ri: to‘rt qozi va ular yonidagi muhrdor, a’lam, muftiylardan iborat bo‘lgan.")
t.TF4([("Jadidlar yoshlarni Germaniyaga o‘qishga yuborish g‘oyasini ilgari surgan.", True), ("Avloniy ta’lim, matbuot va teatr rivojiga hissa qo‘shgan.", True),
       ("Munavvarqori jadid teatri targ‘ibotchisi bo‘lgan.", True), ("Jadidlar fevral voqealaridan keyin hech qanday siyosiy talab qo‘ymagan.", False)],
      "4-noto‘g‘ri: aholi huquqlarini kengaytirish, Dumada o‘rin, matbuot erkinligi kabi talablar qo‘ygan.")
t.MUL([("«Tarbiyai atfol» 1911-yilda 15 nafar talabani Turkiyaga yuborgan.", True),
       ("Taraqqiyparvarlar mahsulotni o‘lkaning o‘zida ishlab chiqarishni zarur deb bilgan.", True),
       ("Ubaydullaxo‘ja Germaniyada tibbiyot bo‘yicha ta’lim olgan.", False)],
      "III noto‘g‘ri: Rossiyada huquqshunoslik bo‘yicha ta’lim olgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Avloniy «Shuhrat» gazetasiga asos soldi", "«Tarbiyai atfol» tuzildi", "Turkiyaga 15 talaba yuborildi", "Turkiyaga 30 talaba yuborildi", "«Fuqaho jamiyati» tashkil topdi"],
      "1907 → 1908 → 1911 → 1912 → 1917.")
t.MATCH("Jadidlarni faoliyati bilan moslashtiring.", ["Behbudiy", "Avloniy", "Munavvarqori", "Ubaydullaxo‘ja"],
        ["harakat asoschisi, «Behbudiya kutubxonasi»", "«Shuhrat» gazetasi, «Birinchi muallim»", "«Adibi avval», «Yer yuzi» darsliklari", "birinchi o‘zbek advokati", "«Tarbiyai atfol» asoschisi"], 'abcd',
        "Behbudiy – kutubxona; Avloniy – Shuhrat; Munavvarqori – Adibi avval; Ubaydullaxo‘ja – advokat.")
t.VENN("Avloniy", "Munavvarqori",
       [("«Shuhrat» gazetasi asoschisi", 1), ("«Turkiy guliston yoxud axloq» muallifi", 1),
        ("«Adibi avval», «Yer yuzi» muallifi", 2), ("1878–1931-yillarda yashagan", 2),
        ("Toshkentlik jadid, darsliklar yaratgan", 3)],
       "Avloniy – Shuhrat, Turkiy guliston; Munavvarqori – Adibi avval; ikkalasi darslik yaratgan.")
t.MAPMATCH('uzb', ['Toshkent', 'Buxoro', 'Andijon'],
           ["1917-yilda «Fuqaho jamiyati» tuzilgan shahar", "1908-yilda «Tarbiyai atfol» tuzilgan shahar", "Mirkomil Mirmo‘minboyev vatani"],
           "1 – Toshkent; 2 – Buxoro; 3 – Andijon.")
