def stop_ascending(list):
    for i in range(len(list)):
        try:
            if list[i] < list[i+1]:
                print("", end="")
            else:
                return i+1
        except IndexError:            
            return i+1
        except ValueError:
            return "List is incorrect format"
        
def main():
    print( stop_ascending([]) ) # None
    print( stop_ascending([1, 2, 3]) ) # 3
    print( stop_ascending([1, 2, 3, 1, 5]) ) # 3

main()