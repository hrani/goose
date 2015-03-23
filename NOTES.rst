There are 3 ways to update gui with the simulation data

1) Implement a function in moose core which after n clock ticks
   copies the moose vectors and lets moose continue running.
   These vector copies can be used to update the GUI.
2)
