def sandwich_order(*items):
  print("\nYou have ordered a sandwich with: ")
  for item in items:
    print(f"\t{item}")

# First call
sandwich_order("turkey", "cheddar cheese", "lettuce", "tomato", "onion")

# Second call
sandwich_order("ham", "swiss cheese", "mayonnaise", "mustard")

# Third call
sandwich_order("roast beef", "lettuce", "pickles", "horseradish")
