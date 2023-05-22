# Homework Week 2
### Question 1

``` mlflow, version 2.3.2 ```

### Question 2
``` bash
(exp-tracking-env) dan@mlops-server:~/mlops-zoomcamp/02-experiment-tracking/homework$ ls -l output
total 7104
-rw-rw-r-- 1 dan dan  153660 May 22 11:41 dv.pkl
-rw-rw-r-- 1 dan dan 2632817 May 22 11:41 test.pkl
-rw-rw-r-- 1 dan dan 2146163 May 22 11:41 train.pkl
-rw-rw-r-- 1 dan dan 2336393 May 22 11:41 val.pkl
```

First line: 154 kb

### Question 3

max_depth was 10

### Question 4. 

``` bash
(exp-tracking-env) dan@mlops-server:~/mlops-zoomcamp/02-experiment-tracking/homework$ python hpo.py
[I 2023-05-22 14:16:49,624] A new study created in memory with name: no-name-6f8b4171-6090-45eb-af5c-cf7282b665db
[I 2023-05-22 14:16:52,560] Trial 0 finished with value: 2.451379690825458 and parameters: {'n_estimators': 25, 'max_depth': 20, 'min_samples_split': 8, 'min_samples_leaf': 3}. Best is trial 0 with value: 2.451379690825458.
[I 2023-05-22 14:16:52,878] Trial 1 finished with value: 2.4667366020368333 and parameters: {'n_estimators': 16, 'max_depth': 4, 'min_samples_split': 2, 'min_samples_leaf': 4}. Best is trial 0 with value: 2.451379690825458.
[I 2023-05-22 14:16:55,604] Trial 2 finished with value: 2.449827329704216 and parameters: {'n_estimators': 34, 'max_depth': 15, 'min_samples_split': 2, 'min_samples_leaf': 4}. Best is trial 2 with value: 2.449827329704216.
[I 2023-05-22 14:16:56,471] Trial 3 finished with value: 2.460983516558473 and parameters: {'n_estimators': 44, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 1}. Best is trial 2 with value: 2.449827329704216.
[I 2023-05-22 14:16:57,634] Trial 4 finished with value: 2.453877262701052 and parameters: {'n_estimators': 22, 'max_depth': 11, 'min_samples_split': 5, 'min_samples_leaf': 2}. Best is trial 2 with value: 2.449827329704216.
[I 2023-05-22 14:16:58,142] Trial 5 finished with value: 2.4720122094960733 and parameters: {'n_estimators': 35, 'max_depth': 3, 'min_samples_split': 4, 'min_samples_leaf': 2}. Best is trial 2 with value: 2.449827329704216.
[I 2023-05-22 14:17:00,699] Trial 6 finished with value: 2.4516421799356767 and parameters: {'n_estimators': 28, 'max_depth': 16, 'min_samples_split': 3, 'min_samples_leaf': 3}. Best is trial 2 with value: 2.449827329704216.
[I 2023-05-22 14:17:00,952] Trial 7 finished with value: 2.5374040268274087 and parameters: {'n_estimators': 34, 'max_depth': 1, 'min_samples_split': 7, 'min_samples_leaf': 1}. Best is trial 2 with value: 2.449827329704216.
[I 2023-05-22 14:17:02,369] Trial 8 finished with value: 2.455971238567075 and parameters: {'n_estimators': 12, 'max_depth': 19, 'min_samples_split': 10, 'min_samples_leaf': 4}. Best is trial 2 with value: 2.449827329704216.
[I 2023-05-22 14:17:02,612] Trial 9 finished with value: 2.486106021576535 and parameters: {'n_estimators': 22, 'max_depth': 2, 'min_samples_split': 8, 'min_samples_leaf': 2}. Best is trial 2 with value: 2.449827329704216.
```

### Question 5
My top output had a test rmse of 2.285