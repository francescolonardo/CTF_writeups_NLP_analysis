**VULNERABILITY_TYPE**:
    - *Injection*: SQL, NoSQL, OS command, or LDAP injection vulnerabilities.
    - *Broken Authentication*: Weak or compromised authentication mechanisms.
    - *Sensitive Data Exposure*: Unprotected sensitive data (e.g., encryption keys, user data).
    - *XML External Entities (XXE)*: Exploits involving external XML entities.
    - *Broken Access Control*: Inadequate access restrictions (e.g., privilege escalation, insecure object references).
    - *Security Misconfigurations*: Insecure default configurations or incomplete security settings.
    - *Cross-Site Scripting (XSS)*: Reflected, stored, or DOM-based XSS vulnerabilities.
    - *Insecure Deserialization*: Vulnerabilities related to unsafe deserialization of objects.
    - *Using Components with Known Vulnerabilities*: Exploiting outdated or vulnerable components.
    - *Insufficient Logging and Monitoring*: Poor logging or monitoring enabling further attacks.
    - *Remote Code Execution (RCE)*: Exploiting a vulnerability to execute arbitrary code remotely.
    - *Directory Traversal*: Accessing restricted directories by manipulating file paths.

**ATTACK_TECHNIQUE**:
    - *Brute Force*: Attempting multiple combinations to guess passwords or encryption keys.
    - *Social Engineering*: Manipulating people to reveal sensitive information or perform actions.
    - *Phishing*: Fraudulent attempts to obtain sensitive information through deceptive communications.
    - *Man-in-the-Middle (MITM)*: Intercepting and altering communications between two parties.
    - *Password Spraying*: Attempting a few common passwords against multiple accounts.
    - *Credential Stuffing*: Automated injection of stolen credentials to gain unauthorized access.
    - *Denial of Service (DoS)*: Overwhelming a system to make it unavailable to users.
    - *Privilege Escalation*: Gaining elevated access to resources reserved for higher privilege levels.

**CODE_WEAKNESS**:
    - *Unsanitized Input*: Failing to sanitize, validate, or escape user inputs, leading to potential injection attacks.
    - *Insecure Defaults*: Using insecure settings or configurations by default, increasing the likelihood of vulnerabilities.
    - *Hardcoded Credentials*: Storing passwords, keys, or other sensitive data directly in the source code.
    - *Insufficient Error Handling*: Failing to handle errors or exceptions properly, potentially exposing sensitive information or causing application instability.
    - *Lack of Input Validation*: Not checking user inputs for correctness, type, or length, leading to potential security and stability issues.
    - *Improper Output Encoding*: Failing to properly escape or encode data before displaying it to users, leading to potential XSS attacks.
    - *Insecure Cryptography*: Using weak or outdated cryptographic algorithms, or implementing cryptography incorrectly.
    - *Race Conditions*: Failing to handle concurrent access to shared resources properly, leading to potential data corruption or other unintended behavior.
    - *Memory Leaks*: Failing to release allocated memory, causing resource exhaustion and potential denial of service.
    - *Lack of Code Reusability*: Writing duplicate code instead of reusing existing code, increasing the likelihood of introducing bugs and making maintenance more difficult.
    - *Poor Code Organization*: Failing to structure code in a modular and maintainable way, making it difficult to understand and modify.
    - *Lack of Comments and Documentation*: Not providing adequate comments or documentation, making it difficult for others to understand the code's purpose and functionality.
    - *Unoptimized Code*: Writing inefficient code that consumes excessive resources, degrading application performance.
    - *Insecure File and Resource Management*: Failing to properly manage access to files or resources, potentially leading to unauthorized access or data leaks.
    - *Inadequate Logging and Monitoring*: Not implementing sufficient logging or monitoring, making it difficult to detect and investigate security incidents or other issues.
    - *Failure to Update Dependencies*: Neglecting to keep software dependencies up to date, increasing the risk of using components with known vulnerabilities.

