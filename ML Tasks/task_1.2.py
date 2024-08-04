gadgets = [
    ("Explosive Batarangs", 3, True),
    ("Batarangs", 5, True), 
    ("Smoke Pellets", 0, False), 
    ("Tear Gas Grenades", 2, True), 
    ("Night Vision Goggles", 1, True), 
    ("Batclaw", 0, False), 
    ("Grapple Gun", 3, True), 
    ("Batsignal", 0, False), 
    ("Utility Belt", 1, True),
    ("Batmobile Tires", 4, True)
]

sorted_inventory = sorted(
    gadgets,
    key= lambda item: (
        not item[2],
        -item[1],
        item[0].lower()
    )
)

print("Sorted Batcave Inventory:")
for gadget in sorted_inventory:
    print(gadget)