# vue-webpack-django
An demo project builed by using Django and vue
## How to run this project
```sh
# Step 1
# Run the Django project
# Environment: python3.7
cd paperReadSmart
pip install -r requirements.txt
python manage.py runserver <your ip>:<the port you want to use>  
# eg: python manage.py runserver 192.168.88.1:8088
# The IP and ports is Useful below for us
```
```sh
# Step 2
# Run the Vue project
# Environment: Node 8.11.4
cd ../webPaperSmart
# Install dependences
npm install
# Building project
npm run build
# No accidents, we can get the directory like this.In particular, pay attention to the dist directory
|   .babelrc
|   .editorconfig
|   .eslintignore
|   .eslintrc.js
|   .gitignore
|   .postcssrc.js
|   index.html
|   package.json
|   README.md
|
+---build
|       build.js
|       check-versions.js
|       logo.png
|       utils.js
|       vue-loader.conf.js
|       webpack.base.conf.js
|       webpack.dev.conf.js
|       webpack.prod.conf.js
|
+---config
|       dev.env.js
|       index.js
|       prod.env.js
|
+---dist
|   |   index.html
|   |
|   \---static
|       +---css
|       |       app.648f5a046b815696f39db57e1336c5c9.css
|       |       app.648f5a046b815696f39db57e1336c5c9.css.map
|       |
|       +---fonts
|       |       ionicons.99ac330.woff
|       |       ionicons.d535a25.ttf
|       |
|       +---img
|       |       ionicons.a2c4a26.svg
|       |
|       \---js
|               0.b687a074c0d1b6a73edf.js
|               0.b687a074c0d1b6a73edf.js.map
|               app.600a074cf83775d0e864.js
|               app.600a074cf83775d0e864.js.map
|               manifest.017b3b0152d0cdd3ec5d.js
|               manifest.017b3b0152d0cdd3ec5d.js.map
|               vendor.43bbe828814b5f961d74.js
|               vendor.43bbe828814b5f961d74.js.map
|
+---src
\---static
```

```sh
# Step 3
# Copy the dist directory to the Django directory
+---paperReadSmart
|   +---data
|   +---dist
|   |   \---static
|   |       +---css
|   |       +---fonts
|   |       +---img
|   |       \---js
|   +---paperReadSmart
|   +---polls
|   +---templates
|   +---tool
|   \---users
|       +---migrations
|       +---static
|       |   +---css
|       |   +---fonts
|       |   +---img
|       |   \---js
```
```sh
# Step 4
# Open Browser eg: http://192.168.88.1:8088
# Bingo, we get an running demo project!
```
![image](https://github.com/wuyueCreator/vue-webpack-django/blob/master/home_20180930031403.png?raw=true)

> If you encounter any problems, please make issue to this project, if you like this demo, please fork it.