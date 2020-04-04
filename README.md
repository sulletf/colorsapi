# Colors REST API

Django REST API to manage a company standardized colors database.

API main entry point is ```http://sulletf.pythonanywhere.com/```

## Listing available colors

### Request

```GET /colores```

Returns a paginated list of the currently available colors in the database. Data is returned as JSON (default) or XML format ; to specify a format, use the ```Accept``` HTTP header.

**Parameters:**
* ```colors_per_page``` : _optional_ ; number of color items per page ; default is 10.
* ```page``` : _optional_ ; page number to display, starting at 1.

### Response

#### ```curl -H 'Accept: text/xml' 'http://sulletf.pythonanywhere.com/colores/?page=2&colors_per_page=5'```

```
HTTP/1.1 200 OK
Date: Sat, 04 Apr 2020 13:10:21 GMT
Content-Type: application/xml
Content-Length: 730
Connection: keep-alive
Vary: Accept-Encoding
X-Frame-Options: SAMEORIGIN
X-Clacks-Overhead: GNU Terry Pratchett
Server: PythonAnywhere

<?xml version="1.0" encoding="UTF-8"?>
<colors>
  <page>2</page>
  <number_pages>3</number_pages>
  <number_colors_per_page>5</number_colors_per_page>

  
  <color>
    <color_id>6</color_id>
    <name>blue turquoise</name>
    <hex_code>#53B0AE</hex_code>
  </color>
  
  <color>
    <color_id>7</color_id>
    <name>sand dollar</name>
    <hex_code>#DECDBE</hex_code>
  </color>
  
  <color>
    <color_id>8</color_id>
    <name>chili pepper</name>
    <hex_code>#9B1B30</hex_code>
  </color>
  
  <color>
    <color_id>9</color_id>
    <name>blue iris</name>
    <hex_code>#5A5B9F</hex_code>
  </color>
  
  <color>
    <color_id>10</color_id>
    <name>mimosa</name>
    <hex_code>#F0C05A</hex_code>
  </color>
  

</colors>
```

#### ```curl http://sulletf.pythonanywhere.com/colores/```

```
HTTP/1.1 200 OK
Date: Sat, 04 Apr 2020 13:13:38 GMT
Content-Type: application/json
Content-Length: 695
Connection: keep-alive
Vary: Accept-Encoding
X-Frame-Options: SAMEORIGIN
X-Clacks-Overhead: GNU Terry Pratchett
Server: PythonAnywhere

{"page": 1, "number_pages": 2, "number_colors_per_page": 10, "colors_list": [{"color_id": 1, "name": "cerulean", "hex_code": "#98B2D1"}, {"color_id": 2, "name": "fuchsia rose", "hex_code": "#C74375"}, {"color_id": 3, "name": "true red", "hex_code": "#BF1932"}, {"color_id": 4, "name": "aqua sky", "hex_code": "#7BC4C4"}, {"color_id": 5, "name": "tigerlily", "hex_code": "#E2583E"}, {"color_id": 6, "name": "blue turquoise", "hex_code": "#53B0AE"}, {"color_id": 7, "name": "sand dollar", "hex_code": "#DECDBE"}, {"color_id": 8, "name": "chili pepper", "hex_code": "#9B1B30"}, {"color_id": 9, "name": "blue iris", "hex_code": "#5A5B9F"}, {"color_id": 10, "name": "mimosa", "hex_code": "#F0C05A"}]}
```

## Getting a color's details

### Request

```GET /colores/:id```

Returns the detailed description of a given color. Data is returned as JSON (default) or XML format ; to specify a format, use the ```Accept``` HTTP header.

### Response

#### ```curl http://sulletf.pythonanywhere.com/colores/10```

```
> Host: sulletf.pythonanywhere.com
> User-Agent: curl/7.58.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Date: Sat, 04 Apr 2020 13:19:00 GMT
< Content-Type: application/json
< Content-Length: 77
< Connection: keep-alive
< X-Frame-Options: SAMEORIGIN
< X-Clacks-Overhead: GNU Terry Pratchett
< Server: PythonAnywhere
< 
* Connection #0 to host sulletf.pythonanywhere.com left intact
{"name": "mimosa", "year": 2009, "hex_code": "#F0C05A", "pantone": "14-0848"}
```

#### ```curl -H 'Accept: text/xml' http://sulletf.pythonanywhere.com/colores/1```

```
HTTP/1.1 200 OK
Date: Sat, 04 Apr 2020 13:49:14 GMT
Content-Type: application/xml
Content-Length: 187
Connection: keep-alive
X-Frame-Options: SAMEORIGIN
X-Clacks-Overhead: GNU Terry Pratchett
Server: PythonAnywhere
 
<?xml version="1.0" encoding="UTF-8"?>

<color>
  <color_id>1</color_id>
  <name>cerulean</name>
  <hex_code>#98B2D1</hex_code>
  <year>2000</year>
  <pantone>15-4020</pantone>
</color>
```
## Adding a new color

### Request

```POST /colores```

Adds a new color record to the database based on parameters passed as urlencoded parameters.

Returns the newly created color id as JSON.

### Response

#### ```curl --data 'pantone=00-0000&hex_code=#000000&name=black&year=2020' http://sulletf.pythonanywhere.com/colores/```

```
HTTP/1.1 201 Created
Date: Sat, 04 Apr 2020 14:04:33 GMT
Content-Type: application/json
Content-Length: 16
Connection: keep-alive
X-Frame-Options: SAMEORIGIN
X-Clacks-Overhead: GNU Terry Pratchett
Server: PythonAnywhere

{"color_id": 13}```
