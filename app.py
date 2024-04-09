from flask import Flask,render_template, jsonify, request
import pickle
from sklearn.preprocessing import StandardScaler

app=Flask(__name__)

load_model=pickle.load(open('Admission_lr_model.sav','rb'))
load_stdsclar=pickle.load(open('std_scalar.sav','rb'))

stdscalr=StandardScaler()

@app.route('/xxx',methods=['GET',"POST"])
def test():
    if request.method=="POST":
        GRE_Score=request.json['GRE_Score']
        TOEFL_Score=request.json['TOEFL_Score']
        University_Rating=request.json['University_Rating']
        SOP=request.json['SOP']
        LOR=request.json['LOR']
        CGPA=request.json['CGPA']
        Research=request.json['Research']
        print([GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA,Research])

        test1=load_stdsclar.transform([[GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA,Research]])
        # print(test1)
        result=load_model.predict(test1)

        return jsonify(str(result))

if __name__=="__main__":
    app.run()