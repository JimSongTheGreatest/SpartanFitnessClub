from myapp import application,db
db.create_all()
application.run(debug= True)
