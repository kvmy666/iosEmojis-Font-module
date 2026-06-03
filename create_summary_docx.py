from docx import Document
from docx.shared import RGBColor, Pt, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from datetime import date

# ── Color constants ──────────────────────────────────────────────
BLUE   = RGBColor(0x00, 0x70, 0xC0)   # term names
RED    = RGBColor(0xC0, 0x00, 0x00)   # key words / exam trap header
GREEN  = RGBColor(0x37, 0x86, 0x10)   # exam tip header
NAVY   = RGBColor(0x1F, 0x39, 0x64)   # chapter headings
TEAL   = RGBColor(0x17, 0x6B, 0x7F)   # section headings
BLACK  = RGBColor(0x00, 0x00, 0x00)
ORANGE = RGBColor(0xC0, 0x55, 0x00)   # extra key words

KEY_RED    = {"always", "never", "must", "cannot", "only", "must not",
              "critical", "important", "warning", "do not", "not"}
KEY_ORANGE = {"note", "required", "ensure", "before", "secure", "essential"}

# ── Helpers ──────────────────────────────────────────────────────

def set_cell_shading(cell, fill_hex):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)


def set_para_shading(para, fill_hex):
    pPr = para._p.get_or_add_pPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    pPr.append(shd)


def colorize_run(run, word):
    """Color individual word if it matches a keyword."""
    token = word.lower().strip(".,;:()")
    if token in KEY_RED:
        run.font.color.rgb = RED
        run.font.bold = True
    elif token in KEY_ORANGE:
        run.font.color.rgb = ORANGE
        run.font.bold = True


def add_chapter_heading(doc, text):
    para = doc.add_paragraph()
    para.paragraph_format.space_before = Pt(6)
    para.paragraph_format.space_after  = Pt(2)
    run = para.add_run(text)
    run.font.size  = Pt(14)
    run.font.bold  = True
    run.font.color.rgb = NAVY
    # bottom border
    pPr = para._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '6')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), '1F3964')
    pBdr.append(bottom)
    pPr.append(pBdr)
    return para


def add_section_heading(doc, text):
    para = doc.add_paragraph()
    para.paragraph_format.space_before = Pt(4)
    para.paragraph_format.space_after  = Pt(1)
    run = para.add_run(text)
    run.font.size  = Pt(11)
    run.font.bold  = True
    run.font.color.rgb = TEAL


def add_term(doc, term, definition):
    """Blue term name + black definition with red/orange keywords."""
    para = doc.add_paragraph()
    para.paragraph_format.space_before = Pt(1)
    para.paragraph_format.space_after  = Pt(1)
    para.paragraph_format.left_indent  = Inches(0.15)

    r = para.add_run(term + ": ")
    r.font.color.rgb = BLUE
    r.font.bold      = True
    r.font.size      = Pt(10)

    words = definition.split()
    for word in words:
        run = para.add_run(word + " ")
        run.font.size = Pt(10)
        colorize_run(run, word)
    return para


def add_code(doc, code_line):
    para = doc.add_paragraph()
    para.paragraph_format.left_indent = Inches(0.3)
    para.paragraph_format.space_before = Pt(1)
    para.paragraph_format.space_after  = Pt(1)
    run = para.add_run(code_line)
    run.font.name = "Courier New"
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0x26, 0x34, 0x3F)
    set_para_shading(para, 'F2F2F2')


def add_exam_tip(doc, text):
    para = doc.add_paragraph()
    para.paragraph_format.left_indent   = Inches(0.15)
    para.paragraph_format.space_before  = Pt(2)
    para.paragraph_format.space_after   = Pt(2)
    set_para_shading(para, 'E2EFDA')
    r = para.add_run("Exam Tip: ")
    r.font.bold = True
    r.font.color.rgb = GREEN
    r.font.size = Pt(9)
    r2 = para.add_run(text)
    r2.font.size = Pt(9)


