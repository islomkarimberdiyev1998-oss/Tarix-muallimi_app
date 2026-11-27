from qlib import Topic, PLACES, REG
TOPICS = {}

# 13-§ Ashtarxoniylar davrida me’morchilik va ta’lim
t = Topic('y9u13', 9013); TOPICS['y9u13'] = t
t.B("Samarqanddagi Sherdor va Tillakori madrasalarini kim qurdirgan?", "Yalangto‘sh Bahodir", "Nodir devonbegi", "Abdulazizxon", "qozi Soqiy", "Yalangto‘sh Bahodir.")
t.B("Buxoroda «Zargarlar madrasasi» deb ataluvchi madrasa qaysi?", "Abdulazizxon madrasasi", "Jo‘ybori Kalon", "Mir Arab", "Xiyobon", "Abdulazizxon madrasasi.")
t.B("Mablag‘iga xonaqoh, hovuz va madrasadan iborat ansambl qurilgan vazir kim?", "Nodir devonbegi", "Yalangto‘sh", "Muhammadyor otaliq", "Poyandabiy", "Nodir devonbegi.")
t.B("Nodir devonbegi Ark devorlari ostida qaysi masjidni qurdirgan?", "Poyandabiy otaliq masjidi", "Bolohovuz masjidi", "Mag‘oki ko‘rpa", "Kalon masjidi", "Poyandabiy otaliq masjidi.")
t.B("Abdulazizxon madrasasi qachon qurilgan?", "1652-yilda", "1682-yilda", "1611-yilda", "1708-yilda", "1652-yilda.")
t.B("Abdulazizxon madrasasining me’mori kim?", "Mimxoqon ibn Xo‘ja Muhammadamin", "Shayx Zakariyo", "Muhammad Murod", "Yusuf Qorabog‘iy", "Mimxoqon ibn Xo‘ja Muhammadamin.")
t.B("Abdulazizxon madrasasi qaysi madrasa qarshisida qurilgan?", "Ulug‘bek madrasasi", "Mir Arab", "Kukeldash", "Modarixon", "Buxorodagi Ulug‘bek madrasasi qarshisida.")
t.B("Abdulazizxon madrasasi naqshlari asosan qaysi rangda chizilgan?", "moviy", "qizil", "sariq", "yashil", "Moviy rang bo‘yoqlar bilan.")
t.B("Jo‘ybori Kalon madrasasi kutubxonasida qancha kitob saqlangan?", "8 ming jilddan ortiq", "800 jild", "80 ming jild", "115 jild", "8 ming jilddan ortiq.")
t.B("Bahor gullari rangidagi bezak san’ati qanday ataladi?", "gulnoriy", "islimiy", "girih", "parchinkoriy", "Gulnoriy.")
t.B("Abdulazizxon qaysi xatlarda yuksak mahorat bilan yozgan?", "nasx va nasta’liq", "kufiy va suls", "uyg‘ur yozuvi", "lotin", "Nasx va nasta’liq.")
t.B("Subhonqulixon davrida Ark devorlari tagida qachon kasalxona qurilgan?", "1682-yilda", "1652-yilda", "1708-yilda", "1611-yilda", "1682-yilda.")
t.B("Subhonqulixon qurdirgan shifoxona qanday atalgan?", "Dor ush-shifo", "Bolohovuz", "Mag‘oki ko‘rpa", "Zargaron", "Dor ush-shifo.")
t.B("Subhonqulixonning tibbiyotga oid asari qaysi?", "«Ihyo at-tibbi Subhoniy»", "«Bahr ul-asror»", "«Dastur al-muluk»", "«Ubaydullanoma»", "«Ihyo at-tibbi Subhoniy».")
t.B("«Ihyo at-tibbi Subhoniy» qo‘lyozmasining bir nusxasi qayerda saqlanmoqda?", "Budapeshtda", "Londonda", "Istanbulda", "Sankt-Peterburgda", "Budapeshtdagi kutubxonada.")
t.B("Subhonqulixonning taxallusi qanday?", "Nishoniy", "Xon", "Shohbaxt", "Fitrat", "Nishoniy.")
t.B("Subhonqulixon yozda novvoylarga non yuziga nima sepishni buyurgan?", "kunjut urug‘i", "sedana", "zira", "shakar", "Kunjut urug‘i – ich ketishni kamaytirish uchun.")
t.B("«Bahr ul-asror» asari muallifi kim?", "Mahmud ibn Vali", "Xoja Samandar Termiziy", "Abdurahmon Tole", "Mir Muhammad Amin Buxoriy", "Mahmud ibn Vali.")
t.B("«Ubaydullanoma» asari muallifi kim?", "Mir Muhammad Amin Buxoriy", "Muhammad Yusuf Munshiy", "Abdurahmon Tole", "Hojamqulixon Balxiy", "Mir Muhammad Amin Buxoriy.")
t.B("Muhammad Murod Samarqandiy «Shohnoma»ga nechta miniatyura ishlagan?", "115 ta", "29 ta", "8 ta", "1000 ta", "115 ta.")
t.NAT("Abdulazizxon madrasasidagi mehrob sharafasi odam boshidagi sallaga monand yasaldi.", "quyosh nuri tushganda mehrobda sallali nuroniy kishi tasviri ko‘rinadi", "mehrob qulab tushdi", "madrasa yopildi", "naqshlar o‘chib ketdi", "Yashirin tasvir paydo bo‘ladi.")
t.NAT("Subhonqulixon non yuziga kunjut sepishni buyurdi.", "bu tadbir keyinchalik odat tusiga aylandi", "non narxi oshdi", "novvoylar norozi bo‘ldi", "kunjut ekish taqiqlandi", "Odatga aylangan.")
t.NAT("Ashtarxoniylar davrida Hindiston bilan aloqalar rivojlandi.", "ikki hudud musavvirlari o‘rtasida aloqalar kuchayib, miniatyura an’analari boyidi", "miniatyura san’ati yo‘qoldi", "Hindiston Buxoroni bosib oldi", "kitob san’ati taqiqlandi", "Miniatyura an’analari boyidi.")
t.NAT("Dor ush-shifo binosi madrasa vazifasini ham o‘tadi.", "talabalarga tabobat va ilohiyot ilmlari o‘rgatildi", "bino omborga aylandi", "kasallarni davolash to‘xtadi", "tabiblar quvildi", "Tibbiy madrasa bo‘lgan.")
t.TF("Abdulazizxon Hindiston, Eron va Usmonli davlatiga yo‘llanadigan maktublarni o‘zi tahrir qilgan.", True, "To‘g‘ri.")
t.TF("Ashtarxoniylar davrida diniy mutaassiblik tufayli ilm ahlining ijodi butunlay to‘xtagan.", False, "Noto‘g‘ri: mutaassiblik kuchaygan bo‘lsa-da, ijod to‘xtamagan.")
t.TF4([("Jo‘ybori Kalon madrasasi Havzi nav guzarida qurilgan.", True), ("Muhammadyor otaliq Bozori-av degan joyda xonaqoh qurgan.", True),
       ("Subhonqulixonning ikkinchi tibbiy asari 8 qismdan iborat.", True), ("«Qipchoqxon tarixi»ni Abdurahmon Tole yozgan.", False)],
      "4-noto‘g‘ri: «Qipchoqxon tarixi» – Hojamqulixon Balxiy; Tole – «Abulfayzxon tarixi».")
