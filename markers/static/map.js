
function map_init_basic(map, options) {
  map.locate()
    .on('locationfound', e => map.setView(e.latlng, 8))
    .on('locationerror', () => map.setView([0, 0], 5))
  async function load_markers() {
    const markers_url = `/api/markers/?in_bbox=${map.getBounds().toBBoxString()}`
    const response = await fetch(markers_url)
    const geojson = await response.json()
    return geojson
  }
  async function render_markers() {
    const markers = await load_markers()
    L.geoJSON(markers).bindPopup(layer => "<strong>" + layer.feature.properties.name + "<br><br>" + layer.feature.properties.uprn + "</strong><br><br>" + layer.feature.properties.description + "<br><br>" + "<a href=" + layer.feature.properties.linked_document + " target='_blank' >" + layer.feature.properties.linked_document + "<\a>").addTo(map)
  }
  map.on('moveend', render_markers)
}