def add_exam_trap(doc, text):
    para = doc.add_paragraph()
    para.paragraph_format.left_indent   = Inches(0.15)
    para.paragraph_format.space_before  = Pt(2)
    para.paragraph_format.space_after   = Pt(2)
    set_para_shading(para, 'FCE4D6')
    r = para.add_run("Exam Trap: ")
    r.font.bold = True
    r.font.color.rgb = RED
    r.font.size = Pt(9)
    r2 = para.add_run(text)
    r2.font.size = Pt(9)


def add_bullet(doc, text):
    para = doc.add_paragraph(style='List Bullet')
    para.paragraph_format.left_indent  = Inches(0.3)
    para.paragraph_format.space_before = Pt(1)
    para.paragraph_format.space_after  = Pt(1)
    words = text.split()
    for word in words:
        run = para.add_run(word + " ")
        run.font.size = Pt(10)
        colorize_run(run, word)


# ── Document setup ───────────────────────────────────────────────

doc = Document()

# Page margins
for section in doc.sections:
    section.top_margin    = Cm(1.8)
    section.bottom_margin = Cm(1.8)
    section.left_margin   = Cm(2.0)
    section.right_margin  = Cm(2.0)

# Default style
style = doc.styles['Normal']
style.font.name = 'Calibri'
style.font.size = Pt(10)


# ══════════════════════════════════════════════════════════════════
# COVER PAGE
# ══════════════════════════════════════════════════════════════════

doc.add_paragraph()
doc.add_paragraph()

title_para = doc.add_paragraph()
title_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = title_para.add_run("Apache HTTP Server")
r.font.size  = Pt(26)
r.font.bold  = True
r.font.color.rgb = NAVY

sub_para = doc.add_paragraph()
sub_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = sub_para.add_run("Study Summary – Chapters 1–8")
r.font.size  = Pt(16)
r.font.color.rgb = TEAL

doc.add_paragraph()
course_para = doc.add_paragraph()
course_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = course_para.add_run("FWD 213 – Web Administration")
r.font.size = Pt(12)
r.font.bold = True

doc.add_paragraph()
date_para = doc.add_paragraph()
date_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = date_para.add_run(f"Prepared: {date.today().strftime('%B %Y')}")
r.font.size  = Pt(11)
r.font.color.rgb = RGBColor(0x70, 0x70, 0x70)

doc.add_page_break()


# ══════════════════════════════════════════════════════════════════
# CHAPTER 1 – INTRODUCTION TO APACHE HTTP SERVER
# ══════════════════════════════════════════════════════════════════

add_chapter_heading(doc, "Chapter 1: Introduction to Apache HTTP Server")

add_section_heading(doc, "Key Definitions")

add_term(doc, "Apache HTTP Server",
    "An open-source web server for Unix/Linux/Windows; derived from the word 'Patchy', "
    "meaning incomplete – built from patches applied to NCSA httpd.")

add_term(doc, "HTTP (Hypertext Transfer Protocol)",
    "An application-layer protocol built on top of TCP that enables communication between "
    "web browsers and servers via request/response messages.")

add_term(doc, "SSL (Secure Sockets Layer)",
    "A security protocol that encrypts client/server communication; runs on top of TCP/IP "
    "and uses public keys, symmetric keys, and certificates.")

add_term(doc, "ARP (Address Resolution Protocol)",
    "A low-level Layer-2 protocol that converts an IP address into its corresponding "
    "physical (MAC) network address.")

add_term(doc, "DHCP (Dynamic Host Configuration Protocol)",
    "A protocol that automatically assigns a unique IP address to any device joining a "
    "network, then releases it when the device leaves.")

add_term(doc, "FTP (File Transfer Protocol)",
    "A simple network protocol based on IP that allows transfer of files between two "
    "nodes on a network.")

add_term(doc, "MPM (Multi-Processing Module)",
    "Platform-specific modules that define how Apache handles multiple simultaneous "
    "connections on different operating systems.")

add_section_heading(doc, "Key Facts")
add_bullet(doc, "Apache uses TCP port 80 by default for HTTP, and port 443 for HTTPS.")
add_bullet(doc, "Apache powers over 67% of all web servers worldwide.")
add_bullet(doc, "Apache supports CGI, SSL, virtual domains, and plug-in modules for extensibility.")
add_bullet(doc, "HTTP 3 main message types: GET, POST, and HEAD.")

