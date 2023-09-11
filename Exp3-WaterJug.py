from collections import deque
def water_jug_problem(capacity_a, capacity_b, target):
    visited = set()
    queue = deque([(0, 0)])
    while queue:
        current_state = queue.popleft()
        a, b = current_state
        if current_state == target:
            return True
        visited.add(current_state)
        # Fill jug A
        if (capacity_a, b) not in visited:
            queue.append((capacity_a, b))
        # Fill jug B
        if (a, capacity_b) not in visited:
            queue.append((a, capacity_b))
        # Empty jug A
        if (0, b) not in visited:
            queue.append((0, b))
        # Empty jug B
        if (a, 0) not in visited:
            queue.append((a, 0))
        # Pour from A to B
        pour_amount = min(a, capacity_b - b)
        if (a - pour_amount, b + pour_amount) not in visited:
            queue.append((a - pour_amount, b + pour_amount))
        pour_amount = min(b, capacity_a - a)
        if (a + pour_amount, b - pour_amount) not in visited:
            queue.append((a + pour_amount, b - pour_amount))
    return False
jugA_capacity = 4
jugB_capacity = 3
target_state = (2, 0)  
if water_jug_problem(jugA_capacity, jugB_capacity, target_state):
    print("Solution exists.")
else:
    print("No solution exists.")
