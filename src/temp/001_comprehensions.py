# Following with https://www.youtube.com/watch?v=AhSvKGTh28Q&t=0s&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=23

squares = []
for i in range(1, 101):
    squares.append(i**2)

print(squares)

squares2 = [i**2 for i in range(1, 101)]
print(squares2)

remainders5 = [x**2 % 5 for x in range(1, 101)]
print(remainders5)

remainders11 = [x**2 % 11 for x in range(1, 101)]
print(remainders11)

movies = ['Star Wars', 'Ghandi', 'Casablanca', 'Gone With The Wind', 'Ghostbusters']

gmovies = []
for title in movies:
    if title.startswith('G'):
        gmovies.append(title)

print(gmovies)

gmovies2 = [title for title in movies if title.startswith('G')]

print(gmovies2)

movies2 = [('Citizen Kane', 1941), ('Spirited Away', 2001), ('It\'s A Wonderful Life', 1946),
('Gattica', 1997), ('No Country For Old Men', 2007), ('Rear Window', 1954),
('Lord Of The Rings: The Fellowship Of The Ring', 2001)]

pre2k = [title for (title, year) in movies2 if year < 2000]
print(pre2k)

v = [2, -3, 1]

w = [4*x for x in v]
print(w)

#Cartesian Product
A = {1, 3, 5, 7}
B = {2, 4, 6, 8}

cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)