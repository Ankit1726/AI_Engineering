# Find Subset of String 
def generate_subset(st,curr="",idx=0):
     if(idx==len(st)):
          print(curr)
          print("------")
          return
     generate_subset(st,curr+st[idx],idx+1) # include choice 
     generate_subset(st,curr,idx+1) # not include choice

st = "efg"
print(generate_subset(st,curr="",idx=0))
     