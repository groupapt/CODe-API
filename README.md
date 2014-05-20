# CODe API
REST API served from Civil Cases database

## API


### /case/{int:reference_p1}/{int:reference_p2}
Sample output:
``` json
{
  "response": [
    {
      "court_name": "The Administrative Review Tribunal",
      "date": "2011-05-13",
      "defendant": " Transport Malta gi\u00e0 Awtorit\u00e0 dwar it-Transport r-Rikors ipprezentat  minn  Martin  Spiteri ",
      "j_name": "GABRIELLA",
      "j_surname": "VELLA",
      "keywords": [
        "[ekwivalenti",
        "intima",
        "dwarhom",
        "harget",
        "mancanza"
      ],
      "node_name": "GVELLA",
      "prosecutor": "Martin Spiteri f\u2019ismu proprju u bhala direttur tas-socjet\u00e0 Car Clinic VRT Station  ",
      "reference": "6/2011"
    }
  ]
}
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
where date should have the following structure:
`` year-month-day ``

Sample call:
`` http://localhost:5000/api/0.1/json/cases/date/2011-05-13 ``

Sample output:
``` json
{
  "response": [
    {
      "court_name": "The Administrative Review Tribunal",
      "date": "2011-05-13",
      "defendant": " Transport Malta gi\u00e0 Awtorit\u00e0 dwar it-Transport r-Rikors ipprezentat  minn  Martin  Spiteri ",
      "j_name": "GABRIELLA",
      "j_surname": "VELLA",
      "keywords": [
        "[ekwivalenti",
        "intima",
        "dwarhom",
        "harget",
        "mancanza"
      ],
      "node_name": "GVELLA",
      "prosecutor": "Martin Spiteri f\u2019ismu proprju u bhala direttur tas-socjet\u00e0 Car Clinic VRT Station  ",
      "reference": "6/2011"
    },
    {
      "date": "2011-05-13",
      "defendant": " Transport Malta gi\u00e0 Awtorit\u00e0 dwar it-Transport r-Rikors ipprezentat  minn  Martin  Spiteri ",
      "j_name": "GABRIELLA",
      "j_surname": "VELLA",
      "keywords": [
        "[ekwivalenti",
        "intima",
        "dwarhom",
        "harget",
        "mancanza"
      ],
      "node_name": "GVELLA",
      "prosecutor": "Martin Spiteri f\u2019ismu proprju u bhala direttur tas-socjet\u00e0 Car Clinic VRT Station  ",
      "reference": "6/2011"
    },
    {
      "court_name": "The Administrative Review Tribunal",
      "date": "2011-05-13",
      "defendant": " Transport Malta gi\u00e0 Awtorit\u00e0 dwar it-Transport r-Rikors ipprezentat  minn  Martin  Spiteri ",
      "keywords": [
        "[ekwivalenti",
        "intima",
        "dwarhom",
        "harget",
        "mancanza"
      ],
      "prosecutor": "Martin Spiteri f\u2019ismu proprju u bhala direttur tas-socjet\u00e0 Car Clinic VRT Station  ",
      "reference": "6/2011",
      "year": "2011"
    },
    {
      "date": "2011-05-13",
      "defendant": " Transport Malta gi\u00e0 Awtorit\u00e0 dwar it-Transport r-Rikors ipprezentat  minn  Martin  Spiteri ",
      "keywords": [
        "[ekwivalenti",
        "intima",
        "dwarhom",
        "harget",
        "mancanza"
      ],
      "prosecutor": "Martin Spiteri f\u2019ismu proprju u bhala direttur tas-socjet\u00e0 Car Clinic VRT Station  ",
      "reference": "6/2011",
      "year": "2011"
    }
  ]
}
```

### /cases/year/{int:year}
Sample output:
``` json
{
  "response": [
    {
      "date": "2011-06-16",
      "defendant": " Andrew Howie This ",
      "keywords": [
        "\u0127sara",
        "acts",
        "\fKopja",
        "fejn",
        "kollha"
      ],
      "pdf": "script_get_judgement_document.aspx?CaseJudgementID=68667",
      "prosecutor": "Brian Gilford ",
      "reference": "2/2011"
    },
    {
      "date": "2011-04-11",
      "defendant": " Awtorit\u00e0 dwar it-Trasport ta\u2019 Malta ",
      "keywords": [
        "\u0121ej",
        "\u010bioe\u2019",
        "Tribnal",
        "ma\u2019",
        "Informal"
      ],
      "pdf": "script_get_judgement_document.aspx?CaseJudgementID=67080",
      "prosecutor": "David Anthony Pollina (detentur tal-Karta ta\u2019 l-Identit\u00e0 bin-Numru 31801A) bhala mandatarju specjali ta\u2019 Miqna Webkoor Limited, kumpannija estera registrata fir-Repubblika ta\u2019 Cipru bin-numru ta\u2019 registrazzjoni HE245926 u b\u2019indirzz ta\u2019 6 Avias Elenis Building, Office 43, 1060 Nicosia, Repubblika ta\u2019 Cipru ",
      "reference": "1/2009"
    },
    {
      "date": "2011-05-13",
      "defendant": " Transport Malta gi\u00e0 Awtorit\u00e0 dwar it-Transport r-Rikors ipprezentat  minn  Martin  Spiteri ",
      "keywords": [
        "[ekwivalenti",
        "intima",
        "dwarhom",
        "harget",
        "mancanza"
      ],
      "prosecutor": "Martin Spiteri f\u2019ismu proprju u bhala direttur tas-socjet\u00e0 Car Clinic VRT Station  ",
      "reference": "6/2011"
    },
    {
      "date": "2011-03-14",
      "defendant": " Kummissarju tat-Taxxi Interni ",
      "keywords": [
        "\u201cC\u201d",
        "\u2018condoim\u2019",
        "biex",
        "Qrati",
        "r-Rikorrent"
      ],
      "prosecutor": "Dennis Borg (I.D. Nru. 381474M) u Sylvana Borg (I.D. Nru. 56477M) ",
      "reference": "34/2010"
    }
  ]
}
```

### /cases/appeals
N.B.: This method is currently outputting duplicate results, due to the internal relationship between case
and appeal nodes.

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
    },
    {
      "court_name": "The Administrative Review Tribunal",
      "date": "2013-01-25",
      "defendant": " Awtorit\u00e0 ghat-Trasport f\u2019Malta ",
      "j_name": "GABRIELLA",
      "j_surname": "VELLA",
      "keywords": [
        "\u201c22",
        "nghaw",
        "l-Awtorit\u00e0",
        "ml-",
        "moghtija"
      ],
      "node_name": "GVELLA",
      "pdf": "script_get_judgement_document.aspx?CaseJudgementID=78919",
      "prosecutor": "Joseph Bajada (Karta ta\u2019 l-Identit\u00e0 bin-Numru 24466G) u S B Autocentre Limited (C-16378) ",
      "reference": "1/2011/1"
    },
    {
      "court_name": "The Administrative Review Tribunal",
      "date": "2013-01-25",
      "defendant": " Awtorit\u00e0 ghat-Trasport f\u2019Malta ",
      "keywords": [
        "\u201c22",
        "nghaw",
        "l-Awtorit\u00e0",
        "ml-",
        "moghtija"
      ],
      "pdf": "script_get_judgement_document.aspx?CaseJudgementID=78919",
      "prosecutor": "Joseph Bajada (Karta ta\u2019 l-Identit\u00e0 bin-Numru 24466G) u S B Autocentre Limited (C-16378) ",
      "reference": "1/2011/1",
      "year": "2012"
    },
    {
      "court_name": "The Administrative Review Tribunal",
      "date": "2012-10-19",
      "defendant": " Awtorit\u00e0 ghat-Trasport f\u2019Malta ",
      "keywords": [
        "-pocy",
        "\u201cB\u2019ittra",
        "xi",
        "xxa",
        "ai"
      ],
      "prosecutor": "Joseph Bajada (Karta ta\u2019 l-Identit\u00e0 bin-Numru 24466G) u S.B. Autocentre Limited (C-16378) ",
      "reference": "6/2011/1",
      "year": "2011"
    }
  ]
}
```