add_section_heading(doc, "Exam Tips & Traps")
add_exam_tip(doc, "HTTP operates at the Application Layer (Layer 7) of the OSI model; "
                  "ARP operates at Layer 2 (Data Link).")
add_exam_tip(doc, "Apache 2.0 introduced hybrid multiprocess/multithreaded mode on Unix "
                  "with POSIX thread support for improved scalability.")
add_exam_trap(doc, "HTTP does NOT inherently provide security — SSL/TLS must be added "
                   "separately; never confuse HTTP with HTTPS.")
add_exam_trap(doc, "ARP resolves IP→MAC (not MAC→IP). Do not confuse ARP with RARP.")

doc.add_page_break()


# ══════════════════════════════════════════════════════════════════
# CHAPTER 2 – INSTALLING APACHE
# ══════════════════════════════════════════════════════════════════

add_chapter_heading(doc, "Chapter 2: Installing Apache on Linux and Windows")

add_section_heading(doc, "Key Definitions")

add_term(doc, "httpd",
    "The Apache HTTP Server daemon process; 'httpd 2.4.56' is the latest stable release.")

add_term(doc, "Static Website",
    "A site built with only HTML/CSS that always delivers the same content to every visitor.")

add_term(doc, "Dynamic Website",
    "A site that generates content at runtime using a database (MySQL/MariaDB) and a "
    "server-side language (PHP, Python, NodeJS).")

add_term(doc, "XAMPP",
    "A pre-built cross-platform installer that bundles Apache, MariaDB, PHP, and Perl "
    "for Windows, macOS, and Linux.")

add_term(doc, "Package Manager Installation",
    "Installing Apache via apt-get (Ubuntu/Debian) or yum/dnf (Fedora/RHEL/CentOS) "
    "for the quickest and easiest setup.")

add_term(doc, "Source Code Installation",
    "Compiling Apache from official source using 'make' then 'make install'; provides "
    "maximum customization but is complex and time-consuming.")

add_section_heading(doc, "Key Commands")
add_code(doc, "sudo apt-get install apache2           # Ubuntu/Debian")
add_code(doc, "sudo systemctl start apache2           # Start service")
add_code(doc, "sudo systemctl stop apache2            # Stop service")
add_code(doc, "sudo systemctl restart apache2         # Restart service")
add_code(doc, "sudo systemctl enable apache2          # Enable at boot")
add_code(doc, "sudo systemctl status apache2          # Check status")
add_code(doc, "docker run -d --name myserver -p 80:80 httpd  # Docker install")

add_section_heading(doc, "Exam Tips & Traps")
add_exam_tip(doc, "On Ubuntu/Debian the service is 'apache2'; on RHEL/CentOS it is 'httpd'. "
                  "Commands differ between distros.")
add_exam_tip(doc, "Apache must be restarted for main configuration file changes to take "
                  "effect; only .htaccess changes apply immediately.")
add_exam_trap(doc, "Source code installation does NOT use 'apt-get' or 'yum' — never "
                   "confuse package manager installation with source compilation.")
add_exam_trap(doc, "XAMPP is not recommended for production environments — it is only "
                   "for development/testing use.")

doc.add_page_break()


# ══════════════════════════════════════════════════════════════════
# CHAPTER 3 – CONFIGURATION FILES
# ══════════════════════════════════════════════════════════════════

add_chapter_heading(doc, "Chapter 3: Configuration Files")

add_section_heading(doc, "Key Definitions")

add_term(doc, "httpd.conf / apache2.conf",
    "The main Apache configuration file; on Ubuntu it is apache2.conf; changes are only "
    "recognized when the server is started or restarted.")

add_term(doc, "Directive",
    "A configuration command consisting of a name followed by space-separated arguments, "
    "placed one per line in a plain text config file.")

