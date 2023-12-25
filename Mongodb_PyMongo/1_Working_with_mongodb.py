import pymongo
client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb=client['Employee']
# print(mydb)

information =mydb.employeeinformation

record=[{
    'firstname':'Animesh',
    'lastname':'Kumar',
    'department':'Quant & Algo'
    },
    {
    'firstname':'Mohit',
    'lastname':'Verma',
    'department':'Quant'   
    },
    {
    'firstname':'MohitV',
    'lastname':'MVerma',
    'department':'Algo'     
    }]
information.insert_many(record)
# result =information.find_one({'firstname':'Animesh'})
# print(result)