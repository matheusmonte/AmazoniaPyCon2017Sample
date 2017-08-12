import mysim
 import sys
 node1 = sim.Entity("node")
 node2 = sim.Entity("node")
 link = sim.Entity("link")
 node1.config("link",link,node2)
 node2.config("link",link,node1)
 link.config("bandwidth",100)
 link.config("latency",30)
 d = "hello world"
 node1.emit([0,1],"data",d,link)
 sim.stopAt(sim.time() + [0,1000])
 sim.run()
 sys.exit()
