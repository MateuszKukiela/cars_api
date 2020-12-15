# yet_another_twitter_clone
Totally not a twitter clone

## About

This is a simple API allowing registered users to post messages.
Unregistered users can only view messages.


## Usage

To view whole API documentation use go to [/docs/](http://fast-fjord-08287.herokuapp.com/docs/)

Short summary below:

To be able to post you have to create an account:
* POST /users/ and in body use json like this: {"username": \<your_username>, "password": \<your_password>}
  
To login you can use BasicAuth

To get posts and post posts yourself use:

* GET /posts/  to get all posts in paginated view
* GET /posts/\<id> to get content of given post
* POST /posts/ and in body use json like this: {"content": \<your message up to 160 characters>}

You are welcome to test this API at: [http://fast-fjord-08287.herokuapp.com/](http://fast-fjord-08287.herokuapp.com/)
There is an already registered user for your convenience login:test password:test

There is also standard django admin available: [http://fast-fjord-08287.herokuapp.com/admin](http://fast-fjord-08287.herokuapp.com/admin)



## Local development

This app is made for heroku deployment, but for local development it uses docker-compose.
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
* Add Token authentication and endpoint for it generating
* Add some sort of CI (Heroku CI isn't free, so I'm thinking about moving this repo to GitLab, as they have free CI)
* Add NginX and Let's Encrypt combo to docker-compose, it would be production ready on any machine then.
* Move Database setting from settings.py to local_settings.py, or deal with it differently as I don't like current solution. 
* Add automatic migrations (maybe as separate container)
* Add migration with automatic admin creation using env provided in config or heroku


## Contributing
Pull requests are welcome. Please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

