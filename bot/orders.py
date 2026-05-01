import logging
from bot.client import get_client

client = get_client()

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        side = side.upper()
        order_type = order_type.upper()

        
        current_price = float(
            client.futures_mark_price(symbol=symbol)["markPrice"]
        )

        
        if order_type == "LIMIT":
            if side == "SELL" and price < current_price:
                raise ValueError(
                    f"SELL price must be >= market price ({current_price})"
                )
            if side == "BUY" and price > current_price:
                raise ValueError(
                    f"BUY price must be <= market price ({current_price})"
                )

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        logging.info(f"Order Request: {params}")

        response = client.futures_create_order(**params)

        logging.info(f"Order Response: {response}")

        return response

    except Exception as e:
        logging.error(f"Error placing order: {e}")
        print("❌ Error:", e)
        return None