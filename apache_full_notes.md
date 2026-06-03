
# Chapter 1: Introduction to Apache HTTP Server

Web Administration – FWD 213

---

This course covers the topics of web
▪
server administration. Topics include
introduction to apache http server,
install apache on linux and windows,
configuration files, virtual host, configure
ssl, configure apache as a forward
proxy, configure apache as a reverse
proxy, and display server statistics.
2

---

The main objective of this course is to
▪
give students a comprehensive
overview of the tools and techniques
needed to successfully administer web
servers.
3

---

# Assessment Task Week Due Percentage of
Total
1 Quizzes/ Individual Homework/ During 20
Projects semester
2 First exam Week 5 20
3 Second exam Week 10 20
4 Final exam Week 13 40
Learning Resources
Textbooks Antun Peicevic. Apache HTTP Server introduction: Learn
how to configure Apache Web Server in an easy and fun
way. CreateSpace Independent Publishing Platform. 2nd ed.
2017..
4

---

▪ The name Apache is derived from the
word “Patchy”, which means the
incomplete
▪ It is an open source web server used
for Unix, Linux and Solaris platforms
▪ The most popular web server on the
net
▪ Very secure, fast, and reliable

---

Unix Threading On Unix systems with POSIX threads support,
▪
Apache can now run in a hybrid multiprocess, multithreaded mode.
This improves scalability for many, but not all configurations.
New Build System The build system has been rewritten from
▪
scratch to be based on autoconf and libtool. This makes
Apache’s configuration system more similar to that of other
packages.
Multiprotocol Support Apache now has some of the infrastructure
▪
in place to support serving multiple protocols.
▪ MOD ECHO has been written as an example.

---

▪ Better support for non-Unix platforms Apache 2.0 is faster and more stable on non-Unix
platforms such as BeOS, OS/2, and Windows. With the introduction of platform-specific multi-
processing modules (p. 73) (MPMs) and the Apache Portable Runtime (APR), these platforms
are now implemented in their native API, avoiding the often buggy and poorly performing
POSIX-emulation layers.
▪ New Apache API The API for modules has changed significantly for 2.0. Many of the module-
ordering/-priority problems from 1.3 should be gone. 2.0 does much of this automatically, and
module ordering is now done per-hook to allow more flexibility. Also, new calls have been
added that provide additional module capabilities without patching the core Apache server.
▪ IPv6 Support On systems where IPv6 is supported by the underlying Apache Portable
Runtime library, Apache gets IPv6 listening sockets by default. Additionally, the LISTEN,
NAMEVIRTUALHOST, and VIRTUALHOST directives support IPv6 numeric address strings
(e.g., "Listen [2001:db8::1]:8080").

---

▪ Filtering Apache modules may now be written as filters which act on the stream of
content as it is delivered to or from the server. This allows, for example, the output of
CGI scripts to be parsed for Server Side Include directives using the INCLUDES
filter in MOD INCLUDE. The module MOD EXT FILTER allows external programs
to act as filters in much the same way that CGI programs can act as handlers.
▪ Multilanguage Error Responses Error response messages to the browser are now
provided in several languages, using SSI documents. They may be customized by the
administrator to achieve a consistent look and feel.
▪ Simplified configuration Many confusing directives have been simplified. The often
confusing Port and BindAddress directives are gone; only the LISTEN
directive is used for IP address binding; the SERVERNAME directive specifies the
server name and port number only for redirection and vhost recognition.

---

▪ Native Windows NT Unicode Support Apache 2.0 on Windows NT now uses
utf-8 for all filename encodings. These directly translate to the underlying
Unicode file system, providing multilanguage support for allWindows NT-
based installations, including Windows 2000 and Windows XP. This support
does not extend to Windows 95, 98 or ME, which continue to use the machine’s
local codepage for filesystem access.
▪ Regular Expression Library Updated Apache 2.0 includes the Perl
Compatible Regular Expression Library6 (PCRE). All regular expression
evaluation now uses the more powerful Perl 5 syntax.

---

▪ Provides a full range of Web server
features including CGL, SSL , and
virtual domains.
▪ It supports plug-in modules for
extensibility

---

▪ The Web server has:
▪ HTTP
▪ IIS
▪ SSL
▪ Apache Web server has been ported to windows and other Network Operating
Systems (NOS)
▪ Apache HTTP Server is a Web server software that played an important role in the
initial growth of World Wide Web (WWW)

---

Apache HTTP web servers are used by over
67% of all web servers in the world. Apache
web servers are easy to customize
environments, they’re fast, reliable, and
highly secure. This makes Apache web
servers a common choice by best-in-class
companies.

---

