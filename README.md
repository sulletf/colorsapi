# Colors REST API

Django REST API to manage a company standardized colors database.

API main entry point is ```http://sulletf.pythonanywhere.com/```

## Listing available colors

### Request

```GET /colores```

**Parameters:**
* ```colors_per_page``` : number of color items per page ; default is 10.
* ```page``` : page number to display, starting at 1.