**TARGET_COMPONENT**:
    - *Functions*: Key web app functionalities (e.g., login, registration, file upload).
    - *Pages*: Distinct pages or sections (e.g., homepage, profile page, admin panel).
    - *Endpoints*: API endpoints, URLs, or resources targeted by attackers.
    - *Server Components*: Web servers, database servers, and caching systems (e.g., Apache, Nginx, MySQL, PostgreSQL, Memcached, Redis).
    - *Frameworks*: Web application frameworks and libraries (e.g., Django, Flask, Ruby on Rails, Express.js, Angular).
    - *External Services*: Third-party services or APIs (e.g., payment gateways, social media platforms, email services).
    - *Config Files*: Files with sensitive configuration data (e.g., .env, .htaccess, web.config).
    - *User Roles*: Web app user roles or privilege levels (e.g., administrator, moderator, regular user).
    - *Network Components*: Network devices or components in the app's infrastructure (e.g., routers, switches, firewalls).
    - *System Files/Directories*: Files, directories, or resources with potential sensitive data or unauthorized access risks.

**INFORMATION_LEAKED**:
    - *User Credentials*: Usernames, passwords, authentication tokens.
    - *Personal Information*: Names, addresses, emails, phone numbers, Social Security numbers.
    - *Financial Data*: Credit card numbers, bank account details, transaction records.
    - *System Configurations*: Configuration files, API keys, encryption keys, passwords.
    - *Application Source Code*: Unintended exposure of proprietary or sensitive code.
    - *Internal Communications*: Emails, chat logs, or other internal communication records.
    - *Infrastructure Details*: IP addresses, domain names, server configurations, network topology.

**ATTACK_VECTOR**:
    - *Payload*: Part of an exploit carrying out the intended malicious action.
    - *Exploit*: Code or software designed to exploit a vulnerability in a system or application.
    - *Shellcode*: Small code piece used as a payload in software vulnerability exploitation.
    - *Backdoor*: Hidden method to bypass authentication or security controls for unauthorized access.
    - *Rootkit*: Tools or software collection enabling an attacker to maintain unauthorized system access.
    - *RAT (Remote Access Trojan)*: Malware allowing an attacker to remotely control a compromised system.
    - *Keylogger*: Tool or software recording keystrokes to capture sensitive information (e.g., passwords, credit card numbers).
    - *Dropper*: Malware used to deliver and install other malicious software on a compromised system.
    - *Protocols*: Network protocols utilized during the attack (e.g., HTTP, HTTPS, FTP, SMTP, DNS).

**TOOL_USED**:
    - *Nmap*: Network scanner for discovering hosts and services.
    - *Wireshark*: Network protocol analyzer for capturing and analyzing network traffic.
    - *Burp Suite*: Web application security testing toolkit.
    - *Metasploit*: Exploitation framework for developing and executing exploit code.
    - *SQLMap*: Automatic SQL injection and database takeover tool.
    - *Nikto*: Web server scanner for identifying vulnerabilities and misconfigurations.
    - John the Ripper: Password cracking tool.
    - *Hydra*: Online password attack tool supporting various protocols.
    - *OWASP ZAP*: Open-source web application security scanner.
    - *Ghidra*: Software reverse engineering framework for analyzing compiled code.
    Command Line Commands:
    - *grep*: Search for specific patterns in files or output data.
    - *curl*: Transfer data to or from a server using various protocols (e.g., HTTP, FTP).
    - *wget*: Retrieve files from the web using HTTP, HTTPS, or FTP.
    - *nc (netcat)*: Networking utility for reading from and writing to network connections.
    - *navigational commands*: Commands for moving through the file system (e.g., cd, ls, pwd).
    - *file manipulation commands*: Commands for handling files and directories (e.g., cp, mv, rm, mkdir).
    - *system commands*: Commands for interacting with the operating system (e.g., ps, top, kill, uname).
    - *text processing commands*: Commands for processing and manipulating text files (e.g., awk, sed, sort, uniq).
    - *permissions commands*: Commands for managing file permissions and ownership (e.g., chmod, chown).
    - *archiving commands*: Commands for compressing and decompressing files (e.g., tar, gzip, bzip2, zip, unzip).

**SECURITY_MECHANISM**:
    - *Authentication*: Verifying user identity (e.g., multi-factor, single sign-on).
    - *Authorization*: Controlling access to resources based on user privileges.
    - *Encryption*: Protecting data confidentiality through cryptographic techniques.
    - *Input Validation*: Verifying and sanitizing user inputs to prevent injection attacks.
    - *Output Encoding*: Escaping and encoding output data to prevent XSS attacks.
    - *Intrusion Detection System (IDS)*: Detecting malicious activity within a network.
    - *Intrusion Prevention System (IPS)*: Detecting and preventing malicious activity in real-time.
    - *Firewall*: Restricting incoming and outgoing network traffic based on security rules.
    - *Security Headers*: Implementing HTTP response headers to enhance web application security.
    - *Logging and Monitoring*: Collecting and analyzing logs to detect and respond to security incidents.

