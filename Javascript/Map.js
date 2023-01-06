//Map setup
            
var map = L.map('map', {
  fullscreenControl: true,
  fullscreenControlOptions: {
      
  }
}).setView([40.863380, -99.681242], 4, {animate: false});


L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}@2x.png', {
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
	subdomains: 'abcd',
	maxZoom: 20
}).addTo(map); ;



const sidepanelRight = L.control.sidepanel('mySidepanelRight', {
			panelPosition: 'right',
			tabsPosition: 'top',
			pushControls: true,
			darkMode: true,
			startTab: 2
		}).addTo(map);



