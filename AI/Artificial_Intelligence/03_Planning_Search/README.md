# heuristic analysis
## 1. Base on the result table below.:
Problem 1 ‘s optimal plan is #7 greedy best first graph search 
Problem 2 ‘s optimal plan is #7 greedy best first graph search 
Problem 3 ‘s optimal plan is #3 depth first graph search
## 2. Compare and contrast non-heuristic search result metrics: **3** depth first graph search is the best search 
methods.
## 3. Compare and contrast heuristic search result metrics: **7** greedy best first graph search .
## 4. The best heuristic is **7** greedy best first graph search. In problem1 and problem 2, the #7 greedy best 
first graph search better than all non-heuristic search. But in problem3 is not better than non-heuristic 
search “**3** depth first graph search”. Because **7** greedy best first graph search almost create 8 times 
nodes of **3** depth first graph search, spend 7 times of time to finished the searching.
Number of 
search method Search Methods
Air Cargo Problem 1
Plan 
Length Expansions Goal 
Test
New 
Nodes
Time 
elapsed
1
nonheuristic
search
Breadth first search 6 43 56 180 0.1092
2 breadth first tree search 6 1458 1459 5960 1.144
3 depth first graph search 20 21 22 84 0.0160
4 depth limited search 50 101 271 414 0.1188
5 uniform cost search 6 55 57 224 0.0426
6
heuristic 
search
recursive best first search h 1 6 4229 4230 17023 3.1435
7 greedy best first graph search h 1 6 7 9 28 0.0061
8 A* search h 1 6 55 57 224 0.0429
9 A*search h ignore preconditions 6 55 57 224 0.0431
10 A* search h pg levelsum 6 45 47 188 0.9550
Problem 1
Number of 
search method
Search Methods Air Cargo Problem 2
Plan 
Length Expansions Goal 
Test
New 
Nodes
Time 
elapsed
1
nonheuristic
search
Breadth first search 9 3343 4609 30509 14.165
2
breadth first tree search Too 
long
3 depth first graph search 619 624 625 5602 3.8188
4 depth limited search 50 222719 2053741 2054119 1087.97
5 uniform cost search 9 4853 4855 44041 13.324
6
heuristic 
search
recursive best first search h 1 Too 
long
7 greedy best first graph search h 1 21 988 1000 8982 2.71867
8 A* search h 1 9 4853 4855 44041 12.829
9 A*search h ignore preconditions 9 4853 4855 44041 14.9858
10 A* search h pg levelsum 9 1643 1645 15414 328.664
Problem 2
Number of 
search method
Search Methods Air Cargo Problem 3
Plan 
Length Expansions Goal 
Test
New 
Nodes
Time 
elapsed
1
nonheuristic
search
Breadth first search 12 14663 18098 129631 99.284
2 breadth first tree search Too long
3 depth first graph search 392 408 409 3364 1.884
4 depth limited search Too long
5 uniform cost search 12 18083 18085 158465 58.207
6
heuristic 
search
recursive best first search h 1 Too long
7 greedy best first graph search h 1 26 3377 3379 29735 10.185
8 A* search h 1 12 18083 18085 158465 55.129
9 A*search h ignore preconditions 12 18083 18085 158465 57.235
10 A* search h pg levelsum 12 2757 2759 26202 1234.71
Problem 3
 Note: Time elapsed ‘s unit is second or Not result: too long
