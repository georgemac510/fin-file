<h1>Financial Data Retrieval App</h1>

<h2>How to Download Code, Install Dependencies and Run App</h2>

<h3>Step 1: Clone repo and cd into app directory</h3>

        git clone https://github.com/georgemac510/filecoinpython.git
        cd hackfs_filecoin_finapp/

<h3>Step 2: Create virtual environment</h3>

        virtualenv -p python3 venv
        source venv/bin/activate

<h3>Step 3: Install Flask using pip</h3>

        pip install flask

<h3>Step 4: Install Yahoo Finance module and other dependencies</h3>

        pip install yfinance lxml html5lib

<h3>Step 5: Run App</h3>

        python app.py
