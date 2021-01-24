<h1 align="left">Leech - Instagram Bot</h1>
<h4 align="left">Tooling that automates your social media interactions to “farm” Likes, Comments, and Followers on Instagram Implemented in Python using the Selenium module.</h4>

<p align="center">
  <a href="https://github.com/mariuszmalek/leech">
    <img src="https://raw.githubusercontent.com/mariuszmalek/leech/main/img/logo.png" alt="Instagram Bot" width="300">
  </a>
</p>

## :books: Documentation

## Introduction
**Tooling that automates your social media interactions to “farm” Likes, Comments, and Followers on Instagram Implemented in Python using the Selenium Framework.**

## Features
  :heavy_check_mark: **Download all posts of a single user**  
  :heavy_check_mark: **Like or unlike all posts of a single user**  
  :heavy_check_mark: **Bulk unfollow**  
  :heavy_check_mark: **Bulk comments on a single post**  
  :heavy_check_mark: **Bulk unfollow all users that do not follow back**  
  :heavy_check_mark: **Delete messages in bulk**  
  :heavy_check_mark: **Download highlighted stories**  
  :heavy_check_mark: **Download stories**  
  :heavy_check_mark: **Download a single post**  
  :heavy_check_mark: **Download an IG TV Video**  
  :heavy_check_mark: **Follow all the followers of a single user**  
  :heavy_check_mark: **Follow all listed users in a file**  
  :heavy_check_mark: **Follow all users that have liked a single post**  
  :heavy_check_mark: **Follow users based on tag**  
  :heavy_check_mark: **Like posts based on tag**  
  :heavy_check_mark: **Like or unlike a single post**  
  :heavy_check_mark: **Comment on a single post**  
  :heavy_check_mark: **Follow or unfollow a user**  
  :heavy_check_mark: **Block or unblock a user**  


## Other Features
  :heavy_check_mark: Support for two languages: English and Polish.  
  :heavy_check_mark: Option of running browser window in normal or incognito modes has been granted.  
  :heavy_check_mark: A settings menu has been included. Settings menu features language and browser settings.  


## Details

:large_blue_diamond:	 You may use the features above by logging into your Instagram account.  
:large_blue_diamond:	 Instagram login for accounts with 2-factor authentication is also possible.  
:large_blue_diamond:	 As the project is currently under development, the 2-factor authentication feature has been set to assume that the 2Fa code is sent to the user's phone number.  
:large_blue_diamond:	 Default language has been set as English.  

## Configuration Settings
 :gear:	 Project utilizes Firefox browser as webdriver. This requires Firefox to be installed for the application to work properly.  
 :gear:	 In order to use Firefox [webdriver](https://github.com/mozilla/geckodriver/releases) needs to be downloaded and the directory path for the downloaded webdriver needs to be set within [config.json](https://github.com/mariuszmalek/leech/blob/master/config.json).  


* ### Config Options

:gear: **driver_path:** Denotes the Webdriver directory path.  
:gear: **headless:** Denotes if the browser is visible or not. Default value:**true**  
:gear: **language:** Denotes the language of the application.  
:gear: **languages:** Includes the settings, menu and warning messages for all language options.  
:gear: **time:** denotes the operation waiting times for all the  operations where **time.sleep()** has been used.  



* ### Package installation for Windows users
```
python -m pip install -r .\requirements.txt
```

## Usage
:small_blue_diamond:  '**menu**' commands needs to be used for returning to the main menu from any prompt that asks the user for input.

```
python bot.py
```



### Notes
:small_blue_diamond: Operation intervals has been set for a length of time that prevents your account from getting banned for bulk operations of post-likes, user-follows or commenting.  
:small_blue_diamond: The operation intervals may be changed from within [config.json](https://github.com/mariuszmalek/leech/blob/master/config.json).  
:small_blue_diamond: Has been tested only under Windows.  
:small_blue_diamond: Python version: 3.8.1  


### Technologies used
 :small_blue_diamond: Python  
 :small_blue_diamond: Selenium  
 :small_blue_diamond: Javascript  

## Screenshots

:small_blue_diamond: Main menu

![Main menu](https://raw.githubusercontent.com/mariuszmalek/leech/main/img/mainMenu.PNG)


:small_blue_diamond: Download posts

![Download posts](https://raw.githubusercontent.com/mariuszmalek/leech/main/img/postsDownload.PNG)

:small_blue_diamond: Like posts

![Like posts](https://raw.githubusercontent.com/mariuszmalek/leech/main/img/postsLike.PNG)

:small_blue_diamond: Bulk unfollow

![Bulk unfollow](https://raw.githubusercontent.com/mariuszmalek/leech/main/img/allUnfollow.PNG)


:small_blue_diamond: Bulk commenting

![Bulk commenting](https://raw.githubusercontent.com/mariuszmalek/leech/main/img/bulkComment.PNG)

:small_blue_diamond: Bulk comment deletion

![Bulk comment deletion](https://raw.githubusercontent.com/mariuszmalek/leech/main/img/messagesDeleted.PNG)




## License
 [![License](https://img.shields.io/github/license/mariuszmalek/leech)](https://github.com/mariuszmalek/leech/blob/master/LICENSE)

