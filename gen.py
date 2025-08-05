def generate_Square(lst):
    for  item in lst:
        yield item**2
num_list=list(range(1,5))
gen=generate_Square(num_list)
for n in gen:
    print(n) 




