"""
MKTB 393 – Chapter 7: Delivering the Digital Customer Experience
Comprehensive study summary (HTML → PDF via WeasyPrint)
Blue terms, red/orange marketing keywords
Arabic translation under every definition (RTL block)
No MCQ section
"""
import re
from datetime import date

KEYWORDS_RED = {
    "always", "never", "must", "cannot", "only", "not", "do not", "no",
    "critical", "essential", "required", "important", "key", "note",
    "must not", "failure", "difficult", "lose", "leave", "lost", "poor",
    "abandon", "bad", "worst", "avoid", "prevent", "if not", "without",
    "first", "prior", "before",
}
KEYWORDS_ORANGE = {
    "usability", "accessibility", "personalisation", "personalisation",
    "experience", "customer", "digital", "online", "website", "mobile",
    "design", "navigation", "content", "trust", "quality", "loyalty",
    "effective", "effectively", "efficiency", "efficient",
    "satisfaction", "learnability", "memorability",
    "conversion", "engagement", "brand", "responsive",
    "architecture", "information", "task", "user", "interaction",
    "performance", "optimisation", "security", "privacy",
    "service", "reliability", "assurance", "empathy",
}


def colorize(text):
    parts = re.split(r'(\s+)', text)
    out = []
    for p in parts:
        tok = p.lower().strip(".,;:()'\"")
        if tok in KEYWORDS_RED:
            out.append(f'<span class="kw-red">{p}</span>')
        elif tok in KEYWORDS_ORANGE:
            out.append(f'<span class="kw-orange">{p}</span>')
        else:
            out.append(p)
    return "".join(out)


def term(name, definition, arabic):
    return (
        f'<div class="term-block">'
        f'<p class="term"><span class="term-name">{name}:</span> '
        f'{colorize(definition)}</p>'
        f'<p class="arabic-def" dir="rtl" lang="ar">{arabic}</p>'
        f'</div>'
    )


def code_line(line):
    return f'<pre class="code">{line}</pre>'


def tip(text):
    return f'<div class="tip"><strong>Exam Tip:</strong> {colorize(text)}</div>'


def trap(text):
    return f'<div class="trap"><strong>Exam Trap:</strong> {colorize(text)}</div>'


def bullet(text, arabic=""):
    ar = f'<span class="ar-inline" dir="rtl" lang="ar"> — {arabic}</span>' if arabic else ""
    return f'<li>{colorize(text)}{ar}</li>'


def chapter_title(title):
    return f'<h2>{title}</h2>'


def section(title):
    return f'<h3>{title}</h3>'


def num_list_item(n, label, text, arabic=""):
    ar = f'<p class="arabic-def" dir="rtl" lang="ar">{arabic}</p>' if arabic else ""
    return (
        f'<div class="num-item"><span class="num-badge">{n}</span>'
        f'<div><strong>{label}:</strong> {colorize(text)}{ar}</div></div>'
    )


CSS = """
@page {
    size: A4;
    margin: 16mm 18mm 16mm 18mm;
    @bottom-right { content: counter(page); font-size:9pt; color:#888; }
}
.cover {
    page-break-after: always;
    text-align: center;
    padding: 44pt 28pt;
    border: 2pt solid #1F3964;
    border-radius: 8pt;
    background: linear-gradient(150deg,#EBF3FB,#F8FBFF);
    min-height: 230mm;
    box-sizing: border-box;
}
body { font-family: Calibri, Arial, 'DejaVu Sans', sans-serif; font-size:9.5pt; color:#222; line-height:1.5; }
h1   { color:#1F3964; font-size:22pt; margin:0 0 6pt; }
.subtitle { color:#17738F; font-size:13pt; margin:4pt 0; }
.course   { font-size:11pt; font-weight:bold; margin:6pt 0; }
.date-line{ color:#888; font-size:10pt; }
h2 {
    color:#1F3964; font-size:12.5pt; font-weight:bold;
    border-bottom:2pt solid #1F3964;
    padding-bottom:2pt; margin:0; margin-bottom:4pt;
    page-break-before: always;
}
h3 { color:#17738F; font-size:10pt; font-weight:bold; margin-top:9pt; margin-bottom:2pt; }
.term-block { margin:3pt 0 3pt 8pt; }
p.term { margin:1pt 0; font-size:9.5pt; }
span.term-name { color:#0070C0; font-weight:bold; }
span.kw-red    { color:#C00000; font-weight:bold; }
span.kw-orange { color:#C05500; font-weight:bold; }
p.arabic-def {
    margin:1pt 0 4pt 16pt;
    font-size:9pt;
    color:#4A4A4A;
    font-family: 'DejaVu Sans', Arial, sans-serif;
    background:#F8F8F8;
    border-right: 3pt solid #0070C0;
    padding: 2pt 6pt;
    border-radius: 2pt;
}
.ar-inline { font-size:8.5pt; color:#555; font-family:'DejaVu Sans',Arial,sans-serif; }
pre.code {
    font-family:'Courier New',monospace; font-size:8pt;
    background:#F2F2F2; color:#26343F;
    margin:2pt 0 2pt 18pt; padding:3pt 6pt;
    border-radius:3pt; white-space:pre-wrap; word-break:break-all;
}
ul { margin:2pt 0 2pt 22pt; padding:0; }
ol { margin:2pt 0 2pt 22pt; padding:0; }
li { margin:2pt 0; font-size:9.5pt; }
.tip  { background:#E2EFDA; border-left:3pt solid #378610; padding:3pt 7pt; margin:4pt 0 4pt 8pt; font-size:8.5pt; }
.tip strong { color:#378610; }
.trap { background:#FCE4D6; border-left:3pt solid #C00000; padding:3pt 7pt; margin:4pt 0 4pt 8pt; font-size:8.5pt; }
.trap strong { color:#C00000; }
.ref-table { width:100%; border-collapse:collapse; font-size:8.5pt; margin:4pt 0 4pt 8pt; }
.ref-table th { background:#1F3964; color:white; padding:3pt 6pt; text-align:left; }
.ref-table td { border:1pt solid #BFBFBF; padding:2pt 6pt; }
.ref-table tr:nth-child(even) td { background:#F2F2F2; }
.ref-table .ar-cell { direction:rtl; text-align:right; font-family:'DejaVu Sans',Arial,sans-serif; font-size:8pt; color:#444; }
.num-item { display:flex; gap:8pt; margin:3pt 0 3pt 8pt; align-items:flex-start; font-size:9.5pt; }
.num-badge { background:#1F3964; color:white; font-weight:bold; min-width:16pt; text-align:center; border-radius:3pt; padding:1pt 4pt; font-size:8.5pt; flex-shrink:0; }
.highlight-box { background:#EBF3FB; border-left:3pt solid #1F3964; padding:4pt 8pt; margin:4pt 0 4pt 8pt; font-size:9pt; }
"""

body = []

# ── COVER ────────────────────────────────────────────────────────
body.append(f"""
<div class="cover">
  <h1>Delivering the Digital<br>Customer Experience</h1>
  <p class="subtitle">Study Summary &ndash; Chapter 7</p>
  <br>
  <p class="course">MKTB 393: Digital Marketing &nbsp;|&nbsp; Strategy, Implementation and Practice</p>
  <p style="font-size:9pt;color:#444;margin-top:6pt;">
    Textbook: <em>Digital Marketing: Strategy, Implementation and Practice</em><br>
    8th Edition &mdash; Pearson Education (2022)
  </p>
  <br>
  <p style="font-size:9pt;color:#444;line-height:2.0;">
    <strong>Topics Covered:</strong><br>
    Digital Customer Experience Framework &bull; Online Brand Equity<br>
    Website Development Process &bull; Usability (Nielsen's 5 Components)<br>
    Digital Accessibility &bull; Personalisation &bull; Information Architecture<br>
    Landing Pages &bull; Responsive Web Design &bull; Information Processing<br>
    Online Retail Merchandising &bull; Service Quality &amp; e-Loyalty &bull; WebQual
  </p>
  <br><br>
  <p class="date-line">Prepared: {date.today().strftime('%B %Y')}</p>
</div>
""")

