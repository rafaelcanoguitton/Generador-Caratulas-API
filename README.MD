# Generador de carátulas UCSP - API

Generating covers for Uni work is tedious. So I made an API to do exactly that! This API will allow you to generate covers with certain parameters.

## How to use

The API can process two requests that does basically one thing. The process goes as follows:

- Make a POST HTTP call to this URL '/' with the following body structure.
  
  ```json
  {
      "carrera":"YOUR MAJOR HERE",
      "titulo":"YOUR WORK TITLE HERE",
      "curso":"YOUR COURSE HERE",
      "semestre":1-10 INT,
      "alumnos":["1ST STUDENT","2ND STUDENT",...]
  }
  ```

The request can be made in any order, simply follow these set of rules:

- `"semestre"` must receive an integer from 1-10

- `"alumnos"` must receive up to 6 names

Otherwise the API will give a `403 BAD REQUEST` response.

The aformentioned request will return a token like this `W2537V67` and you can use it to retrieve the cover with a get request at '/retornar_caratula/**token**'.

## URLS

The urls for the requests are the following:

- `https://generador-caratulas-ucsp-api.herokuapp.com/` For the first request.

- `https://generador-caratulas-ucsp-api.herokuapp.com/retornar_caratula/ `For the second request.

## Example

![](ex_cover.png)

## Currently used by

- [botUCSP](https://github.com/rafaelcanoguitton/botUCSP)

- [rafxarBOT](https://github.com/rafaelcanoguitton/rafxarBOT)
