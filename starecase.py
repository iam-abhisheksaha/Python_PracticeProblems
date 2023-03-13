
# print(space, end='')
# print(space, end='')

n=int(input())
i=1
while i<=n:
    space=" "
    star="#"
    star_count=i
    space_count=n-i
    x=1
    y=1
    while x<=space_count:
        print(space, end='')
        x=x+1
    while y<=star_count:
        print(star, end='')
        y=y+1
    print("")
    i=i+1

