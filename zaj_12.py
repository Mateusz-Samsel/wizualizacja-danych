import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

x = np.linspace(-4, 4, 100)
y = np.sin(2 * x)
y1 = 2*np.sin(x)
y2 = np.sin(x)
plt.plot(x, y2, 'blue', linestyle="solid", label="sinx")
plt.plot(x, y1, 'red', linestyle="dotted", label="2sin(x)")
plt.plot(x, y, 'green', linestyle="dashed", label="sin(2x)")
plt.legend(title='Wykres')
plt.show()

# ZAD 2
x = np.linspace(-10, 10)
y = np.divide(1, 1+x**2)
plt.plot(x, y, 'green', linestyle="-", label="sin(2x)")
plt.legend(title='1/(1+x**2)')
plt.show()

x1 = np.linspace(0, 3)
y1 = x1**2
y2 = math.e**x1
y3 = x1**x1
plt.plot(x1, y1, 'green', linestyle="-", label="pov(x^2)")
plt.plot(x1, y2, 'blue', linestyle=":", label="pov(e^2)")
plt.plot(x1, y3, 'red', linestyle="--", label="pov(x^x)")
plt.legend(title='1/(1+x**2)')
plt.show()

x2 = np.linspace(0, 3)
plt.plot(x2, y1, 'green', linestyle="-", label="pov(x^2)")
plt.plot(x2, y2, 'blue', linestyle=":", label="pov(e^2)")
plt.plot(x2, y3, 'red', linestyle="--", label="pov(x^x)")
plt.legend(title='1/(1+x**2)')
plt.show()


plt.subplot(3, 1, 1)
plt.plot(x2, y1, linestyle='--', color='green', label='x^2')
plt.subplot(3, 1, 2)
plt.plot(x2, y2, linestyle=':', color='red', label='e^x')
plt.subplot(3, 1, 3)
plt.plot(x2, y3, 'blue', linestyle='-', label='x^x')
plt.show()


# ZAD 3
def sinplot(flip=1):
    x0 = np.linspace(0, 2, 100)
    x01 = np.linspace(-2, 2, 100)
    for i in range(-8, 8):
        plt.plot(x01, x01*flip)
        plt.plot(x01, x01**2)
        plt.plot(x01, x01**3)
        plt.plot(x0, x0**(1/2))
        plt.plot(x0, x0**(1/3))


sns.set_style("darkgrid")
sns.set_palette("dark")
sinplot()
print(sns.axes_style())
plt.show()


glue = sns.load_dataset('glue')
data = glue['Score'][glue['Model'] == 'ERNIE']
year = [2017, 2018, 2019]

glue_df = sns.catplot(
    data=glue,
    kind='violin',
    x='Year',
    y='Score',
    hue='Encoder',
    col='Model',
    palette='Set2'
)

glue_df.set_axis_labels('Tasks', 'Scores')
plt.show()
