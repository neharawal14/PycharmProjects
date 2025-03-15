import csv



def split_csv(path):
    f = open(path)

    first = "/Users/neharawal/Documents/Research/CSCAgeingP5/pressure_information/pressurecsc_new2017.h"
    final_file = open(first, "w")
    for line in f:
 #       if(line[0]=="#"):
 #           continue
      #  print(line[1:14])
      #  print(line[17:24])
        timeSecond = line[1:11]
        pressure = line[17:24]
        #data.append(run_nb)

        test_string = "else if(time<"+ timeSecond + " ) return "+pressure+";"
        print(test_string)
        final_file.write(test_string)
        final_file.write("\n")



if __name__ == '__main__':
    path_csv = "/Users/neharawal/Documents/Research/CSCAgeingP5/pressure_information/pressure_time.csv"
    split_csv(path_csv)

