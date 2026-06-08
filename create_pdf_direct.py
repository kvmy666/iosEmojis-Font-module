"""Generate apache_summary.pdf directly via HTML + WeasyPrint."""

from _keywords import KEYWORDS_RED, KEYWORDS_ORANGE
from datetime import date
import re

def colorize(text):
    """Wrap key words in colored spans."""
    parts = re.split(r'(\s+)', text)
    out = []
    for part in parts:
        token = part.lower().strip(".,;:()")
        if token in KEYWORDS_RED:
            out.append(f'<span class="kw-red">{part}</span>')
        elif token in KEYWORDS_ORANGE:
            out.append(f'<span class="kw-orange">{part}</span>')
        else:
            out.append(part)
    return "".join(out)


def term(name, definition):
    return (f'<p class="term">'
            f'<span class="term-name">{name}:</span> '
            f'{colorize(definition)}'
            f'</p>')


def code(line):
    return f'<pre class="code">{line}</pre>'


def tip(text):
    return f'<div class="tip"><strong>Exam Tip:</strong> {colorize(text)}</div>'


def trap(text):
    return f'<div class="trap"><strong>Exam Trap:</strong> {colorize(text)}</div>'


def bullet(text):
    return f'<li>{colorize(text)}</li>'


def section(title):
    return f'<h3>{title}</h3>'


def chapter(title):
    return f'<h2>{title}</h2>'


# ── CSS ──────────────────────────────────────────────────────────
CSS = """
@page {
    size: A4;
    margin: 18mm 20mm 18mm 20mm;
    @bottom-right {
        content: counter(page);
        font-size: 9pt;
        color: #888;
    }
}
.cover {
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    height: 240mm;
    background: linear-gradient(160deg, #EBF3FB 0%, #F8FBFF 100%);
    border: 2px solid #1F3964;
    border-radius: 8pt;
    padding: 40pt;
    box-sizing: border-box;
}
body {
    font-family: Calibri, Arial, sans-serif;
    font-size: 10pt;
    color: #222;
    line-height: 1.5;
}
h1 {
    text-align: center;
    color: #1F3964;
    font-size: 28pt;
    margin-bottom: 6pt;
    letter-spacing: 1pt;
}
.subtitle {
    text-align: center;
    color: #17738F;
    font-size: 14pt;
    margin-bottom: 6pt;
}
.course {
    text-align: center;
    font-size: 11pt;
    font-weight: bold;
    margin-bottom: 4pt;
}
.date-line {
    text-align: center;
    color: #888;
    font-size: 10pt;
}
h2 {
    color: #1F3964;
    font-size: 13pt;
    border-bottom: 2px solid #1F3964;
    padding-bottom: 3pt;
    margin-top: 0;
    margin-bottom: 6pt;
    page-break-before: always;
}
h3 {
    color: #17738F;
    font-size: 10.5pt;
    margin-top: 10pt;
    margin-bottom: 3pt;
}
p.term {
    margin: 3pt 0 3pt 12pt;
    font-size: 10pt;
}
span.term-name {
    color: #0070C0;
    font-weight: bold;
}
span.kw-red    { color: #C00000; font-weight: bold; }
span.kw-orange { color: #C05500; font-weight: bold; }
pre.code {
    font-family: 'Courier New', monospace;
    font-size: 8.5pt;
    background: #F2F2F2;
    color: #26343F;
    margin: 2pt 0 2pt 20pt;
    padding: 3pt 6pt;
    border-radius: 3pt;
    white-space: pre-wrap;
    word-break: break-all;
}
ul { margin: 2pt 0 2pt 28pt; padding: 0; }
li { margin: 1pt 0; font-size: 10pt; }
.tip {
    background: #E2EFDA;
    border-left: 3pt solid #378610;
    padding: 4pt 8pt;
    margin: 3pt 0 3pt 10pt;
    font-size: 9pt;
}
.tip strong { color: #378610; }
.trap {
    background: #FCE4D6;
    border-left: 3pt solid #C00000;
    padding: 4pt 8pt;
    margin: 3pt 0 3pt 10pt;
    font-size: 9pt;
}
.trap strong { color: #C00000; }
"""

