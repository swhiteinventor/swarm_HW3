#report

#Simulation runs:



# My observations regarding convergence to segregation:

1. Convergence to segregation is faster as the threshold decreases for any and all agents. This makes sense because there are more places where agents would be satisfied. This observation seems to contradict logic, for one might reason that those with a higher threshold, aka a desire to have segregation, would contribute to faster segregation. This logic is flawed because it fails to consider there are a fewer number of places to move to that would satisfy an agent with a high threshold while there are many more places that would satsify an agent with a lower threshold. This observation is true whether you look at convergence from the perspective of the number of runs it takes for the world to settle to a static or oscilatory behavior or whether you look at the computation time.
2. As the threshold increases for any and all agents, segregation becomes more pronouced with larger clumps of similar agents. For example, compare the end states of the t=3 vs the t=4 for 80% population. Or we could take it to an extreme, with t=6 for 60% population as shown at the end of this section. Notice how large the clumps are of the different agents. It took 15 minutes to calculate that result.
3. Convergence to segregation was faster after adding in a modification to the code that allowed agents that were not able to find a perfect location that would satisfy their threshold to still move to new location. The new location had to give them more satisfaction than their current location, even if it could not satisfy them completely. I did this under the logic that while an agent might not be satisfied initially after his move to a better location, another similar agent might come join him (or more than one) and increase his satisfaction until it meets his threshold.
4. No noise was created on the edges of the world because the edges wrap to the opposite side. This promotes larger clumps and more segregation (as a percentage of the world, anyway) because it eliminates agents that would otherwise have to contend with being on the edge and having their threshold be scaled down based on how many neighbors the agent actually had. I don't know if this decision impacts the speed of segregation becuase I did not implement it in multiple ways.

