import pandas as pd
from main import transform

def test_transform():
    # Create a sample dataframe
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
    # Expected result after transformation
    expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [5, 7, 9]})
    
    # Apply the transform function
    result_df = transform(df)
    
    # Assert that the result matches the expected dataframe
    pd.testing.assert_frame_equal(result_df, expected_df)

    assert False