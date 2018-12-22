# A Basic Classification NN
A Neural Network to perform 0/1 (True or False) classification on a data-set like the [Pima Indians data-set](https://www.kaggle.com/kumargh/pimaindiansdiabetescsv) for diabetes.

# Setting up:

- Start by Cloning the repo.

- If you have anaconda installed :

  - Make sure that everything is up-to-date and numpy is installed
  
    ```python
    conda update --all
    conda install numpy
    ```
  
  - Then install tensorflow via
  
    ```python
    conda install tensorflow
    ```
- If you have vanilla python instaled then install tensorflow and numpy via pip:

  - Make sure pip is up-to-date

     ```python
      pip install --upgrade pip
     ```
   
   - Then install numpy and tensorflow

     ```python
     pip install numpy
     pip install tensorflow
     ```
  If you're going to do any serious machine learning I really recommend installing anaconda and using that method.
 
 - Place your dataset in form of a .csv and rename it to "data.csv" (without the quotes)
 
 - Run the script via
    
    ```python
    python classification-network.py
    ```
    Enter the dimension of the data when prompted.