# ════════════════════════════════════════════════════════════════
# SECTION 1 – DIGITAL CUSTOMER EXPERIENCE OVERVIEW
# ════════════════════════════════════════════════════════════════
body.append(chapter_title("1. Digital Customer Experience — Overview"))

body.append(section("Core Framework"))

body.append(term(
    "Digital Customer Experience",
    "The sum of all digital interactions a customer has with a brand — encompassing "
    "emotional needs (trust, credibility), rational needs (value, variety), user experience "
    "(ease of use, relevance), and platform performance (speed, availability).",
    "تجربة العميل الرقمية: مجمل التفاعلات الرقمية للعميل مع العلامة التجارية — تشمل الاحتياجات العاطفية (الثقة، المصداقية)، "
    "والاحتياجات العقلانية (القيمة، التنوع)، وتجربة المستخدم (سهولة الاستخدام، الملاءمة)، وأداء المنصة (السرعة، التوفر)."
))

body.append(term(
    "Rational Needs (in digital experience)",
    "Customer's logical requirements from a website: value for money (cost and offers), "
    "product variety, order fulfilment, and customer service support.",
    "الاحتياجات العقلانية: المتطلبات المنطقية للعميل من الموقع — القيمة مقابل المال (التكلفة والعروض)، "
    "تنوع المنتجات، إنجاز الطلبات، ودعم خدمة العملاء."
))

body.append(term(
    "Emotional Needs (in digital experience)",
    "Customer's psychological requirements: trust in the brand, credibility, and feeling "
    "that the site truly understands and cares about them.",
    "الاحتياجات العاطفية: المتطلبات النفسية للعميل — الثقة بالعلامة التجارية، المصداقية، "
    "والشعور بأن الموقع يفهمهم ويهتم بهم فعلاً."
))

body.append(term(
    "Platform Performance (Speed &amp; Availability)",
    "Technical dimensions that determine whether customers can access the site and get "
    "results quickly. Poor performance is a top reason customers leave and do not return.",
    "أداء المنصة (السرعة والتوفر): الأبعاد التقنية التي تحدد ما إذا كان العملاء يستطيعون الوصول إلى الموقع والحصول على نتائج بسرعة. "
    "الأداء السيئ هو أحد أبرز الأسباب التي تجعل العملاء يغادرون ولا يعودون."
))

body.append(tip("A good site must always begin with the USER — understand who the customer is, how they use the channel, and what competitors offer. (Alison Lancaster, John Lewis Direct)"))
body.append(tip("Customers want: convenience, ease of ordering, a quick-loading site, and good service. These are your design priorities."))
body.append(trap("Emotional and rational needs are BOTH essential — a site that is functionally good but emotionally cold (no trust signals) will still lose customers."))

# ════════════════════════════════════════════════════════════════
# SECTION 2 – ONLINE BRAND EQUITY
# ════════════════════════════════════════════════════════════════
body.append(chapter_title("2. Online Brand Equity (Christodoulides et al., 2006)"))

body.append(section("5 Dimensions of Online Brand Equity"))
body.append('<p style="font-size:9pt;margin:2pt 0 6pt 8pt;">A model for measuring how strong a brand\'s equity is in an online context — used by Christodoulides et al. (2006).</p>')
body.append('<p style="font-size:8.5pt;margin:2pt 0 4pt 8pt;font-style:italic;color:#555;">نموذج لقياس قوة حقوق ملكية العلامة التجارية في السياق الرقمي.</p>')

body.append(num_list_item(1, "Emotional Connection",
    "The degree to which customers feel the brand relates to them, cares about them, "
    "and truly understands them. Measured by: 'I feel [X] really understands me.'",
    "الارتباط العاطفي: مدى شعور العملاء بأن العلامة التجارية تتعلق بهم وتهتم بهم وتفهمهم فعلاً."))

body.append(num_list_item(2, "Online Experience",
    "The quality of the digital interaction — whether the site provides easy-to-follow "
    "search paths, users never feel lost, and information is obtained without delay.",
    "التجربة الإلكترونية: جودة التفاعل الرقمي — هل يوفر الموقع مسارات بحث سهلة، لا يشعر المستخدمون بالضياع، "
    "ويمكن الحصول على المعلومات دون تأخير."))

body.append(num_list_item(3, "Responsive Service Nature",
    "The degree to which the brand is willing and ready to respond to customer needs "
    "and gives visitors the opportunity to 'talk back'.",
    "طبيعة الخدمة الاستجابية: مدى استعداد العلامة التجارية للرد على احتياجات العملاء، وتوفير إمكانية التواصل والرد."))

body.append(num_list_item(4, "Trust",
    "The degree to which customers feel their personal information is safe and they feel "
    "secure in transactions with the brand.",
    "الثقة: مدى شعور العملاء بأن معلوماتهم الشخصية آمنة وأنهم يثقون بالمعاملات مع العلامة التجارية."))

body.append(num_list_item(5, "Fulfilment",
    "Whether customers actually received what they ordered and whether delivery occurred "
    "within the promised time frame.",
    "الإنجاز/الوفاء: هل استلم العملاء فعلاً ما طلبوه وهل تم التسليم في الوقت المحدد."))

body.append(tip("Memorize these 5 dimensions as a set: Emotional Connection → Online Experience → Responsive Service → Trust → Fulfilment."))
body.append(trap("This model was from 2006 — exam questions may ask 'How might these differ today?' because mobile, social media, and AI have changed the online experience significantly."))

# ════════════════════════════════════════════════════════════════
# SECTION 3 – PLANNING & DEVELOPMENT PROCESS
# ════════════════════════════════════════════════════════════════
body.append(chapter_title("3. Planning Website, App Design &amp; Redesign Projects"))

body.append(section("7 Main Development Tasks"))
body.append('<p class="arabic-def" dir="rtl" lang="ar">المهام السبع الرئيسية لتطوير موقع ويب أو تطبيق رقمي:</p>')

body.append("<ul>")
body.append(bullet("Pre-development — initial business case and scope definition", "ما قبل التطوير — تحديد نطاق المشروع والجدوى"))
body.append(bullet("Discovery, analysis, design — research and wireframes", "الاكتشاف، التحليل، التصميم — البحث والنماذج الأولية"))
body.append(bullet("Content creation, coding development and testing", "إنشاء المحتوى وتطوير الترميز والاختبار"))
body.append(bullet("Publishing or launching the site or improvement", "نشر أو إطلاق الموقع أو تحسينه"))
body.append(bullet("Pre-launch promotion or communications", "الترويج أو الاتصالات قبل الإطلاق"))
body.append(bullet("Ongoing promotion — driving traffic after launch", "الترويج المستمر — جلب الزوار بعد الإطلاق"))
body.append(bullet("Ongoing development — continuous improvement", "التطوير المستمر — التحسين المتواصل"))
body.append("</ul>")

body.append(section("Stakeholders in a Digital Experience Project"))
body.append('<p class="arabic-def" dir="rtl" lang="ar">أصحاب المصلحة في مشروع التجربة الرقمية (8 أدوار رئيسية):</p>')

