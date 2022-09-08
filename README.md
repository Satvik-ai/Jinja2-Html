### About Project 

This is a skill demonstration project. 

Jinja is a fast, expressive, extensible templating engine. Special placeholders in the template allow writing code similar to 
Python syntax. Then the template is passed data to render the final document.


In this project, I have built an application which renders html file using jinja 2. 
It helps to separate code from content. Code structure has been written on templates file. 
Code structure has many placeholders and jinja2 will pouplate this placeholders with the data
and render the html page. If we want to generate new html page with same structure but with different data, then we can very
easily do it by using jinja2 without writing code from scratch. We just have to pass the template and data to jinja2 templating
engine as shown in the project. 

### How To Run

Open a terminal in the project root directory and run the following commands 

1. Install `virtualenv`:
```
$ pip install virtualenv
```

2. Create virtual environment:
```
$ virtualenv env
```

3. Then run the command:
```
$ .\env\Scripts\activate
```

4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

5. Finally start the web server:
```
$ (env) python app.py
```