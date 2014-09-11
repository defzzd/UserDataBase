This app is written in Python 3.4 and runs on my laptop when the Django dev server is initiated with:

python manage.py runserver

from a shell when in the root directory.


Explanation of early submission:

I spent several days studying Django tutorials, but as soon as I realized how Django code interacted with HTML everything fell into place.
I ended up finishing all requested functionality of this program on Sunday the 7th (after which point I began work on the JS+HTML program, which I did last because I wanted to stay in a python mindset after having completed the Library challenge the first day).

The reason I have not yet submitted the app on Heroku is because I've been working on figuring out how Heroku works since Tuesday the 9th. I've narrowed the problem down to activating a dyno after setting up the proper requirements.txt and a Procfile. I have chosen to rename my current versions of these two files because they interfere with the app's proper functioning in its current, not-yet-debugged state.

After discussing this issue with Lindy I've decided to submit my three programming question responses in their current state, because they all work on my computer and to my knowledge they will work on other computers using Django 1.7 and Python 3.4. Current state details:

- The Library program works on repl.it and can be found at: http://repl.it/YaS
-- as well as: https://github.com/defzzd/Library

- The Todo list works on my computer but NOT on jsfiddle, and I have not yet been able to determine why.
It can be found at: http://jsfiddle.net/Ldzr5dLn/
-- and also at: https://github.com/defzzd/TodoList

- The Django user database works on my computer but I have not yet succeeded at enabling it on Heroku. My current attempt, which is probably still an error page, can be found at:http://udb.herokuapp.com/
-- and the github page: https://github.com/defzzd/UserDataBase