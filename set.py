s1 = {1,2,2,3}
s1.remove(3)

s2 = set([2, 4,6])
s2.add(5)

print(f"s: {s1} - s2: {s2}")

print("union")
print(s1|s2)
print(s1.union(s2))

print("intersection")
print(s1&s2)
print(s1.intersection(s2))

print("difference")
print(s1-s2)
print(s2.difference(s1))

print("symmetric difference")
print(s1^s2)
print(s1.symmetric_difference(s2))


class Guitar:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __hash__(self):
        return hash((self.brand, self.model, self.year))

    def __eq__(self, other):
        if not isinstance(other, Guitar):
            return False
        return self.brand == other.brand and \
                self.model == other.model and \
                self.year == other.year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"




# Create some Guitar objects
guitar1 = Guitar("Fender", "Stratocaster", 1965)
guitar2 = Guitar("Gibson", "Les Paul", 1959)
guitar3 = Guitar("Fender", "Telecaster", 1952)
guitar4 = Guitar("Fender", "Telecaster", 1952)

# Create a set of Guitar objects
guitar_set = {guitar1, guitar2, guitar3, guitar4}

for guitar in guitar_set:
    print(guitar)

print(guitar4 in guitar_set)

guitar_dict = {guitar1:1, guitar2:2, guitar3:3}
print(guitar_dict[guitar2])

print(guitar2 in guitar_dict)
guitar_dict.pop(guitar2)
print(guitar2 in guitar_dict)