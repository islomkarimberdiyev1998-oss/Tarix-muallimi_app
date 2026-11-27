from qlib import Topic, PLACES, REG
TOPICS = {}

# 8-§ Shayboniylar davri me’morchiligi
t = Topic('y9u8', 9008); TOPICS['y9u8'] = t
t.B("Shayboniylar Markaziy Osiyoda necha yil hukmronlik qilgan?", "100 yil (1500–1601)", "200 yil", "50 yil", "300 yil", "100 yil mobaynida.")
t.B("Buxorodagi qurilishlarda qaysi ustalar ishtirok etgan?", "Movarounnahr, Hirot, Balx ustalari", "Eron va Hindiston ustalari", "Xitoy ustalari", "Rus ustalari", "Movarounnahr, Hirot, Balx ustalari.")
t.B("Toshkentdagi Ko‘kaldosh madrasasi qachon qurilgan?", "1551–1575-yillarda", "1530–1536-yillarda", "1531–1532-yillarda", "1582-yilda", "1551–1575-yillar orasida.")
t.B("Ko‘kaldosh madrasasi qayerda joylashgan?", "Chorsu maydonidagi Shahriston tepaligida", "Registonda", "Hazrati Imomda", "Minorayi kalon qarshisida", "Chorsu maydoni, Shahriston tepaligi.")
t.B("Ko‘kaldosh madrasasida nechta hujra bo‘lgan?", "38 ta", "114 ta", "36 ta", "22 ta", "38 ta.")
t.B("Ko‘kaldosh madrasasi dastlab necha qavatli bo‘lgan?", "3 qavatli", "1 qavatli", "4 qavatli", "2 qavatli", "3 qavatli.")
t.B("Mir Arab madrasasi qaysi inshoot qarshisida joylashgan?", "Minorayi kalon", "Ark", "Labi hovuz", "Toqi Zargaron", "Minorayi kalon qarshisida.")
t.B("Mir Arab madrasasida nechta xona bor?", "114 ta", "38 ta", "36 ta", "7 ta", "114 ta xona.")
t.B("Mir Arab madrasasi qachon qurilgan?", "1530–1536-yillarda", "1551–1575-yillarda", "1501-yilda", "1598-yilda", "1530–1536-yillarda.")
t.B("Mir Arabning asl ismi nima?", "Sayyid Abdulloh Yamaniy", "Shayx Zakariyo", "Muhammad Bakr", "Xoja Ahror", "Sayyid Abdulloh Yamaniy.")
t.B("Mir Arab Samarqandda kimga shogird tushgan?", "Xoja Ahror Valiyga", "Ubaydullaxonga", "Muhammad Solihga", "Nisoriyga", "Xoja Ahror Valiyga.")
t.B("Mir Arab vafotidan so‘ng madrasa qurilishini kim yakunlagan?", "kuyovi Shayx Zakariyo", "Ubaydullaxon", "Muhammad Bakr", "Abdullaxon II", "Kuyovi Shayx Zakariyo.")
t.B("Mir Arab madrasasi go‘rxonasida kimning yog‘och sag‘anasi bor?", "Ubaydullaxonning", "Abdullaxon II ning", "Shayboniyxonning", "Baroqxonning", "Ubaydullaxonning xotamkori sag‘anasi.")
t.B("Toqi Zargaronning dalonlarida nechta zargarlik ustaxonasi bo‘lgan?", "36 ta", "38 ta", "114 ta", "7 ta", "36 ta.")
t.B("Toqi Zargaron qaysi madrasa yonida joylashgan?", "Ulug‘bek madrasasi", "Mir Arab madrasasi", "Abdullaxon madrasasi", "Ko‘kaldosh madrasasi", "Ulug‘bek madrasasi yonida.")
t.B("Abdullaxon madrasasi bilan «qo‘sh» uslubni hosil qilgan madrasa qaysi?", "Modarixon", "Mir Arab", "Ko‘kaldosh", "Baroqxon", "Modarixon madrasasi.")
t.B("Modarixon madrasasi kimga atab qurilgan?", "Abdullaxonning onasiga", "Abdullaxonning qiziga", "Ubaydullaxonning onasiga", "Mir Arabga", "Abdullaxonning onasiga.")
t.B("Buxorodagi ayollar hammomi qaysi?", "Hammomi Kunjak", "Hammomi Bozori kord", "Hammomi Sarrofon", "Garmoba", "Hammomi Kunjak.")
t.B("O‘rta asrlarda Buxoro hammomlari qanday nomlangan?", "garmoba", "go‘lax", "sovuqxona", "toq", "«Garmoba».")
t.B("Hammomning olovxonasi qanday atalgan?", "go‘lax", "garmoba", "miyonsaroy", "qorixona", "Go‘lax.")
t.B("Baroqxon kim bo‘lgan?", "Toshkent hokimi Suyunchxo‘janing kichik o‘g‘li", "Abdullaxon II ning ukasi", "Ubaydullaxonning o‘g‘li", "Mir Arabning shogirdi", "Abulxayrxon nevarasi, Suyunchxo‘ja o‘g‘li.")
t.B("Baroqxon madrasasi gumbazining balandligi qancha?", "22 m", "64 m", "4,5 m", "38 m", "22 m.")
t.NAT("Mir Arab ilm-ma’rifati bilan el orasida tanildi.", "Ubaydullaxon homiyligida Buxoroda Mir Arab madrasasi qurildi", "Mir Arab Samarqanddan quvildi", "madrasa vayron qilindi", "Mir Arab Hindistonga ketdi", "Madrasa qurildi.")
t.NAT("Toqi Zargaron chorsuda ikkita katta yo‘lni me’moriy jihatdan uyg‘unlashtirdi.", "ikkala yo‘ldagi qatnov osonlashdi", "yo‘llar yopildi", "savdo to‘xtadi", "bozor ko‘chirildi", "Qatnov osonlashdi.")
t.NAT("Hammom gumbazlari cho‘qqisi oynaband qilib ishlandi.", "hammom yoritilib, havosi yangilanib turdi", "hammom sovib qoldi", "suv oqib ketdi", "gumbazlar quladi", "Yoritish va shamollatish.")
t.NAT("Abdullaxon madrasasi ro‘paradagi Modarixon madrasasiga qarab biroz egilgan holda qurildi.", "bu onaga o‘ziga xos hurmat ramzi sifatida talqin etiladi", "madrasa qulab tushdi", "madrasa qayta qurildi", "ikki madrasa birlashtirildi", "Hurmat ramzi.")
t.TF("1558-yilda Jenkinson Buxoro hammomlari dunyoning hech qayerida yo‘qligini yozgan.", True, "To‘g‘ri.")
t.TF("Mir Arab madrasasining kirish qismi kunchiqar tomonda joylashgan.", False, "Noto‘g‘ri: kunbotar tomonda.")
t.TF4([("Mir Arab madrasasi ikki ulkan gumbazi bilan ajralib turadi.", True), ("Toqi Zargaronda hukmdor farmonlari ham e’lon qilingan.", True),
       ("Hammomlarda issiqxonalar devori bir qavatli bo‘lgan.", False), ("Baroqxon madrasasi o‘rnida dastlab ikkita maqbara bo‘lgan.", True)],
      "3-noto‘g‘ri: issiqxonalar devori ikki qavatli, sovuq xonalarniki bir qavatli.")