body.append("""<table class="ref-table">
<tr><th>Role / الدور</th><th>Responsibility / المسؤولية</th></tr>
<tr><td>Site Sponsor / راعي الموقع</td><td>Provides budget and senior sign-off on direction / يوفر الميزانية والموافقة العليا</td></tr>
<tr><td>Site Owner / مالك الموقع</td><td>Responsible for overall objectives and ROI / مسؤول عن الأهداف العامة والعائد</td></tr>
<tr><td>Project Manager / مدير المشروع</td><td>Day-to-day coordination and timeline control / التنسيق اليومي والجدول الزمني</td></tr>
<tr><td>Site Designer / مصمم الموقع</td><td>Visual design and UX / التصميم البصري وتجربة المستخدم</td></tr>
<tr><td>Content Developer / مطور المحتوى</td><td>Creates and maintains copywriting and media / ينشئ المحتوى ويحافظ عليه</td></tr>
<tr><td>Webmaster / مشرف الموقع</td><td>Technical maintenance and updates / الصيانة التقنية والتحديثات</td></tr>
<tr><td>Digital Experience Analyst / محلل التجربة الرقمية</td><td>Monitors analytics and performance / يراقب التحليلات والأداء</td></tr>
<tr><td>Stakeholder / أصحاب المصلحة</td><td>Other internal/external parties with an interest in the project / أطراف أخرى ذات مصلحة</td></tr>
</table>""")

body.append(section("Typical Website Prototyping Approach"))
body.append(term(
    "Prototyping",
    "Creating progressively detailed visual representations of a site before full build — "
    "starting from low-fidelity wireframes to high-fidelity interactive prototypes to reduce "
    "costly changes during development.",
    "النمذجة الأولية: إنشاء تمثيلات بصرية تدريجية للموقع قبل البناء الكامل — بدءاً من الأطر السلكية (wireframes) "
    "منخفضة الدقة وصولاً إلى النماذج التفاعلية عالية الدقة، لتقليل التغييرات المكلفة أثناء التطوير."
))

body.append(tip("The website development process follows a clear sequence: Pre-development → Discovery/Analysis/Design → Content/Code/Test → Launch → Promote → Ongoing."))
body.append(trap("A 'Site Sponsor' is NOT the same as 'Site Owner' — the sponsor provides budget/authority; the owner manages objectives and ROI on a day-to-day basis."))

# ════════════════════════════════════════════════════════════════
# SECTION 4 – INITIATION OF A DIGITAL PROJECT
# ════════════════════════════════════════════════════════════════
body.append(chapter_title("4. Initiation of a Digital Project"))

body.append(term(
    "Domain Name",
    "A unique address used to identify a website (e.g., www.example.com). Must be selected "
    "and registered before a site goes live. A good domain name is memorable, short, and "
    "reflects the brand.",
    "اسم النطاق: العنوان الفريد المستخدم لتعريف الموقع الإلكتروني. يجب اختياره وتسجيله قبل إطلاق الموقع. "
    "يُفضل أن يكون سهل التذكر وقصيراً ويعكس العلامة التجارية."
))

body.append(term(
    "URL (Uniform Resource Locator)",
    "The full web address pointing to a specific page or resource on the internet. "
    "Structure: protocol (http/https) + domain + path. Key for SEO and user navigation.",
    "URL (محدد موقع الموارد الموحد): العنوان الكامل على الويب الذي يشير إلى صفحة أو مورد معين على الإنترنت. "
    "هيكله: البروتوكول + النطاق + المسار. مهم لتحسين محركات البحث وتنقل المستخدم."
))

body.append(term(
    "Hosting Provider",
    "A company that provides the server infrastructure to store and deliver website files. "
    "Key selection criteria: uptime guarantee (availability), speed, scalability, security, "
    "and customer support.",
    "مزود الاستضافة: شركة توفر البنية التحتية للخادم لتخزين ملفات الموقع وتسليمها. "
    "معايير الاختيار: ضمان وقت التشغيل (التوفر)، السرعة، قابلية التوسع، الأمان، ودعم العملاء."
))

body.append(term(
    "Website Performance Optimisation",
    "Techniques to improve page load speed and availability — critical because slow "
    "loading directly causes users to leave and reduces search engine rankings.",
    "تحسين أداء الموقع: تقنيات لتحسين سرعة تحميل الصفحة وتوفرها — حيوية لأن التحميل البطيء يدفع المستخدمين للمغادرة "
    "ويقلل من ترتيب الموقع في محركات البحث."
))

body.append(tip("Performance optimisation is important for BOTH user experience AND search engine ranking — Google factors page speed into its ranking algorithm."))

# ════════════════════════════════════════════════════════════════
# SECTION 5 – USABILITY
# ════════════════════════════════════════════════════════════════
body.append(chapter_title("5. Usability — What Exactly Is It?"))

body.append(term(
    "Usability (ISO 9241-210)",
    "The degree to which a product can be used by specified users to achieve specified goals "
    "with effectiveness, efficiency, and satisfaction in a specified context of use.",
    "قابلية الاستخدام (ISO 9241-210): الدرجة التي يمكن للمستخدمين المحددين من خلالها استخدام منتج ما "
    "لتحقيق أهداف محددة بفعالية وكفاءة ورضا في سياق محدد للاستخدام."
))

body.append(term(
    "Effectiveness (ISO Definition)",
    "'Accuracy and completeness with which users achieve specified goals.' "
    "Measured by task completion rate — e.g., how many out of 10 users can find a phone number.",
    "الفعالية (تعريف ISO): دقة واكتمال تحقيق المستخدمين للأهداف المحددة. "
    "تُقاس بمعدل إكمال المهام — مثلاً: كم من 10 مستخدمين يستطيعون إيجاد رقم الهاتف."
))

body.append(term(
    "Efficiency (ISO Definition)",
    "'Resources expended in relation to accuracy and completeness with which users achieve goals.' "
    "Measured by how long it takes users to complete a task — time on task.",
    "الكفاءة (تعريف ISO): الموارد المستنفدة مقارنةً بدقة واكتمال تحقيق الأهداف. "
    "تُقاس بالوقت المستغرق لإكمال المهمة."
))

body.append('<div class="highlight-box"><strong>Jakob Nielsen (2012):</strong> <em>"On the web, usability is a necessary condition for survival. If a website is difficult to use, people leave. If the homepage fails to clearly state what a company offers, people leave. If users get lost on a website, they leave."</em></div>')
body.append('<p class="arabic-def" dir="rtl" lang="ar">جاكوب نيلسن (2012): "على الويب، قابلية الاستخدام شرط ضروري للبقاء. إذا كان الموقع صعب الاستخدام، يغادر الناس. إذا فشلت الصفحة الرئيسية في توضيح ما تقدمه الشركة، يغادر الناس. إذا ضاع المستخدمون في الموقع، يغادرون."</p>')

body.append(section("Nielsen's 5 Quality Components of Usability"))
body.append('<p class="arabic-def" dir="rtl" lang="ar">خمسة مكونات جودة قابلية الاستخدام لنيلسن (2012):</p>')

body.append(num_list_item(1, "Learnability",
    "How easy is it for users to accomplish basic tasks the FIRST TIME they encounter the design?",
    "قابلية التعلم: ما مدى سهولة إنجاز المهام الأساسية في المرة الأولى عند مواجهة التصميم؟"))

body.append(num_list_item(2, "Efficiency",
    "Once users have learned the design, how QUICKLY can they perform tasks?",
    "الكفاءة: بعد تعلم التصميم، كم بسرعة يمكن للمستخدمين أداء المهام؟"))

