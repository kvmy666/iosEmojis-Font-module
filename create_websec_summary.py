"""
Web Application Security – Study Summary
13 Chapters | 13–16 pages target
Same format as Apache summary (blue terms, red keywords, exam tips/traps)
"""
import re
from datetime import date

KEYWORDS_RED    = {"always","never","must","cannot","only","critical",
                   "important","warning","do not","not","must not",
                   "never","first","prior","before"}
KEYWORDS_ORANGE = {"note","required","ensure","secure","essential","all",
                   "every","any"}

def colorize(text):
    parts = re.split(r'(\s+)', text)
    out = []
    for p in parts:
        tok = p.lower().strip(".,;:()")
        if tok in KEYWORDS_RED:
            out.append(f'<span class="kw-red">{p}</span>')
        elif tok in KEYWORDS_ORANGE:
            out.append(f'<span class="kw-orange">{p}</span>')
        else:
            out.append(p)
    return "".join(out)

def term(name, definition):
    return (f'<p class="term">'
            f'<span class="term-name">{name}:</span> '
            f'{colorize(definition)}</p>')

def code(line):
    return f'<pre class="code">{line}</pre>'

def tip(text):
    return f'<div class="tip"><strong>Exam Tip:</strong> {colorize(text)}</div>'

def trap(text):
    return f'<div class="trap"><strong>Exam Trap:</strong> {colorize(text)}</div>'

def bullet(text):
    return f'<li>{colorize(text)}</li>'

def chapter(title):
    return f'<h2>{title}</h2>'