t.MUL([("Abdullaxon madrasasi darvozasi xotamkori uslubining noyob namunasi.", True),
       ("Baroqxon madrasasi bezaklari jihatidan Samarqanddagi Oqsaroyga yaqin turadi.", True),
       ("Abdullaxon madrasasining katta peshtoqi shimolga qaragan.", False)],
      "III noto‘g‘ri: katta peshtoq janubga qaragan.")
t.CHR("Inshootlarni qurilish boshlanishi bo‘yicha tartiblang.", ["Mir Arab madrasasi", "Baroqxon madrasasi", "Ko‘kaldosh madrasasi (Toshkent)"],
      "1530 → 1531 → 1551.")
t.MATCH("Inshootlarni shahri bilan moslashtiring.", ["Ko‘kaldosh madrasasi", "Mir Arab madrasasi", "Baroqxon madrasasi", "Toqi Zargaron"],
        ["Toshkent, Chorsu", "Buxoro, Minorayi kalon qarshisi", "Toshkent, Hazrati Imom", "Buxoro, Ulug‘bek madrasasi yoni", "Samarqand, Registon"], 'abcd',
        "Ko‘kaldosh – Chorsu; Mir Arab – Minorayi kalon; Baroqxon – Hazrati Imom; Toqi Zargaron – Ulug‘bek madrasasi yoni.")
t.VENN("Mir Arab madrasasi", "Ko‘kaldosh madrasasi",
       [("114 xona, 4 qavat", 1), ("Ubaydullaxon sag‘anasi bor", 1),
        ("38 hujra, dastlab 3 qavat", 2), ("Chorsu maydonida", 2),
        ("Shayboniylar davrida qurilgan", 3)],
       "Mir Arab – 114 xona; Ko‘kaldosh – 38 hujra, Chorsu; ikkalasi Shayboniylar davri.")
t.MAPN('uzb', ['Buxoro', 'Toshkent', 'Samarqand', 'Xiva'], "Mir Arab, Abdullaxon, Modarixon madrasalari va Toqi Zargaron joylashgan shahar xaritada qaysi raqam bilan belgilangan?",
       "Buxoro.")
