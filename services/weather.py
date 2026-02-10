from datetime import datetime, timezone

import requests

from config import OPENWEATHER_API_KEY

OWM_CURRENT_URL = "https://api.openweathermap.org/data/2.5/weather"


def format_weather(data: dict) -> str:
    name = data.get("name")
    sys = data.get("sys", {})
    country = sys.get("country", "")
    main = data.get("main", {})
    weather_list = data.get("weather", [])
    wind = data.get("wind", {})

    description = weather_list[0]["description"] if weather_list else ""
    temp = main.get("temp")
    feels_like = main.get("feels_like")
    humidity = main.get("humidity")
    wind_speed = wind.get("speed")

    ts = data.get("dt")
    updated_at = ""
    if ts:
        updated_at = datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    return (
        f"Thời tiết hiện tại ở {name} {country}\n"
        f"Mô tả: {description}\n"
        f"Nhiệt độ: {temp}°C (cảm giác: {feels_like}°C)\n"
        f"Độ ẩm: {humidity}%\n"
        f"Gió: {wind_speed} m/s\n"
        f"Cập nhật: {updated_at}"
    )


def get_weather_message(location: str) -> str:
    if not OPENWEATHER_API_KEY:
        return "Thiếu OPENWEATHER_API_KEY. Hãy cấu hình trong file .env"

    params = {
        "q": location,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "vi",
    }

    try:
        resp = requests.get(OWM_CURRENT_URL, params=params, timeout=10)
        data = resp.json()
        if resp.status_code != 200:
            message = data.get("message", "Không tìm thấy địa điểm.")
            return f"Lỗi: {message}"

        return format_weather(data)
    except requests.RequestException:
        return "Không thể kết nối tới OpenWeather. Thử lại sau."
