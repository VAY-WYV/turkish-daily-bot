import requests
from datetime import datetime

BOT_TOKEN = "8605424727:AAGSHnY2aUJ0_bnQ11hbXmFWE9gQ3uS1DPo"
CHAT_ID = "5412144182"

lessons = {
    0: """🇹🇷 درسك التركي اليومي - الأحد

🌅 تحية اليوم:
Günaydın! = صباح الخير!
İyi günler! = يوم سعيد!

📚 كلمات اليوم:
1. ev = بيت | Ben evdeyim (أنا في البيت)
2. su = ماء | Su içiyorum (أنا أشرب ماء)
3. ekmek = خبز | Ekmek istiyorum (أريد خبز)
4. güzel = جميل | Hava çok güzel (الجو جميل جداً)
5. büyük = كبير | Bu ev çok büyük (هذا البيت كبير جداً)

📖 قصة اليوم:
Ahmet sabah erken kalktı. Pencereden dışarıya baktı — hava çok güzeldi, gökyüzü masmaviydi. Mutfağa gitti ve kahvaltı hazırladı. Taze ekmek, beyaz peynir ve domates kesti. Çayını demleyip masaya oturdu. Sessizce yedi ve o günü düşündü. Kahvaltıdan sonra kitabını aldı ve bahçeye çıktı. Ağacın gölgesinde oturdu. Kuşlar ötüyordu, komşunun kedisi yanına geldi ve dizine atladı. Ahmet gülümsedi.

(أحمد صحي بدري. نظر من الشباك — الجو كان جميل، السما زرقاء. راح المطبخ وجهز فطار. قطع خبز وجبنة وطماطم. شرب شايه وقعد. بعد الفطار أخد كتابه وخرج للجنينة. قعد في الظل. العصافير بتغني، قطة الجار جت وقفزت على ركبته. أحمد ابتسم.)

💬 سؤال اليوم:
Sen neredesin? (أنت فين؟)
💡 Ben evdeyim! (أنا في البيت!)

🧠 نصيحة:
كرر كل كلمة 3 مرات بصوت عالي — ده بيثبتها في دماغك!""",

    1: """🇹🇷 درسك التركي اليومي - الاثنين

🌅 تحية اليوم:
Merhaba! = مرحباً!
Nasılsın? = كيف حالك؟

📚 كلمات اليوم:
1. araba = سيارة | Bu benim arabam (هذه سيارتي)
2. yemek = طعام | Yemek yiyorum (أنا آكل)
3. kahve = قهوة | Kahve seviyorum (أنا أحب القهوة)
4. kitap = كتاب | Kitap okuyorum (أنا أقرأ كتاب)
5. para = مال | Param yok (ما عنديش فلوس)

📖 قصة اليوم:
Fatma bugün markete gitmek istedi. Çantasını aldı ve evden çıktı. Yolda komşusuyla karşılaştı. "Günaydın! Nereye gidiyorsun?" dedi komşusu. "Markete gidiyorum, ekmek ve süt alacağım" dedi Fatma. Markette çok insan vardı. Fatma ekmek, süt ve biraz meyve aldı. Kasada sıra bekledi. Yanındaki yaşlı kadın sepetini tutmakta zorlanıyordu — Fatma hemen yardım etti. "Teşekkür ederim!" dedi yaşlı kadın. Fatma güldü ve eve döndü.

(فاطمة أرادت تروح السوق. أخدت شنطتها وخرجت. قابلت الجارة في الطريق. "صباح الخير! رايحة فين؟" قالت الجارة. "رايحة السوق" قالت فاطمة. في السوق كان ناس كتير. أخدت خبز وحليب وفاكهة. استنت في الطابور. ست كبيرة كانت بتتعب تشيل سلتها — فاطمة ساعدتها فوراً. "شكراً!" قالت الست. فاطمة ضحكت ورجعت البيت.)

💬 سؤال اليوم:
Ne içiyorsun? (بتشرب إيه؟)
💡 Kahve içiyorum! (بشرب قهوة!)

🧠 نصيحة:
اكتب الكلمات الجديدة في نوت وراجعها آخر اليوم!""",

    2: """🇹🇷 درسك التركي اليومي - الثلاثاء

🌅 تحية اليوم:
İyi sabahlar! = صباح النور!
Hoş geldiniz! = أهلاً وسهلاً!

📚 كلمات اليوم:
1. okul = مدرسة | Okula gidiyorum (رايح المدرسة)
2. öğretmen = معلم | O iyi bir öğretmen (هو معلم كويس)
3. çalışmak = يذاكر | Çok çalışıyorum (بذاكر كتير)
4. yorgun = تعبان | Çok yorgunum (أنا تعبان جداً)
5. uyumak = ينام | Uyumak istiyorum (عايز أنام)

📖 قصة اليوم:
Ali her sabah erken kalkıyor ve okula yürüyerek gidiyor. Bugün Türkçe sınavı vardı ve biraz gergin hissediyordu. Sınıfa girdiğinde öğretmeni tahtada yeni kelimeler yazıyordu. "Günaydın Ali, hazır mısın?" dedi öğretmeni. Ali derin bir nefes aldı: "Evet, hazırım!" Sınav başladı. Ali dikkatle okudu ve yazdı. Sınav bitti ve sonuçlar geldi: Ali tam not almıştı! Arkadaşına koştu ve bağırdı: "Tam not aldım!" Arkadaşı onu kucakladı.

(علي بيصحى بدري ويروح المدرسة ماشي. النهارده كان في امتحان تركي وكان متوتر. لما دخل الفصل المعلم كان بيكتب على السبورة. "صباح الخير يا علي، جاهز؟" علي أخد نفس: "آيوه جاهز!" الامتحان بدأ. قرأ وكتب بتركيز. النتيجة: درجة كاملة! جري لصاحبه: "أخدت درجة كاملة!" صاحبه عناقه.)

💬 سؤال اليوم:
Nereye gidiyorsun? (رايح فين؟)
💡 Okula gidiyorum! (رايح المدرسة!)

🧠 نصيحة:
ترجم جملة من حياتك للتركي كل يوم!""",

    3: """🇹🇷 درسك التركي اليومي - الأربعاء

🌅 تحية اليوم:
Günaydın! = صباح الخير!
Kolay gelsin! = ربنا يهون!

📚 كلمات اليوم:
1. saat = ساعة | Saat kaç? (الساعة كام؟)
2. sabah = صباح | Sabah kahvaltısı (فطار الصبح)
3. öğle = ظهر | Öğle yemeği (غداء)
4. akşam = مساء | Akşam yemeği (عشاء)
5. gece = ليل | Gece yarısı (منتصف الليل)

📖 قصة اليوم:
Zeynep'in günü çok meşguldü. Sabah saat yedide kalktı ve hızlıca kahvaltı yaptı. İşe gitmeden önce kahvesini içti. Öğle vakti arkadaşıyla buluştu. "Bugün çok yoruldum" dedi Zeynep. "Ben de! Bu hafta çok iş var" dedi arkadaşı. Akşam eve döndüğünde annesi yemek yapmıştı. Birlikte yediler ve konuştular. Gece saat onda kitabını açtı ama gözleri kapanıyordu. Kitabı bıraktı ve uyudu. Rüyasında güzel bir tatil gördü.

(يوم زينب كان مزدحم. صحيت الساعة سبعة وعملت فطار بسرعة. شربت قهوتها. وقت الظهر قابلت صاحبتها. "تعبت جداً النهارده." "أنا كمان! الأسبوع ده صعب." المساء رجعت والأم عاملة أكل. أكلوا مع بعض. الليل فتحت كتابها بس عنيها اتقفلوا. سابته وناضت. في الحلم شافت إجازة حلوة.)

💬 سؤال اليوم:
Saat kaç? (الساعة كام؟)
💡 Saat sekiz! (الساعة تمانية!)

🧠 نصيحة:
غير لغة موبايلك للتركية ليوم واحد!""",

    4: """🇹🇷 درسك التركي اليومي - الخميس

🌅 تحية اليوم:
İyi sabahlar! = صباح النور!
Hayırlı işler! = شغل مبارك!

📚 كلمات اليوم:
1. aile = أسرة | Ailem burada (عيلتي هنا)
2. anne = أم | Annem çok iyi (أمي كويسة)
3. baba = أب | Babam çalışıyor (أبويا بيشتغل)
4. kardeş = أخ/أخت | Bir kardeşim var (عندي أخ)
5. sevmek = يحب | Ailemi seviyorum (بحب عيلتي)

📖 قصة اليوم:
Mehmet büyük bir ailede büyüdü. Annesi, babası, iki ablası ve bir erkek kardeşi vardı. Her akşam birlikte yemek yerlerdi. Bu gece Mehmet heyecanlıydı — Türkçe sınavından tam not almıştı. Yemeği yedi ama bir şey söylemedi. Babası sordu: "Bugün nasıldı?" Mehmet cebinden kağıdı çıkardı ve masaya koydu. Herkes baktı — "100" yazıyordu. Babası ayağa kalktı ve sarıldı. Annesi koşarak geldi. Ablası fotoğraf çekti. O gece en mutlu insandı.

(محمد كبر في عيلة كبيرة. كل مساء بياكلوا مع بعض. الليلة كان متحمس — أخد درجة كاملة في التركي. أكل بس ما قالش حاجة. أبوه سأل: "النهارده كان إزاي؟" أخرج الورقة من جيبه وحطها على المنضدة. الكل بص — "100". أبوه وقف وعناقه. أمه جرت. أخته صورت. كان أسعد واحد.)

💬 سؤال اليوم:
Kaç kardeşin var? (عندك كام أخ؟)
💡 İki kardeşim var! (عندي اتنين!)

🧠 نصيحة:
تكلم مع نفسك بالتركي في المرايا!""",

    5: """🇹🇷 درسك التركي اليومي - الجمعة

🌅 تحية اليوم:
İyi hafta sonlar! = نهاية أسبوع سعيدة!
Hayırlı cumalar! = جمعة مباركة!

📚 كلمات اليوم:
1. film = فيلم | Film izliyorum (بتفرج على فيلم)
2. müzik = موسيقى | Müzik dinliyorum (بسمع موسيقى)
3. tatil = إجازة | Tatil istiyorum (عايز إجازة)
4. eğlenmek = يتسلى | Çok eğleniyorum (بتسلى كتير)
5. arkadaş = صديق | Arkadaşlarım burada (أصحابي هنا)

📖 قصة اليوم:
Cuma geldi ve Selin çok mutluydu. Arkadaşı Ayşe sabah mesaj attı: "Bu akşam sinemaya gidelim mi?" Selin hemen "Evet!" yazdı. Akşam buluştular — Selin mavi elbisesini giymişti. Sinemaya gittiler, film Türk yapımıydı ve çok güzeldi. Film sırasında ikisi de ağladı, ikisi de güldü. Film bitince kafede oturdular. "Harika bir filmdi!" dedi Ayşe. "Evet, ama en güzel şey seninle gelmekti" dedi Selin. Gece geç döndüler ama çok mutluydular.

(الجمعة جت وسيلين سعيدة. صاحبتها آيشة بعتتلها: "نروح سينما الليلة؟" كتبت فوراً "آيوه!" المساء اتقابلوا. السينما كانت فيها ناس. الفيلم تركي وجميل. الاتنين عيطوا وضحكوا. بعدين في كافيه. "فيلم رائع!" قالت آيشة. "آيوه، بس أحلى حاجة إنك جيتي معايا" قالت سيلين. رجعوا متأخرين بس سعداء.)

💬 سؤال اليوم:
Hafta sonu ne yapıyorsun? (بتعمل إيه في الويك إند؟)
💡 Arkadaşlarımla buluşuyorum!

🧠 نصيحة:
شوف مسلسل تركي على يوتيوب!""",

    6: """🇹🇷 درسك التركي اليومي - السبت

🌅 تحية اليوم:
Merhaba! = أهلاً!
Nasıl gidiyor? = عامل إيه؟

📚 كلمات اليوم:
1. alışveriş = تسوق | Alışveriş yapıyorum (بتسوق)
2. mağaza = محل | Mağazaya gidiyorum (رايح المحل)
3. ucuz = رخيص | Bu çok ucuz (ده رخيص)
4. pahalı = غالي | Bu çok pahalı (ده غالي)
5. istemek = يريد | Ne istiyorsun? (عايز إيه؟)

📖 قصة اليوم:
Kemal bugün annesiyle alışverişe çıktı. Büyük mağazaya girdiler. Kemal yeni bir gömlek istiyordu. Bir tane buldu — çok güzeldi ama çok pahalıydı. "Anne, bu gömleği sevdim ama pahalı" dedi. "Daha bakacağız" dedi annesi. Yan sokakta küçük bir dükkan gördüler. İçeri girdiler — tatlı bir yaşlı adam karşıladı onları. Aynı modelde bir gömlek vardı, çok daha ucuzdu! Kemal denedi, tam oldu. "Teşekkürler!" dedi Kemal gülerek. O gün hem güzel bir gömlek aldı hem de güzel bir insan tanıdı.

(كمال خرج مع أمه يتسوقوا. دخلوا المحل الكبير. كان عايز قميص جديد. لقى واحد — جميل بس غالي. "ماما، القميص ده حلو بس غالي." "هنبص أكتر." في شارع جنبي دكان صغير. دخلوا — راجل كبير ظريف استقبلهم. نفس القميص بس أرخص بكتير! جربه، جاب. "شكراً!" قال كمال وهو بيضحك. أخد قميص حلو وعرف إنسان حلو.)

💬 سؤال اليوم:
Ne istiyorsun? (عايز إيه؟)
💡 Yeni bir gömlek istiyorum!

🧠 نصيحة:
مبروك على أسبوع! راجع كل الكلمات دي."""
}

def send_lesson():
    day = datetime.now().weekday()
    day_map = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 0}
    lesson = lessons[day_map[day]]
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    response = requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": lesson
    })
    print(response.json())

if __name__ == "__main__":
    send_lesson()
