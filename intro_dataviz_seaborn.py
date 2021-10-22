# Statistical ploting using Seaborn
#

# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

# Plot a linear regression between 'weight' and 'hp' from dataframe 'auto'
sns.lmplot(x='weight', y='hp', data=auto)

# Display the plot
plt.show()


# Generate a green residual plot of the regression between 'hp' and 'mpg'
sns.residplot(x='hp', y='mpg', data=auto, color='green')

# Display the plot
plt.show()


# regplot
# A principal difference between sns.lmplot() and sns.regplot() is the way in
# which matplotlib options are passed (sns.regplot() is more permissive).
#
# Generate a scatter plot of 'weight' and 'mpg' using red circles
plt.scatter(auto['weight'], auto['mpg'], label='data', color='red', marker='o')

# Plot in blue a linear regression of order 1 between 'weight' and 'mpg'
sns.regplot(x='weight', y='mpg', data=auto, scatter=None, color='blue', label='order 1')

# Plot in green a linear regression of order 2 between 'weight' and 'mpg'
sns.regplot(x='weight', y='mpg', data=auto, scatter=None, order=2, color='green', label='order 2')

# Add a legend and display the plot
plt.legend(loc='upper right')
plt.show()


# Grouping
#
# Using the hue argument, you can specify a categorical variable by which to group data observations.
# The distinct groups of points are used to produce distinct regressions with different hues in the plot.
#
# Plot a linear regression between 'weight' and 'hp', with a hue of 'origin' and palette of 'Set1'
sns.lmplot(x='weight',y='hp',data=auto, hue='origin',palette='Set1')
plt.show()

# You'll use the automobile dataset again and, this time, you'll use the keyword argument row to display
# the subplots organized in rows.
#
## Plot linear regressions between 'weight' and 'hp' grouped row-wise by 'origin'
sns.lmplot(x='weight',y='hp',data=auto,hue='origin',row='origin')
plt.show()


# Strip plot - showing distribution of certain group
#
# Make a strip plot of 'hp' grouped by 'cyl'
plt.subplot(2,1,1)
sns.stripplot(x='cyl', y='hp', data=auto)

# Make the strip plot again using jitter and a smaller point size
plt.subplot(2,1,2)
sns.stripplot(x='cyl', y='hp', data=auto, jitter=True, size=3)

plt.show()


# Swarm plot - similar to strip, but spreads the same points to see the distribution
#
# Generate a swarm plot of 'hp' grouped horizontally by 'cyl'
plt.subplot(2,1,1)
sns.swarmplot(x='cyl',y='hp',data=auto)

# Generate a swarm plot of 'hp' grouped vertically by 'cyl' with a hue of 'origin'
plt.subplot(2,1,2)
sns.swarmplot(x='hp',y='cyl',data=auto,hue='origin',orient='h')

plt.show()


# Violin plot - similar to box plot, with std, avg, outliers and distribution
#
# Generate a violin plot of 'hp' grouped horizontally by 'cyl'
plt.subplot(2,1,1)
sns.violinplot(x='cyl', y='hp', data=auto)

# Generate the same violin plot again with a color of 'lightgray' and without inner annotations
plt.subplot(2,1,2)
sns.violinplot(x='cyl',y='hp',data=auto,inner=None,color='lightgray')

# Overlay a strip plot on the violin plot
plt.subplot(2,1,2)
sns.stripplot(x='cyl',y='hp',data=auto,size=1.5, jitter=True)

plt.show()


# Joint plot - scatter plot with hist distributions of x and y with corrcoef and p-value
# kde=True smooths the distributions and shows the area of scatter
# kind='scatter' uses a scatter plot of the data points
# kind='reg' uses a regression plot (default order 1)
# kind='resid' uses a residual plot
# kind='kde' uses a kernel density estimate of the joint distribution
# kind='hex' uses a hexbin plot of the joint distribution
#
# Generate a joint plot of 'hp' and 'mpg' using a hexbin plot
sns.jointplot(x='hp',y='mpg',data=auto,kind='hex')

plt.show()


# Pair plot - makes matrix of plots with distribution on the diagonal and scattering of other correlations
# you can group points by a columns using key hue=
# You will display regressions as well as scatter plots in the off-diagonal subplots.
# You will do this with the argument kind='reg' (where 'reg' means 'regression').
# Another option for kind is 'scatter' (the default) that plots scatter plots in the off-diagonal subplots.
# You will also visualize the joint distributions separated by continent of origin.
# You will do this with the keyword argument hue specifying the 'origin'
#
# Plot the pairwise joint distributions grouped by 'origin' along with regression lines
sns.pairplot(auto,kind='reg',hue='origin')

plt.show()

# Heatmap - shows heatmap of the covariance per columns
# needs covariance matrix as the input
#
# Visualize the covariance matrix using a heatmap
sns.heatmap(cov_matrix)

plt.show()
