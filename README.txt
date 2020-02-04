# swarm_HW3

This program will run all of the necessary simulations for this homework assignment with the following command:

```
python hw3.py
```

The results are saved in .txt files, following the naming convention below:

```
population_##_t1_#_t1p_##_t2_#_simulation_#.txt
```

Where each number `#` is prefaced by an identifier:
⋅⋅* population --- the percent of the world filled with agents
⋅⋅* t1 ----------- threshold 1, determines what satisfies agents
⋅⋅* t1p ---------- the percent of agents with threshold 1
⋅⋅* t2 ----------- threshold 2, determines what satisfies agents
⋅⋅* simulation --- The simulation number for the given varables

Inside each file is every unique run in order, starting from initialization to conclusion. Noting has to be done to remove the files to run the program again - it will overwrite the old simualtions. if you wish to keep track of where the program is, simply delete the old files before running the program and watch the folder fill back up! It takes about 10 minutes for all of the runs to be calculated.