def section(title):
    return f'<h3>{title}</h3>'

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
body { font-family: Calibri, Arial, sans-serif; font-size:9.5pt; color:#222; line-height:1.45; }
h1   { color:#1F3964; font-size:24pt; margin:0 0 6pt; }
.subtitle { color:#17738F; font-size:13pt; margin:4pt 0; }
.course   { font-size:11pt; font-weight:bold; margin:6pt 0; }
.date-line{ color:#888; font-size:10pt; }
h2 {
    color:#1F3964; font-size:12.5pt; font-weight:bold;
    border-bottom:2pt solid #1F3964;
    padding-bottom:2pt; margin:0; margin-bottom:4pt;
    page-break-before: always;
}
h3 { color:#17738F; font-size:10pt; font-weight:bold; margin-top:8pt; margin-bottom:2pt; }
p.term { margin:2.5pt 0 2.5pt 10pt; font-size:9.5pt; }
span.term-name { color:#0070C0; font-weight:bold; }
span.kw-red    { color:#C00000; font-weight:bold; }
span.kw-orange { color:#C05500; font-weight:bold; }
pre.code {
    font-family:'Courier New',monospace; font-size:8pt;
    background:#F2F2F2; color:#26343F;
    margin:2pt 0 2pt 18pt; padding:3pt 6pt;
    border-radius:3pt; white-space:pre-wrap; word-break:break-all;
}
ul { margin:2pt 0 2pt 24pt; padding:0; }
li { margin:1pt 0; font-size:9.5pt; }
.tip  { background:#E2EFDA; border-left:3pt solid #378610; padding:3pt 7pt; margin:3pt 0 3pt 8pt; font-size:8.5pt; }
.tip strong { color:#378610; }
.trap { background:#FCE4D6; border-left:3pt solid #C00000; padding:3pt 7pt; margin:3pt 0 3pt 8pt; font-size:8.5pt; }
.trap strong { color:#C00000; }
.ref-table { width:100%; border-collapse:collapse; font-size:8.5pt; margin:4pt 0 4pt 8pt; }
.ref-table th { background:#1F3964; color:white; padding:3pt 6pt; text-align:left; }
.ref-table td { border:1pt solid #BFBFBF; padding:2pt 6pt; }
.ref-table tr:nth-child(even) td { background:#F2F2F2; }
"""

body = []

# ── COVER ───────────────────────────────────────────────────────
body.append(f"""
<div class="cover">
  <h1>Web Application Security</h1>
  <p class="subtitle">Study Summary &ndash; Chapters 1&ndash;13</p>
  <br>
  <p class="course">Applied College &nbsp;|&nbsp; Web Security Course</p>
  <p style="font-size:9pt;color:#444;margin-top:8pt;">
    Textbook: <em>Web Application Security</em> &mdash; Andrew Hoffman, O&rsquo;Reilly, 2020
  </p>
  <br>
  <p style="font-size:9pt;color:#444;line-height:1.8;">
    Ch1: History of Software Security &bull; Ch2: Web App Reconnaissance &bull; Ch3: Finding Subdomains<br>
    Ch4: API Analysis &bull; Ch5: Third-Party Dependencies &bull; Ch6: Weak Points in Architecture<br>
    Ch7: Hacking Web Applications &bull; Ch8: Web Security &bull; Ch9: Secure Architecture<br>
    Ch10: Reviewing Code &bull; Ch11: Vulnerability Discovery &bull; Ch12: Vulnerability Management<br>
    Ch13: Defending Against XSS, CSRF &amp; XXE
  </p>
  <br><br>
  <p class="date-line">Prepared: {date.today().strftime('%B %Y')}</p>
</div>
""")

# ════════════════════════════════════════════════════════════════
# CHAPTER 1 – THE HISTORY OF SOFTWARE SECURITY
# ════════════════════════════════════════════════════════════════
body.append(chapter("Chapter 1: The History of Software Security"))
body.append(section("Key Definitions"))

body.append(term("Software Security",
    "A set of practices that help protect software applications and digital solutions "
    "from attackers, incorporated into the software development life cycle and testing processes."))

body.append(term("Hacking",
    "An attempt to exploit a computer system or private network — the unauthorized access to or "
    "control over computer network security systems for illicit purposes."))

body.append(term("Enigma Machine (circa 1930)",
    "An electric-powered mechanical rotor device used to encrypt and decrypt text messages. "
    "It used a symmetric key algorithm — encrypting and decrypting with a single cryptographic key."))

body.append(term("Symmetric Key Algorithm",
    "A cipher that uses a single cryptographic key for both encryption and decryption. "
    "Used by the Enigma machine; still used today for securing data in transit."))

body.append(term("Turing Test",
    "A test developed by Alan Turing to rate conversations generated by machines based on how "
    "difficult it is to differentiate them from human conversations. A foundational concept in AI."))

body.append(term("Morris Worm (1988)",
    "One of the first recognized internet worms; caused widespread damage and led to the creation "
    "of CERT (Computer Emergency Response Team) — the first formal security incident response team."))

body.append(term("CERT (Computer Emergency Response Team)",
    "The first formal security incident response organization, established in response to the "
    "Morris Worm. Marked the beginning of organized software security as a discipline."))

body.append(tip("The Enigma machine is the origin of modern symmetric-key cryptography. Symmetric = one key for both encryption and decryption."))
body.append(tip("Alan Turing is associated with two major contributions: (1) breaking the Enigma code (WWII), (2) the Turing Test (AI foundation)."))
body.append(trap("Symmetric key ≠ asymmetric key. Symmetric uses ONE key; asymmetric (public key cryptography) uses TWO keys (public + private)."))
body.append(trap("CERT was created AFTER the Morris Worm (1988), not before. Formal security organizations did not exist prior to the worm."))

# ════════════════════════════════════════════════════════════════
# CHAPTER 2 – WEB APPLICATION RECONNAISSANCE
# ════════════════════════════════════════════════════════════════
body.append(chapter("Chapter 2: Introduction to Web Application Reconnaissance"))
body.append(section("Key Definitions"))

body.append(term("Web Application Reconnaissance (Recon)",
    "The explorative data-gathering phase that generally occurs prior to hacking a web application. "
    "Performed by hackers, pen testers, or security engineers to find weakly secured mechanisms."))

body.append(term("Information Gathering",
    "Investigating the target using publicly available information. "
    "Includes: organization website, WHOIS databases, ARIN (IP ownership), and DNS records."))

body.append(term("WHOIS Database",
    "A public registry containing information about domain owners including names, telephone numbers, "
    "and email addresses — a primary reconnaissance source."))

body.append(term("ARIN (American Registry for Internet Numbers)",
    "A database that provides information about who owns a specific IP address or range of addresses. "
    "Used during recon to identify server owners."))

body.append(term("Social Engineering",
    "Deceiving people into revealing sensitive or useful information via phone, email, or impersonation. "
    "Results in leaking passwords, credit card numbers, and bank account details."))

body.append(term("Dumpster Diving",
    "An attack technique where an attacker searches through physical trash to find old documents, "
    "discarded disks, or post-it notes containing usernames, passwords, or other sensitive data."))

body.append(term("Web Application Mapping",
    "Building a map representing the structure, organization, and functionality of a web application. "
    "This must be the first step before attempting to hack a web application."))

body.append(tip("Reconnaissance is NOT only performed by attackers — security engineers use the same recon techniques to find and fix weaknesses before attackers do."))
body.append(tip("WHOIS + ARIN + DNS together provide a comprehensive picture of a target's network infrastructure."))
body.append(trap("Web application mapping must always be the FIRST step — never attempt hacking without first mapping the target application."))
body.append(trap("Social engineering attacks do not require any technical skill — they exploit human psychology, not software vulnerabilities."))

# ════════════════════════════════════════════════════════════════
# CHAPTER 3 – FINDING SUBDOMAINS
# ════════════════════════════════════════════════════════════════
body.append(chapter("Chapter 3: Finding Subdomains"))
body.append(section("Key Definitions"))

body.append(term("Subdomain",
    "A subdivision of a primary domain used to host separate services (email, admin, file servers). "
    "Large organizations typically have many subdomains attached to their primary domain."))

body.append(term("Zone Transfer Attack",
    "A DNS attack technique that attempts to retrieve the entire DNS zone file from a misconfigured "
    "DNS server, exposing all subdomains and internal host records at once."))

body.append(term("Brute Force / Dictionary Attack (Subdomains)",
    "Systematically guessing subdomain names using wordlists to discover undocumented or hidden subdomains "
    "that are not listed in public records."))

body.append(section("Subdomain Recon Methods"))
body.append("<ul>")
body.append(bullet("Browser's built-in Network Analysis Tools (DevTools → Network tab)."))
body.append(bullet("Public Records (GitHub repos, certificates, WHOIS)."))
body.append(bullet("Search Engine Caches (Google, Bing cached pages)."))
body.append(bullet("Accidental Archives (leaked repos, exposed configuration files)."))
body.append(bullet("Social Snapshots (Twitter API, LinkedIn)."))
body.append(bullet("Zone Transfer Attacks (DNS misconfiguration exploit)."))
body.append(bullet("Brute Forcing / Dictionary Attacks on subdomain names."))
body.append("</ul>")

body.append(tip("The browser Network tab shows all HTTP requests including those to subdomains — a quick first step for mapping affiliated servers."))
body.append(trap("Zone transfer is only possible on misconfigured DNS servers. Most modern servers restrict zone transfers — do not assume it will always work."))

# ════════════════════════════════════════════════════════════════
# CHAPTER 4 – API ANALYSIS
# ════════════════════════════════════════════════════════════════
body.append(chapter("Chapter 4: API Analysis"))
body.append(section("Key Definitions"))

body.append(term("API Analysis",
    "The second step in web application recon, following subdomain discovery. "
    "Provides information needed to understand the purpose and structure of an exposed API."))

body.append(term("REST API",
    "Representational State Transfer API; specifies resources rather than functions in endpoints, "
    "is stateless (server does not track requesters), and is hierarchical."))

body.append(term("SOAP API",
    "Simple Object Access Protocol; an older, more rigid API format. "
    "REST is now more popular and is the preferred structure for modern web applications."))

body.append(term("OPTIONS Method",
    "A special HTTP method that only exists to provide information about which HTTP verbs "
    "an API endpoint supports. The first go-to method when performing recon against an API."))

body.append(term("Stateless API",
    "A REST API design principle where the server does not keep track of its requesters. "
    "Each request must contain all the information needed to process it independently."))

body.append(section("Authentication Schemes"))
body.append("""<table class="ref-table">
<tr><th>Scheme</th><th>How it works</th></tr>
<tr><td>Session Cookie</td><td>Server creates a session ID stored in a browser cookie</td></tr>
<tr><td>JWT (JSON Web Token)</td><td>Signed token containing claims; sent with every request</td></tr>
<tr><td>OAuth 2.0</td><td>Token-based delegated authorization; used for third-party login</td></tr>
<tr><td>Basic Auth</td><td>Base64-encoded username:password sent in the Authorization header</td></tr>
<tr><td>API Key</td><td>Static key passed in header or query string to identify the caller</td></tr>
</table>""")

body.append(tip("Send an OPTIONS request first when probing an API — it reveals supported HTTP verbs without modifying any data."))
body.append(trap("OPTIONS is not always available — most enterprise APIs disable it. Do not rely solely on OPTIONS for endpoint discovery."))
body.append(trap("REST APIs are stateless — the server does NOT store session state. Do not confuse REST statelessness with SOAP's stateful sessions."))

# ════════════════════════════════════════════════════════════════
# CHAPTER 5 – IDENTIFYING THIRD-PARTY DEPENDENCIES
# ════════════════════════════════════════════════════════════════
body.append(chapter("Chapter 5: Identifying Third-Party Dependencies"))
body.append(section("Key Definitions"))

body.append(term("Third-Party Dependency",
    "External code integrated into a web application (proprietary or open-source). "
    "Often not subject to as robust a security review as in-house code; can become attack vectors."))

body.append(term("CVE (Common Vulnerabilities and Exposures)",
    "A public database of known security vulnerabilities. If a vulnerable third-party dependency "
    "is detected, an attacker may copy an existing attack directly from the CVE database."))

body.append(term("SPA Framework (Single Page Application)",
    "A client-side JavaScript framework that renders pages in the browser without full page reloads. "
    "Major SPA frameworks: React (Facebook), AngularJS (Google), VueJS (Adobe/GitLab), EmberJS."))

body.append(term("Prototype Pollution",
    "A JavaScript vulnerability where an attacker can modify the prototype of a base object, "
    "potentially affecting all instances and enabling unexpected code execution."))

body.append(term("ReDoS (Regular Expression Denial of Service)",
    "An attack that exploits poorly written regular expressions that take exponential time to evaluate "
    "certain inputs, causing a denial of service."))

body.append(section("Detecting SPA Frameworks"))
body.append("""<table class="ref-table">
<tr><th>Framework</th><th>Detection Method</th></tr>
<tr><td>EmberJS</td><td>Global <code>Ember</code> object; DOM elements with <code>id=ember1</code>, <code>class="ember-application"</code></td></tr>
<tr><td>AngularJS</td><td>Global <code>angular</code> or <code>ng</code> object; first root element has <code>ng-version</code> attribute</td></tr>
<tr><td>React</td><td>Global <code>React</code> object; <code>&lt;script type="text/jsx"&gt;</code> tags</td></tr>
<tr><td>VueJS</td><td>Global <code>Vue</code> object; <code>Vue.version</code> constant</td></tr>
</table>""")

body.append(tip("Detecting the exact version of a third-party library lets you search CVE databases for known exploits — even before writing custom attacks."))
body.append(trap("Third-party dependencies are NOT automatically safe just because they are popular or open-source. Always verify versions against CVE databases."))

# ════════════════════════════════════════════════════════════════
# CHAPTER 6 – IDENTIFYING WEAK POINTS IN APPLICATION ARCHITECTURE
# ════════════════════════════════════════════════════════════════
body.append(chapter("Chapter 6: Identifying Weak Points in Application Architecture"))
body.append(section("Key Definitions"))

body.append(term("Architectural Vulnerability",
    "Most vulnerabilities stem from improperly designed application architecture rather than "
    "from poorly written individual methods. Architecture flaws affect entire features, not just one function."))

body.append(term("Multiple Vulnerabilities Indicator",
    "A single vulnerability may result from bad code. "
    "Multiple vulnerabilities in the same application indicate weaknesses in the architecture itself."))

body.append(term("Security Levels",
    "Secure: implements security prior to and during feature development. "
    "Middle-level: partial security. "
    "Insecure: no security implementation at all."))

body.append(term("XSS Risk via innerHTML",
    "Any method that provides HTML directly to the DOM is a risk because it allows HTML to be "
    "uploaded (if sanitization is not provided) and can execute scripts on another user's machine."))

body.append(term("Multiple Layers of Security",
    "Layers for XSS risk in an IM application: (1) API POST, (2) Database Write, "
    "(3) Database Read, (4) API GET, (5) Client Read. Each layer must be secured."))

body.append(tip("Look for multiple vulnerabilities of the same type — they signal a broken security architecture, not just a coding mistake."))
body.append(trap("Fixing one vulnerability does not fix the architecture. If the architecture is insecure, new vulnerabilities will keep appearing in the same areas."))

# ════════════════════════════════════════════════════════════════
# CHAPTER 7 – INTRODUCTION TO HACKING WEB APPLICATIONS
# ════════════════════════════════════════════════════════════════
body.append(chapter("Chapter 7: Introduction to Hacking Web Applications"))
body.append(section("Key Definitions"))

body.append(term("XSS — Cross-Site Scripting",
    "An attacker uploads malicious script code onto a website that can steal data or perform damage. "
    "Three types: Stored (in database), Reflected (not stored, reflected by server), DOM-based (in browser)."))

body.append(term("CSRF — Cross-Site Request Forgery",
    "An attack that tricks an authenticated user into unknowingly submitting a malicious request. "
    "The server cannot distinguish between a legitimate request and a forged one."))

body.append(term("XXE — XML External Entity",
    "An attack against applications that parse XML input. Allows an attacker to view files on the "
    "server's file system, perform SSRF, or execute code by injecting external entity references."))

body.append(term("SQL Injection",
    "Injecting malicious SQL commands into input fields that are passed unsanitized into database "
    "queries, enabling unauthorized data access, modification, or deletion."))

body.append(term("DoS — Denial of Service",
    "An attack that makes a system or service unavailable by overwhelming it with requests or "
    "exploiting vulnerabilities (e.g., ReDoS — crafted regex input causing exponential processing time)."))

body.append(term("Hacker's Mindset",
    "A hacker analyzes existing code to seek entry points rather than making them. "
    "A great hacker is organized, technically skilled, and constantly learning new techniques."))

body.append("""<table class="ref-table">
<tr><th>Attack</th><th>Designated by OWASP</th><th>Target</th></tr>
<tr><td>Stored XSS</td><td>Yes</td><td>Database → Client browser</td></tr>
<tr><td>Reflected XSS</td><td>Yes</td><td>Server response → Client browser</td></tr>
<tr><td>DOM-based XSS</td><td>Yes</td><td>Client-side JavaScript execution</td></tr>
<tr><td>CSRF</td><td>Yes</td><td>Authenticated user session</td></tr>
<tr><td>SQL Injection</td><td>Yes</td><td>Database layer</td></tr>
<tr><td>XXE</td><td>Yes</td><td>XML parser / Server file system</td></tr>
</table>""")

body.append(tip("OWASP designates Stored, Reflected, and DOM-based XSS as the three most common XSS attack vectors — know all three types."))
body.append(trap("CSRF does not steal data — it forces the victim to perform an action. XSS steals data/executes code. Do not confuse their mechanisms."))

# ════════════════════════════════════════════════════════════════
# CHAPTER 8 – WEB SECURITY (SECURING MODERN WEB APPLICATIONS)
# ════════════════════════════════════════════════════════════════
body.append(chapter("Chapter 8: Web Security — Securing Modern Web Applications"))
body.append(section("Key Definitions"))

body.append(term("Defensive Software Architecture",
    "Security begins prior to any code being written, in the architecture phase. "
    "It is much easier to catch and resolve deep architectural security flaws before writing code."))

body.append(term("Comprehensive Code Reviews",
    "Every commit should be reviewed for security standards before release. "
    "Code reviews must be performed not only by the committer's team but also by an unrelated team."))

body.append(term("Bug Bounty Program",
    "A program that incentivizes external security researchers to find and responsibly disclose "
    "vulnerabilities in exchange for monetary rewards, before malicious actors find them."))

body.append(term("Red Team / Blue Team",
    "Red team: internal attackers who try to exploit the application. "
    "Blue team: defenders who detect and respond to attacks. Together they improve security posture."))

body.append(term("Regression Testing",
    "Testing that ensures a previously fixed vulnerability has not been reintroduced in newer code. "
    "Critical because fixes can sometimes break other parts of the application or be undone."))

body.append(term("Vulnerability Triage",
    "The process of prioritizing discovered vulnerabilities based on risk level. "
    "Not all vulnerabilities carry equal risk — some can wait, others require immediate patching."))

body.append(tip("The order in the book (and course) is: Recon → Offense → Defense. Understanding attack techniques is essential for building effective defenses."))
body.append(tip("Code review should check: how data is transmitted, how data is stored, how data is presented to users, and what operations occur on the server."))
body.append(trap("Code review alone is NOT enough — architecture review must come first, then code review, then vulnerability discovery. Never skip the architecture phase."))
body.append(trap("Old-fashioned vulnerability discovery via customer notification or public disclosure is reactive — always prefer proactive methods (bug bounty, red team)."))

# ════════════════════════════════════════════════════════════════
# CHAPTER 9 – SECURE APPLICATION ARCHITECTURE
# ════════════════════════════════════════════════════════════════
body.append(chapter("Chapter 9: Secure Application Architecture"))
body.append(section("Key Definitions"))

body.append(term("Architecture Phase — Cost of Security",
    "NIST study finding: 'The cost of removing an application security vulnerability during the "
    "design phase is 30–60 times less than if removed during production.'"))

body.append(term("Data in Transit",
    "All data sent over the network must be encrypted en route to prevent man-in-the-middle attacks. "
    "Required: SSL or TLS before any data is transmitted."))

body.append(term("TLS vs SSL",
    "TLS (Transport Layer Security) offers the most rigid security. "
    "SSL (Secure Sockets Layer) has higher adoption but multiple known vulnerabilities. "
    "HTTPS requires TLS/SSL before allowing any data to be sent."))

body.append(term("Password Entropy",
    "The amount of randomness and uncertainty in a password. "
    "Secure passwords have high entropy — pattern-based passwords are weak regardless of length."))

body.append(term("Dictionary Attack",
    "A brute-force technique where the attacker uses a list of the most common passwords to guess "
    "credentials. Most effective against low-entropy (predictable) passwords."))

body.append(term("2FA — Two-Factor Authentication",
    "Requires users to provide two forms of identification: something they know (password) and "
    "something they have (phone OTP) or something they are (biometric)."))

body.append(term("PII (Personally Identifiable Information)",
    "Any data that could be used to identify a specific individual. "
    "Must be stored with special security measures and handled according to legal regulations."))

body.append(term("Credential Hashing",
    "Passwords must never be stored in plaintext — they must be hashed using a strong "
    "one-way function (e.g., bcrypt, Argon2) with a unique salt per user."))

body.append(tip("NIST recommends fixing security in the architecture phase — 30–60x cheaper than fixing in production. This is a key exam statistic."))
body.append(tip("TLS is preferred over SSL. When the exam asks about securing data in transit, the answer is TLS (or HTTPS)."))
body.append(trap("Password length and special characters alone do NOT make a password secure — entropy (randomness/unpredictability) is what matters."))
body.append(trap("Never store passwords in plaintext or with reversible encryption. Always use one-way hashing with salt."))

# ════════════════════════════════════════════════════════════════
# CHAPTER 10 – REVIEWING CODE FOR SECURITY
# ════════════════════════════════════════════════════════════════
body.append(chapter("Chapter 10: Reviewing Code for Security"))
body.append(section("Key Definitions"))

body.append(term("Security Code Review",
    "Checks for common vulnerabilities (XSS, CSRF, injection) AND logic-level vulnerabilities "
    "that require deep understanding of the code's purpose. Always occurs after the architecture review."))

body.append(term("Logic Bug",
    "A vulnerability that arises from flawed business logic rather than a common coding mistake. "
    "Cannot be found by automated tools — requires understanding the feature's purpose."))

body.append(term("Blacklist (Anti-Pattern)",
    "A temporary security measure that only blocks known bad inputs. "
    "Only protects if you have perfect knowledge of ALL current and future malicious inputs — impossible in practice."))

body.append(term("Whitelist (Preferred)",
    "Explicitly defines what IS allowed, rejecting everything else. "
    "More secure than a blacklist because it does not rely on enumerating all possible threats."))

body.append(term("Code Review Flow",
    "1. git checkout master, 2. git pull origin master, 3. git checkout feature-branch, "
    "4. git diff origin/master — shows changed files and diffs against master."))

body.append(term("Where to Start a Security Review",
    "1. Client-side code (understand business logic), 2. API layer, 3. Dependencies, "
    "4. Unintentionally exposed public APIs, 5. Remainder of codebase."))

body.append(tip("Code review must always occur AFTER the architecture review — never before. This is the correct order."))
body.append(tip("A whitelist is always preferred over a blacklist for input validation — it is impossible to know every possible future malicious input."))
body.append(trap("Blacklists give a false sense of security — they can almost always be bypassed by an attacker who knows the pattern. Never rely on them as a primary defense."))
body.append(trap("Automated scanners cannot find logic bugs — they only find archetypical vulnerabilities. Human review is always required for logic-level security."))

# ════════════════════════════════════════════════════════════════
# CHAPTER 11 – VULNERABILITY DISCOVERY
# ════════════════════════════════════════════════════════════════
body.append(chapter("Chapter 11: Vulnerability Discovery"))
body.append(section("Key Definitions"))

body.append(term("Security Automation",
    "The first step after architecture and code reviews in discovering vulnerabilities. "
    "Automation is cheap, effective, and long-lasting. Three forms: static analysis, dynamic analysis, regression testing."))

body.append(term("Static Analysis",
    "Scripts that analyze source code for syntax errors and common vulnerabilities without executing code. "
    "Can be run locally, on-demand, or on each commit. NOT suitable for dynamically typed languages."))

body.append(term("Dynamic Analysis",
    "Tests the running application for vulnerabilities. Executes code and observes behavior. "
    "Can detect issues that only appear at runtime (e.g., race conditions)."))

body.append(term("Vulnerability Regression Testing",
    "Automated tests that verify previously fixed vulnerabilities have not been reintroduced. "
    "Essential for ensuring that fixes stay fixed across new releases."))

body.append(section("Static Analysis Tools"))
body.append("""<table class="ref-table">
<tr><th>Tool</th><th>Language</th><th>Cost</th></tr>
<tr><td>Checkmarx</td><td>Most major languages</td><td>Paid</td></tr>
<tr><td>PMD</td><td>Java</td><td>Free</td></tr>
<tr><td>Bandit</td><td>Python</td><td>Free</td></tr>
<tr><td>Brakeman</td><td>Ruby</td><td>Free</td></tr>
</table>""")

body.append(section("What Static Analysis Can Detect"))
body.append("<ul>")
body.append(bullet("General XSS: Look for DOM manipulation with innerHTML."))
body.append(bullet("Reflected XSS: Look for variables pulled from URL parameters."))
body.append(bullet("DOM XSS: Look for dangerous DOM sinks like setInterval()."))
body.append(bullet("SQL Injection: Look for user-provided strings in database queries."))
body.append(bullet("CSRF: Look for state-changing GET requests."))
body.append(bullet("DoS: Look for improperly written regular expressions."))
body.append("</ul>")

body.append(tip("Static analysis is best for statically typed languages (Java, C#). It struggles with dynamically typed languages like JavaScript."))
body.append(trap("Automation cannot detect logical flaws or vulnerability chaining (multiple weak vulnerabilities combined into one strong exploit). Always supplement with manual review."))

# ════════════════════════════════════════════════════════════════
# CHAPTER 12 – VULNERABILITY MANAGEMENT
# ════════════════════════════════════════════════════════════════
body.append(chapter("Chapter 12: Vulnerability Management"))
body.append(section("Key Definitions"))

body.append(term("SSDL (Secure Software Development Life Cycle)",
    "A well-defined pipeline for obtaining, triaging, and resolving vulnerabilities found in a web "
    "application, from the architecture phase through production."))

body.append(term("Staging Environment",
    "An environment that mimics the production environment as closely as possible, used to reproduce "
    "and verify vulnerabilities without affecting real users."))

body.append(term("Reproducing a Vulnerability",
    "The first step in managing a vulnerability report. Allows you to: verify it is a real vulnerability, "
    "avoid paying bug bounty for false positives, and gain insight for fixing it."))

body.append(term("CVSS (Common Vulnerability Scoring System)",
    "A freely published system for ranking vulnerabilities based on how easy they are to exploit and "
    "what type of data or processes can be compromised. Composed of Base, Temporal, and Environmental metrics."))

body.append(term("CVSS Base Metrics",
    "Represent the intrinsic characteristics of a vulnerability that are constant over time and across "
    "environments. Composed of Exploitability metrics and Impact metrics."))

body.append(term("CVSS Temporal Metrics",
    "Score the severity of a vulnerability over time — accounts for availability of exploits, "
    "patches, and workarounds that may change the effective risk."))

body.append(term("CVSS Environmental Metrics",
    "Score a vulnerability based on the specific environment it exists in — considers "
    "the organization's security controls and the criticality of affected systems."))

body.append(term("Risk Factors for Vulnerability Prioritization",
    "Financial risk to the company, difficulty of exploitation, type of data compromised, "
    "existing contractual agreements, and mitigation measures already in place."))

body.append(tip("CVSS has THREE metric groups: Base (constant), Temporal (changes over time), Environmental (context-specific). Know all three."))
body.append(tip("Always reproduce a vulnerability in a staging environment before triaging — a staging environment mimics production but has no real user data."))
body.append(trap("Not all vulnerabilities need immediate fixes — risk assessment determines priority. Never treat all vulnerabilities with equal urgency."))
body.append(trap("Lack of logging for known vulnerabilities has caused company failures — always add logging for known vulnerabilities while the fix is being developed."))

# ════════════════════════════════════════════════════════════════
# CHAPTER 13 – DEFENDING AGAINST XSS, CSRF & XXE
# ════════════════════════════════════════════════════════════════
body.append(chapter("Chapter 13: Defending Against XSS, CSRF &amp; XXE"))
body.append(section("Key Definitions"))

body.append(term("XSS Root Cause",
    "Cross-site scripting is mainly caused by the failure of a web application to sanitize "
    "user inputs embedded in web pages. Conditions: app accepts user input, input creates dynamic content, "
    "input is insufficiently validated."))

body.append(term("Anti-XSS Golden Rule",
    "'Do not allow any user-supplied data to be passed into the DOM — except as strings.' "
    "Use innerText (not innerHTML) whenever appending string-like objects to the DOM."))

body.append(term("innerText vs innerHTML",
    "innerText: interprets content as plain text — safe for user-supplied data. "
    "innerHTML: interprets content as HTML/JS — dangerous with user-supplied data. "
    "Always prefer innerText unless HTML rendering is explicitly required."))

body.append(term("Input Sanitization",
    "Removing or escaping dangerous content from user input before processing or displaying it. "
    "Must allow some HTML tags (e.g., &lt;strong&gt;) but block dangerous ones (e.g., &lt;script&gt;)."))

body.append(term("DOMParser",
    "A JavaScript interface that parses XML or HTML source code from a string into a DOM Document. "
    "Risk: loading untrusted content via parseFromString can execute malicious scripts."))

body.append(term("CSRF Token",
    "A unique, secret, unpredictable token generated per session and embedded in forms. "
    "The server validates the token on every state-changing request — an attacker cannot forge it."))

body.append(term("SameSite Cookie Attribute",
    "A cookie attribute that prevents the browser from sending the cookie in cross-site requests. "
    "SameSite=Strict or SameSite=Lax significantly reduces CSRF attack surface."))

body.append(term("XXE Defense",
    "Disable external entity processing in the XML parser. "
    "Never allow user-supplied XML to define or reference external entities."))

body.append(term("SQL Injection Defense",
    "Use parameterized queries (prepared statements) exclusively. "
    "Never concatenate user-supplied strings directly into SQL queries."))

body.append(term("Content Security Policy (CSP)",
    "An HTTP response header that tells browsers which sources of content are legitimate. "
    "Prevents XSS by blocking inline scripts and scripts from untrusted origins."))

body.append(tip("innerText is always the safe choice for displaying user content in the DOM. innerHTML should only be used when HTML rendering is absolutely necessary."))
body.append(tip("CSRF tokens + SameSite cookies together provide strong CSRF protection. Use both."))
body.append(trap("Sanitizing HTML by blacklisting specific tags (like &lt;script&gt;) is insufficient — attackers bypass blacklists with encoding tricks. Use a whitelist or a trusted sanitization library."))
body.append(trap("CSP does NOT prevent all XSS — it reduces the impact. Proper input sanitization is still required. Never rely on CSP alone."))
body.append(trap("SQL injection cannot be fixed by input filtering alone — parameterized queries are the only complete defense. Never concatenate user input into SQL."))

# ── BUILD HTML ──────────────────────────────────────────────────
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

with open("websec_summary.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Saved: websec_summary.html")

from weasyprint import HTML as WHTML
WHTML(string=html).write_pdf("websec_summary.pdf")
print("Saved: websec_summary.pdf")
