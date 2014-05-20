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
{
  "response": [
    {
      "court_name": "The Administrative Review Tribunal",
      "date": "2013-01-25",
      "defendant": " Awtorit\u00e0 ghat-Trasport f\u2019Malta ",
      "judge": "Gabriella Vella",
      "keywords": [
        "\u201c22",
        "nghaw",
        "l-Awtorit\u00e0",
        "ml-",
        "moghtija"
      ],
      "pdf": "script_get_judgement_document.aspx?CaseJudgementID=78919",
      "prosecutor": "Joseph Bajada (Karta ta\u2019 l-Identit\u00e0 bin-Numru 24466G) u S B Autocentre Limited (C-16378) ",
      "reference": "1/2011/1"
    }
  ]
}
```

### /case/{int:reference_p1}/{int:reference_p2}
Sample call:
`` http://localhost:5000/api/0.1/json/case/1/2011 ``

### /appeal/{int:reference_p1}/{int:reference_p2}/{int:reference_p3}
Sample call:
`` http://localhost:5000/api/0.1/json/appeal/1/2011/1 ``

### /cases/date/{date}
where date should have the following structure:
`` year-month-day ``

Sample call:
`` http://localhost:5000/api/0.1/json/cases/date/2011-05-13 ``

### /cases/appeals
N.B.: This method is currently outputting duplicate results, due to the internal relationship between case
and appeal nodes.

Sample call:
`` http://localhost:5000/api/0.1/json/cases/appeals ``

### /cases
Deprecated

### /cases/party/{surname}/{name}
Searches party by prosecutor or defendant name and surname. If no party with the specified name and surname
is found, an either or condition is applied on the two parameters.

Sample call:
`` http://localhost:5000/api/0.1/json/cases/party/gillford/brian ``

### /cases/party
Similar to `` /cases/party/{surname}/{name} `` above.

Sample call:
`` http://localhost:5000/api/0.1/json/cases/party?surname=gillford&name=brian ``

GET parameters:

* name
* surname

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