add_term(doc, "DSO – Dynamic Shared Object",
    "An external module dynamically loaded into httpd at runtime using the LoadModule "
    "directive; enables modular architecture.")

add_term(doc, ".htaccess File",
    "A per-directory config file that enables decentralized management; changes take "
    "immediate effect because it is read on every request.")

add_term(doc, "AllowOverride",
    "Directive that controls which directives are permitted in .htaccess files; set to "
    "None to completely ignore .htaccess files.")

add_term(doc, "<VirtualHost> Container",
    "A configuration section that applies directives only to requests for a specific "
    "website, enabling multiple sites on one server.")

add_term(doc, "<Location> Container",
    "Applies directives to content in the webspace (URLs); should never be used to "
    "restrict access to filesystem objects.")

add_section_heading(doc, "Container Types")
add_bullet(doc, "<Directory> / <DirectoryMatch> – applies to filesystem directories.")
add_bullet(doc, "<Files> / <FilesMatch> – applies to files by name or regex.")
add_bullet(doc, "<Location> / <LocationMatch> – applies to URL paths (webspace).")
add_bullet(doc, "<IfDefine> / <IfModule> / <IfVersion> – evaluated only at startup.")

add_section_heading(doc, "Key Commands")
add_code(doc, "apachectl configtest       # Test config syntax without restarting")
add_code(doc, "apachectl -l               # List statically compiled modules")
add_code(doc, "apachectl -M               # List all modules (static + dynamic)")
add_code(doc, "LoadModule status_module modules/mod_status.so")
add_code(doc, "Define servername www.example.com")
add_code(doc, "Include conf/vhosts/*.conf")

add_section_heading(doc, "Exam Tips & Traps")
add_exam_tip(doc, "Directives are case-insensitive but their arguments are often "
                  "case-sensitive.")
add_exam_tip(doc, "Use 'apachectl configtest' before restarting to catch syntax errors "
                  "without taking the server down.")
add_exam_trap(doc, "Never use <Location> to restrict access to filesystem objects — it "
                   "can be bypassed via different URL mappings. Always use <Directory> "
                   "or <Files> for filesystem restrictions.")
add_exam_trap(doc, "Comments cannot share a line with a directive. A '#' on the same "
                   "line as a directive does NOT comment it out.")

doc.add_page_break()


# ══════════════════════════════════════════════════════════════════
# CHAPTER 4 – VIRTUAL HOSTS
# ══════════════════════════════════════════════════════════════════

add_chapter_heading(doc, "Chapter 4: Virtual Hosts")

add_section_heading(doc, "Key Definitions")

add_term(doc, "Virtual Host",
    "A configuration that allows multiple websites to run on a single physical server; "
    "each site has its own directory for data storage.")

add_term(doc, "Name-based Virtual Hosting",
    "Multiple websites share the same IP address; the server uses the HTTP Host header "
    "to identify which site to serve.")

add_term(doc, "IP-based Virtual Hosting",
    "Each website has a dedicated IP address; the server selects the virtual host based "
    "on the IP address of the incoming connection.")

add_term(doc, "ServerName Directive",
    "Specifies the hostname and port that the server uses to identify itself within a "
    "VirtualHost block.")

add_term(doc, "ServerAlias Directive",
    "Defines additional hostnames that should be resolved to the same virtual host "
    "(e.g., www.example.com and example.com).")

add_term(doc, "DocumentRoot",
    "The directory from which Apache serves files for a virtual host; must be unique "
    "per virtual host to avoid content mixing.")

add_section_heading(doc, "Example Configuration")
add_code(doc, "<VirtualHost *:80>")
add_code(doc, "    ServerName www.example.com")
add_code(doc, "    ServerAlias example.com")
add_code(doc, "    DocumentRoot /var/www/example")
add_code(doc, "    ErrorLog /var/log/apache2/example_error.log")
add_code(doc, "</VirtualHost>")

add_section_heading(doc, "Exam Tips & Traps")
add_exam_tip(doc, "Name-based virtual hosting is more efficient — it requires only one "
                  "IP address for multiple sites. Always prefer it over IP-based when "
                  "possible.")
