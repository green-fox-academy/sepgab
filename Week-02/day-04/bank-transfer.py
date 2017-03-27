accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

# Create function that returns the name and balance of cash on an account

# Create function that transfers an balance of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - balance
#
# Print "404 - account not found" if any of the account numbers don't exist

def name_balance(account_nr):
    output_list =[]
    for i in range(0, len(accounts)):
        for key, value in accounts[i].items():
            if key == 'account_number':
                if value == account_nr:
                    output_list.append(accounts[i]['client_name'])
                    output_list.append(accounts[i]['balance'])
    print(output_list)


name_balance(43546731)

def transfer(from_account_number, to_account_number, tr_balance):
    list_accounts = []
    for k in range(0, len(accounts)):
        list_accounts.append(accounts[k]['account_number'])

    print(list_accounts)
    switch1 = 0
    switch2 = 0
    switch3 = 0
    for a in range(0, len(list_accounts)):
        if list_accounts[a] == from_account_number:
            switch1 = 1
    print(switch1)
    for b in range(0, len(list_accounts)):
        if list_accounts[b] == to_account_number:
            switch2 = 1
    print(switch2)
    for c in range(0, len(accounts)):
        for key, value in accounts[c].items():
            if key == 'account_number':
                if value == from_account_number:
                    if accounts[c]['balance'] >= tr_balance:
                        switch3 = 1
    print(switch3)
    if switch1 * switch2 == 0:
        print("404 - account not found")
    elif switch3 == 0:
        print("Balance not enough")
    else:
        for i in range(0, len(accounts)):
            for key, value in accounts[i].items():
                if key == 'account_number':
                    if value == from_account_number:
                        accounts[i]['balance'] -= tr_balance
        for j in range(0, len(accounts)):
            for key, value in accounts[j].items():
                if key == 'account_number':
                    if value == to_account_number:
                        accounts[j]['balance'] += tr_balance

transfer(11234543, 23456311, 203004099.2)

name_balance(11234543)
name_balance(23456311)