# ── CONTENT ──────────────────────────────────────────────────────

sections_html = []

# ── Chapter 1 ───────────────────────────────────────────────────
sections_html.append(chapter("Chapter 1: Introduction to Apache HTTP Server"))
sections_html.append(section("Key Definitions"))
sections_html.append(term("Apache HTTP Server",
    "An open-source web server for Unix/Linux/Windows; derived from 'Patchy', "
    "meaning incomplete — built from patches applied to NCSA httpd."))
sections_html.append(term("HTTP (Hypertext Transfer Protocol)",
    "An application-layer protocol built on top of TCP enabling browser-server "
    "communication via GET, POST, and HEAD request/response messages."))
sections_html.append(term("SSL (Secure Sockets Layer)",
    "A security protocol that encrypts client/server communication; runs on top of TCP/IP "
    "using public keys, symmetric keys, and certificates."))
sections_html.append(term("ARP (Address Resolution Protocol)",
    "A low-level Layer-2 protocol that converts an IP address into its corresponding "
    "physical (MAC) network address."))
sections_html.append(term("DHCP (Dynamic Host Configuration Protocol)",
    "A protocol that automatically assigns a unique IP address to any device joining "
    "a network, then releases it when the device leaves."))
sections_html.append(term("FTP (File Transfer Protocol)",
    "A simple IP-based protocol that allows file transfer between two nodes on a network."))
sections_html.append(term("MPM (Multi-Processing Module)",
    "Platform-specific Apache modules that define how multiple simultaneous connections "
    "are handled on different operating systems."))

sections_html.append(section("Key Facts"))
sections_html.append("<ul>")
sections_html.append(bullet("HTTP uses TCP port 80 by default; HTTPS (SSL) always uses port 443."))
sections_html.append(bullet("Apache powers over 67% of all web servers worldwide."))
sections_html.append(bullet("HTTP message types: GET, POST, and HEAD."))
sections_html.append(bullet("Apache 2.0 added hybrid multiprocess/multithreaded mode on Unix for improved scalability."))
sections_html.append("</ul>")

sections_html.append(section("Exam Tips & Traps"))
sections_html.append(tip("HTTP = Application Layer (OSI Layer 7); ARP = Data Link Layer (OSI Layer 2). Know these layers."))
sections_html.append(tip("Apache 2.0 introduced PCRE (Perl-Compatible Regular Expressions) for more powerful pattern matching."))
sections_html.append(trap("HTTP does NOT provide security — SSL/TLS must be added separately. Never confuse HTTP with HTTPS."))
sections_html.append(trap("ARP resolves IP→MAC (not MAC→IP). RARP does the reverse. Do not confuse them."))

# ── Chapter 2 ───────────────────────────────────────────────────
sections_html.append(chapter("Chapter 2: Installing Apache on Linux and Windows"))
sections_html.append(section("Key Definitions"))
sections_html.append(term("httpd",
    "The Apache HTTP Server daemon; version 2.4.56 (released 2023-03-07) is the latest stable release."))
sections_html.append(term("Static Website",
    "A site built with only HTML/CSS that always delivers the same content to every visitor."))
sections_html.append(term("Dynamic Website",
    "A site that generates content at runtime using a database and a server-side language (PHP, Python, NodeJS)."))
sections_html.append(term("XAMPP",
    "A pre-built installer bundling Apache, MariaDB, PHP, and Perl for Windows, macOS, and Linux; not for production."))
sections_html.append(term("Source Code Installation",
    "Compiling Apache from official source using 'make' then 'make install'; maximum customization but complex."))
sections_html.append(term("Package Manager Installation",
    "Installing Apache via apt-get (Ubuntu/Debian) or yum/dnf (Fedora/RHEL) — quickest and easiest method."))