t.MUL([("Subhonqulixon astronomiyaga oid asar ham yozgan.", True),
       ("Mashrab va So‘fi Olloyor XVII asrda faoliyat yuritgan.", True),
       ("Abdulazizxon madrasasi uch qavatli.", False)],
      "III noto‘g‘ri: madrasa ikki qavatli.")
t.CHR("Voqealarni xronologik ketma-ketlikda joylashtiring.", ["Muhammad Murod bezagan «Shohnoma» nusxasi ko‘chirildi", "Abdulazizxon madrasasi qurildi", "Dor ush-shifo kasalxonasi qurildi", "Ubaydullaxonning pul islohoti"],
      "1556 → 1652 → 1682 → 1708.")
t.MATCH("Asarlarni mualliflari bilan moslashtiring.", ["«Dastur al-muluk»", "«Muqimxon tarixi»", "«Abulfayzxon tarixi»", "«Ihyo at-tibbi Subhoniy»"],
        ["Xoja Samandar Termiziy", "Muhammad Yusuf Munshiy", "Abdurahmon Tole", "Subhonqulixon", "Mahmud ibn Vali"], 'abcd',
        "Dastur al-muluk – Termiziy; Muqimxon tarixi – Munshiy; Abulfayzxon tarixi – Tole; Ihyo – Subhonqulixon.")
t.VENN("Abdulazizxon madrasasi", "Jo‘ybori Kalon madrasasi",
       [("«Zargarlar madrasasi» deb atalgan", 1), ("mehrobda yashirin sallali odam tasviri", 1),
        ("8 ming jildli kutubxona", 2), ("gulnoriy rangdagi bezaklar", 2),
        ("ashtarxoniylar davrida Buxoroda qurilgan", 3)],
       "Abdulazizxon – zargarlar, yashirin tasvir; Jo‘ybori Kalon – kutubxona, gulnoriy; ikkalasi Buxoroda XVII asr.")
t.MAPN('uzb', ['Samarqand', 'Buxoro', 'Toshkent', 'Xiva'], "Yalangto‘sh Bahodir Sherdor va Tillakori madrasalarini qurdirgan shahar xaritada qaysi raqam bilan belgilangan?",
       "Samarqand (Registon).")
