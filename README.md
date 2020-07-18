# Casting Agency

Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.

Hosted on heroku. [Link](https://herokuapp.com/).

## Motivation

This is my capstone project for the Udacity FSND nanodegree.

## Dependencies

All dependencies are listed in the `requirements.txt` file. 
They can be installed by running `pip3 install -r requirements.txt`.

Set the required ENV variables mentioned in setup.sh

## Roles & Actions
**Casting Assistant**

Can view actors and movies

Endpoint access:
- `GET /movies`
- `GET /actors`

**Casting Director**

All permissions a Casting Assistant has and
Add or delete an actor from the database
Modify actors or movies

Endpoint access:
- `GET /actors`
- `POST /actors`
- `PATCH /actors/<int:id>`
- `DELETE /actors/<int:id>`
- `GET /movies`
- `PATCH /movies/<int:id>`

  
**Executive Producer**

All permissions a Casting Director has and
Add or delete a movie from the database

Endpoint access:
- `GET /actors`
- `POST /actors`
- `PATCH /actors/<int:id>`
- `DELETE /actors/<int:id>`
- `GET /movies`
- `POST /movies`
- `PATCH /movies/<int:id>`
- `DELETE /movies/<int:id>`

## Authentication

The API has three registered users who have different roles to perform actions.

1. Assistant

```
User:  
assistant@assistant.com

password:
123456@sd

```

2. Director

```
User: 
director@director.com

password:
director@director.com1
```

3. Producer

```
User:
producer@casting.com

Password:
producer@casting.com1
```


## Endpoints

### `GET /movies`

Gets all movies from the db.

Response:

```json5
{
  "movies": [
    {
      "id": 1,
      "movies": "all acted movies here",
      "release_date": "2021-02-02",
      "title": "Movie"
    },
    {
      "id": 2,
      "movies": "all acted movies here",
      "release_date": "2019-01-01",
      "title": "New movie"
    }
  ],
  "success": true
}
```

### `POST /movies`

Adds a new movie to the db.

Data:

```json5
{
  "title": "title",
  "release_date": "release_date"
}
```

Response:

```json5
{
  "success": true,
  "movie": "title"
}
```

### `PATCH /movies/<int:id>`

Edit data on a movie in the db.

Data:

```json5
{
  "title": "new title",
  "release_date": "2021-02-02"
}
```

Response:

```json5
{
  "success": true,
  "movie": {
              "id": 1,
              "movies": "all acted movies here",
              "release_date": "2021-02-02",
              "title": "new title"
            }
}
```

### `DELETE /movies/<int:id>`

Delete a movie from the db.

Response:

```json5
{
  "success": true,
  "delete": 1
}
```

### `GET /actors`

Gets all actors from the db.

Response:

```json5
{
  "actors": [
    {
      "gender": "M",
      "id": 1,
      "movies": "all acted movies here",
      "name": "actor"
    },
    {
      "gender": "F",
      "id": 2,
      "movies": "all acted movies here",
      "name": "ewwe"
    }
  ],
  "success": true
}
```

### `POST /actors`

Adds a new actor to the db.

Data:

```json5
{
  "name": "name",
  "gender": "F"
}
```

Response:

```json5
{
  "success": true,
  "actor": "name"
}
```

### `PATCH /actors/<int:id>`

Edit data on a actor in the db.

Data:

```json5
{
  "name": "new name",
  "gender": "M"
}
```

Response:

```json5
{
  "success": true,
  "actor": {
              "gender": "M",
              "id": 1,
              "movies": "all acted movies here",
              "name": "new name"
            }
}
```

### `DELETE /actors/<int:id>`

Delete a actor from the db.

Response:

```json5
{
  "success": true,
  "delete": 1
}
```

## Development run

- Set the environment variable mentioned in the setup.sh and execute the bash file.
- Update the access token if expired
- Run the application as `python app.py`

## Tests

To run the tests, run `python  app_test.py`.