body.append(num_list_item(3, "Memorability",
    "When users RETURN to the design after a period of not using it, how easily can they re-establish proficiency?",
    "قابلية التذكر: عند عودة المستخدمين بعد فترة انقطاع، كم بسهولة يستعيدون كفاءتهم؟"))

body.append(num_list_item(4, "Errors",
    "How many errors do users make, how SEVERE are these errors, and how easily can they recover?",
    "الأخطاء: كم عدد الأخطاء التي يرتكبها المستخدمون، وكم خطورتها، وكم بسهولة يتعافون منها؟"))

body.append(num_list_item(5, "Satisfaction",
    "How PLEASANT is it to use the design? Covers the subjective experience of using the site.",
    "الرضا: كم يكون استخدام التصميم ممتعاً؟ يغطي التجربة الذاتية لاستخدام الموقع."))

body.append(tip("Mnemonic for Nielsen's 5 components: <strong>L-E-M-E-S</strong> — Learnability, Efficiency, Memorability, Errors, Satisfaction."))
body.append(trap("'Efficiency' in Nielsen's 5 components means SPEED for already-learned users — NOT resource efficiency as in the ISO definition. These are two different uses of the same word."))

body.append(section("Top Tasks Analysis (McGovern, 2018)"))
body.append(term(
    "Top Tasks Analysis",
    "A research methodology to identify and prioritize the tasks that matter MOST to users, "
    "then simplify the site around these. Based on customer surveys, search analysis, website "
    "analytics, and competitor review.",
    "تحليل أهم المهام: منهجية بحثية لتحديد وترتيب أولويات المهام الأكثر أهمية للمستخدمين، "
    "ثم تبسيط الموقع حولها. يعتمد على استطلاعات العملاء، تحليل البحث، تحليلات الموقع، ومراجعة المنافسين."
))

body.append('<div class="highlight-box"><strong>Key Statistic (McGovern):</strong> For a survey with 100 tasks:<br>'
    '• Top <strong>4–5 tasks</strong> get <strong>25%</strong> of the vote<br>'
    '• Next <strong>10–14 tasks</strong> get another 25%<br>'
    '• Next <strong>20–30 tasks</strong> get another 25%<br>'
    '• Remaining <strong>50–60 tasks</strong> get the bottom 25%<br>'
    '<span style="font-size:8pt;color:#555;">→ Typically 400 voters are enough to identify and rank the top 5 tasks.</span></div>')
body.append('<p class="arabic-def" dir="rtl" lang="ar">الإحصائية الرئيسية: في استطلاع بـ100 مهمة: أعلى 4-5 مهام تحصل على 25% من الأصوات، والـ 10-14 التالية على 25% أخرى، وهكذا. عادةً 400 مصوت يكفون لتحديد أعلى 5 مهام.</p>')

body.append(tip("Top tasks analysis proves that a small number of tasks drive the majority of user intent — focus design energy on these, not on secondary features."))

# ════════════════════════════════════════════════════════════════
# SECTION 6 – DIGITAL ACCESSIBILITY
# ════════════════════════════════════════════════════════════════
body.append(chapter_title("6. Digital Accessibility"))

body.append(term(
    "Digital Accessibility",
    "Allowing ALL users of a website to interact with it REGARDLESS of any disabilities "
    "they may have, or the web browser/platform they are using. The visually impaired are "
    "the primary beneficiary, but mobile users also benefit significantly.",
    "إمكانية الوصول الرقمي: السماح لجميع مستخدمي الموقع بالتفاعل معه بصرف النظر عن أي إعاقات قد يعانون منها، "
    "أو المتصفح أو المنصة التي يستخدمونها. المعاقون بصرياً هم المستفيد الرئيسي، لكن مستخدمي الجوال يستفيدون أيضاً."
))

body.append(term(
    "WAI (Website Accessibility Initiative)",
    "Guidelines produced by the World Wide Web Consortium (W3C) to promote web accessibility. "
    "Available at www.w3.org/WAI. Governments and NGOs also produce their own accessibility guidelines.",
    "مبادرة إمكانية الوصول للويب (WAI): مبادئ توجيهية يصدرها اتحاد شبكة الويب العالمية (W3C) "
    "لتعزيز إمكانية الوصول على الويب. الحكومات والمنظمات غير الحكومية تصدر أيضاً مبادئها الخاصة."
))

body.append(section("Common Accessibility Problems (W3C)"))
body.append("<ul>")
body.append(bullet("Images without alternative text (alt text) — screen readers cannot describe them", "صور بدون نص بديل — قارئات الشاشة لا تستطيع وصفها"))
body.append(bullet("Lack of alternative text for imagemap hotspots", "غياب النص البديل لنقاط الصور الخرائطية"))
body.append(bullet("Misleading use of structural elements on pages", "الاستخدام المضلل للعناصر الهيكلية في الصفحات"))
body.append(bullet("Uncaptioned audio or undescribed video", "الصوت بدون ترجمة أو الفيديو بدون وصف"))
body.append(bullet("Lack of alternative information for users who cannot access frames or scripts", "غياب معلومات بديلة للمستخدمين غير القادرين على الوصول للإطارات أو النصوص البرمجية"))
body.append("</ul>")

body.append(tip("Digital accessibility is both a legal requirement in many countries AND good business practice — it expands your audience reach."))
body.append(trap("Accessibility is NOT just for people with disabilities — mobile users (small screen, slow connection) also benefit from accessible design principles."))

# ════════════════════════════════════════════════════════════════
# SECTION 7 – PERSONALISATION
# ════════════════════════════════════════════════════════════════
body.append(chapter_title("7. Personalisation &amp; Cultural Customisation"))

body.append(term(
    "Personalisation",
    "Delivering tailored content, offers, or experiences to individual users based on "
    "their behaviour, preferences, or characteristics — ranging from simple rule-based "
    "targeting to AI-driven machine learning.",
    "التخصيص: تقديم محتوى أو عروض أو تجارب مخصصة للمستخدمين الأفراد بناءً على سلوكهم أو تفضيلاتهم أو خصائصهم "
    "— من الاستهداف القائم على القواعد البسيطة إلى التعلم الآلي المدفوع بالذكاء الاصطناعي."
))

body.append(section("4 Personalisation Options (from Monetate framework)"))
body.append("""<table class="ref-table">
<tr><th>Option / الخيار</th><th>Description / الوصف</th><th class="ar-cell">الوصف بالعربي</th></tr>
<tr><td><strong>A/B Testing</strong></td><td>Test two versions of a page to see which performs better</td><td class="ar-cell">اختبار نسختين من صفحة لمعرفة أيهما يؤدي أفضل</td></tr>
<tr><td><strong>Rule-Based</strong></td><td>Show content based on predefined rules (e.g., location, device)</td><td class="ar-cell">عرض محتوى بناءً على قواعد محددة مسبقاً (الموقع، الجهاز)</td></tr>
<tr><td><strong>Segmentation</strong></td><td>Group users by characteristics and serve segment-specific content</td><td class="ar-cell">تجميع المستخدمين حسب خصائصهم وتقديم محتوى مخصص للشريحة</td></tr>
<tr><td><strong>Machine-Driven</strong></td><td>AI/ML algorithms automatically optimize content for each user</td><td class="ar-cell">خوارزميات الذكاء الاصطناعي تُحسّن المحتوى تلقائياً لكل مستخدم</td></tr>
</table>""")

