
var map = L.map('map').setView([40.0985, -88.2291], 13);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

/*
markers used as placeholders for now
 */
L.marker([40.0985, -88.2291]).addTo(map);
L.marker([40.1, -88.234]).addTo(map);
L.marker([40.11, -88.254]).addTo(map);