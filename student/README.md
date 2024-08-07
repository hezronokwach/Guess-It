# Range Prediction
![image](https://inprogrammer.com/wp-content/uploads/2022/06/Image-for-introduction-to-python-9.jpg)

This Python script reads integer inputs, replaces outliers with the median of the non-outlier values, and predicts the range for subsequent inputs based on the standard deviation of the adjusted values.
## Features

Outlier Replacement: Automatically replaces outliers in the input values with the median of non-outlier values.
Range Prediction: Predicts the range for the next input using the mean and standard deviation of the adjusted values.
Interactive Input: Reads input values from standard input.

## Usage
Running the Script

To run the script, execute the following command:
```bash
python3 script_name.py
```
## Input Format

Enter integer values one per line.

## Sample Output

For each input value (from the second input onward), the script calculates and prints the predicted range for the next input.
```bash
$ python3 script_name.py
100
123
63 160
145
55 190
156
57 205
200
32 258

```
## Error Handling

Invalid Input: If the input is not a valid integer, an error message is printed and the input is ignored.

Insufficient Data: If there are not enough data points to calculate the range after filtering outliers, a message is printed.

## License

This project is licensed under the MIT License.

## Contributions

Contributions are welcome! Please fork this repository and submit pull requests.