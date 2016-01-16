# -*- coding:utf-8 -*-
import psycopg2

conns = dict()

def fetch_json_with_bbox(service_json,layerid,tablename, bbox):
    cur = conns[service_json["name"] + "_" + service_json["layers"][layerid]["datasource"]["workspace"]]

    sql = "select row_to_json(fc)" \
          " FROM (select 'FeatureCollection' As type, array_to_json(array_agg(f)) As features" \
          " FROM (select 'Feature' As type, ST_AsGeoJSON(lg.geom)::json As geometry, row_to_json((select l " \
          " FROM (select %s " \
          ") As l)) As properties FROM %s" \
          " As lg where ST_Intersects(geom,ST_MakeEnvelope(%s" \
          "))) As f )  As fc;" %(fetch_column_names(cur,tablename), str(tablename),str(bbox))
    print sql
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        return row[0]


def fetch_column_names(cur,tablename):
    sql = "select column_name from information_schema.columns where table_name='%s';" %tablename
    cur.execute(sql)
    rows = cur.fetchall()
    cols=''
    for row in rows:
        if row[0]<>'geom':
            cols+=row[0] + ','
    return cols[:-1]

def connectdb(servicename,workspace_name,dbconfig):
    connstr = "host='%s' dbname='%s' user='%s' password='%s'" %(dbconfig["host"],dbconfig["dbname"],dbconfig["user"],dbconfig["password"])
    conn = psycopg2.connect(connstr)
    cur = conn.cursor()
    conns[servicename + "_" + workspace_name] = cur


