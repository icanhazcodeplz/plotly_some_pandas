# Plotly Some Pandas
Learn the basics of pandas and plotly using PyCharm Community Edition.

Why these particual tools? [Pandas](https://github.com/pandas-dev/pandas) for data analysis because it has quickly become the most-used data science tool in industry for a reason: it's amazing! [Plotly](https://github.com/plotly/plotly.py) because it provides much more functionality out of the box than standard visualization packages like matplotlib and seaborn. PyCharm because it is an incredibly feature rich IDE that has an excellent debugging interface. [Jupyter Notebooks](https://jupyter.org/) are also excellent for doing data science work, especially when you want to publish some kind of report in PDF. That said, the developer tools in Jupyter are somewhat minimal. I recommend learning both to see which one you like more! Fwiw, the paid version of PyCharm supports notebooks directly in the IDE. Aka, best of both worlds :). 


# Setup
I assume the user is on Windows. Install the following:
* [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows): Get the "Community" edition, which is free.
* [Anaconda](https://www.anaconda.com/products/individual): Includes a bunch of stuff. We'll just use it for easily creating virtual python environments with specific packages.
* [GitForWindows](https://gitforwindows.org/): Just needed to clone this repo 

### Clone this repo and open in PyCharm CE
1. From some shell (I usually use GitBash), navigate to the folder that you want to clone this repo in, for me that looks like 
`cd /c/Users/bkm22/code` in GitBash or
`cd C:\Users\bkm22\code\` in Powershell
2. Run the command `git clone https://github.com/icanhazcodeplz/plotly_some_pandas.git`
3. Launch PyCharm Community Edition and open this new folder `plotly_some_pandas` that should now be on your local machine. 

### Create a new conda environment
Launch **Anaconda Powershell Prompt** and run the following ***one at a time***
```bash
cd <path_to_this_repo_on_your_local>
conda create --name py310 python=3.10
conda activate py310
pip install -r requirements.txt
```

Now, in PyCharm settings, set the **Project Interpreter** to this new conda environment, "py310".

## Running lesson 1
In PyCharm, open the python script "**01_getting_started.py**". Right-click anywhere in the editor and select "Run". This runs the script and creates a default run-configuration that you can access by navigating to **Run->Edit Configurations** from the top menu.

TODO: More instructions on how to debug

# Next steps
Pandas has a good tutorial that they created themselves: [Getting Started Tutorials](https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/index.html)

### Other resources:
1. [learndatasci](https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/)
