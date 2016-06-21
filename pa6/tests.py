##################
# Tests for PA6
#
#

import numpy as np
import model

#data = np.array([[0, 0 , 0, 6], [0, 1, 0, 0], [0, 1, 1, 96]])

#col_names = ["G", "R", "T", "CR"]

col_names, data_training = model.read_file("data/city/training.csv")
col_names, data_testing = model.read_file("data/city/testing.csv")

#all_r2 = model.get_R2(col_names, data, "Single")
#combined_r2 = model.get_R2(col_names, data, "Multi")
#bivar_r2 = model.get_R2(col_names, data, "BiVar")

#print(bivar_r2)

def get_R2(col_names, data_training, data_testing, num_vars):

    total_cols = len(col_names)
    y_testing = data_testing[:, (total_cols - 1)]
    y_training = data_training[:, (total_cols - 1)]
    all_training = data_training[: , 0:total_cols - 1]
    all_testing = data_testing[: , 0:total_cols - 1]

    y_mean = (y_testing.sum()/len(y_testing))

    num_categories = total_cols - 1

    r2_values = []

    if num_vars == "Single":
        for i in range(num_categories):
            curr_tr_category = all_training[:,[i]] 
            curr_test_category = all_testing[:, [i]]
            r2 = find_R2(curr_tr_category, curr_test_category, y_training, 
                y_testing, y_mean)
            r2_values.append(r2)
        return r2_values

def calculate_R2(curr_yhats, y_test, y_mean):

    numerator = []
    denominator = []

    for i, yn in enumerate(y_test):
        yhat = curr_yhats[i]
        top = (yn - yhat)**2
        bottom = (yn - y_mean)**2
        numerator.append(top)
        denominator.append(bottom)

    sum_numerator = sum(numerator)
    sum_denominator = sum(denominator)
    r2 = 1 - (sum_numerator/sum_denominator)

    return r2

def find_R2(x_tr, x_test, y_tr, y_test, y_mean):

    beta = model.linear_regression(x_tr, y_tr)
    yhats = model.apply_beta(beta, x_test)
    r2 = calculate_R2(yhats, y_test, y_mean)
    return r2


tests = get_R2(col_names, data_training, data_testing, "Single")
print(tests)

def double(g_dex, a_dex):

    total_cols = len(col_names)
    y_testing = data_testing[:, (total_cols - 1)]
    y_training = data_training[:, (total_cols - 1)]
    all_training = data_training[: , 0:total_cols - 1]
    all_testing = data_testing[: , 0:total_cols - 1]

    y_mean = (y_testing.sum()/len(y_testing))

    num_categories = total_cols - 1

    r2_values = []
    
    base_tr_category = all_training[:,[g_dex]]
    paired_tr_category = all_training[:,[a_dex]]

    base_test_category = all_testing[:,[g_dex]]
    paired_test_category = all_testing[:,[a_dex]]

    bivar_tr_data = np.concatenate((base_tr_category, 
                paired_tr_category), axis = 1)

    bivar_test_data = np.concatenate((base_test_category, 
                paired_test_category), axis = 1)

    r2 = find_R2(bivar_tr_data, bivar_test_data, y_training, y_testing, y_mean)

    return r2


doubles = double(3, 6)
print(doubles) 



def build_K_arrays(dex, cat, temp_arrays, r2s, base_category, remaining,
    base_num_rows, y_train, y_mean, temp_train_data = None, y_test = None):

    temp_data = np.empty([base_num_rows, 0])

    temp_data = np.append(temp_data, 
        base_category, axis = 1)
    
    additional_category = remaining[:,[dex]]

    temp_data = np.append(temp_data, 
        additional_category, axis = 1)

    temp_arrays[cat] = temp_data

    if y_test is None:
        r2 = find_R2(temp_data, y_train, y_mean)
    else:
        r2 = find_R2(temp_train_data, y_train, y_mean, temp_data, y_test)

    r2s[cat] = r2

    if y_test is None:
        return r2s, temp_arrays, temp_data
    else:
        return r2s, temp_arrays