body.append(term(
    "Localisation &amp; Cultural Customisation",
    "Adapting a website's content, language, currency, images, and design to suit the "
    "cultural norms and expectations of users in specific geographic regions or countries. "
    "Includes full translation, cultural image selection, and local regulatory compliance.",
    "التوطين والتخصيص الثقافي: تكييف محتوى الموقع ولغته وعملته وصوره وتصميمه ليتناسب مع الأعراف الثقافية "
    "وتوقعات المستخدمين في مناطق أو دول جغرافية محددة. يشمل الترجمة الكاملة واختيار الصور الثقافية والامتثال التنظيمي المحلي."
))

body.append(tip("Personalisation options are on a spectrum from simple (A/B testing) to complex (machine-driven). Each step up the ladder requires more data and technology."))
body.append(trap("Localisation is NOT just translation — it also includes adjusting images (e.g., avoiding images inappropriate for a culture), payment methods, and legal compliance per country."))

# ════════════════════════════════════════════════════════════════
# SECTION 8 – INFORMATION ARCHITECTURE
# ════════════════════════════════════════════════════════════════
body.append(chapter_title("8. Information Architecture (IA)"))

body.append(term(
    "Information Architecture (IA)",
    "The structural design of a website or digital space to facilitate task completion and "
    "intuitive access to content. Involves defining organisation, labelling, and navigation "
    "schemes (Rosenfeld &amp; Morville, 2002).",
    "هندسة المعلومات: التصميم الهيكلي للموقع أو الفضاء الرقمي لتسهيل إكمال المهام والوصول البديهي للمحتوى. "
    "يتضمن تحديد مخططات التنظيم والتسمية والملاحة (روزنفيلد وموريفيل، 2002)."
))

body.append(section("4 Definitions of Information Architecture (Rosenfeld &amp; Morville, 2002)"))
body.append(num_list_item(1, "Definition 1",
    "The combination of organisation, labelling and navigation schemes within an information system.",
    "مجموعة مخططات التنظيم والتسمية والملاحة داخل نظام معلوماتي."))

body.append(num_list_item(2, "Definition 2",
    "The structural design of an information space to facilitate task completion and intuitive access to content.",
    "التصميم الهيكلي للفضاء المعلوماتي لتسهيل إكمال المهام والوصول البديهي للمحتوى."))

body.append(num_list_item(3, "Definition 3",
    "The art and science of structuring and classifying websites and intranets to help people find and manage information.",
    "فن وعلم هيكلة وتصنيف المواقع والشبكات الداخلية لمساعدة الناس على إيجاد المعلومات وإدارتها."))

body.append(num_list_item(4, "Definition 4",
    "An emerging discipline and community of practice focused on bringing principles of design and architecture to the digital landscape.",
    "تخصص ناشئ يركز على تطبيق مبادئ التصميم والهندسة على المشهد الرقمي."))

body.append(section("Key IA Tools"))
body.append(term(
    "Blueprint (Site Map)",
    "A high-level diagram showing the overall structure and hierarchy of the website — "
    "how pages and sections relate to each other. Used in planning and stakeholder communication.",
    "مخطط الموقع (Blueprint): مخطط عالي المستوى يُظهر الهيكل الكلي وتسلسل الموقع — كيف ترتبط الصفحات والأقسام ببعضها. "
    "يُستخدم في التخطيط والتواصل مع أصحاب المصلحة."
))

body.append(term(
    "Wireframe",
    "A low-fidelity, skeletal visual layout of a specific page showing the placement of "
    "content elements, navigation, and calls to action — without colour or final design. "
    "Used to test layout before expensive visual design work begins.",
    "الإطار السلكي (Wireframe): تخطيط بصري هيكلي منخفض الدقة لصفحة محددة يُظهر مواضع عناصر المحتوى والملاحة ودوافع الإجراء "
    "— دون ألوان أو تصميم نهائي. يُستخدم لاختبار التخطيط قبل بدء التصميم المرئي المكلف."
))

body.append(tip("Blueprint = big picture (whole site structure). Wireframe = detail level (individual page layout). Both come BEFORE visual design."))
body.append(trap("Wireframes deliberately exclude colours and images — if you add them, it becomes a mockup, not a wireframe. The purpose is to test layout without distracting visual elements."))

# ════════════════════════════════════════════════════════════════
# SECTION 9 – LANDING PAGES
# ════════════════════════════════════════════════════════════════
body.append(chapter_title("9. Landing Page Requirements"))

body.append(term(
    "Landing Page",
    "The first page a user sees after clicking on a search result, ad, or link. "
    "It must serve multiple aims simultaneously to convert visitors and reduce bounce rate.",
    "صفحة الهبوط: أول صفحة يراها المستخدم بعد النقر على نتيجة بحث أو إعلان أو رابط. "
    "يجب أن تحقق أهدافاً متعددة في آنٍ واحد لتحويل الزوار وتقليل معدل الارتداد."
))

body.append(term(
    "Bounce Rate",
    "The percentage of visitors who leave a website after viewing only one page without "
    "taking any action. A high bounce rate signals that the landing page failed to engage "
    "or meet visitors' expectations.",
    "معدل الارتداد: نسبة الزوار الذين يغادرون الموقع بعد مشاهدة صفحة واحدة فقط دون اتخاذ أي إجراء. "
    "معدل ارتداد مرتفع يشير إلى أن صفحة الهبوط فشلت في إشراك الزوار أو تلبية توقعاتهم."
))

body.append(section("6 Aims of an Effective Landing Page"))

body.append(num_list_item(1, "Generate Response",
    "Drive an online lead, sale, or offline callback. Page must have a PROMINENT call-to-action "
    "(CTA) button above the fold, repeated in text and image form.",
    "توليد استجابة: دفع الزائر لاتخاذ إجراء (عميل محتمل، بيع، طلب معاودة اتصال). يجب وجود زر دعوة للإجراء بارز فوق الطية، مكرر بالنص والصورة."))

body.append(num_list_item(2, "Engage Different Audience Types",
    "Reduce bounce rate by providing clear headlines and scent-trail trigger messages "
    "to show each visitor segment they are in the right place.",
    "إشراك أنواع مختلفة من الجمهور: تقليل معدل الارتداد بتوفير عناوين واضحة ورسائل دليل أثر (scent-trail) لإظهار أن الزائر في المكان الصحيح."))

body.append(num_list_item(3, "Communicate Key Brand Messages",
    "Explain clearly who you are, what you do, where you operate, and what makes you different. "
    "Your online value proposition must be compelling. Use customer testimonials.",
    "إيصال رسائل العلامة التجارية الرئيسية: توضيح من أنت وماذا تفعل وما يميزك. يجب أن تكون عرض القيمة مقنعاً. استخدام شهادات العملاء."))

body.append(num_list_item(4, "Answer the Visitor's Questions",
    "Different audiences have different questions. Identify FAQs for each audience type "
    "to reduce bounce rates and increase conversion.",
    "الإجابة على أسئلة الزائر: جماهير مختلفة لديها أسئلة مختلفة. تحديد الأسئلة الشائعة لكل نوع جمهور لتقليل الارتداد وزيادة التحويل."))

body.append(num_list_item(5, "Showcase Range of Offers (Cross-sell)",
    "Show recommendations for related or best-selling products and display the full range "
    "of your offering through navigation.",
    "عرض مجموعة العروض (بيع متقاطع): عرض توصيات بالمنتجات ذات الصلة أو الأكثر مبيعاً وإظهار النطاق الكامل للعروض عبر التنقل."))

body.append(num_list_item(6, "Attract Visitors Through SEO",
    "Ensure good ranking for relevant search terms. Navigation, copy, and page templates "
    "must signal relevance to search engines through on-page optimisation.",
    "جذب الزوار من خلال تحسين محركات البحث (SEO): ضمان ترتيب جيد لمصطلحات البحث ذات الصلة. التنقل والمحتوى وقوالب الصفحة يجب أن تشير للصلة بمحركات البحث."))

