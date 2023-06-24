
1. Command to generate missing feature file steps
pyetst-bdd generate path to feature file > path to step file
pytest-bdd generate src/tests/features/login.feature > src/tests/steps/test_login.py

2. list all pip modules use command as
pip list

3. use python -m pytest --html=reports.html to generate pytest-html reports.

4. issue with urllib3 library
pip uninstall urllib3
pip install 'urllib3<2.0'

5. to generate sample .gitignore file
https://www.toptal.com/developers/gitignore

6.