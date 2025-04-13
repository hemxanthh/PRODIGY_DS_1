import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create a synthetic dataset with an 'age' variable
np.random.seed(42)
ages = np.random.normal(loc=35, scale=10, size=200)  # 200 ages, normally distributed around 35

# Create a histogram for the 'age' variable
plt.figure(figsize=(10, 6))
sns.histplot(ages, bins=15, kde=True, color='mediumseagreen')
plt.title('Distribution of Age in Population')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()
