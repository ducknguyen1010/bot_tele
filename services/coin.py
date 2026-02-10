import requests

from config import CMC_API_KEY


def get_price_message(symbol: str) -> str:
    if not CMC_API_KEY:
        return "Thiếu CMC_API_KEY. Hãy cấu hình trong file .env"

    params = {"symbol": symbol}
    headers = {"X-CMC_PRO_API_KEY": CMC_API_KEY}

    try:
        resp = requests.get(
            "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest",
            params=params,
            headers=headers,
            timeout=10,
        )
        data = resp.json()
        if resp.status_code != 200:
            message = data.get("status", {}).get("error_message", "Không lấy được giá coin.")
            return f"Lỗi: {message}"

        coin = data.get("data", {}).get(symbol)
        if not coin:
            return f"Không tìm thấy coin {symbol}"

        quote = coin.get("quote", {}).get("USD", {})
        price = quote.get("price")
        change_24h = quote.get("percent_change_24h")
        market_cap = quote.get("market_cap")

        arrow = "➡️"
        if isinstance(change_24h, (int, float)):
            if change_24h > 0:
                arrow = "📈"
            elif change_24h < 0:
                arrow = "📉"

        price_text = f"${price:.2f}" if isinstance(price, (int, float)) else "N/A"
        change_text = f"{change_24h:.2f}%" if isinstance(change_24h, (int, float)) else "N/A"
        market_text = (
            f"${market_cap / 1_000_000_000:.2f}B"
            if isinstance(market_cap, (int, float))
            else "N/A"
        )

        return (
            f"💰 {coin.get('name', symbol)} ({symbol})\n"
            f"Giá: {price_text}\n"
            f"Thay đổi 24h: {change_text} {arrow}\n"
            f"Market Cap: {market_text}"
        )
    except requests.RequestException:
        return "Không thể kết nối tới CoinMarketCap. Thử lại sau."
