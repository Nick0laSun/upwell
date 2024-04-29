"use strict";

var yaMap;

const API_KEY = '08bbb439-3bb4-4624-9139-732963ddac86'

var RECORDS_URL = '/api/v1/records/?api_key=${API_KEY}';

let resevoirs = [{
    "name": "Балтийское море",
    "x": 59.20,
    "y": 21.25}
];
let resevoir;



ymaps.ready(init);
function init(){
    yaMap = new ymaps.Map("map", {
        center: [59.20, 21.25],
        zoom: 5,
        type: 'yandex#satellite',
        controls: ['zoomControl', 'fullscreenControl', 'rulerControl']
    });

    var points = JSON.parse('{{ points }}');
    var point;

    for (point of points) {
        
        if (point.coordinate_x == 'none' && point.coordinate_y == 'none') {
            for (resevoir of resevoirs) {
                if (point.reservoir == resevoir["name"]) {
                    point.coordinate_x = resevoir["x"];
                    point.coordinate_y = resevoir["y"];
                }
            }
        }
        var x_coord = point.coordinate_x;
        var y_coord = point.coordinate_y;

        if (point.longitude == 'W') x_coord = -x_coord;
        if (point.latitude == 'S') y_coord = -y_coord;

        var yaPoint = new ymaps.GeoObject({
            geometry: {
                type: "Point",
                coordinates: [x_coord, y_coord]
            }
        });
        
        yaMap.geoObjects.add(yaPoint);
    }
}