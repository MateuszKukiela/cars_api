# cars_api
For your cars related needs

## About

This is a simple API allowing adding cars to a database and rating them.


## Usage

To view whole API documentation use go to [/docs/](http://afternoon-beach-36358.herokuapp.com/docs/)

(Please make sure you are connected over HTTP not HTTPS or interact button wilt not work properly, I didn't fix this heroku specific bug yet)

Short summary below:

POST /cars
* Request body should contain car make and model name
  e.g. {"make":"Volkswagen", "model":"Golf"}
  
POST /rate
* Add a rate for a car from 1 to 5
 e.g. {"car":<car_id>, "rating":<1-5>}
  
GET /cars
* Will fetch list of all cars already present in application database with their current average rate

GET /popular
* Will return top 10 cars already present in the database ranking based on number of rates


You are welcome to test this API at: [http://afternoon-beach-36358.herokuapp.com/](http://afternoon-beach-36358.herokuapp.com/)

There is also standard django admin available: [http://afternoon-beach-36358.herokuapp.com/admin](http://afternoon-beach-36358.herokuapp.com/admin)



## Local development

This app is made for heroku deployment, but for local development it uses docker-compose. Docker uses requirements_dev.txt ad for production on heroku we use requirements.txt.
Remember to fill .env.sample and rename it to .env
Then:

```docker-compose build```


```docker-compose up -d```

To run migrations (necessary after building)

```docker-compose run web python manage.py migrate```

To add superuser

```docker-compose run web python manage.py createsuperuser```

And to run tests

```docker-compose run web python manage.py test```

You can also use black and isort

```docker-compose run web black .```

```docker-compose run web isort .```


## TO DO
* Increase test coverage
* Separate requirements for dev and production  
* Add some sort of CI (Heroku CI isn't free, so I'm thinking about moving this repo to GitLab, as they have free CI)
* Add NginX and Let's Encrypt combo to docker-compose, it would be production ready on any machine then.
* Move Database setting from settings.py to local_settings.py, or deal with it differently as I don't like current solution. 
* Add automatic migrations (maybe as separate container)
* Add migration with automatic admin creation using env provided in config or heroku


## Contributing
Pull requests are welcome. Please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

