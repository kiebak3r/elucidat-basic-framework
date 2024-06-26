# Installation
1. pip install -r requirements.txt
2. playwright install
3. run tests using: "pytest" from the IDE console (cli flags are stored in pytest.ini)

# Checking Results
1. pytest will print results table (including print statements) to the console
2. I have included CLI flags to work in a CI/CD pipeline (azure devops)
3. CLI arguments for playwright which provide a failure video and a trace report for debugging.
