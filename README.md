# CODe API

REST API served from Civil Cases database

## API

### /case/<reference_p1>/<reference_p2>

### /cases/date/<date>

### /cases/year/<int:year>

### /cases/query

### /cases/defendant/<defendant_surname>/<defendant_name>

### /cases/prosecutor/<prosecutor_surname>/<prosecutor_name>

### /cases/prosecutor/<prosecutor_surname>/<prosecutor_name>

### /cases/judges/<judge_surname>/<judge_name>

### /cases/keywords/<keywords>

### 404 Error
This will always look like:
'''json
{"error": "Not found"}
'''

### 500 Error
This will always look like:
'''json
{"error": "Internal error"}
'''