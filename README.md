with this project I intend to create a simple Movie API, using a third party API and render the info to create an API that will be published using AWS as cloud provider

what I need:
Boto3 as SDK
NoSQL db
AWS cloud storage
serverless function

DATA MODEL
{
    "title":"title of the movie",
    "releaseYear":"when the movie was released",
    "genre":"genre of the movie",
    "coverUrl":"url-to-image-in-cloud-storage"
}

STEPS:
-install boto3 (AWS SDK for python) with pip,
-find a movie third party API and store it in the NoSQL db
-create 3 function: 
    GetMovies: Returns a JSON list of all movies in your db. Make sure to return a URL for the movie cover.
    GetMoviesByYear: Returns a list of movies released in that year. Year is provided by the client.
    EXTRA CREDIT: GetMovieSummary: Returns a summary that is generated by AI.
-publish everything on AWS
