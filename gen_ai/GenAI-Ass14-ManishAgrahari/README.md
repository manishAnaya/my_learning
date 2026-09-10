# ML Feature Engineering & Preprocessing

This project contains a Jupyter Notebook `task.ipynb` that covers feature engineering, preprocessing, scaling, and machine learning pipeline using `final_data.csv`.

## Tasks Covered

1. **Creating New Features**
   - Created AgeGroup and GrossAmount.

2. **Date & Text Features**
   - Extracted date features.
   - Created customer tenure and product text features.

3. **One-Hot Encoding**
   - Converted categorical data into numerical 0/1 values.

4. **ColumnTransformer**
   - Applied One-Hot Encoding to categorical features.
   - Kept numerical features unchanged.

5. **StandardScaler**
   - Standardized numerical features.

6. **MinMaxScaler**
   - Scaled numerical features between 0 and 1.

7. **Preprocessing Pipeline**
   - Handled missing values, scaling, and encoding.

8. **Full Scikit-learn Pipeline**
   - Combined preprocessing with RandomForestRegressor.
   - Predicted Sales and evaluated the model.

9. **Pipeline Benefits**
   - Covered benefits, limitations, and differences of using a pipeline.

## Target

**Target Column:** `Sales`

This is a **Regression Problem** because Sales is a numerical value.

## Libraries Used

- Pandas
- NumPy
- Scikit-learn

## Files

```text
project/
├── task.ipynb
├── final_data.csv
└── README.md