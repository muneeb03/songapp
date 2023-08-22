# Song App

The Song App is a web application that allows users to discover, listen to, and manage their favorite songs, albums, and playlists. It provides various features to enhance the music listening experience.

## Features

### User Registration and Authentication

- Users can register with their email and password.
- Custom user model with extended fields like full name.
- User authentication using JSON Web Tokens (JWT).

### Song Management

- View a list of all songs in the library.
- Search for songs by title, artist, or tags.
- Like and unlike songs.
- Add songs to the user's favorite list.

### Album Management

- Create and manage private or public albums.
- Add and remove songs to/from albums.
- View the list of albums created by the user.

### Comment on Songs

- Users can leave comments on songs.
- View comments and interact with them.

### API Endpoints

- `POST /api/users/register/`: Register a new user.
- `POST /api/users/login/`: Login and obtain a JWT token.
- `GET /api/songs/`: Get a list of all songs.
- `GET /api/albums/`: Get a list of all albums.
- `POST /api/albums/`: Create a new album.
- `GET /api/albums/<album_id>/songs/`: Get songs in a specific album.
- `POST /api/albums/<album_id>/add-songs/`: Add songs to a specific album.
- `GET /api/songs/<song_id>/comments/`: Get comments for a song.
- `POST /api/songs/<song_id>/comments/`: Add a comment to a song.
- `GET /api/users/profile/`: Get user profile, including favorite songs and created albums.

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/yourusername/music-app.git
   ```

2. Navigate to the project directory:

   ```
   cd music-app
   ```

3. Install the required packages using pip:

   ```
   pip install -r requirements.txt
   ```

4. Set up your database by running migrations:

   ```
   python manage.py migrate
   ```

5. Create a superuser account:

   ```
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```
   python manage.py runserver
   ```

7. Access the app at `http://127.0.0.1:8000/`.

## Usage

- Register a new user or log in using the provided API endpoints.
- Browse songs, albums, and playlists.
- Like songs, add them to your favorite list.
- Create and manage albums.
- Comment on songs to share your thoughts.

## Technologies Used

- Django and Django REST framework
- SQLite database
- JSON Web Tokens (JWT) for authentication
