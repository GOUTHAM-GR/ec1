import re


def reader():
    with open("testlog1") as f:
        log = f.readlines()
        resarr = []  # to store all events with repeation
        #print("loop out")
        # print(log)
        # here i used to read each line in file and just take 5th argument always ie my event.
        for line in log:
            # print(line)
            res = line.split(' ')[6-1]
            if "[" in res:
                res = res.split("[")[0]
                # im using list to make note how many times did that event occur.
                resarr.append(res)
            else:
                resarr.append(res)
            # removing the [] in events

        # print(resarr);
        # lets find the no of time our event has occured.
        # here im using set data type to find and store unqiue events
        myset = set(resarr)
        # print(myset)
        # we run for loop to see how many times the event has occured:
        count=0
        for event in myset:
            count+=resarr.count(event)
            print("%s  %s"%(event,resarr.count(event)))
        print("total num of events %s" %count)

if __name__ == '__main__':
    reader()