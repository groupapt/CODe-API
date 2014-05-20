# CODe API
REST API served from Civil Cases database

## API


### /case/{int:reference_p1}/{int:reference_p2}
Sample output:
``` json

```

### /appeal/{int:reference_p1}/{int:reference_p2}/{int:reference_p3}
Sample output:
``` json
{
  "response": [
    {
      "court_name": "The Administrative Review Tribunal",
      "date": "2012-10-19",
      "defendant": " Awtorit\u00e0 ghat-Trasport f\u2019Malta ",
      "j_name": "GABRIELLA",
      "j_surname": "VELLA",
      "keywords": [
        "-pocy",
        "\u201cB\u2019ittra",
        "xi",
        "xxa",
        "ai"
      ],
      "node_name": "GVELLA",
      "prosecutor": "Joseph Bajada (Karta ta\u2019 l-Identit\u00e0 bin-Numru 24466G) u S.B. Autocentre Limited (C-16378) ",
      "reference": "6/2011/1"
    }
  ]
}
```

### /cases/date/{date}
Sample output:
``` json

```

### /cases/year/{int:year}
Sample output:
``` json

```

### /cases/appeals
Sample output:
``` json

```

### /cases
Deprecrated

### /cases/defendant/{defendant_surname}/{defendant_name}
Sample output:
``` json

```

### /cases/prosecutor/{prosecutor_surname}/{prosecutor_name}
Sample output:
``` json

```

### /cases/prosecutor/{prosecutor_surname}/{prosecutor_name}
Sample output:
``` json

```

### /cases/judges/{judge_surname}/{judge_name}
Sample output:
``` json

```

### /cases/keywords/{keywords}
Sample output:
``` json

```

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