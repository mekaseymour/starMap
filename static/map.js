var map;
// Create a new blank array for all the listing markers.
var markers = [];
function initMap() {
  // Constructor creates a new map - only center and zoom are required.
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 37.8393, lng: -84.2700},
    zoom: 3,
    mapTypeControl: false,
    styles: [
       {
         "featureType": "administrative.neighborhood",
         "stylers": [
           {
             "visibility": "off"
           }
         ]
       },
       {
         "featureType": "road.highway",
         "elementType": "geometry.fill",
         "stylers": [
           {
             "visibility": "off"
           }
         ]
       },
       {
         "featureType": "road",
         "stylers": [
           {
             "visibility": "off"
           }
         ]
       },
       {
         "featureType": "water",
         "elementType": "labels.text",
         "stylers": [
           {
             "visibility": "off"
           }
         ]
       },
    ]
  });
  // setting this so the map can't just zoom out forever
  map.setOptions({ minZoom: 3, maxZoom: 50 });

  // These are the real estate listings that will be shown to the user.
  // Normally we'd have these in a database instead.
  var locations = [
    {title: 'Beyonce', location: {lat: 29.7604, lng: -95.3698}, icon: 'http://imageshack.com/a/img924/3972/FWNstD.png', type: 'musicians', quote: '\"I\'m a human being\" - B'},
    {title: 'Barack Obama', location: {lat: 21.3069, lng: -157.8583}, icon: 'http://imageshack.com/a/img924/1223/ci0iYg.png', type: 'public figures', quote: '\"Just a Hawaii boy *wink*\" - BO'},
    {title: 'Justin Bieber', location: {lat: 42.9870, lng: -81.2432}, icon: 'http://imageshack.com/a/img924/6798/vWIELU.png', type: 'musicians', quote: '\"Haters are just confused admirers.\" - JB'},
    {title: 'Michelle Obama', location: {lat: 41.8781, lng: -87.6298}, icon: 'http://imageshack.com/a/img924/7969/trSAlA.png', type: 'public figures', quote: '\"So much history yet to be made.\" - MO'},
    {title: 'Lebron James', location: {lat: 41.0814, lng: -81.5190}, icon: 'http://imageshack.com/a/img923/6185/tf3EF5.png', type: 'athletes', quote: '\"I\'m still working out at my old high school.\" - LJ'},
    {title: 'Mark Zuckerberg', location: {lat: 41.0340, lng: -73.7629}, icon: 'http://imageshack.com/a/img923/7095/HAMELW.png', type: 'bosses', quote: '\"People love photos\" - MZ'},
    {title: 'Nelson Mandela', location: {lat: -31.9407, lng: 28.5492}, icon: 'http://imageshack.com/a/img921/3872/B41J07.png', type: 'public figures', quote: '\"It always seems impossible until it\'s done.\" - NM'},
    {title: 'Mindy Kaling', location: {lat: 42.3736, lng: -71.1097}, icon: 'http://imageshack.com/a/img922/7094/SvKwiq.png', type: 'big screens', quote: '\"Fast food is hugely important in the life of a comedy writer.\" - MK'},
    {title: 'Elon Musk', location: {lat: -25.7479, lng: 28.2293}, icon: 'http://imageshack.com/a/img922/2827/P14l9H.png', type: 'bosses', quote: '\"I would like to die on Mars.\" - EM'},
    {title: 'Adele', location: {lat: 51.6050, lng: -0.0723}, icon: 'http://imageshack.com/a/img924/9344/WJQPHs.png', type: 'musicians', quote: '\"Hello, it\'s me..\" - A'},
    {title: 'Ellen', location: {lat: 29.9841, lng: -90.1529}, icon: 'http://imageshack.com/a/img922/773/De4uHw.png', type: 'big screens', quote: '\"I still have the shirt I wore my first time on Johnny Carson\'s show.\" - E'},
    {title: 'Neymar', location: {lat: -23.5213, lng: -46.1859}, icon: 'http://imageshack.com/a/img923/603/3H6uHv.png', type: 'athletes', quote: '\"I was born to be happy not perfect.\" - N'},
    {title: 'Yao Ming', location: {lat: 31.2304, lng: 121.4737}, icon: 'http://imageshack.com/a/img923/3452/T3eRur.png', type: 'athletes', quote: '\"Friendship first, competition second.\" - YM'},
    {title: 'Malala', location: {lat: 34.7717, lng: 72.3602}, icon: 'http://imageshack.com/a/img921/5057/qg8KNb.png', type: 'public figures', quote: '\"All I want is an education, and I am afraid of no one.\" - M'}
  ];
  var largeInfowindow = new google.maps.InfoWindow();
  // The following group uses the location array to create an array of markers on initialize.
  for (var i = 0; i < locations.length; i++) {
    // Get the position from the location array.
    var position = locations[i].location;
    var title = locations[i].title;
    var icon = locations[i].icon;
    var type = locations[i].type;
    var quote = locations[i].quote;
    // Create a marker per location, and put into markers array.
     var marker = new google.maps.Marker({
      position: position,
      title: title,
      icon: icon,
      type: type,
      quote: quote,
      animation: google.maps.Animation.DROP,
      id: i
    });
    // Push the marker to our array of markers.
    markers.push(marker);
    // Create an onclick event to open an infowindow at each marker.
    marker.addListener('click', function() {
      populateInfoWindow(this, largeInfowindow);
    });
  }
  document.getElementById('show').addEventListener('click', showListings);
  document.getElementById('hide').addEventListener('click', hideListings);
}
// This function populates the infowindow when the marker is clicked. We'll only allow
// one infowindow which will open at the marker that is clicked, and populate based
// on that markers position.
function populateInfoWindow(marker, infowindow) {
  // Check to make sure the infowindow is not already opened on this marker.
  if (infowindow.marker != marker) {
    infowindow.marker = marker;
    infowindow.setContent('<div id="infoWindow">' + marker.quote + '</div>');
    infowindow.open(map, marker);
    // Make sure the marker property is cleared if the infowindow is closed.
    infowindow.addListener('closeclick', function() {
      infowindow.marker = null;
    });
  }
}
// This function will loop through the markers array and display them all.
function showListings() {
  var bounds = new google.maps.LatLngBounds();
  // Extend the boundaries of the map for each marker and display the marker
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(map);
    //bounds.extend(markers[i].position);
  }
 // map.fitBounds(bounds);
}
// This function will loop through the listings and hide them all.
function hideListings() {
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(null);
  }
}

// THE MODAL

// get the modal
var modal = document.getElementById('filterModal');

// get the button that opens the modal
var btn = document.getElementById("filterBtn");

// get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// when the user clicks on the button, open the modal
btn.onclick = function() {
modal.style.display = "block";
}

// when the user clicks on <span> (x), close the modal
span.onclick = function() {
modal.style.display = "none";
}

// when the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
if (event.target == modal) {
 modal.style.display = "none";
}
}

// MODAL LOGIC
// shows marker if cooresponding checkbox is checked
// hides marker otherwise
function filterLocations() {
var checkboxes = Array.from(modalForm); // HTMLElement
markers = Array.from(markers); // GoogleMapsGarbageMarker

var checkedCheckboxes = checkboxes.filter((checkbox) => checkbox.checked);

var categoriesToShow = checkedCheckboxes.map(function(checkbox) {
 return checkbox.name;
});

var markersToDisplay = markers.filter((marker) => categoriesToShow.includes(marker.type));

markers.forEach((marker) => marker.setMap(null));

markersToDisplay.forEach(function(marker) {
 marker.setMap(map);
});

modal.style.display = "none";
}
