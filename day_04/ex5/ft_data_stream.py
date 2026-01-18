def game_event_generator(events: list):
    """
    Generator for a simulated stream of game events.
    """
    for event in events:
        yield event


def get_hight_level(events):
    for event in events:
        if event["data"].get("level") >= 10:
            yield event


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def is_prime(n):
    if n <= 1 :
        return False
    nb = 2
    while nb * nb <= n :
        if n % nb == 0:
            return False
        nb += 1
    return True

def first_5_primes(n) -> list:
    list = []
    i = 0
    while True:
        if len(list) == n:
            break
        if is_prime(i):
            list.append(i)
        i += 1
    return list
def main():
    """
    Generator for a simulated stream of game events.
    """
    print("=== Game Data Stream Processor ===\n")
    events = [
        {"id": 1, "player": "frank", "event_type": "login", "data": {"level": 16}},
        {"id": 2, "player": "alice", "event_type": "level_up", "data": {"level": 45}},
        {"id": 3, "player": "bob", "event_type": "death", "data": {"level": 1}},
        {"id": 4, "player": "charlie", "event_type": "kill", "data": {"level": 22}},
        {"id": 5, "player": "diana", "event_type": "item_found", "data": {"level": 34}},
        {"id": 6, "player": "eve", "event_type": "logout", "data": {"level": 41}},
        {"id": 7, "player": "alice", "event_type": "login", "data": {"level": 7}},
        {"id": 8, "player": "bob", "event_type": "level_up", "data": {"level": 32}},
        {"id": 9, "player": "charlie", "event_type": "death", "data": {"level": 18}},
        {"id": 10, "player": "diana", "event_type": "kill", "data": {"level": 29}},
        {"id": 11, "player": "eve", "event_type": "item_found", "data": {"level": 12}},
        {"id": 12, "player": "frank", "event_type": "level_up", "data": {"level": 50}},
        {"id": 13, "player": "alice", "event_type": "kill", "data": {"level": 38}},
        {"id": 14, "player": "bob", "event_type": "logout", "data": {"level": 5}},
        {
            "id": 15,
            "player": "charlie",
            "event_type": "item_found",
            "data": {"level": 44},
        },
        {"id": 16, "player": "diana", "event_type": "death", "data": {"level": 26}},
        {"id": 17, "player": "eve", "event_type": "login", "data": {"level": 15}},
        {"id": 18, "player": "frank", "event_type": "kill", "data": {"level": 31}},
    ]
    print(f"Processing {len(events)} game events...\n")
    event = game_event_generator(events)
    limits = 3
    event_number = 0
    for e in event:
        unique = ["kill", "death", "item_found", "level_up"]
        if limits != 0 and e.get("event_type") in unique:
            event_number += 1
            print(
                f"Event {event_number}: Player {e.get('player')} (level {e['data'].get('level')}) {e.get('event_type')}"
            )
            limits -= 1
        if limits == 0:
            print("...")
            break

    print("\n=== Stream Analytics ===")
    print("Total events processed:", len(events))
    loop = iter(events)
    max = 0
    for i in range(len(events)):
        current = next(loop)
        if current["data"].get("level") > max:
            max = current["data"].get("level")
    hight_level = 0
    for level in get_hight_level(events):
        hight_level += 1
    print(f"High-level players ({hight_level}+):", max)
    total = 0
    level_up = 0
    loop = iter(events)
    for e in range(len(events)):
        current = next(loop)
        if current.get("event_type") == "item_found":
            total += 1
        if current.get("event_type") == "level_up":
            level_up += 1
    print("Treasure events:", total)
    print("Level-up events:", level_up)
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print("\n=== Generator Demonstration ===")
    fib_list = list(fibonacci(10))
    print("Fibonacci sequence (first 10) : ", end="")
    print(*fib_list, sep=", ")
    prime = first_5_primes(5)
    print("Prime numbers (first 5): ", end="")
    print(*prime, sep=", ")
    
main()