add_exam_tip(doc, "The first VirtualHost block in the config acts as the default virtual "
                  "host for unmatched requests on that IP.")
add_exam_trap(doc, "IP-based virtual hosting requires a separate IP for each site — "
                   "do not confuse it with name-based which shares one IP.")
add_exam_trap(doc, "Forgetting ServerAlias means requests to 'example.com' (without www) "
                   "will not match the virtual host.")

doc.add_page_break()


# ══════════════════════════════════════════════════════════════════
# CHAPTER 5 – SSL CONFIGURATION
# ══════════════════════════════════════════════════════════════════

add_chapter_heading(doc, "Chapter 5: SSL Configuration")

add_section_heading(doc, "Key Definitions")

add_term(doc, "SSL/TLS (Secure Sockets Layer / Transport Layer Security)",
    "A protocol layer between TCP/IP and the application layer (HTTP) that provides "
    "encryption, authentication, and data integrity.")

add_term(doc, "Conventional (Symmetric) Cryptography",
    "Both sender and receiver share the same secret key to encrypt and decrypt; fast but "
    "requires secure key exchange.")

add_term(doc, "Public Key (Asymmetric) Cryptography",
    "Uses two mathematically linked keys: a public key (shared with everyone) to encrypt, "
    "and a private key (kept secret) to decrypt.")

add_term(doc, "Message Digest (Hash Function)",
    "A one-way function that creates a fixed-length summary of a message; used to verify "
    "integrity — any change in the message changes the digest.")

add_term(doc, "Digital Signature",
    "Created by encrypting a message digest with the sender's private key; proves "
    "authenticity and integrity of the message.")

add_term(doc, "Certificate Authority (CA)",
    "A trusted third-party agency that verifies identities and issues digital certificates "
    "signed with the CA's private key.")

add_term(doc, "SSL Certificate",
    "A digital document that associates a public key with an identity (server/person); "
    "must be signed by a trusted CA for browsers to accept it.")

add_term(doc, "SSL Handshake",
    "The sequence of steps where client and server exchange certificates, negotiate "
    "cipher suites, and establish a shared session key.")

add_section_heading(doc, "Key Facts")
add_bullet(doc, "SSL uses port 443 by default.")
add_bullet(doc, "Each SSL certificate has a Public Key (shared) and a Private Key (never disclosed).")
add_bullet(doc, "Once an SSL session is established it can be reused via a Session ID to avoid repeating the handshake.")
add_bullet(doc, "Digital signature ≠ electronic signature.")

add_section_heading(doc, "Key Commands")
add_code(doc, "a2enmod ssl                          # Enable mod_ssl on Ubuntu")
add_code(doc, "openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365")
add_code(doc, "SSLEngine on")
add_code(doc, "SSLCertificateFile    /etc/ssl/certs/server.crt")
add_code(doc, "SSLCertificateKeyFile /etc/ssl/private/server.key")

add_section_heading(doc, "Exam Tips & Traps")
add_exam_tip(doc, "SSL port is always 443 for HTTPS; HTTP always uses port 80. "
                  "Memorize both port numbers.")
add_exam_tip(doc, "The Public Key encrypts; the Private Key decrypts. This is the core "
                  "of asymmetric cryptography.")
add_exam_trap(doc, "Never expose or share the Private Key — only the Public Key is "
                   "distributed. Exposing the private key compromises all encrypted "
                   "communications.")
add_exam_trap(doc, "A self-signed certificate provides encryption but NOT CA-verified "
                   "identity — browsers will show a security warning.")

doc.add_page_break()


# ══════════════════════════════════════════════════════════════════
# CHAPTER 6 – FORWARD PROXY SERVER
# ══════════════════════════════════════════════════════════════════

add_chapter_heading(doc, "Chapter 6: Configure Apache as a Forward Proxy Server")

add_section_heading(doc, "Key Definitions")

add_term(doc, "Proxy Server",
    "A server that routes traffic between clients and external systems; it can regulate "
    "traffic, mask client IP addresses, and enforce security policies.")

