colors = ['red', 'blue', 'yellow']
colors_nl =  [ f"{c}\n" for c in colors]
print(colors_nl)

colors_nl_filtered =  [f"{c}\n" for c in colors if 'l' in c]
print(colors_nl_filtered)

# runs twice, one to generate the list and another to print the elements
cloathes = ['hat', 'pants', 'shirt', 'shoes']
colored_cloathes = [f"{cloath} {color}\n"
                    for cloath in cloathes
                    for color in colors if 'l' in color]
print(colored_cloathes)

# performance improvements, runs only while iterating the generator
colored_cloathes = (f"{cloath} {color}\n"
                    for cloath in cloathes
                    for color in colors if 'l' in color)
# generator object, not a list
# generator generates values on demand
print(colored_cloathes)
for c in colored_cloathes:
    print(c)
print("---")
# Note generator is empty now. 
for c in colored_cloathes:
    print(c)



# generator functions uses yield into a loop
def generator_fn():
    colors = ['red', 'blue', 'yellow']
    for c in colors:
        yield f"{c}--"
my_generator = generator_fn()
# the code
for c in my_generator:
    print(c)
print("---")
# Note generator is empty now. 
for c in colored_cloathes:
    print(c)


l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2
print(l3)
l1.extend(l2)
print(l1)