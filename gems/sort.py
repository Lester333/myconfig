#sort.py - makeshift sort

def sorting(list):
    ret = []
    try:
        minnum = min(list)
        while True:
            for num in list: 
                if num == minnum and len(list) != 1:
                    ret.append(num)
                    list.remove(num)
                    minnum = min(list)
                else:
                    pass
            if len(list) == 1:
                ret.extend(list)
                list.clear()
                break
        if len(list) == 0: pass
    except KeyboardInterrupt:
        print("\n\nInterrupted\n\n")

if __name__ == '__main__': 
  sorting()
