from flask import Flask,render_template
import boto3 

app=Flask(__name__)
@app.route("/")
def jagan():

    tag=boto3.resource('ec2')
    tag1=tag.instances.all()
    
    
    return render_template("cost.html",data=tag1)