# WeddingJukebox
An app that will run the Spotify API via a RFID reader. As seen my my wedding...


To run this container, first cloen this repository.

## Add Spotify Credentials

To setup Spotify API credentials...


Next, add file `credentials.py` 

```
spotipy_credentials = {
    'USERNAME': "user",
    'SPOTIPY_CLIENT_ID': "your-spotify-client-id",
    'SPOTIPY_CLIENT_SECRET': "your-spotfy-secret"
}
```

## Run the container

To run the container 

```
docker run --interactive --tty wedding-jukebox
```
