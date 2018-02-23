import gc
import objgraph
gc.set_debug(gc.DEBUG_SAVEALL)

# Stuff here

gc.collect()
objgraph.show_backrefs(gc.garbage, filename='graph.png')