▪ HTTP is a Hypertext Transfer Protocol that provides a standard
for Web browsers and servers in order to communicate
▪ HTTP is a technical specification of a network protocol that
software must implement
▪ HTTP is an application layer protocol that is built on top of TCP
▪ HTTP clients (web browsers) and servers communicate via
HTTP request and response messages
▪ The three main HTTP message types are: GET, POST, and
HEAD
▪ HTTP utilizes TCP port 80 by default, despite it can use other
ports
▪ HTTP also includes: ARP (Address Resolution Protocol), DHCP
(Dynamic Host Configuration Protocol, and FTP (File Transfer
Protocol)

---

▪ ARP converts an Internet Protocol (IP) address into its corresponding
physical network address
▪ ARP is a low level network protocol that operate at layer 2 of the OSI
model
▪ ARP is implemented in the device drivers of network operating systems
▪ Mostly used on Ethernet networks, ATMs, Token Rings, and other
physical networks

---

DHCP allows a computer to join a network by giving the IP
▪
address automatically when joining the network with having
to configure the device
DHCP is the protocol that assigns a unique IP address to any
▪
device, and then release these addresses to be used later
when a device re-join the network

---

FTP allows the user to transfer files between two
▪
nodes (computers) on the internet (network)
It is simple network protocol based on the Internet
▪
Protocol (IP)

---

▪ SSL is security technology that help in improving the
safety of communications over the internet
▪ It is standard for encrypting client/server communication
between network devices
▪ SSL runs on top of TCP/IP
▪ It utilizes several standard networks security techniques
including public keys, symmetric keys, and certificates
▪ It is used by the Web sites to guard private information
such credit cards numbers, passwords, …etc.

---


---


# Chapter 2: Installing Apache on Linux and Windows

Chapter 2:
Installing Apache on Linux and Windows
FWD 213 - Web Administration
Slides are based on Apache HTTP Server Documentation Version 2.4

---

Apache HTTP Server Project
▪ The Apache HTTP Server Project develops and maintains an open-
source HTTP server for most OSs including UNIX and Windows.
▪ This project aims to provide a secure, efficient and extensible HTTP
server in line with the current standards.
▪ The Apache HTTP Server ("httpd") was launched in 1995 and it has
been the most popular web server on the Internet since April 1996.
▪ The httpd 2.4.56 is the latest available version ( released 2023-03-07 )

---

Hosting Static and Dynamic Websites
• We install web servers, such as Apache (HTTPd), Nginx or others, to host
websites
• These websites can sever either static or dynamic content
• Static websites contain only static content and are usually built using tools,
such as HTML and CSS.
• However, dynamic websites contain dynamic content that is usually
generated with the help of a database (e.g., MySQL, MariaDB and
MongoDB) and a server-side programming language (e.g., PHP, Python,
C#, Java and NodeJS).
• One thing to note here is that you will need to install additional tools
(including DB and server-side programming language) if your web server is
hosting dynamic websites.

---

Hosting Static and Dynamic Websites
Static Websites
Hosting
Dynamic Websites

---

Installing Apache
• Source Code: The Apache HTTP Server Project does not offer pre-compiled
executable software, but only provides source code.
• The official webpage demonstrate how to install Apache from source code for
Windows (https://httpd.apache.org/docs/2.4/platform/win_compiling.html) and
Linux (https://httpd.apache.org/docs/2.4/install.html)
• This option is more advanced and requires more technical expertise than other
installation methods.
• Pre-built Installers: In case you are unable to compile the Apache HTTP Server on
your own, there are various binary distributions that offer pre-built packages, such
as:
• XAMPP contains Apache, MariaDB, PHP, and Perl.
• XAMPP can be installed in Windows, OS X (for Mac) and Linux.
• Download from: https://www.apachefriends.org/download.html
• Other options include: ApacheHaus, Apache Lounge, Bitnami WAMP Stack and
WampServer.

---

Installing Apache
• Package Managers: Apache can be installed on Linux-based systems using
package managers such as apt-get, yum, or dnf.
• For example, to install on Ubuntu, you can run "sudo apt-get install
apache2“
• Docker: The simplest way to install an Apache web server in Docker is to
run a container using a preconfigured Docker Hub image.
• Type the docker run command to create and start a Docker container
based on the httpd image ‘’ docker run -d --name [container-name] -p
80:[host-port] httpd ‘’

---

Installing Apache
Source Code Compiling
n
Pre-built Installers XAMPP, WampServer, MAMP
o
i
t
a
l
l
a Ubuntu/Debian(apt-get)
t
s
n Package Managers
I
Fedora/CentOS/RHEL
(dnf, yum)
Docker

---

Installing: Source Code
• You use the original source code to install the Apache HTTP sever.
• This involves compiling the source code using the “make” command.
• Then, use the “make install” command to install the compiled executable files, libraries, and other necessary
files to the appropriate directories on the system
• Using the source code to install Apache HTTP server has its pros and cons:
• Pros
• Customization: By installing Apache2 from source, it allows for customizing modules, settings, and
features in a way that may not available in the pre-built installers or package managers, which is helpful in
meeting specific requirements.
• This customization can also help improving the performance by fine-tuning the server’s configuration
to the current platform (both SW and HW)
• Compatibility: Compiling source code allows you to create an Apache server that is compatible with your
current software stack, when the existing installers or package managers are not compatible with your
platform.
• Security: Installing Apache from source minimizes security vulnerabilities by allowing for compilation of only
necessary modules and settings, and applying latest security patches.
• Cons
• Time consuming: Installing from source requires downloading the source code, the build environment,
compiling the source code, installing the compiled software, and troubleshooting errors which is complex
and time-consuming
https://httpd.apache.org/docs/2.4/install.html

---

Installing: Source Code
Downloading, compiling and Installing
Customization Time consuming
Compatibility Complex and error-prone
Security
https://httpd.apache.org/docs/2.4/install.html

---

Installing: Source Code
• As we have previously mentioned, the installation from the source code is a little bit
complex and time-consuming for new users.
• Note: Installing from the source code is not required for this course.
• In this slide, we have summarised the steps for installing the Apache (HTTPd) server from
the source code on Linux-based systems, the official website also shows how to compile
the source code on Windows-based systems, which involve:
• Downloading the source code, usually a compressed file.
• Extracting the content of the compressed file. The NN must be replaced with the
downloaded version number
• Configuring the HTTPd server. The PREFIX must be replaced with the filesystem path
under which the server should be installed. If PREFIX is not specified, it defaults to
/usr/local/apache2.
• Then, compile and install using the make command
• You can also customise the configurations of the HTTPd sever by editing the httpd.conf
file
• Finally, start the HTTPd service to run the Apache web server
https://httpd.apache.org/docs/2.4/install.html

---

Installing: Source Code
https://httpd.apache.org/docs/2.4/install.html

---

Installing: Pre-built Installers
• If you cannot compile the Apache HTTP Server yourself, you can obtain a binary package
from numerous binary distributions available on the Internet.
• So, the second option for installing Apache is using pre-built installers, which is
recommended for those who are new to Apache and want an easy and user-friendly
interface.
• Popular options for pre-built installers for deploying Apache (httpd), and, optionally, PHP
and MySQL, include:
• XAMPP
• WampServer
• MAMP
• Apache Lounge
• We will demonstrate XAMPP as it is cross-platform and can be installed on Windows, Mac
and Linux machines.
• So, go to (https://www.apachefriends.org/download.html ) and download and install
XAMPP for your preferred OS.
https://www.apachefriends.org/download.html

---

Installing: Pre-built Installers
XAMPP, WampServer, MAMP, Apache Lounge,
Apache Haus
https://www.apachefriends.org/download.html

---

Starting Apache Web Server

---

Starting Apache Web Server
•After installing XAMPP, Open the XAMPP Control
Panel to start the required service.
•We will start the “Apache” service; however,
XAMPP installed other services, including
MySQL, FileZilla, Mercury and Tomcat

---

Testing Apache Web Server
• After successfully starting Apache from the XAMPP Control Panel, it will
be listening on the default HTTP port (port number 80)
• To connect to the server, and access the default page, open your web
browser (Firefox, Chrome or Edge), and enter the URL:
• http://localhost/
• Optionally, you can use the default loopback address (127.0.0.1) or
even your machine’s IP address instead
• You can also optionally add the port number (http://localhost:80/)
• If everything is fine, then the web browser will display the default web
page for the Apache web server

---

Testing Apache Web Server

---

Example: Creating a New Website
▪ Go to the installation folder of xampp (e.g. C:\xampp)
▪ Then open the htdocs folder, which represents the root folder for the
Apache server in case of XAMPP installation.
▪ In the htdocs, creates a new folder called taibah.
▪ In the taibah folder, create two files:
▪ index.html ( will contain the HTML of our example website )
▪ style.css ( will contain the CSS of styling our example website )

---

Content of index.html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta http-equiv="X-UA-Compatible"
content="IE=edge" />
<meta name="viewport" content="width=device-
width, initial-scale=1.0" />
<link rel="stylesheet" href="style.css" />
<title>Taibah University</title>
</head>
<body>
<h1>Taibha University</h1>
</body>
</html>

---

Content of style.css
body {
margin: 0;
padding: 0;
height: 100vh;
display: flex;
justify-content: center;
align-items: center;
font-family: sans-serif;
background-color: rgb(216, 219, 226);
}
h1 {
font-size: 5rem;
}

---

Opening Taibha Website
Go to: localhost/taibah
• Then, you will be able to see this page in the browser

---

Installing: Package Managers
Ubuntu/Debian Fedora/CentOS/RHEL
sudo dnf install httpd
sudo apt update
sudo systemctl enable httpd
sudo apt install apache2
sudo systemctl start httpd

---

Installing: Package Managers
• The third option for installing Apache is using Linux-based
package managers.
• Using these package managers allows you to easily install
Apache HTTP on different Linux distributions, such as apt-get
and dnf (yum previously)
• You can enable the HTTP service at boot by using the systemctl
enable command
• Then, you can access the default or home page of the Apache
HTTP server by typing “localhost” or the loopback address “e.g.
127.0.0.1” or the current IP address of the server

---

Installing on Ubuntu
• This slide show how to install Apache2 on Ubuntu

---

Checking the Status of Apache2
• This slides show how to check the status Apache2 on Ubuntu

---

Example: Creating Example Website
▪ Go to the Apache installation folder located at /var/www/html which
represents the root folder of the web server in Ubuntu distributions.
▪ In the /var/www/html, create the new folder called taibah,
▪ In the taibah folder, create the index.html, and the style.css files.
▪ Then, open the browser and go to localhost/taibah/
The root directory
for Apache web
server on Ubuntu

---

Installing: Docker
• The fourth and final option is installing Apache using docker.
• Installing Apache using docker involves pulling an Apache image from a
Docker repository (such as Docker Hub) and running it as a container
• Pros:
• Docker allows easy and consistent installation of Apache across different
platforms (e.g., Windows, Mac, Linux)
• Docker images can be easily shared and distributed and you can run
them using a single command as we will see in the following slide
• Cons
• Using docker can add additional overhead to those who have no
experience with docker
• It can also slightly affect the performance of the server as opposed to the
bare-metal (on the server directly without using docker) installation

---

Installing: Docker
Pulling an Apache image from a Docker repository (such as
Docker Hub) and running it as a container
Portable Complexity
Easily Shared Performance

---

Installing: Docker
Using the following command to run the httpd webserver
* Make sure that docker is installed on your machine
docker run -d --rm --name apache -p 10000:80 httpd:latest
* Feel free to choose a port number other than 10000
To test the webserver open the browser and go to localhost:10000

---

Refresh your Mind ☺
Which option for installing Apache server locally provides the
most control over customization and optimization?
1. Using pre-built installers like XAMPP
2. Compiling the source code
3. Using package managers
4. Using dockers

---

Refresh your Mind ☺
Which installation option is most suitable for those who want
to ensure maximum portability and ease of deployment across
different environments?
1. Using pre-built installers like XAMPP
2. Compiling the source code
3. Using package managers
4. Using dockers

---

Refresh your Mind ☺
Which installation option is the most suitable for those who are
new to Apache and want a user-friendly interface?
1. Using pre-built installers like XAMPP
2. Compiling the source code
3. Using package managers
4. Using dockers

---

Refresh your Mind ☺
Which command is used to install Apache on a system that
uses the apt package manager?
1. yum install httpd
2. apt-get install apache2
3. dnf install httpd
4. pacman -S apache

---

Refresh your Mind ☺
What is the default root directory for Apache web server on
Ubuntu?
1. /opt/lampp/htdocs/
2. /usr/local/apache2/htdocs/
3. /var/www/html/
4. /etc/apache2/

---

Thanks

---


# Chapter 3: Configuration Files

Configuration
Files
Web Administration –FWD 213

---

Main Configuration Files
• Apache HTTP Server is configured using the main configuration file httpd.conf (on Ubuntu apache2.conf).
• The location of this file is set at compile-time, but may be overridden with the -f command line flag.
• Other configuration files may be added to the main configuration file httpd.conf using INCLUDE directive,
and wildcards expressions can be used to include many configuration files.
• Example: the following code will include the configuration file “ssl.conf “and all the “*.conf” files inside the
directory “conf/vhosts”.
• Any directive may be placed in any of these configuration files. Changes to the main configuration files are
only recognized by httpd when it is started or restarted.

---

Syntax of the Configuration Files
• Httpd configuration files managed by placing directives in plain text configuration files, one per line.
• The backslash "\" may be used as the last character on a line to indicate that the directive continues
onto the next line. There must be no other characters or white space between the backslash and
the end of the line.
❑Directives:
• Consists of the directive name followed by a series of one or more space-separated arguments. If
an argument contains a space, the argument must be enclosed in double quotes.
- DirectiveName [argument-list]
• Directives in the configuration files are case-insensitive, but arguments to directives are often case
sensitive.
• Lines that begin with the hash character "#" are considered comments, and are ignored. Comments
may not be included on the same line as a configuration directive.

---

apatch2.conf file
in Ubuntu

---

Syntax of the Configuration Files
• The values of variables defined with the Define directive, and can be used in configuration file lines
using the syntax ${VAR}.
- Define parameter-name [parameter-value]
• If "VAR" is the name of a valid variable, the value of that variable is substituted into that spot in the
configuration file line, and processing continues as if that text were found directly in the
configuration file.
• Variable names may not contain colon ":" characters.
Define servername www.example.com
Define SSL
DocumentRoot "/var/www/${servername}/htdocs"
• You can check your configuration files for syntax errors without starting the server by using
apachectl configtest or the -t command line option.

---

Modules
• The Apache HTTP Server is a modular program where the administrator can choose the functionality to
include in the server by selecting a set of modules. Functions are in the form of modules.
• Only the most basic functionality is included in the core server. Extended features are available through
external modules , called Dynamic Shared Objects (DSOs), which can be dynamically loaded into httpd
using LoadModule directive.
• The LoadModule directive links in the object file or library (filename) and adds the module structure named
(module) to the list of active modules.
- LoadModule module filename
• Example
• To see which modules are currently compiled into the server, you can use the apachectl -l command line
option. You can also see what modules are loaded dynamically using the -M command line option.
• apachectl -M: list all Apache installed modules.

---

$apachectl -M
• Static: modules included in the
server at compile-time.
• Dynamic: modules loaded using
the LoadModule directive.

---

Scope of Directives (Containers)
❑Directives placed in the main configuration files apply to the entire server.
❑Scope of Directives:
• Change the configuration for only a part of the server.
• You can scope your directives by placing them in <DIRECTORY>, <DIRECTORYMATCH>, <FILES>,
<FILESMATCH>, <LOCATION>, and <LOCATIONMATCH> sections.
• These sections limit the application of the directives which they enclose to particular filesystem
locations or URLs. They can also be nested, allowing for very fine grained configuration.

---

Scope of Directives (Containers)
• Httpd has the capability to serve many different websites simultaneously. This is called Virtual
Hosting.
• Directives can also be scoped by placing them inside <VIRTUALHOST> sections, so that they will
only apply to requests for a particular website.
• Although most directives can be placed in any of these sections, some directives do not make
sense in some contexts. For example, directives controlling process creation can only be placed in
the main server context.

---

.htaccess Files
• Per-directory configuration files
• Httpd allows for decentralized management of configuration via special files placed inside the
web tree.
• The special files are usually called .htaccess, but any name can be specified in the AccessFileName
directive inside the main configuration file .
• Directives placed in .htaccess files apply to the directory where you place the file, and all sub-
directories.
• The .htaccess files follow the same syntax as the main configuration files. Since .htaccess files are
read on every request, changes made in these files take immediate effect.
• The server administrator further controls what directives may be placed in .htaccess files by
configuring the AllowOverride directive in the main configuration file.

---

.htaccess Files
…
usr DocumentRoot
.htaccess files apply to the
local directory where you place the
file, and all sub-directories.
directory1 directory2
(.htaccess )
apache2
.subd2
conf
Directives declared in .htaccess file
can override earlier configuration
httpd.conf
directives in httpd.conf file

---

AllowOverride Directive
• Determines the types of directives that are allowed in .htaccess files
• When the server finds an .htaccess file (as specified by AccessFilename directive in the main
configuration file), it needs to know which directives declared in that file can override earlier
configuration directives.
Basic directives
• When this directive is set to None, .htaccess files are completely ignored. In this case, the
server will not even attempt to read .htaccess files in the filesystem.
• Example :
AccessFileName .acl
• Before returning the document /usr/local/web/index.html, the server wil read
/.acl, /usr/.acl, /usr/local/.acl and /usr/local/web/.acl for directives unless
they have been disabled with:
<Directory "/">
AllowOverride None
</Directory>

---

apache2.conf

---

Configuration Sections
• Directives in the configuration may apply to the entire server, or they may be restricted to apply only to
particular directories, files, hosts, or URLs using the configuration section containers.
❑Types of Configuration Section Containers:
❖Containers that evaluated for each request. The enclosed directives are applied only for those requests that
match the containers.
➢ <DIRECTORY>, <DIRECTORYMATCH>.
➢ <FILES>, <FILESMATCH>.
➢ <LOCATION>, <LOCATIONMATCH>.
❖Containers that evaluated only at server startup and restart. If their conditions are true at startup, then the
enclosed directives will apply to all requests.
➢ <IFDEFINE>
➢ <IFMODULE>
➢ <IFVERSION>

---

< >
The IfDefine container.
• It encloses directives that will only be applied if an appropriate parameter is defined on
the httpd command line using –D parameter.
• -D parameter:
o Sets a configuration parameter which can be used with <IfDefine> sections in the configuration
files to conditionally skip or process commands at server startup and restart.
• For example, with the following configuration, all requests will be redirected to another site only
if the server is started using httpd –DClosedForNow.
<IfDefine ClosedForNow>
Redirect "/" "http://otherserver.example.com/"
</IfDefine>

---

The <IfModule> container
• It encloses directives that will only be applied if a particular module is available in the server.
• The module must either be statically compiled in the server, or it must be dynamically compiled
and its LoadModule line must be earlier in the configuration file.
• This directive should only be used if you need your configuration file to work whether or not
certain modules are installed. It should not be used to enclose directives that you want to work all
the time, because it can suppress useful error messages about missing modules.
• Example: the MimeMagicFile directive will be applied only if mod_mime_magic is available.
<IfModule mod_mime_magic.c>
MimeMagicFile "conf/magic"
</IfModule>

---

The <IfVersion> container
• Very similar to <IFDEFINE> and <IFMODULE>, except it encloses directives that will only be
applied if a particular version of the server is executing.
• This module is designed for the use in test suites and large networks which have to deal with
different httpd versions and different configurations.
<IfVersion >= 2.4>
# this happens only in versions greater or
# equal 2.4.0.
</IfVersion>

---

Filesystem & Webspace
• The most commonly used configuration section containers are the ones that change the
configuration of particular places in the filesystem or webspace.
• The filesystem: is the view of your disks as seen by your operating system.
• For example, in a default install, Apache httpd resides at /usr/local/apache2 in the Unix filesystem,
"c:/Program Files/Apache Group/Apache2" in the Windows filesystem.
• The webspace: is the view of your site as delivered by the web server and seen by the client. So,
the path /dir/ in the webspace corresponds to the path /usr/local/apache2/htdocs/dir/ in the
filesystem of a default Apache httpd install on Unix.
• The webspace need not map directly to the filesystem, since webpages may be generated
dynamically from databases or other locations.

---

Filesystem Containers
• The <DIRECTORY> and <FILES> directives, along with their regex counterparts, apply directives to parts of the
filesystem.
• Directives enclosed in a <DIRECTORY> section apply to the named filesystem directory and all subdirectories
of that directory (as well as the files in those directories).
• The same effect can be obtained using .htaccess files. For example, in the following configuration, directory
indexes will be enabled for the /var/web/dir1 directory and all subdirectories.
• Directives enclosed in a <FILES> section apply to any file with the specified name, regardless of what
directory it lies in. For example, the following configuration directives will, when placed in the main section
of the configuration file, deny access to any file named private.html regardless of where it is found.

---

Filesystem Containers
• To address files found in a particular part of the filesystem, the <FILES> and <DIRECTORY> sections can be
combined.
• For example, the following configuration will deny access to /var/web/dir1/private.html,
/var/web/dir1/subdir2/private.html, /var/web/dir1/subdir3/private.html, and any other instance of private.html
found under the /var/web/dir1/ directory.

---

Webspace Containers
• The <LOCATION> directive and its regex counterpart change the configuration for content in the webspace.
• For example, the following configuration prevents access to any URL-path that begins in /private.
• In particular, it will apply to requests for http://yoursite.example.com/private,
http://yoursite.example.com/private123, and http://yoursite.example.com/private/dir/file.html as well as any
other requests starting with the /private string.
• The <LOCATION> directive need not have anything to do with the filesystem.
• For example, the following example shows how to map a particular URL to an internal Apache HTTP Server
handler provided by MOD_STATUS. No file called server-status needs to exist in the filesystem.

---

Wildcards and Regular Expressions
• The <DIRECTORY>, <FILES>, and <LOCATION> directives can each use shell-style wildcard
characters.
➢"*" matches any sequence of characters (everything).
➢"?" matches any single character.
➢ "[seq]" matches any character in seq.
➢ Note: The "/" character will not be matched by any wildcard; it must be specified explicitly.
• If even more flexible matching is required, each container has a regular expression (regex)
counterpart <DIRECTORYMATCH>, <FILESMATCH>, and <LOCATIONMATCH> that allow perl-
compatible regular expressions to be used in choosing the matches.

---

Wildcards and Regular Expressions
• A non-regex wildcard section that changes the configuration of all
user directories could look as follows:
<Directory "/home/*/public_html">
Options Indexes
</Directory>
• Using regex sections, we can deny access to many types of image files
(ends with .gif, .png, .jpg ) at once.
<FilesMatch "\.(gif|png|jpg)$">
Require all denied
</FilesMatch>

---

What to use When
• When applying directives to objects that reside in the filesystem always use <DIRECTORY> or
<FILES>.
• When applying directives to objects that do not reside in the filesystem (such as a webpage
generated from a database), use <LOCATION>.
• It is important to never use <LOCATION> when trying to restrict access to objects in the
filesystem.
• This is because many different webspace locations (URLs) could map to the same filesystem
location, allowing your restrictions to be circumvented.

---

Server-Wide Configuration
The directives provided by the CORE server which are used to configure the basic operations of the
server.
Directive Description: Example
ServerRoot Base directory for the server files. ServerRoot /usr/local/apache
ServerAdmin Email address that the server includes in ServerAdmin www-admin@foo.example.com
error messages sent to the client.
ServerName Hostname or IP address that the server ServerName www.example.com Or
uses to identify itself. ServerName 10.0.2.15
DocumentRoot sets the directory from which httpd will DocumentRoot "/usr/web" Or
serve files. DocumentRoot "/var/www"
ErrorLog sets the name of the file to which the ErrorLog "/var/log/httpd/error_log"
server will log any errors it encounters.

---

Access Control
• Apache's Require directive provides a variety of different ways to allow or deny access to resources.
• These authorization providers affect which hosts can access an area of the server.
❑Require All Granted: Access is allowed unconditionally.
❑Require All Denied: Access is denied unconditionally.
▪ Access can be controlled by hostname, IP Address, or IP Address range.
❑Require IP
• The IP provider allows access to the server to be controlled based on the IP address of the remote
client.
• When Require ip ip-address is specified, then the request is allowed access if the IP address matches.
• Full IP address:
Require ip 10.1.2.3
• Partial IP address: the first 1 to 3 bytes of an IP address, for subnet restriction.
Require ip 10.1

---

Access Control
❑Require host
• The host provider allows access to the server to be controlled based on the host name of
the remote client.
• When Require host host-name is specified, then the request is allowed access if the
host name matches.
• (partial) domain-name
Require host example.org
Require host .net example.edu
• Hosts whose names match, or end in, this string are allowed access.
• Only complete components are matched, so the above example will
match foo.example.org but it will not match fooexample.org.

---

Thank You

---


# Chapter 4: Virtual Hosts

Web Administration – FWD 213

---

Understand virtual hosting Virtual host definition
Use virtual hosts to hold
Virtual host types
multiple websites
Explore virtual hosting
Virtual host scenarios
scenarios
Create and configure a virtual
Creating and configuring a vhost
host
Virtual Hosts 2

---

3
Virtual Hosts

---

▪ Virtual Host allows to run
multiple websites from a
single physical server or
virtual private server.
▪ Most of our web root have
/www, so it has high chances
of being hacked. Hence
Virtual Host is used as it
provides security.
Multiple websites on a single server.
▪ Each virtual host needs to
have a directory for storing
virtual host data.
4
Virtual Hosts

---

We can configure Apache Virtual Host in different ways:
▪ Name-based Virtual Hosts (More than one web site per IP
address)
▪ IP-based Virtual Hosts (An IP address for each web site)
▪ Virtual Host examples for common setups
▪ File Descriptor Limits (or, Too many log files)
▪ Dynamically Configured Mass Virtual Hosting
▪ In-Depth Discussion of Virtual Host Matching
Virtual Hosts 5

---

▪ Virtual hosts can be
▪ "IP-based“: meaning that we have a different IP address for
every web site, or
▪ "name-based“: meaning that we have multiple names
running on each IP address.
▪ IP-based virtual hosts use the IP address of the connection
to determine the correct virtual host to serve.
▪ With Name-based virtual hosting, the server relies on the
client to report the hostname as part of the HTTP headers.
Using this technique, many different hosts can share the
same IP address.
Virtual Hosts 6

---

▪ IP-based virtual hosting is a
method to apply different directives
based on the IP address and port a
request is received on. Most
commonly, this is used to serve
different websites on different ports
or interfaces.
▪ The websites point to the same
server which is run by Apache.
Virtual Hosts 7

---

Suppose that we are serving the domain www.example.com and
we wish to add the virtual host other.example.com, which points
at the same IP address. Then, we simply add the following code to
the configuration file httpd.conf
Virtual Hosts 8

---

▪ The server has two IP addresses
(172.20.30.40 and 172.20.30.50)
which resolve to the names
www.example.com and
www.example.org respectively.
▪ Requests for any address not
specified in one of the
<VirtualHost> directives (such
as localhost, for example) will go
to the main server, if there is
one.
Virtual Hosts 9

---

▪ The name-based virtual host allows one IP address to host more
than one Web site (host name).
▪ Name-based virtual hosts have the same IP address but different
host names.
Virtual Hosts 10

---

11
Virtual Hosts

---

Name-based hosts on more than one IP
address:
▪ The server has two IP addresses. On
one (172.20.30.40), we will serve the
"main" server, server.example.com and on
the other (172.20.30.50), we will serve
two or more virtual hosts.
▪ Any request to an address other than
172.20.30.50 will be served from the
main server. A request to 172.20.30.50
with an unknown hostname, or no
Host: header, will be served from
www.example.com.
Virtual Hosts 12

---

Serving the same content on different IP addresses:
▪ The server machine has two IP addresses (192.168.1.1 and 172.20.30.40). The
machine is sitting between an internal (intranet) network and an external
(internet) network.
▪ Outside of the network, the name server.example.com resolves to the external
address (172.20.30.40), but inside the network, that same name resolves to
the internal address (192.168.1.1).
▪ The server can be made to respond to internal and external requests with the
same content, with just one <VirtualHost> section. Now requests from both
networks will be served from the same <VirtualHost>.
Virtual Hosts 13

---

Running different sites on different
ports.
▪ We have multiple domains going to
the same IP and we want to serve
multiple ports.
▪ The following example illustrates
that the name-matching takes place
after the best matching IP address
and port combination is determined.
Virtual Hosts 14

---

Dynamic virtual host:
▪ The dynamic virtual host allows to dynamically add Web sites
(host names) by adding directories of content.
▪ This approach is based on automatically inserting the IP address
and the contents of the Host: header into the pathname of the
file that is used to satisfy the request.
▪ Advantages:
▪ A smaller configuration file so that the server starts faster and uses less
memory.
▪ Adding virtual hosts does not require the configuration to be changed or
the server to be restarted.
▪ We cannot have a different log file for each virtual host
Virtual Hosts 15

---

Mixed port-based and IP-based
virtual hosts:
▪ The server machine has two IP
addresses (172.20.30.40 and
172.20.30.50) which resolve to the
names www.example.com and
www.example.org respectively.
▪ In each case, we want to run hosts
on ports 80 and 8080.
Virtual Hosts 16

---

Mixed name-based and IP-based vhosts:
▪ Any address mentioned in the
argument to a virtual host that
never appears in another virtual
host is a strictly IP-based virtual
host.
Virtual Hosts 17

---

Using “Virtual_host” and “mod_proxy” together:
▪ The following example allows a front-end machine to proxy a
virtual host through to a server running on another machine.
▪ In the example, a virtual host of the same name is configured on
a machine at 192.168.111.2. The ProxyPreserveHostOn directive is
used so that the desired hostname is passed through, in case we
are proxying multiple hostnames to a single machine.
Virtual Hosts 18

---

Using _default_ vhosts:
▪ _default_ vhosts for all ports:
▪ Catching every request to any unspecified IP address and
port, i.e., an address/port combination that is not used for
any other virtual host.
▪ Using such a default vhost with a wildcard port effectively
prevents any request going to the main server.
▪ _default_ vhosts for different ports:
▪ Same as setup 1, but the server listens on several ports and
we want to use a second _default_ vhost for port 80.
▪ The default vhost for port 80 (which must appear before any
default vhost with a wildcard port) catches all requests that
were sent to an unspecified IP address.
▪ The main server is never used to serve a request.
Virtual Hosts 19

---

Using _default_ vhosts:
▪ _default_ vhosts for one port:
▪ We want to have a default vhost for port 80, but no other
default vhosts.
▪ A request to an unspecified address on port 80 is served from the default
vhost. Any other request to an unspecified address and port is served
from the main server.
▪ Any use of * in a virtual host declaration will have higher precedence
than _default_.
Virtual Hosts 20

---

Migrating a name-based vhost to an IP-based
vhost:
▪ The name-based vhost with a hostname
www.example.org should get its own IP address. To
avoid problems with name servers or proxies who
cached the old IP address for the name-based
vhost, we want to provide both variants during a
migration phase.
▪ we can simply add the new IP address
(172.20.30.50) to the VirtualHost directive.
▪ The vhost can now be accessed through the new
address (as an IP-based vhost) and through the
old address (as a name-based vhost).
Virtual Hosts 21

---

22
Virtual Hosts

---

▪ By default, Apache is configured with a single default virtual
host.
▪ The configuration file that contains configuration directives for
the default Web server is
/etc/apache2/sites-available/000-default.conf:
▪ The default Document root is set to /var/www/html/
The simplest way to create a new virtual host is to copy
and rename the default file (/etc/apache2/sites-
available/000-default.conf), and then modify the
directives to point to our new website.
Virtual Hosts 23

---

1. Create a new configuration file by copying and renaming the default
configuration file.
2. Open the new file in a text editor and change the ServerAdmin
directive to an email that the site administrator can receive emails
through.
3. Add a new directive called ServerName. This directive will specify the
domain name our site will answer to. This will most likely be our
domain.
4. Change the DocumentRoot directive to specify the directory that will
contain the webpage files.
5. Activate the website with the a2ensite command.
6. Restart Apache to apply the changes.
Virtual Hosts 24

---

Step 1: Create a Directory Structure: Create directories and a directory
structure at the following location /var/www. In our example, we’ve created
phxnap1.com and phxnap2.com directories, one for each domain name.
1. Enter the following command and replace the example domain with the
domain names. Within the directories, we also created public_html. These
directories are going to store website files for the domains.
2. Next, create a sample index.html page for each domain, using text editor:
Virtual Hosts 25

---

3. Add the following sample HTML:
4. Save and exit the file.
5. Follow the same steps, to create a sample page for the second domain:
Virtual Hosts 26

---

6. To prevent any permission issues, modify the ownership of the
documents’ root directory to www-data, using the chown
command:
Virtual Hosts 27

---

Step 2 “Create a Virtual Host Configuration File”: Apache Virtual Host
configuration files are stored in the /etc/apache2/sites-available directory.
1. To create a basic configuration file for the first domain, enter the domain
information in the command:
2. Add the following configuration block to create a basic configuration file. This
example uses the first test domain, phxnap1.com. Make sure to enter the correct
domain for your website:
ServerName – represents the domain
ServerAlias – represents all other domains (e.g., subdomains)
DocumentRoot – directory used by Apache to serve domain files
ErrorLog, CustomLog – designates the log files location
Virtual Hosts 28

---

3. Once you have edited the config file for the first domain, repeat the process
for the rest. In our case, we will run:
4. Then, add the configuration block as in the example above, making sure to
change the values for phxnap2.com:
Virtual Hosts 29

---

Step 3: Enable Virtual Host Configuration Files: To enable the virtual host
file, create a symbolic link from the virtual host file to the sites-enabled
directory. Apache2 reads this file when staring.
1. Use the a2ensite helper to enable the virtual host file with the command:
The output will appear as:
2. Repeat the process for the second domain.
Virtual Hosts 30

---

3. Verify the configuration file syntax is correct using the command:
The message in the terminal will confirm that the syntax is correct: “Syntax OK”.
4. Restart Apache2 for the changes to be applied.
5. Finally, access the websites (e.g., phxnap1.com). Based on the index.html file
we created earlier, the appropriate message should appear for each domain.
Virtual Hosts 31

---

32
Virtual Hosts

---

▪ To encrypt communication between an Apache web server and web clients,
we need to use the mod_ssl module, we must be enabled using the sudo
a2enmod ssl command:
▪ The default SSL configuration file is
/etc/apache2/sites-available/default-ssl.conf.
Virtual Hosts 33

---

▪ To configure Apache for HTTPS, use the sudo a2ensite default-ssl command:
Virtual Hosts 34

---

▪ Apache in quite good in logging everything that happens on a
webserver, from the initial request, through the URL mapping
process, to the final resolution of the connection.
▪ Two types of log files are available: access.log and error.log.
▪ By default, Apache writes
▪ the transfer log to the /var/log/apache2/access.log file, and
▪ the error log file to /var/log/apache2/error.log.
Virtual Hosts 35

---

▪Example event from the access.log file:
▪The first field (192.168.198.153) represents the IP address of the web
client that requested the list.html web page. We can also recognize the
date, the browser and the operating system used
Virtual Hosts 36

---

▪ error.log contains error events that Apache encounters in processing requests.
Virtual Hosts 37

---

Virtual Hosts

---

▪ Apache HTTP Server Introduction, Antun Peicevic, Marko Maslac,
CreateSpace Independent Publishing Platform, 2016, ISBN:1530866421,
9781530866427.
▪ https://httpd.apache.org/docs/2.4/vhosts/examples.html
▪ https://phoenixnap.com/kb/how-to-set-up-apache-virtual-hosts-ubuntu
Virtual Hosts 39

---


# Chapter 5: SSL Configuration

Web Administration –FWD 213
Dr. Yusra Al Najjar

---

▪ Secure Socket Layer (SSL) port is 443
▪ SSL is important to protect communication between browser and
web-server
▪ Requires the creation of SSL certificates and Certificate Signing
Requests (CSR)
▪ For integrity SSL certificates are signed by a Certificate Authority’s
(CA)
Dr. Yusra Al Najjar

---

▪Each SSL certificate has a Public and Private key
▪The Public Key is used to encrypt the information
▪The Public Key is accessible to everyone
▪The private Key is used to decipher the information
▪The private should be not be disclosed
Dr. Yusra Al Najjar

---

Dr. Yusra Al Najjar

---

Understanding SSL requires an understanding of
cryptographic algorithms, message digest functions (aka.
one-way or hash functions), and digital signatures.
• Cryptographic Algorithms
• Conventional cryptography
• Public key cryptography
• Message Digests
• Digital Signatures
Dr. Yusra Al Najjar

---

Suppose Alice wants to send a message to her bank to transfer some money. Alice would
like the message to be private, since it will include information such as her account
number and transfer amount. One solution is to use a cryptographic algorithm, a
technique that would transform her message into an encrypted form, unreadable until it
is decrypted. Once in this form, the message can only be decrypted by using a secret key.
Without the key the message is useless: good cryptographic algorithms make it so
difficult for intruders to decode the original text that it isn’t worth their effort.
Dr. Yusra Al Najjar

---

• Conventional cryptography: known as symmetric cryptography, requires the sender
and receiver to share a key: a secret piece of information that may be used to encrypt
or decrypt a message.
• Public key cryptography: known as asymmetric cryptography, solves the key exchange
problem by defining an algorithm which uses two keys, each of which may be used to
encrypt a message. If one key is used to encrypt a message then the other must be
used to decrypt it.
Dr. Yusra Al Najjar

---

▪ Although Alice may encrypt her message to make it
private, there is still a concern that someone might
modify her original message or substitute it with a
different one, in order to transfer the money to
themselves, for instance. One way of guaranteeing the
integrity of Alice’s message is for her to create a
concise summary of her message and send this to the
bank as well. Upon receipt of the message, the bank
creates its own summary and compares it with the one
Alice sent. If the summaries are the same then the
message has been received intact.
• A summary such as this is called a message digest,
one-way function or hash function.
• Message digests are used to create a short, fixed-
length representation of a longer, variable-length
message.
Dr. Yusra Al Najjar

---

When Alice sends a message to the bank, the bank needs to ensure that the message is
really from her, so an intruder cannot request a transaction involving her account. A digital
signature, created by Alice and included with the message, serves this purpose. Digital
signatures are created by encrypting a digest of the message and other information (such
as a sequence number) with the sender’s private key. Though anyone can decrypt the
signature using the public key, only the sender knows the private key.
Digital signature is different from electronic signature.
Dr. Yusra Al Najjar

---

Although Alice could have sent a private message to the bank, signed it and ensured the
integrity of the message, she still needs to be sure that she is really communicating with the
bank. This means that she needs to be sure that the public key she is using is part of the
bank’s key-pair, and not an intruder’s. Similarly, the bank needs to verify that the message
signature really was signed by the private key that belongs to Alice.
If each party has a certificate which validates the other’s identity, confirms the public key and
is signed by a trusted agency, then both can be assured that they are communicating with
whom they think they are. Such a trusted agency is called a Certificate Authority and
certificates are used for authentication.
Dr. Yusra Al Najjar

---

▪ Certificate Contents: A certificate associates a public key
with the real identity of an individual, server, or other entity,
known as the subject.
▪ Certificate Authorities: By verifying the information in a
certificate request before granting the certificate, the
Certificate Authority assures itself of the identity of the
private key owner of a key-pair. For instance, if Alice
requests a personal certificate, the Certificate Authority
must first make sure that Alice really is the person the
certificate request claims she is.
▪ Certificate Chains: A Certificate Authority may also issue
a certificate for another Certificate Authority.
Dr. Yusra Al Najjar

---

The Secure Sockets Layer protocol is a protocol layer which may be placed
between a reliable connection-oriented network layer protocol (e.g. TCP/IP) and
the application protocol layer (e.g. HTTP). SSL provides for secure communication
between client and server by allowing mutual authentication, the use of digital
signatures for integrity and encryption for privacy.
Dr. Yusra Al Najjar

---

▪ The SSL session is established
by following a handshake
sequence between client and
server, as shown in the Figure.
This sequence may vary,
depending on whether the server
is configured to provide a server
certificate or request a client
certificate.
▪ Note: Once an SSL session has
been established, it may be
reused. This avoids the
performance penalty of repeating
the many steps needed to start a
session. To do this, the server
assigns each SSL session a unique
session identifier which is cached
in the server and which the client
can use in future connections to
reduce the handshake time.
Dr. Yusra Al Najjar

---

The key exchange method
defines how the shared secret
symmetric cryptography key
used for application data
transfer will be agreed upon
by client and server.
Dr. Yusra Al Najjar

---

SSL uses conventional symmetric
cryptography, as described earlier, for
encrypting messages in a session. There are
nine choices of how to encrypt, including
the option not to encrypt:
• No encryption
• Stream Ciphers: keys and algorithms are
applied to each binary digit in a data
stream, one bit at a time, rather than
encrypting block of data
• Block Ciphers: plain text message divide
into fixed size blocks and encrypt each
block with some fixed size of key
Dr. Yusra Al Najjar

---

The choice of digest function determines how a digest is created from
a record unit. SSL supports the following:
• No digest (Null choice)
• MD5, a 128-bit hash
• Secure Hash Algorithm (SHA-1), a 160-bit hash
The message digest is used to create a Message Authentication Code
(MAC) which is encrypted with the message to verify integrity and to
protect against replay attacks.
Dr. Yusra Al Najjar

---

The handshake sequence uses three
protocols:
1. The SSL Handshake Protocol for
performing the client and server
SSL session establishment.
2. The SSL Change Cipher Spec
Protocol for actually establishing
agreement on the Cipher Suite for
the session.
3. The SSL Alert Protocol for
conveying SSL error messages
between client and server.
Dr. Yusra Al Najjar

---

The SSL Record Protocol, shown in
the figure , is used to transfer
application and SSL Control data
between the client and server,
where necessary fragmenting this
data into smaller units, or
combining multiple higher level
protocol data messages into
single units.
Dr. Yusra Al Najjar

---

One common use of SSL is to secure Web HTTP communication
between a browser and a webserver. This does not preclude the use
of non-secured HTTP - the secure version (called HTTPS) is the same
as plain HTTP over SSL, but uses the URL scheme https rather than
http, and a different server port (by default, port 443). This
functionality is a large part of what MOD SSL provides for the Apache
webserver.
Dr. Yusra Al Najjar

---

Web Administration –FWD 213
Dr. Yusra Al Najjar

---

▪ Look for SSL configuration file httpd-
ssl.conf in the folder \conf\extra
▪ Your SSL configuration will need to
contain, at minimum, the following
directives.

---

▪ The following enables only the strongest ciphers:
▪ SSLCipherSuite HIGH:!aNULL:!MD5
▪ While with the following configuration you specify a preference for
specific speed-optimized ciphers (which will be selected by mod ssl,
provided that they are supported by the client):
▪ SSLCipherSuite RC4-SHA:AES128-SHA:HIGH:!aNULL:!MD5
▪ SSLHonorCipherOrder on

---

▪ MOD SSL can be reconfigured within Location blocks, to give a per-directory
solution, and can automatically force a renegotiation of the SSL parameters to
meet the new configuration. This can be done as follows:
SSLCipherSuite ALL:!aNULL:RC4+RSA:+HIGH:+MEDIUM:+LOW:+EXP:+eNULL
<Location "/strong/area">
# but https://hostname/strong/area/ and below
# requires strong ciphers
SSLCipherSuite HIGH:!aNULL:!MD5
</Location>

---

▪ The Online Certificate Status Protocol (OCSP) is a mechanism for determining whether or not a server
certificate has been revoked, and OCSP Stapling is a special form of this in which the server, such as
httpd and mod ssl, maintains current OCSP responses for its certificates and sends them to clients which
communicate with the server.
▪ Once general SSL support has been configured properly, enabling OCSP Stapling generally requires only
very minor modifications to the httpd configuration - the addition of these two directives:
SSLUseStapling On
SSLStaplingCache "shmcb:logs/ssl_stapling(32768)"
▪ These directives are placed at global scope (i.e., not within a virtual host definition) wherever other
global SSL configuration directives are placed, such as in conf/extra/httpd-ssl.conf
▪ If you enabled an SSL session cache use the mechanism for SSLSTAPLINGCACHE. For example:
SSLSessionCache "dbm:logs/ssl_scache"
SSLStaplingCache "dbm:logs/ssl_stapling"

---

▪ How can I force clients to authenticate using certificates?
▪ When you know all of your users (eg, as is often the case on a corporate
Intranet), you can require plain certificate authentication. All you need to do is
to create client certificates signed by your own CA certificate (ca.crt) and then
verify the clients against this certificate.
# require a client certificate which has to be directly
# signed by our CA certificate in ca.crt
SSLVerifyClient require
SSLVerifyDepth 1
SSLCACertificateFile "conf/ssl.crt/ca.crt"

---

Yes. HTTP and HTTPS use different server
ports (HTTP binds to port 80, HTTPS to port
443), so there is no direct conflict between
them. You can either run two separate server
instances bound to these ports, or use
Apache’s elegant virtual hosting facility to
create two virtual servers, both served by the
same instance of Apache - one responding
over HTTP to requests on port 80, and the
other responding over HTTPS to requests on
port 443.

---

▪ What are RSA Private Keys, CSRs and Certificates?
▪ An RSA private key file is a digital file that you can use to
decrypt messages sent to you. It has a public component
which you distribute (via your Certificate file) which allows
people to encrypt those messages to you.
▪ A Certificate Signing Request (CSR) is a digital file which
contains your public key and your name. You send the CSR to
a Certifying Authority (CA), who will convert it into a real
Certificate, by signing it.
▪ A Certificate contains your RSA public key, your name, the
name of the CA, and is digitally signed by the CA.
▪ Browsers that know the CA can verify the signature on that
Certificate, thereby obtaining your RSA public key. That
enables them to send messages which only you can decrypt.

---

▪ You should now have two files: server.key and
server.crt. These can be used as follows in your
httpd.conf file:
▪ SSLCertificateFile
"/path/to/this/server.crt"
▪ SSLCertificateKeyFile
"/path/to/this/server.key"

---

Dr. Yusra Al Najjar

---


# Chapter 6: Forward Proxy Server

Web Administration – FWD 213

---

A proxy server is a server that routes traffic between
client(s) and another system, usually external to the
network. By doing so, it can regulate traffic according to
pre-set policies, convert and mask client IP addresses,
enforce security protocols, and block unknown traffic.
A proxy server is a server that acts as a middleman in the flow
of your internet traffic so that your internet activities appear to
come from somewhere else.
Proxy server hides the identity of a client.
2

---

3

---

Apache HTTP Server can be configured in both a forward
and reverse proxy (also known as gateway) mode.
An ordinary forward proxy is an intermediate server that
sits between the client and the origin server. In order to
get content from the origin server, the client sends a
request to the proxy naming the origin server as the
target.
The proxy then requests the content from the origin
server and returns it to the client. The client must be
specially configured to use the forward proxy to access
other sites.
4

---

A typical usage of a forward proxy is to provide Internet
access to internal clients that are otherwise restricted by
a firewall. The forward proxy can also use caching (as
provided by MOD CACHE) to reduce network usage.
The forward proxy is activated using the PROXYREQUESTS
directive. Because forward proxies allow clients to access
arbitrary sites through your server and to hide their true
origin, it is essential that you secure your server so that
only authorized clients can access the proxy before
activating a forward proxy.
5

---

This allows or prevents Apache httpd from
functioning as a forward proxy server. In a typical
reverse proxy or gateway configuration, this option
should be set to Off.
In order to get the functionality of proxying HTTP or
FTP sites, you need also MOD PROXY HTTP or MOD
PROXY FTP (or both) present in the server.
In order to get the functionality of (forward)
proxying HTTPS sites, you need MOD PROXY
CONNECT enabled in the server.
! Warning
Do not enable proxying with PROXYREQUESTS until
you have secured your
6

---

7

---

▪There are many different types of forward proxies. The
most common ones are classified by their origin. In this
case, there are two types of proxies – residential
proxies and datacenter proxies.
Residential proxies. These proxies have a real IP address
1.
provided by an Internet Service Provider (ISP) with a
physical location.
Datacenter proxies. This proxy type isn’t affiliated with
2.
an ISP, as IP addresses come from secondary sources like
data centers.
8

---

❑Accessing restricted geo-locations. Forward proxy servers could come in handy to
access geo-restricted content. When users are browsing the internet, they usually
see content according to their geo-location. When using a forward proxy, users can
access a variety of content intended for other countries. For example, this is
especially useful for companies that provide ad verification services. These
companies can monitor ads regardless of their geo-location. For example, if you
were looking to see if your ads are visible in Brazil, you would use a Brazil proxy,
or Germany proxy to access content in Germany.
❑Ensuring anonymity. A forward proxy server acts as an additional safety layer that
hides the web server’s real IP address by using one of its own. This is the reason
why using forward proxy servers ensures higher levels of anonymity and security.
9

---

❑Web scraping. The most common usage of proxies is web scraping.
Companies usually gather data to improve their marketing, pricing, and
other business strategies. Web scraping helps companies to stay
competitive in the market.
Forward proxies can also be used to control and monitor internet usage,
create and manage social media accounts, and much more.
10

---

❑The proxy manages the configuration of origin servers and their
communication parameters in objects called workers.
❑There are two built-in workers: the default forward proxy worker and
the default reverse proxy worker. Additional workers can be configured
explicitly.
❑The two default workers have a fixed configuration and will be used if
no other worker matches the request. They do not use HTTP Keep-Alive
or connection reuse. The TCP connections to the origin server will
instead be opened and closed for each request.
11

---

In order to configure Apache as a proxy server, you need to open the
httpd.conf file in the conf folder installed with apache, and enable the
following modules concerning proxy:
proxy, proxy_http, and proxy_connect modules.
#LoadModule proxy_module modules/mod_proxy.so
#LoadModule proxy_http_module modules/mod_proxy_http.so
#LoadModule proxy_connect_module modules/mod_proxy_connect.so
By uncommenting them (remove the #), then save the file
12

---

• #LoadModule proxy_module modules/mod_proxy.so
• The main proxy module for apache that manages connections and
redirects them
• #LoadModule proxy_http_module modules/mod_proxy_http.so
• The module that implement proxy features for HTTP and HTTPS
protocols
• #LoadModule proxy_connect_module modules/mod_proxy_connect.so
• This module is used for SSL tunnelling
13

---

Now, you need to open the httpd_vhosts.conf file from inside extra
folder inside the conf directory. The file has many configurations. Now
to make the configuration working with the file, add the following lines
to the end of the file to make the forward proxy working with apache:
- Create a virtual host for all hosts and ports
- Add two flags ProxyRequest and ProxyVia and set them “On”
<virtualHost *:*>
ProxyRequest On
ProxyVia On
</virtualHost>
14

---

- Start Apache server
- Go to internet options to provide proxy server
address so that each request from your
system should use the apache proxy server
Go to the browser :
- Settings ->internet options ->
connections -> LAN settings ->
- select check box for proxy server ->
- provide the address as
“localhost” and
- the port as 80
-> ok
15

---

- Go to any browser,
- visit some websites
- Open access.log file from log directory
You will be able to see log of you visited pages.
So if you are trying to access any site, the HTTP
request is going through Apache server.
Apache server is acting as forward proxy server
16

---

▪ Proxy means the authority to act on behalf of someone else.
▪ Forward proxies are crucial for privacy and security when browsing
the internet, accessing geo-restricted content, web scraping, and
much more. Reverse proxies are important for websites with many
visitors daily because they help avoid overloading and are a perfect
fit for caching content, SSL encryption.
17

---


---


# Chapter 7: Reverse Proxy Server

Web Administration – FWD 213

---

Apache HTTP Server can be configured in both a
forward and reverse proxy (also known as gateway)
mode.
A reverse proxy (or gateway), appears to the client
just like an ordinary web server. No special
configuration on the client is necessary. The client
makes ordinary requests for content in the
namespace of the reverse proxy.
2

---

The reverse proxy then decides where to send those requests and
returns the content as if it were itself the origin.
A typical usage of a reverse proxy is to:
provide Internet users access to a server that is behind a firewall.
1.
Reverse proxies can also be used to balance load among several
2.
back-end servers
or to provide caching for a slower back-end server.
3.
In addition, reverse proxies can be used simply to bring several
4.
servers into the same URL space.
3

---

4

---

This allows or prevents Apache httpd from functioning
as a forward proxy server. In a typical reverse proxy or
gateway configuration, this option should be set to Off.
In order to get the functionality of proxying HTTP or FTP
sites, you need also:
- MOD PROXY HTTP
- MOD PROXY FTP
(or both) present in the server.
! Warning
Do not enable proxying with PROXYREQUESTS until you
have secured your server.
5

---

A reverse proxy is activated using the PROXYPASS directive or the [P] flag to
the REWRITERULE directive. It is not necessary to turn PROXYREQUESTS on
in order to configure a reverse proxy.
This directive allows remote servers to be mapped into the space of the
local server. The local server does not act as a proxy in the conventional
sense but appears to be a mirror of the remote server. The local server is
often called a reverse proxy or gateway. The path is the name of a local
virtual path; url is a partial URL for the remote server and cannot include a
query string.
6

---

A Reverse Proxy server sits between origin servers and incoming traffic
requests for websites and applications, to ensure safety for public cloud
application security before forwarding the requests to the backend
server.
▪ It can easily handle both dynamic content and static content.
▪ A reverse proxy is like an endpoint that captures the first HTTP requests.
▪ It secures origin servers and data centres against DDoS attacks, for a
secure server and client communication.
▪ The HTTP request forwarding is smooth for a clean user experience
throughout.
7

---

▪ unlike a forward proxy that acts on behalf of clients, a reverse proxy server
resides in front of backend servers and transfers client requests to these
servers. Reverse proxies are generally employed to increase protection,
speed, and reliableness. A reverse proxy gets the request from a client, passes
it on to another server, and then forwards it back to the client, making it
appear as if the initial proxy server processed it. These proxies make sure that
users don’t reach the origin server directly, thus providing anonymity to this
web server.
▪ While being of no particular use to consumers and regular people, reverse
proxy servers are the perfect fit for service providers and websites that have
numerous visitors daily. These proxies can protect web servers, increase
website performance, and help avoid overloading. Reverse proxies are also
used for load balancing, caching, and SSL encryption.
8

---

➢By routing client traffic through a reverse proxy, admins can
simplify security administration. They can configure backend
servers to only accept traffic directly from the proxy and then
configure access control configurations on the proxy itself.
➢For example, admins can configure the reverse proxy’s firewall to
whitelist or blacklist specific IP addresses. All existing servers
behind the proxy will be protected accordingly, and whenever
admins add a new backend server to the network that is
configured to only accept requests from the proxy server, the new
backend server is protected according to the proxy configuration.
9

---

➢Using a reverse proxy can also allow administrators to easily swap
backend servers in and out without disrupting traffic. Because
clients interact directly with the proxy, they only need to know its
hostname and don't need to worry about changes to the backend
network topology.
➢In addition to simplifying client configuration, an admin can
configure a reverse proxy to load-balance traffic so that requests
can be more evenly distributed to the backend servers and improve
overall performance.
10

---

In their functionality, all reverse proxies are more or less the same.
However, we can distinguish two main types of reverse proxies
based on their features. They are regular reverse proxies and load
balancers.
Regular reverse proxies. This proxy type intercepts the request
1.
from a client, directs it to the server to process it, and then sends
it back to the client. This proxy type is mainly used for security
purposes.
11

---

Load balancers. This proxy is a reverse proxy subtype
2.
that leads to multiple backend instances instead of one.
It is capable of distributing the traffic among multiple
other servers and managing client-server
communication between all of them. This type is more
specifically tailored to distribute the load evenly among
different servers, thus increasing the speed and
performance.
12

---

▪ Websites and service providers may use reverse
proxies for different reasons, and here are some of
them:
1. Load balancing. Frequently visited websites may
sometimes need reverse proxy servers to deal
with the flow of incoming traffic. Instead of
handling it on its own, a popular site may
distribute the traffic between multiple back-end
servers and thus enhancement its capacity for
handling many requests. If one of the servers is
overloaded and out of order, the traffic can be
redirected to other online servers keeping the web
page running. The website engineers may even
add more back-end servers to this load balancer
to increase capacity and meet rising demand for
performance.
13

---

Caching. A reverse proxy is capable of caching data that is
2.
commonly requested. Businesses that store a lot of pictures and
videos may also speed up the performance of their websites by
caching this content and reducing the load on the internet
servers.
14

---

Anonymity and security. Since reverse proxies
3.
intercept all the incoming requests, they serve
as an additional level of protection for backend
servers. It helps prevent any malicious actors
from abusing web servers by blocking suspicious
traffic from specific IP addresses.
15

---

Enable Apache Modules for Reverse Proxy:
To use reverse proxy with Apache Web Server you need to enable specific
Apache modules to support additional functionality that is required for
reverse proxy servers. We will need the following modules for our scenario:
1. mod_proxy: It is the main proxy module for Apache used to manage
connections and redirect them. It allows Apache to act as a gateway to
underlying back-end servers. This module is mandatory for all reverse
proxy scenarios.
2. mod_proxy_http: This module depends on mod_proxy and is required to
support HTTP and HTTPS requests for a proxy server.
3. mod_ssl: The module provides SSL v3 and TLS v1.x protocol support for
the Apache HTTP server.
16

---

▪ The ProxyPass directive specifies the mapping of incoming requests to the backend server (or a
cluster of servers known as a Balancer group). The simplest example proxies all requests ("/") to a
single backend:
ProxyPass "/" "http://www.example.com/"
▪ To ensure that and Location: headers generated from the backend are modified to point to the
reverse proxy, instead of back to itself, the ProxyPassReverse directive is most often required:
ProxyPass "/" "http://www.example.com/"
ProxyPassReverse "/" "http://www.example.com/"
▪ Only specific URIs can be proxied, as shown in this example:
ProxyPass "/images" "http://www.example.com/"
ProxyPassReverse "/images" "http://www.example.com/"
▪ In the above, any requests which start with the /images path with be proxied to the specified
backend, otherwise it will be handled locally. 17

---

Now, you need to open the httpd_vhosts.conf file from inside extra folder inside the
conf directory. The file has many configurations. Now to make the configuration
working with the file, add the following lines to the end of the file to make the
forward proxy working with apache :
- Create a virtual host for all hosts and ports
- Add configuration for reverse proxy server
ProxyPreverseveHost flag, and ProxyPass with path
You can add ProxyPass and ProxyPassReverse for any virtual host on your system
<virtualHost *:*>
ProxyPreserveHost On
ProxyPass /web1 http://localhost:8081/
ProxyPassReverse /web1 http://localhost:8081/
ServerName localhost
<virtualHost>
18

---

Hitting web1 you should be able to access the first java server that is
running on 8081, and using any other path, you will be able to access
the java server running on the specified path (if any)
Restart the Apache server
19

---

▪ The key difference between a forward proxy and
a reverse proxy is that the first one is used by a
client, e.g., a user inside a private network, while
the second one is used by an internet server.
▪ A forward proxy can be positioned in the private
network together with the user, or it can be online.
▪ Forward proxies are used for privacy reasons,
accessing geo-restricted content, web scraping, and
much more. Web servers use reverse proxies to:
▪ avoid overloading,
▪ add additional safety layers from malicious entities,
caching,
▪ SSL encryption, etc.
Therefore, these proxies are used for entirely
different tasks, which is the main difference between
them.
20

---

▪ The main difference between a forward proxy and reverse proxy is
in their purpose. As they are utilized for different tasks, they
cannot be considered as the same proxies. In forward proxy, the
server doesn’t know who the client is, while in the reverse proxy,
the client doesn’t know which server is connecting to
21

---


---


# Chapter 8: Display Server Statistics

1
Web Administration – FWD 213

---

Status module allows server administrator to find out how
well their server is performing. An HTML page present the
current server statistics in an easily readable form. If
required, this page can be made to automatically refresh.
Another page gives a simple machine-readable list of the
current server state
Description: Provides information on server activity and performance
Status: Base
Module Identifier: status_module
Source File: mod_status.c
2

---

The mod_status is an Apache module that helps to monitor
▪
web server load and current httpd connections with an
HTML interface that can be accessed via a web browser.
The mod_status module provides an easy way to access
▪
server statistics.
It generates a server status report, allowing administrators to
▪
monitor server activity.
To install mod_status, ensure the module is loaded in the
▪
Apache configuration file by including the line :
LoadModule status_module modules/mod_status.so
3

---

Apache’s mod_status shows a plain HTML page containing the information
about current statistics of the webserver including:
❑Total number of incoming requests
❑Total number of bytes and counts server
❑The CPU usage of Webserver
❑Server Load
❑Server Uptime
❑Total Traffic
❑Total number of idle workers
❑PIDs with the respective clients and many more.
The default Apache Project enabled their server statistics page to the general
4
public.

---

The default Apache installation comes with mod_status enabled. If
not, make sure to enable it in the Apache configuration file.
To enable mod_status, configure the <Location> section in the
Apache configuration file httpd.conf as shown below:
This configuration allows access to the server status page from the
localhost.
5

---

▪After enabling mod_status,
you can access the server
statistics through a web
browser by visiting
http://localhost/server-status
6

---

▪ you can also access
the server statistics
through the
command:
Apahe2ctl status
7

---

▪ The server status page
provides an overview
of the server's
performance,
including current
time, restart time,
server uptime, total
accesses, and total
traffic.
▪ These metrics help in
understanding the
server's overall health
and performance.
8

---

▪ Monitoring CPU usage
helps identify
performance bottlenecks.
▪ The mod_status report
includes CPU load and
CPU usage information,
which can be used to
determine if the server is
under heavy load or if
adjustments to the
configuration are needed.
9

---

▪ The mod_status report
also provides
information about
requests per second,
bytes per second, and
bytes per request.
▪ These metrics can help
you identify patterns
and optimize your
server configuration to
handle more requests
efficiently.
10

---

▪ To enable extended
server statistics,
include
ExtendedStatus On in
the Apache
configuration file.
▪ Extended server
statistics provide more
detailed information
about the server's
performance, such as
the scoreboard (server
activity in a structure)
and connection details.
11

---

▪ The scoreboard section in the extended server
statistics provides a breakdown of worker statuses
and detailed connection information for each
worker.
▪ This information can be used to understand the
server's performance and identify any bottlenecks
or issues that need to be addressed.
▪ Note: The term “Apache worker” refers to a
process or a thread, depending on the Multi-
Processing Module (MPM) used, that handles the
requests coming to an Apache server.
12

---

Invoking the Apache scoreboard is simple, simply by running the
following command:
apachectl status
This will display output similar to the image:
Each of the characters in this output has a different meaning:
▪ _ — The server is waiting for the connection.
▪ S — The server is starting.
▪ R — The server is reading the request.
▪ W — The server is sending a reply.
▪ K — The server is in keep-alive (read) mode.
▪ D — The server received a DNS request.
▪ C — The server is closing the connection.
▪ I — Idle worker cleanup.
▪ . — Idle worker.
▪ Understanding this will help you troubleshoot the issues that
13
you may be experiencing

---

Understanding previous slide will help you troubleshoot the issues that you
may be experiencing.
▪ For example, a scoreboard that displays a large amount of "W" status, may
indicate a poorly performing web application such as a PHP website.
Alternatively, if this coincides with a large number of traffic spikes, it may be a
result of an attack (DoS).
▪ Similarly, many requests stuck in "R" can be an indication of an attacked
known as Slowloris, in which many connections are opened and kept open for
as long as possible.
If you suspect your server to be undergoing an attack it is recommended that you
contact your service provider/data host for assistance in mitigating the effects.
14

---

▪ apachetop is a command-line tool that provides
real-time monitoring of Apache server statistics.
Install it using
sudo apt install apachetop
▪ and run it with
apachetop -f /var/log/apache2/access.log
15

---

16

---

▪ Server logs are essential for understanding server
performance.
▪ Server log: is a text document that contains a
record of all activity related to a specific web
server over a defined period of time
▪ Access logs and error logs: provide insights into
server activity and can be used to identify issues or
opportunities for optimization.
▪ Access log gathers data related to the files
requested from the server
▪ Error log tracks all failed requests for the server
▪ Logs are typically located in the directory:
/var/log/apache2
17

---

Use the following command:
tail -f /var/log/apache2/access.log
or
tail -f /var/log/apache2/error.log
to monitor logs in real-time.
You can also filter logs using grep, for example:
tail -f /var/log/apache2/access.log | grep "GET /index.php".
Grep (global regular expression print) is a small family of commands that search input files
for a search string and print the lines that match it. Although this may not seem like a terribly
useful command at first, grep is considered one of the most useful commands in any Unix
system.
Tail is a command being executed on the output of the grep command and so will
print the last 4 lines of the output of grep
18

---

19

---

▪ goaccess is a command-line tool that provides an interactive and
visually appealing report of server statistics.
▪ Install it on Unix Ubuntu with the command:
sudo apt install goaccess
and run it with
goaccess /var/log/apache2/access.log -a
20

---

21

---

▪ Regularly monitoring server statistics helps
identify areas for optimization, such as worker
processes, memory usage, and caching. Addressing
these areas can improve the server's performance
and ensure a better experience for users.
▪ Optimizing Apache server performance is crucial
for providing the best possible experience to users
and ensuring that resources are utilized efficiently.
Following are some key areas to focus on when
optimizing Apache server performance.
22

---

KeepAlive allows multiple requests to be
served over a single connection, reducing
server overhead and improving
performance.
Enable KeepAlive by setting KeepAlive On
▪
in the Apache configuration file.
Configure the KeepAliveTimeout and
▪
MaxKeepAliveRequests settings to optimize
the balance between server performance and
resource consumption.
23

---

▪ Caching can significantly improve server performance by storing
static content and serving it to clients without reprocessing.
▪ Enable and configure:
▪ mod_cache,
▪ mod_cache_disk,
▪ or mod_mem_cache
to take advantage of caching capabilities.
▪ Set appropriate cache expiration times and cache-control headers
to ensure that clients receive updated content when necessary.
24

---

Compressing responses can reduce the amount of data
▪
transferred between the server and clients, improving
performance and reducing load times.
Enable the:
▪
▪ mod_deflate module
to compress responses before they are sent to clients.
Configure compression settings, such as the types of files to
▪
compress and the compression level, to optimize performance.
25

---

A reverse proxy can improve server
▪
performance and security by handling
requests on behalf of the Apache
server.
Configure
▪
mod_proxy
▪
to set up a reverse proxy, which can
help distribute the load and manage
connections more efficiently.
26

---

27

---
