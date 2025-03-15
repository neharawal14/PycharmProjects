#!/usr/bin/env python3
def run(name:str):
  d = dict(Buddha="Neha", Neha="Buddha")
  print(f"{d[name]} loves you very much")

if __name__=="__main__":
  myname = "Neha"
  run(myname)
