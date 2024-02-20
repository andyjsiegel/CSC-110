def read_csv(file_name):
    f = open(file_name,'r')
    text = f.read()
    lines = text.split('\n')
    thisdict = {}
    for line in lines:
        header = line.split(',')[0]
        values = line.split(',')
        values.pop(0)
        for value in values:
            if value.replace('.','').isnumeric() == False:
                thisdict[header] = values
            
            elif "." in value:
                thisdict[header] = [float(value) for value in values]
                
            else:
                thisdict[header] = [int(value) for value in values]
                
            
        
    f.close()
    return thisdict
print( read_csv("stipends.csv") ) # {"Peter": [1000], 
                                  #  "Joan": [50500],
                                  #  "Mary": [2400]}
                                  
print( read_csv("population.csv")) # {"Country": ["United States", "Brazil", "Mexico", "Canada"],
                                  #  "Population (in mil)": [331.00, 212.56, 128.93, 37.74]}