// Global variables
let map;
let markers = [];
let activeInfoWindow = null;

// DOM Elements
const elRegionSelect = document.getElementById('select-region');
const elCitySelect = document.getElementById('select-city');
const elBankSelect = document.getElementById('select-bank');
const elSearchForm = document.getElementById('search-form');
const elInfoMessage = document.getElementById('info-message');

/**
 * Initialize the application on DOM Content Loaded
 */
document.addEventListener('DOMContentLoaded', () => {
  setupDropdowns();
  checkAndLoadKakaoMap();
});

/**
 * Check and load Kakao Maps SDK
 */
function checkAndLoadKakaoMap() {
  const isKeyConfigured = typeof API_KEY !== 'undefined' && API_KEY && API_KEY !== 'YOUR_KAKAOMAP_JAVASCRIPT_KEY_HERE';

  if (!isKeyConfigured) {
    updateInfoMessage('카카오 지도 API 키 설정이 필요합니다 (apikey.js).');
    return;
  }

  const script = document.createElement('script');
  script.type = 'text/javascript';
  script.src = `https://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${API_KEY}&libraries=services`;
  
  script.onload = () => {
    kakao.maps.load(() => {
      initMap();
    });
  };
  
  script.onerror = () => {
    updateInfoMessage('카카오 지도 SDK를 로드하는 데 실패했습니다.');
  };

  document.head.appendChild(script);
}

/**
 * Initialize the Kakao Map at Gangnam Station (F1002)
 */
function initMap() {
  const container = document.getElementById('map');
  const gangnamCoords = new kakao.maps.LatLng(37.49818, 127.027386);
  
  const options = {
    center: gangnamCoords,
    level: 3
  };

  map = new kakao.maps.Map(container, options);

  // Add controls
  const mapTypeControl = new kakao.maps.MapTypeControl();
  map.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT);

  const zoomControl = new kakao.maps.ZoomControl();
  map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);

  updateInfoMessage('지도 로드 성공! 강남역을 기준으로 중심이 설정되었습니다.');
  
  elSearchForm.addEventListener('submit', handleSearchSubmit);
}

/**
 * Populate the cascading select boxes (F1003)
 */
function setupDropdowns() {
  // Populate Region Select
  if (typeof BANK_DATA !== 'undefined' && BANK_DATA.mapInfo) {
    BANK_DATA.mapInfo.forEach(region => {
      const option = document.createElement('option');
      option.value = region.name;
      option.textContent = region.name;
      elRegionSelect.appendChild(option);
    });
  }

  // Region change listener
  elRegionSelect.addEventListener('change', () => {
    resetSelect(elCitySelect, '시/군/구를 선택해 주세요');
    resetSelect(elBankSelect, '은행을 선택해 주세요');
    
    const selectedRegion = BANK_DATA.mapInfo.find(r => r.name === elRegionSelect.value);
    if (selectedRegion && selectedRegion.countries) {
      elCitySelect.disabled = false;
      selectedRegion.countries.forEach(city => {
        const option = document.createElement('option');
        option.value = city;
        option.textContent = city;
        elCitySelect.appendChild(option);
      });
      updateInfoMessage('광역시/도가 선택되었습니다. 시/군/구를 선택해 주세요.');
    }
  });

  // City change listener
  elCitySelect.addEventListener('change', () => {
    resetSelect(elBankSelect, '은행을 선택해 주세요');
    
    if (BANK_DATA.bankInfo) {
      elBankSelect.disabled = false;
      BANK_DATA.bankInfo.forEach(bank => {
        const option = document.createElement('option');
        option.value = bank;
        option.textContent = bank;
        elBankSelect.appendChild(option);
      });
      updateInfoMessage('시/군/구가 선택되었습니다. 은행명을 선택하고 검색 버튼을 눌러주세요.');
    }
  });
}

/**
 * Reset select element
 */
