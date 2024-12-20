# Setup and Prerequisites
## Conda
Conda will need to be installed, then create the virtual environment with the provided manifest:

```
conda env create -f environment.yml
```

After your environment is created, activate it with:

```
conda activate cm4ai-quantum
```

Install required packages

```
pip install -r requirements.txt --upgrade
```


## Kaggle Login and Notebook Auth
Create an account with [Kaggle](https://www.kaggle.com/) if you do not already have one. 

**Get Your API Credentials:** Login and go to Profile Picture -> Settings -> Account. Scroll down to the **API section** and click on **Create New API Token**. This will download a file called `kaggle.json`. 

**Place the Credentials in a Secure Location:** By default, the Kaggle API client expects to find the kaggle.json file in `~/.kaggle/` on Unix-based systems (including macOS and Linux) and `%HOMEPATH%\.kaggle\` on Windows. Create the `.kaggle` directory if it doesn't exist and place your `kaggle.json` file inside it.


## D-Wave
Register for an account with [D-Wave](https://cloud.dwavesys.com/leap/) (free trial). After you have an account, obtain your Solver API Token from the menu. Then run:

```
dwave config create
```

# Running the Benchmark Dataset
After running the above setup and configuration steps, you can run a predefined set of parameters against a synthetic, benchmark graph from the root of this project within the Python Notebook: 

```
EXAMPLE-dwave-community-detection.ipynb
```


# References
* https://aws.amazon.com/blogs/quantum-computing/community-detection-using-hybrid-quantum-annealing-on-amazon-braket-part-2/
* https://github.com/aws-samples/amazon-braket-community-detection/blob/main/Hybrid_jobs_for_community_detection.ipynb
* https://github.com/rkdarst/dynbench?tab=readme-ov-file
* https://arxiv.org/pdf/1901.09756.pdf
* https://www.dwavesys.com/media/wafcrbie/18_wed_am_graph_lanl.pdf
* https://github.com/lanl/Quantum_Graph_Algorithms
