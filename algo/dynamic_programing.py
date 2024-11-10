
class Item():
    def __init__(self, name, price, kg):
        self.name = name
        self.price = price
        self.kg = kg
    def __hash__(self):
        return hash(self.name)
    def __eq__(self, other):
        return self.name == other.name and \
                self.price == other.price and \
                self.kg == other.kg


def knapsack(item_list: list[Item], sack_capacity_kg: int) -> tuple[list[Item], int]:
    if len(item_list) == 0 or sack_capacity_kg == 0:
        return [], 0
    matrix = _build_matrix(item_list, sack_capacity_kg)
    sack_items = _figure_out_sack_items(matrix, item_list)
    max_value = matrix[len(matrix)-1][len(matrix[0])-1]
    return sack_items, max_value


def _build_matrix(item_list: list[Item], sack_capacity_kg: int) -> list[list[int]]:
    matrix = [[0] * (sack_capacity_kg+1) for _ in range(len(item_list)+1)]
    for i_item, item in enumerate(item_list):
        # because first line is empty
        i = i_item+1
        for capacity_kg in range(sack_capacity_kg+1):
            # copy from above
            above_max_value = matrix[i-1][capacity_kg]
            computed_max_value = 0
            if item.kg <= capacity_kg:
                computed_max_value = item.price + matrix[i-1][capacity_kg-item.kg]
            matrix[i][capacity_kg] = max(above_max_value, computed_max_value)
    return matrix


def _figure_out_sack_items(matrix: list[list[int]], item_list: list[Item]) -> list[Item]:
    i = len(matrix)-1
    capacity_kg = len(matrix[0])-1
    sack_items = []
    while i > 0:
        value = matrix[i][capacity_kg]
        while i > 0 and value == matrix[i-1][capacity_kg]:
            i -= 1
        if i > 0:
            i_item = i - 1
            item = item_list[i_item]
            sack_items.append(item)
            i -= 1
            capacity_kg -= item.kg
    return sack_items