**LEARNING_RESOURCE**:
    - *MDN Web Docs*: Comprehensive resource for web development documentation.
    - *W3Schools*: Online web tutorials and references for various web technologies.
    - *OWASP*: Open Web Application Security Project focusing on web application security.
    - *OWASP Top Ten*: List of the top 10 most critical web application security risks.
    - *OWASP Cheat Sheets*: Guides and best practices for secure web development.
    - *Stack Overflow*: Q&A platform for programmers to find solutions to coding problems.
    - *GitHub*: Web-based platform for version control, collaboration, and code hosting.
    - *PortSwigger Web Security Academy*: Online resource for learning web security through hands-on labs.
    - *HackerOne CTF Writeups*: Collection of writeups from Capture The Flag competitions.
    - *CTFtime Writeups*: Archive of CTF writeups and solutions.
    - *Google Developers*: Resources and tools for developers provided by Google.
    - *Microsoft Developer Network (MSDN)*: Microsoft's resource for developers.
    - *YouTube Tutorials*: Video tutorials on various programming and web development topics.
    - *Online Learning Platforms*: Websites offering courses on web development and security (e.g., Pluralsight, Coursera, Udemy, Udacity, edX, LinkedIn Learning, Codecademy, FreeCodeCamp).
    - *Medium Articles*: Blog posts and articles on web development and security topics.
    - *Infosec Blogs*: Blogs focused on information security and web application security.
    - *Documentation*: Official technical documentation, API documentation, whitepapers, and research papers.
    - *Online Forums*: Web forums, IRC channels, and Discord channels for discussing web development and security topics.
    - *Wikipedia*: Online encyclopedia with articles on various web technologies and concepts.

**ATTACKER_ACTION**:
    - *View*: Examining or viewing specific resources or data.
    - *Search*: Searching for specific information or vulnerabilities.
    - *Visit*: Accessing or navigating to a particular URL or resource.
    - *Assume*: Taking on a different role or identity (e.g., impersonation).
    - *Inspect*: Analyzing or investigating a specific component or part of the web application.
    - *Exploit*: Executing an attack to take advantage of a vulnerability.
    - *Exfiltrate*: Extracting or stealing sensitive data from the target system.
    - *Check*: Verifying the presence, correctness, or functionality of a specific component or feature.
    - *Notice*: Observing or discovering something important or relevant.
    - *Ensure*: Confirming or validating that a specific condition is met.
    - *Log*: Accessing or interacting with log files or logging functionality.
    - *Create*: Generating or producing a new resource or artifact.
    - *Upload*: Transferring a file or data to the target system or application.
    - *Test*: Assessing or evaluating a specific component, feature, or functionality.
    - *Encode*: Converting data into a different format or representation.
    - *Set up*: Configuring or preparing a specific component or environment.
    - *Pass*: Successfully overcoming a specific barrier or security measure.
    - *Identify*: Recognizing or pinpointing a specific component, feature, or vulnerability.

---

**ATTACKER_GOAL**:
    - *Access Sensitive Data*: Obtain unauthorized access to sensitive information.
    - *Escalate Privileges*: Gain higher-level access or control over the system.
    - *Execute Arbitrary Code*: Run attacker-controlled code on the target system.
    - *Deny Service*: Disrupt normal operations or make the system unavailable to users.
    - *Deface Website*: Modify the appearance or content of the web application.
    - *Maintain Persistence*: Retain unauthorized access to the target system over time.
> Example: "The challenge required us to gain administrator access..."
           {gain administrator access} -> [ATTACKER_GOAL: Escalate Privileges]

**DISCOVERY_METHOD**:
    - *Manual Analysis*: Investigating the application through manual testing and code review.
    - *Automated Scanning*: Using tools or scripts to scan the application for vulnerabilities.
    - *Fuzzing*: Sending malformed or unexpected input to find bugs or vulnerabilities.
    - *Reconnaissance*: Gathering information about the target through passive or active methods.
    - *Information Leakage*: Obtaining sensitive information from unintentional exposure.
    - *Reverse Engineering*: Analyzing compiled code or network traffic to understand the system's behavior.
> Example: "We started by manually inspecting the source code of the page..."
           {manually inspecting the source code} [DISCOVERY_METHOD: Manual Analysis]

**CVE_ID**: ?

**CWE_ID**: ?
