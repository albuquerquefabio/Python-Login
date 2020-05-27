# Python-Login

A simple GUI login in python with http request.

- Done List:

  - [x] Request credenticals over http
  - [x] Save credenticals with sqlite
  - [x] Open app and check if exists credentials and go to welcome window or do login again
  - [x] do logout and remove all data from sqlite

- TODO:

  - [] Connect with Socket.io as client
  - [] Send credentials over the socket

## Depencencies

`pip install functools`
`pip install requests`

## Run

`python main.py`
_work great with Linux and macOS_

## Server side

All server side was made in **nodeJS** with MongoDb, Socket.io, RedisJWT RedisDB and more;
To see more about my nodeJs server follow this: [nodetomic-api.](https://github.com/albuquerquefabio/nodetomic-api)
