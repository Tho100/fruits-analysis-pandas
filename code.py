import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

data = pd.DataFrame({
    'farm': [f'FM {i}' for i in np.random.randint(0, 4, 20)],
    'fruit': [f'FR {i}' for i in np.random.randint(0, 12, 20)],
    'calories': np.random.randint(10, 90, 20),
    'sugar': np.random.randint(1, 25, 20)
})

fruits_calories = data.groupby('fruit')['calories'].sum().reset_index().sort_values(
    by='calories', ascending=False
)

fruits_sugars = data.groupby('fruit')['sugar'].sum().reset_index().sort_values(
    by='sugar', ascending=False
)

number_of_fruits_from_each_farms = data.groupby('farm')['fruit'].count().reset_index().sort_values(
    by='fruit', ascending=False
)

def createFruitFactsChart(title: str, xLabel: str, xValues, yValues, row):

    plt.style.use('ggplot')

    plt.subplot(1, 3, row)

    bars = plt.bar(xValues, yValues, color='purple', alpha=.5)
    plt.plot(xValues, yValues, color='pink')
    plt.scatter(xValues, yValues, color='pink')
    plt.xlabel(xLabel)
    plt.title(title, fontsize=13)

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height}', ha='center', va='bottom', color='purple', alpha=.8)

plt.figure(figsize=(20, 6))

createChart('Fruit Calories', 'Fruit', fruits_calories['fruit'], fruits_calories['calories'], 1)
createChart('Fruit Sugars', 'Fruit', fruits_sugars['fruit'], fruits_sugars['sugar'], 2)

sales_data = pd.DataFrame({
    'farm': [f'FM {i}' for i in np.random.randint(0, 4, 20)],
    'quantity_sold': np.random.randint(50, 200, 20),
    'revenue': np.random.randint(100, 5000, 20)
})

merged_sales_data = sales_data.merge(data[['farm', 'fruit']], on='farm', how='left')

farms_revenue = merged_sales_data.groupby('farm')['revenue'].sum().reset_index()
fruits_sales = merged_sales_data.groupby('fruit')['quantity_sold'].count().reset_index()

def createSalesChart(title: str, xLabel: str, xValues, yValues, row):

    plt.style.use('ggplot')

    plt.subplot(1, 2, row)

    bars = plt.bar(xValues, yValues, color='purple', alpha=.5)
    plt.plot(xValues, yValues, color='pink')
    plt.scatter(xValues, yValues, color='pink')
    plt.xlabel(xLabel)
    plt.title(title, fontsize=13)

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height}', ha='center', va='bottom', color='purple', alpha=.8)

plt.figure(figsize=(20, 6))

createSalesChart('Farms Revenue', 'Farm', farms_revenue['farm'], farms_revenue['revenue'], 1)
createSalesChart('Fruits Sold', 'Fruit', fruits_sales['fruit'], fruits_sales['quantity_sold'], 2)
