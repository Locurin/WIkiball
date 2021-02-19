# Wikiball - Markdown encyclopedia app

Wikiball's execution example available at https://wikiball.pythonanywhere.com/

## Table of contents

*[General info](#general-info)

*[implementation](#implementation)

*[Technologies](#technologies)

*[functionalities](#functionalities)

*[version](#version)

*[credits](#credits)


## General info

Wikiball is a [Wikipedia](https://es.wikipedia.org/)-inspired open source project for easy community-building of encyclopedias or simple text databases for any particular topic. It's based in [Markdown](https://es.wikipedia.org/wiki/Markdown) language on which new entries or articles as posted on a user-friendly, easy, professional format. Its minimalistic design only takes text and links as input (not images or any kind of media) as its true purpose remain: being easy-access, light, and simple. Wikiball app was though not for long, indeep articles, but for short and specific entries, being useful, for example a gadget's user manual, school projects or a restaurant's private recipe book.

Wikiball is fully responsive, working both in mobile and desktop. It displays an navbar where users can easily navigate thru all its functionalities.



## Implementation 

Wikiball is an open source project, so everyone interesed can download all its features from Github [here](https://github.com/Locurin/Wikiball). The same way, users are invited to improve its features or fully customize its look with HTML/CSS to fit their needs for implementation. Wikiball is built using Python's framework Django. 

*To learn how to deploy your costume version of the app into the web visit [Django Docs regarding the issue](https://docs.djangoproject.com/en/3.1/howto/deployment/).
*REMEMBER: go to **settings.py** >> and add the following line ```ALLOWED_HOSTS = ['<web_host_name>']``` to said file to allow our chosen host so it can run our code.
*REMEMBER: All urls in **views.py** may need to be changed according the implementation the user decide to use to match correct paths of the host. 



## Technologies

*[Bootstrap](https://getbootstrap.com/) v.5-0.0-beta2

*[Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) 

*[Django](https://www.djangoproject.com/) v.3.1.6

*[Python](https://www.python.org/) v.3.9.1



## Scope of Functionalities

### Index

Presents user with lastest added articles to the encyclopedia and presents all the main functionalities.

### Articles

User can access a full list of every article uploaded in alphabetical order. When clicking an article title user will be redirected to it, where it can be read and edited aswell. 

### Search

Allows users to look for specific entries. If no article matches the query input by user, the app will present a list of possible articles that partialy match said query.

### New entry

Displays a [Textarea](https://www.w3schools.com/tags/tag_textarea.asp) field where new article can be written using Markdown syntax. Also provides another field for article's title (if said title was previously assigned to another article the app will display an error message). After hitting submit button user will be redirected to the new article's page.

### Edit 

Users can edit articles in any given time by pressing the "edit" button in the entry's page. It will display a Textarea field that works exactly like the one in [New Entry](#new-entry). After hitting submit button user will be redirected to the article's page with its content edited.

### Random

When pressed, this button will redirect user to any random article to look for it.



##  Version

This is version 1 of Wikiball, uploaded to Github in february 2021. Future versions will feature sessions and storage for user data an information, aswell as new articles submitted or edits.



## Credits

This project was built by [Locurin](https://github.com/Locurin) for Github as a personal project. You can also contact me at **matiasfefernandez95@gmail.com**. 