body.append(tip("Above the fold = the area visible without scrolling. ALWAYS put the primary CTA above the fold."))
body.append(tip("'Scent-trail' messages are trigger words/images that tell each visitor segment 'you're in the right place' — matching the ad/search term they used."))
body.append(trap("A landing page has MULTIPLE aims — not just generating a sale. Missing aims like brand communication or SEO means you are leaving value on the table."))

# ════════════════════════════════════════════════════════════════
# SECTION 10 – DEFINING SITE/APP REQUIREMENTS
# ════════════════════════════════════════════════════════════════
body.append(chapter_title("10. Defining Site or App Requirements"))

body.append(term(
    "Discovery / Analysis Phase",
    "The research phase of a digital project that uses marketing research techniques to "
    "identify business needs and audience requirements before design begins.",
    "مرحلة الاكتشاف/التحليل: مرحلة البحث في المشروع الرقمي التي تستخدم تقنيات بحث التسويق "
    "لتحديد احتياجات العمل ومتطلبات الجمهور قبل بدء التصميم."
))

body.append(section("Key Considerations for Site/App Requirements"))
body.append("<ul>")
body.append(bullet("Business requirements — align to commercial and marketing goals", "متطلبات العمل — التوافق مع الأهداف التجارية والتسويقية"))
body.append(bullet("Usability requirements — task completion, ease of use", "متطلبات قابلية الاستخدام — إكمال المهام، سهولة الاستخدام"))
body.append(bullet("Web accessibility requirements — WAI/W3C compliance", "متطلبات إمكانية الوصول — الامتثال لمعايير WAI/W3C"))
body.append(bullet("Personalisation requirements — rule-based to machine-driven", "متطلبات التخصيص — من القواعد إلى الذكاء الاصطناعي"))
body.append(bullet("Localisation and cultural customisation", "التوطين والتخصيص الثقافي"))
body.append(bullet("Reviewing competitor websites — benchmarking", "مراجعة مواقع المنافسين — المقارنة المعيارية"))
body.append(bullet("Designing the information architecture — blueprints and wireframes", "تصميم هندسة المعلومات — المخططات والإطارات السلكية"))
body.append("</ul>")

# ════════════════════════════════════════════════════════════════
# SECTION 11 – RESPONSIVE & MOBILE DESIGN
# ════════════════════════════════════════════════════════════════
body.append(chapter_title("11. Responsive Web Design (RWD) &amp; Mobile"))

body.append(term(
    "Responsive Web Design (RWD)",
    "A design approach where a single website automatically adjusts its layout, images, "
    "and content to fit the screen size of any device — desktop, tablet, or smartphone. "
    "Recommended over separate mobile sites because it is easier to maintain and better for SEO.",
    "تصميم الويب المتجاوب: نهج تصميم يتكيف فيه موقع واحد تلقائياً في تخطيطه وصوره ومحتواه ليتناسب مع حجم شاشة أي جهاز "
    "— سطح المكتب، الجهاز اللوحي، أو الهاتف الذكي. يُوصى به لأنه أسهل في الصيانة وأفضل لتحسين محركات البحث."
))

body.append(term(
    "Mobile-Optimised Site",
    "A website specifically designed for mobile users — may have a separate URL (e.g., m.example.com) "
    "or a dedicated mobile template. Older approach that has largely been replaced by RWD.",
    "الموقع المحسّن للجوال: موقع مصمم خصيصاً لمستخدمي الجوال — قد يكون له URL منفصل (مثل m.example.com). "
    "نهج أقدم تم استبداله إلى حد كبير بالتصميم المتجاوب."
))

body.append(section("Internet of Things (IoT)"))
body.append(term(
    "Internet of Things (IoT)",
    "The network of physical objects ('things') — vehicles, appliances, wearables — embedded "
    "with sensors and connectivity that enables them to collect and exchange data. "
    "Creates new opportunities for contextual, real-time digital marketing.",
    "إنترنت الأشياء: شبكة الأجسام المادية (المركبات، الأجهزة، الأجهزة القابلة للارتداء) المدمجة بمستشعرات واتصالية "
    "تمكّنها من جمع البيانات وتبادلها. يخلق فرصاً جديدة للتسويق الرقمي السياقي في الوقت الفعلي."
))

body.append(section("Augmented Reality (AR) &amp; Virtual Reality (VR)"))
body.append(term(
    "Virtual Reality (VR)",
    "A fully immersive digital environment replacing the real world — users wear a headset "
    "to experience a simulated 3D world. Applications in marketing: virtual product tours, "
    "brand experiences.",
    "الواقع الافتراضي: بيئة رقمية غامرة تماماً تحل محل العالم الحقيقي — يرتدي المستخدمون نظارة للتجربة. "
    "تطبيقات التسويق: جولات المنتجات الافتراضية، تجارب العلامة التجارية."
))

body.append(term(
    "Augmented Reality (AR)",
    "Overlaying digital information (images, text, 3D objects) onto the real world view "
    "via a smartphone or smart glasses. Allows users to 'try' products in their real environment "
    "before purchase (e.g., IKEA Place app — visualise furniture in your room).",
    "الواقع المعزز: تراكب معلومات رقمية (صور، نصوص، كائنات ثلاثية الأبعاد) على رؤية العالم الحقيقي عبر الهاتف الذكي. "
    "يتيح للمستخدمين 'تجربة' المنتجات في بيئتهم الحقيقية قبل الشراء."
))

body.append(tip("RWD is the RECOMMENDED approach today because it uses one URL (better for SEO) and one codebase (easier to maintain)."))
body.append(trap("AR and VR are NOT the same — VR replaces reality entirely (headset), while AR overlays digital elements onto the real world (smartphone camera)."))

# ════════════════════════════════════════════════════════════════
# SECTION 12 – INFORMATION PROCESSING
# ════════════════════════════════════════════════════════════════
body.append(chapter_title("12. Information Processing Model"))

body.append(term(
    "Information Processing",
    "The cognitive process by which users encounter, pay attention to, understand, accept, "
    "and retain marketing messages from a digital medium. Has 5 sequential stages.",
    "معالجة المعلومات: العملية المعرفية التي يواجه من خلالها المستخدمون رسائل التسويق الرقمي وينتبهون إليها "
    "ويفهمونها ويقبلونها ويحتفظون بها. تتكون من 5 مراحل متتالية."
))

body.append(section("5 Stages of Information Processing"))
body.append('<p class="arabic-def" dir="rtl" lang="ar">المراحل الخمس لمعالجة المعلومات:</p>')

body.append(num_list_item(1, "Exposure (التعرض)",
    "The content must be present long enough to be processed. Banner ad content may not be on screen long enough.",
    "يجب أن يكون المحتوى موجوداً لفترة كافية ليتم معالجته. محتوى إعلانات البانر قد لا يكون على الشاشة طويلاً بما يكفي."))

body.append(num_list_item(2, "Attention (الانتباه)",
    "User's eyes will be directed toward headings and content — NOT toward graphics or animated elements "
    "(Nielsen, 2000). Focus on headlines and precise labelling is vital.",
    "ستتجه عيون المستخدم نحو العناوين والمحتوى، وليس نحو الرسومات والعناصر المتحركة. التركيز على العناوين والتسميات الدقيقة أمر حيوي."))

body.append(num_list_item(3, "Understanding / Comprehension (الفهم والإدراك)",
    "The user's interpretation of the content — does the text/design communicate the intended message clearly?",
    "تفسير المستخدم للمحتوى — هل يوصل النص/التصميم الرسالة المقصودة بوضوح؟"))

