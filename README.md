# CODe API
REST API served from Civil Cases database

## Prerequisites
The API is written in Python and makes use of the following libraries:
* Flask: A popular microframework to ease routing
* py2neo: To connect to the Neo4J database

These libraries are to be installed through Pip or as instructed by their
maintainers.

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
Outputs all appeals.

Sample call:
`` http://localhost:5000/api/0.1/json/cases/appeals ``

### /cases
Deprecated (for now)


### /cases/party/{surname}/{name}
Searches party by prosecutor or defendant name and surname. If no party with the specified name and surname
is found, an either or condition is applied on the two parameters.

Sample call:
`` http://localhost:5000/api/0.1/json/cases/party/gillford/brian ``

### /cases/party
Similar to `` /cases/party/{surname}/{name} `` above, but name and surname can be in any order.

Sample call:
`` http://localhost:5000/api/0.1/json/cases/party?surname=gillford&name=brian ``

GET parameters:

* name
* surname

### /cases/judge/{surname}/{name}
Searches for cases by judge name and surname.

Sample call:
`` http://localhost:5000/api/0.1/json/cases/judge/vella/gabriella ``

### /cases/judge
Similar to `` /cases/judge/{surname}/{name} `` above, but name and surname can be in any order.

Sample call:
`` http://localhost:5000/api/0.1/json/cases/judge ``

GET parameters:

* name
* surname

### /cases/keywords/{keywords}
where keywords is a list of keywords seperated by a comma.

Outputs all cases associated to those particular keywords.

Sample calls:
`` http://localhost:5000/api/0.1/json/cases/keywords/qtil ``
`` http://localhost:5000/api/0.1/json/cases/keywords/serqa, bank ``

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
