# Bank of Charles Rewards.

The application is a flask app, and is designed to be unzipped and run in your Kali vm.

To setup, and run the app. Open your terminal in the directory that you have unzipped this source code to, and run the following command `. run-app.sh`.

The application will start and serve a website on http://localhost:5000

You can visit this site, and use Burpsuite to investigate requests, etc.

Ensure you are not connected to the VPN when running this exam, as you need Internet.

# New Code Setup guide 


A batch file (‘setup_flask.bat’) is created to test the code in Windows Operating System, which mimics the ‘run-app.sh’ script.

To access admin previleges use the account with credentials ID:’7’ and password:’qwer’. Since the passwords are hashed, few account's created before introducing the hash feature cannot be accessed.

A .gitignore file is also used to ignore any unnecessary changes, like changes in ‘__pycache__’ directory. The changes to fix the vulnerabilities are not committed. So, if the code is viewed using Visual Studio code, the changes can be viewed easily similar to the picture below. The code is also commented for the required changes similarly.

For any queries, contact at s365442@students.cdu.edu.au (or) s364626@students.cdu.edu.au

# Vulnerability fixes

These are the key vulnerability recommendations and fixes done by Sabrina Doha (s365442) and Yuvanshankar Azhagumurugan (s364626).

- New table ‘admins’ should be created to maintain a list of administrators for accessing ‘/admin’ page. Moreover, added ‘Admin’ Button to the Navbar, only visible to admins, which is done by having a session value ‘admin’ which flags True if an admin logs in. 

- CSRF vulnerability is to be fixed by enabling CSRF feature for forms. 

- XSS vulnerability should be fixed by including a content-security-policy header to the code. 

- Information disclosure vulnerabilities are to be fixed by removing certain part of codes and parameters which leads to the disclosure when tampered with. 

- There should be a hashing technique included to hash passwords. 

- The access to deleted accounts should be rejected.  