body.append(num_list_item(4, "Acceptance / Yielding (الاستسلام والقبول)",
    "Whether the information presented is accepted by the customer. Is the copy (text) persuasive "
    "and credible?",
    "هل المعلومات المقدمة مقبولة من قِبل العميل؟ هل النص مقنع وذو مصداقية؟"))

body.append(num_list_item(5, "Retention (الاحتفاظ)",
    "For traditional advertising, this describes how well information is remembered. "
    "For web, it is about whether the user retains the experience long enough to convert.",
    "بالنسبة للإعلانات التقليدية، يصف مدى تذكر المعلومات. للويب، يتعلق بما إذا كان المستخدم يحتفظ بالتجربة طويلاً بما يكفي للتحويل."))

body.append('<div class="highlight-box"><strong>Key insight on Banner Blindness:</strong> Users typically ignore banner ads and suffer from "banner blindness" — they focus on headings and navigation instead. Focusing on headlines and precise labelling is critical to capturing attention (Stage 2).</div>')
body.append('<p class="arabic-def" dir="rtl" lang="ar">عمى اللافتات: المستخدمون عادةً يتجاهلون الإعلانات البانرية ويعانون من "عمى اللافتات" — يركزون على العناوين والملاحة بدلاً من ذلك. التركيز على العناوين والتسميات الدقيقة أمر حيوي لالتقاط الانتباه.</p>')

body.append(tip("In the Information Processing model, the sequence is ALWAYS: Exposure → Attention → Understanding → Acceptance → Retention. Each stage is a prerequisite for the next."))
body.append(trap("Banner blindness means users do NOT pay attention to banner ads — so Stage 2 (Attention) is where most online ads fail. Design for headlines, not banners."))

# ════════════════════════════════════════════════════════════════
# SECTION 13 – ONLINE RETAIL MERCHANDISING
# ════════════════════════════════════════════════════════════════
body.append(chapter_title("13. Online Retail Merchandising"))

body.append(term(
    "Online Retail Merchandising",
    "Applying merchandising principles to an e-commerce website to maximise conversion "
    "and average order value — making products easy to find, compare, and buy.",
    "تجارة التجزئة الإلكترونية: تطبيق مبادئ الترويج للبضائع على موقع التجارة الإلكترونية لتعظيم التحويل "
    "ومتوسط قيمة الطلب — جعل المنتجات سهلة الإيجاد والمقارنة والشراء."
))

body.append(section("5 Common Approaches to Online Retail Merchandising"))
body.append("<ul>")
body.append(bullet("Expanding navigation through synonyms — ensure products are findable regardless of terminology used",
    "توسيع التنقل عبر المرادفات — ضمان إمكانية العثور على المنتجات بغض النظر عن المصطلحات المستخدمة"))
body.append(bullet("Applying faceted navigation — allow filtering by multiple attributes simultaneously (colour, size, price, brand)",
    "تطبيق الملاحة متعددة الأوجه — السماح بالتصفية بواسطة سمات متعددة في آنٍ واحد (اللون، الحجم، السعر، العلامة التجارية)"))
body.append(bullet("Featuring the best-selling products — prominently display top-sellers to guide purchase decisions",
    "إبراز المنتجات الأكثر مبيعاً — العرض البارز للمنتجات الأعلى مبيعاً لتوجيه قرارات الشراء"))
body.append(bullet("Use of bundling — combine complementary products into packages (cross-sell/upsell)",
    "استخدام التجميع — دمج المنتجات التكميلية في حزم (بيع متقاطع / بيع إضافي)"))
body.append(bullet("Use of customer ratings — social proof to increase trust and purchase confidence",
    "استخدام تقييمات العملاء — الدليل الاجتماعي لزيادة الثقة والثقة في الشراء"))
body.append("</ul>")

body.append(term(
    "Faceted Navigation",
    "A navigation system allowing users to filter search results by multiple attributes "
    "simultaneously (e.g., filter by colour AND size AND price range). Essential for large "
    "product catalogues — prevents users from being overwhelmed.",
    "الملاحة متعددة الأوجه: نظام ملاحة يسمح للمستخدمين بتصفية نتائج البحث بواسطة سمات متعددة في وقت واحد "
    "(مثل: تصفية حسب اللون والحجم ونطاق السعر). ضرورية للكتالوجات الكبيرة — تمنع المستخدمين من الشعور بالإرهاق."
))

body.append(tip("Customer ratings are one of the highest-converting elements on an e-commerce site — social proof reduces the perceived risk of purchase."))

# ════════════════════════════════════════════════════════════════
# SECTION 14 – SERVICE QUALITY & E-LOYALTY
# ════════════════════════════════════════════════════════════════
body.append(chapter_title("14. Service Quality &amp; e-Loyalty"))

body.append(term(
    "e-Loyalty",
    "The tendency of a customer to return to and continue purchasing from the same website. "
    "Driven by the quality of the overall digital service experience across multiple dimensions.",
    "الولاء الإلكتروني: ميل العميل للعودة والاستمرار في الشراء من نفس الموقع. "
    "يتشكل بجودة تجربة الخدمة الرقمية الشاملة عبر أبعاد متعددة."
))

body.append(section("5 Dimensions of Service Quality Affecting e-Loyalty"))
body.append('<p class="arabic-def" dir="rtl" lang="ar">أبعاد جودة الخدمة الخمسة المؤثرة على الولاء الإلكتروني:</p>')

body.append(num_list_item(1, "Tangibles (الملموسات)",
    "The appearance of physical facilities, equipment, and the website design — ease of use, "
    "content quality, availability, and pricing.",
    "مظهر المرافق المادية والمعدات وتصميم الموقع — سهولة الاستخدام وجودة المحتوى والتوفر والأسعار."))

body.append(num_list_item(2, "Reliability &amp; Responsiveness (الموثوقية والاستجابة)",
    "Reliability: site availability and email response reliability. Responsiveness: "
    "download speed, email response time, callback speed.",
    "الموثوقية: توفر الموقع وموثوقية الرد بالبريد الإلكتروني. الاستجابة: سرعة التنزيل، وقت الرد، سرعة معاودة الاتصال."))

body.append(num_list_item(3, "Assurance (الضمان)",
    "The knowledge and courtesy of staff and their ability to convey trust and confidence. "
    "Includes security of transactions and privacy protection.",
    "معرفة الموظفين ولطفهم وقدرتهم على نقل الثقة والمصداقية. يشمل أمان المعاملات وحماية الخصوصية."))

body.append(num_list_item(4, "Multichannel Communication Preferences (تفضيلات التواصل متعدد القنوات)",
    "The ability to interact with the brand through preferred channels (web, phone, email, "
    "chat, social media) — fulfilment and call centre contact.",
    "القدرة على التفاعل مع العلامة التجارية عبر القنوات المفضلة (الويب، الهاتف، البريد الإلكتروني، الدردشة). إنجاز الطلبات والتواصل مع مركز الاتصال."))

body.append(num_list_item(5, "Empathy (التعاطف)",
    "Caring, individualised attention — personalisation of communication, privacy protection, "
    "and treating each customer as an individual.",
    "الرعاية الفردية — تخصيص التواصل وحماية الخصوصية والتعامل مع كل عميل كفرد مستقل."))

# ════════════════════════════════════════════════════════════════
# SECTION 15 – WEBQUAL
# ════════════════════════════════════════════════════════════════
body.append(chapter_title("15. WebQual — 14 Dimensions of Website Quality"))