sections_html.append(section("Key Commands"))
sections_html.append(code("sudo apt-get install apache2         # Ubuntu/Debian"))
sections_html.append(code("sudo systemctl start|stop|restart apache2"))
sections_html.append(code("sudo systemctl enable apache2        # Enable at boot"))
sections_html.append(code("sudo systemctl status apache2        # Check status"))
sections_html.append(code('docker run -d --name myserver -p 80:80 httpd  # Docker'))

sections_html.append(section("Exam Tips & Traps"))
sections_html.append(tip("On Ubuntu/Debian the service is 'apache2'; on RHEL/CentOS it is 'httpd'. Commands differ between distros."))
sections_html.append(tip("Apache must be restarted for main configuration file changes; only .htaccess changes apply immediately."))
sections_html.append(trap("Source code installation does NOT use apt-get or yum — never confuse it with package manager installation."))
sections_html.append(trap("XAMPP is only for development/testing — never deploy it in a production environment."))

# ── Chapter 3 ───────────────────────────────────────────────────
sections_html.append(chapter("Chapter 3: Configuration Files"))
sections_html.append(section("Key Definitions"))
sections_html.append(term("httpd.conf / apache2.conf",
    "The main Apache configuration file; changes are only recognized when the server is started or restarted."))
sections_html.append(term("Directive",
    "A configuration command (name + space-separated arguments) placed one per line in a plain text config file."))
sections_html.append(term("DSO – Dynamic Shared Object",
    "An external module dynamically loaded into httpd at runtime using the LoadModule directive."))
sections_html.append(term(".htaccess File",
    "A per-directory config file for decentralized management; changes take immediate effect as it is read on every request."))
sections_html.append(term("AllowOverride",
    "Directive that controls which directives are permitted in .htaccess files; set to None to completely ignore .htaccess files."))
sections_html.append(term("<Location> Container",
    "Applies directives to URL paths (webspace); should never be used to restrict access to filesystem objects."))
sections_html.append(term("<Directory> Container",
    "Applies directives to filesystem directories and all subdirectories; the correct way to restrict filesystem access."))

sections_html.append(section("Container Summary"))
sections_html.append("<ul>")
sections_html.append(bullet("<Directory> / <DirectoryMatch> — filesystem directories (and regex variant)."))
sections_html.append(bullet("<Files> / <FilesMatch> — files by name or regex pattern."))
sections_html.append(bullet("<Location> / <LocationMatch> — URL paths in webspace."))
sections_html.append(bullet("<IfDefine> / <IfModule> / <IfVersion> — conditional; evaluated only at startup."))
sections_html.append("</ul>")

sections_html.append(section("Key Commands"))
sections_html.append(code("apachectl configtest              # Test config syntax without restarting"))
sections_html.append(code("apachectl -l                      # List statically compiled modules"))
sections_html.append(code("apachectl -M                      # List all modules (static + dynamic)"))
sections_html.append(code("LoadModule status_module modules/mod_status.so"))
sections_html.append(code("Define servername www.example.com"))

sections_html.append(section("Exam Tips & Traps"))
sections_html.append(tip("Directives are case-insensitive, but their arguments are often case-sensitive."))
sections_html.append(tip("Use 'apachectl configtest' before restarting to catch syntax errors without downtime."))
sections_html.append(trap("Never use <Location> to restrict access to filesystem objects — different URL paths can map to the same file, bypassing the restriction."))
sections_html.append(trap("Comments cannot share a line with a directive. A '#' on the same line as a directive does NOT comment it out."))

# ── Chapter 4 ───────────────────────────────────────────────────
sections_html.append(chapter("Chapter 4: Virtual Hosts"))
sections_html.append(section("Key Definitions"))
sections_html.append(term("Virtual Host",
    "Configuration that allows multiple websites to run on a single physical server, each with its own directory."))
sections_html.append(term("Name-based Virtual Hosting",
    "Multiple websites share the same IP address; the server uses the HTTP Host header to identify the site."))
