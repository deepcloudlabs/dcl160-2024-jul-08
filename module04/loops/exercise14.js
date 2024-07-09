numbers = [4, 8, 15, 16, 23, 42]
numbers.filter(n => n%2 == 0).map(u => u ** 3).reduce((x,y)=>x+y)