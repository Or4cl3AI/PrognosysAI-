```python
import pandas as pd
from schema import Schema, And

# Define the data schema
DataSchema = Schema({
    'column1': And(str, len),
    'column2': And(int, lambda n: 0 <= n <= 100),
    'column3': And(float, lambda n: 0 <= n <= 100),
    # Add more columns as per the data
})

def processData(data_input):
    """
    Function to process the input data.
    """
    # Load the data
    data = pd.read_csv(data_input)

    # Validate the data
    if not DataSchema.is_valid(data.to_dict()):
        raise ValueError("Invalid data")

    # Perform data processing tasks here
    # ...

    # Return the processed data
    processed_data = data
    return processed_data
```