from time import perf_counter as pc
from time import sleep as pause

def runner():
    print("Performing a costly function")
    pause(1)
    print("Function complete")
    
if __name__ == "__main__":
 start = pc()
 runner()
 end = pc()
 print(f"Process took {round(end-start, 2)} seconds")