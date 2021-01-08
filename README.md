# Island hop

```The assignment
Write a computer program that prepares one island tour itinerary. The itinerary includes
H+1 islands to visit and thus H hops between islands. It also includes the decision whether
an island hop is airborne or by sea for each hop between two consecutive islands. The
means of transport to the first island and from the last island onwards is not included in
the itinerary.
Although airplanes and helicopters are faster than ships or boats, they're also more
expensive to operate and generate more emissions, so you and your customers aim to
minimise airborne hops.
Satisfying your customers:
You have prepared an initial sequence of islands to visit and sent this to your customers.
(This initial sequence is out of scope for this assignment.) Your customers respond with a
list of preferred island hops and the means of transport for those hops. Each customer is
satisfied if the final itinerary includes at least one island hop from their list with a
matching means of transport. There is at most one airborne hop on each customer's list. If
a customer denotes that they only want an airborne hop between two specific islands,
they are not satisfied with travelling that leg by sea, and vice versa.
Specification
To formulate the above more precisely, prepare the final itinerary as follows:
1. There are exactly H island hops
2. Each hop between consecutive islands is either airborne or by sea
3. Each customer gets at least one hop with a matching means of transport (airborne
or by sea) from their preferred list
4. The final itinerary has the minimum number of airborne hops
5. It may be impossible to satisfy all your customers and your program must detect
this
6. There are at most 400 customers
```
## Prerequisites
Please, use python 3.7+ since I was using dataclasses for this task.
No external dependencies were used

- If you want to read from stdin:
```
cat %filename% |  python3 main.py
```

- If you want to read from file:
```
python3 main.py --file_path /path/to/file
```

- You can run tests:
```
python3 -m unittest discover
```
in project directory

## Explanation
Solving the problem as fast as possible using the most obvious approach
(imperative way/cartesian product)

1. Create all possible itineraries and write them to the list with length of 
number of hops.
2. Sort the list by the amount of airborne hops ascending since they have lower priority by requirements.
3. Then, iterating through itineraries, make sure that itinerary satisfies all customers at once.

Example:

Given 4 customers

```
6
4
0 by-sea, 2 by-sea, 3 by-sea
0 by-sea, 5 airborne
0 airborne, 5 by-sea
2 airborne
```

There are 6 hops, using cartesian product there are 64 different variations to plan 
itinerary. Then sort them by amount of airborne hops ascending. They look like:
```
[(0, 'by-sea'), (1, 'by-sea'), (2, 'by-sea'), (3, 'by-sea'), (4, 'by-sea'), (5, 'by-sea')]
...
[(0, 'by-sea'), (1, 'by-sea'), (2, 'airborne'), (3, 'by-sea'), (4, 'by-sea'), (5, 'by-sea')]
...
[(0, 'airborne'), (1, 'airborne'), (2, 'airborne'), (3, 'airborne'), (4, 'airborne'), (5, 'airborne')]
```

Then iterate through each and check if this itinerary satisfies each customer.
 
In the example below itinerary that satisfied all customers is found:

```
Initerary [(0, 'by-sea'), (1, 'by-sea'), (2, 'airborne'), (3, 'by-sea'), (4, 'by-sea'), (5, 'by-sea')]

customer1 0 by-sea, 2 by-sea, 3 by-sea - satisfied
customer2 0 by-sea, 5 airborne - satisfied
customer3 0 airborne, 5 by-sea - satisfied
customer4 2 airborne - satisfied
```

## Conclusions
I didn't get to calculate algorithm and memory complexity, but since it was quickest way that came into my mind,
it couldn't be that good.
