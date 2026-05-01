import argparse
from urllib import response
from bot.orders import place_order
from bot.validators import validate_input
from bot.logging_config import setup_logging

setup_logging()

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_input(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n📌 Order Summary:")
        print(vars(args))

        response = place_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        if response:
            print("\n✅ Order Success!")
            print("Order ID:", response.get("orderId"))
            print("Status:", response.get("status"))
            print(f"Executed Qty: {response.get('executedQty')}")
            print(f"Avg Price: {response.get('avgPrice', 'N/A')}")
        else:
            print("\n❌ Order Failed")

    except Exception as e:
        print(f"\n⚠️ Error: {e}")

if __name__ == "__main__":
    main()