#Tournament
========

This project sets up a Swiss-Style tournament. This is the final project for the Udacity Relational Databases course. 

###Technology
----------
* Python 2.7.10
    * Special modules:
    * psycopg2
* PSQL
* Oracle VM VirtualBox 5.0.4
* Vagrant 1.7.4


###Directory Structure
----------------------
```
+---Tournament
    +---README.md
    +---tournement.py
    +---tournament_test.py
    +---tournament.sql
```

###To Begin
--------
1. Follow the instructions found [here][1] to install **VirtualBox** and **Vagrant**.
1. Clone the Github repository [here][4].
1. Navigate to **fullstack/vagrant/tournament**
    1. Open **psql** with the following command:
    1. Import **tournament.sql** with the following command:
        * $`\i tournament.sql`
    1. Then quit **psql** with the following command:
        * $`\q`
    1. Run **tournament_test.py** with the following command:
        * $`python tournament_test.py`


###Support/Contact
----------
If you are having issues, please let me know. Contributions, tips and comments are welcome!
* Email: robertkohl125@gmail.com
* [Github Profile][5]
* [StackOverflow Profile][6]
* [LinkedIn Profile][7]

###License
----------
The MIT License (MIT)

Copyright (c) [2015] [Robert Kohl]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[1]: https://docs.google.com/document/d/16IgOm4XprTaKxAa8w02y028oBECOoB1EI1ReddADEeY/pub?embedded=true "Google Doc"
[4]: https://github.com/robertkohl125/Tournament.git "Github repository"
[5]: https://github.com/robertkohl125 "Github Profile"
[6]: http://stackoverflow.com/users/2180707/robertkohl125?tab=profile "Stack Overflow Profile"
[7]: https://www.linkedin.com/in/robertkohl125 "LinkedIn"