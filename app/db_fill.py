# -*- coding: utf-8 -*-

from app import app, db
from app.models import User, Book, Log, Role

app_ctx = app.app_context()
app_ctx.push()
db.create_all()
Role.insert_roles()

admin = User(name=u'root', email='root@gmail.com', password='password', major='administrator',
             headline=u"One temporary administrator", about_me=u"Graduated from the Department of Management and likes to read, so part-time librarian.")
admin2 = User(name=u'root2', email='root2@gmail.com', password='password', major='administrator',
             headline=u"One temporary administrator", about_me=u"Graduated from the Department of Management and likes to read, so part-time librarian.")
user1 = User(name=u'daday', email='graak82@test.com', password='123456', major='Computer Science', headline=u"Ordinary student")
user2 = User(name=u'test', email='test@test.com', password='123456')
user3 = User(name=u'one', email='xiaoming@163.com', password='123456')
user4 = User(name=u'two', email='lihua@yahoo.com', password='123456')

book1 = Book(title=u"Flask Web Development", subtitle=u"Python-based web application development framework ", author=u"Miguel Grinberg", isbn='9787115373991',
             tags_string=u"Computer, program design, web development ", image='http://img3.douban.com/lpic/s27906700.jpg',
             summary=u"""
# This book is not only suitable for primary web developers to learn to learn, but also the excellent reference book for Python programmers to learn advanced web development technology. 
* Learn the basic structure of the Flask application, write example applications; * Use the necessary components, including templates, databases, web forms, and email support; * Use the package and modules to build scalable large applications; * Implement user authentication, role, and personal information; * Reuse templates in blog sites, page display lists, and use rich text; * Use Flask-based REST API to implement available features on smartphones, tablets, and other third-party clients; * Learn run unit testing and improve performance; * Deploy web applications to the production server. """)
book2 = Book(title=u"STL source code analysis ", subtitle=u" ", author=u"Hou Jie ", isbn='9787560926995',
             tags_string=u"Computer, program design, C ++ ", image='http://img3.doubanio.com/lpic/s1092076.jpg',
             summary=u"""* People who learn programming know that reading, profiling is a shortcut to improve the level. Before the source code, there is no secret. Masters' calm thinking, empirical crystallization, technical ideas, unique style, all original original this is in the source code. * The source code presented in this book makes the reader to see the realization of the VECTOR, the implementation of the List, the implementation of the Heap, the implementation of the demary, the implementation of the Red Black Tree, the implementation of Hash Table, SET /Implementation of MAP; see the implementation of various algorithms (sort, lookup, arrangement combination, data movement and replication technology); even can see the implementation of the underlying Memory Pool and high-order abstract traits mechanism. """)
book3 = Book(title=u"Compilation principle (original book 2) ", subtitle=u"Principle, technology and tools ",
             author="Alfred V. Aho / Monica S.Lam / Ravi Sethi / Jeffrey D. Ullman ", isbn="9787111251217",
             tags_string=u"Computer, compilation principle ", image='http://img3.douban.com/lpic/s3392161.jpg',
             summary=u"""* This book is comprehensive and deeply explored important topics in compiler design, including lexical analysis, gramatic analysis, grammar guidance and grammatical translation, runtime environment, target code generation, code optimization technology, parallelism detection, and process Analyze technology and give a large number of examples in related chapters. Compared with the previous version, this book has been amended to cover the latest developments in compiler development. A large number of systems and references are available in each chapter. * This book is a classic textbook in compilation principle, rich in content, suitable for teaching materials for compilation of undergraduate students and graduate students in higher institutions, and is also an excellent reference book for special technicians. """)
book4 = Book(title=u"In-depth understanding of computer system ", author="Randal E.Bryant / David O'Hallaron", isbn="9787111321330",
             tags_string=u"Computer, computer system ", image='http://img3.douban.com/lpic/s4510534.jpg',
             summary=u"""* This book describes the essential concept of computer systems from programmers, and demonstrates how these concepts actually affect the correctness, performance and practicality of the application. The book is 12 chapters, main contents include information representation and processing, program machine-level representation, processor architecture, optimization program performance, memory hierarchical, link, exception control flow, virtual memory, system level I /O, network programming, concurrent programming, etc. A large number of examples and exercises are provided in the book, and some answers are given to help readers to deepen the understanding of the concepts and knowledge of the body. * The biggest advantage of this book is to describe the implementation details of the computer system to help them construct a layered computer system in the brain, from the most underlying data to the configuration of the pipeline instruction, to the virtual memory, To the compilation system, to a dynamic load library, to the final user state application. How to map to the system by mastering the program, as well as how the program is executed, the reader can better understand why the program is like this, and how the efficiency is caused. * This book is suitable for programmers who want to write faster, more reliable procedures, and are also suitable as teaching materials for undergraduate students and related majors in higher institutions. """)
book5 = Book(title=u"C # in the husk ", subtitle=u"C # 5.0 Authoritative Guide ", author=u"Aba Harry (Joseph Albahari) / Aba Harry (Ben Albahari)",
             isbn="9787517010845", tags_string=u"Computer, program design, c # ", image='http://img3.douban.com/lpic/s28152290.jpg',
             summary=u"""* "C # - C # 5.0 Authoritative Guide in the Case" is a C # 5.0 authoritative technical guide, and the first Chinese version C # 5.0 learning information. This book uses the content, system, comprehensive and meticulous command, syntax and usage of the C # 5.0 from the basics to the content, system, comprehensive and meticulousness. The book's explanation is in-depth, and it is specifically designed for every knowledge point, which can help readers accurately understand the meaning of knowledge points and quickly learn. Compared with the previous C # 4.0 version, it has also added a rich concurrent, asynchronous, dynamic programming, code refinement, security, and COM interaction. * "C # - C # 5.0 authority in the husk" also fusures the author's many years of research and practice experience in software development and C #, which is very suitable as a self-study tutorial for C # technology, is also a copy Middle-level C # technicians are a must-have tool book. """)
book6 = Book(title=u"Algorithm introduction (original book 2) ",
             author="Thomas H.Cormen / Charles E.Leiserson / Ronald L.Rivest / Clifford Stein",
             isbn="9787111187776", tags_string=u"Computer, algorithm ", image='http://img3.doubanio.com/lpic/s1959967.jpg',
             summary=u"This book is in-depth and comprehensive introduction to computer algorithms. Analysis of each algorithm is both easy to understand and very interesting, and maintains mathematical stringency. The design objectives of this book are suitable for use in a variety of purposes. The content covered is: the role of the algorithm in the calculation, probability analysis, and introduction of random algorithms. The book is specifically discussed, and the approximate algorithm of two applications, randomized and linear planning techniques of dynamic planning, etc., as well as the score-seeking method and the desired linear time order statistical algorithm for recreation, rapid sorting. And discussions on greedy algorithm elements. This book also introduces the proven of the correctness of strong connecting sub-graph algorithms, the certificate of NP completeness of the Hamilton loop and subsequent NP completeness. The whole book provides more than 900 exercises and thinking questions and a more detailed example study. ")
logs = [Log(user1, book2), Log(user1, book3), Log(user1, book4), Log(user1, book6),
        Log(user2, book1), Log(user2, book3), Log(user2, book5),
        Log(user3, book2), Log(user3, book5)]

db.session.add_all([admin, user1, user2, user3, user4, book1, book2, book3, book4, book5, book6] + logs)
db.session.commit()

app_ctx.pop()
