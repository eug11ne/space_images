# space_images
 
Upload images of space to Telegram channel @space_overview. Use three scripts to fill the **images** folder with space pictures and then publish them to tg channel. 
 
## fetch_spacex_images.py
Downloads images from Space X API. 

### How to use

Enter the following command in the command line: 

<pre>python fetch_spacex_images.py <i>launch_id</i></pre>

where *launch_id* is Space X launch id. If omitted, script uses the latest launch. 

## fetch_nasa_apod_images.py
Downloads images from NASA APOD database. At first you have to get a NASA API key at https://api.nasa.gov/#apod and add it to **.env** file as `NASA_API_KEY` parameter. 

### How to use

Enter the following command: 

<pre>python fetch_nasa_apod_images.py <i>count</i></pre>

where *count* is the number of images to retrieve.

## fetch_nasa_epic_images.py
Downloads images from NASA EPIC database. At first you have to get a NASA API key at https://api.nasa.gov/#apod and add it to **.env** file as `NASA_API_KEY` parameter. 

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
Publishes a random picture from **images** folder to tg channel every N hours. It uses the following parameters from **.env** file: 
- `TG_KEY` - your telegram bot token. 
- `TG_PUBLICATION_PERIOD` - number of hours to wait before publishing the next image. 

## common_functions.py
Contains a set of common functions that are reused by the scripts. 
