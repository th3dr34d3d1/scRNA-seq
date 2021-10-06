import matplotlib.pyplot as plt
from matplotlib import pyplot as pllt


#x-axis title representing data obtained at 30 minute elapsed time intervals after hyphae-inducing conditions, in minutes, for 4 hours
xaxislabel = ['60', '90', '120', '150', '180', '210', '240']


#% cells ≤30microns in Spider or FBS @37deg C
less30spider = [1, .375, 0, 0, .82021, 0, 0]
less30fbs = [0, .475, .04054, .22144, .170535, 0, 0]


#width of bars
width = 0.35

fig, ax = plt.subplots()

ax.bar(xaxislabel, less30spider, width, label='Spider')
ax.bar(xaxislabel, less30fbs, width, bottom=less30spider, label='FBS')

#x-axis labels and title
ax.set_ylabel('%cells ≤30microns')
ax.set_xlabel('elapsed time (minutes)')
ax.set_title('Hyphal Length at 30 minute elapsed times from induction conditions in Spider or FBS @37deg C')
ax.legend()
plt.show()
