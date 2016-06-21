# CS121 Linear regression assignment
# 
# Kristen Witte, kwitte
#
# Generate plots and print text answers for the STOCK data
#
import sys
import model

# useful defined constants for the stock data
#STOCKS = range(0, 11)
#DJIA = 11
#### Did not use

col_names, data = model.read_file("data/stock/training.csv")
col_names, test_data = model.read_file("data/stock/testing.csv")

##TASK 1A
print("Task 1A")
all_r2 = model.get_R2(col_names, data, "Single")
names_1A = col_names[:7]
model.make_table(all_r2, names_1A)


##TASK 1B
print("Task 1B")
combined_r2 = model.get_R2(col_names, data, "Multi")
names_1B = ["All"]
model.make_table(combined_r2, names_1B)


##Task 2
print("Task 2")
pair, bivar_r2 = model.get_R2(col_names, data, "BiVar")
model.make_table(bivar_r2, pair)


##Task 3A
print("Task 3A")
compiled_data = model.get_R2(col_names, data, "Arbitrary")
model.print_dict_data(compiled_data)


##Task3B
print("\nTask 3B")
compiled_data, best_for_01 = model.get_R2(col_names, data, 
    "Arbitrary", threshold = 0.1)
compiled_data, best_for_001 = model.get_R2(col_names, data, 
    "Arbitrary", threshold = 0.01)

print("Threshold = 0.1: ") 
model.print_dict_data(best_for_01)
print("Threshold = 0.01: ") 
model.print_dict_data(best_for_001)


##Task4
print("\nTask 4")
compiled_data = model.get_R2(col_names, data, "Arbitrary", test_data)
model.print_dict_data(compiled_data)





if __name__ == "__main__":
    # remove the next line
    pass

