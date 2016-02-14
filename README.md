# TornadoGIS Server

TornadoGIS Server is a tiny GIS server based on Tornado Web framework.

## Installation

1. Install Python 2.7
2. Install Tornado
3. Install psycopg2
4. Start Server

> python main.py



## Features

- [x] Server/Service information API
- [x] Layer query REST API
- [x] Simple GeoJSON map output
- [ ] Tiled GeoJSON map output
- [ ] Permission
- [x] Log supported

## Structure

```
tornadogis    ##root folder] 
  |--Config    ##server and services file] 
  |   |--services    ##map service definition files 
  |   |--server.conf    ##gis server configuration file 
  | 
  |--db    ## database operation module 
  |--doc    ## documents 
  |--log    ## server log files 
  |--server    ## 
  |--static    ## tornado framework's static files folder
  |--templates    ## tornado framework's template folder. 
  |--util    ## common utilies
  |--main.py    ## server init
  |--settings.py    ##tornado settings
  |--urls.py    
```


