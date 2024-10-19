# NYT Webapp

Displays data from a New York Times RSS onto a New York Times-like webpage.

Backend Performs All Processing, Displays a Static Version of Built Frontend

Deployed to [NYT WebApp on Heroku](https://nyt-webapp-d825b46890e5.herokuapp.com/)

## Frontend

Frontend uses ReactJS. 

Create the build needed by the backend using `REACT_APP_BACKEND_URL=[Insert API URL] npm run build`

## Backend

Requires Python3, as well as `flask, flask_cors, flask_caching, feedparser, google-cloud-translate, dotenv, datetime`
 - `pip3 install flask flask_cors flask_caching feedparser google-cloud-translate dotenv datetime`

To start, run `python3 rss-backend/rss.py`

