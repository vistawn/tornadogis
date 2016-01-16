{
	"name":"china",
	"default_scale":25000000,
	"default_extent":{
		"xmin":60,
      	"ymin":5,
      	"xmax":147,
      	"ymax":68
		},
	"wkid":4326,
	"workspace":{
		"postgis_1":{
			"type":"postgis",
			"host":"10.211.55.8",
			"dbname":"gisdb",
			"user":"postgres",
			"password":"admin"
		},
		"postgis_2":{
			"type":"postgis",
			"host":"10.211.55.8",
			"dbname":"gisdb",
			"user":"postgres",
			"password":"admin"
		}
	},
	"layers":[
		{
			"layername":"province_city_point",
			"id":0,
			"min_scale":0,
			"max_scale":0,
			"datasource":{
				"workspace":"postgis_1"
			},
			"renderer":{
				"type":"single",
				"style": {
		            radius: 4,
					fillColor: "#ff7800",
					color: "#000",
					weight: 1,
					opacity: 1,
					fillOpacity: 0.8
	        	}
	        }
		},
		{
			"layername":"river_line",
			"id":1,
			"min_scale":2000000,
			"max_scale":0,
			"datasource":{
				"workspace":"postgis_1"
			},
			"renderer":{
				"type":"single",
				"style": {
		            "color": '#f00',
		            "weight": 4, 
		            "opacity": 0.4
	        	}
	        }
		},
		{
			"layername":"railway_line",
			"id":2,
			"min_scale":15000000,
			"max_scale":0,
			"datasource":{
				"workspace":"postgis_1"
			},
			"renderer":{
				"type":"single",
				"style": {
		            "color": '#f00',
		            "weight": 4, 
		            "opacity": 0.4
	        	}
	        }
		},
		{
			"layername":"mainroad_line",
			"id":3,
			"min_scale":15000000,
			"max_scale":0,
			"datasource":{
				"workspace":"postgis_1"
			},
			"renderer":{
				"type":"single",
				"style": {
		            "color": '#f00',
		            "weight": 4, 
		            "opacity": 0.4
	        	}
	        }
		},
		{
			"layername":"prefecture_polygon",
			"id":4,
			"min_scale":900000,
			"max_scale":0,
			"datasource":{
				"workspace":"postgis_1"
			},
			"renderer":{
				"type":"single",
				"style": {
					"weight": 2,
	                "color": "#999",
	                "opacity": 1,
	                "fillColor": "#B0DE5C",
	                "fillOpacity": 0.8
	        	}
	        }
		},
		{
			"layername":"province_polygon",
			"id":5,
			"min_scale":0,
			"max_scale":900000,
			"datasource":{
				"workspace":"postgis_1"
			},
			"renderer":{
				"type":"single",
				"style": {
		            "weight": 2,
	                "color": "#999",
	                "opacity": 1,
	                "fillColor": "#B0DE5C",
	                "fillOpacity": 0.8
	        	}
	        }
		}
	]
}