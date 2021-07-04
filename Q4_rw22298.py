# Calculate the recommended amount of fertilizer given the dimensions of the plot of land

def recommended_litres_fertilizer(width, length):
  """Calculate the recommended amount of fertilizer given width and length of plot of land in metres"""
  area = width * length

  # Exact amount calculated from 1 litre per 140 metres squared
  exact_fertilizer_amount = area * 1 / 140

  INDIVIDUAL_NUMBER = 1.01093

  recommended_fertilizer_amount = exact_fertilizer_amount * INDIVIDUAL_NUMBER

  return round(recommended_fertilizer_amount) // 1
