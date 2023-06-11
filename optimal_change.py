def optimal_change(item_cost, amount_paid):
    change_amounts = {
        '$100' : 100.00,
        '$50': 50.00,
        '$20': 20.00,
        '$10': 10.00,
        '$5': 5.00,
        '$1': 1.00,
        'quarter': 0.25,
        'dime': 0.10,
        'nickel': 0.05,
        'penny': 0.01
    }
    counts = {}
    
    #Set res value with initial item cost and amount paid
    res = f'The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is '
    
    #Create a dict of counts for each change amount, from highest to lowest monetary value
    change = amount_paid - item_cost
    for key, value in change_amounts.items():
        while change >= value:
            counts[key] = counts.get(key, 0) + 1
            change = round(change, 2) - value
    
    #If exact change is given, no change returned
    if counts == {}:
        return "No change necessary."

    #Organize and format res string
    for i, (key, value) in enumerate(counts.items()):
        if value > 1 and '$' in key:
            res = res + f'{value} {key} bills'
        elif value == 1 and '$' in key:
            res = res + f'{value} {key} bill'
        elif value > 1 and key != 'penny':
            res = res + f'{value} {key}s'
        elif value > 1 and key == 'penny':
            res = res + f'{value} pennies'
        elif value == 1:
            res = res + f'{value} {key}'
        
        #Add commas between values. If this iteration is the last, add a period to the end of the sentence
        if i == len(counts) - 1:
            res = res + '.'
        else:
            res = res + ', '
            
    return res