from qlib import Topic, PLACES, REG
TOPICS = {}

# 24 Ilk Uyg‘onish davri madaniyati
t = Topic('y8j24', 8024); TOPICS['y8j24'] = t
t.B("«Renessans» so‘zi qanday ma’noni anglatadi?", "uyg‘onish, qayta tiklanish", "yangi dunyo", "insonparvarlik", "inqilob", "Uyg‘onish, qayta tiklanish.")
t.B("Renessans qaysi mamlakatda boshlangan?", "Italiya", "Fransiya", "Germaniya", "Niderlandiya", "Italiyada.")
t.B("Renessans davri namoyandalari qaysi madaniyatdan ilhomlangan?", "qadimgi yunon va rim madaniyati", "Misr madaniyati", "arab madaniyati", "gotika madaniyati", "Qadimgi yunon va rim madaniyati.")
t.B("Ilk Uyg‘onish bosqichi qaysi yillarni o‘z ichiga oladi?", "1420–1500-yillar", "1500–1527-yillar", "1530–1620-yillar", "1300–1420-yillar", "1420–1500-yillar.")
t.B("Rivojlangan Uyg‘onish bosqichi qaysi yillar?", "1500–1527-yillar", "1420–1500-yillar", "1530–1620-yillar", "1453–1492-yillar", "1500–1527-yillar.")
t.B("Gumanitar fanlarni o‘rganish natijasida yuzaga kelgan yangi fikrlash uslubi qanday atalgan?", "insonparvarlik (gumanizm)", "ilohiyot", "sxolastika", "alkimyo", "Insonparvarlik.")
t.B("Asarlarini lotin tilida emas, italyan tilida yozgan ijodkor kim?", "Dante Aligyeri", "Petrarka", "Salutati", "Brunelleski", "Dante Aligyeri.")
t.B("Uyg‘onish davri arxitekturasining asoschisi kim?", "Filippo Brunelleski", "Mazachcho", "Verrokkio", "Van Eyk", "Florensiyalik Filippo Brunelleski.")
t.B("Brunelleskining eng mashhur ijod namunasi qaysi?", "Santa Mariya soborining gumbazi", "Milan sobori", "Kolizey", "San Jovanni maydoni", "Santa Mariya sobori gumbazi.")
t.B("Ilk Uyg‘onish davrining birinchi rassomi kim hisoblanadi?", "Tommazo Mazachcho", "Leonardo da Vinchi", "Bottichelli", "Jovanni Bellini", "Tommazo Mazachcho.")
t.B("«Statir mo‘jizasi» asari muallifi kim?", "Mazachcho", "Verrokkio", "Van Eyk", "Mantenya", "Mazachcho.")
t.B("Jovanni Santi qaysi shaharda mashhur bo‘lgan?", "Urbino", "Mantua", "Ferrara", "Venetsiya", "Urbinoda (Rafaelning otasi).")
t.B("Andrea Mantenya qaysi shaharda mashhur bo‘lgan?", "Mantua", "Peruja", "Urbino", "Florensiya", "Mantuada.")
t.B("Kimning ustaxonasida Bottichelli, Perujino va Leonardo da Vinchi o‘qigan?", "Andrea del Verrokkio", "Brunelleski", "Mazachcho", "Jovanni Santi", "Andrea del Verrokkio.")
t.B("«Qo‘mondon Bartolomeo Kolleoni» haykali qayerda o‘rnatilgan?", "Venetsiyadagi San Jovanni maydonida", "Florensiyada", "Rimda", "Milanda", "Venetsiya, San Jovanni maydoni.")
t.B("Shimoliy Yevropada Uyg‘onish davrining yirik vakili kim?", "Yan van Eyk", "Mazachcho", "Bellini", "Perujino", "Yan van Eyk.")
t.B("Van Eykning italiyalik tadbirkor uchun chizgan portreti qaysi?", "«Jovanni Arnolfini»", "«David»", "«Statir mo‘jizasi»", "«Iso Masih va avliyo Foma»", "«Jovanni Arnolfini» portreti.")
t.B("Ispaniyalik Uyg‘onish davri bastakori kim?", "Xuan de Urrede", "Jovanni Ambrozio", "Domeniko da Ferrara", "Salutati", "Xuan de Urrede.")
t.NAT("XIV asrda Florensiya, Genuya, Milan, Venetsiya Osiyo bilan savdoda yetakchilik qildi.", "hunarmandchilik va savdo rivojlanib, madaniyat o‘choqlari paydo bo‘ldi", "Italiya qashshoqlashdi", "cherkov ta’siri kuchaydi", "universitetlar yopildi", "Renessans uchun zamin yaratildi.")
t.NAT("Iqtisodiy jarayonlar tez rivojlanib, boy o‘rta sinf yuksaldi.", "ular san’at ahlining homiylariga aylandi", "o‘rta sinf yo‘qoldi", "san’atga qiziqish so‘ndi", "zodagonlar kuchaydi", "Homiylik rivojlandi.")
t.NAT("Shimoliy yevropalik talabalar Italiyada gumanist o‘qituvchilardan tahsil oldi.", "yangi g‘oyalarni o‘z vatanlariga olib ketdi", "Italiyada qolib ketdi", "gumanizmga qarshi kurashdi", "lotin tilini unutdi", "Renessans shimolga tarqaldi.")
t.NAT("Matbaa ixtirosi notalarni tarqatish imkonini berdi.", "musiqa san’ati rivojlanib, shaxsiy ifoda masalasiga aylandi", "musiqa faqat cherkovda qoldi", "bastakorlar kamaydi", "musiqa taqiqlandi", "Musiqa rivojlandi.")
t.TF("Petrarka va Bokkachcho yuksak obraz va fikrlarni ochiq, umumiy tilda ifodalay boshlagan.", True, "To‘g‘ri.")
t.TF("Shimollik rassomlar asosan Injildagi voqealarni chizgan.", False, "Noto‘g‘ri: Injil – Italiya Renessansining mavzusi; shimolliklar kundalik hayot sahnalarini chizgan.")
t.TF4([("So‘nggi Uyg‘onish bosqichi 1530–1620-yillarni o‘z ichiga oladi.", True), ("Pyetro Perujino Peruja shahrida mashhur bo‘lgan.", True),
       ("Van Eyk moybo‘yoqning yangi turlarini ishlab chiqqan.", True), ("Jovanni Bellini Ferrara shahrida mashhur bo‘lgan.", False)],
      "4-noto‘g‘ri: Bellini – Venetsiya; Ferrarada Franchesko del Kossa.")
