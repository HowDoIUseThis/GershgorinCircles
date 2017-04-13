# Gershgorin Circles
### Basic Info
This is a simple program to help me visualize Gershgorin circles. As of now it simple uses a hard coded matrix and does nothing to stop you from breaking it.


### The Math
**The Gershgorin circle theorem:** 

![alt tag](https://latex.codecogs.com/gif.latex?%5Ctext%7BLet%20%7D%20%5Cmathbf%7BA%7D%20%5Ctext%7B%20be%20a%20complex%20%7D%20n%5Ctimes%20n%20%5Ctext%7B%20matrix%2C%20with%20entries%20%7D%20%5Cmathbf%7Ba_%7Bij%7D%7D%20%5Ctext%7B.%20For%20%7D%20%5Cmathbf%7Bi%7D%20%5Cin%20%5Cbegin%7BBmatrix%7D%201%2C%20.%20.%20.%20.%20%2C%20n%20%5Cend%7BBmatrix%7D%20%5Ctext%7Blet%20%7D%20%5C%5C%20%5Cmathit%7BR_%7B%5Cmathbf%7Bi%7D%7D%7D%20%3D%20%5Csum_%7B%5Cmathbf%7Bj%5Cneq%20i%7D%7D%5E%7B%20%7D%20%5Cleft%7C%20%5Cmathbf%7Ba_%7Bij%7D%7D%20%5Cright%7C%20%5Ctext%7Bbe%20the%20sum%20of%20absolute%20values%20of%20the%20non-diagonal%20entries%20in%20the%20%5Ctextit%7Bi%7D-th%20row.%7D%20%5C%5C%20%5C%5C%20%5Ctext%7B%20Let%20%7D%20%5Cmathit%7B%5Cmathbf%7BD%28a_%7Bij%7D%2CR_%7Bi%7D%7D%20%29%7D%20%5Ctext%7Bbe%20the%20closed%20disc%20centered%20at%20%7D%20%5Cmathbf%7Ba_%7Bii%7D%7D%20%5Ctext%7B%20with%20radius%20%7D%20%5Cmathbf%7BR_i%7D%20%5Ctext%7B.%20Such%20a%20disk%20is%20called%20a%20%5Ctextbf%7BGershgorin%20disc%7D.%7D)

### Uses
This theorem is very helpful as it allows for the easy approximation of the eigenvalues ( or spectrum ) of a square matrix with little computation.
Each circle represents a domian that an eigenvalues can be found in. If two circles overlap it does not mean that there is one eigenvalues in each, rather that there is simply two eigenvalues found in the union of the two domains. 

### Test case
The hard coded test case for this program is the matrix, 


![alt tag](https://latex.codecogs.com/gif.latex?A%3D%20%5Cbegin%7Bbmatrix%7D%2010%20%26%20-1%20%26%200%20%26%201%20%5C%5C%200.2%26%208%20%260.2%20%260.2%20%5C%5C%201%26%201%20%262%20%261%20%5C%5C%20-1%26-1%20%26-1%20%26-11%20%5Cend%7Bbmatrix%7D)

The result of the program produces,

![alt tag](https://github.com/HowDoIUseThis/GershgorinCircles/blob/master/plotcircles.png)

where the eigenvalues of the matrix in diagonal form are, 


![alt tag](https://latex.codecogs.com/gif.latex?D%3D%20%5Cbegin%7Bbmatrix%7D%209.8218%260%20%260%20%260%20%5C%5C%200%26%208.1478%20%260%20%260%20%5C%5C%200%26%200%20%26%201.8995%20%26%200%5C%5C%200%26%200%20%26%200%26%20-10.86%20%5Cend%7Bbmatrix%7D)

If we were to plot the eigenvalues on our plot we would get,



## Authors

* **Christopher Stewart** 


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
