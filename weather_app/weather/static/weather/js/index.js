const list_location = {
  'ha_noi': 'Thành phố Hà Nội',
  'cao_bang': 'Tỉnh Cao Bằng',
  'tuyen_quang': 'Tỉnh Tuyên Quang',
  'dien_bien': 'Tỉnh Điện Biên',
  'lai_chau': 'Tỉnh Lai Châu',
  'son_la': 'Tỉnh Sơn La',
  'lao_cai': 'Tỉnh Lào Cai',
  'thai_nguyen': 'Tỉnh Thái Nguyên',
  'lang_son': 'Tỉnh Lạng Sơn',
  'quang_ninh': 'Tỉnh Quảng Ninh',
  'bac_ninh': 'Tỉnh Bắc Ninh',
  'phu_tho': 'Tỉnh Phú Thọ',
  'hung_yen': 'Tỉnh Hưng Yên',
  'ninh_binh': 'Tỉnh Ninh Bình',
  'thanh_hoa': 'Tỉnh Thanh Hóa',
  'ha_tinh': 'Tỉnh Hà Tĩnh',
  'quang_tri': 'Tỉnh Quảng Trị',
  'hue': 'Thành phố Huế',
  'da_nang': 'Thành phố Đà Nẵng',
  'quang_ngai': 'Tỉnh Quảng Ngãi',
  'khanh_hoa': 'Tỉnh Khánh Hòa',
  'ho_chi_minh': 'Thành phố Hồ Chí Minh',
  'tay_ninh': 'Tỉnh Tây Ninh',
  'dong_thap': 'Tỉnh Đồng Tháp',
  'vinh_long': 'Tỉnh Vĩnh Long',
  'an_giang': 'Tỉnh An Giang',
  'can_tho': 'Thành phố Cần Thơ',
  'ca_mau': 'Tỉnh Cà Mau',
  'hai_phong': 'Tỉnh Hải Phòng',
  'nghe_an': 'Tỉnh Nghệ An',
  'gia_lai': 'Tỉnh Gia Lai',
  'dak_lak': 'Tỉnh Đắk Lắk',
  'lam_dong': 'Tỉnh Lâm Đồng',
  'dong_nai': 'Tỉnh Đồng Nai',
}
const buttonContainer = document.querySelector('.block-select-day')
// add day & month to buttons
buttonContainer.querySelectorAll('.btn-day').forEach((button, index) => {
  const date = new Date()
  date.setDate(date.getDate() + index);
  const day = date.getDate().toString().padStart(2, '0');
  const month = (date.getMonth() + 1).toString().padStart(2, '0');
  button.innerText = `${day}/${month}`
});


// on off loading animation
const overlay = document.getElementById("loadingOverlay");
export function showLoading(show) {
  overlay.style.display = show ? "flex" : "none";
}



export function addButtonsDayClickEvent(fetchWeather) {
  buttonContainer.addEventListener('click', (event) => {
    const clickedButton = event.target.closest('.btn-day');
    if (clickedButton) {
      // switch aria-selected state of all buttons
      document.querySelectorAll('.btn-day').forEach(btn =>
        btn.setAttribute('aria-selected', 'false')
      );
      // Set true for selected button
      clickedButton.setAttribute('aria-selected', 'true');
      // update chart based on selected day 
      const dayIndex = clickedButton.dataset.index;
      fetchWeather(localStorage.getItem('lastLocation'), dayIndex);
    }
  });
}


export function render_location_selector(fetchWeather, resetButtonsDay) {
  const selector = document.getElementById('locationSelector');
  if (!selector) {
    return;
  }
  // add options from list_location
  for (const [nameNoSign, fullName] of Object.entries(list_location)) {
    const option = document.createElement('option');
    option.value = nameNoSign;
    option.textContent = fullName;
    selector.appendChild(option);
  };
  // button submit
  const buttonSubmit = document.getElementById('btn-submit');
  buttonSubmit.addEventListener('click', () => {
    const location = getSelectedLocation();
    resetButtonsDay();
    fetchWeather(location);
  })
}


export function getSelectedLocation() {
  const selector = document.getElementById('locationSelector');
  return selector.value
}


export function resetButtonsDay() {
  buttonContainer.querySelectorAll('.btn-day').forEach((btn, i) =>
    btn.setAttribute('aria-selected', i === 0)
  );
}


export function displayLocationName(location) {
  document.querySelector('#LocationName').innerText ='Thời tiết tại ' + list_location[location];
}