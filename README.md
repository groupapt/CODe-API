# CODe API
REST API served from Civil Cases database

## API
In URLs listed here, the following notations are used accordingly:

* `` {value} `` used to represent some generic value
* `` {type:value} `` used to represent the data types which could be used

The base URL, one should use in order to access any method is
`` http://localhost:5000/api/0.1/json/ ``

The following is the standard sample output:
``` json

```

### /case/{int:reference_p1}/{int:reference_p2}


### /appeal/{int:reference_p1}/{int:reference_p2}/{int:reference_p3}


### /cases/date/{date}
where date should have the following structure:
`` year-month-day ``

Sample call:
`` http://localhost:5000/api/0.1/json/cases/date/2011-05-13 ``

### /cases/appeals
N.B.: This method is currently outputting duplicate results, due to the internal relationship between case
and appeal nodes.

### /cases
Deprecrated

### /cases/party/{surname}/{name}
Sample call:
`` http://localhost:5000/api/0.1/json/cases/party/gillford/brian ``

### /cases/party
Similar to `` /cases/party/{surname}/{name} `` above.

GET parameters:


### /cases/keywords/{keywords}

### 404 Error
Output:
``` json
{"error": "Not found"}
```

### 500 Error
Output:
``` json
{"error": "Internal error"}
```