sections_html.append(term("IP-based Virtual Hosting",
    "Each website has a dedicated IP address; the server selects the virtual host based on the connection IP."))
sections_html.append(term("ServerName",
    "Directive specifying the hostname (and port) used to identify the server within a VirtualHost block."))
sections_html.append(term("ServerAlias",
    "Defines additional hostnames resolved to the same virtual host (e.g., www.example.com and example.com)."))
sections_html.append(term("DocumentRoot",
    "The filesystem directory from which Apache serves files for a virtual host; must be unique per site."))

sections_html.append(section("Example VirtualHost Configuration"))
sections_html.append(code("<VirtualHost *:80>"))
sections_html.append(code("    ServerName www.example.com"))
sections_html.append(code("    ServerAlias example.com"))
sections_html.append(code("    DocumentRoot /var/www/example"))
sections_html.append(code("    ErrorLog /var/log/apache2/example_error.log"))
sections_html.append(code("</VirtualHost>"))

sections_html.append(section("Exam Tips & Traps"))
sections_html.append(tip("Name-based virtual hosting is more efficient — one IP can host many sites. Always prefer it over IP-based."))
sections_html.append(tip("The first VirtualHost block in the config file acts as the default for unmatched requests on that IP."))
sections_html.append(trap("IP-based hosting requires a separate IP per site — do not confuse it with name-based which shares one IP."))
sections_html.append(trap("Forgetting ServerAlias means requests to 'example.com' (without www) will not match the virtual host."))

# ── Chapter 5 ───────────────────────────────────────────────────
sections_html.append(chapter("Chapter 5: SSL Configuration"))
sections_html.append(section("Key Definitions"))
sections_html.append(term("SSL/TLS",
    "Protocol layer between TCP/IP and HTTP that provides mutual authentication, digital-signature integrity, "
    "and encryption for privacy; uses port 443."))
sections_html.append(term("Symmetric (Conventional) Cryptography",
    "Both sender and receiver share the same secret key for encryption and decryption; fast but requires secure key exchange."))
sections_html.append(term("Asymmetric (Public Key) Cryptography",
    "Uses two keys: Public Key (shared with everyone) to encrypt; Private Key (kept secret) to decrypt."))
sections_html.append(term("Message Digest (Hash Function)",
    "A one-way function producing a fixed-length summary; any change in the message changes the digest, ensuring integrity."))
sections_html.append(term("Digital Signature",
    "Created by encrypting a message digest with the sender's private key; proves authenticity and integrity."))
sections_html.append(term("Certificate Authority (CA)",
    "A trusted third-party that verifies identities and signs digital certificates with its private key."))
sections_html.append(term("SSL Handshake",
    "The sequence where client and server exchange certificates, negotiate cipher suites, and establish a session key."))

sections_html.append(section("Key Commands"))
sections_html.append(code("a2enmod ssl                        # Enable mod_ssl (Ubuntu)"))
sections_html.append(code("openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365"))
sections_html.append(code("SSLEngine on"))
sections_html.append(code("SSLCertificateFile    /etc/ssl/certs/server.crt"))
sections_html.append(code("SSLCertificateKeyFile /etc/ssl/private/server.key"))

sections_html.append(section("Exam Tips & Traps"))
sections_html.append(tip("SSL always uses port 443; HTTP always uses port 80. Know both port numbers."))
sections_html.append(tip("Public Key encrypts data; Private Key decrypts it. Once a session is established it can be reused via a Session ID."))
sections_html.append(trap("Never expose or share the Private Key — only the Public Key is distributed. Exposing it compromises all encrypted communications."))
sections_html.append(trap("A self-signed certificate provides encryption but NOT CA-verified identity — browsers will always show a security warning."))

# ── Chapter 6 ───────────────────────────────────────────────────
sections_html.append(chapter("Chapter 6: Configure Apache as a Forward Proxy Server"))
sections_html.append(section("Key Definitions"))
sections_html.append(term("Proxy Server",
    "A server that routes traffic between clients and external systems; it can mask client IPs and enforce security."))
