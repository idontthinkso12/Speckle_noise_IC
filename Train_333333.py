import MODULE_Train_the_model as tr

datadir = './Training_data_mix/333333'
modelname1 = 'vgg_333333'
networkname1 = 'vgg16'
tr.Train_model(datadir,modelname1, networkname1)

modelname2 = 'res_333333'
networkname2 = 'resnet18'
tr.Train_model(datadir,modelname2, networkname2)