```
-------------------------------------------------------------------------------------------------------
----------------------->    SIMULATION Number:  0    STEP Number:    0    <----------------------------
------------>    100%  agents with Threshold: 6       0% agents with Theshold 2: 0    <----------------
-------------------------------------------------------------------------------------------------------
| O         x O x O x O x       x x O x x x   O O   x x x   O O x   x x O O x   x O O O x x O O     O |
| O     x O x O O   O x O   x O     O O O x x O O O O O O O x x x x x x   O x O x O O   x x x x x   O |
| O O O x O x O x O x O O x O x x x   O O x x x x O O x x x x   x     O O O O x   O O O   O x x x O x |
| O O x O   x O   O x O x O O x O x   O x O   O O   O   O x x x O   x O O O x x O O O O   x O O x x   |
|   O x O     O O   x O x     x x O x     O   x O O O O O   x O O x   O x x x O O   O O O x O O O x O |
| x O x x O x O x   x x O x   O O x x x   O O O x   x O x x x x x x     x O x x O   x x O x O O O O O |
| x O x O x O x x x O x x O O       x O O O x x   x x x O x x O x x x x O O O x     O O O x x O O   x |
| O x x O x x O x   O O x O O     x x x O x x O x x O x O O x O x O x x O x O O x     x O x O x x x O |
|   x x x x x O O x   x   O x   x x x x x   x   O   x O O x O   x x O   x O   O O O O x O O x O x x O |
| x   x     x x O   O O O x x x x   x O x x x   x O x x O O x x x   x x   x O O   x x O x x O   x   O |
| x   O O x O   x O x x   x   x x x O x x O     x x x x O O O x x x   O x     x O   x x x O x x x O O |
| x x x x x O x x x   O   x x O O x x x x x     x x     x   O x x O O O x   O   O O O O O O x x O O O |
| x       O x O O O x     x O   x   x O O O O O   x   O   x   O O x x O x O     O   x   O O O   x x x |
| x     O x   x   O   x O O   O x     x   O x x O O O   O O     x x O x x O   O   O O O x O   O O x   |
| x O x O   x O O O O O x x x x x O x O x O x O   x x O x O x O O x O x O O x x O x     O x x   O O O |
| x x   O x O x O x O O x   x O   x x O O   O O x O x O O x O O x x O x   x x x x O     O O O O   O x |
| x O x O O x O x x x O x       x x   x x O O x x x x   O O x O O x x   x x O x x     x x x x O O x x |
| O x O   x x x x O   x O x O     O x   O O x x O x O   O O x x x x O   x O x   O x O x O O x O x O   |
|       O O O O   O O O   O x x O x x O O O x O   O O O x O x x x O x O   x O O x O O O x x O x O O O |
| O O   O O x     x   x O   x x O O O O   x x O x x x x x x O x O x O x x   x   O   O O x O   x   O O |
| O x x O x x x O O x x x   O O O x     O O x x O O x O x O O x   O x x O O O O   x O O x     x x x O |
|   O O x x x x x x x   x O   O O O O x x O x O   O O O       x x x x x O O O x O O x x   x   O O O   |
| x   O x O x O x O x x x x O x O O   O O O O O x O   x x     O x O O x x O O   x O x x x O O O O x O |
|   x x x   O O O x O     x   O O O   x x   O O x x x   O x x O x O O x O x O O   x O   x O O O O O   |
| x O O   x x O x O O O x O O x O O O x O x   x x O x O x O x O O   O x x x x x O x O O O O O O O O x |
|   x O x O O   x x x O O x x     O x O O     O x     x x O O   x O O x x O   O O x x   O O x x O x O |
| x x O O x x   O O O   x O   x   O O O x x x O O   x O x x x O   O x   x x x O O O O   O   x O x O x |
| O x O O O   O O O O   x O x x O O O O x O O O O O   x x x O O x   O O x O O x x O O   O O   O x x x |
| O   O x O   x O O x x O x x x   x O   O x x   O O   x   O O x x O O x x O x   O x O x     x O O x O |
| O   x O   x   x x x O O O O O x O x O   x O x O x x x O x   O O x O x x     O O x   O   O O x x O   |
| x O O   x x x x O x x O x x O x x   x O O x x O x O O     O O O       O x O x   O O O     O x O O O |
| x   O O x O x   x x   x O x   x O x   O   O       O O x x x   O x x O x O x x x x   O   x x O x     |
| O x x x x x x     O x x x x x x   O O O O   O O x x O   x x   x x O   O x   O x   x O O x O O O O x |
|   x   x x O x   x O O O O O O O O x   O x       x O   x O   x O x x O   O x   x x     O x x   x x   |
| x x x O O O   x O x x x   O O   O x O O x x x x     x x     x O   x O O O O   x O O x O x O x   O x |
|     O   O O O x O x O O x O   x O O x O x   x   x x x x O O O x O x x     x O O   O O x x   O O x O |
| x O   O   O O O x   O O O O   x x x O O O O O x x O x O x x x O   x x x x x x     O   x x   x x x O |
| x O O O x x x x O x x x O O     O x O x x O x O x x O x   x O   O O x   x   x x O x O O O x   O   O |
| O x x x x O x   O   x x x O O x x O   x x   O O x     O x O O       x x O O O x x O     O x x x x O |
|   O     x       x x x O O   O O O O O   O x x x x     O x x x x   x O x x x x O O O O O O O x x O x |
| x x O x O x O x x x x O O O x x O x   x   x x x   x O x O x O x O x x x   x x   O   O O O   x   x O |
| x O O O O O   x   x x x O O   O   O x O O       O   O O x   O   O O x O O   x x O O x O       x     |
| x   x O     O O x O O O x O   O O O x   x x O x   O     x O x O   x O O     O x O O O x x O O O x x |
|   x   x O x x   x O O   O x x O x   x x x O x x O O x x   x x x x O O x   x O x x   x x O       x x |
| x x O x x O O   x x   x O O O O O O   x O     O x   x   O x O O O O O x O O x x x O x x x O x   x O |
| O O O O x x O O x O x O x   x O   x   O x O x   x O x O O x x x x x x O x O O     O   x O x x O O O |
|   x O x O   x     x x O x x O O O O O O   x O   x x O x   x O O O x x O x x   O x     O x O x O x x |
| x x O O x x x O x x O O O   O   x   O O   O     O   x x x O x O O x O   x O   O O O x x x O   x x O |
|   x   O x   O O O x x O O O O   O O x x x O O O x O O O   x O x x   x O O O x O x O O O x x O x O   |
| O O O x   O O   x O x x x   O x O O O O                                                             |
-------------------------------------------------------------------------------------------------------
----> STATS:    0 agents moved,   96 agents satisfied, 1904 agents unsatisfied,    80% population <----
-------------------------------------------------------------------------------------------------------
----------------------->    KEY:    'X' = 'Agent X'    'O' = 'Agent O'    <----------------------------
-------------------------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------------------------
----------------------->    SIMULATION Number:  0    STEP Number:   75    <----------------------------
------------>    100%  agents with Threshold: 6       0% agents with Theshold 2: 0    <----------------
-------------------------------------------------------------------------------------------------------
|                         O                                                                           |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|   x x x x x x x x x x x x x x x x x x x x                                                           |
| x x x x x x x x x x x x x x x x x x x x x x                                   O O O                 |
| x x x x x x x x x x x x x x x x x x x x x x x                               O O O O O             x |
| x x x x x x x x x x x x x x x x x x x x x x x x                           O O O O O O O         x x |
| x x x x x x x x x x x x x x x x x x x x x x x x                         O O O O O O O O O       x x |
| x x x x x x x x x x x x x x x x x x x x x x x             x x x x x     O O O O O O O O O O     x x |
| x x x x x x x x x x x x x x x x x x x x x x             x x x x x x x   O O O O O O O O O O O   x x |
| x x x x x x x x x x x x x x x x x x x x x O O O O     x x x x x x x x x O O O O O O O O O O O O x x |
| x x x x x x x x x x x x x x x x x x x O O O O O O O   x x x x x x x x x O O O O O O O O O O O O O x |
| x x x x x x x x x x x x x x x x x x O O O O O O O O O x x x x x x x x x O O O O O O O O O O O O O O |
| O x x x x x x x x x x x x x x x x O O O O O O O O O O x x x x x x x x x O O O O O O O O O O O O O O |
| O O x x x x x x x x x x x x x x O O O O O O O O O O O x x x x x x x x x O O O O O O O O O O O O O O |
| O O O x x x x x x x x x x x x O O O O O O O O O O O O x x x x x x x x x O O O O O O O O O O O O O O |
| O O O O x x x x x x x x x x O O O O O O O O O O O O x x x x x x x x x x O O O O O O O O O O O O O O |
| O O O O   x x x x x x x x O O O O O O O O O O O O x x x x x x x x x x x O O O O O O O O O O O O O O |
| O O O O                 O O O O O O O O O O O O O x x x x x x x x x x x O O O O O O O O O O O O O O |
| O O O O               O O O O O O O O O O O O O O x x x x x x x x x x x O O O O O O O O O O O O O O |
| O O O O             O O O O O O O O O O O O O O O x x x x x x x x x x x O O O O O O O O O O O O O O |
| O O O O x x       O O O O O O O O O O O O O O O O x x x x x x x x x x x x O O O O O O O O O O O O O |
| O O O x x x x     O O O O O O O O O O O O O O O O x x x x x x x x x x x x O O O O O O O O O O O O O |
| O O x x x x x x   O O O O O O O O O O O O O O O O x x x x x x x x x x x x O O O O O O O O O O O O O |
| O x x x x x x x x O O O O O O O O O O O O O O O O x x x x x x x x x x x O O O O O O O O O O O O O O |
| O x x x x x x x x O O O O O O O O O O O O O O O O x x x x x x x x x x x O O O O O O O O O O O O O O |
| x x x x x x x x x x O O O O O O O O O O O O O O O x x x x x x x x x x x O O O O O O O O O O O O O O |
| x x x x x x x x x x O O O O O O O O O O O O O O O x x x x x x x x x x x O O O O O O O O O O O O O x |
| x x x x x x x x x x O O O O O O O O O O O O O O O x x x x x x x x x x x O O O O O O O O O O O O x x |
| x x x x x x x x x x O O O O O O O O O O O O O O O x x x x x x x x x x x x O O O O O O O O O O x x x |
| x x x x x x x x x x O O O O O O O O O O O O O O O x x x x x x x x x x x x O O O O O O O O O x x x x |
| x x x x x x x x x x O O O O O O O O O O O O O O O x x x x x x x x x x x x O O O O O O O O O x x x x |
| x x x x x x x x x x O O O O O O O O O O O O O O O x x x x x x x x x x x x O O O O O O O O x x x x x |
| x x x x x x x x x x O O O O O O O O O O O O O O x x x x x x x x x x x x x O O O O O O O O x x x x x |
| x x x x x x x x x x O O O O O O O O O O O O O O x x x x x x x x x x x x x O O O O O O O O x x x x x |
| x x x x x x x x x x O O O O O O O O O O O O O O x x x x x x x x x x x x x x O O O O O O O x x x x x |
| x x x x x x x x x x O O O O O O O O O O O O O O x x x x x x x x x x x x x x O O O O O O O x x x x x |
| O O O x x x x x x x O O O O O O O O O O O O O O x x x x x x x x x x x x x x x O O O O O O x x x x x |
| O O O O x x x x x x O O O O O O O O O O O O O O x x x x x x x x x x x x x x x O O O O O O x x x x O |
| O O O O O x x x x x O O O O O O O O O O O O O O x x x x x x x x x x x x x x x O O O O O O x x x x O |
| O O O O O x x x x x O O O O O O O O O O O O O O x x x x x x x x x x x x x x x O O O O O x x x x x O |
| O O O O O x x x x x O O O O O O O O O O O O O O   x x x x x x x x x x x x x x O O O O O x x x x x O |
| O O O O O x x x x x O O O O O O O O O O O O O       x x x x x x x x x x x x x O O O O O x x x x x O |
| O O O O O x x x x x O O O O O O O O O O O O           x x x x x x x x x x x   O O O O O x x x x x O |
| O O O O O x x x x x O O O O O O O O O O O               x x x x x x x x x     O O O O O x x x x x O |
| O O O O x x x x x x O O O O O O O O O O                   x x x x x x x         O O O   x x x x x   |
|   O O   x x x x x x O O O O O O O O O                                                     x x x     |
|           x x x x x O O O O O O O O                                                                 |
|             x   x     O O O O   O                                                                   |
-------------------------------------------------------------------------------------------------------
----> STATS:  383 agents moved, 1621 agents satisfied,  379 agents unsatisfied,    80% population <----
-------------------------------------------------------------------------------------------------------
----------------------->    KEY:    'X' = 'Agent X'    'O' = 'Agent O'    <----------------------------
-------------------------------------------------------------------------------------------------------

Ending simulation 0 because run 73, 74, and 75 were all identical.
```