function resetSelect(selectEl, placeholderText) {
  selectEl.innerHTML = '';
  const defaultOpt = document.createElement('option');
  defaultOpt.value = '';
  defaultOpt.disabled = true;
  defaultOpt.selected = true;
  defaultOpt.textContent = placeholderText;
  selectEl.appendChild(defaultOpt);
  selectEl.disabled = true;
}

/**
 * Update message pill
 */
function updateInfoMessage(message) {
  if (elInfoMessage) {
    elInfoMessage.textContent = message;
  }
}

/**
 * Handle form submission (F1004)
 */
function handleSearchSubmit(event) {
  event.preventDefault();
  
  if (!map) {
    updateInfoMessage('지도가 아직 로드되지 않았습니다.');
    return;
  }

  const region = elRegionSelect.value;
  const city = elCitySelect.value;
  const bank = elBankSelect.value;

  const searchQuery = `${region} ${city} ${bank}`;
  updateInfoMessage(`'${searchQuery}' 검색 중...`);

  const ps = new kakao.maps.services.Places();
  ps.keywordSearch(searchQuery, (data, status) => {
    handlePlacesSearchCallback(data, status, bank);
  });
}

/**
 * Places Search Callback
 */
function handlePlacesSearchCallback(data, status, bankName) {
  clearMarkers();
  
  if (activeInfoWindow) {
    activeInfoWindow.close();
    activeInfoWindow = null;
  }

  if (status === kakao.maps.services.Status.OK) {
    const selectedCity = elCitySelect.value;
    
    // Filter results to match selected city
    let filteredData = data.filter(place => {
      const addr = place.address_name || '';
      const roadAddr = place.road_address_name || '';
      return addr.includes(selectedCity) || roadAddr.includes(selectedCity);
    });

    if (filteredData.length === 0) {
      filteredData = data;
    }

    const bounds = new kakao.maps.LatLngBounds();

    filteredData.forEach(place => {
      const position = new kakao.maps.LatLng(place.y, place.x);
      
      const marker = new kakao.maps.Marker({
        map: map,
        position: position
      });

      markers.push(marker);
      bounds.extend(position);

      // Marker click listener (InfoWindow showing branch name and address)
      kakao.maps.event.addListener(marker, 'click', () => {
        if (activeInfoWindow) {
          activeInfoWindow.close();
        }

        const infoWindowContent = `
          <div style="padding:10px; font-family:sans-serif; min-width:200px;">
            <span style="display:inline-block; background-color:#e0f2fe; color:#0369a1; font-size:11px; font-weight:bold; padding:2px 6px; border-radius:4px; margin-bottom:6px;">${bankName}</span>
            <div style="font-size:14px; font-weight:bold; color:#007aff; margin-bottom:4px;">${place.place_name}</div>
            <div style="font-size:12px; color:#333;">
              ${place.road_address_name ? place.road_address_name : place.address_name}
            </div>
          </div>
        `;

        const infowindow = new kakao.maps.InfoWindow({
          content: infoWindowContent,
          removable: true
        });

        infowindow.open(map, marker);
        activeInfoWindow = infowindow;
        map.panTo(position);
      });
    });

    // Fit map bounds
    if (filteredData.length === 1) {
      map.setCenter(new kakao.maps.LatLng(filteredData[0].y, filteredData[0].x));
      map.setLevel(4);
    } else {
      map.setBounds(bounds);
    }
    
    updateInfoMessage(`'${bankName}' 지점 ${filteredData.length}곳을 찾았습니다! 마커를 클릭하여 정보를 확인하세요.`);

  } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
    updateInfoMessage('검색 결과가 존재하지 않습니다. 다른 지역을 선택해 보세요.');
  } else {
    updateInfoMessage('검색 중 에러가 발생했습니다.');
  }
}

/**
 * Clear existing markers
 */
function clearMarkers() {
  markers.forEach(marker => marker.setMap(null));
  markers = [];
}
