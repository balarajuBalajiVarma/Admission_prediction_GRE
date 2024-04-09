### Steps to create the git reposotory 
1. open git hub
2. Create new repository
3. provide repository name
4. Add description, enable public, Check in Add a README file
5. Crate repository

### Steps to clone the repository to local machine to make the changes in local push to git again
1. Copy the git url file path
2. Create an empty folder path and open the gitbash here
3. Give command "git clone '[Paste repository name here](https://github.com/balarajuBalajiVarma/Admission_prediction_GRE.git)' "
4. Then type cd "Admission_prediction_GRE"
5. Give command "code ."  --- it open vscode and do make changes , commit, push.

### Create the requirements.txt
### Create the template which contains (Src/code, templates, env, app.py etc)

### Why setup.py is needed
1. Usally we install libraries . So by default all the packages can be installed
2. We create our packages in local for calling the function it should reflect in other sytem also. for that we take care in setup.py . while running requirements.txt this local function like src folder can also installed there.
3. to install set.py (add -e . in requirements.txt)