add_term(doc, "Forward Proxy",
    "An intermediate server between the client and origin server; the client must be "
    "specially configured to send requests through it.")

add_term(doc, "ProxyRequests On",
    "Directive that activates Apache as a forward proxy; must never be enabled without "
    "securing the server to prevent unauthorized open proxy use.")

add_term(doc, "Residential Proxy",
    "A forward proxy with a real IP address provided by an ISP, associated with a "
    "physical location.")

add_term(doc, "Datacenter Proxy",
    "A forward proxy whose IP addresses come from data centers rather than ISPs; "
    "faster but easier to detect and block.")

add_term(doc, "mod_proxy",
    "The Apache module that enables proxy functionality; required for both forward and "
    "reverse proxy configurations.")

add_section_heading(doc, "Key Configuration")
add_code(doc, "LoadModule proxy_module modules/mod_proxy.so")
add_code(doc, "LoadModule proxy_http_module modules/mod_proxy_http.so")
add_code(doc, "LoadModule proxy_connect_module modules/mod_proxy_connect.so")
add_code(doc, "ProxyRequests On")
add_code(doc, "ProxyVia On")
add_code(doc, "<Proxy *>")
add_code(doc, "    Require ip 192.168.1.0/24   # only allow local subnet")
add_code(doc, "</Proxy>")

add_section_heading(doc, "Forward Proxy Use Cases")
add_bullet(doc, "Provide internet access to internal clients restricted by a firewall.")
add_bullet(doc, "Access geo-restricted content by routing through a proxy in another country.")
add_bullet(doc, "Ensure client anonymity by masking the real IP address.")
add_bullet(doc, "Reduce bandwidth usage with mod_cache caching.")

add_section_heading(doc, "Exam Tips & Traps")
add_exam_tip(doc, "For HTTPS forward proxying, mod_proxy_connect must also be enabled "
                  "in addition to mod_proxy and mod_proxy_http.")
add_exam_tip(doc, "ProxyRequests On enables a forward proxy; in a reverse proxy setup "
                  "this should always be set to Off.")
add_exam_trap(doc, "Never enable ProxyRequests On without access restrictions — it "
                   "creates an open proxy that anyone on the internet can abuse.")
add_exam_trap(doc, "Forward proxy hides the CLIENT's identity; reverse proxy hides the "
                   "SERVER's identity. Do not confuse the two.")

doc.add_page_break()


# ══════════════════════════════════════════════════════════════════
# CHAPTER 7 – REVERSE PROXY SERVER
# ══════════════════════════════════════════════════════════════════

add_chapter_heading(doc, "Chapter 7: Configure Apache as a Reverse Proxy Server")

add_section_heading(doc, "Key Definitions")

add_term(doc, "Reverse Proxy (Gateway)",
    "A server that sits in front of backend servers; it appears to clients as a normal "
    "web server while forwarding requests to internal servers.")

add_term(doc, "ProxyPass",
    "Directive that maps a local URL path to a remote backend server URL, activating "
    "the reverse proxy.")

add_term(doc, "ProxyPassReverse",
    "Directive that adjusts HTTP redirect headers from the backend server so they "
    "point to the proxy URL, not the internal server URL.")

add_term(doc, "Load Balancing",
    "Distributing incoming requests across multiple backend servers to improve "
    "performance and prevent any single server from being overloaded.")

add_term(doc, "mod_proxy_balancer",
    "Apache module that enables load balancing across a cluster of backend servers "
    "using various balancing algorithms.")

add_section_heading(doc, "Key Configuration")
add_code(doc, "ProxyRequests Off                     # must be Off for reverse proxy")
add_code(doc, "ProxyPass        /app http://backend.internal:8080/app")
add_code(doc, "ProxyPassReverse /app http://backend.internal:8080/app")
add_code(doc, "# Load balancer example:")
add_code(doc, "<Proxy balancer://mycluster>")
add_code(doc, "    BalancerMember http://server1:8080")
add_code(doc, "    BalancerMember http://server2:8080")
add_code(doc, "</Proxy>")
add_code(doc, "ProxyPass / balancer://mycluster/")

