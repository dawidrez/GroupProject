# Backend Setup and Usage

## Running the Backend

To run the backend, use the following command:

```bash
docker-compose up -d
```

## Importing Films from CSV

To load films from the CSV file, use the following command:

```bash
docker exec -it backend-web-1 python read_films.py
```

## Accessing the Films Endpoint

Once the backend is running and the films have been imported, you can access the list of films via the following endpoint:

```bash
GET: http://127.0.0.1:5000/films
```

## Accessing the Genres Endpoint

```bash
GET: http://127.0.0.1:5000/genres
```

This will return the films data as a JSON response.