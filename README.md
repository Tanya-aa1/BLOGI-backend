# Blogi 
-Platform for bloggers to create and share their content with the world.

## Overview

This project is a dockerized backend project for a blogging platform called Blogi, built using FastAPI and PostgreSQL. It fulfills the core assignment objectives, including:

- User registration and login with JWT authentication
- Creating, reading, updating, and deleting personal blog posts
- Viewing a list of all blog posts sorted by most recent posts
- Secure interaction with a PostgreSQL database using SQLAlchemy ORM
- RESTful API architecture with proper error handling
- Support for uploading images to blog posts
- Pagination for the list of all posts
- Searching a blog post by its title/ content
- Dockerized the full backend



## Features

1. User Authentication
   
   - User registration with a unique username and password
   - Hashing of passwords for security
   - Login and returning a JWT token for protected endpoints
   - Tokens secured using PyJWT with expiration
     
2. Blog Post Management
   
   - Create Post -- Authenticated users can create blog posts with title and content
   - Read Posts  -- Retrieve personal posts
                 -- View all blog posts sorted by most recent
   - Update/Delete — Authenticated users can update or delete only their own posts

3. Use PostgreSQL as the database for storing users and blog posts

4. Implemented error handling for all routes

5. **BONUS FEATURES**

   A. Search blog posts by keywords in title or content

   B. Pagination for blog listing

   C. Image upload support while creating a blog
   
   D. Dockerized development environment
   


## Libraries Used

- `FastAPI` - Web framework
- `SQLAlchemy` - ORM
- `Uvicorn` - ASGI server
- `Passlib` - Password hashing
- `PyJWT` - JWT token handling
- `python-dotenv` - Load environment variables

## Database Schema
The application uses a PostgreSQL database with the following two primary tables:

1. users
   - id	
   - username	
   - password
   - posts (relationship)

2. posts
   - id	
   - title	
   - content	
   - created_at	
   - updated_at
   - user_id
   - image_url
   - author (relationship)

## API Endpoints

  POST- /register   - Register a new user 
  
  POST- /login      - Authenticate user and get token 
  
  GET - /me         - Getting the current user
  
  GET - /blogs      - Get all blogs (supports pagination & search) 
  
  GET - /blogs/{id} - Get a single blog post 
  
  POST- /blogs      - Create a blog post (auth required) 
  
  PUT - /blogs/{id} - Update a blog post (auth required) 
  
  DELETE- /blogs/{id} - Delete a blog post (auth required) 

##  How to Run the Project

1. Prerequisites

- [Docker](https://www.docker.com/) & Docker Compose installed
- Clone this repo

2. Setup `.env` File

   Create a file named `.env` in the root directory and fill it as mention in `.env.example`

3. Run with Docker

```bash
docker-compose up --build
```

4. Your FastAPI app will be available at:
  - http://localhost:8000/docs    ← for Swagger UI


## Issues Encountered

- FastAPI starts before PostgreSQL is ready -	Fixed using wait-for-it.sh script
- Environment variables not loading	Ensure  -   ensure .env is present and correct
- Connection refused to DB -	Check if db service is up, and Docker network is working properly


## Output

![image](https://github.com/user-attachments/assets/21b4a2da-8d58-4761-9678-65c26acc226c)

![image](https://github.com/user-attachments/assets/23a1a717-64b5-4d3c-a9b1-a7578a4f41ad)

![image](https://github.com/user-attachments/assets/1a85eba4-ec6d-42eb-9c33-d2f73fd9c757)

![image](https://github.com/user-attachments/assets/c70e195b-b452-40a9-a59f-2cd548b8de23)

![image](https://github.com/user-attachments/assets/61a497ae-e11e-409d-9265-e6dfcd725a1d)




