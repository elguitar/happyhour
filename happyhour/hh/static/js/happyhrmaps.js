/* global L */

"use strict";

var map;
var lat = 61.498167;
var lng = 23.760833;
var zoom = 15;
var bars;

// Timeout is defined to limit the amount of api call if someone goes berserk with clicking
// Minus 1s is just a hack to let the first fetch succeed
var timeout = Date.now() - 1000;

// Passion lat: 61.4985, lng: 23.77786

function init_map() {
	map = new L.Map("map").setView([lat, lng], zoom);
	L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}.png', {
		maxZoom: 20,
		minZoom: 10,
		attribution: 'Map tiles by <a href="https://stamen.com">Stamen Design</a>, under <a href="https://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="https://openstreetmap.org">OpenStreetMap</a>, under <a href="https://creativecommons.org/licenses/by-sa/3.0">CC BY SA</a>',
		subdomains: 'abc',
	}).addTo(map);
}

init_map();
/*
var bounds = map.getBounds();
var northwest = bounds.getNorthWest;
url = 'http://localhost:8000/api/map/bars/' + bounds()
*/

//var bounds = map.getBounds();
function fetch_data() {
	if (Date.now() - timeout > 1000) {
		fetch('http://192.81.222.238/api/bars/')
			.then(res => res.json())
			.then(data => bars = data)
			.then(function(bars){
				let bounds = map.getBounds();
				for (let i=0;i<bars.length;i++){
					let latitude = parseFloat(bars[i]['latitude']);
					let longitude = parseFloat(bars[i]['longitude']);
					let latlng = L.latLng(latitude, longitude);
					if (bounds.contains(latlng)){
						let marker = L.marker(latlng);
						marker.addTo(map);
						marker.bindPopup(bars[i]['name']);
					}
				}
			})
			.catch(function(err){
				console.log(err);
			});
			timeout = Date.now();
	}

	var popup = L.popup();
}
fetch_data();
/*
function onMapClick(e) {
	    popup
	        .setLatLng(e.latlng)
	        .setContent("You clicked the map at " + e.latlng.toString())
	        .openOn(map);
}

map.on('click', onMapClick);
*/
map.on('moveend', fetch_data);