body.append(term(
    "WebQual",
    "A comprehensive model for measuring website quality across 14 dimensions — covering "
    "information quality, usability, trust, emotional appeal, service, and more. "
    "Used to benchmark a website's quality against competitors.",
    "نموذج شامل لقياس جودة الموقع عبر 14 بُعداً — يغطي جودة المعلومات، قابلية الاستخدام، الثقة، "
    "الجاذبية العاطفية، الخدمة، وغيرها. يُستخدم لمقارنة جودة الموقع بالمنافسين."
))

body.append("""<table class="ref-table">
<tr><th>#</th><th>Dimension / البُعد</th><th>Definition / التعريف</th><th class="ar-cell">بالعربي</th></tr>
<tr><td>1</td><td>Information Quality</td><td>Accurate, updated and appropriate information</td><td class="ar-cell">معلومات دقيقة ومحدّثة ومناسبة</td></tr>
<tr><td>2</td><td>Functional Fit to Task</td><td>Website meets user needs</td><td class="ar-cell">الموقع يلبي احتياجات المستخدم</td></tr>
<tr><td>3</td><td>Tailored Communications</td><td>Communications can be personalised to the user</td><td class="ar-cell">يمكن تخصيص التواصل للمستخدم</td></tr>
<tr><td>4</td><td>Trust</td><td>Secure communication and information privacy</td><td class="ar-cell">التواصل الآمن وخصوصية المعلومات</td></tr>
<tr><td>5</td><td>Response Time</td><td>Time to get a response after a request or interaction</td><td class="ar-cell">الوقت للحصول على استجابة بعد طلب أو تفاعل</td></tr>
<tr><td>6</td><td>Ease of Understanding</td><td>Easy to read and understand the content</td><td class="ar-cell">المحتوى سهل القراءة والفهم</td></tr>
<tr><td>7</td><td>Intuitive Operations</td><td>Easy to operate and navigate</td><td class="ar-cell">سهل التشغيل والتنقل</td></tr>
<tr><td>8</td><td>Visual Appeal</td><td>The aesthetics and look of the site</td><td class="ar-cell">الجماليات والمظهر البصري للموقع</td></tr>
<tr><td>9</td><td>Innovativeness</td><td>Creativity and uniqueness of the website</td><td class="ar-cell">الإبداع والتفرد في الموقع</td></tr>
<tr><td>10</td><td>Emotional Appeal</td><td>Emotional effect and intensity of involvement</td><td class="ar-cell">الأثر العاطفي وشدة التورط</td></tr>
<tr><td>11</td><td>Consistent Image</td><td>Site image compatible with that in other media</td><td class="ar-cell">صورة الموقع متوافقة مع سائر الوسائط</td></tr>
<tr><td>12</td><td>Online Completeness</td><td>All necessary transactions can be completed online</td><td class="ar-cell">جميع المعاملات الضرورية يمكن إتمامها أونلاين</td></tr>
<tr><td>13</td><td>Relative Advantage</td><td>Equivalent to or better than other channels of interaction</td><td class="ar-cell">مكافئ أو أفضل من قنوات التفاعل الأخرى</td></tr>
<tr><td>14</td><td>Customer Service</td><td>Responsive and helpful customer support</td><td class="ar-cell">دعم عملاء متجاوب ومفيد</td></tr>
</table>""")

body.append(tip("WebQual has 14 dimensions — exams often test whether you can recall and explain them. The key groupings: Information → Usability → Trust → Emotions → Service."))
body.append(trap("'Online Completeness' (dimension 12) means all transactions can be done ONLINE — a site that requires offline follow-up for core transactions fails this dimension."))
body.append(trap("'Consistent Image' (dimension 11) means the website image must NOT create dissonance with how the brand appears in other media (TV, print, etc.)."))

# ════════════════════════════════════════════════════════════════
# QUICK REFERENCE TABLES
# ════════════════════════════════════════════════════════════════
body.append(chapter_title("Quick Reference Summary Tables"))

body.append(section("At a Glance: Key Models &amp; Their Authors"))
body.append("""<table class="ref-table">
<tr><th>Model / النموذج</th><th>Author / المؤلف</th><th>Year / السنة</th><th>Key Numbers / الأرقام الرئيسية</th></tr>
<tr><td>Online Brand Equity</td><td>Christodoulides et al.</td><td>2006</td><td>5 dimensions</td></tr>
<tr><td>Usability Components</td><td>Jakob Nielsen</td><td>2012</td><td>5 components (L-E-M-E-S)</td></tr>
<tr><td>Usability ISO Standard</td><td>ISO</td><td>9241-210</td><td>Effectiveness + Efficiency + Satisfaction</td></tr>
<tr><td>Top Tasks Analysis</td><td>McGovern</td><td>2018</td><td>Top 4-5 tasks = 25% of votes; 400 voters</td></tr>
<tr><td>Information Architecture</td><td>Rosenfeld & Morville</td><td>2002</td><td>4 definitions</td></tr>
<tr><td>Information Processing</td><td>—</td><td>—</td><td>5 stages (Exposure→Retention)</td></tr>
<tr><td>Service Quality / e-Loyalty</td><td>—</td><td>—</td><td>5 dimensions (TRAME)</td></tr>
<tr><td>WebQual</td><td>—</td><td>—</td><td>14 dimensions</td></tr>
<tr><td>Landing Page Aims</td><td>—</td><td>—</td><td>6 aims</td></tr>
<tr><td>Personalisation Options</td><td>Monetate</td><td>—</td><td>4 options (A/B→Machine)</td></tr>
</table>""")

body.append(section("Mnemonic Cheat Sheet"))
body.append('<p class="arabic-def" dir="rtl" lang="ar">مساعدات التذكر:</p>')
body.append("<ul>")
body.append(bullet("Nielsen's 5 Usability Components → <strong>L-E-M-E-S</strong>: Learnability, Efficiency, Memorability, Errors, Satisfaction",
    "مكونات قابلية الاستخدام الخمسة: التعلم، الكفاءة، التذكر، الأخطاء، الرضا"))
body.append(bullet("Online Brand Equity 5 Dimensions → <strong>E-O-R-T-F</strong>: Emotional Connection, Online Experience, Responsive Service, Trust, Fulfilment",
    "أبعاد حقوق الملكية الخمسة: الارتباط العاطفي، التجربة الإلكترونية، الخدمة الاستجابية، الثقة، الإنجاز"))
body.append(bullet("Information Processing 5 Stages → <strong>E-A-U-A-R</strong>: Exposure, Attention, Understanding, Acceptance, Retention",
    "مراحل معالجة المعلومات: التعرض، الانتباه، الفهم، القبول، الاحتفاظ"))
body.append(bullet("Service Quality 5 Dimensions → <strong>T-R-A-M-E</strong>: Tangibles, Reliability/Responsiveness, Assurance, Multichannel, Empathy",
    "أبعاد جودة الخدمة: الملموسات، الموثوقية/الاستجابة، الضمان، تعدد القنوات، التعاطف"))
body.append(bullet("Landing Page 6 Aims → <strong>Generate, Engage, Communicate, Answer, Showcase, Attract</strong>",
    "أهداف صفحة الهبوط الستة: توليد، إشراك، توصيل، إجابة، عرض، جذب"))
body.append("</ul>")

# ── BUILD HTML ───────────────────────────────────────────────────
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>{CSS}</style>
</head>
<body>
{''.join(body)}
</body>
</html>"""

with open("mktb_ch7_summary.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Saved: mktb_ch7_summary.html")

from weasyprint import HTML as WHTML
WHTML(string=html).write_pdf("mktb_ch7_summary.pdf")
print("Saved: mktb_ch7_summary.pdf")
