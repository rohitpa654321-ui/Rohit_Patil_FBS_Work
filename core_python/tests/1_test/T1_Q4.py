###

# Take input
area1 = int(input('Enter area of single wall per sqf :'))
cost_interior = int(input('Enter cost of interior paint per sqf :'))
cost_exterior = int(input('Enter cost of exterior paint per msf :'))

# perform operation
area_interior = 8*area1
area_exterior = 7*area1

# painting cost
cost_inte = area_interior * cost_interior
cost_exte = area_exterior * cost_exterior

# Final cost of painting
final_cost = cost_inte + cost_exte

# Display
print(f'Final price of painting 8 wall interior({cost_interior}rs. sqft) and 7 wall exterior({cost_exterior}rs. sqft) is : {final_cost}rs.')
