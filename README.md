# CS50W Project 2

## Web Programming with Python and JavaScript

### https://courses.edx.org/courses/course-v1:HarvardX+CS50W+Web/course/

## Login

<!-- ![](https://i.imgur.com/veUhsDb.png) -->
<img src="https://i.imgur.com/veUhsDb.png" width="800">

## Home

<!-- ![](https://i.imgur.com/iZhNWMP.png) -->
<img src="https://i.imgur.com/iZhNWMP.png" width="800">

## Chat (Not the best UI)

<!-- ![](https://i.imgur.com/iKhYyzA.png) -->
<img src="https://i.imgur.com/iKhYyzA.png" width="800">

## Usage

-   Choose a username
-   Create a new channel or select an existent one
-   Start chatting!

## :gear: Setup

```bash
# Clone repo
$ git clone https://github.com/marcorichetta/cs50w-project2.git

$ cd cs50-project2

# Create a virtualenv (Optional but reccomended)
$ python3 -m venv myvirtualenv

# Activate the virtualenv
$ source myvirtualenv/bin/activate (Linux)

# Install all dependencies
$ pip install -r requirements.txt

# Run
$ flask run

# Go to 127.0.0.1:5000 on your web browser.
```

## :page_facing_up: Messages storing example

```python
In [1]: channellsMessages = dict()

In [2]: msg1 = {
   ...: 'message': 'hi',
   ...: 'user': 'marco',
   ...: 'time': '12/23/34 00:00'
   ...: }

In [3]: channellsMessages['room1'] = [msg1]

In [4]: channellsMessages
Out[4]: {'room1': [{'message': 'hi', 'user': 'marco', 'time': '12/23/34 00:00'}]}

In [5]: msg2 = {
   ...: 'message': 'Hello',
   ...: 'user': 'rick',
   ...: 'time': '12/23/34 10:00'
   ...: }

In [6]: channellsMessages['room1']
Out[6]: [{'message': 'hi', 'user': 'marco', 'time': '12/23/34 00:00'}]

In [7]: channellsMessages['room1'].append(msg2)

In [8]: channellsMessages['room1']
Out[8]: [{'message': 'hi', 'user': 'marco', 'time': '12/23/34 00:00'},
 {'message': 'Hello', 'user': 'rick', 'time': '12/23/34 10:00'}]

```
