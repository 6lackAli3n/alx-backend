# Queuing System in JS

## Project Overview
This project demonstrates a queuing system implemented using Node.js and Redis. The system interacts with a Redis instance to store and retrieve values.

## Prerequisites
- Ubuntu 18.04
- Node.js 12.x
- Redis 6.0.10
- Run `npm install` to install project dependencies from `package.json`.

## Setting up Redis
1. Download and install Redis 6.0.10:
    ```bash
    $ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
    $ tar xzf redis-6.0.10.tar.gz
    $ cd redis-6.0.10
    $ make
    ```

2. Start Redis server:
    ```bash
    $ src/redis-server &
    ```

3. Set and get a value in Redis:
    ```bash
    $ src/redis-cli
    127.0.0.1:[Port]> set Holberton School
    OK
    127.0.0.1:[Port]> get Holberton
    "School"
    ```

4. Stop Redis server:
    ```bash
    $ kill [PID_OF_Redis_Server]
    ```

## Project Setup
1. Install the dependencies:
    ```bash
    $ npm install
    ```

2. Copy `dump.rdb` to the project directory:
    ```bash
    $ cp redis-6.0.10/dump.rdb /path/to/project/0x03-queuing_system_in_js/
    ```

## Usage
Run the development server using Nodemon:
```bash
$ npm run dev

