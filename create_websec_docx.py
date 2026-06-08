"""Word document version of Web Application Security summary."""
from docx import Document
from docx.shared import RGBColor, Pt, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from datetime import date

BLUE  = RGBColor(0x00, 0x70, 0xC0)
RED   = RGBColor(0xC0, 0x00, 0x00)
GREEN = RGBColor(0x37, 0x86, 0x10)
NAVY  = RGBColor(0x1F, 0x39, 0x64)
TEAL  = RGBColor(0x17, 0x6B, 0x7F)
ORANGE= RGBColor(0xC0, 0x55, 0x00)

KEY_RED    = {"always","never","must","cannot","only","critical","important",
              "warning","not","never","first","prior","before"}
KEY_ORANGE = {"note","required","ensure","secure","all","every","any","essential"}

def shd(para, fill):
    pPr = para._p.get_or_add_pPr()
    e = OxmlElement('w:shd')
    e.set(qn('w:val'),'clear'); e.set(qn('w:color'),'auto'); e.set(qn('w:fill'), fill)
    pPr.append(e)

def colorize(run, word):
    tok = word.lower().strip(".,;:()")
    if tok in KEY_RED:   run.font.color.rgb = RED;    run.font.bold = True
    elif tok in KEY_ORANGE: run.font.color.rgb = ORANGE; run.font.bold = True

def ch(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(2)
    r = p.add_run(text); r.font.size=Pt(13); r.font.bold=True; r.font.color.rgb=NAVY
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bot = OxmlElement('w:bottom')
    bot.set(qn('w:val'),'single'); bot.set(qn('w:sz'),'6')
    bot.set(qn('w:space'),'1'); bot.set(qn('w:color'),'1F3964')
    pBdr.append(bot); pPr.append(pBdr)

def sec(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4); p.paragraph_format.space_after = Pt(1)
    r = p.add_run(text); r.font.size=Pt(10.5); r.font.bold=True; r.font.color.rgb=TEAL

def trm(doc, name, defn):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1.5); p.paragraph_format.space_after = Pt(1.5)
    p.paragraph_format.left_indent = Inches(0.12)
    r = p.add_run(name + ": "); r.font.color.rgb=BLUE; r.font.bold=True; r.font.size=Pt(9.5)
    for w in defn.split():
        run = p.add_run(w + " "); run.font.size=Pt(9.5); colorize(run, w)

