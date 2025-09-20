import {
    resetButtonsDay,
    addButtonsDayClickEvent,
    render_location_selector,
    displayLocationName,
    showLoading,
    displayWeatherDay,
} from "./index.js";
import { updateChart } from "./chart.js";

render_location_selector(fetchWeather, resetButtonsDay)
resetButtonsDay();
fetchWeather(localStorage.getItem('lastLocation') || 'ho_chi_minh', 0);
addButtonsDayClickEvent(fetchWeather);


async function fetchWeather(location, day_index) {
    showLoading(true);
    try {
        const data = await sendRequest(location, day_index)
        // update chart
        updateChart(data.data.weather_hourly)
        showLoading(false);
        // console.log("DATA: ", data.data);
        displayLocationName(location);
        // display data
        displayWeatherDay(
            data.data.temperature_max,
            data.data.temperature_min,
            data.data.day_description,
            data.data.night_description
        )
        localStorage.setItem('lastLocation', location);
    } catch (err) {
        console.error("ERROR:", err);
        showLoading(false);
    }
}

async function sendRequest(nameNoSign, day = 0) {
    const response = await fetch(`/weather?location=${encodeURIComponent(nameNoSign)}&day=${day}`);
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
}