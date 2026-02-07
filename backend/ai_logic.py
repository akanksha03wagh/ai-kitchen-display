from collections import defaultdict

def compress_orders(orders):
    compressed = defaultdict(int)

    for order in orders:
        key = f"{order['item']} ({order['type']})"
        compressed[key] += order['quantity']

    result = []
    for k, v in compressed.items():
        result.append({
            "item": k,
            "quantity": v
        })

    return result


def predict_priority(orders):
    priority_list = sorted(
        orders,
        key=lambda x: x['prep_time'],
        reverse=True
    )
    return priority_list
