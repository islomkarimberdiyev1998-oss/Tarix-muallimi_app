# Natijalar serveri (@Tarixustoz_bot)

`server.py` — ishtirokchilar natijalarini yig‘adigan kichik server. Faqat Python 3 kerak, qo‘shimcha kutubxona o‘rnatilmaydi.

## Nima qiladi
- Mini App test tugagach natijani (to‘g‘ri javoblar soni, ball, birinchi urinish yoki mashq) serverga yuboradi.
- Ilova ochilganda telefondagi eski ballar ham serverga sinxronlanadi.
- **Hamma uchun:** «Reyting» sahifasida umumiy reyting chiqadi (o‘rin, ism, @username, liga, ball). Ishtirokchi bosilsa, Telegram’da u bilan yozishma ochiladi (username bo‘lsa).
- **Admin uchun:** «Reyting» sahifasida «Ishtirokchilar natijalari» tugmasi chiqadi. U yerda barcha ishtirokchilar, qidiruv, har birining urinishlari va mavzular bo‘yicha ballari bor. «Bot orqali yuborish» tugmasi bilan ishtirokchiga bot nomidan xabar yuboriladi.

Har bir so‘rov Telegram imzosi (`initData`) bilan tekshiriladi, shuning uchun hech kim o‘zini boshqa odam yoki admin qilib ko‘rsata olmaydi.

## Ishga tushirish
```bash
export BOT_TOKEN='123456:ABC...'          # @BotFather bergan token
export ADMIN_IDS='123456789'              # sizning Telegram ID ingiz (bir nechta bo‘lsa vergul bilan)
export ALLOW_ORIGIN='https://<ilova-manzili>'  # Mini App ochiladigan sayt manzili
export PORT=8080
python3 bot/server.py
```
Telegram ID ingizni @userinfobot orqali bilishingiz mumkin.

Server **HTTPS** orqali ochiq bo‘lishi kerak (masalan, nginx yoki Caddy orqasida, yoki Render/Railway kabi xostingda). Tekshirish uchun: `https://<server>/health` → `{"ok": true}`.

Server bot yangilanishlarini o‘qimaydi (getUpdates/webhook ishlatmaydi), faqat xabar yuboradi. Shuning uchun mavjud bot kodi bilan to‘qnashmaydi va u bilan yonma-yon ishlay oladi.

## Ilovaga ulash
`index.html` da ikki joyga server manzilini yozing:
1. `const API_URL='';` → `const API_URL='https://<server>';`
2. Yuqoridagi `Content-Security-Policy` ichida `connect-src 'self';` → `connect-src 'self' https://<server>;`

`API_URL` bo‘sh bo‘lsa, ilova avvalgidek ishlaydi: natijalar faqat telefonda saqlanadi.

## Xabar yetib borishi uchun
Bot faqat botni ishga tushirgan (/start) yoki ruxsat bergan foydalanuvchiga yoza oladi. Ilova birinchi test tugagach ishtirokchidan bir marta shunday ruxsat so‘raydi.