def tipf(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent=Inches(0.12); p.paragraph_format.space_before=Pt(2)
    p.paragraph_format.space_after=Pt(2); shd(p,'E2EFDA')
    r = p.add_run("Exam Tip: "); r.font.bold=True; r.font.color.rgb=GREEN; r.font.size=Pt(8.5)
    p.add_run(text).font.size=Pt(8.5)

def trapf(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent=Inches(0.12); p.paragraph_format.space_before=Pt(2)
    p.paragraph_format.space_after=Pt(2); shd(p,'FCE4D6')
    r = p.add_run("Exam Trap: "); r.font.bold=True; r.font.color.rgb=RED; r.font.size=Pt(8.5)
    p.add_run(text).font.size=Pt(8.5)

def blt(doc, text):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.left_indent=Inches(0.3); p.paragraph_format.space_before=Pt(1)
    p.paragraph_format.space_after=Pt(1)
    for w in text.split():
        run = p.add_run(w + " "); run.font.size=Pt(9.5); colorize(run, w)

doc = Document()
for s in doc.sections:
    s.top_margin=Cm(1.6); s.bottom_margin=Cm(1.6); s.left_margin=Cm(1.9); s.right_margin=Cm(1.9)
doc.styles['Normal'].font.name='Calibri'; doc.styles['Normal'].font.size=Pt(9.5)

# Cover
doc.add_paragraph(); doc.add_paragraph()
p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
r=p.add_run("Web Application Security"); r.font.size=Pt(24); r.font.bold=True; r.font.color.rgb=NAVY
p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
r=p.add_run("Study Summary — Chapters 1–13"); r.font.size=Pt(14); r.font.color.rgb=TEAL
doc.add_paragraph()
p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
r=p.add_run("Applied College | Web Security Course"); r.font.size=Pt(11); r.font.bold=True
doc.add_paragraph()
p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
r=p.add_run(f"Prepared: {date.today().strftime('%B %Y')}"); r.font.size=Pt(10); r.font.color.rgb=RGBColor(0x70,0x70,0x70)
doc.add_page_break()

# Ch1
ch(doc,"Chapter 1: The History of Software Security")
sec(doc,"Key Definitions")
trm(doc,"Software Security","A set of practices protecting software applications from attackers, incorporated into the SDLC and testing processes.")
trm(doc,"Hacking","The unauthorized access to or control over computer network security systems for illicit purposes.")
trm(doc,"Enigma Machine (1930)","Electro-mechanical rotor device that used a symmetric key algorithm — one key for both encryption and decryption. Used in WWII.")
trm(doc,"Symmetric Key Algorithm","A cipher using a single cryptographic key for both encryption and decryption. Still used today for securing data in transit.")
trm(doc,"Turing Test","Alan Turing's test to rate machine-generated conversations based on how hard they are to distinguish from human conversations. Foundation of AI.")
trm(doc,"Morris Worm (1988)","One of the first internet worms; led to the creation of CERT — the first formal security incident response team.")
trm(doc,"CERT","Computer Emergency Response Team; created after the Morris Worm; marked the beginning of organized software security.")
tipf(doc,"Enigma machine = origin of symmetric-key cryptography. Symmetric = one key for both encrypt and decrypt.")
tipf(doc,"Turing: (1) broke Enigma code in WWII, (2) created the Turing Test for AI. Both contributions may appear on the exam.")
trapf(doc,"Symmetric ≠ Asymmetric. Symmetric = 1 key. Asymmetric = 2 keys (public + private).")
trapf(doc,"CERT was created AFTER the Morris Worm. Formal security organizations did not exist before 1988.")

# Ch2
ch(doc,"Chapter 2: Web Application Reconnaissance")
sec(doc,"Key Definitions")
trm(doc,"Recon (Reconnaissance)","Explorative data-gathering that occurs prior to hacking. Performed by hackers, pen testers, and security engineers.")
trm(doc,"Information Gathering","Investigating the target using publicly available info: website, WHOIS, ARIN, DNS records.")
trm(doc,"WHOIS Database","Public registry containing domain owner info: names, phone numbers, email addresses.")
trm(doc,"ARIN","American Registry for Internet Numbers — provides info about who owns specific IP addresses or ranges.")
trm(doc,"Social Engineering","Deceiving people into revealing sensitive information via phone, email, or impersonation. Results in leaking passwords, credit cards, bank accounts.")
trm(doc,"Dumpster Diving","Searching physical trash for discarded documents, disks, or post-it notes containing credentials or sensitive data.")
trm(doc,"Web Application Mapping","Building a map of the structure, organization, and functionality of a web app. Must be the first step before attempting to hack.")
tipf(doc,"Recon is used by both attackers AND security engineers — finding weaknesses before attackers do.")
tipf(doc,"WHOIS + ARIN + DNS together = comprehensive picture of a target's infrastructure.")
trapf(doc,"Web app mapping must always be the FIRST step. Never attempt hacking without first mapping the target.")
trapf(doc,"Social engineering exploits human psychology, not software. Technical skill is not required.")

# Ch3
ch(doc,"Chapter 3: Finding Subdomains")
sec(doc,"Key Definitions")
trm(doc,"Subdomain","A subdivision of a primary domain hosting separate services. Large organizations have many subdomains.")
trm(doc,"Zone Transfer Attack","A DNS attack that retrieves the entire DNS zone file from a misconfigured server, exposing all subdomains at once.")
trm(doc,"Brute Force / Dictionary Attack","Systematically guessing subdomain names using wordlists to discover hidden or undocumented subdomains.")
sec(doc,"Recon Methods")
blt(doc,"Browser Network Analysis Tools (DevTools → Network tab)")
blt(doc,"Public Records (GitHub, certificates, WHOIS)")
blt(doc,"Search Engine Caches")
blt(doc,"Accidental Archives (leaked repos, exposed configs)")
blt(doc,"Zone Transfer Attacks (DNS misconfiguration)")
blt(doc,"Brute Forcing / Dictionary Attacks on subdomain names")
tipf(doc,"Browser Network tab shows all HTTP requests including subdomains — quick first step for mapping.")
trapf(doc,"Zone transfer only works on misconfigured DNS servers. Most modern servers restrict it — do not rely on it.")

# Ch4
ch(doc,"Chapter 4: API Analysis")
sec(doc,"Key Definitions")
trm(doc,"API Analysis","Second step in recon (after subdomain discovery); provides understanding of the API structure and purpose.")
trm(doc,"REST API","Specifies resources (not functions) in endpoints; stateless; hierarchical. The preferred modern API format.")
trm(doc,"SOAP API","Older, more rigid API format. REST is now more popular.")
trm(doc,"OPTIONS Method","Special HTTP method that reveals which HTTP verbs an API endpoint supports. First go-to during API recon.")
trm(doc,"Stateless API","Server does not keep track of requesters — each request must contain all information needed to process it.")
tipf(doc,"Send OPTIONS request first when probing an API — reveals supported verbs without modifying data.")
trapf(doc,"OPTIONS is not always available — most enterprise APIs disable it. Do not rely solely on OPTIONS.")
trapf(doc,"REST is stateless — server does NOT store session state. Do not confuse REST with SOAP's stateful sessions.")

# Ch5
ch(doc,"Chapter 5: Identifying Third-Party Dependencies")
sec(doc,"Key Definitions")
trm(doc,"Third-Party Dependency","External code integrated into an application; often NOT subject to robust security review. Can be attack vectors.")
trm(doc,"CVE Database","Common Vulnerabilities and Exposures — public database of known vulnerabilities. Attackers copy existing exploits from it.")
trm(doc,"SPA Framework","Single Page Application framework rendering pages in the browser. Major: React (Facebook), Angular (Google), Vue (Adobe/GitLab), Ember.")
trm(doc,"Prototype Pollution","JavaScript vulnerability where an attacker modifies the prototype of a base object, affecting all instances.")
trm(doc,"ReDoS","Regular Expression Denial of Service — exploits poorly written regex that takes exponential time on certain inputs.")
tipf(doc,"Detecting the exact library version lets you search CVE for known exploits — no custom attack writing needed.")
trapf(doc,"Third-party libraries are NOT automatically safe. Always verify versions against CVE databases.")

# Ch6
ch(doc,"Chapter 6: Identifying Weak Points in Application Architecture")
sec(doc,"Key Definitions")
trm(doc,"Architectural Vulnerability","Most vulnerabilities stem from improperly designed architecture, not poorly written individual methods.")
trm(doc,"Multiple Vulnerabilities Indicator","A single vulnerability may be bad code. Multiple vulnerabilities = broken architecture.")
trm(doc,"Security Levels","Secure: security built in before and during development. Insecure: no security implementation.")
trm(doc,"XSS Risk via innerHTML","Any method passing HTML directly to the DOM is a risk — allows script execution on another user's machine.")
trm(doc,"Multiple Layers of Security","XSS attack layers in IM: (1) API POST, (2) DB Write, (3) DB Read, (4) API GET, (5) Client Read.")
tipf(doc,"Multiple same-type vulnerabilities signal broken architecture — not just a coding mistake.")
trapf(doc,"Fixing one vulnerability does not fix the architecture. New vulnerabilities will keep appearing if the architecture is insecure.")

# Ch7
ch(doc,"Chapter 7: Introduction to Hacking Web Applications")
sec(doc,"Key Definitions")
trm(doc,"XSS — Cross-Site Scripting","Attacker uploads malicious scripts onto a website. Three types: Stored (DB), Reflected (server), DOM-based (browser).")
trm(doc,"CSRF — Cross-Site Request Forgery","Tricks authenticated user into unknowingly submitting a malicious request; server cannot distinguish from legitimate request.")
trm(doc,"XXE — XML External Entity","Attack against XML parsers; allows attacker to read server files, perform SSRF, or execute code via external entities.")
trm(doc,"SQL Injection","Injecting malicious SQL into unsanitized input fields to gain unauthorized database access, modification, or deletion.")
trm(doc,"DoS — Denial of Service","Makes a service unavailable by overwhelming it or exploiting vulnerabilities like ReDoS.")
trm(doc,"Hacker's Mindset","A hacker seeks existing entry points rather than creating them; is organized, technically skilled, and constantly learning.")
tipf(doc,"OWASP designates Stored, Reflected, and DOM-based XSS as the three most common XSS attack vectors. Know all three.")
trapf(doc,"CSRF does not steal data — it forces the victim to perform an action. XSS executes code / steals data. Do not confuse their mechanisms.")

# Ch8
ch(doc,"Chapter 8: Web Security — Securing Modern Web Applications")
sec(doc,"Key Definitions")
trm(doc,"Defensive Software Architecture","Security must begin in the architecture phase — before any code is written. Easier to fix architectural flaws before deployment.")
trm(doc,"Code Review for Security","Every commit reviewed for security; must include an unrelated team to avoid conflict of interest.")
trm(doc,"Bug Bounty Program","Incentivizes external researchers to find and responsibly disclose vulnerabilities before attackers exploit them.")
trm(doc,"Red Team / Blue Team","Red team: internal attackers. Blue team: defenders. Together they improve overall security posture.")
trm(doc,"Regression Testing","Ensures previously fixed vulnerabilities are not reintroduced in newer code releases.")
trm(doc,"Vulnerability Triage","Prioritizing discovered vulnerabilities based on risk level — not all vulnerabilities require immediate fixes.")
tipf(doc,"Course order: Recon → Offense → Defense. Understanding attacks is essential for building defenses.")
tipf(doc,"Code review checks: data transmission, data storage, data presentation to users, and server-side operations.")
trapf(doc,"Architecture review comes FIRST, then code review. Never start code review without architecture review.")
trapf(doc,"Customer notification for vulnerabilities is reactive. Always use proactive methods: bug bounty, red team, pen testing.")

# Ch9
ch(doc,"Chapter 9: Secure Application Architecture")
sec(doc,"Key Definitions")
trm(doc,"Architecture Phase Cost (NIST)","Fixing a vulnerability in the design phase costs 30–60 times less than fixing it in production.")
trm(doc,"Data in Transit","All network data must be encrypted en route. Required: SSL or TLS before any data is transmitted.")
trm(doc,"TLS vs SSL","TLS offers the most rigid security. SSL has higher adoption but multiple known vulnerabilities. HTTPS requires TLS/SSL.")
trm(doc,"Password Entropy","The randomness and uncertainty of a password. High entropy = secure. Patterns make passwords weak regardless of length.")
trm(doc,"Dictionary Attack","Uses a list of the most common passwords to brute-force credentials. Effective against low-entropy passwords.")
trm(doc,"2FA (Two-Factor Authentication)","Requires two forms of ID: something you know (password) + something you have (OTP) or something you are (biometric).")
trm(doc,"PII (Personally Identifiable Information)","Data that could identify a specific person. Must be stored with special security and legal compliance.")
trm(doc,"Credential Hashing","Passwords must never be stored in plaintext. Always use a strong one-way hash (bcrypt, Argon2) with a unique salt per user.")
tipf(doc,"NIST key stat: architecture-phase fixes are 30–60x cheaper than production fixes. This number appears on exams.")
tipf(doc,"TLS is preferred over SSL. When asked about securing data in transit, the answer is TLS (or HTTPS).")
trapf(doc,"Password length alone does NOT make a password secure — entropy (unpredictability) is what matters.")
trapf(doc,"Never store passwords in plaintext or with reversible encryption. Always use one-way hashing with salt.")

# Ch10
ch(doc,"Chapter 10: Reviewing Code for Security")
sec(doc,"Key Definitions")
trm(doc,"Security Code Review","Checks for common vulnerabilities AND logic bugs. Always occurs AFTER the architecture review.")
trm(doc,"Logic Bug","Vulnerability from flawed business logic; cannot be found by automated tools. Requires human understanding of the feature's purpose.")
trm(doc,"Blacklist (Anti-Pattern)","Only blocks known bad inputs; only protects if you have perfect knowledge of all current and future threats — impossible.")
trm(doc,"Whitelist (Preferred)","Explicitly defines what IS allowed, rejecting everything else. More secure than blacklist.")
trm(doc,"Code Review Flow","1. git checkout master, 2. git pull origin master, 3. git checkout feature, 4. git diff origin/master.")
tipf(doc,"Code review must always occur AFTER architecture review — this is the correct and only acceptable order.")
tipf(doc,"Whitelist is always preferred over blacklist for input validation.")
trapf(doc,"Blacklists give false security — they can almost always be bypassed with encoding tricks. Never rely on blacklists as primary defense.")
trapf(doc,"Automated scanners cannot find logic bugs. Human review is always required for logic-level security.")

# Ch11
ch(doc,"Chapter 11: Vulnerability Discovery")
sec(doc,"Key Definitions")
trm(doc,"Security Automation","First step in vulnerability discovery after architecture and code reviews. Forms: static analysis, dynamic analysis, regression testing.")
trm(doc,"Static Analysis","Analyzes source code for syntax errors and common vulnerabilities without executing code. Not suitable for dynamically typed languages.")
trm(doc,"Dynamic Analysis","Tests the running application; detects runtime vulnerabilities like race conditions.")
trm(doc,"Vulnerability Regression Testing","Verifies previously fixed vulnerabilities are not reintroduced in new releases.")
sec(doc,"Static Analysis Tools")
blt(doc,"Checkmarx — most major languages (paid)")
blt(doc,"PMD — Java (free)")
blt(doc,"Bandit — Python (free)")
blt(doc,"Brakeman — Ruby (free)")
tipf(doc,"Static analysis works best with statically typed languages (Java, C#). Struggles with JavaScript (dynamic typing).")
trapf(doc,"Automation cannot detect logical flaws or vulnerability chaining. Always supplement with manual review.")

# Ch12
ch(doc,"Chapter 12: Vulnerability Management")
sec(doc,"Key Definitions")
trm(doc,"SSDL (Secure Software Development Life Cycle)","A well-defined pipeline for obtaining, triaging, and resolving vulnerabilities from architecture through production.")
trm(doc,"Staging Environment","Mimics production environment as closely as possible, used to reproduce vulnerabilities without affecting real users.")
trm(doc,"Reproducing a Vulnerability","First step in management: verify it's real, avoid paying for false bug bounty, gain insight for fixing.")
trm(doc,"CVSS (Common Vulnerability Scoring System)","Freely published system for ranking vulnerabilities on ease of exploitation and potential damage. Three metrics: Base, Temporal, Environmental.")
trm(doc,"CVSS Base Metrics","Intrinsic vulnerability characteristics constant over time: Exploitability + Impact metrics.")
trm(doc,"CVSS Temporal Metrics","Scores severity over time — availability of exploits, patches, and workarounds change the effective risk.")
trm(doc,"CVSS Environmental Metrics","Scores vulnerability based on the specific environment's security controls and affected system criticality.")
tipf(doc,"CVSS has THREE groups: Base (constant), Temporal (changes over time), Environmental (context-specific).")
tipf(doc,"Always reproduce a vulnerability in a staging environment — staging mimics production but has no real user data.")
trapf(doc,"Not all vulnerabilities need immediate fixes. Risk assessment determines priority — never treat all with equal urgency.")
trapf(doc,"Known unlogged vulnerabilities being actively exploited have caused company failures. Always add logging while fixing.")

# Ch13
ch(doc,"Chapter 13: Defending Against XSS, CSRF & XXE")
sec(doc,"Key Definitions")
trm(doc,"XSS Root Cause","Failure to sanitize user inputs embedded in web pages. Conditions: app accepts user input, creates dynamic content, input is insufficiently validated.")
trm(doc,"Anti-XSS Golden Rule","'Do not allow any user-supplied data to be passed into the DOM — except as strings.' Use innerText, not innerHTML.")
trm(doc,"innerText vs innerHTML","innerText: safe — treats content as plain text. innerHTML: dangerous — interprets content as HTML/JS. Always prefer innerText.")
trm(doc,"Input Sanitization","Removing or escaping dangerous content from user input. Must allow some tags (strong, i) but block others (script).")
trm(doc,"DOMParser Risk","parseFromString() loads HTML/XML strings into DOM nodes — loading untrusted content can execute malicious scripts.")
trm(doc,"CSRF Token","A unique, unpredictable token embedded in forms; server validates it on every state-changing request — cannot be forged by attackers.")
trm(doc,"SameSite Cookie","Cookie attribute preventing cross-site request sending. SameSite=Strict or Lax significantly reduces CSRF attack surface.")
trm(doc,"XXE Defense","Disable external entity processing in the XML parser. Never allow user-supplied XML to define external entities.")
trm(doc,"SQL Injection Defense","Use parameterized queries (prepared statements) only. Never concatenate user strings directly into SQL queries.")
trm(doc,"Content Security Policy (CSP)","HTTP response header telling browsers which content sources are legitimate. Reduces XSS by blocking inline scripts and untrusted sources.")
tipf(doc,"innerText is always the safe choice for displaying user content. Only use innerHTML when HTML rendering is absolutely required.")
tipf(doc,"CSRF tokens + SameSite cookies together = strong CSRF protection. Use both.")
trapf(doc,"Sanitizing by blacklisting tags (like script) is insufficient — attackers bypass with encoding tricks. Use a whitelist or trusted library.")
trapf(doc,"CSP does NOT prevent all XSS — it reduces impact. Input sanitization is still required. Never rely on CSP alone.")
trapf(doc,"SQL injection cannot be fixed by input filtering alone — parameterized queries are the only complete defense.")

doc.save("websec_summary.docx")
print("Saved: websec_summary.docx")
