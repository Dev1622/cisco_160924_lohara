def find_quotient(d,n):
    if n == 0:
        #raise ZeroDivisionError()
        raise Exception()
    return d / n


try:
    # Code that might raise an exception
    number = int(input('Enter a number:'))
    result = find_quotient(10,number)
except ValueError as e:
    print(f'{e} \nInvaid input! Please enter a valid integer ')
except Exception as e:
    #Handle the exception
    print('You cannot divide by zero!')
else:
    # Executes if no exception occurs
    print(f'result:{result}')
    print("Division successful.")
finally:
    # Always executes
    print("Execution complete.")






""" try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle the exception
    print("You cannot divide by zero!")
else:
    # Executes if no exception occurs
    print("Division successful.")
finally:
    # Always executes
    print("Execution complete.") """