### /cases
Deprecrated

### /cases/defendant/{defendant_surname}/{defendant_name}
Sample call:
`` http://localhost:5000/api/0.1/json/cases/defendant/howie/andrew ``

Sample output:
``` json

```

### /cases/prosecutor/{prosecutor_surname}/{prosecutor_name}
Sample call:
`` http://localhost:5000/api/0.1/json/cases/prosecutor/gillford/brian ``

Sample output:
``` json
{
  "response": [
    {
      "court_name": "European Small Claims Procedure",
      "date": "2011-06-16",
      "defendant": " Andrew Howie This ",
      "keywords": [
        "\u0127sara",
        "acts",
        "\fKopja",
        "fejn",
        "kollha"
      ],
      "pdf": "script_get_judgement_document.aspx?CaseJudgementID=68667",
      "prosecutor": "Brian Gilford ",
      "reference": "2/2011",
      "year": "2011"
    },
    {
      "court_name": "European Small Claims Procedure",
      "date": "2011-06-16",
      "defendant": " Andrew Howie This ",
      "j_name": "GRETA",
      "j_surname": "MIFSUD",
      "keywords": [
        "\u0127sara",
        "acts",
        "\fKopja",
        "fejn",
        "kollha"
      ],
      "node_name": "GMIFSUD",
      "pdf": "script_get_judgement_document.aspx?CaseJudgementID=68667",
      "prosecutor": "Brian Gilford ",
      "reference": "2/2011"
    }
  ]
}
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