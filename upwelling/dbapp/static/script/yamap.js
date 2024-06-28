"use strict";

var yaMap;

const API_KEY = '08bbb439-3bb4-4624-9139-732963ddac86';

var RECORDS_URL = '/api/v1/records/?api_key=${API_KEY}';

let resevoirs = [{
    "name": "Балтийское море",
    "x": 59.20,
    "y": 21.25}
];
let resevoir


// window.onload = () => {
//     const yaScript = document.createElement('script');
//     yaScript.setAttribute(
//         'src',
//         'https://api-maps.yandex.ru/2.1/?apikey=08bbb439-3bb4-4624-9139-732963ddac86&lang=ru_RU'
//     );
//     yaScript.addEventListener('load', () => {
//         console.log('map loaded');
//     });
//     document.body.appendChild(yaScript);
// }

ymaps.ready(init);
function init() {
    yaMap = new ymaps.Map("map", {
        center: [59.20, 21.25],
        zoom: 5,
        type: 'yandex#satellite',
        controls: ['zoomControl', 'fullscreenControl', 'rulerControl']
    });
    var objectManager = new ymaps.ObjectManager({
        clusterize: true,
        gridSize: 32,
        clusterDisableClickZoom: true
    });

    objectManager.objects.options.set('preset', 'islands#greenDotIcon');
    objectManager.clusters.options.set('preset', 'islands#greenDotIcon');
    yaMap.geoObjects.add(objectManager);

    $.ajax({
        url: "points_data/"
    }).done(function(data) {
        console.log(data)
        objectManager.add(data);
    });

    // var myPlacemark = new ymaps.Placemark([55.40, 20.50], { 
    //     iconContent: '1', 
    //     balloonContent: 'Балтийское море' 
    // }, {
    //     preset: 'twirl#blueStretchyIcon'
    // });
    // yaMap.geoObjects.add(myPlacemark);

    // var myPlacemark = new ymaps.Placemark([55.80, 20.50], { 
    //     iconContent: '2', 
    //     balloonContent: 'Балтийское море' 
    // }, {
    //     preset: 'twirl#blueStretchyIcon'
    // });
    // yaMap.geoObjects.add(myPlacemark);

    // var myPlacemark = new ymaps.Placemark([55.90, 20.60], { 
    //     iconContent: '3', 
    //     balloonContent: 'Балтийское море' 
    // }, {
    //     preset: 'twirl#blueStretchyIcon'
    // });
    // yaMap.geoObjects.add(myPlacemark);

    // var myPlacemark = new ymaps.Placemark([56.30, 20.60], { 
    //     iconContent: '4', 
    //     balloonContent: 'Балтийское море' 
    // }, {
    //     preset: 'twirl#blueStretchyIcon'
    // });
    // yaMap.geoObjects.add(myPlacemark);

    // var myPlacemark = new ymaps.Placemark([56.60, 20.80], { 
    //     iconContent: '5', 
    //     balloonContent: 'Балтийское море' 
    // }, {
    //     preset: 'twirl#blueStretchyIcon'
    // });
    // yaMap.geoObjects.add(myPlacemark);

    // var myPlacemark = new ymaps.Placemark([57.60, 20.60], { 
    //     iconContent: '6', 
    //     balloonContent: 'Балтийское море' 
    // }, {
    //     preset: 'twirl#blueStretchyIcon'
    // });
    // yaMap.geoObjects.add(myPlacemark);

    // var myPlacemark = new ymaps.Placemark([54.70, 19.90], { 
    //     iconContent: '7', 
    //     balloonContent: 'Балтийское море' 
    // }, {
    //     preset: 'twirl#blueStretchyIcon'
    // });
    // yaMap.geoObjects.add(myPlacemark);

    // var myPlacemark = new ymaps.Placemark([54.90, 19.80], { 
    //     iconContent: '8', 
    //     balloonContent: 'Балтийское море' 
    // }, {
    //     preset: 'twirl#blueStretchyIcon'
    // });
    // yaMap.geoObjects.add(myPlacemark);

    // var myPlacemark = new ymaps.Placemark([57.90, 20.90], { 
    //     iconContent: '9', 
    //     balloonContent: 'Балтийское море' 
    // }, {
    //     preset: 'twirl#blueStretchyIcon'
    // });
    // yaMap.geoObjects.add(myPlacemark);

    // var myPlacemark = new ymaps.Placemark([58.00, 21.00], { 
    //     iconContent: '10', 
    //     balloonContent: 'Балтийское море' 
    // }, {
    //     preset: 'twirl#blueStretchyIcon'
    // });
    // yaMap.geoObjects.add(myPlacemark);

    // var json = {{ points | safe }};
    // var json_p = JSON.parse(json);

    // console.log(json)


    // var points = document.getElementById('jsonData').getAttribute('data-json');
    // var point;

    // points = JSON.parse(points)

    // console.log(points)

    // points.forEach(point => {


    //     if (point["fields"]["coordinate_x"] == 'none' && point["fields"]["coordinate_y"] == 'none') {
    //         resevoirs.forEach(resevoir => {
    //             if (point["fields"]["reservoir"] == resevoir["name"]) {
    //                 point["fields"]["coordinate_x"] = resevoir["x"];
    //                 point["fields"]["coordinate_y"] = resevoir["y"];
    //             }
    //         });
    //     }
    //     var x_coord = point["fields"]["coordinate_x"];
    //     var y_coord = point["fields"]["coordinate_y"];

    //     if (point["fields"]["longitude"] == 'W') x_coord = -x_coord;
    //     if (point["fields"]["latitude"] == 'S') y_coord = -y_coord;

    //     var myPlacemark = new ymaps.Placemark([x_coord, y_coord], { 
    //         iconContent: point["pk"], 
    //         balloonContent: point["fields"]["measurment_place"]
    //     }, {
    //         preset: 'twirl#blueStretchyIcon'
    //     });
    //     yaMap.geoObjects.add(myPlacemark);

    //     console.log(point["fields"])

    //     console.log(myPlacemark)
    // });

}