t.MUL([("Panteon va Kolizey xarobalari kishilarni o‘tmish madaniyatini eslashga undagan.", True),
       ("Cherkov nazoratiga qarshi kayfiyat Renessansning shakllanishiga turtki bo‘lgan.", True),
       ("Uyg‘onish davrida asosiy e’tibor inson shaxsiga emas, diniy omillarga qaratilgan.", False)],
      "III noto‘g‘ri: asosiy e’tibor inson shaxsiga qaratilgan.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Filippo Brunelleski tug‘ildi", "Tommazo Mazachcho tug‘ildi", "Ilk Uyg‘onish bosqichi boshlandi", "Andrea del Verrokkio tug‘ildi", "Rivojlangan Uyg‘onish bosqichi boshlandi"],
      "1377 → 1401 → 1420 → 1435 → 1500.")
t.MATCH("Rassomlarni ular mashhur bo‘lgan shahar bilan moslashtiring.", ["Jovanni Santi", "Franchesko del Kossa", "Andrea Mantenya", "Jovanni Bellini"],
        ["Urbino", "Ferrara", "Mantua", "Venetsiya", "Peruja"], 'abcd',
        "Santi – Urbino; del Kossa – Ferrara; Mantenya – Mantua; Bellini – Venetsiya.")
t.VENN("Italiya Renessansi", "Shimoliy Renessans",
       [("Injil voqealari an’anaviy mavzu", 1), ("Brunelleski, Mazachcho", 1),
        ("kundalik hayot sahnalari", 2), ("Yan van Eyk", 2),
        ("insonparvarlik g‘oyalari", 3)],
       "Italiya – Injil, Brunelleski; shimol – kundalik hayot, Van Eyk; umumiy – gumanizm.")
t.MAPMATCH('italy', ['Florensiya', 'Rim', 'Milan', 'Venetsiya'],
           ["Brunelleski va Mazachcho vatani", "Panteon, Kolizey va forumlar xarobalari joylashgan shahar", "XIV asrda Osiyo bilan savdoda yetakchilik qilgan, Genuya bilan bir qatordagi shahar", "Kolleoni haykali o‘rnatilgan shahar"],
           "1 – Florensiya; 2 – Rim; 3 – Milan; 4 – Venetsiya.")