sections_html.append(term("Forward Proxy",
    "Sits between the client and origin server; the client must be specially configured to send requests through it."))
sections_html.append(term("ProxyRequests On",
    "Directive that activates Apache as a forward proxy; must never be enabled without securing the server to prevent open-proxy abuse."))
sections_html.append(term("mod_proxy",
    "The Apache module required for both forward and reverse proxy configurations."))
sections_html.append(term("Residential Proxy",
    "A forward proxy with a real ISP-assigned IP address associated with a physical location."))
sections_html.append(term("Datacenter Proxy",
    "A forward proxy whose IP addresses come from data centers (not ISPs); faster but easier to detect."))

sections_html.append(section("Key Configuration"))
sections_html.append(code("LoadModule proxy_module modules/mod_proxy.so"))
sections_html.append(code("LoadModule proxy_http_module modules/mod_proxy_http.so"))
sections_html.append(code("LoadModule proxy_connect_module modules/mod_proxy_connect.so"))
sections_html.append(code("ProxyRequests On"))
sections_html.append(code("ProxyVia On"))
sections_html.append(code('<Proxy *>\n    Require ip 192.168.1.0/24   # only allow local subnet\n</Proxy>'))

sections_html.append(section("Exam Tips & Traps"))
sections_html.append(tip("For HTTPS forward proxying, mod_proxy_connect must also be enabled in addition to mod_proxy and mod_proxy_http."))
sections_html.append(tip("ProxyRequests On = forward proxy. In a reverse proxy setup this must always be set to Off."))
sections_html.append(trap("Never enable ProxyRequests On without access restrictions — it creates an open proxy that anyone can abuse."))
sections_html.append(trap("Forward proxy hides the CLIENT's identity. Reverse proxy hides the SERVER's identity. Do not confuse the two."))

# ── Chapter 7 ───────────────────────────────────────────────────
sections_html.append(chapter("Chapter 7: Configure Apache as a Reverse Proxy Server"))
sections_html.append(section("Key Definitions"))
sections_html.append(term("Reverse Proxy (Gateway)",
    "Sits in front of backend servers; appears to clients as a normal web server while forwarding requests internally."))
sections_html.append(term("ProxyPass",
    "Directive mapping a local URL path to a remote backend server URL, activating the reverse proxy."))
sections_html.append(term("ProxyPassReverse",
    "Adjusts HTTP redirect headers from the backend so they point to the proxy URL, not the internal server."))
sections_html.append(term("Load Balancing",
    "Distributing incoming requests across multiple backend servers to improve performance and prevent overloading."))
sections_html.append(term("mod_proxy_balancer",
    "Apache module that enables load balancing across a cluster of backend servers using configurable algorithms."))

sections_html.append(section("Key Configuration"))
sections_html.append(code("ProxyRequests Off   # must be Off for reverse proxy"))
sections_html.append(code("ProxyPass        /app  http://backend:8080/app"))
sections_html.append(code("ProxyPassReverse /app  http://backend:8080/app"))
sections_html.append(code("# Load balancer:\n<Proxy balancer://mycluster>\n    BalancerMember http://server1:8080\n    BalancerMember http://server2:8080\n</Proxy>\nProxyPass / balancer://mycluster/"))

sections_html.append(section("Reverse Proxy Use Cases"))
sections_html.append("<ul>")
sections_html.append(bullet("Provide internet access to servers behind a firewall."))
sections_html.append(bullet("Load balancing across multiple backend servers."))
sections_html.append(bullet("SSL termination — handle SSL at the proxy, plain HTTP to backends."))
sections_html.append(bullet("DDoS protection by shielding origin servers."))
sections_html.append("</ul>")

