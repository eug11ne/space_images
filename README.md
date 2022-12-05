# space_images
 
Upload images of space to the specified Telegram channel. Use three scripts to fill the **images** folder with space pictures and then publish them to the tg channel. 

### How to install

Create a Python vitrual environment using the following command: 

<pre>pip venv <i>dir-name</i></pre>

Copy space_images repo into the virtual environment folder. Open git shell and enter the folloing command: 

```
git clone "https://github.com/devmanorg/everything-recognition.git"
```

Run `activate.bat` from **Scripts** subfolder to activate the virtual envirionment. 

Enter the following command in the command line: 

<pre>python pip install -r requirements.txt</pre>

Obtain NASA API key at https://api.nasa.gov/#apod and add it to **.env** file as `NASA_API_KEY` parameter. Example:

```
NASA_API_KEY=abc12def3g456h7i78j4ea8535fbebb83d0dc8878
```
Also, add the following parameters to **.env** file: 
- `TG_KEY` - your telegram bot token. 
- `TG_PUBLICATION_PERIOD` - number of hours to wait before publishing the next image. 
- `CHAT_ID` - name of the tg channel (for example, @space_overview)

Place **.env** file in the root folder of the project. 
 
## fetch_spacex_images.py
Downloads images from Space X API. 

### How to use

Enter the following command: 

<pre>python fetch_spacex_images.py <i>launch_id</i></pre>

where *launch_id* is Space X launch id. If omitted, script uses the latest launch. 

## fetch_nasa_apod_images.py
Downloads images from NASA APOD database. 

### How to use

Enter the following command: 

<pre>python fetch_nasa_apod_images.py <i>count</i></pre>

where *count* is the number of images to retrieve.

## fetch_nasa_epic_images.py
Downloads images from NASA EPIC database. 

### How to use

Enter the following command: 

<pre>python fetch_nasa_epic_images.py</pre>

## tg-bot.py
Publishes one picture to tg channel. It can be specified manually or randomly chosen.

### How to use

Enter the following command: 

<pre>python tg-bot.py <i>image</i></pre>
where *image* is an image you want to publish. If omitted, it is chosen randomly.


## tg-bot-all.py
Publishes a random picture from **images** folder to tg channel every N hours. 

## common_functions.py
Contains a set of common functions that are reused by the scripts. 
