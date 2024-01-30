// custom.js

var map;
var markers = [];

function initMap() {
    const businessLocation = { lat: 34.052235, lng: -118.243683 }; // Los Angeles coordinates
    map = new google.maps.Map(document.getElementById("map"), {
        center: businessLocation,
        zoom: 10,
        mapId: "bcfd2582bc108b99"
    });

    // Add a marker at the center of the ma
    const marker = new google.maps.Marker({
        position: businessLocation,
        map: map,
        title: "Business Location"
    });

    google.maps.event.addListener(map, 'click', async function (event) {
        var color = document.getElementById('colorPicker').value; // Get selected color
        var text = document.getElementById('markerText').value; // Get entered text
        data={lat:event.latLng.lat(), lng:event.latLng.lng(), text:text}
        const response = await fetch("http://127.0.0.1:8000/markers/", {method: "POST", body: JSON.stringify(data)});
        const status = await response.status;
        console.log(status);
        placeMarker(event.latLng, color, text);
    });
}

function placeMarker(location, color, text) {
    var marker = new google.maps.Marker({
        position: location,
        map: map,
        icon: {
            path: google.maps.SymbolPath.CIRCLE,
            fillColor: color,
            fillOpacity: 1,
            strokeColor: '#fff',
            strokeWeight: 2,
            scale: 10
        }
    });

  // information about the marker
    var markerInfo = {
        position: location,
        color: color,
        text: text
    };

    markers.push(markerInfo);

    // 'text'

    var infowindow = new google.maps.InfoWindow({
        content: text
    });

    google.maps.event.addListener(marker, 'click', function () {
        infowindow.open(map, marker);
    });
}