add_section_heading(doc, "Reverse Proxy Use Cases")
add_bullet(doc, "Provide internet users access to servers behind a firewall.")
add_bullet(doc, "Load balancing across multiple backend servers.")
add_bullet(doc, "Caching responses from slow backend servers.")
add_bullet(doc, "SSL termination — handle SSL at the proxy, plain HTTP to backends.")
add_bullet(doc, "Protection against DDoS attacks by shielding origin servers.")

add_section_heading(doc, "Exam Tips & Traps")
add_exam_tip(doc, "Always use ProxyPassReverse alongside ProxyPass — without it, "
                  "redirects from the backend will expose internal server addresses.")
add_exam_tip(doc, "Reverse proxy hides the SERVER; forward proxy hides the CLIENT. "
                  "Remember: reverse = server anonymity.")
add_exam_trap(doc, "ProxyRequests must be Off in a reverse proxy setup — setting it "
                   "On accidentally turns the server into an open forward proxy.")
add_exam_trap(doc, "Do not confuse the [P] RewriteRule flag with ProxyPass — both can "
                   "create a reverse proxy but are used in different contexts.")

doc.add_page_break()


# ══════════════════════════════════════════════════════════════════
# CHAPTER 8 – DISPLAY SERVER STATISTICS
# ══════════════════════════════════════════════════════════════════

add_chapter_heading(doc, "Chapter 8: Display Server Statistics")

add_section_heading(doc, "Key Definitions")

add_term(doc, "mod_status",
    "An Apache base module that provides an HTML page with real-time server activity "
    "and performance statistics accessible via a web browser.")

add_term(doc, "server-status Page",
    "A URL endpoint (e.g., http://localhost/server-status) that displays live server "
    "metrics; access must be restricted to trusted IPs.")

add_term(doc, "ExtendedStatus On",
    "Directive that enables detailed per-request statistics including CPU usage, "
    "requests/second, and bytes/second in the status report.")

add_term(doc, "mod_info (server-info)",
    "An Apache module that provides a comprehensive overview of the server's "
    "configuration including all loaded modules and directives.")

add_term(doc, "Worker / Idle Worker",
    "A worker is an Apache process/thread handling a request; idle workers are "
    "waiting for requests; the ratio indicates server load.")

add_section_heading(doc, "Statistics Provided by mod_status")
add_bullet(doc, "Total number of incoming requests and bytes transferred.")
add_bullet(doc, "Server uptime and restart time.")
add_bullet(doc, "CPU usage and server load average.")
add_bullet(doc, "Requests per second, bytes per second.")
add_bullet(doc, "Total number of idle and busy workers.")
add_bullet(doc, "PIDs with respective client information.")

add_section_heading(doc, "Key Configuration")
add_code(doc, "LoadModule status_module modules/mod_status.so")
add_code(doc, "<Location /server-status>")
add_code(doc, "    SetHandler server-status")
add_code(doc, "    Require ip 127.0.0.1 ::1   # localhost only")
add_code(doc, "</Location>")
add_code(doc, "ExtendedStatus On")
add_code(doc, "# Access via browser: http://localhost/server-status")
add_code(doc, "# Access via CLI:     apache2ctl status")

add_section_heading(doc, "Exam Tips & Traps")
add_exam_tip(doc, "mod_status is a 'Base' module — it is included with Apache by default "
                  "but must be enabled and configured with a <Location> block.")
add_exam_tip(doc, "Add '?refresh=5' to the URL (server-status?refresh=5) to make the "
                  "page auto-refresh every 5 seconds for live monitoring.")
add_exam_trap(doc, "Never expose /server-status to the public internet — it reveals "
                   "sensitive server information. Always restrict access with 'Require ip'.")
add_exam_trap(doc, "mod_status and mod_info are different: mod_status shows live "
                   "performance data; mod_info shows configuration details.")


# ── Save ─────────────────────────────────────────────────────────

out_path = "apache_summary.docx"
doc.save(out_path)
print(f"Saved: {out_path}")
