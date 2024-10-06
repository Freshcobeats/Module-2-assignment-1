#code correction task one
weather=("sunny")

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")


#Your mood today task two
#ask how the user feels
feeling =input("how do you feel?")
#users response
if feeling == "happy":
    print("That's great to hear!")
elif feeling == "sad":
    print("I hope your day gets better!")    

#2 task 1 

pi_value = 3.14
user_age = 25
user_location = "New York"
MAX_LIMIT = 1000

#3 task 2
#prices are for bread, peanut butter, jelly


def total_cost(prices):
    return sum(prices)
prices = [2,4,6]
print(total_cost(prices))

#3 task 2
#calculate total amount in account after a year with interest
def total_amount(account):
    sum_amount=10000
    interest=0.007
    for amount in account:
        interest=sum_amount*interest
        sum_amount+=interest
    return account
print(total_amount(account))


