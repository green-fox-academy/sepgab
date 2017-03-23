# Join the two lists by matching one girl with one boy in the order list
# Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

girls = ["Eve","Ashley","Bözsi","Kat","Jane"]
boys = ["Joe","Fred","Béla","Todd","Neef","Jeff"]
order = []
n = max(len(girls), len(boys))

for nr in range(0, n):
    if nr <= len(girls)-1:
        order.append(girls[nr])
    else:
        pass
    if nr <= len(boys)-1:
        order.append(boys[nr])
    else:
        pass
print(order)
