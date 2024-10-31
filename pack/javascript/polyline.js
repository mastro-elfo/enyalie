var featureGroup = null;

function addPolyline(mapId, id, trkpts) {
  var map = getElement(mapId).map;
  if (!featureGroup) {
    featureGroup = new L.featureGroup([]);
  }
  map.addLayer(featureGroup);
  var polyline = L.polyline(trkpts, { color: "red" })
    .on("click", function (e) {
      emitEvent("polyline-click", { index: e.target._ix });
    })
    .addTo(featureGroup);
  polyline._ix = id;
}