sections_html.append(section("Exam Tips & Traps"))
sections_html.append(tip("Always use ProxyPassReverse alongside ProxyPass — without it, redirects from the backend expose internal addresses."))
sections_html.append(tip("Reverse proxy hides the SERVER; forward proxy hides the CLIENT."))
sections_html.append(trap("ProxyRequests must be Off in a reverse proxy setup — setting it On accidentally creates an open forward proxy."))
sections_html.append(trap("Do not confuse the [P] RewriteRule flag with ProxyPass — both can create a reverse proxy but are used in different contexts."))

# ── Chapter 8 ───────────────────────────────────────────────────
sections_html.append(chapter("Chapter 8: Display Server Statistics"))
sections_html.append(section("Key Definitions"))
sections_html.append(term("mod_status",
    "An Apache Base module providing a real-time HTML page with server activity and performance statistics."))
sections_html.append(term("server-status Page",
    "URL endpoint (e.g., /server-status) showing live server metrics; access must be restricted to trusted IPs."))
sections_html.append(term("ExtendedStatus On",
    "Directive enabling detailed per-request statistics including CPU usage, requests/second, and bytes/second."))
sections_html.append(term("mod_info (server-info)",
    "Apache module providing a comprehensive overview of server configuration, loaded modules, and all directives."))
sections_html.append(term("Worker / Idle Worker",
    "A worker is a process/thread handling a request; idle workers are waiting. The ratio indicates server load."))

sections_html.append(section("Statistics Provided by mod_status"))
sections_html.append("<ul>")
sections_html.append(bullet("Total requests, bytes transferred, server uptime, and restart time."))
sections_html.append(bullet("CPU usage and server load average."))
sections_html.append(bullet("Requests per second and bytes per second."))
sections_html.append(bullet("Total idle and busy workers with PID and client info."))
sections_html.append("</ul>")

sections_html.append(section("Key Configuration"))
sections_html.append(code("LoadModule status_module modules/mod_status.so"))
sections_html.append(code("<Location /server-status>\n    SetHandler server-status\n    Require ip 127.0.0.1 ::1\n</Location>"))
sections_html.append(code("ExtendedStatus On"))
sections_html.append(code("# Browser: http://localhost/server-status"))
sections_html.append(code("# Auto-refresh: http://localhost/server-status?refresh=5"))
sections_html.append(code("# CLI:     apache2ctl status"))

sections_html.append(section("Exam Tips & Traps"))
sections_html.append(tip("mod_status is a Base module — included with Apache by default but must be enabled with a <Location> block."))
sections_html.append(tip("Add '?refresh=N' to the URL for live auto-refreshing monitoring (e.g., ?refresh=5)."))
sections_html.append(trap("Never expose /server-status to the public internet — it reveals sensitive server info. Always restrict with 'Require ip'."))
sections_html.append(trap("mod_status ≠ mod_info: mod_status shows live performance data; mod_info shows static configuration details."))


# ── BUILD HTML ───────────────────────────────────────────────────

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>{CSS}</style>
</head>
<body>
<div class="cover">
  <h1>Apache HTTP Server</h1>
  <p class="subtitle">Study Summary &ndash; Chapters 1&ndash;8</p>
  <br>
  <p class="course">FWD 213 &ndash; Web Administration</p>
  <br><br>
  <p style="color:#1F3964;font-size:11pt;">
    Ch1: Introduction &bull; Ch2: Installation &bull; Ch3: Configuration Files<br>
    Ch4: Virtual Hosts &bull; Ch5: SSL &bull; Ch6: Forward Proxy<br>
    Ch7: Reverse Proxy &bull; Ch8: Server Statistics
  </p>
  <br><br>
  <p class="date-line">Prepared: {date.today().strftime('%B %Y')}</p>
</div>
{''.join(sections_html)}
</body>
</html>"""

# Save HTML (useful for debugging)
with open("apache_summary.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Saved: apache_summary.html")

# Convert HTML → PDF with WeasyPrint
from weasyprint import HTML, CSS as WCSS
HTML(string=html).write_pdf("apache_summary.pdf")
print("Saved: apache_summary.pdf")
