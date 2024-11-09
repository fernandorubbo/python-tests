import unittest


class Product():
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

def _build_matrix(product_list: list[Product], sack_capacity_kg: int) -> list[list[int]]:
    matrix = [[0] * (sack_capacity_kg+1) for _ in range(len(product_list)+1)]
    for i_product, product in enumerate(product_list):
        # because first line is empty
        i = i_product+1
        for capacity_kg in range(sack_capacity_kg+1):
            # copy from above
            above_max_value = matrix[i-1][capacity_kg]
            computed_max_value = 0
            if product.kg <= capacity_kg:
                computed_max_value = product.price + matrix[i-1][capacity_kg-product.kg]
            matrix[i][capacity_kg] = max(above_max_value, computed_max_value)
    return matrix

def _figure_out_sack_products(matrix: list[list[int]], product_list: list[Product]) -> set[Product]:
    i = len(matrix)-1
    capacity_kg = len(matrix[0])-1
    sack_products = set()
    while i > 0:
        value = matrix[i][capacity_kg]
        while i > 0 and value == matrix[i-1][capacity_kg]:
            i -= 1
        if i > 0:
            i_product = i - 1
            product = product_list[i_product]
            sack_products.add(product)
            i -= 1
            capacity_kg -= product.kg
    return sack_products


def knapsack(product_list: list[Product], sack_capacity_kg: int) -> tuple[set[Product], int]:
    if len(product_list) == 0 or sack_capacity_kg == 0:
        return set(), 0
    matrix = _build_matrix(product_list, sack_capacity_kg)
    sack_products = _figure_out_sack_products(matrix, product_list)
    max_value = matrix[len(matrix)-1][len(matrix[0])-1]
    return sack_products, max_value


class TestFibonacci(unittest.TestCase):
    def test_build_cache_matrix(self):
        product_list = [
            Product("P1", 2, 3)
        ]
        expected_cache_matrix = [[0,0,0,0], \
                                 [0,0,0,2]]
        self.assertEqual(_build_matrix(product_list, 3), expected_cache_matrix)
        product_list = [
            Product("P1", 2, 3),
            Product("P2", 5, 2)
        ]
        expected_cache_matrix = [[0,0,0,0], \
                                 [0,0,0,2], \
                                 [0,0,5,5]]
        self.assertEqual(_build_matrix(product_list, 3), expected_cache_matrix)

    def test_figure_out_chosen_products(self):
        product_list = [
            Product("P1", 2, 3)
        ]
        cache_matrix = [[0,0,0,0], \
                        [0,0,0,2]]
        self.assertEqual(_figure_out_sack_products(cache_matrix, product_list), \
                                                    {Product("P1", 2, 3)})
        product_list = [
            Product("P1", 2, 3),
            Product("P2", 5, 2)
        ]
        cache_matrix = [[0,0,0,0], \
                         [0,0,0,2], \
                         [0,0,5,5]]
        self.assertEqual(_figure_out_sack_products(cache_matrix, product_list), \
                                                    {Product("P2", 5, 2)})

    def test_empty_product_list(self):
        product_list = []
        self.assertEqual(knapsack(product_list, 3), (set(), 0))

    def test_no_sack_capacity(self):
        product_list = [
            Product("P1", 2, 3)
        ]
        self.assertEqual(knapsack(product_list, 0), (set(), 0))

    def test_one_product(self):
        product_list = [
            Product("P1", 2, 3)
        ]
        self.assertEqual(knapsack(product_list, 3), ({Product("P1", 2, 3)}, 2))

    def test_many_products(self):
        product_list = [
            Product("P1", 2, 3),
            Product("P2", 2, 1),
            Product("P3", 4, 3),
            Product("P4", 5, 4),
            Product("P5", 3, 2),
        ]
        sack_product_list = {
            Product("P2", 2, 1),
            Product("P4", 5, 4),
            Product("P5", 3, 2),
        }
        self.assertEqual(knapsack(product_list, 7),
                         (sack_product_list, 10))

if __name__ == '__main__':
    unittest.main()
