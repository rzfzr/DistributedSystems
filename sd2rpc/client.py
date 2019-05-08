import rpyc
conn = rpyc.classic.connect("localhost")
conn.execute("print('Hello from Tutorialspoint')")